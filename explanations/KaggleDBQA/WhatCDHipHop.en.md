# KaggleDBQA / WhatCDHipHop — Schema and business semantics

The saved catalogue for this database contains 2 tables, 10 physical columns, 1 relationships and 15 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## XTB_001

No additional table purpose is recorded in this archive.

Recovered table names: tags
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| XTB_001.XCL_002 | id / tag_id | number | — |
| XTB_001.XCL_001 | index | number | — |
| XTB_001.XCL_003 | tag | text | — |

## XTB_002

No additional table purpose is recorded in this archive.

Recovered table names: torrents
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| XTB_002.XCL_006 | artist | text | kaggledbqa:fewshot:WhatCDHipHop:009 |
| XTB_002.XCL_009 | group id / group_id | number | — |
| XTB_002.XCL_004 | group name / group_name | text | kaggledbqa:fewshot:WhatCDHipHop:011, kaggledbqa:fewshot:WhatCDHipHop:012 |
| XTB_002.XCL_007 | group year / group_year | number | kaggledbqa:fewshot:WhatCDHipHop:007 |
| XTB_002.XCL_010 | id / torrent_id | number | — |
| XTB_002.XCL_008 | release type / release_type | text | kaggledbqa:fewshot:WhatCDHipHop:008 |
| XTB_002.XCL_005 | total snatched / totalSnatched | number | kaggledbqa:fewshot:WhatCDHipHop:011, kaggledbqa:fewshot:WhatCDHipHop:007 |

## Relationships and join evidence

- XTB_001.XCL_002 ↔ XTB_002.XCL_010; declared_or_materialized_relationship

## Business definitions, population and grain

### SELECT SUM("XCL_005"), "XCL_007" FROM "XTB_002" GROUP BY "XCL_007"

```json
{
  "kind": "program",
  "formula": "SELECT SUM(\"XCL_005\"), \"XCL_007\" FROM \"XTB_002\" GROUP BY \"XCL_007\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:WhatCDHipHop:007"
  ]
}
```

### SELECT COUNT(*), "XCL_006" FROM "XTB_002" GROUP BY "XCL_006"

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(*), \"XCL_006\" FROM \"XTB_002\" GROUP BY \"XCL_006\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:WhatCDHipHop:009"
  ]
}
```

### SELECT "XCL_004" FROM "XTB_002" ORDER BY "XCL_005" LIMIT 1

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_004\" FROM \"XTB_002\" ORDER BY \"XCL_005\" LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:WhatCDHipHop:011"
  ]
}
```

### SELECT COUNT(*), "XCL_008" FROM "XTB_002" GROUP BY "XCL_008"

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(*), \"XCL_008\" FROM \"XTB_002\" GROUP BY \"XCL_008\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:WhatCDHipHop:008"
  ]
}
```

### SELECT DISTINCT "XCL_004" FROM "XTB_002"

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_004\" FROM \"XTB_002\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:WhatCDHipHop:012"
  ]
}
```

### "XTB_002"."XCL_004"

```json
{
  "kind": "binding",
  "formula": "\"XTB_002\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_004\" FROM \"XTB_002\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:WhatCDHipHop:012"
  ]
}
```

### SUM("XTB_002"."XCL_005")

```json
{
  "kind": "metric",
  "formula": "SUM(\"XTB_002\".\"XCL_005\")",
  "grain": [
    "\"XTB_002\".\"XCL_007\""
  ],
  "population_scope": "SELECT SUM(\"XCL_005\"), \"XCL_007\" FROM \"XTB_002\" GROUP BY \"XCL_007\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r0\".\"XCL_005\")",
    "grain": [
      "\"r0\".\"XCL_007\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_002"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_007\" AS \"grain_0\", SUM(\"r0\".\"XCL_005\") AS \"value\" FROM \"XTB_002\" AS \"r0\" GROUP BY \"r0\".\"XCL_007\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:WhatCDHipHop:007"
  ]
}
```

### "XTB_002"."XCL_007"

```json
{
  "kind": "binding",
  "formula": "\"XTB_002\".\"XCL_007\"",
  "grain": [
    "\"XTB_002\".\"XCL_007\""
  ],
  "population_scope": "SELECT SUM(\"XCL_005\"), \"XCL_007\" FROM \"XTB_002\" GROUP BY \"XCL_007\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_007\"",
    "grain": [
      "\"r0\".\"XCL_007\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_002"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_007\" AS \"grain_0\", \"r0\".\"XCL_007\" AS \"value\" FROM \"XTB_002\" AS \"r0\" GROUP BY \"r0\".\"XCL_007\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:WhatCDHipHop:007"
  ]
}
```

### "XTB_002"."XCL_004"

