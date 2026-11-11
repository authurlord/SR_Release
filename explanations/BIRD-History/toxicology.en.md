# BIRD-History / toxicology — Schema and business semantics

The saved catalogue for this database contains 4 tables, 11 physical columns, 10 relationships and 145 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## atom

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: A, T, T1, T1b, T2, T3, T4, a, a1, a2, a_cl, a_h, a_n, a_p, a_s, ac, an, ao, ap

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| atom.XCL_001 | atom_id | unknown | bird_dev:243, bird_dev:242, bird_dev:285, bird_dev:295, bird_dev:207, bird_dev:322, bird_dev:271, bird_dev:249 |
| atom.XCL_002 | molecule_id | unknown | bird_dev:242, bird_dev:295, bird_dev:207, bird_dev:274, bird_dev:218, bird_dev:272, bird_dev:339, bird_dev:284 |
| atom.XCL_003 | element_symbol | unknown | bird_dev:243, bird_dev:285, bird_dev:295, bird_dev:207, bird_dev:274, bird_dev:322, bird_dev:271, bird_dev:218 |

## bond

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: B, T, T1, T2, T2b, T3, b, b2, b_double, b_triple, t, tb

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| bond.XCL_004 | bond_id | unknown | bird_dev:301, bird_dev:285, bird_dev:226, bird_dev:324, bird_dev:286, bird_dev:258, bird_dev:248, bird_dev:246 |
| bond.XCL_005 | molecule_id | unknown | bird_dev:226, bird_dev:207, bird_dev:332, bird_dev:232, bird_dev:272, bird_dev:284, bird_dev:262, bird_dev:248 |
| bond.XCL_006 | bond_type | unknown | bird_dev:301, bird_dev:226, bird_dev:324, bird_dev:207, bird_dev:286, bird_dev:332, bird_dev:232, bird_dev:272 |

## connected

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: T, T1, T2, T3, c, c1, c2, c_s

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| connected.XCL_007 | atom_id_1 | unknown | bird_dev:243, bird_dev:285, bird_dev:207, bird_dev:271, bird_dev:249, bird_dev:258, bird_dev:319, bird_dev:257 |
| connected.XCL_008 | atom_id_2 | unknown | bird_dev:271, bird_dev:257, bird_dev:248, bird_dev:236, bird_dev:320, bird_dev:321, bird_dev:216, bird_dev:305 |
| connected.XCL_009 | bond_id | unknown | bird_dev:243, bird_dev:285, bird_dev:271, bird_dev:249, bird_dev:258, bird_dev:319, bird_dev:248, bird_dev:246 |

## molecule

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: M, T, T0, T1, T2, T3, m, m2, mo, t

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| molecule.XCL_010 | molecule_id | unknown | bird_dev:242, bird_dev:227, bird_dev:295, bird_dev:289, bird_dev:232, bird_dev:218, bird_dev:272, bird_dev:339 |
| molecule.XCL_011 | carcinogenic_flag | unknown | bird_dev:242, bird_dev:227, bird_dev:295, bird_dev:289, bird_dev:232, bird_dev:218, bird_dev:272, bird_dev:339 |

## Relationships and join evidence

- atom.XCL_001 ↔ connected.XCL_007; target_disjoint_historical_join
- atom.XCL_002 ↔ bond.XCL_005; target_disjoint_historical_join
- atom.XCL_002 ↔ molecule.XCL_010; target_disjoint_historical_join
- bond.XCL_004 ↔ connected.XCL_009; target_disjoint_historical_join
- bond.XCL_005 ↔ molecule.XCL_010; target_disjoint_historical_join
- atom.XCL_001 ↔ connected.XCL_007; sql_workload_observed_join
- atom.XCL_002 ↔ bond.XCL_005; sql_workload_observed_join
- atom.XCL_002 ↔ molecule.XCL_010; sql_workload_observed_join
- bond.XCL_004 ↔ connected.XCL_009; sql_workload_observed_join
- bond.XCL_005 ↔ molecule.XCL_010; sql_workload_observed_join

## Business definitions, population and grain

### Query for hydrogen-positive molecule percentage

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(CASE WHEN T1.\"XCL_003\" = 'h' AND T2.\"XCL_011\" = '+' THEN T2.\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:298"
  ]
}
```

### A query that retrieves bond identifiers (XCL_004) from the bond table. It joins bond to molecule on XCL_005 = XCL_010 to filter for bonds belonging to

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_004\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+' AND T1.\"XCL_006\" = '='",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:294"
  ]
}
```

### Executes an inner join between atom and molecule tables on atom.XCL_002 = molecule.XCL_010. Filters for molecules where molecule.XCL_011 is '+'. Compu

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(DISTINCT CASE WHEN T1.\"XCL_003\" <> 'f' THEN T2.\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(DISTINCT T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:218"
  ]
}
```

### A program that identifies the single molecule with the highest number of double bonds among all molecules with a positive charge ('+'). It joins bond 

```json
{
  "kind": "program",
  "formula": "SELECT T.\"XCL_010\" FROM (SELECT T3.\"XCL_010\", COUNT(T1.\"XCL_006\") FROM bond AS T1 INNER JOIN molecule AS T3 ON T1.\"XCL_005\" = T3.\"XCL_010\" WHERE T3.\"XCL_011\" = '+' AND T1.\"XCL_006\" = '=' GROUP BY T3.\"XCL_010\" ORDER BY COUNT(T1.\"XCL_006\") DESC LIMIT 1) AS T",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:250"
  ]
}
```

### A SQL program that retrieves the top 5 distinct values of 'XCL_005' from the 'bond' table where 'XCL_006' is exactly '='. It uses DISTINCT to remove d

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T.\"XCL_005\" FROM bond AS T WHERE T.\"XCL_006\" = '=' ORDER BY T.\"XCL_005\" LIMIT 5",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:225"
  ]
}
```

### A full program that joins the atom, connected, and bond tables to identify atoms participating in single bonds (bond type '-'). It computes two condit

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT CASE WHEN T1.\"XCL_003\" = 'i' THEN T1.\"XCL_001\" ELSE NULL END) AS iodine_nums, COUNT(DISTINCT CASE WHEN T1.\"XCL_003\" = 's' THEN T1.\"XCL_001\" ELSE NULL END) AS sulfur_nums FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" INNER JOIN bond AS T3 ON T2.\"XCL_009\" = T3.\"XCL_004\" WHERE T3.\"XCL_006\" = '-'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:215"
  ]
}
```

### Atom count query for TR001

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T.\"XCL_001\") FROM atom AS T WHERE T.\"XCL_002\" = 'TR001'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:313"
  ]
}
```

### A program that identifies the molecule (XCL_011) linked to the bond (XCL_005) with the maximum number of double bonds ('=') in the bond table. It join

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_011\" FROM molecule AS T1 INNER JOIN (SELECT T.\"XCL_005\", COUNT(T.\"XCL_006\") FROM bond AS T WHERE T.\"XCL_006\" = '=' GROUP BY T.\"XCL_005\" ORDER BY COUNT(T.\"XCL_006\") DESC LIMIT 1) AS T2 ON T1.\"XCL_010\" = T2.\"XCL_005\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:244"
  ]
}
```

### A SQL program that computes the percentage of molecules in the 'molecule' table where 'XCL_011' is '+'. It uses a conditional count in the numerator a

```json
{
  "kind": "program",
  "formula": "SELECT ROUND(CAST(COUNT(CASE WHEN T.\"XCL_011\" = '+' THEN T.\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(T.\"XCL_010\"), 3) FROM molecule AS t",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:227"
  ]
}
```

### Full SQL program that joins connected and atom tables to retrieve atom.XCL_003 for a specific connection identifier (XCL_009 = 'TR001_10_11').

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_003\" FROM connected AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_007\" = T2.\"XCL_001\" WHERE T1.\"XCL_009\" = 'TR001_10_11'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:268"
  ]
}
```

### Executes an inner join between 'connected' and 'atom' tables on the atom identifier, filters for chlorine atoms ('cl'), and returns the count of conne

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_009\") FROM connected AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_007\" = T2.\"XCL_001\" WHERE T2.\"XCL_003\" = 'cl'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:308"
  ]
}
```

### A query that retrieves the molecule ID and its carcinogenic status for molecules containing a specific atom. It joins the 'atom' and 'molecule' tables

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_010\", IIF(T2.\"XCL_011\" = '+', 'YES', 'NO') AS flag_carcinogenic FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_001\" = 'TR001_10'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:237"
  ]
}
```

### Executes an inner join between the atom and molecule tables on the atom identifier (XCL_002) matching the molecule identifier (XCL_010). It applies fi

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_002\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'c' AND T2.\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:316"
  ]
}
```

### Chlorine-positive molecule ratio query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(CASE WHEN T2.\"XCL_011\" = '+' AND T1.\"XCL_003\" = 'cl' THEN T2.\"XCL_010\" ELSE NULL END) * 100 / COUNT(T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:317"
  ]
}
```

### A SQL program that joins the atom, molecule, and connected tables to retrieve distinct atom identifiers. It filters for molecules where the XCL_011 fi

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_001\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN connected AS T3 ON T1.\"XCL_001\" = T3.\"XCL_007\" WHERE T2.\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:211"
  ]
}
```

### Query for carbon percentage in double bonds

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(DISTINCT CASE WHEN T1.\"XCL_003\" = 'c' THEN T1.\"XCL_001\" ELSE NULL END) AS REAL) * 100 / COUNT(DISTINCT T1.\"XCL_001\") FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = '='",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:201"
  ]
}
```

### A SQL program that joins the 'atom' table with the 'connected' table on 'XCL_001' = 'XCL_007'. It filters for connections where 'XCL_009' equals 'TR00

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T2.\"XCL_009\" = 'TR004_8_9'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:206"
  ]
}
```

### A query that retrieves the 'XCL_003' value for atoms in the 'atom' table. It joins with the 'molecule' table on 'XCL_002' (atom) to 'XCL_010' (molecul

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_001\" = 'TR004_7' AND T2.\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:334"
  ]
}
```

### Atom-Bond Association for TR002

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_003\", T2.\"XCL_006\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_002\" = 'TR002'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:337"
  ]
}
```

### Executes a SQL query to count entries in the molecule table where the XCL_011 attribute is set to '-'. The result is a single row containing the count

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T.\"XCL_010\") FROM molecule AS T WHERE T.\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:241"
  ]
}
```

### Executes an inner join between the atom table (alias T1) and the connected table (alias T2) on atom.XCL_001 = connected.XCL_007. It filters the connec

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T1.\"XCL_003\") FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T2.\"XCL_009\" = 'TR001_3_4'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:319"
  ]
}
```

### Full SQL program that selects the count of XCL_010 from the molecule table (aliased as T) where the XCL_011 column is equal to the literal string '+'.

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T.\"XCL_010\") FROM molecule AS T WHERE T.\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:331",
    "bird_dev:291"
  ]
}
```

### A query that retrieves distinct bond identifiers by joining the atom, connected, and bond tables. It filters for atoms where XCL_003 equals 'sn' and f

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T3.\"XCL_006\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" INNER JOIN bond AS T3 ON T3.\"XCL_004\" = T2.\"XCL_009\" WHERE T1.\"XCL_003\" = 'sn'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:258"
  ]
}
```

### Executes a join between 'bond' and 'connected' tables to count connected entries for bond 'TR009' where the connected record's 'XCL_007' and 'XCL_008'

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_009\") FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T1.\"XCL_005\" = 'TR009' AND T2.\"XCL_007\" = T1.\"XCL_005\" || '_1' AND T2.\"XCL_008\" = T1.\"XCL_005\" || '_2'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:234"
  ]
}
```

### Bond-Connection Lookup for TR001_6_9

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_006\", T2.\"XCL_007\", T2.\"XCL_008\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T2.\"XCL_009\" = 'TR001_6_9'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:236"
  ]
}
```

### Full SQL program that joins atoms and molecules, filters for molecule ID 'TR006', deduplicates atom-molecule pairs, and calculates the ratio of hydrog

```json
{
  "kind": "program",
  "formula": "WITH SubQuery AS (SELECT DISTINCT T1.\"XCL_001\", T1.\"XCL_003\", T1.\"XCL_002\", T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_010\" = 'TR006') SELECT CAST(COUNT(CASE WHEN \"XCL_003\" = 'h' THEN \"XCL_001\" ELSE NULL END) AS REAL) / (CASE WHEN COUNT(\"XCL_001\") = 0 THEN NULL ELSE COUNT(\"XCL_001\") END) AS ratio, \"XCL_011\" FROM SubQuery GROUP BY \"XCL_011\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:282"
  ]
}
```

### A SQL program that computes the difference between the count of XCL_010 values where XCL_011 is '+' and the count where XCL_011 is '-', returning a si

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(CASE WHEN T.\"XCL_011\" = '+' THEN T.\"XCL_010\" ELSE NULL END) - COUNT(CASE WHEN T.\"XCL_011\" = '-' THEN T.\"XCL_010\" ELSE NULL END) AS diff_car_notcar FROM molecule AS t",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:222"
  ]
}
```

### Full SQL program that computes the percentage of chlorine atoms in molecules linked by single bonds (bond type '-'). Joins atom, molecule, and bond ta

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(CASE WHEN T.\"XCL_003\" = 'cl' THEN T.\"XCL_001\" ELSE NULL END) AS REAL) * 100 / COUNT(T.\"XCL_001\") FROM (SELECT T1.\"XCL_001\", T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '-') AS T",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:263"
  ]
}
```

### Executes an inner join between molecule (T1) and bond (T2) on molecule ID (XCL_010 = XCL_005). Filters for bonds with type '#' and molecules with attr

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T1.\"XCL_010\") FROM molecule AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_010\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = '#' AND T1.\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:336"
  ]
}
```

### A SQL program that joins the bond table (T1) with the molecule table (T2) on bond identifier XCL_005 matching molecule identifier XCL_010. It filters 

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_005\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '-' AND T1.\"XCL_006\" = '-'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:262"
  ]
}
```

### Atom XCL_003 Lookup

```json
{
  "kind": "program",
  "formula": "SELECT T.\"XCL_003\" FROM atom AS T WHERE T.\"XCL_001\" = 'TR000_1'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:322"
  ]
}
```

### A SQL program that joins the 'atom' table (T1) with the 'connected' table (T2) on 'XCL_001' = 'XCL_007'. It filters for connections where 'XCL_009' is

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T2.\"XCL_009\" = 'TR001_2_4'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:302"
  ]
}
```

### Executes a SELECT DISTINCT query on the 'bond' table to retrieve unique 'XCL_006' values where 'XCL_005' is 'TR000'. This program defines the specific

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T.\"XCL_006\" FROM bond AS T WHERE T.\"XCL_005\" = 'TR000'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:229"
  ]
}
```

### Query for XCL_003='h' percentage in TR206

```json
{
  "kind": "program",
  "formula": "SELECT ROUND(CAST(COUNT(CASE WHEN T.\"XCL_003\" = 'h' THEN T.\"XCL_001\" ELSE NULL END) AS REAL) * 100 / COUNT(T.\"XCL_001\"), 4) FROM atom AS T WHERE T.\"XCL_002\" = 'TR206'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:228"
  ]
}
```

### Query for Molecules with Specific Bond and Molecule Attributes

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_010\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '-' AND T2.\"XCL_011\" = '-' ORDER BY T2.\"XCL_010\" LIMIT 3",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:232"
  ]
}
```

### Bond Lookup by XCL_004

```json
{
  "kind": "program",
  "formula": "SELECT T.\"XCL_006\" FROM bond AS T WHERE T.\"XCL_004\" = 'TR007_4_19'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:301"
  ]
}
```

### Computes aggregate statistics for molecules linked to double bonds. It joins the bond table to the molecule table on the bond's molecule reference (XC

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T2.\"XCL_010\"), SUM(CASE WHEN T2.\"XCL_011\" = '+' THEN 1 ELSE 0 END) FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '='",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:310"
  ]
}
```

### A program that identifies the molecule with the highest number of hydrogen atoms. It joins the atom and molecule tables, filters for hydrogen atoms, g

```json
{
  "kind": "program",
  "formula": "SELECT T.\"XCL_011\" FROM (SELECT T2.\"XCL_011\", COUNT(T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'h' GROUP BY T2.\"XCL_011\" ORDER BY COUNT(T2.\"XCL_010\") DESC LIMIT 1) AS t",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:208"
  ]
}
```

### A SQL program that selects distinct 'XCL_003' entries from the 'atom' table where 'XCL_002' is 'TR001'. It serves as a reusable filter-and-distinct pa

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T.\"XCL_003\" FROM atom AS T WHERE T.\"XCL_002\" = 'TR001'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:274"
  ]
}
```

### A full SQL program that identifies connection IDs (XCL_009) in the 'connected' table. It joins 'atom' and 'connected' to find connections where one en

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_009\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T2.\"XCL_009\" IN (SELECT T3.\"XCL_009\" FROM connected AS T3 INNER JOIN atom AS T4 ON T3.\"XCL_007\" = T4.\"XCL_001\" WHERE T4.\"XCL_003\" = 'p') AND T1.\"XCL_003\" = 'n'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:243"
  ]
}
```

### Atom Non-Br Distinct Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T.\"XCL_001\") FROM atom AS T WHERE T.\"XCL_003\" <> 'br'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:203"
  ]
}
```

### Get Connections for Atom TR181

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_007\", T2.\"XCL_008\" FROM atom AS T1 INNER JOIN connected AS T2 ON T2.\"XCL_007\" = T1.\"XCL_001\" WHERE T1.\"XCL_002\" = 'TR181'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:217"
  ]
}
```

### Full SQL program that joins the atom table (T1) with the molecule table (T2) on the foreign key relationship XCL_002 = XCL_010. It filters for molecul

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_001\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:293"
  ]
}
```

### Full SQL program joining atom, molecule, and bond tables. It filters for atoms of type 'p' or 'br' that belong to molecules containing a triple bond (

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_001\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '#' AND T1.\"XCL_003\" IN ('p', 'br')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:260"
  ]
}
```

### A SQL program that selects distinct 'XCL_003' entries from the 'atom' table where 'XCL_002' is 'TR004'. It serves as a reusable filter-and-distinct pa

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T.\"XCL_003\" FROM atom AS T WHERE T.\"XCL_002\" = 'TR004'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:240"
  ]
}
```

### A query that selects XCL_001 from the atom table, restricted to records where XCL_002 falls within the range 'TR010' to 'TR050' and XCL_003 is 'c'.

```json
{
  "kind": "program",
  "formula": "SELECT T.\"XCL_001\" FROM atom AS T WHERE T.\"XCL_002\" BETWEEN 'TR010' AND 'TR050' AND T.\"XCL_003\" = 'c'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:292"
  ]
}
```

### Full SQL program that identifies distinct atom.XCL_003 values by excluding those present in the connected atom subset. The logic uses a NOT IN subquer

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T.\"XCL_003\" FROM atom AS T WHERE NOT T.\"XCL_003\" IN (SELECT DISTINCT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\")",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:247"
  ]
}
```

### Full SQL program joining atom, molecule, and bond tables. It filters for bonds with type '#' (triple bond) and computes the percentage of distinct mol

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(DISTINCT CASE WHEN T2.\"XCL_011\" = '+' THEN T2.\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(DISTINCT T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '#'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:219"
  ]
}
```

### A SQL program that retrieves distinct atom identifiers (XCL_003) by joining the bond, connected, and atom tables. It filters for bonds where XCL_006 i

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T3.\"XCL_003\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" INNER JOIN atom AS T3 ON T2.\"XCL_007\" = T3.\"XCL_001\" WHERE T1.\"XCL_006\" = '#'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:253"
  ]
}
```

### A query that joins the atom and molecule tables to identify molecules. It filters for molecules with a positive charge and ensures they contain atoms 

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_010\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE SUBSTRING(T1.\"XCL_001\", -2) BETWEEN '21' AND '25' AND T2.\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:242"
  ]
}
```

### A query that retrieves specific attributes (XCL_010, XCL_011) from the molecule table, limited to rows where the identifier XCL_010 is one of 'TR000',

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_010\", T.\"XCL_011\" FROM molecule AS T WHERE T.\"XCL_010\" IN ('TR000', 'TR001', 'TR002')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:264"
  ]
}
```

### Query for Negative Molecules with Carbon Triple Bonds

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_010\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '#' AND T1.\"XCL_003\" = 'c' AND T2.\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:272"
  ]
}
```

### Full SQL program that selects the count of 'XCL_001' from the 'atom' table, applying a filter on 'XCL_003' to include only values 'c' or 'h'. This pro

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T.\"XCL_001\") FROM atom AS T WHERE T.\"XCL_003\" = 'c' OR T.\"XCL_003\" = 'h'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:256"
  ]
}
```

### Executes a count aggregation on the atom table (aliased as T) with specific equality filters on columns XCL_002 and XCL_003. The program defines the f

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T.\"XCL_001\") FROM atom AS T WHERE T.\"XCL_002\" = 'TR008' AND T.\"XCL_003\" = 'c'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:333"
  ]
}
```

### A query that retrieves bond identifiers (XCL_006) by joining the bond table with the connected table on XCL_004 = XCL_009. It filters the connected ta

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_006\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T2.\"XCL_007\" = 'TR000_1' AND T2.\"XCL_008\" = 'TR000_2'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:320"
  ]
}
```

### A query that joins the 'atom' table with the 'connected' table on 'XCL_001' = 'XCL_007'. It filters for connections where 'XCL_009' equals 'TR001_1_7'

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_002\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T2.\"XCL_009\" = 'TR001_1_7'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:318"
  ]
}
```

### A full program that joins the 'atom' and 'bond' tables on the condition that the atom's 'XCL_002' matches the bond's 'XCL_005'. It filters for atoms w

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_006\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_003\" = 'c'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:284"
  ]
}
```

### Executes a join between atom (T1) and bond (T2) on XCL_002 = XCL_005, applies filters T1.XCL_003 <> 's' and T2.XCL_006 <> '=', and computes the count 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T1.\"XCL_002\") FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_003\" <> 's' AND T2.\"XCL_006\" <> '='",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:311"
  ]
}
```

### A query that joins the bond table with the connected table on XCL_004 = XCL_009, filtering for connections where XCL_007 is 'TR000_2' and XCL_008 is '

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_005\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T2.\"XCL_007\" = 'TR000_2' AND T2.\"XCL_008\" = 'TR000_4'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:321"
  ]
}
```

### A SQL program that joins the atom table (T1) with the bond table (T2) on atom ID (XCL_002 = XCL_005). It filters for bonds where XCL_006 is '=' and at

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T1.\"XCL_002\") FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = '=' AND T1.\"XCL_003\" = 'o'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:335"
  ]
}
```

### A query that retrieves atom identifiers ('XCL_003') by joining the 'atom', 'connected', and 'bond' tables. It filters results to include only atoms as

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" INNER JOIN bond AS T3 ON T2.\"XCL_009\" = T3.\"XCL_004\" WHERE T3.\"XCL_004\" = 'TR001_10_11'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:285"
  ]
}
```

### Executes a query on the 'atom' table to retrieve the first 3 distinct 'XCL_003' values associated with the 'XCL_002' value 'TR000', ordered ascending 

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T.\"XCL_003\" FROM atom AS T WHERE T.\"XCL_002\" = 'TR000' ORDER BY T.\"XCL_003\" LIMIT 3",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:220"
  ]
}
```

