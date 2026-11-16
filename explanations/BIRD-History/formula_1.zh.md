# BIRD-History / formula_1 — Schema 与业务口径解释

该数据库的存档目录包含 13 张表、80 个物理列、34 条关系，以及 174 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## circuits

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T0, T1, T3, T4, c, c2, ci, ct

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| circuits.XCL_001 | circuit_id | unknown | bird_dev:890, bird_dev:1016, bird_dev:945, bird_dev:1014, bird_dev:925, bird_dev:923, bird_dev:850, bird_dev:903 |
| circuits.XCL_002 | circuit_slug | unknown | bird_dev:912 |
| circuits.XCL_003 | circuit_name | unknown | bird_dev:890, bird_dev:903, bird_dev:1001, bird_dev:924, bird_dev:911, bird_dev:910, bird_dev:993, bird_dev:899 |
| circuits.XCL_004 | location | unknown | bird_dev:945, bird_dev:888, bird_dev:978, bird_dev:900, bird_dev:848, bird_dev:908, bird_dev:1000, bird_dev:901 |
| circuits.XCL_005 | country | unknown | bird_dev:945, bird_dev:1014, bird_dev:923, bird_dev:850, bird_dev:907, bird_dev:1019, bird_dev:888, bird_dev:978 |
| circuits.XCL_006 | latitude | unknown | bird_dev:857, bird_dev:911, bird_dev:910, bird_dev:978, bird_dev:993, bird_dev:854, bird_dev:1017, bird_dev:868 |
| circuits.XCL_007 | longitude | unknown | bird_dev:857, bird_dev:910, bird_dev:978, bird_dev:993, bird_dev:854, bird_dev:1017, bird_dev:868, bird_dev:946 |
| circuits.XCL_008 | 保留物理名称；存档没有恢复别名 | unknown | bird_dev:913 |
| circuits.XCL_009 | url | unknown | bird_dev:925, bird_dev:849, bird_dev:921, bird_dev:855 |

## constructorResults

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, cr

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| constructorResults.XCL_011 | race_id | unknown | bird_dev:994, bird_dev:858, bird_dev:869 |
| constructorResults.XCL_012 | constructor_id | unknown | bird_dev:994, bird_dev:858, bird_dev:869 |
| constructorResults.XCL_013 | points | unknown | bird_dev:994, bird_dev:858, bird_dev:869 |

## constructorStandings

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, cs

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| constructorStandings.XCL_016 | standings_id | unknown | bird_dev:950, bird_dev:951 |
| constructorStandings.XCL_017 | constructor_id | unknown | bird_dev:851, bird_dev:950, bird_dev:983, bird_dev:948, bird_dev:951, bird_dev:949, bird_dev:984 |
| constructorStandings.XCL_018 | points | unknown | bird_dev:950, bird_dev:983, bird_dev:948, bird_dev:951, bird_dev:949 |
| constructorStandings.XCL_019 | position | unknown | bird_dev:851 |
| constructorStandings.XCL_021 | wins | unknown | bird_dev:984 |

## constructors

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, T3, c, co, con, cons, ct

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| constructors.XCL_022 | constructor_id | unknown | bird_dev:952, bird_dev:851, bird_dev:950, bird_dev:990, bird_dev:953, bird_dev:983, bird_dev:948, bird_dev:994 |
| constructors.XCL_023 | constructor_name_slug | unknown | bird_dev:990 |
| constructors.XCL_024 | constructor_name | unknown | bird_dev:952, bird_dev:851, bird_dev:950, bird_dev:994, bird_dev:949 |
| constructors.XCL_025 | nationality | unknown | bird_dev:953, bird_dev:983, bird_dev:948, bird_dev:994, bird_dev:858, bird_dev:951 |
| constructors.XCL_026 | url | unknown | bird_dev:990, bird_dev:983, bird_dev:869, bird_dev:984 |

## driverStandings

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, ds, ds2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| driverStandings.XCL_027 | driver standing id | unknown | bird_dev:896 |
| driverStandings.XCL_028 | race id | unknown | bird_dev:905, bird_dev:892, bird_dev:902, bird_dev:966, bird_dev:903, bird_dev:995, bird_dev:896, bird_dev:893 |
| driverStandings.XCL_029 | driver id | unknown | bird_dev:905, bird_dev:892, bird_dev:902, bird_dev:966, bird_dev:903, bird_dev:995, bird_dev:896, bird_dev:893 |
| driverStandings.XCL_030 | points | unknown | bird_dev:905, bird_dev:892, bird_dev:995, bird_dev:893, bird_dev:998, bird_dev:897, bird_dev:906 |
| driverStandings.XCL_031 | position | unknown | bird_dev:902, bird_dev:896, bird_dev:891 |
| driverStandings.XCL_033 | wins | unknown | bird_dev:903, bird_dev:1004, bird_dev:998, bird_dev:897 |

## drivers

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, T2i, T3, T4, d, d2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| drivers.XCL_034 | driver_id | unknown | bird_dev:879, bird_dev:873, bird_dev:878, bird_dev:905, bird_dev:1011, bird_dev:872, bird_dev:892, bird_dev:902 |
| drivers.XCL_035 | driver_code | unknown | bird_dev:968, bird_dev:846, bird_dev:928, bird_dev:971, bird_dev:918, bird_dev:980 |
| drivers.XCL_036 | car_number | unknown | bird_dev:861 |
| drivers.XCL_037 | driver_abbreviation | unknown | bird_dev:872, bird_dev:972, bird_dev:914, bird_dev:964 |
| drivers.XCL_038 | forename | unknown | bird_dev:968, bird_dev:873, bird_dev:917, bird_dev:991, bird_dev:878, bird_dev:905, bird_dev:1011, bird_dev:898 |
| drivers.XCL_039 | surname | unknown | bird_dev:968, bird_dev:873, bird_dev:917, bird_dev:991, bird_dev:878, bird_dev:905, bird_dev:1011, bird_dev:898 |
| drivers.XCL_040 | date_of_birth | unknown | bird_dev:991, bird_dev:898, bird_dev:988, bird_dev:969, bird_dev:981, bird_dev:915, bird_dev:971, bird_dev:865 |
| drivers.XCL_041 | nationality | unknown | bird_dev:879, bird_dev:991, bird_dev:898, bird_dev:988, bird_dev:969, bird_dev:997, bird_dev:915, bird_dev:971 |
| drivers.XCL_042 | wikipedia_url | unknown | bird_dev:917, bird_dev:938, bird_dev:866, bird_dev:992 |

## lapTimes

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T1i, T2, T3, T5, lt, lt2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| lapTimes.XCL_043 | race_id | unknown | bird_dev:878, bird_dev:975, bird_dev:985, bird_dev:1019, bird_dev:866, bird_dev:895, bird_dev:894, bird_dev:908 |
| lapTimes.XCL_044 | driver_id | unknown | bird_dev:976, bird_dev:878, bird_dev:1011, bird_dev:985, bird_dev:1012, bird_dev:1010, bird_dev:866, bird_dev:895 |
| lapTimes.XCL_045 | lap_number | unknown | bird_dev:976, bird_dev:985, bird_dev:1019, bird_dev:908, bird_dev:986 |
| lapTimes.XCL_046 | position | unknown | bird_dev:1012 |
| lapTimes.XCL_047 | lap_time | unknown | bird_dev:976, bird_dev:1006, bird_dev:878, bird_dev:1011, bird_dev:975, bird_dev:985, bird_dev:1012, bird_dev:1010 |
| lapTimes.XCL_048 | lap_time_ms | unknown | bird_dev:1019, bird_dev:895, bird_dev:894, bird_dev:904, bird_dev:986 |

## pitStops

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T4, p, ps

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| pitStops.XCL_049 | race_id | unknown | bird_dev:1016, bird_dev:1008, bird_dev:1009 |
| pitStops.XCL_050 | driver_id | unknown | bird_dev:1016, bird_dev:988, bird_dev:1007, bird_dev:973, bird_dev:1008, bird_dev:1018, bird_dev:970 |
| pitStops.XCL_052 | lap | unknown | bird_dev:1008 |
| pitStops.XCL_053 | time | unknown | bird_dev:973, bird_dev:970 |
| pitStops.XCL_054 | duration | unknown | bird_dev:1016, bird_dev:1005, bird_dev:988, bird_dev:1007, bird_dev:1009 |

## qualifying

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: Q, T1, T2, q

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| qualifying.XCL_057 | race_id | unknown | bird_dev:872, bird_dev:846, bird_dev:1001, bird_dev:981, bird_dev:847, bird_dev:861, bird_dev:860, bird_dev:871 |
| qualifying.XCL_058 | driver_id | unknown | bird_dev:872, bird_dev:846, bird_dev:1001, bird_dev:981, bird_dev:847, bird_dev:861, bird_dev:860, bird_dev:871 |
| qualifying.XCL_062 | q1_time | unknown | bird_dev:846, bird_dev:870, bird_dev:859 |
| qualifying.XCL_063 | q2_time | unknown | bird_dev:847, bird_dev:860, bird_dev:871, bird_dev:980 |
| qualifying.XCL_064 | q3_time | unknown | bird_dev:872, bird_dev:861 |

## races

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: R, T1, T2, T3, T6, cr, fr, r, r2, ra, ra2, race, rc

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| races.XCL_065 | race_id | unknown | bird_dev:1016, bird_dev:961, bird_dev:1014, bird_dev:905, bird_dev:931, bird_dev:974, bird_dev:892, bird_dev:902 |
| races.XCL_066 | year | unknown | bird_dev:887, bird_dev:961, bird_dev:882, bird_dev:905, bird_dev:886, bird_dev:931, bird_dev:974, bird_dev:925 |
| races.XCL_067 | round | unknown | bird_dev:886, bird_dev:885 |
| races.XCL_068 | circuit_id | unknown | bird_dev:890, bird_dev:1016, bird_dev:1014, bird_dev:925, bird_dev:923, bird_dev:850, bird_dev:903, bird_dev:857 |
| races.XCL_069 | race_name | unknown | bird_dev:890, bird_dev:887, bird_dev:1016, bird_dev:961, bird_dev:882, bird_dev:931, bird_dev:925, bird_dev:902 |
| races.XCL_070 | race_date | unknown | bird_dev:885, bird_dev:981, bird_dev:881, bird_dev:876, bird_dev:907, bird_dev:924, bird_dev:899, bird_dev:922 |
| races.XCL_071 | race_time | unknown | bird_dev:981, bird_dev:922, bird_dev:856 |

## results

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, T3, T4, T5, r, r2, r3, res, rs, w

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| results.XCL_073 | result_id | unknown | bird_dev:943 |
| results.XCL_074 | race_id | unknown | bird_dev:977, bird_dev:873, bird_dev:1016, bird_dev:979, bird_dev:961, bird_dev:1014, bird_dev:931, bird_dev:974 |
| results.XCL_075 | driver_id | unknown | bird_dev:879, bird_dev:873, bird_dev:1016, bird_dev:862, bird_dev:928, bird_dev:958, bird_dev:881, bird_dev:942 |
| results.XCL_076 | constructor_id | unknown | bird_dev:952, bird_dev:990, bird_dev:953 |
| results.XCL_078 | grid_position | unknown | bird_dev:934 |
| results.XCL_079 | position | unknown | bird_dev:874 |
| results.XCL_081 | position_text | unknown | bird_dev:933, bird_dev:955, bird_dev:944 |
| results.XCL_082 | points | unknown | bird_dev:941 |
| results.XCL_083 | laps | unknown | bird_dev:953, bird_dev:962 |
| results.XCL_084 | time | unknown | bird_dev:977, bird_dev:873, bird_dev:979, bird_dev:862, bird_dev:881, bird_dev:959, bird_dev:876, bird_dev:938 |
| results.XCL_085 | milliseconds | unknown | bird_dev:961 |
| results.XCL_086 | fastest_lap | unknown | bird_dev:959, bird_dev:936 |
| results.XCL_087 | fastest_lap_rank | unknown | bird_dev:952, bird_dev:928, bird_dev:956, bird_dev:937, bird_dev:987 |
| results.XCL_088 | fastest_lap_time | unknown | bird_dev:1016, bird_dev:1014, bird_dev:974, bird_dev:958, bird_dev:942, bird_dev:867, bird_dev:972, bird_dev:987 |
| results.XCL_089 | average_speed | unknown | bird_dev:879, bird_dev:931, bird_dev:867, bird_dev:960, bird_dev:927, bird_dev:880 |
| results.XCL_090 | status_id | unknown | bird_dev:977, bird_dev:982, bird_dev:1003 |

## seasons

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| seasons.XCL_091 | year | unknown | bird_dev:863, bird_dev:875 |
| seasons.XCL_092 | url | unknown | bird_dev:863, bird_dev:875 |

## status

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T3, s

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| status.XCL_093 | status_id | unknown | bird_dev:982, bird_dev:1003 |
| status.XCL_094 | status | unknown | bird_dev:982 |

## 表关系与连接依据

- circuits.XCL_001 ↔ races.XCL_068; target_disjoint_historical_join
- constructorResults.XCL_011 ↔ races.XCL_065; target_disjoint_historical_join
- constructorResults.XCL_012 ↔ constructors.XCL_022; target_disjoint_historical_join
- constructorStandings.XCL_017 ↔ constructors.XCL_022; target_disjoint_historical_join
- constructors.XCL_022 ↔ results.XCL_076; target_disjoint_historical_join
- driverStandings.XCL_028 ↔ races.XCL_065; target_disjoint_historical_join
- driverStandings.XCL_029 ↔ drivers.XCL_034; target_disjoint_historical_join
- drivers.XCL_034 ↔ lapTimes.XCL_044; target_disjoint_historical_join
- drivers.XCL_034 ↔ pitStops.XCL_050; target_disjoint_historical_join
- drivers.XCL_034 ↔ qualifying.XCL_058; target_disjoint_historical_join
- drivers.XCL_034 ↔ results.XCL_075; target_disjoint_historical_join
- lapTimes.XCL_043 ↔ races.XCL_065; target_disjoint_historical_join
- pitStops.XCL_049 ↔ races.XCL_065; target_disjoint_historical_join
- qualifying.XCL_057 ↔ races.XCL_065; target_disjoint_historical_join
- races.XCL_065 ↔ results.XCL_074; target_disjoint_historical_join
- races.XCL_066 ↔ seasons.XCL_091; target_disjoint_historical_join
- results.XCL_090 ↔ status.XCL_093; target_disjoint_historical_join
- circuits.XCL_001 ↔ races.XCL_068; sql_workload_observed_join
- constructorResults.XCL_011 ↔ races.XCL_065; sql_workload_observed_join
- constructorResults.XCL_012 ↔ constructors.XCL_022; sql_workload_observed_join
- constructorStandings.XCL_017 ↔ constructors.XCL_022; sql_workload_observed_join
- constructors.XCL_022 ↔ results.XCL_076; sql_workload_observed_join
- driverStandings.XCL_028 ↔ races.XCL_065; sql_workload_observed_join
- driverStandings.XCL_029 ↔ drivers.XCL_034; sql_workload_observed_join
- drivers.XCL_034 ↔ lapTimes.XCL_044; sql_workload_observed_join
- drivers.XCL_034 ↔ pitStops.XCL_050; sql_workload_observed_join
- drivers.XCL_034 ↔ qualifying.XCL_058; sql_workload_observed_join
- drivers.XCL_034 ↔ results.XCL_075; sql_workload_observed_join
- lapTimes.XCL_043 ↔ races.XCL_065; sql_workload_observed_join
- pitStops.XCL_049 ↔ races.XCL_065; sql_workload_observed_join
- qualifying.XCL_057 ↔ races.XCL_065; sql_workload_observed_join
- races.XCL_065 ↔ results.XCL_074; sql_workload_observed_join
- races.XCL_066 ↔ seasons.XCL_091; sql_workload_observed_join
- results.XCL_090 ↔ status.XCL_093; sql_workload_observed_join

## 业务口径、总体与粒度

### Full SQL program that retrieves distinct XCL_019 values from constructorStandings by joining with constructors on XCL_017 = XCL_022 and filtering for 

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_019\" FROM constructorStandings AS T1 INNER JOIN constructors AS T2 ON T2.\"XCL_022\" = T1.\"XCL_017\" WHERE T2.\"XCL_024\" = 'Renault'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:851"
  ]
}
```

### Full SQL program that joins qualifying and drivers tables to retrieve distinct driver identifiers for a specific qualifying session (347) where the qu

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_041\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 347 AND T1.\"XCL_063\" LIKE '1:15%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:871"
  ]
}
```

### A query that retrieves pit stop details by joining pitStops, drivers, and races tables. It filters for the driver with first name 'Lewis' and last nam

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_052\" FROM pitStops AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_050\" = T2.\"XCL_034\" INNER JOIN races AS T3 ON T1.\"XCL_049\" = T3.\"XCL_065\" WHERE T2.\"XCL_038\" = 'Lewis' AND T2.\"XCL_039\" = 'Hamilton' AND T3.\"XCL_066\" = 2011 AND T3.\"XCL_069\" = 'Australian Grand Prix'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1008"
  ]
}
```

### A query that joins races and results to find the maximum non-null value of XCL_089 for the 2009 Spanish Grand Prix. It filters races by name 'Spanish 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_089\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" WHERE T1.\"XCL_069\" = 'Spanish Grand Prix' AND T1.\"XCL_066\" = 2009 AND NOT T2.\"XCL_089\" IS NULL ORDER BY T2.\"XCL_089\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:931"
  ]
}
```

### A program that retrieves the details (ID, name, timestamp, location) of the first race (ordered by XCL_070 ASC) in which the driver with the highest X

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_066\", T3.\"XCL_069\", T3.\"XCL_070\", T3.\"XCL_071\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_058\" = T2.\"XCL_034\" INNER JOIN races AS T3 ON T1.\"XCL_057\" = T3.\"XCL_065\" WHERE T1.\"XCL_058\" = (SELECT \"XCL_034\" FROM drivers ORDER BY \"XCL_040\" DESC LIMIT 1) ORDER BY T3.\"XCL_070\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:981"
  ]
}
```

### Executes an inner join between races and seasons on the condition that seasons.XCL_091 equals races.XCL_066, filtered to races where races.XCL_065 is 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_092\" FROM races AS T1 INNER JOIN seasons AS T2 ON T2.\"XCL_091\" = T1.\"XCL_066\" WHERE T1.\"XCL_065\" = 901",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:863",
    "bird_dev:875"
  ]
}
```

### A query that identifies circuits by joining the 'circuits' and 'races' tables on the circuit ID. It filters races to those occurring between 1990 and 

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_003\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE STRFTIME('%Y', T2.\"XCL_070\") BETWEEN '1990' AND '2000' GROUP BY T1.\"XCL_003\" HAVING COUNT(T2.\"XCL_065\") = 4",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:899"
  ]
}
```

### Full SQL program that joins qualifying and drivers tables to retrieve distinct driver identifiers for a specific qualifying session (355) where the qu

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_041\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 355 AND T1.\"XCL_063\" LIKE '1:40%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:860"
  ]
}
```

### A program that joins the drivers table (T1) with the results table (T2) on T1.XCL_034 = T2.XCL_075. It orders the results by T2.XCL_089 in descending 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_041\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" ORDER BY T2.\"XCL_089\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:879"
  ]
}
```

### A SQL program that retrieves lap times from the lapTimes table by joining with the drivers table on the driver identifier (XCL_044 = XCL_034) and filt

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_047\" FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_044\" = T2.\"XCL_034\" WHERE T2.\"XCL_038\" = 'Lewis' AND T2.\"XCL_039\" = 'Hamilton'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1010"
  ]
}
```

### A program that joins lapTimes and races to find the top lap time record. It filters for the 'French Grand Prix' (races.XCL_069) and a specific driver 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_044\" FROM lapTimes AS T1 INNER JOIN races AS T2 ON T1.\"XCL_043\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'French Grand Prix' AND T1.\"XCL_045\" = 3 ORDER BY T1.\"XCL_047\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:985"
  ]
}
```

### A query that joins circuits, races, and lapTimes to find the single record with the highest value in lapTimes.XCL_045. It returns the lap time value, 

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_045\", T2.\"XCL_069\", T2.\"XCL_066\", T1.\"XCL_004\" FROM circuits AS T1 INNER JOIN races AS T2 ON T1.\"XCL_001\" = T2.\"XCL_068\" INNER JOIN lapTimes AS T3 ON T3.\"XCL_043\" = T2.\"XCL_065\" ORDER BY T3.\"XCL_045\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:908"
  ]
}
```

### Adelaide Australia Circuit Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_001\") FROM circuits WHERE \"XCL_004\" = 'Adelaide' AND \"XCL_005\" = 'Australia'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:945"
  ]
}
```

### A query that filters the races table for the 'Singapore Grand Prix' event, orders the results by the race identifier (XCL_066) in ascending order, and

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_066\" FROM races WHERE \"XCL_069\" = 'Singapore Grand Prix' ORDER BY \"XCL_066\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:882"
  ]
}
```

### Driver-specific result comparison query

```json
{
  "kind": "program",
  "formula": "SELECT (SUM(IIF(T2.\"XCL_074\" = 853, T2.\"XCL_089\", 0)) - SUM(IIF(T2.\"XCL_074\" = 854, T2.\"XCL_089\", 0))) * 100 / SUM(IIF(T2.\"XCL_074\" = 853, T2.\"XCL_089\", 0)) FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE T1.\"XCL_038\" = 'Paul' AND T1.\"XCL_039\" = 'di Resta'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:880"
  ]
}
```

### Query for German Race IDs

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_069\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_005\" = 'Germany'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:850"
  ]
}
```

### A SQL program that joins races, results, and drivers tables to retrieve race identifiers (XCL_069) associated with driver Lewis Hamilton. It filters d

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_069\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T3.\"XCL_038\" = 'Lewis' AND T3.\"XCL_039\" = 'Hamilton'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:929"
  ]
}
```

### Constructor Standings Query

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_024\" FROM constructorStandings AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_017\" = T2.\"XCL_022\" WHERE T1.\"XCL_018\" = 0 AND T1.\"XCL_016\" = 291",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:950"
  ]
}
```

### 2008 Chinese GP Result Query

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_084\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T1.\"XCL_087\" = 2 AND T2.\"XCL_069\" = 'Chinese Grand Prix' AND T2.\"XCL_066\" = 2008",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:937"
  ]
}
```

### A query that joins the 'circuits' table (T1) with the 'races' table (T2) on the circuit key (XCL_001 = XCL_068). It filters for races where the year (

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_009\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_066\" = 2009 AND T2.\"XCL_069\" = 'Spanish Grand Prix'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:925"
  ]
}
```

### 2017 Race-Circuit List

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_069\", T1.\"XCL_005\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_066\" = 2017 ORDER BY T2.\"XCL_070\" ASC",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:907"
  ]
}
```

### Full SQL program that retrieves distinct race identifiers from the races table by joining with the circuits table on the circuit foreign key and filte

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_071\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Sepang International Circuit'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:856"
  ]
}
```

### A program that calculates the percentage gap of the last finishing driver relative to the winner's time in the 2008 Australian Grand Prix. The formula

```json
{
  "kind": "program",
  "formula": "WITH time_in_seconds AS (SELECT T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6) AS REAL) ELSE CAST(SUBSTRING(T1.\"XCL_084\", 2) AS REAL) END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Australian Grand Prix' AND NOT T1.\"XCL_084\" IS NULL AND T2.\"XCL_066\" = 2008), champion_time AS (SELECT \"time_seconds\" FROM time_in_seconds WHERE \"XCL_081\" = 1), last_driver_incremental AS (SELECT \"time_seconds\" FROM time_in_seconds WHERE \"XCL_081\" = (SELECT MAX(\"XCL_081\") FROM time_in_seconds)) SELECT (CAST((SELECT \"time_seconds\" FROM last_driver_incremental) AS REAL) * 100) / (SELECT \"time_seconds\" + (SELECT \"time_seconds\" FROM last_driver_incremental) FROM champion_time)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:944"
  ]
}
```

### A query that retrieves the "XCL_042" value from the drivers table for the driver with first name 'Anthony' and last name 'Davidson' (based on columns 

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_042\" FROM drivers WHERE \"XCL_038\" = 'Anthony' AND \"XCL_039\" = 'Davidson'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:917"
  ]
}
```

### Query that retrieves attributes XCL_006 and XCL_007 from the circuits table where the circuit name (XCL_003) is 'Silverstone Circuit'.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_006\", \"XCL_007\" FROM circuits WHERE \"XCL_003\" = 'Silverstone Circuit'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:910"
  ]
}
```

### A query that retrieves the result identifier ("XCL_081") for a specific driver (Lewis Hamilton) in a specific race (Chinese Grand Prix, 2008). It join

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_081\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T3.\"XCL_038\" = 'Lewis' AND T3.\"XCL_039\" = 'Hamilton' AND T1.\"XCL_069\" = 'Chinese Grand Prix' AND T1.\"XCL_066\" = 2008",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:933"
  ]
}
```

### A query that joins the circuits and races tables to retrieve the circuit name for the race identified as the 'Spanish Grand Prix' in the year 2009. It

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_003\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_066\" = 2009 AND T2.\"XCL_069\" = 'Spanish Grand Prix'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:919"
  ]
}
```

### Full SQL program that filters the 'drivers' table for records with 'British' nationality and a date ('XCL_040') in a year later than 1980, then counts

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_034\") FROM drivers WHERE \"XCL_041\" = 'British' AND STRFTIME('%Y', \"XCL_040\") > '1980'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:947"
  ]
}
```

### Query: Race IDs for Spanish Circuits

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_069\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_005\" = 'Spain'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:853"
  ]
}
```

### 2008 Canadian GP Driver Times

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_084\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Canadian Grand Prix' AND T2.\"XCL_066\" = 2008 AND T1.\"XCL_084\" LIKE '_:%:__.___'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:989"
  ]
}
```

### A query that groups the "races" table by "XCL_066", counts the occurrences of "XCL_067" within each group, orders the results in descending order by t

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_066\" FROM races GROUP BY \"XCL_066\" ORDER BY COUNT(\"XCL_067\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:886"
  ]
}
```

### A query that joins the qualifying and drivers tables to retrieve the XCL_062 value for a specific driver (Lucas di Grassi) in a specific qualifying se

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_062\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 345 AND T2.\"XCL_038\" = 'Lucas' AND T2.\"XCL_039\" = 'di Grassi'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:870"
  ]
}
```

### 1989 Australian GP 4th Place Driver Query

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_038\", T3.\"XCL_039\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T2.\"XCL_078\" = 4 AND T1.\"XCL_069\" = 'Australian Grand Prix' AND T1.\"XCL_066\" = 1989",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:934"
  ]
}
```

### A SQL program that computes the average of 'XCL_030' from 'driverStandings'. It joins 'drivers' (T1) to 'driverStandings' (T2) on 'XCL_034' = 'XCL_029

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T2.\"XCL_030\") FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_029\" = T1.\"XCL_034\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T2.\"XCL_028\" WHERE T1.\"XCL_038\" = 'Eddie' AND T1.\"XCL_039\" = 'Irvine' AND T3.\"XCL_066\" = 2000",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:905"
  ]
}
```

### Full SQL program that joins results and races tables to compute the percentage of non-null XCL_084 values for the 2008 Australian Grand Prix. It filte

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(IIF(NOT T1.\"XCL_084\" IS NULL, 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_073\") FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Australian Grand Prix' AND T2.\"XCL_066\" = 2008",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:943"
  ]
}
```

### Driver Standings Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_029\") FROM driverStandings WHERE \"XCL_028\" = 18",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:966"
  ]
}
```

### 2011 Australian GP Pit Stop Query

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_054\" FROM pitStops AS T1 INNER JOIN races AS T2 ON T1.\"XCL_049\" = T2.\"XCL_065\" WHERE T2.\"XCL_066\" = 2011 AND T2.\"XCL_069\" = 'Australian Grand Prix'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1009"
  ]
}
```

### A query that joins 'driverStandings' and 'drivers' on 'XCL_029' = 'XCL_034', orders the results by 'drivers.XCL_040' in ascending order, and limits th

```json
{
  "kind": "program",
  "formula": "SELECT SUM(T1.\"XCL_033\"), T2.\"XCL_038\", T2.\"XCL_039\" FROM driverStandings AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_029\" = T2.\"XCL_034\" ORDER BY T2.\"XCL_040\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1004"
  ]
}
```

### A full SQL program that joins the drivers, driverStandings, and races tables. It filters for the driver identified by first name 'Lewis' and last name

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T2.\"XCL_030\") FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T2.\"XCL_028\" WHERE T1.\"XCL_038\" = 'Lewis' AND T1.\"XCL_039\" = 'Hamilton' AND T3.\"XCL_069\" = 'Turkish Grand Prix'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:995"
  ]
}
```

### Full SQL program that joins 'constructorStandings' (T1) with 'constructors' (T2) on 'XCL_017' = 'XCL_022', filters for British constructors, and retur

```json
{
  "kind": "program",
  "formula": "SELECT MAX(T1.\"XCL_018\") FROM constructorStandings AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_017\" = T2.\"XCL_022\" WHERE T2.\"XCL_025\" = 'British'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:948"
  ]
}
```

### Full SQL program joining results to races on XCL_074 = XCL_065, filtering for race year 2009 (XCL_066) and results where XCL_084 matches the LIKE patt

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_086\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_066\" = 2009 AND T1.\"XCL_084\" LIKE '_:%:__.___'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:959"
  ]
}
```

### A program that joins the circuits and races tables on the circuit identifier (XCL_001 = XCL_068) and filters for the circuit named 'Shanghai' (XCL_004

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_066\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_004\" = 'Shanghai'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:848"
  ]
}
```

### A query that joins the results table (T1) with the races table (T2) on the condition that T1.XCL_074 equals T2.XCL_065. It filters for rows where T1.X

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_066\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_088\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:974"
  ]
}
```

### Driver-specific result aggregation query

```json
{
  "kind": "program",
  "formula": "SELECT SUM(T2.\"XCL_082\") FROM drivers AS T1 INNER JOIN results AS T2 ON T1.\"XCL_034\" = T2.\"XCL_075\" WHERE T1.\"XCL_038\" = 'Lewis' AND T1.\"XCL_039\" = 'Hamilton'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:941"
  ]
}
```

### A query that identifies distinct circuits (ID and Name) associated with the 'Australian Grand Prix' by joining the circuits table to the races table o

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_006\", T1.\"XCL_007\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Australian Grand Prix'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:854"
  ]
}
```

### Full SQL program that joins races and results tables on XCL_065/XCL_074, filters for the specific race date '1983-07-16', and computes the percentage 

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(CASE WHEN NOT T2.\"XCL_084\" IS NULL THEN T2.\"XCL_075\" END) AS REAL) * 100 / COUNT(T2.\"XCL_075\") FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" WHERE T1.\"XCL_070\" = '1983-07-16'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:881"
  ]
}
```

### A query that filters the 'circuits' table to specific circuits ('Silverstone Circuit', 'Hockenheimring', 'Hungaroring'), orders them by 'XCL_006' in d

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_003\" FROM circuits WHERE \"XCL_003\" IN ('Silverstone Circuit', 'Hockenheimring', 'Hungaroring') ORDER BY \"XCL_006\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:911"
  ]
}
```

### A query that retrieves race identifiers from the 'races' table by joining with 'driverStandings' and 'drivers'. It filters for the driver with first n

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_069\" FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" WHERE T3.\"XCL_038\" = 'Alex' AND T3.\"XCL_039\" = 'Yoong' AND T2.\"XCL_031\" < 20",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:902"
  ]
}
```

### A query returning all race identifiers (XCL_069) from the races table where the date (XCL_070) falls within the same year and month as the minimum dat

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_069\" FROM races WHERE STRFTIME('%Y', \"XCL_070\") = (SELECT STRFTIME('%Y', \"XCL_070\") FROM races ORDER BY \"XCL_070\" ASC LIMIT 1) AND STRFTIME('%m', \"XCL_070\") = (SELECT STRFTIME('%m', \"XCL_070\") FROM races ORDER BY \"XCL_070\" ASC LIMIT 1)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:884"
  ]
}
```

### Full SQL program that joins `drivers` and `results` on `XCL_034` = `XCL_075`, filters for the specific driver 'Lewis Hamilton', and calculates the ave

```json
{
  "kind": "program",
  "formula": "SELECT AVG(CAST(SUBSTRING(T2.\"XCL_088\", 1, INSTR(T2.\"XCL_088\", ':') - 1) AS INTEGER) * 60 + CAST(SUBSTRING(T2.\"XCL_088\", INSTR(T2.\"XCL_088\", ':') + 1) AS REAL)) FROM drivers AS T1 INNER JOIN results AS T2 ON T1.\"XCL_034\" = T2.\"XCL_075\" WHERE T1.\"XCL_039\" = 'Hamilton' AND T1.\"XCL_038\" = 'Lewis'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:942"
  ]
}
```

### Executes an inner join between 'results' (T1) and 'drivers' (T2) on 'XCL_075' = 'XCL_034'. Filters for drivers where 'XCL_041' is 'Italian' and result

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_075\") FROM results AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_075\" = T2.\"XCL_034\" WHERE T2.\"XCL_041\" = 'Italian' AND T1.\"XCL_084\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:957"
  ]
}
```

### 2007 Canadian GP Winner Details

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_038\", T3.\"XCL_039\", T3.\"XCL_035\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T1.\"XCL_069\" = 'Canadian Grand Prix' AND T2.\"XCL_087\" = 1 AND T1.\"XCL_066\" = 2007",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:928"
  ]
}
```

### Query that joins constructors and constructorStandings to identify the top-performing Italian constructor. It filters for nationality 'Italian', order

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_026\" FROM constructors AS T1 INNER JOIN constructorStandings AS T2 ON T1.\"XCL_022\" = T2.\"XCL_017\" WHERE T1.\"XCL_025\" = 'Italian' ORDER BY T2.\"XCL_018\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:983"
  ]
}
```

### Driver Standings for Singapore GP 2010

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_038\", T3.\"XCL_039\" FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_069\" = 'Singapore Grand Prix' AND T1.\"XCL_066\" = 2010 ORDER BY T2.\"XCL_031\" ASC",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:891"
  ]
}
```

### 2009 Race List Query

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_065\" FROM races WHERE \"XCL_066\" = 2009",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:965"
  ]
}
```

### A full SQL program that joins races, lapTimes, and drivers to compute the average lap time. It filters for the driver 'Lewis Hamilton' (first name XCL

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T2.\"XCL_048\") FROM races AS T1 INNER JOIN lapTimes AS T2 ON T2.\"XCL_043\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_044\" WHERE T3.\"XCL_038\" = 'Lewis' AND T3.\"XCL_039\" = 'Hamilton' AND T1.\"XCL_066\" = 2009 AND T1.\"XCL_069\" = 'Malaysian Grand Prix'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:895"
  ]
}
```

### Full SQL program that selects the average of XCL_066 from the races table, filtered by XCL_070 date range '2000-01-01' to '2010-12-31'. The metric is 

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN \"XCL_066\" BETWEEN 2000 AND 2010 THEN 1 ELSE 0 END) AS REAL) / 10 FROM races WHERE \"XCL_070\" BETWEEN '2000-01-01' AND '2010-12-31'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:996"
  ]
}
```

### A query that joins race results to race metadata to calculate the average finishing position for top-10 finishers in a specific race (2006 US GP).

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T1.\"XCL_088\") FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T1.\"XCL_087\" < 11 AND T2.\"XCL_066\" = 2006 AND T2.\"XCL_069\" = 'United States Grand Prix'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:987"
  ]
}
```

### Executes an inner join between circuits and races on the circuit identifier (XCL_001 = XCL_068), filters for circuits in Italy (XCL_005 = 'Italy'), an

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_068\") FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_005\" = 'Italy'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:923"
  ]
}
```

### Retrieves the identifier and name of the driver who achieved a finishing position of 2 in the 2006 San Marino Grand Prix. Joins races, results, and dr

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_038\", T3.\"XCL_039\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T1.\"XCL_066\" = 2006 AND T1.\"XCL_069\" = 'San Marino Grand Prix' AND T2.\"XCL_079\" = 2",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:874"
  ]
}
```

### 2005 Race List Query

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_069\" FROM races WHERE \"XCL_066\" = 2005 ORDER BY \"XCL_069\" DESC",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:883"
  ]
}
```

### Executes an inner join between `drivers` and `results`, filters for the specific driver 'Lewis Hamilton', excludes null values in `results.XCL_088`, s

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_088\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE T1.\"XCL_038\" = 'Lewis' AND T1.\"XCL_039\" = 'Hamilton' AND NOT T2.\"XCL_088\" IS NULL ORDER BY T2.\"XCL_088\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:926"
  ]
}
```

### A SQL program that retrieves the maximum value of XCL_054 from the pitStops table by ordering the results in descending order and limiting the output 

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_054\" FROM pitStops ORDER BY \"XCL_054\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1005"
  ]
}
```

### Full SQL program joining drivers and lapTimes on driver ID, filtering for French drivers and lap times under 120 seconds (parsed from MM:SS.mmm format

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_034\") FROM drivers AS T1 INNER JOIN lapTimes AS T2 ON T1.\"XCL_034\" = T2.\"XCL_044\" WHERE T1.\"XCL_041\" = 'French' AND (CAST(SUBSTRING(T2.\"XCL_047\", 1, 2) AS INTEGER) * 60 + CAST(SUBSTRING(T2.\"XCL_047\", 4, 2) AS INTEGER) + CAST(SUBSTRING(T2.\"XCL_047\", 7, 2) AS REAL) / 1000) < 120",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:963"
  ]
}
```

### A query that joins the qualifying and drivers tables to retrieve a specific qualifying metric (XCL_062) for a named driver in a specific session. It f

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_062\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 354 AND T2.\"XCL_038\" = 'Bruno' AND T2.\"XCL_039\" = 'Senna'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:859"
  ]
}
```

### A program that retrieves the race identifier and driver standing position for Lewis Hamilton's earliest recorded standing, joining races, driverStandi

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_069\", T2.\"XCL_030\" FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" WHERE T3.\"XCL_038\" = 'Lewis' AND T3.\"XCL_039\" = 'Hamilton' ORDER BY T1.\"XCL_066\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:906"
  ]
}
```

### A full SQL program that calculates the number of unique drivers who have a recorded result (non-null XCL_084) in the 2008 Chinese Grand Prix. It joins

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(*) FROM (SELECT T1.\"XCL_075\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Chinese Grand Prix' AND T2.\"XCL_066\" = 2008 AND NOT T1.\"XCL_084\" IS NULL GROUP BY T1.\"XCL_075\" HAVING COUNT(T2.\"XCL_065\") > 0)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:940"
  ]
}
```

### A query that identifies the driver who recorded the first lap (ordered by XCL_047 ascending) in race 348 (XCL_043 = 348) by joining lapTimes and drive

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_038\", T2.\"XCL_039\" FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_044\" WHERE T1.\"XCL_043\" = 348 ORDER BY T1.\"XCL_047\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:878"
  ]
}
```

