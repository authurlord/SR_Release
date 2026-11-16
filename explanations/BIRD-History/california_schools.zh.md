# BIRD-History / california_schools — Schema 与业务口径解释

该数据库的存档目录包含 3 张表、74 个物理列、6 条关系，以及 89 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## frpm

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, T3, T4, f, f2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| frpm.XCL_001 | CDS Code | unknown | bird_dev:8, bird_dev:81, bird_dev:73, bird_dev:3, bird_dev:24, bird_dev:21, bird_dev:75, bird_dev:35 |
| frpm.XCL_002 | Academic Year | unknown | bird_dev:72 |
| frpm.XCL_003 | District Code | unknown | bird_dev:75 |
| frpm.XCL_004 | School Code | unknown | bird_dev:85, bird_dev:71 |
| frpm.XCL_005 | School Number | unknown | bird_dev:9 |
| frpm.XCL_006 | County | unknown | bird_dev:21, bird_dev:18, bird_dev:0 |
| frpm.XCL_007 | District Name | unknown | bird_dev:2, bird_dev:25 |
| frpm.XCL_008 | School Name | unknown | bird_dev:81, bird_dev:24, bird_dev:26, bird_dev:20, bird_dev:80, bird_dev:33 |
| frpm.XCL_010 | School Type | unknown | bird_dev:26, bird_dev:80 |
| frpm.XCL_011 | School Category | unknown | bird_dev:1 |
| frpm.XCL_012 | FRPM Provision Type | unknown | bird_dev:75, bird_dev:83, bird_dev:76 |
| frpm.XCL_013 | Charter Status | unknown | bird_dev:35, bird_dev:4, bird_dev:2 |
| frpm.XCL_015 | Funding Type | unknown | bird_dev:18, bird_dev:4, bird_dev:9, bird_dev:25 |
| frpm.XCL_017 | Grade Span Start | unknown | bird_dev:81, bird_dev:76, bird_dev:20, bird_dev:74 |
| frpm.XCL_018 | Grade Span End | unknown | bird_dev:76, bird_dev:20 |
| frpm.XCL_019 | Enrollment K-12 | unknown | bird_dev:24, bird_dev:35, bird_dev:11, bird_dev:30, bird_dev:23, bird_dev:29, bird_dev:0, bird_dev:28 |
| frpm.XCL_020 | Free Meal Count K-12 | unknown | bird_dev:24, bird_dev:21, bird_dev:0, bird_dev:62, bird_dev:85, bird_dev:31 |
| frpm.XCL_022 | Reduced Price Meal Count | unknown | bird_dev:8, bird_dev:3, bird_dev:21, bird_dev:32 |
| frpm.XCL_024 | Enrollment Ages 5-17 | unknown | bird_dev:1, bird_dev:77, bird_dev:11, bird_dev:23, bird_dev:28, bird_dev:34, bird_dev:14, bird_dev:12 |
| frpm.XCL_025 | Free Meal Count Ages 5-17 | unknown | bird_dev:1, bird_dev:26, bird_dev:34, bird_dev:12, bird_dev:33 |
| frpm.XCL_027 | Reduced Price Meal Count (FRPM) | unknown | bird_dev:73, bird_dev:77, bird_dev:10 |

## satscores

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, T3, s, sat, sat2, sc, t

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| satscores.XCL_030 | CDS Code | unknown | bird_dev:16, bird_dev:17, bird_dev:43, bird_dev:24, bird_dev:36, bird_dev:40, bird_dev:45, bird_dev:57 |
| satscores.XCL_032 | School Name | unknown | bird_dev:22, bird_dev:25 |
| satscores.XCL_034 | County | unknown | bird_dev:22 |
| satscores.XCL_036 | Num Test Takers | unknown | bird_dev:8, bird_dev:16, bird_dev:22, bird_dev:18, bird_dev:6, bird_dev:37, bird_dev:13, bird_dev:53 |
| satscores.XCL_037 | SAT Math Score | unknown | bird_dev:43, bird_dev:40, bird_dev:41, bird_dev:52, bird_dev:15, bird_dev:51, bird_dev:10 |
| satscores.XCL_038 | SAT Reading Score | unknown | bird_dev:43, bird_dev:5, bird_dev:52, bird_dev:19, bird_dev:9, bird_dev:50, bird_dev:42, bird_dev:25 |
| satscores.XCL_039 | SAT Writing Score | unknown | bird_dev:43, bird_dev:45, bird_dev:57, bird_dev:44, bird_dev:52, bird_dev:27 |
| satscores.XCL_040 | Num Students Score 1500 Plus | unknown | bird_dev:24, bird_dev:36, bird_dev:44, bird_dev:37, bird_dev:13, bird_dev:7, bird_dev:12, bird_dev:88 |

## schools

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, T4, T5, s, s2, sc

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| schools.XCL_041 | CDS Code | unknown | bird_dev:16, bird_dev:17, bird_dev:43, bird_dev:81, bird_dev:73, bird_dev:3, bird_dev:36, bird_dev:40 |
| schools.XCL_042 | District CDS Code | unknown | bird_dev:74, bird_dev:69 |
| schools.XCL_043 | School Number | unknown | bird_dev:14 |
| schools.XCL_044 | Status | unknown | bird_dev:16, bird_dev:68, bird_dev:70, bird_dev:48, bird_dev:49, bird_dev:15, bird_dev:56 |
| schools.XCL_045 | County | unknown | bird_dev:16, bird_dev:43, bird_dev:41, bird_dev:77, bird_dev:68, bird_dev:70, bird_dev:55, bird_dev:26 |
| schools.XCL_046 | District Name | unknown | bird_dev:40, bird_dev:86, bird_dev:15, bird_dev:84 |
| schools.XCL_047 | School Name | unknown | bird_dev:54, bird_dev:45, bird_dev:58, bird_dev:75, bird_dev:41, bird_dev:5, bird_dev:77, bird_dev:68 |
| schools.XCL_048 | Street Address | unknown | bird_dev:26, bird_dev:37, bird_dev:23 |
| schools.XCL_050 | City | unknown | bird_dev:81, bird_dev:44, bird_dev:78, bird_dev:83, bird_dev:30, bird_dev:26, bird_dev:37, bird_dev:87 |
| schools.XCL_051 | Mailing Zip Code | unknown | bird_dev:58, bird_dev:26, bird_dev:37, bird_dev:2 |
| schools.XCL_052 | State | unknown | bird_dev:81, bird_dev:26, bird_dev:37 |
| schools.XCL_053 | Mailing Address | unknown | bird_dev:73, bird_dev:3, bird_dev:50, bird_dev:51 |
| schools.XCL_055 | Mailing City | unknown | bird_dev:64, bird_dev:52, bird_dev:53 |
| schools.XCL_056 | Mailing Zip Code | unknown | bird_dev:54 |
| schools.XCL_057 | Mailing State | unknown | bird_dev:55, bird_dev:56 |
| schools.XCL_058 | Phone Number | unknown | bird_dev:40, bird_dev:57, bird_dev:58, bird_dev:4, bird_dev:19, bird_dev:27, bird_dev:13, bird_dev:7 |
| schools.XCL_059 | Fax Number | unknown | bird_dev:57, bird_dev:58 |
| schools.XCL_060 | Website | unknown | bird_dev:59, bird_dev:38, bird_dev:33, bird_dev:60 |
| schools.XCL_061 | Open Date | unknown | bird_dev:4, bird_dev:27, bird_dev:29, bird_dev:87, bird_dev:47, bird_dev:66, bird_dev:39 |
| schools.XCL_062 | Close Date | unknown | bird_dev:68, bird_dev:27, bird_dev:67, bird_dev:49 |
| schools.XCL_063 | Charter Indicator | unknown | bird_dev:61, bird_dev:63, bird_dev:65, bird_dev:62, bird_dev:60 |
| schools.XCL_064 | Charter Number | unknown | bird_dev:64, bird_dev:63, bird_dev:86 |
| schools.XCL_065 | Funding Type | unknown | bird_dev:28, bird_dev:65, bird_dev:66 |
| schools.XCL_066 | EdOps Code | unknown | bird_dev:48, bird_dev:87, bird_dev:61, bird_dev:28, bird_dev:47, bird_dev:46 |
| schools.XCL_067 | District Type | unknown | bird_dev:67 |
| schools.XCL_068 | SOC Code | unknown | bird_dev:68, bird_dev:70, bird_dev:87, bird_dev:32, bird_dev:69 |
| schools.XCL_069 | School Type | unknown | bird_dev:73 |
| schools.XCL_070 | School Category Code | unknown | bird_dev:74, bird_dev:72 |
| schools.XCL_071 | School Category | unknown | bird_dev:42 |
| schools.XCL_072 | Grade Span Code | unknown | bird_dev:76 |
| schools.XCL_073 | Grade Span | unknown | bird_dev:75 |
| schools.XCL_074 | Grade Span Offered | unknown | bird_dev:83, bird_dev:82 |
| schools.XCL_075 | Grade Span Served | unknown | bird_dev:78, bird_dev:77 |
| schools.XCL_076 | Virtual Indicator | unknown | bird_dev:41, bird_dev:5, bird_dev:79, bird_dev:60 |
| schools.XCL_077 | Magnet Status | unknown | bird_dev:83, bird_dev:6, bird_dev:71 |
| schools.XCL_078 | Latitude | unknown | bird_dev:81, bird_dev:80 |
| schools.XCL_079 | Longitude | unknown | bird_dev:82 |
| schools.XCL_080 | Administrator First Name | unknown | bird_dev:36, bird_dev:54, bird_dev:45, bird_dev:34, bird_dev:59, bird_dev:63, bird_dev:85, bird_dev:84 |
| schools.XCL_081 | Principal Last Name | unknown | bird_dev:36, bird_dev:54, bird_dev:45, bird_dev:34, bird_dev:59, bird_dev:63, bird_dev:86 |
| schools.XCL_082 | Principal Email | unknown | bird_dev:35, bird_dev:87, bird_dev:88 |
| schools.XCL_083 | Administrator First Name | unknown | bird_dev:36 |
| schools.XCL_084 | Administrator Last Name | unknown | bird_dev:36 |
| schools.XCL_085 | Administrator Email | unknown | bird_dev:87 |
| schools.XCL_086 | 保留物理名称；存档没有恢复别名 | unknown | bird_dev:36 |
| schools.XCL_087 | 保留物理名称；存档没有恢复别名 | unknown | bird_dev:36 |

## 表关系与连接依据

- frpm.XCL_001 ↔ satscores.XCL_030; target_disjoint_historical_join
- frpm.XCL_001 ↔ schools.XCL_041; target_disjoint_historical_join
- satscores.XCL_030 ↔ schools.XCL_041; target_disjoint_historical_join
- frpm.XCL_001 ↔ satscores.XCL_030; sql_workload_observed_join
- frpm.XCL_001 ↔ schools.XCL_041; sql_workload_observed_join
- satscores.XCL_030 ↔ schools.XCL_041; sql_workload_observed_join

## 业务口径、总体与粒度

### A full SQL program that joins the frpm table (T1) to the schools table (T2) on T1.XCL_001 = T2.XCL_041. It filters for FRPM records with XCL_015 = 'Di

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_058\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_015\" = 'Directly funded' AND T1.\"XCL_013\" = 1 AND T2.\"XCL_061\" > '2000-01-01'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:4"
  ]
}
```

### Filtered School-FRPM Join Query

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_082\", T2.\"XCL_085\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'San Bernardino' AND T2.\"XCL_050\" = 'San Bernardino' AND T2.\"XCL_066\" = 54 AND STRFTIME('%Y', T2.\"XCL_061\") BETWEEN '2009' AND '2010' AND T2.\"XCL_068\" = 62",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:87"
  ]
}
```

### A query that joins the frpm and schools tables on XCL_001 = XCL_041, orders the results by frpm.XCL_022 in descending order, and returns the first row

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_053\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_022\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:3"
  ]
}
```

### Full SQL program that counts schools from the 'schools' table. It applies filters for year 1989 (derived from XCL_062), city 'San Francisco' (XCL_050)

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_047\") FROM schools WHERE STRFTIME('%Y', \"XCL_062\") = '1989' AND \"XCL_050\" = 'San Francisco' AND \"XCL_067\" = 'Community College District'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:67"
  ]
}
```

### A query that identifies the single school identifier (XCL_045) with the maximum number of related entries (COUNT of XCL_047). The population is restri

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_045\" FROM schools WHERE STRFTIME('%Y', \"XCL_062\") BETWEEN '1980' AND '1989' AND \"XCL_044\" = 'Closed' AND \"XCL_068\" = 11 GROUP BY \"XCL_045\" ORDER BY COUNT(\"XCL_047\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:68"
  ]
}
```

### Joins frpm and schools tables on XCL_001 = XCL_041. Filters for schools in 'Monterey' (XCL_045), frpm records with XCL_025 > 800, and school type 'Hig

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_008\", T2.\"XCL_048\", T2.\"XCL_050\", T2.\"XCL_052\", T2.\"XCL_051\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Monterey' AND T1.\"XCL_025\" > 800 AND T1.\"XCL_010\" = 'High Schools (Public)'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:26"
  ]
}
```

### Filtered School Attributes Query

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_080\", \"XCL_081\", \"XCL_047\", \"XCL_050\" FROM schools WHERE \"XCL_063\" = 1 AND \"XCL_064\" = '00D2'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:63"
  ]
}
```

### Full SQL program that selects columns XCL_047 and XCL_056 from the schools table, filtered by specific values in columns XCL_080 ('Avetik') and XCL_08

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_047\", \"XCL_056\" FROM schools WHERE \"XCL_080\" = 'Avetik' AND \"XCL_081\" = 'Atoian'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:54"
  ]
}
```

### A query that joins schools and satscores on XCL_041 = XCL_030, calculates the ratio of XCL_040 to XCL_036 (casting XCL_040 to REAL), sorts in descendi

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_058\" FROM schools AS T1 INNER JOIN satscores AS T2 ON T1.\"XCL_041\" = T2.\"XCL_030\" ORDER BY CAST(T2.\"XCL_040\" AS REAL) / T2.\"XCL_036\" DESC LIMIT 3",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:13"
  ]
}
```

### Full SQL program that joins satscores (T1) and schools (T2) on XCL_030 = XCL_041, filters for female schools (XCL_076 = 'F') and SAT scores > 400 (XCL

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T2.\"XCL_047\") FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_076\" = 'F' AND T1.\"XCL_038\" > 400",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:5"
  ]
}
```

### A query that joins the 'frpm' table (T1) with the 'schools' table (T2) on 'XCL_001' = 'XCL_041'. It filters for FRPM records where 'XCL_013' is 1, ord

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_082\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_013\" = 1 ORDER BY T1.\"XCL_019\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:35"
  ]
}
```

### A query that joins frpm and schools on XCL_001 = XCL_041, filters for schools in Fremont with type SSS and frpm records from 2014-2015, and returns th

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_024\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_070\" = 'SSS' AND T2.\"XCL_050\" = 'Fremont' AND T1.\"XCL_002\" BETWEEN 2014 AND 2015",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:72"
  ]
}
```

### FRPM-Schools Join Query

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_060\", T1.\"XCL_008\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_025\" BETWEEN 1900 AND 2000 AND NOT T2.\"XCL_060\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:33"
  ]
}
```

### Full SQL program joining schools (T2) and satscores (T1) on XCL_041 = XCL_030. Filters rows where the year extracted from schools.XCL_061 is greater t

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_047\", T1.\"XCL_039\", T2.\"XCL_058\" FROM schools AS T2 LEFT JOIN satscores AS T1 ON T2.\"XCL_041\" = T1.\"XCL_030\" WHERE STRFTIME('%Y', T2.\"XCL_061\") > '1991' OR STRFTIME('%Y', T2.\"XCL_062\") < '2000'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:27"
  ]
}
```

### A distinct list of XCL_080 and XCL_046 pairs for schools belonging to the two most common XCL_080 categories.

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_080\", T1.\"XCL_046\" FROM schools AS T1 INNER JOIN (SELECT \"XCL_080\" FROM schools GROUP BY \"XCL_080\" ORDER BY COUNT(\"XCL_080\") DESC LIMIT 2) AS T2 ON T1.\"XCL_080\" = T2.\"XCL_080\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:84"
  ]
}
```

### A SQL program that joins the schools table (T1) with the frpm table (T2) on the key XCL_041 (schools) matching XCL_001 (frpm). It orders the results b

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_043\" FROM schools AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_041\" = T2.\"XCL_001\" ORDER BY T2.\"XCL_024\" DESC LIMIT 5",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:14"
  ]
}
```

### A query that retrieves the SAT score (XCL_036) for the entity (identified by XCL_030 in satscores) that has the maximum value in XCL_022 within the fr

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_036\" FROM satscores WHERE \"XCL_030\" = (SELECT \"XCL_001\" FROM frpm ORDER BY \"XCL_022\" DESC LIMIT 1)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:8"
  ]
}
```

### A query that joins 'satscores' and 'schools' on 'XCL_030' = 'XCL_041'. It filters for schools where 'XCL_077' equals 1 and SAT score records where 'XC

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_047\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_077\" = 1 AND T1.\"XCL_036\" > 500",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:6"
  ]
}
```

### Alusine FRPM Metrics Query

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_020\" * 100 / T1.\"XCL_019\", T1.\"XCL_004\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_080\" = 'Alusine'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:85"
  ]
}
```

### A SQL program that computes the average SAT score for schools in Fresno in 1980. It joins satscores (T1) to schools (T2) on school ID, filters by the 

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T1.\"XCL_036\") FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE STRFTIME('%Y', T2.\"XCL_061\") = '1980' AND T2.\"XCL_045\" = 'Fresno'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:39"
  ]
}
```

