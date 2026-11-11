# BIRD-History / financial — Schema and business semantics

The saved catalogue for this database contains 11 tables, 50 physical columns, 21 relationships and 106 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## Account

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: T2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Account.XCL_001 | account_id | unknown | bird_dev:163 |
| Account.XCL_002 | district_id | unknown | bird_dev:163 |

## District

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: T1

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| District.XCL_017 | district_id | unknown | bird_dev:163 |
| District.XCL_018 | district_name | unknown | bird_dev:163 |

## Loan

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: T3

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Loan.XCL_034 | account_id | unknown | bird_dev:163 |
| Loan.XCL_039 | status | unknown | bird_dev:163 |

## account

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: A, T1, T1a, T1b, T2, T3, T4, T5, a, a2, a3, acc

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| account.XCL_001 | account_id | unknown | bird_dev:173, bird_dev:96, bird_dev:179, bird_dev:188, bird_dev:127, bird_dev:129, bird_dev:144, bird_dev:108 |
| account.XCL_002 | district_id | unknown | bird_dev:129, bird_dev:121, bird_dev:125, bird_dev:148, bird_dev:186, bird_dev:124, bird_dev:131, bird_dev:183 |
| account.XCL_003 | frequency | unknown | bird_dev:173, bird_dev:96, bird_dev:127, bird_dev:186, bird_dev:97, bird_dev:135, bird_dev:136, bird_dev:89 |
| account.XCL_004 | date_opened | unknown | bird_dev:188, bird_dev:121, bird_dev:99, bird_dev:183, bird_dev:102, bird_dev:120, bird_dev:126, bird_dev:119 |

## card

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: T1, T2, T3, T4, T5, c, cd

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| card.XCL_005 | card_id | unknown | bird_dev:153, bird_dev:155, bird_dev:139 |
| card.XCL_006 | disp_id | unknown | bird_dev:143, bird_dev:144, bird_dev:167, bird_dev:178, bird_dev:106, bird_dev:153, bird_dev:194, bird_dev:146 |
| card.XCL_007 | card_type | unknown | bird_dev:143, bird_dev:167, bird_dev:178, bird_dev:153, bird_dev:155, bird_dev:194, bird_dev:161, bird_dev:184 |
| card.XCL_008 | issued_date | unknown | bird_dev:167, bird_dev:106, bird_dev:155, bird_dev:103 |

## client

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: T1, T2, T3, T4, T6, c, c2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| client.XCL_009 | client_id | unknown | bird_dev:179, bird_dev:154, bird_dev:168, bird_dev:186, bird_dev:178, bird_dev:130, bird_dev:181, bird_dev:176 |
| client.XCL_010 | gender | unknown | bird_dev:154, bird_dev:168, bird_dev:186, bird_dev:181, bird_dev:189, bird_dev:132, bird_dev:109, bird_dev:115 |
| client.XCL_011 | date_of_birth | unknown | bird_dev:189, bird_dev:113, bird_dev:190, bird_dev:194, bird_dev:182, bird_dev:174, bird_dev:180, bird_dev:94 |
| client.XCL_012 | district_id | unknown | bird_dev:154, bird_dev:168, bird_dev:186, bird_dev:130, bird_dev:138, bird_dev:189, bird_dev:109, bird_dev:190 |

## disp

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: DP, T1, T2, T3, T4, d, d1, di, disp1, dp

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| disp.XCL_013 | card_id | unknown | bird_dev:143, bird_dev:144, bird_dev:110, bird_dev:167, bird_dev:178, bird_dev:106, bird_dev:153, bird_dev:194 |
| disp.XCL_014 | client_id | unknown | bird_dev:179, bird_dev:167, bird_dev:186, bird_dev:97, bird_dev:178, bird_dev:193, bird_dev:156, bird_dev:130 |
| disp.XCL_015 | account_id | unknown | bird_dev:143, bird_dev:96, bird_dev:179, bird_dev:144, bird_dev:148, bird_dev:110, bird_dev:186, bird_dev:97 |
| disp.XCL_016 | type | unknown | bird_dev:96, bird_dev:148, bird_dev:97, bird_dev:193, bird_dev:156, bird_dev:130, bird_dev:153, bird_dev:149 |

## district

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: D, T1, T2, T2b, T3, T4, T5, d, d2, d3, di, di2, dist, dist2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| district.XCL_017 | district_id | unknown | bird_dev:129, bird_dev:121, bird_dev:154, bird_dev:125, bird_dev:148, bird_dev:168, bird_dev:186, bird_dev:124 |
| district.XCL_018 | district_name | unknown | bird_dev:129, bird_dev:121, bird_dev:154, bird_dev:148, bird_dev:124, bird_dev:183, bird_dev:140, bird_dev:193 |
| district.XCL_019 | region | unknown | bird_dev:131, bird_dev:89, bird_dev:150, bird_dev:130, bird_dev:90, bird_dev:120, bird_dev:190, bird_dev:115 |
| district.XCL_020 | area | unknown | bird_dev:115 |
| district.XCL_027 | unemployment_rate_1995 | unknown | bird_dev:168, bird_dev:124, bird_dev:149, bird_dev:189, bird_dev:94, bird_dev:107, bird_dev:92, bird_dev:93 |
| district.XCL_028 | unemployment_rate_1996 | unknown | bird_dev:125, bird_dev:91 |
| district.XCL_029 | unemployment_rate_1996 | unknown | bird_dev:125, bird_dev:91, bird_dev:133 |
| district.XCL_031 | Physical name retained; no saved recovered alias | unknown | bird_dev:138, bird_dev:157, bird_dev:152 |
| district.XCL_032 | Physical name retained; no saved recovered alias | unknown | bird_dev:134, bird_dev:171 |

## loan

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: L, T1, T2, T2a, T3, T4, T5, l, l2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| loan.XCL_033 | loan_id | unknown | bird_dev:124, bird_dev:122 |
| loan.XCL_034 | account_id | unknown | bird_dev:188, bird_dev:108, bird_dev:125, bird_dev:99, bird_dev:116, bird_dev:124, bird_dev:131, bird_dev:136 |
| loan.XCL_035 | date | unknown | bird_dev:116, bird_dev:136, bird_dev:105, bird_dev:113, bird_dev:98, bird_dev:169 |
| loan.XCL_036 | amount | unknown | bird_dev:188, bird_dev:108, bird_dev:99, bird_dev:131, bird_dev:136, bird_dev:156, bird_dev:181, bird_dev:176 |
| loan.XCL_037 | duration | unknown | bird_dev:188, bird_dev:99, bird_dev:124, bird_dev:191 |
| loan.XCL_039 | status | unknown | bird_dev:125, bird_dev:131, bird_dev:176, bird_dev:137, bird_dev:118, bird_dev:192, bird_dev:117 |

## order

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: T1, o

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| order.XCL_040 | order_id | unknown | bird_dev:164, bird_dev:158 |
| order.XCL_041 | account_id | unknown | bird_dev:173, bird_dev:164, bird_dev:158 |
| order.XCL_044 | amount | unknown | bird_dev:173 |
| order.XCL_045 | order_type | unknown | bird_dev:173 |

## trans

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: T1, T2, T3, T4, T5, T6, t, t1, t2, t3

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| trans.XCL_046 | transaction_id | unknown | bird_dev:159, bird_dev:165, bird_dev:177 |
| trans.XCL_047 | account_id | unknown | bird_dev:179, bird_dev:129, bird_dev:144, bird_dev:108, bird_dev:110, bird_dev:101, bird_dev:116, bird_dev:106 |
| trans.XCL_048 | transaction_date | unknown | bird_dev:179, bird_dev:129, bird_dev:144, bird_dev:108, bird_dev:110, bird_dev:101, bird_dev:116, bird_dev:170 |
| trans.XCL_049 | transaction_direction | unknown | bird_dev:129, bird_dev:151 |
| trans.XCL_050 | transaction_operation | unknown | bird_dev:144, bird_dev:135, bird_dev:170, bird_dev:159 |
| trans.XCL_051 | transaction_amount | unknown | bird_dev:179, bird_dev:144, bird_dev:108, bird_dev:110, bird_dev:106, bird_dev:102, bird_dev:182, bird_dev:145 |
| trans.XCL_052 | account_balance | unknown | bird_dev:116, bird_dev:135, bird_dev:177 |
| trans.XCL_053 | transaction_category | unknown | bird_dev:182, bird_dev:142 |
| trans.XCL_054 | transaction_type_code | unknown | bird_dev:150 |

## Relationships and join evidence

- Account.XCL_001 ↔ Loan.XCL_034; target_disjoint_historical_join
- Account.XCL_002 ↔ District.XCL_017; target_disjoint_historical_join
- account.XCL_001 ↔ disp.XCL_015; target_disjoint_historical_join
- account.XCL_001 ↔ loan.XCL_034; target_disjoint_historical_join
- account.XCL_001 ↔ order.XCL_041; target_disjoint_historical_join
- account.XCL_001 ↔ trans.XCL_047; target_disjoint_historical_join
- account.XCL_002 ↔ district.XCL_017; target_disjoint_historical_join
- card.XCL_006 ↔ disp.XCL_013; target_disjoint_historical_join
- client.XCL_009 ↔ disp.XCL_014; target_disjoint_historical_join
- client.XCL_012 ↔ district.XCL_017; target_disjoint_historical_join
- disp.XCL_015 ↔ loan.XCL_034; target_disjoint_historical_join
- Account.XCL_001 ↔ Loan.XCL_034; sql_workload_observed_join
- Account.XCL_002 ↔ District.XCL_017; sql_workload_observed_join
- account.XCL_001 ↔ disp.XCL_015; sql_workload_observed_join
- account.XCL_001 ↔ loan.XCL_034; sql_workload_observed_join
- account.XCL_001 ↔ order.XCL_041; sql_workload_observed_join
- account.XCL_001 ↔ trans.XCL_047; sql_workload_observed_join
- account.XCL_002 ↔ district.XCL_017; sql_workload_observed_join
- card.XCL_006 ↔ disp.XCL_013; sql_workload_observed_join
- client.XCL_009 ↔ disp.XCL_014; sql_workload_observed_join
- client.XCL_012 ↔ district.XCL_017; sql_workload_observed_join

## Business definitions, population and grain

### A query that joins the account and disp tables on XCL_001 = XCL_015. It filters for accounts where XCL_003 is 'POPLATEK PO OBRATU' and disp records wh

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_014\" FROM account AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_001\" = T2.\"XCL_015\" WHERE T1.\"XCL_003\" = 'POPLATEK PO OBRATU' AND T2.\"XCL_016\" = 'DISPONENT'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:97"
  ]
}
```

### Account Owner District Lookup

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_014\", T2.\"XCL_017\", T2.\"XCL_018\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN disp AS T3 ON T1.\"XCL_001\" = T3.\"XCL_015\" WHERE T3.\"XCL_016\" = 'OWNER'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:193"
  ]
}
```

### Districts with VYDAJ Transactions

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_018\" FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN trans AS T3 ON T2.\"XCL_001\" = T3.\"XCL_047\" WHERE T3.\"XCL_049\" = 'VYDAJ'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:151"
  ]
}
```

### A query that retrieves account IDs by joining district, account, and disp tables. It filters for accounts where the district name is 'Tabor' and the r

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_001\" FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN disp AS T3 ON T2.\"XCL_001\" = T3.\"XCL_015\" WHERE T3.\"XCL_016\" = 'OWNER' AND T1.\"XCL_018\" = 'Tabor'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:148"
  ]
}
```

### Filtered transaction count query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_047\") FROM trans AS T1 INNER JOIN account AS T2 ON T1.\"XCL_047\" = T2.\"XCL_001\" INNER JOIN disp AS T4 ON T2.\"XCL_001\" = T4.\"XCL_015\" INNER JOIN client AS T3 ON T4.\"XCL_014\" = T3.\"XCL_009\" WHERE STRFTIME('%Y', T3.\"XCL_011\") BETWEEN '1974' AND '1976' AND T3.\"XCL_010\" = 'M' AND T1.\"XCL_051\" > 4000 AND T1.\"XCL_053\" = 'SIPO'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:182"
  ]
}
```

### A query that retrieves client identifiers by joining order, account, disp, and client tables, filtered to orders where XCL_040 equals 32423.

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_009\" FROM \"order\" AS T1 INNER JOIN account AS T2 ON T1.\"XCL_041\" = T2.\"XCL_001\" INNER JOIN disp AS T4 ON T4.\"XCL_015\" = T2.\"XCL_001\" INNER JOIN client AS T3 ON T4.\"XCL_014\" = T3.\"XCL_009\" WHERE T1.\"XCL_040\" = 32423",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:164"
  ]
}
```

### Filtered Account-Order Aggregation Query

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_003\", T2.\"XCL_045\" FROM account AS T1 INNER JOIN (SELECT \"XCL_041\", \"XCL_045\", SUM(\"XCL_044\") AS total_amount FROM \"order\" GROUP BY \"XCL_041\", \"XCL_045\") AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_001\" = 3 AND T2.\"total_amount\" = 3539",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:173"
  ]
}
```

### Post-1995 Card Withdrawal Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_047\") FROM trans WHERE STRFTIME('%Y', \"XCL_048\") > '1995' AND \"XCL_050\" = 'VYBER KARTOU'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:170"
  ]
}
```

### 1998 Card Withdrawal Average Query

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T4.\"XCL_051\") FROM card AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_006\" = T2.\"XCL_013\" INNER JOIN account AS T3 ON T2.\"XCL_015\" = T3.\"XCL_001\" INNER JOIN trans AS T4 ON T3.\"XCL_001\" = T4.\"XCL_047\" WHERE STRFTIME('%Y', T4.\"XCL_048\") = '1998' AND T4.\"XCL_050\" = 'VYBER KARTOU'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:144"
  ]
}
```

### Executes an inner join between trans (T1) and account (T2) on transaction ID (XCL_047) and account ID (XCL_001). Filters for negative amounts, 'VYBER 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_047\") FROM trans AS T1 INNER JOIN account AS T2 ON T1.\"XCL_047\" = T2.\"XCL_001\" WHERE T1.\"XCL_052\" < 0 AND T1.\"XCL_050\" = 'VYBER KARTOU' AND T2.\"XCL_003\" = 'POPLATEK MESICNE'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:135"
  ]
}
```

### A query that joins client, disp, and card tables to retrieve client identifiers for cards issued on a specific date (1994-03-03).

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_014\" FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN card AS T3 ON T2.\"XCL_013\" = T3.\"XCL_006\" WHERE T3.\"XCL_008\" = '1994-03-03'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:103"
  ]
}
```

### A query that joins the district table (T1) and client table (T2) on T1.XCL_017 = T2.XCL_012. It orders the results by T1.XCL_027 in descending order a

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_010\" FROM district AS T1 INNER JOIN client AS T2 ON T1.\"XCL_017\" = T2.\"XCL_012\" ORDER BY T1.\"XCL_027\" DESC, T2.\"XCL_011\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:107"
  ]
}
```

### A query that retrieves account identifiers (XCL_001) and attributes (XCL_003) for accounts located in the 'east Bohemia' district, where the account d

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\", T1.\"XCL_003\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE T2.\"XCL_019\" = 'east Bohemia' AND STRFTIME('%Y', T1.\"XCL_004\") BETWEEN '1995' AND '2000'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:120"
  ]
}
```

### A query that identifies account identifiers (XCL_047) from the 'trans' table joined with the 'account' table. It filters for transactions in 1998 with

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_047\" FROM trans AS T1 INNER JOIN account AS T2 ON T1.\"XCL_047\" = T2.\"XCL_001\" WHERE STRFTIME('%Y', T1.\"XCL_048\") = '1998' AND T1.\"XCL_050\" = 'VYBER KARTOU' AND T1.\"XCL_051\" < (SELECT AVG(\"XCL_051\") FROM trans WHERE STRFTIME('%Y', \"XCL_048\") = '1998')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:145"
  ]
}
```

### Full SQL program that joins district and client tables on XCL_017 = XCL_012, filters for districts where XCL_027 > 10000, and computes the percentage 

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(T2.\"XCL_010\" = 'F') AS REAL) * 100 / COUNT(T2.\"XCL_009\") FROM district AS T1 INNER JOIN client AS T2 ON T1.\"XCL_017\" = T2.\"XCL_012\" WHERE T1.\"XCL_027\" > 10000",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:168"
  ]
}
```

### Full SQL program that joins the card table (T1) with the disp table (T2) on the card identifier (XCL_006 = XCL_013). It filters for cards where XCL_00

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_005\") FROM card AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_006\" = T2.\"XCL_013\" WHERE T1.\"XCL_007\" = 'gold' AND T2.\"XCL_016\" = 'OWNER'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:139"
  ]
}
```

### Retrieves the single district record with the maximum value in column XCL_029, returning columns XCL_017 and XCL_018.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_017\", \"XCL_018\" FROM district ORDER BY \"XCL_029\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:133"
  ]
}
```

### A query that retrieves XCL_031 values from the district table by joining with the account table on XCL_017 = XCL_002, filtered to accounts where XCL_0

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_031\" FROM district AS T1 INNER JOIN \"account\" AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE T2.\"XCL_001\" = 532",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:157"
  ]
}
```

### A full SQL program that joins account, district, disp, and client tables. It filters for accounts in the district of the first female client (by XCL_0

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\", (SELECT MAX(\"XCL_027\") - MIN(\"XCL_027\") FROM district) FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN disp AS T3 ON T1.\"XCL_001\" = T3.\"XCL_015\" INNER JOIN client AS T4 ON T3.\"XCL_014\" = T4.\"XCL_009\" WHERE T2.\"XCL_017\" = (SELECT \"XCL_012\" FROM client WHERE \"XCL_010\" = 'F' ORDER BY \"XCL_011\" ASC LIMIT 1) ORDER BY T2.\"XCL_027\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:94"
  ]
}
```

### A query that joins the disp and card tables on disp.XCL_013 = card.XCL_006, filters for cards where card.XCL_007 is 'gold', and returns the correspond

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_015\" FROM disp AS T2 INNER JOIN card AS T1 ON T1.\"XCL_006\" = T2.\"XCL_013\" WHERE T1.\"XCL_007\" = 'gold'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:143"
  ]
}
```

### Computes the percentage of district records where the district type (XCL_018) is 'Decin' among all districts associated with accounts created in 1993.

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(T1.\"XCL_018\" = 'Decin') AS REAL) * 100 / COUNT(\"XCL_001\") FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE STRFTIME('%Y', T2.\"XCL_004\") = '1993'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:126"
  ]
}
```

### A full SQL program that retrieves transaction amounts for a specific client. It joins client, disp, account, and trans tables to link a client (ID 335

```json
{
  "kind": "program",
  "formula": "SELECT T4.\"XCL_046\" FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN account AS T3 ON T2.\"XCL_015\" = T3.\"XCL_001\" INNER JOIN trans AS T4 ON T3.\"XCL_001\" = T4.\"XCL_047\" WHERE T1.\"XCL_009\" = 3356 AND T4.\"XCL_050\" = 'VYBER'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:159"
  ]
}
```

### Full SQL program joining account, district, and trans tables to identify districts where the sum of transaction amounts in 1997 exceeded 10,000. Retur

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_002\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN trans AS T3 ON T1.\"XCL_001\" = T3.\"XCL_047\" WHERE STRFTIME('%Y', T3.\"XCL_048\") = '1997' GROUP BY T1.\"XCL_002\" HAVING SUM(T3.\"XCL_051\") > 10000",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:141"
  ]
}
```

### Full SQL program that joins client, district, account, and disp tables to compute the percentage of male clients associated with accounts of type 'POP

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(T1.\"XCL_010\" = 'M') AS REAL) * 100 / COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T3 ON T1.\"XCL_012\" = T3.\"XCL_017\" INNER JOIN account AS T2 ON T2.\"XCL_002\" = T3.\"XCL_017\" INNER JOIN disp AS T4 ON T1.\"XCL_009\" = T4.\"XCL_014\" AND T2.\"XCL_001\" = T4.\"XCL_015\" WHERE T2.\"XCL_003\" = 'POPLATEK TYDNE'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:186"
  ]
}
```

### A query that identifies the district with the most active loans. It joins District, Account, and Loan tables, filters for loans with status 'A', group

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_018\" FROM District AS T1 INNER JOIN Account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN Loan AS T3 ON T2.\"XCL_001\" = T3.\"XCL_034\" WHERE T3.\"XCL_039\" = 'A' GROUP BY T1.\"XCL_017\" ORDER BY COUNT(T2.\"XCL_001\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:163"
  ]
}
```

### A query that retrieves the client identifier and age for clients who are owners of gold cards. It joins the disp, card, and client tables, filtering f

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_014\", STRFTIME('%Y', CURRENT_TIMESTAMP) - STRFTIME('%Y', T3.\"XCL_011\") FROM disp AS T1 INNER JOIN card AS T2 ON T2.\"XCL_006\" = T1.\"XCL_013\" INNER JOIN client AS T3 ON T1.\"XCL_014\" = T3.\"XCL_009\" WHERE T2.\"XCL_007\" = 'gold' AND T1.\"XCL_016\" = 'OWNER'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:194"
  ]
}
```

### Full query joining district, account, and disp tables to retrieve disposition types for non-owner accounts in districts with population between 8000 a

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_016\" FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN disp AS T3 ON T2.\"XCL_001\" = T3.\"XCL_015\" WHERE T3.\"XCL_016\" <> 'OWNER' AND T1.\"XCL_027\" BETWEEN 8000 AND 9000",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:149"
  ]
}
```

### A query that joins the account table to the district table on the district key, filters for the district named 'Prague', orders the results by the acc

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE T2.\"XCL_019\" = 'Prague' ORDER BY T1.\"XCL_004\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:114"
  ]
}
```

### Account-District Join for Pisek

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_001\") FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE T2.\"XCL_018\" = 'Pisek'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:140"
  ]
}
```

### Full SQL program that joins account, district, and loan tables. It filters for district ID 1 and loan statuses 'C' or 'D', then counts the resulting a

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_001\") FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN loan AS T3 ON T1.\"XCL_001\" = T3.\"XCL_034\" WHERE T1.\"XCL_002\" = 1 AND (T3.\"XCL_039\" = 'C' OR T3.\"XCL_039\" = 'D')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:137"
  ]
}
```

### A query that joins client, district, account, and disp tables to retrieve the account ID for a female client. It filters for clients where XCL_010 is 

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_001\" FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" INNER JOIN account AS T3 ON T2.\"XCL_017\" = T3.\"XCL_002\" INNER JOIN disp AS T4 ON T1.\"XCL_009\" = T4.\"XCL_014\" AND T4.\"XCL_015\" = T3.\"XCL_001\" WHERE T1.\"XCL_010\" = 'F' ORDER BY T1.\"XCL_011\" ASC, T2.\"XCL_027\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:189"
  ]
}
```

### Identifies the district (XCL_020) within the 'south Bohemia' region (XCL_019) that has the highest percentage of male clients. It joins client and dis

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(T1.\"XCL_010\" = 'M') AS REAL) * 100 / COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T2.\"XCL_019\" = 'south Bohemia' GROUP BY T2.\"XCL_020\" ORDER BY T2.\"XCL_020\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:115"
  ]
}
```

### Executes an inner join between the 'account' table (T1) and 'disp' table (T2) on the account identifier (XCL_001 = XCL_015). Filters for dispositions 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_001\") FROM account AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_001\" = T2.\"XCL_015\" WHERE T2.\"XCL_016\" = 'OWNER' AND T1.\"XCL_003\" = 'POPLATEK PO OBRATU'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:175"
  ]
}
```

### Full SQL program that joins client, disp, account, and loan tables to calculate the average loan amount for male clients. It filters the client popula

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T4.\"XCL_036\") FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN account AS T3 ON T2.\"XCL_015\" = T3.\"XCL_001\" INNER JOIN loan AS T4 ON T3.\"XCL_001\" = T4.\"XCL_034\" WHERE T1.\"XCL_010\" = 'M'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:132"
  ]
}
```

### District 5 Transaction Query

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_046\" FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN trans AS T3 ON T2.\"XCL_001\" = T3.\"XCL_047\" WHERE T1.\"XCL_017\" = 5",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:165"
  ]
}
```

### Bohemia Region Comparison Query

```json
{
  "kind": "program",
  "formula": "SELECT SUM(IIF(\"XCL_019\" = 'east Bohemia', \"XCL_032\", 0)) - SUM(IIF(\"XCL_019\" = 'north Bohemia', \"XCL_032\", 0)) FROM district",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:171"
  ]
}
```

### Query for weekly fee owner account count

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_001\") FROM account AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_001\" = T2.\"XCL_015\" WHERE T2.\"XCL_016\" = 'OWNER' AND T1.\"XCL_003\" = 'POPLATEK TYDNE'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:96"
  ]
}
```

### A query that joins the district and client tables to retrieve the district identifier (XCL_018) for clients who are female (XCL_010 = 'F') and were bo

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_018\" FROM district AS T1 INNER JOIN client AS T2 ON T1.\"XCL_017\" = T2.\"XCL_012\" WHERE T2.\"XCL_011\" = '1976-01-29' AND T2.\"XCL_010\" = 'F'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:112"
  ]
}
```

