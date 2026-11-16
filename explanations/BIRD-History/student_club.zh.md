# BIRD-History / student_club — Schema 与业务口径解释

该数据库的存档目录包含 8 张表、46 个物理列、16 条关系，以及 158 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## attendance

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, T3, T4, a, a2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| attendance.XCL_001 | event_id | unknown | bird_dev:1321, bird_dev:1396, bird_dev:1322, bird_dev:1371, bird_dev:1316, bird_dev:1315, bird_dev:1436, bird_dev:1324 |
| attendance.XCL_002 | member_id | unknown | bird_dev:1321, bird_dev:1396, bird_dev:1371, bird_dev:1316, bird_dev:1436, bird_dev:1381, bird_dev:1320, bird_dev:1395 |

## budget

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: B, T1, T2, T2b, T3, T3_sub, T3b, T4, T6, b, b2, b3

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| budget.XCL_003 | budget_id | unknown | bird_dev:1386, bird_dev:1442, bird_dev:1455, bird_dev:1365, bird_dev:1448, bird_dev:1451, bird_dev:1404, bird_dev:1401 |
| budget.XCL_004 | budget_category | unknown | bird_dev:1380, bird_dev:1343, bird_dev:1467, bird_dev:1397, bird_dev:1427, bird_dev:1463, bird_dev:1359, bird_dev:1332 |
| budget.XCL_005 | spent_amount | unknown | bird_dev:1378, bird_dev:1380, bird_dev:1467, bird_dev:1397, bird_dev:1427, bird_dev:1340, bird_dev:1332, bird_dev:1376 |
| budget.XCL_006 | remaining_budget | unknown | bird_dev:1442, bird_dev:1343, bird_dev:1365, bird_dev:1447, bird_dev:1348, bird_dev:1403, bird_dev:1417 |
| budget.XCL_007 | total_budget | unknown | bird_dev:1337, bird_dev:1343, bird_dev:1349, bird_dev:1369, bird_dev:1359, bird_dev:1405, bird_dev:1407, bird_dev:1462 |
| budget.XCL_008 | status | unknown | bird_dev:1397, bird_dev:1350, bird_dev:1403 |
| budget.XCL_009 | event_id | unknown | bird_dev:1386, bird_dev:1337, bird_dev:1467, bird_dev:1349, bird_dev:1369, bird_dev:1448, bird_dev:1427, bird_dev:1451 |

## event

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: EV, T0, T1, T1b, T2, T3, T4, T4_sub, T5, T5b, T7, e, e2, e3, ev, ev2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| event.XCL_010 | event_id | unknown | bird_dev:1321, bird_dev:1386, bird_dev:1337, bird_dev:1467, bird_dev:1322, bird_dev:1349, bird_dev:1371, bird_dev:1369 |
| event.XCL_011 | event_name | unknown | bird_dev:1435, bird_dev:1386, bird_dev:1337, bird_dev:1467, bird_dev:1322, bird_dev:1349, bird_dev:1371, bird_dev:1369 |
| event.XCL_012 | event_datetime | unknown | bird_dev:1321, bird_dev:1400, bird_dev:1435, bird_dev:1448, bird_dev:1340, bird_dev:1324, bird_dev:1395, bird_dev:1443 |
| event.XCL_013 | event_type | unknown | bird_dev:1400, bird_dev:1435, bird_dev:1322, bird_dev:1427, bird_dev:1404, bird_dev:1324, bird_dev:1359, bird_dev:1379 |
| event.XCL_015 | location | unknown | bird_dev:1427, bird_dev:1341, bird_dev:1447, bird_dev:1443, bird_dev:1422, bird_dev:1418, bird_dev:1429 |
| event.XCL_016 | status | unknown | bird_dev:1435, bird_dev:1443, bird_dev:1376 |

## expense

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: E, T1, T2, T2_sub, T2b, T3, T3b, T4, T5, T6, e, e2, e3, ex, ex2, ex3, x

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| expense.XCL_017 | expense_id | unknown | bird_dev:1370 |
| expense.XCL_018 | description | unknown | bird_dev:1455, bird_dev:1408, bird_dev:1444, bird_dev:1370, bird_dev:1365, bird_dev:1448, bird_dev:1342, bird_dev:1460 |
| expense.XCL_019 | date | unknown | bird_dev:1440, bird_dev:1409, bird_dev:1342, bird_dev:1350, bird_dev:1430, bird_dev:1339, bird_dev:1437 |
| expense.XCL_020 | amount | unknown | bird_dev:1386, bird_dev:1455, bird_dev:1440, bird_dev:1408, bird_dev:1444, bird_dev:1452, bird_dev:1449, bird_dev:1448 |
| expense.XCL_021 | approved | unknown | bird_dev:1437, bird_dev:1338 |
| expense.XCL_022 | member_id | unknown | bird_dev:1440, bird_dev:1452, bird_dev:1370, bird_dev:1449, bird_dev:1413, bird_dev:1451, bird_dev:1460, bird_dev:1436 |
| expense.XCL_023 | budget_id | unknown | bird_dev:1386, bird_dev:1455, bird_dev:1365, bird_dev:1448, bird_dev:1451, bird_dev:1404, bird_dev:1401, bird_dev:1453 |

## income

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, T3, T4, i, i2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| income.XCL_024 | income_id | unknown | bird_dev:1423, bird_dev:1432 |
| income.XCL_025 | date | unknown | bird_dev:1357, bird_dev:1392, bird_dev:1464, bird_dev:1344, bird_dev:1358, bird_dev:1372 |
| income.XCL_026 | amount | unknown | bird_dev:1388, bird_dev:1385, bird_dev:1384, bird_dev:1423, bird_dev:1464, bird_dev:1450, bird_dev:1331, bird_dev:1432 |
| income.XCL_027 | type | unknown | bird_dev:1388, bird_dev:1357, bird_dev:1392, bird_dev:1344, bird_dev:1358 |
| income.XCL_028 | notes | unknown | bird_dev:1344 |
| income.XCL_029 | member_id | unknown | bird_dev:1388, bird_dev:1357, bird_dev:1385, bird_dev:1384, bird_dev:1464, bird_dev:1450, bird_dev:1331, bird_dev:1432 |

## major

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, T3, T4, T5, ma, maj, mj

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| major.XCL_030 | major_id | unknown | bird_dev:1459, bird_dev:1394, bird_dev:1396, bird_dev:1439, bird_dev:1368, bird_dev:1428, bird_dev:1415, bird_dev:1425 |
| major.XCL_031 | major_name | unknown | bird_dev:1459, bird_dev:1394, bird_dev:1396, bird_dev:1439, bird_dev:1368, bird_dev:1415, bird_dev:1449, bird_dev:1391 |
| major.XCL_032 | department_name | unknown | bird_dev:1459, bird_dev:1363, bird_dev:1425, bird_dev:1356, bird_dev:1336, bird_dev:1426, bird_dev:1314, bird_dev:1375 |
| major.XCL_033 | college_name | unknown | bird_dev:1363, bird_dev:1439, bird_dev:1425, bird_dev:1330, bird_dev:1313, bird_dev:1438, bird_dev:1319, bird_dev:1426 |

## member

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, T3, T4, T5, m, m2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| member.XCL_034 | member_id | unknown | bird_dev:1321, bird_dev:1394, bird_dev:1396, bird_dev:1440, bird_dev:1388, bird_dev:1357, bird_dev:1452, bird_dev:1370 |
| member.XCL_035 | first_name | unknown | bird_dev:1321, bird_dev:1459, bird_dev:1329, bird_dev:1393, bird_dev:1396, bird_dev:1388, bird_dev:1357, bird_dev:1449 |
| member.XCL_036 | last_name | unknown | bird_dev:1321, bird_dev:1459, bird_dev:1329, bird_dev:1393, bird_dev:1396, bird_dev:1388, bird_dev:1357, bird_dev:1449 |
| member.XCL_037 | email | unknown | bird_dev:1393, bird_dev:1440 |
| member.XCL_038 | position | unknown | bird_dev:1393, bird_dev:1415, bird_dev:1452, bird_dev:1370, bird_dev:1356, bird_dev:1319, bird_dev:1377, bird_dev:1420 |
| member.XCL_039 | shirt_size | unknown | bird_dev:1402, bird_dev:1445, bird_dev:1416, bird_dev:1317, bird_dev:1412, bird_dev:1424, bird_dev:1352, bird_dev:1432 |
| member.XCL_040 | phone_number | unknown | bird_dev:1439, bird_dev:1368, bird_dev:1316, bird_dev:1461, bird_dev:1346, bird_dev:1374, bird_dev:1457 |
| member.XCL_041 | zip_code | unknown | bird_dev:1329, bird_dev:1428, bird_dev:1413, bird_dev:1468, bird_dev:1347, bird_dev:1333, bird_dev:1355, bird_dev:1450 |
| member.XCL_042 | major_id | unknown | bird_dev:1459, bird_dev:1394, bird_dev:1396, bird_dev:1439, bird_dev:1368, bird_dev:1428, bird_dev:1415, bird_dev:1356 |

## zip_code

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, T3, T4, T5, z

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| zip_code.XCL_043 | zip_code | unknown | bird_dev:1329, bird_dev:1428, bird_dev:1468, bird_dev:1434, bird_dev:1347, bird_dev:1446, bird_dev:1333, bird_dev:1355 |
| zip_code.XCL_044 | zip_type | unknown | bird_dev:1434, bird_dev:1446, bird_dev:1433, bird_dev:1353 |
| zip_code.XCL_045 | city | unknown | bird_dev:1362, bird_dev:1468, bird_dev:1333, bird_dev:1450, bird_dev:1383, bird_dev:1364, bird_dev:1469 |
| zip_code.XCL_046 | county | unknown | bird_dev:1329, bird_dev:1362, bird_dev:1434, bird_dev:1347, bird_dev:1450, bird_dev:1364, bird_dev:1433 |
| zip_code.XCL_047 | state | unknown | bird_dev:1362, bird_dev:1434, bird_dev:1333, bird_dev:1355, bird_dev:1383, bird_dev:1364, bird_dev:1373, bird_dev:1458 |

## 表关系与连接依据

- attendance.XCL_001 ↔ event.XCL_010; target_disjoint_historical_join
- attendance.XCL_002 ↔ member.XCL_034; target_disjoint_historical_join
- budget.XCL_003 ↔ expense.XCL_023; target_disjoint_historical_join
- budget.XCL_009 ↔ event.XCL_010; target_disjoint_historical_join
- expense.XCL_022 ↔ member.XCL_034; target_disjoint_historical_join
- income.XCL_029 ↔ member.XCL_034; target_disjoint_historical_join
- major.XCL_030 ↔ member.XCL_042; target_disjoint_historical_join
- member.XCL_041 ↔ zip_code.XCL_043; target_disjoint_historical_join
- attendance.XCL_001 ↔ event.XCL_010; sql_workload_observed_join
- attendance.XCL_002 ↔ member.XCL_034; sql_workload_observed_join
- budget.XCL_003 ↔ expense.XCL_023; sql_workload_observed_join
- budget.XCL_009 ↔ event.XCL_010; sql_workload_observed_join
- expense.XCL_022 ↔ member.XCL_034; sql_workload_observed_join
- income.XCL_029 ↔ member.XCL_034; sql_workload_observed_join
- major.XCL_030 ↔ member.XCL_042; sql_workload_observed_join
- member.XCL_041 ↔ zip_code.XCL_043; sql_workload_observed_join

## 业务口径、总体与粒度

### A query that joins the major and member tables on XCL_030 = XCL_042 to retrieve major details (XCL_031) for the specific member identified by first na

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_031\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" WHERE T2.\"XCL_035\" = 'Phillip' AND T2.\"XCL_036\" = 'Cullen'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1414"
  ]
}
```

### A query that retrieves event identifiers by joining attendance, event, and member tables. It filters for events where the event type is 'Social', the 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_011\" FROM attendance AS T1 INNER JOIN event AS T2 ON T2.\"XCL_010\" = T1.\"XCL_001\" INNER JOIN member AS T3 ON T1.\"XCL_002\" = T3.\"XCL_034\" WHERE T3.\"XCL_038\" = 'Vice President' AND T2.\"XCL_015\" = '900 E. Washington St.' AND T2.\"XCL_013\" = 'Social'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1429"
  ]
}
```

### A point-lookup query that retrieves a specific field (XCL_040) from the member table based on exact matches for two other fields (XCL_035 and XCL_036)

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_040\" FROM member WHERE \"XCL_035\" = 'Carlo' AND \"XCL_036\" = 'Jacobs'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1346"
  ]
}
```

### Major Count by College Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_031\") FROM major WHERE \"XCL_033\" = 'College of Humanities and Social Sciences'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1345"
  ]
}
```

### Event Budget Lookup Program

```json
{
  "kind": "program",
  "formula": "SELECT SUM(T2.\"XCL_007\") FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_011\" = 'October Speaker'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1337"
  ]
}
```

### Executes an inner join between major (T1) and member (T2) on XCL_030 = XCL_042, filters for major type 'Business' and member attribute 'Medium', and r

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_034\") FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" WHERE T1.\"XCL_031\" = 'Business' AND T2.\"XCL_039\" = 'Medium'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1416"
  ]
}
```

### Budget Details for January Speaker

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_004\", T2.\"XCL_007\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_011\" = 'January Speaker'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1462"
  ]
}
```

### Member Major Lookup

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_031\", T2.\"XCL_032\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T1.\"XCL_035\" = 'Garrett' AND T1.\"XCL_036\" = 'Gerke'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1459"
  ]
}
```

### Full SQL program that joins the 'major' table (T1) with the 'member' table (T2) on T1.XCL_030 = T2.XCL_042, filters for T1.XCL_031 = 'Physics Teaching

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_034\") FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" WHERE T1.\"XCL_031\" = 'Physics Teaching'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1394"
  ]
}
```

### Full SQL program that joins event, attendance, and member tables to calculate the count of events. It filters for the year 2019 using a substring chec

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_010\") FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" INNER JOIN member AS T3 ON T2.\"XCL_002\" = T3.\"XCL_034\" WHERE T3.\"XCL_035\" = 'Sacha' AND T3.\"XCL_036\" = 'Harrison' AND SUBSTRING(T1.\"XCL_012\", 1, 4) = '2019'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1321"
  ]
}
```

### Environmental Engineering Member Details

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_036\", T1.\"XCL_032\", T1.\"XCL_033\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" WHERE T2.\"XCL_038\" = 'Member' AND T1.\"XCL_031\" = 'Environmental Engineering'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1426"
  ]
}
```

### A query that joins the member table (T1) with the major table (T2) on the condition that T2.XCL_030 equals T1.XCL_042. It filters for records where th

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_040\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T2.\"XCL_031\" = 'Business' AND T2.\"XCL_033\" = 'College of Agriculture and Applied Sciences'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1439"
  ]
}
```

### Full SQL program that joins the member and income tables on XCL_034 and XCL_029, filters for the member with first name 'Grant' and last name 'Gilmour

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_026\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_035\" = 'Grant' AND T1.\"XCL_036\" = 'Gilmour'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1384"
  ]
}
```

### Expense Sum Query

```json
{
  "kind": "program",
  "formula": "SELECT SUM(\"XCL_020\") FROM expense WHERE \"XCL_018\" = 'Pizza'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1361"
  ]
}
```

### High-Expense Attendance Query

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T3.\"XCL_001\" FROM expense AS T1 INNER JOIN member AS T2 ON T1.\"XCL_022\" = T2.\"XCL_034\" INNER JOIN attendance AS T3 ON T2.\"XCL_034\" = T3.\"XCL_002\" WHERE T1.\"XCL_020\" > 50",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1436"
  ]
}
```

### Full SQL program that joins expense and budget tables on expense.XCL_023 = budget.XCL_003, filters for expense.XCL_018 = 'Posters', and returns distin

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_004\" FROM expense AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_023\" = T2.\"XCL_003\" WHERE T1.\"XCL_018\" = 'Posters'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1465"
  ]
}
```

### Retrieves columns XCL_035, XCL_036, and XCL_037 from the member table, filtered to rows where XCL_038 equals 'Secretary'.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_035\", \"XCL_036\", \"XCL_037\" FROM member WHERE \"XCL_038\" = 'Secretary'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1393"
  ]
}
```

### Full SQL program that joins the member table (T1) with the income table (T2) on XCL_034 = XCL_029. It filters members where XCL_038 is 'Member' and XC

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_026\" = 50 THEN 1.0 ELSE 0 END) AS REAL) * 100 / COUNT(T2.\"XCL_024\") FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_038\" = 'Member' AND T1.\"XCL_039\" = 'Medium'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1432"
  ]
}
```

### Executes a query to retrieve the top 3 entries from the "budget" table filtered by "XCL_004" = 'Advertisement', ordered by "XCL_007" descending, retur

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_003\" FROM budget WHERE \"XCL_004\" = 'Advertisement' ORDER BY \"XCL_007\" DESC LIMIT 3",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1407"
  ]
}
```

### A query that joins event, budget, and expense tables to retrieve expense identifiers (XCL_020) for the 'September Speaker' event where the expense cat

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_020\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" WHERE T1.\"XCL_011\" = 'September Speaker' AND T3.\"XCL_018\" = 'Posters'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1401"
  ]
}
```

### Full SQL program that joins the zip_code table (T1) with the member table (T2) on the zip code identifier (XCL_043 = XCL_041), filters for the state '

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_034\") FROM zip_code AS T1 INNER JOIN member AS T2 ON T1.\"XCL_043\" = T2.\"XCL_041\" WHERE T1.\"XCL_047\" = 'Maryland'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1373"
  ]
}
```

### Georgetown SC Member Lookup

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T2.\"XCL_045\" = 'Georgetown' AND T2.\"XCL_047\" = 'South Carolina'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1383"
  ]
}
```

### A SQL program that retrieves income records for a specific member. It joins the 'member' table (T1) with the 'income' table (T2) on member ID ('XCL_03

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_025\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_035\" = 'Connor' AND T1.\"XCL_036\" = 'Hilton' AND T2.\"XCL_027\" = 'Dues'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1357"
  ]
}
```

### A query that retrieves XCL_015 from the event table for all records where XCL_011 is 'Spring Budget Review'. No aggregation is applied; grain is indiv

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_015\" FROM event WHERE \"XCL_011\" = 'Spring Budget Review'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1341"
  ]
}
```

### Full SQL program that counts records in the member table satisfying the conditions XCL_038 = 'Member' and XCL_039 = 'X-Large'.

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_034\") FROM member WHERE \"XCL_038\" = 'Member' AND \"XCL_039\" = 'X-Large'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1424"
  ]
}
```

### College of Engineering Member Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_034\") FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T2.\"XCL_033\" = 'College of Engineering'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1313"
  ]
}
```

### A query that retrieves the zip code for a member by joining the member and zip_code tables. It filters for a specific member using first name and last

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_046\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_035\" = 'Sherri' AND T1.\"XCL_036\" = 'Ramsey'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1329"
  ]
}
```

### Full SQL program that joins the 'member' table (T1) with the 'major' table (T2) on the major identifier (XCL_030 = XCL_042). It filters for members wh

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_031\" = 'Business' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_034\") FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T1.\"XCL_038\" = 'Member'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1421"
  ]
}
```

### Full query joining member, attendance, and event tables to retrieve specific member columns (XCL_035, XCL_036) where the associated event name (XCL_01

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_034\" = T2.\"XCL_002\" INNER JOIN event AS T3 ON T2.\"XCL_001\" = T3.\"XCL_010\" WHERE T3.\"XCL_011\" = 'Laugh Out Loud'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1327"
  ]
}
```

### Count of Medium Business Members

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_034\") FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T2.\"XCL_031\" = 'Business' AND T1.\"XCL_039\" = 'Medium'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1352"
  ]
}
```

### Full program that joins member and major tables on XCL_042 = XCL_030, filters for major XCL_032 equal to 'School of Applied Sciences, Technology and E

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T2.\"XCL_032\" = 'School of Applied Sciences, Technology and Education'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1375"
  ]
}
```

### Computes the set of event identifiers (XCL_011) that have more than 10 associated attendance records but are not of type 'Meeting'. It achieves this b

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_011\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" GROUP BY T1.\"XCL_010\" HAVING COUNT(T2.\"XCL_001\") > 10 EXCEPT SELECT T1.\"XCL_011\" FROM event AS T1 WHERE T1.\"XCL_013\" = 'Meeting'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1322"
  ]
}
```

### A query that joins the member and income tables on the member identifier (XCL_034 = XCL_029) to retrieve the income attribute XCL_025 for a specific m

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_025\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_035\" = 'Casey' AND T1.\"XCL_036\" = 'Mason'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1372"
  ]
}
```

### Full SQL program that retrieves XCL_006 from the budget table for the 'Food' category (XCL_004 = 'Food') where XCL_007 is at its maximum value for tha

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_006\" FROM budget WHERE \"XCL_004\" = 'Food' AND \"XCL_007\" = (SELECT MAX(\"XCL_007\") FROM budget WHERE \"XCL_004\" = 'Food')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1343"
  ]
}
```

### Parking Expense Query

```json
{
  "kind": "program",
  "formula": "SELECT SUM(\"XCL_020\") FROM expense WHERE \"XCL_018\" = 'Parking'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1408"
  ]
}
```

### A program that identifies distinct member profiles (XCL_035, XCL_036, XCL_040) linked to expenses where the expense amount (XCL_020) is strictly great

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T3.\"XCL_035\", T3.\"XCL_036\", T3.\"XCL_040\" FROM expense AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_023\" = T2.\"XCL_003\" INNER JOIN member AS T3 ON T3.\"XCL_034\" = T1.\"XCL_022\" WHERE T1.\"XCL_020\" > (SELECT AVG(T1.\"XCL_020\") FROM expense AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_023\" = T2.\"XCL_003\" INNER JOIN member AS T3 ON T3.\"XCL_034\" = T1.\"XCL_022\")",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1457"
  ]
}
```

### A query that joins event, budget, and expense tables to calculate the total expense (XCL_020) for each event (XCL_013) where the event name (XCL_011) 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_013\", SUM(T3.\"XCL_020\") FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" WHERE T1.\"XCL_011\" = 'October Meeting'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1404"
  ]
}
```

### A query that joins the member and major tables to retrieve the major attribute (XCL_031) for a specific member filtered by first name 'Brent' and last

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_031\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_035\" = 'Brent' AND T1.\"XCL_036\" = 'Thomason'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1351"
  ]
}
```

### A query that retrieves the major identifiers for all members filtered by the condition that their role or title (XCL_038) is 'President', joined via t

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_032\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_038\" = 'President'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1356"
  ]
}
```

### A full SQL program that retrieves budget amounts (XCL_005) by joining the event and budget tables. It filters for events named 'September Meeting' wit

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_005\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_011\" = 'September Meeting' AND T2.\"XCL_004\" = 'Food' AND SUBSTRING(T1.\"XCL_012\", 6, 2) = '09'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1332"
  ]
}
```

### 2020 Meeting Attendance Average Query

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(T2.\"XCL_001\") AS REAL) / COUNT(DISTINCT T2.\"XCL_001\") FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" WHERE SUBSTRING(T1.\"XCL_012\", 1, 4) = '2020' AND T1.\"XCL_013\" = 'Meeting'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1324"
  ]
}
```

### Event Budget Expense Join

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN T1.\"XCL_011\" = 'Yearly Kickoff' THEN T3.\"XCL_020\" ELSE 0 END) AS REAL) * 100 / SUM(T3.\"XCL_020\") FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1390"
  ]
}
```

### Retrieves the expense amount (XCL_020) from the 'expense' table where the category (XCL_018) is 'Posters' and the date (XCL_019) is '2019-09-04'.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_020\" FROM expense WHERE \"XCL_018\" = 'Posters' AND \"XCL_019\" = '2019-09-04'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1342"
  ]
}
```

### Filtered Member-Expense Join

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_036\", T1.\"XCL_038\" FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T2.\"XCL_019\" = '2019-09-10' AND T2.\"XCL_018\" = 'Pizza'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1430"
  ]
}
```

### A program that identifies the most common value for the 'XCL_039' column in the 'member' table. It groups members by 'XCL_039', counts occurrences, so

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_039\" FROM member GROUP BY \"XCL_039\" ORDER BY COUNT(\"XCL_039\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1402"
  ]
}
```

### Get Top Expense by XCL_020

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_018\" FROM expense ORDER BY \"XCL_020\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1325"
  ]
}
```

### Budget negative XCL_006 ratio query

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN \"XCL_006\" < 0 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"XCL_003\") FROM budget",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1442"
  ]
}
```

### Event Attendance Income Lookup

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T3.\"XCL_035\", T3.\"XCL_036\", T4.\"XCL_026\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" INNER JOIN member AS T3 ON T3.\"XCL_034\" = T2.\"XCL_002\" INNER JOIN income AS T4 ON T4.\"XCL_029\" = T3.\"XCL_034\" WHERE T4.\"XCL_025\" = '2019-09-09'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1464"
  ]
}
```

### A query that joins event, budget, and expense tables to retrieve the event attribute XCL_011 corresponding to the expense record with the lowest value

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_011\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" ORDER BY T3.\"XCL_020\" LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1389"
  ]
}
```

### Full SQL program that selects the count of 'XCL_034' from the 'member' table with a filter on 'XCL_038' = 'President'. This program encapsulates the s

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_034\") FROM member WHERE \"XCL_038\" = 'President'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1377"
  ]
}
```

### A query that joins the member and major tables on XCL_042 = XCL_030, filters for members where XCL_038 is 'vice president', and returns the correspond

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_033\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_038\" LIKE 'vice president'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1319"
  ]
}
```

### Event Extract Q4 2019 to Q1 2020

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_010\", \"XCL_015\", \"XCL_016\" FROM event WHERE DATE(SUBSTRING(\"XCL_012\", 1, 10)) BETWEEN '2019-11-01' AND '2020-03-31'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1443"
  ]
}
```

### Member Zip Code Lookup

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_045\", T2.\"XCL_046\", T2.\"XCL_047\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_035\" = 'Amy' AND T1.\"XCL_036\" = 'Firth'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1364"
  ]
}
```

### A query that retrieves the income amount ("XCL_028") from the income table, filtered to records where the category ("XCL_027") is 'Fundraising' and th

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_028\" FROM income WHERE \"XCL_027\" = 'Fundraising' AND \"XCL_025\" = '2019-09-14'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1344"
  ]
}
```

### Filtered Event-Budget-Expense Join

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_011\", T1.\"XCL_012\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" WHERE T3.\"XCL_018\" = 'Pizza' AND T3.\"XCL_020\" > 50 AND T3.\"XCL_020\" < 100",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1448"
  ]
}
```

### A SQL program that retrieves the zip code for a member by joining the member table with the zip_code table on the member's zip code identifier (XCL_04

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_046\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_035\" = 'Adela' AND T1.\"XCL_036\" = 'O''Gallagher'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1347"
  ]
}
```

### Major Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_030\") FROM major WHERE \"XCL_032\" = 'School of Applied Sciences, Technology and Education' AND \"XCL_033\" = 'College of Agriculture and Applied Sciences'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1425"
  ]
}
```

### A query that retrieves the 'XCL_036' value for members who are joined to the 'major' table via 'XCL_042' = 'XCL_030' and where the major name ('XCL_03

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_036\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T2.\"XCL_031\" = 'Law and Constitutional Studies'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1328"
  ]
}
```

### A query that joins the 'budget' and 'event' tables to find the event identifier ('XCL_011') corresponding to the budget record with the highest 'XCL_0

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_011\" FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T1.\"XCL_004\" = 'Advertisement' ORDER BY T1.\"XCL_005\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1398"
  ]
}
```