### Executes an inner join between the 'schools' table (T1) and 'satscores' table (T2) on the school identifier (XCL_041 = XCL_030). Filters for schools w

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_041\") FROM schools AS T1 INNER JOIN satscores AS T2 ON T1.\"XCL_041\" = T2.\"XCL_030\" WHERE T1.\"XCL_044\" = 'Merged' AND T2.\"XCL_036\" < 100 AND T1.\"XCL_045\" = 'Lake'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:16"
  ]
}
```

### Full SQL program that joins 'satscores' (T1) and 'frpm' (T2) on T1."XCL_030" = T2."XCL_001", filters for T1."XCL_038" > 560 and T2."XCL_015" = 'Direct

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_005\") FROM satscores AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_030\" = T2.\"XCL_001\" WHERE T1.\"XCL_038\" > 560 AND T2.\"XCL_015\" = 'Directly funded'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:9"
  ]
}
```

### A query that identifies schools with 'Locally funded' status (XCL_065) where the linked FRPM record's difference (XCL_019 - XCL_024) is greater than t

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_047\", T2.\"XCL_066\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_065\" = 'Locally funded' AND (T1.\"XCL_019\" - T1.\"XCL_024\") > (SELECT AVG(T3.\"XCL_019\" - T3.\"XCL_024\") FROM frpm AS T3 INNER JOIN schools AS T4 ON T3.\"XCL_001\" = T4.\"XCL_041\" WHERE T4.\"XCL_065\" = 'Locally funded')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:28"
  ]
}
```

### Full query returning the top 5 frpm records (ordered by XCL_022 descending) joined to schools on XCL_001 = XCL_041, filtered to schools where XCL_068 

```json
{
  "kind": "program",
  "formula": "SELECT CAST(T1.\"XCL_022\" AS REAL) / T1.\"XCL_019\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_068\" = 66 ORDER BY T1.\"XCL_022\" DESC LIMIT 5",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:32"
  ]
}
```

### Lowest Score School Lookup

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_053\", T2.\"XCL_047\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE NOT T1.\"XCL_037\" IS NULL ORDER BY T1.\"XCL_037\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:51"
  ]
}
```

### SQL program that filters the frpm table for entries where XCL_006 equals 'Alameda', calculates the ratio of XCL_020 to XCL_019, sorts the results in d

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_020\" / \"XCL_019\" FROM frpm WHERE \"XCL_006\" = 'Alameda' ORDER BY (CAST(\"XCL_020\" AS REAL) / \"XCL_019\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:0"
  ]
}
```

### A program that joins 'schools' and 'satscores' on 'XCL_041' and 'XCL_030', filters for 'Active' schools, orders by 'XCL_037' in descending order, and 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_046\" FROM schools AS T1 INNER JOIN satscores AS T2 ON T1.\"XCL_041\" = T2.\"XCL_030\" WHERE T1.\"XCL_044\" = 'Active' ORDER BY T2.\"XCL_037\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:15"
  ]
}
```

### Query that joins satscores and schools on XCL_030 = XCL_041, orders by satscores.XCL_040 in descending order, and returns the top 1 row containing sat

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_039\", T2.\"XCL_050\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_040\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:44"
  ]
}
```

### A program that retrieves distinct combinations of XCL_045, XCL_047, and XCL_062 for the school with the most non-null XCL_047 entries among closed sch

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_045\", \"XCL_047\", \"XCL_062\" FROM schools WHERE \"XCL_045\" = (SELECT \"XCL_045\" FROM schools WHERE \"XCL_044\" = 'Closed' GROUP BY \"XCL_045\" ORDER BY COUNT(\"XCL_047\") DESC LIMIT 1) AND \"XCL_044\" = 'Closed' AND NOT \"XCL_047\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:49"
  ]
}
```

### A query that retrieves the XCL_074 identifier from the schools table, ordered by the absolute value of XCL_079 in descending order, limited to the top

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_074\" FROM schools ORDER BY ABS(\"XCL_079\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:82"
  ]
}
```

### A query program that joins satscores and frpm tables on school identifiers (XCL_030 = XCL_001), orders the results by the SAT score column (XCL_037) i

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_027\" FROM satscores AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_030\" = T2.\"XCL_001\" ORDER BY T1.\"XCL_037\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:10"
  ]
}
```

### A query that joins frpm and schools tables on XCL_001/XCL_041, orders by frpm.XCL_019 in descending order, and returns the XCL_061 attribute of the to

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_061\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_019\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:29"
  ]
}
```

### A query that joins 'frpm' (T1) and 'schools' (T2) on 'XCL_001' = 'XCL_041'. It groups the results by 'schools.XCL_050', calculates the sum of 'frpm.XC

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_050\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" GROUP BY T2.\"XCL_050\" ORDER BY SUM(T1.\"XCL_019\") ASC LIMIT 5",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:30"
  ]
}
```

### A SQL program that calculates the minimum XCL_017 from the frpm table by joining it with the schools table on XCL_001 = XCL_041, filtering for school 

```json
{
  "kind": "program",
  "formula": "SELECT MIN(T1.\"XCL_017\") FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_042\" = '0613360' AND T2.\"XCL_070\" = 'SPECON'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:74"
  ]
}
```

### Joins frpm to schools on frpm.XCL_001 = schools.XCL_041, orders by schools.XCL_078 descending, and returns the top 1 row containing frpm.XCL_010, frpm

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_010\", T1.\"XCL_008\", T2.\"XCL_078\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" ORDER BY T2.\"XCL_078\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:80"
  ]
}
```

### A SQL program that joins frpm and satscores on XCL_001 = XCL_030, filters for satscores where the ratio of XCL_040 to XCL_036 exceeds 0.3, and returns

```json
{
  "kind": "program",
  "formula": "SELECT MAX(CAST(T1.\"XCL_025\" AS REAL) / T1.\"XCL_024\") FROM frpm AS T1 INNER JOIN satscores AS T2 ON T1.\"XCL_001\" = T2.\"XCL_030\" WHERE CAST(T2.\"XCL_040\" AS REAL) / T2.\"XCL_036\" > 0.3",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:12"
  ]
}
```

### A query that joins satscores and schools on XCL_030 = XCL_041, filters for non-null XCL_038, and returns the single record (XCL_038, XCL_045) where th

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_038\", T2.\"XCL_045\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE NOT T1.\"XCL_038\" IS NULL ORDER BY T1.\"XCL_038\" + T1.\"XCL_037\" + T1.\"XCL_039\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:43"
  ]
}
```

### A query that joins the satscores table (T1) with the schools table (T2) on the key XCL_030 = XCL_041. It filters for schools in 'Los Angeles' (T2.XCL_

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_060\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T1.\"XCL_036\" BETWEEN 2000 AND 3000 AND T2.\"XCL_045\" = 'Los Angeles'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:38"
  ]
}
```

### Retrieves school attributes (XCL_058, XCL_059) for the school associated with the 333rd highest SAT score. Joins satscores and schools on XCL_030 = XC

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_058\", T2.\"XCL_059\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_039\" DESC LIMIT 1 OFFSET 332",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:57"
  ]
}
```

### A query that joins 'frpm' and 'schools' on 'XCL_001' = 'XCL_041'. It filters for schools where 'XCL_066' is 31, orders the results by 'frpm.XCL_019' i

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_047\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_066\" = 31 ORDER BY T1.\"XCL_019\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:46"
  ]
}
```

### A SQL program that joins the 'frpm' table (alias T1) with the 'schools' table (alias T2) on the school identifier ('XCL_001' = 'XCL_041'). It filters 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_008\") FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Amador' AND T1.\"XCL_017\" = 9 AND T1.\"XCL_018\" = 12",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:20"
  ]
}
```

### A query that selects XCL_042 from the schools table, restricted to rows where XCL_068 is 31. This represents a filtered subset of schools based on the

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_042\" FROM schools WHERE \"XCL_068\" = 31",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:69"
  ]
}
```

### A query that joins frpm and schools tables on XCL_001 = XCL_041. It filters for schools in 'Los Angeles' (XCL_045) with grade span 'K-9' (XCL_075). Th

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_047\", T1.\"XCL_027\" * 100 / T1.\"XCL_024\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Los Angeles' AND T2.\"XCL_075\" = 'K-9'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:77"
  ]
}
```

### Full SQL program that selects the ratio of XCL_025 to XCL_024 from the frpm table. It filters for records where XCL_011 equals 'Continuation School' a

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_025\" / \"XCL_024\" FROM frpm WHERE \"XCL_011\" = 'Continuation School' AND NOT \"XCL_025\" / \"XCL_024\" IS NULL ORDER BY \"XCL_025\" / \"XCL_024\" ASC LIMIT 3",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1"
  ]
}
```

### Filtered School Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_047\") FROM schools WHERE (\"XCL_044\" = 'Closed' OR \"XCL_044\" = 'Active') AND \"XCL_068\" = 69 AND \"XCL_045\" = 'Alpine'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:70"
  ]
}
```

### Query returning specific attributes (XCL_081, XCL_046, XCL_045, XCL_047) from the schools table, restricted to records where XCL_064 equals '0040'.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_081\", \"XCL_046\", \"XCL_045\", \"XCL_047\" FROM schools WHERE \"XCL_064\" = '0040'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:86"
  ]
}
```

### Full SQL program that joins schools and frpm tables on XCL_041 = XCL_001, filters for the school with first name 'Kacey' and last name 'Gibson', and c

```json
{
  "kind": "program",
  "formula": "SELECT CAST(T2.\"XCL_025\" AS REAL) / T2.\"XCL_024\" FROM schools AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_041\" = T2.\"XCL_001\" WHERE T1.\"XCL_080\" = 'Kacey' AND T1.\"XCL_081\" = 'Gibson'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:34"
  ]
}
```

### 7th Highest Score School Attributes

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_053\", T2.\"XCL_047\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_038\" DESC LIMIT 1 OFFSET 6",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:50"
  ]
}
```

### Query joining frpm and schools tables to retrieve school attributes XCL_073 and XCL_047 for records where frpm.XCL_012 equals 'Breakfast Provision 2' 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_073\", T2.\"XCL_047\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_012\" = 'Breakfast Provision 2' AND T1.\"XCL_003\" = 37",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:75"
  ]
}
```

### A program that joins 'satscores' and 'schools' tables, filters for a specific school type (XCL_076 = 'F'), ranks schools by score within groups (XCL_0

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_047\" FROM (SELECT T2.\"XCL_047\", T1.\"XCL_037\", RANK() OVER (PARTITION BY T2.\"XCL_045\" ORDER BY T1.\"XCL_037\" DESC) AS rnk FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_076\" = 'F') AS ranked_schools WHERE \"rnk\" <= 5",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:41"
  ]
}
```

### Full SQL program that selects from the schools table. It applies filters on XCL_066 (value 52), XCL_045 (value 'Alameda'), and XCL_061 (year 1980 via 

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(\"XCL_047\") AS REAL) / 12 FROM schools WHERE \"XCL_066\" = 52 AND \"XCL_045\" = 'Alameda' AND STRFTIME('%Y', \"XCL_061\") = '1980'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:47"
  ]
}
```

### A SQL program that joins frpm to schools on XCL_001 = XCL_041, filters schools by address 'PO Box 1040' and facility type 'Youth Authority Facilities'

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_027\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_053\" = 'PO Box 1040' AND T2.\"XCL_069\" = 'Youth Authority Facilities'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:73"
  ]
}
```

### Computes the rank of schools based on their SAT writing scores in descending order. The population is limited to schools with a non-null identifier (X

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_064\", \"XCL_039\", RANK() OVER (ORDER BY \"XCL_039\" DESC) AS WritingScoreRank FROM schools AS T1 INNER JOIN satscores AS T2 ON T1.\"XCL_041\" = T2.\"XCL_030\" WHERE T2.\"XCL_039\" > 499 AND NOT \"XCL_064\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:17"
  ]
}
```

### A query that joins frpm to schools on XCL_001 = XCL_041, filters for schools in Fresno (XCL_050 = 'Fresno') with XCL_077 = 0, and selects frpm.XCL_004

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_004\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_050\" = 'Fresno' AND T2.\"XCL_077\" = 0",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:71"
  ]
}
```

### Schools Ratio Query

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN \"XCL_066\" = 54 THEN 1 ELSE 0 END) AS REAL) / SUM(CASE WHEN \"XCL_066\" = 52 THEN 1 ELSE 0 END) FROM schools WHERE \"XCL_044\" = 'Merged' AND \"XCL_045\" = 'Orange'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:48"
  ]
}
```

### A query that joins satscores and frpm tables on a common key (XCL_030 = XCL_001), filters for entities in the 'Riverside' district (XCL_007 LIKE 'Rive

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_032\", T2.\"XCL_015\" FROM satscores AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_030\" = T2.\"XCL_001\" WHERE T2.\"XCL_007\" LIKE 'Riverside%' GROUP BY T1.\"XCL_032\", T2.\"XCL_015\" HAVING CAST(SUM(T1.\"XCL_038\") AS REAL) / COUNT(T1.\"XCL_030\") > 400",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:25"
  ]
}
```

### Full SQL program joining frpm and satscores on school identifier, filtering for directly funded schools in Fresno with SAT scores <= 250, and returnin

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_001\") FROM frpm AS T1 INNER JOIN satscores AS T2 ON T1.\"XCL_001\" = T2.\"XCL_030\" WHERE T1.\"XCL_015\" = 'Directly funded' AND T1.\"XCL_006\" = 'Fresno' AND T2.\"XCL_036\" <= 250",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:18"
  ]
}
```

### Retrieves specific attributes (XCL_080, XCL_081, XCL_083, XCL_084, XCL_086, XCL_087) from the schools table for the school with the maximum value in s

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_080\", T2.\"XCL_081\", T2.\"XCL_083\", T2.\"XCL_084\", T2.\"XCL_086\", T2.\"XCL_087\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_040\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:36"
  ]
}
```

### A full SQL program that retrieves school identifiers (XCL_060) from the schools table. It filters for records where XCL_045 is 'San Joaquin', XCL_076 

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_060\" FROM schools WHERE \"XCL_045\" = 'San Joaquin' AND \"XCL_076\" = 'P' AND \"XCL_063\" = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:60"
  ]
}
```

### A query that retrieves XCL_060 from the schools table where the combination of XCL_080 and XCL_081 matches either ('Mike', 'Larson') or ('Dante', 'Alv

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_060\" FROM schools WHERE (\"XCL_080\" = 'Mike' AND \"XCL_081\" = 'Larson') OR (\"XCL_080\" = 'Dante' AND \"XCL_081\" = 'Alvarez')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:59"
  ]
}
```

### Full SQL program that joins 'schools' and 'frpm' on 'XCL_041' = 'XCL_001' and filters for FRPM records where the combined value of 'XCL_019' and 'XCL_

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_001\" FROM schools AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_041\" = T2.\"XCL_001\" WHERE T2.\"XCL_019\" + T2.\"XCL_024\" > 500",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:11"
  ]
}
```

### First CA School FRPM Record

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_050\", T1.\"XCL_017\", T1.\"XCL_008\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_052\" = 'CA' ORDER BY T2.\"XCL_078\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:81"
  ]
}
```

### Identifies the single school with the minimum ratio of satscores.XCL_040 to satscores.XCL_036. Returns specific school attributes (XCL_048, XCL_050, X

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_048\", T2.\"XCL_050\", T2.\"XCL_052\", T2.\"XCL_051\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY CAST(T1.\"XCL_040\" AS REAL) / T1.\"XCL_036\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:37"
  ]
}
```

### A full SQL program that joins 'frpm' (T1) and 'schools' (T2) on 'XCL_001' = 'XCL_041'. It filters for schools in 'Merced' (T2.XCL_045) of type 'HS' (T

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_050\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_012\" = 'Lunch Provision 2' AND T2.\"XCL_045\" = 'Merced' AND T1.\"XCL_017\" = 9 AND T1.\"XCL_018\" = 12 AND T2.\"XCL_072\" = 'HS'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:76"
  ]
}
```

### Executes a SELECT statement to count rows in the schools table where XCL_066 equals 52, XCL_063 equals 1, and XCL_050 equals 'Hickman'.

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_047\") FROM schools WHERE \"XCL_066\" = 52 AND \"XCL_063\" = 1 AND \"XCL_050\" = 'Hickman'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:61"
  ]
}
```

### Fresno County FRPM-School Join Query

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_051\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_007\" = 'Fresno County Office of Education' AND T1.\"XCL_013\" = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:2"
  ]
}
```

### California school district ratio query

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN \"XCL_045\" = 'Colusa' THEN 1 ELSE 0 END) AS REAL) / SUM(CASE WHEN \"XCL_045\" = 'Humboldt' THEN 1 ELSE 0 END) FROM schools WHERE \"XCL_057\" = 'CA'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:55"
  ]
}
```

### A query that identifies the district with the highest count of 'F' records among 'San Diego' and 'Santa Barbara'. It filters for these two districts a

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_045\", COUNT(\"XCL_076\") FROM schools WHERE (\"XCL_045\" = 'San Diego' OR \"XCL_045\" = 'Santa Barbara') AND \"XCL_076\" = 'F' GROUP BY \"XCL_045\" ORDER BY COUNT(\"XCL_076\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:79"
  ]
}
```

### SQL program that selects the ratio of XCL_020 to XCL_019 from the frpm table. It orders the results by XCL_019 in descending order, skips the first 9 

```json
{
  "kind": "program",
  "formula": "SELECT CAST(\"XCL_020\" AS REAL) / \"XCL_019\" FROM frpm ORDER BY \"XCL_019\" DESC LIMIT 2 OFFSET 9",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:31"
  ]
}
```

### Filtered frpm XCL_008 extraction

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_008\" FROM satscores AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_030\" = T2.\"XCL_001\" WHERE CAST(T2.\"XCL_020\" AS REAL) / T2.\"XCL_019\" > 0.1 AND T1.\"XCL_040\" > 0",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:24"
  ]
}
```

### Full SQL program that joins satscores (T1) to schools (T2) on XCL_030 = XCL_041, filters for schools in 'Lakeport' and SAT records with a combined sco

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_030\") FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_055\" = 'Lakeport' AND (T1.\"XCL_037\" + T1.\"XCL_038\" + T1.\"XCL_039\") >= 1500",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:52"
  ]
}
```