### Full SQL program that joins district and account tables on XCL_017 = XCL_002, groups by district identifier XCL_032, counts accounts, orders by count 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_001\") FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" GROUP BY T1.\"XCL_032\" ORDER BY T1.\"XCL_032\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:134"
  ]
}
```

### A query that joins loan, account, and trans tables to retrieve a single transaction identifier (XCL_051). It orders results by loan attribute XCL_036 

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_051\" FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" INNER JOIN trans AS T3 ON T2.\"XCL_001\" = T3.\"XCL_047\" ORDER BY T1.\"XCL_036\" DESC, T3.\"XCL_048\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:108"
  ]
}
```

### Full SQL program that computes the percentage of gold cards issued before 1998 from the 'card' table. It uses conditional aggregation to count matchin

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(\"XCL_007\" = 'gold' AND STRFTIME('%Y', \"XCL_008\") < '1998') AS REAL) * 100 / COUNT(\"XCL_005\") FROM card",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:155"
  ]
}
```

### Query for Male Client Count in Second Highest District

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'M' AND T2.\"XCL_031\" = (SELECT T3.\"XCL_031\" FROM district AS T3 ORDER BY T3.\"XCL_031\" DESC LIMIT 1 OFFSET 1)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:138"
  ]
}
```

### Full SQL program that joins loan, account, disp, and client tables to compute the year-over-year percentage change in loan amounts for male account ow

```json
{
  "kind": "program",
  "formula": "SELECT CAST((SUM(CASE WHEN STRFTIME('%Y', T1.\"XCL_035\") = '1997' THEN T1.\"XCL_036\" ELSE 0 END) - SUM(CASE WHEN STRFTIME('%Y', T1.\"XCL_035\") = '1996' THEN T1.\"XCL_036\" ELSE 0 END)) AS REAL) * 100 / SUM(CASE WHEN STRFTIME('%Y', T1.\"XCL_035\") = '1996' THEN T1.\"XCL_036\" ELSE 0 END) FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" INNER JOIN disp AS T3 ON T3.\"XCL_015\" = T2.\"XCL_001\" INNER JOIN client AS T4 ON T4.\"XCL_009\" = T3.\"XCL_014\" WHERE T4.\"XCL_010\" = 'M' AND T3.\"XCL_016\" = 'OWNER'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:169"
  ]
}
```

### Full SQL program that joins client, disp, and card tables to count female clients holding junior cards. It filters clients by gender 'F' and cards by 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN card AS T3 ON T2.\"XCL_013\" = T3.\"XCL_006\" WHERE T1.\"XCL_010\" = 'F' AND T3.\"XCL_007\" = 'junior'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:184"
  ]
}
```

### A query that joins client, disp, account, and trans tables to retrieve transaction IDs (XCL_052) and client IDs (XCL_010). It filters for clients wher

```json
{
  "kind": "program",
  "formula": "SELECT T4.\"XCL_052\", T1.\"XCL_010\" FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN account AS T3 ON T2.\"XCL_015\" = T3.\"XCL_001\" INNER JOIN trans AS T4 ON T3.\"XCL_001\" = T4.\"XCL_047\" WHERE T1.\"XCL_009\" = 4 AND T4.\"XCL_046\" = 851",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:177"
  ]
}
```

### A query that retrieves the client identifier for a specific loan. It joins the loan table to account, then to disp, and finally to client. The computa

```json
{
  "kind": "program",
  "formula": "SELECT T4.\"XCL_011\" FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" INNER JOIN disp AS T3 ON T2.\"XCL_001\" = T3.\"XCL_015\" INNER JOIN client AS T4 ON T3.\"XCL_014\" = T4.\"XCL_009\" WHERE T1.\"XCL_035\" = '1996-01-03' AND T1.\"XCL_036\" = 98832",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:113"
  ]
}
```

### A query that joins transaction, account, and district tables to retrieve distinct account IDs where the transaction type is 'SIPO' and the district na

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_001\" FROM trans AS T1 INNER JOIN account AS T2 ON T1.\"XCL_047\" = T2.\"XCL_001\" INNER JOIN district AS T3 ON T2.\"XCL_002\" = T3.\"XCL_017\" WHERE T1.\"XCL_053\" = 'SIPO' AND T3.\"XCL_018\" = 'Pisek'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:142"
  ]
}
```

### Executes an inner join between district and client tables on district ID (XCL_017 = XCL_012). Filters for female clients born before 1950 in the Sokol

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_009\") FROM district AS T1 INNER JOIN client AS T2 ON T1.\"XCL_017\" = T2.\"XCL_012\" WHERE T2.\"XCL_010\" = 'F' AND STRFTIME('%Y', T2.\"XCL_011\") < '1950' AND T1.\"XCL_018\" = 'Sokolov'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:100"
  ]
}
```

### Filtered District Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T2.\"XCL_017\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'F' AND T2.\"XCL_027\" BETWEEN 6000 AND 10000",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:92"
  ]
}
```

### 1993 Post-Transaction Accounts by District

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\", T2.\"XCL_018\", T2.\"XCL_019\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE T1.\"XCL_003\" = 'POPLATEK PO OBRATU' AND STRFTIME('%Y', T1.\"XCL_004\") = '1993'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:119"
  ]
}
```

### Districts with Jan 1996 Expenses

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_018\" FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN trans AS T3 ON T2.\"XCL_001\" = T3.\"XCL_047\" WHERE T3.\"XCL_049\" = 'VYDAJ' AND T3.\"XCL_048\" LIKE '1996-01%' ORDER BY \"XCL_018\" ASC LIMIT 10",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:129"
  ]
}
```

### Filtered Client Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE STRFTIME('%Y', T1.\"XCL_011\") = '1920' AND T2.\"XCL_019\" = 'east Bohemia'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:190"
  ]
}
```

### A query that retrieves the XCL_001 identifier from the account table, filtered to include only rows where the XCL_003 column matches the literal strin

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_001\" FROM account WHERE \"XCL_003\" = 'POPLATEK MESICNE'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:127"
  ]
}
```

### A SQL program that joins the district table (T1) with the account table (T2) on district XCL_017 equals account XCL_002. It filters for accounts with 

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T1.\"XCL_031\") FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE STRFTIME('%Y', T2.\"XCL_004\") >= '1997' AND T1.\"XCL_031\" > 4000",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:152"
  ]
}
```

### Executes an inner join between the 'account' table (T1) and 'loan' table (T2) on account ID (XCL_001) matching loan account reference (XCL_034). Filte

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_001\") FROM account AS T1 INNER JOIN loan AS T2 ON T1.\"XCL_001\" = T2.\"XCL_034\" WHERE T2.\"XCL_035\" BETWEEN '1995-01-01' AND '1997-12-31' AND T1.\"XCL_003\" = 'POPLATEK MESICNE' AND T2.\"XCL_036\" >= 250000",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:136"
  ]
}
```

### Earliest 1995 Transaction Query

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_047\" FROM trans WHERE STRFTIME('%Y', \"XCL_048\") = '1995' ORDER BY \"XCL_048\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:101"
  ]
}
```

### Full SQL program that joins account, loan, and district tables. It filters for accounts in the 'Prague' district that have linked loans and returns th

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_001\") FROM account AS T1 INNER JOIN loan AS T2 ON T1.\"XCL_001\" = T2.\"XCL_034\" INNER JOIN district AS T3 ON T1.\"XCL_002\" = T3.\"XCL_017\" WHERE T3.\"XCL_019\" = 'Prague'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:90"
  ]
}
```

### A full SQL program that joins the account table (T1) to the trans table (T2) on XCL_001 = XCL_047. It filters transactions where XCL_051 is 840 and XC

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_004\" FROM account AS T1 INNER JOIN trans AS T2 ON T1.\"XCL_001\" = T2.\"XCL_047\" WHERE T2.\"XCL_051\" = 840 AND T2.\"XCL_048\" = '1998-10-14'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:104"
  ]
}
```

### A query that joins the 'account' and 'loan' tables on 'XCL_001' (account) and 'XCL_034' (loan), filtering for loans where 'XCL_035' is '1994-08-25'. I

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_002\" FROM account AS T1 INNER JOIN loan AS T2 ON T1.\"XCL_001\" = T2.\"XCL_034\" WHERE T2.\"XCL_035\" = '1994-08-25'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:105"
  ]
}
```

### Full SQL program that joins 'district', 'client', and 'disp' tables. It filters for the 'south Bohemia' district and excludes 'OWNER' roles in the 'di

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T3.\"XCL_015\") FROM district AS T1 INNER JOIN client AS T2 ON T1.\"XCL_017\" = T2.\"XCL_012\" INNER JOIN disp AS T3 ON T2.\"XCL_009\" = T3.\"XCL_014\" WHERE T1.\"XCL_019\" = 'south Bohemia' AND T3.\"XCL_016\" <> 'OWNER'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:130"
  ]
}
```

### A query that joins disp, account, and loan tables to identify the owner (where disp.XCL_016 is 'OWNER') of the account linked to the loan with the max

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_014\" FROM disp AS T1 INNER JOIN account AS T3 ON T1.\"XCL_015\" = T3.\"XCL_001\" INNER JOIN loan AS T2 ON T3.\"XCL_001\" = T2.\"XCL_034\" WHERE T1.\"XCL_016\" = 'OWNER' ORDER BY T2.\"XCL_036\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:156"
  ]
}
```

### A query that retrieves loan IDs, district names, and district average salaries for all loans with a status code of 60. It joins the loan table to acco

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_033\", T2.\"XCL_018\", T2.\"XCL_027\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN loan AS T3 ON T1.\"XCL_001\" = T3.\"XCL_034\" WHERE T3.\"XCL_037\" = 60",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:124"
  ]
}
```

### Full SQL program joining client and district tables on XCL_012 = XCL_017, filtering for male clients in north Bohemia districts where XCL_027 > 8000, 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'M' AND T2.\"XCL_019\" = 'north Bohemia' AND T2.\"XCL_027\" > 8000",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:93"
  ]
}
```

### A query that retrieves pairs of client IDs and account IDs. It joins client, district, disp, and account tables to find clients born between 1983 and 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_009\", T3.\"XCL_001\" FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" INNER JOIN disp AS T4 ON T1.\"XCL_009\" = T4.\"XCL_014\" INNER JOIN account AS T3 ON T2.\"XCL_017\" = T3.\"XCL_002\" AND T4.\"XCL_015\" = T3.\"XCL_001\" WHERE T2.\"XCL_019\" = 'east Bohemia' AND STRFTIME('%Y', T1.\"XCL_011\") BETWEEN '1983' AND '1987'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:180"
  ]
}
```

### Full SQL program that joins the client table (T1) with the district table (T2) on the district identifier (XCL_012 = XCL_017). It filters for female c

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'F' AND T2.\"XCL_018\" = 'Jesenik'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:109"
  ]
}
```

### Full SQL program that joins the district and client tables on XCL_017 = XCL_012, filters for the district where XCL_019 is 'Prague', and computes the 

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(T2.\"XCL_010\" = 'F') AS REAL) / COUNT(T2.\"XCL_009\") * 100 FROM district AS T1 INNER JOIN client AS T2 ON T1.\"XCL_017\" = T2.\"XCL_012\" WHERE T1.\"XCL_019\" = 'Prague'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:185"
  ]
}
```

### Client 9 Card Lookup

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_007\" FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN card AS T3 ON T2.\"XCL_013\" = T3.\"XCL_006\" WHERE T1.\"XCL_009\" = 9",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:178"
  ]
}
```

### A query that retrieves the single highest transaction amount (XCL_051) for transactions linked to a card (via disp and account) where the card's date 

```json
{
  "kind": "program",
  "formula": "SELECT T4.\"XCL_051\" FROM card AS T1 JOIN disp AS T2 ON T1.\"XCL_006\" = T2.\"XCL_013\" JOIN account AS T3 ON T2.\"XCL_015\" = T3.\"XCL_001\" JOIN trans AS T4 ON T3.\"XCL_001\" = T4.\"XCL_047\" WHERE T1.\"XCL_008\" = '1996-10-21' ORDER BY T4.\"XCL_051\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:106"
  ]
}
```

### District Attributes for Specific Loan Condition

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_018\", T2.\"XCL_019\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN loan AS T3 ON T1.\"XCL_001\" = T3.\"XCL_034\" WHERE T3.\"XCL_033\" = 4990",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:122"
  ]
}
```

### A query that identifies accounts associated with loans exceeding 300,000 (XCL_036 > 300000). It joins the account, district, and loan tables to return

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\", T2.\"XCL_018\", T2.\"XCL_019\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN loan AS T3 ON T1.\"XCL_001\" = T3.\"XCL_034\" WHERE T3.\"XCL_036\" > 300000",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:123"
  ]
}
```

### Client-District Join for Prague Male Count

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'M' AND T2.\"XCL_018\" = 'Hl.m. Praha'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:154"
  ]
}
```

### District Account Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_001\") FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE STRFTIME('%Y', T2.\"XCL_004\") = '1996' AND T1.\"XCL_018\" = 'Litomerice'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:111"
  ]
}
```

### A query that joins the client and district tables on the district ID, filters for female clients (XCL_010 = 'F'), groups by district ID and name, coun

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_018\", COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'F' GROUP BY T2.\"XCL_017\", T2.\"XCL_018\" ORDER BY COUNT(T1.\"XCL_009\") DESC LIMIT 9",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:128"
  ]
}
```

### Executes an inner join between the 'loan' table (T1) and 'account' table (T2) on the loan identifier (XCL_034 = XCL_001). It filters for accounts with

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_034\") FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" WHERE T2.\"XCL_003\" = 'POPLATEK TYDNE' AND T1.\"XCL_036\" < 200000",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:160"
  ]
}
```

### A query that joins the loan table with the account table to find loans associated with accounts opened before 1997. It filters for loans with a term (

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_034\" FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" WHERE T1.\"XCL_037\" > 24 AND STRFTIME('%Y', T2.\"XCL_004\") < '1997' ORDER BY T1.\"XCL_036\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:188"
  ]
}
```

### Full SQL program that computes the percentage of loans with XCL_039 = 'C' among loans where XCL_036 < 100000. It uses the loan table and applies a fil

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(\"XCL_039\" = 'C') AS REAL) * 100 / COUNT(\"XCL_034\") FROM loan WHERE \"XCL_036\" < 100000",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:118"
  ]
}
```

### A query that retrieves account identifiers (XCL_001) and attributes (XCL_004) for all accounts joined to the district table where the district name (X

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\", T1.\"XCL_004\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE T2.\"XCL_018\" = 'Prachatice'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:121"
  ]
}
```

### Executes an inner join between district and account tables on district ID (XCL_017 = XCL_002). Filters for districts in 'east Bohemia' (XCL_019) and a

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_001\") FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE T1.\"XCL_019\" = 'east Bohemia' AND T2.\"XCL_003\" = 'POPLATEK PO OBRATU'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:89"
  ]
}
```

### Client Year for Account 130

```json
{
  "kind": "program",
  "formula": "SELECT STRFTIME('%Y', T1.\"XCL_011\") FROM client AS T1 INNER JOIN disp AS T3 ON T1.\"XCL_009\" = T3.\"XCL_014\" INNER JOIN account AS T2 ON T3.\"XCL_015\" = T2.\"XCL_001\" WHERE T2.\"XCL_001\" = 130",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:174"
  ]
}
```

### A SQL program that joins account, district, and loan tables. It filters loans where XCL_039 is 'C' or 'D', groups by district (XCL_019), sums the loan

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_019\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN loan AS T3 ON T1.\"XCL_001\" = T3.\"XCL_034\" WHERE T3.\"XCL_039\" IN ('C', 'D') GROUP BY T2.\"XCL_019\" ORDER BY SUM(T3.\"XCL_036\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:131"
  ]
}
```

### Client 617 1998 Transaction Sum Query

```json
{
  "kind": "program",
  "formula": "SELECT SUM(T3.\"XCL_051\") FROM client AS T1 INNER JOIN disp AS T4 ON T1.\"XCL_009\" = T4.\"XCL_014\" INNER JOIN account AS T2 ON T4.\"XCL_015\" = T2.\"XCL_001\" INNER JOIN trans AS T3 ON T2.\"XCL_001\" = T3.\"XCL_047\" WHERE STRFTIME('%Y', T3.\"XCL_048\") = '1998' AND T1.\"XCL_009\" = 617",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:179"
  ]
}
```

### A query that joins the 'order', 'account', and 'district' tables to retrieve the district identifier for orders where the order attribute XCL_040 equa

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_017\" FROM \"order\" AS T1 INNER JOIN account AS T2 ON T1.\"XCL_041\" = T2.\"XCL_001\" INNER JOIN district AS T3 ON T2.\"XCL_002\" = T3.\"XCL_017\" WHERE T1.\"XCL_040\" = 33333",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:158"
  ]
}
```

### A query that joins district and client tables on XCL_017 = XCL_012, filters clients where XCL_009 equals 3541, and returns the corresponding district 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_019\" FROM district AS T1 INNER JOIN client AS T2 ON T1.\"XCL_017\" = T2.\"XCL_012\" WHERE T2.\"XCL_009\" = 3541",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:162"
  ]
}
```

### A full SQL program that joins disp, client, and card tables to retrieve card attributes for a specific client. It filters for client ID 13539 and retu

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_007\" FROM disp AS T1 INNER JOIN client AS T2 ON T1.\"XCL_014\" = T2.\"XCL_009\" INNER JOIN card AS T3 ON T1.\"XCL_013\" = T3.\"XCL_006\" WHERE T2.\"XCL_009\" = 13539",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:161"
  ]
}
```

### A SQL program that calculates the average of loan.XCL_036. It joins the account table (T1) to the loan table (T2) on account.XCL_001 = loan.XCL_034. I

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T2.\"XCL_036\") FROM account AS T1 INNER JOIN loan AS T2 ON T1.\"XCL_001\" = T2.\"XCL_034\" WHERE T2.\"XCL_039\" IN ('C', 'D') AND T1.\"XCL_003\" = 'POPLATEK PO OBRATU'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:192"
  ]
}
```

### Executes a join across client, disp, account, loan, and card tables to identify female clients who hold both a loan and a card. Filters on client gend

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_009\" FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN account AS T5 ON T2.\"XCL_015\" = T5.\"XCL_001\" INNER JOIN loan AS T3 ON T5.\"XCL_001\" = T3.\"XCL_034\" INNER JOIN card AS T4 ON T2.\"XCL_013\" = T4.\"XCL_006\" WHERE T1.\"XCL_010\" = 'F'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:146"
  ]
}
```

### Full SQL program that joins district, account, and trans tables. It filters for districts named 'north Bohemia' and transactions with type 'AB', then 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_001\") FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN trans AS T3 ON T2.\"XCL_001\" = T3.\"XCL_047\" WHERE T3.\"XCL_054\" = 'AB' AND T1.\"XCL_019\" = 'north Bohemia'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:150"
  ]
}
```

### A query that joins the card table (T1) to the disp table (T2) on card.XCL_006 = disp.XCL_013, filters for cards where XCL_007 is 'junior' and XCL_008 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_014\" FROM card AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_006\" = T2.\"XCL_013\" WHERE T1.\"XCL_007\" = 'junior' AND T1.\"XCL_008\" >= '1997-01-01'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:167"
  ]
}
```

### Full SQL program that joins loan, account, and trans tables to compute the percentage change in transaction amounts for specific dates (1998-12-27 vs 

```json
{
  "kind": "program",
  "formula": "SELECT CAST((SUM(IIF(T3.\"XCL_048\" = '1998-12-27', T3.\"XCL_052\", 0)) - SUM(IIF(T3.\"XCL_048\" = '1993-03-22', T3.\"XCL_052\", 0))) AS REAL) * 100 / SUM(IIF(T3.\"XCL_048\" = '1993-03-22', T3.\"XCL_052\", 0)) FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" INNER JOIN trans AS T3 ON T3.\"XCL_047\" = T2.\"XCL_001\" WHERE T1.\"XCL_035\" = '1993-07-05'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:116"
  ]
}
```

### A full SQL program that computes the dominant year indicator by comparing global averages of XCL_029 and XCL_028 from the district table. It returns a

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT IIF(AVG(\"XCL_029\") > AVG(\"XCL_028\"), '1996', '1995') FROM district",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:91"
  ]
}
```

### A query that identifies a single loan ID. It joins the 'loan' table to the 'account' table on the loan identifier (XCL_034 = XCL_001). It filters for 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_034\" FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" WHERE STRFTIME('%Y', T2.\"XCL_004\") = '1993' AND T1.\"XCL_037\" > 12 ORDER BY T1.\"XCL_036\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:99"
  ]
}
```

### Query: disp.XCL_013 for specific transaction

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_013\" FROM disp AS T1 INNER JOIN account AS T2 ON T1.\"XCL_015\" = T2.\"XCL_001\" INNER JOIN trans AS T3 ON T2.\"XCL_001\" = T3.\"XCL_047\" WHERE T3.\"XCL_048\" = '1997-08-20' AND T3.\"XCL_051\" = 5100",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:110"
  ]
}
```

### Full SQL program that joins loan, account, and district tables. It filters for loans where XCL_039 equals 'D' and computes the percentage change metri

```json
{
  "kind": "program",
  "formula": "SELECT CAST((T3.\"XCL_029\" - T3.\"XCL_028\") AS REAL) * 100 / T3.\"XCL_028\" FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" INNER JOIN district AS T3 ON T2.\"XCL_002\" = T3.\"XCL_017\" WHERE T1.\"XCL_039\" = 'D'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:125"
  ]
}
```

### Executes an inner join between the account and loan tables on the account identifier (XCL_001) and loan identifier (XCL_034). Filters for accounts wit

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_034\") FROM account AS T1 INNER JOIN loan AS T2 ON T1.\"XCL_001\" = T2.\"XCL_034\" WHERE T2.\"XCL_037\" = 24 AND T1.\"XCL_003\" = 'POPLATEK TYDNE'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:191"
  ]
}
```

### Executes an inner join between 'account' (T1) and 'disp' (T2) on the account identifier (XCL_001 = XCL_015). Filters for accounts with type 'POPLATEK 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_015\") FROM account AS T1 INNER JOIN disp AS T2 ON T2.\"XCL_015\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'POPLATEK TYDNE' AND T2.\"XCL_016\" = 'OWNER'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:187"
  ]
}
```

### A SQL program that joins the district table (T1) with the account table (T2) on district ID (XCL_017) matching account district reference (XCL_002). I

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_001\") FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE T1.\"XCL_018\" = 'Jesenik'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:166"
  ]
}
```

### Full SQL program that computes the percentage of XCL_036 values associated with XCL_039='A' from the 'loan' table. It uses a conditional sum in the nu

```json
{
  "kind": "program",
  "formula": "SELECT (CAST(SUM(CASE WHEN \"XCL_039\" = 'A' THEN \"XCL_036\" ELSE 0 END) AS REAL) * 100) / SUM(\"XCL_036\") FROM loan",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:117"
  ]
}
```

### Full SQL program that joins the client table (T1) with the district table (T2) on the district identifier (XCL_012 = XCL_017). It filters for female c

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'F' AND T2.\"XCL_019\" = 'south Bohemia'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:147"
  ]
}
```

### 1997 Weekly Payment Account Lookup

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_001\" FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" WHERE STRFTIME('%Y', T1.\"XCL_035\") = '1997' AND T2.\"XCL_003\" = 'POPLATEK TYDNE' ORDER BY T1.\"XCL_036\" LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:98"
  ]
}
```

### Classic Owner Card Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_005\") FROM card AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_006\" = T2.\"XCL_013\" WHERE T1.\"XCL_007\" = 'classic' AND T2.\"XCL_016\" = 'OWNER'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:153"
  ]
}
```

### A query that joins account, disp, client, and district tables to find accounts linked to the client with the highest XCL_011 value. It filters the dis

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\" FROM account AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_001\" = T2.\"XCL_015\" INNER JOIN client AS T3 ON T2.\"XCL_014\" = T3.\"XCL_009\" INNER JOIN district AS T4 ON T4.\"XCL_017\" = T1.\"XCL_002\" WHERE T2.\"XCL_014\" = (SELECT \"XCL_009\" FROM client ORDER BY \"XCL_011\" DESC LIMIT 1) GROUP BY T4.\"XCL_027\", T1.\"XCL_001\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:95"
  ]
}
```

### Client Loan Lookup

```json
{
  "kind": "program",
  "formula": "SELECT T4.\"XCL_036\", T4.\"XCL_039\" FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN account AS T3 ON T2.\"XCL_015\" = T3.\"XCL_001\" INNER JOIN loan AS T4 ON T3.\"XCL_001\" = T4.\"XCL_034\" WHERE T1.\"XCL_009\" = 992",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:176"
  ]
}
```

### A full SQL program that joins client, disp, account, and loan tables to identify female clients associated with loans. It filters for female clients, 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_009\" FROM client AS T1 INNER JOIN disp AS T4 ON T1.\"XCL_009\" = T4.\"XCL_014\" INNER JOIN account AS T2 ON T4.\"XCL_015\" = T2.\"XCL_001\" INNER JOIN loan AS T3 ON T2.\"XCL_001\" = T3.\"XCL_034\" AND T4.\"XCL_015\" = T3.\"XCL_034\" WHERE T1.\"XCL_010\" = 'F' ORDER BY T3.\"XCL_036\" DESC LIMIT 3",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:181"
  ]
}
```

### Filtered Account Lookup

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_001\" FROM trans AS T1 INNER JOIN account AS T2 ON T1.\"XCL_047\" = T2.\"XCL_001\" WHERE STRFTIME('%Y', T2.\"XCL_004\") < '1997' AND T1.\"XCL_051\" > 3000",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:102"
  ]
}
```

