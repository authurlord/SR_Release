# KaggleDBQA / USWildFires — Schema 与业务口径解释

该数据库的存档目录包含 1 张表、19 个物理列、0 条关系，以及 27 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## XTB_001

该表的存档未记录额外业务说明。

恢复表名: fires
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| XTB_001.XCL_007 | cont date / containment_date | text | kaggledbqa:fewshot:USWildFires:003 |
| XTB_001.XCL_008 | cont doy / Continental Day of Year | text | — |
| XTB_001.XCL_009 | cont time / containment_time | text | — |
| XTB_001.XCL_017 | county / county_code | text | — |
| XTB_001.XCL_002 | discovery date / discovery_date | number | kaggledbqa:fewshot:USWildFires:003 |
| XTB_001.XCL_003 | discovery doy / discovery_day_of_year | number | — |
| XTB_001.XCL_004 | discovery time / discovery_time | text | kaggledbqa:fewshot:USWildFires:001 |
| XTB_001.XCL_018 | fips code | text | — |
| XTB_001.XCL_019 | fips name / County Name | text | — |
| XTB_001.XCL_010 | fire size / fire_size_of_fire, | number | kaggledbqa:fewshot:USWildFires:005, kaggledbqa:fewshot:USWildFires:008 |
| XTB_001.XCL_011 | fire size class / fire_size_class | text | — |
| XTB_001.XCL_001 | fire year / fire_year | number | kaggledbqa:fewshot:USWildFires:007, kaggledbqa:fewshot:USWildFires:000, kaggledbqa:fewshot:USWildFires:011, kaggledbqa:fewshot:USWildFires:009, kaggledbqa:fewshot:USWildFires:008 |
| XTB_001.XCL_012 | latitude | number | — |
| XTB_001.XCL_013 | longitude | number | — |
| XTB_001.XCL_014 | owner code / owner_code | number | — |
| XTB_001.XCL_015 | owner descr / owner_description | text | — |
| XTB_001.XCL_016 | state | text | kaggledbqa:fewshot:USWildFires:005, kaggledbqa:fewshot:USWildFires:009 |
| XTB_001.XCL_005 | stat cause code / stat_cause_code, | number | — |
| XTB_001.XCL_006 | stat cause descr / Statutory Cause Description | text | kaggledbqa:fewshot:USWildFires:007 |

## 表关系与连接依据


## 业务口径、总体与粒度

### SELECT "XCL_004" FROM "XTB_001" GROUP BY "XCL_004" ORDER BY COUNT(*) DESC LIMIT 1

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_004\" FROM \"XTB_001\" GROUP BY \"XCL_004\" ORDER BY COUNT(*) DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:USWildFires:001"
  ]
}
```

### SELECT COUNT(*) FROM "XTB_001" WHERE "XCL_001" = 2006 AND "XCL_010" > 100

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(*) FROM \"XTB_001\" WHERE \"XCL_001\" = 2006 AND \"XCL_010\" > 100",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:USWildFires:008"
  ]
}
```

### SELECT "XCL_016" FROM "XTB_001" WHERE "XCL_001" = 2001 GROUP BY "XCL_016" ORDER BY COUNT(*) DESC LIMIT 1

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_016\" FROM \"XTB_001\" WHERE \"XCL_001\" = 2001 GROUP BY \"XCL_016\" ORDER BY COUNT(*) DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:USWildFires:009"
  ]
}
```

### SELECT "XCL_006" FROM "XTB_001" WHERE "XCL_001" BETWEEN 2000 AND 2005 GROUP BY "XCL_006" ORDER BY COUNT(*) DESC LIMIT 1

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_006\" FROM \"XTB_001\" WHERE \"XCL_001\" BETWEEN 2000 AND 2005 GROUP BY \"XCL_006\" ORDER BY COUNT(*) DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:USWildFires:007"
  ]
}
```

### SELECT AVG("XCL_007" - "XCL_002") FROM "XTB_001"

```json
{
  "kind": "program",
  "formula": "SELECT AVG(\"XCL_007\" - \"XCL_002\") FROM \"XTB_001\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:USWildFires:003"
  ]
}
```

### SELECT "XCL_001" FROM "XTB_001" GROUP BY "XCL_001" ORDER BY COUNT(*) DESC LIMIT 1

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_001\" FROM \"XTB_001\" GROUP BY \"XCL_001\" ORDER BY COUNT(*) DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:USWildFires:000",
    "kaggledbqa:fewshot:USWildFires:011"
  ]
}
```

### SELECT "XCL_016" FROM "XTB_001" ORDER BY "XCL_010" DESC LIMIT 1

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_016\" FROM \"XTB_001\" ORDER BY \"XCL_010\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:USWildFires:005"
  ]
}
```