### A query that joins the 'bond' and 'molecule' tables on 'XCL_005' = 'XCL_010'. It filters for molecules where 'XCL_011' is '+' and selects the distinct

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_004\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:261"
  ]
}
```

### Query XCL_009 for TR000_2

```json
{
  "kind": "program",
  "formula": "SELECT T.\"XCL_009\" FROM connected AS T WHERE T.\"XCL_008\" = 'TR000_2'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:224"
  ]
}
```

### A query that joins the atom and bond tables on the atom's reference field (XCL_002) matching the bond's XCL_005 field. It filters for atoms where XCL_

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\", COUNT(DISTINCT T2.\"XCL_006\"), T1.\"XCL_002\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_002\" = 'TR000' GROUP BY T1.\"XCL_001\", T2.\"XCL_006\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:309"
  ]
}
```

### A query that retrieves bond identifiers (XCL_006) by joining the bond table with the connected table on XCL_004 = XCL_009. It filters for connections 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_006\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T2.\"XCL_007\" = 'TR004_8' AND T2.\"XCL_008\" = 'TR004_20' OR T2.\"XCL_008\" = 'TR004_8' AND T2.\"XCL_007\" = 'TR004_20'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:213"
  ]
}
```

### Chlorine Percentage Query for Positive Molecules

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(CASE WHEN T1.\"XCL_003\" = 'cl' THEN T1.\"XCL_003\" ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_003\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:273"
  ]
}
```

### A program that identifies molecules with a negative charge (XCL_011 = '-') and more than 5 associated atoms. It joins the molecule and atom tables, fi

```json
{
  "kind": "program",
  "formula": "SELECT T.\"XCL_010\" FROM (SELECT T1.\"XCL_010\", COUNT(T2.\"XCL_001\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" WHERE T1.\"XCL_011\" = '-' GROUP BY T1.\"XCL_010\" HAVING COUNT(T2.\"XCL_001\") > 5) AS t",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:327"
  ]
}
```

### Bond Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T.\"XCL_005\") FROM bond AS T WHERE T.\"XCL_005\" BETWEEN 'TR004' AND 'TR010' AND T.\"XCL_006\" = '-'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:332"
  ]
}
```

### Query Molecule XCL_011 by XCL_010

```json
{
  "kind": "program",
  "formula": "SELECT T.\"XCL_011\" FROM molecule AS T WHERE T.\"XCL_010\" = 'TR151'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:289"
  ]
}
```

### A distinct list of atom identifiers (XCL_005) and their corresponding property values (XCL_003) for bonds where the bond property XCL_006 is '#'. Join

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_005\", T2.\"XCL_003\" FROM bond AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_005\" = T2.\"XCL_002\" WHERE T1.\"XCL_006\" = '#'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:306"
  ]
}
```

### Lead Connections Query

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_007\", T2.\"XCL_008\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T1.\"XCL_003\" = 'pb'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:252"
  ]
}
```

### Query Molecule XCL_011 by XCL_010

```json
{
  "kind": "program",
  "formula": "SELECT T.\"XCL_011\" FROM molecule AS T WHERE T.\"XCL_010\" = 'TR124'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:299"
  ]
}
```

### Executes an inner join between the molecule table (T1) and the atom table (T2) on the molecule identifier (XCL_010 = XCL_002). It filters for molecule

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T1.\"XCL_010\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'n' AND T1.\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:325"
  ]
}
```

### A query that joins the 'atom' and 'connected' tables on 'XCL_001' = 'XCL_007', filters for atoms where 'XCL_002' equals 'TR006', and returns the first

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_009\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T1.\"XCL_002\" = 'TR006' ORDER BY T2.\"XCL_009\" LIMIT 2",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:233"
  ]
}
```

### A program that identifies the XCL_006 value with the highest frequency of XCL_004 occurrences in the bond table by grouping, counting, sorting descend

```json
{
  "kind": "program",
  "formula": "SELECT T.\"XCL_006\" FROM (SELECT \"XCL_006\", COUNT(\"XCL_004\") FROM bond GROUP BY \"XCL_006\" ORDER BY COUNT(\"XCL_004\") DESC LIMIT 1) AS T",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:195"
  ]
}
```

### A query that retrieves distinct pairs of atom identifiers and molecule identifiers. It joins the 'atom' table to the 'molecule' table on the foreign k

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_003\", T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_010\" = 'TR060'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:230"
  ]
}
```

### A query that retrieves the atom identifier ('XCL_003') from the 'atom' table by joining it with the 'connected' table on the atom ID ('XCL_001' = 'XCL

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_003\" FROM connected AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_007\" = T2.\"XCL_001\" WHERE T1.\"XCL_009\" = 'TR144_8_19'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:249"
  ]
}
```

### A two-stage computation that first counts oxygen atoms connected by single bonds for each atom identifier, then calculates the average of these counts

```json
{
  "kind": "program",
  "formula": "SELECT AVG(\"oxygen_count\") FROM (SELECT T1.\"XCL_002\", COUNT(T1.\"XCL_003\") AS oxygen_count FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = '-' AND T1.\"XCL_003\" = 'o' GROUP BY T1.\"XCL_002\") AS oxygen_counts",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:197"
  ]
}
```

### A query that retrieves the 'XCL_011' flag from the 'molecule' table for molecules containing at least one atom where 'XCL_003' is 'ca'. It joins 'atom

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_011\" AS flag_carcinogenic FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'ca'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:283"
  ]
}
```

### Full SQL program that selects XCL_001 from atom filtered by XCL_002 = 'TR186'. Preserves the filter and output column for reuse.

```json
{
  "kind": "program",
  "formula": "SELECT T.\"XCL_001\" FROM atom AS T WHERE T.\"XCL_002\" = 'TR186'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:300"
  ]
}
```

### Full SQL program that filters the molecule table for records with XCL_010 between 'TR000' and 'TR099' and XCL_011 equal to '+', then counts the matchi

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T.\"XCL_010\") FROM molecule AS T WHERE \"XCL_010\" BETWEEN 'TR000' AND 'TR099' AND T.\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:204"
  ]
}
```

### Query for Sulfur Atoms in Double Bonds

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_002\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_003\" = 's' AND T2.\"XCL_006\" = '='",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:326"
  ]
}
```

### A query that retrieves unique 'XCL_008' identifiers from the 'connected' table by joining it with the 'atom' table on 'XCL_001' = 'XCL_007', filtered 

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_008\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T1.\"XCL_003\" = 's'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:257"
  ]
}
```

### A query that identifies the single molecule with the most calcium atoms. It joins the 'atom' table to the 'molecule' table on the molecule ID, filters

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'ca' GROUP BY T2.\"XCL_011\" ORDER BY COUNT(T2.\"XCL_011\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:270"
  ]
}
```

### Bond-Molecule Join Query

```json
{
  "kind": "program",
  "formula": "SELECT ROUND(CAST(COUNT(CASE WHEN T2.\"XCL_011\" = '+' THEN T1.\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_004\"), 5) FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '-'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:255"
  ]
}
```

### A query that retrieves the molecule identifier ('XCL_011') for a specific bond. It joins the 'bond' table (T1) with the 'molecule' table (T2) on the b

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_011\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_004\" = 'TR001_10_11'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:279"
  ]
}
```

### A program that identifies the most common atom type in molecules marked as positive. It joins molecule and atom tables, filters for positive molecules

```json
{
  "kind": "program",
  "formula": "SELECT T.\"XCL_003\" FROM (SELECT T2.\"XCL_003\", COUNT(DISTINCT T2.\"XCL_002\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" WHERE T1.\"XCL_011\" = '+' GROUP BY T2.\"XCL_003\" ORDER BY COUNT(DISTINCT T2.\"XCL_002\") LIMIT 1) AS t",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:251"
  ]
}
```

### A query that joins the atom and connected tables on XCL_001 = XCL_007 to retrieve atom identifiers (XCL_003) for connections where the XCL_009 attribu

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T2.\"XCL_009\" = 'TR000_1_2'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:277"
  ]
}
```

### A program that identifies the XCL_006 value with the highest frequency of XCL_005='TR010' in the bond table. It filters for 'TR010', groups by XCL_006

```json
{
  "kind": "program",
  "formula": "SELECT T.\"XCL_006\" FROM (SELECT T1.\"XCL_006\", COUNT(T1.\"XCL_005\") FROM bond AS T1 WHERE T1.\"XCL_005\" = 'TR010' GROUP BY T1.\"XCL_006\" ORDER BY COUNT(T1.\"XCL_005\") DESC LIMIT 1) AS T",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:231"
  ]
}
```

### A SQL program that computes the percentage of bond records where 'XCL_006' is '-'. It uses a single table scan of 'bond' with alias 't', applying a co

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(CASE WHEN T.\"XCL_006\" = '-' THEN T.\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(T.\"XCL_004\") FROM bond AS t",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:324"
  ]
}
```

### A query that retrieves atom identifiers (XCL_001) from the atom table. It joins atom to molecule on XCL_002 = XCL_010, filters for atoms where XCL_003

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'c' AND T2.\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:297"
  ]
}
```

### A query that retrieves bond identifiers (XCL_005) and attributes (XCL_006) from the 'bond' table. It joins with the 'molecule' table on the condition 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_005\", T2.\"XCL_006\" FROM molecule AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_010\" = T2.\"XCL_005\" WHERE T1.\"XCL_010\" BETWEEN 'TR000' AND 'TR050'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:267"
  ]
}
```

### Executes a SELECT DISTINCT query on the 'atom' table to retrieve unique 'XCL_003' entries filtered by the condition 'XCL_002' = 'TR151'.

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T.\"XCL_003\" FROM atom AS T WHERE T.\"XCL_002\" = 'TR151'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:290"
  ]
}
```

### A SQL program that joins the atom table with the molecule table to retrieve identifiers of oxygen atoms located within positively charged molecules. I

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'o' AND T2.\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:339"
  ]
}
```

### A query that identifies unique molecules by joining the atom, molecule, and bond tables. It filters for bonds where the bond attribute (XCL_004) equal

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_004\" = 'TR001_2_4'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:312"
  ]
}
```

### Full SQL program that selects the count of XCL_004 from the bond table (aliased as T) where XCL_006 is '#'. Serves as the executable unit for retrievi

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T.\"XCL_004\") FROM bond AS T WHERE T.\"XCL_006\" = '#'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:202"
  ]
}
```

### A program that identifies the molecule with the highest number of associated atoms, specifically filtering for molecules where the attribute XCL_011 e

```json
{
  "kind": "program",
  "formula": "SELECT T.\"XCL_010\" FROM (SELECT T2.\"XCL_010\", COUNT(T1.\"XCL_001\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+' GROUP BY T2.\"XCL_010\" ORDER BY COUNT(T1.\"XCL_001\") DESC LIMIT 1) AS t",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:329"
  ]
}
```

### A query that retrieves XCL_007 from the connected table for the specific record identified by XCL_009 = 'TR000_2_5'.

```json
{
  "kind": "program",
  "formula": "SELECT T.\"XCL_007\" FROM connected AS T WHERE T.\"XCL_009\" = 'TR000_2_5'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:223"
  ]
}
```

### Full SQL program that joins the atom table (T1) to the molecule table (T2) on the molecule identifier (XCL_002 = XCL_010). It filters for atoms of typ

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'na' AND T2.\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:199"
  ]
}
```

### Retrieves the constituent atom identifiers for a specific bond defined by bond type 'TR001' and bond ID 'TR001_2_6'. Returns one row containing the de

```json
{
  "kind": "program",
  "formula": "SELECT SUBSTRING(T.\"XCL_004\", 1, 7) AS atom_id1, T.\"XCL_005\" || SUBSTRING(T.\"XCL_004\", 8, 2) AS atom_id2 FROM bond AS T WHERE T.\"XCL_005\" = 'TR001' AND T.\"XCL_004\" = 'TR001_2_6'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:221"
  ]
}
```

### A two-stage computation that first counts single bonds for each positive molecule and then averages those counts across all such molecules. It filters

```json
{
  "kind": "program",
  "formula": "SELECT AVG(\"single_bond_count\") FROM (SELECT T3.\"XCL_010\", COUNT(T1.\"XCL_006\") AS single_bond_count FROM bond AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_005\" = T2.\"XCL_002\" INNER JOIN molecule AS T3 ON T3.\"XCL_010\" = T2.\"XCL_002\" WHERE T1.\"XCL_006\" = '-' AND T3.\"XCL_011\" = '+' GROUP BY T3.\"XCL_010\") AS subquery",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:198"
  ]
}
```

### A query that retrieves distinct pairs of bond identifiers (XCL_004) and molecule identifiers (XCL_011) where the bond is associated with a molecule vi

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_004\", T2.\"XCL_011\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '#'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:280"
  ]
}
```

### Full SQL program that joins the atom table (T1) to the molecule table (T2) on the molecule identifier (XCL_002 = XCL_010). It filters for molecules wi

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+' AND T1.\"XCL_003\" = 'br'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:235"
  ]
}
```

### Full SQL program that joins molecule and atom tables on molecule ID, filters for chlorine atoms and negative molecular charge, and returns the distinc

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T1.\"XCL_010\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'cl' AND T1.\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:196"
  ]
}
```

### A query that joins the bond table with the connected table on XCL_004 = XCL_009, filters for rows where the 7th and 8th characters of connected.XCL_00

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_006\", T1.\"XCL_004\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE SUBSTRING(T2.\"XCL_007\", 7, 2) = '45'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:246"
  ]
}
```

### A SQL program that computes the percentage of bond records where 'XCL_006' is '#', using 'XCL_004' as the count basis. It operates on the 'bond' table

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(CASE WHEN T.\"XCL_006\" = '#' THEN T.\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(T.\"XCL_004\") FROM bond AS T",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:286"
  ]
}
```

### Calculates the percentage of total connections that belong to the most heavily connected bond group. It divides the maximum group connection count by 

```json
{
  "kind": "program",
  "formula": "SELECT CAST((SELECT COUNT(T1.\"XCL_007\") FROM connected AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_009\" = T2.\"XCL_004\" GROUP BY T2.\"XCL_006\" ORDER BY COUNT(T2.\"XCL_004\") DESC LIMIT 1) AS REAL) * 100 / (SELECT COUNT(\"XCL_007\") FROM connected)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:254"
  ]
}
```

### A query that retrieves the atom ID (XCL_007) and bond ID (XCL_008) from the 'connected' table for connections specifically linked to bond 'TR041' of t

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_007\", T2.\"XCL_008\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" INNER JOIN bond AS T3 ON T2.\"XCL_009\" = T3.\"XCL_004\" WHERE T3.\"XCL_006\" = '#' AND T3.\"XCL_005\" = 'TR041'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:248"
  ]
}
```

### A program that retrieves atom identifiers from the 'atom' table by joining with 'molecule' and 'bond' tables. It filters for a specific molecule ID ('

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T2.\"XCL_010\" = 'TR012' AND T3.\"XCL_006\" = '=' AND T1.\"XCL_003\" = 'c'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:338"
  ]
}
```

### Full SQL program that joins the bond table to the molecule table on the molecule ID, filters for bonds where XCL_006 is '#' and molecules where XCL_01

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_010\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '#' AND T2.\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:200"
  ]
}
```

### Full SQL program that selects the count of XCL_009 from the 'connected' table (aliased as T) where the substring of XCL_007 starting from the last 2 c

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T.\"XCL_009\") FROM connected AS T WHERE SUBSTRING(T.\"XCL_007\", -2) = '19'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:239"
  ]
}
```

### Full SQL program that joins the atom and bond tables on the atom identifier (XCL_002 = XCL_005), filters for atom ID 'TR024' and bond type '=', and se

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_002\" = 'TR024' AND T2.\"XCL_006\" = '='",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:328"
  ]
}
```

### A program that identifies the atom type (XCL_003) appearing in the fewest distinct molecules (XCL_002) where the molecule is labeled as negative (XCL_

```json
{
  "kind": "program",
  "formula": "SELECT T.\"XCL_003\" FROM (SELECT T1.\"XCL_003\", COUNT(DISTINCT T1.\"XCL_002\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '-' GROUP BY T1.\"XCL_003\" ORDER BY COUNT(DISTINCT T1.\"XCL_002\") ASC LIMIT 1) AS t",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:212"
  ]
}
```

### A SQL program that joins atom, molecule, and bond tables to filter for molecules with single bonds and counts the distinct atoms associated with those

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T.\"XCL_003\") FROM (SELECT DISTINCT T2.\"XCL_010\", T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '-') AS T",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:259"
  ]
}
```

### Full SQL program that joins bond and molecule tables on XCL_005 = XCL_010, filters for double bonds (XCL_006 = '=') and molecule ID 'TR006', then coun

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_004\"), T2.\"XCL_011\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '=' AND T2.\"XCL_010\" = 'TR006' GROUP BY T2.\"XCL_011\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:303"
  ]
}
```

### Executes a join between the bond and molecule tables on bond.XCL_005 = molecule.XCL_010. Filters for bonds where XCL_006 = '-' and molecules where XCL

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T2.\"XCL_010\") FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '-' AND T1.\"XCL_006\" = '-'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:278"
  ]
}
```

### A program that retrieves distinct bond identifiers from the 'bond' table where the bond is linked via the 'connected' table to an 'atom' with element 

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_006\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" INNER JOIN atom AS T3 ON T2.\"XCL_007\" = T3.\"XCL_001\" WHERE T3.\"XCL_003\" = 'cl'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:209"
  ]
}
```

### A SQL program that joins 'atom', 'bond', and 'connected' tables. It filters for bonds where 'XCL_006' equals '=' (indicating a double bond or specific

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" INNER JOIN connected AS T3 ON T1.\"XCL_001\" = T3.\"XCL_007\" WHERE T2.\"XCL_006\" = '='",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:207"
  ]
}
```

### Executes a filtered count on the 'molecule' table. Filters rows where 'XCL_010' is within the range ['TR000', 'TR030'] and 'XCL_011' equals '+'. The o

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T.\"XCL_010\") FROM molecule AS T WHERE T.\"XCL_010\" BETWEEN 'TR000' AND 'TR030' AND T.\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:266"
  ]
}
```

### Executes an inner join between the atom and molecule tables on the foreign key relationship (XCL_002 to XCL_010). It applies filters for positive mole

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+' AND SUBSTRING(T1.\"XCL_001\", -1) = '4' AND LENGTH(T1.\"XCL_001\") = 7",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:281"
  ]
}
```

### Full SQL program that selects XCL_002 from the atom table where XCL_003 is 'c'. This represents a filtered projection of atom data.

```json
{
  "kind": "program",
  "formula": "SELECT T.\"XCL_002\" FROM atom AS T WHERE T.\"XCL_003\" = 'c'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:205"
  ]
}
```

### Bond-Connected Join Filter

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_007\", T2.\"XCL_008\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T1.\"XCL_006\" = '-'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:210"
  ]
}
```

### Atom-Connected Ratio Query

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(T2.\"XCL_009\") AS REAL) / COUNT(T1.\"XCL_001\") FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T1.\"XCL_003\" = 'i'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:245"
  ]
}
```

### A query that retrieves distinct pairs of molecule identifiers and atom properties for atoms belonging to molecules with a positive charge. It joins th

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_010\", T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:304"
  ]
}
```

### Bond-Connection Lookup

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_004\", T2.\"XCL_007\", T2.\"XCL_008\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T1.\"XCL_006\" = '-'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:305"
  ]
}
```

### A SQL program that selects the 'XCL_011' field from the 'molecule' table, restricted to rows where 'XCL_010' equals 'TR000'.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_011\" FROM molecule AS T WHERE T.\"XCL_010\" = 'TR000'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:323"
  ]
}
```

### A query that retrieves the atom type for a specific connection ('TR001_1_8') by joining the 'connected' and 'atom' tables. It filters for connections 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_009\", T2.\"XCL_008\", T1.\"XCL_003\" AS flag_have_CaCl FROM atom AS T1 INNER JOIN connected AS T2 ON T2.\"XCL_007\" = T1.\"XCL_001\" WHERE T2.\"XCL_009\" = 'TR001_1_8' AND (T1.\"XCL_003\" = 'c1' OR T1.\"XCL_003\" = 'c')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:271"
  ]
}
```

### A query that retrieves the atom identifier ('XCL_003') for atoms linked to a specific connection record. It joins the 'connected' table (alias T1) wit

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_003\" FROM connected AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_007\" = T2.\"XCL_001\" WHERE T1.\"XCL_009\" = 'TR000_2_3'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:307"
  ]
}
```

### A SQL program that calculates the distinct count of XCL_005 from the bond table. It applies a filter on XCL_006 to include only records where the valu

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T.\"XCL_005\") FROM bond AS T WHERE T.\"XCL_006\" = '#'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:238"
  ]
}
```

### Filtered Bond-Connected Join

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_007\", T2.\"XCL_008\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T1.\"XCL_006\" = '#'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:216",
    "bird_dev:276"
  ]
}
```

### Bond percentage calculation for TR047

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(CASE WHEN T.\"XCL_006\" = '=' THEN T.\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(T.\"XCL_004\") FROM bond AS T WHERE T.\"XCL_005\" = 'TR047'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:287"
  ]
}
```

### A query that identifies unique molecules associated with atoms that do not have the value 'sn' in column XCL_003. It joins the atom table to the molec

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" <> 'sn'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:214"
  ]
}
```

### Query for bond count in inorganic molecules

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T3.\"XCL_004\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T1.\"XCL_003\" = 'i'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:269"
  ]
}
```

### Molecule Filter Query

```json
{
  "kind": "program",
  "formula": "SELECT T.\"XCL_010\" FROM molecule AS T WHERE T.\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:265"
  ]
}
```

### Bond count query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T.\"XCL_004\") FROM bond AS T WHERE T.\"XCL_006\" = '-'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:314"
  ]
}
```

### A SQL program that selects distinct 'XCL_005' entries from the 'bond' table, applying a filter condition where 'XCL_006' is exactly equal to '='. This

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T.\"XCL_005\" FROM bond AS T WHERE T.\"XCL_006\" = '='",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:275"
  ]
}
```

### Bond-Connection Lookup

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_005\", T2.\"XCL_004\", T1.\"XCL_007\" FROM connected AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_009\" = T2.\"XCL_004\" WHERE T1.\"XCL_007\" = 'TR000_1' AND T2.\"XCL_004\" = 'TR000_1_2'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:296"
  ]
}
```

### Bond XCL_006 equality rate query for TR008

```json
{
  "kind": "program",
  "formula": "SELECT ROUND(CAST(COUNT(CASE WHEN T.\"XCL_006\" = '=' THEN T.\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(T.\"XCL_004\"), 5) FROM bond AS T WHERE T.\"XCL_005\" = 'TR008'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:226"
  ]
}
```

### Chlorine Atoms in Cationic Molecules Query

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_002\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'cl' AND T2.\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:315"
  ]
}
```

### Full SQL program joining atom and molecule tables. Filters for molecules with charge '+' and atoms of type 'h', then counts the resulting atom records

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_001\") AS atomnums_h FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+' AND T1.\"XCL_003\" = 'h'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:295"
  ]
}
```

