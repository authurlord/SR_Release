# EvoSchema / evoschema::table_split::student_club::1408 — Schema and business semantics

The saved catalogue for this database contains 10 tables, 50 physical columns, 0 relationships and 10 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

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

## ExpenseApproval

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| ExpenseApproval.expense_id | Physical name retained; no saved recovered alias | TEXT | schema / ExpenseApproval |
| ExpenseApproval.approved | Physical name retained; no saved recovered alias | TEXT | schema / ExpenseApproval |

## ExpenseDetails

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| ExpenseDetails.expense_id | Physical name retained; no saved recovered alias | TEXT | schema / ExpenseDetails |
| ExpenseDetails.expense_description | Physical name retained; no saved recovered alias | TEXT | schema / ExpenseDetails |
| ExpenseDetails.expense_date | Physical name retained; no saved recovered alias | TEXT | schema / ExpenseDetails |
| ExpenseDetails.cost | Physical name retained; no saved recovered alias | REAL | schema / ExpenseDetails |

## ExpenseLinks

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| ExpenseLinks.expense_id | Physical name retained; no saved recovered alias | TEXT | schema / ExpenseLinks |
| ExpenseLinks.link_to_member | Physical name retained; no saved recovered alias | TEXT | schema / ExpenseLinks |
| ExpenseLinks.link_to_budget | Physical name retained; no saved recovered alias | TEXT | schema / ExpenseLinks |

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

