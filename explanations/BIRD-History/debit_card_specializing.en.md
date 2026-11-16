# BIRD-History / debit_card_specializing — Schema and business semantics

The saved catalogue for this database contains 5 tables, 21 physical columns, 10 relationships and 64 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## customers

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: C, T1, T2, T3, T5, c, c2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| customers.XCL_001 | customer_id | unknown | bird_dev:1480, bird_dev:1478, bird_dev:1490, bird_dev:1474, bird_dev:1477, bird_dev:1517, bird_dev:1492, bird_dev:1522 |
| customers.XCL_002 | segment | unknown | bird_dev:1480, bird_dev:1478, bird_dev:1490, bird_dev:1517, bird_dev:1492, bird_dev:1515, bird_dev:1496, bird_dev:1481 |
| customers.XCL_003 | currency | unknown | bird_dev:1474, bird_dev:1477, bird_dev:1492, bird_dev:1522, bird_dev:1511, bird_dev:1503, bird_dev:1505, bird_dev:1502 |

## gasstations

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: G, T2, T3, T4, T5, g, gs

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| gasstations.XCL_004 | gasstation_id | unknown | bird_dev:1519, bird_dev:1524, bird_dev:1470, bird_dev:1529, bird_dev:1523, bird_dev:1507, bird_dev:1521, bird_dev:1518 |
| gasstations.XCL_005 | chain_id | unknown | bird_dev:1507, bird_dev:1502 |
| gasstations.XCL_006 | country | unknown | bird_dev:1524, bird_dev:1470, bird_dev:1523, bird_dev:1528, bird_dev:1521, bird_dev:1518, bird_dev:1508, bird_dev:1506 |
| gasstations.XCL_007 | segment | unknown | bird_dev:1470, bird_dev:1528, bird_dev:1484, bird_dev:1491, bird_dev:1494 |

## products

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: P, T2, T3, p

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| products.XCL_008 | product_id | unknown | bird_dev:1506, bird_dev:1503, bird_dev:1500, bird_dev:1530 |
| products.XCL_009 | product_name | unknown | bird_dev:1506, bird_dev:1503, bird_dev:1500, bird_dev:1530 |

## transactions_1k

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: T, T1, T2, T3, T4, t, t2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| transactions_1k.XCL_010 | transaction_id | unknown | bird_dev:1521, bird_dev:1508, bird_dev:1509, bird_dev:1516 |
| transactions_1k.XCL_011 | transaction_date | unknown | bird_dev:1519, bird_dev:1524, bird_dev:1520, bird_dev:1521, bird_dev:1518, bird_dev:1515, bird_dev:1504, bird_dev:1513 |
| transactions_1k.XCL_012 | transaction_time | unknown | bird_dev:1519, bird_dev:1507, bird_dev:1521, bird_dev:1518, bird_dev:1515, bird_dev:1513, bird_dev:1514, bird_dev:1516 |
| transactions_1k.XCL_013 | customer_id | unknown | bird_dev:1529, bird_dev:1520, bird_dev:1517, bird_dev:1511, bird_dev:1503, bird_dev:1515, bird_dev:1533, bird_dev:1502 |
| transactions_1k.XCL_014 | card_id | unknown | bird_dev:1523 |
| transactions_1k.XCL_015 | gas_station_id | unknown | bird_dev:1519, bird_dev:1524, bird_dev:1529, bird_dev:1523, bird_dev:1507, bird_dev:1521, bird_dev:1527, bird_dev:1518 |
| transactions_1k.XCL_016 | product_id | unknown | bird_dev:1519, bird_dev:1506, bird_dev:1503, bird_dev:1533, bird_dev:1500, bird_dev:1532, bird_dev:1530 |
| transactions_1k.XCL_017 | quantity | unknown | bird_dev:1533, bird_dev:1504, bird_dev:1530, bird_dev:1531 |
| transactions_1k.XCL_018 | total_amount | unknown | bird_dev:1524, bird_dev:1529, bird_dev:1520, bird_dev:1527, bird_dev:1508, bird_dev:1511, bird_dev:1510, bird_dev:1533 |

## yearmonth

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: T1, T2, T3, T4, T5, T6, Y, YM, y, ym, ym2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| yearmonth.XCL_019 | customer_id | unknown | bird_dev:1480, bird_dev:1478, bird_dev:1529, bird_dev:1520, bird_dev:1490, bird_dev:1474, bird_dev:1493, bird_dev:1477 |
| yearmonth.XCL_020 | year_month | unknown | bird_dev:1480, bird_dev:1529, bird_dev:1520, bird_dev:1474, bird_dev:1493, bird_dev:1477, bird_dev:1485, bird_dev:1522 |
| yearmonth.XCL_021 | monthly_consumption | unknown | bird_dev:1480, bird_dev:1478, bird_dev:1520, bird_dev:1490, bird_dev:1474, bird_dev:1493, bird_dev:1477, bird_dev:1485 |

## Relationships and join evidence

- customers.XCL_001 ↔ transactions_1k.XCL_013; target_disjoint_historical_join
- customers.XCL_001 ↔ yearmonth.XCL_019; target_disjoint_historical_join
- gasstations.XCL_004 ↔ transactions_1k.XCL_015; target_disjoint_historical_join
- products.XCL_008 ↔ transactions_1k.XCL_016; target_disjoint_historical_join
- transactions_1k.XCL_013 ↔ yearmonth.XCL_019; target_disjoint_historical_join
- customers.XCL_001 ↔ transactions_1k.XCL_013; sql_workload_observed_join
- customers.XCL_001 ↔ yearmonth.XCL_019; sql_workload_observed_join
- gasstations.XCL_004 ↔ transactions_1k.XCL_015; sql_workload_observed_join
- products.XCL_008 ↔ transactions_1k.XCL_016; sql_workload_observed_join
- transactions_1k.XCL_013 ↔ yearmonth.XCL_019; sql_workload_observed_join

## Business definitions, population and grain

### A full SQL program that joins customers and yearmonth tables. It filters for customers with XCL_003='CZK', yearmonth XCL_020 between 201301 and 201312

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(IIF(T1.\"XCL_002\" = 'SME', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\") - CAST(SUM(IIF(T1.\"XCL_002\" = 'LAM', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\"), CAST(SUM(IIF(T1.\"XCL_002\" = 'LAM', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\") - CAST(SUM(IIF(T1.\"XCL_002\" = 'KAM', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\"), CAST(SUM(IIF(T1.\"XCL_002\" = 'KAM', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\") - CAST(SUM(IIF(T1.\"XCL_002\" = 'SME', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\") FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_003\" = 'CZK' AND T2.\"XCL_021\" = (SELECT MIN(\"XCL_021\") FROM yearmonth) AND T2.\"XCL_020\" BETWEEN 201301 AND 201312",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1481"
  ]
}
```

### Full SQL program that joins customers and yearmonth on customer ID, filters for CZK currency and 2011 dates, groups by customer, orders by the sum of 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_003\" = 'CZK' AND T2.\"XCL_020\" BETWEEN 201101 AND 201112 GROUP BY T1.\"XCL_001\" ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1474"
  ]
}
```

### Filtered XCL_021 Sum Query

```json
{
  "kind": "program",
  "formula": "SELECT SUM(\"XCL_021\") FROM yearmonth WHERE \"XCL_019\" = 6 AND \"XCL_020\" BETWEEN '201308' AND '201311'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1483"
  ]
}
```

### Filtered Transaction-YearMonth Join

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_013\", T2.\"XCL_020\", T2.\"XCL_021\" FROM transactions_1k AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_013\" = T2.\"XCL_019\" WHERE T1.\"XCL_011\" = '2012-08-24' AND T1.\"XCL_018\" = 124.05 AND T2.\"XCL_020\" = '201201'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1520"
  ]
}
```

### A query joining transactions_1k and gasstations on XCL_015 = XCL_004, filtering transactions by XCL_014 = '667467', and returning the corresponding ga

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_006\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_014\" = '667467'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1523"
  ]
}
```

### Full SQL program that joins 'customers' (T1) and 'yearmonth' (T2) on 'XCL_001' = 'XCL_019'. It filters for the specific month '201305' and customer ty

```json
{
  "kind": "program",
  "formula": "SELECT SUM(T2.\"XCL_021\") FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T2.\"XCL_020\" = '201305' AND T1.\"XCL_002\" = 'KAM'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1489"
  ]
}
```

### Full SQL program that joins 'transactions_1k' (T1) with 'gasstations' (T2) on 'XCL_015' = 'XCL_004'. It filters for gas stations where 'XCL_006' is 'C

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_010\") FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T2.\"XCL_006\" = 'CZE' AND T1.\"XCL_018\" > 1000",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1508"
  ]
}
```

### Filtered join count query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(*) FROM yearmonth AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_019\" = T2.\"XCL_001\" WHERE T2.\"XCL_003\" = 'EUR' AND T1.\"XCL_021\" > 1000.00",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1505"
  ]
}
```

### Executes a SELECT statement on the 'gasstations' table, filtering for records where 'XCL_006' is 'SVK'. It computes the ratio of 'Premium' values in '

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(IIF(\"XCL_007\" = 'Premium', 1, 0)) AS REAL) * 100 / COUNT(\"XCL_004\") FROM gasstations WHERE \"XCL_006\" = 'SVK'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1494"
  ]
}
```

### A full SQL program that joins 'transactions_1k' (T1) with 'customers' (T2) on 'XCL_013' = 'XCL_001'. It filters transactions by specific date and time

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_002\" FROM transactions_1k AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_013\" = T2.\"XCL_001\" WHERE T1.\"XCL_011\" = '2012-08-23' AND T1.\"XCL_012\" = '21:20:00'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1515"
  ]
}
```

### A query that joins transactions_1k and products on XCL_016 = XCL_008, orders the results by transactions_1k.XCL_017 in descending order, and limits th

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_009\" FROM transactions_1k AS T1 INNER JOIN products AS T2 ON T1.\"XCL_016\" = T2.\"XCL_008\" ORDER BY T1.\"XCL_017\" DESC LIMIT 5",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1530"
  ]
}
```

### A query that groups transactions_1k by XCL_015, orders the groups by the descending sum of XCL_018, and returns the first row (the top XCL_015).

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_015\" FROM transactions_1k GROUP BY \"XCL_015\" ORDER BY SUM(\"XCL_018\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1527"
  ]
}
```

### A SQL program that calculates the average transaction amount for customers transacting in EUR. It joins transactions_1k with gasstations on station ID

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T1.\"XCL_018\") FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" INNER JOIN customers AS T3 ON T1.\"XCL_013\" = T3.\"XCL_001\" WHERE T3.\"XCL_003\" = 'EUR'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1511"
  ]
}
```

### A query that joins transactions_1k and customers on XCL_013 = XCL_001, orders by XCL_011 ascending, and limits to 1 row to identify the customer attri

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_002\" FROM transactions_1k AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_013\" = T2.\"XCL_001\" ORDER BY \"XCL_011\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1517"
  ]
}
```

### A query that identifies the distinct set of product identifiers (XCL_016) and their corresponding product attributes (XCL_009) for transactions where 

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_016\", T3.\"XCL_009\" FROM transactions_1k AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_013\" = T2.\"XCL_001\" INNER JOIN products AS T3 ON T1.\"XCL_016\" = T3.\"XCL_008\" WHERE T2.\"XCL_003\" = 'EUR'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1503"
  ]
}
```

### EUR-Linked Gasstation Query

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T3.\"XCL_005\" FROM transactions_1k AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_013\" = T2.\"XCL_001\" INNER JOIN gasstations AS T3 ON T1.\"XCL_015\" = T3.\"XCL_004\" WHERE T2.\"XCL_003\" = 'EUR'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1502"
  ]
}
```

### The full SQL program that determines a specific entity ID from transactions_1k and gasstations, then calculates the year-over-year change ratio for XC

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(IIF(SUBSTRING(\"XCL_020\", 1, 4) = '2012', \"XCL_021\", 0)) - SUM(IIF(SUBSTRING(\"XCL_020\", 1, 4) = '2013', \"XCL_021\", 0)) AS REAL) / SUM(IIF(SUBSTRING(\"XCL_020\", 1, 4) = '2012', \"XCL_021\", 0)) FROM yearmonth WHERE \"XCL_019\" = (SELECT T1.\"XCL_013\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_011\" = '2012-08-25' AND T1.\"XCL_018\" = 634.8)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1526"
  ]
}
```

### SQL program that joins 'customers' and 'yearmonth' on customer ID, filters for EUR currency, calculates the average monthly consumption per customer, 

```json
{
  "kind": "program",
  "formula": "SELECT SUM(T2.\"XCL_021\") / 12 AS MonthlyConsumption FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_003\" = 'EUR' GROUP BY T1.\"XCL_001\" ORDER BY MonthlyConsumption DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1499"
  ]
}
```

### Customer currency ratio query

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(IIF(\"XCL_003\" = 'EUR', 1, 0)) AS REAL) / SUM(IIF(\"XCL_003\" = 'CZK', 1, 0)) AS ratio FROM customers",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1471"
  ]
}
```

### CZE Transaction Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_010\") FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T2.\"XCL_006\" = 'CZE' AND STRFTIME('%Y', T1.\"XCL_011\") >= '2012'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1509"
  ]
}
```

### Query for Top Transaction Category by Total Amount

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_013\" FROM transactions_1k WHERE \"XCL_011\" = '2012-08-25' GROUP BY \"XCL_013\" ORDER BY SUM(\"XCL_018\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1512"
  ]
}
```

### A query that joins transactions_1k to gasstations on XCL_015 = XCL_004, filters transactions where XCL_016 is 2, orders by XCL_018 in descending order

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_006\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_016\" = 2 ORDER BY T1.\"XCL_018\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1532"
  ]
}
```

### Full SQL program that counts entries in the 'gasstations' table satisfying the conditions 'XCL_006' = 'CZE' and 'XCL_007' = 'Premium'.

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_004\") FROM gasstations WHERE \"XCL_006\" = 'CZE' AND \"XCL_007\" = 'Premium'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1470"
  ]
}
```

### A query program that joins transactions_1k, gasstations, and customers tables. It filters transactions by date ('2012-08-24') and time ('16:25:00') an

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T3.\"XCL_003\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" INNER JOIN customers AS T3 ON T1.\"XCL_013\" = T3.\"XCL_001\" WHERE T1.\"XCL_011\" = '2012-08-24' AND T1.\"XCL_012\" = '16:25:00'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1514"
  ]
}
```

### Full SQL program that joins customers and yearmonth on XCL_001 = XCL_019, filters for currency 'EUR', groups by the year portion of XCL_020, orders by

```json
{
  "kind": "program",
  "formula": "SELECT SUBSTRING(T2.\"XCL_020\", 1, 4) FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_003\" = 'EUR' GROUP BY SUBSTRING(T2.\"XCL_020\", 1, 4) ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1477"
  ]
}
```

### A program that identifies the customer ID (XCL_001) with the minimum aggregated value of XCL_021 for the year 2012. It joins customers and yearmonth t

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_002\" = 'LAM' AND SUBSTRING(T2.\"XCL_020\", 1, 4) = '2012' GROUP BY T1.\"XCL_001\" ORDER BY SUM(T2.\"XCL_021\") ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1472"
  ]
}
```

