"""Compile SQL-history computation interfaces into staged relational programs.

The planner cannot submit replacement SQL. It instantiates immutable historical
programs, binds explicit predicate parameters, and composes their named outputs.
Grouping and joins inside each source scope survive composition. Dependency
fingerprints make cached plans invalid when a source is corrected or withdrawn.
"""
from __future__ import annotations
from hashlib import sha256
import json
import re
from typing import Any
import sqlglot
from sqlglot import exp


class PlanError(ValueError):
    pass


def parse_query(sql, dialect):
    trees=sqlglot.parse(sql,read=dialect.lower())
    if len(trees)!=1 or not isinstance(trees[0],exp.Query):raise PlanError('one read-only query required')
    if any(isinstance(n,(exp.DDL,exp.DML,exp.Into)) for n in trees[0].walk()):raise PlanError('write operator forbidden')
    return trees[0]


def parameters(tree):
    """Only predicate literals/placeholders are externally bindable parameters."""
    comparisons=(exp.EQ,exp.NEQ,exp.GT,exp.GTE,exp.LT,exp.LTE,exp.Like,exp.In,exp.Between,exp.Is)
    return [n for n in tree.walk() if isinstance(n,(exp.Literal,exp.Placeholder))
            and isinstance(n.parent,comparisons) and n.find_ancestor(exp.Where,exp.Having) is not None]


def interface(source_id,sql,*,dialect='SQLite',aliases=(),evidence=()):
    tree=parse_query(sql,dialect)
    projections=tree.selects
    if not projections or any(isinstance(p,exp.Star) or isinstance(p,exp.Column) and p.is_star for p in projections):
        raise PlanError('source requires explicit output columns')
    output=[]
    for i,p in enumerate(projections):
        expression=p.this if isinstance(p,exp.Alias) else p
        output.append({'column':f'c{i}','meaning':p.alias_or_name,'expression':expression.sql(dialect=dialect.lower())})
    unique=[]
    if isinstance(tree,exp.Select):
        group=tree.args.get('group')
        if group and not any(v for k,v in group.args.items() if k!='expressions'):
            grain=[]
            for g in group.expressions:
                match=[o['column'] for o,p in zip(output,projections)
                       if g==(p.this if isinstance(p,exp.Alias) else p)
                       or isinstance(g,exp.Column) and not g.table and g.name==p.alias
                       or isinstance(g,exp.Literal) and g.is_int and int(g.this)==output.index(o)+1]
                if len(match)!=1:break
                grain.append(match[0])
            else:unique.append(grain)
        if tree.args.get('distinct'):unique.append([o['column'] for o in output])
        if not group and any(a.find_ancestor(exp.Window) is None for p in projections for a in p.find_all(exp.AggFunc)):
            unique.append([])
    params=[]
    for i,n in enumerate(parameters(tree)):
        params.append({'index':i,'predicate':n.parent.sql(dialect=dialect.lower()),
                       'required':isinstance(n,exp.Placeholder),'original_sql':n.sql(dialect=dialect.lower())})
    payload={'source_id':source_id,'scope_sql':sql,'aliases':list(aliases),'outputs':output,
             'parameters':params,'unique_keys':unique,'source_evidence_ids':list(evidence)}
    payload['fingerprint']=sha256(json.dumps(payload,sort_keys=True).encode()).hexdigest()
    return payload


def make_interfaces(library,prior_sql,dialect='SQLite'):
    output=[interface('$main',prior_sql,dialect=dialect)]
    for obj in library:
        c=obj.get('metric_contract') or obj.get('binding_contract') or {}
        sql=obj.get('sql_template') or c.get('scope_sql')
        if not sql:continue
        try:
            output.append(interface(obj['source_id'],sql,dialect=dialect,
                         aliases=obj.get('aliases',[]),evidence=obj.get('source_evidence_ids',[])))
        except (PlanError,sqlglot.errors.SqlglotError):continue
    return output


def dependencies_current(dependencies,interfaces):
    current={i['source_id']:i['fingerprint'] for i in interfaces}
    return all(current.get(k)==v for k,v in dependencies.items())