### Full SQL program that joins the 'member' table (T1) with the 'major' table (T2) on the major identifier (T2.XCL_030 = T1.XCL_042). It filters for memb

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_034\") FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T1.\"XCL_038\" = 'Member' AND T2.\"XCL_031\" LIKE '%Education%' AND T2.\"XCL_033\" = 'College of Education & Human Services'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1441"
  ]
}
```

### Full SQL program that joins event, attendance, and member tables to retrieve distinct member IDs who attended the event where event name (XCL_011) is 

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T3.\"XCL_034\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" INNER JOIN member AS T3 ON T2.\"XCL_002\" = T3.\"XCL_034\" WHERE T1.\"XCL_011\" = 'October Meeting'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1366"
  ]
}
```

### 2019 Community Service Event Ratio Query

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN \"XCL_013\" = 'Community Service' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"XCL_013\") FROM event WHERE SUBSTRING(\"XCL_012\", 1, 4) = '2019'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1400"
  ]
}
```

### Event Attendance Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_010\") FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" INNER JOIN member AS T3 ON T2.\"XCL_002\" = T3.\"XCL_034\" WHERE T1.\"XCL_011\" = 'Women''s Soccer' AND T3.\"XCL_039\" = 'Medium'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1317"
  ]
}
```

### Community Theater 2019 Attendance Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_002\") FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" WHERE T1.\"XCL_011\" = 'Community Theater' AND SUBSTRING(T1.\"XCL_012\", 1, 4) = '2019'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1395"
  ]
}
```

### A query that retrieves event identifiers (XCL_011) by joining the event table to the budget table on XCL_010 = XCL_009, filtered to only include recor

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_011\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T2.\"XCL_004\" = 'Food'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1463"
  ]
}
```

### Event-Budget Join Query

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_004\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_015\" = 'MU 215'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1418"
  ]
}
```

### Event-Budget Yearly Comparison Query

```json
{
  "kind": "program",
  "formula": "SELECT SUM(CASE WHEN SUBSTRING(T1.\"XCL_012\", 1, 4) = '2019' THEN T2.\"XCL_005\" ELSE 0 END) - SUM(CASE WHEN SUBSTRING(T1.\"XCL_012\", 1, 4) = '2020' THEN T2.\"XCL_005\" ELSE 0 END) AS num FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1340"
  ]
}
```

### Guest Speaker Budget-Event Lookup

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_004\", T1.\"XCL_013\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_015\" = 'MU 215' AND T2.\"XCL_005\" = 0 AND T1.\"XCL_013\" = 'Guest Speaker'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1427"
  ]
}
```

### A query that joins the event table (T1) with the budget table (T2) on event attribute XCL_010 matching budget attribute XCL_009. It filters for events

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_004\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_015\" = 'MU 215'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1422"
  ]
}
```

### Closed Food Budget Average Query

```json
{
  "kind": "program",
  "formula": "SELECT SUM(\"XCL_005\") / COUNT(\"XCL_005\") FROM budget WHERE \"XCL_004\" = 'Food' AND \"XCL_008\" = 'Closed'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1397"
  ]
}
```

### Retrieves XCL_035 and XCL_036 for all members filtered by XCL_039 = 'X-Large'. Returns one row per matching member record.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_035\", \"XCL_036\" FROM member WHERE \"XCL_039\" = 'X-Large'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1445"
  ]
}
```

### Member contact details for ECE department

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_045\", \"XCL_047\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" INNER JOIN zip_code AS T3 ON T3.\"XCL_043\" = T1.\"XCL_041\" WHERE \"XCL_032\" = 'Electrical and Computer Engineering Department' AND \"XCL_038\" = 'Member'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1428"
  ]
}
```

### A query that joins the 'member' and 'zip_code' tables to retrieve the 'XCL_045' attribute for members where 'XCL_035' is 'Garrett' and 'XCL_036' is 'G

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_045\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T2.\"XCL_043\" = T1.\"XCL_041\" WHERE T1.\"XCL_035\" = 'Garrett' AND T1.\"XCL_036\" = 'Gerke'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1468"
  ]
}
```

### Lincolnton NC Member Attributes Query

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_035\", T1.\"XCL_036\", T1.\"XCL_038\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T2.\"XCL_043\" = T1.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Lincolnton' AND T2.\"XCL_047\" = 'North Carolina' AND T2.\"XCL_043\" = 28092",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1469"
  ]
}
```

### Member Count by Major Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_034\") FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T2.\"XCL_031\" = 'Environmental Engineering'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1326"
  ]
}
```

### Full SQL program that joins member and income tables on XCL_034 = XCL_029, groups by member attributes XCL_035, XCL_036 and income attribute XCL_027, 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_035\", T1.\"XCL_036\", T2.\"XCL_027\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" GROUP BY T1.\"XCL_035\", T1.\"XCL_036\", T2.\"XCL_027\" ORDER BY SUM(T2.\"XCL_026\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1388"
  ]
}
```

### Full SQL program that joins member and major tables on XCL_042 = XCL_030, filters for members with role 'Secretary' (XCL_038), and returns XCL_035, XC

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_035\", T1.\"XCL_036\", \"XCL_033\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T1.\"XCL_038\" = 'Secretary'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1466"
  ]
}
```

### A query that joins the member and expense tables on XCL_034 = XCL_022, filters members where XCL_039 equals 'X-Large', and selects the corresponding e

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_018\" FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T1.\"XCL_039\" = 'X-Large'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1412"
  ]
}
```

### A query that joins the member and major tables on XCL_042 = XCL_030 to find the major record associated with a member identified by the phone number '

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_031\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_040\" = '809-555-3360'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1368"
  ]
}
```

### Computes the set of event identifiers (XCL_011) that have more than 20 attendance records but are not classified as 'Fundraiser' events. It uses an EX

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_011\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" GROUP BY T1.\"XCL_010\" HAVING COUNT(T2.\"XCL_001\") > 20 EXCEPT SELECT T1.\"XCL_011\" FROM event AS T1 WHERE T1.\"XCL_013\" = 'Fundraiser'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1323"
  ]
}
```

### A query that joins 'budget' and 'event' tables on 'XCL_009' and 'XCL_010'. It filters for 'budget' records where 'XCL_008' is 'Closed' and 'XCL_006' i

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_011\" FROM budget AS T1 INNER JOIN event AS T2 ON T2.\"XCL_010\" = T1.\"XCL_009\" WHERE T1.\"XCL_008\" = 'Closed' AND T1.\"XCL_006\" < 0 ORDER BY T1.\"XCL_006\" LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1403"
  ]
}
```

### A query that joins the budget table (T1) to the expense table (T2) on XCL_003 = XCL_023, orders the results by budget column XCL_006, and returns the 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_018\" FROM budget AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_003\" = T2.\"XCL_023\" ORDER BY T1.\"XCL_006\" LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1365"
  ]
}
```

### A SQL program that joins the 'member' and 'expense' tables on member ID (XCL_034 = XCL_022). It filters for members named 'Allen Elijah' and expenses 

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T2.\"XCL_020\") FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T1.\"XCL_036\" = 'Allen' AND T1.\"XCL_035\" = 'Elijah' AND (SUBSTRING(T2.\"XCL_019\", 6, 2) = '09' OR SUBSTRING(T2.\"XCL_019\", 6, 2) = '10')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1339"
  ]
}
```

### A full SQL program that joins event, attendance, and member tables to retrieve member identifiers (XCL_040) where the event name (XCL_011) is 'Women's

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_040\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" INNER JOIN member AS T3 ON T2.\"XCL_002\" = T3.\"XCL_034\" WHERE T1.\"XCL_011\" = 'Women''s Soccer'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1316"
  ]
}
```

### A query that joins expense and budget tables on XCL_023 = XCL_003, filters expenses where XCL_018 equals 'Water, chips, cookies', orders by XCL_020 in

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_003\" FROM expense AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_023\" = T2.\"XCL_003\" WHERE T1.\"XCL_018\" = 'Water, chips, cookies' ORDER BY T1.\"XCL_020\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1455"
  ]
}
```

### Executes an inner join between 'member' and 'major' on 'member.XCL_042' and 'major.XCL_030'. It groups the results by 'major.XCL_030', orders them by 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_033\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" GROUP BY T2.\"XCL_030\" ORDER BY COUNT(T2.\"XCL_033\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1367"
  ]
}
```

### A full SQL program that joins event, budget, and expense tables. It filters for events named 'October Meeting' with a date prefix of '2019-10-08' and 

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_021\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" WHERE T1.\"XCL_011\" = 'October Meeting' AND T1.\"XCL_012\" LIKE '2019-10-08%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1338"
  ]
}
```

### A query that joins the 'member' table (T1) with the 'expense' table (T2) on the condition that T1.'XCL_034' equals T2.'XCL_022'. It filters the result

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_041\" FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T2.\"XCL_020\" < 50",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1413"
  ]
}
```

### Query retrieving member identifiers (XCL_035) and attributes (XCL_036) by joining event, budget, expense, and member tables. Filters for events where 

```json
{
  "kind": "program",
  "formula": "SELECT T4.\"XCL_035\", T4.\"XCL_036\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" INNER JOIN member AS T4 ON T3.\"XCL_022\" = T4.\"XCL_034\" WHERE T1.\"XCL_011\" = 'Yearly Kickoff'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1387"
  ]
}
```

### Event-Budget Link Filter

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_011\", T1.\"XCL_015\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T2.\"XCL_006\" > 0",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1447"
  ]
}
```

### A full SQL program that joins the event table (T1) with the budget table (T2) on event.XCL_010 = budget.XCL_009. It filters for events where event.XCL

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_004\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_012\" = '2020-03-24T12:00:00'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1419"
  ]
}
```

### A program that retrieves event identifiers by joining the event, attendance, and member tables. It filters for the specific member where the first nam

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_011\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" INNER JOIN member AS T3 ON T2.\"XCL_002\" = T3.\"XCL_034\" WHERE T3.\"XCL_035\" = 'Maya' AND T3.\"XCL_036\" = 'Mclean'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1320"
  ]
}
```

### A query that retrieves distinct pairs of expense identifiers and attendance identifiers. It joins expense, member, and attendance tables, filtering fo

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_022\", T3.\"XCL_001\" FROM expense AS T1 INNER JOIN member AS T2 ON T1.\"XCL_022\" = T2.\"XCL_034\" INNER JOIN attendance AS T3 ON T2.\"XCL_034\" = T3.\"XCL_002\" WHERE DATE(SUBSTRING(T1.\"XCL_019\", 1, 10)) BETWEEN '2019-01-10' AND '2019-11-19' AND T1.\"XCL_021\" = 'true'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1437"
  ]
}
```

### Executes a count aggregation on the income table filtered by the condition XCL_026 = 50. Returns a single row containing the count of XCL_024 entries 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_024\") FROM income WHERE \"XCL_026\" = 50",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1423"
  ]
}
```

### SQL program that joins the event table (T1) with the attendance table (T2) on event ID (XCL_010 = XCL_001), filters for 'Women's Soccer' events, and c

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_002\") FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" WHERE T1.\"XCL_011\" = 'Women''s Soccer'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1371"
  ]
}
```

### A query that joins expense, budget, and member tables. It links expenses to budgets via XCL_023/XCL_003 and to members via XCL_022/XCL_034. The result

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_035\", T3.\"XCL_036\" FROM expense AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_023\" = T2.\"XCL_003\" INNER JOIN member AS T3 ON T1.\"XCL_022\" = T3.\"XCL_034\" ORDER BY T2.\"XCL_005\" DESC LIMIT 5",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1456"
  ]
}
```

### A query that retrieves the single highest 'XCL_027' value from the 'income' table for the period between 2019-09-01 and 2019-09-30, based on the 'XCL_

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_027\" FROM income WHERE \"XCL_025\" BETWEEN '2019-09-01' AND '2019-09-30' ORDER BY \"XCL_027\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1392"
  ]
}
```

### Query joining budget and event tables on budget reference (XCL_009) to event ID (XCL_010), filtering for 'Speaker Gifts' category, and summing budget 

```json
{
  "kind": "program",
  "formula": "SELECT SUM(T1.\"XCL_005\"), T2.\"XCL_011\" FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T1.\"XCL_004\" = 'Speaker Gifts' GROUP BY T2.\"XCL_011\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1467"
  ]
}
```

### Members with High-Value Expenses

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_035\", T1.\"XCL_036\", T2.\"XCL_031\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" INNER JOIN expense AS T3 ON T1.\"XCL_034\" = T3.\"XCL_022\" WHERE T3.\"XCL_020\" > 100",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1449"
  ]
}
```

### Latest Food Budget XCL_003

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_003\" FROM budget WHERE \"XCL_004\" = 'Food' AND \"XCL_007\" = (SELECT MAX(\"XCL_007\") FROM budget)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1406"
  ]
}
```

### A SQL program that selects the maximum value of XCL_005 from the budget table. It serves as the executable definition for retrieving the peak value of

```json
{
  "kind": "program",
  "formula": "SELECT MAX(\"XCL_005\") FROM budget",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1378"
  ]
}
```

### Full SQL program that joins the event table (T1) to the budget table (T2) on event ID (XCL_010 = XCL_009) and the budget table to the expense table (T

```json
{
  "kind": "program",
  "formula": "SELECT SUM(CASE WHEN T1.\"XCL_013\" = 'Meeting' THEN T3.\"XCL_020\" ELSE 0 END) * 100 / SUM(T3.\"XCL_020\") FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1454"
  ]
}
```

### Filtered Member List Query

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_037\" FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE DATE(SUBSTRING(T2.\"XCL_019\", 1, 10)) BETWEEN '2019-09-10' AND '2019-11-19' AND T2.\"XCL_020\" > 20",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1440"
  ]
}
```

### A full SQL program that joins expense, member, budget, and event tables to identify the member with the highest total expense who is linked to multipl

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_034\" FROM expense AS T1 INNER JOIN member AS T2 ON T1.\"XCL_022\" = T2.\"XCL_034\" INNER JOIN budget AS T3 ON T1.\"XCL_023\" = T3.\"XCL_003\" INNER JOIN event AS T4 ON T3.\"XCL_009\" = T4.\"XCL_010\" GROUP BY T2.\"XCL_034\" HAVING COUNT(DISTINCT T4.\"XCL_010\") > 1 ORDER BY SUM(T1.\"XCL_020\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1451"
  ]
}
```

### Full SQL program that joins member and expense tables on member.XCL_034 = expense.XCL_022, filters for a specific member ID, and returns member attrib

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_035\", T1.\"XCL_036\", SUM(T2.\"XCL_020\") FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T1.\"XCL_034\" = 'rec4BLdZHS2Blfp4v'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1410"
  ]
}
```

### A query that joins the 'budget' and 'event' tables on 'XCL_009' = 'XCL_010'. It filters for events where 'XCL_016' is 'Closed', orders the results by 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_011\" FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T2.\"XCL_016\" = 'Closed' ORDER BY T1.\"XCL_005\" / T1.\"XCL_007\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1376"
  ]
}
```

### A query that groups the "expense" table by "XCL_018" and filters groups where the average of "XCL_020" is greater than 50. Returns the distinct "XCL_0

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_018\" FROM expense GROUP BY \"XCL_018\" HAVING AVG(\"XCL_020\") > 50",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1444"
  ]
}
```

### Executes a SELECT DISTINCT query on the "zip_code" table to retrieve unique "XCL_046" entries where "XCL_044" is 'PO Box' and "XCL_046" is not null.

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_046\" FROM zip_code WHERE \"XCL_044\" = 'PO Box' AND NOT \"XCL_046\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1433"
  ]
}
```

### Full SQL program that computes the percentage of 'PO Box' entries in the XCL_044 column of the zip_code table, using XCL_043 as the denominator for th

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN \"XCL_044\" = 'PO Box' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"XCL_043\") FROM zip_code",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1446"
  ]
}
```

### Full SQL program that joins event, budget, and expense tables to calculate the total expense amount specifically for the 'Yearly Kickoff' event. It fi

```json
{
  "kind": "program",
  "formula": "SELECT SUM(T3.\"XCL_020\") FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" WHERE T1.\"XCL_011\" = 'Yearly Kickoff'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1386"
  ]
}
```

### A query that joins the member and major tables on the member's major ID (XCL_042) matching the major's ID (XCL_030), filters for the member named Tyle

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_033\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_035\" = 'Tyler' AND T1.\"XCL_036\" = 'Hewitt'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1330"
  ]
}
```

### Executes an inner join between member (T1) and major (T2) on T1.XCL_042 = T2.XCL_030, filtering for members where T1.XCL_036 is 'Pierce' or 'Guidi', a

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_032\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_036\" = 'Pierce' OR T1.\"XCL_036\" = 'Guidi'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1336"
  ]
}
```

### A query that retrieves the zip code for a member by joining the member and zip_code tables. It filters for a specific member using first name and last

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_044\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_035\" = 'Christof' AND T1.\"XCL_036\" = 'Nielson'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1353"
  ]
}
```

### Advertisement Budget Comparison Query

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_011\" = 'Yearly Kickoff' THEN T1.\"XCL_007\" ELSE 0 END) AS REAL) / SUM(CASE WHEN T2.\"XCL_011\" = 'October Meeting' THEN T1.\"XCL_007\" ELSE 0 END) FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T1.\"XCL_004\" = 'Advertisement' AND T2.\"XCL_013\" = 'Meeting'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1359"
  ]
}
```

### Full SQL program that joins the budget table (T1) with the event table (T2) on the budget's event reference (XCL_009) matching the event's identifier 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_010\") FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = 'November Meeting' AND T1.\"XCL_006\" < 0",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1348"
  ]
}
```

### A full SQL program that joins the member table (T1) with the expense table (T2) on member identifier XCL_034 matching expense identifier XCL_022. It f

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_018\" FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T1.\"XCL_035\" = 'Sacha' AND T1.\"XCL_036\" = 'Harrison'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1411"
  ]
}
```

### A query that joins the member and major tables on XCL_042 = XCL_030 to find the major attribute (XCL_031) associated with a member named Angela Sander

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_031\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_035\" = 'Angela' AND T1.\"XCL_036\" = 'Sanders'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1312"
  ]
}
```

### Illinois Member Attributes Query

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T2.\"XCL_047\" = 'Illinois'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1334"
  ]
}
```

### Full SQL program that computes the parking budget percentage. It joins the 'budget' table (T1) to the 'event' table (T2) on XCL_009 = XCL_010, filters

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN T1.\"XCL_004\" = 'Parking' THEN T1.\"XCL_007\" ELSE 0 END) AS REAL) * 100 / SUM(T1.\"XCL_007\") FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = 'November Speaker'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1360"
  ]
}
```

### A query that joins the member and income tables on XCL_034 and XCL_029, filters for members where XCL_038 is 'Vice President', and returns the corresp

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_026\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_038\" = 'Vice President'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1331"
  ]
}
```

### A query that retrieves event identifiers where the event is linked to a budget categorized as 'Parking' and the associated expense amount is less than

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_011\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" WHERE T2.\"XCL_004\" = 'Parking' AND T3.\"XCL_020\" < (SELECT AVG(\"XCL_020\") FROM expense)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1453"
  ]
}
```

### A query that joins the budget and expense tables on XCL_003 = XCL_023 to retrieve the budget identifier (XCL_008) for expenses matching the category '

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_008\" FROM budget AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_003\" = T2.\"XCL_023\" WHERE T2.\"XCL_018\" = 'Post Cards, Posters' AND T2.\"XCL_019\" = '2019-08-20'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1350"
  ]
}
```

### A query that joins `event` and `budget` tables on `XCL_010` = `XCL_009`. It filters events where `XCL_011` equals 'April Speaker', groups the results 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_004\", SUM(T2.\"XCL_007\") FROM event AS T1 JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_011\" = 'April Speaker' GROUP BY T2.\"XCL_004\" ORDER BY SUM(T2.\"XCL_007\") ASC",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1405"
  ]
}
```

### Query: Total Budget for September Speaker

```json
{
  "kind": "program",
  "formula": "SELECT SUM(T1.\"XCL_007\") FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = 'September Speaker'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1349"
  ]
}
```

### A query that joins the event table to the budget table on XCL_010 = XCL_009, filters for budget records where XCL_006 > 30, and returns the correspond

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_013\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T2.\"XCL_006\" > 30",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1417"
  ]
}
```

### Major Ratio Query

```json
{
  "kind": "program",
  "formula": "SELECT SUM(CASE WHEN \"XCL_031\" = 'Finance' THEN 1 ELSE 0 END) / SUM(CASE WHEN \"XCL_031\" = 'Physics' THEN 1 ELSE 0 END) AS ratio FROM major",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1391"
  ]
}
```

### Full SQL program that joins the member table with the zip_code table on the zip code identifier, then computes the percentage difference in member cou

```json
{
  "kind": "program",
  "formula": "SELECT CAST((SUM(CASE WHEN T2.\"XCL_047\" = 'New Jersey' THEN 1 ELSE 0 END) - SUM(CASE WHEN T2.\"XCL_047\" = 'Vermont' THEN 1 ELSE 0 END)) AS REAL) * 100 / COUNT(T1.\"XCL_034\") AS diff FROM member AS T1 INNER JOIN zip_code AS T2 ON T2.\"XCL_043\" = T1.\"XCL_041\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1458"
  ]
}
```

### Full SQL program that joins major, member, and attendance tables to retrieve the major identifier and count of attendance records for the member with 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T3.\"XCL_001\"), T1.\"XCL_031\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" INNER JOIN attendance AS T3 ON T2.\"XCL_034\" = T3.\"XCL_002\" WHERE T2.\"XCL_035\" = 'Luisa' AND T2.\"XCL_036\" = 'Guidi'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1396"
  ]
}
```

### Full SQL program that joins member and attendance tables on XCL_034 = XCL_002, groups by attendance key XCL_002, and filters for groups where the coun

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_034\" = T2.\"XCL_002\" GROUP BY T2.\"XCL_002\" HAVING COUNT(T2.\"XCL_001\") > 7",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1381"
  ]
}
```

### A query that joins the member and zip_code tables to retrieve the zip code attribute (XCL_047) for members where XCL_035 is 'Sacha' and XCL_036 is 'Ha

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_047\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_035\" = 'Sacha' AND T1.\"XCL_036\" = 'Harrison'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1355"
  ]
}
```

### A SQL program that joins the event and attendance tables to count attendance records specifically for 'Women's Soccer' events. It filters events by th

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_010\") FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" WHERE T1.\"XCL_011\" = 'Women''s Soccer'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1315"
  ]
}
```

### A query that joins the member and major tables on XCL_042 and XCL_030, filters for members where XCL_038 is 'Vice President', and returns the correspo

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_031\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_038\" = 'Vice President'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1354"
  ]
}
```

### A SQL program that selects distinct 'XCL_011' identifiers from the 'event' table. It filters for events where 'XCL_013' equals 'Game', the date extrac

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_011\" FROM event WHERE \"XCL_013\" = 'Game' AND DATE(SUBSTRING(\"XCL_012\", 1, 10)) BETWEEN '2019-03-15' AND '2020-03-20' AND \"XCL_016\" = 'Closed'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1435"
  ]
}
```

### President Zip Code Attributes

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_045\", T2.\"XCL_047\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_038\" = 'President'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1333"
  ]
}
```

### A query that retrieves the major identifier (XCL_031) for all records in the major table that are linked via XCL_030 to XCL_042 in the member table, w

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_031\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" WHERE T2.\"XCL_038\" = 'Vice President'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1420"
  ]
}
```

### Event count query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_010\") FROM event WHERE \"XCL_013\" = 'Meeting' AND SUBSTRING(\"XCL_012\", 1, 4) = '2020'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1379"
  ]
}
```

### SQL program that counts rows in the zip_code table where XCL_046 is 'Orange County' and XCL_047 is 'Virginia'. The count is performed on column XCL_04

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_045\") FROM zip_code WHERE \"XCL_046\" = 'Orange County' AND \"XCL_047\" = 'Virginia'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1362"
  ]
}
```

### Query retrieving specific expense attributes (XCL_017, XCL_018) by joining the member and expense tables on member ID (XCL_034 = XCL_022) and filterin

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_017\", T2.\"XCL_018\" FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T1.\"XCL_038\" = 'Vice President'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1370"
  ]
}
```

### Elementary Education Member Query

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_036\", T1.\"XCL_040\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T2.\"XCL_031\" = 'Elementary Education'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1461"
  ]
}
```

### A query that joins attendance, event, and member tables to retrieve member identifiers (XCL_036) where the event name is 'Women's Soccer' and the memb

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_036\" FROM attendance AS T1 INNER JOIN event AS T2 ON T2.\"XCL_010\" = T1.\"XCL_001\" INNER JOIN member AS T3 ON T1.\"XCL_002\" = T3.\"XCL_034\" WHERE T2.\"XCL_011\" = 'Women''s Soccer' AND T3.\"XCL_038\" = 'Member'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1431"
  ]
}
```

### Expense Sum Query

```json
{
  "kind": "program",
  "formula": "SELECT SUM(\"XCL_020\") FROM expense WHERE \"XCL_019\" = '2019-08-20'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1409"
  ]
}
```

### A query that joins the major and member tables on XCL_030 = XCL_042, filters for majors where XCL_031 is 'Business', and returns the corresponding mem

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_038\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" WHERE T1.\"XCL_031\" = 'Business'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1415"
  ]
}
```

### Food Budget Sum Query

```json
{
  "kind": "program",
  "formula": "SELECT SUM(\"XCL_005\") FROM budget WHERE \"XCL_004\" = 'Food'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1380"
  ]
}
```

### Filtered Member-Expense Join

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_035\", T2.\"XCL_036\", T1.\"XCL_020\" FROM expense AS T1 INNER JOIN member AS T2 ON T1.\"XCL_022\" = T2.\"XCL_034\" WHERE T1.\"XCL_018\" = 'Water, Veggie tray, supplies'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1460"
  ]
}
```

### A query that joins the member and income tables on XCL_034 = XCL_029, filters for income type 'Dues', orders by XCL_025 (likely a date or sequence), a

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T2.\"XCL_027\" = 'Dues' ORDER BY T2.\"XCL_025\" LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1358"
  ]
}
```

### A query that joins the member and major tables on the member's XCL_042 field matching the major's XCL_030 field. It filters for a specific member reco

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_033\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T1.\"XCL_042\" = 'rec1N0upiVLy5esTO' AND T1.\"XCL_035\" = 'Katy'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1438"
  ]
}
```

### A query that retrieves the list of major identifiers (XCL_032) from the 'major' table where the college (XCL_033) is 'College of Humanities and Social

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_032\" FROM major WHERE \"XCL_033\" = 'College of Humanities and Social Sciences'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1363"
  ]
}
```

### A query that joins the budget and event tables on XCL_009 = XCL_010, orders the results by budget column XCL_007 in descending order, and returns the 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_011\" FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" ORDER BY T1.\"XCL_007\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1369"
  ]
}
```

### High-Income Member Zip Codes

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T3.\"XCL_045\", T3.\"XCL_046\" FROM income AS T1 INNER JOIN member AS T2 ON T1.\"XCL_029\" = T2.\"XCL_034\" INNER JOIN zip_code AS T3 ON T3.\"XCL_043\" = T2.\"XCL_041\" WHERE T1.\"XCL_026\" > 40",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1450"
  ]
}
```

### A SQL program that joins the expense table (T1) with the member table (T2) on the expense member ID (XCL_022) matching the member ID (XCL_034). It fil

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T1.\"XCL_020\") FROM expense AS T1 INNER JOIN member AS T2 ON T1.\"XCL_022\" = T2.\"XCL_034\" WHERE T2.\"XCL_038\" <> 'Member'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1452"
  ]
}
```

### A program that joins the event table to the attendance table on the event key (XCL_010 = XCL_001), groups by the event identifier (XCL_011), orders th

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_011\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" GROUP BY T1.\"XCL_011\" ORDER BY COUNT(T2.\"XCL_001\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1318"
  ]
}
```

### Art and Design Department Member Query

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T2.\"XCL_032\" = 'Art and Design Department'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1314"
  ]
}
```

### Filtered Member-Income Join

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T2.\"XCL_026\" > 40",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1385"
  ]
}
```

