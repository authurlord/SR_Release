# BIRD-Mini / financial — Schema and business semantics

The saved catalogue for this database contains 8 tables, 55 physical columns, 8 relationships and 8 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## account

Stores information about bank accounts, including their creation date, frequency of statement issuance, and links to districts and transactions.

Recovered table names: account / accounts / bank accounts / customer accounts
SQL table aliases: a

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| account.XCL_001 | account id / account identifier / account number / account key | integer | schema / account |
| account.XCL_002 | district id / district identifier / district number / branch district / region code | integer | schema / account |
| account.XCL_003 | frequency / statement frequency / issuance frequency / billing cycle / payment frequency | text | schema / account |
| account.XCL_004 | date / account creation date / opening date / account start date / established date | date | schema / account |

## card

Stores information about bank cards (credit, debit, etc.) issued to clients, including card type and issue date.

Recovered table names: card / cards / credit cards / debit cards / bank cards
SQL table aliases: k

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| card.XCL_005 | card id / card identifier / card number / card key | integer | schema / card |
| card.XCL_006 | disp id / disp identifier / disposition identifier / client-card link ID / cardholder ID | integer | schema / card |
| card.XCL_007 | type / card type / card category / card class / card level | text | schema / card |
| card.XCL_008 | issued / issue date / card issue date / date issued / issuance date | date | schema / card |

## client

Stores personal information about each client, including unique identifier, gender, birth date, and the district where the client resides.

Recovered table names: client / clients / customer / customers / account holder / account holders
SQL table aliases: c

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| client.XCL_009 | client id / client identifier / client number / customer id / customer identifier / customer number / account holder id | integer | schema / client |
| client.XCL_010 | gender / sex / gender identity / client gender / customer gender | text | schema / client |
| client.XCL_011 | birth date / date of birth / birthday / client birth date / customer birth date / date born | date | schema / client |
| client.XCL_012 | district id / district identifier / district number / client district / customer district / residence district id | integer | schema / client |

## disp

Links clients to accounts and defines the type of relationship (owner or disponent) each client has with an account.

Recovered table names: disp / disposition / account_disposition / client_disposition / disp_table
SQL table aliases: d, d1

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| disp.XCL_013 | disp id / disp identifier / disposition_id / disp_id / disposition_identifier / disp_identifier | integer | schema / disp |
| disp.XCL_014 | client id / client identifier / client_id / customer_id / client_identifier / customer_identifier | integer | schema / disp |
| disp.XCL_015 | account id / account identifier / account_id / account_identifier / account_number | integer | schema / disp |
| disp.XCL_016 | type / disposition_type / relationship_type / client_role / account_role | text | schema / disp |

## district

Geographic and demographic information about districts, including population, crime rates, and economic indicators.

Recovered table names: district / districts / region / area
SQL table aliases: d, d2, di, dist

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| district.XCL_017 | district id / district identifier / region id / area id | integer | schema / district |
| district.XCL_018 | a2 / district name / district / region name / area name | text | schema / district |
| district.XCL_019 | a3 / region / area / geographic region / district region | text | schema / district |
| district.XCL_020 | a4 / population / number of inhabitants / total residents / people count | text | schema / district |
| district.XCL_021 | a5 / number of municipalities with population less than 499 / small municipalities count / towns under 500 | text | schema / district |
| district.XCL_022 | a6 / number of municipalities with population 500-1999 / medium municipalities count / towns 500 to 1999 | text | schema / district |
| district.XCL_023 | a7 / number of municipalities with population 2000-9999 / larger municipalities count / towns 2000 to 9999 | text | schema / district |
| district.XCL_024 | a8 / number of municipalities with population greater than 10000 / large municipalities count / cities over 10000 | integer | schema / district |
| district.XCL_025 | a9 / number of cities / city count / urban centers | integer | schema / district |
| district.XCL_026 | a10 / ratio of urban inhabitants / urban population percentage / urbanization rate | real | schema / district |
| district.XCL_027 | a11 / average salary / mean income / average wage / typical earnings | integer | schema / district |
| district.XCL_028 | a12 / unemployment rate 1995 / jobless rate 1995 / unemployment percentage 1995 | real | schema / district |
| district.XCL_029 | a13 / unemployment rate 1996 / jobless rate 1996 / unemployment percentage 1996 | real | schema / district |
| district.XCL_030 | a14 / number of entrepreneurs per 1000 inhabitants / entrepreneurs per thousand / business owners per 1000 | integer | schema / district |
| district.XCL_031 | a15 / number of crimes 1995 / crime count 1995 / total crimes 1995 | integer | schema / district |
| district.XCL_032 | a16 / number of crimes 1996 / crime count 1996 / total crimes 1996 | integer | schema / district |