def compile_plan(plan,interfaces,*,dialect='SQLite'):
    sources={i['source_id']:i for i in interfaces}
    if plan.get('decision')=='retain':return sources['$main']['scope_sql'],{'decision':'retain','dependencies':{'$main':sources['$main']['fingerprint']}}
    if plan.get('decision')!='compose':raise PlanError('decision must be compose or retain')
    stages=plan.get('stages') or []
    if not 1<=len(stages)<=6:raise PlanError('one to six stages required')
    ctes=[];staged={};dependencies={};certificates=[]
    for stage in stages:
        name=stage.get('id','')
        if not re.fullmatch(r's[0-9]+',name) or name in staged:raise PlanError('unique stage id s0, s1, ... required')
        src=sources.get(stage.get('source_id'))
        if not src:raise PlanError('unknown or withdrawn computation source')
        if stage.get('fingerprint')!=src['fingerprint']:raise PlanError('stale computation binding')
        tree=parse_query(src['scope_sql'],dialect)
        slots=parameters(tree);bound=set()
        for binding in stage.get('parameters',[]):
            index=binding.get('index')
            if not isinstance(index,int) or isinstance(index,bool) or not 0<=index<len(slots) or index in bound:raise PlanError('invalid parameter index')
            value=binding['value']
            if not isinstance(value,(str,int,float,bool,type(None))):raise PlanError('parameter must be a scalar value')
            slots[index].replace(exp.convert(value));bound.add(index)
        if tree.find(exp.Placeholder):raise PlanError('unbound historical placeholder')
        alias=exp.TableAlias(this=exp.to_identifier(name),columns=[exp.to_identifier(o['column']) for o in src['outputs']])
        ctes.append(exp.CTE(this=tree,alias=alias));staged[name]=src;dependencies[src['source_id']]=src['fingerprint']

    def expression(obj):
        if not isinstance(obj,dict):raise PlanError('structured expression required')
        if 'stage' in obj:
            stage=staged.get(obj['stage']);column=obj.get('column')
            if stage is None or column not in {o['column'] for o in stage['outputs']}:raise PlanError('unknown output reference')
            return exp.column(column,table=obj['stage'],quoted=True)
        if 'literal' in obj:
            value=obj['literal']
            if not isinstance(value,(str,int,float,bool,type(None))):raise PlanError('literal must be scalar')
            return exp.convert(value)
        op=obj.get('op');args=[expression(x) for x in obj.get('args',[])]
        functions={'sum':exp.Sum,'avg':exp.Avg,'min':exp.Min,'max':exp.Max,'count':exp.Count}
        if op in functions and len(args)==1:
            if args[0].find(exp.AggFunc):raise PlanError('nested aggregation requires separate stages')
            return functions[op](this=args[0])
        if op=='count_distinct' and len(args)==1:return exp.Count(this=exp.Distinct(expressions=args))
        binary={'add':exp.Add,'subtract':exp.Sub,'multiply':exp.Mul,'divide':exp.Div}
        if op in binary and len(args)==2:
            if op=='divide':return exp.Div(this=exp.Mul(this=exp.Literal.number('1.0'),expression=args[0]),expression=exp.Nullif(this=args[1],expression=exp.Literal.number('0')))
            return binary[op](this=args[0],expression=args[1])
        raise PlanError('unsupported structured expression')

    root=stages[0]['id'];query=exp.Select().from_(exp.to_table(root));connected={root}
    for join in plan.get('joins',[]):
        right=join.get('right');left=join.get('left');kind=join.get('kind','left')
        if left not in connected or right not in staged or right in connected or kind not in {'left','inner'}:raise PlanError('join must extend a connected stage program')
        pairs=join.get('on') or []
        if not pairs:raise PlanError('explicit join keys required')
        right_columns={p['right_column'] for p in pairs}
        if not any(set(key)<=right_columns for key in staged[right]['unique_keys']):
            raise PlanError('right-side uniqueness is not established by the computation grain')
        conditions=[exp.EQ(this=expression({'stage':left,'column':p['left_column']}),
                           expression=expression({'stage':right,'column':p['right_column']})) for p in pairs]
        query=query.join(exp.to_table(right),on=exp.and_(*conditions),join_type=kind)
        connected.add(right);certificates.append({'left':left,'right':right,'right_unique_keys':staged[right]['unique_keys'],'multiplicity':'at_most_one_match'})
    if connected!=set(staged):raise PlanError('unconnected computation stage')
    selected=plan.get('select') or []
    if not selected:raise PlanError('explicit output slots required')
    exprs=[expression(p['expression']) for p in selected]
    group=[expression(p) for p in plan.get('group_by',[])]
    aggregates=any(e.find(exp.AggFunc) for e in exprs)
    if group or aggregates:
        for e in exprs:
            for c in e.find_all(exp.Column):
                if c.find_ancestor(exp.AggFunc) is None and not any(c==g or e==g for g in group):
                    raise PlanError('output not compatible with requested aggregate grain')
    query=query.select(*[exp.alias_(e,p.get('alias') or f'output_{i}',quoted=True) for i,(p,e) in enumerate(zip(selected,exprs))])
    if group:query.set('group',exp.Group(expressions=group))
    def predicate(p):
        left=expression(p['left']);right=expression(p['right'])
        operators={'eq':exp.EQ,'neq':exp.NEQ,'gt':exp.GT,'gte':exp.GTE,'lt':exp.LT,'lte':exp.LTE,'like':exp.Like,'is':exp.Is}
        if p.get('op') not in operators:raise PlanError('unsupported predicate')
        return operators[p['op']](this=left,expression=right)
    if plan.get('where'):
        preds=[predicate(p) for p in plan['where']]
        if any(p.find(exp.AggFunc) for p in preds):raise PlanError('aggregation cannot be filtered in WHERE')
        query=query.where(exp.and_(*preds))
    if plan.get('having'):
        if not (group or aggregates):raise PlanError('HAVING needs aggregation')
        query.set('having',exp.Having(this=exp.and_(*[predicate(p) for p in plan['having']])))
    if plan.get('distinct'):query.set('distinct',exp.Distinct())
    if plan.get('order_by'):
        query.set('order',exp.Order(expressions=[exp.Ordered(this=expression(p['expression']),desc=bool(p.get('descending',False)),nulls_first=not bool(p.get('descending',False))) for p in plan['order_by']]))
    if plan.get('limit') is not None:
        n=plan['limit']
        if not isinstance(n,int) or isinstance(n,bool) or n<1:raise PlanError('positive integer limit required')
        query=query.limit(n)
    query.set('with_',exp.With(expressions=ctes))
    sql=query.sql(dialect=dialect.lower())
    parse_query(sql,dialect)
    return sql,{'decision':'compose','dependencies':dependencies,'stage_count':len(stages),'join_certificates':certificates,'uses_evaluator':False}