### Full SQL program that identifies races won by Lewis Hamilton by joining driver identity, result positions, and race details through nested subqueries.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_069\" FROM races WHERE \"XCL_065\" IN (SELECT \"XCL_074\" FROM results WHERE \"XCL_087\" = 1 AND \"XCL_075\" = (SELECT \"XCL_034\" FROM drivers WHERE \"XCL_038\" = 'Lewis' AND \"XCL_039\" = 'Hamilton'))",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:930"
  ]
}
```

### A SQL program that joins lapTimes and drivers on driver ID, filters for the driver with first name 'Lewis' and last name 'Hamilton', orders by the lap

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_046\" FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_044\" = T2.\"XCL_034\" WHERE T2.\"XCL_038\" = 'Lewis' AND T2.\"XCL_039\" = 'Hamilton' ORDER BY T1.\"XCL_047\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1012"
  ]
}
```

### Average pit stop duration for Lewis Hamilton

```json
{
  "kind": "program",
  "formula": "SELECT AVG(\"XCL_055\") FROM pitStops AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_050\" = T2.\"XCL_034\" WHERE T2.\"XCL_038\" = 'Lewis' AND T2.\"XCL_039\" = 'Hamilton'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1018"
  ]
}
```

### 1971 Active Drivers with Results

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_034\", T2.\"XCL_037\" FROM results AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_075\" = T2.\"XCL_034\" WHERE STRFTIME('%Y', T2.\"XCL_040\") = '1971' AND NOT T1.\"XCL_088\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:972"
  ]
}
```

### A query that joins qualifying and drivers tables on XCL_058 = XCL_034, filters qualifying records where XCL_057 equals 19, orders by XCL_063 ascending

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_039\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 19 ORDER BY T1.\"XCL_063\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:847"
  ]
}
```

### Full SQL program that filters the drivers table for records where XCL_041 equals 'British' and the year portion of XCL_040 equals '1980', then counts 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_034\") FROM drivers WHERE \"XCL_041\" = 'British' AND STRFTIME('%Y', \"XCL_040\") = '1980'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:969"
  ]
}
```

### Full SQL program that joins 'races' and 'results' on 'XCL_065' = 'XCL_074', filters for the specific date '2015-11-29' and null 'XCL_084', and returns

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_075\") FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" WHERE T1.\"XCL_070\" = '2015-11-29' AND T2.\"XCL_084\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:876"
  ]
}
```

### A query that retrieves the "XCL_041" value from the "drivers" table where "XCL_040" is not null, ordered by "XCL_040" in ascending order, limited to t

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_041\" FROM drivers WHERE NOT \"XCL_040\" IS NULL ORDER BY \"XCL_040\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:915"
  ]
}
```

### Full SQL program that joins the 'circuits' table (T1) with the 'races' table (T3) on the circuit identifier (T1.XCL_001 = T3.XCL_068). It filters for 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T3.\"XCL_065\") FROM circuits AS T1 INNER JOIN races AS T3 ON T3.\"XCL_068\" = T1.\"XCL_001\" WHERE NOT T1.\"XCL_005\" IN ('Bahrain', 'China', 'Singapore', 'Japan', 'Korea', 'Turkey', 'UAE', 'Malaysia', 'Spain', 'Monaco', 'Azerbaijan', 'Austria', 'Belgium', 'France', 'Germany', 'Hungary', 'Italy', 'UK') AND T3.\"XCL_066\" = 2010",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:852"
  ]
}
```

### Full SQL program joining drivers, results, and status tables. It filters for drivers where XCL_041 is 'American' and status where XCL_094 is 'Puncture

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_034\") FROM drivers AS T1 INNER JOIN results AS T2 ON T1.\"XCL_034\" = T2.\"XCL_075\" INNER JOIN status AS T3 ON T2.\"XCL_090\" = T3.\"XCL_093\" WHERE T3.\"XCL_094\" = 'Puncture' AND T1.\"XCL_041\" = 'American'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:982"
  ]
}
```

### A query that identifies the race (ID and Date) corresponding to the minimum lap time value for a specific driver. It joins races, lapTimes, and driver

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_069\", T1.\"XCL_066\" FROM races AS T1 INNER JOIN lapTimes AS T2 ON T2.\"XCL_043\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_044\" WHERE T3.\"XCL_038\" = 'Michael' AND T3.\"XCL_039\" = 'Schumacher' ORDER BY T2.\"XCL_048\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:904"
  ]
}
```

### Full SQL program that joins races, driverStandings, and drivers to compute the percentage of non-first-place finishes for driver 'Hamilton' in races f

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(CASE WHEN T2.\"XCL_031\" <> 1 THEN T2.\"XCL_031\" END) AS REAL) * 100 / COUNT(T2.\"XCL_027\") FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" WHERE T3.\"XCL_039\" = 'Hamilton' AND T1.\"XCL_066\" >= 2010",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:896"
  ]
}
```

### A query that identifies the single driver (defined by XCL_038, XCL_039, XCL_041) with the highest count of standing records (XCL_033) where the value 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_041\", MAX(T2.\"XCL_030\") FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_029\" = T1.\"XCL_034\" WHERE T2.\"XCL_033\" >= 1 GROUP BY T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_041\" ORDER BY COUNT(T2.\"XCL_033\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:897"
  ]
}
```

### A query that joins drivers and results tables to retrieve a specific result attribute (XCL_084) for a driver named Bruce McLaren in race 743.

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_084\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE T2.\"XCL_074\" = 743 AND T1.\"XCL_038\" = 'Bruce' AND T1.\"XCL_039\" = 'McLaren'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:873"
  ]
}
```

### A query that joins qualifying and drivers tables to find driver identifiers for a specific qualifying session (ID 45) where the recorded time matches 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_037\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 45 AND T1.\"XCL_064\" LIKE '1:33%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:872"
  ]
}
```

### Query for percentage of specific driver/result conditions in 2000-2005 races

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(IIF(STRFTIME('%Y', T3.\"XCL_040\") < '1985' AND T1.\"XCL_083\" > 50, 1, 0)) AS REAL) * 100 / COUNT(*) FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN drivers AS T3 ON T1.\"XCL_075\" = T3.\"XCL_034\" WHERE T2.\"XCL_066\" BETWEEN 2000 AND 2005",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:962"
  ]
}
```

### Full SQL program that joins drivers, driverStandings, races, and circuits to calculate the sum of driverStandings.XCL_033. It filters for Michael Schu

```json
{
  "kind": "program",
  "formula": "SELECT SUM(T2.\"XCL_033\") FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_029\" = T1.\"XCL_034\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T2.\"XCL_028\" INNER JOIN circuits AS T4 ON T4.\"XCL_001\" = T3.\"XCL_068\" WHERE T1.\"XCL_038\" = 'Michael' AND T1.\"XCL_039\" = 'Schumacher' AND T4.\"XCL_003\" = 'Sepang International Circuit'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:903"
  ]
}
```

### A query that retrieves the first 5 values of XCL_044 from the lapTimes table, restricted to records where XCL_045 is 1, and sorted in ascending order 

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_044\" FROM lapTimes WHERE \"XCL_045\" = 1 ORDER BY \"XCL_047\" LIMIT 5",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:976"
  ]
}
```

### Selects columns XCL_006 and XCL_007 from the circuits table, filtered to rows where XCL_005 equals 'USA'. Returns one row per matching circuit.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_006\", \"XCL_007\" FROM circuits WHERE \"XCL_005\" = 'USA'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:946"
  ]
}
```

### A query that retrieves the circuit identifier (XCL_009) from the 'circuits' table where the circuit name (XCL_003) is 'Sepang International Circuit'. 

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_009\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Sepang International Circuit'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:855"
  ]
}
```

### Query that retrieves the unique set of race identifiers associated with the 'Silverstone Circuit' by joining the circuits and races tables on the circ

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_066\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Silverstone Circuit'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:920"
  ]
}
```

### Hungaroring Circuit Details Query

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_005\", \"XCL_006\", \"XCL_007\" FROM circuits WHERE \"XCL_003\" = 'Hungaroring'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:993"
  ]
}
```

### A query that retrieves the unique identifier for a specific circuit by joining the circuits and races tables, ensuring the circuit has associated race

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_009\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Circuit de Barcelona-Catalunya'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:849"
  ]
}
```

### A query that retrieves distinct race identifiers, circuit names, and circuit locations for races held in September 2005. It joins the races table with

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_069\", T1.\"XCL_003\", T1.\"XCL_004\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_066\" = 2005 AND STRFTIME('%m', T2.\"XCL_070\") = '09'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:901"
  ]
}
```

### 2010 Abu Dhabi Grand Prix Details

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_070\", T2.\"XCL_071\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_066\" = 2010 AND T2.\"XCL_069\" = 'Abu Dhabi Grand Prix'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:922"
  ]
}
```

### A query that identifies the circuit(s) where a specific lap time ('1:29.488') was achieved. It joins lapTimes to races and then to circuits, filtering

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_006\", T3.\"XCL_007\" FROM lapTimes AS T1 INNER JOIN races AS T2 ON T1.\"XCL_043\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T1.\"XCL_047\" = '1:29.488'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1017"
  ]
}
```

### A query that joins constructorResults and constructors to retrieve the constructor identifier for the first-place finisher in race 24.

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_025\" FROM constructorResults AS T1 INNER JOIN constructors AS T2 ON T2.\"XCL_022\" = T1.\"XCL_012\" WHERE T1.\"XCL_011\" = 24 AND T1.\"XCL_013\" = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:858"
  ]
}
```

### Latest Driver Race Record

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_041\", T3.\"XCL_069\" FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" INNER JOIN races AS T3 ON T2.\"XCL_028\" = T3.\"XCL_065\" ORDER BY JULIANDAY(T1.\"XCL_040\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1002"
  ]
}
```

### A query that retrieves distinct circuit identifiers and names from the 'circuits' table by joining with the 'races' table on the circuit ID (XCL_001/X

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_006\", T1.\"XCL_007\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Abu Dhabi Grand Prix'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:857"
  ]
}
```

### Full SQL program joining races, results, and drivers to count drivers linked to results with a null XCL_084 value for the 2007 Bahrain Grand Prix.

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T3.\"XCL_034\") FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T1.\"XCL_066\" = 2007 AND T1.\"XCL_069\" = 'Bahrain Grand Prix' AND T2.\"XCL_084\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:862"
  ]
}
```

### A query that joins 'constructorResults' (T1) with 'constructors' (T2) on 'XCL_022' = 'XCL_012'. It filters for results where 'XCL_011' is 9, orders by

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_026\" FROM constructorResults AS T1 INNER JOIN constructors AS T2 ON T2.\"XCL_022\" = T1.\"XCL_012\" WHERE T1.\"XCL_011\" = 9 ORDER BY T1.\"XCL_013\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:869"
  ]
}
```

### A query that joins races, driverStandings, and drivers tables to retrieve the first name, last name, and points of the top 3 drivers for the 2017 Chin

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_038\", T3.\"XCL_039\", T2.\"XCL_030\" FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_069\" = 'Chinese Grand Prix' AND T1.\"XCL_066\" = 2017 ORDER BY T2.\"XCL_030\" DESC LIMIT 3",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:893"
  ]
}
```

### Austrian Drivers 1981-1991 Query

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_038\", \"XCL_039\", \"XCL_040\" FROM drivers WHERE \"XCL_041\" = 'Austrian' AND STRFTIME('%Y', \"XCL_040\") BETWEEN '1981' AND '1991'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:991"
  ]
}
```

### A query that retrieves the 'XCL_005' value from the 'circuits' table, ordered by 'XCL_008' in descending order, limited to the first result. Used to i

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_005\" FROM circuits ORDER BY \"XCL_008\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:913"
  ]
}
```

### Full SQL program that joins circuits (T1) and races (T2) on the circuit identifier (XCL_001 = XCL_068), filters for the 'European Grand Prix', and com

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(CASE WHEN T1.\"XCL_005\" = 'Germany' THEN T2.\"XCL_068\" END) AS REAL) * 100 / COUNT(T2.\"XCL_068\") FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_069\" = 'European Grand Prix'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:909"
  ]
}
```

### Executes a join between 'races' (T1) and 'results' (T2) on 'XCL_065' and 'XCL_074'. Filters for the race date '2015-11-29' and ensures 'XCL_084' is no

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_075\") FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" WHERE T1.\"XCL_070\" = '2015-11-29' AND NOT T2.\"XCL_084\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:864"
  ]
}
```

### A query that retrieves the unique identifier(s) for 'Silverstone Circuit' by joining the circuits table with the races table on the circuit key (XCL_0

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_009\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Silverstone Circuit'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:921"
  ]
}
```

### A query that joins circuits and races tables on XCL_001 = XCL_068, orders the results by races.XCL_070 in descending order, and returns the XCL_004 va

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_004\" FROM circuits AS T1 INNER JOIN races AS T2 ON T1.\"XCL_001\" = T2.\"XCL_068\" ORDER BY T2.\"XCL_070\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1000"
  ]
}
```

### A query that identifies distinct circuits (ID and Name) by joining the circuits table to the races table on the circuit reference (XCL_068 = XCL_001) 

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_006\", T1.\"XCL_007\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Malaysian Grand Prix'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:868"
  ]
}
```

### A query that retrieves the identifier ("XCL_035") for the driver with first name 'Lewis' ("XCL_038") and last name 'Hamilton' ("XCL_039") from the dri

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_035\" FROM drivers WHERE \"XCL_038\" = 'Lewis' AND \"XCL_039\" = 'Hamilton'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:918"
  ]
}
```

### A query that identifies a single driver from the drivers table. It joins drivers to results on XCL_034 = XCL_075, filters for race ID 592 (XCL_074), r

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_038\", T1.\"XCL_039\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE T2.\"XCL_074\" = 592 AND NOT T2.\"XCL_084\" IS NULL AND NOT T1.\"XCL_040\" IS NULL ORDER BY T1.\"XCL_040\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:865"
  ]
}
```

### 2009 Spanish GP Average XCL_089 Query

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T1.\"XCL_089\") FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_066\" = 2009 AND T2.\"XCL_069\" = 'Spanish Grand Prix'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:960"
  ]
}
```

### Retrieves circuit names, locations, and race names for all races that took place in the USA during the year 2006. Joins circuits and races on circuit 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_003\", T1.\"XCL_004\", T2.\"XCL_069\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_005\" = 'USA' AND T2.\"XCL_066\" = 2006",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:900"
  ]
}
```

### A query that identifies the single constructor with the highest total XCL_013 score at the Monaco Grand Prix between 1980 and 2010. It joins construct

```json
{
  "kind": "program",
  "formula": "SELECT SUM(T1.\"XCL_013\"), T2.\"XCL_024\", T2.\"XCL_025\" FROM constructorResults AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_012\" = T2.\"XCL_022\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T1.\"XCL_011\" WHERE T3.\"XCL_069\" = 'Monaco Grand Prix' AND T3.\"XCL_066\" BETWEEN 1980 AND 2010 GROUP BY T2.\"XCL_024\" ORDER BY SUM(T1.\"XCL_013\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:994"
  ]
}
```

### Full program that joins results, races, and status tables to identify the driver with the most results in the Canadian Grand Prix filtered by status c

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_075\") FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN status AS T3 ON T1.\"XCL_090\" = T3.\"XCL_093\" WHERE T3.\"XCL_093\" = 3 AND T2.\"XCL_069\" = 'Canadian Grand Prix' GROUP BY T1.\"XCL_075\" ORDER BY COUNT(T1.\"XCL_075\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1003"
  ]
}
```

### Drivers with Specific Lap Time Prefix in Race 161

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_038\", T2.\"XCL_039\", T2.\"XCL_042\" FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_044\" WHERE T1.\"XCL_043\" = 161 AND T1.\"XCL_047\" LIKE '1:27%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:866"
  ]
}
```

### A program that calculates the average time in seconds for winning/champion results (XCL_081 = 1) for each year prior to 1975. It joins results to race

```json
{
  "kind": "program",
  "formula": "WITH time_in_seconds AS (SELECT T2.\"XCL_066\", T2.\"XCL_065\", T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(T1.\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_084\" IS NULL), champion_time AS (SELECT \"XCL_066\", \"XCL_065\", \"time_seconds\" FROM time_in_seconds WHERE \"XCL_081\" = 1) SELECT \"XCL_066\", AVG(\"time_seconds\") FROM champion_time WHERE \"XCL_066\" < 1975 GROUP BY \"XCL_066\" HAVING NOT AVG(\"time_seconds\") IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:955"
  ]
}
```

### Filtered Driver Qualifying Lookup

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_035\", T2.\"XCL_041\", T2.\"XCL_040\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_058\" = T2.\"XCL_034\" WHERE T1.\"XCL_057\" = 23 AND NOT T1.\"XCL_063\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:980"
  ]
}
```

### A query that joins drivers, lapTimes, and races to retrieve the driver attributes (XCL_038, XCL_039) and race attribute (XCL_069) corresponding to the

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_048\", T1.\"XCL_038\", T1.\"XCL_039\", T3.\"XCL_069\" FROM drivers AS T1 INNER JOIN lapTimes AS T2 ON T1.\"XCL_034\" = T2.\"XCL_044\" INNER JOIN races AS T3 ON T2.\"XCL_043\" = T3.\"XCL_065\" ORDER BY T2.\"XCL_048\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:894"
  ]
}
```

### A full program that joins the 'circuits' and 'races' tables to identify the most recent 'British Grand Prix' held at 'Brands Hatch'. It filters by cir

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_070\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Brands Hatch' AND T2.\"XCL_069\" = 'British Grand Prix' ORDER BY T2.\"XCL_066\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:889"
  ]
}
```

### A query that joins pitStops and drivers to find the single longest pit stop duration (XCL_054) for the driver identified by first name 'Lewis' and las

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_054\" FROM pitStops AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_050\" = T2.\"XCL_034\" WHERE T2.\"XCL_038\" = 'Lewis' AND T2.\"XCL_039\" = 'Hamilton' ORDER BY T1.\"XCL_054\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1007"
  ]
}
```

### A query that joins "lapTimes" and "races" on the race key ("XCL_043" = "XCL_065"), orders the results by the lap time metric ("XCL_047") in descending

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_066\" FROM lapTimes AS T1 INNER JOIN races AS T2 ON T1.\"XCL_043\" = T2.\"XCL_065\" ORDER BY T1.\"XCL_047\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:975"
  ]
}
```

### Driver count difference query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_034\") - COUNT(CASE WHEN NOT \"XCL_037\" IS NULL THEN \"XCL_037\" END) FROM drivers",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:914"
  ]
}
```

### Full SQL program that joins lapTimes, races, and circuits to calculate the average of lapTimes.XCL_048 for races at Italian circuits. It uses inner jo

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(T1.\"XCL_048\") AS REAL) / COUNT(T1.\"XCL_045\") FROM lapTimes AS T1 INNER JOIN races AS T2 ON T1.\"XCL_043\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T3.\"XCL_005\" = 'Italy'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1019"
  ]
}
```

### Full SQL program that joins drivers (T1), results (T2), and races (T3) to count results where the race name is 'Australian Grand Prix', the year is 20

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(*) FROM drivers AS T1 INNER JOIN results AS T2 ON T1.\"XCL_034\" = T2.\"XCL_075\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T2.\"XCL_074\" WHERE T3.\"XCL_069\" = 'Australian Grand Prix' AND T1.\"XCL_041\" = 'British' AND T3.\"XCL_066\" = 2008",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:939"
  ]
}
```

### First Non-Null Result with Driver Details

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_038\", T2.\"XCL_039\", T1.\"XCL_088\" FROM results AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_075\" = T2.\"XCL_034\" WHERE NOT T1.\"XCL_088\" IS NULL ORDER BY T1.\"XCL_088\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:958"
  ]
}
```

### 2008 Australian GP Finishers Query

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_042\" FROM drivers AS T1 INNER JOIN results AS T2 ON T1.\"XCL_034\" = T2.\"XCL_075\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T2.\"XCL_074\" WHERE T3.\"XCL_069\" = 'Australian Grand Prix' AND T2.\"XCL_084\" LIKE '_:%:__.___' AND T3.\"XCL_066\" = 2008",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:938"
  ]
}
```

### A query that joins qualifying and drivers tables to retrieve driver identifiers for a specific qualifying session (903) filtered by a time prefix ('1:

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_036\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 903 AND T1.\"XCL_064\" LIKE '1:54%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:861"
  ]
}
```

### A query that retrieves the identifier and name of the single driver with the highest score (XCL_040) for a specific event (XCL_074 = 872). It joins th

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_038\", T1.\"XCL_039\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE T2.\"XCL_074\" = 872 AND NOT T2.\"XCL_084\" IS NULL ORDER BY T1.\"XCL_040\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:877"
  ]
}
```

### 2017 Races Not in 2000

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_069\" FROM races WHERE \"XCL_066\" = 2017 AND NOT \"XCL_069\" IN (SELECT \"XCL_069\" FROM races WHERE \"XCL_066\" = 2000)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:887"
  ]
}
```

### A query that joins 'constructors' and 'constructorStandings' on 'XCL_022' and 'XCL_017', orders the results by 'XCL_021' in descending order, and limi

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_026\" FROM constructors AS T1 INNER JOIN constructorStandings AS T2 ON T1.\"XCL_022\" = T2.\"XCL_017\" ORDER BY T2.\"XCL_021\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:984"
  ]
}
```

### Austrian Circuit Attributes Query

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_004\", \"XCL_006\", \"XCL_007\" FROM circuits WHERE \"XCL_005\" = 'Austria'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:978"
  ]
}
```

### Circuit-Race Join Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_068\") FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Silverstone Circuit' AND T2.\"XCL_069\" = 'British Grand Prix'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:890"
  ]
}
```

### Circuit ID Lookup

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_002\" FROM circuits WHERE \"XCL_003\" = 'Marina Bay Street Circuit'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:912"
  ]
}
```

### Full program that calculates the minimum lap time in seconds for each driver, joins with driver details, and returns the top 20 drivers with the faste

```json
{
  "kind": "program",
  "formula": "WITH lap_times_in_seconds AS (SELECT \"XCL_044\", (CASE WHEN SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) AS REAL) * 60 ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) AS REAL) ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) AS REAL) / 1000 ELSE 0 END) AS time_in_seconds FROM lapTimes) SELECT T2.\"XCL_038\", T2.\"XCL_039\", T1.\"XCL_044\" FROM (SELECT \"XCL_044\", MIN(\"time_in_seconds\") AS min_time_in_seconds FROM lap_times_in_seconds GROUP BY \"XCL_044\") AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_044\" = T2.\"XCL_034\" ORDER BY T1.\"min_time_in_seconds\" ASC LIMIT 20",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1011"
  ]
}
```

### Executes a count of non-null XCL_084 values from the 'results' table, restricted to rows where XCL_090 equals 2 and XCL_074 is strictly between 50 and

```json
{
  "kind": "program",
  "formula": "SELECT SUM(IIF(NOT \"XCL_084\" IS NULL, 1, 0)) FROM results WHERE \"XCL_090\" = 2 AND \"XCL_074\" < 100 AND \"XCL_074\" > 50",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:977"
  ]
}
```

### A program that joins qualifying and drivers tables to retrieve the top 5 drivers based on descending order of "XCL_062" for qualifying records where "

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_035\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 20 ORDER BY T1.\"XCL_062\" DESC LIMIT 5",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:846"
  ]
}
```

### A query that retrieves the top driver (limited to 1 row) based on a descending sort of results.XCL_089. It joins drivers and results on drivers.XCL_03

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_038\", T1.\"XCL_039\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE NOT T2.\"XCL_088\" IS NULL ORDER BY T2.\"XCL_089\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:927"
  ]
}
```

### A query that retrieves the "XCL_035" value for the driver in the drivers table where "XCL_041" is 'German', ordered by the Julian day of "XCL_040" in 

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_035\" FROM drivers WHERE \"XCL_041\" = 'German' ORDER BY JULIANDAY(\"XCL_040\") ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:971"
  ]
}
```

### Full SQL program that joins results, races, and drivers to compute the percentage of non-null XCL_084 values. It filters for drivers with nationality 

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(IIF(NOT T1.\"XCL_084\" IS NULL, 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_074\") FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN drivers AS T3 ON T1.\"XCL_075\" = T3.\"XCL_034\" WHERE T3.\"XCL_041\" = 'Japanese' AND T2.\"XCL_066\" BETWEEN 2007 AND 2009",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:954"
  ]
}
```

### Fastest Qualifier at Marina Bay 2008

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_038\", T2.\"XCL_039\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_058\" = T2.\"XCL_034\" INNER JOIN races AS T3 ON T1.\"XCL_057\" = T3.\"XCL_065\" WHERE NOT \"XCL_064\" IS NULL AND T3.\"XCL_066\" = 2008 AND T3.\"XCL_068\" IN (SELECT \"XCL_001\" FROM circuits WHERE \"XCL_003\" = 'Marina Bay Street Circuit') ORDER BY CAST(SUBSTRING(\"XCL_064\", 1, INSTR(\"XCL_064\", ':') - 1) AS INTEGER) * 60 + CAST(SUBSTRING(\"XCL_064\", INSTR(\"XCL_064\", ':') + 1, INSTR(\"XCL_064\", '.') - INSTR(\"XCL_064\", ':') - 1) AS REAL) + CAST(SUBSTRING(\"XCL_064\", INSTR(\"XCL_064\", '.') + 1) AS REAL) / 1000 ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1001"
  ]
}
```

### A query that retrieves the "XCL_037" value for all rows in the drivers table where the "XCL_041" column equals 'American'. The grain is individual dri

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_037\" FROM drivers WHERE \"XCL_041\" = 'American'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:964"
  ]
}
```

### A full SQL program that retrieves a single lap time identifier. It joins lapTimes to races on XCL_043 = XCL_065, filters for XCL_045 = 1, orders by XC

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_048\" FROM lapTimes AS T1 INNER JOIN races AS T2 ON T1.\"XCL_043\" = T2.\"XCL_065\" WHERE T1.\"XCL_045\" = 1 ORDER BY T1.\"XCL_047\" LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:986"
  ]
}
```

### A query that joins drivers and results tables on XCL_034 = XCL_075. It filters results where XCL_074 equals 933 and XCL_088 is not null, orders by XCL

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_041\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE T2.\"XCL_074\" = 933 AND NOT T2.\"XCL_088\" IS NULL ORDER BY T2.\"XCL_089\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:867"
  ]
}
```

### A query that retrieves the XCL_069 and XCL_070 values for the single race in the races table where XCL_066 equals 1999, ordered by XCL_067 in descendi

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_069\", \"XCL_070\" FROM races WHERE \"XCL_066\" = 1999 ORDER BY \"XCL_067\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:885"
  ]
}
```

### A program that counts the number of Dutch drivers among the 3 most recent drivers ordered by the date field XCL_040 in descending order.

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(*) FROM (SELECT T1.\"XCL_041\" FROM drivers AS T1 ORDER BY JULIANDAY(T1.\"XCL_040\") DESC LIMIT 3) AS T3 WHERE T3.\"XCL_041\" = 'Dutch'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:967"
  ]
}
```

### Retrieves the race identifier and attribute for the race linked to the result with the lowest non-null value in XCL_085. Joins races and results on XC

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_069\", T1.\"XCL_066\" FROM races AS T1 INNER JOIN results AS T2 ON T1.\"XCL_065\" = T2.\"XCL_074\" WHERE NOT T2.\"XCL_085\" IS NULL ORDER BY T2.\"XCL_085\" LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:961"
  ]
}
```

### Full SQL program that groups the results table by XCL_074, orders groups by the descending count of non-null XCL_084 values, and returns the single to

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_074\" FROM results GROUP BY \"XCL_074\" ORDER BY COUNT(NOT \"XCL_084\" IS NULL) DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:979"
  ]
}
```

### A program that joins races, driverStandings, and drivers tables to identify the driver with the highest standing value. It links races to driverStandi

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_038\", T3.\"XCL_039\", T2.\"XCL_030\" FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" ORDER BY T2.\"XCL_030\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:892"
  ]
}
```

### A query that joins races and results on XCL_065 = XCL_074, filters for non-null values in results.XCL_088, orders by results.XCL_088 ascending, and re

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_069\" FROM races AS T1 INNER JOIN results AS T2 ON T1.\"XCL_065\" = T2.\"XCL_074\" WHERE NOT T2.\"XCL_088\" IS NULL ORDER BY T2.\"XCL_088\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:999"
  ]
}
```

### Full SQL program selecting specific driver attributes from the drivers table where the nationality is 'German' and the year of the date field XCL_040 

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_038\", \"XCL_039\", \"XCL_042\", \"XCL_040\" FROM drivers WHERE \"XCL_041\" = 'German' AND STRFTIME('%Y', \"XCL_040\") BETWEEN '1971' AND '1985' ORDER BY \"XCL_040\" DESC",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:992"
  ]
}
```

### A program that joins the circuits and races tables on the circuit identifier (XCL_001 = XCL_068) and filters for the specific circuit 'Circuit de Barc

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_070\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Circuit de Barcelona-Catalunya'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:924"
  ]
}
```

### A query that joins results, races, and drivers to retrieve the XCL_086 value for Lewis Hamilton's participation in the 2008 Australian Grand Prix.

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_086\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN drivers AS T3 ON T1.\"XCL_075\" = T3.\"XCL_034\" WHERE T2.\"XCL_069\" = 'Australian Grand Prix' AND T2.\"XCL_066\" = 2008 AND T3.\"XCL_038\" = 'Lewis' AND T3.\"XCL_039\" = 'Hamilton'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:936"
  ]
}
```

### Full SQL program that joins the 'results' table (T1) with the 'constructors' table (T2) on XCL_076 = XCL_022. It filters for results where XCL_083 > 5

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T2.\"XCL_022\") FROM results AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_076\" = T2.\"XCL_022\" WHERE T1.\"XCL_083\" > 50 AND T2.\"XCL_025\" = 'French'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:953"
  ]
}
```

### Executes an inner join between 'races' and 'results' on 'XCL_065' and 'XCL_074'. Filters for the 'Australian Grand Prix' in 2008 and excludes rows whe

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_075\") FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" WHERE T1.\"XCL_069\" = 'Australian Grand Prix' AND T1.\"XCL_066\" = 2008 AND NOT T2.\"XCL_084\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:935"
  ]
}
```

### A complete SQL program that calculates the fastest lap record for the Austrian Grand Prix. It filters results to non-null lap times, joins with races 

```json
{
  "kind": "program",
  "formula": "WITH fastest_lap_times AS (SELECT T1.\"XCL_074\", T1.\"XCL_088\" FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL) SELECT MIN(fastest_lap_times.\"XCL_088\") AS lap_record FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1013"
  ]
}
```

### A query that joins pitStops and drivers to identify the top 10 Spanish drivers born before 1982, ordered by the descending value of the pit stop times

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_034\" FROM pitStops AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_050\" = T2.\"XCL_034\" WHERE T2.\"XCL_041\" = 'Spanish' AND STRFTIME('%Y', T2.\"XCL_040\") < '1982' ORDER BY T1.\"XCL_053\" DESC LIMIT 10",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:973"
  ]
}
```

### A query that retrieves the distinct race identifiers for a specific driver by joining the races, results, and drivers tables. It filters for the drive

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_066\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T3.\"XCL_038\" = 'Lewis' AND T3.\"XCL_039\" = 'Hamilton'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:932"
  ]
}
```

### A query that identifies the lap with the shortest duration by parsing the string format of XCL_047 (handling optional hours, minutes, seconds, and mil

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_047\" FROM lapTimes ORDER BY (CASE WHEN INSTR(\"XCL_047\", ':') <> INSTR(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1), ':') + INSTR(\"XCL_047\", ':') THEN CAST(SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) AS REAL) * 3600 ELSE 0 END) + (CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') - 2 * (INSTR(\"XCL_047\", ':') = INSTR(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1), ':') + INSTR(\"XCL_047\", ':')), INSTR(\"XCL_047\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) AS REAL) / 1000) ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1006"
  ]
}
```

### Austrian GP Fastest Lap Pit Stops

```json
{
  "kind": "program",
  "formula": "WITH fastest_lap_times AS (SELECT T1.\"XCL_074\", T1.\"XCL_075\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL), lap_record_race AS (SELECT T1.\"XCL_074\", T1.\"XCL_075\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" INNER JOIN (SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix') AS T4 ON (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) = T4.\"min_time_in_seconds\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix') SELECT T4.\"XCL_054\" FROM lap_record_race INNER JOIN pitStops AS T4 ON lap_record_race.\"XCL_074\" = T4.\"XCL_049\" AND lap_record_race.\"XCL_075\" = T4.\"XCL_050\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1016"
  ]
}
```

### 2009 Singapore GP Constructor Lookup

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_023\", T3.\"XCL_026\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN constructors AS T3 ON T1.\"XCL_076\" = T3.\"XCL_022\" WHERE T2.\"XCL_069\" = 'Singapore Grand Prix' AND T2.\"XCL_066\" = 2009 AND T1.\"XCL_084\" LIKE '_:%:__.___'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:990"
  ]
}
```

### A SQL program that groups the "drivers" table by "XCL_041", orders the groups by the descending count of "XCL_034", and returns the first row (LIMIT 1

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_041\" FROM drivers GROUP BY \"XCL_041\" ORDER BY COUNT(\"XCL_034\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:997"
  ]
}
```

### Identifies the top 3 German drivers between 1980 and 1985 based on the average duration of their pit stops. Joins pitStops and drivers, filters by nat

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_038\", T2.\"XCL_039\" FROM pitStops AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_050\" = T2.\"XCL_034\" WHERE T2.\"XCL_041\" = 'German' AND STRFTIME('%Y', T2.\"XCL_040\") BETWEEN '1980' AND '1985' GROUP BY T2.\"XCL_038\", T2.\"XCL_039\" ORDER BY AVG(T1.\"XCL_054\") LIMIT 3",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:988"
  ]
}
```

### A SQL program that joins constructorStandings (T1) with constructors (T2) on T1."XCL_017" = T2."XCL_022". It filters for Japanese constructors (T2."XC

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_016\") FROM constructorStandings AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_017\" = T2.\"XCL_022\" WHERE T1.\"XCL_018\" = 0 AND T2.\"XCL_025\" = 'Japanese' GROUP BY T1.\"XCL_017\" HAVING COUNT(\"XCL_016\") = 2",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:951"
  ]
}
```

### A query that identifies the circuit details (ID and Name) for the first occurrence of the 'European Grand Prix' race, ordered by the race date/sequenc

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_005\", T1.\"XCL_004\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_069\" = 'European Grand Prix' ORDER BY T2.\"XCL_066\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:888"
  ]
}
```

### A query that retrieves the "XCL_035" value from the drivers table for the driver with first name 'Robert' and last name 'Kubica'. The grain is a singl

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_035\" FROM drivers WHERE \"XCL_038\" = 'Robert' AND \"XCL_039\" = 'Kubica'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:968"
  ]
}
```

### A query that joins the results table to the constructors table on the constructor reference (XCL_076 to XCL_022), filters for results where XCL_087 is

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_024\" FROM results AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_076\" = T2.\"XCL_022\" WHERE T1.\"XCL_087\" = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:952"
  ]
}
```

### Full query program that filters the 'drivers' table for records where 'XCL_041' is 'Japanese', orders by 'XCL_040' in descending order, and limits the

```json
{
  "kind": "program",
  "formula": "SELECT STRFTIME('%Y', CURRENT_TIMESTAMP) - STRFTIME('%Y', \"XCL_040\"), \"XCL_038\", \"XCL_039\" FROM drivers WHERE \"XCL_041\" = 'Japanese' ORDER BY \"XCL_040\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:898"
  ]
}
```

### A program that joins pitStops and drivers tables to retrieve driver identifiers for German drivers born between 1980 and 1990, ordered by pit stop att

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_034\" FROM pitStops AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_050\" = T2.\"XCL_034\" WHERE T2.\"XCL_041\" = 'German' AND STRFTIME('%Y', T2.\"XCL_040\") BETWEEN '1980' AND '1990' ORDER BY T1.\"XCL_053\" LIMIT 3",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:970"
  ]
}
```

### A query that joins `constructorStandings` and `constructors` to identify the constructor with the maximum value in `XCL_018`. It orders the results by

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_024\" FROM constructorStandings AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_017\" = T2.\"XCL_022\" ORDER BY T1.\"XCL_018\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:949"
  ]
}
```

### A query that retrieves the "XCL_039" values for all rows in the "drivers" table where the "XCL_041" column equals 'Italian'.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_039\" FROM drivers WHERE \"XCL_041\" = 'Italian'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:916"
  ]
}
```

### Filtered Driver Attributes Query

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_038\", T2.\"XCL_039\" FROM results AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_075\" = T2.\"XCL_034\" WHERE STRFTIME('%Y', T2.\"XCL_040\") > '1975' AND T1.\"XCL_087\" = 2",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:956"
  ]
}
```

### A program that identifies the race name associated with the result holding the minimum fastest lap time for the Austrian Grand Prix. It joins results,

```json
{
  "kind": "program",
  "formula": "WITH fastest_lap_times AS (SELECT T1.\"XCL_074\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL) SELECT T2.\"XCL_069\" FROM races AS T2 INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" INNER JOIN results AS T1 ON T2.\"XCL_065\" = T1.\"XCL_074\" INNER JOIN (SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix') AS T4 ON (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) = T4.\"min_time_in_seconds\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1015"
  ]
}
```

### Driver Standings Conditional Aggregation Query

```json
{
  "kind": "program",
  "formula": "SELECT SUM(CASE WHEN \"XCL_030\" = 91 THEN \"XCL_033\" ELSE 0 END) FROM driverStandings",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:998"
  ]
}
```

### A complete SQL program that identifies the fastest lap time recorded at any circuit in Italy. It uses a CTE to convert raw lap time strings to seconds

```json
{
  "kind": "program",
  "formula": "WITH fastest_lap_times AS (SELECT T1.\"XCL_074\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL) SELECT T1.\"XCL_088\" AS lap_record FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" INNER JOIN (SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T3.\"XCL_005\" = 'Italy') AS T4 ON (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) = T4.\"min_time_in_seconds\" LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1014"
  ]
}
```

### Driver Attribute XCL_039

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_038\", \"XCL_039\", \"XCL_042\", \"XCL_040\" FROM drivers WHERE \"XCL_041\" = 'German' AND STRFTIME('%Y', \"XCL_040\") BETWEEN '1971' AND '1985' ORDER BY \"XCL_040\" DESC",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_039\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_039\" AS \"value\" FROM drivers AS \"r0\" WHERE \"r0\".\"XCL_041\" = 'German' AND STRFTIME('%Y', \"r0\".\"XCL_040\") BETWEEN '1971' AND '1985'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:992"
  ]
}
```