### A query joining transactions_1k and yearmonth to retrieve XCL_021 where the ratio of XCL_018 to XCL_017 exceeds 29.00, XCL_016 equals 5, and the yearm

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_021\" FROM transactions_1k AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_013\" = T2.\"XCL_019\" WHERE T1.\"XCL_018\" / T1.\"XCL_017\" > 29.00 AND T1.\"XCL_016\" = 5 AND T2.\"XCL_020\" = '201208'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1533"
  ]
}
```

### A program that joins customers and yearmonth tables on customer ID, filters for a specific month ('201310'), customer type ('LAM'), and currency ('EUR

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_002\" = 'LAM' AND T2.\"XCL_020\" = '201310' AND T1.\"XCL_003\" = 'EUR' GROUP BY T1.\"XCL_001\" ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1487"
  ]
}
```

### EUR Customer Transaction Percentage Query

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(IIF(T2.\"XCL_003\" = 'EUR', 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_013\") FROM transactions_1k AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_013\" = T2.\"XCL_001\" WHERE T1.\"XCL_011\" = '2012-08-25'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1525"
  ]
}
```

### 2012 Currency Difference Query

```json
{
  "kind": "program",
  "formula": "SELECT SUM(IIF(T1.\"XCL_003\" = 'CZK', T2.\"XCL_021\", 0)) - SUM(IIF(T1.\"XCL_003\" = 'EUR', T2.\"XCL_021\", 0)) FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE SUBSTRING(T2.\"XCL_020\", 1, 4) = '2012'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1476"
  ]
}
```

### A query that joins transactions_1k and gasstations to retrieve the gasstation identifier (XCL_006) for a specific transaction date (2012-08-24) and ti

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_006\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_011\" = '2012-08-24' AND T1.\"XCL_012\" = '12:42:00'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1518"
  ]
}
```

### A query that identifies unique gasstations with transaction activity in June 2013. It joins transactions_1k to gasstations on the gasstation key (XCL_

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_006\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" INNER JOIN yearmonth AS T3 ON T1.\"XCL_013\" = T3.\"XCL_019\" WHERE T3.\"XCL_020\" = '201306'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1501"
  ]
}
```

### Identifies the value of XCL_006 that has the maximum number of associated records in the gasstations table where XCL_007 is 'Value for money'. It grou

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_006\", (SELECT COUNT(\"XCL_004\") FROM gasstations WHERE \"XCL_007\" = 'Value for money') FROM gasstations WHERE \"XCL_007\" = 'Value for money' GROUP BY \"XCL_006\" ORDER BY COUNT(\"XCL_004\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1491"
  ]
}
```

### A SQL program that computes the percentage of 'Premium' entries among 'SVK' records in the gasstations table. It uses conditional aggregation to count

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(IIF(\"XCL_006\" = 'SVK' AND \"XCL_007\" = 'Premium', 1, 0)) AS REAL) * 100 / SUM(IIF(\"XCL_006\" = 'SVK', 1, 0)) FROM gasstations",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1528"
  ]
}
```

### Full SQL program that joins customers and yearmonth on XCL_001/XCL_019, filters for year '2013' and customer segment 'SME', groups by the month substr

```json
{
  "kind": "program",
  "formula": "SELECT SUBSTRING(T2.\"XCL_020\", 5, 2) FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE SUBSTRING(T2.\"XCL_020\", 1, 4) = '2013' AND T1.\"XCL_002\" = 'SME' GROUP BY SUBSTRING(T2.\"XCL_020\", 5, 2) ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1480"
  ]
}
```

### A SQL program that joins 'transactions_1k' (T1) with 'gasstations' (T2) on 'XCL_015' = 'XCL_004', filters for 'CZE' in 'XCL_006', and calculates the a

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T1.\"XCL_018\") FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T2.\"XCL_006\" = 'CZE'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1510"
  ]
}
```

### A full SQL program that joins "customers" and "transactions_1k" on customer ID, filters transactions to the latest period defined by "yearmonth", and 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_013\", SUM(T2.\"XCL_018\" / T2.\"XCL_017\"), T1.\"XCL_003\" FROM customers AS T1 INNER JOIN transactions_1k AS T2 ON T1.\"XCL_001\" = T2.\"XCL_013\" WHERE T2.\"XCL_013\" = (SELECT \"XCL_019\" FROM yearmonth ORDER BY \"XCL_021\" DESC LIMIT 1) GROUP BY T2.\"XCL_013\", T1.\"XCL_003\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1531"
  ]
}
```

### A program that identifies the single customer with the highest total XCL_021 value from the yearmonth table, restricted to customers of type 'KAM'. It

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_019\", SUM(T2.\"XCL_021\") FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_002\" = 'KAM' GROUP BY T2.\"XCL_019\" ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1488"
  ]
}
```

### Full SQL program that joins customers (T1) with yearmonth (T2) on customers.XCL_001 = yearmonth.XCL_019, filters for customers.XCL_002 = 'LAM', and co

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(IIF(T2.\"XCL_021\" > 46.73, 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_002\" = 'LAM'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1490"
  ]
}
```

### SME Customer Currency Preference Query

```json
{
  "kind": "program",
  "formula": "SELECT SUM(\"XCL_003\" = 'CZK') - SUM(\"XCL_003\" = 'EUR') FROM customers WHERE \"XCL_002\" = 'SME'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1486"
  ]
}
```

### Full SQL program that joins 'customers' (T1) and 'yearmonth' (T2) on 'XCL_001' = 'XCL_019', filters for 'SME' customers and the year '2013', and calcu

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T2.\"XCL_021\") / 12 FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE SUBSTRING(T2.\"XCL_020\", 1, 4) = '2013' AND T1.\"XCL_002\" = 'SME'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1473"
  ]
}
```

### A SQL program that joins 'transactions_1k' (T1) with 'gasstations' (T2) on the condition that T1.'XCL_015' equals T2.'XCL_004'. It filters for gasstat

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_012\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T2.\"XCL_005\" = 11",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1507"
  ]
}
```

### A program that identifies the single customer identifier (XCL_001) from the 'customers' table where the customer segment (XCL_002) is 'SME'. It joins 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T2.\"XCL_020\" = '201206' AND T1.\"XCL_002\" = 'SME' GROUP BY T1.\"XCL_001\" ORDER BY SUM(T2.\"XCL_021\") ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1497"
  ]
}
```

### Full SQL program that calculates the net difference of XCL_021 between XCL_019 codes 7 and 5 from the yearmonth table, restricted to the period where 

```json
{
  "kind": "program",
  "formula": "SELECT SUM(IIF(\"XCL_019\" = 7, \"XCL_021\", 0)) - SUM(IIF(\"XCL_019\" = 5, \"XCL_021\", 0)) FROM yearmonth WHERE \"XCL_020\" = '201304'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1485"
  ]
}
```

### Customer Segment YoY Growth Query

```json
{
  "kind": "program",
  "formula": "SELECT CAST((SUM(IIF(T1.\"XCL_002\" = 'SME' AND T2.\"XCL_020\" LIKE '2013%', T2.\"XCL_021\", 0)) - SUM(IIF(T1.\"XCL_002\" = 'SME' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0))) AS REAL) * 100 / SUM(IIF(T1.\"XCL_002\" = 'SME' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0)), CAST(SUM(IIF(T1.\"XCL_002\" = 'LAM' AND T2.\"XCL_020\" LIKE '2013%', T2.\"XCL_021\", 0)) - SUM(IIF(T1.\"XCL_002\" = 'LAM' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0)) AS REAL) * 100 / SUM(IIF(T1.\"XCL_002\" = 'LAM' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0)), CAST(SUM(IIF(T1.\"XCL_002\" = 'KAM' AND T2.\"XCL_020\" LIKE '2013%', T2.\"XCL_021\", 0)) - SUM(IIF(T1.\"XCL_002\" = 'KAM' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0)) AS REAL) * 100 / SUM(IIF(T1.\"XCL_002\" = 'KAM' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0)) FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1482"
  ]
}
```

### A SQL program that joins the customers table (T1) with the yearmonth table (T2) on XCL_001 = XCL_019. It filters for customers where XCL_003 equals 'C

```json
{
  "kind": "program",
  "formula": "SELECT SUBSTRING(T2.\"XCL_020\", 1, 4) FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_003\" = 'CZK' GROUP BY SUBSTRING(T2.\"XCL_020\", 1, 4) ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1479"
  ]
}
```

### A query that joins transactions_1k and gasstations on XCL_015 = XCL_004, filters for the date 2012-08-25, orders by XCL_012 in descending order, and r

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_006\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_011\" = '2012-08-25' ORDER BY T1.\"XCL_012\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1513"
  ]
}
```

### CZE Morning Transaction Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_010\") FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_011\" = '2012-08-26' AND T1.\"XCL_012\" BETWEEN '08:00:00' AND '09:00:00' AND T2.\"XCL_006\" = 'CZE'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1521"
  ]
}
```

### A query that joins 'transactions_1k' and 'gasstations' on 'XCL_015' = 'XCL_004'. It filters transactions where 'XCL_011' is '2012-08-24' and 'XCL_018'

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_006\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_011\" = '2012-08-24' AND T1.\"XCL_018\" = 548.4",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1524"
  ]
}
```

### Filtered Transaction Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_010\") FROM transactions_1k AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_013\" = T2.\"XCL_001\" WHERE T1.\"XCL_011\" = '2012-08-26' AND T1.\"XCL_012\" < '13:00:00' AND T2.\"XCL_003\" = 'CZK'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1516"
  ]
}
```

### Full SQL program that filters the 'customers' table for records where 'XCL_002' equals 'KAM' and computes the aggregate percentage of those records wh

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(\"XCL_003\" = 'EUR') AS REAL) * 100 / COUNT(\"XCL_001\") FROM customers WHERE \"XCL_002\" = 'KAM'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1492"
  ]
}
```

### A query that joins 'customers' and 'yearmonth' on 'XCL_001' = 'XCL_019', groups by 'XCL_002', and returns the 'XCL_002' with the minimum aggregated su

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_002\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" GROUP BY T1.\"XCL_002\" ORDER BY SUM(T2.\"XCL_021\") ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1478"
  ]
}
```

### A query that identifies the single month in 2012 with the highest total XCL_021 value. It filters the yearmonth table for the year 2012, aggregates XC

```json
{
  "kind": "program",
  "formula": "SELECT SUM(\"XCL_021\") FROM yearmonth WHERE SUBSTRING(\"XCL_020\", 1, 4) = '2012' GROUP BY SUBSTRING(\"XCL_020\", 5, 2) ORDER BY SUM(\"XCL_021\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1498"
  ]
}
```

### A SQL program that calculates the difference in counts between 'CZE' and 'SVK' values in the XCL_006 column, filtered to gasstations where XCL_007 is 

```json
{
  "kind": "program",
  "formula": "SELECT SUM(IIF(\"XCL_006\" = 'CZE', 1, 0)) - SUM(IIF(\"XCL_006\" = 'SVK', 1, 0)) FROM gasstations WHERE \"XCL_007\" = 'Discount'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1484"
  ]
}
```

### A full SQL program that joins transactions_1k with gasstations to retrieve specific transaction attributes. It filters for a precise date ('2012-08-23

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_016\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_011\" = '2012-08-23' AND T1.\"XCL_012\" = '21:20:00'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1519"
  ]
}
```

### A query that joins transactions_1k to yearmonth (filtered to '201309') and products to retrieve product attribute XCL_009. It links transactions to ti

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_009\" FROM transactions_1k AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_013\" = T2.\"XCL_019\" INNER JOIN products AS T3 ON T1.\"XCL_016\" = T3.\"XCL_008\" WHERE T2.\"XCL_020\" = '201309'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1500"
  ]
}
```

### A program that counts the number of customers with the 'KAM' classification in 2012 whose total XCL_021 value is below 30,000. It joins customers and 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(*) FROM (SELECT T2.\"XCL_019\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_002\" = 'KAM' AND SUBSTRING(T2.\"XCL_020\", 1, 4) = '2012' GROUP BY T2.\"XCL_019\" HAVING SUM(T2.\"XCL_021\") < 30000) AS t1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1475"
  ]
}
```

### A full SQL program that joins transactions_1k, gasstations, and products to retrieve distinct product identifiers. It filters for gas stations in 'CZE

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T3.\"XCL_009\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" INNER JOIN products AS T3 ON T1.\"XCL_016\" = T3.\"XCL_008\" WHERE T2.\"XCL_006\" = 'CZE'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1506"
  ]
}
```

### SELECT AVG("XCL_017") FROM transactions_1k WHERE "XCL_011" LIKE '2012-01%'

```json
{
  "kind": "program",
  "formula": "SELECT AVG(\"XCL_017\") FROM transactions_1k WHERE \"XCL_011\" LIKE '2012-01%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1504"
  ]
}
```

### A query that joins the 'yearmonth' table with the 'customers' table on 'XCL_019' = 'XCL_001'. It filters for records where 'XCL_020' is '201306' and '

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_003\" FROM yearmonth AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_019\" = T2.\"XCL_001\" WHERE T1.\"XCL_020\" = '201306' AND T1.\"XCL_021\" = 214582.17",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1522"
  ]
}
```

### SQL program that joins customers and yearmonth on customer ID, filters for period 201309, groups by customer, orders by the descending sum of XCL_021,

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T2.\"XCL_020\" = '201309' GROUP BY T1.\"XCL_001\" ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1495"
  ]
}
```

### Full SQL program that selects the percentage of entries in the 'yearmonth' table where 'XCL_021' > 528.3, divided by the count of 'XCL_019', restricte

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(IIF(\"XCL_021\" > 528.3, 1, 0)) AS REAL) * 100 / COUNT(\"XCL_019\") FROM yearmonth WHERE \"XCL_020\" = '201202'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1493"
  ]
}
```

### Identifies the customer (XCL_001) with the minimum sum of XCL_021 from the yearmonth table for the period '201309', and returns their XCL_002. Joins c

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_002\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T2.\"XCL_020\" = '201309' GROUP BY T1.\"XCL_001\" ORDER BY SUM(T2.\"XCL_021\") ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1496"
  ]
}
```

### Full SQL program that joins transactions_1k to gasstations and yearmonth tables. It filters transactions by a specific year-month identifier (XCL_013 

```json
{
  "kind": "program",
  "formula": "SELECT SUM(T1.\"XCL_018\"), SUM(IIF(T3.\"XCL_020\" = '201201', T1.\"XCL_018\", 0)) FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" INNER JOIN yearmonth AS T3 ON T1.\"XCL_013\" = T3.\"XCL_019\" WHERE T1.\"XCL_013\" = '38508'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1529"
  ]
}
```

### Product Attribute XCL_009

```json
{
  "kind": "binding",
  "formula": "\"products\".\"XCL_009\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_009\" FROM transactions_1k AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_013\" = T2.\"XCL_019\" INNER JOIN products AS T3 ON T1.\"XCL_016\" = T3.\"XCL_008\" WHERE T2.\"XCL_020\" = '201309'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_009\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      },
      {
        "role": "r1",
        "physical_table": "yearmonth"
      },
      {
        "role": "r2",
        "physical_table": "products"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_009\" AS \"value\" FROM transactions_1k AS \"r0\" INNER JOIN yearmonth AS \"r1\" ON \"r0\".\"XCL_013\" = \"r1\".\"XCL_019\" INNER JOIN products AS \"r2\" ON \"r0\".\"XCL_016\" = \"r2\".\"XCL_008\" WHERE \"r1\".\"XCL_020\" = '201309'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1500"
  ]
}
```

