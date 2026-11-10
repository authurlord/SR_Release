"""Instantiate reusable computation scopes before cross-stage composition.

Explicit role/column bindings and parameterized row predicates let a historical
computation answer a new workload question without requiring an identical old
filter or output grain. Physical relation roles and formula ASTs stay sourced.
"""
from __future__ import annotations
from copy import deepcopy
from hashlib import sha256
import json
import sqlglot
from sqlglot import exp
from sqlglot.optimizer.scope import traverse_scope
from .sql_contract_plan import (PlanError,PROMPT,compile_plan,interface,make_interfaces,parameters,parse_query)


def scope_interfaces(library,prior_sql,tools,dialect='SQLite'):
    # Resolve wildcard output slots from the current physical catalog. Retaining
    # the parent still returns its exact SQL; this only makes its stage reusable.
    tree=parse_query(prior_sql,dialect)
    if any(isinstance(p,exp.Star) or isinstance(p,exp.Column) and p.is_star for p in tree.selects):
        from sqlglot.optimizer.qualify import qualify
        schema={table:{column:'UNKNOWN' for column,_ in columns} for table,columns in tools.columns.items()}
        prior_sql=qualify(tree,dialect=dialect.lower(),schema=schema,infer_schema=False).sql(dialect=dialect.lower())
    interfaces=make_interfaces(library,prior_sql,dialect)
    for item in interfaces:
        tree=parse_query(item['scope_sql'],dialect);scopes=traverse_scope(tree)
        item['supports_scope_adaptation']=False
        if not isinstance(tree,exp.Select) or len(scopes)!=1:continue
        roles={name:source for name,(_,source) in scopes[0].selected_sources.items()}
        if not roles or any(not isinstance(source,exp.Table) or source.name not in tools.columns for source in roles.values()):continue
        item['input_roles']={name:{'physical_table':source.name,'columns':[{'column':c,'type':t} for c,t in tools.columns[source.name]]} for name,source in roles.items()}
        item['supports_scope_adaptation']=True
        item['existing_filter']=tree.args['where'].this.sql(dialect=dialect.lower()) if tree.args.get('where') else None
        item['existing_grain']=[x.sql(dialect=dialect.lower()) for x in tree.args['group'].expressions] if tree.args.get('group') else []
        item['fingerprint']=sha256(json.dumps(item,sort_keys=True).encode()).hexdigest()
    return interfaces