### Circuit Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"circuits\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM circuits WHERE \"XCL_004\" = 'Adelaide' AND \"XCL_005\" = 'Australia'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM circuits AS \"r0\" WHERE \"r0\".\"XCL_004\" = 'Adelaide' AND \"r0\".\"XCL_005\" = 'Australia'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:945"
  ]
}
```

### "constructorResults"."XCL_011" = 24 AND "constructorResults"."XCL_013" = 1

```json
{
  "kind": "predicate",
  "formula": "\"constructorResults\".\"XCL_011\" = 24 AND \"constructorResults\".\"XCL_013\" = 1",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_025\" FROM constructorResults AS T1 INNER JOIN constructors AS T2 ON T2.\"XCL_022\" = T1.\"XCL_012\" WHERE T1.\"XCL_011\" = 24 AND T1.\"XCL_013\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:858"
  ]
}
```

### Date attribute for the driver (drivers.XCL_041) associated with the most recent race event. Note: The ordering is performed on drivers.XCL_040, which 

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_041\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_041\", T3.\"XCL_069\" FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" INNER JOIN races AS T3 ON T2.\"XCL_028\" = T3.\"XCL_065\" ORDER BY JULIANDAY(T1.\"XCL_040\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1002"
  ]
}
```

### Constructor Standings Identifier

```json
{
  "kind": "binding",
  "formula": "\"constructorStandings\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_019\" FROM constructorStandings AS T1 INNER JOIN constructors AS T2 ON T2.\"XCL_022\" = T1.\"XCL_017\" WHERE T2.\"XCL_024\" = 'Renault'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:851"
  ]
}
```

### Last Driver Time Value

```json
{
  "kind": "binding",
  "formula": "CASE WHEN \"results\".\"XCL_081\" = 1 THEN (CAST(SUBSTRING(\"results\".\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(\"results\".\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(\"results\".\"XCL_084\", 6) AS REAL) ELSE CAST(SUBSTRING(\"results\".\"XCL_084\", 2) AS REAL) END",
  "grain": [],
  "population_scope": "SELECT \"time_seconds\" FROM time_in_seconds WHERE \"XCL_081\" = (SELECT MAX(\"XCL_081\") FROM time_in_seconds)",
  "upstream_scopes": [
    "SELECT T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6) AS REAL) ELSE CAST(SUBSTRING(T1.\"XCL_084\", 2) AS REAL) END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Australian Grand Prix' AND NOT T1.\"XCL_084\" IS NULL AND T2.\"XCL_066\" = 2008"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:944"
  ]
}
```

### Driver Identifier XCL_039

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE NOT T2.\"XCL_088\" IS NULL ORDER BY T2.\"XCL_089\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:927"
  ]
}
```

### "races"."XCL_069" = 'Canadian Grand Prix' AND "races"."XCL_066" = 2008 AND "results"."XCL_084" LIKE '_:%:__.___'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Canadian Grand Prix' AND \"races\".\"XCL_066\" = 2008 AND \"results\".\"XCL_084\" LIKE '_:%:__.___'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_084\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Canadian Grand Prix' AND T2.\"XCL_066\" = 2008 AND T1.\"XCL_084\" LIKE '_:%:__.___'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:989"
  ]
}
```

### STRFTIME('%Y', "drivers"."XCL_040") = '1971' AND NOT "results"."XCL_088" IS NULL

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"drivers\".\"XCL_040\") = '1971' AND NOT \"results\".\"XCL_088\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_034\", T2.\"XCL_037\" FROM results AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_075\" = T2.\"XCL_034\" WHERE STRFTIME('%Y', T2.\"XCL_040\") = '1971' AND NOT T1.\"XCL_088\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:972"
  ]
}
```

### "races"."XCL_069" = 'Monaco Grand Prix' AND "races"."XCL_066" BETWEEN 1980 AND 2010

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Monaco Grand Prix' AND \"races\".\"XCL_066\" BETWEEN 1980 AND 2010",
  "grain": [
    "\"constructors\".\"XCL_024\""
  ],
  "population_scope": "SELECT SUM(T1.\"XCL_013\"), T2.\"XCL_024\", T2.\"XCL_025\" FROM constructorResults AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_012\" = T2.\"XCL_022\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T1.\"XCL_011\" WHERE T3.\"XCL_069\" = 'Monaco Grand Prix' AND T3.\"XCL_066\" BETWEEN 1980 AND 2010 GROUP BY T2.\"XCL_024\" ORDER BY SUM(T1.\"XCL_013\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:994"
  ]
}
```

### The value of column "XCL_041" from the "drivers" table that corresponds to the group with the highest count of "XCL_034". The grain is a single row re

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_041\"",
  "grain": [
    "\"drivers\".\"XCL_041\""
  ],
  "population_scope": "SELECT \"XCL_041\" FROM drivers GROUP BY \"XCL_041\" ORDER BY COUNT(\"XCL_034\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:997"
  ]
}
```

### Circuit Identifier

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_009\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_009\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Silverstone Circuit'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:921"
  ]
}
```

### "races"."XCL_066" < 1975

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_066\" < 1975",
  "grain": [
    "\"races\".\"XCL_066\""
  ],
  "population_scope": "WITH time_in_seconds AS (SELECT T2.\"XCL_066\", T2.\"XCL_065\", T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(T1.\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_084\" IS NULL), champion_time AS (SELECT \"XCL_066\", \"XCL_065\", \"time_seconds\" FROM time_in_seconds WHERE \"XCL_081\" = 1) SELECT \"XCL_066\", AVG(\"time_seconds\") FROM champion_time WHERE \"XCL_066\" < 1975 GROUP BY \"XCL_066\" HAVING NOT AVG(\"time_seconds\") IS NULL",
  "upstream_scopes": [
    "SELECT \"XCL_066\", \"XCL_065\", \"time_seconds\" FROM time_in_seconds WHERE \"XCL_081\" = 1",
    "SELECT T2.\"XCL_066\", T2.\"XCL_065\", T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(T1.\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_084\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:955"
  ]
}
```

### "races"."XCL_069" = 'Australian Grand Prix' AND "races"."XCL_066" = 2008

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Australian Grand Prix' AND \"races\".\"XCL_066\" = 2008",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(NOT T1.\"XCL_084\" IS NULL, 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_073\") FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Australian Grand Prix' AND T2.\"XCL_066\" = 2008",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:943"
  ]
}
```

### A calculated metric converting the raw time string (XCL_084) into seconds. For the winner (position 1), it parses hours, minutes, and seconds from a '

```json
{
  "kind": "binding",
  "formula": "CASE WHEN \"results\".\"XCL_081\" = 1 THEN (CAST(SUBSTRING(\"results\".\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(\"results\".\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(\"results\".\"XCL_084\", 6) AS REAL) ELSE CAST(SUBSTRING(\"results\".\"XCL_084\", 2) AS REAL) END",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6) AS REAL) ELSE CAST(SUBSTRING(T1.\"XCL_084\", 2) AS REAL) END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Australian Grand Prix' AND NOT T1.\"XCL_084\" IS NULL AND T2.\"XCL_066\" = 2008",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CASE WHEN \"r0\".\"XCL_081\" = 1 THEN (CAST(SUBSTRING(\"r0\".\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(\"r0\".\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(\"r0\".\"XCL_084\", 6) AS REAL) ELSE CAST(SUBSTRING(\"r0\".\"XCL_084\", 2) AS REAL) END",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT CASE WHEN \"r0\".\"XCL_081\" = 1 THEN (CAST(SUBSTRING(\"r0\".\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(\"r0\".\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(\"r0\".\"XCL_084\", 6) AS REAL) ELSE CAST(SUBSTRING(\"r0\".\"XCL_084\", 2) AS REAL) END AS \"value\" FROM results AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_074\" = \"r1\".\"XCL_065\" WHERE \"r1\".\"XCL_069\" = 'Australian Grand Prix' AND NOT \"r0\".\"XCL_084\" IS NULL AND \"r1\".\"XCL_066\" = 2008",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:944"
  ]
}
```

### Calculates the percentage of race entries (XCL_068) associated with the 'European Grand Prix' (XCL_069) that are located in 'Germany' (XCL_005). The m

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN \"circuits\".\"XCL_005\" = 'Germany' THEN \"races\".\"XCL_068\" END) AS REAL) * 100 / COUNT(\"races\".\"XCL_068\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T1.\"XCL_005\" = 'Germany' THEN T2.\"XCL_068\" END) AS REAL) * 100 / COUNT(T2.\"XCL_068\") FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_069\" = 'European Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(CASE WHEN \"r0\".\"XCL_005\" = 'Germany' THEN \"r1\".\"XCL_068\" END) AS REAL) * 100 / COUNT(\"r1\".\"XCL_068\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(CASE WHEN \"r0\".\"XCL_005\" = 'Germany' THEN \"r1\".\"XCL_068\" END) AS REAL) * 100 / COUNT(\"r1\".\"XCL_068\") AS \"value\" FROM circuits AS \"r0\" INNER JOIN races AS \"r1\" ON \"r1\".\"XCL_068\" = \"r0\".\"XCL_001\" WHERE \"r1\".\"XCL_069\" = 'European Grand Prix'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:909"
  ]
}
```

### A driver-level attribute from the 'drivers' table (T1). It serves as a grouping key and output column, representing a specific characteristic of the d

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [
    "\"drivers\".\"XCL_038\"",
    "\"drivers\".\"XCL_039\"",
    "\"drivers\".\"XCL_041\""
  ],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_041\", MAX(T2.\"XCL_030\") FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_029\" = T1.\"XCL_034\" WHERE T2.\"XCL_033\" >= 1 GROUP BY T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_041\" ORDER BY COUNT(T2.\"XCL_033\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:897"
  ]
}
```

### NOT "results"."XCL_088" IS NULL

```json
{
  "kind": "predicate",
  "formula": "NOT \"results\".\"XCL_088\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_074\", T1.\"XCL_075\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1016"
  ]
}
```

### Name or identifier for the race (races.XCL_069) linked to the driver's standing in the most recent event.

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_041\", T3.\"XCL_069\" FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" INNER JOIN races AS T3 ON T2.\"XCL_028\" = T3.\"XCL_065\" ORDER BY JULIANDAY(T1.\"XCL_040\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1002"
  ]
}
```

### "drivers"."XCL_038" = 'Lewis' AND "drivers"."XCL_039" = 'Hamilton' AND "races"."XCL_069" = 'Chinese Grand Prix' AND "races"."XCL_066" = 2008

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Lewis' AND \"drivers\".\"XCL_039\" = 'Hamilton' AND \"races\".\"XCL_069\" = 'Chinese Grand Prix' AND \"races\".\"XCL_066\" = 2008",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_081\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T3.\"XCL_038\" = 'Lewis' AND T3.\"XCL_039\" = 'Hamilton' AND T1.\"XCL_069\" = 'Chinese Grand Prix' AND T1.\"XCL_066\" = 2008",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:933"
  ]
}
```

### Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_065\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_065\" FROM races WHERE \"XCL_066\" = 2009",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_065\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_065\" AS \"value\" FROM races AS \"r0\" WHERE \"r0\".\"XCL_066\" = 2009",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:965"
  ]
}
```

### Driver Attribute XCL_040

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_040\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_035\", T2.\"XCL_041\", T2.\"XCL_040\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_058\" = T2.\"XCL_034\" WHERE T1.\"XCL_057\" = 23 AND NOT T1.\"XCL_063\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_040\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "qualifying"
      },
      {
        "role": "r1",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_040\" AS \"value\" FROM qualifying AS \"r0\" INNER JOIN drivers AS \"r1\" ON \"r0\".\"XCL_058\" = \"r1\".\"XCL_034\" WHERE \"r0\".\"XCL_057\" = 23 AND NOT \"r0\".\"XCL_063\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:980"
  ]
}
```

### Driver Identifier XCL_039

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_038\", T2.\"XCL_039\", T1.\"XCL_088\" FROM results AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_075\" = T2.\"XCL_034\" WHERE NOT T1.\"XCL_088\" IS NULL ORDER BY T1.\"XCL_088\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:958"
  ]
}
```

### Race Location or Circuit

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_071\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_066\", T3.\"XCL_069\", T3.\"XCL_070\", T3.\"XCL_071\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_058\" = T2.\"XCL_034\" INNER JOIN races AS T3 ON T1.\"XCL_057\" = T3.\"XCL_065\" WHERE T1.\"XCL_058\" = (SELECT \"XCL_034\" FROM drivers ORDER BY \"XCL_040\" DESC LIMIT 1) ORDER BY T3.\"XCL_070\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:981"
  ]
}
```

### Driver Position

```json
{
  "kind": "binding",
  "formula": "\"results\".\"XCL_081\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6) AS REAL) ELSE CAST(SUBSTRING(T1.\"XCL_084\", 2) AS REAL) END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Australian Grand Prix' AND NOT T1.\"XCL_084\" IS NULL AND T2.\"XCL_066\" = 2008",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_081\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_081\" AS \"value\" FROM results AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_074\" = \"r1\".\"XCL_065\" WHERE \"r1\".\"XCL_069\" = 'Australian Grand Prix' AND NOT \"r0\".\"XCL_084\" IS NULL AND \"r1\".\"XCL_066\" = 2008",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:944"
  ]
}
```

### Max Standing Value XCL_030

```json
{
  "kind": "metric",
  "formula": "MAX(\"driverStandings\".\"XCL_030\")",
  "grain": [
    "\"drivers\".\"XCL_038\"",
    "\"drivers\".\"XCL_039\"",
    "\"drivers\".\"XCL_041\""
  ],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_041\", MAX(T2.\"XCL_030\") FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_029\" = T1.\"XCL_034\" WHERE T2.\"XCL_033\" >= 1 GROUP BY T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_041\" ORDER BY COUNT(T2.\"XCL_033\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:897"
  ]
}
```

### Date attribute (XCL_040) for the driver, used to filter records where the year is between 1981 and 1991.

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_040\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_038\", \"XCL_039\", \"XCL_040\" FROM drivers WHERE \"XCL_041\" = 'Austrian' AND STRFTIME('%Y', \"XCL_040\") BETWEEN '1981' AND '1991'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_040\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_040\" AS \"value\" FROM drivers AS \"r0\" WHERE \"r0\".\"XCL_041\" = 'Austrian' AND STRFTIME('%Y', \"r0\".\"XCL_040\") BETWEEN '1981' AND '1991'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:991"
  ]
}
```

### Calculates the percentage of rows in the results table where the column XCL_084 is not null, relative to the total count of rows (identified by XCL_07

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(NOT \"results\".\"XCL_084\" IS NULL, 1, 0)) AS REAL) * 100 / COUNT(\"results\".\"XCL_073\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(NOT T1.\"XCL_084\" IS NULL, 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_073\") FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Australian Grand Prix' AND T2.\"XCL_066\" = 2008",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(IIF(NOT \"r0\".\"XCL_084\" IS NULL, 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_073\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(IIF(NOT \"r0\".\"XCL_084\" IS NULL, 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_073\") AS \"value\" FROM results AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_074\" = \"r1\".\"XCL_065\" WHERE \"r1\".\"XCL_069\" = 'Australian Grand Prix' AND \"r1\".\"XCL_066\" = 2008",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:943"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_035\" FROM drivers WHERE \"XCL_038\" = 'Lewis' AND \"XCL_039\" = 'Hamilton'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_035\" AS \"value\" FROM drivers AS \"r0\" WHERE \"r0\".\"XCL_038\" = 'Lewis' AND \"r0\".\"XCL_039\" = 'Hamilton'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:918"
  ]
}
```

### Constructor Name

```json
{
  "kind": "binding",
  "formula": "\"constructors\".\"XCL_024\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_024\" FROM constructorStandings AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_017\" = T2.\"XCL_022\" ORDER BY T1.\"XCL_018\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:949"
  ]
}
```

### Identifier for a specific race result record in the results table. Used to link individual lap times to their corresponding race event.

```json
{
  "kind": "binding",
  "formula": "\"results\".\"XCL_074\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_074\", T1.\"XCL_075\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_074\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_074\" AS \"value\" FROM results AS \"r0\" WHERE NOT \"r0\".\"XCL_088\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1016",
    "bird_dev:1014",
    "bird_dev:1013",
    "bird_dev:1015"
  ]
}
```

### A scalar metric representing the percentage of rows in the joined dataset where the driver's XCL_040 year is before 1985 AND the result's XCL_083 is g

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(STRFTIME('%Y', \"drivers\".\"XCL_040\") < '1985' AND \"results\".\"XCL_083\" > 50, 1, 0)) AS REAL) * 100 / COUNT(*)",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(STRFTIME('%Y', T3.\"XCL_040\") < '1985' AND T1.\"XCL_083\" > 50, 1, 0)) AS REAL) * 100 / COUNT(*) FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN drivers AS T3 ON T1.\"XCL_075\" = T3.\"XCL_034\" WHERE T2.\"XCL_066\" BETWEEN 2000 AND 2005",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(IIF(STRFTIME('%Y', \"r2\".\"XCL_040\") < '1985' AND \"r0\".\"XCL_083\" > 50, 1, 0)) AS REAL) * 100 / COUNT(*)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "races"
      },
      {
        "role": "r2",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(IIF(STRFTIME('%Y', \"r2\".\"XCL_040\") < '1985' AND \"r0\".\"XCL_083\" > 50, 1, 0)) AS REAL) * 100 / COUNT(*) AS \"value\" FROM results AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_074\" = \"r1\".\"XCL_065\" INNER JOIN drivers AS \"r2\" ON \"r0\".\"XCL_075\" = \"r2\".\"XCL_034\" WHERE \"r1\".\"XCL_066\" BETWEEN 2000 AND 2005",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:962"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_042\" FROM drivers AS T1 INNER JOIN results AS T2 ON T1.\"XCL_034\" = T2.\"XCL_075\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T2.\"XCL_074\" WHERE T3.\"XCL_069\" = 'Australian Grand Prix' AND T2.\"XCL_084\" LIKE '_:%:__.___' AND T3.\"XCL_066\" = 2008",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_038\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      },
      {
        "role": "r1",
        "physical_table": "results"
      },
      {
        "role": "r2",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_038\" AS \"value\" FROM drivers AS \"r0\" INNER JOIN results AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_075\" INNER JOIN races AS \"r2\" ON \"r2\".\"XCL_065\" = \"r1\".\"XCL_074\" WHERE \"r2\".\"XCL_069\" = 'Australian Grand Prix' AND \"r1\".\"XCL_084\" LIKE '_:%:__.___' AND \"r2\".\"XCL_066\" = 2008",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:938"
  ]
}
```

### Pit Stop Duration

```json
{
  "kind": "binding",
  "formula": "T4.\"XCL_054\"",
  "grain": [],
  "population_scope": "WITH fastest_lap_times AS (SELECT T1.\"XCL_074\", T1.\"XCL_075\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL), lap_record_race AS (SELECT T1.\"XCL_074\", T1.\"XCL_075\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" INNER JOIN (SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix') AS T4 ON (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) = T4.\"min_time_in_seconds\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix') SELECT T4.\"XCL_054\" FROM lap_record_race INNER JOIN pitStops AS T4 ON lap_record_race.\"XCL_074\" = T4.\"XCL_049\" AND lap_record_race.\"XCL_075\" = T4.\"XCL_050\"",
  "upstream_scopes": [
    "SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix'",
    "SELECT T1.\"XCL_074\", T1.\"XCL_075\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" INNER JOIN (SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix') AS T4 ON (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) = T4.\"min_time_in_seconds\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix'",
    "SELECT T1.\"XCL_074\", T1.\"XCL_075\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1016"
  ]
}
```

### Aggregates the number of rows in the drivers table where the driver's nationality is 'British' and the year extracted from the date column XCL_040 is 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"drivers\".\"XCL_034\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_034\") FROM drivers WHERE \"XCL_041\" = 'British' AND STRFTIME('%Y', \"XCL_040\") = '1980'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_034\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_034\") AS \"value\" FROM drivers AS \"r0\" WHERE \"r0\".\"XCL_041\" = 'British' AND STRFTIME('%Y', \"r0\".\"XCL_040\") = '1980'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:969"
  ]
}
```

### "circuits"."XCL_005" = 'Italy'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_005\" = 'Italy'",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_068\") FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_005\" = 'Italy'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:923"
  ]
}
```

### "races"."XCL_066" = 2009 AND "races"."XCL_069" = 'Spanish Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_066\" = 2009 AND \"races\".\"XCL_069\" = 'Spanish Grand Prix'",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_089\") FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_066\" = 2009 AND T2.\"XCL_069\" = 'Spanish Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:960"
  ]
}
```

### Count of drivers with null result field

```json
{
  "kind": "metric",
  "formula": "COUNT(\"drivers\".\"XCL_034\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T3.\"XCL_034\") FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T1.\"XCL_066\" = 2007 AND T1.\"XCL_069\" = 'Bahrain Grand Prix' AND T2.\"XCL_084\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r2\".\"XCL_034\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      },
      {
        "role": "r1",
        "physical_table": "results"
      },
      {
        "role": "r2",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r2\".\"XCL_034\") AS \"value\" FROM races AS \"r0\" INNER JOIN results AS \"r1\" ON \"r1\".\"XCL_074\" = \"r0\".\"XCL_065\" INNER JOIN drivers AS \"r2\" ON \"r2\".\"XCL_034\" = \"r1\".\"XCL_075\" WHERE \"r0\".\"XCL_066\" = 2007 AND \"r0\".\"XCL_069\" = 'Bahrain Grand Prix' AND \"r1\".\"XCL_084\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:862"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_041\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_041\" FROM drivers WHERE NOT \"XCL_040\" IS NULL ORDER BY \"XCL_040\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:915"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_035\" FROM drivers WHERE \"XCL_038\" = 'Robert' AND \"XCL_039\" = 'Kubica'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_035\" AS \"value\" FROM drivers AS \"r0\" WHERE \"r0\".\"XCL_038\" = 'Robert' AND \"r0\".\"XCL_039\" = 'Kubica'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:968"
  ]
}
```

### "drivers"."XCL_038" = 'Lewis' AND "drivers"."XCL_039" = 'Hamilton'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Lewis' AND \"drivers\".\"XCL_039\" = 'Hamilton'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_046\" FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_044\" = T2.\"XCL_034\" WHERE T2.\"XCL_038\" = 'Lewis' AND T2.\"XCL_039\" = 'Hamilton' ORDER BY T1.\"XCL_047\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1012"
  ]
}
```

### "lapTimes"."XCL_045" = 1

```json
{
  "kind": "predicate",
  "formula": "\"lapTimes\".\"XCL_045\" = 1",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_048\" FROM lapTimes AS T1 INNER JOIN races AS T2 ON T1.\"XCL_043\" = T2.\"XCL_065\" WHERE T1.\"XCL_045\" = 1 ORDER BY T1.\"XCL_047\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:986"
  ]
}
```

### Driver ID

```json
{
  "kind": "binding",
  "formula": "\"results\".\"XCL_075\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_074\", T1.\"XCL_075\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_075\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_075\" AS \"value\" FROM results AS \"r0\" WHERE NOT \"r0\".\"XCL_088\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1016"
  ]
}
```

### Race Year

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_066\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_066\", T2.\"XCL_065\", T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(T1.\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_084\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_066\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_066\" AS \"value\" FROM results AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_074\" = \"r1\".\"XCL_065\" WHERE NOT \"r0\".\"XCL_084\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:955"
  ]
}
```

### Qualifying Result Identifier

```json
{
  "kind": "binding",
  "formula": "\"qualifying\".\"XCL_062\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_062\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 345 AND T2.\"XCL_038\" = 'Lucas' AND T2.\"XCL_039\" = 'di Grassi'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_062\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "qualifying"
      },
      {
        "role": "r1",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_062\" AS \"value\" FROM qualifying AS \"r0\" INNER JOIN drivers AS \"r1\" ON \"r1\".\"XCL_034\" = \"r0\".\"XCL_058\" WHERE \"r0\".\"XCL_057\" = 345 AND \"r1\".\"XCL_038\" = 'Lucas' AND \"r1\".\"XCL_039\" = 'di Grassi'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:870"
  ]
}
```

### "qualifying"."XCL_057" = 354 AND "drivers"."XCL_038" = 'Bruno' AND "drivers"."XCL_039" = 'Senna'

```json
{
  "kind": "predicate",
  "formula": "\"qualifying\".\"XCL_057\" = 354 AND \"drivers\".\"XCL_038\" = 'Bruno' AND \"drivers\".\"XCL_039\" = 'Senna'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_062\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 354 AND T2.\"XCL_038\" = 'Bruno' AND T2.\"XCL_039\" = 'Senna'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:859"
  ]
}
```

### Aggregated sum of the XCL_013 field from constructorResults, representing the total points or score for a constructor. The population is restricted to

```json
{
  "kind": "metric",
  "formula": "SUM(\"constructorResults\".\"XCL_013\")",
  "grain": [
    "\"constructors\".\"XCL_024\""
  ],
  "population_scope": "SELECT SUM(T1.\"XCL_013\"), T2.\"XCL_024\", T2.\"XCL_025\" FROM constructorResults AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_012\" = T2.\"XCL_022\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T1.\"XCL_011\" WHERE T3.\"XCL_069\" = 'Monaco Grand Prix' AND T3.\"XCL_066\" BETWEEN 1980 AND 2010 GROUP BY T2.\"XCL_024\" ORDER BY SUM(T1.\"XCL_013\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:994"
  ]
}
```

### Minimum Fastest Lap Time

```json
{
  "kind": "metric",
  "formula": "MIN(\"results\".\"XCL_088\")",
  "grain": [],
  "population_scope": "WITH fastest_lap_times AS (SELECT T1.\"XCL_074\", T1.\"XCL_088\" FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL) SELECT MIN(fastest_lap_times.\"XCL_088\") AS lap_record FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix'",
  "upstream_scopes": [
    "SELECT T1.\"XCL_074\", T1.\"XCL_088\" FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1013"
  ]
}
```

### "drivers"."XCL_038" = 'Lewis' AND "drivers"."XCL_039" = 'Hamilton'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Lewis' AND \"drivers\".\"XCL_039\" = 'Hamilton'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_069\", T2.\"XCL_030\" FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" WHERE T3.\"XCL_038\" = 'Lewis' AND T3.\"XCL_039\" = 'Hamilton' ORDER BY T1.\"XCL_066\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:906"
  ]
}
```

### "qualifying"."XCL_057" = 355 AND "qualifying"."XCL_063" LIKE '1:40%'

```json
{
  "kind": "predicate",
  "formula": "\"qualifying\".\"XCL_057\" = 355 AND \"qualifying\".\"XCL_063\" LIKE '1:40%'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_041\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 355 AND T1.\"XCL_063\" LIKE '1:40%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:860"
  ]
}
```

### Driver Attribute XCL_035

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_035\", T2.\"XCL_041\", T2.\"XCL_040\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_058\" = T2.\"XCL_034\" WHERE T1.\"XCL_057\" = 23 AND NOT T1.\"XCL_063\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "qualifying"
      },
      {
        "role": "r1",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_035\" AS \"value\" FROM qualifying AS \"r0\" INNER JOIN drivers AS \"r1\" ON \"r0\".\"XCL_058\" = \"r1\".\"XCL_034\" WHERE \"r0\".\"XCL_057\" = 23 AND NOT \"r0\".\"XCL_063\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:980"
  ]
}
```

### "circuits"."XCL_004" = 'Adelaide' AND "circuits"."XCL_005" = 'Australia'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_004\" = 'Adelaide' AND \"circuits\".\"XCL_005\" = 'Australia'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM circuits WHERE \"XCL_004\" = 'Adelaide' AND \"XCL_005\" = 'Australia'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:945"
  ]
}
```

### The value of column XCL_074 from the results table that has the highest count of non-null entries in column XCL_084. The grain is one row per distinct

```json
{
  "kind": "binding",
  "formula": "\"results\".\"XCL_074\"",
  "grain": [
    "\"results\".\"XCL_074\""
  ],
  "population_scope": "SELECT \"XCL_074\" FROM results GROUP BY \"XCL_074\" ORDER BY COUNT(NOT \"XCL_084\" IS NULL) DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:979"
  ]
}
```

### Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_066\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_066\" FROM lapTimes AS T1 INNER JOIN races AS T2 ON T1.\"XCL_043\" = T2.\"XCL_065\" ORDER BY T1.\"XCL_047\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:975"
  ]
}
```

### Average Lap Time (Italy)

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"lapTimes\".\"XCL_048\") AS REAL) / COUNT(\"lapTimes\".\"XCL_045\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(T1.\"XCL_048\") AS REAL) / COUNT(T1.\"XCL_045\") FROM lapTimes AS T1 INNER JOIN races AS T2 ON T1.\"XCL_043\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T3.\"XCL_005\" = 'Italy'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(\"r0\".\"XCL_048\") AS REAL) / COUNT(\"r0\".\"XCL_045\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "lapTimes"
      },
      {
        "role": "r1",
        "physical_table": "races"
      },
      {
        "role": "r2",
        "physical_table": "circuits"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(\"r0\".\"XCL_048\") AS REAL) / COUNT(\"r0\".\"XCL_045\") AS \"value\" FROM lapTimes AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_043\" = \"r1\".\"XCL_065\" INNER JOIN circuits AS \"r2\" ON \"r1\".\"XCL_068\" = \"r2\".\"XCL_001\" WHERE \"r2\".\"XCL_005\" = 'Italy'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1019"
  ]
}
```

### "circuits"."XCL_005" = 'Austria'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_005\" = 'Austria'",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_004\", \"XCL_006\", \"XCL_007\" FROM circuits WHERE \"XCL_005\" = 'Austria'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:978"
  ]
}
```

### Race Identifier for Lewis Hamilton

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_069\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T3.\"XCL_038\" = 'Lewis' AND T3.\"XCL_039\" = 'Hamilton'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_069\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      },
      {
        "role": "r1",
        "physical_table": "results"
      },
      {
        "role": "r2",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_069\" AS \"value\" FROM races AS \"r0\" INNER JOIN results AS \"r1\" ON \"r1\".\"XCL_074\" = \"r0\".\"XCL_065\" INNER JOIN drivers AS \"r2\" ON \"r2\".\"XCL_034\" = \"r1\".\"XCL_075\" WHERE \"r2\".\"XCL_038\" = 'Lewis' AND \"r2\".\"XCL_039\" = 'Hamilton'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:929"
  ]
}
```

### Average Lap Time

```json
{
  "kind": "metric",
  "formula": "AVG(\"lapTimes\".\"XCL_048\")",
  "grain": [],
  "population_scope": "SELECT AVG(T2.\"XCL_048\") FROM races AS T1 INNER JOIN lapTimes AS T2 ON T2.\"XCL_043\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_044\" WHERE T3.\"XCL_038\" = 'Lewis' AND T3.\"XCL_039\" = 'Hamilton' AND T1.\"XCL_066\" = 2009 AND T1.\"XCL_069\" = 'Malaysian Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r1\".\"XCL_048\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      },
      {
        "role": "r1",
        "physical_table": "lapTimes"
      },
      {
        "role": "r2",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT AVG(\"r1\".\"XCL_048\") AS \"value\" FROM races AS \"r0\" INNER JOIN lapTimes AS \"r1\" ON \"r1\".\"XCL_043\" = \"r0\".\"XCL_065\" INNER JOIN drivers AS \"r2\" ON \"r2\".\"XCL_034\" = \"r1\".\"XCL_044\" WHERE \"r2\".\"XCL_038\" = 'Lewis' AND \"r2\".\"XCL_039\" = 'Hamilton' AND \"r0\".\"XCL_066\" = 2009 AND \"r0\".\"XCL_069\" = 'Malaysian Grand Prix'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:895"
  ]
}
```

### Circuit Location

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\", T1.\"XCL_004\", T2.\"XCL_069\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_005\" = 'USA' AND T2.\"XCL_066\" = 2006",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_004\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_004\" AS \"value\" FROM circuits AS \"r0\" INNER JOIN races AS \"r1\" ON \"r1\".\"XCL_068\" = \"r0\".\"XCL_001\" WHERE \"r0\".\"XCL_005\" = 'USA' AND \"r1\".\"XCL_066\" = 2006",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:900"
  ]
}
```

### The value of column "XCL_066" from the "races" table that corresponds to the group with the highest count of "XCL_067". The grain is a single row repr

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_066\"",
  "grain": [
    "\"races\".\"XCL_066\""
  ],
  "population_scope": "SELECT \"XCL_066\" FROM races GROUP BY \"XCL_066\" ORDER BY COUNT(\"XCL_067\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:886"
  ]
}
```

### Driver Name

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_038\", \"XCL_039\", \"XCL_040\" FROM drivers WHERE \"XCL_041\" = 'Austrian' AND STRFTIME('%Y', \"XCL_040\") BETWEEN '1981' AND '1991'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_039\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_039\" AS \"value\" FROM drivers AS \"r0\" WHERE \"r0\".\"XCL_041\" = 'Austrian' AND STRFTIME('%Y', \"r0\".\"XCL_040\") BETWEEN '1981' AND '1991'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:991"
  ]
}
```

### Last Driver Position

```json
{
  "kind": "metric",
  "formula": "MAX(\"results\".\"XCL_081\")",
  "grain": [],
  "population_scope": "SELECT MAX(\"XCL_081\") FROM time_in_seconds",
  "upstream_scopes": [
    "SELECT T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6) AS REAL) ELSE CAST(SUBSTRING(T1.\"XCL_084\", 2) AS REAL) END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Australian Grand Prix' AND NOT T1.\"XCL_084\" IS NULL AND T2.\"XCL_066\" = 2008"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:944"
  ]
}
```

### Record Holder Race ID

```json
{
  "kind": "binding",
  "formula": "T1.\"XCL_074\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_074\", T1.\"XCL_075\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" INNER JOIN (SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix') AS T4 ON (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) = T4.\"min_time_in_seconds\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix'",
  "upstream_scopes": [
    "SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix'",
    "SELECT T1.\"XCL_074\", T1.\"XCL_075\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1016"
  ]
}
```

### "races"."XCL_069" = 'Australian Grand Prix' AND "drivers"."XCL_041" = 'British' AND "races"."XCL_066" = 2008

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Australian Grand Prix' AND \"drivers\".\"XCL_041\" = 'British' AND \"races\".\"XCL_066\" = 2008",
  "grain": [],
  "population_scope": "SELECT COUNT(*) FROM drivers AS T1 INNER JOIN results AS T2 ON T1.\"XCL_034\" = T2.\"XCL_075\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T2.\"XCL_074\" WHERE T3.\"XCL_069\" = 'Australian Grand Prix' AND T1.\"XCL_041\" = 'British' AND T3.\"XCL_066\" = 2008",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:939"
  ]
}
```

### "races"."XCL_069" = 'Australian Grand Prix' AND "races"."XCL_066" = 2008 AND NOT "results"."XCL_084" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Australian Grand Prix' AND \"races\".\"XCL_066\" = 2008 AND NOT \"results\".\"XCL_084\" IS NULL",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_075\") FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" WHERE T1.\"XCL_069\" = 'Australian Grand Prix' AND T1.\"XCL_066\" = 2008 AND NOT T2.\"XCL_084\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:935"
  ]
}
```

### Champion Race Year

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_066\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_066\", \"XCL_065\", \"time_seconds\" FROM time_in_seconds WHERE \"XCL_081\" = 1",
  "upstream_scopes": [
    "SELECT T2.\"XCL_066\", T2.\"XCL_065\", T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(T1.\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_084\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:955"
  ]
}
```

### Race IDs where Lewis Hamilton won

```json
{
  "kind": "binding",
  "formula": "\"results\".\"XCL_074\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_074\" FROM results WHERE \"XCL_087\" = 1 AND \"XCL_075\" = (SELECT \"XCL_034\" FROM drivers WHERE \"XCL_038\" = 'Lewis' AND \"XCL_039\" = 'Hamilton')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:930"
  ]
}
```

### Champion Race ID

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_065\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_066\", \"XCL_065\", \"time_seconds\" FROM time_in_seconds WHERE \"XCL_081\" = 1",
  "upstream_scopes": [
    "SELECT T2.\"XCL_066\", T2.\"XCL_065\", T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(T1.\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_084\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:955"
  ]
}
```

### "circuits"."XCL_003" = 'Sepang International Circuit'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_003\" = 'Sepang International Circuit'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_071\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Sepang International Circuit'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:856"
  ]
}
```

### Driver Name (Second)

```json
{
  "kind": "binding",
  "formula": "T2.\"XCL_039\"",
  "grain": [],
  "population_scope": "WITH lap_times_in_seconds AS (SELECT \"XCL_044\", (CASE WHEN SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) AS REAL) * 60 ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) AS REAL) ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) AS REAL) / 1000 ELSE 0 END) AS time_in_seconds FROM lapTimes) SELECT T2.\"XCL_038\", T2.\"XCL_039\", T1.\"XCL_044\" FROM (SELECT \"XCL_044\", MIN(\"time_in_seconds\") AS min_time_in_seconds FROM lap_times_in_seconds GROUP BY \"XCL_044\") AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_044\" = T2.\"XCL_034\" ORDER BY T1.\"min_time_in_seconds\" ASC LIMIT 20",
  "upstream_scopes": [
    "SELECT \"XCL_044\", (CASE WHEN SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) AS REAL) * 60 ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) AS REAL) ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) AS REAL) / 1000 ELSE 0 END) AS time_in_seconds FROM lapTimes",
    "SELECT \"XCL_044\", MIN(\"time_in_seconds\") AS min_time_in_seconds FROM lap_times_in_seconds GROUP BY \"XCL_044\""
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1011"
  ]
}
```

### "drivers"."XCL_038" = 'Lewis' AND "drivers"."XCL_039" = 'Hamilton' AND NOT "results"."XCL_088" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Lewis' AND \"drivers\".\"XCL_039\" = 'Hamilton' AND NOT \"results\".\"XCL_088\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_088\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE T1.\"XCL_038\" = 'Lewis' AND T1.\"XCL_039\" = 'Hamilton' AND NOT T2.\"XCL_088\" IS NULL ORDER BY T2.\"XCL_088\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:926"
  ]
}
```

### Constructor Identifier