### Disp Role Distribution Query

```json
{
  "kind": "program",
  "formula": "SELECT SUM(\"XCL_016\" = 'OWNER'), SUM(\"XCL_016\" = 'DISPONENT') FROM disp WHERE \"XCL_015\" BETWEEN 1 AND 10",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:172"
  ]
}
```

### Account count in Beroun district after 1996

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_001\") FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE STRFTIME('%Y', T1.\"XCL_004\") > '1996' AND T2.\"XCL_018\" = 'Beroun'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:183"
  ]
}
```

### Aggregates the number of rows in the 'disp' table where the 'XCL_016' field equals 'OWNER', restricted to records where 'XCL_015' is between 1 and 10.

```json
{
  "kind": "metric",
  "formula": "SUM(\"disp\".\"XCL_016\" = 'OWNER')",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_016\" = 'OWNER'), SUM(\"XCL_016\" = 'DISPONENT') FROM disp WHERE \"XCL_015\" BETWEEN 1 AND 10",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r0\".\"XCL_016\" = 'OWNER')",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "disp"
      }
    ],
    "scope_sql": "SELECT SUM(\"r0\".\"XCL_016\" = 'OWNER') AS \"value\" FROM disp AS \"r0\" WHERE \"r0\".\"XCL_015\" BETWEEN 1 AND 10",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:172"
  ]
}
```

### First Female Client District ID

```json
{
  "kind": "binding",
  "formula": "\"client\".\"XCL_012\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_012\" FROM client WHERE \"XCL_010\" = 'F' ORDER BY \"XCL_011\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:94"
  ]
}
```

### District Name

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_018\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_033\", T2.\"XCL_018\", T2.\"XCL_027\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN loan AS T3 ON T1.\"XCL_001\" = T3.\"XCL_034\" WHERE T3.\"XCL_037\" = 60",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_018\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      },
      {
        "role": "r2",
        "physical_table": "loan"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_018\" AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" INNER JOIN loan AS \"r2\" ON \"r0\".\"XCL_001\" = \"r2\".\"XCL_034\" WHERE \"r2\".\"XCL_037\" = 60",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:124"
  ]
}
```

### Account Identifier

```json
{
  "kind": "binding",
  "formula": "\"account\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_001\" FROM trans AS T1 INNER JOIN account AS T2 ON T1.\"XCL_047\" = T2.\"XCL_001\" INNER JOIN district AS T3 ON T2.\"XCL_002\" = T3.\"XCL_017\" WHERE T1.\"XCL_053\" = 'SIPO' AND T3.\"XCL_018\" = 'Pisek'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:142"
  ]
}
```

### "client"."XCL_010" = 'F' AND "card"."XCL_007" = 'junior'

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_010\" = 'F' AND \"card\".\"XCL_007\" = 'junior'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN card AS T3 ON T2.\"XCL_013\" = T3.\"XCL_006\" WHERE T1.\"XCL_010\" = 'F' AND T3.\"XCL_007\" = 'junior'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:184"
  ]
}
```

### Count of Account IDs

```json
{
  "kind": "metric",
  "formula": "COUNT(\"account\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_001\") FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN trans AS T3 ON T2.\"XCL_001\" = T3.\"XCL_047\" WHERE T3.\"XCL_054\" = 'AB' AND T1.\"XCL_019\" = 'north Bohemia'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "district"
      },
      {
        "role": "r1",
        "physical_table": "account"
      },
      {
        "role": "r2",
        "physical_table": "trans"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_001\") AS \"value\" FROM district AS \"r0\" INNER JOIN account AS \"r1\" ON \"r0\".\"XCL_017\" = \"r1\".\"XCL_002\" INNER JOIN trans AS \"r2\" ON \"r1\".\"XCL_001\" = \"r2\".\"XCL_047\" WHERE \"r2\".\"XCL_054\" = 'AB' AND \"r0\".\"XCL_019\" = 'north Bohemia'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:150"
  ]
}
```

### "card"."XCL_008" = '1994-03-03'

```json
{
  "kind": "predicate",
  "formula": "\"card\".\"XCL_008\" = '1994-03-03'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_014\" FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN card AS T3 ON T2.\"XCL_013\" = T3.\"XCL_006\" WHERE T3.\"XCL_008\" = '1994-03-03'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:103"
  ]
}
```

### "account"."XCL_002" = 1 AND ("loan"."XCL_039" = 'C' OR "loan"."XCL_039" = 'D')

```json
{
  "kind": "predicate",
  "formula": "\"account\".\"XCL_002\" = 1 AND (\"loan\".\"XCL_039\" = 'C' OR \"loan\".\"XCL_039\" = 'D')",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN loan AS T3 ON T1.\"XCL_001\" = T3.\"XCL_034\" WHERE T1.\"XCL_002\" = 1 AND (T3.\"XCL_039\" = 'C' OR T3.\"XCL_039\" = 'D')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:137"
  ]
}
```

### "Loan"."XCL_039" = 'A'

```json
{
  "kind": "predicate",
  "formula": "\"Loan\".\"XCL_039\" = 'A'",
  "grain": [
    "\"District\".\"XCL_017\""
  ],
  "population_scope": "SELECT T1.\"XCL_018\" FROM District AS T1 INNER JOIN Account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN Loan AS T3 ON T2.\"XCL_001\" = T3.\"XCL_034\" WHERE T3.\"XCL_039\" = 'A' GROUP BY T1.\"XCL_017\" ORDER BY COUNT(T2.\"XCL_001\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:163"
  ]
}
```

### "client"."XCL_010" = 'M'

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_010\" = 'M'",
  "grain": [],
  "population_scope": "SELECT AVG(T4.\"XCL_036\") FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN account AS T3 ON T2.\"XCL_015\" = T3.\"XCL_001\" INNER JOIN loan AS T4 ON T3.\"XCL_001\" = T4.\"XCL_034\" WHERE T1.\"XCL_010\" = 'M'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:132"
  ]
}
```

### Count of weekly fee accounts with owner

```json
{
  "kind": "metric",
  "formula": "COUNT(\"account\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM account AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_001\" = T2.\"XCL_015\" WHERE T2.\"XCL_016\" = 'OWNER' AND T1.\"XCL_003\" = 'POPLATEK TYDNE'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "disp"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM account AS \"r0\" INNER JOIN disp AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_015\" WHERE \"r1\".\"XCL_016\" = 'OWNER' AND \"r0\".\"XCL_003\" = 'POPLATEK TYDNE'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:96"
  ]
}
```

### District Identifier

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_017\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_017\" FROM \"order\" AS T1 INNER JOIN account AS T2 ON T1.\"XCL_041\" = T2.\"XCL_001\" INNER JOIN district AS T3 ON T2.\"XCL_002\" = T3.\"XCL_017\" WHERE T1.\"XCL_040\" = 33333",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_017\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "order"
      },
      {
        "role": "r1",
        "physical_table": "account"
      },
      {
        "role": "r2",
        "physical_table": "district"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_017\" AS \"value\" FROM \"order\" AS \"r0\" INNER JOIN account AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_001\" INNER JOIN district AS \"r2\" ON \"r1\".\"XCL_002\" = \"r2\".\"XCL_017\" WHERE \"r0\".\"XCL_040\" = 33333",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:158"
  ]
}
```

### District Identifier XCL_017

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_017\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_017\", \"XCL_018\" FROM district ORDER BY \"XCL_029\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:133"
  ]
}
```

### "card"."XCL_008" = '1996-10-21'

```json
{
  "kind": "predicate",
  "formula": "\"card\".\"XCL_008\" = '1996-10-21'",
  "grain": [],
  "population_scope": "SELECT T4.\"XCL_051\" FROM card AS T1 JOIN disp AS T2 ON T1.\"XCL_006\" = T2.\"XCL_013\" JOIN account AS T3 ON T2.\"XCL_015\" = T3.\"XCL_001\" JOIN trans AS T4 ON T3.\"XCL_001\" = T4.\"XCL_047\" WHERE T1.\"XCL_008\" = '1996-10-21' ORDER BY T4.\"XCL_051\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:106"
  ]
}
```

### Calculates the percentage of clients identified as male (XCL_010 = 'M') among all clients who have at least one account with the type 'POPLATEK TYDNE'

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"client\".\"XCL_010\" = 'M') AS REAL) * 100 / COUNT(\"client\".\"XCL_009\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(T1.\"XCL_010\" = 'M') AS REAL) * 100 / COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T3 ON T1.\"XCL_012\" = T3.\"XCL_017\" INNER JOIN account AS T2 ON T2.\"XCL_002\" = T3.\"XCL_017\" INNER JOIN disp AS T4 ON T1.\"XCL_009\" = T4.\"XCL_014\" AND T2.\"XCL_001\" = T4.\"XCL_015\" WHERE T2.\"XCL_003\" = 'POPLATEK TYDNE'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(\"r0\".\"XCL_010\" = 'M') AS REAL) * 100 / COUNT(\"r0\".\"XCL_009\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "district"
      },
      {
        "role": "r2",
        "physical_table": "account"
      },
      {
        "role": "r3",
        "physical_table": "disp"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(\"r0\".\"XCL_010\" = 'M') AS REAL) * 100 / COUNT(\"r0\".\"XCL_009\") AS \"value\" FROM client AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_012\" = \"r1\".\"XCL_017\" INNER JOIN account AS \"r2\" ON \"r2\".\"XCL_002\" = \"r1\".\"XCL_017\" INNER JOIN disp AS \"r3\" ON \"r0\".\"XCL_009\" = \"r3\".\"XCL_014\" AND \"r2\".\"XCL_001\" = \"r3\".\"XCL_015\" WHERE \"r2\".\"XCL_003\" = 'POPLATEK TYDNE'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:186"
  ]
}
```

### "client"."XCL_009" = 992

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_009\" = 992",
  "grain": [],
  "population_scope": "SELECT T4.\"XCL_036\", T4.\"XCL_039\" FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN account AS T3 ON T2.\"XCL_015\" = T3.\"XCL_001\" INNER JOIN loan AS T4 ON T3.\"XCL_001\" = T4.\"XCL_034\" WHERE T1.\"XCL_009\" = 992",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:176"
  ]
}
```

### "district"."XCL_019" = 'Prague'

```json
{
  "kind": "predicate",
  "formula": "\"district\".\"XCL_019\" = 'Prague'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(T2.\"XCL_010\" = 'F') AS REAL) / COUNT(T2.\"XCL_009\") * 100 FROM district AS T1 INNER JOIN client AS T2 ON T1.\"XCL_017\" = T2.\"XCL_012\" WHERE T1.\"XCL_019\" = 'Prague'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:185"
  ]
}
```

### "disp"."XCL_016" = 'OWNER' AND "district"."XCL_018" = 'Tabor'

```json
{
  "kind": "predicate",
  "formula": "\"disp\".\"XCL_016\" = 'OWNER' AND \"district\".\"XCL_018\" = 'Tabor'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_001\" FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN disp AS T3 ON T2.\"XCL_001\" = T3.\"XCL_015\" WHERE T3.\"XCL_016\" = 'OWNER' AND T1.\"XCL_018\" = 'Tabor'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:148"
  ]
}
```

### Female client ID with top 3 loans

```json
{
  "kind": "binding",
  "formula": "\"client\".\"XCL_009\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_009\" FROM client AS T1 INNER JOIN disp AS T4 ON T1.\"XCL_009\" = T4.\"XCL_014\" INNER JOIN account AS T2 ON T4.\"XCL_015\" = T2.\"XCL_001\" INNER JOIN loan AS T3 ON T2.\"XCL_001\" = T3.\"XCL_034\" AND T4.\"XCL_015\" = T3.\"XCL_034\" WHERE T1.\"XCL_010\" = 'F' ORDER BY T3.\"XCL_036\" DESC LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:181"
  ]
}
```

### District Attribute XCL_018

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_018\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_018\", T2.\"XCL_019\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN loan AS T3 ON T1.\"XCL_001\" = T3.\"XCL_034\" WHERE T3.\"XCL_033\" = 4990",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_018\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      },
      {
        "role": "r2",
        "physical_table": "loan"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_018\" AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" INNER JOIN loan AS \"r2\" ON \"r0\".\"XCL_001\" = \"r2\".\"XCL_034\" WHERE \"r2\".\"XCL_033\" = 4990",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:122"
  ]
}
```

### Disponent Identifier

```json
{
  "kind": "binding",
  "formula": "\"disp\".\"XCL_014\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_014\" FROM account AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_001\" = T2.\"XCL_015\" WHERE T1.\"XCL_003\" = 'POPLATEK PO OBRATU' AND T2.\"XCL_016\" = 'DISPONENT'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_014\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "disp"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_014\" AS \"value\" FROM account AS \"r0\" INNER JOIN disp AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_015\" WHERE \"r0\".\"XCL_003\" = 'POPLATEK PO OBRATU' AND \"r1\".\"XCL_016\" = 'DISPONENT'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:97"
  ]
}
```

### STRFTIME('%Y', "client"."XCL_011") = '1920' AND "district"."XCL_019" = 'east Bohemia'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"client\".\"XCL_011\") = '1920' AND \"district\".\"XCL_019\" = 'east Bohemia'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE STRFTIME('%Y', T1.\"XCL_011\") = '1920' AND T2.\"XCL_019\" = 'east Bohemia'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:190"
  ]
}
```

### "client"."XCL_010" = 'F'

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_010\" = 'F'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_009\" FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN account AS T5 ON T2.\"XCL_015\" = T5.\"XCL_001\" INNER JOIN loan AS T3 ON T5.\"XCL_001\" = T3.\"XCL_034\" INNER JOIN card AS T4 ON T2.\"XCL_013\" = T4.\"XCL_006\" WHERE T1.\"XCL_010\" = 'F'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:146"
  ]
}
```

### Client Identifier

```json
{
  "kind": "binding",
  "formula": "\"disp\".\"XCL_014\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_014\" FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN card AS T3 ON T2.\"XCL_013\" = T3.\"XCL_006\" WHERE T3.\"XCL_008\" = '1994-03-03'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_014\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "disp"
      },
      {
        "role": "r2",
        "physical_table": "card"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_014\" AS \"value\" FROM client AS \"r0\" INNER JOIN disp AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_014\" INNER JOIN card AS \"r2\" ON \"r1\".\"XCL_013\" = \"r2\".\"XCL_006\" WHERE \"r2\".\"XCL_008\" = '1994-03-03'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:103"
  ]
}
```

### Aggregates the count of transaction IDs (trans.XCL_047) where the transaction amount (trans.XCL_051) exceeds 4000 and the transaction type (trans.XCL_

```json
{
  "kind": "metric",
  "formula": "COUNT(\"trans\".\"XCL_047\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_047\") FROM trans AS T1 INNER JOIN account AS T2 ON T1.\"XCL_047\" = T2.\"XCL_001\" INNER JOIN disp AS T4 ON T2.\"XCL_001\" = T4.\"XCL_015\" INNER JOIN client AS T3 ON T4.\"XCL_014\" = T3.\"XCL_009\" WHERE STRFTIME('%Y', T3.\"XCL_011\") BETWEEN '1974' AND '1976' AND T3.\"XCL_010\" = 'M' AND T1.\"XCL_051\" > 4000 AND T1.\"XCL_053\" = 'SIPO'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_047\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "trans"
      },
      {
        "role": "r1",
        "physical_table": "account"
      },
      {
        "role": "r2",
        "physical_table": "disp"
      },
      {
        "role": "r3",
        "physical_table": "client"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_047\") AS \"value\" FROM trans AS \"r0\" INNER JOIN account AS \"r1\" ON \"r0\".\"XCL_047\" = \"r1\".\"XCL_001\" INNER JOIN disp AS \"r2\" ON \"r1\".\"XCL_001\" = \"r2\".\"XCL_015\" INNER JOIN client AS \"r3\" ON \"r2\".\"XCL_014\" = \"r3\".\"XCL_009\" WHERE STRFTIME('%Y', \"r3\".\"XCL_011\") BETWEEN '1974' AND '1976' AND \"r3\".\"XCL_010\" = 'M' AND \"r0\".\"XCL_051\" > 4000 AND \"r0\".\"XCL_053\" = 'SIPO'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:182"
  ]
}
```

### Client Identifier

```json
{
  "kind": "binding",
  "formula": "\"client\".\"XCL_010\"",
  "grain": [],
  "population_scope": "SELECT T4.\"XCL_052\", T1.\"XCL_010\" FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN account AS T3 ON T2.\"XCL_015\" = T3.\"XCL_001\" INNER JOIN trans AS T4 ON T3.\"XCL_001\" = T4.\"XCL_047\" WHERE T1.\"XCL_009\" = 4 AND T4.\"XCL_046\" = 851",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_010\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "disp"
      },
      {
        "role": "r2",
        "physical_table": "account"
      },
      {
        "role": "r3",
        "physical_table": "trans"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_010\" AS \"value\" FROM client AS \"r0\" INNER JOIN disp AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_014\" INNER JOIN account AS \"r2\" ON \"r1\".\"XCL_015\" = \"r2\".\"XCL_001\" INNER JOIN trans AS \"r3\" ON \"r2\".\"XCL_001\" = \"r3\".\"XCL_047\" WHERE \"r0\".\"XCL_009\" = 4 AND \"r3\".\"XCL_046\" = 851",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:177"
  ]
}
```

### "card"."XCL_007" = 'gold' AND "disp"."XCL_016" = 'OWNER'

```json
{
  "kind": "predicate",
  "formula": "\"card\".\"XCL_007\" = 'gold' AND \"disp\".\"XCL_016\" = 'OWNER'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_005\") FROM card AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_006\" = T2.\"XCL_013\" WHERE T1.\"XCL_007\" = 'gold' AND T2.\"XCL_016\" = 'OWNER'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:139"
  ]
}
```

### Order Category/Type Key (Output)

```json
{
  "kind": "binding",
  "formula": "T2.\"XCL_045\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\", T2.\"XCL_045\" FROM account AS T1 INNER JOIN (SELECT \"XCL_041\", \"XCL_045\", SUM(\"XCL_044\") AS total_amount FROM \"order\" GROUP BY \"XCL_041\", \"XCL_045\") AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_001\" = 3 AND T2.\"total_amount\" = 3539",
  "upstream_scopes": [
    "SELECT \"XCL_041\", \"XCL_045\", SUM(\"XCL_044\") AS total_amount FROM \"order\" GROUP BY \"XCL_041\", \"XCL_045\""
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:173"
  ]
}
```

### STRFTIME('%Y', "account"."XCL_004") = '1996' AND "district"."XCL_018" = 'Litomerice'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"account\".\"XCL_004\") = '1996' AND \"district\".\"XCL_018\" = 'Litomerice'",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_001\") FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE STRFTIME('%Y', T2.\"XCL_004\") = '1996' AND T1.\"XCL_018\" = 'Litomerice'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:111"
  ]
}
```

### "client"."XCL_010" = 'M' AND "district"."XCL_019" = 'north Bohemia' AND "district"."XCL_027" > 8000

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_010\" = 'M' AND \"district\".\"XCL_019\" = 'north Bohemia' AND \"district\".\"XCL_027\" > 8000",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'M' AND T2.\"XCL_019\" = 'north Bohemia' AND T2.\"XCL_027\" > 8000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:93"
  ]
}
```

### Client Identifier

```json
{
  "kind": "binding",
  "formula": "\"client\".\"XCL_009\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_009\", T3.\"XCL_001\" FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" INNER JOIN disp AS T4 ON T1.\"XCL_009\" = T4.\"XCL_014\" INNER JOIN account AS T3 ON T2.\"XCL_017\" = T3.\"XCL_002\" AND T4.\"XCL_015\" = T3.\"XCL_001\" WHERE T2.\"XCL_019\" = 'east Bohemia' AND STRFTIME('%Y', T1.\"XCL_011\") BETWEEN '1983' AND '1987'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_009\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "district"
      },
      {
        "role": "r2",
        "physical_table": "disp"
      },
      {
        "role": "r3",
        "physical_table": "account"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_009\" AS \"value\" FROM client AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_012\" = \"r1\".\"XCL_017\" INNER JOIN disp AS \"r2\" ON \"r0\".\"XCL_009\" = \"r2\".\"XCL_014\" INNER JOIN account AS \"r3\" ON \"r1\".\"XCL_017\" = \"r3\".\"XCL_002\" AND \"r2\".\"XCL_015\" = \"r3\".\"XCL_001\" WHERE \"r1\".\"XCL_019\" = 'east Bohemia' AND STRFTIME('%Y', \"r0\".\"XCL_011\") BETWEEN '1983' AND '1987'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:180"
  ]
}
```

### "client"."XCL_010" = 'M' AND "district"."XCL_018" = 'Hl.m. Praha'

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_010\" = 'M' AND \"district\".\"XCL_018\" = 'Hl.m. Praha'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'M' AND T2.\"XCL_018\" = 'Hl.m. Praha'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:154"
  ]
}
```

### Average 1998 Transaction Amount

```json
{
  "kind": "metric",
  "formula": "AVG(\"trans\".\"XCL_051\")",
  "grain": [],
  "population_scope": "SELECT AVG(\"XCL_051\") FROM trans WHERE STRFTIME('%Y', \"XCL_048\") = '1998'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_051\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "trans"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_051\") AS \"value\" FROM trans AS \"r0\" WHERE STRFTIME('%Y', \"r0\".\"XCL_048\") = '1998'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:145"
  ]
}
```

### "loan"."XCL_033" = 4990

```json
{
  "kind": "predicate",
  "formula": "\"loan\".\"XCL_033\" = 4990",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_018\", T2.\"XCL_019\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN loan AS T3 ON T1.\"XCL_001\" = T3.\"XCL_034\" WHERE T3.\"XCL_033\" = 4990",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:122"
  ]
}
```

### Aggregates the count of client records (identified by XCL_009) where the client gender (XCL_010) is 'M' and the associated district (XCL_018) is 'Hl.m

```json
{
  "kind": "metric",
  "formula": "COUNT(\"client\".\"XCL_009\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'M' AND T2.\"XCL_018\" = 'Hl.m. Praha'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_009\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "district"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_009\") AS \"value\" FROM client AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_012\" = \"r1\".\"XCL_017\" WHERE \"r0\".\"XCL_010\" = 'M' AND \"r1\".\"XCL_018\" = 'Hl.m. Praha'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:154"
  ]
}
```

### Loan Identifier

```json
{
  "kind": "binding",
  "formula": "\"loan\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T4.\"XCL_036\", T4.\"XCL_039\" FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN account AS T3 ON T2.\"XCL_015\" = T3.\"XCL_001\" INNER JOIN loan AS T4 ON T3.\"XCL_001\" = T4.\"XCL_034\" WHERE T1.\"XCL_009\" = 992",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r3\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "disp"
      },
      {
        "role": "r2",
        "physical_table": "account"
      },
      {
        "role": "r3",
        "physical_table": "loan"
      }
    ],
    "scope_sql": "SELECT \"r3\".\"XCL_036\" AS \"value\" FROM client AS \"r0\" INNER JOIN disp AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_014\" INNER JOIN account AS \"r2\" ON \"r1\".\"XCL_015\" = \"r2\".\"XCL_001\" INNER JOIN loan AS \"r3\" ON \"r2\".\"XCL_001\" = \"r3\".\"XCL_034\" WHERE \"r0\".\"XCL_009\" = 992",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:176"
  ]
}
```

### Account Attribute

```json
{
  "kind": "binding",
  "formula": "\"account\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T1.\"XCL_003\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE T2.\"XCL_019\" = 'east Bohemia' AND STRFTIME('%Y', T1.\"XCL_004\") BETWEEN '1995' AND '2000'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_003\" AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" WHERE \"r1\".\"XCL_019\" = 'east Bohemia' AND STRFTIME('%Y', \"r0\".\"XCL_004\") BETWEEN '1995' AND '2000'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:120"
  ]
}
```

### District Region

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T2.\"XCL_018\", T2.\"XCL_019\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE T1.\"XCL_003\" = 'POPLATEK PO OBRATU' AND STRFTIME('%Y', T1.\"XCL_004\") = '1993'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_019\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_019\" AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" WHERE \"r0\".\"XCL_003\" = 'POPLATEK PO OBRATU' AND STRFTIME('%Y', \"r0\".\"XCL_004\") = '1993'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:119"
  ]
}
```

### District Identifier

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM district AS T1 INNER JOIN client AS T2 ON T1.\"XCL_017\" = T2.\"XCL_012\" WHERE T2.\"XCL_009\" = 3541",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_019\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "district"
      },
      {
        "role": "r1",
        "physical_table": "client"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_019\" AS \"value\" FROM district AS \"r0\" INNER JOIN client AS \"r1\" ON \"r0\".\"XCL_017\" = \"r1\".\"XCL_012\" WHERE \"r1\".\"XCL_009\" = 3541",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:162"
  ]
}
```

### "disp"."XCL_016" = 'OWNER' AND "account"."XCL_003" = 'POPLATEK PO OBRATU'

