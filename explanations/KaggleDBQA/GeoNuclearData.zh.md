# KaggleDBQA / GeoNuclearData — Schema 与业务口径解释

该数据库的存档目录包含 1 张表、14 个物理列、0 条关系，以及 17 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## XTB_001

该表的存档未记录额外业务说明。

恢复表名: nuclear power plants
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| XTB_001.XCL_012 | capacity | text | — |
| XTB_001.XCL_009 | construction start at / construction_start_date | text | — |
| XTB_001.XCL_005 | country | text | kaggledbqa:fewshot:GeoNuclearData:007, kaggledbqa:fewshot:GeoNuclearData:009 |
| XTB_001.XCL_001 | id / plant_id | text | — |
| XTB_001.XCL_013 | last updated at / last_updated_at | text | — |
| XTB_001.XCL_003 | latitude | text | — |
| XTB_001.XCL_004 | longitude | text | — |
| XTB_001.XCL_002 | name / plant_name | text | kaggledbqa:fewshot:GeoNuclearData:007, kaggledbqa:fewshot:GeoNuclearData:009 |
| XTB_001.XCL_010 | operational from / operational_start_date | text | — |
| XTB_001.XCL_011 | operational to / decommission_date | text | — |
| XTB_001.XCL_008 | reactor model / reactor_model | text | kaggledbqa:fewshot:GeoNuclearData:005 |
| XTB_001.XCL_007 | reactor type / reactor_type | text | — |
| XTB_001.XCL_014 | source / data_source | text | — |
| XTB_001.XCL_006 | status / plant_status | text | — |

## 表关系与连接依据


## 业务口径、总体与粒度

### SELECT "XCL_005" FROM "XTB_001" GROUP BY "XCL_005" HAVING COUNT(Name) = 1

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_005\" FROM \"XTB_001\" GROUP BY \"XCL_005\" HAVING COUNT(Name) = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:GeoNuclearData:009"
  ]
}
```

### SELECT COUNT(DISTINCT "XCL_008") FROM "XTB_001"

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT \"XCL_008\") FROM \"XTB_001\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:GeoNuclearData:005"
  ]
}
```

### SELECT "XCL_005" FROM "XTB_001" GROUP BY "XCL_005" HAVING COUNT(Name) > 3

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_005\" FROM \"XTB_001\" GROUP BY \"XCL_005\" HAVING COUNT(Name) > 3",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:GeoNuclearData:007"
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
  "population_scope": "SELECT \"XCL_005\" FROM \"XTB_001\" GROUP BY \"XCL_005\" HAVING COUNT(Name) > 3",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_005\"",
    "grain": [
      "\"r0\".\"XCL_005\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_001"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_005\" AS \"grain_0\", \"r0\".\"XCL_005\" AS \"value\" FROM \"XTB_001\" AS \"r0\" GROUP BY \"r0\".\"XCL_005\" HAVING COUNT(\"r0\".\"Name\") > 3",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:GeoNuclearData:007"
  ]
}
```

### COUNT("XTB_001"."Name") = 1

```json
{
  "kind": "predicate",
  "formula": "COUNT(\"XTB_001\".\"Name\") = 1",
  "grain": [
    "\"XTB_001\".\"XCL_005\""
  ],
  "population_scope": "SELECT \"XCL_005\" FROM \"XTB_001\" GROUP BY \"XCL_005\" HAVING COUNT(Name) = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:GeoNuclearData:009"
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
  "population_scope": "SELECT \"XCL_005\" FROM \"XTB_001\" GROUP BY \"XCL_005\" HAVING COUNT(Name) = 1",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_005\"",
    "grain": [
      "\"r0\".\"XCL_005\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_001"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_005\" AS \"grain_0\", \"r0\".\"XCL_005\" AS \"value\" FROM \"XTB_001\" AS \"r0\" GROUP BY \"r0\".\"XCL_005\" HAVING COUNT(\"r0\".\"Name\") = 1",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:GeoNuclearData:009"
  ]
}
```

### COUNT(DISTINCT "XTB_001"."XCL_008")

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"XTB_001\".\"XCL_008\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT \"XCL_008\") FROM \"XTB_001\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_008\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_001"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r0\".\"XCL_008\") AS \"value\" FROM \"XTB_001\" AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:GeoNuclearData:005"
  ]
}
```

### COUNT("XTB_001"."Name") > 3

```json
{
  "kind": "predicate",
  "formula": "COUNT(\"XTB_001\".\"Name\") > 3",
  "grain": [
    "\"XTB_001\".\"XCL_005\""
  ],
  "population_scope": "SELECT \"XCL_005\" FROM \"XTB_001\" GROUP BY \"XCL_005\" HAVING COUNT(Name) > 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:GeoNuclearData:007"
  ]
}
```

### nuclear power plants

```json
{
  "kind": "metric",
  "formula": "numeric id key",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.4f26283cd7091ac926628478"
  ]
}
```

### nuclear power plants

```json
{
  "kind": "metric",
  "formula": "nuclear power plant name",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.e76c48ed31383326a1c6ebc5"
  ]
}
```

### nuclear power plants

```json
{
  "kind": "metric",
  "formula": "latitude in decimal format",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.6d9e6da8316f1b0a21a8a95c"
  ]
}
```

### nuclear power plants

```json
{
  "kind": "metric",
  "formula": "longitude in decimal format",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.f9ed428e3ae18c8361c557d7"
  ]
}
```

### nuclear power plants

```json
{
  "kind": "metric",
  "formula": "the country of the nuclear_power_plants",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.8a1723147857daeae6cc40e4"
  ]
}
```

### nuclear power plants

```json
{
  "kind": "metric",
  "formula": "the status of the nuclear_power_plants",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.ea239346c1ce2540be4ddb4e"
  ]
}
```

### nuclear power plants

```json
{
  "kind": "metric",
  "formula": "the reactortype of the nuclear_power_plants",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.38e32c3e0aa6cb732dc831e4"
  ]
}
```

### nuclear power plants

```json
{
  "kind": "metric",
  "formula": "nuclear reactor model",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.fe9354c431650b756b2efb36"
  ]
}
```

### nuclear power plants

```json
{
  "kind": "metric",
  "formula": "date when nuclear power plant construction was started",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.beb72f9ccaf1d6bcaa14b70d"
  ]
}
```

### nuclear power plants

```json
{
  "kind": "metric",
  "formula": "date when nuclear power plant became operational (also known as commercial operation date)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.09547181c31b5534cf559842"
  ]
}
```

### nuclear power plants

```json
{
  "kind": "metric",
  "formula": "date when nuclear power plant was shutdown (also known as permanent shutdown date)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.f9e79cdacef3c1f9cd02bfa8"
  ]
}
```

### nuclear power plants

```json
{
  "kind": "metric",
  "formula": "nuclear power plant capacity (design net capacity in MWe)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.eb63e9cd8fa6f4d9d05bba12"
  ]
}
```

### nuclear power plants

```json
{
  "kind": "metric",
  "formula": "date and time when information was last updated",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.422d208dcb28d09032e7576c"
  ]
}
```

### nuclear power plants

```json
{
  "kind": "metric",
  "formula": "source of the information",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.660c3839a68d87f605619eb5"
  ]
}
```


## 增量维护事件

- Source withdrawal preview · kaggledbqa:fewshot:GeoNuclearData:007 · Review event: withdraw this saved source on a copied ontology
  - XTB_001.XCL_005:  → 
  - XTB_001.Name:  → 