```json
{
  "kind": "binding",
  "formula": "\"constructors\".\"XCL_026\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_026\" FROM constructorResults AS T1 INNER JOIN constructors AS T2 ON T2.\"XCL_022\" = T1.\"XCL_012\" WHERE T1.\"XCL_011\" = 9 ORDER BY T1.\"XCL_013\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:869"
  ]
}
```

### Circuit Identifier XCL_007

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_006\", \"XCL_007\" FROM circuits WHERE \"XCL_005\" = 'USA'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_007\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_007\" AS \"value\" FROM circuits AS \"r0\" WHERE \"r0\".\"XCL_005\" = 'USA'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:946"
  ]
}
```

### "circuits"."XCL_003" = 'Silverstone Circuit' AND "races"."XCL_069" = 'British Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_003\" = 'Silverstone Circuit' AND \"races\".\"XCL_069\" = 'British Grand Prix'",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_068\") FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Silverstone Circuit' AND T2.\"XCL_069\" = 'British Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:890"
  ]
}
```

### Result Identifier

```json
{
  "kind": "binding",
  "formula": "\"results\".\"XCL_084\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_084\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T1.\"XCL_087\" = 2 AND T2.\"XCL_069\" = 'Chinese Grand Prix' AND T2.\"XCL_066\" = 2008",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_084\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_084\" AS \"value\" FROM results AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_074\" = \"r1\".\"XCL_065\" WHERE \"r0\".\"XCL_087\" = 2 AND \"r1\".\"XCL_069\" = 'Chinese Grand Prix' AND \"r1\".\"XCL_066\" = 2008",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:937"
  ]
}
```

### Driver Name

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [
    "\"drivers\".\"XCL_038\"",
    "\"drivers\".\"XCL_039\""
  ],
  "population_scope": "SELECT T2.\"XCL_038\", T2.\"XCL_039\" FROM pitStops AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_050\" = T2.\"XCL_034\" WHERE T2.\"XCL_041\" = 'German' AND STRFTIME('%Y', T2.\"XCL_040\") BETWEEN '1980' AND '1985' GROUP BY T2.\"XCL_038\", T2.\"XCL_039\" ORDER BY AVG(T1.\"XCL_054\") LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:988"
  ]
}
```

### "races"."XCL_066" = 2000

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_066\" = 2000",
  "grain": [],
  "population_scope": "SELECT \"XCL_069\" FROM races WHERE \"XCL_066\" = 2000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:887"
  ]
}
```

### Result Metric XCL_086

```json
{
  "kind": "binding",
  "formula": "\"results\".\"XCL_086\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_086\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN drivers AS T3 ON T1.\"XCL_075\" = T3.\"XCL_034\" WHERE T2.\"XCL_069\" = 'Australian Grand Prix' AND T2.\"XCL_066\" = 2008 AND T3.\"XCL_038\" = 'Lewis' AND T3.\"XCL_039\" = 'Hamilton'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_086\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "races"
      },
      {
        "role": "r2",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_086\" AS \"value\" FROM results AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_074\" = \"r1\".\"XCL_065\" INNER JOIN drivers AS \"r2\" ON \"r0\".\"XCL_075\" = \"r2\".\"XCL_034\" WHERE \"r1\".\"XCL_069\" = 'Australian Grand Prix' AND \"r1\".\"XCL_066\" = 2008 AND \"r2\".\"XCL_038\" = 'Lewis' AND \"r2\".\"XCL_039\" = 'Hamilton'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:936"
  ]
}
```

### "circuits"."XCL_003" = 'Circuit de Barcelona-Catalunya'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_003\" = 'Circuit de Barcelona-Catalunya'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_009\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Circuit de Barcelona-Catalunya'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:849"
  ]
}
```

### Driver Time

```json
{
  "kind": "binding",
  "formula": "\"results\".\"XCL_084\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_084\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Canadian Grand Prix' AND T2.\"XCL_066\" = 2008 AND T1.\"XCL_084\" LIKE '_:%:__.___'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_084\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_084\" AS \"value\" FROM results AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_074\" = \"r1\".\"XCL_065\" WHERE \"r1\".\"XCL_069\" = 'Canadian Grand Prix' AND \"r1\".\"XCL_066\" = 2008 AND \"r0\".\"XCL_084\" LIKE '_:%:__.___'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:989"
  ]
}
```

### Circuit Location

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_069\", T1.\"XCL_003\", T1.\"XCL_004\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_066\" = 2005 AND STRFTIME('%m', T2.\"XCL_070\") = '09'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:901"
  ]
}
```

### Aggregates the count of 'XCL_075' entries from the 'results' table where the associated 'XCL_084' is not null, filtered to races occurring on '2015-11

```json
{
  "kind": "metric",
  "formula": "COUNT(\"results\".\"XCL_075\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_075\") FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" WHERE T1.\"XCL_070\" = '2015-11-29' AND NOT T2.\"XCL_084\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_075\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      },
      {
        "role": "r1",
        "physical_table": "results"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_075\") AS \"value\" FROM races AS \"r0\" INNER JOIN results AS \"r1\" ON \"r1\".\"XCL_074\" = \"r0\".\"XCL_065\" WHERE \"r0\".\"XCL_070\" = '2015-11-29' AND NOT \"r1\".\"XCL_084\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:864"
  ]
}
```

### The value of column XCL_066 from the races table, associated with the race linked to the lap time with the highest XCL_045 value.

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_066\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_045\", T2.\"XCL_069\", T2.\"XCL_066\", T1.\"XCL_004\" FROM circuits AS T1 INNER JOIN races AS T2 ON T1.\"XCL_001\" = T2.\"XCL_068\" INNER JOIN lapTimes AS T3 ON T3.\"XCL_043\" = T2.\"XCL_065\" ORDER BY T3.\"XCL_045\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:908"
  ]
}
```

### "drivers"."XCL_038" = 'Michael' AND "drivers"."XCL_039" = 'Schumacher' AND "circuits"."XCL_003" = 'Sepang International Circuit'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Michael' AND \"drivers\".\"XCL_039\" = 'Schumacher' AND \"circuits\".\"XCL_003\" = 'Sepang International Circuit'",
  "grain": [],
  "population_scope": "SELECT SUM(T2.\"XCL_033\") FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_029\" = T1.\"XCL_034\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T2.\"XCL_028\" INNER JOIN circuits AS T4 ON T4.\"XCL_001\" = T3.\"XCL_068\" WHERE T1.\"XCL_038\" = 'Michael' AND T1.\"XCL_039\" = 'Schumacher' AND T4.\"XCL_003\" = 'Sepang International Circuit'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:903"
  ]
}
```

### Circuit Identifier XCL_006

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_006\", \"XCL_007\" FROM circuits WHERE \"XCL_005\" = 'USA'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_006\" AS \"value\" FROM circuits AS \"r0\" WHERE \"r0\".\"XCL_005\" = 'USA'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:946"
  ]
}
```

### "races"."XCL_069" = 'Austrian Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Austrian Grand Prix'",
  "grain": [],
  "population_scope": "WITH fastest_lap_times AS (SELECT T1.\"XCL_074\", T1.\"XCL_088\" FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL) SELECT MIN(fastest_lap_times.\"XCL_088\") AS lap_record FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix'",
  "upstream_scopes": [
    "SELECT T1.\"XCL_074\", T1.\"XCL_088\" FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1013"
  ]
}
```

### "drivers"."XCL_038" = 'Alex' AND "drivers"."XCL_039" = 'Yoong' AND "driverStandings"."XCL_031" < 20

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Alex' AND \"drivers\".\"XCL_039\" = 'Yoong' AND \"driverStandings\".\"XCL_031\" < 20",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_069\" FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" WHERE T3.\"XCL_038\" = 'Alex' AND T3.\"XCL_039\" = 'Yoong' AND T2.\"XCL_031\" < 20",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:902"
  ]
}
```

### Aggregated metric representing the fastest (minimum) lap time in seconds for each driver, calculated from the converted lap time values.

```json
{
  "kind": "metric",
  "formula": "MIN((CASE WHEN SUBSTRING(\"lapTimes\".\"XCL_047\", 1, INSTR(\"lapTimes\".\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"lapTimes\".\"XCL_047\", 1, INSTR(\"lapTimes\".\"XCL_047\", ':') - 1) AS REAL) * 60 ELSE 0 END + CASE WHEN SUBSTRING(\"lapTimes\".\"XCL_047\", INSTR(\"lapTimes\".\"XCL_047\", ':') + 1, INSTR(\"lapTimes\".\"XCL_047\", '.') - INSTR(\"lapTimes\".\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"lapTimes\".\"XCL_047\", INSTR(\"lapTimes\".\"XCL_047\", ':') + 1, INSTR(\"lapTimes\".\"XCL_047\", '.') - INSTR(\"lapTimes\".\"XCL_047\", ':') - 1) AS REAL) ELSE 0 END + CASE WHEN SUBSTRING(\"lapTimes\".\"XCL_047\", INSTR(\"lapTimes\".\"XCL_047\", '.') + 1) <> '' THEN CAST(SUBSTRING(\"lapTimes\".\"XCL_047\", INSTR(\"lapTimes\".\"XCL_047\", '.') + 1) AS REAL) / 1000 ELSE 0 END))",
  "grain": [
    "\"lapTimes\".\"XCL_044\""
  ],
  "population_scope": "SELECT \"XCL_044\", MIN(\"time_in_seconds\") AS min_time_in_seconds FROM lap_times_in_seconds GROUP BY \"XCL_044\"",
  "upstream_scopes": [
    "SELECT \"XCL_044\", (CASE WHEN SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) AS REAL) * 60 ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) AS REAL) ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) AS REAL) / 1000 ELSE 0 END) AS time_in_seconds FROM lapTimes"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1011"
  ]
}
```

### "drivers"."XCL_038" = 'Paul' AND "drivers"."XCL_039" = 'di Resta'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Paul' AND \"drivers\".\"XCL_039\" = 'di Resta'",
  "grain": [],
  "population_scope": "SELECT (SUM(IIF(T2.\"XCL_074\" = 853, T2.\"XCL_089\", 0)) - SUM(IIF(T2.\"XCL_074\" = 854, T2.\"XCL_089\", 0))) * 100 / SUM(IIF(T2.\"XCL_074\" = 853, T2.\"XCL_089\", 0)) FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE T1.\"XCL_038\" = 'Paul' AND T1.\"XCL_039\" = 'di Resta'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:880"
  ]
}
```

### Aggregated sum of the driverStandings.XCL_033 column. The population is restricted to records for the driver with first name 'Michael' and last name '

```json
{
  "kind": "metric",
  "formula": "SUM(\"driverStandings\".\"XCL_033\")",
  "grain": [],
  "population_scope": "SELECT SUM(T2.\"XCL_033\") FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_029\" = T1.\"XCL_034\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T2.\"XCL_028\" INNER JOIN circuits AS T4 ON T4.\"XCL_001\" = T3.\"XCL_068\" WHERE T1.\"XCL_038\" = 'Michael' AND T1.\"XCL_039\" = 'Schumacher' AND T4.\"XCL_003\" = 'Sepang International Circuit'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r1\".\"XCL_033\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      },
      {
        "role": "r1",
        "physical_table": "driverStandings"
      },
      {
        "role": "r2",
        "physical_table": "races"
      },
      {
        "role": "r3",
        "physical_table": "circuits"
      }
    ],
    "scope_sql": "SELECT SUM(\"r1\".\"XCL_033\") AS \"value\" FROM drivers AS \"r0\" INNER JOIN driverStandings AS \"r1\" ON \"r1\".\"XCL_029\" = \"r0\".\"XCL_034\" INNER JOIN races AS \"r2\" ON \"r2\".\"XCL_065\" = \"r1\".\"XCL_028\" INNER JOIN circuits AS \"r3\" ON \"r3\".\"XCL_001\" = \"r2\".\"XCL_068\" WHERE \"r0\".\"XCL_038\" = 'Michael' AND \"r0\".\"XCL_039\" = 'Schumacher' AND \"r3\".\"XCL_003\" = 'Sepang International Circuit'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:903"
  ]
}
```

### Circuit Identifier

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_004\", \"XCL_006\", \"XCL_007\" FROM circuits WHERE \"XCL_005\" = 'Austria'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:978"
  ]
}
```

### "drivers"."XCL_039" = 'Hamilton' AND "races"."XCL_066" >= 2010

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_039\" = 'Hamilton' AND \"races\".\"XCL_066\" >= 2010",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T2.\"XCL_031\" <> 1 THEN T2.\"XCL_031\" END) AS REAL) * 100 / COUNT(T2.\"XCL_027\") FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" WHERE T3.\"XCL_039\" = 'Hamilton' AND T1.\"XCL_066\" >= 2010",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:896"
  ]
}
```

### Result Attribute XCL_084

```json
{
  "kind": "binding",
  "formula": "\"results\".\"XCL_084\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_084\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE T2.\"XCL_074\" = 743 AND T1.\"XCL_038\" = 'Bruce' AND T1.\"XCL_039\" = 'McLaren'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_084\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      },
      {
        "role": "r1",
        "physical_table": "results"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_084\" AS \"value\" FROM drivers AS \"r0\" INNER JOIN results AS \"r1\" ON \"r1\".\"XCL_075\" = \"r0\".\"XCL_034\" WHERE \"r1\".\"XCL_074\" = 743 AND \"r0\".\"XCL_038\" = 'Bruce' AND \"r0\".\"XCL_039\" = 'McLaren'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:873"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE T2.\"XCL_074\" = 872 AND NOT T2.\"XCL_084\" IS NULL ORDER BY T1.\"XCL_040\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:877"
  ]
}
```

### "races"."XCL_066" = 2009 AND "races"."XCL_069" = 'Spanish Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_066\" = 2009 AND \"races\".\"XCL_069\" = 'Spanish Grand Prix'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_066\" = 2009 AND T2.\"XCL_069\" = 'Spanish Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:919"
  ]
}
```

### Fastest Lap Time for Lewis Hamilton

```json
{
  "kind": "binding",
  "formula": "\"lapTimes\".\"XCL_046\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_046\" FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_044\" = T2.\"XCL_034\" WHERE T2.\"XCL_038\" = 'Lewis' AND T2.\"XCL_039\" = 'Hamilton' ORDER BY T1.\"XCL_047\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1012"
  ]
}
```

### Attribute XCL_039 from the drivers table, likely representing a driver name or related descriptive field, for drivers who recorded lap times starting 

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_038\", T2.\"XCL_039\", T2.\"XCL_042\" FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_044\" WHERE T1.\"XCL_043\" = 161 AND T1.\"XCL_047\" LIKE '1:27%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:866"
  ]
}
```

### Driver Attribute XCL_035

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_038\", T3.\"XCL_039\", T3.\"XCL_035\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T1.\"XCL_069\" = 'Canadian Grand Prix' AND T2.\"XCL_087\" = 1 AND T1.\"XCL_066\" = 2007",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      },
      {
        "role": "r1",
        "physical_table": "results"
      },
      {
        "role": "r2",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_035\" AS \"value\" FROM races AS \"r0\" INNER JOIN results AS \"r1\" ON \"r1\".\"XCL_074\" = \"r0\".\"XCL_065\" INNER JOIN drivers AS \"r2\" ON \"r2\".\"XCL_034\" = \"r1\".\"XCL_075\" WHERE \"r0\".\"XCL_069\" = 'Canadian Grand Prix' AND \"r1\".\"XCL_087\" = 1 AND \"r0\".\"XCL_066\" = 2007",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:928"
  ]
}
```

### 2000 Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_069\" FROM races WHERE \"XCL_066\" = 2000",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_069\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_069\" AS \"value\" FROM races AS \"r0\" WHERE \"r0\".\"XCL_066\" = 2000",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:887"
  ]
}
```

### Driver First Name

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_038\", T2.\"XCL_039\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_058\" = T2.\"XCL_034\" INNER JOIN races AS T3 ON T1.\"XCL_057\" = T3.\"XCL_065\" WHERE NOT \"XCL_064\" IS NULL AND T3.\"XCL_066\" = 2008 AND T3.\"XCL_068\" IN (SELECT \"XCL_001\" FROM circuits WHERE \"XCL_003\" = 'Marina Bay Street Circuit') ORDER BY CAST(SUBSTRING(\"XCL_064\", 1, INSTR(\"XCL_064\", ':') - 1) AS INTEGER) * 60 + CAST(SUBSTRING(\"XCL_064\", INSTR(\"XCL_064\", ':') + 1, INSTR(\"XCL_064\", '.') - INSTR(\"XCL_064\", ':') - 1) AS REAL) + CAST(SUBSTRING(\"XCL_064\", INSTR(\"XCL_064\", '.') + 1) AS REAL) / 1000 ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1001"
  ]
}
```

### Driver Identifier 2

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT STRFTIME('%Y', CURRENT_TIMESTAMP) - STRFTIME('%Y', \"XCL_040\"), \"XCL_038\", \"XCL_039\" FROM drivers WHERE \"XCL_041\" = 'Japanese' ORDER BY \"XCL_040\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:898"
  ]
}
```

### Circuit Attribute XCL_006

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_006\", \"XCL_007\" FROM circuits WHERE \"XCL_003\" = 'Silverstone Circuit'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_006\" AS \"value\" FROM circuits AS \"r0\" WHERE \"r0\".\"XCL_003\" = 'Silverstone Circuit'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:910"
  ]
}
```

### "drivers"."XCL_038" = 'Lewis' AND "drivers"."XCL_039" = 'Hamilton' AND "races"."XCL_069" = 'Turkish Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Lewis' AND \"drivers\".\"XCL_039\" = 'Hamilton' AND \"races\".\"XCL_069\" = 'Turkish Grand Prix'",
  "grain": [],
  "population_scope": "SELECT AVG(T2.\"XCL_030\") FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T2.\"XCL_028\" WHERE T1.\"XCL_038\" = 'Lewis' AND T1.\"XCL_039\" = 'Hamilton' AND T3.\"XCL_069\" = 'Turkish Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:995"
  ]
}
```

### NOT AVG(CASE WHEN "results"."XCL_081" = 1 THEN (CAST(SUBSTRING("results"."XCL_084", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING("results"."XCL_084", 3, 2

```json
{
  "kind": "predicate",
  "formula": "NOT AVG(CASE WHEN \"results\".\"XCL_081\" = 1 THEN (CAST(SUBSTRING(\"results\".\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(\"results\".\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(\"results\".\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(\"results\".\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END) IS NULL",
  "grain": [
    "\"races\".\"XCL_066\""
  ],
  "population_scope": "WITH time_in_seconds AS (SELECT T2.\"XCL_066\", T2.\"XCL_065\", T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(T1.\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_084\" IS NULL), champion_time AS (SELECT \"XCL_066\", \"XCL_065\", \"time_seconds\" FROM time_in_seconds WHERE \"XCL_081\" = 1) SELECT \"XCL_066\", AVG(\"time_seconds\") FROM champion_time WHERE \"XCL_066\" < 1975 GROUP BY \"XCL_066\" HAVING NOT AVG(\"time_seconds\") IS NULL",
  "upstream_scopes": [
    "SELECT \"XCL_066\", \"XCL_065\", \"time_seconds\" FROM time_in_seconds WHERE \"XCL_081\" = 1",
    "SELECT T2.\"XCL_066\", T2.\"XCL_065\", T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(T1.\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_084\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:955"
  ]
}
```

### Driver ID (Lap Time)

```json
{
  "kind": "binding",
  "formula": "\"lapTimes\".\"XCL_044\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_044\", (CASE WHEN SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) AS REAL) * 60 ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) AS REAL) ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) AS REAL) / 1000 ELSE 0 END) AS time_in_seconds FROM lapTimes",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_044\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "lapTimes"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_044\" AS \"value\" FROM lapTimes AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1011"
  ]
}
```

### Circuit Attribute XCL_005

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_005\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_005\", \"XCL_006\", \"XCL_007\" FROM circuits WHERE \"XCL_003\" = 'Hungaroring'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_005\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_005\" AS \"value\" FROM circuits AS \"r0\" WHERE \"r0\".\"XCL_003\" = 'Hungaroring'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:993"
  ]
}
```

### Minimum Fastest Lap Time (Austrian GP)

```json
{
  "kind": "metric",
  "formula": "MIN((CAST(SUBSTRING(\"results\".\"XCL_088\", 1, INSTR(\"results\".\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(\"results\".\"XCL_088\", INSTR(\"results\".\"XCL_088\", ':') + 1, INSTR(\"results\".\"XCL_088\", '.') - INSTR(\"results\".\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(\"results\".\"XCL_088\", INSTR(\"results\".\"XCL_088\", '.') + 1) AS REAL) / 1000))",
  "grain": [],
  "population_scope": "SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix'",
  "upstream_scopes": [
    "SELECT T1.\"XCL_074\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1015"
  ]
}
```

### "results"."XCL_081" = 1

```json
{
  "kind": "predicate",
  "formula": "\"results\".\"XCL_081\" = 1",
  "grain": [],
  "population_scope": "SELECT \"XCL_066\", \"XCL_065\", \"time_seconds\" FROM time_in_seconds WHERE \"XCL_081\" = 1",
  "upstream_scopes": [
    "SELECT T2.\"XCL_066\", T2.\"XCL_065\", T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(T1.\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_084\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:955"
  ]
}
```

### Count of Distinct Drivers

```json
{
  "kind": "metric",
  "formula": "COUNT(*)",
  "grain": [],
  "population_scope": "SELECT COUNT(*) FROM (SELECT T1.\"XCL_075\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Chinese Grand Prix' AND T2.\"XCL_066\" = 2008 AND NOT T1.\"XCL_084\" IS NULL GROUP BY T1.\"XCL_075\" HAVING COUNT(T2.\"XCL_065\") > 0)",
  "upstream_scopes": [
    "SELECT T1.\"XCL_075\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Chinese Grand Prix' AND T2.\"XCL_066\" = 2008 AND NOT T1.\"XCL_084\" IS NULL GROUP BY T1.\"XCL_075\" HAVING COUNT(T2.\"XCL_065\") > 0"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:940"
  ]
}
```

### The calendar month extracted from the earliest date in the races table (XCL_070), determined by ordering ascending and taking the first row.

```json
{
  "kind": "binding",
  "formula": "STRFTIME('%m', \"races\".\"XCL_070\")",
  "grain": [],
  "population_scope": "SELECT STRFTIME('%m', \"XCL_070\") FROM races ORDER BY \"XCL_070\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:884"
  ]
}
```

### Counts the number of result records for each driver (XCL_075) in the Canadian Grand Prix where the status code is 3. The grain is per driver, and the 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"results\".\"XCL_075\")",
  "grain": [
    "\"results\".\"XCL_075\""
  ],
  "population_scope": "SELECT COUNT(T1.\"XCL_075\") FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN status AS T3 ON T1.\"XCL_090\" = T3.\"XCL_093\" WHERE T3.\"XCL_093\" = 3 AND T2.\"XCL_069\" = 'Canadian Grand Prix' GROUP BY T1.\"XCL_075\" ORDER BY COUNT(T1.\"XCL_075\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1003"
  ]
}
```

### "races"."XCL_069" = 'Canadian Grand Prix' AND "results"."XCL_087" = 1 AND "races"."XCL_066" = 2007

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Canadian Grand Prix' AND \"results\".\"XCL_087\" = 1 AND \"races\".\"XCL_066\" = 2007",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_038\", T3.\"XCL_039\", T3.\"XCL_035\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T1.\"XCL_069\" = 'Canadian Grand Prix' AND T2.\"XCL_087\" = 1 AND T1.\"XCL_066\" = 2007",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:928"
  ]
}
```

### "races"."XCL_066" = 2011 AND "races"."XCL_069" = 'Australian Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_066\" = 2011 AND \"races\".\"XCL_069\" = 'Australian Grand Prix'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_054\" FROM pitStops AS T1 INNER JOIN races AS T2 ON T1.\"XCL_049\" = T2.\"XCL_065\" WHERE T2.\"XCL_066\" = 2011 AND T2.\"XCL_069\" = 'Australian Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1009"
  ]
}
```

### Driver Standing Points

```json
{
  "kind": "binding",
  "formula": "\"driverStandings\".\"XCL_030\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_038\", T3.\"XCL_039\", T2.\"XCL_030\" FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_069\" = 'Chinese Grand Prix' AND T1.\"XCL_066\" = 2017 ORDER BY T2.\"XCL_030\" DESC LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:893"
  ]
}
```

### Circuit Name

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_005\", T1.\"XCL_004\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_069\" = 'European Grand Prix' ORDER BY T2.\"XCL_066\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:888"
  ]
}
```

### "races"."XCL_069" = 'Chinese Grand Prix' AND "races"."XCL_066" = 2008 AND NOT "results"."XCL_084" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Chinese Grand Prix' AND \"races\".\"XCL_066\" = 2008 AND NOT \"results\".\"XCL_084\" IS NULL",
  "grain": [
    "\"results\".\"XCL_075\""
  ],
  "population_scope": "SELECT T1.\"XCL_075\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Chinese Grand Prix' AND T2.\"XCL_066\" = 2008 AND NOT T1.\"XCL_084\" IS NULL GROUP BY T1.\"XCL_075\" HAVING COUNT(T2.\"XCL_065\") > 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:940"
  ]
}
```

### Aggregated sum of the 'XCL_082' column from the 'results' table, filtered to records associated with the driver identified by first name 'Lewis' and l

```json
{
  "kind": "metric",
  "formula": "SUM(\"results\".\"XCL_082\")",
  "grain": [],
  "population_scope": "SELECT SUM(T2.\"XCL_082\") FROM drivers AS T1 INNER JOIN results AS T2 ON T1.\"XCL_034\" = T2.\"XCL_075\" WHERE T1.\"XCL_038\" = 'Lewis' AND T1.\"XCL_039\" = 'Hamilton'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r1\".\"XCL_082\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      },
      {
        "role": "r1",
        "physical_table": "results"
      }
    ],
    "scope_sql": "SELECT SUM(\"r1\".\"XCL_082\") AS \"value\" FROM drivers AS \"r0\" INNER JOIN results AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_075\" WHERE \"r0\".\"XCL_038\" = 'Lewis' AND \"r0\".\"XCL_039\" = 'Hamilton'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:941"
  ]
}
```

### A flag from the results table (XCL_081) indicating the status of the result. A value of 1 is used to filter for 'champion' or winning results in the s

```json
{
  "kind": "binding",
  "formula": "\"results\".\"XCL_081\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_066\", T2.\"XCL_065\", T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(T1.\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_084\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_081\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_081\" AS \"value\" FROM results AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_074\" = \"r1\".\"XCL_065\" WHERE NOT \"r0\".\"XCL_084\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:955"
  ]
}
```

### Driver Nationality

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_041\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_041\" FROM drivers AS T1 ORDER BY JULIANDAY(T1.\"XCL_040\") DESC LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:967"
  ]
}
```

### Driver Attribute XCL_039

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_038\", T2.\"XCL_039\" FROM results AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_075\" = T2.\"XCL_034\" WHERE STRFTIME('%Y', T2.\"XCL_040\") > '1975' AND T1.\"XCL_087\" = 2",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_039\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_039\" AS \"value\" FROM results AS \"r0\" INNER JOIN drivers AS \"r1\" ON \"r0\".\"XCL_075\" = \"r1\".\"XCL_034\" WHERE STRFTIME('%Y', \"r1\".\"XCL_040\") > '1975' AND \"r0\".\"XCL_087\" = 2",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:956"
  ]
}
```

### NOT "circuits"."XCL_005" IN ('Bahrain', 'China', 'Singapore', 'Japan', 'Korea', 'Turkey', 'UAE', 'Malaysia', 'Spain', 'Monaco', 'Azerbaijan', 'Austria

```json
{
  "kind": "predicate",
  "formula": "NOT \"circuits\".\"XCL_005\" IN ('Bahrain', 'China', 'Singapore', 'Japan', 'Korea', 'Turkey', 'UAE', 'Malaysia', 'Spain', 'Monaco', 'Azerbaijan', 'Austria', 'Belgium', 'France', 'Germany', 'Hungary', 'Italy', 'UK') AND \"races\".\"XCL_066\" = 2010",
  "grain": [],
  "population_scope": "SELECT COUNT(T3.\"XCL_065\") FROM circuits AS T1 INNER JOIN races AS T3 ON T3.\"XCL_068\" = T1.\"XCL_001\" WHERE NOT T1.\"XCL_005\" IN ('Bahrain', 'China', 'Singapore', 'Japan', 'Korea', 'Turkey', 'UAE', 'Malaysia', 'Spain', 'Monaco', 'Azerbaijan', 'Austria', 'Belgium', 'France', 'Germany', 'Hungary', 'Italy', 'UK') AND T3.\"XCL_066\" = 2010",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:852"
  ]
}
```

### Driver Standing Position

```json
{
  "kind": "binding",
  "formula": "\"driverStandings\".\"XCL_030\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_069\", T2.\"XCL_030\" FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" WHERE T3.\"XCL_038\" = 'Lewis' AND T3.\"XCL_039\" = 'Hamilton' ORDER BY T1.\"XCL_066\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:906"
  ]
}
```

### Driver Identifier XCL_038

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE T2.\"XCL_074\" = 592 AND NOT T2.\"XCL_084\" IS NULL AND NOT T1.\"XCL_040\" IS NULL ORDER BY T1.\"XCL_040\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:865"
  ]
}
```

### "races"."XCL_069" = 'Singapore Grand Prix' AND "races"."XCL_066" = 2010

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Singapore Grand Prix' AND \"races\".\"XCL_066\" = 2010",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_038\", T3.\"XCL_039\" FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_069\" = 'Singapore Grand Prix' AND T1.\"XCL_066\" = 2010 ORDER BY T2.\"XCL_031\" ASC",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:891"
  ]
}
```

### "drivers"."XCL_041" = 'Dutch'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_041\" = 'Dutch'",
  "grain": [],
  "population_scope": "SELECT COUNT(*) FROM (SELECT T1.\"XCL_041\" FROM drivers AS T1 ORDER BY JULIANDAY(T1.\"XCL_040\") DESC LIMIT 3) AS T3 WHERE T3.\"XCL_041\" = 'Dutch'",
  "upstream_scopes": [
    "SELECT T1.\"XCL_041\" FROM drivers AS T1 ORDER BY JULIANDAY(T1.\"XCL_040\") DESC LIMIT 3"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:967"
  ]
}
```

### Distinct values of the driver identifier column (XCL_041) from the drivers table, filtered to drivers who participated in qualifying session 347 with 

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_041\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_041\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 347 AND T1.\"XCL_063\" LIKE '1:15%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:871"
  ]
}
```

### "results"."XCL_087" < 11 AND "races"."XCL_066" = 2006 AND "races"."XCL_069" = 'United States Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"results\".\"XCL_087\" < 11 AND \"races\".\"XCL_066\" = 2006 AND \"races\".\"XCL_069\" = 'United States Grand Prix'",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_088\") FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T1.\"XCL_087\" < 11 AND T2.\"XCL_066\" = 2006 AND T2.\"XCL_069\" = 'United States Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:987"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_034\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_034\", T2.\"XCL_037\" FROM results AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_075\" = T2.\"XCL_034\" WHERE STRFTIME('%Y', T2.\"XCL_040\") = '1971' AND NOT T1.\"XCL_088\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_034\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_034\" AS \"value\" FROM results AS \"r0\" INNER JOIN drivers AS \"r1\" ON \"r0\".\"XCL_075\" = \"r1\".\"XCL_034\" WHERE STRFTIME('%Y', \"r1\".\"XCL_040\") = '1971' AND NOT \"r0\".\"XCL_088\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:972"
  ]
}
```

### Race Name

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\", T1.\"XCL_004\", T2.\"XCL_069\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_005\" = 'USA' AND T2.\"XCL_066\" = 2006",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_069\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_069\" AS \"value\" FROM circuits AS \"r0\" INNER JOIN races AS \"r1\" ON \"r1\".\"XCL_068\" = \"r0\".\"XCL_001\" WHERE \"r0\".\"XCL_005\" = 'USA' AND \"r1\".\"XCL_066\" = 2006",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:900"
  ]
}
```

### STRFTIME('%Y', "races"."XCL_070") BETWEEN '1990' AND '2000'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"races\".\"XCL_070\") BETWEEN '1990' AND '2000'",
  "grain": [
    "\"circuits\".\"XCL_003\""
  ],
  "population_scope": "SELECT DISTINCT T1.\"XCL_003\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE STRFTIME('%Y', T2.\"XCL_070\") BETWEEN '1990' AND '2000' GROUP BY T1.\"XCL_003\" HAVING COUNT(T2.\"XCL_065\") = 4",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:899"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_037\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_037\" FROM drivers WHERE \"XCL_041\" = 'American'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_037\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_037\" AS \"value\" FROM drivers AS \"r0\" WHERE \"r0\".\"XCL_041\" = 'American'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:964"
  ]
}
```

### "driverStandings"."XCL_033" >= 1

```json
{
  "kind": "predicate",
  "formula": "\"driverStandings\".\"XCL_033\" >= 1",
  "grain": [
    "\"drivers\".\"XCL_038\"",
    "\"drivers\".\"XCL_039\"",
    "\"drivers\".\"XCL_041\""
  ],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_041\", MAX(T2.\"XCL_030\") FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_029\" = T1.\"XCL_034\" WHERE T2.\"XCL_033\" >= 1 GROUP BY T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_041\" ORDER BY COUNT(T2.\"XCL_033\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:897"
  ]
}
```

### "drivers"."XCL_041" = 'Italian' AND "results"."XCL_084" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_041\" = 'Italian' AND \"results\".\"XCL_084\" IS NULL",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_075\") FROM results AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_075\" = T2.\"XCL_034\" WHERE T2.\"XCL_041\" = 'Italian' AND T1.\"XCL_084\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:957"
  ]
}
```

### Count of Dutch Drivers in Top 3 Recent

```json
{
  "kind": "metric",
  "formula": "COUNT(*)",
  "grain": [],
  "population_scope": "SELECT COUNT(*) FROM (SELECT T1.\"XCL_041\" FROM drivers AS T1 ORDER BY JULIANDAY(T1.\"XCL_040\") DESC LIMIT 3) AS T3 WHERE T3.\"XCL_041\" = 'Dutch'",
  "upstream_scopes": [
    "SELECT T1.\"XCL_041\" FROM drivers AS T1 ORDER BY JULIANDAY(T1.\"XCL_040\") DESC LIMIT 3"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:967"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_035\" FROM drivers WHERE \"XCL_041\" = 'German' ORDER BY JULIANDAY(\"XCL_040\") ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:971"
  ]
}
```

### "results"."XCL_083" > 50 AND "constructors"."XCL_025" = 'French'

```json
{
  "kind": "predicate",
  "formula": "\"results\".\"XCL_083\" > 50 AND \"constructors\".\"XCL_025\" = 'French'",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T2.\"XCL_022\") FROM results AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_076\" = T2.\"XCL_022\" WHERE T1.\"XCL_083\" > 50 AND T2.\"XCL_025\" = 'French'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:953"
  ]
}
```

### Driver Nationality

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_042\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_042\" FROM drivers AS T1 INNER JOIN results AS T2 ON T1.\"XCL_034\" = T2.\"XCL_075\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T2.\"XCL_074\" WHERE T3.\"XCL_069\" = 'Australian Grand Prix' AND T2.\"XCL_084\" LIKE '_:%:__.___' AND T3.\"XCL_066\" = 2008",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_042\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      },
      {
        "role": "r1",
        "physical_table": "results"
      },
      {
        "role": "r2",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_042\" AS \"value\" FROM drivers AS \"r0\" INNER JOIN results AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_075\" INNER JOIN races AS \"r2\" ON \"r2\".\"XCL_065\" = \"r1\".\"XCL_074\" WHERE \"r2\".\"XCL_069\" = 'Australian Grand Prix' AND \"r1\".\"XCL_084\" LIKE '_:%:__.___' AND \"r2\".\"XCL_066\" = 2008",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:938"
  ]
}
```

### "drivers"."XCL_041" = 'Austrian' AND STRFTIME('%Y', "drivers"."XCL_040") BETWEEN '1981' AND '1991'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_041\" = 'Austrian' AND STRFTIME('%Y', \"drivers\".\"XCL_040\") BETWEEN '1981' AND '1991'",
  "grain": [],
  "population_scope": "SELECT \"XCL_038\", \"XCL_039\", \"XCL_040\" FROM drivers WHERE \"XCL_041\" = 'Austrian' AND STRFTIME('%Y', \"XCL_040\") BETWEEN '1981' AND '1991'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:991"
  ]
}
```

### Minimum non-null result value for Lewis Hamilton

```json
{
  "kind": "binding",
  "formula": "\"results\".\"XCL_088\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_088\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE T1.\"XCL_038\" = 'Lewis' AND T1.\"XCL_039\" = 'Hamilton' AND NOT T2.\"XCL_088\" IS NULL ORDER BY T2.\"XCL_088\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:926"
  ]
}
```

### Distinct values of the race identifier column (XCL_069) from the races table, filtered to include only races associated with circuits located in Spain

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_069\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_005\" = 'Spain'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:853"
  ]
}
```

### Distinct values of the race identifier column (XCL_071) from the races table, filtered to races associated with the 'Sepang International Circuit'.

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_071\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_071\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Sepang International Circuit'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:856"
  ]
}
```

### Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_069\" FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" WHERE T3.\"XCL_038\" = 'Alex' AND T3.\"XCL_039\" = 'Yoong' AND T2.\"XCL_031\" < 20",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_069\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      },
      {
        "role": "r1",
        "physical_table": "driverStandings"
      },
      {
        "role": "r2",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_069\" AS \"value\" FROM races AS \"r0\" INNER JOIN driverStandings AS \"r1\" ON \"r1\".\"XCL_028\" = \"r0\".\"XCL_065\" INNER JOIN drivers AS \"r2\" ON \"r2\".\"XCL_034\" = \"r1\".\"XCL_029\" WHERE \"r2\".\"XCL_038\" = 'Alex' AND \"r2\".\"XCL_039\" = 'Yoong' AND \"r1\".\"XCL_031\" < 20",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:902"
  ]
}
```

### "drivers"."XCL_041" = 'Japanese'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_041\" = 'Japanese'",
  "grain": [],
  "population_scope": "SELECT STRFTIME('%Y', CURRENT_TIMESTAMP) - STRFTIME('%Y', \"XCL_040\"), \"XCL_038\", \"XCL_039\" FROM drivers WHERE \"XCL_041\" = 'Japanese' ORDER BY \"XCL_040\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:898"
  ]
}
```