```json
{
  "kind": "predicate",
  "formula": "\"disp\".\"XCL_016\" = 'OWNER' AND \"account\".\"XCL_003\" = 'POPLATEK PO OBRATU'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM account AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_001\" = T2.\"XCL_015\" WHERE T2.\"XCL_016\" = 'OWNER' AND T1.\"XCL_003\" = 'POPLATEK PO OBRATU'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:175"
  ]
}
```

### "client"."XCL_010" = 'F'

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_010\" = 'F'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_009\" FROM client AS T1 INNER JOIN disp AS T4 ON T1.\"XCL_009\" = T4.\"XCL_014\" INNER JOIN account AS T2 ON T4.\"XCL_015\" = T2.\"XCL_001\" INNER JOIN loan AS T3 ON T2.\"XCL_001\" = T3.\"XCL_034\" AND T4.\"XCL_015\" = T3.\"XCL_034\" WHERE T1.\"XCL_010\" = 'F' ORDER BY T3.\"XCL_036\" DESC LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:181"
  ]
}
```

### "loan"."XCL_039" IN ('C', 'D') AND "account"."XCL_003" = 'POPLATEK PO OBRATU'

```json
{
  "kind": "predicate",
  "formula": "\"loan\".\"XCL_039\" IN ('C', 'D') AND \"account\".\"XCL_003\" = 'POPLATEK PO OBRATU'",
  "grain": [],
  "population_scope": "SELECT AVG(T2.\"XCL_036\") FROM account AS T1 INNER JOIN loan AS T2 ON T1.\"XCL_001\" = T2.\"XCL_034\" WHERE T2.\"XCL_039\" IN ('C', 'D') AND T1.\"XCL_003\" = 'POPLATEK PO OBRATU'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:192"
  ]
}
```

### Account Identifier

```json
{
  "kind": "binding",
  "formula": "\"account\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T2.\"XCL_018\", T2.\"XCL_019\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN loan AS T3 ON T1.\"XCL_001\" = T3.\"XCL_034\" WHERE T3.\"XCL_036\" > 300000",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      },
      {
        "role": "r2",
        "physical_table": "loan"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" INNER JOIN loan AS \"r2\" ON \"r0\".\"XCL_001\" = \"r2\".\"XCL_034\" WHERE \"r2\".\"XCL_036\" > 300000",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:123"
  ]
}
```

### Account Identifier

```json
{
  "kind": "binding",
  "formula": "\"trans\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_047\" FROM trans AS T1 INNER JOIN account AS T2 ON T1.\"XCL_047\" = T2.\"XCL_001\" WHERE STRFTIME('%Y', T1.\"XCL_048\") = '1998' AND T1.\"XCL_050\" = 'VYBER KARTOU' AND T1.\"XCL_051\" < (SELECT AVG(\"XCL_051\") FROM trans WHERE STRFTIME('%Y', \"XCL_048\") = '1998')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:145"
  ]
}
```

### Average District XCL_031

```json
{
  "kind": "metric",
  "formula": "AVG(\"district\".\"XCL_031\")",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_031\") FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE STRFTIME('%Y', T2.\"XCL_004\") >= '1997' AND T1.\"XCL_031\" > 4000",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_031\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "district"
      },
      {
        "role": "r1",
        "physical_table": "account"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_031\") AS \"value\" FROM district AS \"r0\" INNER JOIN account AS \"r1\" ON \"r0\".\"XCL_017\" = \"r1\".\"XCL_002\" WHERE STRFTIME('%Y', \"r1\".\"XCL_004\") >= '1997' AND \"r0\".\"XCL_031\" > 4000",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:152"
  ]
}
```

### Account Count in Pisek District

```json
{
  "kind": "metric",
  "formula": "COUNT(\"account\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE T2.\"XCL_018\" = 'Pisek'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" WHERE \"r1\".\"XCL_018\" = 'Pisek'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:140"
  ]
}
```

### "trans"."XCL_049" = 'VYDAJ'

```json
{
  "kind": "predicate",
  "formula": "\"trans\".\"XCL_049\" = 'VYDAJ'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_018\" FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN trans AS T3 ON T2.\"XCL_001\" = T3.\"XCL_047\" WHERE T3.\"XCL_049\" = 'VYDAJ'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:151"
  ]
}
```

### Aggregates the number of account records (XCL_001) joined to districts in 'east Bohemia' where the account type or status (XCL_003) is 'POPLATEK PO OB

```json
{
  "kind": "metric",
  "formula": "COUNT(\"account\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_001\") FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE T1.\"XCL_019\" = 'east Bohemia' AND T2.\"XCL_003\" = 'POPLATEK PO OBRATU'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "district"
      },
      {
        "role": "r1",
        "physical_table": "account"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_001\") AS \"value\" FROM district AS \"r0\" INNER JOIN account AS \"r1\" ON \"r0\".\"XCL_017\" = \"r1\".\"XCL_002\" WHERE \"r0\".\"XCL_019\" = 'east Bohemia' AND \"r1\".\"XCL_003\" = 'POPLATEK PO OBRATU'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:89"
  ]
}
```

### "disp"."XCL_016" <> 'OWNER' AND "district"."XCL_027" BETWEEN 8000 AND 9000

```json
{
  "kind": "predicate",
  "formula": "\"disp\".\"XCL_016\" <> 'OWNER' AND \"district\".\"XCL_027\" BETWEEN 8000 AND 9000",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_016\" FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN disp AS T3 ON T2.\"XCL_001\" = T3.\"XCL_015\" WHERE T3.\"XCL_016\" <> 'OWNER' AND T1.\"XCL_027\" BETWEEN 8000 AND 9000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:149"
  ]
}
```

### The value of column XCL_013 from the disp table, filtered to rows where the associated account has a transaction on 1997-08-20 with XCL_051 equal to 5

```json
{
  "kind": "binding",
  "formula": "\"disp\".\"XCL_013\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_013\" FROM disp AS T1 INNER JOIN account AS T2 ON T1.\"XCL_015\" = T2.\"XCL_001\" INNER JOIN trans AS T3 ON T2.\"XCL_001\" = T3.\"XCL_047\" WHERE T3.\"XCL_048\" = '1997-08-20' AND T3.\"XCL_051\" = 5100",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_013\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "disp"
      },
      {
        "role": "r1",
        "physical_table": "account"
      },
      {
        "role": "r2",
        "physical_table": "trans"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_013\" AS \"value\" FROM disp AS \"r0\" INNER JOIN account AS \"r1\" ON \"r0\".\"XCL_015\" = \"r1\".\"XCL_001\" INNER JOIN trans AS \"r2\" ON \"r1\".\"XCL_001\" = \"r2\".\"XCL_047\" WHERE \"r2\".\"XCL_048\" = '1997-08-20' AND \"r2\".\"XCL_051\" = 5100",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:110"
  ]
}
```

### "district"."XCL_019" = 'east Bohemia' AND STRFTIME('%Y', "client"."XCL_011") BETWEEN '1983' AND '1987'

```json
{
  "kind": "predicate",
  "formula": "\"district\".\"XCL_019\" = 'east Bohemia' AND STRFTIME('%Y', \"client\".\"XCL_011\") BETWEEN '1983' AND '1987'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_009\", T3.\"XCL_001\" FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" INNER JOIN disp AS T4 ON T1.\"XCL_009\" = T4.\"XCL_014\" INNER JOIN account AS T3 ON T2.\"XCL_017\" = T3.\"XCL_002\" AND T4.\"XCL_015\" = T3.\"XCL_001\" WHERE T2.\"XCL_019\" = 'east Bohemia' AND STRFTIME('%Y', T1.\"XCL_011\") BETWEEN '1983' AND '1987'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:180"
  ]
}
```

### Account Count for District Jesenik

```json
{
  "kind": "metric",
  "formula": "COUNT(\"account\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_001\") FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE T1.\"XCL_018\" = 'Jesenik'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "district"
      },
      {
        "role": "r1",
        "physical_table": "account"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_001\") AS \"value\" FROM district AS \"r0\" INNER JOIN account AS \"r1\" ON \"r0\".\"XCL_017\" = \"r1\".\"XCL_002\" WHERE \"r0\".\"XCL_018\" = 'Jesenik'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:166"
  ]
}
```

### "trans"."XCL_048" = '1997-08-20' AND "trans"."XCL_051" = 5100

```json
{
  "kind": "predicate",
  "formula": "\"trans\".\"XCL_048\" = '1997-08-20' AND \"trans\".\"XCL_051\" = 5100",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_013\" FROM disp AS T1 INNER JOIN account AS T2 ON T1.\"XCL_015\" = T2.\"XCL_001\" INNER JOIN trans AS T3 ON T2.\"XCL_001\" = T3.\"XCL_047\" WHERE T3.\"XCL_048\" = '1997-08-20' AND T3.\"XCL_051\" = 5100",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:110"
  ]
}
```

### Aggregates the count of client identifiers (XCL_009) for clients who are female (XCL_010 = 'F') and hold at least one junior card (XCL_007 = 'junior')

```json
{
  "kind": "metric",
  "formula": "COUNT(\"client\".\"XCL_009\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN card AS T3 ON T2.\"XCL_013\" = T3.\"XCL_006\" WHERE T1.\"XCL_010\" = 'F' AND T3.\"XCL_007\" = 'junior'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_009\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "disp"
      },
      {
        "role": "r2",
        "physical_table": "card"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_009\") AS \"value\" FROM client AS \"r0\" INNER JOIN disp AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_014\" INNER JOIN card AS \"r2\" ON \"r1\".\"XCL_013\" = \"r2\".\"XCL_006\" WHERE \"r0\".\"XCL_010\" = 'F' AND \"r2\".\"XCL_007\" = 'junior'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:184"
  ]
}
```

### Account Identifier

```json
{
  "kind": "binding",
  "formula": "\"account\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_001\" FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" WHERE STRFTIME('%Y', T1.\"XCL_035\") = '1997' AND T2.\"XCL_003\" = 'POPLATEK TYDNE' ORDER BY T1.\"XCL_036\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:98"
  ]
}
```

### A district-level attribute (XCL_018) retrieved from the district table. It is joined to the account via the account's district reference (XCL_002) and

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_018\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T2.\"XCL_018\", T2.\"XCL_019\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN loan AS T3 ON T1.\"XCL_001\" = T3.\"XCL_034\" WHERE T3.\"XCL_036\" > 300000",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_018\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      },
      {
        "role": "r2",
        "physical_table": "loan"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_018\" AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" INNER JOIN loan AS \"r2\" ON \"r0\".\"XCL_001\" = \"r2\".\"XCL_034\" WHERE \"r2\".\"XCL_036\" > 300000",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:123"
  ]
}
```

### District Average Salary

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_027\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_033\", T2.\"XCL_018\", T2.\"XCL_027\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN loan AS T3 ON T1.\"XCL_001\" = T3.\"XCL_034\" WHERE T3.\"XCL_037\" = 60",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_027\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      },
      {
        "role": "r2",
        "physical_table": "loan"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_027\" AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" INNER JOIN loan AS \"r2\" ON \"r0\".\"XCL_001\" = \"r2\".\"XCL_034\" WHERE \"r2\".\"XCL_037\" = 60",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:124"
  ]
}
```

### Loan Identifier

```json
{
  "kind": "binding",
  "formula": "\"loan\".\"XCL_033\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_033\", T2.\"XCL_018\", T2.\"XCL_027\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN loan AS T3 ON T1.\"XCL_001\" = T3.\"XCL_034\" WHERE T3.\"XCL_037\" = 60",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_033\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      },
      {
        "role": "r2",
        "physical_table": "loan"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_033\" AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" INNER JOIN loan AS \"r2\" ON \"r0\".\"XCL_001\" = \"r2\".\"XCL_034\" WHERE \"r2\".\"XCL_037\" = 60",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:124"
  ]
}
```

### "loan"."XCL_039" IN ('C', 'D')

```json
{
  "kind": "predicate",
  "formula": "\"loan\".\"XCL_039\" IN ('C', 'D')",
  "grain": [
    "\"district\".\"XCL_019\""
  ],
  "population_scope": "SELECT T2.\"XCL_019\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN loan AS T3 ON T1.\"XCL_001\" = T3.\"XCL_034\" WHERE T3.\"XCL_039\" IN ('C', 'D') GROUP BY T2.\"XCL_019\" ORDER BY SUM(T3.\"XCL_036\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:131"
  ]
}
```

### "client"."XCL_010" = 'M' AND "disp"."XCL_016" = 'OWNER'

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_010\" = 'M' AND \"disp\".\"XCL_016\" = 'OWNER'",
  "grain": [],
  "population_scope": "SELECT CAST((SUM(CASE WHEN STRFTIME('%Y', T1.\"XCL_035\") = '1997' THEN T1.\"XCL_036\" ELSE 0 END) - SUM(CASE WHEN STRFTIME('%Y', T1.\"XCL_035\") = '1996' THEN T1.\"XCL_036\" ELSE 0 END)) AS REAL) * 100 / SUM(CASE WHEN STRFTIME('%Y', T1.\"XCL_035\") = '1996' THEN T1.\"XCL_036\" ELSE 0 END) FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" INNER JOIN disp AS T3 ON T3.\"XCL_015\" = T2.\"XCL_001\" INNER JOIN client AS T4 ON T4.\"XCL_009\" = T3.\"XCL_014\" WHERE T4.\"XCL_010\" = 'M' AND T3.\"XCL_016\" = 'OWNER'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:169"
  ]
}
```

### Account ID for Top Client

```json
{
  "kind": "binding",
  "formula": "\"account\".\"XCL_001\"",
  "grain": [
    "\"district\".\"XCL_027\"",
    "\"account\".\"XCL_001\""
  ],
  "population_scope": "SELECT T1.\"XCL_001\" FROM account AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_001\" = T2.\"XCL_015\" INNER JOIN client AS T3 ON T2.\"XCL_014\" = T3.\"XCL_009\" INNER JOIN district AS T4 ON T4.\"XCL_017\" = T1.\"XCL_002\" WHERE T2.\"XCL_014\" = (SELECT \"XCL_009\" FROM client ORDER BY \"XCL_011\" DESC LIMIT 1) GROUP BY T4.\"XCL_027\", T1.\"XCL_001\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:95"
  ]
}
```

### The value of the transaction amount field (XCL_051) from the trans table. In this context, it represents the maximum transaction amount associated wit

```json
{
  "kind": "binding",
  "formula": "\"trans\".\"XCL_051\"",
  "grain": [],
  "population_scope": "SELECT T4.\"XCL_051\" FROM card AS T1 JOIN disp AS T2 ON T1.\"XCL_006\" = T2.\"XCL_013\" JOIN account AS T3 ON T2.\"XCL_015\" = T3.\"XCL_001\" JOIN trans AS T4 ON T3.\"XCL_001\" = T4.\"XCL_047\" WHERE T1.\"XCL_008\" = '1996-10-21' ORDER BY T4.\"XCL_051\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:106"
  ]
}
```

### Account Count by District

```json
{
  "kind": "metric",
  "formula": "COUNT(\"account\".\"XCL_001\")",
  "grain": [
    "\"district\".\"XCL_032\""
  ],
  "population_scope": "SELECT COUNT(T2.\"XCL_001\") FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" GROUP BY T1.\"XCL_032\" ORDER BY T1.\"XCL_032\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:134"
  ]
}
```

### Card Withdrawal Transaction Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"trans\".\"XCL_047\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_047\") FROM trans WHERE STRFTIME('%Y', \"XCL_048\") > '1995' AND \"XCL_050\" = 'VYBER KARTOU'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_047\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "trans"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_047\") AS \"value\" FROM trans AS \"r0\" WHERE STRFTIME('%Y', \"r0\".\"XCL_048\") > '1995' AND \"r0\".\"XCL_050\" = 'VYBER KARTOU'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:170"
  ]
}
```

### STRFTIME('%Y', "account"."XCL_004") > '1996' AND "district"."XCL_018" = 'Beroun'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"account\".\"XCL_004\") > '1996' AND \"district\".\"XCL_018\" = 'Beroun'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE STRFTIME('%Y', T1.\"XCL_004\") > '1996' AND T2.\"XCL_018\" = 'Beroun'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:183"
  ]
}
```

### "disp"."XCL_016" = 'OWNER'

```json
{
  "kind": "predicate",
  "formula": "\"disp\".\"XCL_016\" = 'OWNER'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_014\", T2.\"XCL_017\", T2.\"XCL_018\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN disp AS T3 ON T1.\"XCL_001\" = T3.\"XCL_015\" WHERE T3.\"XCL_016\" = 'OWNER'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:193"
  ]
}
```

### STRFTIME('%Y', "client"."XCL_011") BETWEEN '1974' AND '1976' AND "client"."XCL_010" = 'M' AND "trans"."XCL_051" > 4000 AND "trans"."XCL_053" = 'SIPO'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"client\".\"XCL_011\") BETWEEN '1974' AND '1976' AND \"client\".\"XCL_010\" = 'M' AND \"trans\".\"XCL_051\" > 4000 AND \"trans\".\"XCL_053\" = 'SIPO'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_047\") FROM trans AS T1 INNER JOIN account AS T2 ON T1.\"XCL_047\" = T2.\"XCL_001\" INNER JOIN disp AS T4 ON T2.\"XCL_001\" = T4.\"XCL_015\" INNER JOIN client AS T3 ON T4.\"XCL_014\" = T3.\"XCL_009\" WHERE STRFTIME('%Y', T3.\"XCL_011\") BETWEEN '1974' AND '1976' AND T3.\"XCL_010\" = 'M' AND T1.\"XCL_051\" > 4000 AND T1.\"XCL_053\" = 'SIPO'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:182"
  ]
}
```

### Female Client Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"client\".\"XCL_009\")",
  "grain": [
    "\"district\".\"XCL_017\"",
    "\"district\".\"XCL_018\""
  ],
  "population_scope": "SELECT T2.\"XCL_018\", COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'F' GROUP BY T2.\"XCL_017\", T2.\"XCL_018\" ORDER BY COUNT(T1.\"XCL_009\") DESC LIMIT 9",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:128"
  ]
}
```

### "disp"."XCL_016" = 'OWNER' AND "account"."XCL_003" = 'POPLATEK TYDNE'

```json
{
  "kind": "predicate",
  "formula": "\"disp\".\"XCL_016\" = 'OWNER' AND \"account\".\"XCL_003\" = 'POPLATEK TYDNE'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM account AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_001\" = T2.\"XCL_015\" WHERE T2.\"XCL_016\" = 'OWNER' AND T1.\"XCL_003\" = 'POPLATEK TYDNE'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:96"
  ]
}
```

### "client"."XCL_009" = 13539

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_009\" = 13539",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_007\" FROM disp AS T1 INNER JOIN client AS T2 ON T1.\"XCL_014\" = T2.\"XCL_009\" INNER JOIN card AS T3 ON T1.\"XCL_013\" = T3.\"XCL_006\" WHERE T2.\"XCL_009\" = 13539",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:161"
  ]
}
```

### "client"."XCL_010" = 'F'

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_010\" = 'F'",
  "grain": [],
  "population_scope": "SELECT \"XCL_012\" FROM client WHERE \"XCL_010\" = 'F' ORDER BY \"XCL_011\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:94"
  ]
}
```

### The value of the transaction amount field (XCL_046) from the trans table. The grain is individual transactions filtered to those of type 'VYBER' (with

```json
{
  "kind": "binding",
  "formula": "\"trans\".\"XCL_046\"",
  "grain": [],
  "population_scope": "SELECT T4.\"XCL_046\" FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN account AS T3 ON T2.\"XCL_015\" = T3.\"XCL_001\" INNER JOIN trans AS T4 ON T3.\"XCL_001\" = T4.\"XCL_047\" WHERE T1.\"XCL_009\" = 3356 AND T4.\"XCL_050\" = 'VYBER'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r3\".\"XCL_046\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "disp"
      },
      {
        "role": "r2",
        "physical_table": "account"
      },
      {
        "role": "r3",
        "physical_table": "trans"
      }
    ],
    "scope_sql": "SELECT \"r3\".\"XCL_046\" AS \"value\" FROM client AS \"r0\" INNER JOIN disp AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_014\" INNER JOIN account AS \"r2\" ON \"r1\".\"XCL_015\" = \"r2\".\"XCL_001\" INNER JOIN trans AS \"r3\" ON \"r2\".\"XCL_001\" = \"r3\".\"XCL_047\" WHERE \"r0\".\"XCL_009\" = 3356 AND \"r3\".\"XCL_050\" = 'VYBER'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:159"
  ]
}
```

### "client"."XCL_009" = 4 AND "trans"."XCL_046" = 851

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_009\" = 4 AND \"trans\".\"XCL_046\" = 851",
  "grain": [],
  "population_scope": "SELECT T4.\"XCL_052\", T1.\"XCL_010\" FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN account AS T3 ON T2.\"XCL_015\" = T3.\"XCL_001\" INNER JOIN trans AS T4 ON T3.\"XCL_001\" = T4.\"XCL_047\" WHERE T1.\"XCL_009\" = 4 AND T4.\"XCL_046\" = 851",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:177"
  ]
}
```

### "client"."XCL_009" = 3541

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_009\" = 3541",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM district AS T1 INNER JOIN client AS T2 ON T1.\"XCL_017\" = T2.\"XCL_012\" WHERE T2.\"XCL_009\" = 3541",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:162"
  ]
}
```

### "client"."XCL_010" = 'F' AND STRFTIME('%Y', "client"."XCL_011") < '1950' AND "district"."XCL_018" = 'Sokolov'

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_010\" = 'F' AND STRFTIME('%Y', \"client\".\"XCL_011\") < '1950' AND \"district\".\"XCL_018\" = 'Sokolov'",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_009\") FROM district AS T1 INNER JOIN client AS T2 ON T1.\"XCL_017\" = T2.\"XCL_012\" WHERE T2.\"XCL_010\" = 'F' AND STRFTIME('%Y', T2.\"XCL_011\") < '1950' AND T1.\"XCL_018\" = 'Sokolov'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:100"
  ]
}
```

### "client"."XCL_010" = 'F'

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_010\" = 'F'",
  "grain": [
    "\"district\".\"XCL_017\"",
    "\"district\".\"XCL_018\""
  ],
  "population_scope": "SELECT T2.\"XCL_018\", COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'F' GROUP BY T2.\"XCL_017\", T2.\"XCL_018\" ORDER BY COUNT(T1.\"XCL_009\") DESC LIMIT 9",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:128"
  ]
}
```

### Aggregates the count of account identifiers (XCL_001) for accounts classified as 'POPLATEK MESICNE' (monthly payment) that are associated with loans h

```json
{
  "kind": "metric",
  "formula": "COUNT(\"account\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM account AS T1 INNER JOIN loan AS T2 ON T1.\"XCL_001\" = T2.\"XCL_034\" WHERE T2.\"XCL_035\" BETWEEN '1995-01-01' AND '1997-12-31' AND T1.\"XCL_003\" = 'POPLATEK MESICNE' AND T2.\"XCL_036\" >= 250000",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "loan"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM account AS \"r0\" INNER JOIN loan AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_034\" WHERE \"r1\".\"XCL_035\" BETWEEN '1995-01-01' AND '1997-12-31' AND \"r0\".\"XCL_003\" = 'POPLATEK MESICNE' AND \"r1\".\"XCL_036\" >= 250000",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:136"
  ]
}
```

### Account Identifier

```json
{
  "kind": "binding",
  "formula": "\"account\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_001\" FROM trans AS T1 INNER JOIN account AS T2 ON T1.\"XCL_047\" = T2.\"XCL_001\" WHERE STRFTIME('%Y', T2.\"XCL_004\") < '1997' AND T1.\"XCL_051\" > 3000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:102"
  ]
}
```

### District XCL_027 Range

```json
{
  "kind": "metric",
  "formula": "MAX(\"district\".\"XCL_027\") - MIN(\"district\".\"XCL_027\")",
  "grain": [],
  "population_scope": "SELECT MAX(\"XCL_027\") - MIN(\"XCL_027\") FROM district",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MAX(\"r0\".\"XCL_027\") - MIN(\"r0\".\"XCL_027\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "district"
      }
    ],
    "scope_sql": "SELECT MAX(\"r0\".\"XCL_027\") - MIN(\"r0\".\"XCL_027\") AS \"value\" FROM district AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:94"
  ]
}
```

### "loan"."XCL_036" < 100000

```json
{
  "kind": "predicate",
  "formula": "\"loan\".\"XCL_036\" < 100000",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(\"XCL_039\" = 'C') AS REAL) * 100 / COUNT(\"XCL_034\") FROM loan WHERE \"XCL_036\" < 100000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:118"
  ]
}
```

### The value of column XCL_052 from the trans table. Represents a specific transaction record linked to the filtered client and account.

