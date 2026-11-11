# EvoSchema / evoschema::table_merge::financial::152 — Schema and business semantics

The saved catalogue for this database contains 7 tables, 54 physical columns, 0 relationships and 7 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## account_district

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: T1, T2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| account_district.account_id | Physical name retained; no saved recovered alias | INTEGER | schema / account_district |
| account_district.district_id | Physical name retained; no saved recovered alias | INTEGER | schema / account_district |
| account_district.frequency | Physical name retained; no saved recovered alias | TEXT | schema / account_district |
| account_district.date | Physical name retained; no saved recovered alias | DATE | schema / account_district |
| account_district.A2 | Physical name retained; no saved recovered alias | TEXT | schema / account_district |
| account_district.A3 | Physical name retained; no saved recovered alias | TEXT | schema / account_district |
| account_district.A4 | Physical name retained; no saved recovered alias | TEXT | schema / account_district |
| account_district.A5 | Physical name retained; no saved recovered alias | TEXT | schema / account_district |
| account_district.A6 | Physical name retained; no saved recovered alias | TEXT | schema / account_district |
| account_district.A7 | Physical name retained; no saved recovered alias | TEXT | schema / account_district |
| account_district.A8 | Physical name retained; no saved recovered alias | INTEGER | schema / account_district |
| account_district.A9 | Physical name retained; no saved recovered alias | INTEGER | schema / account_district |
| account_district.A10 | Physical name retained; no saved recovered alias | REAL | schema / account_district |
| account_district.A11 | Physical name retained; no saved recovered alias | INTEGER | schema / account_district |
| account_district.A12 | Physical name retained; no saved recovered alias | REAL | schema / account_district |
| account_district.A13 | Physical name retained; no saved recovered alias | REAL | schema / account_district |
| account_district.A14 | Physical name retained; no saved recovered alias | INTEGER | schema / account_district |
| account_district.A15 | Physical name retained; no saved recovered alias | INTEGER | schema / account_district |
| account_district.A16 | Physical name retained; no saved recovered alias | INTEGER | schema / account_district |

## card

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| card.card_id | Physical name retained; no saved recovered alias | INTEGER | schema / card |
| card.disp_id | Physical name retained; no saved recovered alias | INTEGER | schema / card |
| card.type | Physical name retained; no saved recovered alias | TEXT | schema / card |
| card.issued | Physical name retained; no saved recovered alias | DATE | schema / card |

## client

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| client.client_id | Physical name retained; no saved recovered alias | INTEGER | schema / client |
| client.gender | Physical name retained; no saved recovered alias | TEXT | schema / client |
| client.birth_date | Physical name retained; no saved recovered alias | DATE | schema / client |
| client.district_id | Physical name retained; no saved recovered alias | INTEGER | schema / client |

## disp

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| disp.disp_id | Physical name retained; no saved recovered alias | INTEGER | schema / disp |
| disp.client_id | Physical name retained; no saved recovered alias | INTEGER | schema / disp |
| disp.account_id | Physical name retained; no saved recovered alias | INTEGER | schema / disp |
| disp.type | Physical name retained; no saved recovered alias | TEXT | schema / disp |

## loan

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| loan.loan_id | Physical name retained; no saved recovered alias | INTEGER | schema / loan |
| loan.account_id | Physical name retained; no saved recovered alias | INTEGER | schema / loan |
| loan.date | Physical name retained; no saved recovered alias | DATE | schema / loan |
| loan.amount | Physical name retained; no saved recovered alias | INTEGER | schema / loan |
| loan.duration | Physical name retained; no saved recovered alias | INTEGER | schema / loan |
| loan.payments | Physical name retained; no saved recovered alias | REAL | schema / loan |
| loan.status | Physical name retained; no saved recovered alias | TEXT | schema / loan |

## order

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| order.order_id | Physical name retained; no saved recovered alias | INTEGER | schema / order |
| order.account_id | Physical name retained; no saved recovered alias | INTEGER | schema / order |
| order.bank_to | Physical name retained; no saved recovered alias | TEXT | schema / order |
| order.account_to | Physical name retained; no saved recovered alias | INTEGER | schema / order |
| order.amount | Physical name retained; no saved recovered alias | REAL | schema / order |
| order.k_symbol | Physical name retained; no saved recovered alias | TEXT | schema / order |

## trans

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| trans.trans_id | Physical name retained; no saved recovered alias | INTEGER | schema / trans |
| trans.account_id | Physical name retained; no saved recovered alias | INTEGER | schema / trans |
| trans.date | Physical name retained; no saved recovered alias | DATE | schema / trans |
| trans.type | Physical name retained; no saved recovered alias | TEXT | schema / trans |
| trans.operation | Physical name retained; no saved recovered alias | TEXT | schema / trans |
| trans.amount | Physical name retained; no saved recovered alias | INTEGER | schema / trans |
| trans.balance | Physical name retained; no saved recovered alias | INTEGER | schema / trans |
| trans.k_symbol | Physical name retained; no saved recovered alias | TEXT | schema / trans |
| trans.bank | Physical name retained; no saved recovered alias | TEXT | schema / trans |
| trans.account | Physical name retained; no saved recovered alias | INTEGER | schema / trans |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