### LAM Year-over-Year Growth Rate

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(\"customers\".\"XCL_002\" = 'LAM' AND \"yearmonth\".\"XCL_020\" LIKE '2013%', \"yearmonth\".\"XCL_021\", 0)) - SUM(IIF(\"customers\".\"XCL_002\" = 'LAM' AND \"yearmonth\".\"XCL_020\" LIKE '2012%', \"yearmonth\".\"XCL_021\", 0)) AS REAL) * 100 / SUM(IIF(\"customers\".\"XCL_002\" = 'LAM' AND \"yearmonth\".\"XCL_020\" LIKE '2012%', \"yearmonth\".\"XCL_021\", 0))",
  "grain": [],
  "population_scope": "SELECT CAST((SUM(IIF(T1.\"XCL_002\" = 'SME' AND T2.\"XCL_020\" LIKE '2013%', T2.\"XCL_021\", 0)) - SUM(IIF(T1.\"XCL_002\" = 'SME' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0))) AS REAL) * 100 / SUM(IIF(T1.\"XCL_002\" = 'SME' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0)), CAST(SUM(IIF(T1.\"XCL_002\" = 'LAM' AND T2.\"XCL_020\" LIKE '2013%', T2.\"XCL_021\", 0)) - SUM(IIF(T1.\"XCL_002\" = 'LAM' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0)) AS REAL) * 100 / SUM(IIF(T1.\"XCL_002\" = 'LAM' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0)), CAST(SUM(IIF(T1.\"XCL_002\" = 'KAM' AND T2.\"XCL_020\" LIKE '2013%', T2.\"XCL_021\", 0)) - SUM(IIF(T1.\"XCL_002\" = 'KAM' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0)) AS REAL) * 100 / SUM(IIF(T1.\"XCL_002\" = 'KAM' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0)) FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(IIF(\"r0\".\"XCL_002\" = 'LAM' AND \"r1\".\"XCL_020\" LIKE '2013%', \"r1\".\"XCL_021\", 0)) - SUM(IIF(\"r0\".\"XCL_002\" = 'LAM' AND \"r1\".\"XCL_020\" LIKE '2012%', \"r1\".\"XCL_021\", 0)) AS REAL) * 100 / SUM(IIF(\"r0\".\"XCL_002\" = 'LAM' AND \"r1\".\"XCL_020\" LIKE '2012%', \"r1\".\"XCL_021\", 0))",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "customers"
      },
      {
        "role": "r1",
        "physical_table": "yearmonth"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(IIF(\"r0\".\"XCL_002\" = 'LAM' AND \"r1\".\"XCL_020\" LIKE '2013%', \"r1\".\"XCL_021\", 0)) - SUM(IIF(\"r0\".\"XCL_002\" = 'LAM' AND \"r1\".\"XCL_020\" LIKE '2012%', \"r1\".\"XCL_021\", 0)) AS REAL) * 100 / SUM(IIF(\"r0\".\"XCL_002\" = 'LAM' AND \"r1\".\"XCL_020\" LIKE '2012%', \"r1\".\"XCL_021\", 0)) AS \"value\" FROM customers AS \"r0\" INNER JOIN yearmonth AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_019\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1482"
  ]
}
```

### Latest Year-Month Identifier

```json
{
  "kind": "binding",
  "formula": "\"yearmonth\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_019\" FROM yearmonth ORDER BY \"XCL_021\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1531"
  ]
}
```

### "gasstations"."XCL_007" = 'Discount'

```json
{
  "kind": "predicate",
  "formula": "\"gasstations\".\"XCL_007\" = 'Discount'",
  "grain": [],
  "population_scope": "SELECT SUM(IIF(\"XCL_006\" = 'CZE', 1, 0)) - SUM(IIF(\"XCL_006\" = 'SVK', 1, 0)) FROM gasstations WHERE \"XCL_007\" = 'Discount'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1484"
  ]
}
```

### Aggregates the count of non-null values in the 'XCL_010' column from the 'transactions_1k' table. The population is restricted to transactions joined 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"transactions_1k\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_010\") FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T2.\"XCL_006\" = 'CZE' AND T1.\"XCL_018\" > 1000",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      },
      {
        "role": "r1",
        "physical_table": "gasstations"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_010\") AS \"value\" FROM transactions_1k AS \"r0\" INNER JOIN gasstations AS \"r1\" ON \"r0\".\"XCL_015\" = \"r1\".\"XCL_004\" WHERE \"r1\".\"XCL_006\" = 'CZE' AND \"r0\".\"XCL_018\" > 1000",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1508"
  ]
}
```

### "gasstations"."XCL_006" = 'CZE' AND "gasstations"."XCL_007" = 'Premium'

```json
{
  "kind": "predicate",
  "formula": "\"gasstations\".\"XCL_006\" = 'CZE' AND \"gasstations\".\"XCL_007\" = 'Premium'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_004\") FROM gasstations WHERE \"XCL_006\" = 'CZE' AND \"XCL_007\" = 'Premium'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1470"
  ]
}
```

### "transactions_1k"."XCL_011" = '2012-08-25' AND "transactions_1k"."XCL_018" = 634.8

```json
{
  "kind": "predicate",
  "formula": "\"transactions_1k\".\"XCL_011\" = '2012-08-25' AND \"transactions_1k\".\"XCL_018\" = 634.8",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_013\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_011\" = '2012-08-25' AND T1.\"XCL_018\" = 634.8",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1526"
  ]
}
```

### "customers"."XCL_003" = 'EUR'

```json
{
  "kind": "predicate",
  "formula": "\"customers\".\"XCL_003\" = 'EUR'",
  "grain": [
    "SUBSTRING(\"yearmonth\".\"XCL_020\", 1, 4)"
  ],
  "population_scope": "SELECT SUBSTRING(T2.\"XCL_020\", 1, 4) FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_003\" = 'EUR' GROUP BY SUBSTRING(T2.\"XCL_020\", 1, 4) ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1477"
  ]
}
```

### The value of column XCL_021 from the yearmonth table, returned for transactions that meet specific ratio and category criteria in August 2012.

```json
{
  "kind": "binding",
  "formula": "\"yearmonth\".\"XCL_021\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_021\" FROM transactions_1k AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_013\" = T2.\"XCL_019\" WHERE T1.\"XCL_018\" / T1.\"XCL_017\" > 29.00 AND T1.\"XCL_016\" = 5 AND T2.\"XCL_020\" = '201208'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_021\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      },
      {
        "role": "r1",
        "physical_table": "yearmonth"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_021\" AS \"value\" FROM transactions_1k AS \"r0\" INNER JOIN yearmonth AS \"r1\" ON \"r0\".\"XCL_013\" = \"r1\".\"XCL_019\" WHERE \"r0\".\"XCL_018\" / \"r0\".\"XCL_017\" > 29.00 AND \"r0\".\"XCL_016\" = 5 AND \"r1\".\"XCL_020\" = '201208'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1533"
  ]
}
```

### Aggregated sum of the XCL_021 column, grouped by the month portion (characters 5-6) of the XCL_020 column. The population is restricted to records whe

```json
{
  "kind": "metric",
  "formula": "SUM(\"yearmonth\".\"XCL_021\")",
  "grain": [
    "SUBSTRING(\"yearmonth\".\"XCL_020\", 5, 2)"
  ],
  "population_scope": "SELECT SUM(\"XCL_021\") FROM yearmonth WHERE SUBSTRING(\"XCL_020\", 1, 4) = '2012' GROUP BY SUBSTRING(\"XCL_020\", 5, 2) ORDER BY SUM(\"XCL_021\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1498"
  ]
}
```

### Attribute from the yearmonth table (T2) associated with the year-month period. Returned as part of the output grain.

```json
{
  "kind": "binding",
  "formula": "\"yearmonth\".\"XCL_021\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_013\", T2.\"XCL_020\", T2.\"XCL_021\" FROM transactions_1k AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_013\" = T2.\"XCL_019\" WHERE T1.\"XCL_011\" = '2012-08-24' AND T1.\"XCL_018\" = 124.05 AND T2.\"XCL_020\" = '201201'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_021\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      },
      {
        "role": "r1",
        "physical_table": "yearmonth"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_021\" AS \"value\" FROM transactions_1k AS \"r0\" INNER JOIN yearmonth AS \"r1\" ON \"r0\".\"XCL_013\" = \"r1\".\"XCL_019\" WHERE \"r0\".\"XCL_011\" = '2012-08-24' AND \"r0\".\"XCL_018\" = 124.05 AND \"r1\".\"XCL_020\" = '201201'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1520"
  ]
}
```

### Customer Identifier (Low Volume 2012 KAM)

```json
{
  "kind": "binding",
  "formula": "\"yearmonth\".\"XCL_019\"",
  "grain": [
    "\"yearmonth\".\"XCL_019\""
  ],
  "population_scope": "SELECT T2.\"XCL_019\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_002\" = 'KAM' AND SUBSTRING(T2.\"XCL_020\", 1, 4) = '2012' GROUP BY T2.\"XCL_019\" HAVING SUM(T2.\"XCL_021\") < 30000",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_019\"",
    "grain": [
      "\"r1\".\"XCL_019\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "customers"
      },
      {
        "role": "r1",
        "physical_table": "yearmonth"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_019\" AS \"grain_0\", \"r1\".\"XCL_019\" AS \"value\" FROM customers AS \"r0\" INNER JOIN yearmonth AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_019\" WHERE \"r0\".\"XCL_002\" = 'KAM' AND SUBSTRING(\"r1\".\"XCL_020\", 1, 4) = '2012' GROUP BY \"r1\".\"XCL_019\" HAVING SUM(\"r1\".\"XCL_021\") < 30000",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1475"
  ]
}
```

