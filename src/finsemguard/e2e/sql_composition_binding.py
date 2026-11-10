"""Realize composed SQL against draft consensus and observed physical value domains."""
from __future__ import annotations
import sqlglot
from sqlglot import exp
from sqlglot.optimizer.scope import traverse_scope
from finsemguard.e2e.sql_history_composer import preserve_equivalent_projection_order,preserve_existing_output_slots


def _scope_tables(tree):
    scope=traverse_scope(tree)[-1]
    return {a.casefold():s.name for a,(_,s) in scope.selected_sources.items() if isinstance(s,exp.Table)}


def _column_identity(col,sources):
    if not isinstance(col,exp.Column):return None
    table=sources.get(col.table.casefold()) if col.table else next(iter(sources.values())) if len(sources)==1 else None
    return (table,col.name) if table and not col.is_star else None


def _projection_signature(sql,dialect):
    tree=sqlglot.parse_one(sql,read=dialect.lower())
    if not isinstance(tree,exp.Select):return None
    sources=_scope_tables(tree)
    # Same physical source twice requires relation-role alignment; no consensus
    # claim is made merely because its physical column names happen to match.
    if len(set(sources.values()))!=len(sources):return None
    def bind(n):
        if isinstance(n,exp.Column):
            identity=_column_identity(n,sources)
            if not identity:raise ValueError('unbound output')
            return exp.column(identity[1].casefold(),table=identity[0].casefold(),quoted=True)
        return n
    return tuple((p.this if isinstance(p,exp.Alias) else p).copy().transform(bind).sql(dialect=dialect.lower()) for p in tree.expressions)


def realize_computation_bindings(*,prior_sql,candidate_sql,react,tools,dialect='SQLite'):
    """No question IDs, scores, reference SQL, or dataset-specific constants."""
    changes=[]
    if dialect.casefold()!='sqlite':return candidate_sql,changes
    try:
        prior_sig=_projection_signature(prior_sql,dialect)
        consensus=False
        for name in ('auxiliary_raw_evidence_draft','persistent_recovery_advisory_draft'):
            draft=(react.get(name) or {}).get('base_sql')
            if draft and prior_sig and _projection_signature(draft,dialect)==prior_sig:
                consensus=True;break
        sql=(preserve_existing_output_slots(prior_sql,candidate_sql,dialect) if consensus else preserve_equivalent_projection_order(prior_sql,candidate_sql,dialect))
        if sql!=candidate_sql:changes.append({'operator':'reuse_consensus_output_slots' if consensus else 'reuse_output_order'})
        old,new=[sqlglot.parse_one(s,read=dialect.lower()) for s in (prior_sql,sql)]
        if not all(isinstance(t,exp.Select) for t in (old,new)):return sql,changes
        os,ns=_scope_tables(old),_scope_tables(new)
        def literal_bindings(tree,sources):
            out=[];where=tree.args.get('where')
            if where is None:return out
            for eq in where.find_all(exp.EQ):
                if eq.find_ancestor(exp.Select) is not tree:continue
                for col,lit in ((eq.this,eq.expression),(eq.expression,eq.this)):
                    identity=_column_identity(col,sources)
                    if identity and isinstance(lit,exp.Literal):out.append((eq,col,lit,identity))
            return out
        def exists(identity,lit):
            table,column=identity
            if table not in tools.columns or column not in {c for c,_ in tools.columns[table]}:return None
            q=exp.select('1').from_(exp.Table(this=exp.to_identifier(table,quoted=True))).where(exp.EQ(this=exp.column(column,quoted=True),expression=lit.copy())).limit(1).sql(dialect='sqlite')
            observation=tools.execute_sql(q,limit=1)
            return bool(observation.get('rows')) if observation.get('executable') else None
        old_bindings=literal_bindings(old,os)
        for node,col,lit,identity in literal_bindings(new,ns):
            candidates={old_id for _,_,value,old_id in old_bindings if value==lit and old_id!=identity and old_id[0]==identity[0]}
            if len(candidates)!=1:continue
            previous=next(iter(candidates))
            if exists(identity,lit) is False and exists(previous,lit) is True:
                col.set('this',exp.to_identifier(previous[1],quoted=True))
                changes.append({'operator':'realize_literal_binding','literal':lit.sql(),'from':'.'.join(identity),'to':'.'.join(previous),'evidence':'candidate field has no exact value; original role field has the exact requested value'})
        # Reject a newly introduced time-of-day computation when the physical
        # field supplies values but the computation erases all observed values.
        # This infers representable temporal precision from the data itself.
        old_columns={_column_identity(c,os) for c in old.find_all(exp.Column) if c.find_ancestor(exp.Select) is old}
        def time_nodes(tree):
            return [(n,n.this) for n in tree.find_all(exp.Time)] + [(n,n.expressions[0]) for n in tree.find_all(exp.Anonymous) if n.name.casefold()=='time' and len(n.expressions)==1]
        old_time={_column_identity(c,os) for n,c in time_nodes(old) if n.find_ancestor(exp.Select) is old}
        for node,col in time_nodes(new):
            if node.find_ancestor(exp.Select) is not new:continue
            identity=_column_identity(col,ns)
            if not identity or identity not in old_columns or identity in old_time:continue
            table,column=identity
            expression=node.copy().transform(lambda n:exp.column(column,quoted=True) if isinstance(n,exp.Column) else n)
            q=exp.select(exp.column(column,quoted=True),expression).from_(exp.Table(this=exp.to_identifier(table,quoted=True))).where(exp.Not(this=exp.Is(this=exp.column(column,quoted=True),expression=exp.Null()))).limit(12).sql(dialect='sqlite')
            obs=tools.execute_sql(q,limit=12);values=obs.get('rows') or []
            if obs.get('executable') and values and all(row[1] is None for row in values):
                node.replace(col.copy())
                changes.append({'operator':'preserve_observed_temporal_grain','physical_column':'.'.join(identity),'evidence':'time-of-day conversion returns NULL for every observed non-null source value'})
        return new.sql(dialect='sqlite'),changes
    except (ValueError,IndexError,sqlglot.errors.SqlglotError):
        return candidate_sql,changes


def bind_composed_result(result,tools,dialect='SQLite'):
    """Use the same realization in live generation and saved-stage continuation."""
    import copy
    output=copy.deepcopy(result)
    composition=output['react']['sql_history_composition']
    prior=composition['prior_sql']
    raw=composition['plan'].get('candidate_sql') if composition['accepted'] else prior
    sql,changes=realize_computation_bindings(prior_sql=prior,candidate_sql=raw or prior,react=output['react'],tools=tools,dialect=dialect)
    observation=tools.execute_sql(sql,limit=3)
    if not observation.get('executable'):
        sql=prior
    composition.update(method='sql_history_bound_composition_v2',compiled_sql=sql,
        binding_realization=changes,binding_execution=observation,changed=sql!=prior)
    output['sql']=sql
    output['execution_probe']={'executable':True} if observation.get('executable') else output.get('execution_probe')
    return output
