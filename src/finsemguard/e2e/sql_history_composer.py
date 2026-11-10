"""Compose current queries from SQL-derived computations and existing Graph/Evo assets.

This is an additive main-method generation stage. Historical expressions are
reusable implementations, not answers to the current question. No score/label
or evaluator input is accepted by this interface.
"""
from __future__ import annotations

import json
import re
from typing import Any
import sqlglot
from sqlglot import exp
from sqlglot.optimizer.scope import traverse_scope

PROMPT = """Construct the SQL answering the current question by composing the supplied
SQL-derived computation library with the current Graph/Evo bindings. Historical SQL is
semantic supervision: it shows what fields mean, which entity roles join, the grain of a
measure, and which computations must occur in separate stages. Reuse those structures
where they match requested roles. Different occurrences of the same table can have different
roles. Preserve a computation's aggregation/window stage and multiplicity; adapt its
historical literal parameters and output grain to this question. Do not import historical
filters, output columns, grouping, DISTINCT, or LIMIT unless the question requires them.

The existing proposal and independent drafts are useful starting implementations, but their
field choices, literal encodings, date boundaries, and output shapes may be wrong. They are
not immutable. Resolve their disagreements using SQL history, recovered aliases and actual
column values. A successful execution is not semantic proof. An empty result is not evidence
of a mistake. Never invent a numeric threshold for a vague comparison, or a fixed date for
a relative interval, merely because a draft contains it. Stored numeric measures should not
be confused with counts of rows. For an entity request select its human-readable identity
when supported; do not return an unrelated code or extra columns. Distinguish a row-level
maximum from a grouped total according to the requested entity and history.

Return a JSON object with: role_plan (brief requested role -> physical expression),
contract_reuse (list of {source_id, operation, adaptation} describing historical computation
reuse), changes (brief evidence-supported changes), candidate_sql. Use only current physical
identifiers. candidate_sql must be one complete read-only query in sql_dialect. Keep the
existing SQL if no better supported construction is available. No markdown or other prose.
"""


def terms(text: str) -> set[str]:
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    return set(re.findall(r'[a-z][a-z0-9]{2,}', text.lower())) - {'select','from','where','with','the','and','for','has','that','which','what','as','all'}


def _bound(payload, tools):
    catalog = {t.casefold(): {c.casefold() for c, _ in cs} for t, cs in tools.columns.items()}
    for t in payload.get('physical_tables', []):
        if t.casefold() not in catalog: return False
    for ident in payload.get('physical_identifiers', []):
        table, _, column = ident.rpartition('.')
        if table.casefold() not in catalog or column.casefold() not in catalog[table.casefold()]: return False
    return True


def library_for_question(question, documents, tools, reranker=None):
    q = terms(question); groups = {'computation': [], 'program': []}
    for doc in documents:
        if doc.database_id != tools.database_id: continue
        try: obj = json.loads(doc.text)
        except (TypeError, ValueError): continue
        if obj.get('ontology_kind') != 'sql_workload_semantic_object' or not _bound(obj, tools): continue
        kind = obj.get('kind')
        if kind not in {'metric','binding','program'}: continue
        group = 'program' if kind == 'program' else 'computation'
        alias = ' '.join(obj.get('aliases', []))
        score = len(q & terms(alias))*4 + len(q & terms(doc.text))
        groups[group].append((score, doc.candidate_id, obj))
    output = []
    for kind, rows in groups.items():
        rows = sorted(rows, key=lambda r:(-r[0],r[1]))[:48]
        if not rows: continue
        render = [json.dumps(o,ensure_ascii=False) for _,_,o in rows]
        scores = reranker.score(question, render) if reranker else [r[0] for r in rows]
        ranked = sorted(zip(scores,rows),key=lambda pair:(-pair[0],pair[1][1]))
        for score, (_, identity, obj) in ranked[:(6 if kind=='computation' else 3)]:
            output.append({'source_id':identity,'relevance':score,**obj})
    return output