### A scalar metric calculated from the yearmonth table. It computes the relative change between the sum of XCL_021 for records where the first 4 characte

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(SUBSTRING(\"yearmonth\".\"XCL_020\", 1, 4) = '2012', \"yearmonth\".\"XCL_021\", 0)) - SUM(IIF(SUBSTRING(\"yearmonth\".\"XCL_020\", 1, 4) = '2013', \"yearmonth\".\"XCL_021\", 0)) AS REAL) / SUM(IIF(SUBSTRING(\"yearmonth\".\"XCL_020\", 1, 4) = '2012', \"yearmonth\".\"XCL_021\", 0))",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(SUBSTRING(\"XCL_020\", 1, 4) = '2012', \"XCL_021\", 0)) - SUM(IIF(SUBSTRING(\"XCL_020\", 1, 4) = '2013', \"XCL_021\", 0)) AS REAL) / SUM(IIF(SUBSTRING(\"XCL_020\", 1, 4) = '2012', \"XCL_021\", 0)) FROM yearmonth WHERE \"XCL_019\" = (SELECT T1.\"XCL_013\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_011\" = '2012-08-25' AND T1.\"XCL_018\" = 634.8)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1526"
  ]
}
```

### SUBSTRING("yearmonth"."XCL_020", 1, 4) = '2013' AND "customers"."XCL_002" = 'SME'

```json
{
  "kind": "predicate",
  "formula": "SUBSTRING(\"yearmonth\".\"XCL_020\", 1, 4) = '2013' AND \"customers\".\"XCL_002\" = 'SME'",
  "grain": [],
  "population_scope": "SELECT AVG(T2.\"XCL_021\") / 12 FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE SUBSTRING(T2.\"XCL_020\", 1, 4) = '2013' AND T1.\"XCL_002\" = 'SME'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1473"
  ]
}
```

### "transactions_1k"."XCL_011" = '2012-08-23' AND "transactions_1k"."XCL_012" = '21:20:00'

```json
{
  "kind": "predicate",
  "formula": "\"transactions_1k\".\"XCL_011\" = '2012-08-23' AND \"transactions_1k\".\"XCL_012\" = '21:20:00'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_002\" FROM transactions_1k AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_013\" = T2.\"XCL_001\" WHERE T1.\"XCL_011\" = '2012-08-23' AND T1.\"XCL_012\" = '21:20:00'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1515"
  ]
}
```

### CZK minus EUR XCL_021 difference

```json
{
  "kind": "metric",
  "formula": "SUM(IIF(\"customers\".\"XCL_003\" = 'CZK', \"yearmonth\".\"XCL_021\", 0)) - SUM(IIF(\"customers\".\"XCL_003\" = 'EUR', \"yearmonth\".\"XCL_021\", 0))",
  "grain": [],
  "population_scope": "SELECT SUM(IIF(T1.\"XCL_003\" = 'CZK', T2.\"XCL_021\", 0)) - SUM(IIF(T1.\"XCL_003\" = 'EUR', T2.\"XCL_021\", 0)) FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE SUBSTRING(T2.\"XCL_020\", 1, 4) = '2012'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(IIF(\"r0\".\"XCL_003\" = 'CZK', \"r1\".\"XCL_021\", 0)) - SUM(IIF(\"r0\".\"XCL_003\" = 'EUR', \"r1\".\"XCL_021\", 0))",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "customers"
      },
      {
        "role": "r1",
        "physical_table": "yearmonth"
      }
    ],
    "scope_sql": "SELECT SUM(IIF(\"r0\".\"XCL_003\" = 'CZK', \"r1\".\"XCL_021\", 0)) - SUM(IIF(\"r0\".\"XCL_003\" = 'EUR', \"r1\".\"XCL_021\", 0)) AS \"value\" FROM customers AS \"r0\" INNER JOIN yearmonth AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_019\" WHERE SUBSTRING(\"r1\".\"XCL_020\", 1, 4) = '2012'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1476"
  ]
}
```

### Product Attribute XCL_009

```json
{
  "kind": "binding",
  "formula": "\"products\".\"XCL_009\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_016\", T3.\"XCL_009\" FROM transactions_1k AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_013\" = T2.\"XCL_001\" INNER JOIN products AS T3 ON T1.\"XCL_016\" = T3.\"XCL_008\" WHERE T2.\"XCL_003\" = 'EUR'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1503"
  ]
}
```

### "transactions_1k"."XCL_011" = '2012-08-23' AND "transactions_1k"."XCL_012" = '21:20:00'

```json
{
  "kind": "predicate",
  "formula": "\"transactions_1k\".\"XCL_011\" = '2012-08-23' AND \"transactions_1k\".\"XCL_012\" = '21:20:00'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_016\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_011\" = '2012-08-23' AND T1.\"XCL_012\" = '21:20:00'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1519"
  ]
}
```

### Aggregated difference between the sum of XCL_021 where XCL_019 is 7 and the sum of XCL_021 where XCL_019 is 5. Returns a single scalar value represent

```json
{
  "kind": "metric",
  "formula": "SUM(IIF(\"yearmonth\".\"XCL_019\" = 7, \"yearmonth\".\"XCL_021\", 0)) - SUM(IIF(\"yearmonth\".\"XCL_019\" = 5, \"yearmonth\".\"XCL_021\", 0))",
  "grain": [],
  "population_scope": "SELECT SUM(IIF(\"XCL_019\" = 7, \"XCL_021\", 0)) - SUM(IIF(\"XCL_019\" = 5, \"XCL_021\", 0)) FROM yearmonth WHERE \"XCL_020\" = '201304'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(IIF(\"r0\".\"XCL_019\" = 7, \"r0\".\"XCL_021\", 0)) - SUM(IIF(\"r0\".\"XCL_019\" = 5, \"r0\".\"XCL_021\", 0))",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "yearmonth"
      }
    ],
    "scope_sql": "SELECT SUM(IIF(\"r0\".\"XCL_019\" = 7, \"r0\".\"XCL_021\", 0)) - SUM(IIF(\"r0\".\"XCL_019\" = 5, \"r0\".\"XCL_021\", 0)) AS \"value\" FROM yearmonth AS \"r0\" WHERE \"r0\".\"XCL_020\" = '201304'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1485"
  ]
}
```

### Count of qualifying yearmonth records

```json
{
  "kind": "metric",
  "formula": "COUNT(*)",
  "grain": [],
  "population_scope": "SELECT COUNT(*) FROM yearmonth AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_019\" = T2.\"XCL_001\" WHERE T2.\"XCL_003\" = 'EUR' AND T1.\"XCL_021\" > 1000.00",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(*)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "yearmonth"
      },
      {
        "role": "r1",
        "physical_table": "customers"
      }
    ],
    "scope_sql": "SELECT COUNT(*) AS \"value\" FROM yearmonth AS \"r0\" INNER JOIN customers AS \"r1\" ON \"r0\".\"XCL_019\" = \"r1\".\"XCL_001\" WHERE \"r1\".\"XCL_003\" = 'EUR' AND \"r0\".\"XCL_021\" > 1000.00",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1505"
  ]
}
```

### SUBSTRING("yearmonth"."XCL_020", 1, 4) = '2012'

```json
{
  "kind": "predicate",
  "formula": "SUBSTRING(\"yearmonth\".\"XCL_020\", 1, 4) = '2012'",
  "grain": [],
  "population_scope": "SELECT SUM(IIF(T1.\"XCL_003\" = 'CZK', T2.\"XCL_021\", 0)) - SUM(IIF(T1.\"XCL_003\" = 'EUR', T2.\"XCL_021\", 0)) FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE SUBSTRING(T2.\"XCL_020\", 1, 4) = '2012'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1476"
  ]
}
```

### "transactions_1k"."XCL_016" = 2

```json
{
  "kind": "predicate",
  "formula": "\"transactions_1k\".\"XCL_016\" = 2",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_016\" = 2 ORDER BY T1.\"XCL_018\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1532"
  ]
}
```

### SUM("yearmonth"."XCL_021") < 30000

```json
{
  "kind": "predicate",
  "formula": "SUM(\"yearmonth\".\"XCL_021\") < 30000",
  "grain": [
    "\"yearmonth\".\"XCL_019\""
  ],
  "population_scope": "SELECT T2.\"XCL_019\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_002\" = 'KAM' AND SUBSTRING(T2.\"XCL_020\", 1, 4) = '2012' GROUP BY T2.\"XCL_019\" HAVING SUM(T2.\"XCL_021\") < 30000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1475"
  ]
}
```

### "customers"."XCL_002" = 'KAM' AND SUBSTRING("yearmonth"."XCL_020", 1, 4) = '2012'

```json
{
  "kind": "predicate",
  "formula": "\"customers\".\"XCL_002\" = 'KAM' AND SUBSTRING(\"yearmonth\".\"XCL_020\", 1, 4) = '2012'",
  "grain": [
    "\"yearmonth\".\"XCL_019\""
  ],
  "population_scope": "SELECT T2.\"XCL_019\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_002\" = 'KAM' AND SUBSTRING(T2.\"XCL_020\", 1, 4) = '2012' GROUP BY T2.\"XCL_019\" HAVING SUM(T2.\"XCL_021\") < 30000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1475"
  ]
}
```

### "customers"."XCL_002" = 'LAM' AND "yearmonth"."XCL_020" = '201310' AND "customers"."XCL_003" = 'EUR'

```json
{
  "kind": "predicate",
  "formula": "\"customers\".\"XCL_002\" = 'LAM' AND \"yearmonth\".\"XCL_020\" = '201310' AND \"customers\".\"XCL_003\" = 'EUR'",
  "grain": [
    "\"customers\".\"XCL_001\""
  ],
  "population_scope": "SELECT T1.\"XCL_001\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_002\" = 'LAM' AND T2.\"XCL_020\" = '201310' AND T1.\"XCL_003\" = 'EUR' GROUP BY T1.\"XCL_001\" ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1487"
  ]
}
```

### "customers"."XCL_003" = 'CZK'

```json
{
  "kind": "predicate",
  "formula": "\"customers\".\"XCL_003\" = 'CZK'",
  "grain": [
    "SUBSTRING(\"yearmonth\".\"XCL_020\", 1, 4)"
  ],
  "population_scope": "SELECT SUBSTRING(T2.\"XCL_020\", 1, 4) FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_003\" = 'CZK' GROUP BY SUBSTRING(T2.\"XCL_020\", 1, 4) ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1479"
  ]
}
```

### "yearmonth"."XCL_020" = '201304'

```json
{
  "kind": "predicate",
  "formula": "\"yearmonth\".\"XCL_020\" = '201304'",
  "grain": [],
  "population_scope": "SELECT SUM(IIF(\"XCL_019\" = 7, \"XCL_021\", 0)) - SUM(IIF(\"XCL_019\" = 5, \"XCL_021\", 0)) FROM yearmonth WHERE \"XCL_020\" = '201304'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1485"
  ]
}
```

### "transactions_1k"."XCL_011" = '2012-08-25'

```json
{
  "kind": "predicate",
  "formula": "\"transactions_1k\".\"XCL_011\" = '2012-08-25'",
  "grain": [
    "\"transactions_1k\".\"XCL_013\""
  ],
  "population_scope": "SELECT \"XCL_013\" FROM transactions_1k WHERE \"XCL_011\" = '2012-08-25' GROUP BY \"XCL_013\" ORDER BY SUM(\"XCL_018\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1512"
  ]
}
```

### "customers"."XCL_002" = 'SME'

```json
{
  "kind": "predicate",
  "formula": "\"customers\".\"XCL_002\" = 'SME'",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_003\" = 'CZK') - SUM(\"XCL_003\" = 'EUR') FROM customers WHERE \"XCL_002\" = 'SME'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1486"
  ]
}
```

### Calculates the percentage of transactions (counted by transaction ID XCL_013) where the associated customer's currency (XCL_003) is 'EUR'. The populat

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(\"customers\".\"XCL_003\" = 'EUR', 1, 0)) AS REAL) * 100 / COUNT(\"transactions_1k\".\"XCL_013\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(T2.\"XCL_003\" = 'EUR', 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_013\") FROM transactions_1k AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_013\" = T2.\"XCL_001\" WHERE T1.\"XCL_011\" = '2012-08-25'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(IIF(\"r1\".\"XCL_003\" = 'EUR', 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_013\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      },
      {
        "role": "r1",
        "physical_table": "customers"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(IIF(\"r1\".\"XCL_003\" = 'EUR', 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_013\") AS \"value\" FROM transactions_1k AS \"r0\" INNER JOIN customers AS \"r1\" ON \"r0\".\"XCL_013\" = \"r1\".\"XCL_001\" WHERE \"r0\".\"XCL_011\" = '2012-08-25'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1525"
  ]
}
```

### Calculates the percentage of rows in the 'yearmonth' table where the value in column 'XCL_021' is greater than 528.3, relative to the total count of n

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(\"yearmonth\".\"XCL_021\" > 528.3, 1, 0)) AS REAL) * 100 / COUNT(\"yearmonth\".\"XCL_019\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(\"XCL_021\" > 528.3, 1, 0)) AS REAL) * 100 / COUNT(\"XCL_019\") FROM yearmonth WHERE \"XCL_020\" = '201202'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(IIF(\"r0\".\"XCL_021\" > 528.3, 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_019\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "yearmonth"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(IIF(\"r0\".\"XCL_021\" > 528.3, 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_019\") AS \"value\" FROM yearmonth AS \"r0\" WHERE \"r0\".\"XCL_020\" = '201202'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1493"
  ]
}
```

### Aggregated count of transaction records (identified by XCL_010) from the transactions_1k table. The population is restricted to transactions occurring

```json
{
  "kind": "metric",
  "formula": "COUNT(\"transactions_1k\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_010\") FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_011\" = '2012-08-26' AND T1.\"XCL_012\" BETWEEN '08:00:00' AND '09:00:00' AND T2.\"XCL_006\" = 'CZE'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      },
      {
        "role": "r1",
        "physical_table": "gasstations"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_010\") AS \"value\" FROM transactions_1k AS \"r0\" INNER JOIN gasstations AS \"r1\" ON \"r0\".\"XCL_015\" = \"r1\".\"XCL_004\" WHERE \"r0\".\"XCL_011\" = '2012-08-26' AND \"r0\".\"XCL_012\" BETWEEN '08:00:00' AND '09:00:00' AND \"r1\".\"XCL_006\" = 'CZE'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1521"
  ]
}
```

### CZE vs SVK Gasstation Count Difference

```json
{
  "kind": "metric",
  "formula": "SUM(IIF(\"gasstations\".\"XCL_006\" = 'CZE', 1, 0)) - SUM(IIF(\"gasstations\".\"XCL_006\" = 'SVK', 1, 0))",
  "grain": [],
  "population_scope": "SELECT SUM(IIF(\"XCL_006\" = 'CZE', 1, 0)) - SUM(IIF(\"XCL_006\" = 'SVK', 1, 0)) FROM gasstations WHERE \"XCL_007\" = 'Discount'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(IIF(\"r0\".\"XCL_006\" = 'CZE', 1, 0)) - SUM(IIF(\"r0\".\"XCL_006\" = 'SVK', 1, 0))",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "gasstations"
      }
    ],
    "scope_sql": "SELECT SUM(IIF(\"r0\".\"XCL_006\" = 'CZE', 1, 0)) - SUM(IIF(\"r0\".\"XCL_006\" = 'SVK', 1, 0)) AS \"value\" FROM gasstations AS \"r0\" WHERE \"r0\".\"XCL_007\" = 'Discount'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1484"
  ]
}
```

### Gasstation Identifier

```json
{
  "kind": "binding",
  "formula": "\"gasstations\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_016\" = 2 ORDER BY T1.\"XCL_018\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1532"
  ]
}
```

### KAM vs SME Average Difference

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(\"customers\".\"XCL_002\" = 'KAM', \"yearmonth\".\"XCL_021\", 0)) AS REAL) / COUNT(\"customers\".\"XCL_001\") - CAST(SUM(IIF(\"customers\".\"XCL_002\" = 'SME', \"yearmonth\".\"XCL_021\", 0)) AS REAL) / COUNT(\"customers\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(T1.\"XCL_002\" = 'SME', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\") - CAST(SUM(IIF(T1.\"XCL_002\" = 'LAM', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\"), CAST(SUM(IIF(T1.\"XCL_002\" = 'LAM', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\") - CAST(SUM(IIF(T1.\"XCL_002\" = 'KAM', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\"), CAST(SUM(IIF(T1.\"XCL_002\" = 'KAM', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\") - CAST(SUM(IIF(T1.\"XCL_002\" = 'SME', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\") FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_003\" = 'CZK' AND T2.\"XCL_021\" = (SELECT MIN(\"XCL_021\") FROM yearmonth) AND T2.\"XCL_020\" BETWEEN 201301 AND 201312",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1481"
  ]
}
```

### Attribute from the yearmonth table (T2) representing the year-month period. Filtered to '201201' in this query.

```json
{
  "kind": "binding",
  "formula": "\"yearmonth\".\"XCL_020\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_013\", T2.\"XCL_020\", T2.\"XCL_021\" FROM transactions_1k AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_013\" = T2.\"XCL_019\" WHERE T1.\"XCL_011\" = '2012-08-24' AND T1.\"XCL_018\" = 124.05 AND T2.\"XCL_020\" = '201201'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_020\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      },
      {
        "role": "r1",
        "physical_table": "yearmonth"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_020\" AS \"value\" FROM transactions_1k AS \"r0\" INNER JOIN yearmonth AS \"r1\" ON \"r0\".\"XCL_013\" = \"r1\".\"XCL_019\" WHERE \"r0\".\"XCL_011\" = '2012-08-24' AND \"r0\".\"XCL_018\" = 124.05 AND \"r1\".\"XCL_020\" = '201201'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1520"
  ]
}
```

### "transactions_1k"."XCL_011" = '2012-08-24' AND "transactions_1k"."XCL_012" = '12:42:00'

```json
{
  "kind": "predicate",
  "formula": "\"transactions_1k\".\"XCL_011\" = '2012-08-24' AND \"transactions_1k\".\"XCL_012\" = '12:42:00'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_011\" = '2012-08-24' AND T1.\"XCL_012\" = '12:42:00'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1518"
  ]
}
```

### The single customer identifier (XCL_001) with the highest aggregated sum of XCL_021 from the yearmonth table for the year 2011, restricted to customer

```json
{
  "kind": "binding",
  "formula": "\"customers\".\"XCL_001\"",
  "grain": [
    "\"customers\".\"XCL_001\""
  ],
  "population_scope": "SELECT T1.\"XCL_001\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_003\" = 'CZK' AND T2.\"XCL_020\" BETWEEN 201101 AND 201112 GROUP BY T1.\"XCL_001\" ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1474"
  ]
}
```

### "transactions_1k"."XCL_011" = '2012-08-24' AND "transactions_1k"."XCL_012" = '16:25:00'

```json
{
  "kind": "predicate",
  "formula": "\"transactions_1k\".\"XCL_011\" = '2012-08-24' AND \"transactions_1k\".\"XCL_012\" = '16:25:00'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_003\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" INNER JOIN customers AS T3 ON T1.\"XCL_013\" = T3.\"XCL_001\" WHERE T1.\"XCL_011\" = '2012-08-24' AND T1.\"XCL_012\" = '16:25:00'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1514"
  ]
}
```

### Aggregated count of the 'XCL_004' column from the 'gasstations' table, filtered to rows where 'XCL_006' equals 'CZE' and 'XCL_007' equals 'Premium'. R

```json
{
  "kind": "metric",
  "formula": "COUNT(\"gasstations\".\"XCL_004\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_004\") FROM gasstations WHERE \"XCL_006\" = 'CZE' AND \"XCL_007\" = 'Premium'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_004\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "gasstations"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_004\") AS \"value\" FROM gasstations AS \"r0\" WHERE \"r0\".\"XCL_006\" = 'CZE' AND \"r0\".\"XCL_007\" = 'Premium'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1470"
  ]
}
```

### Customer Identifier

```json
{
  "kind": "binding",
  "formula": "\"customers\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM yearmonth AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_019\" = T2.\"XCL_001\" WHERE T1.\"XCL_020\" = '201306' AND T1.\"XCL_021\" = 214582.17",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "yearmonth"
      },
      {
        "role": "r1",
        "physical_table": "customers"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_003\" AS \"value\" FROM yearmonth AS \"r0\" INNER JOIN customers AS \"r1\" ON \"r0\".\"XCL_019\" = \"r1\".\"XCL_001\" WHERE \"r0\".\"XCL_020\" = '201306' AND \"r0\".\"XCL_021\" = 214582.17",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1522"
  ]
}
```

### Conditional aggregate sum of the transaction value field (XCL_018) from the transactions_1k table, counting only rows where the associated year-month 

