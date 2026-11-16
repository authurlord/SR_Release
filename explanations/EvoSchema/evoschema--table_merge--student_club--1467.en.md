# EvoSchema / evoschema::table_merge::student_club::1467 — Schema and business semantics

The saved catalogue for this database contains 7 tables, 48 physical columns, 0 relationships and 7 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## attendance

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| attendance.link_to_event | Physical name retained; no saved recovered alias | TEXT | schema / attendance |
| attendance.link_to_member | Physical name retained; no saved recovered alias | TEXT | schema / attendance |

## budget_event

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: T1

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| budget_event.budget_id | Physical name retained; no saved recovered alias | TEXT | schema / budget_event |
| budget_event.category | Physical name retained; no saved recovered alias | TEXT | schema / budget_event |
| budget_event.spent | Physical name retained; no saved recovered alias | REAL | schema / budget_event |
| budget_event.remaining | Physical name retained; no saved recovered alias | REAL | schema / budget_event |
| budget_event.amount | Physical name retained; no saved recovered alias | INTEGER | schema / budget_event |
| budget_event.event_status | Physical name retained; no saved recovered alias | TEXT | schema / budget_event |
| budget_event.link_to_event | Physical name retained; no saved recovered alias | TEXT | schema / budget_event |
| budget_event.event_id | Physical name retained; no saved recovered alias | TEXT | schema / budget_event |
| budget_event.event_name | Physical name retained; no saved recovered alias | TEXT | schema / budget_event |
| budget_event.event_date | Physical name retained; no saved recovered alias | TEXT | schema / budget_event |
| budget_event.type | Physical name retained; no saved recovered alias | TEXT | schema / budget_event |
| budget_event.notes | Physical name retained; no saved recovered alias | TEXT | schema / budget_event |
| budget_event.location | Physical name retained; no saved recovered alias | TEXT | schema / budget_event |
| budget_event.status | Physical name retained; no saved recovered alias | TEXT | schema / budget_event |

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

