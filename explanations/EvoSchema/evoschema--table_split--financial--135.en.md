# EvoSchema / evoschema::table_split::financial::135 — Schema and business semantics

The saved catalogue for this database contains 10 tables, 57 physical columns, 0 relationships and 10 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## account

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| account.account_id | Physical name retained; no saved recovered alias | INTEGER | schema / account |
| account.district_id | Physical name retained; no saved recovered alias | INTEGER | schema / account |
| account.frequency | Physical name retained; no saved recovered alias | TEXT | schema / account |
| account.date | Physical name retained; no saved recovered alias | DATE | schema / account |

## account_reference

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| account_reference.trans_id | Physical name retained; no saved recovered alias | INTEGER | schema / account_reference |
| account_reference.account_id | Physical name retained; no saved recovered alias | INTEGER | schema / account_reference |

## bank_details

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| bank_details.trans_id | Physical name retained; no saved recovered alias | INTEGER | schema / bank_details |
| bank_details.bank | Physical name retained; no saved recovered alias | TEXT | schema / bank_details |
| bank_details.account | Physical name retained; no saved recovered alias | INTEGER | schema / bank_details |

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

## district

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| district.district_id | Physical name retained; no saved recovered alias | INTEGER | schema / district |
| district.A2 | Physical name retained; no saved recovered alias | TEXT | schema / district |
| district.A3 | Physical name retained; no saved recovered alias | TEXT | schema / district |
| district.A4 | Physical name retained; no saved recovered alias | TEXT | schema / district |
| district.A5 | Physical name retained; no saved recovered alias | TEXT | schema / district |
| district.A6 | Physical name retained; no saved recovered alias | TEXT | schema / district |
| district.A7 | Physical name retained; no saved recovered alias | TEXT | schema / district |
| district.A8 | Physical name retained; no saved recovered alias | INTEGER | schema / district |
| district.A9 | Physical name retained; no saved recovered alias | INTEGER | schema / district |
| district.A10 | Physical name retained; no saved recovered alias | REAL | schema / district |
| district.A11 | Physical name retained; no saved recovered alias | INTEGER | schema / district |
| district.A12 | Physical name retained; no saved recovered alias | REAL | schema / district |
| district.A13 | Physical name retained; no saved recovered alias | REAL | schema / district |
| district.A14 | Physical name retained; no saved recovered alias | INTEGER | schema / district |
| district.A15 | Physical name retained; no saved recovered alias | INTEGER | schema / district |
| district.A16 | Physical name retained; no saved recovered alias | INTEGER | schema / district |

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

## transaction_details

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| transaction_details.trans_id | Physical name retained; no saved recovered alias | INTEGER | schema / transaction_details |
| transaction_details.date | Physical name retained; no saved recovered alias | DATE | schema / transaction_details |
| transaction_details.type | Physical name retained; no saved recovered alias | TEXT | schema / transaction_details |
| transaction_details.operation | Physical name retained; no saved recovered alias | TEXT | schema / transaction_details |
| transaction_details.amount | Physical name retained; no saved recovered alias | INTEGER | schema / transaction_details |
| transaction_details.balance | Physical name retained; no saved recovered alias | INTEGER | schema / transaction_details |
| transaction_details.k_symbol | Physical name retained; no saved recovered alias | TEXT | schema / transaction_details |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