## loan

This table stores information about loans issued to accounts, including loan identifiers, associated account, disbursement date, amount, duration, payment amount, and status.

Recovered table names: loan / loans / loan records / loan applications / borrowing records
SQL table aliases: l

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| loan.XCL_033 | loan id / loan identifier / loan number / loan code | integer | schema / loan |
| loan.XCL_034 | account id / account identifier / account number / account code | integer | schema / loan |
| loan.XCL_035 | date / loan date / disbursement date / loan start date / issue date / date of loan | date | schema / loan |
| loan.XCL_036 | amount / loan amount / principal amount / loan value / borrowed amount / loan sum | integer | schema / loan |
| loan.XCL_037 | duration / loan duration / loan term / repayment period / loan length / term in months | integer | schema / loan |
| loan.XCL_038 | payments / monthly payment / installment amount / payment per month / loan payment / repayment amount | real | schema / loan |
| loan.XCL_039 | status / loan status / loan state / status code / loan condition / repayment status | text | schema / loan |

## order

Records payment orders initiated from accounts, including destination bank and account, amount, and transaction category.

Recovered table names: order / orders / payment orders / transaction orders
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| order.XCL_040 | order id / order identifier / order number / payment order ID | integer | schema / order |
| order.XCL_041 | account id / account identifier / source account / account number / owner account | integer | schema / order |
| order.XCL_042 | bank to / destination bank / recipient bank / target bank / bank code | text | schema / order |
| order.XCL_043 | account to / destination account / recipient account / target account / beneficiary account | integer | schema / order |
| order.XCL_044 | amount / order amount / payment amount / transaction amount / value | real | schema / order |
| order.XCL_045 | k symbol / transaction type / payment category / order symbol / transaction code | text | schema / order |

## trans

Records all financial transactions for bank accounts, including deposits, withdrawals, transfers, and payments.

Recovered table names: trans / transactions / transaction records / financial transactions
SQL table aliases: t

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| trans.XCL_046 | trans id / trans identifier / transaction id / transaction number / txn id / tx id / transaction identifier | integer | schema / trans |
| trans.XCL_047 | account id / account identifier / account number / customer account id | integer | schema / trans |
| trans.XCL_048 | date / transaction date / txn date / posting date / date of transaction | date | schema / trans |
| trans.XCL_049 | type / transaction type / txn type / credit debit indicator / direction | text | schema / trans |
| trans.XCL_050 | operation / operation type / transaction operation / operation code / transaction category | text | schema / trans |
| trans.XCL_051 | amount / transaction amount / txn amount / value / sum / money amount | integer | schema / trans |
| trans.XCL_052 | balance / account balance / balance after transaction / post-transaction balance / running balance | integer | schema / trans |
| trans.XCL_053 | k symbol / symbol / transaction symbol / payment symbol / category code | text | schema / trans |
| trans.XCL_054 | bank / bank code / bank identifier / bank abbreviation / bank name | text | schema / trans |
| trans.XCL_055 | account / counterparty account / other account / partner account / account number | integer | schema / trans |

## Relationships and join evidence

- account.XCL_001 ↔ disp.XCL_015; declared_or_materialized_relationship
- account.XCL_001 ↔ loan.XCL_034; declared_or_materialized_relationship
- account.XCL_001 ↔ order.XCL_041; declared_or_materialized_relationship
- account.XCL_001 ↔ trans.XCL_047; declared_or_materialized_relationship
- account.XCL_002 ↔ district.XCL_017; declared_or_materialized_relationship
- card.XCL_006 ↔ disp.XCL_013; declared_or_materialized_relationship
- client.XCL_009 ↔ disp.XCL_014; declared_or_materialized_relationship
- client.XCL_012 ↔ district.XCL_017; declared_or_materialized_relationship

## Business definitions, population and grain


## Incremental maintenance events