def instantiate(source,adaptation,dialect):
    if not source.get('supports_scope_adaptation'):raise PlanError('staged source cannot be flattened; use its complete interface')
    tree=parse_query(source['scope_sql'],dialect)
    projections=[p.this.copy() if isinstance(p,exp.Alias) else p.copy() for p in tree.expressions]
    def field(obj):
        role=obj.get('role');column=obj.get('column');r=source['input_roles'].get(role)
        if r is None or column not in {x['column'] for x in r['columns']}:raise PlanError('unknown physical role/column')
        return exp.column(column,table=role,quoted=True)
    def expression(obj):
        if 'role' in obj:return field(obj)
        if 'output_column' in obj:
            name=obj['output_column'];valid={o['column']:i for i,o in enumerate(source['outputs'])}
            if name not in valid:raise PlanError('unknown source formula')
            return projections[valid[name]].copy()
        if 'literal' in obj:
            value=obj['literal']
            if not isinstance(value,(str,int,float,bool,type(None))):raise PlanError('scalar literal required')
            return exp.convert(value)
        raise PlanError('scope expression must reference a source formula or physical role')
    def predicate(obj):
        op=obj.get('op')
        if op in {'and','or'}:
            args=[predicate(x) for x in obj.get('args',[])]
            if len(args)<2:raise PlanError('boolean connective needs at least two predicates')
            return (exp.and_ if op=='and' else exp.or_)(*args)
        if op=='in':return exp.In(this=expression(obj['left']),expressions=[expression(x) for x in obj['values']])
        operators={'eq':exp.EQ,'neq':exp.NEQ,'gt':exp.GT,'gte':exp.GTE,'lt':exp.LT,'lte':exp.LTE,'like':exp.Like,'is':exp.Is}
        if op not in operators:raise PlanError('unsupported scope predicate')
        return operators[op](this=expression(obj['left']),expression=expression(obj['right']))
    if 'where' in adaptation:
        p=adaptation['where'];node=predicate(p) if p is not None else None
        if node is not None and node.find(exp.AggFunc):raise PlanError('row filtering cannot contain an aggregate')
        tree.set('where',exp.Where(this=node) if node is not None else None)
    if 'group_by' in adaptation:
        groups=[expression(g) for g in adaptation['group_by']]
        if any(g.find(exp.AggFunc,exp.Window) for g in groups):raise PlanError('invalid grouping key')
        tree.set('group',exp.Group(expressions=groups) if groups else None)
    if 'project' in adaptation:
        project=adaptation['project']
        if not project:raise PlanError('scope needs outputs')
        expressions=[expression(p['expression']) for p in project]
        tree.set('expressions',[exp.alias_(e,p.get('alias') or f'slot_{i}',quoted=True) for i,(p,e) in enumerate(zip(project,expressions))])
        # A changed projection must not leave ORDER BY ordinal/alias pointing at
        # a different expression. Source ranking/limits require the original full
        # program unless the plan explicitly removes both to move ranking outside.
        if tree.args.get('order') or tree.args.get('limit') or tree.args.get('offset'):
            if not adaptation.get('move_ranking_outside'):raise PlanError('projection change needs explicit outer ranking plan')
            tree.set('order',None);tree.set('limit',None);tree.set('offset',None)
    if 'distinct' in adaptation:tree.set('distinct',exp.Distinct() if adaptation['distinct'] else None)
    if 'having' in adaptation:
        p=adaptation['having'];tree.set('having',exp.Having(this=predicate(p)) if p is not None else None)
    group=tree.args.get('group');keys=[]
    def canonical(node):
        result=node.copy()
        if len(source['input_roles'])==1:
            role=next(iter(source['input_roles']))
            for col in result.find_all(exp.Column):
                if not col.table:col.set('table',exp.to_identifier(role,quoted=True))
        return result.sql(dialect=dialect.lower()).casefold().replace('"','')
    for key in group.expressions if group else []:
        if isinstance(key,exp.Literal) and key.is_int and 1<=int(key.this)<=len(tree.expressions):
            key=tree.expressions[int(key.this)-1]
        elif isinstance(key,exp.Column) and not key.table:
            matches=[p for p in tree.expressions if p.alias and p.alias.casefold()==key.name.casefold()]
            if len(matches)==1:key=matches[0]
        keys.append(key.this if isinstance(key,exp.Alias) else key)
    has_aggregate=any(a.find_ancestor(exp.Window) is None for p in tree.expressions for a in p.find_all(exp.AggFunc))
    if group or has_aggregate:
        for projection in tree.expressions:
            e=projection.this if isinstance(projection,exp.Alias) else projection
            if any(canonical(e)==canonical(g) for g in keys):continue
            for col in e.find_all(exp.Column):
                if col.find_ancestor(exp.AggFunc) is None and not any(canonical(col)==canonical(g) for g in keys):raise PlanError('adapted output violates computation grain')
    return tree.sql(dialect=dialect.lower())


def compile_scope_plan(plan,interfaces,dialect='SQLite'):
    if plan.get('decision')=='retain':return compile_plan(plan,interfaces,dialect=dialect)
    sources={i['source_id']:i for i in interfaces};new_sources=[];adapted=deepcopy(plan);dependencies={};changes=[]
    for stage in adapted.get('stages',[]):
        original=sources.get(stage.get('source_id'))
        if not original:raise PlanError('unknown or withdrawn source')
        if stage.get('fingerprint')!=original['fingerprint']:raise PlanError('stale role bindings')
        dependencies[original['source_id']]=original['fingerprint']
        # Parameters bind the original scope first so exposed indexes remain stable.
        source=deepcopy(original);tree=parse_query(source['scope_sql'],dialect);slots=parameters(tree);bound=set()
        for parameter in stage.pop('parameters',[]):
            index=parameter['index']
            if not isinstance(index,int) or isinstance(index,bool) or not 0<=index<len(slots) or index in bound:raise PlanError('invalid parameter binding')
            value=parameter['value']
            if not isinstance(value,(str,int,float,bool,type(None))):raise PlanError('scalar parameter required')
            slots[index].replace(exp.convert(value));bound.add(index)
        source['scope_sql']=tree.sql(dialect=dialect.lower())
        adaptation=stage.pop('adapt_scope',None)
        if adaptation:
            if not str(adaptation.get('reason','')).strip():raise PlanError('scope adaptation needs requested semantic intent')
            source['scope_sql']=instantiate(source,adaptation,dialect)
            changes.append({'source_id':original['source_id'],'stage':stage['id'],'adaptation':adaptation})
        local_id=original['source_id']+'@'+stage['id']
        rebound=interface(local_id,source['scope_sql'],dialect=dialect,aliases=source.get('aliases',[]),evidence=source.get('source_evidence_ids',[]))
        new_sources.append(rebound);stage['source_id']=local_id;stage['fingerprint']=rebound['fingerprint']
    sql,metadata=compile_plan(adapted,new_sources,dialect=dialect)
    metadata['dependencies']=dependencies;metadata['scope_adaptations']=changes
    return sql,metadata