```json
{
  "kind": "metric",
  "formula": "SUM(IIF(\"yearmonth\".\"XCL_020\" = '201201', \"transactions_1k\".\"XCL_018\", 0))",
  "grain": [],
  "population_scope": "SELECT SUM(T1.\"XCL_018\"), SUM(IIF(T3.\"XCL_020\" = '201201', T1.\"XCL_018\", 0)) FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" INNER JOIN yearmonth AS T3 ON T1.\"XCL_013\" = T3.\"XCL_019\" WHERE T1.\"XCL_013\" = '38508'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(IIF(\"r2\".\"XCL_020\" = '201201', \"r0\".\"XCL_018\", 0))",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      },
      {
        "role": "r1",
        "physical_table": "gasstations"
      },
      {
        "role": "r2",
        "physical_table": "yearmonth"
      }
    ],
    "scope_sql": "SELECT SUM(IIF(\"r2\".\"XCL_020\" = '201201', \"r0\".\"XCL_018\", 0)) AS \"value\" FROM transactions_1k AS \"r0\" INNER JOIN gasstations AS \"r1\" ON \"r0\".\"XCL_015\" = \"r1\".\"XCL_004\" INNER JOIN yearmonth AS \"r2\" ON \"r0\".\"XCL_013\" = \"r2\".\"XCL_019\" WHERE \"r0\".\"XCL_013\" = '38508'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1529"
  ]
}
```

### "transactions_1k"."XCL_013" = '38508'

```json
{
  "kind": "predicate",
  "formula": "\"transactions_1k\".\"XCL_013\" = '38508'",
  "grain": [],
  "population_scope": "SELECT SUM(T1.\"XCL_018\"), SUM(IIF(T3.\"XCL_020\" = '201201', T1.\"XCL_018\", 0)) FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" INNER JOIN yearmonth AS T3 ON T1.\"XCL_013\" = T3.\"XCL_019\" WHERE T1.\"XCL_013\" = '38508'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1529"
  ]
}
```

### "transactions_1k"."XCL_014" = '667467'

```json
{
  "kind": "predicate",
  "formula": "\"transactions_1k\".\"XCL_014\" = '667467'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_014\" = '667467'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1523"
  ]
}
```

### "gasstations"."XCL_006" = 'SVK'

```json
{
  "kind": "predicate",
  "formula": "\"gasstations\".\"XCL_006\" = 'SVK'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(\"XCL_007\" = 'Premium', 1, 0)) AS REAL) * 100 / COUNT(\"XCL_004\") FROM gasstations WHERE \"XCL_006\" = 'SVK'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1494"
  ]
}
```

### SUBSTRING("yearmonth"."XCL_020", 1, 4) = '2012'

```json
{
  "kind": "predicate",
  "formula": "SUBSTRING(\"yearmonth\".\"XCL_020\", 1, 4) = '2012'",
  "grain": [
    "SUBSTRING(\"yearmonth\".\"XCL_020\", 5, 2)"
  ],
  "population_scope": "SELECT SUM(\"XCL_021\") FROM yearmonth WHERE SUBSTRING(\"XCL_020\", 1, 4) = '2012' GROUP BY SUBSTRING(\"XCL_020\", 5, 2) ORDER BY SUM(\"XCL_021\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1498"
  ]
}
```

### Distinct values of the gasstation identifier (XCL_005) from the gasstations table. The population is restricted to gasstations that have at least one 

```json
{
  "kind": "binding",
  "formula": "\"gasstations\".\"XCL_005\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_005\" FROM transactions_1k AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_013\" = T2.\"XCL_001\" INNER JOIN gasstations AS T3 ON T1.\"XCL_015\" = T3.\"XCL_004\" WHERE T2.\"XCL_003\" = 'EUR'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1502"
  ]
}
```

### Gasstation Identifier

```json
{
  "kind": "binding",
  "formula": "\"gasstations\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_011\" = '2012-08-24' AND T1.\"XCL_018\" = 548.4",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      },
      {
        "role": "r1",
        "physical_table": "gasstations"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_006\" AS \"value\" FROM transactions_1k AS \"r0\" INNER JOIN gasstations AS \"r1\" ON \"r0\".\"XCL_015\" = \"r1\".\"XCL_004\" WHERE \"r0\".\"XCL_011\" = '2012-08-24' AND \"r0\".\"XCL_018\" = 548.4",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1524"
  ]
}
```

### Calculates the percentage of customers where the currency field (XCL_003) is 'EUR' among the subset of customers where the segment or type field (XCL_

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"customers\".\"XCL_003\" = 'EUR') AS REAL) * 100 / COUNT(\"customers\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(\"XCL_003\" = 'EUR') AS REAL) * 100 / COUNT(\"XCL_001\") FROM customers WHERE \"XCL_002\" = 'KAM'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(\"r0\".\"XCL_003\" = 'EUR') AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "customers"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(\"r0\".\"XCL_003\" = 'EUR') AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM customers AS \"r0\" WHERE \"r0\".\"XCL_002\" = 'KAM'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1492"
  ]
}
```

### "customers"."XCL_003" = 'EUR'

```json
{
  "kind": "predicate",
  "formula": "\"customers\".\"XCL_003\" = 'EUR'",
  "grain": [
    "\"customers\".\"XCL_001\""
  ],
  "population_scope": "SELECT SUM(T2.\"XCL_021\") / 12 AS MonthlyConsumption FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_003\" = 'EUR' GROUP BY T1.\"XCL_001\" ORDER BY MonthlyConsumption DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1499"
  ]
}
```

### Customer Identifier

```json
{
  "kind": "binding",
  "formula": "\"customers\".\"XCL_002\"",
  "grain": [
    "\"customers\".\"XCL_002\""
  ],
  "population_scope": "SELECT T1.\"XCL_002\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" GROUP BY T1.\"XCL_002\" ORDER BY SUM(T2.\"XCL_021\") ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1478"
  ]
}
```

### Customer Identifier

```json
{
  "kind": "binding",
  "formula": "\"customers\".\"XCL_002\"",
  "grain": [
    "\"customers\".\"XCL_001\""
  ],
  "population_scope": "SELECT T1.\"XCL_002\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T2.\"XCL_020\" = '201309' GROUP BY T1.\"XCL_001\" ORDER BY SUM(T2.\"XCL_021\") ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1496"
  ]
}
```

### Distinct values of the gasstation identifier (XCL_006) from the gasstations table. The population is limited to gasstations that have at least one tra

```json
{
  "kind": "binding",
  "formula": "\"gasstations\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_006\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" INNER JOIN yearmonth AS T3 ON T1.\"XCL_013\" = T3.\"XCL_019\" WHERE T3.\"XCL_020\" = '201306'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1501"
  ]
}
```

### Percentage change in the sum of `yearmonth.XCL_021` for customers where `customers.XCL_002` is 'SME', comparing periods starting with '2013' against '

```json
{
  "kind": "metric",
  "formula": "CAST((SUM(IIF(\"customers\".\"XCL_002\" = 'SME' AND \"yearmonth\".\"XCL_020\" LIKE '2013%', \"yearmonth\".\"XCL_021\", 0)) - SUM(IIF(\"customers\".\"XCL_002\" = 'SME' AND \"yearmonth\".\"XCL_020\" LIKE '2012%', \"yearmonth\".\"XCL_021\", 0))) AS REAL) * 100 / SUM(IIF(\"customers\".\"XCL_002\" = 'SME' AND \"yearmonth\".\"XCL_020\" LIKE '2012%', \"yearmonth\".\"XCL_021\", 0))",
  "grain": [],
  "population_scope": "SELECT CAST((SUM(IIF(T1.\"XCL_002\" = 'SME' AND T2.\"XCL_020\" LIKE '2013%', T2.\"XCL_021\", 0)) - SUM(IIF(T1.\"XCL_002\" = 'SME' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0))) AS REAL) * 100 / SUM(IIF(T1.\"XCL_002\" = 'SME' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0)), CAST(SUM(IIF(T1.\"XCL_002\" = 'LAM' AND T2.\"XCL_020\" LIKE '2013%', T2.\"XCL_021\", 0)) - SUM(IIF(T1.\"XCL_002\" = 'LAM' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0)) AS REAL) * 100 / SUM(IIF(T1.\"XCL_002\" = 'LAM' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0)), CAST(SUM(IIF(T1.\"XCL_002\" = 'KAM' AND T2.\"XCL_020\" LIKE '2013%', T2.\"XCL_021\", 0)) - SUM(IIF(T1.\"XCL_002\" = 'KAM' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0)) AS REAL) * 100 / SUM(IIF(T1.\"XCL_002\" = 'KAM' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0)) FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST((SUM(IIF(\"r0\".\"XCL_002\" = 'SME' AND \"r1\".\"XCL_020\" LIKE '2013%', \"r1\".\"XCL_021\", 0)) - SUM(IIF(\"r0\".\"XCL_002\" = 'SME' AND \"r1\".\"XCL_020\" LIKE '2012%', \"r1\".\"XCL_021\", 0))) AS REAL) * 100 / SUM(IIF(\"r0\".\"XCL_002\" = 'SME' AND \"r1\".\"XCL_020\" LIKE '2012%', \"r1\".\"XCL_021\", 0))",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "customers"
      },
      {
        "role": "r1",
        "physical_table": "yearmonth"
      }
    ],
    "scope_sql": "SELECT CAST((SUM(IIF(\"r0\".\"XCL_002\" = 'SME' AND \"r1\".\"XCL_020\" LIKE '2013%', \"r1\".\"XCL_021\", 0)) - SUM(IIF(\"r0\".\"XCL_002\" = 'SME' AND \"r1\".\"XCL_020\" LIKE '2012%', \"r1\".\"XCL_021\", 0))) AS REAL) * 100 / SUM(IIF(\"r0\".\"XCL_002\" = 'SME' AND \"r1\".\"XCL_020\" LIKE '2012%', \"r1\".\"XCL_021\", 0)) AS \"value\" FROM customers AS \"r0\" INNER JOIN yearmonth AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_019\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1482"
  ]
}
```

### "yearmonth"."XCL_020" = '201306'

```json
{
  "kind": "predicate",
  "formula": "\"yearmonth\".\"XCL_020\" = '201306'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_006\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" INNER JOIN yearmonth AS T3 ON T1.\"XCL_013\" = T3.\"XCL_019\" WHERE T3.\"XCL_020\" = '201306'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1501"
  ]
}
```

### Count of transaction records (XCL_010) from transactions_1k, filtered to a specific date (2012-08-26), time before 13:00:00, and joined to customers w

```json
{
  "kind": "metric",
  "formula": "COUNT(\"transactions_1k\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_010\") FROM transactions_1k AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_013\" = T2.\"XCL_001\" WHERE T1.\"XCL_011\" = '2012-08-26' AND T1.\"XCL_012\" < '13:00:00' AND T2.\"XCL_003\" = 'CZK'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      },
      {
        "role": "r1",
        "physical_table": "customers"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_010\") AS \"value\" FROM transactions_1k AS \"r0\" INNER JOIN customers AS \"r1\" ON \"r0\".\"XCL_013\" = \"r1\".\"XCL_001\" WHERE \"r0\".\"XCL_011\" = '2012-08-26' AND \"r0\".\"XCL_012\" < '13:00:00' AND \"r1\".\"XCL_003\" = 'CZK'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1516"
  ]
}
```

### Average Transaction Amount (EUR)

```json
{
  "kind": "metric",
  "formula": "AVG(\"transactions_1k\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_018\") FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" INNER JOIN customers AS T3 ON T1.\"XCL_013\" = T3.\"XCL_001\" WHERE T3.\"XCL_003\" = 'EUR'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      },
      {
        "role": "r1",
        "physical_table": "gasstations"
      },
      {
        "role": "r2",
        "physical_table": "customers"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_018\") AS \"value\" FROM transactions_1k AS \"r0\" INNER JOIN gasstations AS \"r1\" ON \"r0\".\"XCL_015\" = \"r1\".\"XCL_004\" INNER JOIN customers AS \"r2\" ON \"r0\".\"XCL_013\" = \"r2\".\"XCL_001\" WHERE \"r2\".\"XCL_003\" = 'EUR'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1511"
  ]
}
```

### Calculates the percentage of rows in the joined dataset (customers and yearmonth) where the value of yearmonth.XCL_021 is greater than 46.73, relative

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(\"yearmonth\".\"XCL_021\" > 46.73, 1, 0)) AS REAL) * 100 / COUNT(\"customers\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(T2.\"XCL_021\" > 46.73, 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_002\" = 'LAM'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(IIF(\"r1\".\"XCL_021\" > 46.73, 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "customers"
      },
      {
        "role": "r1",
        "physical_table": "yearmonth"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(IIF(\"r1\".\"XCL_021\" > 46.73, 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM customers AS \"r0\" INNER JOIN yearmonth AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_019\" WHERE \"r0\".\"XCL_002\" = 'LAM'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1490"
  ]
}
```

### Identifier from the transactions_1k table (T1) used to join with the yearmonth table. Represents the specific transaction record selected by the filte

```json
{
  "kind": "binding",
  "formula": "\"transactions_1k\".\"XCL_013\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_013\", T2.\"XCL_020\", T2.\"XCL_021\" FROM transactions_1k AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_013\" = T2.\"XCL_019\" WHERE T1.\"XCL_011\" = '2012-08-24' AND T1.\"XCL_018\" = 124.05 AND T2.\"XCL_020\" = '201201'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_013\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      },
      {
        "role": "r1",
        "physical_table": "yearmonth"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_013\" AS \"value\" FROM transactions_1k AS \"r0\" INNER JOIN yearmonth AS \"r1\" ON \"r0\".\"XCL_013\" = \"r1\".\"XCL_019\" WHERE \"r0\".\"XCL_011\" = '2012-08-24' AND \"r0\".\"XCL_018\" = 124.05 AND \"r1\".\"XCL_020\" = '201201'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1520"
  ]
}
```

### "yearmonth"."XCL_020" = '201309'

```json
{
  "kind": "predicate",
  "formula": "\"yearmonth\".\"XCL_020\" = '201309'",
  "grain": [
    "\"customers\".\"XCL_001\""
  ],
  "population_scope": "SELECT T1.\"XCL_001\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T2.\"XCL_020\" = '201309' GROUP BY T1.\"XCL_001\" ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1495"
  ]
}
```

### Returns the value of column XCL_016 from the transactions_1k table. The population is restricted to transactions occurring on '2012-08-23' at '21:20:0

```json
{
  "kind": "binding",
  "formula": "\"transactions_1k\".\"XCL_016\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_016\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_011\" = '2012-08-23' AND T1.\"XCL_012\" = '21:20:00'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_016\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      },
      {
        "role": "r1",
        "physical_table": "gasstations"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_016\" AS \"value\" FROM transactions_1k AS \"r0\" INNER JOIN gasstations AS \"r1\" ON \"r0\".\"XCL_015\" = \"r1\".\"XCL_004\" WHERE \"r0\".\"XCL_011\" = '2012-08-23' AND \"r0\".\"XCL_012\" = '21:20:00'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1519"
  ]
}
```

### "transactions_1k"."XCL_011" = '2012-08-25'

```json
{
  "kind": "predicate",
  "formula": "\"transactions_1k\".\"XCL_011\" = '2012-08-25'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(T2.\"XCL_003\" = 'EUR', 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_013\") FROM transactions_1k AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_013\" = T2.\"XCL_001\" WHERE T1.\"XCL_011\" = '2012-08-25'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1525"
  ]
}
```

### The customer identifier (XCL_001) of the single customer with the highest total value (SUM of XCL_021) for the specific month '201310', filtered by cu

```json
{
  "kind": "binding",
  "formula": "\"customers\".\"XCL_001\"",
  "grain": [
    "\"customers\".\"XCL_001\""
  ],
  "population_scope": "SELECT T1.\"XCL_001\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_002\" = 'LAM' AND T2.\"XCL_020\" = '201310' AND T1.\"XCL_003\" = 'EUR' GROUP BY T1.\"XCL_001\" ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1487"
  ]
}
```

### Sum of Transaction Ratio

