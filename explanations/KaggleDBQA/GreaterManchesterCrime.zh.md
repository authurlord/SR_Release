# KaggleDBQA / GreaterManchesterCrime — Schema 与业务口径解释

该数据库的存档目录包含 1 张表、6 个物理列、0 条关系，以及 8 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## XTB_001

该表的存档未记录额外业务说明。

恢复表名: greater manchester crime
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| XTB_001.XCL_001 | crime id / CrimeID | text | — |
| XTB_001.XCL_002 | crime ts / crime_timestamp | time | — |
| XTB_001.XCL_004 | lsoa / Lower Layer Super Output Area | text | kaggledbqa:fewshot:GreaterManchesterCrime:008, kaggledbqa:fewshot:GreaterManchesterCrime:003 |
| XTB_001.XCL_003 | location / crime_location_description | text | — |
| XTB_001.XCL_006 | outcome / crime_outcome_status | text | — |
| XTB_001.XCL_005 | type / crime_type | text | — |

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
    "kaggledbqa:fewshot:GreaterManchesterCrime:008",
    "kaggledbqa:fewshot:GreaterManchesterCrime:003"
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
    "kaggledbqa:fewshot:GreaterManchesterCrime:008",
    "kaggledbqa:fewshot:GreaterManchesterCrime:003"
  ]
}
```

### greater manchester crime

```json
{
  "kind": "metric",
  "formula": "this is a randomly generated text string to uniquely indentify each crime record",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.942f1bb576dfd5b3a6effae4"
  ]
}
```

### greater manchester crime

```json
{
  "kind": "metric",
  "formula": "the crime time stamp of the GreaterManchesterCrime",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.adc371787423fa6e6601d1f6"
  ]
}
```

### greater manchester crime

```json
{
  "kind": "metric",
  "formula": "this is the text description of the area in Greater Manchester where the crime occured",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.e1cc31e722c9889de22cf22b"
  ]
}
```

### greater manchester crime

```json
{
  "kind": "metric",
  "formula": "Lower Layer Super Output Area (LSOA) is a GEOGRAPHIC AREA. Lower Layer Super Output Areas are a geographic hierarchy designed to improve the reporting of small area statistics in England and Wales",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.799845160d33fe94c37b3dd7"
  ]
}
```

### greater manchester crime

```json
{
  "kind": "metric",
  "formula": "this is the type or class of crime",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.097851fce1875ccaf78eac10"
  ]
}
```

### greater manchester crime

```json
{
  "kind": "metric",
  "formula": "this is an indication of the outcome of the police investigation",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.02e38f83fd54bd3e8db8ea65"
  ]
}
```


## 增量维护事件

- Source withdrawal preview · kaggledbqa:fewshot:GreaterManchesterCrime:003 · Review event: withdraw this saved source on a copied ontology
  - XTB_001.XCL_004:  → 