### A query that joins the 'atom' and 'molecule' tables to retrieve the 'XCL_011' property of a molecule. It filters for atoms where 'XCL_001' equals 'TR0

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_011\" AS flag_carcinogenic FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_001\" = 'TR001_1'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:288"
  ]
}
```

### Full SQL program joining molecule, atom, and bond tables. It filters for bonds with type '#' (triple) and atoms with type 'h' (hydrogen), then compute

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN T1.\"XCL_011\" = '+' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(DISTINCT T1.\"XCL_010\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" INNER JOIN bond AS T3 ON T1.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '#' AND T2.\"XCL_003\" = 'h'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:330"
  ]
}
```

### Atom Identifier

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_001\", T1.\"XCL_003\", T1.\"XCL_002\", T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_010\" = 'TR006'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:282"
  ]
}
```

### Molecule Identifier

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_010\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_010\", T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:304"
  ]
}
```

### "atom"."XCL_002" = 'TR151'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_002\" = 'TR151'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T.\"XCL_003\" FROM atom AS T WHERE T.\"XCL_002\" = 'TR151'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:290"
  ]
}
```

### Connection Attribute

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_009\", T2.\"XCL_008\", T1.\"XCL_003\" AS flag_have_CaCl FROM atom AS T1 INNER JOIN connected AS T2 ON T2.\"XCL_007\" = T1.\"XCL_001\" WHERE T2.\"XCL_009\" = 'TR001_1_8' AND (T1.\"XCL_003\" = 'c1' OR T1.\"XCL_003\" = 'c')",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_008\" AS \"value\" FROM atom AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r1\".\"XCL_007\" = \"r0\".\"XCL_001\" WHERE \"r1\".\"XCL_009\" = 'TR001_1_8' AND (\"r0\".\"XCL_003\" = 'c1' OR \"r0\".\"XCL_003\" = 'c')",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:271"
  ]
}
```

### The single value of XCL_006 that has the maximum count of associated XCL_004 records in the bond table.

```json
{
  "kind": "binding",
  "formula": "T.\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_006\" FROM (SELECT \"XCL_006\", COUNT(\"XCL_004\") FROM bond GROUP BY \"XCL_006\" ORDER BY COUNT(\"XCL_004\") DESC LIMIT 1) AS T",
  "upstream_scopes": [
    "SELECT \"XCL_006\", COUNT(\"XCL_004\") FROM bond GROUP BY \"XCL_006\" ORDER BY COUNT(\"XCL_004\") DESC LIMIT 1"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:195"
  ]
}
```

### Connected Entity Identifier

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_008\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T1.\"XCL_003\" = 's'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:257"
  ]
}
```

### Percentage of atoms of type 'cl' among all atoms connected via a bond of type '-'. Calculated as (count of atoms where XCL_003='cl' / total count of a

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN \"atom\".\"XCL_003\" = 'cl' THEN \"atom\".\"XCL_001\" ELSE NULL END) AS REAL) * 100 / COUNT(\"atom\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T.\"XCL_003\" = 'cl' THEN T.\"XCL_001\" ELSE NULL END) AS REAL) * 100 / COUNT(T.\"XCL_001\") FROM (SELECT T1.\"XCL_001\", T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '-') AS T",
  "upstream_scopes": [
    "SELECT T1.\"XCL_001\", T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '-'"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:263"
  ]
}
```

### Count of XCL_004 per XCL_006

```json
{
  "kind": "metric",
  "formula": "COUNT(\"bond\".\"XCL_004\")",
  "grain": [
    "\"bond\".\"XCL_006\""
  ],
  "population_scope": "SELECT \"XCL_006\", COUNT(\"XCL_004\") FROM bond GROUP BY \"XCL_006\" ORDER BY COUNT(\"XCL_004\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:195"
  ]
}
```

### Carcinogenic Flag

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" AS flag_carcinogenic FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'ca'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_011\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_011\" AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\" WHERE \"r0\".\"XCL_003\" = 'ca'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:283"
  ]
}
```

### Bond Connection Key

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_006\", T1.\"XCL_004\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE SUBSTRING(T2.\"XCL_007\", 7, 2) = '45'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_004\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_004\" AS \"value\" FROM bond AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_004\" = \"r1\".\"XCL_009\" WHERE SUBSTRING(\"r1\".\"XCL_007\", 7, 2) = '45'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:246"
  ]
}
```

### "bond"."XCL_006" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '-'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_007\", T2.\"XCL_008\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T1.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:210"
  ]
}
```

### A scalar metric representing the percentage of rows in the 'molecule' table where the column 'XCL_011' has the value '+'. It is calculated by dividing

```json
{
  "kind": "metric",
  "formula": "ROUND(CAST(COUNT(CASE WHEN \"molecule\".\"XCL_011\" = '+' THEN \"molecule\".\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(\"molecule\".\"XCL_010\"), 3)",
  "grain": [],
  "population_scope": "SELECT ROUND(CAST(COUNT(CASE WHEN T.\"XCL_011\" = '+' THEN T.\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(T.\"XCL_010\"), 3) FROM molecule AS t",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "ROUND(CAST(COUNT(CASE WHEN \"r0\".\"XCL_011\" = '+' THEN \"r0\".\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_010\"), 3)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT ROUND(CAST(COUNT(CASE WHEN \"r0\".\"XCL_011\" = '+' THEN \"r0\".\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_010\"), 3) AS \"value\" FROM molecule AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:227"
  ]
}
```

### "molecule"."XCL_010" IN ('TR000', 'TR001', 'TR002')

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_010\" IN ('TR000', 'TR001', 'TR002')",
  "grain": [],
  "population_scope": "SELECT \"XCL_010\", T.\"XCL_011\" FROM molecule AS T WHERE T.\"XCL_010\" IN ('TR000', 'TR001', 'TR002')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:264"
  ]
}
```

### "atom"."XCL_003" = 'i'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 'i'",
  "grain": [],
  "population_scope": "SELECT COUNT(T3.\"XCL_004\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T1.\"XCL_003\" = 'i'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:269"
  ]
}
```

### Bond Identifier

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_006\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T2.\"XCL_007\" = 'TR000_1' AND T2.\"XCL_008\" = 'TR000_2'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_006\" AS \"value\" FROM bond AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_004\" = \"r1\".\"XCL_009\" WHERE \"r1\".\"XCL_007\" = 'TR000_1' AND \"r1\".\"XCL_008\" = 'TR000_2'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:320"
  ]
}
```

### Distinct identifiers of molecules that contain at least one carbon atom ('c') connected via a triple bond ('#') and are classified as negative ('-').

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_010\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_010\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '#' AND T1.\"XCL_003\" = 'c' AND T2.\"XCL_011\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:272"
  ]
}
```

### Molecule attribute XCL_011

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_011\"",
  "grain": [
    "\"molecule\".\"XCL_011\""
  ],
  "population_scope": "SELECT COUNT(T1.\"XCL_004\"), T2.\"XCL_011\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '=' AND T2.\"XCL_010\" = 'TR006' GROUP BY T2.\"XCL_011\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_011\"",
    "grain": [
      "\"r1\".\"XCL_011\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_011\" AS \"grain_0\", \"r1\".\"XCL_011\" AS \"value\" FROM bond AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_005\" = \"r1\".\"XCL_010\" WHERE \"r0\".\"XCL_006\" = '=' AND \"r1\".\"XCL_010\" = 'TR006' GROUP BY \"r1\".\"XCL_011\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:303"
  ]
}
```

### Molecule XCL_011 Attribute

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_011\" FROM molecule AS T WHERE T.\"XCL_010\" = 'TR151'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_011\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_011\" AS \"value\" FROM molecule AS \"r0\" WHERE \"r0\".\"XCL_010\" = 'TR151'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:289"
  ]
}
```

### "bond"."XCL_006" = '=' AND "molecule"."XCL_010" = 'TR006'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '=' AND \"molecule\".\"XCL_010\" = 'TR006'",
  "grain": [
    "\"molecule\".\"XCL_011\""
  ],
  "population_scope": "SELECT COUNT(T1.\"XCL_004\"), T2.\"XCL_011\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '=' AND T2.\"XCL_010\" = 'TR006' GROUP BY T2.\"XCL_011\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:303"
  ]
}
```

### Molecule Identifier

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_003\", T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_010\" = 'TR060'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:230"
  ]
}
```

### "bond"."XCL_006" = '#' AND "atom"."XCL_003" = 'c' AND "molecule"."XCL_011" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '#' AND \"atom\".\"XCL_003\" = 'c' AND \"molecule\".\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_010\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '#' AND T1.\"XCL_003\" = 'c' AND T2.\"XCL_011\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:272"
  ]
}
```

### "molecule"."XCL_010" = 'TR006'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_010\" = 'TR006'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_001\", T1.\"XCL_003\", T1.\"XCL_002\", T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_010\" = 'TR006'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:282"
  ]
}
```

### "molecule"."XCL_011" = '+'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_011\" = '+'",
  "grain": [
    "\"atom\".\"XCL_003\""
  ],
  "population_scope": "SELECT T2.\"XCL_003\", COUNT(DISTINCT T2.\"XCL_002\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" WHERE T1.\"XCL_011\" = '+' GROUP BY T2.\"XCL_003\" ORDER BY COUNT(DISTINCT T2.\"XCL_002\") LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:251"
  ]
}
```

### Oxygen Bond Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"atom\".\"XCL_003\")",
  "grain": [
    "\"atom\".\"XCL_002\""
  ],
  "population_scope": "SELECT T1.\"XCL_002\", COUNT(T1.\"XCL_003\") AS oxygen_count FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = '-' AND T1.\"XCL_003\" = 'o' GROUP BY T1.\"XCL_002\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_003\")",
    "grain": [
      "\"r0\".\"XCL_002\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_002\" AS \"grain_0\", COUNT(\"r0\".\"XCL_003\") AS \"value\" FROM atom AS \"r0\" INNER JOIN bond AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_005\" WHERE \"r1\".\"XCL_006\" = '-' AND \"r0\".\"XCL_003\" = 'o' GROUP BY \"r0\".\"XCL_002\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:197"
  ]
}
```

### "molecule"."XCL_011" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": "SELECT COUNT(T.\"XCL_010\") FROM molecule AS T WHERE T.\"XCL_011\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:241"
  ]
}
```

### "bond"."XCL_004" = 'TR007_4_19'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_004\" = 'TR007_4_19'",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_006\" FROM bond AS T WHERE T.\"XCL_004\" = 'TR007_4_19'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:301"
  ]
}
```

### The value of column XCL_007 from the connected table, filtered to rows where XCL_009 equals 'TR000_2_5'.

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_007\" FROM connected AS T WHERE T.\"XCL_009\" = 'TR000_2_5'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_007\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_007\" AS \"value\" FROM connected AS \"r0\" WHERE \"r0\".\"XCL_009\" = 'TR000_2_5'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:223"
  ]
}
```

### Molecule Identifier

```json
{
  "kind": "binding",
  "formula": "T1.\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_011\" FROM molecule AS T1 INNER JOIN (SELECT T.\"XCL_005\", COUNT(T.\"XCL_006\") FROM bond AS T WHERE T.\"XCL_006\" = '=' GROUP BY T.\"XCL_005\" ORDER BY COUNT(T.\"XCL_006\") DESC LIMIT 1) AS T2 ON T1.\"XCL_010\" = T2.\"XCL_005\"",
  "upstream_scopes": [
    "SELECT T.\"XCL_005\", COUNT(T.\"XCL_006\") FROM bond AS T WHERE T.\"XCL_006\" = '=' GROUP BY T.\"XCL_005\" ORDER BY COUNT(T.\"XCL_006\") DESC LIMIT 1"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:244"
  ]
}
```

### "molecule"."XCL_011" = '+'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": "SELECT COUNT(T.\"XCL_010\") FROM molecule AS T WHERE T.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:331",
    "bird_dev:291"
  ]
}
```

### "molecule"."XCL_011" = '-' AND "bond"."XCL_006" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_011\" = '-' AND \"bond\".\"XCL_006\" = '-'",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T2.\"XCL_010\") FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '-' AND T1.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:278"
  ]
}
```

### A scalar metric representing the percentage of molecules with a positive charge (XCL_011 = '+') that contain at least one hydrogen atom (XCL_003 = 'h'

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN \"atom\".\"XCL_003\" = 'h' AND \"molecule\".\"XCL_011\" = '+' THEN \"molecule\".\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(\"molecule\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T1.\"XCL_003\" = 'h' AND T2.\"XCL_011\" = '+' THEN T2.\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(CASE WHEN \"r0\".\"XCL_003\" = 'h' AND \"r1\".\"XCL_011\" = '+' THEN \"r1\".\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r1\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(CASE WHEN \"r0\".\"XCL_003\" = 'h' AND \"r1\".\"XCL_011\" = '+' THEN \"r1\".\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r1\".\"XCL_010\") AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:298"
  ]
}
```

### "connected"."XCL_007" = 'TR000_2' AND "connected"."XCL_008" = 'TR000_4'

```json
{
  "kind": "predicate",
  "formula": "\"connected\".\"XCL_007\" = 'TR000_2' AND \"connected\".\"XCL_008\" = 'TR000_4'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_005\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T2.\"XCL_007\" = 'TR000_2' AND T2.\"XCL_008\" = 'TR000_4'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:321"
  ]
}
```

### COUNT("atom"."XCL_001") > 5

```json
{
  "kind": "predicate",
  "formula": "COUNT(\"atom\".\"XCL_001\") > 5",
  "grain": [
    "\"molecule\".\"XCL_010\""
  ],
  "population_scope": "SELECT T1.\"XCL_010\", COUNT(T2.\"XCL_001\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" WHERE T1.\"XCL_011\" = '-' GROUP BY T1.\"XCL_010\" HAVING COUNT(T2.\"XCL_001\") > 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:327"
  ]
}
```

### Connected Atom ID

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_007\", T2.\"XCL_008\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" INNER JOIN bond AS T3 ON T2.\"XCL_009\" = T3.\"XCL_004\" WHERE T3.\"XCL_006\" = '#' AND T3.\"XCL_005\" = 'TR041'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_007\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      },
      {
        "role": "r2",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_007\" AS \"value\" FROM atom AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_007\" INNER JOIN bond AS \"r2\" ON \"r1\".\"XCL_009\" = \"r2\".\"XCL_004\" WHERE \"r2\".\"XCL_006\" = '#' AND \"r2\".\"XCL_005\" = 'TR041'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:248"
  ]
}
```

### Molecule Identifier

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_010\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_010\", T.\"XCL_011\" FROM molecule AS T WHERE T.\"XCL_010\" IN ('TR000', 'TR001', 'TR002')",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_010\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_010\" AS \"value\" FROM molecule AS \"r0\" WHERE \"r0\".\"XCL_010\" IN ('TR000', 'TR001', 'TR002')",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:264"
  ]
}
```

### Atom Type/Element

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_001\", T1.\"XCL_003\", T1.\"XCL_002\", T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_010\" = 'TR006'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:282"
  ]
}
```

### Bond Identifier

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_004\", T2.\"XCL_011\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '#'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:280"
  ]
}
```

### Returns the value of column XCL_001 from the atom table where XCL_002 equals 'TR186'. Grain is one row per matching atom record.

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_001\" FROM atom AS T WHERE T.\"XCL_002\" = 'TR186'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM atom AS \"r0\" WHERE \"r0\".\"XCL_002\" = 'TR186'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:300"
  ]
}
```

### "bond"."XCL_006" = '='

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '='",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(DISTINCT CASE WHEN T1.\"XCL_003\" = 'c' THEN T1.\"XCL_001\" ELSE NULL END) AS REAL) * 100 / COUNT(DISTINCT T1.\"XCL_001\") FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = '='",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:201"
  ]
}
```

### "molecule"."XCL_010" = 'TR012' AND "bond"."XCL_006" = '=' AND "atom"."XCL_003" = 'c'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_010\" = 'TR012' AND \"bond\".\"XCL_006\" = '=' AND \"atom\".\"XCL_003\" = 'c'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T2.\"XCL_010\" = 'TR012' AND T3.\"XCL_006\" = '=' AND T1.\"XCL_003\" = 'c'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:338"
  ]
}
```

### "molecule"."XCL_011" = '+'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_004\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:261"
  ]
}
```

### Double Bond Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"bond\".\"XCL_006\")",
  "grain": [
    "\"molecule\".\"XCL_010\""
  ],
  "population_scope": "SELECT T3.\"XCL_010\", COUNT(T1.\"XCL_006\") FROM bond AS T1 INNER JOIN molecule AS T3 ON T1.\"XCL_005\" = T3.\"XCL_010\" WHERE T3.\"XCL_011\" = '+' AND T1.\"XCL_006\" = '=' GROUP BY T3.\"XCL_010\" ORDER BY COUNT(T1.\"XCL_006\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:250"
  ]
}
```

### "molecule"."XCL_010" BETWEEN 'TR000' AND 'TR050'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_010\" BETWEEN 'TR000' AND 'TR050'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_005\", T2.\"XCL_006\" FROM molecule AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_010\" = T2.\"XCL_005\" WHERE T1.\"XCL_010\" BETWEEN 'TR000' AND 'TR050'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:267"
  ]
}
```

### Distinct XCL_003 values for TR001

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T.\"XCL_003\" FROM atom AS T WHERE T.\"XCL_002\" = 'TR001'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:274"
  ]
}
```

### Atom XCL_003

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM connected AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_007\" = T2.\"XCL_001\" WHERE T1.\"XCL_009\" = 'TR001_10_11'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "connected"
      },
      {
        "role": "r1",
        "physical_table": "atom"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_003\" AS \"value\" FROM connected AS \"r0\" INNER JOIN atom AS \"r1\" ON \"r0\".\"XCL_007\" = \"r1\".\"XCL_001\" WHERE \"r0\".\"XCL_009\" = 'TR001_10_11'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:268"
  ]
}
```

### "atom"."XCL_002" = 'TR024' AND "bond"."XCL_006" = '='

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_002\" = 'TR024' AND \"bond\".\"XCL_006\" = '='",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_002\" = 'TR024' AND T2.\"XCL_006\" = '='",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:328"
  ]
}
```

### "connected"."XCL_009" = 'TR001_3_4'

```json
{
  "kind": "predicate",
  "formula": "\"connected\".\"XCL_009\" = 'TR001_3_4'",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_003\") FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T2.\"XCL_009\" = 'TR001_3_4'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:319"
  ]
}
```

### Molecule Identifier

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_011\"",
  "grain": [
    "\"molecule\".\"XCL_011\""
  ],
  "population_scope": "SELECT T2.\"XCL_011\", COUNT(T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'h' GROUP BY T2.\"XCL_011\" ORDER BY COUNT(T2.\"XCL_010\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:208"
  ]
}
```

### "atom"."XCL_003" = 'cl' AND "molecule"."XCL_011" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 'cl' AND \"molecule\".\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_010\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'cl' AND T1.\"XCL_011\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:196"
  ]
}
```

### "atom"."XCL_002" = 'TR008' AND "atom"."XCL_003" = 'c'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_002\" = 'TR008' AND \"atom\".\"XCL_003\" = 'c'",
  "grain": [],
  "population_scope": "SELECT COUNT(T.\"XCL_001\") FROM atom AS T WHERE T.\"XCL_002\" = 'TR008' AND T.\"XCL_003\" = 'c'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:333"
  ]
}
```

### "molecule"."XCL_010" = 'TR060'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_010\" = 'TR060'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_003\", T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_010\" = 'TR060'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:230"
  ]
}
```

### "bond"."XCL_006" = '#'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '#'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_003\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" INNER JOIN atom AS T3 ON T2.\"XCL_007\" = T3.\"XCL_001\" WHERE T1.\"XCL_006\" = '#'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:253"
  ]
}
```

### "molecule"."XCL_010" = 'TR151'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_010\" = 'TR151'",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_011\" FROM molecule AS T WHERE T.\"XCL_010\" = 'TR151'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:289"
  ]
}
```

### Aggregates the total number of bond records (identified by XCL_004) associated with molecules that contain at least one atom classified as 'i' (inorga

```json
{
  "kind": "metric",
  "formula": "COUNT(\"bond\".\"XCL_004\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T3.\"XCL_004\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T1.\"XCL_003\" = 'i'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r2\".\"XCL_004\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      },
      {
        "role": "r2",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r2\".\"XCL_004\") AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\" INNER JOIN bond AS \"r2\" ON \"r1\".\"XCL_010\" = \"r2\".\"XCL_005\" WHERE \"r0\".\"XCL_003\" = 'i'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:269"
  ]
}
```

### Connected Attribute XCL_007

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_007\", T2.\"XCL_008\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T1.\"XCL_006\" = '#'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_007\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_007\" AS \"value\" FROM bond AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_004\" = \"r1\".\"XCL_009\" WHERE \"r0\".\"XCL_006\" = '#'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:216",
    "bird_dev:276"
  ]
}
```

### Aggregates the total number of non-null values in column XCL_009 from the 'connected' table, restricted to rows where the last two characters of colum

```json
{
  "kind": "metric",
  "formula": "COUNT(\"connected\".\"XCL_009\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T.\"XCL_009\") FROM connected AS T WHERE SUBSTRING(T.\"XCL_007\", -2) = '19'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_009\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_009\") AS \"value\" FROM connected AS \"r0\" WHERE SUBSTRING(\"r0\".\"XCL_007\", -2) = '19'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:239"
  ]
}
```

### Bond Identifier

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_005\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_005\", T2.\"XCL_006\" FROM molecule AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_010\" = T2.\"XCL_005\" WHERE T1.\"XCL_010\" BETWEEN 'TR000' AND 'TR050'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_005\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "molecule"
      },
      {
        "role": "r1",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_005\" AS \"value\" FROM molecule AS \"r0\" INNER JOIN bond AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_005\" WHERE \"r0\".\"XCL_010\" BETWEEN 'TR000' AND 'TR050'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:267"
  ]
}
```

### Calculates the percentage of non-null 'XCL_004' values where 'XCL_006' is exactly '='. The numerator counts rows satisfying the condition, and the den

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN \"bond\".\"XCL_006\" = '=' THEN \"bond\".\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(\"bond\".\"XCL_004\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T.\"XCL_006\" = '=' THEN T.\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(T.\"XCL_004\") FROM bond AS T WHERE T.\"XCL_005\" = 'TR047'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(CASE WHEN \"r0\".\"XCL_006\" = '=' THEN \"r0\".\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_004\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(CASE WHEN \"r0\".\"XCL_006\" = '=' THEN \"r0\".\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_004\") AS \"value\" FROM bond AS \"r0\" WHERE \"r0\".\"XCL_005\" = 'TR047'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:287"
  ]
}
```

### Connection Identifier

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_009\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_009\", T2.\"XCL_008\", T1.\"XCL_003\" AS flag_have_CaCl FROM atom AS T1 INNER JOIN connected AS T2 ON T2.\"XCL_007\" = T1.\"XCL_001\" WHERE T2.\"XCL_009\" = 'TR001_1_8' AND (T1.\"XCL_003\" = 'c1' OR T1.\"XCL_003\" = 'c')",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_009\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_009\" AS \"value\" FROM atom AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r1\".\"XCL_007\" = \"r0\".\"XCL_001\" WHERE \"r1\".\"XCL_009\" = 'TR001_1_8' AND (\"r0\".\"XCL_003\" = 'c1' OR \"r0\".\"XCL_003\" = 'c')",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:271"
  ]
}
```