### A query that joins 'satscores' and 'schools' on 'XCL_030' = 'XCL_041', orders by 'XCL_038' in descending order, and limits the result to 1 row. It ret

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_071\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_038\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:42"
  ]
}
```

### A SQL query that retrieves the XCL_032 value from satscores filtered by XCL_034 = 'Contra Costa' and non-null XCL_032, ordered by XCL_036 in descendin

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_032\" FROM satscores WHERE \"XCL_034\" = 'Contra Costa' AND NOT \"XCL_032\" IS NULL ORDER BY \"XCL_036\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:22"
  ]
}
```

### A query that joins satscores and schools on XCL_030 = XCL_041, orders by satscores.XCL_040 in descending order, and limits to 1 row to retrieve the sc

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_058\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_040\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:7"
  ]
}
```

### A program that joins 'schools' and 'satscores' on 'XCL_041' = 'XCL_030', orders by 'XCL_038' descending, and limits to 1 to retrieve the top-performin

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_058\" FROM schools AS T1 INNER JOIN satscores AS T2 ON T1.\"XCL_041\" = T2.\"XCL_030\" ORDER BY T2.\"XCL_038\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:19"
  ]
}
```

### Full SQL program that computes the locally funded to non-locally funded ratio for schools in Santa Clara (XCL_045 = 'Santa Clara') where XCL_063 equal

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN \"XCL_065\" = 'Locally funded' THEN 1 ELSE 0 END) AS REAL) * 100 / SUM(CASE WHEN \"XCL_065\" <> 'Locally funded' THEN 1 ELSE 0 END) FROM schools WHERE \"XCL_045\" = 'Santa Clara' AND \"XCL_063\" = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:65"
  ]
}
```

### Full SQL program that joins the frpm and schools tables on XCL_001 = XCL_041, filters for Los Angeles schools with XCL_063 = 0 and a calculated FRPM p

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_047\") FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Los Angeles' AND T2.\"XCL_063\" = 0 AND CAST(T1.\"XCL_020\" AS REAL) * 100 / T1.\"XCL_019\" < 0.18",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:62"
  ]
}
```

### Full program retrieving the school identifier and SAT score for the school 'Ricci Ulrich' by joining 'satscores' and 'schools' on their respective ID 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_047\", T1.\"XCL_039\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_080\" = 'Ricci' AND T2.\"XCL_081\" = 'Ulrich'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:45"
  ]
}
```

### Executes a count on the 'schools' table, filtering for records where the year extracted from XCL_061 is between 2000 and 2005, XCL_045 equals 'Stanisl

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_047\") FROM schools WHERE STRFTIME('%Y', \"XCL_061\") BETWEEN '2000' AND '2005' AND \"XCL_045\" = 'Stanislaus' AND \"XCL_065\" = 'Directly funded'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:66"
  ]
}
```

### Query joining schools and frpm tables on XCL_041 = XCL_001, filtering for records where frpm.XCL_019 minus frpm.XCL_024 is greater than 30, and return

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_047\", T1.\"XCL_048\" FROM schools AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_041\" = T2.\"XCL_001\" WHERE T2.\"XCL_019\" - T2.\"XCL_024\" > 30",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:23"
  ]
}
```

### Query that retrieves specific attributes (XCL_058, XCL_059, XCL_047) from the schools table where the identifier XCL_051 matches the literal '95203-37

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_058\", \"XCL_059\", \"XCL_047\" FROM schools WHERE \"XCL_051\" = '95203-3704'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:58"
  ]
}
```

### A SQL program that identifies the most common value of "XCL_075" among schools where "XCL_050" is 'Adelanto'. It groups by "XCL_075", orders by the co

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_075\" FROM schools WHERE \"XCL_050\" = 'Adelanto' GROUP BY \"XCL_075\" ORDER BY COUNT(\"XCL_075\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:78"
  ]
}
```

### A query that retrieves SAT scores (XCL_036) by joining the satscores table with the schools table on the school identifier (XCL_030 = XCL_041) and fil

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_036\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_055\" = 'Fresno'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:53"
  ]
}
```

### A full program that joins the frpm and schools tables on school identifier (XCL_001 = XCL_041). It filters for K-8 schools (XCL_074='K-8') with XCL_07

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_050\", COUNT(T2.\"XCL_041\") FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_077\" = 1 AND T2.\"XCL_074\" = 'K-8' AND T1.\"XCL_012\" = 'Multiple Provision Types' GROUP BY T2.\"XCL_050\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:83"
  ]
}
```

### Full SQL program that queries the 'schools' table to count entries where the county is 'San Joaquin', the state is 'CA', and the status is 'Active'. T

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_041\") FROM schools WHERE \"XCL_050\" = 'San Joaquin' AND \"XCL_057\" = 'CA' AND \"XCL_044\" = 'Active'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:56"
  ]
}
```

### Executes a SELECT COUNT on the frpm table with specific filters: XCL_006 equals 'Los Angeles', XCL_020 exceeds 500, and XCL_022 is below 700. Returns 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_001\") FROM frpm WHERE \"XCL_006\" = 'Los Angeles' AND \"XCL_020\" > 500 AND \"XCL_022\" < 700",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:21"
  ]
}
```

### A query that joins satscores and schools on their respective ID columns (XCL_030 and XCL_041), orders the results by the SAT score column (XCL_040) in

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_082\", T2.\"XCL_047\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_040\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:88"
  ]
}
```

### A query that joins SAT scores to schools, filters for the Fresno Unified district and non-null scores, orders by score ascending, and returns the iden

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_058\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_046\" = 'Fresno Unified' AND NOT T1.\"XCL_037\" IS NULL ORDER BY T1.\"XCL_037\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:40"
  ]
}
```

### Filtered School Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(*) FROM schools WHERE \"XCL_064\" = '00D4' AND \"XCL_055\" = 'Hickman'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:64"
  ]
}
```

### Computed ratio of column XCL_025 divided by column XCL_024. Returns a single numeric value per row in the frpm table, filtered to rows where XCL_011 i

```json
{
  "kind": "binding",
  "formula": "\"frpm\".\"XCL_025\" / \"frpm\".\"XCL_024\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_025\" / \"XCL_024\" FROM frpm WHERE \"XCL_011\" = 'Continuation School' AND NOT \"XCL_025\" / \"XCL_024\" IS NULL ORDER BY \"XCL_025\" / \"XCL_024\" ASC LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1"
  ]
}
```

### "schools"."XCL_080" = 'Avetik' AND "schools"."XCL_081" = 'Atoian'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_080\" = 'Avetik' AND \"schools\".\"XCL_081\" = 'Atoian'",
  "grain": [],
  "population_scope": "SELECT \"XCL_047\", \"XCL_056\" FROM schools WHERE \"XCL_080\" = 'Avetik' AND \"XCL_081\" = 'Atoian'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:54"
  ]
}
```

### The value of column XCL_027 from the frpm table, returned for records joined to schools where the school address is 'PO Box 1040' and the facility typ

```json
{
  "kind": "binding",
  "formula": "\"frpm\".\"XCL_027\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_027\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_053\" = 'PO Box 1040' AND T2.\"XCL_069\" = 'Youth Authority Facilities'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_027\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_027\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_053\" = 'PO Box 1040' AND \"r1\".\"XCL_069\" = 'Youth Authority Facilities'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:73"
  ]
}
```

### "schools"."XCL_064" = '00D4' AND "schools"."XCL_055" = 'Hickman'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_064\" = '00D4' AND \"schools\".\"XCL_055\" = 'Hickman'",
  "grain": [],
  "population_scope": "SELECT COUNT(*) FROM schools WHERE \"XCL_064\" = '00D4' AND \"XCL_055\" = 'Hickman'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:64"
  ]
}
```

### Output column from the schools table (alias T2). Represents a school attribute selected for each row in the joined result set.

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_058\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\", T1.\"XCL_039\", T2.\"XCL_058\" FROM schools AS T2 LEFT JOIN satscores AS T1 ON T2.\"XCL_041\" = T1.\"XCL_030\" WHERE STRFTIME('%Y', T2.\"XCL_061\") > '1991' OR STRFTIME('%Y', T2.\"XCL_062\") < '2000'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_058\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      },
      {
        "role": "r1",
        "physical_table": "satscores"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_058\" AS \"value\" FROM schools AS \"r0\" LEFT JOIN satscores AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_030\" WHERE STRFTIME('%Y', \"r0\".\"XCL_061\") > '1991' OR STRFTIME('%Y', \"r0\".\"XCL_062\") < '2000'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:27"
  ]
}
```

### Output column from the satscores table (alias T1). Represents a score attribute selected for each row in the joined result set.

```json
{
  "kind": "binding",
  "formula": "\"satscores\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\", T1.\"XCL_039\", T2.\"XCL_058\" FROM schools AS T2 LEFT JOIN satscores AS T1 ON T2.\"XCL_041\" = T1.\"XCL_030\" WHERE STRFTIME('%Y', T2.\"XCL_061\") > '1991' OR STRFTIME('%Y', T2.\"XCL_062\") < '2000'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_039\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      },
      {
        "role": "r1",
        "physical_table": "satscores"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_039\" AS \"value\" FROM schools AS \"r0\" LEFT JOIN satscores AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_030\" WHERE STRFTIME('%Y', \"r0\".\"XCL_061\") > '1991' OR STRFTIME('%Y', \"r0\".\"XCL_062\") < '2000'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:27"
  ]
}
```

### School Attribute (XCL_047)

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_082\", T2.\"XCL_047\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_040\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:88"
  ]
}
```

### Returns the value of column XCL_047 from the schools table for records where XCL_080 is 'Avetik' and XCL_081 is 'Atoian'. Grain is individual school r

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_047\", \"XCL_056\" FROM schools WHERE \"XCL_080\" = 'Avetik' AND \"XCL_081\" = 'Atoian'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_047\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_047\" AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_080\" = 'Avetik' AND \"r0\".\"XCL_081\" = 'Atoian'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:54"
  ]
}
```

### School Attribute XCL_050

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_050\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_080\", \"XCL_081\", \"XCL_047\", \"XCL_050\" FROM schools WHERE \"XCL_063\" = 1 AND \"XCL_064\" = '00D2'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_050\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_050\" AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_063\" = 1 AND \"r0\".\"XCL_064\" = '00D2'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:63"
  ]
}
```

### Computed metric representing the ratio of column XCL_020 to column XCL_019, with XCL_020 cast to REAL to ensure floating-point division. The result is

```json
{
  "kind": "binding",
  "formula": "CAST(\"frpm\".\"XCL_020\" AS REAL) / \"frpm\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT CAST(\"XCL_020\" AS REAL) / \"XCL_019\" FROM frpm ORDER BY \"XCL_019\" DESC LIMIT 2 OFFSET 9",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:31"
  ]
}
```

### School Attribute XCL_081

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_081\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_081\", \"XCL_046\", \"XCL_045\", \"XCL_047\" FROM schools WHERE \"XCL_064\" = '0040'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_081\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_081\" AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_064\" = '0040'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:86"
  ]
}
```

### Aggregates the count of records from the 'frpm' table (aliased as T2) where the school is 'Directly funded' (T2."XCL_015") and the associated 'satscor

```json
{
  "kind": "metric",
  "formula": "COUNT(\"frpm\".\"XCL_005\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_005\") FROM satscores AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_030\" = T2.\"XCL_001\" WHERE T1.\"XCL_038\" > 560 AND T2.\"XCL_015\" = 'Directly funded'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_005\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "satscores"
      },
      {
        "role": "r1",
        "physical_table": "frpm"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_005\") AS \"value\" FROM satscores AS \"r0\" INNER JOIN frpm AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_001\" WHERE \"r0\".\"XCL_038\" > 560 AND \"r1\".\"XCL_015\" = 'Directly funded'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:9"
  ]
}
```

### "schools"."XCL_044" = 'Merged' AND "schools"."XCL_045" = 'Orange'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_044\" = 'Merged' AND \"schools\".\"XCL_045\" = 'Orange'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN \"XCL_066\" = 54 THEN 1 ELSE 0 END) AS REAL) / SUM(CASE WHEN \"XCL_066\" = 52 THEN 1 ELSE 0 END) FROM schools WHERE \"XCL_044\" = 'Merged' AND \"XCL_045\" = 'Orange'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:48"
  ]
}
```

### "schools"."XCL_057" = 'CA'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_057\" = 'CA'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN \"XCL_045\" = 'Colusa' THEN 1 ELSE 0 END) AS REAL) / SUM(CASE WHEN \"XCL_045\" = 'Humboldt' THEN 1 ELSE 0 END) FROM schools WHERE \"XCL_057\" = 'CA'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:55"
  ]
}
```

### Returns the value of column XCL_056 from the schools table for records where XCL_080 is 'Avetik' and XCL_081 is 'Atoian'. Grain is individual school r

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_056\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_047\", \"XCL_056\" FROM schools WHERE \"XCL_080\" = 'Avetik' AND \"XCL_081\" = 'Atoian'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_056\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_056\" AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_080\" = 'Avetik' AND \"r0\".\"XCL_081\" = 'Atoian'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:54"
  ]
}
```

### School Attribute XCL_081

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_081\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_080\", \"XCL_081\", \"XCL_047\", \"XCL_050\" FROM schools WHERE \"XCL_063\" = 1 AND \"XCL_064\" = '00D2'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_081\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_081\" AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_063\" = 1 AND \"r0\".\"XCL_064\" = '00D2'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:63"
  ]
}
```

### School Identifier

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_060\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_060\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T1.\"XCL_036\" BETWEEN 2000 AND 3000 AND T2.\"XCL_045\" = 'Los Angeles'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_060\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "satscores"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_060\" AS \"value\" FROM satscores AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_041\" WHERE \"r0\".\"XCL_036\" BETWEEN 2000 AND 3000 AND \"r1\".\"XCL_045\" = 'Los Angeles'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:38"
  ]
}
```

### "frpm"."XCL_012" = 'Breakfast Provision 2' AND "frpm"."XCL_003" = 37

```json
{
  "kind": "predicate",
  "formula": "\"frpm\".\"XCL_012\" = 'Breakfast Provision 2' AND \"frpm\".\"XCL_003\" = 37",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_073\", T2.\"XCL_047\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_012\" = 'Breakfast Provision 2' AND T1.\"XCL_003\" = 37",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:75"
  ]
}
```

### Count of Schools

```json
{
  "kind": "metric",
  "formula": "COUNT(\"schools\".\"XCL_047\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_047\") FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Los Angeles' AND T2.\"XCL_063\" = 0 AND CAST(T1.\"XCL_020\" AS REAL) * 100 / T1.\"XCL_019\" < 0.18",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_047\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_047\") AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_045\" = 'Los Angeles' AND \"r1\".\"XCL_063\" = 0 AND CAST(\"r0\".\"XCL_020\" AS REAL) * 100 / \"r0\".\"XCL_019\" < 0.18",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:62"
  ]
}
```

### "frpm"."XCL_017"

```json
{
  "kind": "binding",
  "formula": "\"frpm\".\"XCL_017\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_050\", T1.\"XCL_017\", T1.\"XCL_008\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_052\" = 'CA' ORDER BY T2.\"XCL_078\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:81"
  ]
}
```

### School Identifier

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_050\"",
  "grain": [
    "\"schools\".\"XCL_050\""
  ],
  "population_scope": "SELECT T2.\"XCL_050\", COUNT(T2.\"XCL_041\") FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_077\" = 1 AND T2.\"XCL_074\" = 'K-8' AND T1.\"XCL_012\" = 'Multiple Provision Types' GROUP BY T2.\"XCL_050\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_050\"",
    "grain": [
      "\"r1\".\"XCL_050\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_050\" AS \"grain_0\", \"r1\".\"XCL_050\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_077\" = 1 AND \"r1\".\"XCL_074\" = 'K-8' AND \"r0\".\"XCL_012\" = 'Multiple Provision Types' GROUP BY \"r1\".\"XCL_050\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:83"
  ]
}
```

### Aggregates the count of non-null values in column XCL_047 from the schools table, filtered by specific conditions on XCL_066, XCL_063, and XCL_050.

```json
{
  "kind": "metric",
  "formula": "COUNT(\"schools\".\"XCL_047\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_047\") FROM schools WHERE \"XCL_066\" = 52 AND \"XCL_063\" = 1 AND \"XCL_050\" = 'Hickman'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_047\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_047\") AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_066\" = 52 AND \"r0\".\"XCL_063\" = 1 AND \"r0\".\"XCL_050\" = 'Hickman'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:61"
  ]
}
```

### "frpm"."XCL_019" + "frpm"."XCL_024" > 500

```json
{
  "kind": "predicate",
  "formula": "\"frpm\".\"XCL_019\" + \"frpm\".\"XCL_024\" > 500",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_001\" FROM schools AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_041\" = T2.\"XCL_001\" WHERE T2.\"XCL_019\" + T2.\"XCL_024\" > 500",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:11"
  ]
}
```

### School Attribute XCL_047

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_073\", T2.\"XCL_047\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_012\" = 'Breakfast Provision 2' AND T1.\"XCL_003\" = 37",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_047\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_047\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r0\".\"XCL_012\" = 'Breakfast Provision 2' AND \"r0\".\"XCL_003\" = 37",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:75"
  ]
}
```

### "schools"."XCL_050" = 'Fresno' AND "schools"."XCL_077" = 0

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_050\" = 'Fresno' AND \"schools\".\"XCL_077\" = 0",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_004\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_050\" = 'Fresno' AND T2.\"XCL_077\" = 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:71"
  ]
}
```

### Name or descriptive label from the schools table (T2) for the school associated with the SAT score record having the minimum non-null value in column 

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_053\", T2.\"XCL_047\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE NOT T1.\"XCL_037\" IS NULL ORDER BY T1.\"XCL_037\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:51"
  ]
}
```