### The value of the 'XCL_005' column from the 'circuits' table for the single row with the highest value in the 'XCL_008' column. Represents the identifi

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_005\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_005\" FROM circuits ORDER BY \"XCL_008\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:913"
  ]
}
```

### Record Holder Driver ID

```json
{
  "kind": "binding",
  "formula": "T1.\"XCL_075\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_074\", T1.\"XCL_075\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" INNER JOIN (SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix') AS T4 ON (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) = T4.\"min_time_in_seconds\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix'",
  "upstream_scopes": [
    "SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix'",
    "SELECT T1.\"XCL_074\", T1.\"XCL_075\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1016"
  ]
}
```

### "circuits"."XCL_003" = 'Brands Hatch' AND "races"."XCL_069" = 'British Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_003\" = 'Brands Hatch' AND \"races\".\"XCL_069\" = 'British Grand Prix'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_070\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Brands Hatch' AND T2.\"XCL_069\" = 'British Grand Prix' ORDER BY T2.\"XCL_066\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:889"
  ]
}
```

### Pre-1975 Race Year

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_066\"",
  "grain": [
    "\"races\".\"XCL_066\""
  ],
  "population_scope": "WITH time_in_seconds AS (SELECT T2.\"XCL_066\", T2.\"XCL_065\", T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(T1.\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_084\" IS NULL), champion_time AS (SELECT \"XCL_066\", \"XCL_065\", \"time_seconds\" FROM time_in_seconds WHERE \"XCL_081\" = 1) SELECT \"XCL_066\", AVG(\"time_seconds\") FROM champion_time WHERE \"XCL_066\" < 1975 GROUP BY \"XCL_066\" HAVING NOT AVG(\"time_seconds\") IS NULL",
  "upstream_scopes": [
    "SELECT \"XCL_066\", \"XCL_065\", \"time_seconds\" FROM time_in_seconds WHERE \"XCL_081\" = 1",
    "SELECT T2.\"XCL_066\", T2.\"XCL_065\", T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(T1.\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_084\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:955"
  ]
}
```

### Attribute XCL_007 associated with circuits in Austria. Returned as part of a distinct set of circuit attributes.

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_004\", \"XCL_006\", \"XCL_007\" FROM circuits WHERE \"XCL_005\" = 'Austria'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:978"
  ]
}
```

### "drivers"."XCL_038" = 'Lewis' AND "drivers"."XCL_039" = 'Hamilton'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Lewis' AND \"drivers\".\"XCL_039\" = 'Hamilton'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_069\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T3.\"XCL_038\" = 'Lewis' AND T3.\"XCL_039\" = 'Hamilton'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:929"
  ]
}
```

### Aggregates the number of unique constructors (identified by XCL_022) who are French (XCL_025 = 'French') and have associated results where XCL_083 is 

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"constructors\".\"XCL_022\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T2.\"XCL_022\") FROM results AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_076\" = T2.\"XCL_022\" WHERE T1.\"XCL_083\" > 50 AND T2.\"XCL_025\" = 'French'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r1\".\"XCL_022\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "constructors"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r1\".\"XCL_022\") AS \"value\" FROM results AS \"r0\" INNER JOIN constructors AS \"r1\" ON \"r0\".\"XCL_076\" = \"r1\".\"XCL_022\" WHERE \"r0\".\"XCL_083\" > 50 AND \"r1\".\"XCL_025\" = 'French'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:953"
  ]
}
```

### "races"."XCL_069" = 'Chinese Grand Prix' AND "races"."XCL_066" = 2017

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Chinese Grand Prix' AND \"races\".\"XCL_066\" = 2017",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_038\", T3.\"XCL_039\", T2.\"XCL_030\" FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_069\" = 'Chinese Grand Prix' AND T1.\"XCL_066\" = 2017 ORDER BY T2.\"XCL_030\" DESC LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:893"
  ]
}
```

### Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_069\", T1.\"XCL_066\" FROM races AS T1 INNER JOIN lapTimes AS T2 ON T2.\"XCL_043\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_044\" WHERE T3.\"XCL_038\" = 'Michael' AND T3.\"XCL_039\" = 'Schumacher' ORDER BY T2.\"XCL_048\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:904"
  ]
}
```

### Aggregated sum of the 'XCL_033' column from the 'driverStandings' table. The computation is constrained to the single driver record identified by the 

```json
{
  "kind": "metric",
  "formula": "SUM(\"driverStandings\".\"XCL_033\")",
  "grain": [],
  "population_scope": "SELECT SUM(T1.\"XCL_033\"), T2.\"XCL_038\", T2.\"XCL_039\" FROM driverStandings AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_029\" = T2.\"XCL_034\" ORDER BY T2.\"XCL_040\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1004"
  ]
}
```

### Aggregates the total number of race records (identified by XCL_065) for the year 2010 (XCL_066 = 2010) where the associated circuit's country (XCL_005

```json
{
  "kind": "metric",
  "formula": "COUNT(\"races\".\"XCL_065\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T3.\"XCL_065\") FROM circuits AS T1 INNER JOIN races AS T3 ON T3.\"XCL_068\" = T1.\"XCL_001\" WHERE NOT T1.\"XCL_005\" IN ('Bahrain', 'China', 'Singapore', 'Japan', 'Korea', 'Turkey', 'UAE', 'Malaysia', 'Spain', 'Monaco', 'Azerbaijan', 'Austria', 'Belgium', 'France', 'Germany', 'Hungary', 'Italy', 'UK') AND T3.\"XCL_066\" = 2010",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_065\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_065\") AS \"value\" FROM circuits AS \"r0\" INNER JOIN races AS \"r1\" ON \"r1\".\"XCL_068\" = \"r0\".\"XCL_001\" WHERE NOT \"r0\".\"XCL_005\" IN ('Bahrain', 'China', 'Singapore', 'Japan', 'Korea', 'Turkey', 'UAE', 'Malaysia', 'Spain', 'Monaco', 'Azerbaijan', 'Austria', 'Belgium', 'France', 'Germany', 'Hungary', 'Italy', 'UK') AND \"r1\".\"XCL_066\" = 2010",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:852"
  ]
}
```

### Driver Name

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_038\", T3.\"XCL_039\", T2.\"XCL_030\" FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" ORDER BY T2.\"XCL_030\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:892"
  ]
}
```

### "results"."XCL_087" = 2 AND "races"."XCL_069" = 'Chinese Grand Prix' AND "races"."XCL_066" = 2008

```json
{
  "kind": "predicate",
  "formula": "\"results\".\"XCL_087\" = 2 AND \"races\".\"XCL_069\" = 'Chinese Grand Prix' AND \"races\".\"XCL_066\" = 2008",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_084\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T1.\"XCL_087\" = 2 AND T2.\"XCL_069\" = 'Chinese Grand Prix' AND T2.\"XCL_066\" = 2008",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:937"
  ]
}
```

### The value of column XCL_045 from the lapTimes table. In this query, it is used as the sorting key in descending order to identify the maximum value, a

```json
{
  "kind": "binding",
  "formula": "\"lapTimes\".\"XCL_045\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_045\", T2.\"XCL_069\", T2.\"XCL_066\", T1.\"XCL_004\" FROM circuits AS T1 INNER JOIN races AS T2 ON T1.\"XCL_001\" = T2.\"XCL_068\" INNER JOIN lapTimes AS T3 ON T3.\"XCL_043\" = T2.\"XCL_065\" ORDER BY T3.\"XCL_045\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:908"
  ]
}
```

### "circuits"."XCL_003" IN ('Silverstone Circuit', 'Hockenheimring', 'Hungaroring')

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_003\" IN ('Silverstone Circuit', 'Hockenheimring', 'Hungaroring')",
  "grain": [],
  "population_scope": "SELECT \"XCL_003\" FROM circuits WHERE \"XCL_003\" IN ('Silverstone Circuit', 'Hockenheimring', 'Hungaroring') ORDER BY \"XCL_006\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:911"
  ]
}
```

### Race Attribute XCL_070

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_070\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_070\", T2.\"XCL_071\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_066\" = 2010 AND T2.\"XCL_069\" = 'Abu Dhabi Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_070\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_070\" AS \"value\" FROM circuits AS \"r0\" INNER JOIN races AS \"r1\" ON \"r1\".\"XCL_068\" = \"r0\".\"XCL_001\" WHERE \"r1\".\"XCL_066\" = 2010 AND \"r1\".\"XCL_069\" = 'Abu Dhabi Grand Prix'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:922"
  ]
}
```

### "races"."XCL_069" = 'French Grand Prix' AND "lapTimes"."XCL_045" = 3

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'French Grand Prix' AND \"lapTimes\".\"XCL_045\" = 3",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_044\" FROM lapTimes AS T1 INNER JOIN races AS T2 ON T1.\"XCL_043\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'French Grand Prix' AND T1.\"XCL_045\" = 3 ORDER BY T1.\"XCL_047\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:985"
  ]
}
```

### Champion Time in Seconds

```json
{
  "kind": "binding",
  "formula": "CASE WHEN \"results\".\"XCL_081\" = 1 THEN (CAST(SUBSTRING(\"results\".\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(\"results\".\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(\"results\".\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(\"results\".\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END",
  "grain": [],
  "population_scope": "SELECT \"XCL_066\", \"XCL_065\", \"time_seconds\" FROM time_in_seconds WHERE \"XCL_081\" = 1",
  "upstream_scopes": [
    "SELECT T2.\"XCL_066\", T2.\"XCL_065\", T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(T1.\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_084\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:955"
  ]
}
```

### Circuit Identifier

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_009\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_009\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Sepang International Circuit'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:855"
  ]
}
```

### Calculated metric converting the raw lap time string (XCL_047) from 'MM:SS.mmm' format into a numeric value in seconds. Handles missing minutes, secon

```json
{
  "kind": "binding",
  "formula": "(CASE WHEN SUBSTRING(\"lapTimes\".\"XCL_047\", 1, INSTR(\"lapTimes\".\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"lapTimes\".\"XCL_047\", 1, INSTR(\"lapTimes\".\"XCL_047\", ':') - 1) AS REAL) * 60 ELSE 0 END + CASE WHEN SUBSTRING(\"lapTimes\".\"XCL_047\", INSTR(\"lapTimes\".\"XCL_047\", ':') + 1, INSTR(\"lapTimes\".\"XCL_047\", '.') - INSTR(\"lapTimes\".\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"lapTimes\".\"XCL_047\", INSTR(\"lapTimes\".\"XCL_047\", ':') + 1, INSTR(\"lapTimes\".\"XCL_047\", '.') - INSTR(\"lapTimes\".\"XCL_047\", ':') - 1) AS REAL) ELSE 0 END + CASE WHEN SUBSTRING(\"lapTimes\".\"XCL_047\", INSTR(\"lapTimes\".\"XCL_047\", '.') + 1) <> '' THEN CAST(SUBSTRING(\"lapTimes\".\"XCL_047\", INSTR(\"lapTimes\".\"XCL_047\", '.') + 1) AS REAL) / 1000 ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT \"XCL_044\", (CASE WHEN SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) AS REAL) * 60 ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) AS REAL) ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) AS REAL) / 1000 ELSE 0 END) AS time_in_seconds FROM lapTimes",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "(CASE WHEN SUBSTRING(\"r0\".\"XCL_047\", 1, INSTR(\"r0\".\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"r0\".\"XCL_047\", 1, INSTR(\"r0\".\"XCL_047\", ':') - 1) AS REAL) * 60 ELSE 0 END + CASE WHEN SUBSTRING(\"r0\".\"XCL_047\", INSTR(\"r0\".\"XCL_047\", ':') + 1, INSTR(\"r0\".\"XCL_047\", '.') - INSTR(\"r0\".\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"r0\".\"XCL_047\", INSTR(\"r0\".\"XCL_047\", ':') + 1, INSTR(\"r0\".\"XCL_047\", '.') - INSTR(\"r0\".\"XCL_047\", ':') - 1) AS REAL) ELSE 0 END + CASE WHEN SUBSTRING(\"r0\".\"XCL_047\", INSTR(\"r0\".\"XCL_047\", '.') + 1) <> '' THEN CAST(SUBSTRING(\"r0\".\"XCL_047\", INSTR(\"r0\".\"XCL_047\", '.') + 1) AS REAL) / 1000 ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "lapTimes"
      }
    ],
    "scope_sql": "SELECT (CASE WHEN SUBSTRING(\"r0\".\"XCL_047\", 1, INSTR(\"r0\".\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"r0\".\"XCL_047\", 1, INSTR(\"r0\".\"XCL_047\", ':') - 1) AS REAL) * 60 ELSE 0 END + CASE WHEN SUBSTRING(\"r0\".\"XCL_047\", INSTR(\"r0\".\"XCL_047\", ':') + 1, INSTR(\"r0\".\"XCL_047\", '.') - INSTR(\"r0\".\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"r0\".\"XCL_047\", INSTR(\"r0\".\"XCL_047\", ':') + 1, INSTR(\"r0\".\"XCL_047\", '.') - INSTR(\"r0\".\"XCL_047\", ':') - 1) AS REAL) ELSE 0 END + CASE WHEN SUBSTRING(\"r0\".\"XCL_047\", INSTR(\"r0\".\"XCL_047\", '.') + 1) <> '' THEN CAST(SUBSTRING(\"r0\".\"XCL_047\", INSTR(\"r0\".\"XCL_047\", '.') + 1) AS REAL) / 1000 ELSE 0 END) AS \"value\" FROM lapTimes AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1011"
  ]
}
```

### Driver XCL_038 Attribute

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT SUM(T1.\"XCL_033\"), T2.\"XCL_038\", T2.\"XCL_039\" FROM driverStandings AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_029\" = T2.\"XCL_034\" ORDER BY T2.\"XCL_040\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1004"
  ]
}
```

### Returns the value of column XCL_092 from the seasons table for seasons associated with races where the race attribute XCL_065 equals 901. The grain is

```json
{
  "kind": "binding",
  "formula": "\"seasons\".\"XCL_092\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_092\" FROM races AS T1 INNER JOIN seasons AS T2 ON T2.\"XCL_091\" = T1.\"XCL_066\" WHERE T1.\"XCL_065\" = 901",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_092\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      },
      {
        "role": "r1",
        "physical_table": "seasons"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_092\" AS \"value\" FROM races AS \"r0\" INNER JOIN seasons AS \"r1\" ON \"r1\".\"XCL_091\" = \"r0\".\"XCL_066\" WHERE \"r0\".\"XCL_065\" = 901",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:863",
    "bird_dev:875"
  ]
}
```

### Driver XCL_039 Attribute

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT SUM(T1.\"XCL_033\"), T2.\"XCL_038\", T2.\"XCL_039\" FROM driverStandings AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_029\" = T2.\"XCL_034\" ORDER BY T2.\"XCL_040\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1004"
  ]
}
```

### Driver Last Name

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_038\", T3.\"XCL_039\", T2.\"XCL_030\" FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_069\" = 'Chinese Grand Prix' AND T1.\"XCL_066\" = 2017 ORDER BY T2.\"XCL_030\" DESC LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:893"
  ]
}
```

### "races"."XCL_069" = 'Singapore Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Singapore Grand Prix'",
  "grain": [],
  "population_scope": "SELECT \"XCL_066\" FROM races WHERE \"XCL_069\" = 'Singapore Grand Prix' ORDER BY \"XCL_066\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:882"
  ]
}
```

### Constructor Identifier

```json
{
  "kind": "binding",
  "formula": "\"constructors\".\"XCL_025\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_025\" FROM constructorResults AS T1 INNER JOIN constructors AS T2 ON T2.\"XCL_022\" = T1.\"XCL_012\" WHERE T1.\"XCL_011\" = 24 AND T1.\"XCL_013\" = 1",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_025\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "constructorResults"
      },
      {
        "role": "r1",
        "physical_table": "constructors"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_025\" AS \"value\" FROM constructorResults AS \"r0\" INNER JOIN constructors AS \"r1\" ON \"r1\".\"XCL_022\" = \"r0\".\"XCL_012\" WHERE \"r0\".\"XCL_011\" = 24 AND \"r0\".\"XCL_013\" = 1",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:858"
  ]
}
```

### "constructors"."XCL_024" = 'Renault'

```json
{
  "kind": "predicate",
  "formula": "\"constructors\".\"XCL_024\" = 'Renault'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_019\" FROM constructorStandings AS T1 INNER JOIN constructors AS T2 ON T2.\"XCL_022\" = T1.\"XCL_017\" WHERE T2.\"XCL_024\" = 'Renault'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:851"
  ]
}
```

### Driver Attribute XCL_039

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_038\", T3.\"XCL_039\", T3.\"XCL_035\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T1.\"XCL_069\" = 'Canadian Grand Prix' AND T2.\"XCL_087\" = 1 AND T1.\"XCL_066\" = 2007",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_039\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      },
      {
        "role": "r1",
        "physical_table": "results"
      },
      {
        "role": "r2",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_039\" AS \"value\" FROM races AS \"r0\" INNER JOIN results AS \"r1\" ON \"r1\".\"XCL_074\" = \"r0\".\"XCL_065\" INNER JOIN drivers AS \"r2\" ON \"r2\".\"XCL_034\" = \"r1\".\"XCL_075\" WHERE \"r0\".\"XCL_069\" = 'Canadian Grand Prix' AND \"r1\".\"XCL_087\" = 1 AND \"r0\".\"XCL_066\" = 2007",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:928"
  ]
}
```

### "races"."XCL_069" = 'Austrian Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Austrian Grand Prix'",
  "grain": [],
  "population_scope": "WITH fastest_lap_times AS (SELECT T1.\"XCL_074\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL) SELECT T2.\"XCL_069\" FROM races AS T2 INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" INNER JOIN results AS T1 ON T2.\"XCL_065\" = T1.\"XCL_074\" INNER JOIN (SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix') AS T4 ON (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) = T4.\"min_time_in_seconds\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix'",
  "upstream_scopes": [
    "SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix'",
    "SELECT T1.\"XCL_074\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1015"
  ]
}
```

### "qualifying"."XCL_057" = 347 AND "qualifying"."XCL_063" LIKE '1:15%'

```json
{
  "kind": "predicate",
  "formula": "\"qualifying\".\"XCL_057\" = 347 AND \"qualifying\".\"XCL_063\" LIKE '1:15%'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_041\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 347 AND T1.\"XCL_063\" LIKE '1:15%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:871"
  ]
}
```

### "races"."XCL_069" = 'Austrian Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Austrian Grand Prix'",
  "grain": [],
  "population_scope": "SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix'",
  "upstream_scopes": [
    "SELECT T1.\"XCL_074\", T1.\"XCL_075\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1016"
  ]
}
```

### "races"."XCL_070" = '2015-11-29' AND NOT "results"."XCL_084" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_070\" = '2015-11-29' AND NOT \"results\".\"XCL_084\" IS NULL",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_075\") FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" WHERE T1.\"XCL_070\" = '2015-11-29' AND NOT T2.\"XCL_084\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:864"
  ]
}
```

### "races"."XCL_070" BETWEEN '2000-01-01' AND '2010-12-31'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_070\" BETWEEN '2000-01-01' AND '2010-12-31'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN \"XCL_066\" BETWEEN 2000 AND 2010 THEN 1 ELSE 0 END) AS REAL) / 10 FROM races WHERE \"XCL_070\" BETWEEN '2000-01-01' AND '2010-12-31'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:996"
  ]
}
```

### Average XCL_089

```json
{
  "kind": "metric",
  "formula": "AVG(\"results\".\"XCL_089\")",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_089\") FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_066\" = 2009 AND T2.\"XCL_069\" = 'Spanish Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_089\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_089\") AS \"value\" FROM results AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_074\" = \"r1\".\"XCL_065\" WHERE \"r1\".\"XCL_066\" = 2009 AND \"r1\".\"XCL_069\" = 'Spanish Grand Prix'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:960"
  ]
}
```

### Circuit Identifier

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_006\", T1.\"XCL_007\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Abu Dhabi Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:857"
  ]
}
```

### Constructor Name

```json
{
  "kind": "binding",
  "formula": "\"constructors\".\"XCL_024\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_024\" FROM constructorStandings AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_017\" = T2.\"XCL_022\" WHERE T1.\"XCL_018\" = 0 AND T1.\"XCL_016\" = 291",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_024\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "constructorStandings"
      },
      {
        "role": "r1",
        "physical_table": "constructors"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_024\" AS \"value\" FROM constructorStandings AS \"r0\" INNER JOIN constructors AS \"r1\" ON \"r0\".\"XCL_017\" = \"r1\".\"XCL_022\" WHERE \"r0\".\"XCL_018\" = 0 AND \"r0\".\"XCL_016\" = 291",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:950"
  ]
}
```

### Distinct values of the driver identifier column (XCL_041) from the drivers table, filtered to drivers who participated in qualifying session 355 with 

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_041\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_041\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 355 AND T1.\"XCL_063\" LIKE '1:40%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:860"
  ]
}
```

### Circuit Identifier

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_006\", T3.\"XCL_007\" FROM lapTimes AS T1 INNER JOIN races AS T2 ON T1.\"XCL_043\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T1.\"XCL_047\" = '1:29.488'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "lapTimes"
      },
      {
        "role": "r1",
        "physical_table": "races"
      },
      {
        "role": "r2",
        "physical_table": "circuits"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_006\" AS \"value\" FROM lapTimes AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_043\" = \"r1\".\"XCL_065\" INNER JOIN circuits AS \"r2\" ON \"r1\".\"XCL_068\" = \"r2\".\"XCL_001\" WHERE \"r0\".\"XCL_047\" = '1:29.488'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1017"
  ]
}
```

### "results"."XCL_074" = 592 AND NOT "results"."XCL_084" IS NULL AND NOT "drivers"."XCL_040" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"results\".\"XCL_074\" = 592 AND NOT \"results\".\"XCL_084\" IS NULL AND NOT \"drivers\".\"XCL_040\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE T2.\"XCL_074\" = 592 AND NOT T2.\"XCL_084\" IS NULL AND NOT T1.\"XCL_040\" IS NULL ORDER BY T1.\"XCL_040\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:865"
  ]
}
```

### Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_069\" FROM races WHERE \"XCL_066\" = 2005 ORDER BY \"XCL_069\" DESC",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_069\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_069\" AS \"value\" FROM races AS \"r0\" WHERE \"r0\".\"XCL_066\" = 2005",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:883"
  ]
}
```

### "races"."XCL_069" = 'European Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'European Grand Prix'",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T1.\"XCL_005\" = 'Germany' THEN T2.\"XCL_068\" END) AS REAL) * 100 / COUNT(T2.\"XCL_068\") FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_069\" = 'European Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:909"
  ]
}
```

### Driver ID (Final Output)

```json
{
  "kind": "binding",
  "formula": "T1.\"XCL_044\"",
  "grain": [],
  "population_scope": "WITH lap_times_in_seconds AS (SELECT \"XCL_044\", (CASE WHEN SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) AS REAL) * 60 ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) AS REAL) ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) AS REAL) / 1000 ELSE 0 END) AS time_in_seconds FROM lapTimes) SELECT T2.\"XCL_038\", T2.\"XCL_039\", T1.\"XCL_044\" FROM (SELECT \"XCL_044\", MIN(\"time_in_seconds\") AS min_time_in_seconds FROM lap_times_in_seconds GROUP BY \"XCL_044\") AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_044\" = T2.\"XCL_034\" ORDER BY T1.\"min_time_in_seconds\" ASC LIMIT 20",
  "upstream_scopes": [
    "SELECT \"XCL_044\", (CASE WHEN SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) AS REAL) * 60 ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) AS REAL) ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) AS REAL) / 1000 ELSE 0 END) AS time_in_seconds FROM lapTimes",
    "SELECT \"XCL_044\", MIN(\"time_in_seconds\") AS min_time_in_seconds FROM lap_times_in_seconds GROUP BY \"XCL_044\""
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1011"
  ]
}
```

### Race Identifier for Shanghai Circuit

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_066\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_066\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_004\" = 'Shanghai'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_066\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_066\" AS \"value\" FROM circuits AS \"r0\" INNER JOIN races AS \"r1\" ON \"r1\".\"XCL_068\" = \"r0\".\"XCL_001\" WHERE \"r0\".\"XCL_004\" = 'Shanghai'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:848"
  ]
}
```

### "races"."XCL_066" = 2007 AND "races"."XCL_069" = 'Bahrain Grand Prix' AND "results"."XCL_084" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_066\" = 2007 AND \"races\".\"XCL_069\" = 'Bahrain Grand Prix' AND \"results\".\"XCL_084\" IS NULL",
  "grain": [],
  "population_scope": "SELECT COUNT(T3.\"XCL_034\") FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T1.\"XCL_066\" = 2007 AND T1.\"XCL_069\" = 'Bahrain Grand Prix' AND T2.\"XCL_084\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:862"
  ]
}
```

### Driver Identifier XCL_039

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE T2.\"XCL_074\" = 592 AND NOT T2.\"XCL_084\" IS NULL AND NOT T1.\"XCL_040\" IS NULL ORDER BY T1.\"XCL_040\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:865"
  ]
}
```

### Race Attribute

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_070\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_069\", \"XCL_070\" FROM races WHERE \"XCL_066\" = 1999 ORDER BY \"XCL_067\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:885"
  ]
}
```

### Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_066\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_066\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_088\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_066\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_066\" AS \"value\" FROM results AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_074\" = \"r1\".\"XCL_065\" WHERE NOT \"r0\".\"XCL_088\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:974"
  ]
}
```

### Circuit Identifier

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_009\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_009\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Circuit de Barcelona-Catalunya'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:849"
  ]
}
```

### Driver Identifier XCL_038

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_038\", T2.\"XCL_039\", T1.\"XCL_088\" FROM results AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_075\" = T2.\"XCL_034\" WHERE NOT T1.\"XCL_088\" IS NULL ORDER BY T1.\"XCL_088\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:958"
  ]
}
```

### Driver ID for Lewis Hamilton

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_034\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_034\" FROM drivers WHERE \"XCL_038\" = 'Lewis' AND \"XCL_039\" = 'Hamilton'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_034\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_034\" AS \"value\" FROM drivers AS \"r0\" WHERE \"r0\".\"XCL_038\" = 'Lewis' AND \"r0\".\"XCL_039\" = 'Hamilton'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:930"
  ]
}
```

### Age in Years

```json
{
  "kind": "binding",
  "formula": "STRFTIME('%Y', CURRENT_TIMESTAMP) - STRFTIME('%Y', \"drivers\".\"XCL_040\")",
  "grain": [],
  "population_scope": "SELECT STRFTIME('%Y', CURRENT_TIMESTAMP) - STRFTIME('%Y', \"XCL_040\"), \"XCL_038\", \"XCL_039\" FROM drivers WHERE \"XCL_041\" = 'Japanese' ORDER BY \"XCL_040\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:898"
  ]
}
```

### Champion Time in Seconds

```json
{
  "kind": "binding",
  "formula": "CASE WHEN \"results\".\"XCL_081\" = 1 THEN (CAST(SUBSTRING(\"results\".\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(\"results\".\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(\"results\".\"XCL_084\", 6) AS REAL) ELSE CAST(SUBSTRING(\"results\".\"XCL_084\", 2) AS REAL) END",
  "grain": [],
  "population_scope": "SELECT \"time_seconds\" FROM time_in_seconds WHERE \"XCL_081\" = 1",
  "upstream_scopes": [
    "SELECT T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6) AS REAL) ELSE CAST(SUBSTRING(T1.\"XCL_084\", 2) AS REAL) END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Australian Grand Prix' AND NOT T1.\"XCL_084\" IS NULL AND T2.\"XCL_066\" = 2008"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:944"
  ]
}
```

### Driver Identifier (XCL_038)

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_038\", T3.\"XCL_039\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T2.\"XCL_078\" = 4 AND T1.\"XCL_069\" = 'Australian Grand Prix' AND T1.\"XCL_066\" = 1989",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_038\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      },
      {
        "role": "r1",
        "physical_table": "results"
      },
      {
        "role": "r2",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_038\" AS \"value\" FROM races AS \"r0\" INNER JOIN results AS \"r1\" ON \"r1\".\"XCL_074\" = \"r0\".\"XCL_065\" INNER JOIN drivers AS \"r2\" ON \"r2\".\"XCL_034\" = \"r1\".\"XCL_075\" WHERE \"r1\".\"XCL_078\" = 4 AND \"r0\".\"XCL_069\" = 'Australian Grand Prix' AND \"r0\".\"XCL_066\" = 1989",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:934"
  ]
}
```

### Race Attribute

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_066\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_069\", T1.\"XCL_066\" FROM races AS T1 INNER JOIN results AS T2 ON T1.\"XCL_065\" = T2.\"XCL_074\" WHERE NOT T2.\"XCL_085\" IS NULL ORDER BY T2.\"XCL_085\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:961"
  ]
}
```

### "drivers"."XCL_038" = 'Robert' AND "drivers"."XCL_039" = 'Kubica'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Robert' AND \"drivers\".\"XCL_039\" = 'Kubica'",
  "grain": [],
  "population_scope": "SELECT \"XCL_035\" FROM drivers WHERE \"XCL_038\" = 'Robert' AND \"XCL_039\" = 'Kubica'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:968"
  ]
}
```

### NOT "results"."XCL_088" IS NULL

```json
{
  "kind": "predicate",
  "formula": "NOT \"results\".\"XCL_088\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_038\", T2.\"XCL_039\", T1.\"XCL_088\" FROM results AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_075\" = T2.\"XCL_034\" WHERE NOT T1.\"XCL_088\" IS NULL ORDER BY T1.\"XCL_088\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:958"
  ]
}
```

### "drivers"."XCL_038" = 'Lewis' AND "drivers"."XCL_039" = 'Hamilton'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Lewis' AND \"drivers\".\"XCL_039\" = 'Hamilton'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_066\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T3.\"XCL_038\" = 'Lewis' AND T3.\"XCL_039\" = 'Hamilton'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:932"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_035\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 20 ORDER BY T1.\"XCL_062\" DESC LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:846"
  ]
}
```

### "drivers"."XCL_038" = 'Lewis' AND "drivers"."XCL_039" = 'Hamilton'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Lewis' AND \"drivers\".\"XCL_039\" = 'Hamilton'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_047\" FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_044\" = T2.\"XCL_034\" WHERE T2.\"XCL_038\" = 'Lewis' AND T2.\"XCL_039\" = 'Hamilton'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1010"
  ]
}
```

### "circuits"."XCL_003" = 'Silverstone Circuit'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_003\" = 'Silverstone Circuit'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_009\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Silverstone Circuit'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:921"
  ]
}
```

### Aggregates the total number of result records for drivers with nationality 'British' in the 2008 Australian Grand Prix. The grain is a single scalar c

```json
{
  "kind": "metric",
  "formula": "COUNT(*)",
  "grain": [],
  "population_scope": "SELECT COUNT(*) FROM drivers AS T1 INNER JOIN results AS T2 ON T1.\"XCL_034\" = T2.\"XCL_075\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T2.\"XCL_074\" WHERE T3.\"XCL_069\" = 'Australian Grand Prix' AND T1.\"XCL_041\" = 'British' AND T3.\"XCL_066\" = 2008",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(*)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      },
      {
        "role": "r1",
        "physical_table": "results"
      },
      {
        "role": "r2",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT COUNT(*) AS \"value\" FROM drivers AS \"r0\" INNER JOIN results AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_075\" INNER JOIN races AS \"r2\" ON \"r2\".\"XCL_065\" = \"r1\".\"XCL_074\" WHERE \"r2\".\"XCL_069\" = 'Australian Grand Prix' AND \"r0\".\"XCL_041\" = 'British' AND \"r2\".\"XCL_066\" = 2008",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:939"
  ]
}
```

### "drivers"."XCL_038" = 'Lewis' AND "drivers"."XCL_039" = 'Hamilton'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Lewis' AND \"drivers\".\"XCL_039\" = 'Hamilton'",
  "grain": [],
  "population_scope": "SELECT \"XCL_035\" FROM drivers WHERE \"XCL_038\" = 'Lewis' AND \"XCL_039\" = 'Hamilton'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:918"
  ]
}
```

### "circuits"."XCL_005" = 'Italy'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_005\" = 'Italy'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(T1.\"XCL_048\") AS REAL) / COUNT(T1.\"XCL_045\") FROM lapTimes AS T1 INNER JOIN races AS T2 ON T1.\"XCL_043\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T3.\"XCL_005\" = 'Italy'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1019"
  ]
}
```

### Driver ID (Aggregated)

```json
{
  "kind": "binding",
  "formula": "\"lapTimes\".\"XCL_044\"",
  "grain": [
    "\"lapTimes\".\"XCL_044\""
  ],
  "population_scope": "SELECT \"XCL_044\", MIN(\"time_in_seconds\") AS min_time_in_seconds FROM lap_times_in_seconds GROUP BY \"XCL_044\"",
  "upstream_scopes": [
    "SELECT \"XCL_044\", (CASE WHEN SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) AS REAL) * 60 ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) AS REAL) ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) AS REAL) / 1000 ELSE 0 END) AS time_in_seconds FROM lapTimes"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1011"
  ]
}
```

### "circuits"."XCL_005" = 'Spain'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_005\" = 'Spain'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_069\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_005\" = 'Spain'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:853"
  ]
}
```

### "races"."XCL_066" = 2006 AND "races"."XCL_069" = 'San Marino Grand Prix' AND "results"."XCL_079" = 2

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_066\" = 2006 AND \"races\".\"XCL_069\" = 'San Marino Grand Prix' AND \"results\".\"XCL_079\" = 2",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_038\", T3.\"XCL_039\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T1.\"XCL_066\" = 2006 AND T1.\"XCL_069\" = 'San Marino Grand Prix' AND T2.\"XCL_079\" = 2",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:874"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"results\".\"XCL_075\"",
  "grain": [
    "\"results\".\"XCL_075\""
  ],
  "population_scope": "SELECT T1.\"XCL_075\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Chinese Grand Prix' AND T2.\"XCL_066\" = 2008 AND NOT T1.\"XCL_084\" IS NULL GROUP BY T1.\"XCL_075\" HAVING COUNT(T2.\"XCL_065\") > 0",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_075\"",
    "grain": [
      "\"r0\".\"XCL_075\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_075\" AS \"grain_0\", \"r0\".\"XCL_075\" AS \"value\" FROM results AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_074\" = \"r1\".\"XCL_065\" WHERE \"r1\".\"XCL_069\" = 'Chinese Grand Prix' AND \"r1\".\"XCL_066\" = 2008 AND NOT \"r0\".\"XCL_084\" IS NULL GROUP BY \"r0\".\"XCL_075\" HAVING COUNT(\"r1\".\"XCL_065\") > 0",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:940"
  ]
}
```

### "races"."XCL_066" = 2005 AND STRFTIME('%m', "races"."XCL_070") = '09'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_066\" = 2005 AND STRFTIME('%m', \"races\".\"XCL_070\") = '09'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_069\", T1.\"XCL_003\", T1.\"XCL_004\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_066\" = 2005 AND STRFTIME('%m', T2.\"XCL_070\") = '09'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:901"
  ]
}
```

### "circuits"."XCL_003" = 'Circuit de Barcelona-Catalunya'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_003\" = 'Circuit de Barcelona-Catalunya'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_070\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Circuit de Barcelona-Catalunya'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:924"
  ]
}
```

### NOT "drivers"."XCL_040" IS NULL

```json
{
  "kind": "predicate",
  "formula": "NOT \"drivers\".\"XCL_040\" IS NULL",
  "grain": [],
  "population_scope": "SELECT \"XCL_041\" FROM drivers WHERE NOT \"XCL_040\" IS NULL ORDER BY \"XCL_040\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:915"
  ]
}
```

### Selected Circuit Name

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_003\" FROM circuits WHERE \"XCL_003\" IN ('Silverstone Circuit', 'Hockenheimring', 'Hungaroring') ORDER BY \"XCL_006\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:911"
  ]
}
```

### Constructor Standing Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"constructorStandings\".\"XCL_016\")",
  "grain": [
    "\"constructorStandings\".\"XCL_017\""
  ],
  "population_scope": "SELECT COUNT(T1.\"XCL_016\") FROM constructorStandings AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_017\" = T2.\"XCL_022\" WHERE T1.\"XCL_018\" = 0 AND T2.\"XCL_025\" = 'Japanese' GROUP BY T1.\"XCL_017\" HAVING COUNT(\"XCL_016\") = 2",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:951"
  ]
}
```

### NOT "results"."XCL_084" IS NULL

```json
{
  "kind": "predicate",
  "formula": "NOT \"results\".\"XCL_084\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_066\", T2.\"XCL_065\", T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(T1.\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_084\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:955"
  ]
}
```

### Race Date

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_066\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_069\", T1.\"XCL_066\" FROM races AS T1 INNER JOIN lapTimes AS T2 ON T2.\"XCL_043\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_044\" WHERE T3.\"XCL_038\" = 'Michael' AND T3.\"XCL_039\" = 'Schumacher' ORDER BY T2.\"XCL_048\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:904"
  ]
}
```

### Circuit Identifier

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_009\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_009\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_066\" = 2009 AND T2.\"XCL_069\" = 'Spanish Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_009\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_009\" AS \"value\" FROM circuits AS \"r0\" INNER JOIN races AS \"r1\" ON \"r1\".\"XCL_068\" = \"r0\".\"XCL_001\" WHERE \"r1\".\"XCL_066\" = 2009 AND \"r1\".\"XCL_069\" = 'Spanish Grand Prix'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:925"
  ]
}
```