```json
{
  "kind": "metric",
  "formula": "SUM(\"transactions_1k\".\"XCL_018\" / \"transactions_1k\".\"XCL_017\")",
  "grain": [
    "\"transactions_1k\".\"XCL_013\"",
    "\"customers\".\"XCL_003\""
  ],
  "population_scope": "SELECT T2.\"XCL_013\", SUM(T2.\"XCL_018\" / T2.\"XCL_017\"), T1.\"XCL_003\" FROM customers AS T1 INNER JOIN transactions_1k AS T2 ON T1.\"XCL_001\" = T2.\"XCL_013\" WHERE T2.\"XCL_013\" = (SELECT \"XCL_019\" FROM yearmonth ORDER BY \"XCL_021\" DESC LIMIT 1) GROUP BY T2.\"XCL_013\", T1.\"XCL_003\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1531"
  ]
}
```

### "customers"."XCL_003" = 'EUR'

```json
{
  "kind": "predicate",
  "formula": "\"customers\".\"XCL_003\" = 'EUR'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_016\", T3.\"XCL_009\" FROM transactions_1k AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_013\" = T2.\"XCL_001\" INNER JOIN products AS T3 ON T1.\"XCL_016\" = T3.\"XCL_008\" WHERE T2.\"XCL_003\" = 'EUR'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1503"
  ]
}
```

### LAM vs KAM Average Difference

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(\"customers\".\"XCL_002\" = 'LAM', \"yearmonth\".\"XCL_021\", 0)) AS REAL) / COUNT(\"customers\".\"XCL_001\") - CAST(SUM(IIF(\"customers\".\"XCL_002\" = 'KAM', \"yearmonth\".\"XCL_021\", 0)) AS REAL) / COUNT(\"customers\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(T1.\"XCL_002\" = 'SME', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\") - CAST(SUM(IIF(T1.\"XCL_002\" = 'LAM', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\"), CAST(SUM(IIF(T1.\"XCL_002\" = 'LAM', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\") - CAST(SUM(IIF(T1.\"XCL_002\" = 'KAM', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\"), CAST(SUM(IIF(T1.\"XCL_002\" = 'KAM', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\") - CAST(SUM(IIF(T1.\"XCL_002\" = 'SME', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\") FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_003\" = 'CZK' AND T2.\"XCL_021\" = (SELECT MIN(\"XCL_021\") FROM yearmonth) AND T2.\"XCL_020\" BETWEEN 201301 AND 201312",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1481"
  ]
}
```

### "transactions_1k"."XCL_011" = '2012-08-24' AND "transactions_1k"."XCL_018" = 548.4

```json
{
  "kind": "predicate",
  "formula": "\"transactions_1k\".\"XCL_011\" = '2012-08-24' AND \"transactions_1k\".\"XCL_018\" = 548.4",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_011\" = '2012-08-24' AND T1.\"XCL_018\" = 548.4",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1524"
  ]
}
```

### The "XCL_013" column from "transactions_1k", representing the period identifier for each transaction. It is filtered to match the latest year-month an

```json
{
  "kind": "binding",
  "formula": "\"transactions_1k\".\"XCL_013\"",
  "grain": [
    "\"transactions_1k\".\"XCL_013\"",
    "\"customers\".\"XCL_003\""
  ],
  "population_scope": "SELECT T2.\"XCL_013\", SUM(T2.\"XCL_018\" / T2.\"XCL_017\"), T1.\"XCL_003\" FROM customers AS T1 INNER JOIN transactions_1k AS T2 ON T1.\"XCL_001\" = T2.\"XCL_013\" WHERE T2.\"XCL_013\" = (SELECT \"XCL_019\" FROM yearmonth ORDER BY \"XCL_021\" DESC LIMIT 1) GROUP BY T2.\"XCL_013\", T1.\"XCL_003\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1531"
  ]
}
```

### Aggregated count of transaction records (identified by XCL_010) from the transactions_1k table. The population is restricted to transactions linked to

```json
{
  "kind": "metric",
  "formula": "COUNT(\"transactions_1k\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_010\") FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T2.\"XCL_006\" = 'CZE' AND STRFTIME('%Y', T1.\"XCL_011\") >= '2012'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      },
      {
        "role": "r1",
        "physical_table": "gasstations"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_010\") AS \"value\" FROM transactions_1k AS \"r0\" INNER JOIN gasstations AS \"r1\" ON \"r0\".\"XCL_015\" = \"r1\".\"XCL_004\" WHERE \"r1\".\"XCL_006\" = 'CZE' AND STRFTIME('%Y', \"r0\".\"XCL_011\") >= '2012'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1509"
  ]
}
```

### "transactions_1k"."XCL_011" = '2012-08-25'

```json
{
  "kind": "predicate",
  "formula": "\"transactions_1k\".\"XCL_011\" = '2012-08-25'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_011\" = '2012-08-25' ORDER BY T1.\"XCL_012\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1513"
  ]
}
```

### "gasstations"."XCL_007" = 'Value for money'

```json
{
  "kind": "predicate",
  "formula": "\"gasstations\".\"XCL_007\" = 'Value for money'",
  "grain": [
    "\"gasstations\".\"XCL_006\""
  ],
  "population_scope": "SELECT \"XCL_006\", (SELECT COUNT(\"XCL_004\") FROM gasstations WHERE \"XCL_007\" = 'Value for money') FROM gasstations WHERE \"XCL_007\" = 'Value for money' GROUP BY \"XCL_006\" ORDER BY COUNT(\"XCL_004\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1491"
  ]
}
```

### Customer Identifier

```json
{
  "kind": "binding",
  "formula": "\"customers\".\"XCL_001\"",
  "grain": [
    "\"customers\".\"XCL_001\""
  ],
  "population_scope": "SELECT T1.\"XCL_001\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T2.\"XCL_020\" = '201206' AND T1.\"XCL_002\" = 'SME' GROUP BY T1.\"XCL_001\" ORDER BY SUM(T2.\"XCL_021\") ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1497"
  ]
}
```

### The customer identifier (XCL_001) from the customers table that has the highest aggregated sum of XCL_021 in the yearmonth table for the specific peri

```json
{
  "kind": "binding",
  "formula": "\"customers\".\"XCL_001\"",
  "grain": [
    "\"customers\".\"XCL_001\""
  ],
  "population_scope": "SELECT T1.\"XCL_001\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T2.\"XCL_020\" = '201309' GROUP BY T1.\"XCL_001\" ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1495"
  ]
}
```

### Average XCL_017 for January 2012

```json
{
  "kind": "metric",
  "formula": "AVG(\"transactions_1k\".\"XCL_017\")",
  "grain": [],
  "population_scope": "SELECT AVG(\"XCL_017\") FROM transactions_1k WHERE \"XCL_011\" LIKE '2012-01%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_017\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_017\") AS \"value\" FROM transactions_1k AS \"r0\" WHERE \"r0\".\"XCL_011\" LIKE '2012-01%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1504"
  ]
}
```

### "customers"."XCL_003" = 'EUR' AND "yearmonth"."XCL_021" > 1000.00

```json
{
  "kind": "predicate",
  "formula": "\"customers\".\"XCL_003\" = 'EUR' AND \"yearmonth\".\"XCL_021\" > 1000.00",
  "grain": [],
  "population_scope": "SELECT COUNT(*) FROM yearmonth AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_019\" = T2.\"XCL_001\" WHERE T2.\"XCL_003\" = 'EUR' AND T1.\"XCL_021\" > 1000.00",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1505"
  ]
}
```

### Grouping Key XCL_006

```json
{
  "kind": "binding",
  "formula": "\"gasstations\".\"XCL_006\"",
  "grain": [
    "\"gasstations\".\"XCL_006\""
  ],
  "population_scope": "SELECT \"XCL_006\", (SELECT COUNT(\"XCL_004\") FROM gasstations WHERE \"XCL_007\" = 'Value for money') FROM gasstations WHERE \"XCL_007\" = 'Value for money' GROUP BY \"XCL_006\" ORDER BY COUNT(\"XCL_004\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1491"
  ]
}
```

### "customers"."XCL_002" = 'LAM'

```json
{
  "kind": "predicate",
  "formula": "\"customers\".\"XCL_002\" = 'LAM'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(T2.\"XCL_021\" > 46.73, 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_002\" = 'LAM'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1490"
  ]
}
```

### "customers"."XCL_002" = 'KAM'

```json
{
  "kind": "predicate",
  "formula": "\"customers\".\"XCL_002\" = 'KAM'",
  "grain": [
    "\"yearmonth\".\"XCL_019\""
  ],
  "population_scope": "SELECT T2.\"XCL_019\", SUM(T2.\"XCL_021\") FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_002\" = 'KAM' GROUP BY T2.\"XCL_019\" ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1488"
  ]
}
```

### "gasstations"."XCL_006" = 'CZE' AND "transactions_1k"."XCL_018" > 1000

```json
{
  "kind": "predicate",
  "formula": "\"gasstations\".\"XCL_006\" = 'CZE' AND \"transactions_1k\".\"XCL_018\" > 1000",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_010\") FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T2.\"XCL_006\" = 'CZE' AND T1.\"XCL_018\" > 1000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1508"
  ]
}
```

### The single month (derived from positions 5-6 of yearmonth.XCL_020) with the highest sum of yearmonth.XCL_021, restricted to customers where customers.

```json
{
  "kind": "binding",
  "formula": "SUBSTRING(\"yearmonth\".\"XCL_020\", 5, 2)",
  "grain": [
    "SUBSTRING(\"yearmonth\".\"XCL_020\", 5, 2)"
  ],
  "population_scope": "SELECT SUBSTRING(T2.\"XCL_020\", 5, 2) FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE SUBSTRING(T2.\"XCL_020\", 1, 4) = '2013' AND T1.\"XCL_002\" = 'SME' GROUP BY SUBSTRING(T2.\"XCL_020\", 5, 2) ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1480"
  ]
}
```

### Calculates the percentage of rows in the gasstations table where XCL_006 is 'SVK' and XCL_007 is 'Premium', relative to the total count of rows where 

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(\"gasstations\".\"XCL_006\" = 'SVK' AND \"gasstations\".\"XCL_007\" = 'Premium', 1, 0)) AS REAL) * 100 / SUM(IIF(\"gasstations\".\"XCL_006\" = 'SVK', 1, 0))",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(\"XCL_006\" = 'SVK' AND \"XCL_007\" = 'Premium', 1, 0)) AS REAL) * 100 / SUM(IIF(\"XCL_006\" = 'SVK', 1, 0)) FROM gasstations",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(IIF(\"r0\".\"XCL_006\" = 'SVK' AND \"r0\".\"XCL_007\" = 'Premium', 1, 0)) AS REAL) * 100 / SUM(IIF(\"r0\".\"XCL_006\" = 'SVK', 1, 0))",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "gasstations"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(IIF(\"r0\".\"XCL_006\" = 'SVK' AND \"r0\".\"XCL_007\" = 'Premium', 1, 0)) AS REAL) * 100 / SUM(IIF(\"r0\".\"XCL_006\" = 'SVK', 1, 0)) AS \"value\" FROM gasstations AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1528"
  ]
}
```

### The customer identifier (XCL_019) from the yearmonth table that corresponds to the highest aggregated value of XCL_021 among customers classified as '

```json
{
  "kind": "binding",
  "formula": "\"yearmonth\".\"XCL_019\"",
  "grain": [
    "\"yearmonth\".\"XCL_019\""
  ],
  "population_scope": "SELECT T2.\"XCL_019\", SUM(T2.\"XCL_021\") FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_002\" = 'KAM' GROUP BY T2.\"XCL_019\" ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1488"
  ]
}
```

### Average monthly consumption calculated by summing the 'XCL_021' values from the 'yearmonth' table and dividing by 12. The calculation is performed for

```json
{
  "kind": "metric",
  "formula": "SUM(\"yearmonth\".\"XCL_021\") / 12",
  "grain": [
    "\"customers\".\"XCL_001\""
  ],
  "population_scope": "SELECT SUM(T2.\"XCL_021\") / 12 AS MonthlyConsumption FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_003\" = 'EUR' GROUP BY T1.\"XCL_001\" ORDER BY MonthlyConsumption DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1499"
  ]
}
```

### Customer Attribute XCL_002

```json
{
  "kind": "binding",
  "formula": "\"customers\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_002\" FROM transactions_1k AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_013\" = T2.\"XCL_001\" ORDER BY \"XCL_011\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1517"
  ]
}
```

### Average XCL_018 for Czech Gasstations

```json
{
  "kind": "metric",
  "formula": "AVG(\"transactions_1k\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_018\") FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T2.\"XCL_006\" = 'CZE'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      },
      {
        "role": "r1",
        "physical_table": "gasstations"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_018\") AS \"value\" FROM transactions_1k AS \"r0\" INNER JOIN gasstations AS \"r1\" ON \"r0\".\"XCL_015\" = \"r1\".\"XCL_004\" WHERE \"r1\".\"XCL_006\" = 'CZE'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1510"
  ]
}
```

### The value of column XCL_013 from the transactions_1k table that corresponds to the highest sum of XCL_018 for transactions dated 2012-08-25. The grain

```json
{
  "kind": "binding",
  "formula": "\"transactions_1k\".\"XCL_013\"",
  "grain": [
    "\"transactions_1k\".\"XCL_013\""
  ],
  "population_scope": "SELECT \"XCL_013\" FROM transactions_1k WHERE \"XCL_011\" = '2012-08-25' GROUP BY \"XCL_013\" ORDER BY SUM(\"XCL_018\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1512"
  ]
}
```

### Gasstation Attribute XCL_006

```json
{
  "kind": "binding",
  "formula": "\"gasstations\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_014\" = '667467'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      },
      {
        "role": "r1",
        "physical_table": "gasstations"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_006\" AS \"value\" FROM transactions_1k AS \"r0\" INNER JOIN gasstations AS \"r1\" ON \"r0\".\"XCL_015\" = \"r1\".\"XCL_004\" WHERE \"r0\".\"XCL_014\" = '667467'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1523"
  ]
}
```

### "gasstations"."XCL_007" = 'Value for money'

```json
{
  "kind": "predicate",
  "formula": "\"gasstations\".\"XCL_007\" = 'Value for money'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_004\") FROM gasstations WHERE \"XCL_007\" = 'Value for money'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1491"
  ]
}
```

