# EvoSchema / evoschema::table_split::debit_card_specializing::1502 — Schema and business semantics

The saved catalogue for this database contains 7 tables, 23 physical columns, 0 relationships and 7 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## customers

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: c

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| customers.CustomerID | Physical name retained; no saved recovered alias | INTEGER | schema / customers |
| customers.Segment | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.Currency | Physical name retained; no saved recovered alias | TEXT | schema / customers |

## CustomerTransactions

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: ct

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| CustomerTransactions.TransactionID | Physical name retained; no saved recovered alias | INTEGER | schema / CustomerTransactions |
| CustomerTransactions.CustomerID | Physical name retained; no saved recovered alias | INTEGER | schema / CustomerTransactions |
| CustomerTransactions.CardID | Physical name retained; no saved recovered alias | INTEGER | schema / CustomerTransactions |

## gasstations

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: gs

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| gasstations.GasStationID | Physical name retained; no saved recovered alias | INTEGER | schema / gasstations |
| gasstations.ChainID | Physical name retained; no saved recovered alias | INTEGER | schema / gasstations |
| gasstations.Country | Physical name retained; no saved recovered alias | TEXT | schema / gasstations |
| gasstations.Segment | Physical name retained; no saved recovered alias | TEXT | schema / gasstations |

## GasStationTransactions

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: gst

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| GasStationTransactions.TransactionID | Physical name retained; no saved recovered alias | INTEGER | schema / GasStationTransactions |
| GasStationTransactions.GasStationID | Physical name retained; no saved recovered alias | INTEGER | schema / GasStationTransactions |
| GasStationTransactions.ProductID | Physical name retained; no saved recovered alias | INTEGER | schema / GasStationTransactions |

## products

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

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

