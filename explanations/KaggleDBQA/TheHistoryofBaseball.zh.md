# KaggleDBQA / TheHistoryofBaseball — Schema 与业务口径解释

该数据库的存档目录包含 5 张表、44 个物理列、4 条关系，以及 51 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## XTB_001

该表的存档未记录额外业务说明。

恢复表名: hall of fame
SQL表别名: T1s

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| XTB_001.XCL_004 | ballots / ballots_cast, | text | — |
| XTB_001.XCL_008 | category / induction_category | text | — |
| XTB_001.XCL_007 | inducted / hall_of_fame_inducted | text | — |
| XTB_001.XCL_005 | needed / votes_needed | text | — |
| XTB_001.XCL_009 | needed note / hall_of_fame_ranking_note | text | — |
| XTB_001.XCL_001 | player id / player_id | text | — |
| XTB_001.XCL_003 | votedby / voting_body | text | — |
| XTB_001.XCL_006 | votes / hall_of_fame_votes | text | — |
| XTB_001.XCL_002 | yearid | number | — |

## XTB_002

该表的存档未记录额外业务说明。

恢复表名: player
SQL表别名: T1, T2s, p

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| XTB_002.XCL_016 | birth city / birth_city | text | — |
| XTB_002.XCL_014 | birth country / birth_country | text | kaggledbqa:fewshot:TheHistoryofBaseball:006 |
| XTB_002.XCL_013 | birth day / birth_day | text | — |
| XTB_002.XCL_012 | birth month / birth_month | text | — |
| XTB_002.XCL_015 | birth state / birth_state | text | — |
| XTB_002.XCL_011 | birth year / birth_year | text | kaggledbqa:fewshot:TheHistoryofBaseball:007, kaggledbqa:fewshot:TheHistoryofBaseball:011 |
| XTB_002.XCL_022 | death city / death_city | text | — |
| XTB_002.XCL_020 | death country / death_country | text | — |
| XTB_002.XCL_019 | death day / death_day | text | — |
| XTB_002.XCL_018 | death month / death_month | text | — |
| XTB_002.XCL_021 | death state / death_state | text | — |
| XTB_002.XCL_017 | death year / death_year | text | kaggledbqa:fewshot:TheHistoryofBaseball:011 |
| XTB_002.XCL_023 | name first / canonical_name | text | kaggledbqa:fewshot:TheHistoryofBaseball:007 |
| XTB_002.XCL_025 | name given / given_name | text | — |
| XTB_002.XCL_024 | name last / last_name | text | kaggledbqa:fewshot:TheHistoryofBaseball:007 |
| XTB_002.XCL_010 | player id / player_id | text | — |
| XTB_002.XCL_026 | weight / player_weight | text | — |

## XTB_003

该表的存档未记录额外业务说明。

恢复表名: player award
SQL表别名: T2, T3, T3s, a, pa

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| XTB_003.XCL_028 | award id / award_name | text | — |
| XTB_003.XCL_030 | league id / league_id | text | — |
| XTB_003.XCL_032 | notes | text | — |
| XTB_003.XCL_027 | player id / player_id | text | — |
| XTB_003.XCL_031 | tie | text | — |
| XTB_003.XCL_029 | year / award_year | number | — |

## XTB_004

该表的存档未记录额外业务说明。

恢复表名: player award vote
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| XTB_004.XCL_033 | award id / award_name | text | — |
| XTB_004.XCL_035 | league id / league_id | text | — |
| XTB_004.XCL_036 | player id / player_id | text | — |
| XTB_004.XCL_038 | points max / maximum_vote_points | number | — |
| XTB_004.XCL_037 | points won / points_won | number | — |
| XTB_004.XCL_039 | votes first / first_place_votes | text | — |
| XTB_004.XCL_034 | year / award_year | number | — |

## XTB_005

该表的存档未记录额外业务说明。

恢复表名: salary
SQL表别名: T5, s

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| XTB_005.XCL_042 | league id / league_id | text | kaggledbqa:fewshot:TheHistoryofBaseball:005, kaggledbqa:fewshot:TheHistoryofBaseball:008, kaggledbqa:fewshot:TheHistoryofBaseball:001, kaggledbqa:fewshot:TheHistoryofBaseball:002 |
| XTB_005.XCL_043 | player id / player_id | text | — |
| XTB_005.XCL_044 | salary | number | kaggledbqa:fewshot:TheHistoryofBaseball:005, kaggledbqa:fewshot:TheHistoryofBaseball:008, kaggledbqa:fewshot:TheHistoryofBaseball:001, kaggledbqa:fewshot:TheHistoryofBaseball:002 |
| XTB_005.XCL_041 | team id / team_id | text | — |
| XTB_005.XCL_040 | year | number | — |