### "XTB_001"."XCL_004"

```json
{
  "kind": "binding",
  "formula": "\"XTB_001\".\"XCL_004\"",
  "grain": [
    "\"XTB_001\".\"XCL_004\""
  ],
  "population_scope": "SELECT \"XCL_004\" FROM \"XTB_001\" GROUP BY \"XCL_004\" ORDER BY COUNT(*) DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:USWildFires:001"
  ]
}
```

### "XTB_001"."XCL_016"

```json
{
  "kind": "binding",
  "formula": "\"XTB_001\".\"XCL_016\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_016\" FROM \"XTB_001\" ORDER BY \"XCL_010\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:USWildFires:005"
  ]
}
```

### "XTB_001"."XCL_001"

```json
{
  "kind": "binding",
  "formula": "\"XTB_001\".\"XCL_001\"",
  "grain": [
    "\"XTB_001\".\"XCL_001\""
  ],
  "population_scope": "SELECT \"XCL_001\" FROM \"XTB_001\" GROUP BY \"XCL_001\" ORDER BY COUNT(*) DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:USWildFires:000",
    "kaggledbqa:fewshot:USWildFires:011"
  ]
}
```

### "XTB_001"."XCL_006"

```json
{
  "kind": "binding",
  "formula": "\"XTB_001\".\"XCL_006\"",
  "grain": [
    "\"XTB_001\".\"XCL_006\""
  ],
  "population_scope": "SELECT \"XCL_006\" FROM \"XTB_001\" WHERE \"XCL_001\" BETWEEN 2000 AND 2005 GROUP BY \"XCL_006\" ORDER BY COUNT(*) DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:USWildFires:007"
  ]
}
```

### "XTB_001"."XCL_001" BETWEEN 2000 AND 2005

```json
{
  "kind": "predicate",
  "formula": "\"XTB_001\".\"XCL_001\" BETWEEN 2000 AND 2005",
  "grain": [
    "\"XTB_001\".\"XCL_006\""
  ],
  "population_scope": "SELECT \"XCL_006\" FROM \"XTB_001\" WHERE \"XCL_001\" BETWEEN 2000 AND 2005 GROUP BY \"XCL_006\" ORDER BY COUNT(*) DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:USWildFires:007"
  ]
}
```

### "XTB_001"."XCL_001" = 2006 AND "XTB_001"."XCL_010" > 100

```json
{
  "kind": "predicate",
  "formula": "\"XTB_001\".\"XCL_001\" = 2006 AND \"XTB_001\".\"XCL_010\" > 100",
  "grain": [],
  "population_scope": "SELECT COUNT(*) FROM \"XTB_001\" WHERE \"XCL_001\" = 2006 AND \"XCL_010\" > 100",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:USWildFires:008"
  ]
}
```

### AVG("XTB_001"."XCL_007" - "XTB_001"."XCL_002")

```json
{
  "kind": "metric",
  "formula": "AVG(\"XTB_001\".\"XCL_007\" - \"XTB_001\".\"XCL_002\")",
  "grain": [],
  "population_scope": "SELECT AVG(\"XCL_007\" - \"XCL_002\") FROM \"XTB_001\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_007\" - \"r0\".\"XCL_002\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_001"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_007\" - \"r0\".\"XCL_002\") AS \"value\" FROM \"XTB_001\" AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:USWildFires:003"
  ]
}
```

### COUNT(*)

```json
{
  "kind": "metric",
  "formula": "COUNT(*)",
  "grain": [],
  "population_scope": "SELECT COUNT(*) FROM \"XTB_001\" WHERE \"XCL_001\" = 2006 AND \"XCL_010\" > 100",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(*)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_001"
      }
    ],
    "scope_sql": "SELECT COUNT(*) AS \"value\" FROM \"XTB_001\" AS \"r0\" WHERE \"r0\".\"XCL_001\" = 2006 AND \"r0\".\"XCL_010\" > 100",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:USWildFires:008"
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
  "population_scope": "SELECT \"XCL_016\" FROM \"XTB_001\" WHERE \"XCL_001\" = 2001 GROUP BY \"XCL_016\" ORDER BY COUNT(*) DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:USWildFires:009"
  ]
}
```