### Attribute XCL_042 from the drivers table, representing another driver characteristic or identifier, for drivers who recorded lap times starting with '

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_042\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_038\", T2.\"XCL_039\", T2.\"XCL_042\" FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_044\" WHERE T1.\"XCL_043\" = 161 AND T1.\"XCL_047\" LIKE '1:27%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:866"
  ]
}
```

### Minimum Non-Null Result Value XCL_088

```json
{
  "kind": "binding",
  "formula": "\"results\".\"XCL_088\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_038\", T2.\"XCL_039\", T1.\"XCL_088\" FROM results AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_075\" = T2.\"XCL_034\" WHERE NOT T1.\"XCL_088\" IS NULL ORDER BY T1.\"XCL_088\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:958"
  ]
}
```

### Constructor Name

```json
{
  "kind": "binding",
  "formula": "\"constructors\".\"XCL_023\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_023\", T3.\"XCL_026\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN constructors AS T3 ON T1.\"XCL_076\" = T3.\"XCL_022\" WHERE T2.\"XCL_069\" = 'Singapore Grand Prix' AND T2.\"XCL_066\" = 2009 AND T1.\"XCL_084\" LIKE '_:%:__.___'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_023\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "races"
      },
      {
        "role": "r2",
        "physical_table": "constructors"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_023\" AS \"value\" FROM results AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_074\" = \"r1\".\"XCL_065\" INNER JOIN constructors AS \"r2\" ON \"r0\".\"XCL_076\" = \"r2\".\"XCL_022\" WHERE \"r1\".\"XCL_069\" = 'Singapore Grand Prix' AND \"r1\".\"XCL_066\" = 2009 AND \"r0\".\"XCL_084\" LIKE '_:%:__.___'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:990"
  ]
}
```

### "qualifying"."XCL_057" = 20

```json
{
  "kind": "predicate",
  "formula": "\"qualifying\".\"XCL_057\" = 20",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_035\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 20 ORDER BY T1.\"XCL_062\" DESC LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:846"
  ]
}
```

### "constructorStandings"."XCL_018" = 0 AND "constructorStandings"."XCL_016" = 291

```json
{
  "kind": "predicate",
  "formula": "\"constructorStandings\".\"XCL_018\" = 0 AND \"constructorStandings\".\"XCL_016\" = 291",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_024\" FROM constructorStandings AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_017\" = T2.\"XCL_022\" WHERE T1.\"XCL_018\" = 0 AND T1.\"XCL_016\" = 291",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:950"
  ]
}
```

### Lap Record

```json
{
  "kind": "binding",
  "formula": "T1.\"XCL_088\"",
  "grain": [],
  "population_scope": "WITH fastest_lap_times AS (SELECT T1.\"XCL_074\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL) SELECT T1.\"XCL_088\" AS lap_record FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" INNER JOIN (SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T3.\"XCL_005\" = 'Italy') AS T4 ON (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) = T4.\"min_time_in_seconds\" LIMIT 1",
  "upstream_scopes": [
    "SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T3.\"XCL_005\" = 'Italy'",
    "SELECT T1.\"XCL_074\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1014"
  ]
}
```

### Lap Time Value

```json
{
  "kind": "binding",
  "formula": "\"lapTimes\".\"XCL_044\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_044\" FROM lapTimes AS T1 INNER JOIN races AS T2 ON T1.\"XCL_043\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'French Grand Prix' AND T1.\"XCL_045\" = 3 ORDER BY T1.\"XCL_047\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:985"
  ]
}
```

### "races"."XCL_069" = 'Spanish Grand Prix' AND "races"."XCL_066" = 2009 AND NOT "results"."XCL_089" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Spanish Grand Prix' AND \"races\".\"XCL_066\" = 2009 AND NOT \"results\".\"XCL_089\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_089\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" WHERE T1.\"XCL_069\" = 'Spanish Grand Prix' AND T1.\"XCL_066\" = 2009 AND NOT T2.\"XCL_089\" IS NULL ORDER BY T2.\"XCL_089\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:931"
  ]
}
```

### The minimum value of the race identifier column (XCL_066) for the specific event 'Singapore Grand Prix'. Returns a single scalar value representing th

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_066\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_066\" FROM races WHERE \"XCL_069\" = 'Singapore Grand Prix' ORDER BY \"XCL_066\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:882"
  ]
}
```

### "results"."XCL_081" = 1

```json
{
  "kind": "predicate",
  "formula": "\"results\".\"XCL_081\" = 1",
  "grain": [],
  "population_scope": "SELECT \"time_seconds\" FROM time_in_seconds WHERE \"XCL_081\" = 1",
  "upstream_scopes": [
    "SELECT T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6) AS REAL) ELSE CAST(SUBSTRING(T1.\"XCL_084\", 2) AS REAL) END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Australian Grand Prix' AND NOT T1.\"XCL_084\" IS NULL AND T2.\"XCL_066\" = 2008"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:944"
  ]
}
```

### Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_069\", T1.\"XCL_066\" FROM races AS T1 INNER JOIN results AS T2 ON T1.\"XCL_065\" = T2.\"XCL_074\" WHERE NOT T2.\"XCL_085\" IS NULL ORDER BY T2.\"XCL_085\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:961"
  ]
}
```

### Driver Name

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_038\", T2.\"XCL_039\" FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_044\" WHERE T1.\"XCL_043\" = 348 ORDER BY T1.\"XCL_047\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:878"
  ]
}
```

### "status"."XCL_094" = 'Puncture' AND "drivers"."XCL_041" = 'American'

```json
{
  "kind": "predicate",
  "formula": "\"status\".\"XCL_094\" = 'Puncture' AND \"drivers\".\"XCL_041\" = 'American'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_034\") FROM drivers AS T1 INNER JOIN results AS T2 ON T1.\"XCL_034\" = T2.\"XCL_075\" INNER JOIN status AS T3 ON T2.\"XCL_090\" = T3.\"XCL_093\" WHERE T3.\"XCL_094\" = 'Puncture' AND T1.\"XCL_041\" = 'American'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:982"
  ]
}
```

### Result Metric XCL_089

```json
{
  "kind": "binding",
  "formula": "\"results\".\"XCL_089\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_089\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" WHERE T1.\"XCL_069\" = 'Spanish Grand Prix' AND T1.\"XCL_066\" = 2009 AND NOT T2.\"XCL_089\" IS NULL ORDER BY T2.\"XCL_089\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:931"
  ]
}
```

### Circuit Name

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\", T1.\"XCL_004\", T2.\"XCL_069\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_005\" = 'USA' AND T2.\"XCL_066\" = 2006",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_003\" AS \"value\" FROM circuits AS \"r0\" INNER JOIN races AS \"r1\" ON \"r1\".\"XCL_068\" = \"r0\".\"XCL_001\" WHERE \"r0\".\"XCL_005\" = 'USA' AND \"r1\".\"XCL_066\" = 2006",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:900"
  ]
}
```

### "races"."XCL_066" = 2009

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_066\" = 2009",
  "grain": [],
  "population_scope": "SELECT \"XCL_065\" FROM races WHERE \"XCL_066\" = 2009",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:965"
  ]
}
```

### Average XCL_066 for 2000-2010

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"races\".\"XCL_066\" BETWEEN 2000 AND 2010 THEN 1 ELSE 0 END) AS REAL) / 10",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN \"XCL_066\" BETWEEN 2000 AND 2010 THEN 1 ELSE 0 END) AS REAL) / 10 FROM races WHERE \"XCL_070\" BETWEEN '2000-01-01' AND '2010-12-31'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r0\".\"XCL_066\" BETWEEN 2000 AND 2010 THEN 1 ELSE 0 END) AS REAL) / 10",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r0\".\"XCL_066\" BETWEEN 2000 AND 2010 THEN 1 ELSE 0 END) AS REAL) / 10 AS \"value\" FROM races AS \"r0\" WHERE \"r0\".\"XCL_070\" BETWEEN '2000-01-01' AND '2010-12-31'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:996"
  ]
}
```

### Driver Attribute XCL_038

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_038\", T2.\"XCL_039\" FROM results AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_075\" = T2.\"XCL_034\" WHERE STRFTIME('%Y', T2.\"XCL_040\") > '1975' AND T1.\"XCL_087\" = 2",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_038\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_038\" AS \"value\" FROM results AS \"r0\" INNER JOIN drivers AS \"r1\" ON \"r0\".\"XCL_075\" = \"r1\".\"XCL_034\" WHERE STRFTIME('%Y', \"r1\".\"XCL_040\") > '1975' AND \"r0\".\"XCL_087\" = 2",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:956"
  ]
}
```

### Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_069\", T1.\"XCL_005\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_066\" = 2017 ORDER BY T2.\"XCL_070\" ASC",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:907"
  ]
}
```

### Driver Attribute XCL_038

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_038\", T3.\"XCL_039\", T3.\"XCL_035\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T1.\"XCL_069\" = 'Canadian Grand Prix' AND T2.\"XCL_087\" = 1 AND T1.\"XCL_066\" = 2007",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_038\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      },
      {
        "role": "r1",
        "physical_table": "results"
      },
      {
        "role": "r2",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_038\" AS \"value\" FROM races AS \"r0\" INNER JOIN results AS \"r1\" ON \"r1\".\"XCL_074\" = \"r0\".\"XCL_065\" INNER JOIN drivers AS \"r2\" ON \"r2\".\"XCL_034\" = \"r1\".\"XCL_075\" WHERE \"r0\".\"XCL_069\" = 'Canadian Grand Prix' AND \"r1\".\"XCL_087\" = 1 AND \"r0\".\"XCL_066\" = 2007",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:928"
  ]
}
```

### Qualifying Result Value

```json
{
  "kind": "binding",
  "formula": "\"qualifying\".\"XCL_062\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_062\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 354 AND T2.\"XCL_038\" = 'Bruno' AND T2.\"XCL_039\" = 'Senna'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_062\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "qualifying"
      },
      {
        "role": "r1",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_062\" AS \"value\" FROM qualifying AS \"r0\" INNER JOIN drivers AS \"r1\" ON \"r1\".\"XCL_034\" = \"r0\".\"XCL_058\" WHERE \"r0\".\"XCL_057\" = 354 AND \"r1\".\"XCL_038\" = 'Bruno' AND \"r1\".\"XCL_039\" = 'Senna'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:859"
  ]
}
```

### "races"."XCL_069" = 'Australian Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Australian Grand Prix'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_006\", T1.\"XCL_007\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Australian Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:854"
  ]
}
```

### "results"."XCL_078" = 4 AND "races"."XCL_069" = 'Australian Grand Prix' AND "races"."XCL_066" = 1989

```json
{
  "kind": "predicate",
  "formula": "\"results\".\"XCL_078\" = 4 AND \"races\".\"XCL_069\" = 'Australian Grand Prix' AND \"races\".\"XCL_066\" = 1989",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_038\", T3.\"XCL_039\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T2.\"XCL_078\" = 4 AND T1.\"XCL_069\" = 'Australian Grand Prix' AND T1.\"XCL_066\" = 1989",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:934"
  ]
}
```

### Race ID

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_065\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_066\", T2.\"XCL_065\", T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(T1.\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_084\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_065\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_065\" AS \"value\" FROM results AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_074\" = \"r1\".\"XCL_065\" WHERE NOT \"r0\".\"XCL_084\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:955"
  ]
}
```

### "constructors"."XCL_025" = 'Italian'

```json
{
  "kind": "predicate",
  "formula": "\"constructors\".\"XCL_025\" = 'Italian'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_026\" FROM constructors AS T1 INNER JOIN constructorStandings AS T2 ON T1.\"XCL_022\" = T2.\"XCL_017\" WHERE T1.\"XCL_025\" = 'Italian' ORDER BY T2.\"XCL_018\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:983"
  ]
}
```

### Circuit Attribute XCL_007

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_006\", \"XCL_007\" FROM circuits WHERE \"XCL_003\" = 'Silverstone Circuit'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_007\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_007\" AS \"value\" FROM circuits AS \"r0\" WHERE \"r0\".\"XCL_003\" = 'Silverstone Circuit'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:910"
  ]
}
```

### Race Attribute XCL_071

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_071\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_070\", T2.\"XCL_071\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_066\" = 2010 AND T2.\"XCL_069\" = 'Abu Dhabi Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_071\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_071\" AS \"value\" FROM circuits AS \"r0\" INNER JOIN races AS \"r1\" ON \"r1\".\"XCL_068\" = \"r0\".\"XCL_001\" WHERE \"r1\".\"XCL_066\" = 2010 AND \"r1\".\"XCL_069\" = 'Abu Dhabi Grand Prix'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:922"
  ]
}
```

### "races"."XCL_069" = 'Malaysian Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Malaysian Grand Prix'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_006\", T1.\"XCL_007\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Malaysian Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:868"
  ]
}
```

### Circuit Name

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_006\", T1.\"XCL_007\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Abu Dhabi Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:857"
  ]
}
```

### Circuit Identifier

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_005\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_005\", T1.\"XCL_004\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_069\" = 'European Grand Prix' ORDER BY T2.\"XCL_066\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:888"
  ]
}
```

### The value of column XCL_039 from the drivers table, associated with the driver linked to the lap time record.

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_048\", T1.\"XCL_038\", T1.\"XCL_039\", T3.\"XCL_069\" FROM drivers AS T1 INNER JOIN lapTimes AS T2 ON T1.\"XCL_034\" = T2.\"XCL_044\" INNER JOIN races AS T3 ON T2.\"XCL_043\" = T3.\"XCL_065\" ORDER BY T2.\"XCL_048\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:894"
  ]
}
```

### "races"."XCL_069" = 'Austrian Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Austrian Grand Prix'",
  "grain": [],
  "population_scope": "SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix'",
  "upstream_scopes": [
    "SELECT T1.\"XCL_074\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1015"
  ]
}
```

### "lapTimes"."XCL_043" = 161 AND "lapTimes"."XCL_047" LIKE '1:27%'

```json
{
  "kind": "predicate",
  "formula": "\"lapTimes\".\"XCL_043\" = 161 AND \"lapTimes\".\"XCL_047\" LIKE '1:27%'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_038\", T2.\"XCL_039\", T2.\"XCL_042\" FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_044\" WHERE T1.\"XCL_043\" = 161 AND T1.\"XCL_047\" LIKE '1:27%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:866"
  ]
}
```

### "races"."XCL_069" = 'Abu Dhabi Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Abu Dhabi Grand Prix'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_006\", T1.\"XCL_007\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Abu Dhabi Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:857"
  ]
}
```

### Circuit Name

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_069\", T1.\"XCL_003\", T1.\"XCL_004\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_066\" = 2005 AND STRFTIME('%m', T2.\"XCL_070\") = '09'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:901"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_041\", T3.\"XCL_069\" FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" INNER JOIN races AS T3 ON T2.\"XCL_028\" = T3.\"XCL_065\" ORDER BY JULIANDAY(T1.\"XCL_040\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1002"
  ]
}
```

### "races"."XCL_066" = 1999

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_066\" = 1999",
  "grain": [],
  "population_scope": "SELECT \"XCL_069\", \"XCL_070\" FROM races WHERE \"XCL_066\" = 1999 ORDER BY \"XCL_067\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:885"
  ]
}
```

### The value of column XCL_048 from the lapTimes table. It is used as the primary sorting key (ascending) to identify the minimum value in the result set

```json
{
  "kind": "binding",
  "formula": "\"lapTimes\".\"XCL_048\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_048\", T1.\"XCL_038\", T1.\"XCL_039\", T3.\"XCL_069\" FROM drivers AS T1 INNER JOIN lapTimes AS T2 ON T1.\"XCL_034\" = T2.\"XCL_044\" INNER JOIN races AS T3 ON T2.\"XCL_043\" = T3.\"XCL_065\" ORDER BY T2.\"XCL_048\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:894"
  ]
}
```

### "circuits"."XCL_005" = 'USA'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_005\" = 'USA'",
  "grain": [],
  "population_scope": "SELECT \"XCL_006\", \"XCL_007\" FROM circuits WHERE \"XCL_005\" = 'USA'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:946"
  ]
}
```

### "races"."XCL_069" = 'Australian Grand Prix' AND "results"."XCL_084" LIKE '_:%:__.___' AND "races"."XCL_066" = 2008

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Australian Grand Prix' AND \"results\".\"XCL_084\" LIKE '_:%:__.___' AND \"races\".\"XCL_066\" = 2008",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_042\" FROM drivers AS T1 INNER JOIN results AS T2 ON T1.\"XCL_034\" = T2.\"XCL_075\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T2.\"XCL_074\" WHERE T3.\"XCL_069\" = 'Australian Grand Prix' AND T2.\"XCL_084\" LIKE '_:%:__.___' AND T3.\"XCL_066\" = 2008",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:938"
  ]
}
```

### "constructors"."XCL_025" = 'British'

```json
{
  "kind": "predicate",
  "formula": "\"constructors\".\"XCL_025\" = 'British'",
  "grain": [],
  "population_scope": "SELECT MAX(T1.\"XCL_018\") FROM constructorStandings AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_017\" = T2.\"XCL_022\" WHERE T2.\"XCL_025\" = 'British'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:948"
  ]
}
```

### "drivers"."XCL_041" = 'French' AND (CAST(SUBSTRING("lapTimes"."XCL_047", 1, 2) AS INTEGER) * 60 + CAST(SUBSTRING("lapTimes"."XCL_047", 4, 2) AS INTEGE

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_041\" = 'French' AND (CAST(SUBSTRING(\"lapTimes\".\"XCL_047\", 1, 2) AS INTEGER) * 60 + CAST(SUBSTRING(\"lapTimes\".\"XCL_047\", 4, 2) AS INTEGER) + CAST(SUBSTRING(\"lapTimes\".\"XCL_047\", 7, 2) AS REAL) / 1000) < 120",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_034\") FROM drivers AS T1 INNER JOIN lapTimes AS T2 ON T1.\"XCL_034\" = T2.\"XCL_044\" WHERE T1.\"XCL_041\" = 'French' AND (CAST(SUBSTRING(T2.\"XCL_047\", 1, 2) AS INTEGER) * 60 + CAST(SUBSTRING(T2.\"XCL_047\", 4, 2) AS INTEGER) + CAST(SUBSTRING(T2.\"XCL_047\", 7, 2) AS REAL) / 1000) < 120",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:963"
  ]
}
```

### Aggregates the maximum value of the 'XCL_018' column from the 'constructorStandings' table, restricted to records where the associated constructor in 

```json
{
  "kind": "metric",
  "formula": "MAX(\"constructorStandings\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT MAX(T1.\"XCL_018\") FROM constructorStandings AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_017\" = T2.\"XCL_022\" WHERE T2.\"XCL_025\" = 'British'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MAX(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "constructorStandings"
      },
      {
        "role": "r1",
        "physical_table": "constructors"
      }
    ],
    "scope_sql": "SELECT MAX(\"r0\".\"XCL_018\") AS \"value\" FROM constructorStandings AS \"r0\" INNER JOIN constructors AS \"r1\" ON \"r0\".\"XCL_017\" = \"r1\".\"XCL_022\" WHERE \"r1\".\"XCL_025\" = 'British'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:948"
  ]
}
```

### Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_069\", T1.\"XCL_003\", T1.\"XCL_004\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_066\" = 2005 AND STRFTIME('%m', T2.\"XCL_070\") = '09'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:901"
  ]
}
```

### Aggregates the count of 'XCL_075' from the 'results' table where the associated race is the 'Australian Grand Prix' in 2008 and 'XCL_084' is not null.

```json
{
  "kind": "metric",
  "formula": "COUNT(\"results\".\"XCL_075\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_075\") FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" WHERE T1.\"XCL_069\" = 'Australian Grand Prix' AND T1.\"XCL_066\" = 2008 AND NOT T2.\"XCL_084\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_075\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      },
      {
        "role": "r1",
        "physical_table": "results"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_075\") AS \"value\" FROM races AS \"r0\" INNER JOIN results AS \"r1\" ON \"r1\".\"XCL_074\" = \"r0\".\"XCL_065\" WHERE \"r0\".\"XCL_069\" = 'Australian Grand Prix' AND \"r0\".\"XCL_066\" = 2008 AND NOT \"r1\".\"XCL_084\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:935"
  ]
}
```

### "races"."XCL_066" = 2017

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_066\" = 2017",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_069\", T1.\"XCL_005\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_066\" = 2017 ORDER BY T2.\"XCL_070\" ASC",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:907"
  ]
}
```

### The identifier (XCL_069) for races occurring in the same year and month as the earliest race in the dataset.

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_069\" FROM races WHERE STRFTIME('%Y', \"XCL_070\") = (SELECT STRFTIME('%Y', \"XCL_070\") FROM races ORDER BY \"XCL_070\" ASC LIMIT 1) AND STRFTIME('%m', \"XCL_070\") = (SELECT STRFTIME('%m', \"XCL_070\") FROM races ORDER BY \"XCL_070\" ASC LIMIT 1)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:884"
  ]
}
```

### The value of column XCL_044 from the lapTimes table, filtered to rows where XCL_045 equals 1, ordered by XCL_047, and limited to the first 5 results.

```json
{
  "kind": "binding",
  "formula": "\"lapTimes\".\"XCL_044\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_044\" FROM lapTimes WHERE \"XCL_045\" = 1 ORDER BY \"XCL_047\" LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:976"
  ]
}
```

### Driver Name

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_038\", T3.\"XCL_039\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T1.\"XCL_066\" = 2006 AND T1.\"XCL_069\" = 'San Marino Grand Prix' AND T2.\"XCL_079\" = 2",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_039\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      },
      {
        "role": "r1",
        "physical_table": "results"
      },
      {
        "role": "r2",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_039\" AS \"value\" FROM races AS \"r0\" INNER JOIN results AS \"r1\" ON \"r1\".\"XCL_074\" = \"r0\".\"XCL_065\" INNER JOIN drivers AS \"r2\" ON \"r2\".\"XCL_034\" = \"r1\".\"XCL_075\" WHERE \"r0\".\"XCL_066\" = 2006 AND \"r0\".\"XCL_069\" = 'San Marino Grand Prix' AND \"r1\".\"XCL_079\" = 2",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:874"
  ]
}
```

### Circuit Name

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_006\", T1.\"XCL_007\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Malaysian Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:868"
  ]
}
```

### Result Identifier XCL_086

```json
{
  "kind": "binding",
  "formula": "\"results\".\"XCL_086\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_086\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_066\" = 2009 AND T1.\"XCL_084\" LIKE '_:%:__.___'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_086\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_086\" AS \"value\" FROM results AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_074\" = \"r1\".\"XCL_065\" WHERE \"r1\".\"XCL_066\" = 2009 AND \"r0\".\"XCL_084\" LIKE '_:%:__.___'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:959"
  ]
}
```

### Circuit ID for Marina Bay Street Circuit

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM circuits WHERE \"XCL_003\" = 'Marina Bay Street Circuit'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM circuits AS \"r0\" WHERE \"r0\".\"XCL_003\" = 'Marina Bay Street Circuit'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1001"
  ]
}
```

### Driver Name

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_038\", T3.\"XCL_039\" FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_069\" = 'Singapore Grand Prix' AND T1.\"XCL_066\" = 2010 ORDER BY T2.\"XCL_031\" ASC",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_039\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      },
      {
        "role": "r1",
        "physical_table": "driverStandings"
      },
      {
        "role": "r2",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_039\" AS \"value\" FROM races AS \"r0\" INNER JOIN driverStandings AS \"r1\" ON \"r1\".\"XCL_028\" = \"r0\".\"XCL_065\" INNER JOIN drivers AS \"r2\" ON \"r2\".\"XCL_034\" = \"r1\".\"XCL_029\" WHERE \"r0\".\"XCL_069\" = 'Singapore Grand Prix' AND \"r0\".\"XCL_066\" = 2010",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:891"
  ]
}
```

### "circuits"."XCL_003" = 'Sepang International Circuit'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_003\" = 'Sepang International Circuit'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_009\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Sepang International Circuit'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:855"
  ]
}
```

### A calculated metric converting the raw fastest lap time string into a numeric value in seconds. It parses the minutes, seconds, and milliseconds compo

```json
{
  "kind": "binding",
  "formula": "(CAST(SUBSTRING(\"results\".\"XCL_088\", 1, INSTR(\"results\".\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(\"results\".\"XCL_088\", INSTR(\"results\".\"XCL_088\", ':') + 1, INSTR(\"results\".\"XCL_088\", '.') - INSTR(\"results\".\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(\"results\".\"XCL_088\", INSTR(\"results\".\"XCL_088\", '.') + 1) AS REAL) / 1000)",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_074\", T1.\"XCL_075\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "(CAST(SUBSTRING(\"r0\".\"XCL_088\", 1, INSTR(\"r0\".\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(\"r0\".\"XCL_088\", INSTR(\"r0\".\"XCL_088\", ':') + 1, INSTR(\"r0\".\"XCL_088\", '.') - INSTR(\"r0\".\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(\"r0\".\"XCL_088\", INSTR(\"r0\".\"XCL_088\", '.') + 1) AS REAL) / 1000)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      }
    ],
    "scope_sql": "SELECT (CAST(SUBSTRING(\"r0\".\"XCL_088\", 1, INSTR(\"r0\".\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(\"r0\".\"XCL_088\", INSTR(\"r0\".\"XCL_088\", ':') + 1, INSTR(\"r0\".\"XCL_088\", '.') - INSTR(\"r0\".\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(\"r0\".\"XCL_088\", INSTR(\"r0\".\"XCL_088\", '.') + 1) AS REAL) / 1000) AS \"value\" FROM results AS \"r0\" WHERE NOT \"r0\".\"XCL_088\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1016",
    "bird_dev:1014",
    "bird_dev:1015"
  ]
}
```

### "races"."XCL_070" = '1983-07-16'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_070\" = '1983-07-16'",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN NOT T2.\"XCL_084\" IS NULL THEN T2.\"XCL_075\" END) AS REAL) * 100 / COUNT(T2.\"XCL_075\") FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" WHERE T1.\"XCL_070\" = '1983-07-16'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:881"
  ]
}
```

### The value of column XCL_038 from the drivers table, associated with the driver linked to the lap time record.

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_048\", T1.\"XCL_038\", T1.\"XCL_039\", T3.\"XCL_069\" FROM drivers AS T1 INNER JOIN lapTimes AS T2 ON T1.\"XCL_034\" = T2.\"XCL_044\" INNER JOIN races AS T3 ON T2.\"XCL_043\" = T3.\"XCL_065\" ORDER BY T2.\"XCL_048\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:894"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_042\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_042\" FROM drivers WHERE \"XCL_038\" = 'Anthony' AND \"XCL_039\" = 'Davidson'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_042\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_042\" AS \"value\" FROM drivers AS \"r0\" WHERE \"r0\".\"XCL_038\" = 'Anthony' AND \"r0\".\"XCL_039\" = 'Davidson'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:917"
  ]
}
```

### "qualifying"."XCL_057" = 23 AND NOT "qualifying"."XCL_063" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"qualifying\".\"XCL_057\" = 23 AND NOT \"qualifying\".\"XCL_063\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_035\", T2.\"XCL_041\", T2.\"XCL_040\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_058\" = T2.\"XCL_034\" WHERE T1.\"XCL_057\" = 23 AND NOT T1.\"XCL_063\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:980"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_036\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 903 AND T1.\"XCL_064\" LIKE '1:54%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "qualifying"
      },
      {
        "role": "r1",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_036\" AS \"value\" FROM qualifying AS \"r0\" INNER JOIN drivers AS \"r1\" ON \"r1\".\"XCL_034\" = \"r0\".\"XCL_058\" WHERE \"r0\".\"XCL_057\" = 903 AND \"r0\".\"XCL_064\" LIKE '1:54%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:861"
  ]
}
```

### Constructor Name

```json
{
  "kind": "binding",
  "formula": "\"constructors\".\"XCL_025\"",
  "grain": [
    "\"constructors\".\"XCL_024\""
  ],
  "population_scope": "SELECT SUM(T1.\"XCL_013\"), T2.\"XCL_024\", T2.\"XCL_025\" FROM constructorResults AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_012\" = T2.\"XCL_022\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T1.\"XCL_011\" WHERE T3.\"XCL_069\" = 'Monaco Grand Prix' AND T3.\"XCL_066\" BETWEEN 1980 AND 2010 GROUP BY T2.\"XCL_024\" ORDER BY SUM(T1.\"XCL_013\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:994"
  ]
}
```

### 2017 Race Identifier (Excluding 2000)

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_069\" FROM races WHERE \"XCL_066\" = 2017 AND NOT \"XCL_069\" IN (SELECT \"XCL_069\" FROM races WHERE \"XCL_066\" = 2000)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:887"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_039\" FROM drivers WHERE \"XCL_041\" = 'Italian'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_039\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_039\" AS \"value\" FROM drivers AS \"r0\" WHERE \"r0\".\"XCL_041\" = 'Italian'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:916"
  ]
}
```

### "circuits"."XCL_005" = 'Germany'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_005\" = 'Germany'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_069\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_005\" = 'Germany'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:850"
  ]
}
```

### Circuit Identifier

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_003\"",
  "grain": [
    "\"circuits\".\"XCL_003\""
  ],
  "population_scope": "SELECT DISTINCT T1.\"XCL_003\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE STRFTIME('%Y', T2.\"XCL_070\") BETWEEN '1990' AND '2000' GROUP BY T1.\"XCL_003\" HAVING COUNT(T2.\"XCL_065\") = 4",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:899"
  ]
}
```

### NOT "results"."XCL_088" IS NULL

```json
{
  "kind": "predicate",
  "formula": "NOT \"results\".\"XCL_088\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_074\", T1.\"XCL_088\" FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1013"
  ]
}
```

### Average Champion Time (Seconds)

```json
{
  "kind": "metric",
  "formula": "AVG(CASE WHEN \"results\".\"XCL_081\" = 1 THEN (CAST(SUBSTRING(\"results\".\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(\"results\".\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(\"results\".\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(\"results\".\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END)",
  "grain": [
    "\"races\".\"XCL_066\""
  ],
  "population_scope": "WITH time_in_seconds AS (SELECT T2.\"XCL_066\", T2.\"XCL_065\", T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(T1.\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_084\" IS NULL), champion_time AS (SELECT \"XCL_066\", \"XCL_065\", \"time_seconds\" FROM time_in_seconds WHERE \"XCL_081\" = 1) SELECT \"XCL_066\", AVG(\"time_seconds\") FROM champion_time WHERE \"XCL_066\" < 1975 GROUP BY \"XCL_066\" HAVING NOT AVG(\"time_seconds\") IS NULL",
  "upstream_scopes": [
    "SELECT \"XCL_066\", \"XCL_065\", \"time_seconds\" FROM time_in_seconds WHERE \"XCL_081\" = 1",
    "SELECT T2.\"XCL_066\", T2.\"XCL_065\", T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(T1.\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_084\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:955"
  ]
}
```

### "races"."XCL_065" = 901

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_065\" = 901",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_092\" FROM races AS T1 INNER JOIN seasons AS T2 ON T2.\"XCL_091\" = T1.\"XCL_066\" WHERE T1.\"XCL_065\" = 901",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:863",
    "bird_dev:875"
  ]
}
```

### "drivers"."XCL_038" = 'Eddie' AND "drivers"."XCL_039" = 'Irvine' AND "races"."XCL_066" = 2000

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Eddie' AND \"drivers\".\"XCL_039\" = 'Irvine' AND \"races\".\"XCL_066\" = 2000",
  "grain": [],
  "population_scope": "SELECT AVG(T2.\"XCL_030\") FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_029\" = T1.\"XCL_034\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T2.\"XCL_028\" WHERE T1.\"XCL_038\" = 'Eddie' AND T1.\"XCL_039\" = 'Irvine' AND T3.\"XCL_066\" = 2000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:905"
  ]
}
```

### Attribute XCL_006 associated with circuits in Austria. Returned as part of a distinct set of circuit attributes.

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_004\", \"XCL_006\", \"XCL_007\" FROM circuits WHERE \"XCL_005\" = 'Austria'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:978"
  ]
}
```

### Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_069\", \"XCL_070\" FROM races WHERE \"XCL_066\" = 1999 ORDER BY \"XCL_067\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:885"
  ]
}
```

### "races"."XCL_066" BETWEEN 2000 AND 2005

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_066\" BETWEEN 2000 AND 2005",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(STRFTIME('%Y', T3.\"XCL_040\") < '1985' AND T1.\"XCL_083\" > 50, 1, 0)) AS REAL) * 100 / COUNT(*) FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN drivers AS T3 ON T1.\"XCL_075\" = T3.\"XCL_034\" WHERE T2.\"XCL_066\" BETWEEN 2000 AND 2005",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:962"
  ]
}
```

### "circuits"."XCL_003" = 'Silverstone Circuit'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_003\" = 'Silverstone Circuit'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_066\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Silverstone Circuit'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:920"
  ]
}
```

### Aggregates the total number of rows in the 'drivers' table where the nationality ('XCL_041') is 'British' and the year extracted from the date field (

```json
{
  "kind": "metric",
  "formula": "COUNT(\"drivers\".\"XCL_034\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_034\") FROM drivers WHERE \"XCL_041\" = 'British' AND STRFTIME('%Y', \"XCL_040\") > '1980'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_034\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_034\") AS \"value\" FROM drivers AS \"r0\" WHERE \"r0\".\"XCL_041\" = 'British' AND STRFTIME('%Y', \"r0\".\"XCL_040\") > '1980'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:947"
  ]
}
```

### Distinct values of the race identifier column (XCL_066) from the races table, filtered to races held at the circuit named 'Silverstone Circuit'.

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_066\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_066\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Silverstone Circuit'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:920"
  ]
}
```

### "circuits"."XCL_003" = 'Silverstone Circuit'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_003\" = 'Silverstone Circuit'",
  "grain": [],
  "population_scope": "SELECT \"XCL_006\", \"XCL_007\" FROM circuits WHERE \"XCL_003\" = 'Silverstone Circuit'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:910"
  ]
}
```

### NOT "results"."XCL_088" IS NULL

```json
{
  "kind": "predicate",
  "formula": "NOT \"results\".\"XCL_088\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE NOT T2.\"XCL_088\" IS NULL ORDER BY T2.\"XCL_089\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:927"
  ]
}
```

### The driver identifier (XCL_034) of the single driver with the highest value in the XCL_040 column. This subquery acts as a filter to isolate records f

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_034\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_034\" FROM drivers ORDER BY \"XCL_040\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:981"
  ]
}
```

### "races"."XCL_069" = 'Australian Grand Prix' AND "races"."XCL_066" = 2008 AND "drivers"."XCL_038" = 'Lewis' AND "drivers"."XCL_039" = 'Hamilton'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Australian Grand Prix' AND \"races\".\"XCL_066\" = 2008 AND \"drivers\".\"XCL_038\" = 'Lewis' AND \"drivers\".\"XCL_039\" = 'Hamilton'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_086\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN drivers AS T3 ON T1.\"XCL_075\" = T3.\"XCL_034\" WHERE T2.\"XCL_069\" = 'Australian Grand Prix' AND T2.\"XCL_066\" = 2008 AND T3.\"XCL_038\" = 'Lewis' AND T3.\"XCL_039\" = 'Hamilton'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:936"
  ]
}
```

### Aggregates the count of driver identifiers (XCL_034) from the drivers table, restricted to drivers with nationality 'French' (XCL_041) who have at lea

```json
{
  "kind": "metric",
  "formula": "COUNT(\"drivers\".\"XCL_034\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_034\") FROM drivers AS T1 INNER JOIN lapTimes AS T2 ON T1.\"XCL_034\" = T2.\"XCL_044\" WHERE T1.\"XCL_041\" = 'French' AND (CAST(SUBSTRING(T2.\"XCL_047\", 1, 2) AS INTEGER) * 60 + CAST(SUBSTRING(T2.\"XCL_047\", 4, 2) AS INTEGER) + CAST(SUBSTRING(T2.\"XCL_047\", 7, 2) AS REAL) / 1000) < 120",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_034\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      },
      {
        "role": "r1",
        "physical_table": "lapTimes"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_034\") AS \"value\" FROM drivers AS \"r0\" INNER JOIN lapTimes AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_044\" WHERE \"r0\".\"XCL_041\" = 'French' AND (CAST(SUBSTRING(\"r1\".\"XCL_047\", 1, 2) AS INTEGER) * 60 + CAST(SUBSTRING(\"r1\".\"XCL_047\", 4, 2) AS INTEGER) + CAST(SUBSTRING(\"r1\".\"XCL_047\", 7, 2) AS REAL) / 1000) < 120",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:963"
  ]
}
```

### NOT "results"."XCL_088" IS NULL

```json
{
  "kind": "predicate",
  "formula": "NOT \"results\".\"XCL_088\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_069\" FROM races AS T1 INNER JOIN results AS T2 ON T1.\"XCL_065\" = T2.\"XCL_074\" WHERE NOT T2.\"XCL_088\" IS NULL ORDER BY T2.\"XCL_088\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:999"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_034\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_034\" FROM pitStops AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_050\" = T2.\"XCL_034\" WHERE T2.\"XCL_041\" = 'Spanish' AND STRFTIME('%Y', T2.\"XCL_040\") < '1982' ORDER BY T1.\"XCL_053\" DESC LIMIT 10",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:973"
  ]
}
```

### "constructorResults"."XCL_011" = 9

```json
{
  "kind": "predicate",
  "formula": "\"constructorResults\".\"XCL_011\" = 9",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_026\" FROM constructorResults AS T1 INNER JOIN constructors AS T2 ON T2.\"XCL_022\" = T1.\"XCL_012\" WHERE T1.\"XCL_011\" = 9 ORDER BY T1.\"XCL_013\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:869"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_038\", T3.\"XCL_039\" FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_069\" = 'Singapore Grand Prix' AND T1.\"XCL_066\" = 2010 ORDER BY T2.\"XCL_031\" ASC",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_038\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      },
      {
        "role": "r1",
        "physical_table": "driverStandings"
      },
      {
        "role": "r2",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_038\" AS \"value\" FROM races AS \"r0\" INNER JOIN driverStandings AS \"r1\" ON \"r1\".\"XCL_028\" = \"r0\".\"XCL_065\" INNER JOIN drivers AS \"r2\" ON \"r2\".\"XCL_034\" = \"r1\".\"XCL_029\" WHERE \"r0\".\"XCL_069\" = 'Singapore Grand Prix' AND \"r0\".\"XCL_066\" = 2010",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:891"
  ]
}
```

### Constructor Name

```json
{
  "kind": "binding",
  "formula": "\"constructors\".\"XCL_026\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_026\" FROM constructors AS T1 INNER JOIN constructorStandings AS T2 ON T1.\"XCL_022\" = T2.\"XCL_017\" WHERE T1.\"XCL_025\" = 'Italian' ORDER BY T2.\"XCL_018\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:983"
  ]
}
```

### Circuit Name

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_066\" = 2009 AND T2.\"XCL_069\" = 'Spanish Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_003\" AS \"value\" FROM circuits AS \"r0\" INNER JOIN races AS \"r1\" ON \"r1\".\"XCL_068\" = \"r0\".\"XCL_001\" WHERE \"r1\".\"XCL_066\" = 2009 AND \"r1\".\"XCL_069\" = 'Spanish Grand Prix'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:919"
  ]
}
```

### Driver Name

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_042\" FROM drivers AS T1 INNER JOIN results AS T2 ON T1.\"XCL_034\" = T2.\"XCL_075\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T2.\"XCL_074\" WHERE T3.\"XCL_069\" = 'Australian Grand Prix' AND T2.\"XCL_084\" LIKE '_:%:__.___' AND T3.\"XCL_066\" = 2008",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_039\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      },
      {
        "role": "r1",
        "physical_table": "results"
      },
      {
        "role": "r2",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_039\" AS \"value\" FROM drivers AS \"r0\" INNER JOIN results AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_075\" INNER JOIN races AS \"r2\" ON \"r2\".\"XCL_065\" = \"r1\".\"XCL_074\" WHERE \"r2\".\"XCL_069\" = 'Australian Grand Prix' AND \"r1\".\"XCL_084\" LIKE '_:%:__.___' AND \"r2\".\"XCL_066\" = 2008",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:938"
  ]
}
```