SCOPE_PROMPT=PROMPT+'''
Additional capability: simple source scopes expose input_roles with current physical columns.
A stage may include adapt_scope to instantiate a historical computation for NEW requested roles,
filters or grain. This is a structured binding plan, not replacement SQL. Be active in resolving
incorrect draft bindings using supplied recovered semantics and observed value domains.
adapt_scope={"reason":"question-grounded intent","project":[{"expression":{"role":"alias",
"column":"physical_column"},"alias":"name"},{"expression":{"output_column":"c1"},"alias":"metric"}],
"where":predicate-or-null,"group_by":[scope expressions],"having":predicate-or-null,"distinct":false}.
Each key is OPTIONAL: absent means preserve original clause. Output_column reuses an original
formula; role+column selects a physically available field without changing that relation role.
project changes stage outputs to c0,c1,... in its new order; outer select references these NEW slots.
Scope predicates use the same comparison ops but their expressions are role+column, output_column,
or literal; {"op":"and|or","args":[predicates]} and {"op":"in","left":expr,"values":[exprs]}
are also supported. Row filters must precede aggregation; group_by names the desired entity grain.
Do not change grain, drop a filter, or remove an output solely to match a historical query. Apply
the current question's complete requested semantics. Preserve existing valid joins and roles.
When project changes a ranked/limited source, move_ranking_outside:true removes inner ranking and
limit; then explicitly express the intended order_by and limit in the outer plan. Without it,
projection changes in ranked/limited sources are rejected. Complex sources are reusable whole;
adapt_scope is available only when supports_scope_adaptation=true.
'''


def plan_scoped_sql_history(*,question,proposal_sql,react,documents,tools,client,reranker=None,dialect='SQLite'):
    from .sql_history_composer import library_for_question,column_domains
    library=library_for_question(question,documents,tools,reranker)
    interfaces=scope_interfaces(library,proposal_sql,tools,dialect)
    evidence=[{'source_id':r.get('evidence_candidate_id'),'evidence':r.get('evidence')} for r in (react.get('initial_search') or {}).get('results',[])][:12]
    payload={'question':question,'sql_dialect':dialect,'interfaces':interfaces,'recovered_evidence':evidence,
             'column_values':column_domains([proposal_sql],tools,dialect),
             'graph_program':react.get('compact_relational_program') or react.get('graph_evo_program_context') or {}}
    plan,usage=client.chat_json_with_metadata(SCOPE_PROMPT,json.dumps(payload,ensure_ascii=False))
    meta={'method':'sql_history_contract_scope_v2','plan':plan,'usage':usage,'prior_sql':proposal_sql,
          'interfaces':interfaces,'accepted':False,'changed':False,'uses_evaluator_gold':False}
    try:
        sql,compilation=compile_scope_plan(plan,interfaces,dialect);meta.update(compiled_sql=sql,compilation=compilation)
        if plan.get('decision')=='retain':meta['accepted']=True;return proposal_sql,meta
        observation=tools.execute_sql(sql,limit=3);meta['execution']=observation
        if not observation.get('executable'):raise PlanError('compiled SQL execution failed')
        meta.update(accepted=True,changed=sql!=proposal_sql);return sql,meta
    except (PlanError,ValueError,KeyError,TypeError,sqlglot.errors.SqlglotError) as exc:
        meta['compile_error']=str(exc);return proposal_sql,meta