### "schools"."XCL_080" = 'Alusine'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_080\" = 'Alusine'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_020\" * 100 / T1.\"XCL_019\", T1.\"XCL_004\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_080\" = 'Alusine'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:85"
  ]
}
```

### School Attribute XCL_058

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_058\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_058\", \"XCL_059\", \"XCL_047\" FROM schools WHERE \"XCL_051\" = '95203-3704'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_058\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_058\" AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_051\" = '95203-3704'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:58"
  ]
}
```

### A scalar metric calculated as the count of rows where XCL_066 equals 54 divided by the count of rows where XCL_066 equals 52. The numerator is cast to

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"schools\".\"XCL_066\" = 54 THEN 1 ELSE 0 END) AS REAL) / SUM(CASE WHEN \"schools\".\"XCL_066\" = 52 THEN 1 ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN \"XCL_066\" = 54 THEN 1 ELSE 0 END) AS REAL) / SUM(CASE WHEN \"XCL_066\" = 52 THEN 1 ELSE 0 END) FROM schools WHERE \"XCL_044\" = 'Merged' AND \"XCL_045\" = 'Orange'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r0\".\"XCL_066\" = 54 THEN 1 ELSE 0 END) AS REAL) / SUM(CASE WHEN \"r0\".\"XCL_066\" = 52 THEN 1 ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r0\".\"XCL_066\" = 54 THEN 1 ELSE 0 END) AS REAL) / SUM(CASE WHEN \"r0\".\"XCL_066\" = 52 THEN 1 ELSE 0 END) AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_044\" = 'Merged' AND \"r0\".\"XCL_045\" = 'Orange'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:48"
  ]
}
```

### ("schools"."XCL_080" = 'Mike' AND "schools"."XCL_081" = 'Larson') OR ("schools"."XCL_080" = 'Dante' AND "schools"."XCL_081" = 'Alvarez')

```json
{
  "kind": "predicate",
  "formula": "(\"schools\".\"XCL_080\" = 'Mike' AND \"schools\".\"XCL_081\" = 'Larson') OR (\"schools\".\"XCL_080\" = 'Dante' AND \"schools\".\"XCL_081\" = 'Alvarez')",
  "grain": [],
  "population_scope": "SELECT \"XCL_060\" FROM schools WHERE (\"XCL_080\" = 'Mike' AND \"XCL_081\" = 'Larson') OR (\"XCL_080\" = 'Dante' AND \"XCL_081\" = 'Alvarez')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:59"
  ]
}
```

### RANK() OVER (PARTITION BY "schools"."XCL_045" ORDER BY "satscores"."XCL_037" DESC) <= 5

```json
{
  "kind": "predicate",
  "formula": "RANK() OVER (PARTITION BY \"schools\".\"XCL_045\" ORDER BY \"satscores\".\"XCL_037\" DESC) <= 5",
  "grain": [],
  "population_scope": "SELECT \"XCL_047\" FROM (SELECT T2.\"XCL_047\", T1.\"XCL_037\", RANK() OVER (PARTITION BY T2.\"XCL_045\" ORDER BY T1.\"XCL_037\" DESC) AS rnk FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_076\" = 'F') AS ranked_schools WHERE \"rnk\" <= 5",
  "upstream_scopes": [
    "SELECT T2.\"XCL_047\", T1.\"XCL_037\", RANK() OVER (PARTITION BY T2.\"XCL_045\" ORDER BY T1.\"XCL_037\" DESC) AS rnk FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_076\" = 'F'"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:41"
  ]
}
```

### "schools"."XCL_064" = '0040'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_064\" = '0040'",
  "grain": [],
  "population_scope": "SELECT \"XCL_081\", \"XCL_046\", \"XCL_045\", \"XCL_047\" FROM schools WHERE \"XCL_064\" = '0040'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:86"
  ]
}
```

### School Attribute XCL_080

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_080\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_080\", \"XCL_081\", \"XCL_047\", \"XCL_050\" FROM schools WHERE \"XCL_063\" = 1 AND \"XCL_064\" = '00D2'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_080\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_080\" AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_063\" = 1 AND \"r0\".\"XCL_064\" = '00D2'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:63"
  ]
}
```

### Value of column XCL_051 from the schools table, representing a specific attribute of the school record for the filtered population.

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_051\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_008\", T2.\"XCL_048\", T2.\"XCL_050\", T2.\"XCL_052\", T2.\"XCL_051\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Monterey' AND T1.\"XCL_025\" > 800 AND T1.\"XCL_010\" = 'High Schools (Public)'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_051\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_051\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_045\" = 'Monterey' AND \"r0\".\"XCL_025\" > 800 AND \"r0\".\"XCL_010\" = 'High Schools (Public)'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:26"
  ]
}
```

### FRPM XCL_008

```json
{
  "kind": "binding",
  "formula": "\"frpm\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_060\", T1.\"XCL_008\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_025\" BETWEEN 1900 AND 2000 AND NOT T2.\"XCL_060\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_008\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r0\".\"XCL_025\" BETWEEN 1900 AND 2000 AND NOT \"r1\".\"XCL_060\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:33"
  ]
}
```

### "schools"."XCL_065" = 'Locally funded'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_065\" = 'Locally funded'",
  "grain": [],
  "population_scope": "SELECT AVG(T3.\"XCL_019\" - T3.\"XCL_024\") FROM frpm AS T3 INNER JOIN schools AS T4 ON T3.\"XCL_001\" = T4.\"XCL_041\" WHERE T4.\"XCL_065\" = 'Locally funded'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:28"
  ]
}
```

### School Attribute XCL_046

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_046\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_081\", \"XCL_046\", \"XCL_045\", \"XCL_047\" FROM schools WHERE \"XCL_064\" = '0040'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_046\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_046\" AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_064\" = '0040'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:86"
  ]
}
```

### School Attribute XCL_062

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_062\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_045\", \"XCL_047\", \"XCL_062\" FROM schools WHERE \"XCL_045\" = (SELECT \"XCL_045\" FROM schools WHERE \"XCL_044\" = 'Closed' GROUP BY \"XCL_045\" ORDER BY COUNT(\"XCL_047\") DESC LIMIT 1) AND \"XCL_044\" = 'Closed' AND NOT \"XCL_047\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:49"
  ]
}
```

### Aggregates the count of school records (identified by XCL_041) filtered to those located in San Joaquin County (XCL_050), California (XCL_057), with a

```json
{
  "kind": "metric",
  "formula": "COUNT(\"schools\".\"XCL_041\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_041\") FROM schools WHERE \"XCL_050\" = 'San Joaquin' AND \"XCL_057\" = 'CA' AND \"XCL_044\" = 'Active'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_041\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_041\") AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_050\" = 'San Joaquin' AND \"r0\".\"XCL_057\" = 'CA' AND \"r0\".\"XCL_044\" = 'Active'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:56"
  ]
}
```

### "schools"."XCL_052" = 'CA'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_052\" = 'CA'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_050\", T1.\"XCL_017\", T1.\"XCL_008\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_052\" = 'CA' ORDER BY T2.\"XCL_078\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:81"
  ]
}
```

### Aggregates the total number of school records (identified by XCL_047) that match specific criteria. The population is restricted to schools in 'San Fr

```json
{
  "kind": "metric",
  "formula": "COUNT(\"schools\".\"XCL_047\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_047\") FROM schools WHERE STRFTIME('%Y', \"XCL_062\") = '1989' AND \"XCL_050\" = 'San Francisco' AND \"XCL_067\" = 'Community College District'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_047\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_047\") AS \"value\" FROM schools AS \"r0\" WHERE STRFTIME('%Y', \"r0\".\"XCL_062\") = '1989' AND \"r0\".\"XCL_050\" = 'San Francisco' AND \"r0\".\"XCL_067\" = 'Community College District'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:67"
  ]
}
```

### "schools"."XCL_045" = 'Monterey' AND "frpm"."XCL_025" > 800 AND "frpm"."XCL_010" = 'High Schools (Public)'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_045\" = 'Monterey' AND \"frpm\".\"XCL_025\" > 800 AND \"frpm\".\"XCL_010\" = 'High Schools (Public)'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_008\", T2.\"XCL_048\", T2.\"XCL_050\", T2.\"XCL_052\", T2.\"XCL_051\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Monterey' AND T1.\"XCL_025\" > 800 AND T1.\"XCL_010\" = 'High Schools (Public)'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:26"
  ]
}
```

### School Identifier

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_045\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_045\", \"XCL_047\", \"XCL_062\" FROM schools WHERE \"XCL_045\" = (SELECT \"XCL_045\" FROM schools WHERE \"XCL_044\" = 'Closed' GROUP BY \"XCL_045\" ORDER BY COUNT(\"XCL_047\") DESC LIMIT 1) AND \"XCL_044\" = 'Closed' AND NOT \"XCL_047\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:49"
  ]
}
```

### Aggregates the total number of rows in the frpm table where XCL_006 is 'Los Angeles', XCL_020 is greater than 500, and XCL_022 is less than 700. The g

```json
{
  "kind": "metric",
  "formula": "COUNT(\"frpm\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM frpm WHERE \"XCL_006\" = 'Los Angeles' AND \"XCL_020\" > 500 AND \"XCL_022\" < 700",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM frpm AS \"r0\" WHERE \"r0\".\"XCL_006\" = 'Los Angeles' AND \"r0\".\"XCL_020\" > 500 AND \"r0\".\"XCL_022\" < 700",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:21"
  ]
}
```

### "schools"."XCL_080" = 'Kacey' AND "schools"."XCL_081" = 'Gibson'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_080\" = 'Kacey' AND \"schools\".\"XCL_081\" = 'Gibson'",
  "grain": [],
  "population_scope": "SELECT CAST(T2.\"XCL_025\" AS REAL) / T2.\"XCL_024\" FROM schools AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_041\" = T2.\"XCL_001\" WHERE T1.\"XCL_080\" = 'Kacey' AND T1.\"XCL_081\" = 'Gibson'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:34"
  ]
}
```

### Computed ratio of frpm.XCL_022 to frpm.XCL_019, cast to REAL. Grain: one row per frpm record joined to schools where schools.XCL_068 = 66. Used as the

```json
{
  "kind": "binding",
  "formula": "CAST(\"frpm\".\"XCL_022\" AS REAL) / \"frpm\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT CAST(T1.\"XCL_022\" AS REAL) / T1.\"XCL_019\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_068\" = 66 ORDER BY T1.\"XCL_022\" DESC LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:32"
  ]
}
```

### The value of the 'XCL_046' column from the 'schools' table for the single active school with the highest 'XCL_037' score in the 'satscores' table.

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_046\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_046\" FROM schools AS T1 INNER JOIN satscores AS T2 ON T1.\"XCL_041\" = T2.\"XCL_030\" WHERE T1.\"XCL_044\" = 'Active' ORDER BY T2.\"XCL_037\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:15"
  ]
}
```

### "schools"."XCL_066" = 31

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_066\" = 31",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_066\" = 31 ORDER BY T1.\"XCL_019\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:46"
  ]
}
```

### "frpm"."XCL_007" = 'Fresno County Office of Education' AND "frpm"."XCL_013" = 1

```json
{
  "kind": "predicate",
  "formula": "\"frpm\".\"XCL_007\" = 'Fresno County Office of Education' AND \"frpm\".\"XCL_013\" = 1",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_051\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_007\" = 'Fresno County Office of Education' AND T1.\"XCL_013\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:2"
  ]
}
```

### Value of column XCL_008 from the frpm table for the single record with the highest schools.XCL_078 value.

```json
{
  "kind": "binding",
  "formula": "\"frpm\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_010\", T1.\"XCL_008\", T2.\"XCL_078\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" ORDER BY T2.\"XCL_078\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:80"
  ]
}
```

### "satscores"."XCL_034" = 'Contra Costa' AND NOT "satscores"."XCL_032" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"satscores\".\"XCL_034\" = 'Contra Costa' AND NOT \"satscores\".\"XCL_032\" IS NULL",
  "grain": [],
  "population_scope": "SELECT \"XCL_032\" FROM satscores WHERE \"XCL_034\" = 'Contra Costa' AND NOT \"XCL_032\" IS NULL ORDER BY \"XCL_036\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:22"
  ]
}
```

### School Identifier

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_074\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_074\" FROM schools ORDER BY ABS(\"XCL_079\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:82"
  ]
}
```

### STRFTIME('%Y', "schools"."XCL_061") > '1991' OR STRFTIME('%Y', "schools"."XCL_062") < '2000'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"schools\".\"XCL_061\") > '1991' OR STRFTIME('%Y', \"schools\".\"XCL_062\") < '2000'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\", T1.\"XCL_039\", T2.\"XCL_058\" FROM schools AS T2 LEFT JOIN satscores AS T1 ON T2.\"XCL_041\" = T1.\"XCL_030\" WHERE STRFTIME('%Y', T2.\"XCL_061\") > '1991' OR STRFTIME('%Y', T2.\"XCL_062\") < '2000'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:27"
  ]
}
```

### CAST(SUM("satscores"."XCL_038") AS REAL) / COUNT("satscores"."XCL_030") > 400

```json
{
  "kind": "predicate",
  "formula": "CAST(SUM(\"satscores\".\"XCL_038\") AS REAL) / COUNT(\"satscores\".\"XCL_030\") > 400",
  "grain": [
    "\"satscores\".\"XCL_032\"",
    "\"frpm\".\"XCL_015\""
  ],
  "population_scope": "SELECT T1.\"XCL_032\", T2.\"XCL_015\" FROM satscores AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_030\" = T2.\"XCL_001\" WHERE T2.\"XCL_007\" LIKE 'Riverside%' GROUP BY T1.\"XCL_032\", T2.\"XCL_015\" HAVING CAST(SUM(T1.\"XCL_038\") AS REAL) / COUNT(T1.\"XCL_030\") > 400",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:25"
  ]
}
```

### "frpm"."XCL_015" = 'Directly funded' AND "frpm"."XCL_006" = 'Fresno' AND "satscores"."XCL_036" <= 250

```json
{
  "kind": "predicate",
  "formula": "\"frpm\".\"XCL_015\" = 'Directly funded' AND \"frpm\".\"XCL_006\" = 'Fresno' AND \"satscores\".\"XCL_036\" <= 250",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM frpm AS T1 INNER JOIN satscores AS T2 ON T1.\"XCL_001\" = T2.\"XCL_030\" WHERE T1.\"XCL_015\" = 'Directly funded' AND T1.\"XCL_006\" = 'Fresno' AND T2.\"XCL_036\" <= 250",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:18"
  ]
}
```

### Ratio of frpm.XCL_025 to frpm.XCL_024, computed by casting XCL_025 to REAL and dividing by XCL_024. Returns one value per joined row for the specific 

```json
{
  "kind": "binding",
  "formula": "CAST(\"frpm\".\"XCL_025\" AS REAL) / \"frpm\".\"XCL_024\"",
  "grain": [],
  "population_scope": "SELECT CAST(T2.\"XCL_025\" AS REAL) / T2.\"XCL_024\" FROM schools AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_041\" = T2.\"XCL_001\" WHERE T1.\"XCL_080\" = 'Kacey' AND T1.\"XCL_081\" = 'Gibson'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(\"r1\".\"XCL_025\" AS REAL) / \"r1\".\"XCL_024\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      },
      {
        "role": "r1",
        "physical_table": "frpm"
      }
    ],
    "scope_sql": "SELECT CAST(\"r1\".\"XCL_025\" AS REAL) / \"r1\".\"XCL_024\" AS \"value\" FROM schools AS \"r0\" INNER JOIN frpm AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_001\" WHERE \"r0\".\"XCL_080\" = 'Kacey' AND \"r0\".\"XCL_081\" = 'Gibson'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:34"
  ]
}
```

### School XCL_046 Attribute

```json
{
  "kind": "binding",
  "formula": "T1.\"XCL_046\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_080\", T1.\"XCL_046\" FROM schools AS T1 INNER JOIN (SELECT \"XCL_080\" FROM schools GROUP BY \"XCL_080\" ORDER BY COUNT(\"XCL_080\") DESC LIMIT 2) AS T2 ON T1.\"XCL_080\" = T2.\"XCL_080\"",
  "upstream_scopes": [
    "SELECT \"XCL_080\" FROM schools GROUP BY \"XCL_080\" ORDER BY COUNT(\"XCL_080\") DESC LIMIT 2"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:84"
  ]
}
```

### School Attribute XCL_048

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_048\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_048\", T2.\"XCL_050\", T2.\"XCL_052\", T2.\"XCL_051\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY CAST(T1.\"XCL_040\" AS REAL) / T1.\"XCL_036\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:37"
  ]
}
```

### Returns the value of column XCL_058 from the schools table. The population is restricted to schools that are linked via XCL_041 to FRPM records where 

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_058\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_058\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_015\" = 'Directly funded' AND T1.\"XCL_013\" = 1 AND T2.\"XCL_061\" > '2000-01-01'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_058\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_058\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r0\".\"XCL_015\" = 'Directly funded' AND \"r0\".\"XCL_013\" = 1 AND \"r1\".\"XCL_061\" > '2000-01-01'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:4"
  ]
}
```