### Bond Attribute XCL_006

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_006\", T2.\"XCL_007\", T2.\"XCL_008\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T2.\"XCL_009\" = 'TR001_6_9'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_006\" AS \"value\" FROM bond AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_004\" = \"r1\".\"XCL_009\" WHERE \"r1\".\"XCL_009\" = 'TR001_6_9'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:236"
  ]
}
```

### Count of distinct atoms in non-single bonds (non-sulfur)

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"atom\".\"XCL_002\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_002\") FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_003\" <> 's' AND T2.\"XCL_006\" <> '='",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_002\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r0\".\"XCL_002\") AS \"value\" FROM atom AS \"r0\" INNER JOIN bond AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_005\" WHERE \"r0\".\"XCL_003\" <> 's' AND \"r1\".\"XCL_006\" <> '='",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:311"
  ]
}
```

### Molecule Identifier

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_004\", T2.\"XCL_011\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '#'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:280"
  ]
}
```

### "bond"."XCL_004" = 'TR001_2_4'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_004\" = 'TR001_2_4'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_004\" = 'TR001_2_4'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:312"
  ]
}
```

### Aggregates the total number of atom records (identified by XCL_001) that are associated with molecules where the attribute XCL_011 is equal to '+'. Th

```json
{
  "kind": "metric",
  "formula": "COUNT(\"atom\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\" WHERE \"r1\".\"XCL_011\" = '+'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:293"
  ]
}
```

### "molecule"."XCL_011" = '+' AND SUBSTRING("atom"."XCL_001", -1) = '4' AND LENGTH("atom"."XCL_001") = 7

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_011\" = '+' AND SUBSTRING(\"atom\".\"XCL_001\", -1) = '4' AND LENGTH(\"atom\".\"XCL_001\") = 7",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+' AND SUBSTRING(T1.\"XCL_001\", -1) = '4' AND LENGTH(T1.\"XCL_001\") = 7",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:281"
  ]
}
```

### "molecule"."XCL_011" = '+' AND "bond"."XCL_006" = '='

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_011\" = '+' AND \"bond\".\"XCL_006\" = '='",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_004\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+' AND T1.\"XCL_006\" = '='",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:294"
  ]
}
```

### A scalar metric calculated as the count of 'connected' table rows (specifically the 'XCL_009' column) divided by the count of 'atom' table rows (speci

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(\"connected\".\"XCL_009\") AS REAL) / COUNT(\"atom\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(T2.\"XCL_009\") AS REAL) / COUNT(T1.\"XCL_001\") FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T1.\"XCL_003\" = 'i'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(\"r1\".\"XCL_009\") AS REAL) / COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(\"r1\".\"XCL_009\") AS REAL) / COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM atom AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_007\" WHERE \"r0\".\"XCL_003\" = 'i'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:245"
  ]
}
```

### "bond"."XCL_006" = '#' AND "molecule"."XCL_011" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '#' AND \"molecule\".\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_010\") FROM molecule AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_010\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = '#' AND T1.\"XCL_011\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:336"
  ]
}
```

### Aggregates the count of non-null values in column XCL_010 from the molecule table, restricted to rows where XCL_011 equals '+'. Returns a single scala

```json
{
  "kind": "metric",
  "formula": "COUNT(\"molecule\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T.\"XCL_010\") FROM molecule AS T WHERE T.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_010\") AS \"value\" FROM molecule AS \"r0\" WHERE \"r0\".\"XCL_011\" = '+'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:331",
    "bird_dev:291"
  ]
}
```

### Bond XCL_006

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_003\", T2.\"XCL_006\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_002\" = 'TR002'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:337"
  ]
}
```

### Atom Type Identifier

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [
    "\"atom\".\"XCL_003\""
  ],
  "population_scope": "SELECT T1.\"XCL_003\", COUNT(DISTINCT T1.\"XCL_002\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '-' GROUP BY T1.\"XCL_003\" ORDER BY COUNT(DISTINCT T1.\"XCL_002\") ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:212"
  ]
}
```

### Distinct identifiers (XCL_010) of molecules that are positively charged (XCL_011 = '+') and contain at least one atom with a type code (XCL_001) endin

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_010\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_010\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE SUBSTRING(T1.\"XCL_001\", -2) BETWEEN '21' AND '25' AND T2.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:242"
  ]
}
```

### "molecule"."XCL_011" = '+'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T1.\"XCL_003\" = 'cl' THEN T1.\"XCL_003\" ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_003\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:273"
  ]
}
```

### Filtered Molecule Identifier

```json
{
  "kind": "binding",
  "formula": "T.\"XCL_010\"",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_010\" FROM (SELECT T1.\"XCL_010\", COUNT(T2.\"XCL_001\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" WHERE T1.\"XCL_011\" = '-' GROUP BY T1.\"XCL_010\" HAVING COUNT(T2.\"XCL_001\") > 5) AS t",
  "upstream_scopes": [
    "SELECT T1.\"XCL_010\", COUNT(T2.\"XCL_001\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" WHERE T1.\"XCL_011\" = '-' GROUP BY T1.\"XCL_010\" HAVING COUNT(T2.\"XCL_001\") > 5"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:327"
  ]
}
```

### Aggregates the count of unique molecule identifiers (XCL_010) from the molecule table where the molecule has a negative charge (XCL_011 = '-') and is 

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"molecule\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_010\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'cl' AND T1.\"XCL_011\" = '-'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "molecule"
      },
      {
        "role": "r1",
        "physical_table": "atom"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r0\".\"XCL_010\") AS \"value\" FROM molecule AS \"r0\" INNER JOIN atom AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_002\" WHERE \"r1\".\"XCL_003\" = 'cl' AND \"r0\".\"XCL_011\" = '-'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:196"
  ]
}
```

### Calculates the percentage of distinct molecules (XCL_010) that have a positive charge (XCL_011 = '+') among the subset of molecules that contain a tri

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"molecule\".\"XCL_011\" = '+' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(DISTINCT \"molecule\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T1.\"XCL_011\" = '+' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(DISTINCT T1.\"XCL_010\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" INNER JOIN bond AS T3 ON T1.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '#' AND T2.\"XCL_003\" = 'h'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r0\".\"XCL_011\" = '+' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(DISTINCT \"r0\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "molecule"
      },
      {
        "role": "r1",
        "physical_table": "atom"
      },
      {
        "role": "r2",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r0\".\"XCL_011\" = '+' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(DISTINCT \"r0\".\"XCL_010\") AS \"value\" FROM molecule AS \"r0\" INNER JOIN atom AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_002\" INNER JOIN bond AS \"r2\" ON \"r0\".\"XCL_010\" = \"r2\".\"XCL_005\" WHERE \"r2\".\"XCL_006\" = '#' AND \"r1\".\"XCL_003\" = 'h'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:330"
  ]
}
```

### "molecule"."XCL_011" = '+' AND "atom"."XCL_003" = 'br'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_011\" = '+' AND \"atom\".\"XCL_003\" = 'br'",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+' AND T1.\"XCL_003\" = 'br'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:235"
  ]
}
```

### "bond"."XCL_006" = '-' AND "molecule"."XCL_011" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '-' AND \"molecule\".\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_010\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '-' AND T2.\"XCL_011\" = '-' ORDER BY T2.\"XCL_010\" LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:232"
  ]
}
```

### "bond"."XCL_005" = 'TR008'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_005\" = 'TR008'",
  "grain": [],
  "population_scope": "SELECT ROUND(CAST(COUNT(CASE WHEN T.\"XCL_006\" = '=' THEN T.\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(T.\"XCL_004\"), 5) FROM bond AS T WHERE T.\"XCL_005\" = 'TR008'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:226"
  ]
}
```

### "bond"."XCL_005" = 'TR047'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_005\" = 'TR047'",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T.\"XCL_006\" = '=' THEN T.\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(T.\"XCL_004\") FROM bond AS T WHERE T.\"XCL_005\" = 'TR047'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:287"
  ]
}
```

### Constructs the identifier for the second atom by concatenating the bond type (XCL_005) with the last 2 characters of the bond identifier (XCL_004). Re

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_005\" || SUBSTRING(\"bond\".\"XCL_004\", 8, 2)",
  "grain": [],
  "population_scope": "SELECT SUBSTRING(T.\"XCL_004\", 1, 7) AS atom_id1, T.\"XCL_005\" || SUBSTRING(T.\"XCL_004\", 8, 2) AS atom_id2 FROM bond AS T WHERE T.\"XCL_005\" = 'TR001' AND T.\"XCL_004\" = 'TR001_2_6'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_005\" || SUBSTRING(\"r0\".\"XCL_004\", 8, 2)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_005\" || SUBSTRING(\"r0\".\"XCL_004\", 8, 2) AS \"value\" FROM bond AS \"r0\" WHERE \"r0\".\"XCL_005\" = 'TR001' AND \"r0\".\"XCL_004\" = 'TR001_2_6'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:221"
  ]
}
```

### Atom Molecule Link

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_001\", T1.\"XCL_003\", T1.\"XCL_002\", T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_010\" = 'TR006'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:282"
  ]
}
```

### Molecule Identifier

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_011\"",
  "grain": [
    "\"molecule\".\"XCL_011\""
  ],
  "population_scope": "SELECT T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'ca' GROUP BY T2.\"XCL_011\" ORDER BY COUNT(T2.\"XCL_011\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:270"
  ]
}
```

### Aggregates the number of rows in the 'connected' table that satisfy specific structural conditions relative to the bond 'TR009'. The count is based on

```json
{
  "kind": "metric",
  "formula": "COUNT(\"connected\".\"XCL_009\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_009\") FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T1.\"XCL_005\" = 'TR009' AND T2.\"XCL_007\" = T1.\"XCL_005\" || '_1' AND T2.\"XCL_008\" = T1.\"XCL_005\" || '_2'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_009\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_009\") AS \"value\" FROM bond AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_004\" = \"r1\".\"XCL_009\" WHERE \"r0\".\"XCL_005\" = 'TR009' AND \"r1\".\"XCL_007\" = \"r0\".\"XCL_005\" || '_1' AND \"r1\".\"XCL_008\" = \"r0\".\"XCL_005\" || '_2'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:234"
  ]
}
```

### Count of distinct molecules with specific bond and molecule attributes

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"molecule\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T2.\"XCL_010\") FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '-' AND T1.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r1\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r1\".\"XCL_010\") AS \"value\" FROM bond AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_005\" = \"r1\".\"XCL_010\" WHERE \"r1\".\"XCL_011\" = '-' AND \"r0\".\"XCL_006\" = '-'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:278"
  ]
}
```

### Calculates the percentage of rows in the 'bond' table where the column 'XCL_006' contains the literal value '-'. The numerator counts non-null 'XCL_00

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN \"bond\".\"XCL_006\" = '-' THEN \"bond\".\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(\"bond\".\"XCL_004\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T.\"XCL_006\" = '-' THEN T.\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(T.\"XCL_004\") FROM bond AS t",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(CASE WHEN \"r0\".\"XCL_006\" = '-' THEN \"r0\".\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_004\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(CASE WHEN \"r0\".\"XCL_006\" = '-' THEN \"r0\".\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_004\") AS \"value\" FROM bond AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:324"
  ]
}
```

### Carcinogenic Flag

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" AS flag_carcinogenic FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_001\" = 'TR001_1'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_011\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_011\" AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\" WHERE \"r0\".\"XCL_001\" = 'TR001_1'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:288"
  ]
}
```

### Count of distinct values in column XCL_001 from the atom table, filtered to rows where XCL_003 is not equal to 'br'.

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"atom\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T.\"XCL_001\") FROM atom AS T WHERE T.\"XCL_003\" <> 'br'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r0\".\"XCL_001\") AS \"value\" FROM atom AS \"r0\" WHERE \"r0\".\"XCL_003\" <> 'br'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:203"
  ]
}
```

### Bond Identifier

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_006\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" INNER JOIN atom AS T3 ON T2.\"XCL_007\" = T3.\"XCL_001\" WHERE T3.\"XCL_003\" = 'cl'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:209"
  ]
}
```

### Aggregates the number of unique molecule identifiers (XCL_010) from the molecule table. The population is restricted to molecules that are linked to a

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"molecule\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'na' AND T2.\"XCL_011\" = '-'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r1\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r1\".\"XCL_010\") AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\" WHERE \"r0\".\"XCL_003\" = 'na' AND \"r1\".\"XCL_011\" = '-'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:199"
  ]
}
```

### Count of distinct sulfur atoms in single bonds

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT CASE WHEN \"atom\".\"XCL_003\" = 's' THEN \"atom\".\"XCL_001\" ELSE NULL END)",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT CASE WHEN T1.\"XCL_003\" = 'i' THEN T1.\"XCL_001\" ELSE NULL END) AS iodine_nums, COUNT(DISTINCT CASE WHEN T1.\"XCL_003\" = 's' THEN T1.\"XCL_001\" ELSE NULL END) AS sulfur_nums FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" INNER JOIN bond AS T3 ON T2.\"XCL_009\" = T3.\"XCL_004\" WHERE T3.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT CASE WHEN \"r0\".\"XCL_003\" = 's' THEN \"r0\".\"XCL_001\" ELSE NULL END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      },
      {
        "role": "r2",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT CASE WHEN \"r0\".\"XCL_003\" = 's' THEN \"r0\".\"XCL_001\" ELSE NULL END) AS \"value\" FROM atom AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_007\" INNER JOIN bond AS \"r2\" ON \"r1\".\"XCL_009\" = \"r2\".\"XCL_004\" WHERE \"r2\".\"XCL_006\" = '-'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:215"
  ]
}
```

### The final output identifier of the molecule that has the maximum number of double bonds, filtered to only include molecules with a charge of '+'.

```json
{
  "kind": "binding",
  "formula": "T.\"XCL_010\"",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_010\" FROM (SELECT T3.\"XCL_010\", COUNT(T1.\"XCL_006\") FROM bond AS T1 INNER JOIN molecule AS T3 ON T1.\"XCL_005\" = T3.\"XCL_010\" WHERE T3.\"XCL_011\" = '+' AND T1.\"XCL_006\" = '=' GROUP BY T3.\"XCL_010\" ORDER BY COUNT(T1.\"XCL_006\") DESC LIMIT 1) AS T",
  "upstream_scopes": [
    "SELECT T3.\"XCL_010\", COUNT(T1.\"XCL_006\") FROM bond AS T1 INNER JOIN molecule AS T3 ON T1.\"XCL_005\" = T3.\"XCL_010\" WHERE T3.\"XCL_011\" = '+' AND T1.\"XCL_006\" = '=' GROUP BY T3.\"XCL_010\" ORDER BY COUNT(T1.\"XCL_006\") DESC LIMIT 1"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:250"
  ]
}
```

### A list of unique values from the 'XCL_005' column in the 'bond' table, filtered to rows where 'XCL_006' equals '='. The results are sorted by 'XCL_005

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_005\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T.\"XCL_005\" FROM bond AS T WHERE T.\"XCL_006\" = '=' ORDER BY T.\"XCL_005\" LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:225"
  ]
}
```

### SUBSTRING("connected"."XCL_007", -2) = '19'

```json
{
  "kind": "predicate",
  "formula": "SUBSTRING(\"connected\".\"XCL_007\", -2) = '19'",
  "grain": [],
  "population_scope": "SELECT COUNT(T.\"XCL_009\") FROM connected AS T WHERE SUBSTRING(T.\"XCL_007\", -2) = '19'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:239"
  ]
}
```

### Aggregates the total number of rows in the 'connected' table where the associated atom (via 'XCL_007' = 'XCL_001') has an element type of 'cl' (chlori

```json
{
  "kind": "metric",
  "formula": "COUNT(\"connected\".\"XCL_009\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_009\") FROM connected AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_007\" = T2.\"XCL_001\" WHERE T2.\"XCL_003\" = 'cl'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_009\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "connected"
      },
      {
        "role": "r1",
        "physical_table": "atom"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_009\") AS \"value\" FROM connected AS \"r0\" INNER JOIN atom AS \"r1\" ON \"r0\".\"XCL_007\" = \"r1\".\"XCL_001\" WHERE \"r1\".\"XCL_003\" = 'cl'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:308"
  ]
}
```

### "bond"."XCL_006" = '#'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '#'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_007\", T2.\"XCL_008\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T1.\"XCL_006\" = '#'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:216",
    "bird_dev:276"
  ]
}
```

### "connected"."XCL_009" = 'TR144_8_19'

```json
{
  "kind": "predicate",
  "formula": "\"connected\".\"XCL_009\" = 'TR144_8_19'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM connected AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_007\" = T2.\"XCL_001\" WHERE T1.\"XCL_009\" = 'TR144_8_19'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:249"
  ]
}
```

### Connected Bond ID

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_007\", T2.\"XCL_008\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" INNER JOIN bond AS T3 ON T2.\"XCL_009\" = T3.\"XCL_004\" WHERE T3.\"XCL_006\" = '#' AND T3.\"XCL_005\" = 'TR041'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      },
      {
        "role": "r2",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_008\" AS \"value\" FROM atom AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_007\" INNER JOIN bond AS \"r2\" ON \"r1\".\"XCL_009\" = \"r2\".\"XCL_004\" WHERE \"r2\".\"XCL_006\" = '#' AND \"r2\".\"XCL_005\" = 'TR041'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:248"
  ]
}
```

### "atom"."XCL_003" = 'cl'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 'cl'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_006\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" INNER JOIN atom AS T3 ON T2.\"XCL_007\" = T3.\"XCL_001\" WHERE T3.\"XCL_003\" = 'cl'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:209"
  ]
}
```

### SUBSTRING("atom"."XCL_001", -2) BETWEEN '21' AND '25' AND "molecule"."XCL_011" = '+'

```json
{
  "kind": "predicate",
  "formula": "SUBSTRING(\"atom\".\"XCL_001\", -2) BETWEEN '21' AND '25' AND \"molecule\".\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_010\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE SUBSTRING(T1.\"XCL_001\", -2) BETWEEN '21' AND '25' AND T2.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:242"
  ]
}
```

### Aggregates the total number of rows in the 'atom' table where the 'XCL_003' column equals 'c' or 'h'. The count is performed on the 'XCL_001' identifi

```json
{
  "kind": "metric",
  "formula": "COUNT(\"atom\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T.\"XCL_001\") FROM atom AS T WHERE T.\"XCL_003\" = 'c' OR T.\"XCL_003\" = 'h'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM atom AS \"r0\" WHERE \"r0\".\"XCL_003\" = 'c' OR \"r0\".\"XCL_003\" = 'h'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:256"
  ]
}
```

### Atom Identifier

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_010\", T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:259"
  ]
}
```

### Atom Identifier

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_001\" = 'TR004_7' AND T2.\"XCL_011\" = '-'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_003\" AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\" WHERE \"r0\".\"XCL_001\" = 'TR004_7' AND \"r1\".\"XCL_011\" = '-'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:334"
  ]
}
```

### "bond"."XCL_005" = 'TR009' AND "connected"."XCL_007" = "bond"."XCL_005" || '_1' AND "connected"."XCL_008" = "bond"."XCL_005" || '_2'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_005\" = 'TR009' AND \"connected\".\"XCL_007\" = \"bond\".\"XCL_005\" || '_1' AND \"connected\".\"XCL_008\" = \"bond\".\"XCL_005\" || '_2'",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_009\") FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T1.\"XCL_005\" = 'TR009' AND T2.\"XCL_007\" = T1.\"XCL_005\" || '_1' AND T2.\"XCL_008\" = T1.\"XCL_005\" || '_2'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:234"
  ]
}
```

### Atom Count per Molecule

```json
{
  "kind": "metric",
  "formula": "COUNT(\"atom\".\"XCL_001\")",
  "grain": [
    "\"molecule\".\"XCL_010\""
  ],
  "population_scope": "SELECT T1.\"XCL_010\", COUNT(T2.\"XCL_001\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" WHERE T1.\"XCL_011\" = '-' GROUP BY T1.\"XCL_010\" HAVING COUNT(T2.\"XCL_001\") > 5",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_001\")",
    "grain": [
      "\"r0\".\"XCL_010\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "molecule"
      },
      {
        "role": "r1",
        "physical_table": "atom"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_010\" AS \"grain_0\", COUNT(\"r1\".\"XCL_001\") AS \"value\" FROM molecule AS \"r0\" INNER JOIN atom AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_002\" WHERE \"r0\".\"XCL_011\" = '-' GROUP BY \"r0\".\"XCL_010\" HAVING COUNT(\"r1\".\"XCL_001\") > 5",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:327"
  ]
}
```

### Calculates the percentage of bonds where bond.XCL_006 is '-' among all bonds joined to molecules where molecule.XCL_011 is '+'. The metric is computed

```json
{
  "kind": "metric",
  "formula": "ROUND(CAST(COUNT(CASE WHEN \"molecule\".\"XCL_011\" = '+' THEN \"bond\".\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(\"bond\".\"XCL_004\"), 5)",
  "grain": [],
  "population_scope": "SELECT ROUND(CAST(COUNT(CASE WHEN T2.\"XCL_011\" = '+' THEN T1.\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_004\"), 5) FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "ROUND(CAST(COUNT(CASE WHEN \"r1\".\"XCL_011\" = '+' THEN \"r0\".\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_004\"), 5)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT ROUND(CAST(COUNT(CASE WHEN \"r1\".\"XCL_011\" = '+' THEN \"r0\".\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_004\"), 5) AS \"value\" FROM bond AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_005\" = \"r1\".\"XCL_010\" WHERE \"r0\".\"XCL_006\" = '-'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:255"
  ]
}
```

### "atom"."XCL_003" = 'c' OR "atom"."XCL_003" = 'h'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 'c' OR \"atom\".\"XCL_003\" = 'h'",
  "grain": [],
  "population_scope": "SELECT COUNT(T.\"XCL_001\") FROM atom AS T WHERE T.\"XCL_003\" = 'c' OR T.\"XCL_003\" = 'h'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:256"
  ]
}
```

### Atom Identifier

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM connected AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_007\" = T2.\"XCL_001\" WHERE T1.\"XCL_009\" = 'TR144_8_19'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "connected"
      },
      {
        "role": "r1",
        "physical_table": "atom"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_003\" AS \"value\" FROM connected AS \"r0\" INNER JOIN atom AS \"r1\" ON \"r0\".\"XCL_007\" = \"r1\".\"XCL_001\" WHERE \"r0\".\"XCL_009\" = 'TR144_8_19'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:249"
  ]
}
```

### Extracts the first 7 characters of the bond identifier (XCL_004) to represent the first atom involved in the bond. Returns a single string value per b

```json
{
  "kind": "binding",
  "formula": "SUBSTRING(\"bond\".\"XCL_004\", 1, 7)",
  "grain": [],
  "population_scope": "SELECT SUBSTRING(T.\"XCL_004\", 1, 7) AS atom_id1, T.\"XCL_005\" || SUBSTRING(T.\"XCL_004\", 8, 2) AS atom_id2 FROM bond AS T WHERE T.\"XCL_005\" = 'TR001' AND T.\"XCL_004\" = 'TR001_2_6'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUBSTRING(\"r0\".\"XCL_004\", 1, 7)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT SUBSTRING(\"r0\".\"XCL_004\", 1, 7) AS \"value\" FROM bond AS \"r0\" WHERE \"r0\".\"XCL_005\" = 'TR001' AND \"r0\".\"XCL_004\" = 'TR001_2_6'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:221"
  ]
}
```

### Double Bond Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"bond\".\"XCL_006\")",
  "grain": [
    "\"bond\".\"XCL_005\""
  ],
  "population_scope": "SELECT T.\"XCL_005\", COUNT(T.\"XCL_006\") FROM bond AS T WHERE T.\"XCL_006\" = '=' GROUP BY T.\"XCL_005\" ORDER BY COUNT(T.\"XCL_006\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:244"
  ]
}
```