## 表关系与连接依据

- XTB_001.XCL_001 ↔ XTB_002.XCL_010; declared_or_materialized_relationship
- XTB_001.XCL_001 ↔ XTB_003.XCL_027; declared_or_materialized_relationship
- XTB_001.XCL_001 ↔ XTB_004.XCL_036; declared_or_materialized_relationship
- XTB_001.XCL_001 ↔ XTB_005.XCL_043; declared_or_materialized_relationship

## 业务口径、总体与粒度

### SELECT "XCL_023", "XCL_024" FROM "XTB_002" ORDER BY "XCL_011" DESC LIMIT 1

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_023\", \"XCL_024\" FROM \"XTB_002\" ORDER BY \"XCL_011\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:TheHistoryofBaseball:007"
  ]
}
```

### SELECT "XCL_042" FROM "XTB_005" GROUP BY "XCL_042" ORDER BY AVG("XCL_044") DESC LIMIT 1

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_042\" FROM \"XTB_005\" GROUP BY \"XCL_042\" ORDER BY AVG(\"XCL_044\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:TheHistoryofBaseball:005"
  ]
}
```

### SELECT "XCL_042" FROM "XTB_005" GROUP BY "XCL_042" ORDER BY SUM("XCL_044") DESC LIMIT 1

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_042\" FROM \"XTB_005\" GROUP BY \"XCL_042\" ORDER BY SUM(\"XCL_044\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:TheHistoryofBaseball:008",
    "kaggledbqa:fewshot:TheHistoryofBaseball:001"
  ]
}
```

### SELECT AVG("XCL_017" - "XCL_011") FROM "XTB_002"

```json
{
  "kind": "program",
  "formula": "SELECT AVG(\"XCL_017\" - \"XCL_011\") FROM \"XTB_002\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:TheHistoryofBaseball:011"
  ]
}
```

### SELECT "XCL_014" FROM "XTB_002" GROUP BY "XCL_014" ORDER BY COUNT(*) DESC LIMIT 1

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_014\" FROM \"XTB_002\" GROUP BY \"XCL_014\" ORDER BY COUNT(*) DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:TheHistoryofBaseball:006"
  ]
}
```