### Returns the value of the 'XCL_050' column from the 'schools' table. The population is restricted to schools in 'Merced' (XCL_045) of type 'HS' (XCL_07

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_050\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_050\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_012\" = 'Lunch Provision 2' AND T2.\"XCL_045\" = 'Merced' AND T1.\"XCL_017\" = 9 AND T1.\"XCL_018\" = 12 AND T2.\"XCL_072\" = 'HS'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_050\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_050\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r0\".\"XCL_012\" = 'Lunch Provision 2' AND \"r1\".\"XCL_045\" = 'Merced' AND \"r0\".\"XCL_017\" = 9 AND \"r0\".\"XCL_018\" = 12 AND \"r1\".\"XCL_072\" = 'HS'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:76"
  ]
}
```

### "frpm"."XCL_006" = 'Los Angeles' AND "frpm"."XCL_020" > 500 AND "frpm"."XCL_022" < 700

```json
{
  "kind": "predicate",
  "formula": "\"frpm\".\"XCL_006\" = 'Los Angeles' AND \"frpm\".\"XCL_020\" > 500 AND \"frpm\".\"XCL_022\" < 700",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM frpm WHERE \"XCL_006\" = 'Los Angeles' AND \"XCL_020\" > 500 AND \"XCL_022\" < 700",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:21"
  ]
}
```

### "frpm"."XCL_011" = 'Continuation School' AND NOT "frpm"."XCL_025" / "frpm"."XCL_024" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"frpm\".\"XCL_011\" = 'Continuation School' AND NOT \"frpm\".\"XCL_025\" / \"frpm\".\"XCL_024\" IS NULL",
  "grain": [],
  "population_scope": "SELECT \"XCL_025\" / \"XCL_024\" FROM frpm WHERE \"XCL_011\" = 'Continuation School' AND NOT \"XCL_025\" / \"XCL_024\" IS NULL ORDER BY \"XCL_025\" / \"XCL_024\" ASC LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1"
  ]
}
```

### STRFTIME('%Y', "schools"."XCL_061") = '1980' AND "schools"."XCL_045" = 'Fresno'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"schools\".\"XCL_061\") = '1980' AND \"schools\".\"XCL_045\" = 'Fresno'",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_036\") FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE STRFTIME('%Y', T2.\"XCL_061\") = '1980' AND T2.\"XCL_045\" = 'Fresno'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:39"
  ]
}
```

### Computed metric representing the ratio of frpm.XCL_020 to frpm.XCL_019, scaled by 100. Returns a single value per row in the joined result set for sch

```json
{
  "kind": "binding",
  "formula": "\"frpm\".\"XCL_020\" * 100 / \"frpm\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_020\" * 100 / T1.\"XCL_019\", T1.\"XCL_004\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_080\" = 'Alusine'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_020\" * 100 / \"r0\".\"XCL_019\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_020\" * 100 / \"r0\".\"XCL_019\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_080\" = 'Alusine'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:85"
  ]
}
```

### School Attribute XCL_084

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_084\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_080\", T2.\"XCL_081\", T2.\"XCL_083\", T2.\"XCL_084\", T2.\"XCL_086\", T2.\"XCL_087\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_040\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:36"
  ]
}
```

### STRFTIME('%Y', "schools"."XCL_062") = '1989' AND "schools"."XCL_050" = 'San Francisco' AND "schools"."XCL_067" = 'Community College District'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"schools\".\"XCL_062\") = '1989' AND \"schools\".\"XCL_050\" = 'San Francisco' AND \"schools\".\"XCL_067\" = 'Community College District'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_047\") FROM schools WHERE STRFTIME('%Y', \"XCL_062\") = '1989' AND \"XCL_050\" = 'San Francisco' AND \"XCL_067\" = 'Community College District'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:67"
  ]
}
```

### School Attribute XCL_086

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_086\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_080\", T2.\"XCL_081\", T2.\"XCL_083\", T2.\"XCL_084\", T2.\"XCL_086\", T2.\"XCL_087\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_040\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:36"
  ]
}
```

### School Count

```json
{
  "kind": "metric",
  "formula": "COUNT(*)",
  "grain": [],
  "population_scope": "SELECT COUNT(*) FROM schools WHERE \"XCL_064\" = '00D4' AND \"XCL_055\" = 'Hickman'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(*)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT COUNT(*) AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_064\" = '00D4' AND \"r0\".\"XCL_055\" = 'Hickman'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:64"
  ]
}
```

### "frpm"."XCL_019" - "frpm"."XCL_024" > 30

```json
{
  "kind": "predicate",
  "formula": "\"frpm\".\"XCL_019\" - \"frpm\".\"XCL_024\" > 30",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_047\", T1.\"XCL_048\" FROM schools AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_041\" = T2.\"XCL_001\" WHERE T2.\"XCL_019\" - T2.\"XCL_024\" > 30",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:23"
  ]
}
```

### CAST("satscores"."XCL_040" AS REAL) / "satscores"."XCL_036" > 0.3

```json
{
  "kind": "predicate",
  "formula": "CAST(\"satscores\".\"XCL_040\" AS REAL) / \"satscores\".\"XCL_036\" > 0.3",
  "grain": [],
  "population_scope": "SELECT MAX(CAST(T1.\"XCL_025\" AS REAL) / T1.\"XCL_024\") FROM frpm AS T1 INNER JOIN satscores AS T2 ON T1.\"XCL_001\" = T2.\"XCL_030\" WHERE CAST(T2.\"XCL_040\" AS REAL) / T2.\"XCL_036\" > 0.3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:12"
  ]
}
```

### "schools"."XCL_080" = 'Ricci' AND "schools"."XCL_081" = 'Ulrich'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_080\" = 'Ricci' AND \"schools\".\"XCL_081\" = 'Ulrich'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\", T1.\"XCL_039\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_080\" = 'Ricci' AND T2.\"XCL_081\" = 'Ulrich'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:45"
  ]
}
```

### Value of column XCL_052 from the schools table, representing a specific attribute of the school record for the filtered population.

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_052\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_008\", T2.\"XCL_048\", T2.\"XCL_050\", T2.\"XCL_052\", T2.\"XCL_051\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Monterey' AND T1.\"XCL_025\" > 800 AND T1.\"XCL_010\" = 'High Schools (Public)'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_052\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_052\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_045\" = 'Monterey' AND \"r0\".\"XCL_025\" > 800 AND \"r0\".\"XCL_010\" = 'High Schools (Public)'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:26"
  ]
}
```

### School Attribute XCL_061

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_061\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_061\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_019\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:29"
  ]
}
```

### CAST("frpm"."XCL_020" AS REAL) / "frpm"."XCL_019" > 0.1 AND "satscores"."XCL_040" > 0

```json
{
  "kind": "predicate",
  "formula": "CAST(\"frpm\".\"XCL_020\" AS REAL) / \"frpm\".\"XCL_019\" > 0.1 AND \"satscores\".\"XCL_040\" > 0",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_008\" FROM satscores AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_030\" = T2.\"XCL_001\" WHERE CAST(T2.\"XCL_020\" AS REAL) / T2.\"XCL_019\" > 0.1 AND T1.\"XCL_040\" > 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:24"
  ]
}
```

### Returns the value of column XCL_027 from the frpm table for the single school record associated with the highest value in satscores.XCL_037. The grain

```json
{
  "kind": "binding",
  "formula": "\"frpm\".\"XCL_027\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_027\" FROM satscores AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_030\" = T2.\"XCL_001\" ORDER BY T1.\"XCL_037\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:10"
  ]
}
```

### "schools"."XCL_076" = 'F'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_076\" = 'F'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\", T1.\"XCL_037\", RANK() OVER (PARTITION BY T2.\"XCL_045\" ORDER BY T1.\"XCL_037\" DESC) AS rnk FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_076\" = 'F'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:41"
  ]
}
```

### School Identifier

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_058\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_058\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_046\" = 'Fresno Unified' AND NOT T1.\"XCL_037\" IS NULL ORDER BY T1.\"XCL_037\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:40"
  ]
}
```

### Average FRPM Difference for Locally Funded Schools

```json
{
  "kind": "metric",
  "formula": "AVG(\"frpm\".\"XCL_019\" - \"frpm\".\"XCL_024\")",
  "grain": [],
  "population_scope": "SELECT AVG(T3.\"XCL_019\" - T3.\"XCL_024\") FROM frpm AS T3 INNER JOIN schools AS T4 ON T3.\"XCL_001\" = T4.\"XCL_041\" WHERE T4.\"XCL_065\" = 'Locally funded'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_019\" - \"r0\".\"XCL_024\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_019\" - \"r0\".\"XCL_024\") AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_065\" = 'Locally funded'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:28"
  ]
}
```

### School Attribute XCL_058

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_058\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_058\", T2.\"XCL_059\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_039\" DESC LIMIT 1 OFFSET 332",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:57"
  ]
}
```

### The value of column XCL_032 from the satscores table for the single row where XCL_034 is 'Contra Costa', XCL_032 is not null, and XCL_036 is the maxim

```json
{
  "kind": "binding",
  "formula": "\"satscores\".\"XCL_032\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_032\" FROM satscores WHERE \"XCL_034\" = 'Contra Costa' AND NOT \"XCL_032\" IS NULL ORDER BY \"XCL_036\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:22"
  ]
}
```

### School Attribute XCL_073

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_073\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_073\", T2.\"XCL_047\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_012\" = 'Breakfast Provision 2' AND T1.\"XCL_003\" = 37",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_073\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_073\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r0\".\"XCL_012\" = 'Breakfast Provision 2' AND \"r0\".\"XCL_003\" = 37",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:75"
  ]
}
```

### Value of column XCL_048 from the schools table, representing a specific attribute of the school record for the filtered population.

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_048\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_008\", T2.\"XCL_048\", T2.\"XCL_050\", T2.\"XCL_052\", T2.\"XCL_051\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Monterey' AND T1.\"XCL_025\" > 800 AND T1.\"XCL_010\" = 'High Schools (Public)'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_048\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_048\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_045\" = 'Monterey' AND \"r0\".\"XCL_025\" > 800 AND \"r0\".\"XCL_010\" = 'High Schools (Public)'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:26"
  ]
}
```

### "schools"."XCL_070" = 'SSS' AND "schools"."XCL_050" = 'Fremont' AND "frpm"."XCL_002" BETWEEN 2014 AND 2015

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_070\" = 'SSS' AND \"schools\".\"XCL_050\" = 'Fremont' AND \"frpm\".\"XCL_002\" BETWEEN 2014 AND 2015",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_024\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_070\" = 'SSS' AND T2.\"XCL_050\" = 'Fremont' AND T1.\"XCL_002\" BETWEEN 2014 AND 2015",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:72"
  ]
}
```

### "frpm"."XCL_025" BETWEEN 1900 AND 2000 AND NOT "schools"."XCL_060" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"frpm\".\"XCL_025\" BETWEEN 1900 AND 2000 AND NOT \"schools\".\"XCL_060\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_060\", T1.\"XCL_008\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_025\" BETWEEN 1900 AND 2000 AND NOT T2.\"XCL_060\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:33"
  ]
}
```

### Value of column XCL_008 from the frpm table (T2), returned for rows where the frpm record is joined to a satscores record and meets the specified rati

```json
{
  "kind": "binding",
  "formula": "\"frpm\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_008\" FROM satscores AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_030\" = T2.\"XCL_001\" WHERE CAST(T2.\"XCL_020\" AS REAL) / T2.\"XCL_019\" > 0.1 AND T1.\"XCL_040\" > 0",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "satscores"
      },
      {
        "role": "r1",
        "physical_table": "frpm"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_008\" AS \"value\" FROM satscores AS \"r0\" INNER JOIN frpm AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_001\" WHERE CAST(\"r1\".\"XCL_020\" AS REAL) / \"r1\".\"XCL_019\" > 0.1 AND \"r0\".\"XCL_040\" > 0",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:24"
  ]
}
```

### School Attribute XCL_047

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_080\", \"XCL_081\", \"XCL_047\", \"XCL_050\" FROM schools WHERE \"XCL_063\" = 1 AND \"XCL_064\" = '00D2'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_047\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_047\" AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_063\" = 1 AND \"r0\".\"XCL_064\" = '00D2'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:63"
  ]
}
```

### School Attribute XCL_047

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_081\", \"XCL_046\", \"XCL_045\", \"XCL_047\" FROM schools WHERE \"XCL_064\" = '0040'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_047\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_047\" AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_064\" = '0040'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:86"
  ]
}
```

### A specific attribute from the frpm table (XCL_015), representing a dimension of the Free and Reduced Price Meal data. It is part of the grouping grain

```json
{
  "kind": "binding",
  "formula": "\"frpm\".\"XCL_015\"",
  "grain": [
    "\"satscores\".\"XCL_032\"",
    "\"frpm\".\"XCL_015\""
  ],
  "population_scope": "SELECT T1.\"XCL_032\", T2.\"XCL_015\" FROM satscores AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_030\" = T2.\"XCL_001\" WHERE T2.\"XCL_007\" LIKE 'Riverside%' GROUP BY T1.\"XCL_032\", T2.\"XCL_015\" HAVING CAST(SUM(T1.\"XCL_038\") AS REAL) / COUNT(T1.\"XCL_030\") > 400",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_015\"",
    "grain": [
      "\"r0\".\"XCL_032\"",
      "\"r1\".\"XCL_015\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "satscores"
      },
      {
        "role": "r1",
        "physical_table": "frpm"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_032\" AS \"grain_0\", \"r1\".\"XCL_015\" AS \"grain_1\", \"r1\".\"XCL_015\" AS \"value\" FROM satscores AS \"r0\" INNER JOIN frpm AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_001\" WHERE \"r1\".\"XCL_007\" LIKE 'Riverside%' GROUP BY \"r0\".\"XCL_032\", \"r1\".\"XCL_015\" HAVING CAST(SUM(\"r0\".\"XCL_038\") AS REAL) / COUNT(\"r0\".\"XCL_030\") > 400",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:25"
  ]
}
```

### "schools"."XCL_044" = 'Closed'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_044\" = 'Closed'",
  "grain": [
    "\"schools\".\"XCL_045\""
  ],
  "population_scope": "SELECT \"XCL_045\" FROM schools WHERE \"XCL_044\" = 'Closed' GROUP BY \"XCL_045\" ORDER BY COUNT(\"XCL_047\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:49"
  ]
}
```

### Value of column XCL_078 from the schools table, used as the descending sort key to identify the top record.

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_078\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_010\", T1.\"XCL_008\", T2.\"XCL_078\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" ORDER BY T2.\"XCL_078\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:80"
  ]
}
```

### School Attribute XCL_048

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_048\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_047\", T1.\"XCL_048\" FROM schools AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_041\" = T2.\"XCL_001\" WHERE T2.\"XCL_019\" - T2.\"XCL_024\" > 30",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_048\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      },
      {
        "role": "r1",
        "physical_table": "frpm"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_048\" AS \"value\" FROM schools AS \"r0\" INNER JOIN frpm AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_001\" WHERE \"r1\".\"XCL_019\" - \"r1\".\"XCL_024\" > 30",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:23"
  ]
}
```

### Value of column XCL_050 from the schools table, representing a specific attribute of the school record for the filtered population.

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_050\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_008\", T2.\"XCL_048\", T2.\"XCL_050\", T2.\"XCL_052\", T2.\"XCL_051\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Monterey' AND T1.\"XCL_025\" > 800 AND T1.\"XCL_010\" = 'High Schools (Public)'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_050\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_050\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_045\" = 'Monterey' AND \"r0\".\"XCL_025\" > 800 AND \"r0\".\"XCL_010\" = 'High Schools (Public)'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:26"
  ]
}
```

### School Identifier XCL_047

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\", T2.\"XCL_066\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_065\" = 'Locally funded' AND (T1.\"XCL_019\" - T1.\"XCL_024\") > (SELECT AVG(T3.\"XCL_019\" - T3.\"XCL_024\") FROM frpm AS T3 INNER JOIN schools AS T4 ON T3.\"XCL_001\" = T4.\"XCL_041\" WHERE T4.\"XCL_065\" = 'Locally funded')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:28"
  ]
}
```

### Returns the value of column XCL_043 from the schools table for the top 5 records, ranked in descending order by the value of column XCL_024 in the joi

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_043\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_043\" FROM schools AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_041\" = T2.\"XCL_001\" ORDER BY T2.\"XCL_024\" DESC LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:14"
  ]
}
```

### A specific attribute from the satscores table (XCL_032), representing a dimension of the test score data. It is part of the grouping grain and serves 

```json
{
  "kind": "binding",
  "formula": "\"satscores\".\"XCL_032\"",
  "grain": [
    "\"satscores\".\"XCL_032\"",
    "\"frpm\".\"XCL_015\""
  ],
  "population_scope": "SELECT T1.\"XCL_032\", T2.\"XCL_015\" FROM satscores AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_030\" = T2.\"XCL_001\" WHERE T2.\"XCL_007\" LIKE 'Riverside%' GROUP BY T1.\"XCL_032\", T2.\"XCL_015\" HAVING CAST(SUM(T1.\"XCL_038\") AS REAL) / COUNT(T1.\"XCL_030\") > 400",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_032\"",
    "grain": [
      "\"r0\".\"XCL_032\"",
      "\"r1\".\"XCL_015\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "satscores"
      },
      {
        "role": "r1",
        "physical_table": "frpm"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_032\" AS \"grain_0\", \"r1\".\"XCL_015\" AS \"grain_1\", \"r0\".\"XCL_032\" AS \"value\" FROM satscores AS \"r0\" INNER JOIN frpm AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_001\" WHERE \"r1\".\"XCL_007\" LIKE 'Riverside%' GROUP BY \"r0\".\"XCL_032\", \"r1\".\"XCL_015\" HAVING CAST(SUM(\"r0\".\"XCL_038\") AS REAL) / COUNT(\"r0\".\"XCL_030\") > 400",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:25"
  ]
}
```

### School Identifier

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_058\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_058\" FROM schools AS T1 INNER JOIN satscores AS T2 ON T1.\"XCL_041\" = T2.\"XCL_030\" ORDER BY CAST(T2.\"XCL_040\" AS REAL) / T2.\"XCL_036\" DESC LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:13"
  ]
}
```

### SAT Score

```json
{
  "kind": "binding",
  "formula": "\"satscores\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_036\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_055\" = 'Fresno'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "satscores"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_036\" AS \"value\" FROM satscores AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_055\" = 'Fresno'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:53"
  ]
}
```

### School Identifier (XCL_047)

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_066\" = 31 ORDER BY T1.\"XCL_019\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:46"
  ]
}
```