### "bond"."XCL_006" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '-'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:263"
  ]
}
```

### "atom"."XCL_003" = 'cl'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 'cl'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_009\") FROM connected AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_007\" = T2.\"XCL_001\" WHERE T2.\"XCL_003\" = 'cl'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:308"
  ]
}
```

### "atom"."XCL_003" = 'o' AND "molecule"."XCL_011" = '+'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 'o' AND \"molecule\".\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'o' AND T2.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:339"
  ]
}
```

### Aggregates the number of bond records (XCL_004) where the bond type (XCL_006) is '=' (double bond) for the specific molecule identified by XCL_010 = '

```json
{
  "kind": "metric",
  "formula": "COUNT(\"bond\".\"XCL_004\")",
  "grain": [
    "\"molecule\".\"XCL_011\""
  ],
  "population_scope": "SELECT COUNT(T1.\"XCL_004\"), T2.\"XCL_011\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '=' AND T2.\"XCL_010\" = 'TR006' GROUP BY T2.\"XCL_011\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_004\")",
    "grain": [
      "\"r1\".\"XCL_011\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_011\" AS \"grain_0\", COUNT(\"r0\".\"XCL_004\") AS \"value\" FROM bond AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_005\" = \"r1\".\"XCL_010\" WHERE \"r0\".\"XCL_006\" = '=' AND \"r1\".\"XCL_010\" = 'TR006' GROUP BY \"r1\".\"XCL_011\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:303"
  ]
}
```

### Count of XCL_005 per XCL_006

```json
{
  "kind": "metric",
  "formula": "COUNT(\"bond\".\"XCL_005\")",
  "grain": [
    "\"bond\".\"XCL_006\""
  ],
  "population_scope": "SELECT T1.\"XCL_006\", COUNT(T1.\"XCL_005\") FROM bond AS T1 WHERE T1.\"XCL_005\" = 'TR010' GROUP BY T1.\"XCL_006\" ORDER BY COUNT(T1.\"XCL_005\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:231"
  ]
}
```

### Aggregates the count of non-null values in column XCL_001 from the atom table, filtered to rows where XCL_002 equals 'TR008' and XCL_003 equals 'c'. R

```json
{
  "kind": "metric",
  "formula": "COUNT(\"atom\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T.\"XCL_001\") FROM atom AS T WHERE T.\"XCL_002\" = 'TR008' AND T.\"XCL_003\" = 'c'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM atom AS \"r0\" WHERE \"r0\".\"XCL_002\" = 'TR008' AND \"r0\".\"XCL_003\" = 'c'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:333"
  ]
}
```

### Connection Attribute

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_007\", T2.\"XCL_008\" FROM atom AS T1 INNER JOIN connected AS T2 ON T2.\"XCL_007\" = T1.\"XCL_001\" WHERE T1.\"XCL_002\" = 'TR181'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_008\" AS \"value\" FROM atom AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r1\".\"XCL_007\" = \"r0\".\"XCL_001\" WHERE \"r0\".\"XCL_002\" = 'TR181'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:217"
  ]
}
```

### "connected"."XCL_009" = 'TR000_2_5'

```json
{
  "kind": "predicate",
  "formula": "\"connected\".\"XCL_009\" = 'TR000_2_5'",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_007\" FROM connected AS T WHERE T.\"XCL_009\" = 'TR000_2_5'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:223"
  ]
}
```

### Calculates the percentage of non-null XCL_004 values where XCL_006 is exactly '='. The numerator counts XCL_004 entries satisfying the condition, and 

```json
{
  "kind": "metric",
  "formula": "ROUND(CAST(COUNT(CASE WHEN \"bond\".\"XCL_006\" = '=' THEN \"bond\".\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(\"bond\".\"XCL_004\"), 5)",
  "grain": [],
  "population_scope": "SELECT ROUND(CAST(COUNT(CASE WHEN T.\"XCL_006\" = '=' THEN T.\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(T.\"XCL_004\"), 5) FROM bond AS T WHERE T.\"XCL_005\" = 'TR008'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "ROUND(CAST(COUNT(CASE WHEN \"r0\".\"XCL_006\" = '=' THEN \"r0\".\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_004\"), 5)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT ROUND(CAST(COUNT(CASE WHEN \"r0\".\"XCL_006\" = '=' THEN \"r0\".\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_004\"), 5) AS \"value\" FROM bond AS \"r0\" WHERE \"r0\".\"XCL_005\" = 'TR008'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:226"
  ]
}
```

### "atom"."XCL_002" = 'TR001'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_002\" = 'TR001'",
  "grain": [],
  "population_scope": "SELECT COUNT(T.\"XCL_001\") FROM atom AS T WHERE T.\"XCL_002\" = 'TR001'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:313"
  ]
}
```

### Distinct Atom Identifier

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_002\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'c' AND T2.\"XCL_011\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:316"
  ]
}
```

### Atom Identifier

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" INNER JOIN bond AS T3 ON T2.\"XCL_009\" = T3.\"XCL_004\" WHERE T3.\"XCL_004\" = 'TR001_10_11'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      },
      {
        "role": "r2",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_003\" AS \"value\" FROM atom AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_007\" INNER JOIN bond AS \"r2\" ON \"r1\".\"XCL_009\" = \"r2\".\"XCL_004\" WHERE \"r2\".\"XCL_004\" = 'TR001_10_11'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:285"
  ]
}
```

### Bond Identifier

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_006\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T2.\"XCL_007\" = 'TR004_8' AND T2.\"XCL_008\" = 'TR004_20' OR T2.\"XCL_008\" = 'TR004_8' AND T2.\"XCL_007\" = 'TR004_20'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_006\" AS \"value\" FROM bond AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_004\" = \"r1\".\"XCL_009\" WHERE \"r1\".\"XCL_007\" = 'TR004_8' AND \"r1\".\"XCL_008\" = 'TR004_20' OR \"r1\".\"XCL_008\" = 'TR004_8' AND \"r1\".\"XCL_007\" = 'TR004_20'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:213"
  ]
}
```

### "atom"."XCL_003" = 'cl' AND "molecule"."XCL_011" = '+'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 'cl' AND \"molecule\".\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_002\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'cl' AND T2.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:315"
  ]
}
```

### "bond"."XCL_006" = '=' AND "atom"."XCL_003" = 'o'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '=' AND \"atom\".\"XCL_003\" = 'o'",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_002\") FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = '=' AND T1.\"XCL_003\" = 'o'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:335"
  ]
}
```

### "bond"."XCL_006" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '-'",
  "grain": [],
  "population_scope": "SELECT COUNT(T.\"XCL_004\") FROM bond AS T WHERE T.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:314"
  ]
}
```

### Connected Attribute XCL_008

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_007\", T2.\"XCL_008\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T1.\"XCL_006\" = '#'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_008\" AS \"value\" FROM bond AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_004\" = \"r1\".\"XCL_009\" WHERE \"r0\".\"XCL_006\" = '#'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:216",
    "bird_dev:276"
  ]
}
```

### "atom"."XCL_003" <> 'sn'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" <> 'sn'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" <> 'sn'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:214"
  ]
}
```

### Bond Attribute XCL_006

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_006\"",
  "grain": [
    "\"bond\".\"XCL_006\""
  ],
  "population_scope": "SELECT T1.\"XCL_006\", COUNT(T1.\"XCL_005\") FROM bond AS T1 WHERE T1.\"XCL_005\" = 'TR010' GROUP BY T1.\"XCL_006\" ORDER BY COUNT(T1.\"XCL_005\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:231"
  ]
}
```

### "bond"."XCL_006" = '#' AND "molecule"."XCL_011" = '+'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '#' AND \"molecule\".\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_010\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '#' AND T2.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:200"
  ]
}
```

### Distinct Atom Identifier

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T2.\"XCL_009\" = 'TR004_8_9'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:206"
  ]
}
```

### Max Bond Group Connection Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"connected\".\"XCL_007\")",
  "grain": [
    "\"bond\".\"XCL_006\""
  ],
  "population_scope": "SELECT COUNT(T1.\"XCL_007\") FROM connected AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_009\" = T2.\"XCL_004\" GROUP BY T2.\"XCL_006\" ORDER BY COUNT(T2.\"XCL_004\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:254"
  ]
}
```

### Atom Type Flag

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_009\", T2.\"XCL_008\", T1.\"XCL_003\" AS flag_have_CaCl FROM atom AS T1 INNER JOIN connected AS T2 ON T2.\"XCL_007\" = T1.\"XCL_001\" WHERE T2.\"XCL_009\" = 'TR001_1_8' AND (T1.\"XCL_003\" = 'c1' OR T1.\"XCL_003\" = 'c')",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_003\" AS \"value\" FROM atom AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r1\".\"XCL_007\" = \"r0\".\"XCL_001\" WHERE \"r1\".\"XCL_009\" = 'TR001_1_8' AND (\"r0\".\"XCL_003\" = 'c1' OR \"r0\".\"XCL_003\" = 'c')",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:271"
  ]
}
```

### Molecule Identifier

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_004\" = 'TR001_10_11'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_011\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_011\" AS \"value\" FROM bond AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_005\" = \"r1\".\"XCL_010\" WHERE \"r0\".\"XCL_004\" = 'TR001_10_11'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:279"
  ]
}
```

### A property or identifier of an atom (XCL_003) from the atom table. It is returned for atoms that are part of positively charged molecules.

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_010\", T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:304"
  ]
}
```

### Distinct molecule identifiers (XCL_010) associated with bonds where the bond attribute XCL_006 is '-' and the molecule attribute XCL_011 is '-'. Grain

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_010\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_010\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '-' AND T2.\"XCL_011\" = '-' ORDER BY T2.\"XCL_010\" LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:232"
  ]
}
```

### "connected"."XCL_009" = 'TR004_8_9'

```json
{
  "kind": "predicate",
  "formula": "\"connected\".\"XCL_009\" = 'TR004_8_9'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T2.\"XCL_009\" = 'TR004_8_9'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:206"
  ]
}
```

### "bond"."XCL_006" = '='

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '='",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T2.\"XCL_010\"), SUM(CASE WHEN T2.\"XCL_011\" = '+' THEN 1 ELSE 0 END) FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '='",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:310"
  ]
}
```

### Distinct values of the molecule identifier (XCL_011) for molecules that contain at least one bond with the specific bond type or attribute 'TR001_2_4'

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_004\" = 'TR001_2_4'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:312"
  ]
}
```

### "bond"."XCL_006" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '-'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_010\", T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:259"
  ]
}
```

### "connected"."XCL_009" = 'TR001_1_7'

```json
{
  "kind": "predicate",
  "formula": "\"connected\".\"XCL_009\" = 'TR001_1_7'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_002\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T2.\"XCL_009\" = 'TR001_1_7'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:318"
  ]
}
```

### "atom"."XCL_001" = 'TR004_7' AND "molecule"."XCL_011" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_001\" = 'TR004_7' AND \"molecule\".\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_001\" = 'TR004_7' AND T2.\"XCL_011\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:334"
  ]
}
```

### Connection Attribute XCL_008

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_006\", T2.\"XCL_007\", T2.\"XCL_008\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T2.\"XCL_009\" = 'TR001_6_9'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_008\" AS \"value\" FROM bond AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_004\" = \"r1\".\"XCL_009\" WHERE \"r1\".\"XCL_009\" = 'TR001_6_9'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:236"
  ]
}
```

### Molecule XCL_010 Attribute

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_010\"",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_010\" FROM molecule AS T WHERE T.\"XCL_011\" = '-'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_010\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_010\" AS \"value\" FROM molecule AS \"r0\" WHERE \"r0\".\"XCL_011\" = '-'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:265"
  ]
}
```

### Count of distinct iodine atoms in single bonds

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT CASE WHEN \"atom\".\"XCL_003\" = 'i' THEN \"atom\".\"XCL_001\" ELSE NULL END)",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT CASE WHEN T1.\"XCL_003\" = 'i' THEN T1.\"XCL_001\" ELSE NULL END) AS iodine_nums, COUNT(DISTINCT CASE WHEN T1.\"XCL_003\" = 's' THEN T1.\"XCL_001\" ELSE NULL END) AS sulfur_nums FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" INNER JOIN bond AS T3 ON T2.\"XCL_009\" = T3.\"XCL_004\" WHERE T3.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT CASE WHEN \"r0\".\"XCL_003\" = 'i' THEN \"r0\".\"XCL_001\" ELSE NULL END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      },
      {
        "role": "r2",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT CASE WHEN \"r0\".\"XCL_003\" = 'i' THEN \"r0\".\"XCL_001\" ELSE NULL END) AS \"value\" FROM atom AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_007\" INNER JOIN bond AS \"r2\" ON \"r1\".\"XCL_009\" = \"r2\".\"XCL_004\" WHERE \"r2\".\"XCL_006\" = '-'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:215"
  ]
}
```

### Calculates the ratio of distinct molecules with a positive charge (XCL_011 = '+') to the total distinct molecules, expressed as a percentage. The popu

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(DISTINCT CASE WHEN \"molecule\".\"XCL_011\" = '+' THEN \"molecule\".\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(DISTINCT \"molecule\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(DISTINCT CASE WHEN T2.\"XCL_011\" = '+' THEN T2.\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(DISTINCT T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '#'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(DISTINCT CASE WHEN \"r1\".\"XCL_011\" = '+' THEN \"r1\".\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(DISTINCT \"r1\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      },
      {
        "role": "r2",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(DISTINCT CASE WHEN \"r1\".\"XCL_011\" = '+' THEN \"r1\".\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(DISTINCT \"r1\".\"XCL_010\") AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\" INNER JOIN bond AS \"r2\" ON \"r1\".\"XCL_010\" = \"r2\".\"XCL_005\" WHERE \"r2\".\"XCL_006\" = '#'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:219"
  ]
}
```

### "molecule"."XCL_011" = '+'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_011\" = '+'",
  "grain": [
    "\"molecule\".\"XCL_010\""
  ],
  "population_scope": "SELECT T2.\"XCL_010\", COUNT(T1.\"XCL_001\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+' GROUP BY T2.\"XCL_010\" ORDER BY COUNT(T1.\"XCL_001\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:329"
  ]
}
```

### "bond"."XCL_006" = '#'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '#'",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(DISTINCT CASE WHEN T2.\"XCL_011\" = '+' THEN T2.\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(DISTINCT T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '#'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:219"
  ]
}
```

### The specific molecule identifier (XCL_011) selected from the subquery that has the maximum count of hydrogen atoms. This is the output of the outer qu

```json
{
  "kind": "binding",
  "formula": "T.\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_011\" FROM (SELECT T2.\"XCL_011\", COUNT(T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'h' GROUP BY T2.\"XCL_011\" ORDER BY COUNT(T2.\"XCL_010\") DESC LIMIT 1) AS t",
  "upstream_scopes": [
    "SELECT T2.\"XCL_011\", COUNT(T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'h' GROUP BY T2.\"XCL_011\" ORDER BY COUNT(T2.\"XCL_010\") DESC LIMIT 1"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:208"
  ]
}
```

### Molecule Identifier

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_010\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_010\", T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:259"
  ]
}
```

### "atom"."XCL_002" = 'TR000'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_002\" = 'TR000'",
  "grain": [
    "\"atom\".\"XCL_001\"",
    "\"bond\".\"XCL_006\""
  ],
  "population_scope": "SELECT T1.\"XCL_001\", COUNT(DISTINCT T2.\"XCL_006\"), T1.\"XCL_002\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_002\" = 'TR000' GROUP BY T1.\"XCL_001\", T2.\"XCL_006\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:309"
  ]
}
```

### Aggregates the total number of rows in the molecule table where the XCL_010 identifier falls within the range 'TR000' to 'TR099' (inclusive) and the X

```json
{
  "kind": "metric",
  "formula": "COUNT(\"molecule\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T.\"XCL_010\") FROM molecule AS T WHERE \"XCL_010\" BETWEEN 'TR000' AND 'TR099' AND T.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_010\") AS \"value\" FROM molecule AS \"r0\" WHERE \"r0\".\"XCL_010\" BETWEEN 'TR000' AND 'TR099' AND \"r0\".\"XCL_011\" = '+'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:204"
  ]
}
```

### "atom"."XCL_002" BETWEEN 'TR010' AND 'TR050' AND "atom"."XCL_003" = 'c'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_002\" BETWEEN 'TR010' AND 'TR050' AND \"atom\".\"XCL_003\" = 'c'",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_001\" FROM atom AS T WHERE T.\"XCL_002\" BETWEEN 'TR010' AND 'TR050' AND T.\"XCL_003\" = 'c'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:292"
  ]
}
```

### "connected"."XCL_007" = 'TR004_8' AND "connected"."XCL_008" = 'TR004_20' OR "connected"."XCL_008" = 'TR004_8' AND "connected"."XCL_007" = 'TR004_20'

```json
{
  "kind": "predicate",
  "formula": "\"connected\".\"XCL_007\" = 'TR004_8' AND \"connected\".\"XCL_008\" = 'TR004_20' OR \"connected\".\"XCL_008\" = 'TR004_8' AND \"connected\".\"XCL_007\" = 'TR004_20'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_006\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T2.\"XCL_007\" = 'TR004_8' AND T2.\"XCL_008\" = 'TR004_20' OR T2.\"XCL_008\" = 'TR004_8' AND T2.\"XCL_007\" = 'TR004_20'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:213"
  ]
}
```

### "bond"."XCL_006" = '-' AND "atom"."XCL_003" = 'o'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '-' AND \"atom\".\"XCL_003\" = 'o'",
  "grain": [
    "\"atom\".\"XCL_002\""
  ],
  "population_scope": "SELECT T1.\"XCL_002\", COUNT(T1.\"XCL_003\") AS oxygen_count FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = '-' AND T1.\"XCL_003\" = 'o' GROUP BY T1.\"XCL_002\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:197"
  ]
}
```

### Count of Atoms in Single-Bonded Molecules

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT T.\"XCL_003\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T.\"XCL_003\") FROM (SELECT DISTINCT T2.\"XCL_010\", T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '-') AS T",
  "upstream_scopes": [
    "SELECT DISTINCT T2.\"XCL_010\", T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '-'"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:259"
  ]
}
```

### Molecule Identifier

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_010\"",
  "grain": [
    "\"molecule\".\"XCL_010\""
  ],
  "population_scope": "SELECT T1.\"XCL_010\", COUNT(T2.\"XCL_001\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" WHERE T1.\"XCL_011\" = '-' GROUP BY T1.\"XCL_010\" HAVING COUNT(T2.\"XCL_001\") > 5",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_010\"",
    "grain": [
      "\"r0\".\"XCL_010\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "molecule"
      },
      {
        "role": "r1",
        "physical_table": "atom"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_010\" AS \"grain_0\", \"r0\".\"XCL_010\" AS \"value\" FROM molecule AS \"r0\" INNER JOIN atom AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_002\" WHERE \"r0\".\"XCL_011\" = '-' GROUP BY \"r0\".\"XCL_010\" HAVING COUNT(\"r1\".\"XCL_001\") > 5",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:327"
  ]
}
```

### Atom Identifier

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T2.\"XCL_010\" = 'TR012' AND T3.\"XCL_006\" = '=' AND T1.\"XCL_003\" = 'c'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      },
      {
        "role": "r2",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\" INNER JOIN bond AS \"r2\" ON \"r1\".\"XCL_010\" = \"r2\".\"XCL_005\" WHERE \"r1\".\"XCL_010\" = 'TR012' AND \"r2\".\"XCL_006\" = '=' AND \"r0\".\"XCL_003\" = 'c'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:338"
  ]
}
```

### "atom"."XCL_003" = 'c' AND "molecule"."XCL_011" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 'c' AND \"molecule\".\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'c' AND T2.\"XCL_011\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:297"
  ]
}
```

### Hydrogen Atom Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"molecule\".\"XCL_010\")",
  "grain": [
    "\"molecule\".\"XCL_011\""
  ],
  "population_scope": "SELECT T2.\"XCL_011\", COUNT(T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'h' GROUP BY T2.\"XCL_011\" ORDER BY COUNT(T2.\"XCL_010\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:208"
  ]
}
```

### "molecule"."XCL_011" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_011\" = '-'",
  "grain": [
    "\"atom\".\"XCL_003\""
  ],
  "population_scope": "SELECT T1.\"XCL_003\", COUNT(DISTINCT T1.\"XCL_002\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '-' GROUP BY T1.\"XCL_003\" ORDER BY COUNT(DISTINCT T1.\"XCL_002\") ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:212"
  ]
}
```

### Connected Entity Identifier

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_009\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_009\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T1.\"XCL_002\" = 'TR006' ORDER BY T2.\"XCL_009\" LIMIT 2",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:233"
  ]
}
```

### Attribute XCL_007 from the connected table (T2), returned in the output. Represents a property of the connection associated with the bond.

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_004\", T2.\"XCL_007\", T2.\"XCL_008\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T1.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_007\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_007\" AS \"value\" FROM bond AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_004\" = \"r1\".\"XCL_009\" WHERE \"r0\".\"XCL_006\" = '-'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:305",
    "bird_dev:210"
  ]
}
```

### The final output identifier, representing the single molecule with the maximum atom count among those filtered by XCL_011 = '+'. It is the result of t

```json
{
  "kind": "binding",
  "formula": "T.\"XCL_010\"",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_010\" FROM (SELECT T2.\"XCL_010\", COUNT(T1.\"XCL_001\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+' GROUP BY T2.\"XCL_010\" ORDER BY COUNT(T1.\"XCL_001\") DESC LIMIT 1) AS t",
  "upstream_scopes": [
    "SELECT T2.\"XCL_010\", COUNT(T1.\"XCL_001\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+' GROUP BY T2.\"XCL_010\" ORDER BY COUNT(T1.\"XCL_001\") DESC LIMIT 1"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:329"
  ]
}
```

### "molecule"."XCL_010" BETWEEN 'TR000' AND 'TR099' AND "molecule"."XCL_011" = '+'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_010\" BETWEEN 'TR000' AND 'TR099' AND \"molecule\".\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": "SELECT COUNT(T.\"XCL_010\") FROM molecule AS T WHERE \"XCL_010\" BETWEEN 'TR000' AND 'TR099' AND T.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:204"
  ]
}
```

### "atom"."XCL_003" = 'c' AND "molecule"."XCL_011" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 'c' AND \"molecule\".\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_002\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'c' AND T2.\"XCL_011\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:316"
  ]
}
```

### Identifier for the molecule (XCL_011) from the 'molecule' table. Serves as the grouping key for the final aggregation.

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_001\", T1.\"XCL_003\", T1.\"XCL_002\", T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_010\" = 'TR006'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:282"
  ]
}
```