```json
{
  "kind": "binding",
  "formula": "\"trans\".\"XCL_052\"",
  "grain": [],
  "population_scope": "SELECT T4.\"XCL_052\", T1.\"XCL_010\" FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN account AS T3 ON T2.\"XCL_015\" = T3.\"XCL_001\" INNER JOIN trans AS T4 ON T3.\"XCL_001\" = T4.\"XCL_047\" WHERE T1.\"XCL_009\" = 4 AND T4.\"XCL_046\" = 851",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r3\".\"XCL_052\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "disp"
      },
      {
        "role": "r2",
        "physical_table": "account"
      },
      {
        "role": "r3",
        "physical_table": "trans"
      }
    ],
    "scope_sql": "SELECT \"r3\".\"XCL_052\" AS \"value\" FROM client AS \"r0\" INNER JOIN disp AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_014\" INNER JOIN account AS \"r2\" ON \"r1\".\"XCL_015\" = \"r2\".\"XCL_001\" INNER JOIN trans AS \"r3\" ON \"r2\".\"XCL_001\" = \"r3\".\"XCL_047\" WHERE \"r0\".\"XCL_009\" = 4 AND \"r3\".\"XCL_046\" = 851",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:177"
  ]
}
```

### "card"."XCL_007" = 'junior' AND "card"."XCL_008" >= '1997-01-01'

```json
{
  "kind": "predicate",
  "formula": "\"card\".\"XCL_007\" = 'junior' AND \"card\".\"XCL_008\" >= '1997-01-01'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_014\" FROM card AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_006\" = T2.\"XCL_013\" WHERE T1.\"XCL_007\" = 'junior' AND T1.\"XCL_008\" >= '1997-01-01'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:167"
  ]
}
```

### "loan"."XCL_037" > 24 AND STRFTIME('%Y', "account"."XCL_004") < '1997'

```json
{
  "kind": "predicate",
  "formula": "\"loan\".\"XCL_037\" > 24 AND STRFTIME('%Y', \"account\".\"XCL_004\") < '1997'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_034\" FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" WHERE T1.\"XCL_037\" > 24 AND STRFTIME('%Y', T2.\"XCL_004\") < '1997' ORDER BY T1.\"XCL_036\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:188"
  ]
}
```

### Identifier from the 'disp' table (XCL_014) for records where the role is 'OWNER'. Represents the specific owner associated with an account.

```json
{
  "kind": "binding",
  "formula": "\"disp\".\"XCL_014\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_014\", T2.\"XCL_017\", T2.\"XCL_018\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN disp AS T3 ON T1.\"XCL_001\" = T3.\"XCL_015\" WHERE T3.\"XCL_016\" = 'OWNER'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_014\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      },
      {
        "role": "r2",
        "physical_table": "disp"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_014\" AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" INNER JOIN disp AS \"r2\" ON \"r0\".\"XCL_001\" = \"r2\".\"XCL_015\" WHERE \"r2\".\"XCL_016\" = 'OWNER'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:193"
  ]
}
```

### "loan"."XCL_035" = '1994-08-25'

```json
{
  "kind": "predicate",
  "formula": "\"loan\".\"XCL_035\" = '1994-08-25'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_002\" FROM account AS T1 INNER JOIN loan AS T2 ON T1.\"XCL_001\" = T2.\"XCL_034\" WHERE T2.\"XCL_035\" = '1994-08-25'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:105"
  ]
}
```

### STRFTIME('%Y', "trans"."XCL_048") > '1995' AND "trans"."XCL_050" = 'VYBER KARTOU'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"trans\".\"XCL_048\") > '1995' AND \"trans\".\"XCL_050\" = 'VYBER KARTOU'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_047\") FROM trans WHERE STRFTIME('%Y', \"XCL_048\") > '1995' AND \"XCL_050\" = 'VYBER KARTOU'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:170"
  ]
}
```

### East vs North Bohemia XCL_032 Difference

```json
{
  "kind": "metric",
  "formula": "SUM(IIF(\"district\".\"XCL_019\" = 'east Bohemia', \"district\".\"XCL_032\", 0)) - SUM(IIF(\"district\".\"XCL_019\" = 'north Bohemia', \"district\".\"XCL_032\", 0))",
  "grain": [],
  "population_scope": "SELECT SUM(IIF(\"XCL_019\" = 'east Bohemia', \"XCL_032\", 0)) - SUM(IIF(\"XCL_019\" = 'north Bohemia', \"XCL_032\", 0)) FROM district",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(IIF(\"r0\".\"XCL_019\" = 'east Bohemia', \"r0\".\"XCL_032\", 0)) - SUM(IIF(\"r0\".\"XCL_019\" = 'north Bohemia', \"r0\".\"XCL_032\", 0))",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "district"
      }
    ],
    "scope_sql": "SELECT SUM(IIF(\"r0\".\"XCL_019\" = 'east Bohemia', \"r0\".\"XCL_032\", 0)) - SUM(IIF(\"r0\".\"XCL_019\" = 'north Bohemia', \"r0\".\"XCL_032\", 0)) AS \"value\" FROM district AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:171"
  ]
}
```

### Counts the number of unique district identifiers (XCL_017) associated with clients. The population is restricted to clients with status 'F' (XCL_010) 

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"district\".\"XCL_017\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T2.\"XCL_017\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'F' AND T2.\"XCL_027\" BETWEEN 6000 AND 10000",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r1\".\"XCL_017\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "district"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r1\".\"XCL_017\") AS \"value\" FROM client AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_012\" = \"r1\".\"XCL_017\" WHERE \"r0\".\"XCL_010\" = 'F' AND \"r1\".\"XCL_027\" BETWEEN 6000 AND 10000",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:92"
  ]
}
```

### "district"."XCL_027" > 10000

```json
{
  "kind": "predicate",
  "formula": "\"district\".\"XCL_027\" > 10000",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(T2.\"XCL_010\" = 'F') AS REAL) * 100 / COUNT(T2.\"XCL_009\") FROM district AS T1 INNER JOIN client AS T2 ON T1.\"XCL_017\" = T2.\"XCL_012\" WHERE T1.\"XCL_027\" > 10000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:168"
  ]
}
```

### Account Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"account\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_001\") FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE STRFTIME('%Y', T2.\"XCL_004\") = '1996' AND T1.\"XCL_018\" = 'Litomerice'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "district"
      },
      {
        "role": "r1",
        "physical_table": "account"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_001\") AS \"value\" FROM district AS \"r0\" INNER JOIN account AS \"r1\" ON \"r0\".\"XCL_017\" = \"r1\".\"XCL_002\" WHERE STRFTIME('%Y', \"r1\".\"XCL_004\") = '1996' AND \"r0\".\"XCL_018\" = 'Litomerice'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:111"
  ]
}
```

### Aggregates the count of account identifiers (XCL_001) from the account table. The population is restricted to accounts that have at least one associat

```json
{
  "kind": "metric",
  "formula": "COUNT(\"account\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM account AS T1 INNER JOIN loan AS T2 ON T1.\"XCL_001\" = T2.\"XCL_034\" INNER JOIN district AS T3 ON T1.\"XCL_002\" = T3.\"XCL_017\" WHERE T3.\"XCL_019\" = 'Prague'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "loan"
      },
      {
        "role": "r2",
        "physical_table": "district"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM account AS \"r0\" INNER JOIN loan AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_034\" INNER JOIN district AS \"r2\" ON \"r0\".\"XCL_002\" = \"r2\".\"XCL_017\" WHERE \"r2\".\"XCL_019\" = 'Prague'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:90"
  ]
}
```

### "loan"."XCL_035" BETWEEN '1995-01-01' AND '1997-12-31' AND "account"."XCL_003" = 'POPLATEK MESICNE' AND "loan"."XCL_036" >= 250000

```json
{
  "kind": "predicate",
  "formula": "\"loan\".\"XCL_035\" BETWEEN '1995-01-01' AND '1997-12-31' AND \"account\".\"XCL_003\" = 'POPLATEK MESICNE' AND \"loan\".\"XCL_036\" >= 250000",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM account AS T1 INNER JOIN loan AS T2 ON T1.\"XCL_001\" = T2.\"XCL_034\" WHERE T2.\"XCL_035\" BETWEEN '1995-01-01' AND '1997-12-31' AND T1.\"XCL_003\" = 'POPLATEK MESICNE' AND T2.\"XCL_036\" >= 250000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:136"
  ]
}
```

### "client"."XCL_009" = 9

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_009\" = 9",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_007\" FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN card AS T3 ON T2.\"XCL_013\" = T3.\"XCL_006\" WHERE T1.\"XCL_009\" = 9",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:178"
  ]
}
```

### First 1995 Transaction Identifier

```json
{
  "kind": "binding",
  "formula": "\"trans\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_047\" FROM trans WHERE STRFTIME('%Y', \"XCL_048\") = '1995' ORDER BY \"XCL_048\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:101"
  ]
}
```

### Account Identifier

```json
{
  "kind": "binding",
  "formula": "\"account\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_001\" FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" INNER JOIN account AS T3 ON T2.\"XCL_017\" = T3.\"XCL_002\" INNER JOIN disp AS T4 ON T1.\"XCL_009\" = T4.\"XCL_014\" AND T4.\"XCL_015\" = T3.\"XCL_001\" WHERE T1.\"XCL_010\" = 'F' ORDER BY T1.\"XCL_011\" ASC, T2.\"XCL_027\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:189"
  ]
}
```

### Loan Identifier

```json
{
  "kind": "binding",
  "formula": "\"loan\".\"XCL_034\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_034\" FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" WHERE T1.\"XCL_037\" > 24 AND STRFTIME('%Y', T2.\"XCL_004\") < '1997' ORDER BY T1.\"XCL_036\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:188"
  ]
}
```

### Calculates the percentage change in the sum of loan amounts (XCL_036) between 1997 and 1996. The formula is ((Sum_1997 - Sum_1996) / Sum_1996) * 100. 

```json
{
  "kind": "metric",
  "formula": "CAST((SUM(CASE WHEN STRFTIME('%Y', \"loan\".\"XCL_035\") = '1997' THEN \"loan\".\"XCL_036\" ELSE 0 END) - SUM(CASE WHEN STRFTIME('%Y', \"loan\".\"XCL_035\") = '1996' THEN \"loan\".\"XCL_036\" ELSE 0 END)) AS REAL) * 100 / SUM(CASE WHEN STRFTIME('%Y', \"loan\".\"XCL_035\") = '1996' THEN \"loan\".\"XCL_036\" ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT CAST((SUM(CASE WHEN STRFTIME('%Y', T1.\"XCL_035\") = '1997' THEN T1.\"XCL_036\" ELSE 0 END) - SUM(CASE WHEN STRFTIME('%Y', T1.\"XCL_035\") = '1996' THEN T1.\"XCL_036\" ELSE 0 END)) AS REAL) * 100 / SUM(CASE WHEN STRFTIME('%Y', T1.\"XCL_035\") = '1996' THEN T1.\"XCL_036\" ELSE 0 END) FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" INNER JOIN disp AS T3 ON T3.\"XCL_015\" = T2.\"XCL_001\" INNER JOIN client AS T4 ON T4.\"XCL_009\" = T3.\"XCL_014\" WHERE T4.\"XCL_010\" = 'M' AND T3.\"XCL_016\" = 'OWNER'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST((SUM(CASE WHEN STRFTIME('%Y', \"r0\".\"XCL_035\") = '1997' THEN \"r0\".\"XCL_036\" ELSE 0 END) - SUM(CASE WHEN STRFTIME('%Y', \"r0\".\"XCL_035\") = '1996' THEN \"r0\".\"XCL_036\" ELSE 0 END)) AS REAL) * 100 / SUM(CASE WHEN STRFTIME('%Y', \"r0\".\"XCL_035\") = '1996' THEN \"r0\".\"XCL_036\" ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "loan"
      },
      {
        "role": "r1",
        "physical_table": "account"
      },
      {
        "role": "r2",
        "physical_table": "disp"
      },
      {
        "role": "r3",
        "physical_table": "client"
      }
    ],
    "scope_sql": "SELECT CAST((SUM(CASE WHEN STRFTIME('%Y', \"r0\".\"XCL_035\") = '1997' THEN \"r0\".\"XCL_036\" ELSE 0 END) - SUM(CASE WHEN STRFTIME('%Y', \"r0\".\"XCL_035\") = '1996' THEN \"r0\".\"XCL_036\" ELSE 0 END)) AS REAL) * 100 / SUM(CASE WHEN STRFTIME('%Y', \"r0\".\"XCL_035\") = '1996' THEN \"r0\".\"XCL_036\" ELSE 0 END) AS \"value\" FROM loan AS \"r0\" INNER JOIN account AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_001\" INNER JOIN disp AS \"r2\" ON \"r2\".\"XCL_015\" = \"r1\".\"XCL_001\" INNER JOIN client AS \"r3\" ON \"r3\".\"XCL_009\" = \"r2\".\"XCL_014\" WHERE \"r3\".\"XCL_010\" = 'M' AND \"r2\".\"XCL_016\" = 'OWNER'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:169"
  ]
}
```

### Aggregated sum of the 'XCL_051' column from the 'trans' table. The population is restricted to transactions occurring in the year 1998 (derived from '

```json
{
  "kind": "metric",
  "formula": "SUM(\"trans\".\"XCL_051\")",
  "grain": [],
  "population_scope": "SELECT SUM(T3.\"XCL_051\") FROM client AS T1 INNER JOIN disp AS T4 ON T1.\"XCL_009\" = T4.\"XCL_014\" INNER JOIN account AS T2 ON T4.\"XCL_015\" = T2.\"XCL_001\" INNER JOIN trans AS T3 ON T2.\"XCL_001\" = T3.\"XCL_047\" WHERE STRFTIME('%Y', T3.\"XCL_048\") = '1998' AND T1.\"XCL_009\" = 617",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r3\".\"XCL_051\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "disp"
      },
      {
        "role": "r2",
        "physical_table": "account"
      },
      {
        "role": "r3",
        "physical_table": "trans"
      }
    ],
    "scope_sql": "SELECT SUM(\"r3\".\"XCL_051\") AS \"value\" FROM client AS \"r0\" INNER JOIN disp AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_014\" INNER JOIN account AS \"r2\" ON \"r1\".\"XCL_015\" = \"r2\".\"XCL_001\" INNER JOIN trans AS \"r3\" ON \"r2\".\"XCL_001\" = \"r3\".\"XCL_047\" WHERE STRFTIME('%Y', \"r3\".\"XCL_048\") = '1998' AND \"r0\".\"XCL_009\" = 617",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:179"
  ]
}
```

### STRFTIME('%Y', "trans"."XCL_048") = '1998'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"trans\".\"XCL_048\") = '1998'",
  "grain": [],
  "population_scope": "SELECT AVG(\"XCL_051\") FROM trans WHERE STRFTIME('%Y', \"XCL_048\") = '1998'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:145"
  ]
}
```

### Calculates the percentage of loan records where the field XCL_039 equals 'C' relative to the total count of records in the filtered population. The po

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"loan\".\"XCL_039\" = 'C') AS REAL) * 100 / COUNT(\"loan\".\"XCL_034\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(\"XCL_039\" = 'C') AS REAL) * 100 / COUNT(\"XCL_034\") FROM loan WHERE \"XCL_036\" < 100000",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(\"r0\".\"XCL_039\" = 'C') AS REAL) * 100 / COUNT(\"r0\".\"XCL_034\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "loan"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(\"r0\".\"XCL_039\" = 'C') AS REAL) * 100 / COUNT(\"r0\".\"XCL_034\") AS \"value\" FROM loan AS \"r0\" WHERE \"r0\".\"XCL_036\" < 100000",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:118"
  ]
}
```

### Card Attribute XCL_007

```json
{
  "kind": "binding",
  "formula": "\"card\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_007\" FROM disp AS T1 INNER JOIN client AS T2 ON T1.\"XCL_014\" = T2.\"XCL_009\" INNER JOIN card AS T3 ON T1.\"XCL_013\" = T3.\"XCL_006\" WHERE T2.\"XCL_009\" = 13539",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_007\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "disp"
      },
      {
        "role": "r1",
        "physical_table": "client"
      },
      {
        "role": "r2",
        "physical_table": "card"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_007\" AS \"value\" FROM disp AS \"r0\" INNER JOIN client AS \"r1\" ON \"r0\".\"XCL_014\" = \"r1\".\"XCL_009\" INNER JOIN card AS \"r2\" ON \"r0\".\"XCL_013\" = \"r2\".\"XCL_006\" WHERE \"r1\".\"XCL_009\" = 13539",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:161"
  ]
}
```

### Aggregates the number of loan records (identified by XCL_034) that are associated with accounts having a weekly fee type (XCL_003 = 'POPLATEK TYDNE') 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"loan\".\"XCL_034\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_034\") FROM account AS T1 INNER JOIN loan AS T2 ON T1.\"XCL_001\" = T2.\"XCL_034\" WHERE T2.\"XCL_037\" = 24 AND T1.\"XCL_003\" = 'POPLATEK TYDNE'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_034\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "loan"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_034\") AS \"value\" FROM account AS \"r0\" INNER JOIN loan AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_034\" WHERE \"r1\".\"XCL_037\" = 24 AND \"r0\".\"XCL_003\" = 'POPLATEK TYDNE'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:191"
  ]
}
```

### "order"."XCL_040" = 33333

```json
{
  "kind": "predicate",
  "formula": "\"order\".\"XCL_040\" = 33333",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_017\" FROM \"order\" AS T1 INNER JOIN account AS T2 ON T1.\"XCL_041\" = T2.\"XCL_001\" INNER JOIN district AS T3 ON T2.\"XCL_002\" = T3.\"XCL_017\" WHERE T1.\"XCL_040\" = 33333",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:158"
  ]
}
```

### Aggregates the count of client records (XCL_009) where the client is female (XCL_010 = 'F'), born before 1950 (STRFTIME('%Y', XCL_011) < '1950'), and 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"client\".\"XCL_009\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_009\") FROM district AS T1 INNER JOIN client AS T2 ON T1.\"XCL_017\" = T2.\"XCL_012\" WHERE T2.\"XCL_010\" = 'F' AND STRFTIME('%Y', T2.\"XCL_011\") < '1950' AND T1.\"XCL_018\" = 'Sokolov'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_009\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "district"
      },
      {
        "role": "r1",
        "physical_table": "client"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_009\") AS \"value\" FROM district AS \"r0\" INNER JOIN client AS \"r1\" ON \"r0\".\"XCL_017\" = \"r1\".\"XCL_012\" WHERE \"r1\".\"XCL_010\" = 'F' AND STRFTIME('%Y', \"r1\".\"XCL_011\") < '1950' AND \"r0\".\"XCL_018\" = 'Sokolov'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:100"
  ]
}
```

### Returns the value of column XCL_046 from the trans table. The population is restricted to transactions linked to accounts in district 5. The grain is 

```json
{
  "kind": "binding",
  "formula": "\"trans\".\"XCL_046\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_046\" FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN trans AS T3 ON T2.\"XCL_001\" = T3.\"XCL_047\" WHERE T1.\"XCL_017\" = 5",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_046\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "district"
      },
      {
        "role": "r1",
        "physical_table": "account"
      },
      {
        "role": "r2",
        "physical_table": "trans"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_046\" AS \"value\" FROM district AS \"r0\" INNER JOIN account AS \"r1\" ON \"r0\".\"XCL_017\" = \"r1\".\"XCL_002\" INNER JOIN trans AS \"r2\" ON \"r1\".\"XCL_001\" = \"r2\".\"XCL_047\" WHERE \"r0\".\"XCL_017\" = 5",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:165"
  ]
}
```

### "district"."XCL_018" = 'Prachatice'

```json
{
  "kind": "predicate",
  "formula": "\"district\".\"XCL_018\" = 'Prachatice'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T1.\"XCL_004\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE T2.\"XCL_018\" = 'Prachatice'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:121"
  ]
}
```

### A single-value metric that returns '1996' if the average of XCL_029 across all districts is greater than the average of XCL_028, otherwise '1995'. The

```json
{
  "kind": "metric",
  "formula": "IIF(AVG(\"district\".\"XCL_029\") > AVG(\"district\".\"XCL_028\"), '1996', '1995')",
  "grain": [],
  "population_scope": "SELECT DISTINCT IIF(AVG(\"XCL_029\") > AVG(\"XCL_028\"), '1996', '1995') FROM district",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:91"
  ]
}
```

### "client"."XCL_009" = 3356 AND "trans"."XCL_050" = 'VYBER'

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_009\" = 3356 AND \"trans\".\"XCL_050\" = 'VYBER'",
  "grain": [],
  "population_scope": "SELECT T4.\"XCL_046\" FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN account AS T3 ON T2.\"XCL_015\" = T3.\"XCL_001\" INNER JOIN trans AS T4 ON T3.\"XCL_001\" = T4.\"XCL_047\" WHERE T1.\"XCL_009\" = 3356 AND T4.\"XCL_050\" = 'VYBER'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:159"
  ]
}
```

### Average Card Withdrawal Amount

```json
{
  "kind": "metric",
  "formula": "AVG(\"trans\".\"XCL_051\")",
  "grain": [],
  "population_scope": "SELECT AVG(T4.\"XCL_051\") FROM card AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_006\" = T2.\"XCL_013\" INNER JOIN account AS T3 ON T2.\"XCL_015\" = T3.\"XCL_001\" INNER JOIN trans AS T4 ON T3.\"XCL_001\" = T4.\"XCL_047\" WHERE STRFTIME('%Y', T4.\"XCL_048\") = '1998' AND T4.\"XCL_050\" = 'VYBER KARTOU'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r3\".\"XCL_051\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "card"
      },
      {
        "role": "r1",
        "physical_table": "disp"
      },
      {
        "role": "r2",
        "physical_table": "account"
      },
      {
        "role": "r3",
        "physical_table": "trans"
      }
    ],
    "scope_sql": "SELECT AVG(\"r3\".\"XCL_051\") AS \"value\" FROM card AS \"r0\" INNER JOIN disp AS \"r1\" ON \"r0\".\"XCL_006\" = \"r1\".\"XCL_013\" INNER JOIN account AS \"r2\" ON \"r1\".\"XCL_015\" = \"r2\".\"XCL_001\" INNER JOIN trans AS \"r3\" ON \"r2\".\"XCL_001\" = \"r3\".\"XCL_047\" WHERE STRFTIME('%Y', \"r3\".\"XCL_048\") = '1998' AND \"r3\".\"XCL_050\" = 'VYBER KARTOU'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:144"
  ]
}
```

### STRFTIME('%Y', "trans"."XCL_048") = '1997'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"trans\".\"XCL_048\") = '1997'",
  "grain": [
    "\"account\".\"XCL_002\""
  ],
  "population_scope": "SELECT T1.\"XCL_002\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN trans AS T3 ON T1.\"XCL_001\" = T3.\"XCL_047\" WHERE STRFTIME('%Y', T3.\"XCL_048\") = '1997' GROUP BY T1.\"XCL_002\" HAVING SUM(T3.\"XCL_051\") > 10000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:141"
  ]
}
```

### District Attribute XCL_019

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_018\", T2.\"XCL_019\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN loan AS T3 ON T1.\"XCL_001\" = T3.\"XCL_034\" WHERE T3.\"XCL_033\" = 4990",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_019\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      },
      {
        "role": "r2",
        "physical_table": "loan"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_019\" AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" INNER JOIN loan AS \"r2\" ON \"r0\".\"XCL_001\" = \"r2\".\"XCL_034\" WHERE \"r2\".\"XCL_033\" = 4990",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:122"
  ]
}
```

### Calculates the percentage of the total sum of column XCL_036 that corresponds to rows where column XCL_039 equals 'A'. The metric aggregates the entir

```json
{
  "kind": "metric",
  "formula": "(CAST(SUM(CASE WHEN \"loan\".\"XCL_039\" = 'A' THEN \"loan\".\"XCL_036\" ELSE 0 END) AS REAL) * 100) / SUM(\"loan\".\"XCL_036\")",
  "grain": [],
  "population_scope": "SELECT (CAST(SUM(CASE WHEN \"XCL_039\" = 'A' THEN \"XCL_036\" ELSE 0 END) AS REAL) * 100) / SUM(\"XCL_036\") FROM loan",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "(CAST(SUM(CASE WHEN \"r0\".\"XCL_039\" = 'A' THEN \"r0\".\"XCL_036\" ELSE 0 END) AS REAL) * 100) / SUM(\"r0\".\"XCL_036\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "loan"
      }
    ],
    "scope_sql": "SELECT (CAST(SUM(CASE WHEN \"r0\".\"XCL_039\" = 'A' THEN \"r0\".\"XCL_036\" ELSE 0 END) AS REAL) * 100) / SUM(\"r0\".\"XCL_036\") AS \"value\" FROM loan AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:117"
  ]
}
```

### The district identifier (XCL_019) for the single district with the highest total loan amount (XCL_036) among loans with status 'C' or 'D'. The grain i

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_019\"",
  "grain": [
    "\"district\".\"XCL_019\""
  ],
  "population_scope": "SELECT T2.\"XCL_019\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN loan AS T3 ON T1.\"XCL_001\" = T3.\"XCL_034\" WHERE T3.\"XCL_039\" IN ('C', 'D') GROUP BY T2.\"XCL_019\" ORDER BY SUM(T3.\"XCL_036\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:131"
  ]
}
```

### The value of column XCL_051 from the trans table. It represents a specific transaction record linked to an account and loan, selected as the single to

```json
{
  "kind": "binding",
  "formula": "\"trans\".\"XCL_051\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_051\" FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" INNER JOIN trans AS T3 ON T2.\"XCL_001\" = T3.\"XCL_047\" ORDER BY T1.\"XCL_036\" DESC, T3.\"XCL_048\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:108"
  ]
}
```

### Account Identifier