### Returns the value of column XCL_085 from the schools table for records matching the specified filters. Grain is one row per matching school record.

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_085\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_082\", T2.\"XCL_085\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'San Bernardino' AND T2.\"XCL_050\" = 'San Bernardino' AND T2.\"XCL_066\" = 54 AND STRFTIME('%Y', T2.\"XCL_061\") BETWEEN '2009' AND '2010' AND T2.\"XCL_068\" = 62",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_085\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_085\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_045\" = 'San Bernardino' AND \"r1\".\"XCL_050\" = 'San Bernardino' AND \"r1\".\"XCL_066\" = 54 AND STRFTIME('%Y', \"r1\".\"XCL_061\") BETWEEN '2009' AND '2010' AND \"r1\".\"XCL_068\" = 62",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:87"
  ]
}
```

### The value of column XCL_001 from the frpm table for the single row with the highest value in column XCL_022. This acts as a lookup key to identify a s

```json
{
  "kind": "binding",
  "formula": "\"frpm\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM frpm ORDER BY \"XCL_022\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:8"
  ]
}
```

### "frpm"."XCL_007" LIKE 'Riverside%'

```json
{
  "kind": "predicate",
  "formula": "\"frpm\".\"XCL_007\" LIKE 'Riverside%'",
  "grain": [
    "\"satscores\".\"XCL_032\"",
    "\"frpm\".\"XCL_015\""
  ],
  "population_scope": "SELECT T1.\"XCL_032\", T2.\"XCL_015\" FROM satscores AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_030\" = T2.\"XCL_001\" WHERE T2.\"XCL_007\" LIKE 'Riverside%' GROUP BY T1.\"XCL_032\", T2.\"XCL_015\" HAVING CAST(SUM(T1.\"XCL_038\") AS REAL) / COUNT(T1.\"XCL_030\") > 400",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:25"
  ]
}
```

### Value of column XCL_008 from the frpm table, representing a specific attribute of the Free and Reduced Price Meal record for the filtered population.

```json
{
  "kind": "binding",
  "formula": "\"frpm\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_008\", T2.\"XCL_048\", T2.\"XCL_050\", T2.\"XCL_052\", T2.\"XCL_051\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Monterey' AND T1.\"XCL_025\" > 800 AND T1.\"XCL_010\" = 'High Schools (Public)'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_008\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_045\" = 'Monterey' AND \"r0\".\"XCL_025\" > 800 AND \"r0\".\"XCL_010\" = 'High Schools (Public)'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:26"
  ]
}
```

### School Attribute XCL_047

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_047\", T1.\"XCL_048\" FROM schools AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_041\" = T2.\"XCL_001\" WHERE T2.\"XCL_019\" - T2.\"XCL_024\" > 30",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_047\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      },
      {
        "role": "r1",
        "physical_table": "frpm"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_047\" AS \"value\" FROM schools AS \"r0\" INNER JOIN frpm AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_001\" WHERE \"r1\".\"XCL_019\" - \"r1\".\"XCL_024\" > 30",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:23"
  ]
}
```

### NOT "satscores"."XCL_037" IS NULL

```json
{
  "kind": "predicate",
  "formula": "NOT \"satscores\".\"XCL_037\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_053\", T2.\"XCL_047\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE NOT T1.\"XCL_037\" IS NULL ORDER BY T1.\"XCL_037\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:51"
  ]
}
```

### Most Frequent XCL_075 Value

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_075\"",
  "grain": [
    "\"schools\".\"XCL_075\""
  ],
  "population_scope": "SELECT \"XCL_075\" FROM schools WHERE \"XCL_050\" = 'Adelanto' GROUP BY \"XCL_075\" ORDER BY COUNT(\"XCL_075\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:78"
  ]
}
```

### Attribute from the frpm table (T1) for the single record selected. Represents a specific data point from the Free and Reduced Price Meal program recor

```json
{
  "kind": "binding",
  "formula": "\"frpm\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_050\", T1.\"XCL_017\", T1.\"XCL_008\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_052\" = 'CA' ORDER BY T2.\"XCL_078\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:81"
  ]
}
```

### Average count of XCL_047 per year

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(\"schools\".\"XCL_047\") AS REAL) / 12",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(\"XCL_047\") AS REAL) / 12 FROM schools WHERE \"XCL_066\" = 52 AND \"XCL_045\" = 'Alameda' AND STRFTIME('%Y', \"XCL_061\") = '1980'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(\"r0\".\"XCL_047\") AS REAL) / 12",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(\"r0\".\"XCL_047\") AS REAL) / 12 AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_066\" = 52 AND \"r0\".\"XCL_045\" = 'Alameda' AND STRFTIME('%Y', \"r0\".\"XCL_061\") = '1980'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:47"
  ]
}
```

### School Attribute XCL_083

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_083\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_080\", T2.\"XCL_081\", T2.\"XCL_083\", T2.\"XCL_084\", T2.\"XCL_086\", T2.\"XCL_087\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_040\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:36"
  ]
}
```

### "schools"."XCL_053" = 'PO Box 1040' AND "schools"."XCL_069" = 'Youth Authority Facilities'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_053\" = 'PO Box 1040' AND \"schools\".\"XCL_069\" = 'Youth Authority Facilities'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_027\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_053\" = 'PO Box 1040' AND T2.\"XCL_069\" = 'Youth Authority Facilities'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:73"
  ]
}
```

### SAT Score

```json
{
  "kind": "binding",
  "formula": "\"satscores\".\"XCL_037\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\", T1.\"XCL_037\", RANK() OVER (PARTITION BY T2.\"XCL_045\" ORDER BY T1.\"XCL_037\" DESC) AS rnk FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_076\" = 'F'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_037\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "satscores"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_037\" AS \"value\" FROM satscores AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_076\" = 'F'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:41"
  ]
}
```

### School Attribute XCL_080

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_080\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_080\", T2.\"XCL_081\", T2.\"XCL_083\", T2.\"XCL_084\", T2.\"XCL_086\", T2.\"XCL_087\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_040\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:36"
  ]
}
```

### SAT Score Component 1

```json
{
  "kind": "binding",
  "formula": "\"satscores\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_038\", T2.\"XCL_045\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE NOT T1.\"XCL_038\" IS NULL ORDER BY T1.\"XCL_038\" + T1.\"XCL_037\" + T1.\"XCL_039\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:43"
  ]
}
```

### Identifier from the schools table (T2) for the single record selected. Represents the specific school associated with the FRPM record.

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_050\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_050\", T1.\"XCL_017\", T1.\"XCL_008\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_052\" = 'CA' ORDER BY T2.\"XCL_078\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:81"
  ]
}
```

### School District

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_045\"",
  "grain": [
    "\"schools\".\"XCL_045\""
  ],
  "population_scope": "SELECT \"XCL_045\", COUNT(\"XCL_076\") FROM schools WHERE (\"XCL_045\" = 'San Diego' OR \"XCL_045\" = 'Santa Barbara') AND \"XCL_076\" = 'F' GROUP BY \"XCL_045\" ORDER BY COUNT(\"XCL_076\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:79"
  ]
}
```

### "schools"."XCL_077" = 1 AND "satscores"."XCL_036" > 500

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_077\" = 1 AND \"satscores\".\"XCL_036\" > 500",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_077\" = 1 AND T1.\"XCL_036\" > 500",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:6"
  ]
}
```

### Aggregates the total number of school records (identified by XCL_047) that satisfy the specified temporal, geographic, and funding criteria. The grain

```json
{
  "kind": "metric",
  "formula": "COUNT(\"schools\".\"XCL_047\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_047\") FROM schools WHERE STRFTIME('%Y', \"XCL_061\") BETWEEN '2000' AND '2005' AND \"XCL_045\" = 'Stanislaus' AND \"XCL_065\" = 'Directly funded'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_047\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_047\") AS \"value\" FROM schools AS \"r0\" WHERE STRFTIME('%Y', \"r0\".\"XCL_061\") BETWEEN '2000' AND '2005' AND \"r0\".\"XCL_045\" = 'Stanislaus' AND \"r0\".\"XCL_065\" = 'Directly funded'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:66"
  ]
}
```

### "schools"."XCL_050" = 'San Joaquin' AND "schools"."XCL_057" = 'CA' AND "schools"."XCL_044" = 'Active'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_050\" = 'San Joaquin' AND \"schools\".\"XCL_057\" = 'CA' AND \"schools\".\"XCL_044\" = 'Active'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_041\") FROM schools WHERE \"XCL_050\" = 'San Joaquin' AND \"XCL_057\" = 'CA' AND \"XCL_044\" = 'Active'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:56"
  ]
}
```

### Value of column XCL_010 from the frpm table for the single record with the highest schools.XCL_078 value.

```json
{
  "kind": "binding",
  "formula": "\"frpm\".\"XCL_010\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_010\", T1.\"XCL_008\", T2.\"XCL_078\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" ORDER BY T2.\"XCL_078\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:80"
  ]
}
```

### "schools"."XCL_051" = '95203-3704'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_051\" = '95203-3704'",
  "grain": [],
  "population_scope": "SELECT \"XCL_058\", \"XCL_059\", \"XCL_047\" FROM schools WHERE \"XCL_051\" = '95203-3704'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:58"
  ]
}
```

### "frpm"."XCL_006" = 'Alameda'

```json
{
  "kind": "predicate",
  "formula": "\"frpm\".\"XCL_006\" = 'Alameda'",
  "grain": [],
  "population_scope": "SELECT \"XCL_020\" / \"XCL_019\" FROM frpm WHERE \"XCL_006\" = 'Alameda' ORDER BY (CAST(\"XCL_020\" AS REAL) / \"XCL_019\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:0"
  ]
}
```

### "schools"."XCL_063" = 1 AND "schools"."XCL_064" = '00D2'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_063\" = 1 AND \"schools\".\"XCL_064\" = '00D2'",
  "grain": [],
  "population_scope": "SELECT \"XCL_080\", \"XCL_081\", \"XCL_047\", \"XCL_050\" FROM schools WHERE \"XCL_063\" = 1 AND \"XCL_064\" = '00D2'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:63"
  ]
}
```

### Identifier for the school record from the 'schools' table (T2). In the context of the full query, this represents the identifier of schools that are a

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\", T1.\"XCL_037\", RANK() OVER (PARTITION BY T2.\"XCL_045\" ORDER BY T1.\"XCL_037\" DESC) AS rnk FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_076\" = 'F'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_047\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "satscores"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_047\" AS \"value\" FROM satscores AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_076\" = 'F'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:41"
  ]
}
```

### "schools"."XCL_044" = 'Active'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_044\" = 'Active'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_046\" FROM schools AS T1 INNER JOIN satscores AS T2 ON T1.\"XCL_041\" = T2.\"XCL_030\" WHERE T1.\"XCL_044\" = 'Active' ORDER BY T2.\"XCL_037\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:15"
  ]
}
```

### Returns the value of column XCL_051 from the schools table. The population is restricted to schools linked via XCL_041 to FRPM records where XCL_007 i

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_051\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_051\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_007\" = 'Fresno County Office of Education' AND T1.\"XCL_013\" = 1",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_051\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_051\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r0\".\"XCL_007\" = 'Fresno County Office of Education' AND \"r0\".\"XCL_013\" = 1",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:2"
  ]
}
```

### "schools"."XCL_076" = 'F' AND "satscores"."XCL_038" > 400

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_076\" = 'F' AND \"satscores\".\"XCL_038\" > 400",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T2.\"XCL_047\") FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_076\" = 'F' AND T1.\"XCL_038\" > 400",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:5"
  ]
}
```

### STRFTIME('%Y', "schools"."XCL_062") BETWEEN '1980' AND '1989' AND "schools"."XCL_044" = 'Closed' AND "schools"."XCL_068" = 11

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"schools\".\"XCL_062\") BETWEEN '1980' AND '1989' AND \"schools\".\"XCL_044\" = 'Closed' AND \"schools\".\"XCL_068\" = 11",
  "grain": [
    "\"schools\".\"XCL_045\""
  ],
  "population_scope": "SELECT \"XCL_045\" FROM schools WHERE STRFTIME('%Y', \"XCL_062\") BETWEEN '1980' AND '1989' AND \"XCL_044\" = 'Closed' AND \"XCL_068\" = 11 GROUP BY \"XCL_045\" ORDER BY COUNT(\"XCL_047\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:68"
  ]
}
```

### The value of column XCL_024 from the frpm table for records joined to schools in Fremont with school type SSS, filtered to academic years 2014 and 201

```json
{
  "kind": "binding",
  "formula": "\"frpm\".\"XCL_024\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_024\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_070\" = 'SSS' AND T2.\"XCL_050\" = 'Fremont' AND T1.\"XCL_002\" BETWEEN 2014 AND 2015",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_024\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_024\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_070\" = 'SSS' AND \"r1\".\"XCL_050\" = 'Fremont' AND \"r0\".\"XCL_002\" BETWEEN 2014 AND 2015",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:72"
  ]
}
```

### School Attribute XCL_047

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_045\", \"XCL_047\", \"XCL_062\" FROM schools WHERE \"XCL_045\" = (SELECT \"XCL_045\" FROM schools WHERE \"XCL_044\" = 'Closed' GROUP BY \"XCL_045\" ORDER BY COUNT(\"XCL_047\") DESC LIMIT 1) AND \"XCL_044\" = 'Closed' AND NOT \"XCL_047\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:49"
  ]
}
```

### The XCL_045 identifier of the school with the highest count of non-null XCL_047 records among schools with status 'Closed'. This subquery acts as a fi

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_045\"",
  "grain": [
    "\"schools\".\"XCL_045\""
  ],
  "population_scope": "SELECT \"XCL_045\" FROM schools WHERE \"XCL_044\" = 'Closed' GROUP BY \"XCL_045\" ORDER BY COUNT(\"XCL_047\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:49"
  ]
}
```

### ("schools"."XCL_045" = 'San Diego' OR "schools"."XCL_045" = 'Santa Barbara') AND "schools"."XCL_076" = 'F'

```json
{
  "kind": "predicate",
  "formula": "(\"schools\".\"XCL_045\" = 'San Diego' OR \"schools\".\"XCL_045\" = 'Santa Barbara') AND \"schools\".\"XCL_076\" = 'F'",
  "grain": [
    "\"schools\".\"XCL_045\""
  ],
  "population_scope": "SELECT \"XCL_045\", COUNT(\"XCL_076\") FROM schools WHERE (\"XCL_045\" = 'San Diego' OR \"XCL_045\" = 'Santa Barbara') AND \"XCL_076\" = 'F' GROUP BY \"XCL_045\" ORDER BY COUNT(\"XCL_076\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:79"
  ]
}
```

### "schools"."XCL_045" = 'Amador' AND "frpm"."XCL_017" = 9 AND "frpm"."XCL_018" = 12

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_045\" = 'Amador' AND \"frpm\".\"XCL_017\" = 9 AND \"frpm\".\"XCL_018\" = 12",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_008\") FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Amador' AND T1.\"XCL_017\" = 9 AND T1.\"XCL_018\" = 12",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:20"
  ]
}
```

### Aggregates the count of school records (identified by XCL_001) from the frpm table that are directly funded, located in Fresno, and have a correspondi

```json
{
  "kind": "metric",
  "formula": "COUNT(\"frpm\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM frpm AS T1 INNER JOIN satscores AS T2 ON T1.\"XCL_001\" = T2.\"XCL_030\" WHERE T1.\"XCL_015\" = 'Directly funded' AND T1.\"XCL_006\" = 'Fresno' AND T2.\"XCL_036\" <= 250",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "satscores"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM frpm AS \"r0\" INNER JOIN satscores AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_030\" WHERE \"r0\".\"XCL_015\" = 'Directly funded' AND \"r0\".\"XCL_006\" = 'Fresno' AND \"r1\".\"XCL_036\" <= 250",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:18"
  ]
}
```

### School Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"schools\".\"XCL_047\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_047\") FROM schools WHERE (\"XCL_044\" = 'Closed' OR \"XCL_044\" = 'Active') AND \"XCL_068\" = 69 AND \"XCL_045\" = 'Alpine'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_047\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_047\") AS \"value\" FROM schools AS \"r0\" WHERE (\"r0\".\"XCL_044\" = 'Closed' OR \"r0\".\"XCL_044\" = 'Active') AND \"r0\".\"XCL_068\" = 69 AND \"r0\".\"XCL_045\" = 'Alpine'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:70"
  ]
}
```

### "schools"."XCL_055" = 'Fresno'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_055\" = 'Fresno'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_036\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_055\" = 'Fresno'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:53"
  ]
}
```

### The two most frequent values of the XCL_080 column in the schools table, determined by grouping on XCL_080 and ordering by the count of occurrences in

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_080\"",
  "grain": [
    "\"schools\".\"XCL_080\""
  ],
  "population_scope": "SELECT \"XCL_080\" FROM schools GROUP BY \"XCL_080\" ORDER BY COUNT(\"XCL_080\") DESC LIMIT 2",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:84"
  ]
}
```

### The final output column, representing the school identifier (XCL_047) for records where the calculated rank is 5 or less. This filters the dataset to 

```json
{
  "kind": "binding",
  "formula": "\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_047\" FROM (SELECT T2.\"XCL_047\", T1.\"XCL_037\", RANK() OVER (PARTITION BY T2.\"XCL_045\" ORDER BY T1.\"XCL_037\" DESC) AS rnk FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_076\" = 'F') AS ranked_schools WHERE \"rnk\" <= 5",
  "upstream_scopes": [
    "SELECT T2.\"XCL_047\", T1.\"XCL_037\", RANK() OVER (PARTITION BY T2.\"XCL_045\" ORDER BY T1.\"XCL_037\" DESC) AS rnk FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_076\" = 'F'"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:41"
  ]
}
```

