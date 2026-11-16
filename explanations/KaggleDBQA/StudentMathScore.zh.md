# KaggleDBQA / StudentMathScore — Schema 与业务口径解释

该数据库的存档目录包含 3 张表、15 个物理列、1 条关系，以及 21 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## XTB_001

该表的存档未记录额外业务说明。

恢复表名: finrev fed 17
SQL表别名: T1, f, t1

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| XTB_001.XCL_007 | c14 / Federal Revenue | number | kaggledbqa:fewshot:StudentMathScore:004 |
| XTB_001.XCL_008 | c25 | number | — |
| XTB_001.XCL_002 | idcensus / Census ID | number | — |
| XTB_001.XCL_004 | nces id | text | — |
| XTB_001.XCL_003 | school district / school_district | text | kaggledbqa:fewshot:StudentMathScore:001 |
| XTB_001.XCL_001 | state code | number | kaggledbqa:fewshot:StudentMathScore:000, kaggledbqa:fewshot:StudentMathScore:001 |
| XTB_001.XCL_006 | t fed rev / Federal Revenue | number | kaggledbqa:fewshot:StudentMathScore:000 |
| XTB_001.XCL_005 | yr data / data_year | number | kaggledbqa:fewshot:StudentMathScore:004 |

## XTB_002

该表的存档未记录额外业务说明。

恢复表名: finrev fed key 17
SQL表别名: T2, s, t2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| XTB_002.XCL_011 | records / record_count | text | — |
| XTB_002.XCL_010 | state | text | kaggledbqa:fewshot:StudentMathScore:000, kaggledbqa:fewshot:StudentMathScore:001 |
| XTB_002.XCL_009 | state code | number | kaggledbqa:fewshot:StudentMathScore:000, kaggledbqa:fewshot:StudentMathScore:001 |

## XTB_003

该表的存档未记录额外业务说明。

恢复表名: ndecore excel math grade8
SQL表别名: T3, m, s

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| XTB_003.XCL_014 | all students / student_subset | text | — |
| XTB_003.XCL_015 | average scale score / average_scale_score | number | kaggledbqa:fewshot:StudentMathScore:007, kaggledbqa:fewshot:StudentMathScore:008 |
| XTB_003.XCL_013 | state | text | kaggledbqa:fewshot:StudentMathScore:007, kaggledbqa:fewshot:StudentMathScore:002 |
| XTB_003.XCL_012 | year / assessment_year | number | kaggledbqa:fewshot:StudentMathScore:002 |

## 表关系与连接依据

- XTB_001.XCL_001 ↔ XTB_002.XCL_009; target_disjoint_historical_join

## 业务口径、总体与粒度

### SELECT AVG("XCL_015") FROM "XTB_003"

```json
{
  "kind": "program",
  "formula": "SELECT AVG(\"XCL_015\") FROM \"XTB_003\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:StudentMathScore:008"
  ]
}
```

### SELECT T2."XCL_010" FROM "XTB_001" AS T1 JOIN "XTB_002" AS T2 ON T1."XCL_001" = T2."XCL_009" GROUP BY T2."XCL_010" ORDER BY COUNT("XCL_003") DESC LIMI

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_010\" FROM \"XTB_001\" AS T1 JOIN \"XTB_002\" AS T2 ON T1.\"XCL_001\" = T2.\"XCL_009\" GROUP BY T2.\"XCL_010\" ORDER BY COUNT(\"XCL_003\") DESC LIMIT 5",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:StudentMathScore:001"
  ]
}
```

### SELECT SUM("XCL_007") FROM "XTB_001" WHERE "XCL_005" = 17

```json
{
  "kind": "program",
  "formula": "SELECT SUM(\"XCL_007\") FROM \"XTB_001\" WHERE \"XCL_005\" = 17",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:StudentMathScore:004"
  ]
}
```

### SELECT T2."XCL_010" FROM "XTB_002" AS T2 JOIN "XTB_001" AS T1 ON T1."XCL_001" = T2."XCL_009" GROUP BY T1."XCL_001" ORDER BY SUM("XCL_006")

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_010\" FROM \"XTB_002\" AS T2 JOIN \"XTB_001\" AS T1 ON T1.\"XCL_001\" = T2.\"XCL_009\" GROUP BY T1.\"XCL_001\" ORDER BY SUM(\"XCL_006\")",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:StudentMathScore:000"
  ]
}
```

