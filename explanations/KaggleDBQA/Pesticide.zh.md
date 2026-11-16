# KaggleDBQA / Pesticide — Schema 与业务口径解释

该数据库的存档目录包含 2 张表、34 个物理列、1 条关系，以及 45 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## XTB_001

该表的存档未记录额外业务说明。

恢复表名: resultsdata15
SQL表别名: T1, T2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| XTB_001.XCL_012 | annotate / annotation_code | text | — |
| XTB_001.XCL_002 | commod / commodity_code | text | — |
| XTB_001.XCL_003 | commtype | text | — |
| XTB_001.XCL_007 | concen / concentration | number | kaggledbqa:fewshot:Pesticide:006, kaggledbqa:fewshot:Pesticide:005 |
| XTB_001.XCL_010 | confmethod / confidence_method | text | — |
| XTB_001.XCL_011 | confmethod2 | text | — |
| XTB_001.XCL_009 | conunit / concentration_unit | text | — |
| XTB_001.XCL_016 | determin | text | kaggledbqa:fewshot:Pesticide:002 |
| XTB_001.XCL_015 | extract | text | kaggledbqa:fewshot:Pesticide:001 |
| XTB_001.XCL_004 | lab / laboratory_code | text | — |
| XTB_001.XCL_008 | lod / limit_of_detection | number | — |
| XTB_001.XCL_014 | mean / mean_result_code | text | — |
| XTB_001.XCL_005 | pestcode / pesticide_code | text | kaggledbqa:fewshot:Pesticide:009, kaggledbqa:fewshot:Pesticide:010 |
| XTB_001.XCL_013 | quantitate | text | — |
| XTB_001.XCL_001 | sample pk / sample_pk | number | kaggledbqa:fewshot:Pesticide:011, kaggledbqa:fewshot:Pesticide:006, kaggledbqa:fewshot:Pesticide:005 |
| XTB_001.XCL_006 | testclass / test_class | text | kaggledbqa:fewshot:Pesticide:011 |

## XTB_002

该表的存档未记录额外业务说明。

恢复表名: sampledata15
SQL表别名: T1, T2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| XTB_002.XCL_030 | claim | text | — |
| XTB_002.XCL_023 | commod / commodity_code | text | kaggledbqa:fewshot:Pesticide:008 |
| XTB_002.XCL_029 | commtype | text | — |
| XTB_002.XCL_027 | country | text | kaggledbqa:fewshot:Pesticide:005 |
| XTB_002.XCL_021 | day | text | — |
| XTB_002.XCL_034 | distst / Distribution State | text | kaggledbqa:fewshot:Pesticide:014 |
| XTB_002.XCL_028 | disttype / Distribution Type | text | kaggledbqa:fewshot:Pesticide:006 |
| XTB_002.XCL_032 | growst / growing_state | text | kaggledbqa:fewshot:Pesticide:012 |
| XTB_002.XCL_020 | month | text | — |
| XTB_002.XCL_026 | origin / origin_code | text | — |
| XTB_002.XCL_033 | packst | text | kaggledbqa:fewshot:Pesticide:013 |
| XTB_002.XCL_031 | quantity | number | — |
| XTB_002.XCL_017 | sample pk / sample_pk | number | kaggledbqa:fewshot:Pesticide:006, kaggledbqa:fewshot:Pesticide:013, kaggledbqa:fewshot:Pesticide:005, kaggledbqa:fewshot:Pesticide:012, kaggledbqa:fewshot:Pesticide:014 |
| XTB_002.XCL_022 | site / site_id | text | — |
| XTB_002.XCL_024 | source id / source_id | text | — |
| XTB_002.XCL_018 | state | text | — |
| XTB_002.XCL_025 | variety | text | — |
| XTB_002.XCL_019 | year | text | — |

## 表关系与连接依据

- XTB_001.XCL_001 ↔ XTB_002.XCL_017; declared_or_materialized_relationship, target_disjoint_historical_join

## 业务口径、总体与粒度