### "circuits"."XCL_003" = 'Marina Bay Street Circuit'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_003\" = 'Marina Bay Street Circuit'",
  "grain": [],
  "population_scope": "SELECT \"XCL_002\" FROM circuits WHERE \"XCL_003\" = 'Marina Bay Street Circuit'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:912"
  ]
}
```

### "circuits"."XCL_004" = 'Shanghai'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_004\" = 'Shanghai'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_066\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_004\" = 'Shanghai'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:848"
  ]
}
```

### The value of the 'XCL_026' column from the 'constructors' table for the single record associated with the highest 'XCL_021' value in 'constructorStand

```json
{
  "kind": "binding",
  "formula": "\"constructors\".\"XCL_026\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_026\" FROM constructors AS T1 INNER JOIN constructorStandings AS T2 ON T1.\"XCL_022\" = T2.\"XCL_017\" ORDER BY T2.\"XCL_021\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:984"
  ]
}
```

### "drivers"."XCL_041" = 'German' AND STRFTIME('%Y', "drivers"."XCL_040") BETWEEN '1971' AND '1985'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_041\" = 'German' AND STRFTIME('%Y', \"drivers\".\"XCL_040\") BETWEEN '1971' AND '1985'",
  "grain": [],
  "population_scope": "SELECT \"XCL_038\", \"XCL_039\", \"XCL_042\", \"XCL_040\" FROM drivers WHERE \"XCL_041\" = 'German' AND STRFTIME('%Y', \"XCL_040\") BETWEEN '1971' AND '1985' ORDER BY \"XCL_040\" DESC",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:992"
  ]
}
```

### A calculated field converting the time string (XCL_084) into seconds. It parses hours, minutes, seconds, and milliseconds from the string format. Retu

```json
{
  "kind": "binding",
  "formula": "CASE WHEN \"results\".\"XCL_081\" = 1 THEN (CAST(SUBSTRING(\"results\".\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(\"results\".\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(\"results\".\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(\"results\".\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_066\", T2.\"XCL_065\", T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(T1.\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_084\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CASE WHEN \"r0\".\"XCL_081\" = 1 THEN (CAST(SUBSTRING(\"r0\".\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(\"r0\".\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(\"r0\".\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(\"r0\".\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT CASE WHEN \"r0\".\"XCL_081\" = 1 THEN (CAST(SUBSTRING(\"r0\".\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(\"r0\".\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(\"r0\".\"XCL_084\", 6, 2) AS REAL) + CAST(SUBSTRING(\"r0\".\"XCL_084\", 9) AS REAL) / 1000 ELSE 0 END AS \"value\" FROM results AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_074\" = \"r1\".\"XCL_065\" WHERE NOT \"r0\".\"XCL_084\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:955"
  ]
}
```

### Calculates the percentage of rows in the results table (joined to races) where the column XCL_084 is not null, relative to the total count of XCL_075 

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN NOT \"results\".\"XCL_084\" IS NULL THEN \"results\".\"XCL_075\" END) AS REAL) * 100 / COUNT(\"results\".\"XCL_075\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN NOT T2.\"XCL_084\" IS NULL THEN T2.\"XCL_075\" END) AS REAL) * 100 / COUNT(T2.\"XCL_075\") FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" WHERE T1.\"XCL_070\" = '1983-07-16'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(CASE WHEN NOT \"r1\".\"XCL_084\" IS NULL THEN \"r1\".\"XCL_075\" END) AS REAL) * 100 / COUNT(\"r1\".\"XCL_075\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      },
      {
        "role": "r1",
        "physical_table": "results"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(CASE WHEN NOT \"r1\".\"XCL_084\" IS NULL THEN \"r1\".\"XCL_075\" END) AS REAL) * 100 / COUNT(\"r1\".\"XCL_075\") AS \"value\" FROM races AS \"r0\" INNER JOIN results AS \"r1\" ON \"r1\".\"XCL_074\" = \"r0\".\"XCL_065\" WHERE \"r0\".\"XCL_070\" = '1983-07-16'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:881"
  ]
}
```

### The value of column XCL_069 from the races table, associated with the race linked to the lap time with the highest XCL_045 value.

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_045\", T2.\"XCL_069\", T2.\"XCL_066\", T1.\"XCL_004\" FROM circuits AS T1 INNER JOIN races AS T2 ON T1.\"XCL_001\" = T2.\"XCL_068\" INNER JOIN lapTimes AS T3 ON T3.\"XCL_043\" = T2.\"XCL_065\" ORDER BY T3.\"XCL_045\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:908"
  ]
}
```

### "results"."XCL_074" = 872 AND NOT "results"."XCL_084" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"results\".\"XCL_074\" = 872 AND NOT \"results\".\"XCL_084\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE T2.\"XCL_074\" = 872 AND NOT T2.\"XCL_084\" IS NULL ORDER BY T1.\"XCL_040\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:877"
  ]
}
```

### Circuit Name

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_006\", T1.\"XCL_007\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Australian Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:854"
  ]
}
```

### "drivers"."XCL_038" = 'Anthony' AND "drivers"."XCL_039" = 'Davidson'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Anthony' AND \"drivers\".\"XCL_039\" = 'Davidson'",
  "grain": [],
  "population_scope": "SELECT \"XCL_042\" FROM drivers WHERE \"XCL_038\" = 'Anthony' AND \"XCL_039\" = 'Davidson'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:917"
  ]
}
```

### "drivers"."XCL_041" = 'German'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_041\" = 'German'",
  "grain": [],
  "population_scope": "SELECT \"XCL_035\" FROM drivers WHERE \"XCL_041\" = 'German' ORDER BY JULIANDAY(\"XCL_040\") ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:971"
  ]
}
```

### Driver Last Name

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_038\", T2.\"XCL_039\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_058\" = T2.\"XCL_034\" INNER JOIN races AS T3 ON T1.\"XCL_057\" = T3.\"XCL_065\" WHERE NOT \"XCL_064\" IS NULL AND T3.\"XCL_066\" = 2008 AND T3.\"XCL_068\" IN (SELECT \"XCL_001\" FROM circuits WHERE \"XCL_003\" = 'Marina Bay Street Circuit') ORDER BY CAST(SUBSTRING(\"XCL_064\", 1, INSTR(\"XCL_064\", ':') - 1) AS INTEGER) * 60 + CAST(SUBSTRING(\"XCL_064\", INSTR(\"XCL_064\", ':') + 1, INSTR(\"XCL_064\", '.') - INSTR(\"XCL_064\", ':') - 1) AS REAL) + CAST(SUBSTRING(\"XCL_064\", INSTR(\"XCL_064\", '.') + 1) AS REAL) / 1000 ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1001"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_041\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_041\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE T2.\"XCL_074\" = 933 AND NOT T2.\"XCL_088\" IS NULL ORDER BY T2.\"XCL_089\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:867"
  ]
}
```

### "lapTimes"."XCL_043" = 348

```json
{
  "kind": "predicate",
  "formula": "\"lapTimes\".\"XCL_043\" = 348",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_038\", T2.\"XCL_039\" FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_044\" WHERE T1.\"XCL_043\" = 348 ORDER BY T1.\"XCL_047\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:878"
  ]
}
```

### The value of column XCL_004 from the circuits table, associated with the circuit where the race with the highest lap time value (XCL_045) took place.

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_045\", T2.\"XCL_069\", T2.\"XCL_066\", T1.\"XCL_004\" FROM circuits AS T1 INNER JOIN races AS T2 ON T1.\"XCL_001\" = T2.\"XCL_068\" INNER JOIN lapTimes AS T3 ON T3.\"XCL_043\" = T2.\"XCL_065\" ORDER BY T3.\"XCL_045\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:908"
  ]
}
```

### Average Driver Standing Value

```json
{
  "kind": "metric",
  "formula": "AVG(\"driverStandings\".\"XCL_030\")",
  "grain": [],
  "population_scope": "SELECT AVG(T2.\"XCL_030\") FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_029\" = T1.\"XCL_034\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T2.\"XCL_028\" WHERE T1.\"XCL_038\" = 'Eddie' AND T1.\"XCL_039\" = 'Irvine' AND T3.\"XCL_066\" = 2000",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r1\".\"XCL_030\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      },
      {
        "role": "r1",
        "physical_table": "driverStandings"
      },
      {
        "role": "r2",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT AVG(\"r1\".\"XCL_030\") AS \"value\" FROM drivers AS \"r0\" INNER JOIN driverStandings AS \"r1\" ON \"r1\".\"XCL_029\" = \"r0\".\"XCL_034\" INNER JOIN races AS \"r2\" ON \"r2\".\"XCL_065\" = \"r1\".\"XCL_028\" WHERE \"r0\".\"XCL_038\" = 'Eddie' AND \"r0\".\"XCL_039\" = 'Irvine' AND \"r2\".\"XCL_066\" = 2000",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:905"
  ]
}
```

### Lap Time Identifier

```json
{
  "kind": "binding",
  "formula": "\"lapTimes\".\"XCL_048\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_048\" FROM lapTimes AS T1 INNER JOIN races AS T2 ON T1.\"XCL_043\" = T2.\"XCL_065\" WHERE T1.\"XCL_045\" = 1 ORDER BY T1.\"XCL_047\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:986"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_038\", T3.\"XCL_039\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T1.\"XCL_066\" = 2006 AND T1.\"XCL_069\" = 'San Marino Grand Prix' AND T2.\"XCL_079\" = 2",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_038\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      },
      {
        "role": "r1",
        "physical_table": "results"
      },
      {
        "role": "r2",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_038\" AS \"value\" FROM races AS \"r0\" INNER JOIN results AS \"r1\" ON \"r1\".\"XCL_074\" = \"r0\".\"XCL_065\" INNER JOIN drivers AS \"r2\" ON \"r2\".\"XCL_034\" = \"r1\".\"XCL_075\" WHERE \"r0\".\"XCL_066\" = 2006 AND \"r0\".\"XCL_069\" = 'San Marino Grand Prix' AND \"r1\".\"XCL_079\" = 2",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:874"
  ]
}
```

### Aggregates the count of 'XCL_075' from the 'results' table (T2) for records joined to the 'races' table (T1) where the race date 'XCL_070' is '2015-11

```json
{
  "kind": "metric",
  "formula": "COUNT(\"results\".\"XCL_075\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_075\") FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" WHERE T1.\"XCL_070\" = '2015-11-29' AND T2.\"XCL_084\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_075\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      },
      {
        "role": "r1",
        "physical_table": "results"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_075\") AS \"value\" FROM races AS \"r0\" INNER JOIN results AS \"r1\" ON \"r1\".\"XCL_074\" = \"r0\".\"XCL_065\" WHERE \"r0\".\"XCL_070\" = '2015-11-29' AND \"r1\".\"XCL_084\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:876"
  ]
}
```

### Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_066\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_066\", T3.\"XCL_069\", T3.\"XCL_070\", T3.\"XCL_071\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_058\" = T2.\"XCL_034\" INNER JOIN races AS T3 ON T1.\"XCL_057\" = T3.\"XCL_065\" WHERE T1.\"XCL_058\" = (SELECT \"XCL_034\" FROM drivers ORDER BY \"XCL_040\" DESC LIMIT 1) ORDER BY T3.\"XCL_070\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:981"
  ]
}
```

### Average Result Position

```json
{
  "kind": "metric",
  "formula": "AVG(\"results\".\"XCL_088\")",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_088\") FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T1.\"XCL_087\" < 11 AND T2.\"XCL_066\" = 2006 AND T2.\"XCL_069\" = 'United States Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_088\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_088\") AS \"value\" FROM results AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_074\" = \"r1\".\"XCL_065\" WHERE \"r0\".\"XCL_087\" < 11 AND \"r1\".\"XCL_066\" = 2006 AND \"r1\".\"XCL_069\" = 'United States Grand Prix'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:987"
  ]
}
```

### Constructor Identifier

```json
{
  "kind": "binding",
  "formula": "\"constructors\".\"XCL_024\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_024\" FROM results AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_076\" = T2.\"XCL_022\" WHERE T1.\"XCL_087\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:952"
  ]
}
```

### Distinct values of the race identifier column (XCL_066) from the races table, representing the specific races in which the driver Lewis Hamilton parti

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_066\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_066\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T3.\"XCL_038\" = 'Lewis' AND T3.\"XCL_039\" = 'Hamilton'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:932"
  ]
}
```

### Race Name

```json
{
  "kind": "binding",
  "formula": "T2.\"XCL_069\"",
  "grain": [],
  "population_scope": "WITH fastest_lap_times AS (SELECT T1.\"XCL_074\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL) SELECT T2.\"XCL_069\" FROM races AS T2 INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" INNER JOIN results AS T1 ON T2.\"XCL_065\" = T1.\"XCL_074\" INNER JOIN (SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix') AS T4 ON (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) = T4.\"min_time_in_seconds\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix'",
  "upstream_scopes": [
    "SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix'",
    "SELECT T1.\"XCL_074\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1015"
  ]
}
```

### An aggregated metric representing the minimum (fastest) lap time in seconds across all races held at circuits located in Italy. It is calculated by jo

```json
{
  "kind": "metric",
  "formula": "MIN((CAST(SUBSTRING(\"results\".\"XCL_088\", 1, INSTR(\"results\".\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(\"results\".\"XCL_088\", INSTR(\"results\".\"XCL_088\", ':') + 1, INSTR(\"results\".\"XCL_088\", '.') - INSTR(\"results\".\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(\"results\".\"XCL_088\", INSTR(\"results\".\"XCL_088\", '.') + 1) AS REAL) / 1000))",
  "grain": [],
  "population_scope": "SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T3.\"XCL_005\" = 'Italy'",
  "upstream_scopes": [
    "SELECT T1.\"XCL_074\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1014"
  ]
}
```

### "drivers"."XCL_041" = 'British' AND STRFTIME('%Y', "drivers"."XCL_040") > '1980'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_041\" = 'British' AND STRFTIME('%Y', \"drivers\".\"XCL_040\") > '1980'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_034\") FROM drivers WHERE \"XCL_041\" = 'British' AND STRFTIME('%Y', \"XCL_040\") > '1980'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:947"
  ]
}
```

### "status"."XCL_093" = 3 AND "races"."XCL_069" = 'Canadian Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"status\".\"XCL_093\" = 3 AND \"races\".\"XCL_069\" = 'Canadian Grand Prix'",
  "grain": [
    "\"results\".\"XCL_075\""
  ],
  "population_scope": "SELECT COUNT(T1.\"XCL_075\") FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN status AS T3 ON T1.\"XCL_090\" = T3.\"XCL_093\" WHERE T3.\"XCL_093\" = 3 AND T2.\"XCL_069\" = 'Canadian Grand Prix' GROUP BY T1.\"XCL_075\" ORDER BY COUNT(T1.\"XCL_075\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1003"
  ]
}
```

### Race Identifier for Barcelona Circuit

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_070\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_070\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Circuit de Barcelona-Catalunya'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_070\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_070\" AS \"value\" FROM circuits AS \"r0\" INNER JOIN races AS \"r1\" ON \"r1\".\"XCL_068\" = \"r0\".\"XCL_001\" WHERE \"r0\".\"XCL_003\" = 'Circuit de Barcelona-Catalunya'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:924"
  ]
}
```

### Calculates the percentage of driver standings records where the position (XCL_031) is not 1, relative to the total number of standings records (XCL_02

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN \"driverStandings\".\"XCL_031\" <> 1 THEN \"driverStandings\".\"XCL_031\" END) AS REAL) * 100 / COUNT(\"driverStandings\".\"XCL_027\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T2.\"XCL_031\" <> 1 THEN T2.\"XCL_031\" END) AS REAL) * 100 / COUNT(T2.\"XCL_027\") FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" WHERE T3.\"XCL_039\" = 'Hamilton' AND T1.\"XCL_066\" >= 2010",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(CASE WHEN \"r1\".\"XCL_031\" <> 1 THEN \"r1\".\"XCL_031\" END) AS REAL) * 100 / COUNT(\"r1\".\"XCL_027\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      },
      {
        "role": "r1",
        "physical_table": "driverStandings"
      },
      {
        "role": "r2",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(CASE WHEN \"r1\".\"XCL_031\" <> 1 THEN \"r1\".\"XCL_031\" END) AS REAL) * 100 / COUNT(\"r1\".\"XCL_027\") AS \"value\" FROM races AS \"r0\" INNER JOIN driverStandings AS \"r1\" ON \"r1\".\"XCL_028\" = \"r0\".\"XCL_065\" INNER JOIN drivers AS \"r2\" ON \"r2\".\"XCL_034\" = \"r1\".\"XCL_029\" WHERE \"r2\".\"XCL_039\" = 'Hamilton' AND \"r0\".\"XCL_066\" >= 2010",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:896"
  ]
}
```

### Driver Name

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE T2.\"XCL_074\" = 872 AND NOT T2.\"XCL_084\" IS NULL ORDER BY T1.\"XCL_040\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:877"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_038\", T3.\"XCL_039\", T2.\"XCL_030\" FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" ORDER BY T2.\"XCL_030\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:892"
  ]
}
```

### "drivers"."XCL_038" = 'Lewis' AND "drivers"."XCL_039" = 'Hamilton'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Lewis' AND \"drivers\".\"XCL_039\" = 'Hamilton'",
  "grain": [],
  "population_scope": "SELECT SUM(T2.\"XCL_082\") FROM drivers AS T1 INNER JOIN results AS T2 ON T1.\"XCL_034\" = T2.\"XCL_075\" WHERE T1.\"XCL_038\" = 'Lewis' AND T1.\"XCL_039\" = 'Hamilton'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:941"
  ]
}
```

### Constructor Identifier

```json
{
  "kind": "binding",
  "formula": "\"constructors\".\"XCL_024\"",
  "grain": [
    "\"constructors\".\"XCL_024\""
  ],
  "population_scope": "SELECT SUM(T1.\"XCL_013\"), T2.\"XCL_024\", T2.\"XCL_025\" FROM constructorResults AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_012\" = T2.\"XCL_022\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T1.\"XCL_011\" WHERE T3.\"XCL_069\" = 'Monaco Grand Prix' AND T3.\"XCL_066\" BETWEEN 1980 AND 2010 GROUP BY T2.\"XCL_024\" ORDER BY SUM(T1.\"XCL_013\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:994"
  ]
}
```

### "circuits"."XCL_005" = 'Italy'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_005\" = 'Italy'",
  "grain": [],
  "population_scope": "SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T3.\"XCL_005\" = 'Italy'",
  "upstream_scopes": [
    "SELECT T1.\"XCL_074\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1014"
  ]
}
```

### "races"."XCL_069" = 'Singapore Grand Prix' AND "races"."XCL_066" = 2009 AND "results"."XCL_084" LIKE '_:%:__.___'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Singapore Grand Prix' AND \"races\".\"XCL_066\" = 2009 AND \"results\".\"XCL_084\" LIKE '_:%:__.___'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_023\", T3.\"XCL_026\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN constructors AS T3 ON T1.\"XCL_076\" = T3.\"XCL_022\" WHERE T2.\"XCL_069\" = 'Singapore Grand Prix' AND T2.\"XCL_066\" = 2009 AND T1.\"XCL_084\" LIKE '_:%:__.___'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:990"
  ]
}
```

### "races"."XCL_069" = 'Australian Grand Prix' AND NOT "results"."XCL_084" IS NULL AND "races"."XCL_066" = 2008

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Australian Grand Prix' AND NOT \"results\".\"XCL_084\" IS NULL AND \"races\".\"XCL_066\" = 2008",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6) AS REAL) ELSE CAST(SUBSTRING(T1.\"XCL_084\", 2) AS REAL) END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Australian Grand Prix' AND NOT T1.\"XCL_084\" IS NULL AND T2.\"XCL_066\" = 2008",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:944"
  ]
}
```

### Driver First Name

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_038\", T3.\"XCL_039\", T2.\"XCL_030\" FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_069\" = 'Chinese Grand Prix' AND T1.\"XCL_066\" = 2017 ORDER BY T2.\"XCL_030\" DESC LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:893"
  ]
}
```

### "results"."XCL_090" = 2 AND "results"."XCL_074" < 100 AND "results"."XCL_074" > 50

```json
{
  "kind": "predicate",
  "formula": "\"results\".\"XCL_090\" = 2 AND \"results\".\"XCL_074\" < 100 AND \"results\".\"XCL_074\" > 50",
  "grain": [],
  "population_scope": "SELECT SUM(IIF(NOT \"XCL_084\" IS NULL, 1, 0)) FROM results WHERE \"XCL_090\" = 2 AND \"XCL_074\" < 100 AND \"XCL_074\" > 50",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:977"
  ]
}
```

### "circuits"."XCL_003" = 'Hungaroring'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_003\" = 'Hungaroring'",
  "grain": [],
  "population_scope": "SELECT \"XCL_005\", \"XCL_006\", \"XCL_007\" FROM circuits WHERE \"XCL_003\" = 'Hungaroring'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:993"
  ]
}
```

### Driver Standing Value

```json
{
  "kind": "binding",
  "formula": "\"driverStandings\".\"XCL_030\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_038\", T3.\"XCL_039\", T2.\"XCL_030\" FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" ORDER BY T2.\"XCL_030\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:892"
  ]
}
```

### "drivers"."XCL_038" = 'Lewis' AND "drivers"."XCL_039" = 'Hamilton'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Lewis' AND \"drivers\".\"XCL_039\" = 'Hamilton'",
  "grain": [],
  "population_scope": "SELECT \"XCL_034\" FROM drivers WHERE \"XCL_038\" = 'Lewis' AND \"XCL_039\" = 'Hamilton'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:930"
  ]
}
```

### Lewis Hamilton Lap Time

```json
{
  "kind": "binding",
  "formula": "\"lapTimes\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_047\" FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_044\" = T2.\"XCL_034\" WHERE T2.\"XCL_038\" = 'Lewis' AND T2.\"XCL_039\" = 'Hamilton'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_047\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "lapTimes"
      },
      {
        "role": "r1",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_047\" AS \"value\" FROM lapTimes AS \"r0\" INNER JOIN drivers AS \"r1\" ON \"r0\".\"XCL_044\" = \"r1\".\"XCL_034\" WHERE \"r1\".\"XCL_038\" = 'Lewis' AND \"r1\".\"XCL_039\" = 'Hamilton'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1010"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_037\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_037\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 45 AND T1.\"XCL_064\" LIKE '1:33%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_037\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "qualifying"
      },
      {
        "role": "r1",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_037\" AS \"value\" FROM qualifying AS \"r0\" INNER JOIN drivers AS \"r1\" ON \"r1\".\"XCL_034\" = \"r0\".\"XCL_058\" WHERE \"r0\".\"XCL_057\" = 45 AND \"r0\".\"XCL_064\" LIKE '1:33%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:872"
  ]
}
```

### Pit Stop Duration

```json
{
  "kind": "binding",
  "formula": "\"pitStops\".\"XCL_054\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_054\" FROM pitStops AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_050\" = T2.\"XCL_034\" WHERE T2.\"XCL_038\" = 'Lewis' AND T2.\"XCL_039\" = 'Hamilton' ORDER BY T1.\"XCL_054\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1007"
  ]
}
```

### Driver Identifier 1

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT STRFTIME('%Y', CURRENT_TIMESTAMP) - STRFTIME('%Y', \"XCL_040\"), \"XCL_038\", \"XCL_039\" FROM drivers WHERE \"XCL_041\" = 'Japanese' ORDER BY \"XCL_040\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:898"
  ]
}
```

### Driver Identifier XCL_038

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_038\", \"XCL_039\", \"XCL_042\", \"XCL_040\" FROM drivers WHERE \"XCL_041\" = 'German' AND STRFTIME('%Y', \"XCL_040\") BETWEEN '1971' AND '1985' ORDER BY \"XCL_040\" DESC",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_038\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_038\" AS \"value\" FROM drivers AS \"r0\" WHERE \"r0\".\"XCL_041\" = 'German' AND STRFTIME('%Y', \"r0\".\"XCL_040\") BETWEEN '1971' AND '1985'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:992"
  ]
}
```

### Qualifying Session Timestamp

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_070\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_066\", T3.\"XCL_069\", T3.\"XCL_070\", T3.\"XCL_071\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_058\" = T2.\"XCL_034\" INNER JOIN races AS T3 ON T1.\"XCL_057\" = T3.\"XCL_065\" WHERE T1.\"XCL_058\" = (SELECT \"XCL_034\" FROM drivers ORDER BY \"XCL_040\" DESC LIMIT 1) ORDER BY T3.\"XCL_070\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:981"
  ]
}
```

### Result Identifier

```json
{
  "kind": "binding",
  "formula": "\"results\".\"XCL_081\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_081\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T3.\"XCL_038\" = 'Lewis' AND T3.\"XCL_039\" = 'Hamilton' AND T1.\"XCL_069\" = 'Chinese Grand Prix' AND T1.\"XCL_066\" = 2008",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_081\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      },
      {
        "role": "r1",
        "physical_table": "results"
      },
      {
        "role": "r2",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_081\" AS \"value\" FROM races AS \"r0\" INNER JOIN results AS \"r1\" ON \"r1\".\"XCL_074\" = \"r0\".\"XCL_065\" INNER JOIN drivers AS \"r2\" ON \"r2\".\"XCL_034\" = \"r1\".\"XCL_075\" WHERE \"r2\".\"XCL_038\" = 'Lewis' AND \"r2\".\"XCL_039\" = 'Hamilton' AND \"r0\".\"XCL_069\" = 'Chinese Grand Prix' AND \"r0\".\"XCL_066\" = 2008",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:933"
  ]
}
```

### "qualifying"."XCL_057" = 19

```json
{
  "kind": "predicate",
  "formula": "\"qualifying\".\"XCL_057\" = 19",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_039\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 19 ORDER BY T1.\"XCL_063\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:847"
  ]
}
```

### Driver Name (XCL_039)

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_038\", T3.\"XCL_039\" FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_075\" WHERE T2.\"XCL_078\" = 4 AND T1.\"XCL_069\" = 'Australian Grand Prix' AND T1.\"XCL_066\" = 1989",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_039\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "races"
      },
      {
        "role": "r1",
        "physical_table": "results"
      },
      {
        "role": "r2",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_039\" AS \"value\" FROM races AS \"r0\" INNER JOIN results AS \"r1\" ON \"r1\".\"XCL_074\" = \"r0\".\"XCL_065\" INNER JOIN drivers AS \"r2\" ON \"r2\".\"XCL_034\" = \"r1\".\"XCL_075\" WHERE \"r1\".\"XCL_078\" = 4 AND \"r0\".\"XCL_069\" = 'Australian Grand Prix' AND \"r0\".\"XCL_066\" = 1989",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:934"
  ]
}
```

### "races"."XCL_066" = 2009 AND "results"."XCL_084" LIKE '_:%:__.___'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_066\" = 2009 AND \"results\".\"XCL_084\" LIKE '_:%:__.___'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_086\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_066\" = 2009 AND T1.\"XCL_084\" LIKE '_:%:__.___'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:959"
  ]
}
```

### Average Driver Standing Value

```json
{
  "kind": "metric",
  "formula": "AVG(\"driverStandings\".\"XCL_030\")",
  "grain": [],
  "population_scope": "SELECT AVG(T2.\"XCL_030\") FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" INNER JOIN races AS T3 ON T3.\"XCL_065\" = T2.\"XCL_028\" WHERE T1.\"XCL_038\" = 'Lewis' AND T1.\"XCL_039\" = 'Hamilton' AND T3.\"XCL_069\" = 'Turkish Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r1\".\"XCL_030\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      },
      {
        "role": "r1",
        "physical_table": "driverStandings"
      },
      {
        "role": "r2",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT AVG(\"r1\".\"XCL_030\") AS \"value\" FROM drivers AS \"r0\" INNER JOIN driverStandings AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_029\" INNER JOIN races AS \"r2\" ON \"r2\".\"XCL_065\" = \"r1\".\"XCL_028\" WHERE \"r0\".\"XCL_038\" = 'Lewis' AND \"r0\".\"XCL_039\" = 'Hamilton' AND \"r2\".\"XCL_069\" = 'Turkish Grand Prix'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:995"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_038\", T2.\"XCL_039\", T2.\"XCL_042\" FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_044\" WHERE T1.\"XCL_043\" = 161 AND T1.\"XCL_047\" LIKE '1:27%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:866"
  ]
}
```

### Circuit Name

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_005\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_069\", T1.\"XCL_005\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_066\" = 2017 ORDER BY T2.\"XCL_070\" ASC",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:907"
  ]
}
```

### "lapTimes"."XCL_045" = 1

```json
{
  "kind": "predicate",
  "formula": "\"lapTimes\".\"XCL_045\" = 1",
  "grain": [],
  "population_scope": "SELECT \"XCL_044\" FROM lapTimes WHERE \"XCL_045\" = 1 ORDER BY \"XCL_047\" LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:976"
  ]
}
```

### "results"."XCL_074" = 933 AND NOT "results"."XCL_088" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"results\".\"XCL_074\" = 933 AND NOT \"results\".\"XCL_088\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_041\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE T2.\"XCL_074\" = 933 AND NOT T2.\"XCL_088\" IS NULL ORDER BY T2.\"XCL_089\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:867"
  ]
}
```

### The value of column XCL_041 from the drivers table for the single driver associated with the result having the highest value in column XCL_089. The gr

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_041\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_041\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" ORDER BY T2.\"XCL_089\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:879"
  ]
}
```

### Circuit Identifier

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_006\", T1.\"XCL_007\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Australian Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:854"
  ]
}
```

### Fastest Lap Time

```json
{
  "kind": "binding",
  "formula": "\"results\".\"XCL_088\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_074\", T1.\"XCL_075\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_088\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_088\" AS \"value\" FROM results AS \"r0\" WHERE NOT \"r0\".\"XCL_088\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1016",
    "bird_dev:1014",
    "bird_dev:1013",
    "bird_dev:1015"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_038\", T2.\"XCL_039\" FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_044\" WHERE T1.\"XCL_043\" = 348 ORDER BY T1.\"XCL_047\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:878"
  ]
}
```

### "lapTimes"."XCL_047" = '1:29.488'

```json
{
  "kind": "predicate",
  "formula": "\"lapTimes\".\"XCL_047\" = '1:29.488'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_006\", T3.\"XCL_007\" FROM lapTimes AS T1 INNER JOIN races AS T2 ON T1.\"XCL_043\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T1.\"XCL_047\" = '1:29.488'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1017"
  ]
}
```

### "qualifying"."XCL_057" = 903 AND "qualifying"."XCL_064" LIKE '1:54%'

```json
{
  "kind": "predicate",
  "formula": "\"qualifying\".\"XCL_057\" = 903 AND \"qualifying\".\"XCL_064\" LIKE '1:54%'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_036\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 903 AND T1.\"XCL_064\" LIKE '1:54%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:861"
  ]
}
```

### Maximum XCL_054 Value

```json
{
  "kind": "binding",
  "formula": "\"pitStops\".\"XCL_054\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_054\" FROM pitStops ORDER BY \"XCL_054\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1005"
  ]
}
```

### Circuit Attribute XCL_007

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_005\", \"XCL_006\", \"XCL_007\" FROM circuits WHERE \"XCL_003\" = 'Hungaroring'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_007\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_007\" AS \"value\" FROM circuits AS \"r0\" WHERE \"r0\".\"XCL_003\" = 'Hungaroring'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:993"
  ]
}
```

### Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_070\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_070\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Brands Hatch' AND T2.\"XCL_069\" = 'British Grand Prix' ORDER BY T2.\"XCL_066\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:889"
  ]
}
```

### "drivers"."XCL_038" = 'Lewis' AND "drivers"."XCL_039" = 'Hamilton'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Lewis' AND \"drivers\".\"XCL_039\" = 'Hamilton'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_054\" FROM pitStops AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_050\" = T2.\"XCL_034\" WHERE T2.\"XCL_038\" = 'Lewis' AND T2.\"XCL_039\" = 'Hamilton' ORDER BY T1.\"XCL_054\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1007"
  ]
}
```

### Aggregates the count of driver identifiers (XCL_034) from the drivers table, restricted to drivers with nationality 'American' (XCL_041) who have asso

```json
{
  "kind": "metric",
  "formula": "COUNT(\"drivers\".\"XCL_034\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_034\") FROM drivers AS T1 INNER JOIN results AS T2 ON T1.\"XCL_034\" = T2.\"XCL_075\" INNER JOIN status AS T3 ON T2.\"XCL_090\" = T3.\"XCL_093\" WHERE T3.\"XCL_094\" = 'Puncture' AND T1.\"XCL_041\" = 'American'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_034\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      },
      {
        "role": "r1",
        "physical_table": "results"
      },
      {
        "role": "r2",
        "physical_table": "status"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_034\") AS \"value\" FROM drivers AS \"r0\" INNER JOIN results AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_075\" INNER JOIN status AS \"r2\" ON \"r1\".\"XCL_090\" = \"r2\".\"XCL_093\" WHERE \"r2\".\"XCL_094\" = 'Puncture' AND \"r0\".\"XCL_041\" = 'American'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:982"
  ]
}
```

### Average Result Duration in Minutes

```json
{
  "kind": "metric",
  "formula": "AVG(CAST(SUBSTRING(\"results\".\"XCL_088\", 1, INSTR(\"results\".\"XCL_088\", ':') - 1) AS INTEGER) * 60 + CAST(SUBSTRING(\"results\".\"XCL_088\", INSTR(\"results\".\"XCL_088\", ':') + 1) AS REAL))",
  "grain": [],
  "population_scope": "SELECT AVG(CAST(SUBSTRING(T2.\"XCL_088\", 1, INSTR(T2.\"XCL_088\", ':') - 1) AS INTEGER) * 60 + CAST(SUBSTRING(T2.\"XCL_088\", INSTR(T2.\"XCL_088\", ':') + 1) AS REAL)) FROM drivers AS T1 INNER JOIN results AS T2 ON T1.\"XCL_034\" = T2.\"XCL_075\" WHERE T1.\"XCL_039\" = 'Hamilton' AND T1.\"XCL_038\" = 'Lewis'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(CAST(SUBSTRING(\"r1\".\"XCL_088\", 1, INSTR(\"r1\".\"XCL_088\", ':') - 1) AS INTEGER) * 60 + CAST(SUBSTRING(\"r1\".\"XCL_088\", INSTR(\"r1\".\"XCL_088\", ':') + 1) AS REAL))",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      },
      {
        "role": "r1",
        "physical_table": "results"
      }
    ],
    "scope_sql": "SELECT AVG(CAST(SUBSTRING(\"r1\".\"XCL_088\", 1, INSTR(\"r1\".\"XCL_088\", ':') - 1) AS INTEGER) * 60 + CAST(SUBSTRING(\"r1\".\"XCL_088\", INSTR(\"r1\".\"XCL_088\", ':') + 1) AS REAL)) AS \"value\" FROM drivers AS \"r0\" INNER JOIN results AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_075\" WHERE \"r0\".\"XCL_039\" = 'Hamilton' AND \"r0\".\"XCL_038\" = 'Lewis'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:942"
  ]
}
```

### "results"."XCL_074" = 743 AND "drivers"."XCL_038" = 'Bruce' AND "drivers"."XCL_039" = 'McLaren'

```json
{
  "kind": "predicate",
  "formula": "\"results\".\"XCL_074\" = 743 AND \"drivers\".\"XCL_038\" = 'Bruce' AND \"drivers\".\"XCL_039\" = 'McLaren'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_084\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE T2.\"XCL_074\" = 743 AND T1.\"XCL_038\" = 'Bruce' AND T1.\"XCL_039\" = 'McLaren'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:873"
  ]
}
```

### "drivers"."XCL_041" = 'German' AND STRFTIME('%Y', "drivers"."XCL_040") BETWEEN '1980' AND '1985'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_041\" = 'German' AND STRFTIME('%Y', \"drivers\".\"XCL_040\") BETWEEN '1980' AND '1985'",
  "grain": [
    "\"drivers\".\"XCL_038\"",
    "\"drivers\".\"XCL_039\""
  ],
  "population_scope": "SELECT T2.\"XCL_038\", T2.\"XCL_039\" FROM pitStops AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_050\" = T2.\"XCL_034\" WHERE T2.\"XCL_041\" = 'German' AND STRFTIME('%Y', T2.\"XCL_040\") BETWEEN '1980' AND '1985' GROUP BY T2.\"XCL_038\", T2.\"XCL_039\" ORDER BY AVG(T1.\"XCL_054\") LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:988"
  ]
}
```

### Driver Attribute XCL_042

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_042\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_038\", \"XCL_039\", \"XCL_042\", \"XCL_040\" FROM drivers WHERE \"XCL_041\" = 'German' AND STRFTIME('%Y', \"XCL_040\") BETWEEN '1971' AND '1985' ORDER BY \"XCL_040\" DESC",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_042\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_042\" AS \"value\" FROM drivers AS \"r0\" WHERE \"r0\".\"XCL_041\" = 'German' AND STRFTIME('%Y', \"r0\".\"XCL_040\") BETWEEN '1971' AND '1985'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:992"
  ]
}
```

### "results"."XCL_087" = 1

```json
{
  "kind": "predicate",
  "formula": "\"results\".\"XCL_087\" = 1",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_024\" FROM results AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_076\" = T2.\"XCL_022\" WHERE T1.\"XCL_087\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:952"
  ]
}
```

### "drivers"."XCL_038" = 'Lewis' AND "drivers"."XCL_039" = 'Hamilton' AND "races"."XCL_066" = 2009 AND "races"."XCL_069" = 'Malaysian Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Lewis' AND \"drivers\".\"XCL_039\" = 'Hamilton' AND \"races\".\"XCL_066\" = 2009 AND \"races\".\"XCL_069\" = 'Malaysian Grand Prix'",
  "grain": [],
  "population_scope": "SELECT AVG(T2.\"XCL_048\") FROM races AS T1 INNER JOIN lapTimes AS T2 ON T2.\"XCL_043\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_044\" WHERE T3.\"XCL_038\" = 'Lewis' AND T3.\"XCL_039\" = 'Hamilton' AND T1.\"XCL_066\" = 2009 AND T1.\"XCL_069\" = 'Malaysian Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:895"
  ]
}
```

### Aggregates the total number of non-null values in the XCL_029 column from the driverStandings table, restricted to rows where XCL_028 equals 18. Retur