### Distinct values of atom.XCL_003 for atoms that do not appear in the set of connected atoms (defined by the join of atom and connected tables). Represe

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T.\"XCL_003\" FROM atom AS T WHERE NOT T.\"XCL_003\" IN (SELECT DISTINCT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\")",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:247"
  ]
}
```

### "bond"."XCL_006" = '#'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '#'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_004\", T2.\"XCL_011\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '#'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:280"
  ]
}
```

### Calculates the percentage of distinct positive molecules (where molecule.XCL_011 = '+') that contain at least one atom where atom.XCL_003 is not 'f'. 

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(DISTINCT CASE WHEN \"atom\".\"XCL_003\" <> 'f' THEN \"molecule\".\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(DISTINCT \"molecule\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(DISTINCT CASE WHEN T1.\"XCL_003\" <> 'f' THEN T2.\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(DISTINCT T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(DISTINCT CASE WHEN \"r0\".\"XCL_003\" <> 'f' THEN \"r1\".\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(DISTINCT \"r1\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(DISTINCT CASE WHEN \"r0\".\"XCL_003\" <> 'f' THEN \"r1\".\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(DISTINCT \"r1\".\"XCL_010\") AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\" WHERE \"r1\".\"XCL_011\" = '+'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:218"
  ]
}
```

### Aggregates the number of unique molecule identifiers (XCL_010) from the molecule table where the molecule charge (XCL_011) is '+' and the molecule is 

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"molecule\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+' AND T1.\"XCL_003\" = 'br'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r1\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r1\".\"XCL_010\") AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\" WHERE \"r1\".\"XCL_011\" = '+' AND \"r0\".\"XCL_003\" = 'br'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:235"
  ]
}
```

### "atom"."XCL_003" = 's'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 's'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_008\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T1.\"XCL_003\" = 's'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:257"
  ]
}
```

### "atom"."XCL_002" = 'TR206'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_002\" = 'TR206'",
  "grain": [],
  "population_scope": "SELECT ROUND(CAST(COUNT(CASE WHEN T.\"XCL_003\" = 'h' THEN T.\"XCL_001\" ELSE NULL END) AS REAL) * 100 / COUNT(T.\"XCL_001\"), 4) FROM atom AS T WHERE T.\"XCL_002\" = 'TR206'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:228"
  ]
}
```

### "atom"."XCL_003" = 'ca'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 'ca'",
  "grain": [
    "\"molecule\".\"XCL_011\""
  ],
  "population_scope": "SELECT T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'ca' GROUP BY T2.\"XCL_011\" ORDER BY COUNT(T2.\"XCL_011\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:270"
  ]
}
```

### A list of unique atom identifiers (XCL_001) that are part of molecules marked with a specific status ('-') and are present in the connected table. The

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_001\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN connected AS T3 ON T1.\"XCL_001\" = T3.\"XCL_007\" WHERE T2.\"XCL_011\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:211"
  ]
}
```

### Average Single Bond Count

```json
{
  "kind": "metric",
  "formula": "AVG(\"single_bond_count\")",
  "grain": [],
  "population_scope": "SELECT AVG(\"single_bond_count\") FROM (SELECT T3.\"XCL_010\", COUNT(T1.\"XCL_006\") AS single_bond_count FROM bond AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_005\" = T2.\"XCL_002\" INNER JOIN molecule AS T3 ON T3.\"XCL_010\" = T2.\"XCL_002\" WHERE T1.\"XCL_006\" = '-' AND T3.\"XCL_011\" = '+' GROUP BY T3.\"XCL_010\") AS subquery",
  "upstream_scopes": [
    "SELECT T3.\"XCL_010\", COUNT(T1.\"XCL_006\") AS single_bond_count FROM bond AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_005\" = T2.\"XCL_002\" INNER JOIN molecule AS T3 ON T3.\"XCL_010\" = T2.\"XCL_002\" WHERE T1.\"XCL_006\" = '-' AND T3.\"XCL_011\" = '+' GROUP BY T3.\"XCL_010\""
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:198"
  ]
}
```

### Atom Identifier

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM connected AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_007\" = T2.\"XCL_001\" WHERE T1.\"XCL_009\" = 'TR000_2_3'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "connected"
      },
      {
        "role": "r1",
        "physical_table": "atom"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_003\" AS \"value\" FROM connected AS \"r0\" INNER JOIN atom AS \"r1\" ON \"r0\".\"XCL_007\" = \"r1\".\"XCL_001\" WHERE \"r0\".\"XCL_009\" = 'TR000_2_3'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:307"
  ]
}
```

### Molecule XCL_011 Attribute

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_011\" FROM molecule AS T WHERE T.\"XCL_010\" = 'TR124'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_011\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_011\" AS \"value\" FROM molecule AS \"r0\" WHERE \"r0\".\"XCL_010\" = 'TR124'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:299"
  ]
}
```

### "molecule"."XCL_010" = 'TR000'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_010\" = 'TR000'",
  "grain": [],
  "population_scope": "SELECT \"XCL_011\" FROM molecule AS T WHERE T.\"XCL_010\" = 'TR000'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:323"
  ]
}
```

### Returns the value of column XCL_002 from the atom table, restricted to rows where XCL_003 equals 'c'. The grain is individual atom records matching th

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_002\" FROM atom AS T WHERE T.\"XCL_003\" = 'c'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_002\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_002\" AS \"value\" FROM atom AS \"r0\" WHERE \"r0\".\"XCL_003\" = 'c'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:205"
  ]
}
```

### "atom"."XCL_002" = 'TR000'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_002\" = 'TR000'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T.\"XCL_003\" FROM atom AS T WHERE T.\"XCL_002\" = 'TR000' ORDER BY T.\"XCL_003\" LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:220"
  ]
}
```

### "molecule"."XCL_011" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_011\" = '-'",
  "grain": [
    "\"molecule\".\"XCL_010\""
  ],
  "population_scope": "SELECT T1.\"XCL_010\", COUNT(T2.\"XCL_001\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" WHERE T1.\"XCL_011\" = '-' GROUP BY T1.\"XCL_010\" HAVING COUNT(T2.\"XCL_001\") > 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:327"
  ]
}
```

### "atom"."XCL_003" = 'h'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 'h'",
  "grain": [
    "\"molecule\".\"XCL_011\""
  ],
  "population_scope": "SELECT T2.\"XCL_011\", COUNT(T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'h' GROUP BY T2.\"XCL_011\" ORDER BY COUNT(T2.\"XCL_010\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:208"
  ]
}
```

### "bond"."XCL_005" = 'TR010'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_005\" = 'TR010'",
  "grain": [
    "\"bond\".\"XCL_006\""
  ],
  "population_scope": "SELECT T1.\"XCL_006\", COUNT(T1.\"XCL_005\") FROM bond AS T1 WHERE T1.\"XCL_005\" = 'TR010' GROUP BY T1.\"XCL_006\" ORDER BY COUNT(T1.\"XCL_005\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:231"
  ]
}
```

### Average Oxygen Bond Count

```json
{
  "kind": "metric",
  "formula": "AVG(\"oxygen_count\")",
  "grain": [],
  "population_scope": "SELECT AVG(\"oxygen_count\") FROM (SELECT T1.\"XCL_002\", COUNT(T1.\"XCL_003\") AS oxygen_count FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = '-' AND T1.\"XCL_003\" = 'o' GROUP BY T1.\"XCL_002\") AS oxygen_counts",
  "upstream_scopes": [
    "SELECT T1.\"XCL_002\", COUNT(T1.\"XCL_003\") AS oxygen_count FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = '-' AND T1.\"XCL_003\" = 'o' GROUP BY T1.\"XCL_002\""
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:197"
  ]
}
```

### Bond Attribute XCL_006

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_006\" FROM bond AS T WHERE T.\"XCL_004\" = 'TR007_4_19'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_006\" AS \"value\" FROM bond AS \"r0\" WHERE \"r0\".\"XCL_004\" = 'TR007_4_19'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:301"
  ]
}
```

### Atom Identifier

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'c' AND T2.\"XCL_011\" = '-'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\" WHERE \"r0\".\"XCL_003\" = 'c' AND \"r1\".\"XCL_011\" = '-'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:297"
  ]
}
```

### Identifier for an atom (XCL_001) that is part of a molecule and connected via a bond with type '-'. Used as the counting unit for the total population

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      },
      {
        "role": "r2",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\" INNER JOIN bond AS \"r2\" ON \"r1\".\"XCL_010\" = \"r2\".\"XCL_005\" WHERE \"r2\".\"XCL_006\" = '-'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:263"
  ]
}
```

### Molecule Identifier

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_010\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_010\", IIF(T2.\"XCL_011\" = '+', 'YES', 'NO') AS flag_carcinogenic FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_001\" = 'TR001_10'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_010\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_010\" AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\" WHERE \"r0\".\"XCL_001\" = 'TR001_10'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:237"
  ]
}
```

### "bond"."XCL_006" = '#'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '#'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_005\", T2.\"XCL_003\" FROM bond AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_005\" = T2.\"XCL_002\" WHERE T1.\"XCL_006\" = '#'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:306"
  ]
}
```

### Bond Identifier

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_004\", T2.\"XCL_007\", T2.\"XCL_008\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T1.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_004\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_004\" AS \"value\" FROM bond AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_004\" = \"r1\".\"XCL_009\" WHERE \"r0\".\"XCL_006\" = '-'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:305"
  ]
}
```

### "molecule"."XCL_010" = 'TR124'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_010\" = 'TR124'",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_011\" FROM molecule AS T WHERE T.\"XCL_010\" = 'TR124'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:299"
  ]
}
```

### Counts the number of unique molecules (identified by XCL_010) that are associated with at least one double bond (XCL_006 = '='). The grain is the aggr

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"molecule\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T2.\"XCL_010\"), SUM(CASE WHEN T2.\"XCL_011\" = '+' THEN 1 ELSE 0 END) FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '='",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r1\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r1\".\"XCL_010\") AS \"value\" FROM bond AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_005\" = \"r1\".\"XCL_010\" WHERE \"r0\".\"XCL_006\" = '='",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:310"
  ]
}
```

### "bond"."XCL_006" = '#'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '#'",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T.\"XCL_005\") FROM bond AS T WHERE T.\"XCL_006\" = '#'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:238"
  ]
}
```

### "bond"."XCL_006" = '#' AND "atom"."XCL_003" IN ('p', 'br')

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '#' AND \"atom\".\"XCL_003\" IN ('p', 'br')",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '#' AND T1.\"XCL_003\" IN ('p', 'br')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:260"
  ]
}
```

### "molecule"."XCL_011" = '-' AND "bond"."XCL_006" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_011\" = '-' AND \"bond\".\"XCL_006\" = '-'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_005\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '-' AND T1.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:262"
  ]
}
```

### Molecule Identifier

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_010\"",
  "grain": [
    "\"molecule\".\"XCL_010\""
  ],
  "population_scope": "SELECT T2.\"XCL_010\", COUNT(T1.\"XCL_001\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+' GROUP BY T2.\"XCL_010\" ORDER BY COUNT(T1.\"XCL_001\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:329"
  ]
}
```

### Count of distinct atoms with double bonds

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"atom\".\"XCL_002\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_002\") FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = '=' AND T1.\"XCL_003\" = 'o'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_002\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r0\".\"XCL_002\") AS \"value\" FROM atom AS \"r0\" INNER JOIN bond AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_005\" WHERE \"r1\".\"XCL_006\" = '=' AND \"r0\".\"XCL_003\" = 'o'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:335"
  ]
}
```

### "bond"."XCL_006" = '#' AND "bond"."XCL_005" = 'TR041'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '#' AND \"bond\".\"XCL_005\" = 'TR041'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_007\", T2.\"XCL_008\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" INNER JOIN bond AS T3 ON T2.\"XCL_009\" = T3.\"XCL_004\" WHERE T3.\"XCL_006\" = '#' AND T3.\"XCL_005\" = 'TR041'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:248"
  ]
}
```

### "molecule"."XCL_011" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_001\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN connected AS T3 ON T1.\"XCL_001\" = T3.\"XCL_007\" WHERE T2.\"XCL_011\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:211"
  ]
}
```

### "bond"."XCL_005" = 'TR000'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_005\" = 'TR000'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T.\"XCL_006\" FROM bond AS T WHERE T.\"XCL_005\" = 'TR000'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:229"
  ]
}
```

### Connection Attribute XCL_007

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_006\", T2.\"XCL_007\", T2.\"XCL_008\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T2.\"XCL_009\" = 'TR001_6_9'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_007\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_007\" AS \"value\" FROM bond AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_004\" = \"r1\".\"XCL_009\" WHERE \"r1\".\"XCL_009\" = 'TR001_6_9'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:236"
  ]
}
```

### Bond Identifier

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_005\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_005\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '-' AND T1.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:262"
  ]
}
```

### Bond Identifier

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_005\"",
  "grain": [
    "\"bond\".\"XCL_005\""
  ],
  "population_scope": "SELECT T.\"XCL_005\", COUNT(T.\"XCL_006\") FROM bond AS T WHERE T.\"XCL_006\" = '=' GROUP BY T.\"XCL_005\" ORDER BY COUNT(T.\"XCL_006\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:244"
  ]
}
```

### Grouping Key: Molecule ID

```json
{
  "kind": "binding",
  "formula": "\"XCL_011\"",
  "grain": [
    "\"molecule\".\"XCL_011\""
  ],
  "population_scope": "WITH SubQuery AS (SELECT DISTINCT T1.\"XCL_001\", T1.\"XCL_003\", T1.\"XCL_002\", T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_010\" = 'TR006') SELECT CAST(COUNT(CASE WHEN \"XCL_003\" = 'h' THEN \"XCL_001\" ELSE NULL END) AS REAL) / (CASE WHEN COUNT(\"XCL_001\") = 0 THEN NULL ELSE COUNT(\"XCL_001\") END) AS ratio, \"XCL_011\" FROM SubQuery GROUP BY \"XCL_011\"",
  "upstream_scopes": [
    "SELECT DISTINCT T1.\"XCL_001\", T1.\"XCL_003\", T1.\"XCL_002\", T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_010\" = 'TR006'"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:282"
  ]
}
```

### Calculates the ratio of distinct molecules (identified by XCL_010) that have a positive charge (XCL_011 = '+') and contain at least one chlorine atom 

```json
{
  "kind": "metric",
  "formula": "COUNT(CASE WHEN \"molecule\".\"XCL_011\" = '+' AND \"atom\".\"XCL_003\" = 'cl' THEN \"molecule\".\"XCL_010\" ELSE NULL END) * 100 / COUNT(\"molecule\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(CASE WHEN T2.\"XCL_011\" = '+' AND T1.\"XCL_003\" = 'cl' THEN T2.\"XCL_010\" ELSE NULL END) * 100 / COUNT(T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(CASE WHEN \"r1\".\"XCL_011\" = '+' AND \"r0\".\"XCL_003\" = 'cl' THEN \"r1\".\"XCL_010\" ELSE NULL END) * 100 / COUNT(\"r1\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT COUNT(CASE WHEN \"r1\".\"XCL_011\" = '+' AND \"r0\".\"XCL_003\" = 'cl' THEN \"r1\".\"XCL_010\" ELSE NULL END) * 100 / COUNT(\"r1\".\"XCL_010\") AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:317"
  ]
}
```

### Atom Bond Reference

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_002\"",
  "grain": [
    "\"atom\".\"XCL_001\"",
    "\"bond\".\"XCL_006\""
  ],
  "population_scope": "SELECT T1.\"XCL_001\", COUNT(DISTINCT T2.\"XCL_006\"), T1.\"XCL_002\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_002\" = 'TR000' GROUP BY T1.\"XCL_001\", T2.\"XCL_006\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:309"
  ]
}
```

### "molecule"."XCL_011" = '+'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(DISTINCT CASE WHEN T1.\"XCL_003\" <> 'f' THEN T2.\"XCL_010\" ELSE NULL END) AS REAL) * 100 / COUNT(DISTINCT T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:218"
  ]
}
```

### Bond Attribute

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_005\", T2.\"XCL_006\" FROM molecule AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_010\" = T2.\"XCL_005\" WHERE T1.\"XCL_010\" BETWEEN 'TR000' AND 'TR050'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "molecule"
      },
      {
        "role": "r1",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_006\" AS \"value\" FROM molecule AS \"r0\" INNER JOIN bond AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_005\" WHERE \"r0\".\"XCL_010\" BETWEEN 'TR000' AND 'TR050'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:267"
  ]
}
```

### Distinct Atom XCL_003

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" INNER JOIN connected AS T3 ON T1.\"XCL_001\" = T3.\"XCL_007\" WHERE T2.\"XCL_006\" = '='",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:207"
  ]
}
```

### Molecule Identifier

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_010\"",
  "grain": [
    "\"molecule\".\"XCL_010\""
  ],
  "population_scope": "SELECT T3.\"XCL_010\", COUNT(T1.\"XCL_006\") AS single_bond_count FROM bond AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_005\" = T2.\"XCL_002\" INNER JOIN molecule AS T3 ON T3.\"XCL_010\" = T2.\"XCL_002\" WHERE T1.\"XCL_006\" = '-' AND T3.\"XCL_011\" = '+' GROUP BY T3.\"XCL_010\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_010\"",
    "grain": [
      "\"r2\".\"XCL_010\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "atom"
      },
      {
        "role": "r2",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_010\" AS \"grain_0\", \"r2\".\"XCL_010\" AS \"value\" FROM bond AS \"r0\" INNER JOIN atom AS \"r1\" ON \"r0\".\"XCL_005\" = \"r1\".\"XCL_002\" INNER JOIN molecule AS \"r2\" ON \"r2\".\"XCL_010\" = \"r1\".\"XCL_002\" WHERE \"r0\".\"XCL_006\" = '-' AND \"r2\".\"XCL_011\" = '+' GROUP BY \"r2\".\"XCL_010\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:198"
  ]
}
```

### "bond"."XCL_006" = '='

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '='",
  "grain": [],
  "population_scope": "SELECT DISTINCT T.\"XCL_005\" FROM bond AS T WHERE T.\"XCL_006\" = '=' ORDER BY T.\"XCL_005\" LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:225"
  ]
}
```

### Bond Atom Identifier

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_005\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_005\", T2.\"XCL_003\" FROM bond AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_005\" = T2.\"XCL_002\" WHERE T1.\"XCL_006\" = '#'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:306"
  ]
}
```

### Molecule Identifier

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_010\"",
  "grain": [
    "\"molecule\".\"XCL_010\""
  ],
  "population_scope": "SELECT T3.\"XCL_010\", COUNT(T1.\"XCL_006\") FROM bond AS T1 INNER JOIN molecule AS T3 ON T1.\"XCL_005\" = T3.\"XCL_010\" WHERE T3.\"XCL_011\" = '+' AND T1.\"XCL_006\" = '=' GROUP BY T3.\"XCL_010\" ORDER BY COUNT(T1.\"XCL_006\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:250"
  ]
}
```

### Calculates the percentage of rows in the 'bond' table where the column 'XCL_006' contains the value '#'. The numerator counts non-null 'XCL_004' value

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN \"bond\".\"XCL_006\" = '#' THEN \"bond\".\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(\"bond\".\"XCL_004\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T.\"XCL_006\" = '#' THEN T.\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(T.\"XCL_004\") FROM bond AS T",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(CASE WHEN \"r0\".\"XCL_006\" = '#' THEN \"r0\".\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_004\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(CASE WHEN \"r0\".\"XCL_006\" = '#' THEN \"r0\".\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_004\") AS \"value\" FROM bond AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:286"
  ]
}
```

### "atom"."XCL_003" <> 's' AND "bond"."XCL_006" <> '='

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" <> 's' AND \"bond\".\"XCL_006\" <> '='",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_002\") FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_003\" <> 's' AND T2.\"XCL_006\" <> '='",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:311"
  ]
}
```

### Bond Identifier

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_004\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+' AND T1.\"XCL_006\" = '='",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_004\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_004\" AS \"value\" FROM bond AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_005\" = \"r1\".\"XCL_010\" WHERE \"r1\".\"XCL_011\" = '+' AND \"r0\".\"XCL_006\" = '='",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:294"
  ]
}
```

### Aggregates the number of unique molecule identifiers (XCL_010) from the molecule table. The population is restricted to molecules that are joined to b

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"molecule\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_010\") FROM molecule AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_010\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = '#' AND T1.\"XCL_011\" = '-'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "molecule"
      },
      {
        "role": "r1",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r0\".\"XCL_010\") AS \"value\" FROM molecule AS \"r0\" INNER JOIN bond AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_005\" WHERE \"r1\".\"XCL_006\" = '#' AND \"r0\".\"XCL_011\" = '-'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:336"
  ]
}
```

### "atom"."XCL_003" = 'p'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 'p'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_009\" FROM connected AS T3 INNER JOIN atom AS T4 ON T3.\"XCL_007\" = T4.\"XCL_001\" WHERE T4.\"XCL_003\" = 'p'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:243"
  ]
}
```

### "atom"."XCL_002" = 'TR186'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_002\" = 'TR186'",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_001\" FROM atom AS T WHERE T.\"XCL_002\" = 'TR186'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:300"
  ]
}
```

### Atom Identifier

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_002\"",
  "grain": [
    "\"atom\".\"XCL_002\""
  ],
  "population_scope": "SELECT T1.\"XCL_002\", COUNT(T1.\"XCL_003\") AS oxygen_count FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = '-' AND T1.\"XCL_003\" = 'o' GROUP BY T1.\"XCL_002\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_002\"",
    "grain": [
      "\"r0\".\"XCL_002\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_002\" AS \"grain_0\", \"r0\".\"XCL_002\" AS \"value\" FROM atom AS \"r0\" INNER JOIN bond AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_005\" WHERE \"r1\".\"XCL_006\" = '-' AND \"r0\".\"XCL_003\" = 'o' GROUP BY \"r0\".\"XCL_002\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:197"
  ]
}
```

### "connected"."XCL_007" = 'TR000_1' AND "bond"."XCL_004" = 'TR000_1_2'

```json
{
  "kind": "predicate",
  "formula": "\"connected\".\"XCL_007\" = 'TR000_1' AND \"bond\".\"XCL_004\" = 'TR000_1_2'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_005\", T2.\"XCL_004\", T1.\"XCL_007\" FROM connected AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_009\" = T2.\"XCL_004\" WHERE T1.\"XCL_007\" = 'TR000_1' AND T2.\"XCL_004\" = 'TR000_1_2'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:296"
  ]
}
```

### "atom"."XCL_003" = 'c'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 'c'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_006\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_003\" = 'c'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:284"
  ]
}
```

### Distinct Bond Identifier

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_006\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_003\" = 'c'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:284"
  ]
}
```

### "atom"."XCL_003" = 's' AND "bond"."XCL_006" = '='

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 's' AND \"bond\".\"XCL_006\" = '='",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_002\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_003\" = 's' AND T2.\"XCL_006\" = '='",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:326"
  ]
}
```

### Distinct values of the molecule identifier column (XCL_011) from the molecule table. The population is restricted to molecules that contain at least o

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" <> 'sn'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:214"
  ]
}
```

### "atom"."XCL_003" = 'sn'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 'sn'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_006\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" INNER JOIN bond AS T3 ON T3.\"XCL_004\" = T2.\"XCL_009\" WHERE T1.\"XCL_003\" = 'sn'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:258"
  ]
}
```

### "bond"."XCL_004" = 'TR001_10_11'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_004\" = 'TR001_10_11'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_004\" = 'TR001_10_11'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:279"
  ]
}
```