### A full query program that joins member, attendance, and event tables to determine if the specific member 'Maya Mclean' attended a 'Women's Soccer' eve

```json
{
  "kind": "program",
  "formula": "SELECT CASE WHEN T3.\"XCL_011\" = 'Women''s Soccer' THEN 'YES' END AS result FROM member AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_034\" = T2.\"XCL_002\" INNER JOIN event AS T3 ON T2.\"XCL_001\" = T3.\"XCL_010\" WHERE T1.\"XCL_035\" = 'Maya' AND T1.\"XCL_036\" = 'Mclean'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1399"
  ]
}
```

### A query that retrieves the zip code (XCL_043) from the zip_code table where the delivery type (XCL_044) is 'PO Box', the municipality (XCL_046) is 'Sa

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_043\" FROM zip_code WHERE \"XCL_044\" = 'PO Box' AND \"XCL_046\" = 'San Juan Municipio' AND \"XCL_047\" = 'Puerto Rico'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1434"
  ]
}
```

### Full SQL program that joins the 'event' and 'budget' tables on event ID (XCL_010 = XCL_009). It filters for events named 'September Meeting' with a mo

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_005\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_011\" = 'September Meeting' AND T2.\"XCL_004\" = 'Advertisement' AND SUBSTRING(T1.\"XCL_012\", 6, 2) = '09'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1335"
  ]
}
```

### Full SQL program that joins the member table (T1) with the attendance table (T2) on member ID (XCL_034 = XCL_002), filters for a specific member phone

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_001\") FROM member AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_034\" = T2.\"XCL_002\" WHERE T1.\"XCL_040\" = '954-555-6240'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1374"
  ]
}
```

### A query that retrieves specific member details (XCL_035, XCL_036) by joining major, member, attendance, and event tables. It filters for events named 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_035\", T2.\"XCL_036\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" INNER JOIN attendance AS T3 ON T2.\"XCL_034\" = T3.\"XCL_002\" INNER JOIN event AS T4 ON T3.\"XCL_001\" = T4.\"XCL_010\" WHERE T4.\"XCL_011\" = 'Community Theater' AND T1.\"XCL_031\" = 'Interior Design'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1382"
  ]
}
```

### "event"."XCL_011" = 'September Meeting' AND "budget"."XCL_004" = 'Food' AND SUBSTRING("event"."XCL_012", 6, 2) = '09'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'September Meeting' AND \"budget\".\"XCL_004\" = 'Food' AND SUBSTRING(\"event\".\"XCL_012\", 6, 2) = '09'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_005\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_011\" = 'September Meeting' AND T2.\"XCL_004\" = 'Food' AND SUBSTRING(T1.\"XCL_012\", 6, 2) = '09'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1332"
  ]
}
```

### "major"."XCL_031" = 'Business'

```json
{
  "kind": "predicate",
  "formula": "\"major\".\"XCL_031\" = 'Business'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_038\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" WHERE T1.\"XCL_031\" = 'Business'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1415"
  ]
}
```

### "income"."XCL_027" = 'Dues'

```json
{
  "kind": "predicate",
  "formula": "\"income\".\"XCL_027\" = 'Dues'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T2.\"XCL_027\" = 'Dues' ORDER BY T2.\"XCL_025\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1358"
  ]
}
```

### "zip_code"."XCL_047" = 'Maryland'

```json
{
  "kind": "predicate",
  "formula": "\"zip_code\".\"XCL_047\" = 'Maryland'",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_034\") FROM zip_code AS T1 INNER JOIN member AS T2 ON T1.\"XCL_043\" = T2.\"XCL_041\" WHERE T1.\"XCL_047\" = 'Maryland'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1373"
  ]
}
```

### Member Identifier

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_040\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_040\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T2.\"XCL_031\" = 'Business' AND T2.\"XCL_033\" = 'College of Agriculture and Applied Sciences'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_040\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_040\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r1\".\"XCL_030\" = \"r0\".\"XCL_042\" WHERE \"r1\".\"XCL_031\" = 'Business' AND \"r1\".\"XCL_033\" = 'College of Agriculture and Applied Sciences'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1439"
  ]
}
```

### Member Identifier for Women's Soccer Attendees

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_040\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_040\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" INNER JOIN member AS T3 ON T2.\"XCL_002\" = T3.\"XCL_034\" WHERE T1.\"XCL_011\" = 'Women''s Soccer'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_040\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "attendance"
      },
      {
        "role": "r2",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_040\" AS \"value\" FROM event AS \"r0\" INNER JOIN attendance AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_001\" INNER JOIN member AS \"r2\" ON \"r1\".\"XCL_002\" = \"r2\".\"XCL_034\" WHERE \"r0\".\"XCL_011\" = 'Women''s Soccer'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1316"
  ]
}
```

### Budget Attribute XCL_004

```json
{
  "kind": "binding",
  "formula": "\"budget\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_004\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_015\" = 'MU 215'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_004\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_004\" AS \"value\" FROM event AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" WHERE \"r0\".\"XCL_015\" = 'MU 215'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1418"
  ]
}
```

### Event Attribute XCL_011

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" ORDER BY T1.\"XCL_007\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1369"
  ]
}
```

### Calculates the percentage of rows in the 'event' table where the 'XCL_013' column equals 'Community Service', relative to the total count of non-null 

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"event\".\"XCL_013\" = 'Community Service' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"event\".\"XCL_013\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN \"XCL_013\" = 'Community Service' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"XCL_013\") FROM event WHERE SUBSTRING(\"XCL_012\", 1, 4) = '2019'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r0\".\"XCL_013\" = 'Community Service' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_013\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r0\".\"XCL_013\" = 'Community Service' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_013\") AS \"value\" FROM event AS \"r0\" WHERE SUBSTRING(\"r0\".\"XCL_012\", 1, 4) = '2019'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1400"
  ]
}
```

### Major XCL_031

```json
{
  "kind": "binding",
  "formula": "\"major\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_031\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" WHERE T2.\"XCL_035\" = 'Phillip' AND T2.\"XCL_036\" = 'Cullen'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_031\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "major"
      },
      {
        "role": "r1",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_031\" AS \"value\" FROM major AS \"r0\" INNER JOIN member AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_042\" WHERE \"r1\".\"XCL_035\" = 'Phillip' AND \"r1\".\"XCL_036\" = 'Cullen'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1414"
  ]
}
```

### "zip_code"."XCL_047" = 'Illinois'

```json
{
  "kind": "predicate",
  "formula": "\"zip_code\".\"XCL_047\" = 'Illinois'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T2.\"XCL_047\" = 'Illinois'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1334"
  ]
}
```

### Member Attribute XCL_035

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\", SUM(T2.\"XCL_020\") FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T1.\"XCL_034\" = 'rec4BLdZHS2Blfp4v'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1410"
  ]
}
```

### "event"."XCL_011" = 'September Speaker'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'September Speaker'",
  "grain": [],
  "population_scope": "SELECT SUM(T1.\"XCL_007\") FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = 'September Speaker'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1349"
  ]
}
```

### Finance to Physics Major Ratio

```json
{
  "kind": "metric",
  "formula": "SUM(CASE WHEN \"major\".\"XCL_031\" = 'Finance' THEN 1 ELSE 0 END) / SUM(CASE WHEN \"major\".\"XCL_031\" = 'Physics' THEN 1 ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN \"XCL_031\" = 'Finance' THEN 1 ELSE 0 END) / SUM(CASE WHEN \"XCL_031\" = 'Physics' THEN 1 ELSE 0 END) AS ratio FROM major",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(CASE WHEN \"r0\".\"XCL_031\" = 'Finance' THEN 1 ELSE 0 END) / SUM(CASE WHEN \"r0\".\"XCL_031\" = 'Physics' THEN 1 ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT SUM(CASE WHEN \"r0\".\"XCL_031\" = 'Finance' THEN 1 ELSE 0 END) / SUM(CASE WHEN \"r0\".\"XCL_031\" = 'Physics' THEN 1 ELSE 0 END) AS \"value\" FROM major AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1391"
  ]
}
```

### "member"."XCL_040" = '954-555-6240'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_040\" = '954-555-6240'",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_001\") FROM member AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_034\" = T2.\"XCL_002\" WHERE T1.\"XCL_040\" = '954-555-6240'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1374"
  ]
}
```

### "expense"."XCL_019" = '2019-08-20'

```json
{
  "kind": "predicate",
  "formula": "\"expense\".\"XCL_019\" = '2019-08-20'",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_020\") FROM expense WHERE \"XCL_019\" = '2019-08-20'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1409"
  ]
}
```

### Member Zip Code Attribute

```json
{
  "kind": "binding",
  "formula": "\"zip_code\".\"XCL_045\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_045\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T2.\"XCL_043\" = T1.\"XCL_041\" WHERE T1.\"XCL_035\" = 'Garrett' AND T1.\"XCL_036\" = 'Gerke'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_045\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_045\" AS \"value\" FROM member AS \"r0\" INNER JOIN zip_code AS \"r1\" ON \"r1\".\"XCL_043\" = \"r0\".\"XCL_041\" WHERE \"r0\".\"XCL_035\" = 'Garrett' AND \"r0\".\"XCL_036\" = 'Gerke'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1468"
  ]
}
```

### A conditional indicator that returns 'YES' if the associated event is 'Women's Soccer', otherwise NULL. It operates at the grain of the joined member-

```json
{
  "kind": "binding",
  "formula": "CASE WHEN \"event\".\"XCL_011\" = 'Women''s Soccer' THEN 'YES' END",
  "grain": [],
  "population_scope": "SELECT CASE WHEN T3.\"XCL_011\" = 'Women''s Soccer' THEN 'YES' END AS result FROM member AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_034\" = T2.\"XCL_002\" INNER JOIN event AS T3 ON T2.\"XCL_001\" = T3.\"XCL_010\" WHERE T1.\"XCL_035\" = 'Maya' AND T1.\"XCL_036\" = 'Mclean'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CASE WHEN \"r2\".\"XCL_011\" = 'Women''s Soccer' THEN 'YES' END",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "attendance"
      },
      {
        "role": "r2",
        "physical_table": "event"
      }
    ],
    "scope_sql": "SELECT CASE WHEN \"r2\".\"XCL_011\" = 'Women''s Soccer' THEN 'YES' END AS \"value\" FROM member AS \"r0\" INNER JOIN attendance AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_002\" INNER JOIN event AS \"r2\" ON \"r1\".\"XCL_001\" = \"r2\".\"XCL_010\" WHERE \"r0\".\"XCL_035\" = 'Maya' AND \"r0\".\"XCL_036\" = 'Mclean'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1399"
  ]
}
```

### "event"."XCL_011" = 'January Speaker'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'January Speaker'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_004\", T2.\"XCL_007\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_011\" = 'January Speaker'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1462"
  ]
}
```

### Member Attribute XCL_035

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T2.\"XCL_026\" > 40",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "income"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_035\" AS \"value\" FROM member AS \"r0\" INNER JOIN income AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_029\" WHERE \"r1\".\"XCL_026\" > 40",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1385"
  ]
}
```

### "budget"."XCL_008" = 'Closed' AND "budget"."XCL_006" < 0

```json
{
  "kind": "predicate",
  "formula": "\"budget\".\"XCL_008\" = 'Closed' AND \"budget\".\"XCL_006\" < 0",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" FROM budget AS T1 INNER JOIN event AS T2 ON T2.\"XCL_010\" = T1.\"XCL_009\" WHERE T1.\"XCL_008\" = 'Closed' AND T1.\"XCL_006\" < 0 ORDER BY T1.\"XCL_006\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1403"
  ]
}
```

### Event Identifier

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T2.\"XCL_016\" = 'Closed' ORDER BY T1.\"XCL_005\" / T1.\"XCL_007\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1376"
  ]
}
```

### Major Identifier

```json
{
  "kind": "binding",
  "formula": "\"major\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT COUNT(T3.\"XCL_001\"), T1.\"XCL_031\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" INNER JOIN attendance AS T3 ON T2.\"XCL_034\" = T3.\"XCL_002\" WHERE T2.\"XCL_035\" = 'Luisa' AND T2.\"XCL_036\" = 'Guidi'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1396"
  ]
}
```

### Event ID for High-Attendance Non-Meetings

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_011\"",
  "grain": [
    "\"event\".\"XCL_010\""
  ],
  "population_scope": "SELECT T1.\"XCL_011\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" GROUP BY T1.\"XCL_010\" HAVING COUNT(T2.\"XCL_001\") > 10",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_011\"",
    "grain": [
      "\"r0\".\"XCL_010\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "attendance"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_010\" AS \"grain_0\", \"r0\".\"XCL_011\" AS \"value\" FROM event AS \"r0\" INNER JOIN attendance AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_001\" GROUP BY \"r0\".\"XCL_010\" HAVING COUNT(\"r1\".\"XCL_001\") > 10",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1322"
  ]
}
```

### "budget"."XCL_004" = 'Advertisement'

```json
{
  "kind": "predicate",
  "formula": "\"budget\".\"XCL_004\" = 'Advertisement'",
  "grain": [],
  "population_scope": "SELECT \"XCL_003\" FROM budget WHERE \"XCL_004\" = 'Advertisement' ORDER BY \"XCL_007\" DESC LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1407"
  ]
}
```

### Event Attribute XCL_015

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_015\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_010\", \"XCL_015\", \"XCL_016\" FROM event WHERE DATE(SUBSTRING(\"XCL_012\", 1, 10)) BETWEEN '2019-11-01' AND '2020-03-31'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_015\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_015\" AS \"value\" FROM event AS \"r0\" WHERE DATE(SUBSTRING(\"r0\".\"XCL_012\", 1, 10)) BETWEEN '2019-11-01' AND '2020-03-31'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1443"
  ]
}
```

### "major"."XCL_032" = 'Art and Design Department'

```json
{
  "kind": "predicate",
  "formula": "\"major\".\"XCL_032\" = 'Art and Design Department'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T2.\"XCL_032\" = 'Art and Design Department'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1314"
  ]
}
```

### "member"."XCL_034" = 'rec4BLdZHS2Blfp4v'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_034\" = 'rec4BLdZHS2Blfp4v'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\", SUM(T2.\"XCL_020\") FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T1.\"XCL_034\" = 'rec4BLdZHS2Blfp4v'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1410"
  ]
}
```

### Major Attribute XCL_032

```json
{
  "kind": "binding",
  "formula": "\"major\".\"XCL_032\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_032\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_036\" = 'Pierce' OR T1.\"XCL_036\" = 'Guidi'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_032\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_032\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r0\".\"XCL_042\" = \"r1\".\"XCL_030\" WHERE \"r0\".\"XCL_036\" = 'Pierce' OR \"r0\".\"XCL_036\" = 'Guidi'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1336"
  ]
}
```

### Aggregates the count of non-null values in the member.XCL_034 column. The population is restricted to members (T1) who are joined to majors (T2) where

```json
{
  "kind": "metric",
  "formula": "COUNT(\"member\".\"XCL_034\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_034\") FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T2.\"XCL_031\" = 'Business' AND T1.\"XCL_039\" = 'Medium'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_034\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_034\") AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r0\".\"XCL_042\" = \"r1\".\"XCL_030\" WHERE \"r1\".\"XCL_031\" = 'Business' AND \"r0\".\"XCL_039\" = 'Medium'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1352"
  ]
}
```

### Attendance Identifier

```json
{
  "kind": "binding",
  "formula": "\"attendance\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_001\" FROM expense AS T1 INNER JOIN member AS T2 ON T1.\"XCL_022\" = T2.\"XCL_034\" INNER JOIN attendance AS T3 ON T2.\"XCL_034\" = T3.\"XCL_002\" WHERE T1.\"XCL_020\" > 50",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1436"
  ]
}
```

### Major XCL_033 for most frequent member association

```json
{
  "kind": "binding",
  "formula": "\"major\".\"XCL_033\"",
  "grain": [
    "\"major\".\"XCL_030\""
  ],
  "population_scope": "SELECT T2.\"XCL_033\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" GROUP BY T2.\"XCL_030\" ORDER BY COUNT(T2.\"XCL_033\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1367"
  ]
}
```

### The sum of column XCL_020 from the expense table, aggregated per event identifier (XCL_013) for events named 'October Meeting'.

```json
{
  "kind": "metric",
  "formula": "SUM(\"expense\".\"XCL_020\")",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_013\", SUM(T3.\"XCL_020\") FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" WHERE T1.\"XCL_011\" = 'October Meeting'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r2\".\"XCL_020\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      },
      {
        "role": "r2",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT SUM(\"r2\".\"XCL_020\") AS \"value\" FROM event AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" INNER JOIN expense AS \"r2\" ON \"r1\".\"XCL_003\" = \"r2\".\"XCL_023\" WHERE \"r0\".\"XCL_011\" = 'October Meeting'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1404"
  ]
}
```

### Budget Amount

```json
{
  "kind": "binding",
  "formula": "\"budget\".\"XCL_005\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_005\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_011\" = 'September Meeting' AND T2.\"XCL_004\" = 'Food' AND SUBSTRING(T1.\"XCL_012\", 6, 2) = '09'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_005\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_005\" AS \"value\" FROM event AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" WHERE \"r0\".\"XCL_011\" = 'September Meeting' AND \"r1\".\"XCL_004\" = 'Food' AND SUBSTRING(\"r0\".\"XCL_012\", 6, 2) = '09'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1332"
  ]
}
```

### "event"."XCL_015" = 'MU 215'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_015\" = 'MU 215'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_004\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_015\" = 'MU 215'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1418"
  ]
}
```

### "event"."XCL_011" = 'September Meeting' AND "budget"."XCL_004" = 'Advertisement' AND SUBSTRING("event"."XCL_012", 6, 2) = '09'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'September Meeting' AND \"budget\".\"XCL_004\" = 'Advertisement' AND SUBSTRING(\"event\".\"XCL_012\", 6, 2) = '09'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_005\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_011\" = 'September Meeting' AND T2.\"XCL_004\" = 'Advertisement' AND SUBSTRING(T1.\"XCL_012\", 6, 2) = '09'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1335"
  ]
}
```

### "member"."XCL_038" = 'Member' AND "major"."XCL_031" LIKE '%Education%' AND "major"."XCL_033" = 'College of Education & Human Services'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_038\" = 'Member' AND \"major\".\"XCL_031\" LIKE '%Education%' AND \"major\".\"XCL_033\" = 'College of Education & Human Services'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_034\") FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T1.\"XCL_038\" = 'Member' AND T2.\"XCL_031\" LIKE '%Education%' AND T2.\"XCL_033\" = 'College of Education & Human Services'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1441"
  ]
}
```

### Member Identifier 2

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T2.\"XCL_027\" = 'Dues' ORDER BY T2.\"XCL_025\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1358"
  ]
}
```

### DATE(SUBSTRING("expense"."XCL_019", 1, 10)) BETWEEN '2019-01-10' AND '2019-11-19' AND "expense"."XCL_021" = 'true'

```json
{
  "kind": "predicate",
  "formula": "DATE(SUBSTRING(\"expense\".\"XCL_019\", 1, 10)) BETWEEN '2019-01-10' AND '2019-11-19' AND \"expense\".\"XCL_021\" = 'true'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_022\", T3.\"XCL_001\" FROM expense AS T1 INNER JOIN member AS T2 ON T1.\"XCL_022\" = T2.\"XCL_034\" INNER JOIN attendance AS T3 ON T2.\"XCL_034\" = T3.\"XCL_002\" WHERE DATE(SUBSTRING(T1.\"XCL_019\", 1, 10)) BETWEEN '2019-01-10' AND '2019-11-19' AND T1.\"XCL_021\" = 'true'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1437"
  ]
}
```

### Attendance Identifier

```json
{
  "kind": "binding",
  "formula": "\"attendance\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_022\", T3.\"XCL_001\" FROM expense AS T1 INNER JOIN member AS T2 ON T1.\"XCL_022\" = T2.\"XCL_034\" INNER JOIN attendance AS T3 ON T2.\"XCL_034\" = T3.\"XCL_002\" WHERE DATE(SUBSTRING(T1.\"XCL_019\", 1, 10)) BETWEEN '2019-01-10' AND '2019-11-19' AND T1.\"XCL_021\" = 'true'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1437"
  ]
}
```

### "income"."XCL_025" BETWEEN '2019-09-01' AND '2019-09-30'

```json
{
  "kind": "predicate",
  "formula": "\"income\".\"XCL_025\" BETWEEN '2019-09-01' AND '2019-09-30'",
  "grain": [],
  "population_scope": "SELECT \"XCL_027\" FROM income WHERE \"XCL_025\" BETWEEN '2019-09-01' AND '2019-09-30' ORDER BY \"XCL_027\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1392"
  ]
}
```

### Calculates the percentage of rows in the 'budget' table where the value of 'XCL_006' is less than 0, relative to the total count of non-null 'XCL_003'

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"budget\".\"XCL_006\" < 0 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"budget\".\"XCL_003\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN \"XCL_006\" < 0 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"XCL_003\") FROM budget",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r0\".\"XCL_006\" < 0 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_003\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "budget"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r0\".\"XCL_006\" < 0 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_003\") AS \"value\" FROM budget AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1442"
  ]
}
```

### Member Attribute XCL_036

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\", \"XCL_033\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T1.\"XCL_038\" = 'Secretary'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_036\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r1\".\"XCL_030\" = \"r0\".\"XCL_042\" WHERE \"r0\".\"XCL_038\" = 'Secretary'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1466"
  ]
}
```

### "member"."XCL_038" LIKE 'vice president'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_038\" LIKE 'vice president'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_033\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_038\" LIKE 'vice president'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1319"
  ]
}
```

### "major"."XCL_031" = 'Elementary Education'

```json
{
  "kind": "predicate",
  "formula": "\"major\".\"XCL_031\" = 'Elementary Education'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_036\", T1.\"XCL_040\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T2.\"XCL_031\" = 'Elementary Education'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1461"
  ]
}
```

### "member"."XCL_035" = 'Luisa' AND "member"."XCL_036" = 'Guidi'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_035\" = 'Luisa' AND \"member\".\"XCL_036\" = 'Guidi'",
  "grain": [],
  "population_scope": "SELECT COUNT(T3.\"XCL_001\"), T1.\"XCL_031\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" INNER JOIN attendance AS T3 ON T2.\"XCL_034\" = T3.\"XCL_002\" WHERE T2.\"XCL_035\" = 'Luisa' AND T2.\"XCL_036\" = 'Guidi'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1396"
  ]
}
```

### Budget Identifier

```json
{
  "kind": "binding",
  "formula": "\"budget\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_004\", T1.\"XCL_013\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_015\" = 'MU 215' AND T2.\"XCL_005\" = 0 AND T1.\"XCL_013\" = 'Guest Speaker'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1427"
  ]
}
```

### Average Expense Amount for Non-Members

```json
{
  "kind": "metric",
  "formula": "AVG(\"expense\".\"XCL_020\")",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_020\") FROM expense AS T1 INNER JOIN member AS T2 ON T1.\"XCL_022\" = T2.\"XCL_034\" WHERE T2.\"XCL_038\" <> 'Member'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_020\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "expense"
      },
      {
        "role": "r1",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_020\") AS \"value\" FROM expense AS \"r0\" INNER JOIN member AS \"r1\" ON \"r0\".\"XCL_022\" = \"r1\".\"XCL_034\" WHERE \"r1\".\"XCL_038\" <> 'Member'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1452"
  ]
}
```

### Member XCL_038

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_036\", T1.\"XCL_038\" FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T2.\"XCL_019\" = '2019-09-10' AND T2.\"XCL_018\" = 'Pizza'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_038\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_038\" AS \"value\" FROM member AS \"r0\" INNER JOIN expense AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_022\" WHERE \"r1\".\"XCL_019\" = '2019-09-10' AND \"r1\".\"XCL_018\" = 'Pizza'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1430"
  ]
}
```

### Budget Identifier for Posters Expenses

```json
{
  "kind": "binding",
  "formula": "\"budget\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_004\" FROM expense AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_023\" = T2.\"XCL_003\" WHERE T1.\"XCL_018\" = 'Posters'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1465"
  ]
}
```

### Aggregates the count of non-null values in column XCL_010 from the event table, filtered to rows where XCL_013 is 'Meeting' and the first four charact

```json
{
  "kind": "metric",
  "formula": "COUNT(\"event\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_010\") FROM event WHERE \"XCL_013\" = 'Meeting' AND SUBSTRING(\"XCL_012\", 1, 4) = '2020'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_010\") AS \"value\" FROM event AS \"r0\" WHERE \"r0\".\"XCL_013\" = 'Meeting' AND SUBSTRING(\"r0\".\"XCL_012\", 1, 4) = '2020'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1379"
  ]
}
```

### "member"."XCL_035" = 'Sacha' AND "member"."XCL_036" = 'Harrison'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_035\" = 'Sacha' AND \"member\".\"XCL_036\" = 'Harrison'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_035\" = 'Sacha' AND T1.\"XCL_036\" = 'Harrison'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1355"
  ]
}
```

### Member Attribute XCL_038

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\", T1.\"XCL_038\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T2.\"XCL_043\" = T1.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Lincolnton' AND T2.\"XCL_047\" = 'North Carolina' AND T2.\"XCL_043\" = 28092",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_038\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_038\" AS \"value\" FROM member AS \"r0\" INNER JOIN zip_code AS \"r1\" ON \"r1\".\"XCL_043\" = \"r0\".\"XCL_041\" WHERE \"r1\".\"XCL_045\" = 'Lincolnton' AND \"r1\".\"XCL_047\" = 'North Carolina' AND \"r1\".\"XCL_043\" = 28092",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1469"
  ]
}
```

### "member"."XCL_038" = 'Member' AND "member"."XCL_039" = 'Medium'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_038\" = 'Member' AND \"member\".\"XCL_039\" = 'Medium'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_026\" = 50 THEN 1.0 ELSE 0 END) AS REAL) * 100 / COUNT(T2.\"XCL_024\") FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_038\" = 'Member' AND T1.\"XCL_039\" = 'Medium'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1432"
  ]
}
```

### "member"."XCL_040" = '809-555-3360'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_040\" = '809-555-3360'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_031\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_040\" = '809-555-3360'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1368"
  ]
}
```

### "event"."XCL_011" = 'Yearly Kickoff'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'Yearly Kickoff'",
  "grain": [],
  "population_scope": "SELECT T4.\"XCL_035\", T4.\"XCL_036\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" INNER JOIN member AS T4 ON T3.\"XCL_022\" = T4.\"XCL_034\" WHERE T1.\"XCL_011\" = 'Yearly Kickoff'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1387"
  ]
}
```

### Event Attribute XCL_013

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_013\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_013\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T2.\"XCL_006\" > 30",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_013\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_013\" AS \"value\" FROM event AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" WHERE \"r1\".\"XCL_006\" > 30",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1417"
  ]
}
```

### Event Attribute XCL_010

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_010\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_010\", \"XCL_015\", \"XCL_016\" FROM event WHERE DATE(SUBSTRING(\"XCL_012\", 1, 10)) BETWEEN '2019-11-01' AND '2020-03-31'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_010\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_010\" AS \"value\" FROM event AS \"r0\" WHERE DATE(SUBSTRING(\"r0\".\"XCL_012\", 1, 10)) BETWEEN '2019-11-01' AND '2020-03-31'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1443"
  ]
}
```