### "XTB_001"."XCL_001" = 2001

```json
{
  "kind": "predicate",
  "formula": "\"XTB_001\".\"XCL_001\" = 2001",
  "grain": [
    "\"XTB_001\".\"XCL_016\""
  ],
  "population_scope": "SELECT \"XCL_016\" FROM \"XTB_001\" WHERE \"XCL_001\" = 2001 GROUP BY \"XCL_016\" ORDER BY COUNT(*) DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:USWildFires:009"
  ]
}
```

### fires

```json
{
  "kind": "metric",
  "formula": "Calendar year in which the fire was discovered or confirmed to exist.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.927dd520d2a06bf5c62ce248"
  ]
}
```

### fires

```json
{
  "kind": "metric",
  "formula": "Date on which the fire was discovered or confirmed to exist.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.3c616185b0bcaf04296cae8e"
  ]
}
```

### fires

```json
{
  "kind": "metric",
  "formula": "Day of year on which the fire was discovered or confirmed to exist.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.2c12366b07ed49fbd4aacdc1"
  ]
}
```

### fires

```json
{
  "kind": "metric",
  "formula": "Time of day that the fire was discovered or confirmed to exist.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.e6703a356c41d57ecb464a93"
  ]
}
```

### fires

```json
{
  "kind": "metric",
  "formula": "Code for the (statistical) cause of the fire.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.976ca25dddb461ce4b33abf9"
  ]
}
```

### fires

```json
{
  "kind": "metric",
  "formula": "Description of the (statistical) cause of the fire.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.e7796bc08a3c11102010bddf"
  ]
}
```

### fires

```json
{
  "kind": "metric",
  "formula": "Date on which the fire was declared contained or otherwise controlled",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.845a87703f530902426a8f50"
  ]
}
```

### fires

```json
{
  "kind": "metric",
  "formula": "Day of year on which the fire was declared contained or otherwise controlled.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.103127b07149403376618a1b"
  ]
}
```

### fires

```json
{
  "kind": "metric",
  "formula": "Time of day that the fire was declared contained or otherwise controlled",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.287148ae09a762bbe72fe1c1"
  ]
}
```

### fires

```json
{
  "kind": "metric",
  "formula": "Estimate of acres within the final perimeter of the fire.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.e96e5b3188cab2d54c7be673"
  ]
}
```

### fires

```json
{
  "kind": "metric",
  "formula": "Code for fire size based on the number of acres within the final fire perimeter expenditures.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.1a6e402ec3cbb707fe6d92e3"
  ]
}
```

### fires

```json
{
  "kind": "metric",
  "formula": "Latitude (NAD83) for point location of the fire",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.b21a32d507ff80dbfe140097"
  ]
}
```

### fires

```json
{
  "kind": "metric",
  "formula": "Longitude (NAD83) for point location of the fire",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.78e9517c3e570a46ca4477dd"
  ]
}
```

### fires

```json
{
  "kind": "metric",
  "formula": "Code for primary owner or entity responsible for managing the land at the point of origin of the fire at the time of the incident.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.ec90585feba0a4096f96dfe9"
  ]
}
```

### fires

```json
{
  "kind": "metric",
  "formula": "Name of primary owner or entity responsible for managing the land at the point of origin of the fire at the time of the incident.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.354d10478ee900c70f24885d"
  ]
}
```

### fires

```json
{
  "kind": "metric",
  "formula": "Two-letter code for the state in which the unit is located",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.64e1adeb98de640cb3a2d87d"
  ]
}
```

### fires

```json
{
  "kind": "metric",
  "formula": "County, or equivalent, in which the fire burned (or originated), based on nominal designation in the fire report.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.359a305030ca9eb83f59061b"
  ]
}
```

### fires

```json
{
  "kind": "metric",
  "formula": "Three-digit code from the Federal Information Process Standards (FIPS) publication 6-4 for representation of counties and equivalent entities.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.fa723f4f3c1f8fb40004ddde"
  ]
}
```

### fires

```json
{
  "kind": "metric",
  "formula": "County name from the FIPS publication 6-4 for representation of counties and equivalent entities.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.3d22ab163e247a8afc0bd1c6"
  ]
}
```


## 增量维护事件

- Source withdrawal preview · kaggledbqa:fewshot:USWildFires:003 · Review event: withdraw this saved source on a copied ontology
  - XTB_001.XCL_002:  → 
  - XTB_001.XCL_007:  → 