### SELECT "XCL_013", MAX("XCL_012") FROM "XTB_003" GROUP BY "XCL_013"

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_013\", MAX(\"XCL_012\") FROM \"XTB_003\" GROUP BY \"XCL_013\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:StudentMathScore:002"
  ]
}
```

### SELECT "XCL_013" FROM "XTB_003" ORDER BY "XCL_015" LIMIT 1

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_013\" FROM \"XTB_003\" ORDER BY \"XCL_015\" LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:StudentMathScore:007"
  ]
}
```

### "XTB_003"."XCL_013"

```json
{
  "kind": "binding",
  "formula": "\"XTB_003\".\"XCL_013\"",
  "grain": [
    "\"XTB_003\".\"XCL_013\""
  ],
  "population_scope": "SELECT \"XCL_013\", MAX(\"XCL_012\") FROM \"XTB_003\" GROUP BY \"XCL_013\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_013\"",
    "grain": [
      "\"r0\".\"XCL_013\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_003"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_013\" AS \"grain_0\", \"r0\".\"XCL_013\" AS \"value\" FROM \"XTB_003\" AS \"r0\" GROUP BY \"r0\".\"XCL_013\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:StudentMathScore:002"
  ]
}
```

### SUM("XTB_001"."XCL_007")

```json
{
  "kind": "metric",
  "formula": "SUM(\"XTB_001\".\"XCL_007\")",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_007\") FROM \"XTB_001\" WHERE \"XCL_005\" = 17",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r0\".\"XCL_007\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_001"
      }
    ],
    "scope_sql": "SELECT SUM(\"r0\".\"XCL_007\") AS \"value\" FROM \"XTB_001\" AS \"r0\" WHERE \"r0\".\"XCL_005\" = 17",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:StudentMathScore:004"
  ]
}
```

### "XTB_001"."XCL_005" = 17

```json
{
  "kind": "predicate",
  "formula": "\"XTB_001\".\"XCL_005\" = 17",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_007\") FROM \"XTB_001\" WHERE \"XCL_005\" = 17",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:StudentMathScore:004"
  ]
}
```

### "XTB_002"."XCL_010"

```json
{
  "kind": "binding",
  "formula": "\"XTB_002\".\"XCL_010\"",
  "grain": [
    "\"XTB_001\".\"XCL_001\""
  ],
  "population_scope": "SELECT T2.\"XCL_010\" FROM \"XTB_002\" AS T2 JOIN \"XTB_001\" AS T1 ON T1.\"XCL_001\" = T2.\"XCL_009\" GROUP BY T1.\"XCL_001\" ORDER BY SUM(\"XCL_006\")",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_010\"",
    "grain": [
      "\"r1\".\"XCL_001\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_002"
      },
      {
        "role": "r1",
        "physical_table": "XTB_001"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_001\" AS \"grain_0\", \"r0\".\"XCL_010\" AS \"value\" FROM \"XTB_002\" AS \"r0\" JOIN \"XTB_001\" AS \"r1\" ON \"r1\".\"XCL_001\" = \"r0\".\"XCL_009\" GROUP BY \"r1\".\"XCL_001\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:StudentMathScore:000"
  ]
}
```

### "XTB_003"."XCL_013"

```json
{
  "kind": "binding",
  "formula": "\"XTB_003\".\"XCL_013\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_013\" FROM \"XTB_003\" ORDER BY \"XCL_015\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:StudentMathScore:007"
  ]
}
```

### "XTB_002"."XCL_010"

```json
{
  "kind": "binding",
  "formula": "\"XTB_002\".\"XCL_010\"",
  "grain": [
    "\"XTB_002\".\"XCL_010\""
  ],
  "population_scope": "SELECT T2.\"XCL_010\" FROM \"XTB_001\" AS T1 JOIN \"XTB_002\" AS T2 ON T1.\"XCL_001\" = T2.\"XCL_009\" GROUP BY T2.\"XCL_010\" ORDER BY COUNT(\"XCL_003\") DESC LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:StudentMathScore:001"
  ]
}
```

### AVG("XTB_003"."XCL_015")