### "member"."XCL_035" = 'Casey' AND "member"."XCL_036" = 'Mason'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_035\" = 'Casey' AND \"member\".\"XCL_036\" = 'Mason'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_025\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_035\" = 'Casey' AND T1.\"XCL_036\" = 'Mason'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1372"
  ]
}
```

### COUNT("attendance"."XCL_001") > 10

```json
{
  "kind": "predicate",
  "formula": "COUNT(\"attendance\".\"XCL_001\") > 10",
  "grain": [
    "\"event\".\"XCL_010\""
  ],
  "population_scope": "SELECT T1.\"XCL_011\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" GROUP BY T1.\"XCL_010\" HAVING COUNT(T2.\"XCL_001\") > 10",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1322"
  ]
}
```

### Member Identifier

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_036\" FROM attendance AS T1 INNER JOIN event AS T2 ON T2.\"XCL_010\" = T1.\"XCL_001\" INNER JOIN member AS T3 ON T1.\"XCL_002\" = T3.\"XCL_034\" WHERE T2.\"XCL_011\" = 'Women''s Soccer' AND T3.\"XCL_038\" = 'Member'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "attendance"
      },
      {
        "role": "r1",
        "physical_table": "event"
      },
      {
        "role": "r2",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_036\" AS \"value\" FROM attendance AS \"r0\" INNER JOIN event AS \"r1\" ON \"r1\".\"XCL_010\" = \"r0\".\"XCL_001\" INNER JOIN member AS \"r2\" ON \"r0\".\"XCL_002\" = \"r2\".\"XCL_034\" WHERE \"r1\".\"XCL_011\" = 'Women''s Soccer' AND \"r2\".\"XCL_038\" = 'Member'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1431"
  ]
}
```

### Average XCL_005 for Closed Food Budgets

```json
{
  "kind": "metric",
  "formula": "SUM(\"budget\".\"XCL_005\") / COUNT(\"budget\".\"XCL_005\")",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_005\") / COUNT(\"XCL_005\") FROM budget WHERE \"XCL_004\" = 'Food' AND \"XCL_008\" = 'Closed'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r0\".\"XCL_005\") / COUNT(\"r0\".\"XCL_005\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "budget"
      }
    ],
    "scope_sql": "SELECT SUM(\"r0\".\"XCL_005\") / COUNT(\"r0\".\"XCL_005\") AS \"value\" FROM budget AS \"r0\" WHERE \"r0\".\"XCL_004\" = 'Food' AND \"r0\".\"XCL_008\" = 'Closed'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1397"
  ]
}
```

### "member"."XCL_038" = 'President'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_038\" = 'President'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_045\", T2.\"XCL_047\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_038\" = 'President'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1333"
  ]
}
```

### "member"."XCL_035" = 'Maya' AND "member"."XCL_036" = 'Mclean'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_035\" = 'Maya' AND \"member\".\"XCL_036\" = 'Mclean'",
  "grain": [],
  "population_scope": "SELECT CASE WHEN T3.\"XCL_011\" = 'Women''s Soccer' THEN 'YES' END AS result FROM member AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_034\" = T2.\"XCL_002\" INNER JOIN event AS T3 ON T2.\"XCL_001\" = T3.\"XCL_010\" WHERE T1.\"XCL_035\" = 'Maya' AND T1.\"XCL_036\" = 'Mclean'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1399"
  ]
}
```

### Major Attribute XCL_031

```json
{
  "kind": "binding",
  "formula": "\"major\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_031\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_035\" = 'Brent' AND T1.\"XCL_036\" = 'Thomason'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_031\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_031\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r0\".\"XCL_042\" = \"r1\".\"XCL_030\" WHERE \"r0\".\"XCL_035\" = 'Brent' AND \"r0\".\"XCL_036\" = 'Thomason'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1351"
  ]
}
```

### Income Attribute XCL_026

```json
{
  "kind": "binding",
  "formula": "\"income\".\"XCL_026\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_026\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_035\" = 'Grant' AND T1.\"XCL_036\" = 'Gilmour'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_026\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "income"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_026\" AS \"value\" FROM member AS \"r0\" INNER JOIN income AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_029\" WHERE \"r0\".\"XCL_035\" = 'Grant' AND \"r0\".\"XCL_036\" = 'Gilmour'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1384"
  ]
}
```

### "member"."XCL_035" = 'Phillip' AND "member"."XCL_036" = 'Cullen'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_035\" = 'Phillip' AND \"member\".\"XCL_036\" = 'Cullen'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_031\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" WHERE T2.\"XCL_035\" = 'Phillip' AND T2.\"XCL_036\" = 'Cullen'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1414"
  ]
}
```

### "major"."XCL_033" = 'College of Engineering'

```json
{
  "kind": "predicate",
  "formula": "\"major\".\"XCL_033\" = 'College of Engineering'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_034\") FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T2.\"XCL_033\" = 'College of Engineering'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1313"
  ]
}
```

### COUNT("attendance"."XCL_001") > 20

```json
{
  "kind": "predicate",
  "formula": "COUNT(\"attendance\".\"XCL_001\") > 20",
  "grain": [
    "\"event\".\"XCL_010\""
  ],
  "population_scope": "SELECT T1.\"XCL_011\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" GROUP BY T1.\"XCL_010\" HAVING COUNT(T2.\"XCL_001\") > 20",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1323"
  ]
}
```

### "event"."XCL_011" = 'Community Theater' AND SUBSTRING("event"."XCL_012", 1, 4) = '2019'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'Community Theater' AND SUBSTRING(\"event\".\"XCL_012\", 1, 4) = '2019'",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_002\") FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" WHERE T1.\"XCL_011\" = 'Community Theater' AND SUBSTRING(T1.\"XCL_012\", 1, 4) = '2019'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1395"
  ]
}
```

### "income"."XCL_026" = 50

```json
{
  "kind": "predicate",
  "formula": "\"income\".\"XCL_026\" = 50",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_024\") FROM income WHERE \"XCL_026\" = 50",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1423"
  ]
}
```

### "member"."XCL_038" = 'Vice President'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_038\" = 'Vice President'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_031\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_038\" = 'Vice President'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1354"
  ]
}
```

### Major Attribute XCL_033

```json
{
  "kind": "binding",
  "formula": "\"major\".\"XCL_033\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_033\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_035\" = 'Tyler' AND T1.\"XCL_036\" = 'Hewitt'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_033\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_033\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r0\".\"XCL_042\" = \"r1\".\"XCL_030\" WHERE \"r0\".\"XCL_035\" = 'Tyler' AND \"r0\".\"XCL_036\" = 'Hewitt'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1330"
  ]
}
```

### Expense Attribute XCL_018

```json
{
  "kind": "binding",
  "formula": "\"expense\".\"XCL_018\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_018\" FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T1.\"XCL_035\" = 'Sacha' AND T1.\"XCL_036\" = 'Harrison'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_018\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_018\" AS \"value\" FROM member AS \"r0\" INNER JOIN expense AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_022\" WHERE \"r0\".\"XCL_035\" = 'Sacha' AND \"r0\".\"XCL_036\" = 'Harrison'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1411"
  ]
}
```

### Maximum XCL_005

```json
{
  "kind": "metric",
  "formula": "MAX(\"budget\".\"XCL_005\")",
  "grain": [],
  "population_scope": "SELECT MAX(\"XCL_005\") FROM budget",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MAX(\"r0\".\"XCL_005\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "budget"
      }
    ],
    "scope_sql": "SELECT MAX(\"r0\".\"XCL_005\") AS \"value\" FROM budget AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1378"
  ]
}
```

### Aggregated sum of the XCL_020 column from the expense table, filtered to records where XCL_019 equals '2019-08-20'. Returns a single scalar value repr

```json
{
  "kind": "metric",
  "formula": "SUM(\"expense\".\"XCL_020\")",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_020\") FROM expense WHERE \"XCL_019\" = '2019-08-20'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r0\".\"XCL_020\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT SUM(\"r0\".\"XCL_020\") AS \"value\" FROM expense AS \"r0\" WHERE \"r0\".\"XCL_019\" = '2019-08-20'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1409"
  ]
}
```

### Identifier from the member table (XCL_036) for records where the member type (XCL_038) is 'Member' and the associated major is 'Environmental Engineer

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_036\", T1.\"XCL_032\", T1.\"XCL_033\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" WHERE T2.\"XCL_038\" = 'Member' AND T1.\"XCL_031\" = 'Environmental Engineering'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "major"
      },
      {
        "role": "r1",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_036\" AS \"value\" FROM major AS \"r0\" INNER JOIN member AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_042\" WHERE \"r1\".\"XCL_038\" = 'Member' AND \"r0\".\"XCL_031\" = 'Environmental Engineering'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1426"
  ]
}
```

### Aggregated sum of the XCL_020 column from the expense table, filtered to rows where XCL_018 equals 'Parking'. Represents the total amount for parking-

```json
{
  "kind": "metric",
  "formula": "SUM(\"expense\".\"XCL_020\")",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_020\") FROM expense WHERE \"XCL_018\" = 'Parking'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r0\".\"XCL_020\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT SUM(\"r0\".\"XCL_020\") AS \"value\" FROM expense AS \"r0\" WHERE \"r0\".\"XCL_018\" = 'Parking'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1408"
  ]
}
```

### Distinct value of member column XCL_035 for members who attended an event and have an income record dated '2019-09-09'.

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_035\", T3.\"XCL_036\", T4.\"XCL_026\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" INNER JOIN member AS T3 ON T3.\"XCL_034\" = T2.\"XCL_002\" INNER JOIN income AS T4 ON T4.\"XCL_029\" = T3.\"XCL_034\" WHERE T4.\"XCL_025\" = '2019-09-09'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1464"
  ]
}
```

### "member"."XCL_035" = 'Garrett' AND "member"."XCL_036" = 'Gerke'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_035\" = 'Garrett' AND \"member\".\"XCL_036\" = 'Gerke'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_045\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T2.\"XCL_043\" = T1.\"XCL_041\" WHERE T1.\"XCL_035\" = 'Garrett' AND T1.\"XCL_036\" = 'Gerke'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1468"
  ]
}
```

### "major"."XCL_031" = 'Business' AND "member"."XCL_039" = 'Medium'

```json
{
  "kind": "predicate",
  "formula": "\"major\".\"XCL_031\" = 'Business' AND \"member\".\"XCL_039\" = 'Medium'",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_034\") FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" WHERE T1.\"XCL_031\" = 'Business' AND T2.\"XCL_039\" = 'Medium'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1416"
  ]
}
```

### Budget Attribute XCL_007

```json
{
  "kind": "binding",
  "formula": "\"budget\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_004\", T2.\"XCL_007\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_011\" = 'January Speaker'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_007\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_007\" AS \"value\" FROM event AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" WHERE \"r0\".\"XCL_011\" = 'January Speaker'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1462"
  ]
}
```

### Member Attribute XCL_035

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\", T1.\"XCL_038\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T2.\"XCL_043\" = T1.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Lincolnton' AND T2.\"XCL_047\" = 'North Carolina' AND T2.\"XCL_043\" = 28092",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_035\" AS \"value\" FROM member AS \"r0\" INNER JOIN zip_code AS \"r1\" ON \"r1\".\"XCL_043\" = \"r0\".\"XCL_041\" WHERE \"r1\".\"XCL_045\" = 'Lincolnton' AND \"r1\".\"XCL_047\" = 'North Carolina' AND \"r1\".\"XCL_043\" = 28092",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1469"
  ]
}
```

### "event"."XCL_011" = 'November Meeting' AND "budget"."XCL_006" < 0

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'November Meeting' AND \"budget\".\"XCL_006\" < 0",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_010\") FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = 'November Meeting' AND T1.\"XCL_006\" < 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1348"
  ]
}
```

### Member Attribute XCL_036

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T2.\"XCL_026\" > 40",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "income"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_036\" AS \"value\" FROM member AS \"r0\" INNER JOIN income AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_029\" WHERE \"r1\".\"XCL_026\" > 40",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1385"
  ]
}
```

### "member"."XCL_035" = 'Connor' AND "member"."XCL_036" = 'Hilton' AND "income"."XCL_027" = 'Dues'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_035\" = 'Connor' AND \"member\".\"XCL_036\" = 'Hilton' AND \"income\".\"XCL_027\" = 'Dues'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_025\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_035\" = 'Connor' AND T1.\"XCL_036\" = 'Hilton' AND T2.\"XCL_027\" = 'Dues'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1357"
  ]
}
```

### "event"."XCL_011" = 'Community Theater' AND "major"."XCL_031" = 'Interior Design'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'Community Theater' AND \"major\".\"XCL_031\" = 'Interior Design'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_035\", T2.\"XCL_036\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" INNER JOIN attendance AS T3 ON T2.\"XCL_034\" = T3.\"XCL_002\" INNER JOIN event AS T4 ON T3.\"XCL_001\" = T4.\"XCL_010\" WHERE T4.\"XCL_011\" = 'Community Theater' AND T1.\"XCL_031\" = 'Interior Design'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1382"
  ]
}
```

### The sum of the `XCL_007` column from the `budget` table. This metric aggregates budget values for each `XCL_004` group, restricted to events where `XC

```json
{
  "kind": "metric",
  "formula": "SUM(\"budget\".\"XCL_007\")",
  "grain": [
    "\"budget\".\"XCL_004\""
  ],
  "population_scope": "SELECT T2.\"XCL_004\", SUM(T2.\"XCL_007\") FROM event AS T1 JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_011\" = 'April Speaker' GROUP BY T2.\"XCL_004\" ORDER BY SUM(T2.\"XCL_007\") ASC",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r1\".\"XCL_007\")",
    "grain": [
      "\"r1\".\"XCL_004\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_004\" AS \"grain_0\", SUM(\"r1\".\"XCL_007\") AS \"value\" FROM event AS \"r0\" JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" WHERE \"r0\".\"XCL_011\" = 'April Speaker' GROUP BY \"r1\".\"XCL_004\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1405"
  ]
}
```

### "member"."XCL_038" = 'Secretary'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_038\" = 'Secretary'",
  "grain": [],
  "population_scope": "SELECT \"XCL_035\", \"XCL_036\", \"XCL_037\" FROM member WHERE \"XCL_038\" = 'Secretary'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1393"
  ]
}
```

### Expense Attribute XCL_018

```json
{
  "kind": "binding",
  "formula": "\"expense\".\"XCL_018\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_018\" FROM budget AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_003\" = T2.\"XCL_023\" ORDER BY T1.\"XCL_006\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1365"
  ]
}
```

### Member Identifier XCL_035

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_035\", T2.\"XCL_036\", T1.\"XCL_020\" FROM expense AS T1 INNER JOIN member AS T2 ON T1.\"XCL_022\" = T2.\"XCL_034\" WHERE T1.\"XCL_018\" = 'Water, Veggie tray, supplies'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "expense"
      },
      {
        "role": "r1",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_035\" AS \"value\" FROM expense AS \"r0\" INNER JOIN member AS \"r1\" ON \"r0\".\"XCL_022\" = \"r1\".\"XCL_034\" WHERE \"r0\".\"XCL_018\" = 'Water, Veggie tray, supplies'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1460"
  ]
}
```

### High-attendance event identifier

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_011\"",
  "grain": [
    "\"event\".\"XCL_010\""
  ],
  "population_scope": "SELECT T1.\"XCL_011\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" GROUP BY T1.\"XCL_010\" HAVING COUNT(T2.\"XCL_001\") > 20",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_011\"",
    "grain": [
      "\"r0\".\"XCL_010\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "attendance"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_010\" AS \"grain_0\", \"r0\".\"XCL_011\" AS \"value\" FROM event AS \"r0\" INNER JOIN attendance AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_001\" GROUP BY \"r0\".\"XCL_010\" HAVING COUNT(\"r1\".\"XCL_001\") > 20",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1323"
  ]
}
```

### Member Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"member\".\"XCL_034\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_034\") FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T2.\"XCL_031\" = 'Environmental Engineering'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_034\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_034\") AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r0\".\"XCL_042\" = \"r1\".\"XCL_030\" WHERE \"r1\".\"XCL_031\" = 'Environmental Engineering'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1326"
  ]
}
```

### "event"."XCL_013" = 'Game' AND DATE(SUBSTRING("event"."XCL_012", 1, 10)) BETWEEN '2019-03-15' AND '2020-03-20' AND "event"."XCL_016" = 'Closed'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_013\" = 'Game' AND DATE(SUBSTRING(\"event\".\"XCL_012\", 1, 10)) BETWEEN '2019-03-15' AND '2020-03-20' AND \"event\".\"XCL_016\" = 'Closed'",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_011\" FROM event WHERE \"XCL_013\" = 'Game' AND DATE(SUBSTRING(\"XCL_012\", 1, 10)) BETWEEN '2019-03-15' AND '2020-03-20' AND \"XCL_016\" = 'Closed'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1435"
  ]
}
```

### Member Attribute XCL_035

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_035\", T3.\"XCL_036\" FROM expense AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_023\" = T2.\"XCL_003\" INNER JOIN member AS T3 ON T1.\"XCL_022\" = T3.\"XCL_034\" ORDER BY T2.\"XCL_005\" DESC LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1456"
  ]
}
```

### Aggregates the count of member records (XCL_034) joined to major records where the major type (XCL_031) is 'Business' and the member attribute (XCL_03

```json
{
  "kind": "metric",
  "formula": "COUNT(\"member\".\"XCL_034\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_034\") FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" WHERE T1.\"XCL_031\" = 'Business' AND T2.\"XCL_039\" = 'Medium'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_034\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "major"
      },
      {
        "role": "r1",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_034\") AS \"value\" FROM major AS \"r0\" INNER JOIN member AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_042\" WHERE \"r0\".\"XCL_031\" = 'Business' AND \"r1\".\"XCL_039\" = 'Medium'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1416"
  ]
}
```

### A distinct member attribute (XCL_036) for members associated with expenses that exceed the global average expense amount. The grain is unique combinat

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_035\", T3.\"XCL_036\", T3.\"XCL_040\" FROM expense AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_023\" = T2.\"XCL_003\" INNER JOIN member AS T3 ON T3.\"XCL_034\" = T1.\"XCL_022\" WHERE T1.\"XCL_020\" > (SELECT AVG(T1.\"XCL_020\") FROM expense AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_023\" = T2.\"XCL_003\" INNER JOIN member AS T3 ON T3.\"XCL_034\" = T1.\"XCL_022\")",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1457"
  ]
}
```

### Distinct value of column XCL_031 from the major table, representing the major associated with members who have qualifying expenses.

```json
{
  "kind": "binding",
  "formula": "\"major\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_035\", T1.\"XCL_036\", T2.\"XCL_031\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" INNER JOIN expense AS T3 ON T1.\"XCL_034\" = T3.\"XCL_022\" WHERE T3.\"XCL_020\" > 100",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1449"
  ]
}
```

### Expense Attribute XCL_021

```json
{
  "kind": "binding",
  "formula": "\"expense\".\"XCL_021\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_021\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" WHERE T1.\"XCL_011\" = 'October Meeting' AND T1.\"XCL_012\" LIKE '2019-10-08%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_021\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      },
      {
        "role": "r2",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_021\" AS \"value\" FROM event AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" INNER JOIN expense AS \"r2\" ON \"r1\".\"XCL_003\" = \"r2\".\"XCL_023\" WHERE \"r0\".\"XCL_011\" = 'October Meeting' AND \"r0\".\"XCL_012\" LIKE '2019-10-08%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1338"
  ]
}
```

### "major"."XCL_032" = 'School of Applied Sciences, Technology and Education' AND "major"."XCL_033" = 'College of Agriculture and Applied Sciences'

```json
{
  "kind": "predicate",
  "formula": "\"major\".\"XCL_032\" = 'School of Applied Sciences, Technology and Education' AND \"major\".\"XCL_033\" = 'College of Agriculture and Applied Sciences'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_030\") FROM major WHERE \"XCL_032\" = 'School of Applied Sciences, Technology and Education' AND \"XCL_033\" = 'College of Agriculture and Applied Sciences'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1425"
  ]
}
```

### Most Frequent Member Attribute

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_039\"",
  "grain": [
    "\"member\".\"XCL_039\""
  ],
  "population_scope": "SELECT \"XCL_039\" FROM member GROUP BY \"XCL_039\" ORDER BY COUNT(\"XCL_039\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1402"
  ]
}
```

### Member Attribute XCL_036

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\", SUM(T2.\"XCL_020\") FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T1.\"XCL_034\" = 'rec4BLdZHS2Blfp4v'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1410"
  ]
}
```

### "event"."XCL_011" = 'September Speaker' AND "expense"."XCL_018" = 'Posters'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'September Speaker' AND \"expense\".\"XCL_018\" = 'Posters'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_020\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" WHERE T1.\"XCL_011\" = 'September Speaker' AND T3.\"XCL_018\" = 'Posters'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1401"
  ]
}
```

### Member Identifier

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_035\", T2.\"XCL_036\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" INNER JOIN attendance AS T3 ON T2.\"XCL_034\" = T3.\"XCL_002\" INNER JOIN event AS T4 ON T3.\"XCL_001\" = T4.\"XCL_010\" WHERE T4.\"XCL_011\" = 'Community Theater' AND T1.\"XCL_031\" = 'Interior Design'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "major"
      },
      {
        "role": "r1",
        "physical_table": "member"
      },
      {
        "role": "r2",
        "physical_table": "attendance"
      },
      {
        "role": "r3",
        "physical_table": "event"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_035\" AS \"value\" FROM major AS \"r0\" INNER JOIN member AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_042\" INNER JOIN attendance AS \"r2\" ON \"r1\".\"XCL_034\" = \"r2\".\"XCL_002\" INNER JOIN event AS \"r3\" ON \"r2\".\"XCL_001\" = \"r3\".\"XCL_010\" WHERE \"r3\".\"XCL_011\" = 'Community Theater' AND \"r0\".\"XCL_031\" = 'Interior Design'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1382"
  ]
}
```

### "zip_code"."XCL_044" = 'PO Box' AND NOT "zip_code"."XCL_046" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"zip_code\".\"XCL_044\" = 'PO Box' AND NOT \"zip_code\".\"XCL_046\" IS NULL",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_046\" FROM zip_code WHERE \"XCL_044\" = 'PO Box' AND NOT \"XCL_046\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1433"
  ]
}
```

### Identifier field from the member table (T4) for members associated with expenses in the 'Yearly Kickoff' event. Grain: one row per matching member-exp

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T4.\"XCL_035\", T4.\"XCL_036\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" INNER JOIN member AS T4 ON T3.\"XCL_022\" = T4.\"XCL_034\" WHERE T1.\"XCL_011\" = 'Yearly Kickoff'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r3\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      },
      {
        "role": "r2",
        "physical_table": "expense"
      },
      {
        "role": "r3",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r3\".\"XCL_035\" AS \"value\" FROM event AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" INNER JOIN expense AS \"r2\" ON \"r1\".\"XCL_003\" = \"r2\".\"XCL_023\" INNER JOIN member AS \"r3\" ON \"r2\".\"XCL_022\" = \"r3\".\"XCL_034\" WHERE \"r0\".\"XCL_011\" = 'Yearly Kickoff'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1387"
  ]
}
```

### Distinct Event Identifier

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_011\" FROM event WHERE \"XCL_013\" = 'Game' AND DATE(SUBSTRING(\"XCL_012\", 1, 10)) BETWEEN '2019-03-15' AND '2020-03-20' AND \"XCL_016\" = 'Closed'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1435"
  ]
}
```

### Member Identifier

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_038\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" WHERE T1.\"XCL_031\" = 'Business'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_038\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "major"
      },
      {
        "role": "r1",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_038\" AS \"value\" FROM major AS \"r0\" INNER JOIN member AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_042\" WHERE \"r0\".\"XCL_031\" = 'Business'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1415"
  ]
}
```

### A distinct member attribute (XCL_035) for members associated with expenses that exceed the global average expense amount. The grain is unique combinat

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_035\", T3.\"XCL_036\", T3.\"XCL_040\" FROM expense AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_023\" = T2.\"XCL_003\" INNER JOIN member AS T3 ON T3.\"XCL_034\" = T1.\"XCL_022\" WHERE T1.\"XCL_020\" > (SELECT AVG(T1.\"XCL_020\") FROM expense AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_023\" = T2.\"XCL_003\" INNER JOIN member AS T3 ON T3.\"XCL_034\" = T1.\"XCL_022\")",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1457"
  ]
}
```

### "event"."XCL_011" = 'April Speaker'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'April Speaker'",
  "grain": [
    "\"budget\".\"XCL_004\""
  ],
  "population_scope": "SELECT T2.\"XCL_004\", SUM(T2.\"XCL_007\") FROM event AS T1 JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_011\" = 'April Speaker' GROUP BY T2.\"XCL_004\" ORDER BY SUM(T2.\"XCL_007\") ASC",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1405"
  ]
}
```

### Count of major records (identified by XCL_031) filtered to those belonging to the 'College of Humanities and Social Sciences' (XCL_033). Returns a sin

```json
{
  "kind": "metric",
  "formula": "COUNT(\"major\".\"XCL_031\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_031\") FROM major WHERE \"XCL_033\" = 'College of Humanities and Social Sciences'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_031\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_031\") AS \"value\" FROM major AS \"r0\" WHERE \"r0\".\"XCL_033\" = 'College of Humanities and Social Sciences'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1345"
  ]
}
```

### Event Identifier

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" FROM budget AS T1 INNER JOIN event AS T2 ON T2.\"XCL_010\" = T1.\"XCL_009\" WHERE T1.\"XCL_008\" = 'Closed' AND T1.\"XCL_006\" < 0 ORDER BY T1.\"XCL_006\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1403"
  ]
}
```

### "major"."XCL_031" = 'Physics Teaching'

```json
{
  "kind": "predicate",
  "formula": "\"major\".\"XCL_031\" = 'Physics Teaching'",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_034\") FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" WHERE T1.\"XCL_031\" = 'Physics Teaching'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1394"
  ]
}
```

### "expense"."XCL_020" < 50

```json
{
  "kind": "predicate",
  "formula": "\"expense\".\"XCL_020\" < 50",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_041\" FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T2.\"XCL_020\" < 50",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1413"
  ]
}
```

### Count of Women's Soccer Event Attendance Records

```json
{
  "kind": "metric",
  "formula": "COUNT(\"event\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_010\") FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" WHERE T1.\"XCL_011\" = 'Women''s Soccer'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "attendance"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_010\") AS \"value\" FROM event AS \"r0\" INNER JOIN attendance AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_001\" WHERE \"r0\".\"XCL_011\" = 'Women''s Soccer'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1315"
  ]
}
```

### 2019 vs 2020 Budget Difference

```json
{
  "kind": "metric",
  "formula": "SUM(CASE WHEN SUBSTRING(\"event\".\"XCL_012\", 1, 4) = '2019' THEN \"budget\".\"XCL_005\" ELSE 0 END) - SUM(CASE WHEN SUBSTRING(\"event\".\"XCL_012\", 1, 4) = '2020' THEN \"budget\".\"XCL_005\" ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN SUBSTRING(T1.\"XCL_012\", 1, 4) = '2019' THEN T2.\"XCL_005\" ELSE 0 END) - SUM(CASE WHEN SUBSTRING(T1.\"XCL_012\", 1, 4) = '2020' THEN T2.\"XCL_005\" ELSE 0 END) AS num FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(CASE WHEN SUBSTRING(\"r0\".\"XCL_012\", 1, 4) = '2019' THEN \"r1\".\"XCL_005\" ELSE 0 END) - SUM(CASE WHEN SUBSTRING(\"r0\".\"XCL_012\", 1, 4) = '2020' THEN \"r1\".\"XCL_005\" ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      }
    ],
    "scope_sql": "SELECT SUM(CASE WHEN SUBSTRING(\"r0\".\"XCL_012\", 1, 4) = '2019' THEN \"r1\".\"XCL_005\" ELSE 0 END) - SUM(CASE WHEN SUBSTRING(\"r0\".\"XCL_012\", 1, 4) = '2020' THEN \"r1\".\"XCL_005\" ELSE 0 END) AS \"value\" FROM event AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1340"
  ]
}
```

### "expense"."XCL_018" = 'Water, chips, cookies'

```json
{
  "kind": "predicate",
  "formula": "\"expense\".\"XCL_018\" = 'Water, chips, cookies'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM expense AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_023\" = T2.\"XCL_003\" WHERE T1.\"XCL_018\" = 'Water, chips, cookies' ORDER BY T1.\"XCL_020\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1455"
  ]
}
```