### SELECT "XCL_016" FROM "XTB_001" GROUP BY "XCL_016" ORDER BY COUNT(*) DESC LIMIT 1

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_016\" FROM \"XTB_001\" GROUP BY \"XCL_016\" ORDER BY COUNT(*) DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:002"
  ]
}
```

### SELECT "XCL_023", COUNT(*) FROM "XTB_002" GROUP BY "XCL_023"

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_023\", COUNT(*) FROM \"XTB_002\" GROUP BY \"XCL_023\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:008"
  ]
}
```

### SELECT "XCL_005" FROM "XTB_001" GROUP BY "XCL_005" ORDER BY COUNT(*) DESC LIMIT 1

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_005\" FROM \"XTB_001\" GROUP BY \"XCL_005\" ORDER BY COUNT(*) DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:009"
  ]
}
```

### SELECT "XCL_015" FROM "XTB_001" GROUP BY "XCL_015" ORDER BY COUNT(*) DESC LIMIT 1

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_015\" FROM \"XTB_001\" GROUP BY \"XCL_015\" ORDER BY COUNT(*) DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:001"
  ]
}
```

### SELECT T1."XCL_027" FROM "XTB_002" AS T1 JOIN "XTB_001" AS T2 ON T1."XCL_017" = T2."XCL_001" GROUP BY T1."XCL_027" ORDER BY T2."XCL_007"

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_027\" FROM \"XTB_002\" AS T1 JOIN \"XTB_001\" AS T2 ON T1.\"XCL_017\" = T2.\"XCL_001\" GROUP BY T1.\"XCL_027\" ORDER BY T2.\"XCL_007\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:005"
  ]
}
```

### SELECT "XCL_017", "XCL_033" FROM "XTB_002"

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_017\", \"XCL_033\" FROM \"XTB_002\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:013"
  ]
}
```

### SELECT "XCL_001", "XCL_006" FROM "XTB_001"

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_001\", \"XCL_006\" FROM \"XTB_001\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:011"
  ]
}
```

### SELECT "XCL_017", "XCL_034" FROM "XTB_002"

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_017\", \"XCL_034\" FROM \"XTB_002\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:014"
  ]
}
```

### SELECT "XCL_005" FROM "XTB_001" GROUP BY "XCL_005" ORDER BY COUNT(*) LIMIT 1

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_005\" FROM \"XTB_001\" GROUP BY \"XCL_005\" ORDER BY COUNT(*) LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:010"
  ]
}
```

### SELECT T1."XCL_028" FROM "XTB_002" AS T1 JOIN "XTB_001" AS T2 ON T1."XCL_017" = T2."XCL_001" GROUP BY T1."XCL_028" ORDER BY SUM(T2."XCL_007") DESC LIM

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_028\" FROM \"XTB_002\" AS T1 JOIN \"XTB_001\" AS T2 ON T1.\"XCL_017\" = T2.\"XCL_001\" GROUP BY T1.\"XCL_028\" ORDER BY SUM(T2.\"XCL_007\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:006"
  ]
}
```