### SME vs LAM Average Difference

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(\"customers\".\"XCL_002\" = 'SME', \"yearmonth\".\"XCL_021\", 0)) AS REAL) / COUNT(\"customers\".\"XCL_001\") - CAST(SUM(IIF(\"customers\".\"XCL_002\" = 'LAM', \"yearmonth\".\"XCL_021\", 0)) AS REAL) / COUNT(\"customers\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(T1.\"XCL_002\" = 'SME', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\") - CAST(SUM(IIF(T1.\"XCL_002\" = 'LAM', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\"), CAST(SUM(IIF(T1.\"XCL_002\" = 'LAM', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\") - CAST(SUM(IIF(T1.\"XCL_002\" = 'KAM', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\"), CAST(SUM(IIF(T1.\"XCL_002\" = 'KAM', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\") - CAST(SUM(IIF(T1.\"XCL_002\" = 'SME', T2.\"XCL_021\", 0)) AS REAL) / COUNT(T1.\"XCL_001\") FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_003\" = 'CZK' AND T2.\"XCL_021\" = (SELECT MIN(\"XCL_021\") FROM yearmonth) AND T2.\"XCL_020\" BETWEEN 201301 AND 201312",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1481"
  ]
}
```

### Aggregated sum of the XCL_021 column from the yearmonth table, filtered to records where XCL_019 equals 6 and XCL_020 is between '201308' and '201311'

```json
{
  "kind": "metric",
  "formula": "SUM(\"yearmonth\".\"XCL_021\")",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_021\") FROM yearmonth WHERE \"XCL_019\" = 6 AND \"XCL_020\" BETWEEN '201308' AND '201311'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r0\".\"XCL_021\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "yearmonth"
      }
    ],
    "scope_sql": "SELECT SUM(\"r0\".\"XCL_021\") AS \"value\" FROM yearmonth AS \"r0\" WHERE \"r0\".\"XCL_019\" = 6 AND \"r0\".\"XCL_020\" BETWEEN '201308' AND '201311'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1483"
  ]
}
```

### Gasstation Identifier

```json
{
  "kind": "binding",
  "formula": "\"gasstations\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_011\" = '2012-08-24' AND T1.\"XCL_012\" = '12:42:00'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      },
      {
        "role": "r1",
        "physical_table": "gasstations"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_006\" AS \"value\" FROM transactions_1k AS \"r0\" INNER JOIN gasstations AS \"r1\" ON \"r0\".\"XCL_015\" = \"r1\".\"XCL_004\" WHERE \"r0\".\"XCL_011\" = '2012-08-24' AND \"r0\".\"XCL_012\" = '12:42:00'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1518"
  ]
}
```

### "yearmonth"."XCL_020" = '201206' AND "customers"."XCL_002" = 'SME'

```json
{
  "kind": "predicate",
  "formula": "\"yearmonth\".\"XCL_020\" = '201206' AND \"customers\".\"XCL_002\" = 'SME'",
  "grain": [
    "\"customers\".\"XCL_001\""
  ],
  "population_scope": "SELECT T1.\"XCL_001\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T2.\"XCL_020\" = '201206' AND T1.\"XCL_002\" = 'SME' GROUP BY T1.\"XCL_001\" ORDER BY SUM(T2.\"XCL_021\") ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1497"
  ]
}
```

### KAM Year-over-Year Growth Rate

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(\"customers\".\"XCL_002\" = 'KAM' AND \"yearmonth\".\"XCL_020\" LIKE '2013%', \"yearmonth\".\"XCL_021\", 0)) - SUM(IIF(\"customers\".\"XCL_002\" = 'KAM' AND \"yearmonth\".\"XCL_020\" LIKE '2012%', \"yearmonth\".\"XCL_021\", 0)) AS REAL) * 100 / SUM(IIF(\"customers\".\"XCL_002\" = 'KAM' AND \"yearmonth\".\"XCL_020\" LIKE '2012%', \"yearmonth\".\"XCL_021\", 0))",
  "grain": [],
  "population_scope": "SELECT CAST((SUM(IIF(T1.\"XCL_002\" = 'SME' AND T2.\"XCL_020\" LIKE '2013%', T2.\"XCL_021\", 0)) - SUM(IIF(T1.\"XCL_002\" = 'SME' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0))) AS REAL) * 100 / SUM(IIF(T1.\"XCL_002\" = 'SME' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0)), CAST(SUM(IIF(T1.\"XCL_002\" = 'LAM' AND T2.\"XCL_020\" LIKE '2013%', T2.\"XCL_021\", 0)) - SUM(IIF(T1.\"XCL_002\" = 'LAM' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0)) AS REAL) * 100 / SUM(IIF(T1.\"XCL_002\" = 'LAM' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0)), CAST(SUM(IIF(T1.\"XCL_002\" = 'KAM' AND T2.\"XCL_020\" LIKE '2013%', T2.\"XCL_021\", 0)) - SUM(IIF(T1.\"XCL_002\" = 'KAM' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0)) AS REAL) * 100 / SUM(IIF(T1.\"XCL_002\" = 'KAM' AND T2.\"XCL_020\" LIKE '2012%', T2.\"XCL_021\", 0)) FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(IIF(\"r0\".\"XCL_002\" = 'KAM' AND \"r1\".\"XCL_020\" LIKE '2013%', \"r1\".\"XCL_021\", 0)) - SUM(IIF(\"r0\".\"XCL_002\" = 'KAM' AND \"r1\".\"XCL_020\" LIKE '2012%', \"r1\".\"XCL_021\", 0)) AS REAL) * 100 / SUM(IIF(\"r0\".\"XCL_002\" = 'KAM' AND \"r1\".\"XCL_020\" LIKE '2012%', \"r1\".\"XCL_021\", 0))",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "customers"
      },
      {
        "role": "r1",
        "physical_table": "yearmonth"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(IIF(\"r0\".\"XCL_002\" = 'KAM' AND \"r1\".\"XCL_020\" LIKE '2013%', \"r1\".\"XCL_021\", 0)) - SUM(IIF(\"r0\".\"XCL_002\" = 'KAM' AND \"r1\".\"XCL_020\" LIKE '2012%', \"r1\".\"XCL_021\", 0)) AS REAL) * 100 / SUM(IIF(\"r0\".\"XCL_002\" = 'KAM' AND \"r1\".\"XCL_020\" LIKE '2012%', \"r1\".\"XCL_021\", 0)) AS \"value\" FROM customers AS \"r0\" INNER JOIN yearmonth AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_019\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1482"
  ]
}
```

### The single year (first 4 characters of XCL_020) with the highest sum of XCL_021 for customers where XCL_003 is 'EUR'. Grain is one row representing th

```json
{
  "kind": "binding",
  "formula": "SUBSTRING(\"yearmonth\".\"XCL_020\", 1, 4)",
  "grain": [
    "SUBSTRING(\"yearmonth\".\"XCL_020\", 1, 4)"
  ],
  "population_scope": "SELECT SUBSTRING(T2.\"XCL_020\", 1, 4) FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_003\" = 'EUR' GROUP BY SUBSTRING(T2.\"XCL_020\", 1, 4) ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1477"
  ]
}
```

### Aggregated sum of the transaction value field (XCL_018) from the transactions_1k table. The population is restricted to transactions where the year-mo

```json
{
  "kind": "metric",
  "formula": "SUM(\"transactions_1k\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT SUM(T1.\"XCL_018\"), SUM(IIF(T3.\"XCL_020\" = '201201', T1.\"XCL_018\", 0)) FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" INNER JOIN yearmonth AS T3 ON T1.\"XCL_013\" = T3.\"XCL_019\" WHERE T1.\"XCL_013\" = '38508'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      },
      {
        "role": "r1",
        "physical_table": "gasstations"
      },
      {
        "role": "r2",
        "physical_table": "yearmonth"
      }
    ],
    "scope_sql": "SELECT SUM(\"r0\".\"XCL_018\") AS \"value\" FROM transactions_1k AS \"r0\" INNER JOIN gasstations AS \"r1\" ON \"r0\".\"XCL_015\" = \"r1\".\"XCL_004\" INNER JOIN yearmonth AS \"r2\" ON \"r0\".\"XCL_013\" = \"r2\".\"XCL_019\" WHERE \"r0\".\"XCL_013\" = '38508'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1529"
  ]
}
```

### "transactions_1k"."XCL_011" = '2012-08-26' AND "transactions_1k"."XCL_012" BETWEEN '08:00:00' AND '09:00:00' AND "gasstations"."XCL_006" = 'CZE'

```json
{
  "kind": "predicate",
  "formula": "\"transactions_1k\".\"XCL_011\" = '2012-08-26' AND \"transactions_1k\".\"XCL_012\" BETWEEN '08:00:00' AND '09:00:00' AND \"gasstations\".\"XCL_006\" = 'CZE'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_010\") FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_011\" = '2012-08-26' AND T1.\"XCL_012\" BETWEEN '08:00:00' AND '09:00:00' AND T2.\"XCL_006\" = 'CZE'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1521"
  ]
}
```

### "customers"."XCL_003" = 'EUR'

```json
{
  "kind": "predicate",
  "formula": "\"customers\".\"XCL_003\" = 'EUR'",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_018\") FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" INNER JOIN customers AS T3 ON T1.\"XCL_013\" = T3.\"XCL_001\" WHERE T3.\"XCL_003\" = 'EUR'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1511"
  ]
}
```

### Aggregates the count of column XCL_004 from the gasstations table where XCL_007 equals 'Value for money'. This metric is used to rank groups by the vo

```json
{
  "kind": "metric",
  "formula": "COUNT(\"gasstations\".\"XCL_004\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_004\") FROM gasstations WHERE \"XCL_007\" = 'Value for money'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_004\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "gasstations"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_004\") AS \"value\" FROM gasstations AS \"r0\" WHERE \"r0\".\"XCL_007\" = 'Value for money'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1491"
  ]
}
```

### The product identifier (XCL_016) from the transactions_1k table. In this context, it represents the specific products associated with transactions mad

```json
{
  "kind": "binding",
  "formula": "\"transactions_1k\".\"XCL_016\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_016\", T3.\"XCL_009\" FROM transactions_1k AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_013\" = T2.\"XCL_001\" INNER JOIN products AS T3 ON T1.\"XCL_016\" = T3.\"XCL_008\" WHERE T2.\"XCL_003\" = 'EUR'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1503"
  ]
}
```

### "yearmonth"."XCL_020" = '201305' AND "customers"."XCL_002" = 'KAM'

```json
{
  "kind": "predicate",
  "formula": "\"yearmonth\".\"XCL_020\" = '201305' AND \"customers\".\"XCL_002\" = 'KAM'",
  "grain": [],
  "population_scope": "SELECT SUM(T2.\"XCL_021\") FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T2.\"XCL_020\" = '201305' AND T1.\"XCL_002\" = 'KAM'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1489"
  ]
}
```

### "gasstations"."XCL_006" = 'CZE'

```json
{
  "kind": "predicate",
  "formula": "\"gasstations\".\"XCL_006\" = 'CZE'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_009\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" INNER JOIN products AS T3 ON T1.\"XCL_016\" = T3.\"XCL_008\" WHERE T2.\"XCL_006\" = 'CZE'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1506"
  ]
}
```

### "yearmonth"."XCL_020" = '201202'

```json
{
  "kind": "predicate",
  "formula": "\"yearmonth\".\"XCL_020\" = '201202'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(\"XCL_021\" > 528.3, 1, 0)) AS REAL) * 100 / COUNT(\"XCL_019\") FROM yearmonth WHERE \"XCL_020\" = '201202'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1493"
  ]
}
```

### EUR to CZK customer count ratio

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(\"customers\".\"XCL_003\" = 'EUR', 1, 0)) AS REAL) / SUM(IIF(\"customers\".\"XCL_003\" = 'CZK', 1, 0))",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(\"XCL_003\" = 'EUR', 1, 0)) AS REAL) / SUM(IIF(\"XCL_003\" = 'CZK', 1, 0)) AS ratio FROM customers",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(IIF(\"r0\".\"XCL_003\" = 'EUR', 1, 0)) AS REAL) / SUM(IIF(\"r0\".\"XCL_003\" = 'CZK', 1, 0))",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "customers"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(IIF(\"r0\".\"XCL_003\" = 'EUR', 1, 0)) AS REAL) / SUM(IIF(\"r0\".\"XCL_003\" = 'CZK', 1, 0)) AS \"value\" FROM customers AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1471"
  ]
}
```

### A deduplicated list of values from the 'XCL_012' column in the 'transactions_1k' table. The population is restricted to transactions that have a corre

```json
{
  "kind": "binding",
  "formula": "\"transactions_1k\".\"XCL_012\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_012\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T2.\"XCL_005\" = 11",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1507"
  ]
}
```

### "yearmonth"."XCL_019" = 6 AND "yearmonth"."XCL_020" BETWEEN '201308' AND '201311'

```json
{
  "kind": "predicate",
  "formula": "\"yearmonth\".\"XCL_019\" = 6 AND \"yearmonth\".\"XCL_020\" BETWEEN '201308' AND '201311'",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_021\") FROM yearmonth WHERE \"XCL_019\" = 6 AND \"XCL_020\" BETWEEN '201308' AND '201311'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1483"
  ]
}
```

### "gasstations"."XCL_005" = 11

```json
{
  "kind": "predicate",
  "formula": "\"gasstations\".\"XCL_005\" = 11",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_012\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T2.\"XCL_005\" = 11",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1507"
  ]
}
```

### Target Entity Identifier

```json
{
  "kind": "binding",
  "formula": "\"transactions_1k\".\"XCL_013\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_013\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_011\" = '2012-08-25' AND T1.\"XCL_018\" = 634.8",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_013\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      },
      {
        "role": "r1",
        "physical_table": "gasstations"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_013\" AS \"value\" FROM transactions_1k AS \"r0\" INNER JOIN gasstations AS \"r1\" ON \"r0\".\"XCL_015\" = \"r1\".\"XCL_004\" WHERE \"r0\".\"XCL_011\" = '2012-08-25' AND \"r0\".\"XCL_018\" = 634.8",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1526"
  ]
}
```

### "gasstations"."XCL_006" = 'CZE'

```json
{
  "kind": "predicate",
  "formula": "\"gasstations\".\"XCL_006\" = 'CZE'",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_018\") FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T2.\"XCL_006\" = 'CZE'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1510"
  ]
}
```

### Minimum Yearmonth Identifier

```json
{
  "kind": "metric",
  "formula": "MIN(\"yearmonth\".\"XCL_021\")",
  "grain": [],
  "population_scope": "SELECT MIN(\"XCL_021\") FROM yearmonth",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MIN(\"r0\".\"XCL_021\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "yearmonth"
      }
    ],
    "scope_sql": "SELECT MIN(\"r0\".\"XCL_021\") AS \"value\" FROM yearmonth AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1481"
  ]
}
```

### Average Monthly XCL_021 for SME Customers in 2013

```json
{
  "kind": "metric",
  "formula": "AVG(\"yearmonth\".\"XCL_021\") / 12",
  "grain": [],
  "population_scope": "SELECT AVG(T2.\"XCL_021\") / 12 FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE SUBSTRING(T2.\"XCL_020\", 1, 4) = '2013' AND T1.\"XCL_002\" = 'SME'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r1\".\"XCL_021\") / 12",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "customers"
      },
      {
        "role": "r1",
        "physical_table": "yearmonth"
      }
    ],
    "scope_sql": "SELECT AVG(\"r1\".\"XCL_021\") / 12 AS \"value\" FROM customers AS \"r0\" INNER JOIN yearmonth AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_019\" WHERE SUBSTRING(\"r1\".\"XCL_020\", 1, 4) = '2013' AND \"r0\".\"XCL_002\" = 'SME'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1473"
  ]
}
```

### Customer Identifier

```json
{
  "kind": "binding",
  "formula": "\"customers\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_003\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" INNER JOIN customers AS T3 ON T1.\"XCL_013\" = T3.\"XCL_001\" WHERE T1.\"XCL_011\" = '2012-08-24' AND T1.\"XCL_012\" = '16:25:00'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1514"
  ]
}
```

### "customers"."XCL_002" = 'KAM'

```json
{
  "kind": "predicate",
  "formula": "\"customers\".\"XCL_002\" = 'KAM'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(\"XCL_003\" = 'EUR') AS REAL) * 100 / COUNT(\"XCL_001\") FROM customers WHERE \"XCL_002\" = 'KAM'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1492"
  ]
}
```

### "transactions_1k"."XCL_011" = '2012-08-26' AND "transactions_1k"."XCL_012" < '13:00:00' AND "customers"."XCL_003" = 'CZK'

```json
{
  "kind": "predicate",
  "formula": "\"transactions_1k\".\"XCL_011\" = '2012-08-26' AND \"transactions_1k\".\"XCL_012\" < '13:00:00' AND \"customers\".\"XCL_003\" = 'CZK'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_010\") FROM transactions_1k AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_013\" = T2.\"XCL_001\" WHERE T1.\"XCL_011\" = '2012-08-26' AND T1.\"XCL_012\" < '13:00:00' AND T2.\"XCL_003\" = 'CZK'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1516"
  ]
}
```

### "transactions_1k"."XCL_011" = '2012-08-24' AND "transactions_1k"."XCL_018" = 124.05 AND "yearmonth"."XCL_020" = '201201'

```json
{
  "kind": "predicate",
  "formula": "\"transactions_1k\".\"XCL_011\" = '2012-08-24' AND \"transactions_1k\".\"XCL_018\" = 124.05 AND \"yearmonth\".\"XCL_020\" = '201201'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_013\", T2.\"XCL_020\", T2.\"XCL_021\" FROM transactions_1k AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_013\" = T2.\"XCL_019\" WHERE T1.\"XCL_011\" = '2012-08-24' AND T1.\"XCL_018\" = 124.05 AND T2.\"XCL_020\" = '201201'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1520"
  ]
}
```

### Customer Identifier

```json
{
  "kind": "binding",
  "formula": "\"customers\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_002\" FROM transactions_1k AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_013\" = T2.\"XCL_001\" WHERE T1.\"XCL_011\" = '2012-08-23' AND T1.\"XCL_012\" = '21:20:00'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_002\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "transactions_1k"
      },
      {
        "role": "r1",
        "physical_table": "customers"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_002\" AS \"value\" FROM transactions_1k AS \"r0\" INNER JOIN customers AS \"r1\" ON \"r0\".\"XCL_013\" = \"r1\".\"XCL_001\" WHERE \"r0\".\"XCL_011\" = '2012-08-23' AND \"r0\".\"XCL_012\" = '21:20:00'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1515"
  ]
}
```

### "yearmonth"."XCL_020" = '201306' AND "yearmonth"."XCL_021" = 214582.17

```json
{
  "kind": "predicate",
  "formula": "\"yearmonth\".\"XCL_020\" = '201306' AND \"yearmonth\".\"XCL_021\" = 214582.17",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM yearmonth AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_019\" = T2.\"XCL_001\" WHERE T1.\"XCL_020\" = '201306' AND T1.\"XCL_021\" = 214582.17",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1522"
  ]
}
```

### Gasstation Identifier

```json
{
  "kind": "binding",
  "formula": "\"gasstations\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T1.\"XCL_011\" = '2012-08-25' ORDER BY T1.\"XCL_012\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1513"
  ]
}
```

### Product Attribute XCL_009

```json
{
  "kind": "binding",
  "formula": "\"products\".\"XCL_009\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_009\" FROM transactions_1k AS T1 INNER JOIN products AS T2 ON T1.\"XCL_016\" = T2.\"XCL_008\" ORDER BY T1.\"XCL_017\" DESC LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1530"
  ]
}
```

### Calculates the percentage of rows where the attribute 'XCL_007' equals 'Premium' relative to the total count of 'XCL_004' entries, restricted to gasst

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(\"gasstations\".\"XCL_007\" = 'Premium', 1, 0)) AS REAL) * 100 / COUNT(\"gasstations\".\"XCL_004\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(\"XCL_007\" = 'Premium', 1, 0)) AS REAL) * 100 / COUNT(\"XCL_004\") FROM gasstations WHERE \"XCL_006\" = 'SVK'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(IIF(\"r0\".\"XCL_007\" = 'Premium', 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_004\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "gasstations"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(IIF(\"r0\".\"XCL_007\" = 'Premium', 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_004\") AS \"value\" FROM gasstations AS \"r0\" WHERE \"r0\".\"XCL_006\" = 'SVK'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1494"
  ]
}
```

