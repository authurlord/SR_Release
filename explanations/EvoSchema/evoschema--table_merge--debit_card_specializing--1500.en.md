# EvoSchema / evoschema::table_merge::debit_card_specializing::1500 — Schema and business semantics

The saved catalogue for this database contains 4 tables, 20 physical columns, 0 relationships and 4 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## customers

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| customers.CustomerID | Physical name retained; no saved recovered alias | INTEGER | schema / customers |
| customers.Segment | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.Currency | Physical name retained; no saved recovered alias | TEXT | schema / customers |

## gasstations

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| gasstations.GasStationID | Physical name retained; no saved recovered alias | INTEGER | schema / gasstations |
| gasstations.ChainID | Physical name retained; no saved recovered alias | INTEGER | schema / gasstations |
| gasstations.Country | Physical name retained; no saved recovered alias | TEXT | schema / gasstations |
| gasstations.Segment | Physical name retained; no saved recovered alias | TEXT | schema / gasstations |

## merged_transactions_products

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| merged_transactions_products.TransactionID | Physical name retained; no saved recovered alias | INTEGER | schema / merged_transactions_products |
| merged_transactions_products.Date | Physical name retained; no saved recovered alias | DATE | schema / merged_transactions_products |
| merged_transactions_products.Time | Physical name retained; no saved recovered alias | TEXT | schema / merged_transactions_products |
| merged_transactions_products.CustomerID | Physical name retained; no saved recovered alias | INTEGER | schema / merged_transactions_products |
| merged_transactions_products.CardID | Physical name retained; no saved recovered alias | INTEGER | schema / merged_transactions_products |
| merged_transactions_products.GasStationID | Physical name retained; no saved recovered alias | INTEGER | schema / merged_transactions_products |
| merged_transactions_products.ProductID | Physical name retained; no saved recovered alias | INTEGER | schema / merged_transactions_products |
| merged_transactions_products.Amount | Physical name retained; no saved recovered alias | INTEGER | schema / merged_transactions_products |
| merged_transactions_products.Price | Physical name retained; no saved recovered alias | REAL | schema / merged_transactions_products |
| merged_transactions_products.Description | Physical name retained; no saved recovered alias | TEXT | schema / merged_transactions_products |

## yearmonth

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| yearmonth.CustomerID | Physical name retained; no saved recovered alias | INTEGER | schema / yearmonth |
| yearmonth.Date | Physical name retained; no saved recovered alias | TEXT | schema / yearmonth |
| yearmonth.Consumption | Physical name retained; no saved recovered alias | REAL | schema / yearmonth |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