### "schools"."XCL_077" = 1 AND "schools"."XCL_074" = 'K-8' AND "frpm"."XCL_012" = 'Multiple Provision Types'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_077\" = 1 AND \"schools\".\"XCL_074\" = 'K-8' AND \"frpm\".\"XCL_012\" = 'Multiple Provision Types'",
  "grain": [
    "\"schools\".\"XCL_050\""
  ],
  "population_scope": "SELECT T2.\"XCL_050\", COUNT(T2.\"XCL_041\") FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_077\" = 1 AND T2.\"XCL_074\" = 'K-8' AND T1.\"XCL_012\" = 'Multiple Provision Types' GROUP BY T2.\"XCL_050\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:83"
  ]
}
```

### School Identifier

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_045\"",
  "grain": [
    "\"schools\".\"XCL_045\""
  ],
  "population_scope": "SELECT \"XCL_045\" FROM schools WHERE STRFTIME('%Y', \"XCL_062\") BETWEEN '1980' AND '1989' AND \"XCL_044\" = 'Closed' AND \"XCL_068\" = 11 GROUP BY \"XCL_045\" ORDER BY COUNT(\"XCL_047\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:68"
  ]
}
```

### "schools"."XCL_044" = 'Merged' AND "satscores"."XCL_036" < 100 AND "schools"."XCL_045" = 'Lake'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_044\" = 'Merged' AND \"satscores\".\"XCL_036\" < 100 AND \"schools\".\"XCL_045\" = 'Lake'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_041\") FROM schools AS T1 INNER JOIN satscores AS T2 ON T1.\"XCL_041\" = T2.\"XCL_030\" WHERE T1.\"XCL_044\" = 'Merged' AND T2.\"XCL_036\" < 100 AND T1.\"XCL_045\" = 'Lake'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:16"
  ]
}
```

### "schools"."XCL_068" = 66

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_068\" = 66",
  "grain": [],
  "population_scope": "SELECT CAST(T1.\"XCL_022\" AS REAL) / T1.\"XCL_019\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_068\" = 66 ORDER BY T1.\"XCL_022\" DESC LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:32"
  ]
}
```

### Returns the value of column XCL_082 from the schools table for records matching the specified filters. Grain is one row per matching school record.

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_082\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_082\", T2.\"XCL_085\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'San Bernardino' AND T2.\"XCL_050\" = 'San Bernardino' AND T2.\"XCL_066\" = 54 AND STRFTIME('%Y', T2.\"XCL_061\") BETWEEN '2009' AND '2010' AND T2.\"XCL_068\" = 62",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_082\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_082\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_045\" = 'San Bernardino' AND \"r1\".\"XCL_050\" = 'San Bernardino' AND \"r1\".\"XCL_066\" = 54 AND STRFTIME('%Y', \"r1\".\"XCL_061\") BETWEEN '2009' AND '2010' AND \"r1\".\"XCL_068\" = 62",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:87"
  ]
}
```

### "schools"."XCL_045" = 'San Joaquin' AND "schools"."XCL_076" = 'P' AND "schools"."XCL_063" = 1

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_045\" = 'San Joaquin' AND \"schools\".\"XCL_076\" = 'P' AND \"schools\".\"XCL_063\" = 1",
  "grain": [],
  "population_scope": "SELECT \"XCL_060\" FROM schools WHERE \"XCL_045\" = 'San Joaquin' AND \"XCL_076\" = 'P' AND \"XCL_063\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:60"
  ]
}
```

### School Attribute XCL_066

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_066\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\", T2.\"XCL_066\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_065\" = 'Locally funded' AND (T1.\"XCL_019\" - T1.\"XCL_024\") > (SELECT AVG(T3.\"XCL_019\" - T3.\"XCL_024\") FROM frpm AS T3 INNER JOIN schools AS T4 ON T3.\"XCL_001\" = T4.\"XCL_041\" WHERE T4.\"XCL_065\" = 'Locally funded')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:28"
  ]
}
```

### The value of the 'XCL_058' column from the 'schools' table for the single school with the highest 'XCL_038' score in the 'satscores' table. Grain: sin

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_058\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_058\" FROM schools AS T1 INNER JOIN satscores AS T2 ON T1.\"XCL_041\" = T2.\"XCL_030\" ORDER BY T2.\"XCL_038\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:19"
  ]
}
```

### School Identifier (XCL_082)

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_082\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_082\", T2.\"XCL_047\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_040\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:88"
  ]
}
```

### "schools"."XCL_055" = 'Lakeport' AND ("satscores"."XCL_037" + "satscores"."XCL_038" + "satscores"."XCL_039") >= 1500

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_055\" = 'Lakeport' AND (\"satscores\".\"XCL_037\" + \"satscores\".\"XCL_038\" + \"satscores\".\"XCL_039\") >= 1500",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_030\") FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_055\" = 'Lakeport' AND (T1.\"XCL_037\" + T1.\"XCL_038\" + T1.\"XCL_039\") >= 1500",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:52"
  ]
}
```

### School Identifier

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_077\" = 1 AND T1.\"XCL_036\" > 500",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_047\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "satscores"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_047\" AS \"value\" FROM satscores AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_077\" = 1 AND \"r0\".\"XCL_036\" > 500",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:6"
  ]
}
```

### School Attribute XCL_053

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_053\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_053\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_022\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:3"
  ]
}
```

### A window function metric that assigns a rank to each row based on the descending order of the SAT score (XCL_037), partitioned by the school group ide

```json
{
  "kind": "metric",
  "formula": "RANK() OVER (PARTITION BY \"schools\".\"XCL_045\" ORDER BY \"satscores\".\"XCL_037\" DESC)",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\", T1.\"XCL_037\", RANK() OVER (PARTITION BY T2.\"XCL_045\" ORDER BY T1.\"XCL_037\" DESC) AS rnk FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_076\" = 'F'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "RANK() OVER (PARTITION BY \"r1\".\"XCL_045\" ORDER BY \"r0\".\"XCL_037\" DESC)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "satscores"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT RANK() OVER (PARTITION BY \"r1\".\"XCL_045\" ORDER BY \"r0\".\"XCL_037\" DESC) AS \"value\" FROM satscores AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_076\" = 'F'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:41"
  ]
}
```

### School Attribute XCL_087

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_087\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_080\", T2.\"XCL_081\", T2.\"XCL_083\", T2.\"XCL_084\", T2.\"XCL_086\", T2.\"XCL_087\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_040\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:36"
  ]
}
```

### Average SAT Score

```json
{
  "kind": "metric",
  "formula": "AVG(\"satscores\".\"XCL_036\")",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_036\") FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE STRFTIME('%Y', T2.\"XCL_061\") = '1980' AND T2.\"XCL_045\" = 'Fresno'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_036\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "satscores"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_036\") AS \"value\" FROM satscores AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_041\" WHERE STRFTIME('%Y', \"r1\".\"XCL_061\") = '1980' AND \"r1\".\"XCL_045\" = 'Fresno'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:39"
  ]
}
```

### A single scalar metric representing the ratio of the count of schools where XCL_045 is 'Colusa' to the count of schools where XCL_045 is 'Humboldt'. T

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"schools\".\"XCL_045\" = 'Colusa' THEN 1 ELSE 0 END) AS REAL) / SUM(CASE WHEN \"schools\".\"XCL_045\" = 'Humboldt' THEN 1 ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN \"XCL_045\" = 'Colusa' THEN 1 ELSE 0 END) AS REAL) / SUM(CASE WHEN \"XCL_045\" = 'Humboldt' THEN 1 ELSE 0 END) FROM schools WHERE \"XCL_057\" = 'CA'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r0\".\"XCL_045\" = 'Colusa' THEN 1 ELSE 0 END) AS REAL) / SUM(CASE WHEN \"r0\".\"XCL_045\" = 'Humboldt' THEN 1 ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r0\".\"XCL_045\" = 'Colusa' THEN 1 ELSE 0 END) AS REAL) / SUM(CASE WHEN \"r0\".\"XCL_045\" = 'Humboldt' THEN 1 ELSE 0 END) AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_057\" = 'CA'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:55"
  ]
}
```

### Aggregates the count of non-null values in the 'XCL_008' column from the 'frpm' table. The population is restricted to records where the school distri

```json
{
  "kind": "metric",
  "formula": "COUNT(\"frpm\".\"XCL_008\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_008\") FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Amador' AND T1.\"XCL_017\" = 9 AND T1.\"XCL_018\" = 12",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_008\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_008\") AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_045\" = 'Amador' AND \"r0\".\"XCL_017\" = 9 AND \"r0\".\"XCL_018\" = 12",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:20"
  ]
}
```

### Count of FRPM Records

```json
{
  "kind": "metric",
  "formula": "COUNT(\"schools\".\"XCL_041\")",
  "grain": [
    "\"schools\".\"XCL_050\""
  ],
  "population_scope": "SELECT T2.\"XCL_050\", COUNT(T2.\"XCL_041\") FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_077\" = 1 AND T2.\"XCL_074\" = 'K-8' AND T1.\"XCL_012\" = 'Multiple Provision Types' GROUP BY T2.\"XCL_050\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_041\")",
    "grain": [
      "\"r1\".\"XCL_050\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_050\" AS \"grain_0\", COUNT(\"r1\".\"XCL_041\") AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_077\" = 1 AND \"r1\".\"XCL_074\" = 'K-8' AND \"r0\".\"XCL_012\" = 'Multiple Provision Types' GROUP BY \"r1\".\"XCL_050\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:83"
  ]
}
```

### Aggregates the count of school records (identified by XCL_041) that are classified as 'Merged' (XCL_044) and located in 'Lake' (XCL_045), where the as

```json
{
  "kind": "metric",
  "formula": "COUNT(\"schools\".\"XCL_041\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_041\") FROM schools AS T1 INNER JOIN satscores AS T2 ON T1.\"XCL_041\" = T2.\"XCL_030\" WHERE T1.\"XCL_044\" = 'Merged' AND T2.\"XCL_036\" < 100 AND T1.\"XCL_045\" = 'Lake'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_041\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      },
      {
        "role": "r1",
        "physical_table": "satscores"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_041\") AS \"value\" FROM schools AS \"r0\" INNER JOIN satscores AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_030\" WHERE \"r0\".\"XCL_044\" = 'Merged' AND \"r1\".\"XCL_036\" < 100 AND \"r0\".\"XCL_045\" = 'Lake'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:16"
  ]
}
```

### Max FRPM Ratio

```json
{
  "kind": "metric",
  "formula": "MAX(CAST(\"frpm\".\"XCL_025\" AS REAL) / \"frpm\".\"XCL_024\")",
  "grain": [],
  "population_scope": "SELECT MAX(CAST(T1.\"XCL_025\" AS REAL) / T1.\"XCL_024\") FROM frpm AS T1 INNER JOIN satscores AS T2 ON T1.\"XCL_001\" = T2.\"XCL_030\" WHERE CAST(T2.\"XCL_040\" AS REAL) / T2.\"XCL_036\" > 0.3",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MAX(CAST(\"r0\".\"XCL_025\" AS REAL) / \"r0\".\"XCL_024\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "satscores"
      }
    ],
    "scope_sql": "SELECT MAX(CAST(\"r0\".\"XCL_025\" AS REAL) / \"r0\".\"XCL_024\") AS \"value\" FROM frpm AS \"r0\" INNER JOIN satscores AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_030\" WHERE CAST(\"r1\".\"XCL_040\" AS REAL) / \"r1\".\"XCL_036\" > 0.3",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:12"
  ]
}
```

### "satscores"."XCL_038" > 560 AND "frpm"."XCL_015" = 'Directly funded'

```json
{
  "kind": "predicate",
  "formula": "\"satscores\".\"XCL_038\" > 560 AND \"frpm\".\"XCL_015\" = 'Directly funded'",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_005\") FROM satscores AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_030\" = T2.\"XCL_001\" WHERE T1.\"XCL_038\" > 560 AND T2.\"XCL_015\" = 'Directly funded'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:9"
  ]
}
```

### "schools"."XCL_045" = 'Santa Clara' AND "schools"."XCL_063" = 1

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_045\" = 'Santa Clara' AND \"schools\".\"XCL_063\" = 1",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN \"XCL_065\" = 'Locally funded' THEN 1 ELSE 0 END) AS REAL) * 100 / SUM(CASE WHEN \"XCL_065\" <> 'Locally funded' THEN 1 ELSE 0 END) FROM schools WHERE \"XCL_045\" = 'Santa Clara' AND \"XCL_063\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:65"
  ]
}
```

### School Identifier (XCL_082)

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_082\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_082\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_013\" = 1 ORDER BY T1.\"XCL_019\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:35"
  ]
}
```

### School Identifier (XCL_058)

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_058\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_058\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_040\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:7"
  ]
}
```

### School Identifier

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\", T1.\"XCL_027\" * 100 / T1.\"XCL_024\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Los Angeles' AND T2.\"XCL_075\" = 'K-9'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_047\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_047\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_045\" = 'Los Angeles' AND \"r1\".\"XCL_075\" = 'K-9'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:77"
  ]
}
```

### School Attribute XCL_052

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_052\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_048\", T2.\"XCL_050\", T2.\"XCL_052\", T2.\"XCL_051\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY CAST(T1.\"XCL_040\" AS REAL) / T1.\"XCL_036\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:37"
  ]
}
```

### "schools"."XCL_045" = 'San Bernardino' AND "schools"."XCL_050" = 'San Bernardino' AND "schools"."XCL_066" = 54 AND STRFTIME('%Y', "schools"."XCL_061")

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_045\" = 'San Bernardino' AND \"schools\".\"XCL_050\" = 'San Bernardino' AND \"schools\".\"XCL_066\" = 54 AND STRFTIME('%Y', \"schools\".\"XCL_061\") BETWEEN '2009' AND '2010' AND \"schools\".\"XCL_068\" = 62",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_082\", T2.\"XCL_085\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'San Bernardino' AND T2.\"XCL_050\" = 'San Bernardino' AND T2.\"XCL_066\" = 54 AND STRFTIME('%Y', T2.\"XCL_061\") BETWEEN '2009' AND '2010' AND T2.\"XCL_068\" = 62",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:87"
  ]
}
```

### "schools"."XCL_046" = 'Fresno Unified' AND NOT "satscores"."XCL_037" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_046\" = 'Fresno Unified' AND NOT \"satscores\".\"XCL_037\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_058\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_046\" = 'Fresno Unified' AND NOT T1.\"XCL_037\" IS NULL ORDER BY T1.\"XCL_037\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:40"
  ]
}
```

### Direct attribute from the frpm table (XCL_004). Returns the value for each row in the joined result set for schools in Alusine.

```json
{
  "kind": "binding",
  "formula": "\"frpm\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_020\" * 100 / T1.\"XCL_019\", T1.\"XCL_004\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_080\" = 'Alusine'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_004\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_004\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_080\" = 'Alusine'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:85"
  ]
}
```

### School Attribute XCL_047

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_053\", T2.\"XCL_047\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_038\" DESC LIMIT 1 OFFSET 6",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:50"
  ]
}
```

### Calculates the ratio of schools with 'Locally funded' status to those with other funding statuses, expressed as a percentage. The numerator counts row

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"schools\".\"XCL_065\" = 'Locally funded' THEN 1 ELSE 0 END) AS REAL) * 100 / SUM(CASE WHEN \"schools\".\"XCL_065\" <> 'Locally funded' THEN 1 ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN \"XCL_065\" = 'Locally funded' THEN 1 ELSE 0 END) AS REAL) * 100 / SUM(CASE WHEN \"XCL_065\" <> 'Locally funded' THEN 1 ELSE 0 END) FROM schools WHERE \"XCL_045\" = 'Santa Clara' AND \"XCL_063\" = 1",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r0\".\"XCL_065\" = 'Locally funded' THEN 1 ELSE 0 END) AS REAL) * 100 / SUM(CASE WHEN \"r0\".\"XCL_065\" <> 'Locally funded' THEN 1 ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r0\".\"XCL_065\" = 'Locally funded' THEN 1 ELSE 0 END) AS REAL) * 100 / SUM(CASE WHEN \"r0\".\"XCL_065\" <> 'Locally funded' THEN 1 ELSE 0 END) AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_045\" = 'Santa Clara' AND \"r0\".\"XCL_063\" = 1",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:65"
  ]
}
```

### "schools"."XCL_045" = 'Los Angeles' AND "schools"."XCL_063" = 0 AND CAST("frpm"."XCL_020" AS REAL) * 100 / "frpm"."XCL_019" < 0.18

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_045\" = 'Los Angeles' AND \"schools\".\"XCL_063\" = 0 AND CAST(\"frpm\".\"XCL_020\" AS REAL) * 100 / \"frpm\".\"XCL_019\" < 0.18",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_047\") FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Los Angeles' AND T2.\"XCL_063\" = 0 AND CAST(T1.\"XCL_020\" AS REAL) * 100 / T1.\"XCL_019\" < 0.18",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:62"
  ]
}
```

### "frpm"."XCL_015" = 'Directly funded' AND "frpm"."XCL_013" = 1 AND "schools"."XCL_061" > '2000-01-01'

```json
{
  "kind": "predicate",
  "formula": "\"frpm\".\"XCL_015\" = 'Directly funded' AND \"frpm\".\"XCL_013\" = 1 AND \"schools\".\"XCL_061\" > '2000-01-01'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_058\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_015\" = 'Directly funded' AND T1.\"XCL_013\" = 1 AND T2.\"XCL_061\" > '2000-01-01'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:4"
  ]
}
```

### "frpm"."XCL_012" = 'Lunch Provision 2' AND "schools"."XCL_045" = 'Merced' AND "frpm"."XCL_017" = 9 AND "frpm"."XCL_018" = 12 AND "schools"."XCL_072" =

```json
{
  "kind": "predicate",
  "formula": "\"frpm\".\"XCL_012\" = 'Lunch Provision 2' AND \"schools\".\"XCL_045\" = 'Merced' AND \"frpm\".\"XCL_017\" = 9 AND \"frpm\".\"XCL_018\" = 12 AND \"schools\".\"XCL_072\" = 'HS'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_050\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_012\" = 'Lunch Provision 2' AND T2.\"XCL_045\" = 'Merced' AND T1.\"XCL_017\" = 9 AND T1.\"XCL_018\" = 12 AND T2.\"XCL_072\" = 'HS'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:76"
  ]
}
```

