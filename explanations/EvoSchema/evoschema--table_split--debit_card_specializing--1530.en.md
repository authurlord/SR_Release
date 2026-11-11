# EvoSchema / evoschema::table_split::debit_card_specializing::1530 — Schema and business semantics

The saved catalogue for this database contains 7 tables, 23 physical columns, 0 relationships and 7 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## CustomerInfo

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| CustomerInfo.TransactionID | Physical name retained; no saved recovered alias | INTEGER | schema / CustomerInfo |
| CustomerInfo.CustomerID | Physical name retained; no saved recovered alias | INTEGER | schema / CustomerInfo |
| CustomerInfo.CardID | Physical name retained; no saved recovered alias | INTEGER | schema / CustomerInfo |

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

## ProductInfo

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: pi

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| ProductInfo.TransactionID | Physical name retained; no saved recovered alias | INTEGER | schema / ProductInfo |
| ProductInfo.GasStationID | Physical name retained; no saved recovered alias | INTEGER | schema / ProductInfo |
| ProductInfo.ProductID | Physical name retained; no saved recovered alias | INTEGER | schema / ProductInfo |

## products

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: p

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| products.ProductID | Physical name retained; no saved recovered alias | INTEGER | schema / products |
| products.Description | Physical name retained; no saved recovered alias | TEXT | schema / products |

## TransactionDetails

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| TransactionDetails.TransactionID | Physical name retained; no saved recovered alias | INTEGER | schema / TransactionDetails |
| TransactionDetails.Date | Physical name retained; no saved recovered alias | DATE | schema / TransactionDetails |
| TransactionDetails.Time | Physical name retained; no saved recovered alias | TEXT | schema / TransactionDetails |
| TransactionDetails.Amount | Physical name retained; no saved recovered alias | INTEGER | schema / TransactionDetails |
| TransactionDetails.Price | Physical name retained; no saved recovered alias | REAL | schema / TransactionDetails |

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

