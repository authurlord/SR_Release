# KaggleDBQA / WorldSoccerDataBase — Schema 与业务口径解释

该数据库的存档目录包含 2 张表、37 个物理列、0 条关系，以及 39 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## XTB_001

该表的存档未记录额外业务说明。

恢复表名: betfront
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| XTB_001.XCL_011 | away closing / away_closing_odds | number | — |
| XTB_001.XCL_008 | away opening / away_opening_odds | number | — |
| XTB_001.XCL_004 | competion / competition_slug | text | — |
| XTB_001.XCL_003 | country | text | — |
| XTB_001.XCL_002 | datetime / match_datetime | time | — |
| XTB_001.XCL_010 | draw closing / draw_closing_odds | number | — |
| XTB_001.XCL_007 | draw opening / draw_opening_odds | number | — |
| XTB_001.XCL_009 | home closing / home_closing_odds | number | — |
| XTB_001.XCL_006 | home opening / home_opening_odds | number | — |
| XTB_001.XCL_005 | match / match_opponents | text | — |
| XTB_001.XCL_001 | year | number | — |

## XTB_002

该表的存档未记录额外业务说明。

恢复表名: football data
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| XTB_002.XCL_019 | away team / away_team_name | text | — |
| XTB_002.XCL_031 | b365 a / bet365_away_odds | number | — |
| XTB_002.XCL_030 | b365 d / B365 Home Win Odds | number | kaggledbqa:fewshot:WorldSoccerDataBase:003 |
| XTB_002.XCL_029 | b365 h / Bet365 Home Win Odds | number | — |
| XTB_002.XCL_037 | bwa | number | — |
| XTB_002.XCL_036 | bwd | number | — |
| XTB_002.XCL_035 | bwh | number | — |
| XTB_002.XCL_015 | country | text | — |
| XTB_002.XCL_013 | datetime / match_datetime, | time | — |
| XTB_002.XCL_014 | div / division_code, | text | — |
| XTB_002.XCL_021 | ftag / Away Team Full-Time Goals | number | kaggledbqa:fewshot:WorldSoccerDataBase:005 |
| XTB_002.XCL_020 | fthg / Full Time Home Goals | number | kaggledbqa:fewshot:WorldSoccerDataBase:005 |
| XTB_002.XCL_022 | ftr / full_time_result | text | — |
| XTB_002.XCL_024 | htag / home_team_aggregated_goals | number | — |
| XTB_002.XCL_023 | hthg / Home Team Goals | number | — |
| XTB_002.XCL_025 | htr / Half-Time Result | text | — |
| XTB_002.XCL_018 | home team / home_team_name | text | — |
| XTB_002.XCL_034 | lba | number | — |
| XTB_002.XCL_033 | lbd | number | — |
| XTB_002.XCL_032 | lbh | number | — |
| XTB_002.XCL_016 | league / league_name | text | — |
| XTB_002.XCL_028 | psa | number | — |
| XTB_002.XCL_027 | psd | number | — |
| XTB_002.XCL_026 | psh | number | — |
| XTB_002.XCL_017 | referee / referee_name | text | — |
| XTB_002.XCL_012 | season | text | — |

## 表关系与连接依据


## 业务口径、总体与粒度

### SELECT * FROM "XTB_002" WHERE ("XCL_020" + "XCL_021") = 0

```json
{
  "kind": "program",
  "formula": "SELECT * FROM \"XTB_002\" WHERE (\"XCL_020\" + \"XCL_021\") = 0",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:WorldSoccerDataBase:005"
  ]
}
```

### SELECT * FROM "XTB_002" WHERE "XCL_030" > 3

```json
{
  "kind": "program",
  "formula": "SELECT * FROM \"XTB_002\" WHERE \"XCL_030\" > 3",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:WorldSoccerDataBase:003"
  ]
}
```

### ("XTB_002"."XCL_020" + "XTB_002"."XCL_021") = 0

```json
{
  "kind": "predicate",
  "formula": "(\"XTB_002\".\"XCL_020\" + \"XTB_002\".\"XCL_021\") = 0",
  "grain": [],
  "population_scope": "SELECT * FROM \"XTB_002\" WHERE (\"XCL_020\" + \"XCL_021\") = 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:WorldSoccerDataBase:005"
  ]
}
```

### "XTB_002"."XCL_030" > 3