```json
{
  "kind": "binding",
  "formula": "\"account\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM account WHERE \"XCL_003\" = 'POPLATEK MESICNE'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM account AS \"r0\" WHERE \"r0\".\"XCL_003\" = 'POPLATEK MESICNE'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:127"
  ]
}
```

### "card"."XCL_007" = 'gold'

```json
{
  "kind": "predicate",
  "formula": "\"card\".\"XCL_007\" = 'gold'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_015\" FROM disp AS T2 INNER JOIN card AS T1 ON T1.\"XCL_006\" = T2.\"XCL_013\" WHERE T1.\"XCL_007\" = 'gold'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:143"
  ]
}
```

### "loan"."XCL_036" > 300000

```json
{
  "kind": "predicate",
  "formula": "\"loan\".\"XCL_036\" > 300000",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T2.\"XCL_018\", T2.\"XCL_019\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN loan AS T3 ON T1.\"XCL_001\" = T3.\"XCL_034\" WHERE T3.\"XCL_036\" > 300000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:123"
  ]
}
```

### Calculates the percentage of clients identified as male ('M') within a specific district. The numerator counts clients where XCL_010 equals 'M', and t

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"client\".\"XCL_010\" = 'M') AS REAL) * 100 / COUNT(\"client\".\"XCL_009\")",
  "grain": [
    "\"district\".\"XCL_020\""
  ],
  "population_scope": "SELECT CAST(SUM(T1.\"XCL_010\" = 'M') AS REAL) * 100 / COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T2.\"XCL_019\" = 'south Bohemia' GROUP BY T2.\"XCL_020\" ORDER BY T2.\"XCL_020\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:115"
  ]
}
```

### "trans"."XCL_052" < 0 AND "trans"."XCL_050" = 'VYBER KARTOU' AND "account"."XCL_003" = 'POPLATEK MESICNE'

```json
{
  "kind": "predicate",
  "formula": "\"trans\".\"XCL_052\" < 0 AND \"trans\".\"XCL_050\" = 'VYBER KARTOU' AND \"account\".\"XCL_003\" = 'POPLATEK MESICNE'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_047\") FROM trans AS T1 INNER JOIN account AS T2 ON T1.\"XCL_047\" = T2.\"XCL_001\" WHERE T1.\"XCL_052\" < 0 AND T1.\"XCL_050\" = 'VYBER KARTOU' AND T2.\"XCL_003\" = 'POPLATEK MESICNE'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:135"
  ]
}
```

### "district"."XCL_019" = 'Prague'

```json
{
  "kind": "predicate",
  "formula": "\"district\".\"XCL_019\" = 'Prague'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM account AS T1 INNER JOIN loan AS T2 ON T1.\"XCL_001\" = T2.\"XCL_034\" INNER JOIN district AS T3 ON T1.\"XCL_002\" = T3.\"XCL_017\" WHERE T3.\"XCL_019\" = 'Prague'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:90"
  ]
}
```

### "district"."XCL_019" = 'east Bohemia' AND STRFTIME('%Y', "account"."XCL_004") BETWEEN '1995' AND '2000'

```json
{
  "kind": "predicate",
  "formula": "\"district\".\"XCL_019\" = 'east Bohemia' AND STRFTIME('%Y', \"account\".\"XCL_004\") BETWEEN '1995' AND '2000'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T1.\"XCL_003\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE T2.\"XCL_019\" = 'east Bohemia' AND STRFTIME('%Y', T1.\"XCL_004\") BETWEEN '1995' AND '2000'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:120"
  ]
}
```

### District Identifier

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_017\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_014\", T2.\"XCL_017\", T2.\"XCL_018\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN disp AS T3 ON T1.\"XCL_001\" = T3.\"XCL_015\" WHERE T3.\"XCL_016\" = 'OWNER'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_017\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      },
      {
        "role": "r2",
        "physical_table": "disp"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_017\" AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" INNER JOIN disp AS \"r2\" ON \"r0\".\"XCL_001\" = \"r2\".\"XCL_015\" WHERE \"r2\".\"XCL_016\" = 'OWNER'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:193"
  ]
}
```

### Aggregates the count of client records (XCL_009) where the client gender (XCL_010) is 'F' and the associated district (XCL_018) is 'Jesenik'. The grai

```json
{
  "kind": "metric",
  "formula": "COUNT(\"client\".\"XCL_009\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'F' AND T2.\"XCL_018\" = 'Jesenik'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_009\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "district"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_009\") AS \"value\" FROM client AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_012\" = \"r1\".\"XCL_017\" WHERE \"r0\".\"XCL_010\" = 'F' AND \"r1\".\"XCL_018\" = 'Jesenik'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:109"
  ]
}
```

### "client"."XCL_010" = 'F' AND "district"."XCL_019" = 'south Bohemia'

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_010\" = 'F' AND \"district\".\"XCL_019\" = 'south Bohemia'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'F' AND T2.\"XCL_019\" = 'south Bohemia'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:147"
  ]
}
```

### Client Identifier

```json
{
  "kind": "binding",
  "formula": "\"client\".\"XCL_009\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_009\" FROM \"order\" AS T1 INNER JOIN account AS T2 ON T1.\"XCL_041\" = T2.\"XCL_001\" INNER JOIN disp AS T4 ON T4.\"XCL_015\" = T2.\"XCL_001\" INNER JOIN client AS T3 ON T4.\"XCL_014\" = T3.\"XCL_009\" WHERE T1.\"XCL_040\" = 32423",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r3\".\"XCL_009\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "order"
      },
      {
        "role": "r1",
        "physical_table": "account"
      },
      {
        "role": "r2",
        "physical_table": "disp"
      },
      {
        "role": "r3",
        "physical_table": "client"
      }
    ],
    "scope_sql": "SELECT \"r3\".\"XCL_009\" AS \"value\" FROM \"order\" AS \"r0\" INNER JOIN account AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_001\" INNER JOIN disp AS \"r2\" ON \"r2\".\"XCL_015\" = \"r1\".\"XCL_001\" INNER JOIN client AS \"r3\" ON \"r2\".\"XCL_014\" = \"r3\".\"XCL_009\" WHERE \"r0\".\"XCL_040\" = 32423",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:164"
  ]
}
```

### Calculates the percentage of clients in the 'Prague' district where the column XCL_010 has the value 'F'. The numerator counts rows where XCL_010 = 'F

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"client\".\"XCL_010\" = 'F') AS REAL) / COUNT(\"client\".\"XCL_009\") * 100",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(T2.\"XCL_010\" = 'F') AS REAL) / COUNT(T2.\"XCL_009\") * 100 FROM district AS T1 INNER JOIN client AS T2 ON T1.\"XCL_017\" = T2.\"XCL_012\" WHERE T1.\"XCL_019\" = 'Prague'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(\"r1\".\"XCL_010\" = 'F') AS REAL) / COUNT(\"r1\".\"XCL_009\") * 100",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "district"
      },
      {
        "role": "r1",
        "physical_table": "client"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(\"r1\".\"XCL_010\" = 'F') AS REAL) / COUNT(\"r1\".\"XCL_009\") * 100 AS \"value\" FROM district AS \"r0\" INNER JOIN client AS \"r1\" ON \"r0\".\"XCL_017\" = \"r1\".\"XCL_012\" WHERE \"r0\".\"XCL_019\" = 'Prague'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:185"
  ]
}
```

### "district"."XCL_018" = 'Pisek'

```json
{
  "kind": "predicate",
  "formula": "\"district\".\"XCL_018\" = 'Pisek'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE T2.\"XCL_018\" = 'Pisek'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:140"
  ]
}
```

### District Name

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_018\"",
  "grain": [
    "\"district\".\"XCL_017\"",
    "\"district\".\"XCL_018\""
  ],
  "population_scope": "SELECT T2.\"XCL_018\", COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'F' GROUP BY T2.\"XCL_017\", T2.\"XCL_018\" ORDER BY COUNT(T1.\"XCL_009\") DESC LIMIT 9",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:128"
  ]
}
```

### SUM("trans"."XCL_051") > 10000

```json
{
  "kind": "predicate",
  "formula": "SUM(\"trans\".\"XCL_051\") > 10000",
  "grain": [
    "\"account\".\"XCL_002\""
  ],
  "population_scope": "SELECT T1.\"XCL_002\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN trans AS T3 ON T1.\"XCL_001\" = T3.\"XCL_047\" WHERE STRFTIME('%Y', T3.\"XCL_048\") = '1997' GROUP BY T1.\"XCL_002\" HAVING SUM(T3.\"XCL_051\") > 10000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:141"
  ]
}
```

### "client"."XCL_010" = 'F' AND "district"."XCL_027" BETWEEN 6000 AND 10000

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_010\" = 'F' AND \"district\".\"XCL_027\" BETWEEN 6000 AND 10000",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T2.\"XCL_017\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'F' AND T2.\"XCL_027\" BETWEEN 6000 AND 10000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:92"
  ]
}
```

### Non-owner account disposition type

```json
{
  "kind": "binding",
  "formula": "\"disp\".\"XCL_016\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_016\" FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN disp AS T3 ON T2.\"XCL_001\" = T3.\"XCL_015\" WHERE T3.\"XCL_016\" <> 'OWNER' AND T1.\"XCL_027\" BETWEEN 8000 AND 9000",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_016\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "district"
      },
      {
        "role": "r1",
        "physical_table": "account"
      },
      {
        "role": "r2",
        "physical_table": "disp"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_016\" AS \"value\" FROM district AS \"r0\" INNER JOIN account AS \"r1\" ON \"r0\".\"XCL_017\" = \"r1\".\"XCL_002\" INNER JOIN disp AS \"r2\" ON \"r1\".\"XCL_001\" = \"r2\".\"XCL_015\" WHERE \"r2\".\"XCL_016\" <> 'OWNER' AND \"r0\".\"XCL_027\" BETWEEN 8000 AND 9000",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:149"
  ]
}
```

### The value of column XCL_015 from the disp table, restricted to rows where the associated card (joined via XCL_013 = XCL_006) has XCL_007 equal to 'gol

```json
{
  "kind": "binding",
  "formula": "\"disp\".\"XCL_015\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_015\" FROM disp AS T2 INNER JOIN card AS T1 ON T1.\"XCL_006\" = T2.\"XCL_013\" WHERE T1.\"XCL_007\" = 'gold'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_015\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "disp"
      },
      {
        "role": "r1",
        "physical_table": "card"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_015\" AS \"value\" FROM disp AS \"r0\" INNER JOIN card AS \"r1\" ON \"r1\".\"XCL_006\" = \"r0\".\"XCL_013\" WHERE \"r1\".\"XCL_007\" = 'gold'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:143"
  ]
}
```

### Aggregates the count of card records (XCL_005) that are associated with a 'gold' card type (XCL_007) and where the associated client holds an 'OWNER' 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"card\".\"XCL_005\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_005\") FROM card AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_006\" = T2.\"XCL_013\" WHERE T1.\"XCL_007\" = 'gold' AND T2.\"XCL_016\" = 'OWNER'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_005\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "card"
      },
      {
        "role": "r1",
        "physical_table": "disp"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_005\") AS \"value\" FROM card AS \"r0\" INNER JOIN disp AS \"r1\" ON \"r0\".\"XCL_006\" = \"r1\".\"XCL_013\" WHERE \"r0\".\"XCL_007\" = 'gold' AND \"r1\".\"XCL_016\" = 'OWNER'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:139"
  ]
}
```

### "disp"."XCL_015" BETWEEN 1 AND 10

```json
{
  "kind": "predicate",
  "formula": "\"disp\".\"XCL_015\" BETWEEN 1 AND 10",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_016\" = 'OWNER'), SUM(\"XCL_016\" = 'DISPONENT') FROM disp WHERE \"XCL_015\" BETWEEN 1 AND 10",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:172"
  ]
}
```

### Loan Status or Type

```json
{
  "kind": "binding",
  "formula": "\"loan\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T4.\"XCL_036\", T4.\"XCL_039\" FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN account AS T3 ON T2.\"XCL_015\" = T3.\"XCL_001\" INNER JOIN loan AS T4 ON T3.\"XCL_001\" = T4.\"XCL_034\" WHERE T1.\"XCL_009\" = 992",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r3\".\"XCL_039\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "disp"
      },
      {
        "role": "r2",
        "physical_table": "account"
      },
      {
        "role": "r3",
        "physical_table": "loan"
      }
    ],
    "scope_sql": "SELECT \"r3\".\"XCL_039\" AS \"value\" FROM client AS \"r0\" INNER JOIN disp AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_014\" INNER JOIN account AS \"r2\" ON \"r1\".\"XCL_015\" = \"r2\".\"XCL_001\" INNER JOIN loan AS \"r3\" ON \"r2\".\"XCL_001\" = \"r3\".\"XCL_034\" WHERE \"r0\".\"XCL_009\" = 992",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:176"
  ]
}
```

### "trans"."XCL_053" = 'SIPO' AND "district"."XCL_018" = 'Pisek'

```json
{
  "kind": "predicate",
  "formula": "\"trans\".\"XCL_053\" = 'SIPO' AND \"district\".\"XCL_018\" = 'Pisek'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_001\" FROM trans AS T1 INNER JOIN account AS T2 ON T1.\"XCL_047\" = T2.\"XCL_001\" INNER JOIN district AS T3 ON T2.\"XCL_002\" = T3.\"XCL_017\" WHERE T1.\"XCL_053\" = 'SIPO' AND T3.\"XCL_018\" = 'Pisek'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:142"
  ]
}
```

### Average Loan XCL_036

```json
{
  "kind": "metric",
  "formula": "AVG(\"loan\".\"XCL_036\")",
  "grain": [],
  "population_scope": "SELECT AVG(T2.\"XCL_036\") FROM account AS T1 INNER JOIN loan AS T2 ON T1.\"XCL_001\" = T2.\"XCL_034\" WHERE T2.\"XCL_039\" IN ('C', 'D') AND T1.\"XCL_003\" = 'POPLATEK PO OBRATU'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r1\".\"XCL_036\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "loan"
      }
    ],
    "scope_sql": "SELECT AVG(\"r1\".\"XCL_036\") AS \"value\" FROM account AS \"r0\" INNER JOIN loan AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_034\" WHERE \"r1\".\"XCL_039\" IN ('C', 'D') AND \"r0\".\"XCL_003\" = 'POPLATEK PO OBRATU'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:192"
  ]
}
```

### The value of column XCL_014 from the disp table, returned for rows where the associated card (joined via XCL_006 = XCL_013) has XCL_007 equal to 'juni

```json
{
  "kind": "binding",
  "formula": "\"disp\".\"XCL_014\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_014\" FROM card AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_006\" = T2.\"XCL_013\" WHERE T1.\"XCL_007\" = 'junior' AND T1.\"XCL_008\" >= '1997-01-01'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_014\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "card"
      },
      {
        "role": "r1",
        "physical_table": "disp"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_014\" AS \"value\" FROM card AS \"r0\" INNER JOIN disp AS \"r1\" ON \"r0\".\"XCL_006\" = \"r1\".\"XCL_013\" WHERE \"r0\".\"XCL_007\" = 'junior' AND \"r0\".\"XCL_008\" >= '1997-01-01'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:167"
  ]
}
```

### A scalar subquery that identifies the second highest value of the 'XCL_031' column from the 'district' table. It is used as a filter condition to sele

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_031\" FROM district AS T3 ORDER BY T3.\"XCL_031\" DESC LIMIT 1 OFFSET 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:138"
  ]
}
```

### "disp"."XCL_016" = 'OWNER'

```json
{
  "kind": "predicate",
  "formula": "\"disp\".\"XCL_016\" = 'OWNER'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_014\" FROM disp AS T1 INNER JOIN account AS T3 ON T1.\"XCL_015\" = T3.\"XCL_001\" INNER JOIN loan AS T2 ON T3.\"XCL_001\" = T2.\"XCL_034\" WHERE T1.\"XCL_016\" = 'OWNER' ORDER BY T2.\"XCL_036\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:156"
  ]
}
```

### STRFTIME('%Y', "account"."XCL_004") = '1993'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"account\".\"XCL_004\") = '1993'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(T1.\"XCL_018\" = 'Decin') AS REAL) * 100 / COUNT(\"XCL_001\") FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE STRFTIME('%Y', T2.\"XCL_004\") = '1993'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:126"
  ]
}
```

### Aggregates the count of card records (XCL_005) where the card type is 'classic' and the associated customer role in the disp table is 'OWNER'. The gra

```json
{
  "kind": "metric",
  "formula": "COUNT(\"card\".\"XCL_005\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_005\") FROM card AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_006\" = T2.\"XCL_013\" WHERE T1.\"XCL_007\" = 'classic' AND T2.\"XCL_016\" = 'OWNER'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_005\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "card"
      },
      {
        "role": "r1",
        "physical_table": "disp"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_005\") AS \"value\" FROM card AS \"r0\" INNER JOIN disp AS \"r1\" ON \"r0\".\"XCL_006\" = \"r1\".\"XCL_013\" WHERE \"r0\".\"XCL_007\" = 'classic' AND \"r1\".\"XCL_016\" = 'OWNER'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:153"
  ]
}
```

### District Name

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_018\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T2.\"XCL_018\", T2.\"XCL_019\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE T1.\"XCL_003\" = 'POPLATEK PO OBRATU' AND STRFTIME('%Y', T1.\"XCL_004\") = '1993'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_018\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_018\" AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" WHERE \"r0\".\"XCL_003\" = 'POPLATEK PO OBRATU' AND STRFTIME('%Y', \"r0\".\"XCL_004\") = '1993'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:119"
  ]
}
```

### "account"."XCL_003" = 'POPLATEK PO OBRATU' AND "disp"."XCL_016" = 'DISPONENT'

```json
{
  "kind": "predicate",
  "formula": "\"account\".\"XCL_003\" = 'POPLATEK PO OBRATU' AND \"disp\".\"XCL_016\" = 'DISPONENT'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_014\" FROM account AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_001\" = T2.\"XCL_015\" WHERE T1.\"XCL_003\" = 'POPLATEK PO OBRATU' AND T2.\"XCL_016\" = 'DISPONENT'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:97"
  ]
}
```

### STRFTIME('%Y', "account"."XCL_004") = '1993' AND "loan"."XCL_037" > 12

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"account\".\"XCL_004\") = '1993' AND \"loan\".\"XCL_037\" > 12",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_034\" FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" WHERE STRFTIME('%Y', T2.\"XCL_004\") = '1993' AND T1.\"XCL_037\" > 12 ORDER BY T1.\"XCL_036\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:99"
  ]
}
```

### "account"."XCL_003" = 'POPLATEK MESICNE'

```json
{
  "kind": "predicate",
  "formula": "\"account\".\"XCL_003\" = 'POPLATEK MESICNE'",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM account WHERE \"XCL_003\" = 'POPLATEK MESICNE'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:127"
  ]
}
```

### "loan"."XCL_037" = 60

```json
{
  "kind": "predicate",
  "formula": "\"loan\".\"XCL_037\" = 60",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_033\", T2.\"XCL_018\", T2.\"XCL_027\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN loan AS T3 ON T1.\"XCL_001\" = T3.\"XCL_034\" WHERE T3.\"XCL_037\" = 60",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:124"
  ]
}
```

### "client"."XCL_010" = 'F'

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_010\" = 'F'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_001\" FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" INNER JOIN account AS T3 ON T2.\"XCL_017\" = T3.\"XCL_002\" INNER JOIN disp AS T4 ON T1.\"XCL_009\" = T4.\"XCL_014\" AND T4.\"XCL_015\" = T3.\"XCL_001\" WHERE T1.\"XCL_010\" = 'F' ORDER BY T1.\"XCL_011\" ASC, T2.\"XCL_027\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:189"
  ]
}
```

### District Name

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_018\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_014\", T2.\"XCL_017\", T2.\"XCL_018\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN disp AS T3 ON T1.\"XCL_001\" = T3.\"XCL_015\" WHERE T3.\"XCL_016\" = 'OWNER'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_018\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      },
      {
        "role": "r2",
        "physical_table": "disp"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_018\" AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" INNER JOIN disp AS \"r2\" ON \"r0\".\"XCL_001\" = \"r2\".\"XCL_015\" WHERE \"r2\".\"XCL_016\" = 'OWNER'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:193"
  ]
}
```

### Identifier from the 'order' table used to join with the 'account' table. In the subquery, it serves as a grouping dimension for aggregating order amou

```json
{
  "kind": "binding",
  "formula": "\"order\".\"XCL_041\"",
  "grain": [
    "\"order\".\"XCL_041\"",
    "\"order\".\"XCL_045\""
  ],
  "population_scope": "SELECT \"XCL_041\", \"XCL_045\", SUM(\"XCL_044\") AS total_amount FROM \"order\" GROUP BY \"XCL_041\", \"XCL_045\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_041\"",
    "grain": [
      "\"r0\".\"XCL_041\"",
      "\"r0\".\"XCL_045\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "order"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_041\" AS \"grain_0\", \"r0\".\"XCL_045\" AS \"grain_1\", \"r0\".\"XCL_041\" AS \"value\" FROM \"order\" AS \"r0\" GROUP BY \"r0\".\"XCL_041\", \"r0\".\"XCL_045\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:173"
  ]
}
```

### District Identifier

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_018\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_018\" FROM district AS T1 INNER JOIN client AS T2 ON T1.\"XCL_017\" = T2.\"XCL_012\" WHERE T2.\"XCL_011\" = '1976-01-29' AND T2.\"XCL_010\" = 'F'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_018\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "district"
      },
      {
        "role": "r1",
        "physical_table": "client"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_018\" AS \"value\" FROM district AS \"r0\" INNER JOIN client AS \"r1\" ON \"r0\".\"XCL_017\" = \"r1\".\"XCL_012\" WHERE \"r1\".\"XCL_011\" = '1976-01-29' AND \"r1\".\"XCL_010\" = 'F'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:112"
  ]
}
```

### "account"."XCL_001" = 3 AND SUM("order"."XCL_044") = 3539

```json
{
  "kind": "predicate",
  "formula": "\"account\".\"XCL_001\" = 3 AND SUM(\"order\".\"XCL_044\") = 3539",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\", T2.\"XCL_045\" FROM account AS T1 INNER JOIN (SELECT \"XCL_041\", \"XCL_045\", SUM(\"XCL_044\") AS total_amount FROM \"order\" GROUP BY \"XCL_041\", \"XCL_045\") AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_001\" = 3 AND T2.\"total_amount\" = 3539",
  "upstream_scopes": [
    "SELECT \"XCL_041\", \"XCL_045\", SUM(\"XCL_044\") AS total_amount FROM \"order\" GROUP BY \"XCL_041\", \"XCL_045\""
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:173"
  ]
}
```

### Client Birth Year

```json
{
  "kind": "binding",
  "formula": "STRFTIME('%Y', \"client\".\"XCL_011\")",
  "grain": [],
  "population_scope": "SELECT STRFTIME('%Y', T1.\"XCL_011\") FROM client AS T1 INNER JOIN disp AS T3 ON T1.\"XCL_009\" = T3.\"XCL_014\" INNER JOIN account AS T2 ON T3.\"XCL_015\" = T2.\"XCL_001\" WHERE T2.\"XCL_001\" = 130",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "STRFTIME('%Y', \"r0\".\"XCL_011\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "disp"
      },
      {
        "role": "r2",
        "physical_table": "account"
      }
    ],
    "scope_sql": "SELECT STRFTIME('%Y', \"r0\".\"XCL_011\") AS \"value\" FROM client AS \"r0\" INNER JOIN disp AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_014\" INNER JOIN account AS \"r2\" ON \"r1\".\"XCL_015\" = \"r2\".\"XCL_001\" WHERE \"r2\".\"XCL_001\" = 130",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:174"
  ]
}
```

### A district-level attribute (XCL_019) retrieved from the district table. It is joined to the account via the account's district reference (XCL_002) and

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T2.\"XCL_018\", T2.\"XCL_019\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN loan AS T3 ON T1.\"XCL_001\" = T3.\"XCL_034\" WHERE T3.\"XCL_036\" > 300000",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_019\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      },
      {
        "role": "r2",
        "physical_table": "loan"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_019\" AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" INNER JOIN loan AS \"r2\" ON \"r0\".\"XCL_001\" = \"r2\".\"XCL_034\" WHERE \"r2\".\"XCL_036\" > 300000",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:123"
  ]
}
```

### Account Identifier

```json
{
  "kind": "binding",
  "formula": "\"account\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T1.\"XCL_003\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE T2.\"XCL_019\" = 'east Bohemia' AND STRFTIME('%Y', T1.\"XCL_004\") BETWEEN '1995' AND '2000'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" WHERE \"r1\".\"XCL_019\" = 'east Bohemia' AND STRFTIME('%Y', \"r0\".\"XCL_004\") BETWEEN '1995' AND '2000'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:120"
  ]
}
```

### Aggregates the total number of account records (XCL_001) where the account type is 'POPLATEK PO OBRATU' and the associated disposition (disp) indicate

```json
{
  "kind": "metric",
  "formula": "COUNT(\"account\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM account AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_001\" = T2.\"XCL_015\" WHERE T2.\"XCL_016\" = 'OWNER' AND T1.\"XCL_003\" = 'POPLATEK PO OBRATU'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "disp"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM account AS \"r0\" INNER JOIN disp AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_015\" WHERE \"r1\".\"XCL_016\" = 'OWNER' AND \"r0\".\"XCL_003\" = 'POPLATEK PO OBRATU'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:175"
  ]
}
```

### Aggregates the number of rows in the 'disp' table where the 'XCL_016' field equals 'DISPONENT', restricted to records where 'XCL_015' is between 1 and

```json
{
  "kind": "metric",
  "formula": "SUM(\"disp\".\"XCL_016\" = 'DISPONENT')",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_016\" = 'OWNER'), SUM(\"XCL_016\" = 'DISPONENT') FROM disp WHERE \"XCL_015\" BETWEEN 1 AND 10",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r0\".\"XCL_016\" = 'DISPONENT')",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "disp"
      }
    ],
    "scope_sql": "SELECT SUM(\"r0\".\"XCL_016\" = 'DISPONENT') AS \"value\" FROM disp AS \"r0\" WHERE \"r0\".\"XCL_015\" BETWEEN 1 AND 10",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:172"
  ]
}
```

### Distinct values of the district identifier (XCL_018) for districts that have at least one account with a transaction of type 'VYDAJ'.

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_018\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_018\" FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN trans AS T3 ON T2.\"XCL_001\" = T3.\"XCL_047\" WHERE T3.\"XCL_049\" = 'VYDAJ'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:151"
  ]
}
```

