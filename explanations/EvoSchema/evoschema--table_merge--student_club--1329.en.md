# EvoSchema / evoschema::table_merge::student_club::1329 — Schema and business semantics

The saved catalogue for this database contains 7 tables, 48 physical columns, 0 relationships and 7 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## attendance

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| attendance.link_to_event | Physical name retained; no saved recovered alias | TEXT | schema / attendance |
| attendance.link_to_member | Physical name retained; no saved recovered alias | TEXT | schema / attendance |

## budget

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| budget.budget_id | Physical name retained; no saved recovered alias | TEXT | schema / budget |
| budget.category | Physical name retained; no saved recovered alias | TEXT | schema / budget |
| budget.spent | Physical name retained; no saved recovered alias | REAL | schema / budget |
| budget.remaining | Physical name retained; no saved recovered alias | REAL | schema / budget |
| budget.amount | Physical name retained; no saved recovered alias | INTEGER | schema / budget |
| budget.event_status | Physical name retained; no saved recovered alias | TEXT | schema / budget |
| budget.link_to_event | Physical name retained; no saved recovered alias | TEXT | schema / budget |

## event

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| event.event_id | Physical name retained; no saved recovered alias | TEXT | schema / event |
| event.event_name | Physical name retained; no saved recovered alias | TEXT | schema / event |
| event.event_date | Physical name retained; no saved recovered alias | TEXT | schema / event |
| event.type | Physical name retained; no saved recovered alias | TEXT | schema / event |
| event.notes | Physical name retained; no saved recovered alias | TEXT | schema / event |
| event.location | Physical name retained; no saved recovered alias | TEXT | schema / event |
| event.status | Physical name retained; no saved recovered alias | TEXT | schema / event |

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

## member_zip

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| member_zip.member_id | Physical name retained; no saved recovered alias | TEXT | schema / member_zip |
| member_zip.first_name | Physical name retained; no saved recovered alias | TEXT | schema / member_zip |
| member_zip.last_name | Physical name retained; no saved recovered alias | TEXT | schema / member_zip |
| member_zip.email | Physical name retained; no saved recovered alias | TEXT | schema / member_zip |
| member_zip.position | Physical name retained; no saved recovered alias | TEXT | schema / member_zip |
| member_zip.t_shirt_size | Physical name retained; no saved recovered alias | TEXT | schema / member_zip |
| member_zip.phone | Physical name retained; no saved recovered alias | TEXT | schema / member_zip |
| member_zip.zip | Physical name retained; no saved recovered alias | INTEGER | schema / member_zip |
| member_zip.link_to_major | Physical name retained; no saved recovered alias | TEXT | schema / member_zip |
| member_zip.zip_code | Physical name retained; no saved recovered alias | INTEGER | schema / member_zip |
| member_zip.type | Physical name retained; no saved recovered alias | TEXT | schema / member_zip |
| member_zip.city | Physical name retained; no saved recovered alias | TEXT | schema / member_zip |
| member_zip.county | Physical name retained; no saved recovered alias | TEXT | schema / member_zip |
| member_zip.state | Physical name retained; no saved recovered alias | TEXT | schema / member_zip |
| member_zip.short_state | Physical name retained; no saved recovered alias | TEXT | schema / member_zip |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