### SELECT "XCL_042" FROM "XTB_005" GROUP BY "XCL_042" ORDER BY MAX("XCL_044") - MIN("XCL_044") DESC LIMIT 1

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_042\" FROM \"XTB_005\" GROUP BY \"XCL_042\" ORDER BY MAX(\"XCL_044\") - MIN(\"XCL_044\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:TheHistoryofBaseball:002"
  ]
}
```

### "XTB_005"."XCL_042"

```json
{
  "kind": "binding",
  "formula": "\"XTB_005\".\"XCL_042\"",
  "grain": [
    "\"XTB_005\".\"XCL_042\""
  ],
  "population_scope": "SELECT \"XCL_042\" FROM \"XTB_005\" GROUP BY \"XCL_042\" ORDER BY SUM(\"XCL_044\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:TheHistoryofBaseball:008",
    "kaggledbqa:fewshot:TheHistoryofBaseball:001"
  ]
}
```

### AVG("XTB_002"."XCL_017" - "XTB_002"."XCL_011")

```json
{
  "kind": "metric",
  "formula": "AVG(\"XTB_002\".\"XCL_017\" - \"XTB_002\".\"XCL_011\")",
  "grain": [],
  "population_scope": "SELECT AVG(\"XCL_017\" - \"XCL_011\") FROM \"XTB_002\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_017\" - \"r0\".\"XCL_011\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_002"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_017\" - \"r0\".\"XCL_011\") AS \"value\" FROM \"XTB_002\" AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:TheHistoryofBaseball:011"
  ]
}
```

### "XTB_002"."XCL_024"

```json
{
  "kind": "binding",
  "formula": "\"XTB_002\".\"XCL_024\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_023\", \"XCL_024\" FROM \"XTB_002\" ORDER BY \"XCL_011\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:TheHistoryofBaseball:007"
  ]
}
```

### "XTB_002"."XCL_014"

```json
{
  "kind": "binding",
  "formula": "\"XTB_002\".\"XCL_014\"",
  "grain": [
    "\"XTB_002\".\"XCL_014\""
  ],
  "population_scope": "SELECT \"XCL_014\" FROM \"XTB_002\" GROUP BY \"XCL_014\" ORDER BY COUNT(*) DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:TheHistoryofBaseball:006"
  ]
}
```

### "XTB_005"."XCL_042"

```json
{
  "kind": "binding",
  "formula": "\"XTB_005\".\"XCL_042\"",
  "grain": [
    "\"XTB_005\".\"XCL_042\""
  ],
  "population_scope": "SELECT \"XCL_042\" FROM \"XTB_005\" GROUP BY \"XCL_042\" ORDER BY MAX(\"XCL_044\") - MIN(\"XCL_044\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:TheHistoryofBaseball:002"
  ]
}
```

### "XTB_005"."XCL_042"

```json
{
  "kind": "binding",
  "formula": "\"XTB_005\".\"XCL_042\"",
  "grain": [
    "\"XTB_005\".\"XCL_042\""
  ],
  "population_scope": "SELECT \"XCL_042\" FROM \"XTB_005\" GROUP BY \"XCL_042\" ORDER BY AVG(\"XCL_044\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:TheHistoryofBaseball:005"
  ]
}
```

### "XTB_002"."XCL_023"

```json
{
  "kind": "binding",
  "formula": "\"XTB_002\".\"XCL_023\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_023\", \"XCL_024\" FROM \"XTB_002\" ORDER BY \"XCL_011\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:TheHistoryofBaseball:007"
  ]
}
```

### hall of fame

```json
{
  "kind": "metric",
  "formula": "Player ID code",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.887ffaebab9b012ffcec5871"
  ]
}
```

### hall of fame

```json
{
  "kind": "metric",
  "formula": "Year of ballot",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.de15e2efc9a2a885539689c8"
  ]
}
```

### hall of fame

```json
{
  "kind": "metric",
  "formula": "Method by which player was voted upon",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.d307d9b60134255cb99b3cf2"
  ]
}
```

### hall of fame

```json
{
  "kind": "metric",
  "formula": "Total ballots cast in that year",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.c9b940719dedc73450e78347"
  ]
}
```

### hall of fame

```json
{
  "kind": "metric",
  "formula": "Number of votes needed for selection in that year",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.f58bdcf10363c317eee4fe9c"
  ]
}
```

### hall of fame

```json
{
  "kind": "metric",
  "formula": "Total votes received",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.b4ecc0ae816eca4d0feb58ae"
  ]
}
```

### hall of fame

```json
{
  "kind": "metric",
  "formula": "Whether player was inducted by that vote or not (Y or N)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.9bd7f985d35b268429603a6c"
  ]
}
```

### hall of fame

```json
{
  "kind": "metric",
  "formula": "Category in which candidate was honored",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.add973a6b3f345467db73540"
  ]
}
```

### hall of fame

```json
{
  "kind": "metric",
  "formula": "Explanation of qualifiers for special elections",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.411a645462f46c0425c27be4"
  ]
}
```

### player award

```json
{
  "kind": "metric",
  "formula": "Player ID code",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.7523f946ca0eed92faf4b4a2"
  ]
}
```

### player award

```json
{
  "kind": "metric",
  "formula": "Name of award won",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.a936d0f406912d67e6d5a686"
  ]
}
```

### player award

```json
{
  "kind": "metric",
  "formula": "the year of the player_award",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.23258e4fda2ae7805c7d68ef"
  ]
}
```

### player award

```json
{
  "kind": "metric",
  "formula": "the league id of the player_award",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.4c9f2d272426fc6f19d65f07"
  ]
}
```

### player award

```json
{
  "kind": "metric",
  "formula": "Award was a tie (Y or N)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.2b40fbbeba78ee5e2f149a30"
  ]
}
```

### player award

```json
{
  "kind": "metric",
  "formula": "Notes about the award",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.ea29eac64440ac7ccf37f536"
  ]
}
```

### player award vote

```json
{
  "kind": "metric",
  "formula": "name of award votes were received for",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.440ed952252e8a641fb9b25b"
  ]
}
```

### player award vote

```json
{
  "kind": "metric",
  "formula": "the year of the player_award_vote",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.900f51eff5e68d64cca907ae"
  ]
}
```

### player award vote

```json
{
  "kind": "metric",
  "formula": "the league id of the player_award_vote",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.4184f80eeddf817a13393d83"
  ]
}
```

### player award vote

```json
{
  "kind": "metric",
  "formula": "Player ID code",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.21f96c821dbc64927d491e75"
  ]
}
```

### player award vote

```json
{
  "kind": "metric",
  "formula": "Number of points received",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.7b0fff1732aafcfeea28e765"
  ]
}
```

### player award vote

```json
{
  "kind": "metric",
  "formula": "Maximum numner of points possible",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.331af32d6a281168b9c8a42f"
  ]
}
```

### player award vote

```json
{
  "kind": "metric",
  "formula": "Number of first place votes",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.b0f5b55a11cbb5f6e54a0ebe"
  ]
}
```

### salary

```json
{
  "kind": "metric",
  "formula": "the year of the salary",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.72c4e772c3c9da5ef446f138"
  ]
}
```

### salary

```json
{
  "kind": "metric",
  "formula": "Team",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.a4a61693fc46948d92495c00"
  ]
}
```

### salary

```json
{
  "kind": "metric",
  "formula": "the league id of the salary",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.5f8e3e56e30f408930300b06"
  ]
}
```

### salary

```json
{
  "kind": "metric",
  "formula": "Player ID code",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.eb21101c8adec05ed66d9995"
  ]
}
```

### salary

```json
{
  "kind": "metric",
  "formula": "Salary",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.a26b87c8aca7fb93d834b19f"
  ]
}
```

### player

```json
{
  "kind": "metric",
  "formula": "Player ID code",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.c81df3e2f7e15a78eb06512f"
  ]
}
```

### player

```json
{
  "kind": "metric",
  "formula": "Year player was born",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.8254cbd468a4359c1a4c5b45"
  ]
}
```

### player

```json
{
  "kind": "metric",
  "formula": "Month player was born",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.baaef280e83831a97d2febae"
  ]
}
```

### player

```json
{
  "kind": "metric",
  "formula": "Day player was born",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.3de6d8f8f4ce3c9d778003a9"
  ]
}
```

### player

```json
{
  "kind": "metric",
  "formula": "Country where player was born",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.ff9cc29530c7c88b776c31af"
  ]
}
```

### player

```json
{
  "kind": "metric",
  "formula": "State where player was born",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.0b3afee35d89aca6c4548a65"
  ]
}
```

### player

```json
{
  "kind": "metric",
  "formula": "City where player was born",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.90ed0bd19c231a380201a6f8"
  ]
}
```

### player

```json
{
  "kind": "metric",
  "formula": "Year player died",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.67e743f98f7de7198f7610ae"
  ]
}
```

### player

```json
{
  "kind": "metric",
  "formula": "Month player died",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.19e4826bd34f640406f26278"
  ]
}
```

### player

```json
{
  "kind": "metric",
  "formula": "Day player died",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.d3961b80a37669340c8d88eb"
  ]
}
```

### player

```json
{
  "kind": "metric",
  "formula": "Country where player died",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.4a956ef9fbdc484a5bf5a050"
  ]
}
```

### player

```json
{
  "kind": "metric",
  "formula": "State where player died",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.73f0401000b8f7932ce97505"
  ]
}
```

### player

```json
{
  "kind": "metric",
  "formula": "City where player died",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.e5d3e394a617ba909e6617bb"
  ]
}
```

### player

```json
{
  "kind": "metric",
  "formula": "Player's first name",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.3dd8e1948116c13be020df8f"
  ]
}
```

### player

```json
{
  "kind": "metric",
  "formula": "Player's last name",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.4359322d967b79a813c0c3d7"
  ]
}
```

### player

```json
{
  "kind": "metric",
  "formula": "Player's given name (typically first and middle)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.4ba55310b5de1b14f67c111f"
  ]
}
```

### player

```json
{
  "kind": "metric",
  "formula": "Player's weight in pounds",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.3f052410128d92f7ffe6ebb1"
  ]
}
```


## 增量维护事件

- Source withdrawal preview · kaggledbqa:fewshot:TheHistoryofBaseball:007 · Review event: withdraw this saved source on a copied ontology
  - XTB_002.XCL_011:  → 
  - XTB_002.XCL_024:  → 
  - XTB_002.XCL_023:  → 