```json
{
  "kind": "metric",
  "formula": "AVG(\"XTB_003\".\"XCL_015\")",
  "grain": [],
  "population_scope": "SELECT AVG(\"XCL_015\") FROM \"XTB_003\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_015\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_003"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_015\") AS \"value\" FROM \"XTB_003\" AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:StudentMathScore:008"
  ]
}
```

### MAX("XTB_003"."XCL_012")

```json
{
  "kind": "metric",
  "formula": "MAX(\"XTB_003\".\"XCL_012\")",
  "grain": [
    "\"XTB_003\".\"XCL_013\""
  ],
  "population_scope": "SELECT \"XCL_013\", MAX(\"XCL_012\") FROM \"XTB_003\" GROUP BY \"XCL_013\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MAX(\"r0\".\"XCL_012\")",
    "grain": [
      "\"r0\".\"XCL_013\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_003"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_013\" AS \"grain_0\", MAX(\"r0\".\"XCL_012\") AS \"value\" FROM \"XTB_003\" AS \"r0\" GROUP BY \"r0\".\"XCL_013\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:StudentMathScore:002"
  ]
}
```

### finrev fed 17

```json
{
  "kind": "metric",
  "formula": "the state code of the FINREV_FED_17",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.8e5d4795efe2ff2091644625"
  ]
}
```

### finrev fed 17

```json
{
  "kind": "metric",
  "formula": "the idcensus of the FINREV_FED_17",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.e577b7f47c4bbbc62df944a3"
  ]
}
```

### finrev fed 17

```json
{
  "kind": "metric",
  "formula": "the school district of the FINREV_FED_17",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.ebf2744ca4b93bb49f388ad8"
  ]
}
```

### finrev fed 17

```json
{
  "kind": "metric",
  "formula": "the nces id of the FINREV_FED_17",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.55bbfd707a4c1b8b6b9efb0f"
  ]
}
```

### finrev fed 17

```json
{
  "kind": "metric",
  "formula": "the year data of the FINREV_FED_17",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.691935dfdec01e5b0eb7d292"
  ]
}
```

### finrev fed 17

```json
{
  "kind": "metric",
  "formula": "Total federal revenue through the state to each school district.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.37b61566666b5264f19205c5"
  ]
}
```

### finrev fed 17

```json
{
  "kind": "metric",
  "formula": "Federal revenue through the state- Title 1 (no child left behind act).",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.aa4d08dbf4103d0f049ecd92"
  ]
}
```

### finrev fed 17

```json
{
  "kind": "metric",
  "formula": "Federal revenue through the state- Child Nutrition A",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.94f251b4c7c34636a1bfa624"
  ]
}
```

### ndecoreexcel math grade8

```json
{
  "kind": "metric",
  "formula": "the year of the NDECoreExcel_Math_Grade8",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.aa27c5701e80534a08a4ccfb"
  ]
}
```

### ndecoreexcel math grade8

```json
{
  "kind": "metric",
  "formula": "the state of the NDECoreExcel_Math_Grade8",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.bb7a8d5530558e470dc8461c"
  ]
}
```

### ndecoreexcel math grade8

```json
{
  "kind": "metric",
  "formula": "the all students of the NDECoreExcel_Math_Grade8",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.428350aebbb1f163a1d19207"
  ]
}
```

### ndecoreexcel math grade8

```json
{
  "kind": "metric",
  "formula": "the average scale score of the NDECoreExcel_Math_Grade8",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.8860ec0432a2819f81a600d3"
  ]
}
```

### finrev fed key 17

```json
{
  "kind": "metric",
  "formula": "the state code of the FINREV_FED_KEY_17",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.0e2af10272e867996832d00a"
  ]
}
```

### finrev fed key 17

```json
{
  "kind": "metric",
  "formula": "the state of the FINREV_FED_KEY_17",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.e478b9e5f3992eed35eb476e"
  ]
}
```

### finrev fed key 17

```json
{
  "kind": "metric",
  "formula": "the number of records of the FINREV_FED_KEY_17",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.e84a88035b36400437075455"
  ]
}
```


## 增量维护事件

- Source withdrawal preview · kaggledbqa:fewshot:StudentMathScore:000 · Review event: withdraw this saved source on a copied ontology
  - XTB_001.XCL_001:  → 
  - XTB_002.XCL_009:  → 
  - XTB_002.XCL_010:  → 