def column_domains(sqls, tools, dialect):
    """Bounded value observations on physical fields already used by proposals."""
    columns = {}
    for sql in sqls:
        try:
            scopes = traverse_scope(sqlglot.parse_one(sql,read=dialect.lower()))
            for scope in scopes:
                physical = {name.casefold():source.name for name,(_,source) in scope.selected_sources.items() if isinstance(source,exp.Table)}
                for col in scope.columns:
                    table = physical.get(col.table.casefold()) if col.table else next(iter(physical.values())) if len(physical)==1 else None
                    if table not in tools.columns or col.name not in {c for c,_ in tools.columns[table]}: continue
                    priority = 0 if col.find_ancestor(exp.Where,exp.Having) is not None else 1
                    key=(table,col.name);columns[key]=min(priority,columns.get(key,2))
        except (ValueError, sqlglot.errors.SqlglotError): continue
    output=[]
    for (table,column),_ in sorted(columns.items(),key=lambda p:p[1])[:18]:
        t=exp.to_identifier(table,quoted=True).sql(dialect=dialect.lower());c=exp.to_identifier(column,quoted=True).sql(dialect=dialect.lower())
        observation=tools.execute_sql(f'SELECT {c}, COUNT(*) AS frequency FROM {t} WHERE {c} IS NOT NULL GROUP BY {c} ORDER BY frequency DESC LIMIT 12',limit=12)
        if observation.get('executable'):
            output.append({'physical_identifier':f'{table}.{column}','sample_values_with_frequency':observation.get('rows',[]),'sample_is_exhaustive':False})
    return output


def preserve_equivalent_projection_order(prior_sql, candidate_sql, dialect='SQLite'):
    """Reuse the existing output contract when composition only permutes fields.

    Never map across relation occurrences, staged scopes or positional clauses.
    Changed expressions/projection sets remain the composer's responsibility.
    """
    try:
        old,new=[sqlglot.parse_one(s,read=dialect.lower()) for s in (prior_sql,candidate_sql)]
        if not all(isinstance(t,exp.Select) for t in (old,new)):return candidate_sql
        def keys(tree):
            scope=traverse_scope(tree)[-1]
            sources={name.casefold():source.name for name,(_,source) in scope.selected_sources.items() if isinstance(source,exp.Table)}
            if len(sources)!=len(scope.selected_sources) or len(set(sources.values()))!=len(sources):raise ValueError('staged or repeated sources')
            for clause in (tree.args.get('group'),tree.args.get('order')):
                if clause and any(isinstance(n,exp.Literal) and n.is_int for n in clause.walk()):raise ValueError('positional clause')
            def bind(node):
                if isinstance(node,exp.Column):
                    table=sources.get(node.table.casefold()) if node.table else next(iter(sources.values())) if len(sources)==1 else None
                    if not table or node.is_star:raise ValueError('unresolved projection')
                    return exp.column(node.name.casefold(),table=table.casefold(),quoted=True)
                return node
            return [(p.this if isinstance(p,exp.Alias) else p).copy().transform(bind).sql(dialect=dialect.lower()) for p in tree.expressions]
        a,b=keys(old),keys(new)
        if a!=b and len(set(a))==len(a) and len(set(b))==len(b) and set(a)==set(b):
            new.set('expressions',[new.expressions[b.index(k)].copy() for k in a])
            return new.sql(dialect=dialect.lower())
    except (ValueError,IndexError,sqlglot.errors.SqlglotError):pass
    return candidate_sql


