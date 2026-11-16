# BIRD-Dev / debit_card_specializing — Schema 与业务口径解释

该数据库的存档目录包含 5 张表、21 个物理列、1 条关系，以及 5 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## customers

Stores information about customers, including their unique identifier, market segment, and preferred currency.

恢复表名: customers / customer / clients / accounts
SQL表别名: c

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| customers.XCL_001 | customer id / customer identifier / client id / account number | integer | schema / customers |
| customers.XCL_002 | segment / market segment / customer segment / segment code | text | schema / customers |
| customers.XCL_003 | currency / currency code / transaction currency | text | schema / customers |

## gasstations

Stores information about gas stations including their chain, country, and market segment.

恢复表名: gasstations / gas stations / fuel stations / petrol stations / gas station locations
SQL表别名: g

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| gasstations.XCL_004 | gas station id / gas station identifier / station identifier / gas station number / station ID | integer | schema / gasstations |
| gasstations.XCL_005 | chain id / chain identifier / brand identifier / chain number / brand ID | integer | schema / gasstations |
| gasstations.XCL_006 | country / nation / country code | text | schema / gasstations |
| gasstations.XCL_007 | segment / market segment / station type / category / class | text | schema / gasstations |

## products

This table stores information about products, including their unique identifiers and descriptions.

恢复表名: products / product catalog / product list
SQL表别名: p

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| products.XCL_008 | product id / product identifier / product number / product code | integer | schema / products |
| products.XCL_009 | description / product description / product name / product type / product category | text | schema / products |

## transactions_1k

Records of debit card transactions including purchase details, customer and card information, and amounts.

恢复表名: transactions 1k / transactions / debit card transactions / purchase transactions / transaction records
SQL表别名: t

| Physical | 恢复名称 | Type | 来源 |
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

恢复表名: yearmonth / year_month / monthly_usage / period_consumption
SQL表别名: T1, y, ym

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| yearmonth.XCL_019 | customer id / customer identifier / customer_id / client id / account number | integer | schema / yearmonth |
| yearmonth.XCL_020 | date / year_month / month / period / reporting month / statement date | text | schema / yearmonth |
| yearmonth.XCL_021 | consumption / usage / amount / consumption amount / monthly usage / spending | real | schema / yearmonth |

## 表关系与连接依据

- customers.XCL_001 ↔ yearmonth.XCL_019; declared_or_materialized_relationship

## 业务口径、总体与粒度


## 增量维护事件