### SELECT "XCL_017", "XCL_032" FROM "XTB_002"

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_017\", \"XCL_032\" FROM \"XTB_002\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:012"
  ]
}
```

### "XTB_001"."XCL_005"

```json
{
  "kind": "binding",
  "formula": "\"XTB_001\".\"XCL_005\"",
  "grain": [
    "\"XTB_001\".\"XCL_005\""
  ],
  "population_scope": "SELECT \"XCL_005\" FROM \"XTB_001\" GROUP BY \"XCL_005\" ORDER BY COUNT(*) LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:010"
  ]
}
```

### "XTB_001"."XCL_005"

```json
{
  "kind": "binding",
  "formula": "\"XTB_001\".\"XCL_005\"",
  "grain": [
    "\"XTB_001\".\"XCL_005\""
  ],
  "population_scope": "SELECT \"XCL_005\" FROM \"XTB_001\" GROUP BY \"XCL_005\" ORDER BY COUNT(*) DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:009"
  ]
}
```

### "XTB_001"."XCL_016"

```json
{
  "kind": "binding",
  "formula": "\"XTB_001\".\"XCL_016\"",
  "grain": [
    "\"XTB_001\".\"XCL_016\""
  ],
  "population_scope": "SELECT \"XCL_016\" FROM \"XTB_001\" GROUP BY \"XCL_016\" ORDER BY COUNT(*) DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:002"
  ]
}
```

### "XTB_002"."XCL_034"

```json
{
  "kind": "binding",
  "formula": "\"XTB_002\".\"XCL_034\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_017\", \"XCL_034\" FROM \"XTB_002\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_034\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_002"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_034\" AS \"value\" FROM \"XTB_002\" AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:014"
  ]
}
```

### "XTB_001"."XCL_001"

```json
{
  "kind": "binding",
  "formula": "\"XTB_001\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\", \"XCL_006\" FROM \"XTB_001\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_001"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM \"XTB_001\" AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:011"
  ]
}
```

### "XTB_002"."XCL_017"

```json
{
  "kind": "binding",
  "formula": "\"XTB_002\".\"XCL_017\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_017\", \"XCL_033\" FROM \"XTB_002\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_017\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_002"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_017\" AS \"value\" FROM \"XTB_002\" AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:013",
    "kaggledbqa:fewshot:Pesticide:012",
    "kaggledbqa:fewshot:Pesticide:014"
  ]
}
```

### "XTB_002"."XCL_027"

```json
{
  "kind": "binding",
  "formula": "\"XTB_002\".\"XCL_027\"",
  "grain": [
    "\"XTB_002\".\"XCL_027\""
  ],
  "population_scope": "SELECT T1.\"XCL_027\" FROM \"XTB_002\" AS T1 JOIN \"XTB_001\" AS T2 ON T1.\"XCL_017\" = T2.\"XCL_001\" GROUP BY T1.\"XCL_027\" ORDER BY T2.\"XCL_007\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_027\"",
    "grain": [
      "\"r0\".\"XCL_027\""
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
    "scope_sql": "SELECT \"r0\".\"XCL_027\" AS \"grain_0\", \"r0\".\"XCL_027\" AS \"value\" FROM \"XTB_002\" AS \"r0\" JOIN \"XTB_001\" AS \"r1\" ON \"r0\".\"XCL_017\" = \"r1\".\"XCL_001\" GROUP BY \"r0\".\"XCL_027\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:005"
  ]
}
```

### "XTB_002"."XCL_033"

```json
{
  "kind": "binding",
  "formula": "\"XTB_002\".\"XCL_033\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_017\", \"XCL_033\" FROM \"XTB_002\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_033\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_002"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_033\" AS \"value\" FROM \"XTB_002\" AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:013"
  ]
}
```

### "XTB_001"."XCL_015"

```json
{
  "kind": "binding",
  "formula": "\"XTB_001\".\"XCL_015\"",
  "grain": [
    "\"XTB_001\".\"XCL_015\""
  ],
  "population_scope": "SELECT \"XCL_015\" FROM \"XTB_001\" GROUP BY \"XCL_015\" ORDER BY COUNT(*) DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:001"
  ]
}
```

### COUNT(*)

```json
{
  "kind": "metric",
  "formula": "COUNT(*)",
  "grain": [
    "\"XTB_002\".\"XCL_023\""
  ],
  "population_scope": "SELECT \"XCL_023\", COUNT(*) FROM \"XTB_002\" GROUP BY \"XCL_023\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(*)",
    "grain": [
      "\"r0\".\"XCL_023\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_002"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_023\" AS \"grain_0\", COUNT(*) AS \"value\" FROM \"XTB_002\" AS \"r0\" GROUP BY \"r0\".\"XCL_023\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:008"
  ]
}
```

### "XTB_002"."XCL_023"

```json
{
  "kind": "binding",
  "formula": "\"XTB_002\".\"XCL_023\"",
  "grain": [
    "\"XTB_002\".\"XCL_023\""
  ],
  "population_scope": "SELECT \"XCL_023\", COUNT(*) FROM \"XTB_002\" GROUP BY \"XCL_023\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_023\"",
    "grain": [
      "\"r0\".\"XCL_023\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_002"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_023\" AS \"grain_0\", \"r0\".\"XCL_023\" AS \"value\" FROM \"XTB_002\" AS \"r0\" GROUP BY \"r0\".\"XCL_023\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:008"
  ]
}
```

### "XTB_002"."XCL_032"

```json
{
  "kind": "binding",
  "formula": "\"XTB_002\".\"XCL_032\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_017\", \"XCL_032\" FROM \"XTB_002\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_032\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_002"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_032\" AS \"value\" FROM \"XTB_002\" AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:012"
  ]
}
```

### "XTB_002"."XCL_028"

```json
{
  "kind": "binding",
  "formula": "\"XTB_002\".\"XCL_028\"",
  "grain": [
    "\"XTB_002\".\"XCL_028\""
  ],
  "population_scope": "SELECT T1.\"XCL_028\" FROM \"XTB_002\" AS T1 JOIN \"XTB_001\" AS T2 ON T1.\"XCL_017\" = T2.\"XCL_001\" GROUP BY T1.\"XCL_028\" ORDER BY SUM(T2.\"XCL_007\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:006"
  ]
}
```

### "XTB_001"."XCL_006"

```json
{
  "kind": "binding",
  "formula": "\"XTB_001\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\", \"XCL_006\" FROM \"XTB_001\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_001"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_006\" AS \"value\" FROM \"XTB_001\" AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:Pesticide:011"
  ]
}
```

### sampledata15

```json
{
  "kind": "metric",
  "formula": "PDP Sample ID - unique sample identifer",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.6ff2da8f47582a561c98dd6e"
  ]
}
```

### sampledata15

```json
{
  "kind": "metric",
  "formula": "State code for location of origin (grower packer or distributor) if sample is domestic",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.df7b0eda77edf90e3d3ff87e"
  ]
}
```

### sampledata15

```json
{
  "kind": "metric",
  "formula": "2-digit Year",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.f696969ef51202bdd58c2588"
  ]
}
```

### sampledata15

```json
{
  "kind": "metric",
  "formula": "2-digit Month",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.850cdf301da79a53a629b416"
  ]
}
```

### sampledata15

```json
{
  "kind": "metric",
  "formula": "2-digit Day",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.4e75aa794e07548548b2f55f"
  ]
}
```

### sampledata15

```json
{
  "kind": "metric",
  "formula": "4-digit Collection Site code",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.ecfeffda45cb4cd8c0929530"
  ]
}
```

### sampledata15

```json
{
  "kind": "metric",
  "formula": "Commodity Code for product collected",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.bacab1aaa1a12bf0e91176e2"
  ]
}
```

### sampledata15

```json
{
  "kind": "metric",
  "formula": "optional 1-letter Source ID code",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.76a70a911380f6e88b5d09f3"
  ]
}
```

### sampledata15

```json
{
  "kind": "metric",
  "formula": "Variety/class of the product collected",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.7f3f87d33d415f25e2d75c92"
  ]
}
```

### sampledata15

```json
{
  "kind": "metric",
  "formula": "Code indicating sample origin",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.3b83d3a389cebc8b249b69ff"
  ]
}
```

### sampledata15

```json
{
  "kind": "metric",
  "formula": "Country of origin if the sample was imported",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.a2371674a374d140418b25c8"
  ]
}
```

### sampledata15

```json
{
  "kind": "metric",
  "formula": "Code for type of collection/distribution facility",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.42879e4524ab9447fc58a8e7"
  ]
}
```

### sampledata15

```json
{
  "kind": "metric",
  "formula": "Code for commodity or package/container type",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.d57a24eb9ecbad5efe4f7a91"
  ]
}
```

### sampledata15

```json
{
  "kind": "metric",
  "formula": "Code for claim made on product",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.e5dcb54a2a93ec10022b3c28"
  ]
}
```

### sampledata15

```json
{
  "kind": "metric",
  "formula": "Number of individual units in sample for select non-clustered products",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.f439d5c745ffd3832ba2a6e8"
  ]
}
```

### sampledata15

```json
{
  "kind": "metric",
  "formula": "the grow state of the sampledata15",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.af269f826c6afc39cd45ece5"
  ]
}
```

### sampledata15

```json
{
  "kind": "metric",
  "formula": "the pack state of the sampledata15",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.4fccfffb8c339cc027dab8a9"
  ]
}
```

### sampledata15

```json
{
  "kind": "metric",
  "formula": "the distribution state of the sampledata15",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.ec20f0e939862f91f2327346"
  ]
}
```

### resultsdata15

```json
{
  "kind": "metric",
  "formula": "the sample pk of the resultsdata15",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.17b61b9f2ccbaf5fc1ef6fb9"
  ]
}
```

### resultsdata15

```json
{
  "kind": "metric",
  "formula": "the commodity code of the resultsdata15",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.1bba154c60bebbd9b5ee0e93"
  ]
}
```

### resultsdata15

```json
{
  "kind": "metric",
  "formula": "the commodity type of the resultsdata15",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.2ea64b069f2f51f029c143d9"
  ]
}
```

### resultsdata15

```json
{
  "kind": "metric",
  "formula": "the lab code of the resultsdata15",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.9ecda13569a8c753cd456db9"
  ]
}
```

### resultsdata15

```json
{
  "kind": "metric",
  "formula": "FDA/PDP Pesticide Code for compound tested",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.262b931ab6e2ebfc030b213d"
  ]
}
```

### resultsdata15

```json
{
  "kind": "metric",
  "formula": "Code for Test Classification",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.8b695b8fe2ed1ab22319aced"
  ]
}
```

### resultsdata15

```json
{
  "kind": "metric",
  "formula": "Concentration of residue detected. Zero (0) for non-detect",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.467fb85d0c1ecfeea90e3382"
  ]
}
```

### resultsdata15

```json
{
  "kind": "metric",
  "formula": "Limit of Detection for pesticide/commodity pair",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.7237c2d5ce7d7b198e05aa52"
  ]
}
```

### resultsdata15

```json
{
  "kind": "metric",
  "formula": "Concentration of residue detected",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.19b0fb2c5e4c81b5c19762ea"
  ]
}
```

### resultsdata15

```json
{
  "kind": "metric",
  "formula": "Code for primary Confirmation method",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.e5ae860416653fa5863474e0"
  ]
}
```

### resultsdata15

```json
{
  "kind": "metric",
  "formula": "Code for secondary Confirmation method",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.67907bfddc3c37b347d8fe20"
  ]
}
```

### resultsdata15

```json
{
  "kind": "metric",
  "formula": "Code for Annotated Information",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.cffb1cd4c5d3f1123a6354a8"
  ]
}
```

### resultsdata15

```json
{
  "kind": "metric",
  "formula": "Code for Quantitative method",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.0a94cf042b2cb712173e940a"
  ]
}
```

### resultsdata15

```json
{
  "kind": "metric",
  "formula": "Code for Mean Result finding",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.d0bb0ea8d968f90a8b1f7bf0"
  ]
}
```

### resultsdata15

```json
{
  "kind": "metric",
  "formula": "Code for Extraction method",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.9b10cb7d8b9889e659b1baf7"
  ]
}
```

### resultsdata15

```json
{
  "kind": "metric",
  "formula": "Code for Determinative method",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.89e18d485e9de85c09200de0"
  ]
}
```


## 增量维护事件

- Source withdrawal preview · kaggledbqa:fewshot:Pesticide:005 · Review event: withdraw this saved source on a copied ontology
  - XTB_001.XCL_007:  → 
  - XTB_001.XCL_001:  → 
  - XTB_002.XCL_017:  → 
  - XTB_002.XCL_027:  → 