```json
{
  "kind": "metric",
  "formula": "COUNT(\"driverStandings\".\"XCL_029\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_029\") FROM driverStandings WHERE \"XCL_028\" = 18",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_029\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "driverStandings"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_029\") AS \"value\" FROM driverStandings AS \"r0\" WHERE \"r0\".\"XCL_028\" = 18",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:966"
  ]
}
```

### Calculates the percentage difference between the sum of XCL_089 where XCL_074 is 854 and the sum of XCL_089 where XCL_074 is 853, using the 853 sum as

```json
{
  "kind": "metric",
  "formula": "(SUM(IIF(\"results\".\"XCL_074\" = 853, \"results\".\"XCL_089\", 0)) - SUM(IIF(\"results\".\"XCL_074\" = 854, \"results\".\"XCL_089\", 0))) * 100 / SUM(IIF(\"results\".\"XCL_074\" = 853, \"results\".\"XCL_089\", 0))",
  "grain": [],
  "population_scope": "SELECT (SUM(IIF(T2.\"XCL_074\" = 853, T2.\"XCL_089\", 0)) - SUM(IIF(T2.\"XCL_074\" = 854, T2.\"XCL_089\", 0))) * 100 / SUM(IIF(T2.\"XCL_074\" = 853, T2.\"XCL_089\", 0)) FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE T1.\"XCL_038\" = 'Paul' AND T1.\"XCL_039\" = 'di Resta'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "(SUM(IIF(\"r1\".\"XCL_074\" = 853, \"r1\".\"XCL_089\", 0)) - SUM(IIF(\"r1\".\"XCL_074\" = 854, \"r1\".\"XCL_089\", 0))) * 100 / SUM(IIF(\"r1\".\"XCL_074\" = 853, \"r1\".\"XCL_089\", 0))",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      },
      {
        "role": "r1",
        "physical_table": "results"
      }
    ],
    "scope_sql": "SELECT (SUM(IIF(\"r1\".\"XCL_074\" = 853, \"r1\".\"XCL_089\", 0)) - SUM(IIF(\"r1\".\"XCL_074\" = 854, \"r1\".\"XCL_089\", 0))) * 100 / SUM(IIF(\"r1\".\"XCL_074\" = 853, \"r1\".\"XCL_089\", 0)) AS \"value\" FROM drivers AS \"r0\" INNER JOIN results AS \"r1\" ON \"r1\".\"XCL_075\" = \"r0\".\"XCL_034\" WHERE \"r0\".\"XCL_038\" = 'Paul' AND \"r0\".\"XCL_039\" = 'di Resta'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:880"
  ]
}
```

### Counts the number of race records (races.XCL_068) associated with a specific circuit and race name. The grain is a single aggregate value representing

```json
{
  "kind": "metric",
  "formula": "COUNT(\"races\".\"XCL_068\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_068\") FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_003\" = 'Silverstone Circuit' AND T2.\"XCL_069\" = 'British Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_068\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_068\") AS \"value\" FROM circuits AS \"r0\" INNER JOIN races AS \"r1\" ON \"r1\".\"XCL_068\" = \"r0\".\"XCL_001\" WHERE \"r0\".\"XCL_003\" = 'Silverstone Circuit' AND \"r1\".\"XCL_069\" = 'British Grand Prix'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:890"
  ]
}
```

### Constructor Nationality

```json
{
  "kind": "binding",
  "formula": "\"constructors\".\"XCL_026\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_023\", T3.\"XCL_026\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN constructors AS T3 ON T1.\"XCL_076\" = T3.\"XCL_022\" WHERE T2.\"XCL_069\" = 'Singapore Grand Prix' AND T2.\"XCL_066\" = 2009 AND T1.\"XCL_084\" LIKE '_:%:__.___'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_026\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "races"
      },
      {
        "role": "r2",
        "physical_table": "constructors"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_026\" AS \"value\" FROM results AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_074\" = \"r1\".\"XCL_065\" INNER JOIN constructors AS \"r2\" ON \"r0\".\"XCL_076\" = \"r2\".\"XCL_022\" WHERE \"r1\".\"XCL_069\" = 'Singapore Grand Prix' AND \"r1\".\"XCL_066\" = 2009 AND \"r0\".\"XCL_084\" LIKE '_:%:__.___'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:990"
  ]
}
```

### "races"."XCL_066" = 2005

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_066\" = 2005",
  "grain": [],
  "population_scope": "SELECT \"XCL_069\" FROM races WHERE \"XCL_066\" = 2005 ORDER BY \"XCL_069\" DESC",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:883"
  ]
}
```

### Circuit Identifier

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_004\" FROM circuits AS T1 INNER JOIN races AS T2 ON T1.\"XCL_001\" = T2.\"XCL_068\" ORDER BY T2.\"XCL_070\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1000"
  ]
}
```

### Aggregates the total number of race records (identified by XCL_068) associated with circuits located in Italy. The population is restricted to circuit

```json
{
  "kind": "metric",
  "formula": "COUNT(\"races\".\"XCL_068\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_068\") FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_005\" = 'Italy'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_068\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_068\") AS \"value\" FROM circuits AS \"r0\" INNER JOIN races AS \"r1\" ON \"r1\".\"XCL_068\" = \"r0\".\"XCL_001\" WHERE \"r0\".\"XCL_005\" = 'Italy'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:923"
  ]
}
```

### Race Name/ID for Lewis Hamilton Wins

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_069\" FROM races WHERE \"XCL_065\" IN (SELECT \"XCL_074\" FROM results WHERE \"XCL_087\" = 1 AND \"XCL_075\" = (SELECT \"XCL_034\" FROM drivers WHERE \"XCL_038\" = 'Lewis' AND \"XCL_039\" = 'Hamilton'))",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:930"
  ]
}
```

### Driver Name (First)

```json
{
  "kind": "binding",
  "formula": "T2.\"XCL_038\"",
  "grain": [],
  "population_scope": "WITH lap_times_in_seconds AS (SELECT \"XCL_044\", (CASE WHEN SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) AS REAL) * 60 ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) AS REAL) ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) AS REAL) / 1000 ELSE 0 END) AS time_in_seconds FROM lapTimes) SELECT T2.\"XCL_038\", T2.\"XCL_039\", T1.\"XCL_044\" FROM (SELECT \"XCL_044\", MIN(\"time_in_seconds\") AS min_time_in_seconds FROM lap_times_in_seconds GROUP BY \"XCL_044\") AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_044\" = T2.\"XCL_034\" ORDER BY T1.\"min_time_in_seconds\" ASC LIMIT 20",
  "upstream_scopes": [
    "SELECT \"XCL_044\", (CASE WHEN SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) AS REAL) * 60 ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) AS REAL) ELSE 0 END + CASE WHEN SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) <> '' THEN CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) AS REAL) / 1000 ELSE 0 END) AS time_in_seconds FROM lapTimes",
    "SELECT \"XCL_044\", MIN(\"time_in_seconds\") AS min_time_in_seconds FROM lap_times_in_seconds GROUP BY \"XCL_044\""
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1011"
  ]
}
```

### Distinct values of the race identifier column (XCL_069) from the races table, filtered to include only races associated with circuits located in Germa

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_069\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_005\" = 'Germany'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:850"
  ]
}
```

### Aggregates the sum of column XCL_033 from the driverStandings table, restricted to rows where column XCL_030 equals 91. Returns a single scalar value 

```json
{
  "kind": "metric",
  "formula": "SUM(CASE WHEN \"driverStandings\".\"XCL_030\" = 91 THEN \"driverStandings\".\"XCL_033\" ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN \"XCL_030\" = 91 THEN \"XCL_033\" ELSE 0 END) FROM driverStandings",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(CASE WHEN \"r0\".\"XCL_030\" = 91 THEN \"r0\".\"XCL_033\" ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "driverStandings"
      }
    ],
    "scope_sql": "SELECT SUM(CASE WHEN \"r0\".\"XCL_030\" = 91 THEN \"r0\".\"XCL_033\" ELSE 0 END) AS \"value\" FROM driverStandings AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:998"
  ]
}
```

### "drivers"."XCL_041" = 'Japanese' AND "races"."XCL_066" BETWEEN 2007 AND 2009

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_041\" = 'Japanese' AND \"races\".\"XCL_066\" BETWEEN 2007 AND 2009",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(NOT T1.\"XCL_084\" IS NULL, 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_074\") FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN drivers AS T3 ON T1.\"XCL_075\" = T3.\"XCL_034\" WHERE T3.\"XCL_041\" = 'Japanese' AND T2.\"XCL_066\" BETWEEN 2007 AND 2009",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:954"
  ]
}
```

### Aggregates the count of 'XCL_075' values from the 'results' table where the associated driver in the 'drivers' table has 'XCL_041' equal to 'Italian' 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"results\".\"XCL_075\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_075\") FROM results AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_075\" = T2.\"XCL_034\" WHERE T2.\"XCL_041\" = 'Italian' AND T1.\"XCL_084\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_075\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_075\") AS \"value\" FROM results AS \"r0\" INNER JOIN drivers AS \"r1\" ON \"r0\".\"XCL_075\" = \"r1\".\"XCL_034\" WHERE \"r1\".\"XCL_041\" = 'Italian' AND \"r0\".\"XCL_084\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:957"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_038\", \"XCL_039\", \"XCL_040\" FROM drivers WHERE \"XCL_041\" = 'Austrian' AND STRFTIME('%Y', \"XCL_040\") BETWEEN '1981' AND '1991'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_038\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_038\" AS \"value\" FROM drivers AS \"r0\" WHERE \"r0\".\"XCL_041\" = 'Austrian' AND STRFTIME('%Y', \"r0\".\"XCL_040\") BETWEEN '1981' AND '1991'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:991"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_039\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 19 ORDER BY T1.\"XCL_063\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:847"
  ]
}
```

### "drivers"."XCL_041" = 'German' AND STRFTIME('%Y', "drivers"."XCL_040") BETWEEN '1980' AND '1990'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_041\" = 'German' AND STRFTIME('%Y', \"drivers\".\"XCL_040\") BETWEEN '1980' AND '1990'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_034\" FROM pitStops AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_050\" = T2.\"XCL_034\" WHERE T2.\"XCL_041\" = 'German' AND STRFTIME('%Y', T2.\"XCL_040\") BETWEEN '1980' AND '1990' ORDER BY T1.\"XCL_053\" LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:970"
  ]
}
```

### Driver Date XCL_040

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_040\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_038\", \"XCL_039\", \"XCL_042\", \"XCL_040\" FROM drivers WHERE \"XCL_041\" = 'German' AND STRFTIME('%Y', \"XCL_040\") BETWEEN '1971' AND '1985' ORDER BY \"XCL_040\" DESC",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_040\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_040\" AS \"value\" FROM drivers AS \"r0\" WHERE \"r0\".\"XCL_041\" = 'German' AND STRFTIME('%Y', \"r0\".\"XCL_040\") BETWEEN '1971' AND '1985'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:992"
  ]
}
```

### "races"."XCL_066" = 2010 AND "races"."XCL_069" = 'Abu Dhabi Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_066\" = 2010 AND \"races\".\"XCL_069\" = 'Abu Dhabi Grand Prix'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_070\", T2.\"XCL_071\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_066\" = 2010 AND T2.\"XCL_069\" = 'Abu Dhabi Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:922"
  ]
}
```

### "drivers"."XCL_041" = 'Italian'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_041\" = 'Italian'",
  "grain": [],
  "population_scope": "SELECT \"XCL_039\" FROM drivers WHERE \"XCL_041\" = 'Italian'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:916"
  ]
}
```

### "drivers"."XCL_041" = 'British' AND STRFTIME('%Y', "drivers"."XCL_040") = '1980'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_041\" = 'British' AND STRFTIME('%Y', \"drivers\".\"XCL_040\") = '1980'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_034\") FROM drivers WHERE \"XCL_041\" = 'British' AND STRFTIME('%Y', \"XCL_040\") = '1980'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:969"
  ]
}
```

### Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_069\", T2.\"XCL_030\" FROM races AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_028\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_029\" WHERE T3.\"XCL_038\" = 'Lewis' AND T3.\"XCL_039\" = 'Hamilton' ORDER BY T1.\"XCL_066\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:906"
  ]
}
```

### "drivers"."XCL_038" = 'Lewis' AND "drivers"."XCL_039" = 'Hamilton'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Lewis' AND \"drivers\".\"XCL_039\" = 'Hamilton'",
  "grain": [],
  "population_scope": "SELECT AVG(\"XCL_055\") FROM pitStops AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_050\" = T2.\"XCL_034\" WHERE T2.\"XCL_038\" = 'Lewis' AND T2.\"XCL_039\" = 'Hamilton'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1018"
  ]
}
```

### A driver-level attribute from the 'drivers' table (T1). It serves as a grouping key and output column, representing a specific characteristic of the d

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_041\"",
  "grain": [
    "\"drivers\".\"XCL_038\"",
    "\"drivers\".\"XCL_039\"",
    "\"drivers\".\"XCL_041\""
  ],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_041\", MAX(T2.\"XCL_030\") FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_029\" = T1.\"XCL_034\" WHERE T2.\"XCL_033\" >= 1 GROUP BY T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_041\" ORDER BY COUNT(T2.\"XCL_033\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:897"
  ]
}
```

### Circuit Identifier

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_006\", T1.\"XCL_007\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Malaysian Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:868"
  ]
}
```

### Calculates the percentage of result rows where the column XCL_084 is not null, relative to the total count of result rows (XCL_074). The computation a

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(NOT \"results\".\"XCL_084\" IS NULL, 1, 0)) AS REAL) * 100 / COUNT(\"results\".\"XCL_074\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(NOT T1.\"XCL_084\" IS NULL, 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_074\") FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN drivers AS T3 ON T1.\"XCL_075\" = T3.\"XCL_034\" WHERE T3.\"XCL_041\" = 'Japanese' AND T2.\"XCL_066\" BETWEEN 2007 AND 2009",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(IIF(NOT \"r0\".\"XCL_084\" IS NULL, 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_074\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "races"
      },
      {
        "role": "r2",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(IIF(NOT \"r0\".\"XCL_084\" IS NULL, 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_074\") AS \"value\" FROM results AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_074\" = \"r1\".\"XCL_065\" INNER JOIN drivers AS \"r2\" ON \"r0\".\"XCL_075\" = \"r2\".\"XCL_034\" WHERE \"r2\".\"XCL_041\" = 'Japanese' AND \"r1\".\"XCL_066\" BETWEEN 2007 AND 2009",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:954"
  ]
}
```

### Pit Stop Duration

```json
{
  "kind": "binding",
  "formula": "\"pitStops\".\"XCL_052\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_052\" FROM pitStops AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_050\" = T2.\"XCL_034\" INNER JOIN races AS T3 ON T1.\"XCL_049\" = T3.\"XCL_065\" WHERE T2.\"XCL_038\" = 'Lewis' AND T2.\"XCL_039\" = 'Hamilton' AND T3.\"XCL_066\" = 2011 AND T3.\"XCL_069\" = 'Australian Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_052\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "pitStops"
      },
      {
        "role": "r1",
        "physical_table": "drivers"
      },
      {
        "role": "r2",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_052\" AS \"value\" FROM pitStops AS \"r0\" INNER JOIN drivers AS \"r1\" ON \"r0\".\"XCL_050\" = \"r1\".\"XCL_034\" INNER JOIN races AS \"r2\" ON \"r0\".\"XCL_049\" = \"r2\".\"XCL_065\" WHERE \"r1\".\"XCL_038\" = 'Lewis' AND \"r1\".\"XCL_039\" = 'Hamilton' AND \"r2\".\"XCL_066\" = 2011 AND \"r2\".\"XCL_069\" = 'Australian Grand Prix'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1008"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [
    "\"drivers\".\"XCL_038\"",
    "\"drivers\".\"XCL_039\""
  ],
  "population_scope": "SELECT T2.\"XCL_038\", T2.\"XCL_039\" FROM pitStops AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_050\" = T2.\"XCL_034\" WHERE T2.\"XCL_041\" = 'German' AND STRFTIME('%Y', T2.\"XCL_040\") BETWEEN '1980' AND '1985' GROUP BY T2.\"XCL_038\", T2.\"XCL_039\" ORDER BY AVG(T1.\"XCL_054\") LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:988"
  ]
}
```

### COUNT("races"."XCL_065") = 4

```json
{
  "kind": "predicate",
  "formula": "COUNT(\"races\".\"XCL_065\") = 4",
  "grain": [
    "\"circuits\".\"XCL_003\""
  ],
  "population_scope": "SELECT DISTINCT T1.\"XCL_003\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE STRFTIME('%Y', T2.\"XCL_070\") BETWEEN '1990' AND '2000' GROUP BY T1.\"XCL_003\" HAVING COUNT(T2.\"XCL_065\") = 4",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:899"
  ]
}
```

### "constructorStandings"."XCL_018" = 0 AND "constructors"."XCL_025" = 'Japanese'

```json
{
  "kind": "predicate",
  "formula": "\"constructorStandings\".\"XCL_018\" = 0 AND \"constructors\".\"XCL_025\" = 'Japanese'",
  "grain": [
    "\"constructorStandings\".\"XCL_017\""
  ],
  "population_scope": "SELECT COUNT(T1.\"XCL_016\") FROM constructorStandings AS T1 INNER JOIN constructors AS T2 ON T1.\"XCL_017\" = T2.\"XCL_022\" WHERE T1.\"XCL_018\" = 0 AND T2.\"XCL_025\" = 'Japanese' GROUP BY T1.\"XCL_017\" HAVING COUNT(\"XCL_016\") = 2",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:951"
  ]
}
```

### A driver-level attribute from the 'drivers' table (T1). It serves as a grouping key and output column, representing a specific characteristic of the d

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [
    "\"drivers\".\"XCL_038\"",
    "\"drivers\".\"XCL_039\"",
    "\"drivers\".\"XCL_041\""
  ],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_041\", MAX(T2.\"XCL_030\") FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T2.\"XCL_029\" = T1.\"XCL_034\" WHERE T2.\"XCL_033\" >= 1 GROUP BY T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_041\" ORDER BY COUNT(T2.\"XCL_033\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:897"
  ]
}
```

### NOT "results"."XCL_088" IS NULL

```json
{
  "kind": "predicate",
  "formula": "NOT \"results\".\"XCL_088\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_066\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE NOT T1.\"XCL_088\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:974"
  ]
}
```

### NOT "results"."XCL_088" IS NULL

```json
{
  "kind": "predicate",
  "formula": "NOT \"results\".\"XCL_088\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_074\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1014",
    "bird_dev:1015"
  ]
}
```

### "drivers"."XCL_039" = 'Hamilton' AND "drivers"."XCL_038" = 'Lewis'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_039\" = 'Hamilton' AND \"drivers\".\"XCL_038\" = 'Lewis'",
  "grain": [],
  "population_scope": "SELECT AVG(CAST(SUBSTRING(T2.\"XCL_088\", 1, INSTR(T2.\"XCL_088\", ':') - 1) AS INTEGER) * 60 + CAST(SUBSTRING(T2.\"XCL_088\", INSTR(T2.\"XCL_088\", ':') + 1) AS REAL)) FROM drivers AS T1 INNER JOIN results AS T2 ON T1.\"XCL_034\" = T2.\"XCL_075\" WHERE T1.\"XCL_039\" = 'Hamilton' AND T1.\"XCL_038\" = 'Lewis'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:942"
  ]
}
```

### "races"."XCL_066" = 2009 AND "races"."XCL_069" = 'Spanish Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_066\" = 2009 AND \"races\".\"XCL_069\" = 'Spanish Grand Prix'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_009\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_066\" = 2009 AND T2.\"XCL_069\" = 'Spanish Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:925"
  ]
}
```

### The calendar year extracted from the earliest date in the races table (XCL_070), determined by ordering ascending and taking the first row.

```json
{
  "kind": "binding",
  "formula": "STRFTIME('%Y', \"races\".\"XCL_070\")",
  "grain": [],
  "population_scope": "SELECT STRFTIME('%Y', \"XCL_070\") FROM races ORDER BY \"XCL_070\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:884"
  ]
}
```

### "races"."XCL_070" = '2015-11-29' AND "results"."XCL_084" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_070\" = '2015-11-29' AND \"results\".\"XCL_084\" IS NULL",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_075\") FROM races AS T1 INNER JOIN results AS T2 ON T2.\"XCL_074\" = T1.\"XCL_065\" WHERE T1.\"XCL_070\" = '2015-11-29' AND T2.\"XCL_084\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:876"
  ]
}
```

### STRFTIME('%Y', "drivers"."XCL_040") > '1975' AND "results"."XCL_087" = 2

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"drivers\".\"XCL_040\") > '1975' AND \"results\".\"XCL_087\" = 2",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_038\", T2.\"XCL_039\" FROM results AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_075\" = T2.\"XCL_034\" WHERE STRFTIME('%Y', T2.\"XCL_040\") > '1975' AND T1.\"XCL_087\" = 2",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:956"
  ]
}
```

### Driver Name

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\", T1.\"XCL_041\", T3.\"XCL_069\" FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" INNER JOIN races AS T3 ON T2.\"XCL_028\" = T3.\"XCL_065\" ORDER BY JULIANDAY(T1.\"XCL_040\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1002"
  ]
}
```

### "qualifying"."XCL_057" = 45 AND "qualifying"."XCL_064" LIKE '1:33%'

```json
{
  "kind": "predicate",
  "formula": "\"qualifying\".\"XCL_057\" = 45 AND \"qualifying\".\"XCL_064\" LIKE '1:33%'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_037\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 45 AND T1.\"XCL_064\" LIKE '1:33%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:872"
  ]
}
```

### Minimum Fastest Lap Time (Austrian GP)

```json
{
  "kind": "metric",
  "formula": "MIN((CAST(SUBSTRING(\"results\".\"XCL_088\", 1, INSTR(\"results\".\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(\"results\".\"XCL_088\", INSTR(\"results\".\"XCL_088\", ':') + 1, INSTR(\"results\".\"XCL_088\", '.') - INSTR(\"results\".\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(\"results\".\"XCL_088\", INSTR(\"results\".\"XCL_088\", '.') + 1) AS REAL) / 1000))",
  "grain": [],
  "population_scope": "SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix'",
  "upstream_scopes": [
    "SELECT T1.\"XCL_074\", T1.\"XCL_075\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1016"
  ]
}
```

### The value of column XCL_069 from the races table, associated with the race linked to the lap time record.

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_048\", T1.\"XCL_038\", T1.\"XCL_039\", T3.\"XCL_069\" FROM drivers AS T1 INNER JOIN lapTimes AS T2 ON T1.\"XCL_034\" = T2.\"XCL_044\" INNER JOIN races AS T3 ON T2.\"XCL_043\" = T3.\"XCL_065\" ORDER BY T2.\"XCL_048\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:894"
  ]
}
```

### "drivers"."XCL_041" = 'American'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_041\" = 'American'",
  "grain": [],
  "population_scope": "SELECT \"XCL_037\" FROM drivers WHERE \"XCL_041\" = 'American'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:964"
  ]
}
```

### COUNT("races"."XCL_065") > 0

```json
{
  "kind": "predicate",
  "formula": "COUNT(\"races\".\"XCL_065\") > 0",
  "grain": [
    "\"results\".\"XCL_075\""
  ],
  "population_scope": "SELECT T1.\"XCL_075\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Chinese Grand Prix' AND T2.\"XCL_066\" = 2008 AND NOT T1.\"XCL_084\" IS NULL GROUP BY T1.\"XCL_075\" HAVING COUNT(T2.\"XCL_065\") > 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:940"
  ]
}
```

### "drivers"."XCL_038" = 'Lewis' AND "drivers"."XCL_039" = 'Hamilton' AND "races"."XCL_066" = 2011 AND "races"."XCL_069" = 'Australian Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Lewis' AND \"drivers\".\"XCL_039\" = 'Hamilton' AND \"races\".\"XCL_066\" = 2011 AND \"races\".\"XCL_069\" = 'Australian Grand Prix'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_052\" FROM pitStops AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_050\" = T2.\"XCL_034\" INNER JOIN races AS T3 ON T1.\"XCL_049\" = T3.\"XCL_065\" WHERE T2.\"XCL_038\" = 'Lewis' AND T2.\"XCL_039\" = 'Hamilton' AND T3.\"XCL_066\" = 2011 AND T3.\"XCL_069\" = 'Australian Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1008"
  ]
}
```

### Circuit Identifier

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_002\" FROM circuits WHERE \"XCL_003\" = 'Marina Bay Street Circuit'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_002\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_002\" AS \"value\" FROM circuits AS \"r0\" WHERE \"r0\".\"XCL_003\" = 'Marina Bay Street Circuit'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:912"
  ]
}
```

### "qualifying"."XCL_057" = 345 AND "drivers"."XCL_038" = 'Lucas' AND "drivers"."XCL_039" = 'di Grassi'

```json
{
  "kind": "predicate",
  "formula": "\"qualifying\".\"XCL_057\" = 345 AND \"drivers\".\"XCL_038\" = 'Lucas' AND \"drivers\".\"XCL_039\" = 'di Grassi'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_062\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T2.\"XCL_034\" = T1.\"XCL_058\" WHERE T1.\"XCL_057\" = 345 AND T2.\"XCL_038\" = 'Lucas' AND T2.\"XCL_039\" = 'di Grassi'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:870"
  ]
}
```

### Fastest Lap Time String

```json
{
  "kind": "binding",
  "formula": "\"lapTimes\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_047\" FROM lapTimes ORDER BY (CASE WHEN INSTR(\"XCL_047\", ':') <> INSTR(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1), ':') + INSTR(\"XCL_047\", ':') THEN CAST(SUBSTRING(\"XCL_047\", 1, INSTR(\"XCL_047\", ':') - 1) AS REAL) * 3600 ELSE 0 END) + (CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') - 2 * (INSTR(\"XCL_047\", ':') = INSTR(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1), ':') + INSTR(\"XCL_047\", ':')), INSTR(\"XCL_047\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", ':') + 1, INSTR(\"XCL_047\", '.') - INSTR(\"XCL_047\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(\"XCL_047\", INSTR(\"XCL_047\", '.') + 1) AS REAL) / 1000) ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1006"
  ]
}
```

### Driver Name

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_037\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_034\", T2.\"XCL_037\" FROM results AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_075\" = T2.\"XCL_034\" WHERE STRFTIME('%Y', T2.\"XCL_040\") = '1971' AND NOT T1.\"XCL_088\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_037\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      },
      {
        "role": "r1",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_037\" AS \"value\" FROM results AS \"r0\" INNER JOIN drivers AS \"r1\" ON \"r0\".\"XCL_075\" = \"r1\".\"XCL_034\" WHERE STRFTIME('%Y', \"r1\".\"XCL_040\") = '1971' AND NOT \"r0\".\"XCL_088\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:972"
  ]
}
```

### Last Driver Incremental Time

```json
{
  "kind": "binding",
  "formula": "\"time_seconds\"",
  "grain": [],
  "population_scope": "SELECT \"time_seconds\" FROM last_driver_incremental",
  "upstream_scopes": [
    "SELECT \"time_seconds\" FROM time_in_seconds WHERE \"XCL_081\" = (SELECT MAX(\"XCL_081\") FROM time_in_seconds)",
    "SELECT T1.\"XCL_081\", CASE WHEN T1.\"XCL_081\" = 1 THEN (CAST(SUBSTRING(T1.\"XCL_084\", 1, 1) AS REAL) * 3600) + (CAST(SUBSTRING(T1.\"XCL_084\", 3, 2) AS REAL) * 60) + CAST(SUBSTRING(T1.\"XCL_084\", 6) AS REAL) ELSE CAST(SUBSTRING(T1.\"XCL_084\", 2) AS REAL) END AS time_seconds FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" WHERE T2.\"XCL_069\" = 'Australian Grand Prix' AND NOT T1.\"XCL_084\" IS NULL AND T2.\"XCL_066\" = 2008"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:944"
  ]
}
```

### Driver Attribute XCL_041

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_041\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_035\", T2.\"XCL_041\", T2.\"XCL_040\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_058\" = T2.\"XCL_034\" WHERE T1.\"XCL_057\" = 23 AND NOT T1.\"XCL_063\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_041\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "qualifying"
      },
      {
        "role": "r1",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_041\" AS \"value\" FROM qualifying AS \"r0\" INNER JOIN drivers AS \"r1\" ON \"r0\".\"XCL_058\" = \"r1\".\"XCL_034\" WHERE \"r0\".\"XCL_057\" = 23 AND NOT \"r0\".\"XCL_063\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:980"
  ]
}
```

### "drivers"."XCL_038" = 'Michael' AND "drivers"."XCL_039" = 'Schumacher'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_038\" = 'Michael' AND \"drivers\".\"XCL_039\" = 'Schumacher'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_069\", T1.\"XCL_066\" FROM races AS T1 INNER JOIN lapTimes AS T2 ON T2.\"XCL_043\" = T1.\"XCL_065\" INNER JOIN drivers AS T3 ON T3.\"XCL_034\" = T2.\"XCL_044\" WHERE T3.\"XCL_038\" = 'Michael' AND T3.\"XCL_039\" = 'Schumacher' ORDER BY T2.\"XCL_048\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:904"
  ]
}
```

### Driver Identifier

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_034\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_034\" FROM pitStops AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_050\" = T2.\"XCL_034\" WHERE T2.\"XCL_041\" = 'German' AND STRFTIME('%Y', T2.\"XCL_040\") BETWEEN '1980' AND '1990' ORDER BY T1.\"XCL_053\" LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:970"
  ]
}
```

### "circuits"."XCL_005" = 'USA' AND "races"."XCL_066" = 2006

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_005\" = 'USA' AND \"races\".\"XCL_066\" = 2006",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\", T1.\"XCL_004\", T2.\"XCL_069\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T1.\"XCL_005\" = 'USA' AND T2.\"XCL_066\" = 2006",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:900"
  ]
}
```

### "drivers"."XCL_041" = 'Spanish' AND STRFTIME('%Y', "drivers"."XCL_040") < '1982'

```json
{
  "kind": "predicate",
  "formula": "\"drivers\".\"XCL_041\" = 'Spanish' AND STRFTIME('%Y', \"drivers\".\"XCL_040\") < '1982'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_034\" FROM pitStops AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_050\" = T2.\"XCL_034\" WHERE T2.\"XCL_041\" = 'Spanish' AND STRFTIME('%Y', T2.\"XCL_040\") < '1982' ORDER BY T1.\"XCL_053\" DESC LIMIT 10",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:973"
  ]
}
```

### Pit Stop Identifier

```json
{
  "kind": "binding",
  "formula": "\"pitStops\".\"XCL_054\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_054\" FROM pitStops AS T1 INNER JOIN races AS T2 ON T1.\"XCL_049\" = T2.\"XCL_065\" WHERE T2.\"XCL_066\" = 2011 AND T2.\"XCL_069\" = 'Australian Grand Prix'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_054\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "pitStops"
      },
      {
        "role": "r1",
        "physical_table": "races"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_054\" AS \"value\" FROM pitStops AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_049\" = \"r1\".\"XCL_065\" WHERE \"r1\".\"XCL_066\" = 2011 AND \"r1\".\"XCL_069\" = 'Australian Grand Prix'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1009"
  ]
}
```

### NOT "results"."XCL_085" IS NULL

```json
{
  "kind": "predicate",
  "formula": "NOT \"results\".\"XCL_085\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_069\", T1.\"XCL_066\" FROM races AS T1 INNER JOIN results AS T2 ON T1.\"XCL_065\" = T2.\"XCL_074\" WHERE NOT T2.\"XCL_085\" IS NULL ORDER BY T2.\"XCL_085\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:961"
  ]
}
```

### Driver Identifier XCL_038

```json
{
  "kind": "binding",
  "formula": "\"drivers\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_038\", T1.\"XCL_039\" FROM drivers AS T1 INNER JOIN results AS T2 ON T2.\"XCL_075\" = T1.\"XCL_034\" WHERE NOT T2.\"XCL_088\" IS NULL ORDER BY T2.\"XCL_089\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:927"
  ]
}
```

### "driverStandings"."XCL_028" = 18

```json
{
  "kind": "predicate",
  "formula": "\"driverStandings\".\"XCL_028\" = 18",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_029\") FROM driverStandings WHERE \"XCL_028\" = 18",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:966"
  ]
}
```

### "races"."XCL_069" = 'Austrian Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'Austrian Grand Prix'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_074\", T1.\"XCL_075\" FROM results AS T1 INNER JOIN races AS T2 ON T1.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" INNER JOIN (SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix') AS T4 ON (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) = T4.\"min_time_in_seconds\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix'",
  "upstream_scopes": [
    "SELECT MIN(fastest_lap_times.\"time_in_seconds\") AS min_time_in_seconds FROM fastest_lap_times INNER JOIN races AS T2 ON fastest_lap_times.\"XCL_074\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T2.\"XCL_069\" = 'Austrian Grand Prix'",
    "SELECT T1.\"XCL_074\", T1.\"XCL_075\", T1.\"XCL_088\", (CAST(SUBSTRING(T1.\"XCL_088\", 1, INSTR(T1.\"XCL_088\", ':') - 1) AS REAL) * 60) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", ':') + 1, INSTR(T1.\"XCL_088\", '.') - INSTR(T1.\"XCL_088\", ':') - 1) AS REAL)) + (CAST(SUBSTRING(T1.\"XCL_088\", INSTR(T1.\"XCL_088\", '.') + 1) AS REAL) / 1000) AS time_in_seconds FROM results AS T1 WHERE NOT T1.\"XCL_088\" IS NULL"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1016"
  ]
}
```

### Circuit Attribute XCL_006

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_005\", \"XCL_006\", \"XCL_007\" FROM circuits WHERE \"XCL_003\" = 'Hungaroring'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "circuits"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_006\" AS \"value\" FROM circuits AS \"r0\" WHERE \"r0\".\"XCL_003\" = 'Hungaroring'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:993"
  ]
}
```

### Aggregates the number of rows where the column XCL_084 is not null, within the filtered population defined by the program.

```json
{
  "kind": "metric",
  "formula": "SUM(IIF(NOT \"results\".\"XCL_084\" IS NULL, 1, 0))",
  "grain": [],
  "population_scope": "SELECT SUM(IIF(NOT \"XCL_084\" IS NULL, 1, 0)) FROM results WHERE \"XCL_090\" = 2 AND \"XCL_074\" < 100 AND \"XCL_074\" > 50",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(IIF(NOT \"r0\".\"XCL_084\" IS NULL, 1, 0))",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "results"
      }
    ],
    "scope_sql": "SELECT SUM(IIF(NOT \"r0\".\"XCL_084\" IS NULL, 1, 0)) AS \"value\" FROM results AS \"r0\" WHERE \"r0\".\"XCL_090\" = 2 AND \"r0\".\"XCL_074\" < 100 AND \"r0\".\"XCL_074\" > 50",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:977"
  ]
}
```

### "circuits"."XCL_003" = 'Marina Bay Street Circuit'

```json
{
  "kind": "predicate",
  "formula": "\"circuits\".\"XCL_003\" = 'Marina Bay Street Circuit'",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM circuits WHERE \"XCL_003\" = 'Marina Bay Street Circuit'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1001"
  ]
}
```

### Circuit Name

```json
{
  "kind": "binding",
  "formula": "\"circuits\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_006\", T3.\"XCL_007\" FROM lapTimes AS T1 INNER JOIN races AS T2 ON T1.\"XCL_043\" = T2.\"XCL_065\" INNER JOIN circuits AS T3 ON T2.\"XCL_068\" = T3.\"XCL_001\" WHERE T1.\"XCL_047\" = '1:29.488'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_007\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "lapTimes"
      },
      {
        "role": "r1",
        "physical_table": "races"
      },
      {
        "role": "r2",
        "physical_table": "circuits"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_007\" AS \"value\" FROM lapTimes AS \"r0\" INNER JOIN races AS \"r1\" ON \"r0\".\"XCL_043\" = \"r1\".\"XCL_065\" INNER JOIN circuits AS \"r2\" ON \"r1\".\"XCL_068\" = \"r2\".\"XCL_001\" WHERE \"r0\".\"XCL_047\" = '1:29.488'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1017"
  ]
}
```

### "races"."XCL_069" = 'European Grand Prix'

```json
{
  "kind": "predicate",
  "formula": "\"races\".\"XCL_069\" = 'European Grand Prix'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_005\", T1.\"XCL_004\" FROM circuits AS T1 INNER JOIN races AS T2 ON T2.\"XCL_068\" = T1.\"XCL_001\" WHERE T2.\"XCL_069\" = 'European Grand Prix' ORDER BY T2.\"XCL_066\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:888"
  ]
}
```

### Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_069\" FROM races AS T1 INNER JOIN results AS T2 ON T1.\"XCL_065\" = T2.\"XCL_074\" WHERE NOT T2.\"XCL_088\" IS NULL ORDER BY T2.\"XCL_088\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:999"
  ]
}
```

### Race Name or Title

```json
{
  "kind": "binding",
  "formula": "\"races\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_066\", T3.\"XCL_069\", T3.\"XCL_070\", T3.\"XCL_071\" FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T1.\"XCL_058\" = T2.\"XCL_034\" INNER JOIN races AS T3 ON T1.\"XCL_057\" = T3.\"XCL_065\" WHERE T1.\"XCL_058\" = (SELECT \"XCL_034\" FROM drivers ORDER BY \"XCL_040\" DESC LIMIT 1) ORDER BY T3.\"XCL_070\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:981"
  ]
}
```

### A scalar metric computed over the entire `drivers` table. It calculates the difference between the total count of non-null values in column `XCL_034` 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"drivers\".\"XCL_034\") - COUNT(CASE WHEN NOT \"drivers\".\"XCL_037\" IS NULL THEN \"drivers\".\"XCL_037\" END)",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_034\") - COUNT(CASE WHEN NOT \"XCL_037\" IS NULL THEN \"XCL_037\" END) FROM drivers",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_034\") - COUNT(CASE WHEN NOT \"r0\".\"XCL_037\" IS NULL THEN \"r0\".\"XCL_037\" END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "drivers"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_034\") - COUNT(CASE WHEN NOT \"r0\".\"XCL_037\" IS NULL THEN \"r0\".\"XCL_037\" END) AS \"value\" FROM drivers AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:914"
  ]
}
```


## 增量维护事件

- Recorded alias revision · races.XCL_069 · Archived superseded_alias_hypotheses → archived aliases
  - races.XCL_069: name → race_name
- Recorded alias revision · constructorStandings.XCL_016 · Archived superseded_alias_hypotheses → archived aliases
  - constructorStandings.XCL_016: constructor_standings_id → standings_id
- Recorded alias revision · results.XCL_087 · Archived superseded_alias_hypotheses → archived aliases
  - results.XCL_087: rank → fastest_lap_rank