### The value of the event identifier column (XCL_011) for the single event with the highest number of associated attendance records. The grain is one row

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_011\"",
  "grain": [
    "\"event\".\"XCL_011\""
  ],
  "population_scope": "SELECT T1.\"XCL_011\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" GROUP BY T1.\"XCL_011\" ORDER BY COUNT(T2.\"XCL_001\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1318"
  ]
}
```

### Member Identifier XCL_036

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T2.\"XCL_045\" = 'Georgetown' AND T2.\"XCL_047\" = 'South Carolina'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_036\" AS \"value\" FROM member AS \"r0\" INNER JOIN zip_code AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_043\" WHERE \"r1\".\"XCL_045\" = 'Georgetown' AND \"r1\".\"XCL_047\" = 'South Carolina'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1383"
  ]
}
```

### Counts the number of member records (identified by XCL_034) associated with zip codes in Maryland. The population is limited to members linked via the

```json
{
  "kind": "metric",
  "formula": "COUNT(\"member\".\"XCL_034\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_034\") FROM zip_code AS T1 INNER JOIN member AS T2 ON T1.\"XCL_043\" = T2.\"XCL_041\" WHERE T1.\"XCL_047\" = 'Maryland'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_034\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "zip_code"
      },
      {
        "role": "r1",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_034\") AS \"value\" FROM zip_code AS \"r0\" INNER JOIN member AS \"r1\" ON \"r0\".\"XCL_043\" = \"r1\".\"XCL_041\" WHERE \"r0\".\"XCL_047\" = 'Maryland'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1373"
  ]
}
```

### Income Attribute XCL_026

```json
{
  "kind": "binding",
  "formula": "\"income\".\"XCL_026\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_026\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_038\" = 'Vice President'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_026\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "income"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_026\" AS \"value\" FROM member AS \"r0\" INNER JOIN income AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_029\" WHERE \"r0\".\"XCL_038\" = 'Vice President'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1331"
  ]
}
```

### Aggregated sum of the expense amount (XCL_020) for all expenses linked to budgets associated with the 'Yearly Kickoff' event. The grain is a single sc

```json
{
  "kind": "metric",
  "formula": "SUM(\"expense\".\"XCL_020\")",
  "grain": [],
  "population_scope": "SELECT SUM(T3.\"XCL_020\") FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" WHERE T1.\"XCL_011\" = 'Yearly Kickoff'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r2\".\"XCL_020\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      },
      {
        "role": "r2",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT SUM(\"r2\".\"XCL_020\") AS \"value\" FROM event AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" INNER JOIN expense AS \"r2\" ON \"r1\".\"XCL_003\" = \"r2\".\"XCL_023\" WHERE \"r0\".\"XCL_011\" = 'Yearly Kickoff'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1386"
  ]
}
```

### Event Identifier

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_011\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" INNER JOIN member AS T3 ON T2.\"XCL_002\" = T3.\"XCL_034\" WHERE T3.\"XCL_035\" = 'Maya' AND T3.\"XCL_036\" = 'Mclean'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_011\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "attendance"
      },
      {
        "role": "r2",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_011\" AS \"value\" FROM event AS \"r0\" INNER JOIN attendance AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_001\" INNER JOIN member AS \"r2\" ON \"r1\".\"XCL_002\" = \"r2\".\"XCL_034\" WHERE \"r2\".\"XCL_035\" = 'Maya' AND \"r2\".\"XCL_036\" = 'Mclean'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1320"
  ]
}
```

### Major Attribute XCL_031

```json
{
  "kind": "binding",
  "formula": "\"major\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_031\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_035\" = 'Angela' AND T1.\"XCL_036\" = 'Sanders'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_031\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_031\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r0\".\"XCL_042\" = \"r1\".\"XCL_030\" WHERE \"r0\".\"XCL_035\" = 'Angela' AND \"r0\".\"XCL_036\" = 'Sanders'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1312"
  ]
}
```

### "event"."XCL_016" = 'Closed'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_016\" = 'Closed'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T2.\"XCL_016\" = 'Closed' ORDER BY T1.\"XCL_005\" / T1.\"XCL_007\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1376"
  ]
}
```

### Expense Identifier

```json
{
  "kind": "binding",
  "formula": "\"expense\".\"XCL_020\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_020\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" WHERE T1.\"XCL_011\" = 'September Speaker' AND T3.\"XCL_018\" = 'Posters'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_020\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      },
      {
        "role": "r2",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_020\" AS \"value\" FROM event AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" INNER JOIN expense AS \"r2\" ON \"r1\".\"XCL_003\" = \"r2\".\"XCL_023\" WHERE \"r0\".\"XCL_011\" = 'September Speaker' AND \"r2\".\"XCL_018\" = 'Posters'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1401"
  ]
}
```

### Event Attribute XCL_016

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_016\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_010\", \"XCL_015\", \"XCL_016\" FROM event WHERE DATE(SUBSTRING(\"XCL_012\", 1, 10)) BETWEEN '2019-11-01' AND '2020-03-31'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_016\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_016\" AS \"value\" FROM event AS \"r0\" WHERE DATE(SUBSTRING(\"r0\".\"XCL_012\", 1, 10)) BETWEEN '2019-11-01' AND '2020-03-31'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1443"
  ]
}
```

### "budget"."XCL_004" = 'Food'

```json
{
  "kind": "predicate",
  "formula": "\"budget\".\"XCL_004\" = 'Food'",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_005\") FROM budget WHERE \"XCL_004\" = 'Food'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1380"
  ]
}
```

### "expense"."XCL_018" = 'Water, Veggie tray, supplies'

```json
{
  "kind": "predicate",
  "formula": "\"expense\".\"XCL_018\" = 'Water, Veggie tray, supplies'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_035\", T2.\"XCL_036\", T1.\"XCL_020\" FROM expense AS T1 INNER JOIN member AS T2 ON T1.\"XCL_022\" = T2.\"XCL_034\" WHERE T1.\"XCL_018\" = 'Water, Veggie tray, supplies'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1460"
  ]
}
```

### "budget"."XCL_004" = 'Speaker Gifts'

```json
{
  "kind": "predicate",
  "formula": "\"budget\".\"XCL_004\" = 'Speaker Gifts'",
  "grain": [
    "\"event\".\"XCL_011\""
  ],
  "population_scope": "SELECT SUM(T1.\"XCL_005\"), T2.\"XCL_011\" FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T1.\"XCL_004\" = 'Speaker Gifts' GROUP BY T2.\"XCL_011\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1467"
  ]
}
```

### "expense"."XCL_020" > 100

```json
{
  "kind": "predicate",
  "formula": "\"expense\".\"XCL_020\" > 100",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_035\", T1.\"XCL_036\", T2.\"XCL_031\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" INNER JOIN expense AS T3 ON T1.\"XCL_034\" = T3.\"XCL_022\" WHERE T3.\"XCL_020\" > 100",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1449"
  ]
}
```

### The value of column XCL_047 from the zip_code table, retrieved for members matching specific name criteria.

```json
{
  "kind": "binding",
  "formula": "\"zip_code\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_047\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_035\" = 'Sacha' AND T1.\"XCL_036\" = 'Harrison'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_047\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_047\" AS \"value\" FROM member AS \"r0\" INNER JOIN zip_code AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_043\" WHERE \"r0\".\"XCL_035\" = 'Sacha' AND \"r0\".\"XCL_036\" = 'Harrison'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1355"
  ]
}
```

### Count of zip code records (identified by column XCL_045) filtered to those where XCL_046 equals 'Orange County' and XCL_047 equals 'Virginia'. Returns

```json
{
  "kind": "metric",
  "formula": "COUNT(\"zip_code\".\"XCL_045\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_045\") FROM zip_code WHERE \"XCL_046\" = 'Orange County' AND \"XCL_047\" = 'Virginia'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_045\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_045\") AS \"value\" FROM zip_code AS \"r0\" WHERE \"r0\".\"XCL_046\" = 'Orange County' AND \"r0\".\"XCL_047\" = 'Virginia'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1362"
  ]
}
```

### Event Identifier

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_011\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" WHERE T2.\"XCL_004\" = 'Parking' AND T3.\"XCL_020\" < (SELECT AVG(\"XCL_020\") FROM expense)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1453"
  ]
}
```

### "member"."XCL_038" = 'Secretary'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_038\" = 'Secretary'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\", \"XCL_033\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T1.\"XCL_038\" = 'Secretary'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1466"
  ]
}
```

### Distinct Budget Identifier

```json
{
  "kind": "binding",
  "formula": "\"budget\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_004\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_015\" = 'MU 215'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1422"
  ]
}
```

### Major Attribute XCL_031

```json
{
  "kind": "binding",
  "formula": "\"major\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_031\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_040\" = '809-555-3360'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_031\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_031\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r0\".\"XCL_042\" = \"r1\".\"XCL_030\" WHERE \"r0\".\"XCL_040\" = '809-555-3360'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1368"
  ]
}
```

### Member Identifier

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_041\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_041\" FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T2.\"XCL_020\" < 50",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_041\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_041\" AS \"value\" FROM member AS \"r0\" INNER JOIN expense AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_022\" WHERE \"r1\".\"XCL_020\" < 50",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1413"
  ]
}
```

### "member"."XCL_039" = 'X-Large'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_039\" = 'X-Large'",
  "grain": [],
  "population_scope": "SELECT \"XCL_035\", \"XCL_036\" FROM member WHERE \"XCL_039\" = 'X-Large'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1445"
  ]
}
```

### Member Identifier XCL_036

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_036\", T1.\"XCL_040\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T2.\"XCL_031\" = 'Elementary Education'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_036\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r1\".\"XCL_030\" = \"r0\".\"XCL_042\" WHERE \"r1\".\"XCL_031\" = 'Elementary Education'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1461"
  ]
}
```

### Member Zip Code

```json
{
  "kind": "binding",
  "formula": "\"zip_code\".\"XCL_044\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_044\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_035\" = 'Christof' AND T1.\"XCL_036\" = 'Nielson'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_044\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_044\" AS \"value\" FROM member AS \"r0\" INNER JOIN zip_code AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_043\" WHERE \"r0\".\"XCL_035\" = 'Christof' AND \"r0\".\"XCL_036\" = 'Nielson'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1353"
  ]
}
```

### Event Attribute XCL_011

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_011\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" ORDER BY T3.\"XCL_020\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1389"
  ]
}
```

### Value of column XCL_045 from the zip_code table for members with role 'President'.

```json
{
  "kind": "binding",
  "formula": "\"zip_code\".\"XCL_045\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_045\", T2.\"XCL_047\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_038\" = 'President'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_045\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_045\" AS \"value\" FROM member AS \"r0\" INNER JOIN zip_code AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_043\" WHERE \"r0\".\"XCL_038\" = 'President'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1333"
  ]
}
```

### A scalar ratio metric comparing the total budget amount (XCL_007) for 'Yearly Kickoff' events against the total budget amount for 'October Meeting' ev

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"event\".\"XCL_011\" = 'Yearly Kickoff' THEN \"budget\".\"XCL_007\" ELSE 0 END) AS REAL) / SUM(CASE WHEN \"event\".\"XCL_011\" = 'October Meeting' THEN \"budget\".\"XCL_007\" ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_011\" = 'Yearly Kickoff' THEN T1.\"XCL_007\" ELSE 0 END) AS REAL) / SUM(CASE WHEN T2.\"XCL_011\" = 'October Meeting' THEN T1.\"XCL_007\" ELSE 0 END) FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T1.\"XCL_004\" = 'Advertisement' AND T2.\"XCL_013\" = 'Meeting'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r1\".\"XCL_011\" = 'Yearly Kickoff' THEN \"r0\".\"XCL_007\" ELSE 0 END) AS REAL) / SUM(CASE WHEN \"r1\".\"XCL_011\" = 'October Meeting' THEN \"r0\".\"XCL_007\" ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "budget"
      },
      {
        "role": "r1",
        "physical_table": "event"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r1\".\"XCL_011\" = 'Yearly Kickoff' THEN \"r0\".\"XCL_007\" ELSE 0 END) AS REAL) / SUM(CASE WHEN \"r1\".\"XCL_011\" = 'October Meeting' THEN \"r0\".\"XCL_007\" ELSE 0 END) AS \"value\" FROM budget AS \"r0\" INNER JOIN event AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_010\" WHERE \"r0\".\"XCL_004\" = 'Advertisement' AND \"r1\".\"XCL_013\" = 'Meeting'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1359"
  ]
}
```

### Budget Attribute XCL_004

```json
{
  "kind": "binding",
  "formula": "\"budget\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_004\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_012\" = '2020-03-24T12:00:00'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_004\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_004\" AS \"value\" FROM event AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" WHERE \"r0\".\"XCL_012\" = '2020-03-24T12:00:00'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1419"
  ]
}
```

### Average Expense Amount

```json
{
  "kind": "metric",
  "formula": "AVG(\"expense\".\"XCL_020\")",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_020\") FROM expense AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_023\" = T2.\"XCL_003\" INNER JOIN member AS T3 ON T3.\"XCL_034\" = T1.\"XCL_022\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_020\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "expense"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      },
      {
        "role": "r2",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_020\") AS \"value\" FROM expense AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_023\" = \"r1\".\"XCL_003\" INNER JOIN member AS \"r2\" ON \"r2\".\"XCL_034\" = \"r0\".\"XCL_022\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1457"
  ]
}
```

### "event"."XCL_011" = 'Yearly Kickoff'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'Yearly Kickoff'",
  "grain": [],
  "population_scope": "SELECT SUM(T3.\"XCL_020\") FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" WHERE T1.\"XCL_011\" = 'Yearly Kickoff'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1386"
  ]
}
```

### "budget"."XCL_006" > 0

```json
{
  "kind": "predicate",
  "formula": "\"budget\".\"XCL_006\" > 0",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_011\", T1.\"XCL_015\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T2.\"XCL_006\" > 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1447"
  ]
}
```

### The value of column XCL_006 from the budget table for the row(s) where XCL_004 is 'Food' and XCL_007 equals the maximum XCL_007 for 'Food'.

```json
{
  "kind": "binding",
  "formula": "\"budget\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_006\" FROM budget WHERE \"XCL_004\" = 'Food' AND \"XCL_007\" = (SELECT MAX(\"XCL_007\") FROM budget WHERE \"XCL_004\" = 'Food')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1343"
  ]
}
```

### Event Attribute XCL_011

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_011\", T1.\"XCL_012\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" WHERE T3.\"XCL_018\" = 'Pizza' AND T3.\"XCL_020\" > 50 AND T3.\"XCL_020\" < 100",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_011\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      },
      {
        "role": "r2",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_011\" AS \"value\" FROM event AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" INNER JOIN expense AS \"r2\" ON \"r1\".\"XCL_003\" = \"r2\".\"XCL_023\" WHERE \"r2\".\"XCL_018\" = 'Pizza' AND \"r2\".\"XCL_020\" > 50 AND \"r2\".\"XCL_020\" < 100",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1448"
  ]
}
```

### "member"."XCL_035" = 'Sherri' AND "member"."XCL_036" = 'Ramsey'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_035\" = 'Sherri' AND \"member\".\"XCL_036\" = 'Ramsey'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_046\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_035\" = 'Sherri' AND T1.\"XCL_036\" = 'Ramsey'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1329"
  ]
}
```

### Attendance Record Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"attendance\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T3.\"XCL_001\"), T1.\"XCL_031\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" INNER JOIN attendance AS T3 ON T2.\"XCL_034\" = T3.\"XCL_002\" WHERE T2.\"XCL_035\" = 'Luisa' AND T2.\"XCL_036\" = 'Guidi'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r2\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "major"
      },
      {
        "role": "r1",
        "physical_table": "member"
      },
      {
        "role": "r2",
        "physical_table": "attendance"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r2\".\"XCL_001\") AS \"value\" FROM major AS \"r0\" INNER JOIN member AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_042\" INNER JOIN attendance AS \"r2\" ON \"r1\".\"XCL_034\" = \"r2\".\"XCL_002\" WHERE \"r1\".\"XCL_035\" = 'Luisa' AND \"r1\".\"XCL_036\" = 'Guidi'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1396"
  ]
}
```

### "member"."XCL_035" = 'Sacha' AND "member"."XCL_036" = 'Harrison'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_035\" = 'Sacha' AND \"member\".\"XCL_036\" = 'Harrison'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_018\" FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T1.\"XCL_035\" = 'Sacha' AND T1.\"XCL_036\" = 'Harrison'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1411"
  ]
}
```

### Attendance Record Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"attendance\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_001\") FROM member AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_034\" = T2.\"XCL_002\" WHERE T1.\"XCL_040\" = '954-555-6240'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "attendance"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_001\") AS \"value\" FROM member AS \"r0\" INNER JOIN attendance AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_002\" WHERE \"r0\".\"XCL_040\" = '954-555-6240'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1374"
  ]
}
```

### Grouping Key

```json
{
  "kind": "binding",
  "formula": "\"expense\".\"XCL_018\"",
  "grain": [
    "\"expense\".\"XCL_018\""
  ],
  "population_scope": "SELECT \"XCL_018\" FROM expense GROUP BY \"XCL_018\" HAVING AVG(\"XCL_020\") > 50",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_018\"",
    "grain": [
      "\"r0\".\"XCL_018\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_018\" AS \"grain_0\", \"r0\".\"XCL_018\" AS \"value\" FROM expense AS \"r0\" GROUP BY \"r0\".\"XCL_018\" HAVING AVG(\"r0\".\"XCL_020\") > 50",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1444"
  ]
}
```

### "budget"."XCL_004" = 'Advertisement'

```json
{
  "kind": "predicate",
  "formula": "\"budget\".\"XCL_004\" = 'Advertisement'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T1.\"XCL_004\" = 'Advertisement' ORDER BY T1.\"XCL_005\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1398"
  ]
}
```

### "event"."XCL_012" = '2020-03-24T12:00:00'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_012\" = '2020-03-24T12:00:00'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_004\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_012\" = '2020-03-24T12:00:00'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1419"
  ]
}
```

### The identifier (XCL_034) of the single member with the highest total expense amount (SUM of expense.XCL_020), restricted to members who have expenses 

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_034\"",
  "grain": [
    "\"member\".\"XCL_034\""
  ],
  "population_scope": "SELECT T2.\"XCL_034\" FROM expense AS T1 INNER JOIN member AS T2 ON T1.\"XCL_022\" = T2.\"XCL_034\" INNER JOIN budget AS T3 ON T1.\"XCL_023\" = T3.\"XCL_003\" INNER JOIN event AS T4 ON T3.\"XCL_009\" = T4.\"XCL_010\" GROUP BY T2.\"XCL_034\" HAVING COUNT(DISTINCT T4.\"XCL_010\") > 1 ORDER BY SUM(T1.\"XCL_020\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1451"
  ]
}
```

### Average Attendance Count per Event

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(\"attendance\".\"XCL_001\") AS REAL) / COUNT(DISTINCT \"attendance\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(T2.\"XCL_001\") AS REAL) / COUNT(DISTINCT T2.\"XCL_001\") FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" WHERE SUBSTRING(T1.\"XCL_012\", 1, 4) = '2020' AND T1.\"XCL_013\" = 'Meeting'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(\"r1\".\"XCL_001\") AS REAL) / COUNT(DISTINCT \"r1\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "attendance"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(\"r1\".\"XCL_001\") AS REAL) / COUNT(DISTINCT \"r1\".\"XCL_001\") AS \"value\" FROM event AS \"r0\" INNER JOIN attendance AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_001\" WHERE SUBSTRING(\"r0\".\"XCL_012\", 1, 4) = '2020' AND \"r0\".\"XCL_013\" = 'Meeting'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1324"
  ]
}
```

### Attendance Count for Women's Soccer

```json
{
  "kind": "metric",
  "formula": "COUNT(\"attendance\".\"XCL_002\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_002\") FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" WHERE T1.\"XCL_011\" = 'Women''s Soccer'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_002\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "attendance"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_002\") AS \"value\" FROM event AS \"r0\" INNER JOIN attendance AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_001\" WHERE \"r0\".\"XCL_011\" = 'Women''s Soccer'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1371"
  ]
}
```

### Member Identifier XCL_036

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_035\", T2.\"XCL_036\", T1.\"XCL_020\" FROM expense AS T1 INNER JOIN member AS T2 ON T1.\"XCL_022\" = T2.\"XCL_034\" WHERE T1.\"XCL_018\" = 'Water, Veggie tray, supplies'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "expense"
      },
      {
        "role": "r1",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_036\" AS \"value\" FROM expense AS \"r0\" INNER JOIN member AS \"r1\" ON \"r0\".\"XCL_022\" = \"r1\".\"XCL_034\" WHERE \"r0\".\"XCL_018\" = 'Water, Veggie tray, supplies'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1460"
  ]
}
```

### Value of column XCL_045 from the zip_code table for the member identified by first name 'Amy' and last name 'Firth'.

```json
{
  "kind": "binding",
  "formula": "\"zip_code\".\"XCL_045\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_045\", T2.\"XCL_046\", T2.\"XCL_047\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_035\" = 'Amy' AND T1.\"XCL_036\" = 'Firth'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_045\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_045\" AS \"value\" FROM member AS \"r0\" INNER JOIN zip_code AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_043\" WHERE \"r0\".\"XCL_035\" = 'Amy' AND \"r0\".\"XCL_036\" = 'Firth'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1364"
  ]
}
```

### "zip_code"."XCL_045" = 'Lincolnton' AND "zip_code"."XCL_047" = 'North Carolina' AND "zip_code"."XCL_043" = 28092

```json
{
  "kind": "predicate",
  "formula": "\"zip_code\".\"XCL_045\" = 'Lincolnton' AND \"zip_code\".\"XCL_047\" = 'North Carolina' AND \"zip_code\".\"XCL_043\" = 28092",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\", T1.\"XCL_038\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T2.\"XCL_043\" = T1.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Lincolnton' AND T2.\"XCL_047\" = 'North Carolina' AND T2.\"XCL_043\" = 28092",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1469"
  ]
}
```

### Income Attribute XCL_027

```json
{
  "kind": "binding",
  "formula": "\"income\".\"XCL_027\"",
  "grain": [
    "\"member\".\"XCL_035\"",
    "\"member\".\"XCL_036\"",
    "\"income\".\"XCL_027\""
  ],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\", T2.\"XCL_027\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" GROUP BY T1.\"XCL_035\", T1.\"XCL_036\", T2.\"XCL_027\" ORDER BY SUM(T2.\"XCL_026\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1388"
  ]
}
```

### Expense Attribute XCL_017

```json
{
  "kind": "binding",
  "formula": "\"expense\".\"XCL_017\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_017\", T2.\"XCL_018\" FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T1.\"XCL_038\" = 'Vice President'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_017\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_017\" AS \"value\" FROM member AS \"r0\" INNER JOIN expense AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_022\" WHERE \"r0\".\"XCL_038\" = 'Vice President'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1370"
  ]
}
```

### Member Attribute XCL_037

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_037\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_035\", \"XCL_036\", \"XCL_037\" FROM member WHERE \"XCL_038\" = 'Secretary'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_037\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_037\" AS \"value\" FROM member AS \"r0\" WHERE \"r0\".\"XCL_038\" = 'Secretary'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1393"
  ]
}
```

### "expense"."XCL_018" = 'Pizza'

```json
{
  "kind": "predicate",
  "formula": "\"expense\".\"XCL_018\" = 'Pizza'",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_020\") FROM expense WHERE \"XCL_018\" = 'Pizza'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1361"
  ]
}
```

### "event"."XCL_015" = 'MU 215'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_015\" = 'MU 215'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_004\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_015\" = 'MU 215'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1422"
  ]
}
```

### Attribute field from the member table (T4) for members associated with expenses in the 'Yearly Kickoff' event. Grain: one row per matching member-expe

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T4.\"XCL_035\", T4.\"XCL_036\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" INNER JOIN member AS T4 ON T3.\"XCL_022\" = T4.\"XCL_034\" WHERE T1.\"XCL_011\" = 'Yearly Kickoff'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r3\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      },
      {
        "role": "r2",
        "physical_table": "expense"
      },
      {
        "role": "r3",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r3\".\"XCL_036\" AS \"value\" FROM event AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" INNER JOIN expense AS \"r2\" ON \"r1\".\"XCL_003\" = \"r2\".\"XCL_023\" INNER JOIN member AS \"r3\" ON \"r2\".\"XCL_022\" = \"r3\".\"XCL_034\" WHERE \"r0\".\"XCL_011\" = 'Yearly Kickoff'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1387"
  ]
}
```

### "income"."XCL_026" > 40

```json
{
  "kind": "predicate",
  "formula": "\"income\".\"XCL_026\" > 40",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T2.\"XCL_026\" > 40",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1385"
  ]
}
```

### "income"."XCL_026" > 40

```json
{
  "kind": "predicate",
  "formula": "\"income\".\"XCL_026\" > 40",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_045\", T3.\"XCL_046\" FROM income AS T1 INNER JOIN member AS T2 ON T1.\"XCL_029\" = T2.\"XCL_034\" INNER JOIN zip_code AS T3 ON T3.\"XCL_043\" = T2.\"XCL_041\" WHERE T1.\"XCL_026\" > 40",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1450"
  ]
}
```

### "member"."XCL_035" = 'Garrett' AND "member"."XCL_036" = 'Gerke'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_035\" = 'Garrett' AND \"member\".\"XCL_036\" = 'Gerke'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_031\", T2.\"XCL_032\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T1.\"XCL_035\" = 'Garrett' AND T1.\"XCL_036\" = 'Gerke'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1459"
  ]
}
```

### Member Attribute XCL_035

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_035\", \"XCL_036\", \"XCL_037\" FROM member WHERE \"XCL_038\" = 'Secretary'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_035\" AS \"value\" FROM member AS \"r0\" WHERE \"r0\".\"XCL_038\" = 'Secretary'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1393"
  ]
}
```

### Major Identifier

```json
{
  "kind": "binding",
  "formula": "\"major\".\"XCL_032\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_032\" FROM major WHERE \"XCL_033\" = 'College of Humanities and Social Sciences'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_032\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_032\" AS \"value\" FROM major AS \"r0\" WHERE \"r0\".\"XCL_033\" = 'College of Humanities and Social Sciences'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1363"
  ]
}
```

### "event"."XCL_011" = 'Women''s Soccer' AND "member"."XCL_039" = 'Medium'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'Women''s Soccer' AND \"member\".\"XCL_039\" = 'Medium'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_010\") FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" INNER JOIN member AS T3 ON T2.\"XCL_002\" = T3.\"XCL_034\" WHERE T1.\"XCL_011\" = 'Women''s Soccer' AND T3.\"XCL_039\" = 'Medium'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1317"
  ]
}
```

### "expense"."XCL_018" = 'Posters'

```json
{
  "kind": "predicate",
  "formula": "\"expense\".\"XCL_018\" = 'Posters'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_004\" FROM expense AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_023\" = T2.\"XCL_003\" WHERE T1.\"XCL_018\" = 'Posters'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1465"
  ]
}
```

### "member"."XCL_035" = 'Adela' AND "member"."XCL_036" = 'O''Gallagher'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_035\" = 'Adela' AND \"member\".\"XCL_036\" = 'O''Gallagher'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_046\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_035\" = 'Adela' AND T1.\"XCL_036\" = 'O''Gallagher'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1347"
  ]
}
```

### "event"."XCL_011" = 'Women''s Soccer' AND "member"."XCL_038" = 'Member'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'Women''s Soccer' AND \"member\".\"XCL_038\" = 'Member'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_036\" FROM attendance AS T1 INNER JOIN event AS T2 ON T2.\"XCL_010\" = T1.\"XCL_001\" INNER JOIN member AS T3 ON T1.\"XCL_002\" = T3.\"XCL_034\" WHERE T2.\"XCL_011\" = 'Women''s Soccer' AND T3.\"XCL_038\" = 'Member'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1431"
  ]
}
```