### Count of Female Students

```json
{
  "kind": "metric",
  "formula": "COUNT(\"schools\".\"XCL_076\")",
  "grain": [
    "\"schools\".\"XCL_045\""
  ],
  "population_scope": "SELECT \"XCL_045\", COUNT(\"XCL_076\") FROM schools WHERE (\"XCL_045\" = 'San Diego' OR \"XCL_045\" = 'Santa Barbara') AND \"XCL_076\" = 'F' GROUP BY \"XCL_045\" ORDER BY COUNT(\"XCL_076\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:79"
  ]
}
```

### School Attribute XCL_053

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_053\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_053\", T2.\"XCL_047\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_038\" DESC LIMIT 1 OFFSET 6",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:50"
  ]
}
```

### School Attribute XCL_047

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_058\", \"XCL_059\", \"XCL_047\" FROM schools WHERE \"XCL_051\" = '95203-3704'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_047\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_047\" AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_051\" = '95203-3704'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:58"
  ]
}
```

### Aggregates the count of rows from the satscores table (T1) that are joined to the schools table (T2) where the school city (T2.XCL_055) is 'Lakeport' 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"satscores\".\"XCL_030\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_030\") FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_055\" = 'Lakeport' AND (T1.\"XCL_037\" + T1.\"XCL_038\" + T1.\"XCL_039\") >= 1500",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_030\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "satscores"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_030\") AS \"value\" FROM satscores AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_055\" = 'Lakeport' AND (\"r0\".\"XCL_037\" + \"r0\".\"XCL_038\" + \"r0\".\"XCL_039\") >= 1500",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:52"
  ]
}
```

### Computed ratio of column XCL_020 divided by column XCL_019 for records in the frpm table where XCL_006 is 'Alameda'. The result is ordered in descendi

```json
{
  "kind": "binding",
  "formula": "\"frpm\".\"XCL_020\" / \"frpm\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_020\" / \"XCL_019\" FROM frpm WHERE \"XCL_006\" = 'Alameda' ORDER BY (CAST(\"XCL_020\" AS REAL) / \"XCL_019\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:0"
  ]
}
```

### School Attribute XCL_050

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_050\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_048\", T2.\"XCL_050\", T2.\"XCL_052\", T2.\"XCL_051\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY CAST(T1.\"XCL_040\" AS REAL) / T1.\"XCL_036\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:37"
  ]
}
```

### "schools"."XCL_068" = 31

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_068\" = 31",
  "grain": [],
  "population_scope": "SELECT \"XCL_042\" FROM schools WHERE \"XCL_068\" = 31",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:69"
  ]
}
```

### Output column from the schools table (alias T2). Represents a school attribute selected for each row in the joined result set.

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\", T1.\"XCL_039\", T2.\"XCL_058\" FROM schools AS T2 LEFT JOIN satscores AS T1 ON T2.\"XCL_041\" = T1.\"XCL_030\" WHERE STRFTIME('%Y', T2.\"XCL_061\") > '1991' OR STRFTIME('%Y', T2.\"XCL_062\") < '2000'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_047\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      },
      {
        "role": "r1",
        "physical_table": "satscores"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_047\" AS \"value\" FROM schools AS \"r0\" LEFT JOIN satscores AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_030\" WHERE STRFTIME('%Y', \"r0\".\"XCL_061\") > '1991' OR STRFTIME('%Y', \"r0\".\"XCL_062\") < '2000'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:27"
  ]
}
```

### NOT "satscores"."XCL_038" IS NULL

```json
{
  "kind": "predicate",
  "formula": "NOT \"satscores\".\"XCL_038\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_038\", T2.\"XCL_045\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE NOT T1.\"XCL_038\" IS NULL ORDER BY T1.\"XCL_038\" + T1.\"XCL_037\" + T1.\"XCL_039\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:43"
  ]
}
```

### SAT Score Metric

```json
{
  "kind": "binding",
  "formula": "\"satscores\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\", T1.\"XCL_039\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_080\" = 'Ricci' AND T2.\"XCL_081\" = 'Ulrich'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_039\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "satscores"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_039\" AS \"value\" FROM satscores AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_080\" = 'Ricci' AND \"r1\".\"XCL_081\" = 'Ulrich'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:45"
  ]
}
```

### School Identifier/Attribute

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_045\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_038\", T2.\"XCL_045\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE NOT T1.\"XCL_038\" IS NULL ORDER BY T1.\"XCL_038\" + T1.\"XCL_037\" + T1.\"XCL_039\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:43"
  ]
}
```

### School Attribute XCL_059

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_059\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_058\", T2.\"XCL_059\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_039\" DESC LIMIT 1 OFFSET 332",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:57"
  ]
}
```

### Identifier from the schools table (T2) for the school associated with the SAT score record having the minimum non-null value in column XCL_037.

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_053\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_053\", T2.\"XCL_047\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE NOT T1.\"XCL_037\" IS NULL ORDER BY T1.\"XCL_037\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:51"
  ]
}
```

### School XCL_080 Identifier

```json
{
  "kind": "binding",
  "formula": "T1.\"XCL_080\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_080\", T1.\"XCL_046\" FROM schools AS T1 INNER JOIN (SELECT \"XCL_080\" FROM schools GROUP BY \"XCL_080\" ORDER BY COUNT(\"XCL_080\") DESC LIMIT 2) AS T2 ON T1.\"XCL_080\" = T2.\"XCL_080\"",
  "upstream_scopes": [
    "SELECT \"XCL_080\" FROM schools GROUP BY \"XCL_080\" ORDER BY COUNT(\"XCL_080\") DESC LIMIT 2"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:84"
  ]
}
```

### School Identifier

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_060\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_060\" FROM schools WHERE \"XCL_045\" = 'San Joaquin' AND \"XCL_076\" = 'P' AND \"XCL_063\" = 1",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_060\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_060\" AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_045\" = 'San Joaquin' AND \"r0\".\"XCL_076\" = 'P' AND \"r0\".\"XCL_063\" = 1",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:60"
  ]
}
```

### Value of column XCL_050 from the schools table for the school associated with the satscores record having the highest XCL_040 value.

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_050\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_039\", T2.\"XCL_050\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_040\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:44"
  ]
}
```

### "satscores"."XCL_036" BETWEEN 2000 AND 3000 AND "schools"."XCL_045" = 'Los Angeles'

```json
{
  "kind": "predicate",
  "formula": "\"satscores\".\"XCL_036\" BETWEEN 2000 AND 3000 AND \"schools\".\"XCL_045\" = 'Los Angeles'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_060\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T1.\"XCL_036\" BETWEEN 2000 AND 3000 AND T2.\"XCL_045\" = 'Los Angeles'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:38"
  ]
}
```

### "frpm"."XCL_013" = 1

```json
{
  "kind": "predicate",
  "formula": "\"frpm\".\"XCL_013\" = 1",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_082\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_013\" = 1 ORDER BY T1.\"XCL_019\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:35"
  ]
}
```

### Value of column XCL_039 from the satscores table for the single record with the highest XCL_040 value.

```json
{
  "kind": "binding",
  "formula": "\"satscores\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_039\", T2.\"XCL_050\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_040\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:44"
  ]
}
```

### School Identifier

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_060\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_060\" FROM schools WHERE (\"XCL_080\" = 'Mike' AND \"XCL_081\" = 'Larson') OR (\"XCL_080\" = 'Dante' AND \"XCL_081\" = 'Alvarez')",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_060\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_060\" AS \"value\" FROM schools AS \"r0\" WHERE (\"r0\".\"XCL_080\" = 'Mike' AND \"r0\".\"XCL_081\" = 'Larson') OR (\"r0\".\"XCL_080\" = 'Dante' AND \"r0\".\"XCL_081\" = 'Alvarez')",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:59"
  ]
}
```

### School Attribute XCL_059

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_059\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_058\", \"XCL_059\", \"XCL_047\" FROM schools WHERE \"XCL_051\" = '95203-3704'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_059\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_059\" AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_051\" = '95203-3704'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:58"
  ]
}
```

### STRFTIME('%Y', "schools"."XCL_061") BETWEEN '2000' AND '2005' AND "schools"."XCL_045" = 'Stanislaus' AND "schools"."XCL_065" = 'Directly funded'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"schools\".\"XCL_061\") BETWEEN '2000' AND '2005' AND \"schools\".\"XCL_045\" = 'Stanislaus' AND \"schools\".\"XCL_065\" = 'Directly funded'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_047\") FROM schools WHERE STRFTIME('%Y', \"XCL_061\") BETWEEN '2000' AND '2005' AND \"XCL_045\" = 'Stanislaus' AND \"XCL_065\" = 'Directly funded'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:66"
  ]
}
```

### "schools"."XCL_042" = '0613360' AND "schools"."XCL_070" = 'SPECON'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_042\" = '0613360' AND \"schools\".\"XCL_070\" = 'SPECON'",
  "grain": [],
  "population_scope": "SELECT MIN(T1.\"XCL_017\") FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_042\" = '0613360' AND T2.\"XCL_070\" = 'SPECON'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:74"
  ]
}
```

### School Identifier (XCL_050)

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_050\"",
  "grain": [
    "\"schools\".\"XCL_050\""
  ],
  "population_scope": "SELECT T2.\"XCL_050\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" GROUP BY T2.\"XCL_050\" ORDER BY SUM(T1.\"XCL_019\") ASC LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:30"
  ]
}
```

### School Identifier (XCL_071)

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_071\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_071\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_038\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:42"
  ]
}
```

### SAT score metric

```json
{
  "kind": "binding",
  "formula": "\"satscores\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_036\" FROM satscores WHERE \"XCL_030\" = (SELECT \"XCL_001\" FROM frpm ORDER BY \"XCL_022\" DESC LIMIT 1)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:8"
  ]
}
```

### A calculated metric derived from the frpm table, computed as (XCL_027 * 100) / XCL_024. It represents a percentage ratio of two FRPM fields, likely in

```json
{
  "kind": "binding",
  "formula": "\"frpm\".\"XCL_027\" * 100 / \"frpm\".\"XCL_024\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\", T1.\"XCL_027\" * 100 / T1.\"XCL_024\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Los Angeles' AND T2.\"XCL_075\" = 'K-9'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_027\" * 100 / \"r0\".\"XCL_024\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_027\" * 100 / \"r0\".\"XCL_024\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_045\" = 'Los Angeles' AND \"r1\".\"XCL_075\" = 'K-9'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:77"
  ]
}
```

### School Attribute XCL_081

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_081\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_080\", T2.\"XCL_081\", T2.\"XCL_083\", T2.\"XCL_084\", T2.\"XCL_086\", T2.\"XCL_087\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY T1.\"XCL_040\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:36"
  ]
}
```

### Identifier for the school record from the 'schools' table (T2), filtered to the specific school named 'Ricci Ulrich'.

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\", T1.\"XCL_039\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_080\" = 'Ricci' AND T2.\"XCL_081\" = 'Ulrich'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_047\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "satscores"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_047\" AS \"value\" FROM satscores AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_080\" = 'Ricci' AND \"r1\".\"XCL_081\" = 'Ulrich'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:45"
  ]
}
```

### School Attribute XCL_051

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_051\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_048\", T2.\"XCL_050\", T2.\"XCL_052\", T2.\"XCL_051\" FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" ORDER BY CAST(T1.\"XCL_040\" AS REAL) / T1.\"XCL_036\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:37"
  ]
}
```

### Count of distinct schools with high SAT scores

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"schools\".\"XCL_047\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T2.\"XCL_047\") FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_030\" = T2.\"XCL_041\" WHERE T2.\"XCL_076\" = 'F' AND T1.\"XCL_038\" > 400",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r1\".\"XCL_047\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "satscores"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r1\".\"XCL_047\") AS \"value\" FROM satscores AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_076\" = 'F' AND \"r0\".\"XCL_038\" > 400",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:5"
  ]
}
```

### School Attribute XCL_045

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_045\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_081\", \"XCL_046\", \"XCL_045\", \"XCL_047\" FROM schools WHERE \"XCL_064\" = '0040'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_045\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_045\" AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_064\" = '0040'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:86"
  ]
}
```

### "schools"."XCL_066" = 52 AND "schools"."XCL_045" = 'Alameda' AND STRFTIME('%Y', "schools"."XCL_061") = '1980'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_066\" = 52 AND \"schools\".\"XCL_045\" = 'Alameda' AND STRFTIME('%Y', \"schools\".\"XCL_061\") = '1980'",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(\"XCL_047\") AS REAL) / 12 FROM schools WHERE \"XCL_066\" = 52 AND \"XCL_045\" = 'Alameda' AND STRFTIME('%Y', \"XCL_061\") = '1980'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:47"
  ]
}
```

### Minimum XCL_017 for SPECON school 0613360

```json
{
  "kind": "metric",
  "formula": "MIN(\"frpm\".\"XCL_017\")",
  "grain": [],
  "population_scope": "SELECT MIN(T1.\"XCL_017\") FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_042\" = '0613360' AND T2.\"XCL_070\" = 'SPECON'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MIN(\"r0\".\"XCL_017\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT MIN(\"r0\".\"XCL_017\") AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_042\" = '0613360' AND \"r1\".\"XCL_070\" = 'SPECON'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:74"
  ]
}
```

### Filtered FRPM School Identifier

```json
{
  "kind": "binding",
  "formula": "\"frpm\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_001\" FROM schools AS T1 INNER JOIN frpm AS T2 ON T1.\"XCL_041\" = T2.\"XCL_001\" WHERE T2.\"XCL_019\" + T2.\"XCL_024\" > 500",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      },
      {
        "role": "r1",
        "physical_table": "frpm"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_001\" AS \"value\" FROM schools AS \"r0\" INNER JOIN frpm AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_001\" WHERE \"r1\".\"XCL_019\" + \"r1\".\"XCL_024\" > 500",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:11"
  ]
}
```

### Schools XCL_060

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_060\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_060\", T1.\"XCL_008\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T1.\"XCL_025\" BETWEEN 1900 AND 2000 AND NOT T2.\"XCL_060\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_060\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_060\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r0\".\"XCL_025\" BETWEEN 1900 AND 2000 AND NOT \"r1\".\"XCL_060\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:33"
  ]
}
```

### "schools"."XCL_050" = 'Adelanto'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_050\" = 'Adelanto'",
  "grain": [
    "\"schools\".\"XCL_075\""
  ],
  "population_scope": "SELECT \"XCL_075\" FROM schools WHERE \"XCL_050\" = 'Adelanto' GROUP BY \"XCL_075\" ORDER BY COUNT(\"XCL_075\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:78"
  ]
}
```

### "schools"."XCL_066" = 52 AND "schools"."XCL_063" = 1 AND "schools"."XCL_050" = 'Hickman'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_066\" = 52 AND \"schools\".\"XCL_063\" = 1 AND \"schools\".\"XCL_050\" = 'Hickman'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_047\") FROM schools WHERE \"XCL_066\" = 52 AND \"XCL_063\" = 1 AND \"XCL_050\" = 'Hickman'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:61"
  ]
}
```

### The value of column XCL_004 from the frpm table, returned for records joined to schools in Fresno where schools.XCL_077 is 0.

```json
{
  "kind": "binding",
  "formula": "\"frpm\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_004\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_050\" = 'Fresno' AND T2.\"XCL_077\" = 0",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_004\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "frpm"
      },
      {
        "role": "r1",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_004\" AS \"value\" FROM frpm AS \"r0\" INNER JOIN schools AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_041\" WHERE \"r1\".\"XCL_050\" = 'Fresno' AND \"r1\".\"XCL_077\" = 0",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:71"
  ]
}
```

### "schools"."XCL_045" = 'Los Angeles' AND "schools"."XCL_075" = 'K-9'

```json
{
  "kind": "predicate",
  "formula": "\"schools\".\"XCL_045\" = 'Los Angeles' AND \"schools\".\"XCL_075\" = 'K-9'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\", T1.\"XCL_027\" * 100 / T1.\"XCL_024\" FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.\"XCL_001\" = T2.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Los Angeles' AND T2.\"XCL_075\" = 'K-9'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:77"
  ]
}
```

### Returns the value of column XCL_042 for schools where column XCL_068 equals 31. The grain is individual school records filtered by the condition on XC

```json
{
  "kind": "binding",
  "formula": "\"schools\".\"XCL_042\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_042\" FROM schools WHERE \"XCL_068\" = 31",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_042\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "schools"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_042\" AS \"value\" FROM schools AS \"r0\" WHERE \"r0\".\"XCL_068\" = 31",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:69"
  ]
}
```

### ("schools"."XCL_044" = 'Closed' OR "schools"."XCL_044" = 'Active') AND "schools"."XCL_068" = 69 AND "schools"."XCL_045" = 'Alpine'

```json
{
  "kind": "predicate",
  "formula": "(\"schools\".\"XCL_044\" = 'Closed' OR \"schools\".\"XCL_044\" = 'Active') AND \"schools\".\"XCL_068\" = 69 AND \"schools\".\"XCL_045\" = 'Alpine'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_047\") FROM schools WHERE (\"XCL_044\" = 'Closed' OR \"XCL_044\" = 'Active') AND \"XCL_068\" = 69 AND \"XCL_045\" = 'Alpine'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:70"
  ]
}
```


## 增量维护事件

- Recorded alias revision · schools.XCL_080 · Archived superseded_alias_hypotheses → archived aliases
  - schools.XCL_080: Principal First Name → Administrator First Name
- Recorded alias revision · schools.XCL_051 · Archived superseded_alias_hypotheses → archived aliases
  - schools.XCL_051: Zip Code → Mailing Zip Code
- Recorded alias revision · schools.XCL_066 · Archived superseded_alias_hypotheses → archived aliases
  - schools.XCL_066: District Type Code → EdOps Code