### Least Frequent Atom Type in Negative Molecules

```json
{
  "kind": "binding",
  "formula": "T.\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_003\" FROM (SELECT T1.\"XCL_003\", COUNT(DISTINCT T1.\"XCL_002\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '-' GROUP BY T1.\"XCL_003\" ORDER BY COUNT(DISTINCT T1.\"XCL_002\") ASC LIMIT 1) AS t",
  "upstream_scopes": [
    "SELECT T1.\"XCL_003\", COUNT(DISTINCT T1.\"XCL_002\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '-' GROUP BY T1.\"XCL_003\" ORDER BY COUNT(DISTINCT T1.\"XCL_002\") ASC LIMIT 1"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:212"
  ]
}
```

### Distinct Bond Count

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"bond\".\"XCL_006\")",
  "grain": [
    "\"atom\".\"XCL_001\"",
    "\"bond\".\"XCL_006\""
  ],
  "population_scope": "SELECT T1.\"XCL_001\", COUNT(DISTINCT T2.\"XCL_006\"), T1.\"XCL_002\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_002\" = 'TR000' GROUP BY T1.\"XCL_001\", T2.\"XCL_006\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r1\".\"XCL_006\")",
    "grain": [
      "\"r0\".\"XCL_001\"",
      "\"r1\".\"XCL_006\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"grain_0\", \"r1\".\"XCL_006\" AS \"grain_1\", COUNT(DISTINCT \"r1\".\"XCL_006\") AS \"value\" FROM atom AS \"r0\" INNER JOIN bond AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_005\" WHERE \"r0\".\"XCL_002\" = 'TR000' GROUP BY \"r0\".\"XCL_001\", \"r1\".\"XCL_006\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:309"
  ]
}
```

### "bond"."XCL_006" = '#'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '#'",
  "grain": [],
  "population_scope": "SELECT COUNT(T.\"XCL_004\") FROM bond AS T WHERE T.\"XCL_006\" = '#'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:202"
  ]
}
```

### Distinct XCL_003 values

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T.\"XCL_003\" FROM atom AS T WHERE T.\"XCL_002\" = 'TR151'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:290"
  ]
}
```

### "bond"."XCL_006" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '-'",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT CASE WHEN T1.\"XCL_003\" = 'i' THEN T1.\"XCL_001\" ELSE NULL END) AS iodine_nums, COUNT(DISTINCT CASE WHEN T1.\"XCL_003\" = 's' THEN T1.\"XCL_001\" ELSE NULL END) AS sulfur_nums FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" INNER JOIN bond AS T3 ON T2.\"XCL_009\" = T3.\"XCL_004\" WHERE T3.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:215"
  ]
}
```

### Distinct Atom Identifier

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+' AND SUBSTRING(T1.\"XCL_001\", -1) = '4' AND LENGTH(T1.\"XCL_001\") = 7",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:281"
  ]
}
```

### The value of column XCL_001 from the atom table, filtered to rows where XCL_002 is between 'TR010' and 'TR050' and XCL_003 equals 'c'.

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_001\" FROM atom AS T WHERE T.\"XCL_002\" BETWEEN 'TR010' AND 'TR050' AND T.\"XCL_003\" = 'c'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM atom AS \"r0\" WHERE \"r0\".\"XCL_002\" BETWEEN 'TR010' AND 'TR050' AND \"r0\".\"XCL_003\" = 'c'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:292"
  ]
}
```

### Atom Identifier

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_001\"",
  "grain": [
    "\"atom\".\"XCL_001\"",
    "\"bond\".\"XCL_006\""
  ],
  "population_scope": "SELECT T1.\"XCL_001\", COUNT(DISTINCT T2.\"XCL_006\"), T1.\"XCL_002\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_002\" = 'TR000' GROUP BY T1.\"XCL_001\", T2.\"XCL_006\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [
      "\"r0\".\"XCL_001\"",
      "\"r1\".\"XCL_006\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"grain_0\", \"r1\".\"XCL_006\" AS \"grain_1\", \"r0\".\"XCL_001\" AS \"value\" FROM atom AS \"r0\" INNER JOIN bond AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_005\" WHERE \"r0\".\"XCL_002\" = 'TR000' GROUP BY \"r0\".\"XCL_001\", \"r1\".\"XCL_006\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:309"
  ]
}
```

### "connected"."XCL_009" = 'TR001_1_8' AND ("atom"."XCL_003" = 'c1' OR "atom"."XCL_003" = 'c')

```json
{
  "kind": "predicate",
  "formula": "\"connected\".\"XCL_009\" = 'TR001_1_8' AND (\"atom\".\"XCL_003\" = 'c1' OR \"atom\".\"XCL_003\" = 'c')",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_009\", T2.\"XCL_008\", T1.\"XCL_003\" AS flag_have_CaCl FROM atom AS T1 INNER JOIN connected AS T2 ON T2.\"XCL_007\" = T1.\"XCL_001\" WHERE T2.\"XCL_009\" = 'TR001_1_8' AND (T1.\"XCL_003\" = 'c1' OR T1.\"XCL_003\" = 'c')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:271"
  ]
}
```

### "atom"."XCL_001" = 'TR001_10'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_001\" = 'TR001_10'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_010\", IIF(T2.\"XCL_011\" = '+', 'YES', 'NO') AS flag_carcinogenic FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_001\" = 'TR001_10'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:237"
  ]
}
```

### Atom Identifier

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_003\", T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_010\" = 'TR060'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:230"
  ]
}
```

### "atom"."XCL_003" = 'n' AND "molecule"."XCL_011" = '+'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 'n' AND \"molecule\".\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_010\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'n' AND T1.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:325"
  ]
}
```

### Distinct XCL_005 values

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_005\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T.\"XCL_005\" FROM bond AS T WHERE T.\"XCL_006\" = '='",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:275"
  ]
}
```

### Counts the number of bond-molecule associations where the molecule attribute XCL_011 is '+', restricted to double bonds (XCL_006 = '='). This is a con

```json
{
  "kind": "metric",
  "formula": "SUM(CASE WHEN \"molecule\".\"XCL_011\" = '+' THEN 1 ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T2.\"XCL_010\"), SUM(CASE WHEN T2.\"XCL_011\" = '+' THEN 1 ELSE 0 END) FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '='",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(CASE WHEN \"r1\".\"XCL_011\" = '+' THEN 1 ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT SUM(CASE WHEN \"r1\".\"XCL_011\" = '+' THEN 1 ELSE 0 END) AS \"value\" FROM bond AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_005\" = \"r1\".\"XCL_010\" WHERE \"r0\".\"XCL_006\" = '='",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:310"
  ]
}
```

### Calculates the percentage of atoms with type 'cl' among all atoms in molecules marked as positive. The population is restricted to atoms joined to mol

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN \"atom\".\"XCL_003\" = 'cl' THEN \"atom\".\"XCL_003\" ELSE NULL END) AS REAL) * 100 / COUNT(\"atom\".\"XCL_003\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T1.\"XCL_003\" = 'cl' THEN T1.\"XCL_003\" ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_003\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(CASE WHEN \"r0\".\"XCL_003\" = 'cl' THEN \"r0\".\"XCL_003\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_003\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(CASE WHEN \"r0\".\"XCL_003\" = 'cl' THEN \"r0\".\"XCL_003\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_003\") AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\" WHERE \"r1\".\"XCL_011\" = '+'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:273"
  ]
}
```

### Connection ID linked to nitrogen atoms intersecting phosphorus connections

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_009\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_009\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T2.\"XCL_009\" IN (SELECT T3.\"XCL_009\" FROM connected AS T3 INNER JOIN atom AS T4 ON T3.\"XCL_007\" = T4.\"XCL_001\" WHERE T4.\"XCL_003\" = 'p') AND T1.\"XCL_003\" = 'n'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:243"
  ]
}
```

### Aggregates the count of non-null values in the XCL_010 column from the molecule table, restricted to rows where XCL_011 equals '-'. Returns a single s

```json
{
  "kind": "metric",
  "formula": "COUNT(\"molecule\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T.\"XCL_010\") FROM molecule AS T WHERE T.\"XCL_011\" = '-'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_010\") AS \"value\" FROM molecule AS \"r0\" WHERE \"r0\".\"XCL_011\" = '-'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:241"
  ]
}
```

### Bond Identifier

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_006\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" INNER JOIN bond AS T3 ON T3.\"XCL_004\" = T2.\"XCL_009\" WHERE T1.\"XCL_003\" = 'sn'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:258"
  ]
}
```

### "atom"."XCL_003" <> 'br'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" <> 'br'",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T.\"XCL_001\") FROM atom AS T WHERE T.\"XCL_003\" <> 'br'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:203"
  ]
}
```

### "atom"."XCL_003" = 'na' AND "molecule"."XCL_011" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 'na' AND \"molecule\".\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T2.\"XCL_010\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'na' AND T2.\"XCL_011\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:199"
  ]
}
```

### Distinct Atom Count

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"atom\".\"XCL_002\")",
  "grain": [
    "\"atom\".\"XCL_003\""
  ],
  "population_scope": "SELECT T2.\"XCL_003\", COUNT(DISTINCT T2.\"XCL_002\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" WHERE T1.\"XCL_011\" = '+' GROUP BY T2.\"XCL_003\" ORDER BY COUNT(DISTINCT T2.\"XCL_002\") LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:251"
  ]
}
```

### Distinct Atom Identifier

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_002\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T2.\"XCL_009\" = 'TR001_1_7'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:318"
  ]
}
```

### "bond"."XCL_006" = '#' AND "atom"."XCL_003" = 'h'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '#' AND \"atom\".\"XCL_003\" = 'h'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T1.\"XCL_011\" = '+' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(DISTINCT T1.\"XCL_010\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" INNER JOIN bond AS T3 ON T1.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '#' AND T2.\"XCL_003\" = 'h'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:330"
  ]
}
```

### Aggregates the count of non-null values in column XCL_001 from the atom table, restricted to rows where XCL_002 equals 'TR001'. Returns a single scala

```json
{
  "kind": "metric",
  "formula": "COUNT(\"atom\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T.\"XCL_001\") FROM atom AS T WHERE T.\"XCL_002\" = 'TR001'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM atom AS \"r0\" WHERE \"r0\".\"XCL_002\" = 'TR001'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:313"
  ]
}
```

### Aggregates the count of non-null values in column XCL_004 from the bond table, restricted to rows where column XCL_006 equals the literal string '#'. 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"bond\".\"XCL_004\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T.\"XCL_004\") FROM bond AS T WHERE T.\"XCL_006\" = '#'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_004\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_004\") AS \"value\" FROM bond AS \"r0\" WHERE \"r0\".\"XCL_006\" = '#'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:202"
  ]
}
```

### "atom"."XCL_002" = 'TR004'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_002\" = 'TR004'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T.\"XCL_003\" FROM atom AS T WHERE T.\"XCL_002\" = 'TR004'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:240"
  ]
}
```

### Aggregates the count of unique molecule identifiers (XCL_010) from the molecule table. The population is restricted to molecules where the attribute X

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"molecule\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_010\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'n' AND T1.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "molecule"
      },
      {
        "role": "r1",
        "physical_table": "atom"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r0\".\"XCL_010\") AS \"value\" FROM molecule AS \"r0\" INNER JOIN atom AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_002\" WHERE \"r1\".\"XCL_003\" = 'n' AND \"r0\".\"XCL_011\" = '+'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:325"
  ]
}
```

### Bond Identifier XCL_004

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_005\", T2.\"XCL_004\", T1.\"XCL_007\" FROM connected AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_009\" = T2.\"XCL_004\" WHERE T1.\"XCL_007\" = 'TR000_1' AND T2.\"XCL_004\" = 'TR000_1_2'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_004\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "connected"
      },
      {
        "role": "r1",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_004\" AS \"value\" FROM connected AS \"r0\" INNER JOIN bond AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_004\" WHERE \"r0\".\"XCL_007\" = 'TR000_1' AND \"r1\".\"XCL_004\" = 'TR000_1_2'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:296"
  ]
}
```

### The single value of XCL_006 selected from the subquery, corresponding to the group with the maximum count of XCL_005 entries equal to 'TR010'.

```json
{
  "kind": "binding",
  "formula": "T.\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_006\" FROM (SELECT T1.\"XCL_006\", COUNT(T1.\"XCL_005\") FROM bond AS T1 WHERE T1.\"XCL_005\" = 'TR010' GROUP BY T1.\"XCL_006\" ORDER BY COUNT(T1.\"XCL_005\") DESC LIMIT 1) AS T",
  "upstream_scopes": [
    "SELECT T1.\"XCL_006\", COUNT(T1.\"XCL_005\") FROM bond AS T1 WHERE T1.\"XCL_005\" = 'TR010' GROUP BY T1.\"XCL_006\" ORDER BY COUNT(T1.\"XCL_005\") DESC LIMIT 1"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:231"
  ]
}
```

### Connected Atom ID

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_007\", T2.\"XCL_008\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T1.\"XCL_003\" = 'pb'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_007\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_007\" AS \"value\" FROM atom AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_007\" WHERE \"r0\".\"XCL_003\" = 'pb'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:252"
  ]
}
```

### "atom"."XCL_003" = 'c'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 'c'",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_002\" FROM atom AS T WHERE T.\"XCL_003\" = 'c'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:205"
  ]
}
```

### Distinct Atom Identifier

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T2.\"XCL_009\" = 'TR001_2_4'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:302"
  ]
}
```

### Counts the number of unique values in the atom.XCL_003 column. The population is restricted to atoms that are connected to a specific connection recor

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"atom\".\"XCL_003\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_003\") FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T2.\"XCL_009\" = 'TR001_3_4'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_003\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r0\".\"XCL_003\") AS \"value\" FROM atom AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_007\" WHERE \"r1\".\"XCL_009\" = 'TR001_3_4'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:319"
  ]
}
```

### "connected"."XCL_009" = 'TR001_10_11'

```json
{
  "kind": "predicate",
  "formula": "\"connected\".\"XCL_009\" = 'TR001_10_11'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM connected AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_007\" = T2.\"XCL_001\" WHERE T1.\"XCL_009\" = 'TR001_10_11'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:268"
  ]
}
```

### The single atom type identifier (XCL_003) that has the highest count of distinct associated atoms within positive molecules. This is the final output 

```json
{
  "kind": "binding",
  "formula": "T.\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_003\" FROM (SELECT T2.\"XCL_003\", COUNT(DISTINCT T2.\"XCL_002\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" WHERE T1.\"XCL_011\" = '+' GROUP BY T2.\"XCL_003\" ORDER BY COUNT(DISTINCT T2.\"XCL_002\") LIMIT 1) AS t",
  "upstream_scopes": [
    "SELECT T2.\"XCL_003\", COUNT(DISTINCT T2.\"XCL_002\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" WHERE T1.\"XCL_011\" = '+' GROUP BY T2.\"XCL_003\" ORDER BY COUNT(DISTINCT T2.\"XCL_002\") LIMIT 1"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:251"
  ]
}
```

### Single Bond Count per Molecule

```json
{
  "kind": "metric",
  "formula": "COUNT(\"bond\".\"XCL_006\")",
  "grain": [
    "\"molecule\".\"XCL_010\""
  ],
  "population_scope": "SELECT T3.\"XCL_010\", COUNT(T1.\"XCL_006\") AS single_bond_count FROM bond AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_005\" = T2.\"XCL_002\" INNER JOIN molecule AS T3 ON T3.\"XCL_010\" = T2.\"XCL_002\" WHERE T1.\"XCL_006\" = '-' AND T3.\"XCL_011\" = '+' GROUP BY T3.\"XCL_010\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_006\")",
    "grain": [
      "\"r2\".\"XCL_010\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "atom"
      },
      {
        "role": "r2",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_010\" AS \"grain_0\", COUNT(\"r0\".\"XCL_006\") AS \"value\" FROM bond AS \"r0\" INNER JOIN atom AS \"r1\" ON \"r0\".\"XCL_005\" = \"r1\".\"XCL_002\" INNER JOIN molecule AS \"r2\" ON \"r2\".\"XCL_010\" = \"r1\".\"XCL_002\" WHERE \"r0\".\"XCL_006\" = '-' AND \"r2\".\"XCL_011\" = '+' GROUP BY \"r2\".\"XCL_010\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:198"
  ]
}
```

### SUBSTRING("connected"."XCL_007", 7, 2) = '45'

```json
{
  "kind": "predicate",
  "formula": "SUBSTRING(\"connected\".\"XCL_007\", 7, 2) = '45'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_006\", T1.\"XCL_004\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE SUBSTRING(T2.\"XCL_007\", 7, 2) = '45'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:246"
  ]
}
```

### The total number of records in the 'connected' table, used as the denominator for the concentration ratio.

```json
{
  "kind": "metric",
  "formula": "COUNT(\"connected\".\"XCL_007\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_007\") FROM connected",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_007\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_007\") AS \"value\" FROM connected AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:254"
  ]
}
```

### Distinct XCL_006 values for TR000

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T.\"XCL_006\" FROM bond AS T WHERE T.\"XCL_005\" = 'TR000'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:229"
  ]
}
```

### Aggregates the total number of rows in the 'molecule' table where the 'XCL_010' value is between 'TR000' and 'TR030' (inclusive) and the 'XCL_011' val

```json
{
  "kind": "metric",
  "formula": "COUNT(\"molecule\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T.\"XCL_010\") FROM molecule AS T WHERE T.\"XCL_010\" BETWEEN 'TR000' AND 'TR030' AND T.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_010\") AS \"value\" FROM molecule AS \"r0\" WHERE \"r0\".\"XCL_010\" BETWEEN 'TR000' AND 'TR030' AND \"r0\".\"XCL_011\" = '+'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:266"
  ]
}
```

### Attribute XCL_008 from the connected table (T2), returned in the output. Represents a property of the connection associated with the bond.

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_004\", T2.\"XCL_007\", T2.\"XCL_008\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T1.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_008\" AS \"value\" FROM bond AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_004\" = \"r1\".\"XCL_009\" WHERE \"r0\".\"XCL_006\" = '-'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:305",
    "bird_dev:210"
  ]
}
```

### A scalar metric calculated by subtracting the count of rows where XCL_011 is '-' from the count of rows where XCL_011 is '+', counting non-null values

```json
{
  "kind": "metric",
  "formula": "COUNT(CASE WHEN \"molecule\".\"XCL_011\" = '+' THEN \"molecule\".\"XCL_010\" ELSE NULL END) - COUNT(CASE WHEN \"molecule\".\"XCL_011\" = '-' THEN \"molecule\".\"XCL_010\" ELSE NULL END)",
  "grain": [],
  "population_scope": "SELECT COUNT(CASE WHEN T.\"XCL_011\" = '+' THEN T.\"XCL_010\" ELSE NULL END) - COUNT(CASE WHEN T.\"XCL_011\" = '-' THEN T.\"XCL_010\" ELSE NULL END) AS diff_car_notcar FROM molecule AS t",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(CASE WHEN \"r0\".\"XCL_011\" = '+' THEN \"r0\".\"XCL_010\" ELSE NULL END) - COUNT(CASE WHEN \"r0\".\"XCL_011\" = '-' THEN \"r0\".\"XCL_010\" ELSE NULL END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT COUNT(CASE WHEN \"r0\".\"XCL_011\" = '+' THEN \"r0\".\"XCL_010\" ELSE NULL END) - COUNT(CASE WHEN \"r0\".\"XCL_011\" = '-' THEN \"r0\".\"XCL_010\" ELSE NULL END) AS \"value\" FROM molecule AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:222"
  ]
}
```

### "atom"."XCL_001" = 'TR000_1'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_001\" = 'TR000_1'",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_003\" FROM atom AS T WHERE T.\"XCL_001\" = 'TR000_1'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:322"
  ]
}
```

### "connected"."XCL_009" = 'TR000_1_2'

```json
{
  "kind": "predicate",
  "formula": "\"connected\".\"XCL_009\" = 'TR000_1_2'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T2.\"XCL_009\" = 'TR000_1_2'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:277"
  ]
}
```

### Oxygen Atom Identifier in Positive Molecules

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'o' AND T2.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\" WHERE \"r0\".\"XCL_003\" = 'o' AND \"r1\".\"XCL_011\" = '+'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:339"
  ]
}
```

### "bond"."XCL_006" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '-'",
  "grain": [],
  "population_scope": "SELECT ROUND(CAST(COUNT(CASE WHEN T2.\"XCL_011\" = '+' THEN T1.\"XCL_004\" ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_004\"), 5) FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:255"
  ]
}
```

### Distinct Molecule Count

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"atom\".\"XCL_002\")",
  "grain": [
    "\"atom\".\"XCL_003\""
  ],
  "population_scope": "SELECT T1.\"XCL_003\", COUNT(DISTINCT T1.\"XCL_002\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '-' GROUP BY T1.\"XCL_003\" ORDER BY COUNT(DISTINCT T1.\"XCL_002\") ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:212"
  ]
}
```

### "molecule"."XCL_011" = '+' AND "atom"."XCL_003" = 'h'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_011\" = '+' AND \"atom\".\"XCL_003\" = 'h'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") AS atomnums_h FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+' AND T1.\"XCL_003\" = 'h'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:295"
  ]
}
```

### "bond"."XCL_006" = '='

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '='",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" INNER JOIN connected AS T3 ON T1.\"XCL_001\" = T3.\"XCL_007\" WHERE T2.\"XCL_006\" = '='",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:207"
  ]
}
```

### Connected Atom ID

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_007\", T2.\"XCL_008\" FROM atom AS T1 INNER JOIN connected AS T2 ON T2.\"XCL_007\" = T1.\"XCL_001\" WHERE T1.\"XCL_002\" = 'TR181'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_007\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_007\" AS \"value\" FROM atom AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r1\".\"XCL_007\" = \"r0\".\"XCL_001\" WHERE \"r0\".\"XCL_002\" = 'TR181'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:217"
  ]
}
```

### Atom XCL_003 for double-bonded TR024

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_002\" = 'TR024' AND T2.\"XCL_006\" = '='",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_003\" AS \"value\" FROM atom AS \"r0\" INNER JOIN bond AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_005\" WHERE \"r0\".\"XCL_002\" = 'TR024' AND \"r1\".\"XCL_006\" = '='",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:328"
  ]
}
```

### Chlorine Atom ID in Positive Molecules

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_002\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'cl' AND T2.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:315"
  ]
}
```

### Count of unique values in the XCL_005 column from the bond table, filtered to rows where XCL_005 is between 'TR004' and 'TR010' and XCL_006 is '-'. Re

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"bond\".\"XCL_005\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T.\"XCL_005\") FROM bond AS T WHERE T.\"XCL_005\" BETWEEN 'TR004' AND 'TR010' AND T.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_005\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r0\".\"XCL_005\") AS \"value\" FROM bond AS \"r0\" WHERE \"r0\".\"XCL_005\" BETWEEN 'TR004' AND 'TR010' AND \"r0\".\"XCL_006\" = '-'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:332"
  ]
}
```

### Bond Category Identifier

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_006\"",
  "grain": [
    "\"bond\".\"XCL_006\""
  ],
  "population_scope": "SELECT \"XCL_006\", COUNT(\"XCL_004\") FROM bond GROUP BY \"XCL_006\" ORDER BY COUNT(\"XCL_004\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:195"
  ]
}
```