### "event"."XCL_013" = 'Meeting' AND SUBSTRING("event"."XCL_012", 1, 4) = '2020'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_013\" = 'Meeting' AND SUBSTRING(\"event\".\"XCL_012\", 1, 4) = '2020'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_010\") FROM event WHERE \"XCL_013\" = 'Meeting' AND SUBSTRING(\"XCL_012\", 1, 4) = '2020'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1379"
  ]
}
```

### COUNT("attendance"."XCL_001") > 7

```json
{
  "kind": "predicate",
  "formula": "COUNT(\"attendance\".\"XCL_001\") > 7",
  "grain": [
    "\"attendance\".\"XCL_002\""
  ],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_034\" = T2.\"XCL_002\" GROUP BY T2.\"XCL_002\" HAVING COUNT(T2.\"XCL_001\") > 7",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1381"
  ]
}
```

### "budget"."XCL_004" = 'Food'

```json
{
  "kind": "predicate",
  "formula": "\"budget\".\"XCL_004\" = 'Food'",
  "grain": [],
  "population_scope": "SELECT MAX(\"XCL_007\") FROM budget WHERE \"XCL_004\" = 'Food'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1343"
  ]
}
```

### A distinct member attribute (XCL_040) for members associated with expenses that exceed the global average expense amount. The grain is unique combinat

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_040\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_035\", T3.\"XCL_036\", T3.\"XCL_040\" FROM expense AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_023\" = T2.\"XCL_003\" INNER JOIN member AS T3 ON T3.\"XCL_034\" = T1.\"XCL_022\" WHERE T1.\"XCL_020\" > (SELECT AVG(T1.\"XCL_020\") FROM expense AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_023\" = T2.\"XCL_003\" INNER JOIN member AS T3 ON T3.\"XCL_034\" = T1.\"XCL_022\")",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1457"
  ]
}
```

### Distinct values of the member identifier column XCL_037 from the member table, filtered to members who have associated expenses with a date between 20

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_037\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_037\" FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE DATE(SUBSTRING(T2.\"XCL_019\", 1, 10)) BETWEEN '2019-09-10' AND '2019-11-19' AND T2.\"XCL_020\" > 20",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1440"
  ]
}
```

### Aggregated sum of the budget field XCL_007 from the budget table, filtered to records linked to events where the event name or category XCL_011 is 'Oc

```json
{
  "kind": "metric",
  "formula": "SUM(\"budget\".\"XCL_007\")",
  "grain": [],
  "population_scope": "SELECT SUM(T2.\"XCL_007\") FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_011\" = 'October Speaker'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r1\".\"XCL_007\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      }
    ],
    "scope_sql": "SELECT SUM(\"r1\".\"XCL_007\") AS \"value\" FROM event AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" WHERE \"r0\".\"XCL_011\" = 'October Speaker'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1337"
  ]
}
```

### "zip_code"."XCL_045" = 'Georgetown' AND "zip_code"."XCL_047" = 'South Carolina'

```json
{
  "kind": "predicate",
  "formula": "\"zip_code\".\"XCL_045\" = 'Georgetown' AND \"zip_code\".\"XCL_047\" = 'South Carolina'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T2.\"XCL_045\" = 'Georgetown' AND T2.\"XCL_047\" = 'South Carolina'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1383"
  ]
}
```

### "zip_code"."XCL_044" = 'PO Box' AND "zip_code"."XCL_046" = 'San Juan Municipio' AND "zip_code"."XCL_047" = 'Puerto Rico'

```json
{
  "kind": "predicate",
  "formula": "\"zip_code\".\"XCL_044\" = 'PO Box' AND \"zip_code\".\"XCL_046\" = 'San Juan Municipio' AND \"zip_code\".\"XCL_047\" = 'Puerto Rico'",
  "grain": [],
  "population_scope": "SELECT \"XCL_043\" FROM zip_code WHERE \"XCL_044\" = 'PO Box' AND \"XCL_046\" = 'San Juan Municipio' AND \"XCL_047\" = 'Puerto Rico'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1434"
  ]
}
```

### DATE(SUBSTRING("event"."XCL_012", 1, 10)) BETWEEN '2019-11-01' AND '2020-03-31'

```json
{
  "kind": "predicate",
  "formula": "DATE(SUBSTRING(\"event\".\"XCL_012\", 1, 10)) BETWEEN '2019-11-01' AND '2020-03-31'",
  "grain": [],
  "population_scope": "SELECT \"XCL_010\", \"XCL_015\", \"XCL_016\" FROM event WHERE DATE(SUBSTRING(\"XCL_012\", 1, 10)) BETWEEN '2019-11-01' AND '2020-03-31'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1443"
  ]
}
```

### "expense"."XCL_018" = 'Pizza' AND "expense"."XCL_020" > 50 AND "expense"."XCL_020" < 100

```json
{
  "kind": "predicate",
  "formula": "\"expense\".\"XCL_018\" = 'Pizza' AND \"expense\".\"XCL_020\" > 50 AND \"expense\".\"XCL_020\" < 100",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_011\", T1.\"XCL_012\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" WHERE T3.\"XCL_018\" = 'Pizza' AND T3.\"XCL_020\" > 50 AND T3.\"XCL_020\" < 100",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1448"
  ]
}
```

### "major"."XCL_032" = 'School of Applied Sciences, Technology and Education'

```json
{
  "kind": "predicate",
  "formula": "\"major\".\"XCL_032\" = 'School of Applied Sciences, Technology and Education'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T2.\"XCL_032\" = 'School of Applied Sciences, Technology and Education'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1375"
  ]
}
```

### Member Identifier XCL_035

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T2.\"XCL_045\" = 'Georgetown' AND T2.\"XCL_047\" = 'South Carolina'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_035\" AS \"value\" FROM member AS \"r0\" INNER JOIN zip_code AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_043\" WHERE \"r1\".\"XCL_045\" = 'Georgetown' AND \"r1\".\"XCL_047\" = 'South Carolina'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1383"
  ]
}
```

### "member"."XCL_038" = 'Vice President'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_038\" = 'Vice President'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_017\", T2.\"XCL_018\" FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T1.\"XCL_038\" = 'Vice President'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1370"
  ]
}
```

### Max XCL_007 for Food

```json
{
  "kind": "metric",
  "formula": "MAX(\"budget\".\"XCL_007\")",
  "grain": [],
  "population_scope": "SELECT MAX(\"XCL_007\") FROM budget WHERE \"XCL_004\" = 'Food'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MAX(\"r0\".\"XCL_007\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "budget"
      }
    ],
    "scope_sql": "SELECT MAX(\"r0\".\"XCL_007\") AS \"value\" FROM budget AS \"r0\" WHERE \"r0\".\"XCL_004\" = 'Food'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1343"
  ]
}
```

### Aggregates the number of rows resulting from the join between budget and event tables, specifically counting the event identifier (XCL_010) for record

```json
{
  "kind": "metric",
  "formula": "COUNT(\"event\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_010\") FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = 'November Meeting' AND T1.\"XCL_006\" < 0",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "budget"
      },
      {
        "role": "r1",
        "physical_table": "event"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_010\") AS \"value\" FROM budget AS \"r0\" INNER JOIN event AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_010\" WHERE \"r1\".\"XCL_011\" = 'November Meeting' AND \"r0\".\"XCL_006\" < 0",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1348"
  ]
}
```

### "event"."XCL_011" = 'Laugh Out Loud'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'Laugh Out Loud'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_034\" = T2.\"XCL_002\" INNER JOIN event AS T3 ON T2.\"XCL_001\" = T3.\"XCL_010\" WHERE T3.\"XCL_011\" = 'Laugh Out Loud'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1327"
  ]
}
```

### The zip code identifier (column XCL_043) for postal records in San Juan Municipio, Puerto Rico, specifically filtered to the 'PO Box' delivery type.

```json
{
  "kind": "binding",
  "formula": "\"zip_code\".\"XCL_043\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_043\" FROM zip_code WHERE \"XCL_044\" = 'PO Box' AND \"XCL_046\" = 'San Juan Municipio' AND \"XCL_047\" = 'Puerto Rico'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_043\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_043\" AS \"value\" FROM zip_code AS \"r0\" WHERE \"r0\".\"XCL_044\" = 'PO Box' AND \"r0\".\"XCL_046\" = 'San Juan Municipio' AND \"r0\".\"XCL_047\" = 'Puerto Rico'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1434"
  ]
}
```

### Member Attribute XCL_035

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [
    "\"attendance\".\"XCL_002\""
  ],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_034\" = T2.\"XCL_002\" GROUP BY T2.\"XCL_002\" HAVING COUNT(T2.\"XCL_001\") > 7",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_035\"",
    "grain": [
      "\"r1\".\"XCL_002\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "attendance"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_002\" AS \"grain_0\", \"r0\".\"XCL_035\" AS \"value\" FROM member AS \"r0\" INNER JOIN attendance AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_002\" GROUP BY \"r1\".\"XCL_002\" HAVING COUNT(\"r1\".\"XCL_001\") > 7",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1381"
  ]
}
```

### Returns the values of column "XCL_003" from the "budget" table for rows where "XCL_004" is 'Advertisement', sorted by "XCL_007" in descending order, l

```json
{
  "kind": "binding",
  "formula": "\"budget\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_003\" FROM budget WHERE \"XCL_004\" = 'Advertisement' ORDER BY \"XCL_007\" DESC LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1407"
  ]
}
```

### "member"."XCL_038" = 'Vice President'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_038\" = 'Vice President'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_026\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_038\" = 'Vice President'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1331"
  ]
}
```

### Sum of column XCL_020 from the expense table, aggregated for all expenses linked to the member via the join condition member.XCL_034 = expense.XCL_022

```json
{
  "kind": "metric",
  "formula": "SUM(\"expense\".\"XCL_020\")",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\", SUM(T2.\"XCL_020\") FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T1.\"XCL_034\" = 'rec4BLdZHS2Blfp4v'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r1\".\"XCL_020\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT SUM(\"r1\".\"XCL_020\") AS \"value\" FROM member AS \"r0\" INNER JOIN expense AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_022\" WHERE \"r0\".\"XCL_034\" = 'rec4BLdZHS2Blfp4v'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1410"
  ]
}
```

### Member Attribute XCL_036

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_035\", T3.\"XCL_036\" FROM expense AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_023\" = T2.\"XCL_003\" INNER JOIN member AS T3 ON T1.\"XCL_022\" = T3.\"XCL_034\" ORDER BY T2.\"XCL_005\" DESC LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1456"
  ]
}
```

### Expense Attribute XCL_018

```json
{
  "kind": "binding",
  "formula": "\"expense\".\"XCL_018\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_018\" FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T1.\"XCL_039\" = 'X-Large'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_018\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_018\" AS \"value\" FROM member AS \"r0\" INNER JOIN expense AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_022\" WHERE \"r0\".\"XCL_039\" = 'X-Large'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1412"
  ]
}
```

### Event Identifier

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_011\"",
  "grain": [
    "\"event\".\"XCL_011\""
  ],
  "population_scope": "SELECT SUM(T1.\"XCL_005\"), T2.\"XCL_011\" FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T1.\"XCL_004\" = 'Speaker Gifts' GROUP BY T2.\"XCL_011\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_011\"",
    "grain": [
      "\"r1\".\"XCL_011\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "budget"
      },
      {
        "role": "r1",
        "physical_table": "event"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_011\" AS \"grain_0\", \"r1\".\"XCL_011\" AS \"value\" FROM budget AS \"r0\" INNER JOIN event AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_010\" WHERE \"r0\".\"XCL_004\" = 'Speaker Gifts' GROUP BY \"r1\".\"XCL_011\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1467"
  ]
}
```

### "event"."XCL_011" = 'October Meeting'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'October Meeting'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_013\", SUM(T3.\"XCL_020\") FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" WHERE T1.\"XCL_011\" = 'October Meeting'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1404"
  ]
}
```

### Event Identifier

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_011\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T2.\"XCL_004\" = 'Food'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_011\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_011\" AS \"value\" FROM event AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" WHERE \"r1\".\"XCL_004\" = 'Food'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1463"
  ]
}
```

### The value of column "XCL_018" from the "expense" table for the single row with the highest value in column "XCL_020".

```json
{
  "kind": "binding",
  "formula": "\"expense\".\"XCL_018\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_018\" FROM expense ORDER BY \"XCL_020\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1325"
  ]
}
```

### Income Attribute XCL_025

```json
{
  "kind": "binding",
  "formula": "\"income\".\"XCL_025\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_025\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_035\" = 'Casey' AND T1.\"XCL_036\" = 'Mason'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_025\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "income"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_025\" AS \"value\" FROM member AS \"r0\" INNER JOIN income AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_029\" WHERE \"r0\".\"XCL_035\" = 'Casey' AND \"r0\".\"XCL_036\" = 'Mason'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1372"
  ]
}
```

### Member XCL_036

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_036\", T1.\"XCL_038\" FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T2.\"XCL_019\" = '2019-09-10' AND T2.\"XCL_018\" = 'Pizza'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_036\" AS \"value\" FROM member AS \"r0\" INNER JOIN expense AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_022\" WHERE \"r1\".\"XCL_019\" = '2019-09-10' AND \"r1\".\"XCL_018\" = 'Pizza'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1430"
  ]
}
```

### Member Zip Code

```json
{
  "kind": "binding",
  "formula": "\"zip_code\".\"XCL_046\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_046\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_035\" = 'Sherri' AND T1.\"XCL_036\" = 'Ramsey'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_046\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_046\" AS \"value\" FROM member AS \"r0\" INNER JOIN zip_code AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_043\" WHERE \"r0\".\"XCL_035\" = 'Sherri' AND \"r0\".\"XCL_036\" = 'Ramsey'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1329"
  ]
}
```

### Calculates the percentage of income rows (identified by XCL_024) where the value of XCL_026 is 50, within the population of members filtered by XCL_03

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"income\".\"XCL_026\" = 50 THEN 1.0 ELSE 0 END) AS REAL) * 100 / COUNT(\"income\".\"XCL_024\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_026\" = 50 THEN 1.0 ELSE 0 END) AS REAL) * 100 / COUNT(T2.\"XCL_024\") FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_038\" = 'Member' AND T1.\"XCL_039\" = 'Medium'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r1\".\"XCL_026\" = 50 THEN 1.0 ELSE 0 END) AS REAL) * 100 / COUNT(\"r1\".\"XCL_024\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "income"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r1\".\"XCL_026\" = 50 THEN 1.0 ELSE 0 END) AS REAL) * 100 / COUNT(\"r1\".\"XCL_024\") AS \"value\" FROM member AS \"r0\" INNER JOIN income AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_029\" WHERE \"r0\".\"XCL_038\" = 'Member' AND \"r0\".\"XCL_039\" = 'Medium'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1432"
  ]
}
```

### COUNT(DISTINCT "event"."XCL_010") > 1

```json
{
  "kind": "predicate",
  "formula": "COUNT(DISTINCT \"event\".\"XCL_010\") > 1",
  "grain": [
    "\"member\".\"XCL_034\""
  ],
  "population_scope": "SELECT T2.\"XCL_034\" FROM expense AS T1 INNER JOIN member AS T2 ON T1.\"XCL_022\" = T2.\"XCL_034\" INNER JOIN budget AS T3 ON T1.\"XCL_023\" = T3.\"XCL_003\" INNER JOIN event AS T4 ON T3.\"XCL_009\" = T4.\"XCL_010\" GROUP BY T2.\"XCL_034\" HAVING COUNT(DISTINCT T4.\"XCL_010\") > 1 ORDER BY SUM(T1.\"XCL_020\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1451"
  ]
}
```

### Member Attribute XCL_036

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\", T1.\"XCL_038\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T2.\"XCL_043\" = T1.\"XCL_041\" WHERE T2.\"XCL_045\" = 'Lincolnton' AND T2.\"XCL_047\" = 'North Carolina' AND T2.\"XCL_043\" = 28092",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_036\" AS \"value\" FROM member AS \"r0\" INNER JOIN zip_code AS \"r1\" ON \"r1\".\"XCL_043\" = \"r0\".\"XCL_041\" WHERE \"r1\".\"XCL_045\" = 'Lincolnton' AND \"r1\".\"XCL_047\" = 'North Carolina' AND \"r1\".\"XCL_043\" = 28092",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1469"
  ]
}
```

### Aggregated sum of the budget field XCL_007 for all budget records associated with the event identified as 'September Speaker'. The grain is a single s

```json
{
  "kind": "metric",
  "formula": "SUM(\"budget\".\"XCL_007\")",
  "grain": [],
  "population_scope": "SELECT SUM(T1.\"XCL_007\") FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = 'September Speaker'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r0\".\"XCL_007\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "budget"
      },
      {
        "role": "r1",
        "physical_table": "event"
      }
    ],
    "scope_sql": "SELECT SUM(\"r0\".\"XCL_007\") AS \"value\" FROM budget AS \"r0\" INNER JOIN event AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_010\" WHERE \"r1\".\"XCL_011\" = 'September Speaker'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1349"
  ]
}
```

### Member Attribute XCL_036

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_035\", \"XCL_036\" FROM member WHERE \"XCL_039\" = 'X-Large'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_036\" AS \"value\" FROM member AS \"r0\" WHERE \"r0\".\"XCL_039\" = 'X-Large'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1445"
  ]
}
```

### "event"."XCL_011" = 'Women''s Soccer'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'Women''s Soccer'",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_002\") FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" WHERE T1.\"XCL_011\" = 'Women''s Soccer'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1371"
  ]
}
```

### Average Expense Amount

```json
{
  "kind": "metric",
  "formula": "AVG(\"expense\".\"XCL_020\")",
  "grain": [],
  "population_scope": "SELECT AVG(T2.\"XCL_020\") FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T1.\"XCL_036\" = 'Allen' AND T1.\"XCL_035\" = 'Elijah' AND (SUBSTRING(T2.\"XCL_019\", 6, 2) = '09' OR SUBSTRING(T2.\"XCL_019\", 6, 2) = '10')",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r1\".\"XCL_020\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT AVG(\"r1\".\"XCL_020\") AS \"value\" FROM member AS \"r0\" INNER JOIN expense AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_022\" WHERE \"r0\".\"XCL_036\" = 'Allen' AND \"r0\".\"XCL_035\" = 'Elijah' AND (SUBSTRING(\"r1\".\"XCL_019\", 6, 2) = '09' OR SUBSTRING(\"r1\".\"XCL_019\", 6, 2) = '10')",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1339"
  ]
}
```

### Major Attribute XCL_033

```json
{
  "kind": "binding",
  "formula": "\"major\".\"XCL_033\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_033\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T1.\"XCL_042\" = 'rec1N0upiVLy5esTO' AND T1.\"XCL_035\" = 'Katy'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_033\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_033\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r1\".\"XCL_030\" = \"r0\".\"XCL_042\" WHERE \"r0\".\"XCL_042\" = 'rec1N0upiVLy5esTO' AND \"r0\".\"XCL_035\" = 'Katy'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1438"
  ]
}
```

### Member Identifier XCL_036

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T2.\"XCL_032\" = 'Art and Design Department'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_036\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r0\".\"XCL_042\" = \"r1\".\"XCL_030\" WHERE \"r1\".\"XCL_032\" = 'Art and Design Department'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1314"
  ]
}
```

### Member Attribute XCL_036

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T2.\"XCL_047\" = 'Illinois'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_036\" AS \"value\" FROM member AS \"r0\" INNER JOIN zip_code AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_043\" WHERE \"r1\".\"XCL_047\" = 'Illinois'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1334"
  ]
}
```

### Distinct values of the event attribute XCL_011 for events linked to budgets with a positive XCL_006 value.

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_011\", T1.\"XCL_015\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T2.\"XCL_006\" > 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1447"
  ]
}
```

### Major Attribute XCL_031

```json
{
  "kind": "binding",
  "formula": "\"major\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_031\", T2.\"XCL_032\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T1.\"XCL_035\" = 'Garrett' AND T1.\"XCL_036\" = 'Gerke'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_031\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_031\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r1\".\"XCL_030\" = \"r0\".\"XCL_042\" WHERE \"r0\".\"XCL_035\" = 'Garrett' AND \"r0\".\"XCL_036\" = 'Gerke'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1459"
  ]
}
```

### "income"."XCL_025" = '2019-09-09'

```json
{
  "kind": "predicate",
  "formula": "\"income\".\"XCL_025\" = '2019-09-09'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_035\", T3.\"XCL_036\", T4.\"XCL_026\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" INNER JOIN member AS T3 ON T3.\"XCL_034\" = T2.\"XCL_002\" INNER JOIN income AS T4 ON T4.\"XCL_029\" = T3.\"XCL_034\" WHERE T4.\"XCL_025\" = '2019-09-09'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1464"
  ]
}
```

### Event Identifier

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T1.\"XCL_004\" = 'Advertisement' ORDER BY T1.\"XCL_005\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1398"
  ]
}
```

### Aggregates the count of the 'XCL_034' column from the 'member' table, restricted to rows where 'XCL_038' equals 'President'. Returns a single scalar v

```json
{
  "kind": "metric",
  "formula": "COUNT(\"member\".\"XCL_034\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_034\") FROM member WHERE \"XCL_038\" = 'President'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_034\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_034\") AS \"value\" FROM member AS \"r0\" WHERE \"r0\".\"XCL_038\" = 'President'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1377"
  ]
}
```

### Calculates the percentage of total budget amount (XCL_007) allocated to 'Parking' (XCL_004) for events named 'November Speaker'. The metric aggregates

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"budget\".\"XCL_004\" = 'Parking' THEN \"budget\".\"XCL_007\" ELSE 0 END) AS REAL) * 100 / SUM(\"budget\".\"XCL_007\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T1.\"XCL_004\" = 'Parking' THEN T1.\"XCL_007\" ELSE 0 END) AS REAL) * 100 / SUM(T1.\"XCL_007\") FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = 'November Speaker'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r0\".\"XCL_004\" = 'Parking' THEN \"r0\".\"XCL_007\" ELSE 0 END) AS REAL) * 100 / SUM(\"r0\".\"XCL_007\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "budget"
      },
      {
        "role": "r1",
        "physical_table": "event"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r0\".\"XCL_004\" = 'Parking' THEN \"r0\".\"XCL_007\" ELSE 0 END) AS REAL) * 100 / SUM(\"r0\".\"XCL_007\") AS \"value\" FROM budget AS \"r0\" INNER JOIN event AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_010\" WHERE \"r1\".\"XCL_011\" = 'November Speaker'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1360"
  ]
}
```

### "event"."XCL_013" = 'Meeting'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_013\" = 'Meeting'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_011\" FROM event AS T1 WHERE T1.\"XCL_013\" = 'Meeting'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1322"
  ]
}
```

### "member"."XCL_035" = 'Angela' AND "member"."XCL_036" = 'Sanders'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_035\" = 'Angela' AND \"member\".\"XCL_036\" = 'Sanders'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_031\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_035\" = 'Angela' AND T1.\"XCL_036\" = 'Sanders'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1312"
  ]
}
```

### The maximum value of the 'XCL_027' column from the 'income' table, restricted to records where 'XCL_025' falls within the date range 2019-09-01 to 201

```json
{
  "kind": "binding",
  "formula": "\"income\".\"XCL_027\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_027\" FROM income WHERE \"XCL_025\" BETWEEN '2019-09-01' AND '2019-09-30' ORDER BY \"XCL_027\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1392"
  ]
}
```

### "member"."XCL_035" = 'Brent' AND "member"."XCL_036" = 'Thomason'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_035\" = 'Brent' AND \"member\".\"XCL_036\" = 'Thomason'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_031\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_035\" = 'Brent' AND T1.\"XCL_036\" = 'Thomason'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1351"
  ]
}
```

### Count of major records (XCL_030) filtered by specific school and college names.

```json
{
  "kind": "metric",
  "formula": "COUNT(\"major\".\"XCL_030\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_030\") FROM major WHERE \"XCL_032\" = 'School of Applied Sciences, Technology and Education' AND \"XCL_033\" = 'College of Agriculture and Applied Sciences'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_030\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_030\") AS \"value\" FROM major AS \"r0\" WHERE \"r0\".\"XCL_032\" = 'School of Applied Sciences, Technology and Education' AND \"r0\".\"XCL_033\" = 'College of Agriculture and Applied Sciences'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1425"
  ]
}
```

### Major Attribute XCL_031

```json
{
  "kind": "binding",
  "formula": "\"major\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_031\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_038\" = 'Vice President'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_031\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_031\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r0\".\"XCL_042\" = \"r1\".\"XCL_030\" WHERE \"r0\".\"XCL_038\" = 'Vice President'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1354"
  ]
}
```

### "budget"."XCL_004" = 'Food' AND "budget"."XCL_008" = 'Closed'

```json
{
  "kind": "predicate",
  "formula": "\"budget\".\"XCL_004\" = 'Food' AND \"budget\".\"XCL_008\" = 'Closed'",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_005\") / COUNT(\"XCL_005\") FROM budget WHERE \"XCL_004\" = 'Food' AND \"XCL_008\" = 'Closed'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1397"
  ]
}
```

### "event"."XCL_011" = 'November Speaker'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'November Speaker'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T1.\"XCL_004\" = 'Parking' THEN T1.\"XCL_007\" ELSE 0 END) AS REAL) * 100 / SUM(T1.\"XCL_007\") FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T2.\"XCL_011\" = 'November Speaker'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1360"
  ]
}
```

### Advertisement Budget Amount for September Meeting

```json
{
  "kind": "binding",
  "formula": "\"budget\".\"XCL_005\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_005\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_011\" = 'September Meeting' AND T2.\"XCL_004\" = 'Advertisement' AND SUBSTRING(T1.\"XCL_012\", 6, 2) = '09'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_005\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_005\" AS \"value\" FROM event AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" WHERE \"r0\".\"XCL_011\" = 'September Meeting' AND \"r1\".\"XCL_004\" = 'Advertisement' AND SUBSTRING(\"r0\".\"XCL_012\", 6, 2) = '09'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1335"
  ]
}
```

### "member"."XCL_036" = 'Allen' AND "member"."XCL_035" = 'Elijah' AND (SUBSTRING("expense"."XCL_019", 6, 2) = '09' OR SUBSTRING("expense"."XCL_019", 6, 2

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_036\" = 'Allen' AND \"member\".\"XCL_035\" = 'Elijah' AND (SUBSTRING(\"expense\".\"XCL_019\", 6, 2) = '09' OR SUBSTRING(\"expense\".\"XCL_019\", 6, 2) = '10')",
  "grain": [],
  "population_scope": "SELECT AVG(T2.\"XCL_020\") FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T1.\"XCL_036\" = 'Allen' AND T1.\"XCL_035\" = 'Elijah' AND (SUBSTRING(T2.\"XCL_019\", 6, 2) = '09' OR SUBSTRING(T2.\"XCL_019\", 6, 2) = '10')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1339"
  ]
}
```

### Member Attribute XCL_036

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_035\", \"XCL_036\", \"XCL_037\" FROM member WHERE \"XCL_038\" = 'Secretary'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_036\" AS \"value\" FROM member AS \"r0\" WHERE \"r0\".\"XCL_038\" = 'Secretary'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1393"
  ]
}
```