### Aggregated Year-Month Metric

```json
{
  "kind": "metric",
  "formula": "SUM(\"yearmonth\".\"XCL_021\")",
  "grain": [
    "\"yearmonth\".\"XCL_019\""
  ],
  "population_scope": "SELECT T2.\"XCL_019\", SUM(T2.\"XCL_021\") FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_002\" = 'KAM' GROUP BY T2.\"XCL_019\" ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1488"
  ]
}
```

### Customer Identifier

```json
{
  "kind": "binding",
  "formula": "\"customers\".\"XCL_003\"",
  "grain": [
    "\"transactions_1k\".\"XCL_013\"",
    "\"customers\".\"XCL_003\""
  ],
  "population_scope": "SELECT T2.\"XCL_013\", SUM(T2.\"XCL_018\" / T2.\"XCL_017\"), T1.\"XCL_003\" FROM customers AS T1 INNER JOIN transactions_1k AS T2 ON T1.\"XCL_001\" = T2.\"XCL_013\" WHERE T2.\"XCL_013\" = (SELECT \"XCL_019\" FROM yearmonth ORDER BY \"XCL_021\" DESC LIMIT 1) GROUP BY T2.\"XCL_013\", T1.\"XCL_003\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1531"
  ]
}
```

### "transactions_1k"."XCL_011" LIKE '2012-01%'

```json
{
  "kind": "predicate",
  "formula": "\"transactions_1k\".\"XCL_011\" LIKE '2012-01%'",
  "grain": [],
  "population_scope": "SELECT AVG(\"XCL_017\") FROM transactions_1k WHERE \"XCL_011\" LIKE '2012-01%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1504"
  ]
}
```

### The single value of XCL_015 from the transactions_1k table that has the highest total sum of XCL_018. The grain is one row representing the top-ranked

```json
{
  "kind": "binding",
  "formula": "\"transactions_1k\".\"XCL_015\"",
  "grain": [
    "\"transactions_1k\".\"XCL_015\""
  ],
  "population_scope": "SELECT \"XCL_015\" FROM transactions_1k GROUP BY \"XCL_015\" ORDER BY SUM(\"XCL_018\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1527"
  ]
}
```

### A deduplicated list of product identifiers (XCL_009) from the products table. The population is restricted to products that have at least one transact

```json
{
  "kind": "binding",
  "formula": "\"products\".\"XCL_009\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_009\" FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" INNER JOIN products AS T3 ON T1.\"XCL_016\" = T3.\"XCL_008\" WHERE T2.\"XCL_006\" = 'CZE'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1506"
  ]
}
```

### Customer Identifier

```json
{
  "kind": "binding",
  "formula": "\"customers\".\"XCL_001\"",
  "grain": [
    "\"customers\".\"XCL_001\""
  ],
  "population_scope": "SELECT T1.\"XCL_001\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_002\" = 'LAM' AND SUBSTRING(T2.\"XCL_020\", 1, 4) = '2012' GROUP BY T1.\"XCL_001\" ORDER BY SUM(T2.\"XCL_021\") ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1472"
  ]
}
```

### The 4-character year prefix extracted from the yearmonth table's XCL_020 field. This value represents the single year with the highest aggregated sum 

```json
{
  "kind": "binding",
  "formula": "SUBSTRING(\"yearmonth\".\"XCL_020\", 1, 4)",
  "grain": [
    "SUBSTRING(\"yearmonth\".\"XCL_020\", 1, 4)"
  ],
  "population_scope": "SELECT SUBSTRING(T2.\"XCL_020\", 1, 4) FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_003\" = 'CZK' GROUP BY SUBSTRING(T2.\"XCL_020\", 1, 4) ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1479"
  ]
}
```

### Aggregated sum of the 'XCL_021' column from the 'yearmonth' table, filtered to records where 'XCL_020' is '201305' and joined to 'customers' where 'XC

```json
{
  "kind": "metric",
  "formula": "SUM(\"yearmonth\".\"XCL_021\")",
  "grain": [],
  "population_scope": "SELECT SUM(T2.\"XCL_021\") FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T2.\"XCL_020\" = '201305' AND T1.\"XCL_002\" = 'KAM'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r1\".\"XCL_021\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "customers"
      },
      {
        "role": "r1",
        "physical_table": "yearmonth"
      }
    ],
    "scope_sql": "SELECT SUM(\"r1\".\"XCL_021\") AS \"value\" FROM customers AS \"r0\" INNER JOIN yearmonth AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_019\" WHERE \"r1\".\"XCL_020\" = '201305' AND \"r0\".\"XCL_002\" = 'KAM'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1489"
  ]
}
```

### "customers"."XCL_002" = 'LAM' AND SUBSTRING("yearmonth"."XCL_020", 1, 4) = '2012'

```json
{
  "kind": "predicate",
  "formula": "\"customers\".\"XCL_002\" = 'LAM' AND SUBSTRING(\"yearmonth\".\"XCL_020\", 1, 4) = '2012'",
  "grain": [
    "\"customers\".\"XCL_001\""
  ],
  "population_scope": "SELECT T1.\"XCL_001\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_002\" = 'LAM' AND SUBSTRING(T2.\"XCL_020\", 1, 4) = '2012' GROUP BY T1.\"XCL_001\" ORDER BY SUM(T2.\"XCL_021\") ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1472"
  ]
}
```

### "customers"."XCL_003" = 'EUR'

```json
{
  "kind": "predicate",
  "formula": "\"customers\".\"XCL_003\" = 'EUR'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_005\" FROM transactions_1k AS T1 INNER JOIN customers AS T2 ON T1.\"XCL_013\" = T2.\"XCL_001\" INNER JOIN gasstations AS T3 ON T1.\"XCL_015\" = T3.\"XCL_004\" WHERE T2.\"XCL_003\" = 'EUR'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1502"
  ]
}
```

### "customers"."XCL_003" = 'CZK' AND "yearmonth"."XCL_020" BETWEEN 201101 AND 201112

```json
{
  "kind": "predicate",
  "formula": "\"customers\".\"XCL_003\" = 'CZK' AND \"yearmonth\".\"XCL_020\" BETWEEN 201101 AND 201112",
  "grain": [
    "\"customers\".\"XCL_001\""
  ],
  "population_scope": "SELECT T1.\"XCL_001\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_003\" = 'CZK' AND T2.\"XCL_020\" BETWEEN 201101 AND 201112 GROUP BY T1.\"XCL_001\" ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1474"
  ]
}
```

### "yearmonth"."XCL_020" = '201309'

```json
{
  "kind": "predicate",
  "formula": "\"yearmonth\".\"XCL_020\" = '201309'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_009\" FROM transactions_1k AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_013\" = T2.\"XCL_019\" INNER JOIN products AS T3 ON T1.\"XCL_016\" = T3.\"XCL_008\" WHERE T2.\"XCL_020\" = '201309'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1500"
  ]
}
```

### A scalar metric representing the net difference in the count of SME customers preferring CZK versus EUR. It is calculated by subtracting the count of 

```json
{
  "kind": "metric",
  "formula": "SUM(\"customers\".\"XCL_003\" = 'CZK') - SUM(\"customers\".\"XCL_003\" = 'EUR')",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_003\" = 'CZK') - SUM(\"XCL_003\" = 'EUR') FROM customers WHERE \"XCL_002\" = 'SME'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r0\".\"XCL_003\" = 'CZK') - SUM(\"r0\".\"XCL_003\" = 'EUR')",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "customers"
      }
    ],
    "scope_sql": "SELECT SUM(\"r0\".\"XCL_003\" = 'CZK') - SUM(\"r0\".\"XCL_003\" = 'EUR') AS \"value\" FROM customers AS \"r0\" WHERE \"r0\".\"XCL_002\" = 'SME'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1486"
  ]
}
```

### SUBSTRING("yearmonth"."XCL_020", 1, 4) = '2013' AND "customers"."XCL_002" = 'SME'

```json
{
  "kind": "predicate",
  "formula": "SUBSTRING(\"yearmonth\".\"XCL_020\", 1, 4) = '2013' AND \"customers\".\"XCL_002\" = 'SME'",
  "grain": [
    "SUBSTRING(\"yearmonth\".\"XCL_020\", 5, 2)"
  ],
  "population_scope": "SELECT SUBSTRING(T2.\"XCL_020\", 5, 2) FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE SUBSTRING(T2.\"XCL_020\", 1, 4) = '2013' AND T1.\"XCL_002\" = 'SME' GROUP BY SUBSTRING(T2.\"XCL_020\", 5, 2) ORDER BY SUM(T2.\"XCL_021\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1480"
  ]
}
```

### "gasstations"."XCL_006" = 'CZE' AND STRFTIME('%Y', "transactions_1k"."XCL_011") >= '2012'

```json
{
  "kind": "predicate",
  "formula": "\"gasstations\".\"XCL_006\" = 'CZE' AND STRFTIME('%Y', \"transactions_1k\".\"XCL_011\") >= '2012'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_010\") FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.\"XCL_015\" = T2.\"XCL_004\" WHERE T2.\"XCL_006\" = 'CZE' AND STRFTIME('%Y', T1.\"XCL_011\") >= '2012'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1509"
  ]
}
```

### "transactions_1k"."XCL_018" / "transactions_1k"."XCL_017" > 29.00 AND "transactions_1k"."XCL_016" = 5 AND "yearmonth"."XCL_020" = '201208'

```json
{
  "kind": "predicate",
  "formula": "\"transactions_1k\".\"XCL_018\" / \"transactions_1k\".\"XCL_017\" > 29.00 AND \"transactions_1k\".\"XCL_016\" = 5 AND \"yearmonth\".\"XCL_020\" = '201208'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_021\" FROM transactions_1k AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_013\" = T2.\"XCL_019\" WHERE T1.\"XCL_018\" / T1.\"XCL_017\" > 29.00 AND T1.\"XCL_016\" = 5 AND T2.\"XCL_020\" = '201208'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1533"
  ]
}
```

### Count of Low Volume KAM Customers (2012)

```json
{
  "kind": "metric",
  "formula": "COUNT(*)",
  "grain": [],
  "population_scope": "SELECT COUNT(*) FROM (SELECT T2.\"XCL_019\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_002\" = 'KAM' AND SUBSTRING(T2.\"XCL_020\", 1, 4) = '2012' GROUP BY T2.\"XCL_019\" HAVING SUM(T2.\"XCL_021\") < 30000) AS t1",
  "upstream_scopes": [
    "SELECT T2.\"XCL_019\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T1.\"XCL_002\" = 'KAM' AND SUBSTRING(T2.\"XCL_020\", 1, 4) = '2012' GROUP BY T2.\"XCL_019\" HAVING SUM(T2.\"XCL_021\") < 30000"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1475"
  ]
}
```

### "yearmonth"."XCL_020" = '201309'

```json
{
  "kind": "predicate",
  "formula": "\"yearmonth\".\"XCL_020\" = '201309'",
  "grain": [
    "\"customers\".\"XCL_001\""
  ],
  "population_scope": "SELECT T1.\"XCL_002\" FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.\"XCL_001\" = T2.\"XCL_019\" WHERE T2.\"XCL_020\" = '201309' GROUP BY T1.\"XCL_001\" ORDER BY SUM(T2.\"XCL_021\") ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1496"
  ]
}
```


## Incremental maintenance events

- Source withdrawal preview · bird_dev:1470 · Review event: withdraw this archived SQL source on a copied ontology
  - gasstations.XCL_004: gasstation_id → gasstation_id
  - gasstations.XCL_007: segment → segment
  - gasstations.XCL_006: country → country