def preserve_existing_output_slots(prior_sql, candidate_sql, dialect='SQLite'):
    """Compose a row-query repair without silently deleting existing output slots.

    A strict subset of the same role-bound fields is a formatting simplification,
    not a new semantic binding. Keep the existing output contract in that case.
    New/different fields and aggregate/staged projections are never restored here.
    """
    candidate_sql=preserve_equivalent_projection_order(prior_sql,candidate_sql,dialect)
    try:
        old,new=[sqlglot.parse_one(s,read=dialect.lower()) for s in (prior_sql,candidate_sql)]
        if not all(isinstance(t,exp.Select) for t in (old,new)):return candidate_sql
        if any(t.args.get(k) for t in (old,new) for k in ('group','having','qualify')):return candidate_sql
        if any(p.find(exp.AggFunc,exp.Window,exp.Select,exp.Star) for t in (old,new) for p in t.expressions):return candidate_sql
        def sources_and_edges(tree):
            scope=traverse_scope(tree)[-1]
            sources={a.casefold():s.name.casefold() for a,(_,s) in scope.selected_sources.items() if isinstance(s,exp.Table)}
            if len(sources)!=len(scope.selected_sources):raise ValueError('staged sources')
            edges={a:set() for a in sources}
            for join in tree.args.get('joins') or []:
                on=join.args.get('on')
                if on is None:continue
                for eq in on.find_all(exp.EQ):
                    a,b=eq.this,eq.expression
                    if not all(isinstance(c,exp.Column) and c.table.casefold() in sources for c in (a,b)):continue
                    for left,right in ((a,b),(b,a)):
                        edges[left.table.casefold()].add((left.name.casefold(),sources[right.table.casefold()],right.name.casefold()))
            return sources,edges
        os,oe=sources_and_edges(old);ns,ne=sources_and_edges(new);mapping={}
        for alias,table in os.items():
            candidates=[a for a,t in ns.items() if t==table and oe[alias]<=ne[a]]
            if len(candidates)!=1:raise ValueError('ambiguous role transfer')
            mapping[alias]=candidates[0]
        if len(set(mapping.values()))!=len(mapping):return candidate_sql
        def bind(node, sources, remap):
            if not isinstance(node,exp.Column):return node
            alias=node.table.casefold() if node.table else next(iter(sources)) if len(sources)==1 else ''
            if alias not in remap or node.is_star:raise ValueError('ambiguous projection')
            return exp.column(node.name.casefold(),table=remap[alias],quoted=True)
        transferred=[p.copy().transform(lambda n:bind(n,os,mapping)) for p in old.expressions]
        current=[p.copy().transform(lambda n:bind(n,ns,{a:a for a in ns})) for p in new.expressions]
        key=lambda p:(p.this if isinstance(p,exp.Alias) else p).sql(dialect=dialect.lower())
        a,b=[key(p) for p in transferred],[key(p) for p in current]
        if len(set(a))==len(a) and len(set(b))==len(b) and set(b)<set(a):
            # Positional ordering would refer to a different column after insertion.
            order=new.args.get('order')
            if order and any(isinstance(n,exp.Literal) and n.is_int for n in order.walk()):return candidate_sql
            new.set('expressions',transferred)
            new.set('distinct',old.args['distinct'].copy() if old.args.get('distinct') else None)
            return new.sql(dialect=dialect.lower())
    except (ValueError,IndexError,sqlglot.errors.SqlglotError):pass
    return candidate_sql


def compose_sql_history(*, question: str, proposal_sql: str, react: dict[str,Any],
                        documents, tools, client, dialect='SQLite', reranker=None):
    library=library_for_question(question,documents,tools,reranker)
    drafts=[proposal_sql]
    for key in ('base_solution_anchor','auxiliary_raw_evidence_draft','persistent_recovery_advisory_draft'):
        sql=(react.get(key) or {}).get('base_sql')
        if sql and sql not in drafts: drafts.append(sql)
    evidence=[]; chars=0
    for row in (react.get('initial_search') or {}).get('results',[]):
        text=str(row.get('evidence') or '')
        if chars+len(text)>30000: continue
        evidence.append({'source_id':row.get('evidence_candidate_id'),'evidence':text});chars+=len(text)
        if len(evidence)>=18: break
    involved={t for item in library for t in item.get('physical_tables',[])}
    for sql in drafts:
        try: involved.update(t.name for t in sqlglot.parse_one(sql,read=dialect.lower()).find_all(exp.Table))
        except (ValueError,sqlglot.errors.SqlglotError): pass
    graph=react.get('compact_relational_program') or react.get('graph_evo_program_context') or {}
    schema={t:tools.columns[t] for t in sorted(involved) if t in tools.columns}
    payload={'question':question,'sql_dialect':dialect,'existing_proposal':proposal_sql,
        'independent_drafts':drafts[1:],'sql_computation_library':library,
        'current_schema':schema,'graph_evo_program':graph,'recovered_evidence':evidence,
        'current_column_values':column_domains(drafts,tools,dialect),
        'unresolved_roles':(react.get('compiled_semantic_plan') or {}).get('unresolved_ambiguities',[])}
    plan,usage=client.chat_json_with_metadata(PROMPT,json.dumps(payload,ensure_ascii=False))
    sql=str(plan.get('candidate_sql') or '').strip()
    sql=preserve_existing_output_slots(proposal_sql,sql,dialect)
    trees=sqlglot.parse(sql,read=dialect.lower())
    if len(trees)!=1 or not isinstance(trees[0],exp.Query): raise ValueError('composer must return one read-only query')
    observation=tools.execute_sql(sql,limit=3)
    accepted=bool(observation.get('executable'))
    return (sql if accepted else proposal_sql),{
        'method':'sql_history_composition_v1_2','plan':plan,'accepted':accepted,
        'compiled_sql':sql,
        'source_ids':[x['source_id'] for x in library], 'column_domains':payload['current_column_values'],
        'execution':observation,'usage':usage,'prior_sql':proposal_sql,
        'changed':accepted and sql != proposal_sql,
        'uses_evaluator_gold':False,
    }