```json
{
  "kind": "predicate",
  "formula": "\"XTB_002\".\"XCL_030\" > 3",
  "grain": [],
  "population_scope": "SELECT * FROM \"XTB_002\" WHERE \"XCL_030\" > 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:WorldSoccerDataBase:003"
  ]
}
```

### betfront

```json
{
  "kind": "metric",
  "formula": "the year of the betfront",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.6ace1deaa62f7a04b3cf9397"
  ]
}
```

### betfront

```json
{
  "kind": "metric",
  "formula": "the datetime of the betfront",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.464fa60f9ba724e77a992030"
  ]
}
```

### betfront

```json
{
  "kind": "metric",
  "formula": "the country of the betfront",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.70baf8b2f548fe3755a24a4a"
  ]
}
```

### betfront

```json
{
  "kind": "metric",
  "formula": "the competion of the betfront",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.1b46104b1b0d9befa59ad7d2"
  ]
}
```

### betfront

```json
{
  "kind": "metric",
  "formula": "the match of the betfront",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.20da584789c97f74d3bba116"
  ]
}
```

### betfront

```json
{
  "kind": "metric",
  "formula": "the home opening of the betfront",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.4ac4991e294ecbfab0e3a56c"
  ]
}
```

### betfront

```json
{
  "kind": "metric",
  "formula": "the draw opening of the betfront",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.228ccc8eda1cfd67d9629d95"
  ]
}
```

### betfront

```json
{
  "kind": "metric",
  "formula": "the away opening of the betfront",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.c706356c13a9e77a63f92aaa"
  ]
}
```

### betfront

```json
{
  "kind": "metric",
  "formula": "the home closing of the betfront",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.d5063ba0c5ea79366fffa20c"
  ]
}
```

### betfront

```json
{
  "kind": "metric",
  "formula": "the draw closing of the betfront",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.4ba674e10426ee97de34a32b"
  ]
}
```

### betfront

```json
{
  "kind": "metric",
  "formula": "the away closing of the betfront",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.85cf743022e73efe84052b8e"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "the season of the football_data",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.e0f5a8b01641baea02ed80a9"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "the datetime of the football_data",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.3d21b4b58c5ec80f25986172"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "League Division",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.08a658342742ab863fa8a691"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "the country of the football_data",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.09bdaec97e6c0f4e40b3d50d"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "the league of the football_data",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.083e82c9d6e63577ab3f58f9"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Match Referee",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.2095fc2bd5a0e04ac969b35b"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Home Team",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.c9fa0746ed37c9659cd957a5"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Away Team",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.b33039e518eaaa7037285f1c"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Full Time Home Team Goals",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.afead35634a30b4cdf2e5427"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Full Time Away Team Goals",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.4b4bd025588e41538ac30b5c"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Full Time Result (H: Home Win, D: Draw, A: Away Win)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.34bf4319eb304961734988d3"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Half Time Home Team Goals",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.821bb7203ad5e987c6c45eea"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Half Time Away Team Goals",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.2cf0b68689e0f4a0576e212f"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Half Time Result (H: Home Win, D: Draw, A: Away Win)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.5c3136c15ab3f953b87ed532"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Pinnacle home win odds",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.6661c8560dd9ef4571d0240d"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Pinnacle draw odds",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.7a8033ee3beca30685d0463f"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Pinnacle away win odds",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.696d4cb885268d6fc5f1906f"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Bet365 home win odds",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.ca089e2f3ed8e0e4a3e484d2"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Bet365 draw odds",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.900724d8a3d578993ace071e"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Bet365 away win odds",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.39bfdfdd221bfabf1a52ab10"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Ladbrokes home win odds",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.65355a68d3b43cbefc76a136"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Ladbrokes draw odds",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.6819c57d360dedd300d995bc"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Ladbrokes away win odds",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.9f6ea0537bbce0e16e502168"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Bet&Win home win odds",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.46fc41660354e7e8a5901559"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Bet&Win draw odds",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.6df827f891d41e5148427037"
  ]
}
```

### football data

```json
{
  "kind": "metric",
  "formula": "Bet&Win away win odds",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.aa071f6ea2ec9cca62b6b8f3"
  ]
}
```


## 增量维护事件

- Source withdrawal preview · kaggledbqa:fewshot:WorldSoccerDataBase:005 · Review event: withdraw this saved source on a copied ontology
  - XTB_002.XCL_021:  → 
  - XTB_002.XCL_020:  → 