### "event"."XCL_011" = 'Women''s Soccer'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'Women''s Soccer'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_040\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" INNER JOIN member AS T3 ON T2.\"XCL_002\" = T3.\"XCL_034\" WHERE T1.\"XCL_011\" = 'Women''s Soccer'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1316"
  ]
}
```

### "zip_code"."XCL_046" = 'Orange County' AND "zip_code"."XCL_047" = 'Virginia'

```json
{
  "kind": "predicate",
  "formula": "\"zip_code\".\"XCL_046\" = 'Orange County' AND \"zip_code\".\"XCL_047\" = 'Virginia'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_045\") FROM zip_code WHERE \"XCL_046\" = 'Orange County' AND \"XCL_047\" = 'Virginia'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1362"
  ]
}
```

### Calculates the percentage of records in the zip_code table where the XCL_044 field equals 'PO Box', relative to the total count of non-null XCL_043 va

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"zip_code\".\"XCL_044\" = 'PO Box' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"zip_code\".\"XCL_043\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN \"XCL_044\" = 'PO Box' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"XCL_043\") FROM zip_code",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r0\".\"XCL_044\" = 'PO Box' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_043\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r0\".\"XCL_044\" = 'PO Box' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_043\") AS \"value\" FROM zip_code AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1446"
  ]
}
```

### The value of column XCL_003 for the specific budget record where XCL_004 is 'Food' and XCL_007 matches the global maximum of XCL_007.

```json
{
  "kind": "binding",
  "formula": "\"budget\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_003\" FROM budget WHERE \"XCL_004\" = 'Food' AND \"XCL_007\" = (SELECT MAX(\"XCL_007\") FROM budget)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1406"
  ]
}
```

### Aggregates the count of non-null values in column XCL_034 from the member table, filtered to rows where XCL_038 is 'Member' and XCL_039 is 'X-Large'. 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"member\".\"XCL_034\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_034\") FROM member WHERE \"XCL_038\" = 'Member' AND \"XCL_039\" = 'X-Large'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_034\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_034\") AS \"value\" FROM member AS \"r0\" WHERE \"r0\".\"XCL_038\" = 'Member' AND \"r0\".\"XCL_039\" = 'X-Large'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1424"
  ]
}
```

### Attribute XCL_033 from the major table, representing a specific property of the 'Environmental Engineering' major.

```json
{
  "kind": "binding",
  "formula": "\"major\".\"XCL_033\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_036\", T1.\"XCL_032\", T1.\"XCL_033\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" WHERE T2.\"XCL_038\" = 'Member' AND T1.\"XCL_031\" = 'Environmental Engineering'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_033\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "major"
      },
      {
        "role": "r1",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_033\" AS \"value\" FROM major AS \"r0\" INNER JOIN member AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_042\" WHERE \"r1\".\"XCL_038\" = 'Member' AND \"r0\".\"XCL_031\" = 'Environmental Engineering'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1426"
  ]
}
```

### "member"."XCL_038" = 'Member' AND "major"."XCL_031" = 'Environmental Engineering'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_038\" = 'Member' AND \"major\".\"XCL_031\" = 'Environmental Engineering'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_036\", T1.\"XCL_032\", T1.\"XCL_033\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" WHERE T2.\"XCL_038\" = 'Member' AND T1.\"XCL_031\" = 'Environmental Engineering'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1426"
  ]
}
```

### "member"."XCL_035" = 'Christof' AND "member"."XCL_036" = 'Nielson'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_035\" = 'Christof' AND \"member\".\"XCL_036\" = 'Nielson'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_044\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_035\" = 'Christof' AND T1.\"XCL_036\" = 'Nielson'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1353"
  ]
}
```

### "member"."XCL_038" = 'Vice President' AND "event"."XCL_015" = '900 E. Washington St.' AND "event"."XCL_013" = 'Social'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_038\" = 'Vice President' AND \"event\".\"XCL_015\" = '900 E. Washington St.' AND \"event\".\"XCL_013\" = 'Social'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" FROM attendance AS T1 INNER JOIN event AS T2 ON T2.\"XCL_010\" = T1.\"XCL_001\" INNER JOIN member AS T3 ON T1.\"XCL_002\" = T3.\"XCL_034\" WHERE T3.\"XCL_038\" = 'Vice President' AND T2.\"XCL_015\" = '900 E. Washington St.' AND T2.\"XCL_013\" = 'Social'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1429"
  ]
}
```

### Aggregated sum of the XCL_020 column from the expense table, restricted to rows where XCL_018 equals 'Pizza'. Returns a single scalar value representi

```json
{
  "kind": "metric",
  "formula": "SUM(\"expense\".\"XCL_020\")",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_020\") FROM expense WHERE \"XCL_018\" = 'Pizza'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r0\".\"XCL_020\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT SUM(\"r0\".\"XCL_020\") AS \"value\" FROM expense AS \"r0\" WHERE \"r0\".\"XCL_018\" = 'Pizza'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1361"
  ]
}
```

### "event"."XCL_011" = 'October Meeting' AND "event"."XCL_012" LIKE '2019-10-08%'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'October Meeting' AND \"event\".\"XCL_012\" LIKE '2019-10-08%'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_021\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" WHERE T1.\"XCL_011\" = 'October Meeting' AND T1.\"XCL_012\" LIKE '2019-10-08%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1338"
  ]
}
```

### Member Attribute XCL_035

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [
    "\"member\".\"XCL_035\"",
    "\"member\".\"XCL_036\"",
    "\"income\".\"XCL_027\""
  ],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\", T2.\"XCL_027\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" GROUP BY T1.\"XCL_035\", T1.\"XCL_036\", T2.\"XCL_027\" ORDER BY SUM(T2.\"XCL_026\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1388"
  ]
}
```

### Member Identifier XCL_035

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T2.\"XCL_032\" = 'Art and Design Department'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_035\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r0\".\"XCL_042\" = \"r1\".\"XCL_030\" WHERE \"r1\".\"XCL_032\" = 'Art and Design Department'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1314"
  ]
}
```

### "event"."XCL_011" = 'Spring Budget Review'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'Spring Budget Review'",
  "grain": [],
  "population_scope": "SELECT \"XCL_015\" FROM event WHERE \"XCL_011\" = 'Spring Budget Review'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1341"
  ]
}
```

### "budget"."XCL_006" > 30

```json
{
  "kind": "predicate",
  "formula": "\"budget\".\"XCL_006\" > 30",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_013\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T2.\"XCL_006\" > 30",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1417"
  ]
}
```

### "member"."XCL_038" <> 'Member'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_038\" <> 'Member'",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_020\") FROM expense AS T1 INNER JOIN member AS T2 ON T1.\"XCL_022\" = T2.\"XCL_034\" WHERE T2.\"XCL_038\" <> 'Member'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1452"
  ]
}
```

### "expense"."XCL_020" > 50

```json
{
  "kind": "predicate",
  "formula": "\"expense\".\"XCL_020\" > 50",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_001\" FROM expense AS T1 INNER JOIN member AS T2 ON T1.\"XCL_022\" = T2.\"XCL_034\" INNER JOIN attendance AS T3 ON T2.\"XCL_034\" = T3.\"XCL_002\" WHERE T1.\"XCL_020\" > 50",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1436"
  ]
}
```

### "member"."XCL_035" = 'Grant' AND "member"."XCL_036" = 'Gilmour'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_035\" = 'Grant' AND \"member\".\"XCL_036\" = 'Gilmour'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_026\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_035\" = 'Grant' AND T1.\"XCL_036\" = 'Gilmour'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1384"
  ]
}
```

### Budget Identifier

```json
{
  "kind": "binding",
  "formula": "\"budget\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_008\" FROM budget AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_003\" = T2.\"XCL_023\" WHERE T2.\"XCL_018\" = 'Post Cards, Posters' AND T2.\"XCL_019\" = '2019-08-20'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "budget"
      },
      {
        "role": "r1",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_008\" AS \"value\" FROM budget AS \"r0\" INNER JOIN expense AS \"r1\" ON \"r0\".\"XCL_003\" = \"r1\".\"XCL_023\" WHERE \"r1\".\"XCL_018\" = 'Post Cards, Posters' AND \"r1\".\"XCL_019\" = '2019-08-20'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1350"
  ]
}
```

### Distinct values of the zip code attribute (XCL_046) from the zip_code table, filtered to locations associated with members having income records where

```json
{
  "kind": "binding",
  "formula": "\"zip_code\".\"XCL_046\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_045\", T3.\"XCL_046\" FROM income AS T1 INNER JOIN member AS T2 ON T1.\"XCL_029\" = T2.\"XCL_034\" INNER JOIN zip_code AS T3 ON T3.\"XCL_043\" = T2.\"XCL_041\" WHERE T1.\"XCL_026\" > 40",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1450"
  ]
}
```

### Expense Identifier

```json
{
  "kind": "binding",
  "formula": "\"expense\".\"XCL_022\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_022\", T3.\"XCL_001\" FROM expense AS T1 INNER JOIN member AS T2 ON T1.\"XCL_022\" = T2.\"XCL_034\" INNER JOIN attendance AS T3 ON T2.\"XCL_034\" = T3.\"XCL_002\" WHERE DATE(SUBSTRING(T1.\"XCL_019\", 1, 10)) BETWEEN '2019-01-10' AND '2019-11-19' AND T1.\"XCL_021\" = 'true'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1437"
  ]
}
```

### Member Attribute XCL_035

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_035\", \"XCL_036\" FROM member WHERE \"XCL_039\" = 'X-Large'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_035\" AS \"value\" FROM member AS \"r0\" WHERE \"r0\".\"XCL_039\" = 'X-Large'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1445"
  ]
}
```

### Value of column XCL_047 from the zip_code table for the member identified by first name 'Amy' and last name 'Firth'.

```json
{
  "kind": "binding",
  "formula": "\"zip_code\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_045\", T2.\"XCL_046\", T2.\"XCL_047\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_035\" = 'Amy' AND T1.\"XCL_036\" = 'Firth'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_047\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_047\" AS \"value\" FROM member AS \"r0\" INNER JOIN zip_code AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_043\" WHERE \"r0\".\"XCL_035\" = 'Amy' AND \"r0\".\"XCL_036\" = 'Firth'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1364"
  ]
}
```

### Fundraiser event identifier

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_011\" FROM event AS T1 WHERE T1.\"XCL_013\" = 'Fundraiser'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_011\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_011\" AS \"value\" FROM event AS \"r0\" WHERE \"r0\".\"XCL_013\" = 'Fundraiser'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1323"
  ]
}
```

### "major"."XCL_031" = 'Law and Constitutional Studies'

```json
{
  "kind": "predicate",
  "formula": "\"major\".\"XCL_031\" = 'Law and Constitutional Studies'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_036\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T2.\"XCL_031\" = 'Law and Constitutional Studies'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1328"
  ]
}
```

### Aggregates the number of event identifiers (XCL_010) from the event table, restricted to events occurring in 2019 (based on the first 4 characters of 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"event\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_010\") FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" INNER JOIN member AS T3 ON T2.\"XCL_002\" = T3.\"XCL_034\" WHERE T3.\"XCL_035\" = 'Sacha' AND T3.\"XCL_036\" = 'Harrison' AND SUBSTRING(T1.\"XCL_012\", 1, 4) = '2019'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "attendance"
      },
      {
        "role": "r2",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_010\") AS \"value\" FROM event AS \"r0\" INNER JOIN attendance AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_001\" INNER JOIN member AS \"r2\" ON \"r1\".\"XCL_002\" = \"r2\".\"XCL_034\" WHERE \"r2\".\"XCL_035\" = 'Sacha' AND \"r2\".\"XCL_036\" = 'Harrison' AND SUBSTRING(\"r0\".\"XCL_012\", 1, 4) = '2019'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1321"
  ]
}
```

### Distinct XCL_046 values for PO Box records

```json
{
  "kind": "binding",
  "formula": "\"zip_code\".\"XCL_046\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_046\" FROM zip_code WHERE \"XCL_044\" = 'PO Box' AND NOT \"XCL_046\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1433"
  ]
}
```

### Distinct value of column XCL_035 from the member table, representing a member attribute for those with qualifying expenses.

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_035\", T1.\"XCL_036\", T2.\"XCL_031\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" INNER JOIN expense AS T3 ON T1.\"XCL_034\" = T3.\"XCL_022\" WHERE T3.\"XCL_020\" > 100",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1449"
  ]
}
```

### "member"."XCL_038" = 'Member'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_038\" = 'Member'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_031\" = 'Business' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_034\") FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T1.\"XCL_038\" = 'Member'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1421"
  ]
}
```

### Budget Attribute XCL_004

```json
{
  "kind": "binding",
  "formula": "\"budget\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_004\", T2.\"XCL_007\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_011\" = 'January Speaker'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_004\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_004\" AS \"value\" FROM event AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" WHERE \"r0\".\"XCL_011\" = 'January Speaker'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1462"
  ]
}
```

### Member Identifier XCL_035

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T2.\"XCL_032\" = 'School of Applied Sciences, Technology and Education'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_035\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r0\".\"XCL_042\" = \"r1\".\"XCL_030\" WHERE \"r1\".\"XCL_032\" = 'School of Applied Sciences, Technology and Education'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1375"
  ]
}
```

### Member Zip Code

```json
{
  "kind": "binding",
  "formula": "\"zip_code\".\"XCL_046\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_046\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_035\" = 'Adela' AND T1.\"XCL_036\" = 'O''Gallagher'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_046\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_046\" AS \"value\" FROM member AS \"r0\" INNER JOIN zip_code AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_043\" WHERE \"r0\".\"XCL_035\" = 'Adela' AND \"r0\".\"XCL_036\" = 'O''Gallagher'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1347"
  ]
}
```

### Sum of budget amount (XCL_005) for records where the budget category (XCL_004) is 'Speaker Gifts', aggregated by event identifier (XCL_011).

```json
{
  "kind": "metric",
  "formula": "SUM(\"budget\".\"XCL_005\")",
  "grain": [
    "\"event\".\"XCL_011\""
  ],
  "population_scope": "SELECT SUM(T1.\"XCL_005\"), T2.\"XCL_011\" FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T1.\"XCL_004\" = 'Speaker Gifts' GROUP BY T2.\"XCL_011\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r0\".\"XCL_005\")",
    "grain": [
      "\"r1\".\"XCL_011\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "budget"
      },
      {
        "role": "r1",
        "physical_table": "event"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_011\" AS \"grain_0\", SUM(\"r0\".\"XCL_005\") AS \"value\" FROM budget AS \"r0\" INNER JOIN event AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_010\" WHERE \"r0\".\"XCL_004\" = 'Speaker Gifts' GROUP BY \"r1\".\"XCL_011\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1467"
  ]
}
```

### Member Attribute XCL_036

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [
    "\"member\".\"XCL_035\"",
    "\"member\".\"XCL_036\"",
    "\"income\".\"XCL_027\""
  ],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\", T2.\"XCL_027\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" GROUP BY T1.\"XCL_035\", T1.\"XCL_036\", T2.\"XCL_027\" ORDER BY SUM(T2.\"XCL_026\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1388"
  ]
}
```

### Percentage of total expense amount (XCL_020) attributable to events labeled 'Yearly Kickoff' (XCL_011). The metric aggregates across the joined popula

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"event\".\"XCL_011\" = 'Yearly Kickoff' THEN \"expense\".\"XCL_020\" ELSE 0 END) AS REAL) * 100 / SUM(\"expense\".\"XCL_020\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T1.\"XCL_011\" = 'Yearly Kickoff' THEN T3.\"XCL_020\" ELSE 0 END) AS REAL) * 100 / SUM(T3.\"XCL_020\") FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r0\".\"XCL_011\" = 'Yearly Kickoff' THEN \"r2\".\"XCL_020\" ELSE 0 END) AS REAL) * 100 / SUM(\"r2\".\"XCL_020\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      },
      {
        "role": "r2",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r0\".\"XCL_011\" = 'Yearly Kickoff' THEN \"r2\".\"XCL_020\" ELSE 0 END) AS REAL) * 100 / SUM(\"r2\".\"XCL_020\") AS \"value\" FROM event AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" INNER JOIN expense AS \"r2\" ON \"r1\".\"XCL_003\" = \"r2\".\"XCL_023\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1390"
  ]
}
```

### "event"."XCL_011" = 'October Speaker'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'October Speaker'",
  "grain": [],
  "population_scope": "SELECT SUM(T2.\"XCL_007\") FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_011\" = 'October Speaker'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1337"
  ]
}
```

### DATE(SUBSTRING("expense"."XCL_019", 1, 10)) BETWEEN '2019-09-10' AND '2019-11-19' AND "expense"."XCL_020" > 20

```json
{
  "kind": "predicate",
  "formula": "DATE(SUBSTRING(\"expense\".\"XCL_019\", 1, 10)) BETWEEN '2019-09-10' AND '2019-11-19' AND \"expense\".\"XCL_020\" > 20",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_037\" FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE DATE(SUBSTRING(T2.\"XCL_019\", 1, 10)) BETWEEN '2019-09-10' AND '2019-11-19' AND T2.\"XCL_020\" > 20",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1440"
  ]
}
```

### "member"."XCL_035" = 'Carlo' AND "member"."XCL_036" = 'Jacobs'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_035\" = 'Carlo' AND \"member\".\"XCL_036\" = 'Jacobs'",
  "grain": [],
  "population_scope": "SELECT \"XCL_040\" FROM member WHERE \"XCL_035\" = 'Carlo' AND \"XCL_036\" = 'Jacobs'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1346"
  ]
}
```

### SUBSTRING("event"."XCL_012", 1, 4) = '2019'

```json
{
  "kind": "predicate",
  "formula": "SUBSTRING(\"event\".\"XCL_012\", 1, 4) = '2019'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN \"XCL_013\" = 'Community Service' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"XCL_013\") FROM event WHERE SUBSTRING(\"XCL_012\", 1, 4) = '2019'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1400"
  ]
}
```

### Attribute XCL_032 from the major table, representing a specific property of the 'Environmental Engineering' major.

```json
{
  "kind": "binding",
  "formula": "\"major\".\"XCL_032\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_036\", T1.\"XCL_032\", T1.\"XCL_033\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" WHERE T2.\"XCL_038\" = 'Member' AND T1.\"XCL_031\" = 'Environmental Engineering'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_032\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "major"
      },
      {
        "role": "r1",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_032\" AS \"value\" FROM major AS \"r0\" INNER JOIN member AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_042\" WHERE \"r1\".\"XCL_038\" = 'Member' AND \"r0\".\"XCL_031\" = 'Environmental Engineering'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1426"
  ]
}
```

### Member Attribute XCL_036

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [
    "\"attendance\".\"XCL_002\""
  ],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_034\" = T2.\"XCL_002\" GROUP BY T2.\"XCL_002\" HAVING COUNT(T2.\"XCL_001\") > 7",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_036\"",
    "grain": [
      "\"r1\".\"XCL_002\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "attendance"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_002\" AS \"grain_0\", \"r0\".\"XCL_036\" AS \"value\" FROM member AS \"r0\" INNER JOIN attendance AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_002\" GROUP BY \"r1\".\"XCL_002\" HAVING COUNT(\"r1\".\"XCL_001\") > 7",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1381"
  ]
}
```

### "member"."XCL_038" = 'President'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_038\" = 'President'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_034\") FROM member WHERE \"XCL_038\" = 'President'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1377"
  ]
}
```

### "major"."XCL_031" = 'Business' AND "major"."XCL_033" = 'College of Agriculture and Applied Sciences'

```json
{
  "kind": "predicate",
  "formula": "\"major\".\"XCL_031\" = 'Business' AND \"major\".\"XCL_033\" = 'College of Agriculture and Applied Sciences'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_040\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T2.\"XCL_031\" = 'Business' AND T2.\"XCL_033\" = 'College of Agriculture and Applied Sciences'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1439"
  ]
}
```

### Max XCL_007

```json
{
  "kind": "metric",
  "formula": "MAX(\"budget\".\"XCL_007\")",
  "grain": [],
  "population_scope": "SELECT MAX(\"XCL_007\") FROM budget",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MAX(\"r0\".\"XCL_007\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "budget"
      }
    ],
    "scope_sql": "SELECT MAX(\"r0\".\"XCL_007\") AS \"value\" FROM budget AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1406"
  ]
}
```

### Expense Attribute XCL_020

```json
{
  "kind": "binding",
  "formula": "\"expense\".\"XCL_020\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_035\", T2.\"XCL_036\", T1.\"XCL_020\" FROM expense AS T1 INNER JOIN member AS T2 ON T1.\"XCL_022\" = T2.\"XCL_034\" WHERE T1.\"XCL_018\" = 'Water, Veggie tray, supplies'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_020\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "expense"
      },
      {
        "role": "r1",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_020\" AS \"value\" FROM expense AS \"r0\" INNER JOIN member AS \"r1\" ON \"r0\".\"XCL_022\" = \"r1\".\"XCL_034\" WHERE \"r0\".\"XCL_018\" = 'Water, Veggie tray, supplies'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1460"
  ]
}
```

### "expense"."XCL_018" = 'Post Cards, Posters' AND "expense"."XCL_019" = '2019-08-20'

```json
{
  "kind": "predicate",
  "formula": "\"expense\".\"XCL_018\" = 'Post Cards, Posters' AND \"expense\".\"XCL_019\" = '2019-08-20'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_008\" FROM budget AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_003\" = T2.\"XCL_023\" WHERE T2.\"XCL_018\" = 'Post Cards, Posters' AND T2.\"XCL_019\" = '2019-08-20'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1350"
  ]
}
```

### Budget Identifier

```json
{
  "kind": "binding",
  "formula": "\"budget\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM expense AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_023\" = T2.\"XCL_003\" WHERE T1.\"XCL_018\" = 'Water, chips, cookies' ORDER BY T1.\"XCL_020\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1455"
  ]
}
```

### Member Identifier XCL_036

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_034\" = T2.\"XCL_002\" INNER JOIN event AS T3 ON T2.\"XCL_001\" = T3.\"XCL_010\" WHERE T3.\"XCL_011\" = 'Laugh Out Loud'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "attendance"
      },
      {
        "role": "r2",
        "physical_table": "event"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_036\" AS \"value\" FROM member AS \"r0\" INNER JOIN attendance AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_002\" INNER JOIN event AS \"r2\" ON \"r1\".\"XCL_001\" = \"r2\".\"XCL_010\" WHERE \"r2\".\"XCL_011\" = 'Laugh Out Loud'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1327"
  ]
}
```

### Member Identifier XCL_035

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_034\" = T2.\"XCL_002\" INNER JOIN event AS T3 ON T2.\"XCL_001\" = T3.\"XCL_010\" WHERE T3.\"XCL_011\" = 'Laugh Out Loud'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "attendance"
      },
      {
        "role": "r2",
        "physical_table": "event"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_035\" AS \"value\" FROM member AS \"r0\" INNER JOIN attendance AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_002\" INNER JOIN event AS \"r2\" ON \"r1\".\"XCL_001\" = \"r2\".\"XCL_010\" WHERE \"r2\".\"XCL_011\" = 'Laugh Out Loud'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1327"
  ]
}
```

### Calculates the percentage difference between the count of members associated with 'New Jersey' and 'Vermont' (via zip_code state), relative to the tot

```json
{
  "kind": "metric",
  "formula": "CAST((SUM(CASE WHEN \"zip_code\".\"XCL_047\" = 'New Jersey' THEN 1 ELSE 0 END) - SUM(CASE WHEN \"zip_code\".\"XCL_047\" = 'Vermont' THEN 1 ELSE 0 END)) AS REAL) * 100 / COUNT(\"member\".\"XCL_034\")",
  "grain": [],
  "population_scope": "SELECT CAST((SUM(CASE WHEN T2.\"XCL_047\" = 'New Jersey' THEN 1 ELSE 0 END) - SUM(CASE WHEN T2.\"XCL_047\" = 'Vermont' THEN 1 ELSE 0 END)) AS REAL) * 100 / COUNT(T1.\"XCL_034\") AS diff FROM member AS T1 INNER JOIN zip_code AS T2 ON T2.\"XCL_043\" = T1.\"XCL_041\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST((SUM(CASE WHEN \"r1\".\"XCL_047\" = 'New Jersey' THEN 1 ELSE 0 END) - SUM(CASE WHEN \"r1\".\"XCL_047\" = 'Vermont' THEN 1 ELSE 0 END)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_034\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT CAST((SUM(CASE WHEN \"r1\".\"XCL_047\" = 'New Jersey' THEN 1 ELSE 0 END) - SUM(CASE WHEN \"r1\".\"XCL_047\" = 'Vermont' THEN 1 ELSE 0 END)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_034\") AS \"value\" FROM member AS \"r0\" INNER JOIN zip_code AS \"r1\" ON \"r1\".\"XCL_043\" = \"r0\".\"XCL_041\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1458"
  ]
}
```

### "member"."XCL_042" = 'rec1N0upiVLy5esTO' AND "member"."XCL_035" = 'Katy'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_042\" = 'rec1N0upiVLy5esTO' AND \"member\".\"XCL_035\" = 'Katy'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_033\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T1.\"XCL_042\" = 'rec1N0upiVLy5esTO' AND T1.\"XCL_035\" = 'Katy'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1438"
  ]
}
```

### "member"."XCL_039" = 'X-Large'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_039\" = 'X-Large'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_018\" FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T1.\"XCL_039\" = 'X-Large'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1412"
  ]
}
```

### Aggregated sum of the XCL_005 column from the budget table, restricted to rows where XCL_004 equals 'Food'. Returns a single scalar value representing

```json
{
  "kind": "metric",
  "formula": "SUM(\"budget\".\"XCL_005\")",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_005\") FROM budget WHERE \"XCL_004\" = 'Food'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r0\".\"XCL_005\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "budget"
      }
    ],
    "scope_sql": "SELECT SUM(\"r0\".\"XCL_005\") AS \"value\" FROM budget AS \"r0\" WHERE \"r0\".\"XCL_004\" = 'Food'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1380"
  ]
}
```

### "major"."XCL_033" = 'College of Humanities and Social Sciences'

```json
{
  "kind": "predicate",
  "formula": "\"major\".\"XCL_033\" = 'College of Humanities and Social Sciences'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_031\") FROM major WHERE \"XCL_033\" = 'College of Humanities and Social Sciences'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1345"
  ]
}
```

### "member"."XCL_035" = 'Sacha' AND "member"."XCL_036" = 'Harrison' AND SUBSTRING("event"."XCL_012", 1, 4) = '2019'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_035\" = 'Sacha' AND \"member\".\"XCL_036\" = 'Harrison' AND SUBSTRING(\"event\".\"XCL_012\", 1, 4) = '2019'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_010\") FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" INNER JOIN member AS T3 ON T2.\"XCL_002\" = T3.\"XCL_034\" WHERE T3.\"XCL_035\" = 'Sacha' AND T3.\"XCL_036\" = 'Harrison' AND SUBSTRING(T1.\"XCL_012\", 1, 4) = '2019'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1321"
  ]
}
```

### Member Identifier

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_036\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T2.\"XCL_031\" = 'Law and Constitutional Studies'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_036\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r0\".\"XCL_042\" = \"r1\".\"XCL_030\" WHERE \"r1\".\"XCL_031\" = 'Law and Constitutional Studies'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1328"
  ]
}
```

### "expense"."XCL_019" = '2019-09-10' AND "expense"."XCL_018" = 'Pizza'

```json
{
  "kind": "predicate",
  "formula": "\"expense\".\"XCL_019\" = '2019-09-10' AND \"expense\".\"XCL_018\" = 'Pizza'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_036\", T1.\"XCL_038\" FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T2.\"XCL_019\" = '2019-09-10' AND T2.\"XCL_018\" = 'Pizza'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1430"
  ]
}
```

### Expense Attribute XCL_018

```json
{
  "kind": "binding",
  "formula": "\"expense\".\"XCL_018\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_017\", T2.\"XCL_018\" FROM member AS T1 INNER JOIN expense AS T2 ON T1.\"XCL_034\" = T2.\"XCL_022\" WHERE T1.\"XCL_038\" = 'Vice President'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_018\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_018\" AS \"value\" FROM member AS \"r0\" INNER JOIN expense AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_022\" WHERE \"r0\".\"XCL_038\" = 'Vice President'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1370"
  ]
}
```

