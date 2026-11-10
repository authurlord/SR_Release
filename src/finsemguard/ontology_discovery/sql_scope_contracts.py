"""Role-preserving computation contracts inferred solely from a SQL scope.

Canonicalization is deliberately structural: source aliases may change, but
join direction, filters, grouping and relation occurrences cannot disappear.
Complex scopes retain their original staged program in workload_semantics.
"""
from __future__ import annotations

from typing import Any
from sqlglot import exp
from sqlglot.optimizer.scope import Scope


class ScopeContract:
    def __init__(self, scope: Scope, dialect: str):
        self.dialect = dialect
        self.select = scope.expression
        if not isinstance(self.select, exp.Select):
            raise ValueError("not a SELECT scope")
        # These operators require preserving the full projection/staged query.
        if any(self.select.args.get(k) for k in ("distinct", "limit", "offset", "qualify")):
            raise ValueError("projection-sensitive scope")
        self.sources = {name.casefold(): source for name, (_, source) in scope.selected_sources.items()}
        if not self.sources or not all(isinstance(s, exp.Table) for s in self.sources.values()):
            raise ValueError("derived relation needs a staged contract")
        if any(j.args.get("using") or j.args.get("method") for j in self.select.args.get("joins") or []):
            raise ValueError("implicit join needs a catalogue")
        self.roles = {name: f"r{i}" for i, name in enumerate(self.sources)}
        self.relations = [{"role": self.roles[name],
                           "physical_table": ".".join(p.name for p in source.parts)}
                          for name, source in self.sources.items()]
        self.outputs: dict[str, exp.Expression] = {}
        self.duplicate_outputs: set[str] = set()
        self.aggregate_scope = any(a.find_ancestor(exp.Window) is None
            for p in self.select.expressions for a in p.find_all(exp.AggFunc))
        for projection in self.select.expressions:
            name = projection.alias_or_name.casefold()
            if name in self.outputs:
                self.duplicate_outputs.add(name)
            self.outputs[name] = projection.this if isinstance(projection, exp.Alias) else projection
        self.grain = []
        group = self.select.args.get("group")
        for item in group.expressions if group else []:
            if isinstance(item, exp.Literal) and item.is_int:
                position = int(item.this)
                if not 1 <= position <= len(self.select.expressions):
                    raise ValueError("invalid grouping position")
                item = self.select.expressions[position-1]
                item = item.this if isinstance(item, exp.Alias) else item
            self.grain.append(self.canonical(item, output_aliases=True))
        # GROUPING SETS/ROLLUP/CUBE need their exact staged program, not a flat grain.
        if group and any(v for k, v in group.args.items() if k != "expressions"):
            raise ValueError("non-flat grouping")
        self.base = self.select.copy()
        self.base.set("expressions", [])
        self.base.set("order", None)  # No LIMIT/OFFSET: outer ordering does not change a value.
        self.base.set("with_", None)  # All selected sources are physical; unused CTEs are irrelevant.
        for table in self.base.find_all(exp.Table):
            name = table.alias_or_name.casefold()
            if name not in self.roles:
                raise ValueError("nested source")
            table.set("alias", exp.TableAlias(this=exp.to_identifier(self.roles[name], quoted=True)))
        for key in ("where", "having"):
            clause = self.select.args.get(key)
            if clause is not None:
                self.base.set(key, self.canonical(clause, output_aliases=key == "having"))
        for old, new in zip(self.select.args.get("joins") or [], self.base.args.get("joins") or []):
            if old.args.get("on") is not None:
                new.set("on", self.canonical(old.args["on"]))
        if group:
            self.base.set("group", exp.Group(expressions=[g.copy() for g in self.grain]))
        # Identity excludes output spelling and unrelated projections, while
        # retaining every row-selection and join-multiplicity operator.
        self.context = {"relations": self.relations, "relational_sql": self.render(self.base)}

    def render(self, expression: exp.Expression) -> str:
        if self.dialect.casefold() == 'sqlite':
            def adapt(node: exp.Expression) -> exp.Expression:
                # The history parser understands these standard date parts,
                # but SQLite has no YEAR()/MONTH() builtins. Realize their
                # integer-valued contract using SQLite's native date function.
                formats = {exp.Year: '%Y', exp.Month: '%m', exp.Day: '%d', exp.DayOfMonth: '%d'}
                fmt = formats.get(type(node))
                if fmt:
                    return exp.Cast(this=exp.Anonymous(this='STRFTIME',
                        expressions=[exp.Literal.string(fmt), node.this.copy()]),
                        to=exp.DataType.build('INTEGER'))
                return node
            expression = expression.copy().transform(adapt)
        return expression.sql(dialect=self.dialect)

    def canonical(self, expression: exp.Expression, *, output_aliases: bool = False) -> exp.Expression:
        if any(isinstance(n, (exp.Select, exp.Subquery, exp.Star)) for n in expression.walk()
               if not isinstance(n.parent, exp.Count)):
            raise ValueError("unresolved nested expression")

        def replace(node: exp.Expression) -> exp.Expression:
            if not isinstance(node, exp.Column):
                return node
            if node.is_star:
                raise ValueError("wildcard")
            if output_aliases and not node.table and node.name.casefold() in self.outputs:
                if node.name.casefold() in self.duplicate_outputs:
                    raise ValueError("ambiguous output alias")
                return self.canonical(self.outputs[node.name.casefold()])
            name = node.table.casefold() if node.table else next(iter(self.sources)) if len(self.sources) == 1 else ""
            if name not in self.roles:
                raise ValueError("ambiguous source")
            return exp.column(node.name, table=self.roles[name], quoted=True)

        return expression.copy().transform(replace)

    def computation(self, expression: exp.Expression) -> dict[str, Any]:
        formula = self.canonical(expression)
        if self.aggregate_scope and (
            formula.find(exp.Window) is not None
            or (formula.find(exp.AggFunc) is None and not any(formula == g for g in self.grain))
        ):
            # Bare columns beside MIN/MAX may depend on which aggregate picked
            # a row. A global aggregate also turns many rows into one: projecting
            # its bare column alone would change cardinality.
            raise ValueError("projection depends on another aggregate")
        query = self.base.copy()
        query.set("expressions", [
            *(exp.alias_(g.copy(), f"grain_{i}", quoted=True) for i, g in enumerate(self.grain)),
            exp.alias_(formula.copy(), "value", quoted=True),
        ])
        return {"formula": self.render(formula),
                "grain": [self.render(g) for g in self.grain],
                "role_bindings": self.relations,
                "scope_sql": self.render(query),
                "requires_staged_execution": False}
