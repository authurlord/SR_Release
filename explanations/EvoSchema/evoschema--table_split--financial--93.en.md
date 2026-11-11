# EvoSchema / evoschema::table_split::financial::93 — Schema and business semantics

The saved catalogue for this database contains 10 tables, 57 physical columns, 0 relationships and 10 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## account

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: a

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| account.account_id | Physical name retained; no saved recovered alias | INTEGER | schema / account |
| account.district_id | Physical name retained; no saved recovered alias | INTEGER | schema / account |
| account.frequency | Physical name retained; no saved recovered alias | TEXT | schema / account |
| account.date | Physical name retained; no saved recovered alias | DATE | schema / account |

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
SQL table aliases: c

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| client.client_id | Physical name retained; no saved recovered alias | INTEGER | schema / client |
| client.gender | Physical name retained; no saved recovered alias | TEXT | schema / client |
| client.birth_date | Physical name retained; no saved recovered alias | DATE | schema / client |
| client.district_id | Physical name retained; no saved recovered alias | INTEGER | schema / client |

## disp

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: dp

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| disp.disp_id | Physical name retained; no saved recovered alias | INTEGER | schema / disp |
| disp.client_id | Physical name retained; no saved recovered alias | INTEGER | schema / disp |
| disp.account_id | Physical name retained; no saved recovered alias | INTEGER | schema / disp |
| disp.type | Physical name retained; no saved recovered alias | TEXT | schema / disp |

## district_info

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: d

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| district_info.district_id | Physical name retained; no saved recovered alias | INTEGER | schema / district_info |
| district_info.A2 | Physical name retained; no saved recovered alias | TEXT | schema / district_info |
| district_info.A3 | Physical name retained; no saved recovered alias | TEXT | schema / district_info |

## district_numeric

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| district_numeric.district_id | Physical name retained; no saved recovered alias | INTEGER | schema / district_numeric |
| district_numeric.A8 | Physical name retained; no saved recovered alias | INTEGER | schema / district_numeric |
| district_numeric.A9 | Physical name retained; no saved recovered alias | INTEGER | schema / district_numeric |
| district_numeric.A11 | Physical name retained; no saved recovered alias | INTEGER | schema / district_numeric |
| district_numeric.A14 | Physical name retained; no saved recovered alias | INTEGER | schema / district_numeric |
| district_numeric.A15 | Physical name retained; no saved recovered alias | INTEGER | schema / district_numeric |
| district_numeric.A16 | Physical name retained; no saved recovered alias | INTEGER | schema / district_numeric |

## district_real

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| district_real.district_id | Physical name retained; no saved recovered alias | INTEGER | schema / district_real |
| district_real.A4 | Physical name retained; no saved recovered alias | TEXT | schema / district_real |
| district_real.A5 | Physical name retained; no saved recovered alias | TEXT | schema / district_real |
| district_real.A6 | Physical name retained; no saved recovered alias | TEXT | schema / district_real |
| district_real.A7 | Physical name retained; no saved recovered alias | TEXT | schema / district_real |
| district_real.A10 | Physical name retained; no saved recovered alias | REAL | schema / district_real |
| district_real.A12 | Physical name retained; no saved recovered alias | REAL | schema / district_real |
| district_real.A13 | Physical name retained; no saved recovered alias | REAL | schema / district_real |

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
SQL table aliases: t

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