PROMPT='''Use the supplied SQL-history computation interfaces to answer the current question.
Return a JSON PLAN, never SQL. Existing main SQL is an available complete stage $main.
Historical scope SQL remains immutable except for declared predicate parameters. Preserve
each historical computation's roles, filtering, aggregation and window stages. Select a
history source only when its business scope and grain match the question. Literal parameters
may be changed to requested values; bind every required placeholder. Do not import unrelated
historical filters or choose a computation merely because it mentions a similar table.

Decisions: {"decision":"retain","reason":"..."} keeps the complete existing main.
Or {"decision":"compose","reason":"...","stages":[{"id":"s0","source_id":"...",
"fingerprint":"copy exact supplied fingerprint","parameters":[{"index":0,"value":"..."}]}],
"joins":[],"select":[{"expression":{"stage":"s0","column":"c0"},"alias":"..."}],
"group_by":[],"where":[],"having":[],"order_by":[],"limit":null,"distinct":false}.
References are {"stage":"s0","column":"c0"}; scalar constants are {"literal":123}.
Expressions may be {"op":"sum|avg|min|max|count|count_distinct|add|subtract|multiply|divide",
"args":[expressions]}. Binary arithmetic needs two args, aggregate needs one. Aggregating
an already-aggregated source operates on that stage's output and preserves the inner stage.
Every non-aggregated output must belong to group_by when aggregating.
Joins: {"left":"s0","right":"s1","kind":"left|inner",
"on":[{"left_column":"c0","right_column":"c0"}]}. A right unique_key must be
covered by join keys so joining metrics cannot multiply the left rows. All stages connected.
Filters: {"left":expression,"op":"eq|neq|gt|gte|lt|lte|like|is","right":expression}.
order_by: [{"expression":expression,"descending":true}].
Preserve requested output roles and ordering. A successful execution is not proof of meaning.
Use retain if available interfaces do not support a better answer. Keep all existing main
capabilities; do not simplify away valid fields or add unwarranted time/aggregation transforms.
'''


def plan_sql_history(*,question,proposal_sql,react,documents,tools,client,reranker=None,dialect='SQLite'):
    from .sql_history_composer import library_for_question,column_domains
    library=library_for_question(question,documents,tools,reranker)
    interfaces=make_interfaces(library,proposal_sql,dialect)
    evidence=[{'source_id':r.get('evidence_candidate_id'),'evidence':r.get('evidence')} for r in (react.get('initial_search') or {}).get('results',[])][:12]
    payload={'question':question,'sql_dialect':dialect,'interfaces':interfaces,'recovered_evidence':evidence,
             'column_values':column_domains([proposal_sql],tools,dialect),
             'graph_program':react.get('compact_relational_program') or react.get('graph_evo_program_context') or {}}
    plan,usage=client.chat_json_with_metadata(PROMPT,json.dumps(payload,ensure_ascii=False))
    meta={'method':'sql_history_contract_plan_v1','plan':plan,'usage':usage,'prior_sql':proposal_sql,
          'interfaces':interfaces,'accepted':False,'changed':False,'uses_evaluator_gold':False}
    try:
        sql,compilation=compile_plan(plan,interfaces,dialect=dialect)
        meta['compilation']=compilation;meta['compiled_sql']=sql
        if plan.get('decision')=='retain':meta['accepted']=True;return proposal_sql,meta
        observation=tools.execute_sql(sql,limit=3);meta['execution']=observation
        if not observation.get('executable'):raise PlanError('compiled SQL execution failed')
        meta.update(accepted=True,changed=sql!=proposal_sql)
        return sql,meta
    except (PlanError,ValueError,KeyError,TypeError,sqlglot.errors.SqlglotError) as exc:
        meta['compile_error']=str(exc)
        return proposal_sql,meta
