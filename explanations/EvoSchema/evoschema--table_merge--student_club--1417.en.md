# EvoSchema / evoschema::table_merge::student_club::1417 — Schema and business semantics

The saved catalogue for this database contains 7 tables, 48 physical columns, 0 relationships and 7 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## attendance

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| attendance.link_to_event | Physical name retained; no saved recovered alias | TEXT | schema / attendance |
| attendance.link_to_member | Physical name retained; no saved recovered alias | TEXT | schema / attendance |

## event_budget

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| event_budget.event_id | Physical name retained; no saved recovered alias | TEXT | schema / event_budget |
| event_budget.event_name | Physical name retained; no saved recovered alias | TEXT | schema / event_budget |
| event_budget.event_date | Physical name retained; no saved recovered alias | TEXT | schema / event_budget |
| event_budget.type | Physical name retained; no saved recovered alias | TEXT | schema / event_budget |
| event_budget.notes | Physical name retained; no saved recovered alias | TEXT | schema / event_budget |
| event_budget.location | Physical name retained; no saved recovered alias | TEXT | schema / event_budget |
| event_budget.status | Physical name retained; no saved recovered alias | TEXT | schema / event_budget |
| event_budget.budget_id | Physical name retained; no saved recovered alias | TEXT | schema / event_budget |
| event_budget.category | Physical name retained; no saved recovered alias | TEXT | schema / event_budget |
| event_budget.spent | Physical name retained; no saved recovered alias | REAL | schema / event_budget |
| event_budget.remaining | Physical name retained; no saved recovered alias | REAL | schema / event_budget |
| event_budget.amount | Physical name retained; no saved recovered alias | INTEGER | schema / event_budget |
| event_budget.event_status | Physical name retained; no saved recovered alias | TEXT | schema / event_budget |
| event_budget.link_to_event | Physical name retained; no saved recovered alias | TEXT | schema / event_budget |

## expense

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| expense.expense_id | Physical name retained; no saved recovered alias | TEXT | schema / expense |
| expense.expense_description | Physical name retained; no saved recovered alias | TEXT | schema / expense |
| expense.expense_date | Physical name retained; no saved recovered alias | TEXT | schema / expense |
| expense.cost | Physical name retained; no saved recovered alias | REAL | schema / expense |
| expense.approved | Physical name retained; no saved recovered alias | TEXT | schema / expense |
| expense.link_to_member | Physical name retained; no saved recovered alias | TEXT | schema / expense |
| expense.link_to_budget | Physical name retained; no saved recovered alias | TEXT | schema / expense |

## income

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| income.income_id | Physical name retained; no saved recovered alias | TEXT | schema / income |
| income.date_received | Physical name retained; no saved recovered alias | TEXT | schema / income |
| income.amount | Physical name retained; no saved recovered alias | INTEGER | schema / income |
| income.source | Physical name retained; no saved recovered alias | TEXT | schema / income |
| income.notes | Physical name retained; no saved recovered alias | TEXT | schema / income |
| income.link_to_member | Physical name retained; no saved recovered alias | TEXT | schema / income |

## major

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| major.major_id | Physical name retained; no saved recovered alias | TEXT | schema / major |
| major.major_name | Physical name retained; no saved recovered alias | TEXT | schema / major |
| major.department | Physical name retained; no saved recovered alias | TEXT | schema / major |
| major.college | Physical name retained; no saved recovered alias | TEXT | schema / major |

## member

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| member.member_id | Physical name retained; no saved recovered alias | TEXT | schema / member |
| member.first_name | Physical name retained; no saved recovered alias | TEXT | schema / member |
| member.last_name | Physical name retained; no saved recovered alias | TEXT | schema / member |
| member.email | Physical name retained; no saved recovered alias | TEXT | schema / member |
| member.position | Physical name retained; no saved recovered alias | TEXT | schema / member |
| member.t_shirt_size | Physical name retained; no saved recovered alias | TEXT | schema / member |
| member.phone | Physical name retained; no saved recovered alias | TEXT | schema / member |
| member.zip | Physical name retained; no saved recovered alias | INTEGER | schema / member |
| member.link_to_major | Physical name retained; no saved recovered alias | TEXT | schema / member |

## zip_code

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| zip_code.zip_code | Physical name retained; no saved recovered alias | INTEGER | schema / zip_code |
| zip_code.type | Physical name retained; no saved recovered alias | TEXT | schema / zip_code |
| zip_code.city | Physical name retained; no saved recovered alias | TEXT | schema / zip_code |
| zip_code.county | Physical name retained; no saved recovered alias | TEXT | schema / zip_code |
| zip_code.state | Physical name retained; no saved recovered alias | TEXT | schema / zip_code |
| zip_code.short_state | Physical name retained; no saved recovered alias | TEXT | schema / zip_code |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

