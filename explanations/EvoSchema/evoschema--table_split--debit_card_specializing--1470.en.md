# EvoSchema / evoschema::table_split::debit_card_specializing::1470 — Schema and business semantics

The saved catalogue for this database contains 7 tables, 23 physical columns, 0 relationships and 7 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## customers

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| customers.CustomerID | Physical name retained; no saved recovered alias | INTEGER | schema / customers |
| customers.Segment | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.Currency | Physical name retained; no saved recovered alias | TEXT | schema / customers |

## products

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| products.ProductID | Physical name retained; no saved recovered alias | INTEGER | schema / products |
| products.Description | Physical name retained; no saved recovered alias | TEXT | schema / products |

## StationDetails

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: T1

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| StationDetails.GasStationID | Physical name retained; no saved recovered alias | INTEGER | schema / StationDetails |
| StationDetails.ChainID | Physical name retained; no saved recovered alias | INTEGER | schema / StationDetails |

## StationLocation

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: T2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| StationLocation.GasStationID | Physical name retained; no saved recovered alias | INTEGER | schema / StationLocation |
| StationLocation.Country | Physical name retained; no saved recovered alias | TEXT | schema / StationLocation |

## StationSegment

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: T3

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| StationSegment.GasStationID | Physical name retained; no saved recovered alias | INTEGER | schema / StationSegment |
| StationSegment.Segment | Physical name retained; no saved recovered alias | TEXT | schema / StationSegment |

## transactions_1k

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| transactions_1k.TransactionID | Physical name retained; no saved recovered alias | INTEGER | schema / transactions_1k |
| transactions_1k.Date | Physical name retained; no saved recovered alias | DATE | schema / transactions_1k |
| transactions_1k.Time | Physical name retained; no saved recovered alias | TEXT | schema / transactions_1k |
| transactions_1k.CustomerID | Physical name retained; no saved recovered alias | INTEGER | schema / transactions_1k |
| transactions_1k.CardID | Physical name retained; no saved recovered alias | INTEGER | schema / transactions_1k |
| transactions_1k.GasStationID | Physical name retained; no saved recovered alias | INTEGER | schema / transactions_1k |
| transactions_1k.ProductID | Physical name retained; no saved recovered alias | INTEGER | schema / transactions_1k |
| transactions_1k.Amount | Physical name retained; no saved recovered alias | INTEGER | schema / transactions_1k |
| transactions_1k.Price | Physical name retained; no saved recovered alias | REAL | schema / transactions_1k |

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