### "connected"."XCL_007" = 'TR000_1' AND "connected"."XCL_008" = 'TR000_2'

```json
{
  "kind": "predicate",
  "formula": "\"connected\".\"XCL_007\" = 'TR000_1' AND \"connected\".\"XCL_008\" = 'TR000_2'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_006\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T2.\"XCL_007\" = 'TR000_1' AND T2.\"XCL_008\" = 'TR000_2'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:320"
  ]
}
```

### Aggregates the total number of atom records (XCL_001) where the atom type (XCL_003) is 'p' or 'br' and the atom is part of a molecule (XCL_002) that c

```json
{
  "kind": "metric",
  "formula": "COUNT(\"atom\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '#' AND T1.\"XCL_003\" IN ('p', 'br')",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      },
      {
        "role": "r2",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\" INNER JOIN bond AS \"r2\" ON \"r1\".\"XCL_010\" = \"r2\".\"XCL_005\" WHERE \"r2\".\"XCL_006\" = '#' AND \"r0\".\"XCL_003\" IN ('p', 'br')",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:260"
  ]
}
```

### "molecule"."XCL_011" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_011\" = '-'",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_010\" FROM molecule AS T WHERE T.\"XCL_011\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:265"
  ]
}
```

### Atom Property XCL_003

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_005\", T2.\"XCL_003\" FROM bond AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_005\" = T2.\"XCL_002\" WHERE T1.\"XCL_006\" = '#'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:306"
  ]
}
```

### The value of column XCL_003 from the atom table, filtered to rows where XCL_001 equals 'TR000_1'. Returns one row per matching atom record.

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_003\" FROM atom AS T WHERE T.\"XCL_001\" = 'TR000_1'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_003\" AS \"value\" FROM atom AS \"r0\" WHERE \"r0\".\"XCL_001\" = 'TR000_1'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:322"
  ]
}
```

### "connected"."XCL_009" = 'TR000_2_3'

```json
{
  "kind": "predicate",
  "formula": "\"connected\".\"XCL_009\" = 'TR000_2_3'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM connected AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_007\" = T2.\"XCL_001\" WHERE T1.\"XCL_009\" = 'TR000_2_3'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:307"
  ]
}
```

### Attribute from the 'connected' table (XCL_008) associated with the connection record. Returned alongside the connected atom ID for atoms linked to lea

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_007\", T2.\"XCL_008\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T1.\"XCL_003\" = 'pb'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_008\" AS \"value\" FROM atom AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_007\" WHERE \"r0\".\"XCL_003\" = 'pb'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:252"
  ]
}
```

### "atom"."XCL_002" = 'TR001'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_002\" = 'TR001'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T.\"XCL_003\" FROM atom AS T WHERE T.\"XCL_002\" = 'TR001'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:274"
  ]
}
```

### "molecule"."XCL_011" = '+'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_010\", T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:304"
  ]
}
```

### Distinct XCL_003 values for TR004

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T.\"XCL_003\" FROM atom AS T WHERE T.\"XCL_002\" = 'TR004'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:240"
  ]
}
```

### A specific attribute or property column from the molecule table, retrieved for the filtered subset of molecules.

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_010\", T.\"XCL_011\" FROM molecule AS T WHERE T.\"XCL_010\" IN ('TR000', 'TR001', 'TR002')",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_011\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_011\" AS \"value\" FROM molecule AS \"r0\" WHERE \"r0\".\"XCL_010\" IN ('TR000', 'TR001', 'TR002')",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:264"
  ]
}
```

### Connection ID linked to phosphorus atoms

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_009\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_009\" FROM connected AS T3 INNER JOIN atom AS T4 ON T3.\"XCL_007\" = T4.\"XCL_001\" WHERE T4.\"XCL_003\" = 'p'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_009\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "connected"
      },
      {
        "role": "r1",
        "physical_table": "atom"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_009\" AS \"value\" FROM connected AS \"r0\" INNER JOIN atom AS \"r1\" ON \"r0\".\"XCL_007\" = \"r1\".\"XCL_001\" WHERE \"r1\".\"XCL_003\" = 'p'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:243"
  ]
}
```

### "bond"."XCL_004" = 'TR001_10_11'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_004\" = 'TR001_10_11'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" INNER JOIN bond AS T3 ON T2.\"XCL_009\" = T3.\"XCL_004\" WHERE T3.\"XCL_004\" = 'TR001_10_11'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:285"
  ]
}
```

### Atom Type Identifier

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [
    "\"atom\".\"XCL_003\""
  ],
  "population_scope": "SELECT T2.\"XCL_003\", COUNT(DISTINCT T2.\"XCL_002\") FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_010\" = T2.\"XCL_002\" WHERE T1.\"XCL_011\" = '+' GROUP BY T2.\"XCL_003\" ORDER BY COUNT(DISTINCT T2.\"XCL_002\") LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:251"
  ]
}
```

### Distinct identifiers (XCL_002) of atoms that are sulfur (XCL_003 = 's') and participate in at least one double bond (XCL_006 = '='). The grain is uniq

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_002\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_003\" = 's' AND T2.\"XCL_006\" = '='",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:326"
  ]
}
```

### "bond"."XCL_006" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '-'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_004\", T2.\"XCL_007\", T2.\"XCL_008\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T1.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:305"
  ]
}
```

### "atom"."XCL_003" = 'ca'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 'ca'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" AS flag_carcinogenic FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_003\" = 'ca'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:283"
  ]
}
```

### "molecule"."XCL_011" = '+' AND "bond"."XCL_006" = '='

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_011\" = '+' AND \"bond\".\"XCL_006\" = '='",
  "grain": [
    "\"molecule\".\"XCL_010\""
  ],
  "population_scope": "SELECT T3.\"XCL_010\", COUNT(T1.\"XCL_006\") FROM bond AS T1 INNER JOIN molecule AS T3 ON T1.\"XCL_005\" = T3.\"XCL_010\" WHERE T3.\"XCL_011\" = '+' AND T1.\"XCL_006\" = '=' GROUP BY T3.\"XCL_010\" ORDER BY COUNT(T1.\"XCL_006\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:250"
  ]
}
```

### Bond Identifier

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_006\", T1.\"XCL_004\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE SUBSTRING(T2.\"XCL_007\", 7, 2) = '45'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_006\" AS \"value\" FROM bond AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_004\" = \"r1\".\"XCL_009\" WHERE SUBSTRING(\"r1\".\"XCL_007\", 7, 2) = '45'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:246"
  ]
}
```

### "atom"."XCL_001" = 'TR001_1'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_001\" = 'TR001_1'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" AS flag_carcinogenic FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_001\" = 'TR001_1'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:288"
  ]
}
```

### Calculates the percentage of distinct atoms (XCL_001) that are carbon (XCL_003 = 'c') among all distinct atoms involved in double bonds (XCL_006 = '='

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(DISTINCT CASE WHEN \"atom\".\"XCL_003\" = 'c' THEN \"atom\".\"XCL_001\" ELSE NULL END) AS REAL) * 100 / COUNT(DISTINCT \"atom\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(DISTINCT CASE WHEN T1.\"XCL_003\" = 'c' THEN T1.\"XCL_001\" ELSE NULL END) AS REAL) * 100 / COUNT(DISTINCT T1.\"XCL_001\") FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = '='",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(DISTINCT CASE WHEN \"r0\".\"XCL_003\" = 'c' THEN \"r0\".\"XCL_001\" ELSE NULL END) AS REAL) * 100 / COUNT(DISTINCT \"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(DISTINCT CASE WHEN \"r0\".\"XCL_003\" = 'c' THEN \"r0\".\"XCL_001\" ELSE NULL END) AS REAL) * 100 / COUNT(DISTINCT \"r0\".\"XCL_001\") AS \"value\" FROM atom AS \"r0\" INNER JOIN bond AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_005\" WHERE \"r1\".\"XCL_006\" = '='",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:201"
  ]
}
```

### "bond"."XCL_006" = '-' AND "molecule"."XCL_011" = '+'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '-' AND \"molecule\".\"XCL_011\" = '+'",
  "grain": [
    "\"molecule\".\"XCL_010\""
  ],
  "population_scope": "SELECT T3.\"XCL_010\", COUNT(T1.\"XCL_006\") AS single_bond_count FROM bond AS T1 INNER JOIN atom AS T2 ON T1.\"XCL_005\" = T2.\"XCL_002\" INNER JOIN molecule AS T3 ON T3.\"XCL_010\" = T2.\"XCL_002\" WHERE T1.\"XCL_006\" = '-' AND T3.\"XCL_011\" = '+' GROUP BY T3.\"XCL_010\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:198"
  ]
}
```

### "atom"."XCL_002" = 'TR002'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_002\" = 'TR002'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_003\", T2.\"XCL_006\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_002\" = 'TR002'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:337"
  ]
}
```

### "connected"."XCL_009" = 'TR001_6_9'

```json
{
  "kind": "predicate",
  "formula": "\"connected\".\"XCL_009\" = 'TR001_6_9'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_006\", T2.\"XCL_007\", T2.\"XCL_008\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T2.\"XCL_009\" = 'TR001_6_9'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:236"
  ]
}
```

### Type or element code of the atom (XCL_003). Used to filter for specific atom types (e.g., 'cl') in conditional metrics.

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T1.\"XCL_003\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" INNER JOIN bond AS T3 ON T2.\"XCL_010\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      },
      {
        "role": "r2",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_003\" AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\" INNER JOIN bond AS \"r2\" ON \"r1\".\"XCL_010\" = \"r2\".\"XCL_005\" WHERE \"r2\".\"XCL_006\" = '-'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:263"
  ]
}
```

### "bond"."XCL_006" = '='

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '='",
  "grain": [
    "\"bond\".\"XCL_005\""
  ],
  "population_scope": "SELECT T.\"XCL_005\", COUNT(T.\"XCL_006\") FROM bond AS T WHERE T.\"XCL_006\" = '=' GROUP BY T.\"XCL_005\" ORDER BY COUNT(T.\"XCL_006\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:244"
  ]
}
```

### Bond Identifier

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_005\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_005\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" WHERE T2.\"XCL_007\" = 'TR000_2' AND T2.\"XCL_008\" = 'TR000_4'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_005\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_005\" AS \"value\" FROM bond AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_004\" = \"r1\".\"XCL_009\" WHERE \"r1\".\"XCL_007\" = 'TR000_2' AND \"r1\".\"XCL_008\" = 'TR000_4'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:321"
  ]
}
```

### "connected"."XCL_009" = 'TR001_2_4'

```json
{
  "kind": "predicate",
  "formula": "\"connected\".\"XCL_009\" = 'TR001_2_4'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T2.\"XCL_009\" = 'TR001_2_4'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:302"
  ]
}
```

### "connected"."XCL_008" = 'TR000_2'

```json
{
  "kind": "predicate",
  "formula": "\"connected\".\"XCL_008\" = 'TR000_2'",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_009\" FROM connected AS T WHERE T.\"XCL_008\" = 'TR000_2'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:224"
  ]
}
```

### "bond"."XCL_006" = '='

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_006\" = '='",
  "grain": [],
  "population_scope": "SELECT DISTINCT T.\"XCL_005\" FROM bond AS T WHERE T.\"XCL_006\" = '='",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:275"
  ]
}
```

### Distinct identifiers (XCL_010) of molecules that contain at least one bond marked with '#' (XCL_006) and where the molecule itself is marked with '+' 

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_010\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_010\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T1.\"XCL_006\" = '#' AND T2.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:200"
  ]
}
```

### Bond Attribute XCL_005

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_005\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_005\", T2.\"XCL_004\", T1.\"XCL_007\" FROM connected AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_009\" = T2.\"XCL_004\" WHERE T1.\"XCL_007\" = 'TR000_1' AND T2.\"XCL_004\" = 'TR000_1_2'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_005\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "connected"
      },
      {
        "role": "r1",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_005\" AS \"value\" FROM connected AS \"r0\" INNER JOIN bond AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_004\" WHERE \"r0\".\"XCL_007\" = 'TR000_1' AND \"r1\".\"XCL_004\" = 'TR000_1_2'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:296"
  ]
}
```

### A binary indicator derived from the molecule's XCL_011 attribute. It returns 'YES' if XCL_011 is '+', otherwise 'NO'. This metric flags whether the mo

```json
{
  "kind": "binding",
  "formula": "IIF(\"molecule\".\"XCL_011\" = '+', 'YES', 'NO')",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_010\", IIF(T2.\"XCL_011\" = '+', 'YES', 'NO') AS flag_carcinogenic FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T1.\"XCL_001\" = 'TR001_10'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "IIF(\"r1\".\"XCL_011\" = '+', 'YES', 'NO')",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT IIF(\"r1\".\"XCL_011\" = '+', 'YES', 'NO') AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\" WHERE \"r0\".\"XCL_001\" = 'TR001_10'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:237"
  ]
}
```

### "atom"."XCL_003" = 'i'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 'i'",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(T2.\"XCL_009\") AS REAL) / COUNT(T1.\"XCL_001\") FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T1.\"XCL_003\" = 'i'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:245"
  ]
}
```

### Aggregates the count of non-null values in the XCL_004 column from the bond table, restricted to rows where XCL_006 equals '-'. Returns a single scala

```json
{
  "kind": "metric",
  "formula": "COUNT(\"bond\".\"XCL_004\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T.\"XCL_004\") FROM bond AS T WHERE T.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_004\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_004\") AS \"value\" FROM bond AS \"r0\" WHERE \"r0\".\"XCL_006\" = '-'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:314"
  ]
}
```

### "atom"."XCL_002" = 'TR181'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_002\" = 'TR181'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_007\", T2.\"XCL_008\" FROM atom AS T1 INNER JOIN connected AS T2 ON T2.\"XCL_007\" = T1.\"XCL_001\" WHERE T1.\"XCL_002\" = 'TR181'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:217"
  ]
}
```

### Distinct Bond Identifier

```json
{
  "kind": "binding",
  "formula": "\"bond\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_004\" FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_005\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:261"
  ]
}
```

### "atom"."XCL_003" = 'pb'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_003\" = 'pb'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_007\", T2.\"XCL_008\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T1.\"XCL_003\" = 'pb'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:252"
  ]
}
```

### Atom Count per Molecule

```json
{
  "kind": "metric",
  "formula": "COUNT(\"atom\".\"XCL_001\")",
  "grain": [
    "\"molecule\".\"XCL_010\""
  ],
  "population_scope": "SELECT T2.\"XCL_010\", COUNT(T1.\"XCL_001\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+' GROUP BY T2.\"XCL_010\" ORDER BY COUNT(T1.\"XCL_001\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:329"
  ]
}
```

### "molecule"."XCL_011" = '+'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:293"
  ]
}
```

### Atom XCL_003

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_003\", T2.\"XCL_006\" FROM atom AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_002\" = T2.\"XCL_005\" WHERE T1.\"XCL_002\" = 'TR002'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:337"
  ]
}
```

### Calculates the percentage of rows in the 'atom' table where 'XCL_003' equals 'h', relative to the total count of 'XCL_001' entries, filtered by 'XCL_0

```json
{
  "kind": "metric",
  "formula": "ROUND(CAST(COUNT(CASE WHEN \"atom\".\"XCL_003\" = 'h' THEN \"atom\".\"XCL_001\" ELSE NULL END) AS REAL) * 100 / COUNT(\"atom\".\"XCL_001\"), 4)",
  "grain": [],
  "population_scope": "SELECT ROUND(CAST(COUNT(CASE WHEN T.\"XCL_003\" = 'h' THEN T.\"XCL_001\" ELSE NULL END) AS REAL) * 100 / COUNT(T.\"XCL_001\"), 4) FROM atom AS T WHERE T.\"XCL_002\" = 'TR206'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "ROUND(CAST(COUNT(CASE WHEN \"r0\".\"XCL_003\" = 'h' THEN \"r0\".\"XCL_001\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\"), 4)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      }
    ],
    "scope_sql": "SELECT ROUND(CAST(COUNT(CASE WHEN \"r0\".\"XCL_003\" = 'h' THEN \"r0\".\"XCL_001\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\"), 4) AS \"value\" FROM atom AS \"r0\" WHERE \"r0\".\"XCL_002\" = 'TR206'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:228"
  ]
}
```

### "atom"."XCL_002" = 'TR006'

```json
{
  "kind": "predicate",
  "formula": "\"atom\".\"XCL_002\" = 'TR006'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_009\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T1.\"XCL_002\" = 'TR006' ORDER BY T2.\"XCL_009\" LIMIT 2",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:233"
  ]
}
```

### Connected Atom XCL_003

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:247"
  ]
}
```

### "bond"."XCL_005" = 'TR001' AND "bond"."XCL_004" = 'TR001_2_6'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_005\" = 'TR001' AND \"bond\".\"XCL_004\" = 'TR001_2_6'",
  "grain": [],
  "population_scope": "SELECT SUBSTRING(T.\"XCL_004\", 1, 7) AS atom_id1, T.\"XCL_005\" || SUBSTRING(T.\"XCL_004\", 8, 2) AS atom_id2 FROM bond AS T WHERE T.\"XCL_005\" = 'TR001' AND T.\"XCL_004\" = 'TR001_2_6'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:221"
  ]
}
```

### "molecule"."XCL_010" BETWEEN 'TR000' AND 'TR030' AND "molecule"."XCL_011" = '+'

```json
{
  "kind": "predicate",
  "formula": "\"molecule\".\"XCL_010\" BETWEEN 'TR000' AND 'TR030' AND \"molecule\".\"XCL_011\" = '+'",
  "grain": [],
  "population_scope": "SELECT COUNT(T.\"XCL_010\") FROM molecule AS T WHERE T.\"XCL_010\" BETWEEN 'TR000' AND 'TR030' AND T.\"XCL_011\" = '+'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:266"
  ]
}
```

### Atom Identifier

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\" FROM atom AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_001\" = T2.\"XCL_007\" WHERE T2.\"XCL_009\" = 'TR000_1_2'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_003\" AS \"value\" FROM atom AS \"r0\" INNER JOIN connected AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_007\" WHERE \"r1\".\"XCL_009\" = 'TR000_1_2'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:277"
  ]
}
```

### Molecule XCL_011 Attribute

```json
{
  "kind": "binding",
  "formula": "\"molecule\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_011\" FROM molecule AS T WHERE T.\"XCL_010\" = 'TR000'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_011\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_011\" AS \"value\" FROM molecule AS \"r0\" WHERE \"r0\".\"XCL_010\" = 'TR000'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:323"
  ]
}
```

### "bond"."XCL_005" BETWEEN 'TR004' AND 'TR010' AND "bond"."XCL_006" = '-'

```json
{
  "kind": "predicate",
  "formula": "\"bond\".\"XCL_005\" BETWEEN 'TR004' AND 'TR010' AND \"bond\".\"XCL_006\" = '-'",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T.\"XCL_005\") FROM bond AS T WHERE T.\"XCL_005\" BETWEEN 'TR004' AND 'TR010' AND T.\"XCL_006\" = '-'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:332"
  ]
}
```

### Counts the number of unique values in the XCL_005 column from the bond table, restricted to rows where XCL_006 equals '#'. The result is a single scal

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"bond\".\"XCL_005\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T.\"XCL_005\") FROM bond AS T WHERE T.\"XCL_006\" = '#'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_005\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r0\".\"XCL_005\") AS \"value\" FROM bond AS \"r0\" WHERE \"r0\".\"XCL_006\" = '#'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:238"
  ]
}
```

### Hydrogen Atom Ratio

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN \"XCL_003\" = 'h' THEN \"XCL_001\" ELSE NULL END) AS REAL) / (CASE WHEN COUNT(\"XCL_001\") = 0 THEN NULL ELSE COUNT(\"XCL_001\") END)",
  "grain": [
    "\"molecule\".\"XCL_011\""
  ],
  "population_scope": "WITH SubQuery AS (SELECT DISTINCT T1.\"XCL_001\", T1.\"XCL_003\", T1.\"XCL_002\", T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_010\" = 'TR006') SELECT CAST(COUNT(CASE WHEN \"XCL_003\" = 'h' THEN \"XCL_001\" ELSE NULL END) AS REAL) / (CASE WHEN COUNT(\"XCL_001\") = 0 THEN NULL ELSE COUNT(\"XCL_001\") END) AS ratio, \"XCL_011\" FROM SubQuery GROUP BY \"XCL_011\"",
  "upstream_scopes": [
    "SELECT DISTINCT T1.\"XCL_001\", T1.\"XCL_003\", T1.\"XCL_002\", T2.\"XCL_011\" FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_010\" = 'TR006'"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:282"
  ]
}
```

### Connection Attribute XCL_007

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_005\", T2.\"XCL_004\", T1.\"XCL_007\" FROM connected AS T1 INNER JOIN bond AS T2 ON T1.\"XCL_009\" = T2.\"XCL_004\" WHERE T1.\"XCL_007\" = 'TR000_1' AND T2.\"XCL_004\" = 'TR000_1_2'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_007\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "connected"
      },
      {
        "role": "r1",
        "physical_table": "bond"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_007\" AS \"value\" FROM connected AS \"r0\" INNER JOIN bond AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_004\" WHERE \"r0\".\"XCL_007\" = 'TR000_1' AND \"r1\".\"XCL_004\" = 'TR000_1_2'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:296"
  ]
}
```

### Distinct XCL_003 values

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T.\"XCL_003\" FROM atom AS T WHERE T.\"XCL_002\" = 'TR000' ORDER BY T.\"XCL_003\" LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:220"
  ]
}
```

### Atom Identifier

```json
{
  "kind": "binding",
  "formula": "\"atom\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_003\" FROM bond AS T1 INNER JOIN connected AS T2 ON T1.\"XCL_004\" = T2.\"XCL_009\" INNER JOIN atom AS T3 ON T2.\"XCL_007\" = T3.\"XCL_001\" WHERE T1.\"XCL_006\" = '#'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:253"
  ]
}
```

### The value of column XCL_009 from the 'connected' table, filtered to rows where XCL_008 equals 'TR000_2'.

```json
{
  "kind": "binding",
  "formula": "\"connected\".\"XCL_009\"",
  "grain": [],
  "population_scope": "SELECT T.\"XCL_009\" FROM connected AS T WHERE T.\"XCL_008\" = 'TR000_2'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_009\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "connected"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_009\" AS \"value\" FROM connected AS \"r0\" WHERE \"r0\".\"XCL_008\" = 'TR000_2'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:224"
  ]
}
```

### Aggregates the count of atom records (XCL_001) where the atom type (XCL_003) is 'h' and the associated molecule (via XCL_002 = XCL_010) has a charge (

```json
{
  "kind": "metric",
  "formula": "COUNT(\"atom\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") AS atomnums_h FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.\"XCL_002\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = '+' AND T1.\"XCL_003\" = 'h'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "atom"
      },
      {
        "role": "r1",
        "physical_table": "molecule"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM atom AS \"r0\" INNER JOIN molecule AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_010\" WHERE \"r1\".\"XCL_011\" = '+' AND \"r0\".\"XCL_003\" = 'h'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:295"
  ]
}
```


## Incremental maintenance events

- Source withdrawal preview · bird_dev:195 · Review event: withdraw this archived SQL source on a copied ontology
  - bond.XCL_004: bond_id → bond_id
  - bond.XCL_006: bond_type → bond_type