```json
{
  "kind": "binding",
  "formula": "\"XTB_002\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_004\" FROM \"XTB_002\" ORDER BY \"XCL_005\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa:fewshot:WhatCDHipHop:011"
  ]
}
```

### COUNT(*)

```json
{
  "kind": "metric",
  "formula": "COUNT(*)",
  "grain": [
    "\"XTB_002\".\"XCL_008\""
  ],
  "population_scope": "SELECT COUNT(*), \"XCL_008\" FROM \"XTB_002\" GROUP BY \"XCL_008\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(*)",
    "grain": [
      "\"r0\".\"XCL_008\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_002"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_008\" AS \"grain_0\", COUNT(*) AS \"value\" FROM \"XTB_002\" AS \"r0\" GROUP BY \"r0\".\"XCL_008\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:WhatCDHipHop:008"
  ]
}
```

### "XTB_002"."XCL_006"

```json
{
  "kind": "binding",
  "formula": "\"XTB_002\".\"XCL_006\"",
  "grain": [
    "\"XTB_002\".\"XCL_006\""
  ],
  "population_scope": "SELECT COUNT(*), \"XCL_006\" FROM \"XTB_002\" GROUP BY \"XCL_006\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_006\"",
    "grain": [
      "\"r0\".\"XCL_006\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_002"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_006\" AS \"grain_0\", \"r0\".\"XCL_006\" AS \"value\" FROM \"XTB_002\" AS \"r0\" GROUP BY \"r0\".\"XCL_006\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:WhatCDHipHop:009"
  ]
}
```

### "XTB_002"."XCL_008"

```json
{
  "kind": "binding",
  "formula": "\"XTB_002\".\"XCL_008\"",
  "grain": [
    "\"XTB_002\".\"XCL_008\""
  ],
  "population_scope": "SELECT COUNT(*), \"XCL_008\" FROM \"XTB_002\" GROUP BY \"XCL_008\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_008\"",
    "grain": [
      "\"r0\".\"XCL_008\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_002"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_008\" AS \"grain_0\", \"r0\".\"XCL_008\" AS \"value\" FROM \"XTB_002\" AS \"r0\" GROUP BY \"r0\".\"XCL_008\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:WhatCDHipHop:008"
  ]
}
```

### COUNT(*)

```json
{
  "kind": "metric",
  "formula": "COUNT(*)",
  "grain": [
    "\"XTB_002\".\"XCL_006\""
  ],
  "population_scope": "SELECT COUNT(*), \"XCL_006\" FROM \"XTB_002\" GROUP BY \"XCL_006\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(*)",
    "grain": [
      "\"r0\".\"XCL_006\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "XTB_002"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_006\" AS \"grain_0\", COUNT(*) AS \"value\" FROM \"XTB_002\" AS \"r0\" GROUP BY \"r0\".\"XCL_006\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "kaggledbqa:fewshot:WhatCDHipHop:009"
  ]
}
```

### torrents

```json
{
  "kind": "metric",
  "formula": "Release title",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.16098690314563534683c8a5"
  ]
}
```

### torrents

```json
{
  "kind": "metric",
  "formula": "Number of times the release has been downloaded.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.427b0129f7db416025ab09d9"
  ]
}
```

### torrents

```json
{
  "kind": "metric",
  "formula": "Artist/group name.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.cf0b3f5e868503781a95ce25"
  ]
}
```

### torrents

```json
{
  "kind": "metric",
  "formula": "Release year.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.39f730607f6c47a1a2ca196e"
  ]
}
```

### torrents

```json
{
  "kind": "metric",
  "formula": "Release type (e.g. album single mixtape)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.9188e5495815db9c6a4f1fdd"
  ]
}
```

### torrents

```json
{
  "kind": "metric",
  "formula": "Unique release identifier from What.CD. Used to ensure no releases are duplicates.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.14a3fb0654f393e850845968"
  ]
}
```

### torrents

```json
{
  "kind": "metric",
  "formula": "unique identifier (essentially an index).",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.d60481325db2e5308e889f29"
  ]
}
```

### tags

```json
{
  "kind": "metric",
  "formula": "the index of the tags",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.cfad6399583b061ff846a1a1"
  ]
}
```

### tags

```json
{
  "kind": "metric",
  "formula": "unique identifier (essentially an index).",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.44f95a11030ff89e575dc66d"
  ]
}
```

### tags

```json
{
  "kind": "metric",
  "formula": "the tag of the tags",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "kaggledbqa_kb.8c6b864c580969a1e0d2de8c"
  ]
}
```


## Incremental maintenance events

- Source withdrawal preview · kaggledbqa:fewshot:WhatCDHipHop:007 · Review event: withdraw this saved source on a copied ontology
  - XTB_002.XCL_005:  → 
  - XTB_002.XCL_007:  → 