### "district"."XCL_019" = 'east Bohemia' AND "account"."XCL_003" = 'POPLATEK PO OBRATU'

```json
{
  "kind": "predicate",
  "formula": "\"district\".\"XCL_019\" = 'east Bohemia' AND \"account\".\"XCL_003\" = 'POPLATEK PO OBRATU'",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_001\") FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE T1.\"XCL_019\" = 'east Bohemia' AND T2.\"XCL_003\" = 'POPLATEK PO OBRATU'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:89"
  ]
}
```

### Client Identifier

```json
{
  "kind": "binding",
  "formula": "\"client\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T4.\"XCL_011\" FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" INNER JOIN disp AS T3 ON T2.\"XCL_001\" = T3.\"XCL_015\" INNER JOIN client AS T4 ON T3.\"XCL_014\" = T4.\"XCL_009\" WHERE T1.\"XCL_035\" = '1996-01-03' AND T1.\"XCL_036\" = 98832",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r3\".\"XCL_011\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "loan"
      },
      {
        "role": "r1",
        "physical_table": "account"
      },
      {
        "role": "r2",
        "physical_table": "disp"
      },
      {
        "role": "r3",
        "physical_table": "client"
      }
    ],
    "scope_sql": "SELECT \"r3\".\"XCL_011\" AS \"value\" FROM loan AS \"r0\" INNER JOIN account AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_001\" INNER JOIN disp AS \"r2\" ON \"r1\".\"XCL_001\" = \"r2\".\"XCL_015\" INNER JOIN client AS \"r3\" ON \"r2\".\"XCL_014\" = \"r3\".\"XCL_009\" WHERE \"r0\".\"XCL_035\" = '1996-01-03' AND \"r0\".\"XCL_036\" = 98832",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:113"
  ]
}
```

### "trans"."XCL_049" = 'VYDAJ' AND "trans"."XCL_048" LIKE '1996-01%'

```json
{
  "kind": "predicate",
  "formula": "\"trans\".\"XCL_049\" = 'VYDAJ' AND \"trans\".\"XCL_048\" LIKE '1996-01%'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_018\" FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN trans AS T3 ON T2.\"XCL_001\" = T3.\"XCL_047\" WHERE T3.\"XCL_049\" = 'VYDAJ' AND T3.\"XCL_048\" LIKE '1996-01%' ORDER BY \"XCL_018\" ASC LIMIT 10",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:129"
  ]
}
```

### "account"."XCL_001" = 130

```json
{
  "kind": "predicate",
  "formula": "\"account\".\"XCL_001\" = 130",
  "grain": [],
  "population_scope": "SELECT STRFTIME('%Y', T1.\"XCL_011\") FROM client AS T1 INNER JOIN disp AS T3 ON T1.\"XCL_009\" = T3.\"XCL_014\" INNER JOIN account AS T2 ON T3.\"XCL_015\" = T2.\"XCL_001\" WHERE T2.\"XCL_001\" = 130",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:174"
  ]
}
```

### Aggregates the count of 'disp' records (identified by XCL_015) that are linked to 'account' records (XCL_001) where the account type is 'POPLATEK TYDN

```json
{
  "kind": "metric",
  "formula": "COUNT(\"disp\".\"XCL_015\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_015\") FROM account AS T1 INNER JOIN disp AS T2 ON T2.\"XCL_015\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'POPLATEK TYDNE' AND T2.\"XCL_016\" = 'OWNER'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_015\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "disp"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_015\") AS \"value\" FROM account AS \"r0\" INNER JOIN disp AS \"r1\" ON \"r1\".\"XCL_015\" = \"r0\".\"XCL_001\" WHERE \"r0\".\"XCL_003\" = 'POPLATEK TYDNE' AND \"r1\".\"XCL_016\" = 'OWNER'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:187"
  ]
}
```

### "card"."XCL_007" = 'classic' AND "disp"."XCL_016" = 'OWNER'

```json
{
  "kind": "predicate",
  "formula": "\"card\".\"XCL_007\" = 'classic' AND \"disp\".\"XCL_016\" = 'OWNER'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_005\") FROM card AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_006\" = T2.\"XCL_013\" WHERE T1.\"XCL_007\" = 'classic' AND T2.\"XCL_016\" = 'OWNER'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:153"
  ]
}
```

### Calculates the percentage change of district attribute XCL_029 relative to XCL_028. The formula is ((XCL_029 - XCL_028) / XCL_028) * 100, with the num

```json
{
  "kind": "binding",
  "formula": "CAST((\"district\".\"XCL_029\" - \"district\".\"XCL_028\") AS REAL) * 100 / \"district\".\"XCL_028\"",
  "grain": [],
  "population_scope": "SELECT CAST((T3.\"XCL_029\" - T3.\"XCL_028\") AS REAL) * 100 / T3.\"XCL_028\" FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" INNER JOIN district AS T3 ON T2.\"XCL_002\" = T3.\"XCL_017\" WHERE T1.\"XCL_039\" = 'D'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST((\"r2\".\"XCL_029\" - \"r2\".\"XCL_028\") AS REAL) * 100 / \"r2\".\"XCL_028\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "loan"
      },
      {
        "role": "r1",
        "physical_table": "account"
      },
      {
        "role": "r2",
        "physical_table": "district"
      }
    ],
    "scope_sql": "SELECT CAST((\"r2\".\"XCL_029\" - \"r2\".\"XCL_028\") AS REAL) * 100 / \"r2\".\"XCL_028\" AS \"value\" FROM loan AS \"r0\" INNER JOIN account AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_001\" INNER JOIN district AS \"r2\" ON \"r1\".\"XCL_002\" = \"r2\".\"XCL_017\" WHERE \"r0\".\"XCL_039\" = 'D'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:125"
  ]
}
```

### STRFTIME('%Y', "account"."XCL_004") >= '1997' AND "district"."XCL_031" > 4000

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"account\".\"XCL_004\") >= '1997' AND \"district\".\"XCL_031\" > 4000",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_031\") FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE STRFTIME('%Y', T2.\"XCL_004\") >= '1997' AND T1.\"XCL_031\" > 4000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:152"
  ]
}
```

### Calculates the percentage of clients (identified by XCL_009) where the attribute XCL_010 is 'F', within the population of clients joined to districts 

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"client\".\"XCL_010\" = 'F') AS REAL) * 100 / COUNT(\"client\".\"XCL_009\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(T2.\"XCL_010\" = 'F') AS REAL) * 100 / COUNT(T2.\"XCL_009\") FROM district AS T1 INNER JOIN client AS T2 ON T1.\"XCL_017\" = T2.\"XCL_012\" WHERE T1.\"XCL_027\" > 10000",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(\"r1\".\"XCL_010\" = 'F') AS REAL) * 100 / COUNT(\"r1\".\"XCL_009\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "district"
      },
      {
        "role": "r1",
        "physical_table": "client"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(\"r1\".\"XCL_010\" = 'F') AS REAL) * 100 / COUNT(\"r1\".\"XCL_009\") AS \"value\" FROM district AS \"r0\" INNER JOIN client AS \"r1\" ON \"r0\".\"XCL_017\" = \"r1\".\"XCL_012\" WHERE \"r0\".\"XCL_027\" > 10000",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:168"
  ]
}
```

### "loan"."XCL_035" = '1996-01-03' AND "loan"."XCL_036" = 98832

```json
{
  "kind": "predicate",
  "formula": "\"loan\".\"XCL_035\" = '1996-01-03' AND \"loan\".\"XCL_036\" = 98832",
  "grain": [],
  "population_scope": "SELECT T4.\"XCL_011\" FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" INNER JOIN disp AS T3 ON T2.\"XCL_001\" = T3.\"XCL_015\" INNER JOIN client AS T4 ON T3.\"XCL_014\" = T4.\"XCL_009\" WHERE T1.\"XCL_035\" = '1996-01-03' AND T1.\"XCL_036\" = 98832",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:113"
  ]
}
```

### Calculates the percentage of card records where the card type (XCL_007) is 'gold' and the issue year (derived from XCL_008) is strictly before 1998, r

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"card\".\"XCL_007\" = 'gold' AND STRFTIME('%Y', \"card\".\"XCL_008\") < '1998') AS REAL) * 100 / COUNT(\"card\".\"XCL_005\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(\"XCL_007\" = 'gold' AND STRFTIME('%Y', \"XCL_008\") < '1998') AS REAL) * 100 / COUNT(\"XCL_005\") FROM card",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(\"r0\".\"XCL_007\" = 'gold' AND STRFTIME('%Y', \"r0\".\"XCL_008\") < '1998') AS REAL) * 100 / COUNT(\"r0\".\"XCL_005\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "card"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(\"r0\".\"XCL_007\" = 'gold' AND STRFTIME('%Y', \"r0\".\"XCL_008\") < '1998') AS REAL) * 100 / COUNT(\"r0\".\"XCL_005\") AS \"value\" FROM card AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:155"
  ]
}
```

### "account"."XCL_003" = 'POPLATEK TYDNE' AND "disp"."XCL_016" = 'OWNER'

```json
{
  "kind": "predicate",
  "formula": "\"account\".\"XCL_003\" = 'POPLATEK TYDNE' AND \"disp\".\"XCL_016\" = 'OWNER'",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_015\") FROM account AS T1 INNER JOIN disp AS T2 ON T2.\"XCL_015\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'POPLATEK TYDNE' AND T2.\"XCL_016\" = 'OWNER'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:187"
  ]
}
```

### "card"."XCL_007" = 'gold' AND "disp"."XCL_016" = 'OWNER'

```json
{
  "kind": "predicate",
  "formula": "\"card\".\"XCL_007\" = 'gold' AND \"disp\".\"XCL_016\" = 'OWNER'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_014\", STRFTIME('%Y', CURRENT_TIMESTAMP) - STRFTIME('%Y', T3.\"XCL_011\") FROM disp AS T1 INNER JOIN card AS T2 ON T2.\"XCL_006\" = T1.\"XCL_013\" INNER JOIN client AS T3 ON T1.\"XCL_014\" = T3.\"XCL_009\" WHERE T2.\"XCL_007\" = 'gold' AND T1.\"XCL_016\" = 'OWNER'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:194"
  ]
}
```

### STRFTIME('%Y', "loan"."XCL_035") = '1997' AND "account"."XCL_003" = 'POPLATEK TYDNE'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"loan\".\"XCL_035\") = '1997' AND \"account\".\"XCL_003\" = 'POPLATEK TYDNE'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_001\" FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" WHERE STRFTIME('%Y', T1.\"XCL_035\") = '1997' AND T2.\"XCL_003\" = 'POPLATEK TYDNE' ORDER BY T1.\"XCL_036\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:98"
  ]
}
```

### "loan"."XCL_039" = 'D'

```json
{
  "kind": "predicate",
  "formula": "\"loan\".\"XCL_039\" = 'D'",
  "grain": [],
  "population_scope": "SELECT CAST((T3.\"XCL_029\" - T3.\"XCL_028\") AS REAL) * 100 / T3.\"XCL_028\" FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" INNER JOIN district AS T3 ON T2.\"XCL_002\" = T3.\"XCL_017\" WHERE T1.\"XCL_039\" = 'D'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:125"
  ]
}
```

### Client Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"client\".\"XCL_009\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE STRFTIME('%Y', T1.\"XCL_011\") = '1920' AND T2.\"XCL_019\" = 'east Bohemia'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_009\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "district"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_009\") AS \"value\" FROM client AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_012\" = \"r1\".\"XCL_017\" WHERE STRFTIME('%Y', \"r0\".\"XCL_011\") = '1920' AND \"r1\".\"XCL_019\" = 'east Bohemia'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:190"
  ]
}
```

### Aggregates the count of transaction IDs (XCL_047) from the trans table where the transaction amount (XCL_052) is negative, the transaction type (XCL_0

```json
{
  "kind": "metric",
  "formula": "COUNT(\"trans\".\"XCL_047\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_047\") FROM trans AS T1 INNER JOIN account AS T2 ON T1.\"XCL_047\" = T2.\"XCL_001\" WHERE T1.\"XCL_052\" < 0 AND T1.\"XCL_050\" = 'VYBER KARTOU' AND T2.\"XCL_003\" = 'POPLATEK MESICNE'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_047\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "trans"
      },
      {
        "role": "r1",
        "physical_table": "account"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_047\") AS \"value\" FROM trans AS \"r0\" INNER JOIN account AS \"r1\" ON \"r0\".\"XCL_047\" = \"r1\".\"XCL_001\" WHERE \"r0\".\"XCL_052\" < 0 AND \"r0\".\"XCL_050\" = 'VYBER KARTOU' AND \"r1\".\"XCL_003\" = 'POPLATEK MESICNE'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:135"
  ]
}
```

### "order"."XCL_040" = 32423

```json
{
  "kind": "predicate",
  "formula": "\"order\".\"XCL_040\" = 32423",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_009\" FROM \"order\" AS T1 INNER JOIN account AS T2 ON T1.\"XCL_041\" = T2.\"XCL_001\" INNER JOIN disp AS T4 ON T4.\"XCL_015\" = T2.\"XCL_001\" INNER JOIN client AS T3 ON T4.\"XCL_014\" = T3.\"XCL_009\" WHERE T1.\"XCL_040\" = 32423",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:164"
  ]
}
```

### Aggregates the count of 'XCL_015' from the 'disp' table (aliased as T3) for records where the district is 'south Bohemia' and the 'XCL_016' field is n

```json
{
  "kind": "metric",
  "formula": "COUNT(\"disp\".\"XCL_015\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T3.\"XCL_015\") FROM district AS T1 INNER JOIN client AS T2 ON T1.\"XCL_017\" = T2.\"XCL_012\" INNER JOIN disp AS T3 ON T2.\"XCL_009\" = T3.\"XCL_014\" WHERE T1.\"XCL_019\" = 'south Bohemia' AND T3.\"XCL_016\" <> 'OWNER'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r2\".\"XCL_015\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "district"
      },
      {
        "role": "r1",
        "physical_table": "client"
      },
      {
        "role": "r2",
        "physical_table": "disp"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r2\".\"XCL_015\") AS \"value\" FROM district AS \"r0\" INNER JOIN client AS \"r1\" ON \"r0\".\"XCL_017\" = \"r1\".\"XCL_012\" INNER JOIN disp AS \"r2\" ON \"r1\".\"XCL_009\" = \"r2\".\"XCL_014\" WHERE \"r0\".\"XCL_019\" = 'south Bohemia' AND \"r2\".\"XCL_016\" <> 'OWNER'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:130"
  ]
}
```

### "trans"."XCL_051" = 840 AND "trans"."XCL_048" = '1998-10-14'

```json
{
  "kind": "predicate",
  "formula": "\"trans\".\"XCL_051\" = 840 AND \"trans\".\"XCL_048\" = '1998-10-14'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_004\" FROM account AS T1 INNER JOIN trans AS T2 ON T1.\"XCL_001\" = T2.\"XCL_047\" WHERE T2.\"XCL_051\" = 840 AND T2.\"XCL_048\" = '1998-10-14'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:104"
  ]
}
```

### "account"."XCL_003" = 'POPLATEK PO OBRATU' AND STRFTIME('%Y', "account"."XCL_004") = '1993'

```json
{
  "kind": "predicate",
  "formula": "\"account\".\"XCL_003\" = 'POPLATEK PO OBRATU' AND STRFTIME('%Y', \"account\".\"XCL_004\") = '1993'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T2.\"XCL_018\", T2.\"XCL_019\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE T1.\"XCL_003\" = 'POPLATEK PO OBRATU' AND STRFTIME('%Y', T1.\"XCL_004\") = '1993'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:119"
  ]
}
```

### Account Identifier

```json
{
  "kind": "binding",
  "formula": "\"account\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_004\" FROM account AS T1 INNER JOIN trans AS T2 ON T1.\"XCL_001\" = T2.\"XCL_047\" WHERE T2.\"XCL_051\" = 840 AND T2.\"XCL_048\" = '1998-10-14'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_004\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "trans"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_004\" AS \"value\" FROM account AS \"r0\" INNER JOIN trans AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_047\" WHERE \"r1\".\"XCL_051\" = 840 AND \"r1\".\"XCL_048\" = '1998-10-14'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:104"
  ]
}
```

### Card Attribute XCL_007

```json
{
  "kind": "binding",
  "formula": "\"card\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_007\" FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN card AS T3 ON T2.\"XCL_013\" = T3.\"XCL_006\" WHERE T1.\"XCL_009\" = 9",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_007\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "disp"
      },
      {
        "role": "r2",
        "physical_table": "card"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_007\" AS \"value\" FROM client AS \"r0\" INNER JOIN disp AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_014\" INNER JOIN card AS \"r2\" ON \"r1\".\"XCL_013\" = \"r2\".\"XCL_006\" WHERE \"r0\".\"XCL_009\" = 9",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:178"
  ]
}
```

### Account Identifier

```json
{
  "kind": "binding",
  "formula": "\"account\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_009\", T3.\"XCL_001\" FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" INNER JOIN disp AS T4 ON T1.\"XCL_009\" = T4.\"XCL_014\" INNER JOIN account AS T3 ON T2.\"XCL_017\" = T3.\"XCL_002\" AND T4.\"XCL_015\" = T3.\"XCL_001\" WHERE T2.\"XCL_019\" = 'east Bohemia' AND STRFTIME('%Y', T1.\"XCL_011\") BETWEEN '1983' AND '1987'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r3\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "district"
      },
      {
        "role": "r2",
        "physical_table": "disp"
      },
      {
        "role": "r3",
        "physical_table": "account"
      }
    ],
    "scope_sql": "SELECT \"r3\".\"XCL_001\" AS \"value\" FROM client AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_012\" = \"r1\".\"XCL_017\" INNER JOIN disp AS \"r2\" ON \"r0\".\"XCL_009\" = \"r2\".\"XCL_014\" INNER JOIN account AS \"r3\" ON \"r1\".\"XCL_017\" = \"r3\".\"XCL_002\" AND \"r2\".\"XCL_015\" = \"r3\".\"XCL_001\" WHERE \"r1\".\"XCL_019\" = 'east Bohemia' AND STRFTIME('%Y', \"r0\".\"XCL_011\") BETWEEN '1983' AND '1987'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:180"
  ]
}
```

### Aggregated sum of 'XCL_044' from the 'order' table. Calculated at the grain of 'XCL_041' and 'XCL_045'. Used in the outer query to filter for a specif

```json
{
  "kind": "metric",
  "formula": "SUM(\"order\".\"XCL_044\")",
  "grain": [
    "\"order\".\"XCL_041\"",
    "\"order\".\"XCL_045\""
  ],
  "population_scope": "SELECT \"XCL_041\", \"XCL_045\", SUM(\"XCL_044\") AS total_amount FROM \"order\" GROUP BY \"XCL_041\", \"XCL_045\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r0\".\"XCL_044\")",
    "grain": [
      "\"r0\".\"XCL_041\"",
      "\"r0\".\"XCL_045\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "order"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_041\" AS \"grain_0\", \"r0\".\"XCL_045\" AS \"grain_1\", SUM(\"r0\".\"XCL_044\") AS \"value\" FROM \"order\" AS \"r0\" GROUP BY \"r0\".\"XCL_041\", \"r0\".\"XCL_045\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:173"
  ]
}
```

### "district"."XCL_019" = 'south Bohemia' AND "disp"."XCL_016" <> 'OWNER'

```json
{
  "kind": "predicate",
  "formula": "\"district\".\"XCL_019\" = 'south Bohemia' AND \"disp\".\"XCL_016\" <> 'OWNER'",
  "grain": [],
  "population_scope": "SELECT COUNT(T3.\"XCL_015\") FROM district AS T1 INNER JOIN client AS T2 ON T1.\"XCL_017\" = T2.\"XCL_012\" INNER JOIN disp AS T3 ON T2.\"XCL_009\" = T3.\"XCL_014\" WHERE T1.\"XCL_019\" = 'south Bohemia' AND T3.\"XCL_016\" <> 'OWNER'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:130"
  ]
}
```

### Distinct district identifier (XCL_018) for districts that have at least one account with a transaction recorded in January 1996 classified as 'VYDAJ' 

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_018\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_018\" FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN trans AS T3 ON T2.\"XCL_001\" = T3.\"XCL_047\" WHERE T3.\"XCL_049\" = 'VYDAJ' AND T3.\"XCL_048\" LIKE '1996-01%' ORDER BY \"XCL_018\" ASC LIMIT 10",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:129"
  ]
}
```

### Account Attribute XCL_003

```json
{
  "kind": "binding",
  "formula": "T1.\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\", T2.\"XCL_045\" FROM account AS T1 INNER JOIN (SELECT \"XCL_041\", \"XCL_045\", SUM(\"XCL_044\") AS total_amount FROM \"order\" GROUP BY \"XCL_041\", \"XCL_045\") AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_001\" = 3 AND T2.\"total_amount\" = 3539",
  "upstream_scopes": [
    "SELECT \"XCL_041\", \"XCL_045\", SUM(\"XCL_044\") AS total_amount FROM \"order\" GROUP BY \"XCL_041\", \"XCL_045\""
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:173"
  ]
}
```

### Calculates the percentage difference between the sum of transaction amounts (XCL_052) on 1998-12-27 and 1993-03-22, relative to the 1993-03-22 total. 

```json
{
  "kind": "metric",
  "formula": "CAST((SUM(IIF(\"trans\".\"XCL_048\" = '1998-12-27', \"trans\".\"XCL_052\", 0)) - SUM(IIF(\"trans\".\"XCL_048\" = '1993-03-22', \"trans\".\"XCL_052\", 0))) AS REAL) * 100 / SUM(IIF(\"trans\".\"XCL_048\" = '1993-03-22', \"trans\".\"XCL_052\", 0))",
  "grain": [],
  "population_scope": "SELECT CAST((SUM(IIF(T3.\"XCL_048\" = '1998-12-27', T3.\"XCL_052\", 0)) - SUM(IIF(T3.\"XCL_048\" = '1993-03-22', T3.\"XCL_052\", 0))) AS REAL) * 100 / SUM(IIF(T3.\"XCL_048\" = '1993-03-22', T3.\"XCL_052\", 0)) FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" INNER JOIN trans AS T3 ON T3.\"XCL_047\" = T2.\"XCL_001\" WHERE T1.\"XCL_035\" = '1993-07-05'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST((SUM(IIF(\"r2\".\"XCL_048\" = '1998-12-27', \"r2\".\"XCL_052\", 0)) - SUM(IIF(\"r2\".\"XCL_048\" = '1993-03-22', \"r2\".\"XCL_052\", 0))) AS REAL) * 100 / SUM(IIF(\"r2\".\"XCL_048\" = '1993-03-22', \"r2\".\"XCL_052\", 0))",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "loan"
      },
      {
        "role": "r1",
        "physical_table": "account"
      },
      {
        "role": "r2",
        "physical_table": "trans"
      }
    ],
    "scope_sql": "SELECT CAST((SUM(IIF(\"r2\".\"XCL_048\" = '1998-12-27', \"r2\".\"XCL_052\", 0)) - SUM(IIF(\"r2\".\"XCL_048\" = '1993-03-22', \"r2\".\"XCL_052\", 0))) AS REAL) * 100 / SUM(IIF(\"r2\".\"XCL_048\" = '1993-03-22', \"r2\".\"XCL_052\", 0)) AS \"value\" FROM loan AS \"r0\" INNER JOIN account AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_001\" INNER JOIN trans AS \"r2\" ON \"r2\".\"XCL_047\" = \"r1\".\"XCL_001\" WHERE \"r0\".\"XCL_035\" = '1993-07-05'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:116"
  ]
}
```

### Client Identifier

