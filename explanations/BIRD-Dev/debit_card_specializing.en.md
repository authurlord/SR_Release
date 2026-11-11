# BIRD-Dev / debit_card_specializing — Schema and business semantics

The saved catalogue for this database contains 5 tables, 21 physical columns, 1 relationships and 5 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## customers

Stores information about customers, including their unique identifier, market segment, and preferred currency.

Recovered table names: customers / customer / clients / accounts
SQL table aliases: c

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| customers.XCL_001 | customer id / customer identifier / client id / account number | integer | schema / customers |
| customers.XCL_002 | segment / market segment / customer segment / segment code | text | schema / customers |
| customers.XCL_003 | currency / currency code / transaction currency | text | schema / customers |

## gasstations

Stores information about gas stations including their chain, country, and market segment.

Recovered table names: gasstations / gas stations / fuel stations / petrol stations / gas station locations
SQL table aliases: g

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| gasstations.XCL_004 | gas station id / gas station identifier / station identifier / gas station number / station ID | integer | schema / gasstations |
| gasstations.XCL_005 | chain id / chain identifier / brand identifier / chain number / brand ID | integer | schema / gasstations |
| gasstations.XCL_006 | country / nation / country code | text | schema / gasstations |
| gasstations.XCL_007 | segment / market segment / station type / category / class | text | schema / gasstations |

## products

This table stores information about products, including their unique identifiers and descriptions.

Recovered table names: products / product catalog / product list
SQL table aliases: p

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| products.XCL_008 | product id / product identifier / product number / product code | integer | schema / products |
| products.XCL_009 | description / product description / product name / product type / product category | text | schema / products |

## transactions_1k

Records of debit card transactions including purchase details, customer and card information, and amounts.

Recovered table names: transactions 1k / transactions / debit card transactions / purchase transactions / transaction records
SQL table aliases: t

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| transactions_1k.XCL_010 | transaction id / transaction identifier / transaction number / txn id / txn number / id | integer | schema / transactions_1k |
| transactions_1k.XCL_011 | date / transaction date / purchase date / date of transaction / date of purchase / txn date | date | schema / transactions_1k |
| transactions_1k.XCL_012 | time / transaction time / purchase time / time of transaction / time of purchase / txn time | text | schema / transactions_1k |
| transactions_1k.XCL_013 | customer id / customer identifier / customer number / client id / client number | integer | schema / transactions_1k |
| transactions_1k.XCL_014 | card id / card identifier / card number / debit card id / debit card number | integer | schema / transactions_1k |
| transactions_1k.XCL_015 | gas station id / gas station identifier / station id / gas station number / station number / fuel station id | integer | schema / transactions_1k |
| transactions_1k.XCL_016 | product id / product identifier / product number / item id / item number | integer | schema / transactions_1k |
| transactions_1k.XCL_017 | amount / quantity / number of items / units / purchase quantity / item count | integer | schema / transactions_1k |
| transactions_1k.XCL_018 | price / total price / transaction amount / purchase amount / cost / total cost / price paid | real | schema / transactions_1k |

## yearmonth

Stores monthly consumption data per customer, keyed by customer ID and date (YYYYMM format).

Recovered table names: yearmonth / year_month / monthly_usage / period_consumption
SQL table aliases: T1, y, ym

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| yearmonth.XCL_019 | customer id / customer identifier / customer_id / client id / account number | integer | schema / yearmonth |
| yearmonth.XCL_020 | date / year_month / month / period / reporting month / statement date | text | schema / yearmonth |
| yearmonth.XCL_021 | consumption / usage / amount / consumption amount / monthly usage / spending | real | schema / yearmonth |

## Relationships and join evidence

- customers.XCL_001 ↔ yearmonth.XCL_019; declared_or_materialized_relationship

## Business definitions, population and grain


## Incremental maintenance events