### Distinct value of member column XCL_036 for members who attended an event and have an income record dated '2019-09-09'.

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_035\", T3.\"XCL_036\", T4.\"XCL_026\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" INNER JOIN member AS T3 ON T3.\"XCL_034\" = T2.\"XCL_002\" INNER JOIN income AS T4 ON T4.\"XCL_029\" = T3.\"XCL_034\" WHERE T4.\"XCL_025\" = '2019-09-09'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1464"
  ]
}
```

### SUBSTRING("event"."XCL_012", 1, 4) = '2020' AND "event"."XCL_013" = 'Meeting'

```json
{
  "kind": "predicate",
  "formula": "SUBSTRING(\"event\".\"XCL_012\", 1, 4) = '2020' AND \"event\".\"XCL_013\" = 'Meeting'",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(T2.\"XCL_001\") AS REAL) / COUNT(DISTINCT T2.\"XCL_001\") FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" WHERE SUBSTRING(T1.\"XCL_012\", 1, 4) = '2020' AND T1.\"XCL_013\" = 'Meeting'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1324"
  ]
}
```

### "major"."XCL_031" = 'Business' AND "member"."XCL_039" = 'Medium'

```json
{
  "kind": "predicate",
  "formula": "\"major\".\"XCL_031\" = 'Business' AND \"member\".\"XCL_039\" = 'Medium'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_034\") FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T2.\"XCL_031\" = 'Business' AND T1.\"XCL_039\" = 'Medium'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1352"
  ]
}
```

### "member"."XCL_035" = 'Tyler' AND "member"."XCL_036" = 'Hewitt'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_035\" = 'Tyler' AND \"member\".\"XCL_036\" = 'Hewitt'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_033\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_035\" = 'Tyler' AND T1.\"XCL_036\" = 'Hewitt'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1330"
  ]
}
```

### Member Identifier XCL_036

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T2.\"XCL_032\" = 'School of Applied Sciences, Technology and Education'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_036\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r0\".\"XCL_042\" = \"r1\".\"XCL_030\" WHERE \"r1\".\"XCL_032\" = 'School of Applied Sciences, Technology and Education'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1375"
  ]
}
```

### Expense Amount

```json
{
  "kind": "binding",
  "formula": "\"expense\".\"XCL_020\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_020\" FROM expense WHERE \"XCL_018\" = 'Posters' AND \"XCL_019\" = '2019-09-04'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_020\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_020\" AS \"value\" FROM expense AS \"r0\" WHERE \"r0\".\"XCL_018\" = 'Posters' AND \"r0\".\"XCL_019\" = '2019-09-04'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1342"
  ]
}
```

### AVG("expense"."XCL_020") > 50

```json
{
  "kind": "predicate",
  "formula": "AVG(\"expense\".\"XCL_020\") > 50",
  "grain": [
    "\"expense\".\"XCL_018\""
  ],
  "population_scope": "SELECT \"XCL_018\" FROM expense GROUP BY \"XCL_018\" HAVING AVG(\"XCL_020\") > 50",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1444"
  ]
}
```

### "member"."XCL_035" = 'Maya' AND "member"."XCL_036" = 'Mclean'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_035\" = 'Maya' AND \"member\".\"XCL_036\" = 'Mclean'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_011\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" INNER JOIN member AS T3 ON T2.\"XCL_002\" = T3.\"XCL_034\" WHERE T3.\"XCL_035\" = 'Maya' AND T3.\"XCL_036\" = 'Mclean'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1320"
  ]
}
```

### Major Attribute XCL_032

```json
{
  "kind": "binding",
  "formula": "\"major\".\"XCL_032\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_031\", T2.\"XCL_032\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T1.\"XCL_035\" = 'Garrett' AND T1.\"XCL_036\" = 'Gerke'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_032\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_032\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r1\".\"XCL_030\" = \"r0\".\"XCL_042\" WHERE \"r0\".\"XCL_035\" = 'Garrett' AND \"r0\".\"XCL_036\" = 'Gerke'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1459"
  ]
}
```

### "budget"."XCL_004" = 'Food'

```json
{
  "kind": "predicate",
  "formula": "\"budget\".\"XCL_004\" = 'Food'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_011\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T2.\"XCL_004\" = 'Food'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1463"
  ]
}
```

### "member"."XCL_038" = 'Member' AND "member"."XCL_039" = 'X-Large'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_038\" = 'Member' AND \"member\".\"XCL_039\" = 'X-Large'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_034\") FROM member WHERE \"XCL_038\" = 'Member' AND \"XCL_039\" = 'X-Large'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1424"
  ]
}
```

### Distinct value of income column XCL_026 for income records dated '2019-09-09' associated with members who attended an event.

```json
{
  "kind": "binding",
  "formula": "\"income\".\"XCL_026\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_035\", T3.\"XCL_036\", T4.\"XCL_026\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" INNER JOIN member AS T3 ON T3.\"XCL_034\" = T2.\"XCL_002\" INNER JOIN income AS T4 ON T4.\"XCL_029\" = T3.\"XCL_034\" WHERE T4.\"XCL_025\" = '2019-09-09'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1464"
  ]
}
```

### Member Identifier XCL_040

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_040\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_040\" FROM member WHERE \"XCL_035\" = 'Carlo' AND \"XCL_036\" = 'Jacobs'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_040\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_040\" AS \"value\" FROM member AS \"r0\" WHERE \"r0\".\"XCL_035\" = 'Carlo' AND \"r0\".\"XCL_036\" = 'Jacobs'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1346"
  ]
}
```

### Calculates the percentage of records where the major type (XCL_031) is 'Business' relative to the total count of member identifiers (XCL_034). The pop

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"major\".\"XCL_031\" = 'Business' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"member\".\"XCL_034\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_031\" = 'Business' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_034\") FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T1.\"XCL_038\" = 'Member'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r1\".\"XCL_031\" = 'Business' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_034\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r1\".\"XCL_031\" = 'Business' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_034\") AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r1\".\"XCL_030\" = \"r0\".\"XCL_042\" WHERE \"r0\".\"XCL_038\" = 'Member'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1421"
  ]
}
```

### Member Attribute XCL_040

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_040\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_036\", T1.\"XCL_040\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T2.\"XCL_031\" = 'Elementary Education'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_040\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_040\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r1\".\"XCL_030\" = \"r0\".\"XCL_042\" WHERE \"r1\".\"XCL_031\" = 'Elementary Education'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1461"
  ]
}
```

### Value of column XCL_046 from the zip_code table for the member identified by first name 'Amy' and last name 'Firth'.

```json
{
  "kind": "binding",
  "formula": "\"zip_code\".\"XCL_046\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_045\", T2.\"XCL_046\", T2.\"XCL_047\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_035\" = 'Amy' AND T1.\"XCL_036\" = 'Firth'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_046\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_046\" AS \"value\" FROM member AS \"r0\" INNER JOIN zip_code AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_043\" WHERE \"r0\".\"XCL_035\" = 'Amy' AND \"r0\".\"XCL_036\" = 'Firth'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1364"
  ]
}
```

### Event Identifier

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" FROM attendance AS T1 INNER JOIN event AS T2 ON T2.\"XCL_010\" = T1.\"XCL_001\" INNER JOIN member AS T3 ON T1.\"XCL_002\" = T3.\"XCL_034\" WHERE T3.\"XCL_038\" = 'Vice President' AND T2.\"XCL_015\" = '900 E. Washington St.' AND T2.\"XCL_013\" = 'Social'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_011\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "attendance"
      },
      {
        "role": "r1",
        "physical_table": "event"
      },
      {
        "role": "r2",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_011\" AS \"value\" FROM attendance AS \"r0\" INNER JOIN event AS \"r1\" ON \"r1\".\"XCL_010\" = \"r0\".\"XCL_001\" INNER JOIN member AS \"r2\" ON \"r0\".\"XCL_002\" = \"r2\".\"XCL_034\" WHERE \"r2\".\"XCL_038\" = 'Vice President' AND \"r1\".\"XCL_015\" = '900 E. Washington St.' AND \"r1\".\"XCL_013\" = 'Social'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1429"
  ]
}
```

### Member Attribute

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_035\", T2.\"XCL_036\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" INNER JOIN attendance AS T3 ON T2.\"XCL_034\" = T3.\"XCL_002\" INNER JOIN event AS T4 ON T3.\"XCL_001\" = T4.\"XCL_010\" WHERE T4.\"XCL_011\" = 'Community Theater' AND T1.\"XCL_031\" = 'Interior Design'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "major"
      },
      {
        "role": "r1",
        "physical_table": "member"
      },
      {
        "role": "r2",
        "physical_table": "attendance"
      },
      {
        "role": "r3",
        "physical_table": "event"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_036\" AS \"value\" FROM major AS \"r0\" INNER JOIN member AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_042\" INNER JOIN attendance AS \"r2\" ON \"r1\".\"XCL_034\" = \"r2\".\"XCL_002\" INNER JOIN event AS \"r3\" ON \"r2\".\"XCL_001\" = \"r3\".\"XCL_010\" WHERE \"r3\".\"XCL_011\" = 'Community Theater' AND \"r0\".\"XCL_031\" = 'Interior Design'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1382"
  ]
}
```

### Aggregates the total number of member records (counting XCL_034) that are associated with majors in the 'College of Education & Human Services' where 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"member\".\"XCL_034\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_034\") FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T1.\"XCL_038\" = 'Member' AND T2.\"XCL_031\" LIKE '%Education%' AND T2.\"XCL_033\" = 'College of Education & Human Services'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_034\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_034\") AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r1\".\"XCL_030\" = \"r0\".\"XCL_042\" WHERE \"r0\".\"XCL_038\" = 'Member' AND \"r1\".\"XCL_031\" LIKE '%Education%' AND \"r1\".\"XCL_033\" = 'College of Education & Human Services'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1441"
  ]
}
```

### "member"."XCL_038" = 'President'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_038\" = 'President'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_032\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_038\" = 'President'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1356"
  ]
}
```

### Member Identifier 1

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T2.\"XCL_027\" = 'Dues' ORDER BY T2.\"XCL_025\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1358"
  ]
}
```

### "income"."XCL_027" = 'Fundraising' AND "income"."XCL_025" = '2019-09-14'

```json
{
  "kind": "predicate",
  "formula": "\"income\".\"XCL_027\" = 'Fundraising' AND \"income\".\"XCL_025\" = '2019-09-14'",
  "grain": [],
  "population_scope": "SELECT \"XCL_028\" FROM income WHERE \"XCL_027\" = 'Fundraising' AND \"XCL_025\" = '2019-09-14'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1344"
  ]
}
```

### Major Identifier

```json
{
  "kind": "binding",
  "formula": "\"major\".\"XCL_032\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_032\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_038\" = 'President'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_032\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_032\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r0\".\"XCL_042\" = \"r1\".\"XCL_030\" WHERE \"r0\".\"XCL_038\" = 'President'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1356"
  ]
}
```

### Meeting Expense Share

```json
{
  "kind": "metric",
  "formula": "SUM(CASE WHEN \"event\".\"XCL_013\" = 'Meeting' THEN \"expense\".\"XCL_020\" ELSE 0 END) * 100 / SUM(\"expense\".\"XCL_020\")",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN T1.\"XCL_013\" = 'Meeting' THEN T3.\"XCL_020\" ELSE 0 END) * 100 / SUM(T3.\"XCL_020\") FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(CASE WHEN \"r0\".\"XCL_013\" = 'Meeting' THEN \"r2\".\"XCL_020\" ELSE 0 END) * 100 / SUM(\"r2\".\"XCL_020\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      },
      {
        "role": "r2",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT SUM(CASE WHEN \"r0\".\"XCL_013\" = 'Meeting' THEN \"r2\".\"XCL_020\" ELSE 0 END) * 100 / SUM(\"r2\".\"XCL_020\") AS \"value\" FROM event AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" INNER JOIN expense AS \"r2\" ON \"r1\".\"XCL_003\" = \"r2\".\"XCL_023\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1454"
  ]
}
```

### Major Identifier

```json
{
  "kind": "binding",
  "formula": "\"major\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_031\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" WHERE T2.\"XCL_038\" = 'Vice President'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_031\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "major"
      },
      {
        "role": "r1",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_031\" AS \"value\" FROM major AS \"r0\" INNER JOIN member AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_042\" WHERE \"r1\".\"XCL_038\" = 'Vice President'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1420"
  ]
}
```

### Income Amount

```json
{
  "kind": "binding",
  "formula": "\"income\".\"XCL_028\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_028\" FROM income WHERE \"XCL_027\" = 'Fundraising' AND \"XCL_025\" = '2019-09-14'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_028\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "income"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_028\" AS \"value\" FROM income AS \"r0\" WHERE \"r0\".\"XCL_027\" = 'Fundraising' AND \"r0\".\"XCL_025\" = '2019-09-14'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1344"
  ]
}
```

### "major"."XCL_033" = 'College of Humanities and Social Sciences'

```json
{
  "kind": "predicate",
  "formula": "\"major\".\"XCL_033\" = 'College of Humanities and Social Sciences'",
  "grain": [],
  "population_scope": "SELECT \"XCL_032\" FROM major WHERE \"XCL_033\" = 'College of Humanities and Social Sciences'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1363"
  ]
}
```

### "expense"."XCL_018" = 'Posters' AND "expense"."XCL_019" = '2019-09-04'

```json
{
  "kind": "predicate",
  "formula": "\"expense\".\"XCL_018\" = 'Posters' AND \"expense\".\"XCL_019\" = '2019-09-04'",
  "grain": [],
  "population_scope": "SELECT \"XCL_020\" FROM expense WHERE \"XCL_018\" = 'Posters' AND \"XCL_019\" = '2019-09-04'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1342"
  ]
}
```

### Value of column XCL_047 from the zip_code table for members with role 'President'.

```json
{
  "kind": "binding",
  "formula": "\"zip_code\".\"XCL_047\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_045\", T2.\"XCL_047\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_038\" = 'President'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_047\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_047\" AS \"value\" FROM member AS \"r0\" INNER JOIN zip_code AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_043\" WHERE \"r0\".\"XCL_038\" = 'President'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1333"
  ]
}
```

### Major Identifier

```json
{
  "kind": "binding",
  "formula": "\"major\".\"XCL_033\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_033\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_038\" LIKE 'vice president'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_033\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_033\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r0\".\"XCL_042\" = \"r1\".\"XCL_030\" WHERE \"r0\".\"XCL_038\" LIKE 'vice president'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1319"
  ]
}
```

### Event ID for Meetings

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_011\" FROM event AS T1 WHERE T1.\"XCL_013\" = 'Meeting'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_011\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_011\" AS \"value\" FROM event AS \"r0\" WHERE \"r0\".\"XCL_013\" = 'Meeting'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1322"
  ]
}
```

### Counts the number of members (T2) associated with the 'Physics Teaching' major (T1). The population is restricted to members linked via the join condi

```json
{
  "kind": "metric",
  "formula": "COUNT(\"member\".\"XCL_034\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_034\") FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" WHERE T1.\"XCL_031\" = 'Physics Teaching'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_034\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "major"
      },
      {
        "role": "r1",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_034\") AS \"value\" FROM major AS \"r0\" INNER JOIN member AS \"r1\" ON \"r0\".\"XCL_030\" = \"r1\".\"XCL_042\" WHERE \"r0\".\"XCL_031\" = 'Physics Teaching'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1394"
  ]
}
```

### "budget"."XCL_004" = 'Advertisement' AND "event"."XCL_013" = 'Meeting'

```json
{
  "kind": "predicate",
  "formula": "\"budget\".\"XCL_004\" = 'Advertisement' AND \"event\".\"XCL_013\" = 'Meeting'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_011\" = 'Yearly Kickoff' THEN T1.\"XCL_007\" ELSE 0 END) AS REAL) / SUM(CASE WHEN T2.\"XCL_011\" = 'October Meeting' THEN T1.\"XCL_007\" ELSE 0 END) FROM budget AS T1 INNER JOIN event AS T2 ON T1.\"XCL_009\" = T2.\"XCL_010\" WHERE T1.\"XCL_004\" = 'Advertisement' AND T2.\"XCL_013\" = 'Meeting'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1359"
  ]
}
```

### Event Identifier

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_015\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_015\" FROM event WHERE \"XCL_011\" = 'Spring Budget Review'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_015\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_015\" AS \"value\" FROM event AS \"r0\" WHERE \"r0\".\"XCL_011\" = 'Spring Budget Review'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1341"
  ]
}
```

### Budget Identifier

```json
{
  "kind": "binding",
  "formula": "\"budget\".\"XCL_004\"",
  "grain": [
    "\"budget\".\"XCL_004\""
  ],
  "population_scope": "SELECT T2.\"XCL_004\", SUM(T2.\"XCL_007\") FROM event AS T1 JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_011\" = 'April Speaker' GROUP BY T2.\"XCL_004\" ORDER BY SUM(T2.\"XCL_007\") ASC",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_004\"",
    "grain": [
      "\"r1\".\"XCL_004\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_004\" AS \"grain_0\", \"r1\".\"XCL_004\" AS \"value\" FROM event AS \"r0\" JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" WHERE \"r0\".\"XCL_011\" = 'April Speaker' GROUP BY \"r1\".\"XCL_004\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1405"
  ]
}
```

### Event Attribute XCL_012

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_012\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_011\", T1.\"XCL_012\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" WHERE T3.\"XCL_018\" = 'Pizza' AND T3.\"XCL_020\" > 50 AND T3.\"XCL_020\" < 100",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_012\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "budget"
      },
      {
        "role": "r2",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_012\" AS \"value\" FROM event AS \"r0\" INNER JOIN budget AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_009\" INNER JOIN expense AS \"r2\" ON \"r1\".\"XCL_003\" = \"r2\".\"XCL_023\" WHERE \"r2\".\"XCL_018\" = 'Pizza' AND \"r2\".\"XCL_020\" > 50 AND \"r2\".\"XCL_020\" < 100",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1448"
  ]
}
```

### Member Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"member\".\"XCL_034\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_034\") FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T2.\"XCL_033\" = 'College of Engineering'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_034\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_034\") AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r0\".\"XCL_042\" = \"r1\".\"XCL_030\" WHERE \"r1\".\"XCL_033\" = 'College of Engineering'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1313"
  ]
}
```

### "member"."XCL_036" = 'Pierce' OR "member"."XCL_036" = 'Guidi'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_036\" = 'Pierce' OR \"member\".\"XCL_036\" = 'Guidi'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_032\" FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T1.\"XCL_036\" = 'Pierce' OR T1.\"XCL_036\" = 'Guidi'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1336"
  ]
}
```

### Average Expense Amount

```json
{
  "kind": "metric",
  "formula": "AVG(\"expense\".\"XCL_020\")",
  "grain": [],
  "population_scope": "SELECT AVG(\"XCL_020\") FROM expense",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_020\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "expense"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_020\") AS \"value\" FROM expense AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1453"
  ]
}
```

### "event"."XCL_015" = 'MU 215' AND "budget"."XCL_005" = 0 AND "event"."XCL_013" = 'Guest Speaker'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_015\" = 'MU 215' AND \"budget\".\"XCL_005\" = 0 AND \"event\".\"XCL_013\" = 'Guest Speaker'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_004\", T1.\"XCL_013\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_015\" = 'MU 215' AND T2.\"XCL_005\" = 0 AND T1.\"XCL_013\" = 'Guest Speaker'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1427"
  ]
}
```

### Attendance Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"attendance\".\"XCL_002\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_002\") FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" WHERE T1.\"XCL_011\" = 'Community Theater' AND SUBSTRING(T1.\"XCL_012\", 1, 4) = '2019'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_002\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "attendance"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_002\") AS \"value\" FROM event AS \"r0\" INNER JOIN attendance AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_001\" WHERE \"r0\".\"XCL_011\" = 'Community Theater' AND SUBSTRING(\"r0\".\"XCL_012\", 1, 4) = '2019'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1395"
  ]
}
```

### Income Amount

```json
{
  "kind": "binding",
  "formula": "\"income\".\"XCL_025\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_025\" FROM member AS T1 INNER JOIN income AS T2 ON T1.\"XCL_034\" = T2.\"XCL_029\" WHERE T1.\"XCL_035\" = 'Connor' AND T1.\"XCL_036\" = 'Hilton' AND T2.\"XCL_027\" = 'Dues'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_025\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "income"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_025\" AS \"value\" FROM member AS \"r0\" INNER JOIN income AS \"r1\" ON \"r0\".\"XCL_034\" = \"r1\".\"XCL_029\" WHERE \"r0\".\"XCL_035\" = 'Connor' AND \"r0\".\"XCL_036\" = 'Hilton' AND \"r1\".\"XCL_027\" = 'Dues'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1357"
  ]
}
```

### "member"."XCL_038" = 'Vice President'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_038\" = 'Vice President'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_031\" FROM major AS T1 INNER JOIN member AS T2 ON T1.\"XCL_030\" = T2.\"XCL_042\" WHERE T2.\"XCL_038\" = 'Vice President'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1420"
  ]
}
```

### "event"."XCL_011" = 'October Meeting'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'October Meeting'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_034\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" INNER JOIN member AS T3 ON T2.\"XCL_002\" = T3.\"XCL_034\" WHERE T1.\"XCL_011\" = 'October Meeting'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1366"
  ]
}
```

### "major"."XCL_031" = 'Environmental Engineering'

```json
{
  "kind": "predicate",
  "formula": "\"major\".\"XCL_031\" = 'Environmental Engineering'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_034\") FROM member AS T1 INNER JOIN major AS T2 ON T1.\"XCL_042\" = T2.\"XCL_030\" WHERE T2.\"XCL_031\" = 'Environmental Engineering'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1326"
  ]
}
```

### Aggregates the total number of non-null values in the XCL_024 column from the income table, restricted to rows where XCL_026 equals 50. Returns a sing

```json
{
  "kind": "metric",
  "formula": "COUNT(\"income\".\"XCL_024\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_024\") FROM income WHERE \"XCL_026\" = 50",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_024\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "income"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_024\") AS \"value\" FROM income AS \"r0\" WHERE \"r0\".\"XCL_026\" = 50",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1423"
  ]
}
```

### Aggregates the count of event identifiers (XCL_010) from the event table, filtered to events where the sport is 'Women's Soccer' and the associated me

```json
{
  "kind": "metric",
  "formula": "COUNT(\"event\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_010\") FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" INNER JOIN member AS T3 ON T2.\"XCL_002\" = T3.\"XCL_034\" WHERE T1.\"XCL_011\" = 'Women''s Soccer' AND T3.\"XCL_039\" = 'Medium'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "event"
      },
      {
        "role": "r1",
        "physical_table": "attendance"
      },
      {
        "role": "r2",
        "physical_table": "member"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_010\") AS \"value\" FROM event AS \"r0\" INNER JOIN attendance AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_001\" INNER JOIN member AS \"r2\" ON \"r1\".\"XCL_002\" = \"r2\".\"XCL_034\" WHERE \"r0\".\"XCL_011\" = 'Women''s Soccer' AND \"r2\".\"XCL_039\" = 'Medium'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1317"
  ]
}
```

### Member Attribute XCL_035

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T2.\"XCL_047\" = 'Illinois'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "zip_code"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_035\" AS \"value\" FROM member AS \"r0\" INNER JOIN zip_code AS \"r1\" ON \"r0\".\"XCL_041\" = \"r1\".\"XCL_043\" WHERE \"r1\".\"XCL_047\" = 'Illinois'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1334"
  ]
}
```

### Distinct values of the event category (XCL_013) from the event table, filtered to records where XCL_015 is 'MU 215' and XCL_013 is 'Guest Speaker', li

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_013\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_004\", T1.\"XCL_013\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T1.\"XCL_015\" = 'MU 215' AND T2.\"XCL_005\" = 0 AND T1.\"XCL_013\" = 'Guest Speaker'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1427"
  ]
}
```

### Distinct value of column XCL_036 from the member table, representing a member attribute for those with qualifying expenses.

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_035\", T1.\"XCL_036\", T2.\"XCL_031\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" INNER JOIN expense AS T3 ON T1.\"XCL_034\" = T3.\"XCL_022\" WHERE T3.\"XCL_020\" > 100",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1449"
  ]
}
```

### "expense"."XCL_018" = 'Parking'

```json
{
  "kind": "predicate",
  "formula": "\"expense\".\"XCL_018\" = 'Parking'",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_020\") FROM expense WHERE \"XCL_018\" = 'Parking'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1408"
  ]
}
```

### Distinct values of the event attribute XCL_015 for events linked to budgets with a positive XCL_006 value.

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_015\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_011\", T1.\"XCL_015\" FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" WHERE T2.\"XCL_006\" > 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1447"
  ]
}
```

### "event"."XCL_013" = 'Fundraiser'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_013\" = 'Fundraiser'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_011\" FROM event AS T1 WHERE T1.\"XCL_013\" = 'Fundraiser'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1323"
  ]
}
```

### "event"."XCL_011" = 'Women''s Soccer'

```json
{
  "kind": "predicate",
  "formula": "\"event\".\"XCL_011\" = 'Women''s Soccer'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_010\") FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" WHERE T1.\"XCL_011\" = 'Women''s Soccer'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1315"
  ]
}
```

### Distinct member identifiers (XCL_034) associated with attendance records for the event named 'October Meeting'. Grain: unique member.

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_034\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_034\" FROM event AS T1 INNER JOIN attendance AS T2 ON T1.\"XCL_010\" = T2.\"XCL_001\" INNER JOIN member AS T3 ON T2.\"XCL_002\" = T3.\"XCL_034\" WHERE T1.\"XCL_011\" = 'October Meeting'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1366"
  ]
}
```

### Distinct values of the zip code identifier (XCL_045) from the zip_code table, filtered to locations associated with members having income records wher

```json
{
  "kind": "binding",
  "formula": "\"zip_code\".\"XCL_045\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_045\", T3.\"XCL_046\" FROM income AS T1 INNER JOIN member AS T2 ON T1.\"XCL_029\" = T2.\"XCL_034\" INNER JOIN zip_code AS T3 ON T3.\"XCL_043\" = T2.\"XCL_041\" WHERE T1.\"XCL_026\" > 40",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1450"
  ]
}
```

### Member Attribute XCL_035

```json
{
  "kind": "binding",
  "formula": "\"member\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T1.\"XCL_036\", \"XCL_033\" FROM member AS T1 INNER JOIN major AS T2 ON T2.\"XCL_030\" = T1.\"XCL_042\" WHERE T1.\"XCL_038\" = 'Secretary'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "member"
      },
      {
        "role": "r1",
        "physical_table": "major"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_035\" AS \"value\" FROM member AS \"r0\" INNER JOIN major AS \"r1\" ON \"r1\".\"XCL_030\" = \"r0\".\"XCL_042\" WHERE \"r0\".\"XCL_038\" = 'Secretary'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1466"
  ]
}
```

### "member"."XCL_035" = 'Amy' AND "member"."XCL_036" = 'Firth'

```json
{
  "kind": "predicate",
  "formula": "\"member\".\"XCL_035\" = 'Amy' AND \"member\".\"XCL_036\" = 'Firth'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_045\", T2.\"XCL_046\", T2.\"XCL_047\" FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.\"XCL_041\" = T2.\"XCL_043\" WHERE T1.\"XCL_035\" = 'Amy' AND T1.\"XCL_036\" = 'Firth'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1364"
  ]
}
```

### Event Identifier

```json
{
  "kind": "binding",
  "formula": "\"event\".\"XCL_013\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_013\", SUM(T3.\"XCL_020\") FROM event AS T1 INNER JOIN budget AS T2 ON T1.\"XCL_010\" = T2.\"XCL_009\" INNER JOIN expense AS T3 ON T2.\"XCL_003\" = T3.\"XCL_023\" WHERE T1.\"XCL_011\" = 'October Meeting'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1404"
  ]
}
```


## 增量维护事件

- Recorded alias revision · event.XCL_012 · Archived superseded_alias_hypotheses → archived aliases
  - event.XCL_012: event_date → event_datetime