```json
{
  "kind": "binding",
  "formula": "\"disp\".\"XCL_014\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_014\", STRFTIME('%Y', CURRENT_TIMESTAMP) - STRFTIME('%Y', T3.\"XCL_011\") FROM disp AS T1 INNER JOIN card AS T2 ON T2.\"XCL_006\" = T1.\"XCL_013\" INNER JOIN client AS T3 ON T1.\"XCL_014\" = T3.\"XCL_009\" WHERE T2.\"XCL_007\" = 'gold' AND T1.\"XCL_016\" = 'OWNER'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_014\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "disp"
      },
      {
        "role": "r1",
        "physical_table": "card"
      },
      {
        "role": "r2",
        "physical_table": "client"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_014\" AS \"value\" FROM disp AS \"r0\" INNER JOIN card AS \"r1\" ON \"r1\".\"XCL_006\" = \"r0\".\"XCL_013\" INNER JOIN client AS \"r2\" ON \"r0\".\"XCL_014\" = \"r2\".\"XCL_009\" WHERE \"r1\".\"XCL_007\" = 'gold' AND \"r0\".\"XCL_016\" = 'OWNER'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:194"
  ]
}
```

### STRFTIME('%Y', "trans"."XCL_048") = '1998' AND "trans"."XCL_050" = 'VYBER KARTOU'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"trans\".\"XCL_048\") = '1998' AND \"trans\".\"XCL_050\" = 'VYBER KARTOU'",
  "grain": [],
  "population_scope": "SELECT AVG(T4.\"XCL_051\") FROM card AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_006\" = T2.\"XCL_013\" INNER JOIN account AS T3 ON T2.\"XCL_015\" = T3.\"XCL_001\" INNER JOIN trans AS T4 ON T3.\"XCL_001\" = T4.\"XCL_047\" WHERE STRFTIME('%Y', T4.\"XCL_048\") = '1998' AND T4.\"XCL_050\" = 'VYBER KARTOU'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:144"
  ]
}
```

### District Attribute XCL_018

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_018\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_017\", \"XCL_018\" FROM district ORDER BY \"XCL_029\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:133"
  ]
}
```

### "trans"."XCL_054" = 'AB' AND "district"."XCL_019" = 'north Bohemia'

```json
{
  "kind": "predicate",
  "formula": "\"trans\".\"XCL_054\" = 'AB' AND \"district\".\"XCL_019\" = 'north Bohemia'",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_001\") FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN trans AS T3 ON T2.\"XCL_001\" = T3.\"XCL_047\" WHERE T3.\"XCL_054\" = 'AB' AND T1.\"XCL_019\" = 'north Bohemia'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:150"
  ]
}
```

### The name (XCL_018) of the single district with the highest number of active loans. The population is restricted to districts linked to accounts that h

```json
{
  "kind": "binding",
  "formula": "\"District\".\"XCL_018\"",
  "grain": [
    "\"District\".\"XCL_017\""
  ],
  "population_scope": "SELECT T1.\"XCL_018\" FROM District AS T1 INNER JOIN Account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN Loan AS T3 ON T2.\"XCL_001\" = T3.\"XCL_034\" WHERE T3.\"XCL_039\" = 'A' GROUP BY T1.\"XCL_017\" ORDER BY COUNT(T2.\"XCL_001\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:163"
  ]
}
```

### STRFTIME('%Y', "trans"."XCL_048") = '1995'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"trans\".\"XCL_048\") = '1995'",
  "grain": [],
  "population_scope": "SELECT \"XCL_047\" FROM trans WHERE STRFTIME('%Y', \"XCL_048\") = '1995' ORDER BY \"XCL_048\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:101"
  ]
}
```

### Account Identifier

```json
{
  "kind": "binding",
  "formula": "\"account\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T2.\"XCL_018\", T2.\"XCL_019\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE T1.\"XCL_003\" = 'POPLATEK PO OBRATU' AND STRFTIME('%Y', T1.\"XCL_004\") = '1993'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" WHERE \"r0\".\"XCL_003\" = 'POPLATEK PO OBRATU' AND STRFTIME('%Y', \"r0\".\"XCL_004\") = '1993'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:119"
  ]
}
```

### "district"."XCL_019" = 'Prague'

```json
{
  "kind": "predicate",
  "formula": "\"district\".\"XCL_019\" = 'Prague'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE T2.\"XCL_019\" = 'Prague' ORDER BY T1.\"XCL_004\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:114"
  ]
}
```

### The XCL_001 (account identifier) from the account table for the single record that has the highest XCL_027 value in its associated district, among acc

```json
{
  "kind": "binding",
  "formula": "\"account\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", (SELECT MAX(\"XCL_027\") - MIN(\"XCL_027\") FROM district) FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN disp AS T3 ON T1.\"XCL_001\" = T3.\"XCL_015\" INNER JOIN client AS T4 ON T3.\"XCL_014\" = T4.\"XCL_009\" WHERE T2.\"XCL_017\" = (SELECT \"XCL_012\" FROM client WHERE \"XCL_010\" = 'F' ORDER BY \"XCL_011\" ASC LIMIT 1) ORDER BY T2.\"XCL_027\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:94"
  ]
}
```

### STRFTIME('%Y', "account"."XCL_004") < '1997' AND "trans"."XCL_051" > 3000

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"account\".\"XCL_004\") < '1997' AND \"trans\".\"XCL_051\" > 3000",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_001\" FROM trans AS T1 INNER JOIN account AS T2 ON T1.\"XCL_047\" = T2.\"XCL_001\" WHERE STRFTIME('%Y', T2.\"XCL_004\") < '1997' AND T1.\"XCL_051\" > 3000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:102"
  ]
}
```

### "client"."XCL_011" = '1976-01-29' AND "client"."XCL_010" = 'F'

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_011\" = '1976-01-29' AND \"client\".\"XCL_010\" = 'F'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_018\" FROM district AS T1 INNER JOIN client AS T2 ON T1.\"XCL_017\" = T2.\"XCL_012\" WHERE T2.\"XCL_011\" = '1976-01-29' AND T2.\"XCL_010\" = 'F'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:112"
  ]
}
```

### Aggregates the count of account identifiers (XCL_001) from the account table. The population is restricted to accounts located in district 1 (XCL_002 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"account\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN loan AS T3 ON T1.\"XCL_001\" = T3.\"XCL_034\" WHERE T1.\"XCL_002\" = 1 AND (T3.\"XCL_039\" = 'C' OR T3.\"XCL_039\" = 'D')",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      },
      {
        "role": "r2",
        "physical_table": "loan"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" INNER JOIN loan AS \"r2\" ON \"r0\".\"XCL_001\" = \"r2\".\"XCL_034\" WHERE \"r0\".\"XCL_002\" = 1 AND (\"r2\".\"XCL_039\" = 'C' OR \"r2\".\"XCL_039\" = 'D')",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:137"
  ]
}
```

### Account Identifier (Prague, Earliest)

```json
{
  "kind": "binding",
  "formula": "\"account\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE T2.\"XCL_019\" = 'Prague' ORDER BY T1.\"XCL_004\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:114"
  ]
}
```

### "loan"."XCL_037" = 24 AND "account"."XCL_003" = 'POPLATEK TYDNE'

```json
{
  "kind": "predicate",
  "formula": "\"loan\".\"XCL_037\" = 24 AND \"account\".\"XCL_003\" = 'POPLATEK TYDNE'",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_034\") FROM account AS T1 INNER JOIN loan AS T2 ON T1.\"XCL_001\" = T2.\"XCL_034\" WHERE T2.\"XCL_037\" = 24 AND T1.\"XCL_003\" = 'POPLATEK TYDNE'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:191"
  ]
}
```

### Owner Identifier

```json
{
  "kind": "binding",
  "formula": "\"disp\".\"XCL_014\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_014\" FROM disp AS T1 INNER JOIN account AS T3 ON T1.\"XCL_015\" = T3.\"XCL_001\" INNER JOIN loan AS T2 ON T3.\"XCL_001\" = T2.\"XCL_034\" WHERE T1.\"XCL_016\" = 'OWNER' ORDER BY T2.\"XCL_036\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:156"
  ]
}
```

### District Identifier

```json
{
  "kind": "binding",
  "formula": "\"district\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_031\" FROM district AS T1 INNER JOIN \"account\" AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE T2.\"XCL_001\" = 532",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_031\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "district"
      },
      {
        "role": "r1",
        "physical_table": "account"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_031\" AS \"value\" FROM district AS \"r0\" INNER JOIN \"account\" AS \"r1\" ON \"r0\".\"XCL_017\" = \"r1\".\"XCL_002\" WHERE \"r1\".\"XCL_001\" = 532",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:157"
  ]
}
```

### Account Identifier

```json
{
  "kind": "binding",
  "formula": "\"account\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T1.\"XCL_004\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE T2.\"XCL_018\" = 'Prachatice'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" WHERE \"r1\".\"XCL_018\" = 'Prachatice'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:121"
  ]
}
```

### Account Identifier

```json
{
  "kind": "binding",
  "formula": "\"account\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_002\" FROM account AS T1 INNER JOIN loan AS T2 ON T1.\"XCL_001\" = T2.\"XCL_034\" WHERE T2.\"XCL_035\" = '1994-08-25'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_002\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "loan"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_002\" AS \"value\" FROM account AS \"r0\" INNER JOIN loan AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_034\" WHERE \"r1\".\"XCL_035\" = '1994-08-25'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:105"
  ]
}
```

### "district"."XCL_019" = 'south Bohemia'

```json
{
  "kind": "predicate",
  "formula": "\"district\".\"XCL_019\" = 'south Bohemia'",
  "grain": [
    "\"district\".\"XCL_020\""
  ],
  "population_scope": "SELECT CAST(SUM(T1.\"XCL_010\" = 'M') AS REAL) * 100 / COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T2.\"XCL_019\" = 'south Bohemia' GROUP BY T2.\"XCL_020\" ORDER BY T2.\"XCL_020\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:115"
  ]
}
```

### "account"."XCL_001" = 532

```json
{
  "kind": "predicate",
  "formula": "\"account\".\"XCL_001\" = 532",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_031\" FROM district AS T1 INNER JOIN \"account\" AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE T2.\"XCL_001\" = 532",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:157"
  ]
}
```

### "district"."XCL_017" = 5

```json
{
  "kind": "predicate",
  "formula": "\"district\".\"XCL_017\" = 5",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_046\" FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN trans AS T3 ON T2.\"XCL_001\" = T3.\"XCL_047\" WHERE T1.\"XCL_017\" = 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:165"
  ]
}
```

### A metric that counts the number of rows in the 'client' table (specifically the 'XCL_009' column) where the client's gender ('XCL_010') is 'M' and the

```json
{
  "kind": "metric",
  "formula": "COUNT(\"client\".\"XCL_009\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'M' AND T2.\"XCL_031\" = (SELECT T3.\"XCL_031\" FROM district AS T3 ORDER BY T3.\"XCL_031\" DESC LIMIT 1 OFFSET 1)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:138"
  ]
}
```

### Client Age in Years

```json
{
  "kind": "binding",
  "formula": "STRFTIME('%Y', CURRENT_TIMESTAMP) - STRFTIME('%Y', \"client\".\"XCL_011\")",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_014\", STRFTIME('%Y', CURRENT_TIMESTAMP) - STRFTIME('%Y', T3.\"XCL_011\") FROM disp AS T1 INNER JOIN card AS T2 ON T2.\"XCL_006\" = T1.\"XCL_013\" INNER JOIN client AS T3 ON T1.\"XCL_014\" = T3.\"XCL_009\" WHERE T2.\"XCL_007\" = 'gold' AND T1.\"XCL_016\" = 'OWNER'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "STRFTIME('%Y', CURRENT_TIMESTAMP) - STRFTIME('%Y', \"r2\".\"XCL_011\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "disp"
      },
      {
        "role": "r1",
        "physical_table": "card"
      },
      {
        "role": "r2",
        "physical_table": "client"
      }
    ],
    "scope_sql": "SELECT STRFTIME('%Y', CURRENT_TIMESTAMP) - STRFTIME('%Y', \"r2\".\"XCL_011\") AS \"value\" FROM disp AS \"r0\" INNER JOIN card AS \"r1\" ON \"r1\".\"XCL_006\" = \"r0\".\"XCL_013\" INNER JOIN client AS \"r2\" ON \"r0\".\"XCL_014\" = \"r2\".\"XCL_009\" WHERE \"r1\".\"XCL_007\" = 'gold' AND \"r0\".\"XCL_016\" = 'OWNER'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:194"
  ]
}
```

### Client Identifier XCL_010

```json
{
  "kind": "binding",
  "formula": "\"client\".\"XCL_010\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_010\" FROM district AS T1 INNER JOIN client AS T2 ON T1.\"XCL_017\" = T2.\"XCL_012\" ORDER BY T1.\"XCL_027\" DESC, T2.\"XCL_011\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:107"
  ]
}
```

### "loan"."XCL_035" = '1993-07-05'

```json
{
  "kind": "predicate",
  "formula": "\"loan\".\"XCL_035\" = '1993-07-05'",
  "grain": [],
  "population_scope": "SELECT CAST((SUM(IIF(T3.\"XCL_048\" = '1998-12-27', T3.\"XCL_052\", 0)) - SUM(IIF(T3.\"XCL_048\" = '1993-03-22', T3.\"XCL_052\", 0))) AS REAL) * 100 / SUM(IIF(T3.\"XCL_048\" = '1993-03-22', T3.\"XCL_052\", 0)) FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" INNER JOIN trans AS T3 ON T3.\"XCL_047\" = T2.\"XCL_001\" WHERE T1.\"XCL_035\" = '1993-07-05'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:116"
  ]
}
```

### Aggregates the number of client records (identified by XCL_009) where the client gender (XCL_010) is 'F' and the associated district (XCL_019) is 'sou

```json
{
  "kind": "metric",
  "formula": "COUNT(\"client\".\"XCL_009\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'F' AND T2.\"XCL_019\" = 'south Bohemia'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_009\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "district"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_009\") AS \"value\" FROM client AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_012\" = \"r1\".\"XCL_017\" WHERE \"r0\".\"XCL_010\" = 'F' AND \"r1\".\"XCL_019\" = 'south Bohemia'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:147"
  ]
}
```

### Loan Identifier

```json
{
  "kind": "binding",
  "formula": "\"loan\".\"XCL_034\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_034\" FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" WHERE STRFTIME('%Y', T2.\"XCL_004\") = '1993' AND T1.\"XCL_037\" > 12 ORDER BY T1.\"XCL_036\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:99"
  ]
}
```

### Identifies the single client ID (XCL_009) from the client table that has the maximum value in the XCL_011 column. This acts as a filter parameter to i

```json
{
  "kind": "binding",
  "formula": "\"client\".\"XCL_009\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_009\" FROM client ORDER BY \"XCL_011\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:95"
  ]
}
```

### Aggregates the total number of client records (XCL_009) where the client gender (XCL_010) is 'M', located in districts (XCL_019) named 'north Bohemia'

```json
{
  "kind": "metric",
  "formula": "COUNT(\"client\".\"XCL_009\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'M' AND T2.\"XCL_019\" = 'north Bohemia' AND T2.\"XCL_027\" > 8000",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_009\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "district"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_009\") AS \"value\" FROM client AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_012\" = \"r1\".\"XCL_017\" WHERE \"r0\".\"XCL_010\" = 'M' AND \"r1\".\"XCL_019\" = 'north Bohemia' AND \"r1\".\"XCL_027\" > 8000",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:93"
  ]
}
```

### Identifier from the 'order' table used as a secondary grouping dimension in the subquery. It is joined with the account key to define the grain of the

```json
{
  "kind": "binding",
  "formula": "\"order\".\"XCL_045\"",
  "grain": [
    "\"order\".\"XCL_041\"",
    "\"order\".\"XCL_045\""
  ],
  "population_scope": "SELECT \"XCL_041\", \"XCL_045\", SUM(\"XCL_044\") AS total_amount FROM \"order\" GROUP BY \"XCL_041\", \"XCL_045\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_045\"",
    "grain": [
      "\"r0\".\"XCL_041\"",
      "\"r0\".\"XCL_045\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "order"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_041\" AS \"grain_0\", \"r0\".\"XCL_045\" AS \"grain_1\", \"r0\".\"XCL_045\" AS \"value\" FROM \"order\" AS \"r0\" GROUP BY \"r0\".\"XCL_041\", \"r0\".\"XCL_045\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:173"
  ]
}
```

### Account District Identifier

```json
{
  "kind": "binding",
  "formula": "\"account\".\"XCL_002\"",
  "grain": [
    "\"account\".\"XCL_002\""
  ],
  "population_scope": "SELECT T1.\"XCL_002\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" INNER JOIN trans AS T3 ON T1.\"XCL_001\" = T3.\"XCL_047\" WHERE STRFTIME('%Y', T3.\"XCL_048\") = '1997' GROUP BY T1.\"XCL_002\" HAVING SUM(T3.\"XCL_051\") > 10000",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_002\"",
    "grain": [
      "\"r0\".\"XCL_002\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      },
      {
        "role": "r2",
        "physical_table": "trans"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_002\" AS \"grain_0\", \"r0\".\"XCL_002\" AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" INNER JOIN trans AS \"r2\" ON \"r0\".\"XCL_001\" = \"r2\".\"XCL_047\" WHERE STRFTIME('%Y', \"r2\".\"XCL_048\") = '1997' GROUP BY \"r0\".\"XCL_002\" HAVING SUM(\"r2\".\"XCL_051\") > 10000",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:141"
  ]
}
```

### "client"."XCL_010" = 'F' AND "district"."XCL_018" = 'Jesenik'

```json
{
  "kind": "predicate",
  "formula": "\"client\".\"XCL_010\" = 'F' AND \"district\".\"XCL_018\" = 'Jesenik'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T2 ON T1.\"XCL_012\" = T2.\"XCL_017\" WHERE T1.\"XCL_010\" = 'F' AND T2.\"XCL_018\" = 'Jesenik'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:109"
  ]
}
```

### "account"."XCL_003" = 'POPLATEK TYDNE'

```json
{
  "kind": "predicate",
  "formula": "\"account\".\"XCL_003\" = 'POPLATEK TYDNE'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(T1.\"XCL_010\" = 'M') AS REAL) * 100 / COUNT(T1.\"XCL_009\") FROM client AS T1 INNER JOIN district AS T3 ON T1.\"XCL_012\" = T3.\"XCL_017\" INNER JOIN account AS T2 ON T2.\"XCL_002\" = T3.\"XCL_017\" INNER JOIN disp AS T4 ON T1.\"XCL_009\" = T4.\"XCL_014\" AND T2.\"XCL_001\" = T4.\"XCL_015\" WHERE T2.\"XCL_003\" = 'POPLATEK TYDNE'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:186"
  ]
}
```

### "account"."XCL_003" = 'POPLATEK TYDNE' AND "loan"."XCL_036" < 200000

```json
{
  "kind": "predicate",
  "formula": "\"account\".\"XCL_003\" = 'POPLATEK TYDNE' AND \"loan\".\"XCL_036\" < 200000",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_034\") FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" WHERE T2.\"XCL_003\" = 'POPLATEK TYDNE' AND T1.\"XCL_036\" < 200000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:160"
  ]
}
```

### Aggregates the count of loan records (identified by XCL_034) that are associated with accounts having a payment type of 'POPLATEK TYDNE' (Weekly Payme

```json
{
  "kind": "metric",
  "formula": "COUNT(\"loan\".\"XCL_034\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_034\") FROM loan AS T1 INNER JOIN account AS T2 ON T1.\"XCL_034\" = T2.\"XCL_001\" WHERE T2.\"XCL_003\" = 'POPLATEK TYDNE' AND T1.\"XCL_036\" < 200000",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_034\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "loan"
      },
      {
        "role": "r1",
        "physical_table": "account"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_034\") AS \"value\" FROM loan AS \"r0\" INNER JOIN account AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_001\" WHERE \"r1\".\"XCL_003\" = 'POPLATEK TYDNE' AND \"r0\".\"XCL_036\" < 200000",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:160"
  ]
}
```

### Account Attribute XCL_004

```json
{
  "kind": "binding",
  "formula": "\"account\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T1.\"XCL_004\" FROM account AS T1 INNER JOIN district AS T2 ON T1.\"XCL_002\" = T2.\"XCL_017\" WHERE T2.\"XCL_018\" = 'Prachatice'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_004\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "account"
      },
      {
        "role": "r1",
        "physical_table": "district"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_004\" AS \"value\" FROM account AS \"r0\" INNER JOIN district AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_017\" WHERE \"r1\".\"XCL_018\" = 'Prachatice'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:121"
  ]
}
```

### STRFTIME('%Y', "trans"."XCL_048") = '1998' AND "client"."XCL_009" = 617

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"trans\".\"XCL_048\") = '1998' AND \"client\".\"XCL_009\" = 617",
  "grain": [],
  "population_scope": "SELECT SUM(T3.\"XCL_051\") FROM client AS T1 INNER JOIN disp AS T4 ON T1.\"XCL_009\" = T4.\"XCL_014\" INNER JOIN account AS T2 ON T4.\"XCL_015\" = T2.\"XCL_001\" INNER JOIN trans AS T3 ON T2.\"XCL_001\" = T3.\"XCL_047\" WHERE STRFTIME('%Y', T3.\"XCL_048\") = '1998' AND T1.\"XCL_009\" = 617",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:179"
  ]
}
```

### Female client ID with active loan and card

```json
{
  "kind": "binding",
  "formula": "\"client\".\"XCL_009\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_009\" FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN account AS T5 ON T2.\"XCL_015\" = T5.\"XCL_001\" INNER JOIN loan AS T3 ON T5.\"XCL_001\" = T3.\"XCL_034\" INNER JOIN card AS T4 ON T2.\"XCL_013\" = T4.\"XCL_006\" WHERE T1.\"XCL_010\" = 'F'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_009\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "disp"
      },
      {
        "role": "r2",
        "physical_table": "account"
      },
      {
        "role": "r3",
        "physical_table": "loan"
      },
      {
        "role": "r4",
        "physical_table": "card"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_009\" AS \"value\" FROM client AS \"r0\" INNER JOIN disp AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_014\" INNER JOIN account AS \"r2\" ON \"r1\".\"XCL_015\" = \"r2\".\"XCL_001\" INNER JOIN loan AS \"r3\" ON \"r2\".\"XCL_001\" = \"r3\".\"XCL_034\" INNER JOIN card AS \"r4\" ON \"r1\".\"XCL_013\" = \"r4\".\"XCL_006\" WHERE \"r0\".\"XCL_010\" = 'F'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:146"
  ]
}
```

### Average Loan Amount for Male Clients

```json
{
  "kind": "metric",
  "formula": "AVG(\"loan\".\"XCL_036\")",
  "grain": [],
  "population_scope": "SELECT AVG(T4.\"XCL_036\") FROM client AS T1 INNER JOIN disp AS T2 ON T1.\"XCL_009\" = T2.\"XCL_014\" INNER JOIN account AS T3 ON T2.\"XCL_015\" = T3.\"XCL_001\" INNER JOIN loan AS T4 ON T3.\"XCL_001\" = T4.\"XCL_034\" WHERE T1.\"XCL_010\" = 'M'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r3\".\"XCL_036\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "client"
      },
      {
        "role": "r1",
        "physical_table": "disp"
      },
      {
        "role": "r2",
        "physical_table": "account"
      },
      {
        "role": "r3",
        "physical_table": "loan"
      }
    ],
    "scope_sql": "SELECT AVG(\"r3\".\"XCL_036\") AS \"value\" FROM client AS \"r0\" INNER JOIN disp AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_014\" INNER JOIN account AS \"r2\" ON \"r1\".\"XCL_015\" = \"r2\".\"XCL_001\" INNER JOIN loan AS \"r3\" ON \"r2\".\"XCL_001\" = \"r3\".\"XCL_034\" WHERE \"r0\".\"XCL_010\" = 'M'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:132"
  ]
}
```

### Account ID

```json
{
  "kind": "binding",
  "formula": "\"account\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_001\" FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" INNER JOIN disp AS T3 ON T2.\"XCL_001\" = T3.\"XCL_015\" WHERE T3.\"XCL_016\" = 'OWNER' AND T1.\"XCL_018\" = 'Tabor'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "district"
      },
      {
        "role": "r1",
        "physical_table": "account"
      },
      {
        "role": "r2",
        "physical_table": "disp"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_001\" AS \"value\" FROM district AS \"r0\" INNER JOIN account AS \"r1\" ON \"r0\".\"XCL_017\" = \"r1\".\"XCL_002\" INNER JOIN disp AS \"r2\" ON \"r1\".\"XCL_001\" = \"r2\".\"XCL_015\" WHERE \"r2\".\"XCL_016\" = 'OWNER' AND \"r0\".\"XCL_018\" = 'Tabor'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:148"
  ]
}
```

### "district"."XCL_018" = 'Jesenik'

```json
{
  "kind": "predicate",
  "formula": "\"district\".\"XCL_018\" = 'Jesenik'",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_001\") FROM district AS T1 INNER JOIN account AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE T1.\"XCL_018\" = 'Jesenik'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:166"
  ]
}
```


## Incremental maintenance events

- Recorded alias revision · card.XCL_007 · Archived superseded_alias_hypotheses → archived aliases
  - card.XCL_007: type → card_type
- Recorded alias revision · trans.XCL_049 · Archived superseded_alias_hypotheses → archived aliases
  - trans.XCL_049: transaction_type → transaction_direction
- Recorded alias revision · card.XCL_008 · Archived superseded_alias_hypotheses → archived aliases
  - card.XCL_008: issued → issued_date
