# BIRD-History / card_games — Schema 与业务口径解释

该数据库的存档目录包含 6 张表、78 个物理列、14 条关系，以及 191 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## cards

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: C, C2, T1, T1b, T2, T3, T4, c, c1, c2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cards.XCL_001 | id | unknown | bird_dev:436, bird_dev:346, bird_dev:372, bird_dev:410, bird_dev:371, bird_dev:370, bird_dev:395, bird_dev:526 |
| cards.XCL_002 | artist | unknown | bird_dev:411, bird_dev:346, bird_dev:410, bird_dev:521, bird_dev:508, bird_dev:395, bird_dev:526, bird_dev:494 |
| cards.XCL_004 | availability | unknown | bird_dev:410, bird_dev:508, bird_dev:395, bird_dev:526, bird_dev:396, bird_dev:374, bird_dev:451, bird_dev:397 |
| cards.XCL_005 | border_color | unknown | bird_dev:370, bird_dev:368, bird_dev:374, bird_dev:435, bird_dev:341, bird_dev:397, bird_dev:437, bird_dev:394 |
| cards.XCL_006 | card_kingdom_foil_id | unknown | bird_dev:511, bird_dev:487, bird_dev:378, bird_dev:393, bird_dev:394, bird_dev:423, bird_dev:340, bird_dev:450 |
| cards.XCL_007 | card_kingdom_id | unknown | bird_dev:511, bird_dev:487, bird_dev:378, bird_dev:341, bird_dev:393, bird_dev:394, bird_dev:423, bird_dev:340 |
| cards.XCL_010 | color | unknown | bird_dev:391, bird_dev:387, bird_dev:390 |
| cards.XCL_011 | power | unknown | bird_dev:510, bird_dev:446, bird_dev:461, bird_dev:501, bird_dev:484, bird_dev:388, bird_dev:479, bird_dev:476 |
| cards.XCL_012 | duel_deck_side | unknown | bird_dev:379, bird_dev:512 |
| cards.XCL_013 | price | unknown | bird_dev:522, bird_dev:343, bird_dev:380, bird_dev:419 |
| cards.XCL_014 | edhrec_rank | unknown | bird_dev:342 |
| cards.XCL_016 | 保留物理名称；存档没有恢复别名 | unknown | bird_dev:460 |
| cards.XCL_018 | frame_effects | unknown | bird_dev:436, bird_dev:511, bird_dev:401 |
| cards.XCL_019 | frame_version | unknown | bird_dev:521, bird_dev:396, bird_dev:461, bird_dev:397, bird_dev:386, bird_dev:343, bird_dev:530, bird_dev:380 |
| cards.XCL_020 | toughness | unknown | bird_dev:395, bird_dev:451 |
| cards.XCL_022 | is_textless | unknown | bird_dev:521, bird_dev:494, bird_dev:396, bird_dev:415, bird_dev:347 |
| cards.XCL_023 | 保留物理名称；存档没有恢复别名 | unknown | bird_dev:512 |
| cards.XCL_026 | 保留物理名称；存档没有恢复别名 | unknown | bird_dev:437 |
| cards.XCL_027 | is_legendary | unknown | bird_dev:401 |
| cards.XCL_028 | 保留物理名称；存档没有恢复别名 | unknown | bird_dev:420 |
| cards.XCL_029 | is_starter | unknown | bird_dev:349, bird_dev:455, bird_dev:420 |
| cards.XCL_030 | 保留物理名称；存档没有恢复别名 | unknown | bird_dev:369, bird_dev:420 |
| cards.XCL_032 | is_restricted | unknown | bird_dev:363 |
| cards.XCL_033 | is_banned | unknown | bird_dev:371, bird_dev:402 |
| cards.XCL_034 | is_story_spotlight | unknown | bird_dev:508, bird_dev:402, bird_dev:424, bird_dev:361, bird_dev:452 |
| cards.XCL_036 | abilities | unknown | bird_dev:355, bird_dev:376 |
| cards.XCL_037 | layout | unknown | bird_dev:397, bird_dev:424, bird_dev:376, bird_dev:412 |
| cards.XCL_041 | mana_cost | unknown | bird_dev:514, bird_dev:397, bird_dev:398, bird_dev:453 |
| cards.XCL_049 | name | unknown | bird_dev:362, bird_dev:485, bird_dev:462, bird_dev:518, bird_dev:456, bird_dev:514, bird_dev:355, bird_dev:522 |
| cards.XCL_050 | number | unknown | bird_dev:350, bird_dev:478, bird_dev:348 |
| cards.XCL_051 | flavor_text | unknown | bird_dev:515 |
| cards.XCL_053 | type_line | unknown | bird_dev:391, bird_dev:389, bird_dev:359, bird_dev:377 |
| cards.XCL_055 | power | unknown | bird_dev:346, bird_dev:416, bird_dev:479, bird_dev:421, bird_dev:454, bird_dev:356, bird_dev:512, bird_dev:408 |
| cards.XCL_057 | frame_effect | unknown | bird_dev:457, bird_dev:421, bird_dev:357 |
| cards.XCL_058 | links | unknown | bird_dev:457 |
| cards.XCL_059 | rarity | unknown | bird_dev:344, bird_dev:517, bird_dev:413, bird_dev:392, bird_dev:515 |
| cards.XCL_063 | set_code | unknown | bird_dev:462, bird_dev:469, bird_dev:487, bird_dev:446, bird_dev:501, bird_dev:500, bird_dev:484, bird_dev:503 |
| cards.XCL_064 | content_warning | unknown | bird_dev:510, bird_dev:409, bird_dev:345, bird_dev:455, bird_dev:425 |
| cards.XCL_065 | subtypes | unknown | bird_dev:456, bird_dev:399, bird_dev:425, bird_dev:407, bird_dev:377 |
| cards.XCL_066 | supertypes | unknown | bird_dev:456, bird_dev:399, bird_dev:407 |
| cards.XCL_069 | toughness | unknown | bird_dev:372 |
| cards.XCL_070 | type_line | unknown | bird_dev:365, bird_dev:449, bird_dev:444, bird_dev:448, bird_dev:482, bird_dev:345, bird_dev:354 |
| cards.XCL_071 | card_type | unknown | bird_dev:406, bird_dev:517, bird_dev:412 |
| cards.XCL_072 | uuid | unknown | bird_dev:362, bird_dev:411, bird_dev:346, bird_dev:485, bird_dev:410, bird_dev:371, bird_dev:370, bird_dev:518 |
| cards.XCL_074 | watermark | unknown | bird_dev:445, bird_dev:449, bird_dev:444, bird_dev:448 |

## foreign_data

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: F2, T1, T2, T3, T4, T4b, T5, f, fd, fd2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| foreign_data.XCL_076 | flavor_text | unknown | bird_dev:411, bird_dev:445, bird_dev:481, bird_dev:480 |
| foreign_data.XCL_077 | language | unknown | bird_dev:371, bird_dev:370, bird_dev:352, bird_dev:416, bird_dev:445, bird_dev:403, bird_dev:449, bird_dev:484 |
| foreign_data.XCL_078 | card_id | unknown | bird_dev:422 |
| foreign_data.XCL_079 | name | unknown | bird_dev:403, bird_dev:440, bird_dev:412 |
| foreign_data.XCL_080 | text | unknown | bird_dev:483 |
| foreign_data.XCL_082 | uuid | unknown | bird_dev:411, bird_dev:371, bird_dev:370, bird_dev:365, bird_dev:352, bird_dev:416, bird_dev:445, bird_dev:449 |

## legalities

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: L, L2, T1, T2, T2b, T3, T3b, T4, T6, l, l2, l3

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| legalities.XCL_084 | format | unknown | bird_dev:346, bird_dev:410, bird_dev:518, bird_dev:521, bird_dev:514, bird_dev:522, bird_dev:520, bird_dev:344 |
| legalities.XCL_085 | legality_status | unknown | bird_dev:346, bird_dev:518, bird_dev:521, bird_dev:522, bird_dev:364, bird_dev:363, bird_dev:344, bird_dev:361 |
| legalities.XCL_086 | card_id | unknown | bird_dev:346, bird_dev:410, bird_dev:518, bird_dev:521, bird_dev:514, bird_dev:522, bird_dev:364, bird_dev:363 |

## rulings

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T2, T3, T4, r

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| rulings.XCL_088 | ruling_date | unknown | bird_dev:485, bird_dev:389, bird_dev:527, bird_dev:413, bird_dev:392 |
| rulings.XCL_089 | ruling_text | unknown | bird_dev:362, bird_dev:494, bird_dev:409, bird_dev:527, bird_dev:348, bird_dev:347, bird_dev:385, bird_dev:408 |
| rulings.XCL_090 | card_uuid | unknown | bird_dev:362, bird_dev:485, bird_dev:494, bird_dev:389, bird_dev:406, bird_dev:409, bird_dev:527, bird_dev:349 |

## set_translations

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: ST, T2, T3, T4, st, st2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| set_translations.XCL_091 | translation_id | unknown | bird_dev:387, bird_dev:523, bird_dev:388, bird_dev:429, bird_dev:428, bird_dev:438 |
| set_translations.XCL_092 | language | unknown | bird_dev:400, bird_dev:434, bird_dev:427, bird_dev:414, bird_dev:468, bird_dev:472, bird_dev:353, bird_dev:431 |
| set_translations.XCL_093 | set_code | unknown | bird_dev:441, bird_dev:400, bird_dev:434, bird_dev:502, bird_dev:427, bird_dev:414, bird_dev:468, bird_dev:472 |
| set_translations.XCL_094 | translated_set_name | unknown | bird_dev:502, bird_dev:462, bird_dev:468, bird_dev:472, bird_dev:467, bird_dev:500, bird_dev:498, bird_dev:463 |

## sets

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: S, T1, T2, T2b, T3, T4, T5, s, s2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| sets.XCL_095 | set_id | unknown | bird_dev:434, bird_dev:472, bird_dev:431, bird_dev:509, bird_dev:523, bird_dev:506, bird_dev:519, bird_dev:507 |
| sets.XCL_096 | base_set_size | unknown | bird_dev:414, bird_dev:509, bird_dev:467, bird_dev:442, bird_dev:404, bird_dev:432, bird_dev:496, bird_dev:474 |
| sets.XCL_097 | block | unknown | bird_dev:414, bird_dev:472, bird_dev:442, bird_dev:430, bird_dev:405 |
| sets.XCL_099 | code | unknown | bird_dev:441, bird_dev:439, bird_dev:434, bird_dev:502, bird_dev:488, bird_dev:427, bird_dev:414, bird_dev:489 |
| sets.XCL_100 | 保留物理名称；存档没有恢复别名 | unknown | bird_dev:431 |
| sets.XCL_101 | 保留物理名称；存档没有恢复别名 | unknown | bird_dev:431 |
| sets.XCL_102 | 保留物理名称；存档没有恢复别名 | unknown | bird_dev:506 |
| sets.XCL_103 | 保留物理名称；存档没有恢复别名 | unknown | bird_dev:507, bird_dev:433 |
| sets.XCL_105 | tcgplayer_code | unknown | bird_dev:489 |
| sets.XCL_106 | card_count | unknown | bird_dev:490 |
| sets.XCL_108 | name | unknown | bird_dev:427, bird_dev:491 |
| sets.XCL_109 | parent_code | unknown | bird_dev:434, bird_dev:469, bird_dev:426 |
| sets.XCL_110 | set_name | unknown | bird_dev:492, bird_dev:439, bird_dev:468, bird_dev:353, bird_dev:487, bird_dev:431, bird_dev:501, bird_dev:484 |
| sets.XCL_111 | block_code | unknown | bird_dev:493 |
| sets.XCL_112 | release_date | unknown | bird_dev:441, bird_dev:502, bird_dev:488, bird_dev:523, bird_dev:470, bird_dev:495, bird_dev:491 |
| sets.XCL_114 | order_number | unknown | bird_dev:353, bird_dev:513 |
| sets.XCL_115 | set_type | unknown | bird_dev:492, bird_dev:503, bird_dev:429, bird_dev:447, bird_dev:417, bird_dev:471, bird_dev:443, bird_dev:513 |

## 表关系与连接依据

- cards.XCL_063 ↔ set_translations.XCL_093; target_disjoint_historical_join
- cards.XCL_063 ↔ sets.XCL_099; target_disjoint_historical_join
- cards.XCL_072 ↔ foreign_data.XCL_082; target_disjoint_historical_join
- cards.XCL_072 ↔ legalities.XCL_086; target_disjoint_historical_join
- cards.XCL_072 ↔ rulings.XCL_090; target_disjoint_historical_join
- set_translations.XCL_091 ↔ sets.XCL_095; target_disjoint_historical_join
- set_translations.XCL_093 ↔ sets.XCL_099; target_disjoint_historical_join
- cards.XCL_063 ↔ set_translations.XCL_093; sql_workload_observed_join
- cards.XCL_063 ↔ sets.XCL_099; sql_workload_observed_join
- cards.XCL_072 ↔ foreign_data.XCL_082; sql_workload_observed_join
- cards.XCL_072 ↔ legalities.XCL_086; sql_workload_observed_join
- cards.XCL_072 ↔ rulings.XCL_090; sql_workload_observed_join
- set_translations.XCL_091 ↔ sets.XCL_095; sql_workload_observed_join
- set_translations.XCL_093 ↔ sets.XCL_099; sql_workload_observed_join

## 业务口径、总体与粒度

### Legal Cards in Hour of Devastation

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_049\", CASE WHEN T1.\"XCL_085\" = 'Legal' THEN T1.\"XCL_084\" ELSE NULL END FROM legalities AS T1 INNER JOIN cards AS T2 ON T2.\"XCL_072\" = T1.\"XCL_086\" WHERE T2.\"XCL_063\" IN (SELECT \"XCL_099\" FROM sets WHERE \"XCL_110\" = 'Hour of Devastation')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:528"
  ]
}
```

### A query that retrieves distinct values from column "XCL_036" in the "cards" table where column "XCL_049" matches the literal string 'Angel of Mercy'. 

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_036\" FROM cards WHERE \"XCL_049\" = 'Angel of Mercy'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:355"
  ]
}
```

### Full SQL program that joins cards and legalities tables to retrieve distinct legality identifiers for cards matching specific designer, year, and form

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_085\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T2.\"XCL_086\" = T1.\"XCL_072\" WHERE T1.\"XCL_019\" = 1997 AND T1.\"XCL_022\" = 1 AND T1.\"XCL_002\" = 'D. Alexander Gregory' AND T2.\"XCL_084\" = 'legacy'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:521"
  ]
}
```

### A complete query that calculates the number of distinct, non-null translation entries for the card named 'Angel of Mercy'. It joins the set_translatio

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT \"XCL_094\") FROM set_translations WHERE \"XCL_093\" IN (SELECT \"XCL_063\" FROM cards WHERE \"XCL_049\" = 'Angel of Mercy') AND NOT \"XCL_094\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:463"
  ]
}
```

### A query that retrieves the set translation (XCL_092) for the set containing the card 'Angel of Mercy' by joining cards and set_translations on the car

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_092\" FROM set_translations WHERE \"XCL_091\" IN (SELECT \"XCL_001\" FROM cards WHERE \"XCL_049\" = 'Angel of Mercy')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:360"
  ]
}
```

### Full SQL program that selects the 'XCL_079' column for all rows in 'foreign_data' where 'XCL_077' is 'Spanish'. It also includes a scalar subquery in 

```json
{
  "kind": "program",
  "formula": "SELECT (SELECT CAST(SUM(CASE WHEN \"XCL_077\" = 'Spanish' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) FROM foreign_data), \"XCL_079\" FROM foreign_data WHERE \"XCL_077\" = 'Spanish'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:403"
  ]
}
```

### A query that joins 'cards' and 'sets' to retrieve a presence flag for a specific set attribute. It filters the 'cards' table for the name 'Angel of Me

```json
{
  "kind": "program",
  "formula": "SELECT IIF(NOT T2.\"XCL_109\" IS NULL, 'YES', 'NO') FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Angel of Mercy'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:469"
  ]
}
```

### Query XCL_106 for SS2

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_106\" FROM sets WHERE \"XCL_099\" = 'SS2'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:490"
  ]
}
```

### Card Ruling Lookup

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_088\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T2.\"XCL_090\" = T1.\"XCL_072\" WHERE T1.\"XCL_049\" = 'Reminisce'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:485"
  ]
}
```

### A query that filters the "sets" table for rows where "XCL_115" is 'commander', sorts them by "XCL_114" in descending order, and returns the top result

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_095\" FROM sets WHERE \"XCL_115\" = 'commander' ORDER BY \"XCL_114\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:513"
  ]
}
```

### A query that retrieves distinct pairs of card identifiers ('XCL_049') and names ('XCL_070') from the 'cards' table where the faction ('XCL_074') is 'b

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_049\", T1.\"XCL_070\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_074\" = 'boros'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:444"
  ]
}
```

### Filtered Set-Translation Lookup

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_096\", T2.\"XCL_093\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_097\" IN ('Masques', 'Mirage')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:442"
  ]
}
```

### A query that retrieves specific foreign data values (XCL_079) in French for cards that meet specific criteria: Creature type, normal layout, black col

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_079\" FROM foreign_data WHERE \"XCL_082\" IN (SELECT \"XCL_072\" FROM cards WHERE \"XCL_071\" = 'Creature' AND \"XCL_037\" = 'normal' AND \"XCL_005\" = 'black' AND \"XCL_002\" = 'Matthew D. Wilson') AND \"XCL_077\" = 'French'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:412"
  ]
}
```

### Full SQL program that joins 'cards' and 'legalities' tables to retrieve distinct legality identifiers for Artifact cards in the 'vintage' format where

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_085\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_070\" = 'Artifact' AND T2.\"XCL_084\" = 'vintage' AND T1.\"XCL_064\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:345"
  ]
}
```

### A query that joins the sets table with set_translations on XCL_099 (sets) to XCL_093 (translations) to retrieve the set identifier (XCL_115) where the

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_115\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T2.\"XCL_094\" = 'Hauptset Zehnte Edition'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:471"
  ]
}
```

### Retrieves the set identifier from the 'sets' table where the set name (XCL_110) is exactly 'Commander 2014 Oversized'.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_111\" FROM sets WHERE \"XCL_110\" = 'Commander 2014 Oversized'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:493"
  ]
}
```

### A query that retrieves the first 3 card identifiers from the 'cards' table. It filters for cards associated with 'arenaleague' (where XCL_057 = 'arena

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_049\" FROM cards WHERE (\"XCL_055\" IS NULL OR \"XCL_055\" LIKE '%*%') AND \"XCL_057\" = 'arenaleague' ORDER BY \"XCL_049\" LIMIT 3",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:421"
  ]
}
```

### A SQL program that joins the cards table with the foreign_data table on XCL_072 = XCL_082 and filters for records where the foreign_data language (XCL

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_002\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T2.\"XCL_077\" = 'Chinese Simplified'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:381"
  ]
}
```

### Executes an inner join between 'cards' and 'foreign_data' to filter for cards with 'borderless' status and 'Russian' foreign data, then counts the res

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_005\" = 'borderless' AND T2.\"XCL_077\" = 'Russian'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:370"
  ]
}
```

### A SQL program that filters the "legalities" table to identify entries associated with the 'oldschool' format that have a status of 'Banned' or 'Restri

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_086\" FROM legalities WHERE \"XCL_084\" = 'oldschool' AND (\"XCL_085\" = 'Banned' OR \"XCL_085\" = 'Restricted')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:525"
  ]
}
```

### A SQL program that selects distinct values from XCL_077 in foreign_data, applying a filter on XCL_079 to match the specific value 'A Pedra Fellwar'. T

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_077\" FROM foreign_data WHERE \"XCL_079\" = 'A Pedra Fellwar'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:440"
  ]
}
```

### A query that retrieves the XCL_002 identifier from the cards table where the XCL_016 field matches the literal string 'Battra, Dark Destroyer'. Used t

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_002\" FROM cards WHERE \"XCL_016\" = 'Battra, Dark Destroyer'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:460"
  ]
}
```

### Query distinct XCL_058 where XCL_057 is bundle

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_058\" FROM cards WHERE \"XCL_057\" = 'bundle'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:457"
  ]
}
```

### A query that retrieves the distinct identifiers of all cards from the 'cards' table where the value of column XCL_005 is 'black'.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_005\" = 'black' GROUP BY \"XCL_001\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:435"
  ]
}
```

### A query that retrieves the legality status for a specific card by name. It joins the 'cards' table (T1) with the 'legalities' table (T2) on the card I

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_084\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_049\" = 'Benalish Knight'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:366"
  ]
}
```

### A query that retrieves card identifiers by joining the 'cards' and 'legalities' tables on the card reference (XCL_072 = XCL_086). It filters for cards

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_002\" = 'Erica Yang' AND T2.\"XCL_084\" = 'pauper' AND T1.\"XCL_004\" = 'paper'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:410"
  ]
}
```

### A query that retrieves distinct pairs of 'XCL_077' from 'foreign_data' and 'XCL_070' from 'cards' by joining the tables on 'XCL_082' = 'XCL_072' and f

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_077\", T1.\"XCL_070\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_074\" = 'azorius'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:449"
  ]
}
```

### Full SQL program that computes the percentage of 'cards' with 'XCL_034' = 0 within the subset where 'XCL_033' = 1. It aggregates over the entire filte

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN \"XCL_034\" = 0 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"XCL_001\") FROM cards WHERE \"XCL_033\" = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:402"
  ]
}
```

### A full SQL program that joins 'cards' and 'legalities' on the card's foreign key (XCL_072 = XCL_086). It groups by the card identifier (XCL_002), orde

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_002\", T2.\"XCL_084\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T2.\"XCL_086\" = T1.\"XCL_072\" GROUP BY T1.\"XCL_002\" ORDER BY COUNT(T1.\"XCL_001\") ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:520"
  ]
}
```

### Returns the single card name from the 'cards' table where the name is either 'Serra Angel' or 'Shrine Keeper', ordered by the 'XCL_011' column in desc

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_049\" FROM cards WHERE \"XCL_049\" IN ('Serra Angel', 'Shrine Keeper') ORDER BY \"XCL_011\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:459"
  ]
}
```

### A query that joins the 'sets' table with 'set_translations' to retrieve the translation field (XCL_092) for the specific set identified by the name 'A

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_092\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T1.\"XCL_108\" = 'Archenemy' AND T2.\"XCL_093\" = 'ARC'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:427"
  ]
}
```

### A query that retrieves the XCL_049 value from the cards table by joining it with the foreign_data table on XCL_072 = XCL_082. It filters the results t

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T2.\"XCL_077\" = 'Japanese'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:351"
  ]
}
```

### Brazilian Portuguese Set Flag Percentage Query

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN \"XCL_103\" = 1 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"XCL_095\") FROM sets WHERE \"XCL_099\" IN (SELECT \"XCL_093\" FROM set_translations WHERE \"XCL_092\" = 'Portuguese (Brazil)')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:507"
  ]
}
```

### A query that retrieves the 'XCL_002' identifier from the 'cards' table by joining with 'foreign_data' on 'XCL_072' = 'XCL_082'. It filters for records

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_002\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T2.\"XCL_077\" = 'Phyrexian'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:367"
  ]
}
```

### Card-Set Translation Join Program

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_063\" WHERE T2.\"XCL_094\" = 'Hauptset Zehnte Edition' AND T1.\"XCL_002\" = 'Adam Rex'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:466"
  ]
}
```

### A full SQL program that joins the 'cards' table with the 'foreign_data' table on 'XCL_072' = 'XCL_082'. It filters for cards where 'XCL_053' equals 'A

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_053\" = 'Artifact' AND T1.\"XCL_010\" = 'B'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:391"
  ]
}
```

### German Card ID Lookup

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_070\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_049\" = 'Ancestor''s Chosen' AND T2.\"XCL_077\" = 'German'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:482"
  ]
}
```

### Card Translation Check Program

```json
{
  "kind": "program",
  "formula": "SELECT IIF(SUM(CASE WHEN T2.\"XCL_092\" = 'Korean' AND NOT T2.\"XCL_094\" IS NULL THEN 1 ELSE 0 END) > 0, 'YES', 'NO') FROM cards AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Ancestor''s Chosen'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:465"
  ]
}
```

### Executes a join between cards and legalities on the card ID (XCL_072 = XCL_086), filters for active cards (XCL_032 = 1) and restricted status (XCL_085

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T2.\"XCL_085\" = 'Restricted' AND T1.\"XCL_032\" = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:363"
  ]
}
```

### A query that retrieves the non-null value of "XCL_057" from the "cards" table, filtered to the specific card where "XCL_049" equals 'Duress'.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_057\" FROM cards WHERE \"XCL_049\" = 'Duress' AND NOT \"XCL_057\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:357"
  ]
}
```

### A query that joins the cards and rulings tables to retrieve card identifiers and their corresponding rulings, filtered specifically to cards where the

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\", T2.\"XCL_088\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_053\" = 'Creature - Elf'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:389"
  ]
}
```

### A query that retrieves XCL_001 from the cards table where both XCL_006 and XCL_007 are not null, effectively filtering for complete card records based

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_001\" FROM cards WHERE NOT \"XCL_006\" IS NULL AND NOT \"XCL_007\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:340"
  ]
}
```

### A query that retrieves distinct translation identifiers (XCL_093) from set_translations by joining with sets on the set identifier (XCL_099) and filte

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_093\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_115\" = 'expansion' GROUP BY T2.\"XCL_093\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:443"
  ]
}
```

### Get Localized Set Name

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_094\" FROM set_translations WHERE \"XCL_093\" IN (SELECT \"XCL_099\" FROM sets WHERE \"XCL_110\" = 'Mirrodin') AND \"XCL_092\" = 'Chinese Simplified'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:505"
  ]
}
```

### Card Lookup by Name

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_041\" FROM cards WHERE \"XCL_049\" = 'Ancestor''s Chosen'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:453"
  ]
}
```

### A query that retrieves card identifiers ('XCL_049') from the 'cards' table. It joins 'foreign_data' to filter for cards with 'Italian' language ('XCL_

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_049\" FROM foreign_data AS T1 INNER JOIN cards AS T2 ON T2.\"XCL_072\" = T1.\"XCL_082\" INNER JOIN sets AS T3 ON T3.\"XCL_099\" = T2.\"XCL_063\" WHERE T3.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_077\" = 'Italian' ORDER BY T2.\"XCL_011\" DESC",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:484"
  ]
}
```

### A query that joins the sets table with the set_translations table to retrieve the translated name (XCL_092) for a specific set. It filters the sets ta

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_092\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T1.\"XCL_097\" = 'Ravnica' AND T1.\"XCL_096\" = 180",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:414"
  ]
}
```

### French Percentage Query

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_077\" = 'French' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_033\" = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:371"
  ]
}
```

### A program that joins foreign_data, cards, and sets to retrieve distinct foreign data identifiers (XCL_080) where the set name is 'Coldsnap' and the fo

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_080\" FROM foreign_data AS T1 INNER JOIN cards AS T2 ON T2.\"XCL_072\" = T1.\"XCL_082\" INNER JOIN sets AS T3 ON T3.\"XCL_099\" = T2.\"XCL_063\" WHERE T3.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_077\" = 'Italian'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:483"
  ]
}
```

### A query that joins sets and set_translations on XCL_099 = XCL_093, filters for set_translations where XCL_091 = 206, and returns the corresponding XCL

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_092\", T1.\"XCL_115\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_091\" = 206",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:429"
  ]
}
```

### A full SQL program that joins card data with set translations to find the Italian name of the set containing the card 'Ancestor's Chosen'. It uses a s

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_094\" FROM set_translations WHERE \"XCL_093\" IN (SELECT \"XCL_063\" FROM cards WHERE \"XCL_049\" = 'Ancestor''s Chosen') AND \"XCL_092\" = 'Italian'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:462"
  ]
}
```

### Full SQL program that selects the count of 'cards' where 'XCL_005' is 'white' and 'XCL_055' is either null or contains an asterisk. It serves as the e

```json
{
  "kind": "program",
  "formula": "SELECT SUM(CASE WHEN \"XCL_055\" LIKE '%*%' OR \"XCL_055\" IS NULL THEN 1 ELSE 0 END) FROM cards WHERE \"XCL_005\" = 'white'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:454"
  ]
}
```

### Count Sets by Format and Language

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_095\") FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_092\" = 'Portuguese (Brazil)' AND T1.\"XCL_097\" = 'Commander'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:405"
  ]
}
```

### Full SQL program that joins cards and foreign_data tables to retrieve XCL_077 for cards filtered by status 'Annul' and code 29. The join condition lin

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_077\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_049\" = 'Annul' AND T1.\"XCL_050\" = 29",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:350"
  ]
}
```

### Full SQL program that joins the cards table (T1) with the legalities table (T2) on T2.XCL_086 = T1.XCL_072. It filters for cards with rarity 'rare' (T

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T2.\"XCL_086\" = T1.\"XCL_072\" WHERE T1.\"XCL_059\" = 'rare' AND T1.\"XCL_071\" = 'Enchantment' AND T1.\"XCL_049\" = 'Abundance' AND T2.\"XCL_085\" = 'Legal'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:517"
  ]
}
```

### Banned Cards by Format

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_049\", T2.\"XCL_084\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T2.\"XCL_086\" = T1.\"XCL_072\" WHERE T1.\"XCL_013\" = 1 AND T2.\"XCL_085\" = 'Banned' GROUP BY T1.\"XCL_049\", T2.\"XCL_084\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:522"
  ]
}
```

### Full SQL program that joins cards and legalities tables on XCL_072 = XCL_086, filters for restricted legalities and non-flagged cards, and returns the

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T2.\"XCL_085\" = 'Restricted' AND T1.\"XCL_034\" = 0",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:361"
  ]
}
```

### Find Sets by Translation Text

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_112\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T2.\"XCL_094\" = 'Ola de frío'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:502"
  ]
}
```

### A SQL program that joins the 'sets' table (T1) with the 'set_translations' table (T2) on the key XCL_099 = XCL_093. It calculates the proportion of re

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_092\" = 'Chinese Simplified' AND T1.\"XCL_103\" = 1 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:433"
  ]
}
```

### Find Set for Card

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_115\" FROM sets WHERE \"XCL_099\" IN (SELECT \"XCL_063\" FROM cards WHERE \"XCL_049\" = 'Samite Pilgrim')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:503"
  ]
}
```

### Executes a SELECT statement on the 'cards' table to compute the count of 'XCL_001' records. It applies two filter conditions: 'XCL_013' > 12000 and 'X

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_013\" > 12000 AND \"XCL_005\" = 'borderless'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:419"
  ]
}
```

### A query that retrieves the identifier and name of sets from the 'sets' table that are joined with 'set_translations' to ensure a Japanese translation 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_110\", T1.\"XCL_095\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_092\" = 'Japanese' AND T1.\"XCL_100\" = 1 AND T1.\"XCL_101\" = 0",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:431"
  ]
}
```

### A query that retrieves card identifiers (XCL_049) from the cards table by joining with foreign_data on XCL_072 = XCL_082, filtered to cards where XCL_

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_004\" = 'paper' AND T2.\"XCL_077\" = 'Japanese'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:382"
  ]
}
```

### Executes an inner join between cards and legalities tables, filters for cards with status 'future', and returns the total count of matching card recor

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_019\" = 'future'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:386"
  ]
}
```

### A query that joins cards and set_translations to retrieve the non-null French translation (XCL_094) for the card named 'Tendo Ice Bridge' (XCL_049), m

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_094\" FROM cards AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Tendo Ice Bridge' AND T2.\"XCL_092\" = 'French' AND NOT T2.\"XCL_094\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:498"
  ]
}
```

### Italian Sets Query

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_110\", T1.\"XCL_114\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_092\" = 'Italian'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:353"
  ]
}
```

### A query that joins the 'cards' and 'rulings' tables on 'XCL_072' (cards) and 'XCL_090' (rulings). It filters for cards where 'XCL_002' is 'Kev Walker'

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_089\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T2.\"XCL_090\" = T1.\"XCL_072\" WHERE T1.\"XCL_002\" = 'Kev Walker' ORDER BY T2.\"XCL_088\" DESC",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:527"
  ]
}
```

### A query that joins the cards and legalities tables on XCL_072 = XCL_086 to retrieve XCL_010 and XCL_084 for cards where XCL_001 is between 1 and 20.

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_010\", T2.\"XCL_084\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_001\" BETWEEN 1 AND 20",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:390"
  ]
}
```

### A SQL program that joins the 'sets' table (alias T1) with the 'set_translations' table (alias T2) on the condition that T2.'XCL_093' equals T1.'XCL_09

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_095\") FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE NOT T2.\"XCL_094\" IS NULL AND T1.\"XCL_096\" < 100 AND T2.\"XCL_092\" = 'Italian'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:474"
  ]
}
```

### Query for normal status percentage

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN \"XCL_034\" = 1 AND \"XCL_037\" = 'normal' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) FROM cards",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:424"
  ]
}
```

### A query that retrieves XCL_077 from foreign_data for the specific record identified by XCL_078 = 149934.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_077\" FROM foreign_data WHERE \"XCL_078\" = 149934",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:422"
  ]
}
```

### A query that retrieves the ID of the first card (ordered by card ID) that is of 'mythic' rarity and is marked as 'Legal' in the legalities table. It j

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_051\", T2.\"XCL_084\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_059\" = 'mythic' AND NOT T1.\"XCL_051\" IS NULL AND T2.\"XCL_085\" = 'Legal' ORDER BY T1.\"XCL_051\" LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:515"
  ]
}
```

### A query that retrieves card identifiers and their associated foreign data attributes for cards that are legal in the 'legacy' format. It joins the 'ca

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_072\", T3.\"XCL_077\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" INNER JOIN foreign_data AS T3 ON T1.\"XCL_072\" = T3.\"XCL_082\" WHERE T2.\"XCL_084\" = 'legacy'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:384"
  ]
}
```

### A query that retrieves the XCL_092 value from set_translations for the specific record where XCL_091 is 174. Acts as a point lookup for a translation 

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_092\" FROM set_translations WHERE \"XCL_091\" = 174",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:438"
  ]
}
```

### A program that joins cards and rulings tables on XCL_072 = XCL_090. It filters for cards where XCL_055 is NULL or '*' and selects ruling texts (XCL_08

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_089\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE (T1.\"XCL_055\" IS NULL OR T1.\"XCL_055\" = '*') AND T2.\"XCL_089\" LIKE '%triggered ability%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:408"
  ]
}
```

### Card Lookup by Name

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_005\" FROM cards WHERE \"XCL_049\" = 'Ancestor''s Chosen'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:358"
  ]
}
```

### Full SQL program that joins sets (T1) and set_translations (T2) on T1.XCL_099 = T2.XCL_093. It filters for sets where XCL_110 is 'Tenth Edition' and e

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T2.\"XCL_094\") FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_110\" = 'Tenth Edition' AND NOT T2.\"XCL_094\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:499"
  ]
}
```

### A full program that retrieves distinct card identifiers and names for a specific player ('Allen Williams') and determines if any associated card is ba

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_019\", T1.\"XCL_049\", IIF(T2.\"XCL_085\" = 'Banned', T1.\"XCL_049\", 'NO') FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_002\" = 'Allen Williams'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:530"
  ]
}
```

### Full SQL program that calculates the percentage of sets with XCL_102=1 for sets linked to Japanese translations.

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN \"XCL_102\" = 1 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"XCL_095\") FROM sets WHERE \"XCL_099\" IN (SELECT \"XCL_093\" FROM set_translations WHERE \"XCL_092\" = 'Japanese')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:506"
  ]
}
```

### A query that retrieves distinct pairs of 'XCL_049' and 'XCL_070' from the 'cards' table. It filters for cards where 'XCL_074' is 'abzan' and ensures t

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_049\", T1.\"XCL_070\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_074\" = 'abzan'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:448"
  ]
}
```

### Query for percentage of cards with XCL_022 equal to 0 in commander legal set

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN T1.\"XCL_022\" = 0 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T2.\"XCL_084\" = 'commander' AND T2.\"XCL_085\" = 'Legal'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:415"
  ]
}
```

### Executes a SELECT statement on the 'cards' table to count records where 'XCL_028', 'XCL_030', and 'XCL_029' are all equal to 1. This program defines t

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_028\" = 1 AND \"XCL_030\" = 1 AND \"XCL_029\" = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:420"
  ]
}
```

### Full query that joins sets and set_translations to retrieve the translation field XCL_092 for the set identified by XCL_096 = 309. Returns the transla

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_092\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T1.\"XCL_096\" = 309",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:404"
  ]
}
```

### A query program that retrieves the XCL_095 value associated with the highest XCL_096 value in the sets table. It uses descending order on XCL_096 and 

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_095\" FROM sets ORDER BY \"XCL_096\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:509"
  ]
}
```

### A query that retrieves the set identifier (XCL_096) from the 'sets' table by joining with 'set_translations' on the set ID (XCL_099/XCL_093) and filte

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_096\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T2.\"XCL_094\" = 'Hauptset Zehnte Edition'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:467"
  ]
}
```

### A full SQL program that computes the percentage of borderless cards from the 'cards' table. It aggregates the entire table without grouping, returning

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN \"XCL_005\" = 'borderless' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"XCL_001\") FROM cards",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:368"
  ]
}
```

### Query returning the top 10 distinct card names (XCL_049) from the cards table that are legal in the 'duel' format, ordered by XCL_041 in descending or

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_049\" FROM cards WHERE \"XCL_072\" IN (SELECT \"XCL_086\" FROM legalities WHERE \"XCL_084\" = 'duel') ORDER BY \"XCL_041\" DESC LIMIT 10 OFFSET 0",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:514"
  ]
}
```

### Executes a SELECT DISTINCT query on the cards table, filtering rows where XCL_002 is 'Aaron Boyd' and returning the unique XCL_049 values.

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_049\" FROM cards WHERE \"XCL_002\" = 'Aaron Boyd'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:373"
  ]
}
```

### A query that joins 'cards' and 'sets' to identify the card with the maximum 'XCL_011' value within a specific set defined by 'XCL_110'.

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Journey into Nyx Hero''s Path' ORDER BY T1.\"XCL_011\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:501"
  ]
}
```

### Executes a join between 'sets' (T1) and 'set_translations' (T2) on 'XCL_099' = 'XCL_093'. Filters for translations where 'XCL_092' equals 'Japanese' a

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_095\") FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T2.\"XCL_092\" = 'Japanese' AND (T1.\"XCL_109\" IS NULL OR T1.\"XCL_109\" = '')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:434"
  ]
}
```

### A query that retrieves set identifiers (XCL_110) from the sets table by filtering for sets whose ID (XCL_099) exists in the set_translations table wit

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_110\" FROM sets WHERE \"XCL_099\" IN (SELECT \"XCL_093\" FROM set_translations WHERE \"XCL_092\" = 'Korean' AND \"XCL_092\" NOT LIKE '%Japanese%')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:529"
  ]
}
```

### German Card Attributes Query

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_065\", T1.\"XCL_066\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T2.\"XCL_077\" = 'German' AND NOT T1.\"XCL_065\" IS NULL AND NOT T1.\"XCL_066\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:407"
  ]
}
```

### A query that identifies the format with the most banned cards and returns the names of all cards banned in that specific format. It uses a CTE to find

```json
{
  "kind": "program",
  "formula": "WITH MaxBanned AS (SELECT \"XCL_084\", COUNT(*) AS count_banned FROM legalities WHERE \"XCL_085\" = 'Banned' GROUP BY \"XCL_084\" ORDER BY COUNT(*) DESC LIMIT 1) SELECT T2.\"XCL_084\", T1.\"XCL_049\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T2.\"XCL_086\" = T1.\"XCL_072\" INNER JOIN MaxBanned AS MB ON MB.\"XCL_084\" = T2.\"XCL_084\" WHERE T2.\"XCL_085\" = 'Banned'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:518"
  ]
}
```

### A query program that joins the sets table (T1) with the set_translations table (T2) on T2.XCL_093 = T1.XCL_099. It filters for sets where T1.XCL_110 i

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_094\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_110\" = 'Eighth Edition' AND T2.\"XCL_092\" = 'Chinese Simplified'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:468"
  ]
}
```

### Coldsnap card completeness metric query

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN NOT T1.\"XCL_006\" IS NULL AND NOT T1.\"XCL_007\" IS NULL THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Coldsnap'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:487"
  ]
}
```

### Filtered card count query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_019\" = 1993 AND \"XCL_004\" = 'paper' AND \"XCL_022\" = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:396"
  ]
}
```

### A query joining cards and rulings tables to retrieve ruling identifiers and a derived flag status for cards where the attribute XCL_002 equals 'Jim Pa

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_089\", CASE WHEN T1.\"XCL_022\" = 1 THEN 'YES' ELSE 'NO' END FROM cards AS T1 INNER JOIN rulings AS T2 ON T2.\"XCL_090\" = T1.\"XCL_072\" WHERE T1.\"XCL_002\" = 'Jim Pavelec'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:494"
  ]
}
```

### A query that retrieves the names of specific cards ('Chippy', 'Aaron Miller', 'Jeremy Jarvis') that belong to the 'Coldsnap' set. It joins the cards a

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_002\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE (T2.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_002\" = 'Chippy') OR (T2.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_002\" = 'Aaron Miller') OR (T2.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_002\" = 'Jeremy Jarvis') GROUP BY T1.\"XCL_002\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:477"
  ]
}
```

### A simple selection query that retrieves XCL_013 from the cards table, restricted to records where XCL_019 is 2015.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_013\" FROM cards WHERE \"XCL_019\" = 2015",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:380"
  ]
}
```

### A query that joins the cards table with the rulings table on the card identifier (XCL_072 = XCL_090) to retrieve rulings for a specific card name (XCL

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_089\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_049\" = 'Beacon of Immortality'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:385"
  ]
}
```

### Executes a SELECT statement on the 'cards' table to compute the sum of a conditional flag. The flag is 1 when 'XCL_004' equals 'paper' and 'XCL_020' e

```json
{
  "kind": "program",
  "formula": "SELECT SUM(CASE WHEN \"XCL_004\" = 'paper' AND \"XCL_020\" = '3' THEN 1 ELSE 0 END) FROM cards",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:451"
  ]
}
```

### Banned White Card Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T2.\"XCL_085\" = 'Banned' AND T1.\"XCL_005\" = 'white'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:383"
  ]
}
```

### Arena Card Attribute Pairs

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_065\", \"XCL_066\" FROM cards WHERE \"XCL_004\" = 'arena' AND NOT \"XCL_065\" IS NULL AND NOT \"XCL_066\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:399"
  ]
}
```

### Full SQL program selecting XCL_105 from sets filtered by XCL_099 = 'PKHC'. No aggregation or joins.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_105\" FROM sets WHERE \"XCL_099\" = 'PKHC'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:489"
  ]
}
```

### A query that joins the cards table with the foreign_data table on the card ID (XCL_072 = XCL_082) to retrieve distinct card identifiers (XCL_002) wher

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_002\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T2.\"XCL_076\" LIKE '%DAS perfekte Gegenmittel zu einer dichten Formation%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:411"
  ]
}
```

### Full SQL program that selects XCL_108 from the sets table filtered by the condition XCL_112 = '2017-06-09'.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_108\" FROM sets WHERE \"XCL_112\" = '2017-06-09'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:491"
  ]
}
```

### Get Set Translation for Card 5 in Language 10E

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_091\", \"XCL_092\" FROM set_translations WHERE \"XCL_091\" = (SELECT \"XCL_001\" FROM cards WHERE \"XCL_011\" = 5) AND \"XCL_093\" = '10E'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:388"
  ]
}
```

### Query: Mythic Banned Cards in Gladiator

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_001\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T2.\"XCL_084\" = 'gladiator' AND T2.\"XCL_085\" = 'Banned' AND T1.\"XCL_059\" = 'mythic'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:344"
  ]
}
```

### A program that counts the number of distinct cards (XCL_001) for the player 'Volkan Baǵa' (cards.XCL_002) that have a French foreign data entry (forei

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T3.\"XCL_001\") FROM (SELECT T1.\"XCL_001\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_002\" = 'Volkan Baǵa' AND T2.\"XCL_077\" = 'French' GROUP BY T1.\"XCL_001\") AS T3",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:516"
  ]
}
```

### Executes a filtered count on the 'cards' table. It applies two equality filters: 'XCL_004' = 'mtgo' (likely platform/game) and 'XCL_005' = 'black' (li

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_004\" = 'mtgo' AND \"XCL_005\" = 'black'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:374"
  ]
}
```

### A query that retrieves the first 3 values of XCL_110 from the sets table where XCL_109 is NULL, ordered by XCL_110.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_110\" FROM sets WHERE \"XCL_109\" IS NULL ORDER BY \"XCL_110\" LIMIT 3",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:426"
  ]
}
```

### Executes a SELECT DISTINCT query on the cards table to retrieve unique XCL_049 entries filtered by the condition XCL_034 = 0.

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_049\" FROM cards WHERE \"XCL_034\" = 0",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:452"
  ]
}
```

### Borderless Card Query

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_005\" = 'borderless' AND (\"XCL_007\" IS NULL OR \"XCL_007\" IS NULL)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:341"
  ]
}
```

### Filtered Card Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_002\" = 'Matthew D. Wilson' AND \"XCL_004\" = 'paper'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:526"
  ]
}
```

### A full SQL program that selects distinct 'XCL_002' values from the 'cards' table, filtered by 'XCL_004' = 'arena' and 'XCL_005' = 'black'.

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_002\" FROM cards WHERE \"XCL_004\" = 'arena' AND \"XCL_005\" = 'black'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:524"
  ]
}
```

### A SQL program that calculates the mode (most common value) of XCL_018 in the cards table. It filters out rows where XCL_006 or XCL_007 is null, groups

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_018\" FROM cards WHERE NOT \"XCL_006\" IS NULL AND NOT \"XCL_007\" IS NULL GROUP BY \"XCL_018\" ORDER BY COUNT(\"XCL_018\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:511"
  ]
}
```

### A query that retrieves XCL_001 from the cards table, filtering for records where XCL_005 equals 'black' and XCL_026 equals 1. This defines a specific 

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_005\" = 'black' AND \"XCL_026\" = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:437"
  ]
}
```

### A query that retrieves the top 3 values of XCL_049 from the cards table where XCL_019 equals 2003, ordered by XCL_011 in descending order.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_049\" FROM cards WHERE \"XCL_019\" = 2003 ORDER BY \"XCL_011\" DESC LIMIT 3",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:461"
  ]
}
```

### A query that retrieves the identifiers of all cards from the 'cards' table where the attribute XCL_036 is equal to 'Flying'.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_037\" FROM cards WHERE \"XCL_036\" = 'Flying'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:376"
  ]
}
```

### A full SQL program that joins 'cards' and 'set_translations' on 'XCL_063' = 'XCL_093', filters for the specific set translation 'Hauptset Zehnte Editi

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_063\" WHERE T2.\"XCL_094\" = 'Hauptset Zehnte Edition'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:464"
  ]
}
```

### A program that retrieves the XCL_001 values from the cards table where the XCL_011 column equals 0. This defines a specific subset of cards based on t

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_011\" = 0",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:375"
  ]
}
```

### Retrieves the identifier and date for the 'Shadowmoor' set by joining 'sets' with 'set_translations' to verify the Italian translation exists. Returns

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_110\", T1.\"XCL_095\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T1.\"XCL_097\" = 'Shadowmoor' AND T2.\"XCL_092\" = 'Italian' ORDER BY T1.\"XCL_095\" LIMIT 2",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:430"
  ]
}
```

### A program that joins the 'cards', 'rulings', and 'legalities' tables to retrieve identifiers for cards that are both 'Creature' type and 'Legal' statu

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" INNER JOIN legalities AS T3 ON T1.\"XCL_072\" = T3.\"XCL_086\" WHERE T3.\"XCL_085\" = 'Legal' AND T1.\"XCL_071\" = 'Creature'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:406"
  ]
}
```

### Commander Set Translation Lookup

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_093\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_115\" = 'commander'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:447"
  ]
}
```

### Card count query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_020\" = '-1' AND \"XCL_002\" = 'UDON' AND \"XCL_004\" = 'mtgo'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:395"
  ]
}
```

### A full query program that joins `sets` and `set_translations`, filters `sets` for the period between 2012-01-01 and 2015-12-31, groups by `XCL_112`, a

```json
{
  "kind": "program",
  "formula": "SELECT (CAST(SUM(T1.\"XCL_095\") AS REAL) / COUNT(T1.\"XCL_095\")) / 4, T2.\"XCL_092\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_095\" = T2.\"XCL_091\" WHERE T1.\"XCL_112\" BETWEEN '2012-01-01' AND '2015-12-31' GROUP BY T1.\"XCL_112\" ORDER BY COUNT(T2.\"XCL_092\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:523"
  ]
}
```

### French Foreign Data Percentage Query

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_077\" = 'French' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_055\" IS NULL OR T1.\"XCL_055\" = '*'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:416"
  ]
}
```

### A query that retrieves translation identifiers (XCL_093) from the set_translations table by joining with the sets table. The join condition links set_

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_093\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_112\" = '2007-07-13'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:441"
  ]
}
```

### A SQL program that counts cards in the 'cards' table filtered by a specific set ('World Championship Decks 2004') and an attribute value (XCL_011 = 3)

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_063\" IN (SELECT \"XCL_099\" FROM sets WHERE \"XCL_110\" = 'World Championship Decks 2004') AND \"XCL_011\" = 3",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:504"
  ]
}
```

### Executes a SELECT statement against the 'cards' table to compute the count of cards matching specific platform and color criteria defined by columns '

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(CASE WHEN \"XCL_004\" LIKE '%arena,mtgo%' AND \"XCL_005\" = 'black' THEN 1 ELSE NULL END) FROM cards",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:458"
  ]
}
```

### Full SQL program that counts cards (T1) filtered by XCL_030 = 1, joined to foreign_data (T2) on XCL_072 = XCL_082, and filtered by XCL_077 = 'German'.

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T2.\"XCL_077\" = 'German' AND T1.\"XCL_030\" = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:369"
  ]
}
```

### Full SQL program selecting the count of 'XCL_001' from 'cards' filtered by 'XCL_002' = 'John Avon' and the condition that 'XCL_007' IS NULL OR 'XCL_00

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_001\") FROM cards WHERE (\"XCL_007\" IS NULL OR \"XCL_006\" IS NULL) AND \"XCL_002\" = 'John Avon'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:393"
  ]
}
```

### A query that retrieves the top 3 distinct card identifiers (XCL_049) from the cards table where the rarity (XCL_059) is 'uncommon', joined with the ru

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_059\" = 'uncommon' ORDER BY T2.\"XCL_088\" ASC LIMIT 3",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:392"
  ]
}
```

### A full SQL program that retrieves the Japanese translation for the card set 'Fellwar Stone'. It joins the 'cards' table with 'set_translations' on the

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_094\" FROM cards AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Fellwar Stone' AND T2.\"XCL_092\" = 'Japanese' AND NOT T2.\"XCL_094\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:500"
  ]
}
```

### Executes a SELECT statement on the 'cards' table to count entries where 'XCL_053' is 'Summon - Angel' and 'XCL_065' is not 'Angel'. This program serve

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_053\" = 'Summon - Angel' AND \"XCL_065\" <> 'Angel'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:377"
  ]
}
```

### Full query program that retrieves set identifiers (XCL_115) from the sets table where the set's translation reference (XCL_099) exists in the set_tran

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_115\" FROM sets WHERE \"XCL_099\" IN (SELECT \"XCL_093\" FROM set_translations WHERE \"XCL_094\" = 'Huitième édition')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:497"
  ]
}
```

### Computes the distinct pairs of set identifiers and translation identifiers where the translation language code is 5. Joins 'sets' and 'set_translation

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_110\", T2.\"XCL_094\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_091\" = 5 GROUP BY T1.\"XCL_110\", T2.\"XCL_094\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:428"
  ]
}
```

### A query that retrieves the translation (XCL_092) for the 'Battlebond' set by joining set_translations to sets via the set ID (XCL_095/XCL_091) and fil

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_092\" FROM set_translations WHERE \"XCL_091\" IN (SELECT \"XCL_095\" FROM sets WHERE \"XCL_110\" = 'Battlebond')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:519"
  ]
}
```

### A query that retrieves card identifiers, ruling texts, and card attributes for cards designed by 'Stephen Daniele'. It joins the 'cards' and 'rulings'

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\", T2.\"XCL_089\", T1.\"XCL_022\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_002\" = 'Stephen Daniele'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:347"
  ]
}
```

### A query that selects the XCL_001 column from the cards table, restricted to records where the XCL_012 column has the value 'a'. The grain is individua

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_012\" = 'a'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:379"
  ]
}
```

### Full SQL program that joins the 'cards' table (T1) with the 'sets' table (T2) on the condition T2."XCL_099" = T1."XCL_063". It filters for the set whe

```json
{
  "kind": "program",
  "formula": "SELECT SUM(CASE WHEN T1.\"XCL_005\" = 'black' THEN 1 ELSE 0 END) FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Coldsnap'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:475"
  ]
}
```

### Executes a SELECT statement against the 'cards' table to compute the sum of a conditional flag. The flag is 1 if 'XCL_002' equals 'Aaron Miller' and '

```json
{
  "kind": "program",
  "formula": "SELECT SUM(CASE WHEN \"XCL_002\" = 'Aaron Miller' AND NOT \"XCL_006\" IS NULL AND NOT \"XCL_007\" IS NULL THEN 1 ELSE 0 END) FROM cards",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:450"
  ]
}
```

### Latest Null-Field Card Query

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_002\" FROM cards WHERE \"XCL_064\" IS NULL ORDER BY \"XCL_011\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:510"
  ]
}
```

### Count Cards by XCL_002

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_070\") FROM cards WHERE \"XCL_002\" = 'Aaron Boyd'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:354"
  ]
}
```

### Adarkar Valkyrie set membership check

```json
{
  "kind": "program",
  "formula": "SELECT IIF(\"XCL_101\" = 1, 'YES', 'NO') FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Adarkar Valkyrie'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:473"
  ]
}
```

### Executes a count query on the 'cards' table, filtering for records where the 'XCL_055' field is exactly '*'. This program returns a single integer val

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(*) FROM cards WHERE \"XCL_055\" = '*'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:356"
  ]
}
```

### A query that retrieves unique card identifiers for 'Benalish Knight' by joining the cards table with foreign_data on the card's foreign key (XCL_072) 

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_070\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_049\" = 'Benalish Knight'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:365"
  ]
}
```

### Full SQL program that counts cards filtered by 'XCL_005' = 'white' and non-null values in 'XCL_006' and 'XCL_007'.

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_005\" = 'white' AND NOT \"XCL_007\" IS NULL AND NOT \"XCL_006\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:394"
  ]
}
```

### A query that retrieves the card ID (XCL_001) and attribute XCL_010 from the cards table. It filters results to include only cards whose ID matches an 

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_001\", \"XCL_010\" FROM cards WHERE \"XCL_001\" IN (SELECT \"XCL_091\" FROM set_translations WHERE \"XCL_093\" = 'OGW')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:387"
  ]
}
```

### Count cards with XCL_069=99

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_069\" = 99",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:372"
  ]
}
```

### A query returning the XCL_001 values from the cards table where XCL_013 is less than 100 and XCL_019 equals 2015. The grain is individual card records

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_013\" < 100 AND \"XCL_019\" = 2015",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:343"
  ]
}
```

### Full SQL program that joins cards and rulings tables on XCL_072 = XCL_090, filters for rare cards and rulings from 2007-02-01, and returns the distinc

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T1.\"XCL_001\") FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_059\" = 'rare' AND T2.\"XCL_088\" = '2007-02-01'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:413"
  ]
}
```

### Query XCL_004 for Daren Bader

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_004\" FROM cards WHERE \"XCL_002\" = 'Daren Bader'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:418"
  ]
}
```

### Retrieves set identifiers by joining the 'sets' table with 'set_translations' on the set ID (XCL_099/XCL_093) and filtering for the specific translati

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_096\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T2.\"XCL_094\" = 'Rinascita di Alara'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:496"
  ]
}
```

### A program that retrieves a single card (XCL_049, XCL_002, XCL_029) from the cards table. It joins with the rulings table to ensure the card has associ

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_049\", T1.\"XCL_002\", T1.\"XCL_029\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_029\" = 1 AND T1.\"XCL_002\" = (SELECT \"XCL_002\" FROM cards WHERE \"XCL_029\" = 1 GROUP BY \"XCL_002\" HAVING COUNT(DISTINCT \"XCL_072\") = (SELECT MAX(\"count_uuid\") FROM (SELECT COUNT(DISTINCT \"XCL_072\") AS count_uuid FROM cards WHERE \"XCL_029\" = 1 GROUP BY \"XCL_002\"))) LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:349"
  ]
}
```

### A query that retrieves the identifiers of all cards from the 'cards' table where the type or classification (XCL_065) is exactly 'Angel,Wizard' and th

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_065\" = 'Angel,Wizard' AND \"XCL_064\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:425"
  ]
}
```

### A query that retrieves the value of XCL_093 from the set_translations table specifically for the Spanish language, identified by the filter XCL_092 = 

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_093\" FROM set_translations WHERE \"XCL_092\" = 'Spanish'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:400"
  ]
}
```

### Card Ruling Lookup

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_089\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_049\" = 'Condemn'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:362"
  ]
}
```

### Full SQL program that joins the 'cards' table (T1) with the 'sets' table (T2) on T2.XCL_099 = T1.XCL_063. It filters for the set named 'Coldsnap' (T2.

```json
{
  "kind": "program",
  "formula": "SELECT SUM(CASE WHEN T1.\"XCL_055\" LIKE '*' OR T1.\"XCL_055\" IS NULL THEN 1 ELSE 0 END) FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_011\" > 5",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:479"
  ]
}
```

### Molimo Maro-Sorcerer Attribute Lookup

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_065\", \"XCL_066\" FROM cards WHERE \"XCL_049\" = 'Molimo, Maro-Sorcerer'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:456"
  ]
}
```

### Colorpie Foreign Data Attributes Query

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_077\", T2.\"XCL_076\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_074\" = 'colorpie'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:445"
  ]
}
```

### Retrieves the first 3 rows from the cards table where both XCL_006 and XCL_007 are non-null, ordered by XCL_006. Returns a sample of card records with

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_006\", \"XCL_007\" FROM cards WHERE NOT \"XCL_006\" IS NULL AND NOT \"XCL_007\" IS NULL ORDER BY \"XCL_006\" LIMIT 3",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:423"
  ]
}
```

### A SQL program that selects from the 'cards' table. It applies two binding filters: 'XCL_023' must equal 0 and 'XCL_012' must equal 'a'. It then comput

```json
{
  "kind": "program",
  "formula": "SELECT SUM(CASE WHEN \"XCL_055\" = '*' OR \"XCL_055\" IS NULL THEN 1 ELSE 0 END) FROM cards WHERE \"XCL_023\" = 0 AND \"XCL_012\" = 'a'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:512"
  ]
}
```

### Query XCL_110 for ALL

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_110\" FROM sets WHERE \"XCL_099\" = 'ALL'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:439"
  ]
}
```

### A SQL program that joins the cards table with the foreign_data table on XCL_072/XCL_082 to retrieve XCL_077 for the specific card 'Ancestor's Chosen' 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_077\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_049\" = 'Ancestor''s Chosen' AND NOT T2.\"XCL_076\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:481"
  ]
}
```

### Query XCL_099 by XCL_112 date

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_099\" FROM sets WHERE \"XCL_112\" = '2017-07-14' GROUP BY \"XCL_112\", \"XCL_099\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:488"
  ]
}
```

### A SQL program that selects XCL_115 from the 'sets' table where XCL_110 matches the pattern '%FROM the Vault: Lore%'.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_115\" FROM sets WHERE \"XCL_110\" LIKE '%FROM the Vault: Lore%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:492"
  ]
}
```

### A query that retrieves the XCL_049 value from the cards table, ordered by XCL_014 in ascending order, limited to the first result.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_049\" FROM cards ORDER BY \"XCL_014\" LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:342"
  ]
}
```

### A SQL program that joins the cards table with the foreign_data table on XCL_082 = XCL_072. It filters for the specific card 'Ancestor's Chosen' and th

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_076\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_049\" = 'Ancestor''s Chosen' AND T2.\"XCL_077\" = 'Italian'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:480"
  ]
}
```

### Full SQL program that computes the percentage of 'legendary' cards (where 'XCL_018' = 'legendary') that have 'XCL_027' = 1. It aggregates over the 'ca

```json
{
  "kind": "program",
  "formula": "SELECT SUM(CASE WHEN \"XCL_027\" = 1 THEN 1.0 ELSE 0 END) / COUNT(\"XCL_001\") * 100 FROM cards WHERE \"XCL_018\" = 'legendary'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:401"
  ]
}
```

### Full SQL program that joins cards and sets, filters for XCL_049 = 'Abyssal Horror', and computes the percentage of cards where XCL_011 is 10.

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN T1.\"XCL_011\" = 10 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\"), T1.\"XCL_049\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Abyssal Horror'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:446"
  ]
}
```

### Card Ruling Lookup

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_089\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_049\" = 'Sublime Epiphany' AND T1.\"XCL_050\" = '74s'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:348"
  ]
}
```

### Card to Foreign Data Join for Language Percentage

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_077\" = 'Chinese Simplified' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:352"
  ]
}
```

### Executes a SELECT DISTINCT query on the 'cards' table to retrieve unique 'XCL_049' entries, applying conditions that 'XCL_029' must be 1 and 'XCL_064'

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_049\" FROM cards WHERE \"XCL_029\" = 1 AND NOT \"XCL_064\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:455"
  ]
}
```

### Card-to-Set Lookup

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_112\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Ancestor''s Chosen'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:470"
  ]
}
```

### A query that retrieves the XCL_041 value from the cards table for the record where XCL_002 is 'Rob Alexander'. Acts as a point lookup for a specific c

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_041\" FROM cards WHERE \"XCL_002\" = 'Rob Alexander'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:398"
  ]
}
```

### A query that joins 'cards' and 'sets' on 'XCL_063' = 'XCL_099', filters for the 'Coldsnap' set, orders by 'XCL_011' descending, and returns the top 'X

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Coldsnap' ORDER BY T1.\"XCL_011\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:476"
  ]
}
```

### A query that joins the 'cards' and 'legalities' tables on the card identifier ('XCL_072' = 'XCL_086') to retrieve the distinct legality identifiers ('

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_085\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_049\" = 'Cloudchaser Eagle'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:364"
  ]
}
```

### Full SQL program that joins sets and set_translations on set ID, filters for expansion sets, and computes the ratio of Japanese translations to total 

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_092\" = 'Japanese' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_095\") FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T1.\"XCL_115\" = 'expansion'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:417"
  ]
}
```

### Full SQL program that joins sets and set_translations to count distinct sets with available Italian translations for a specific set name.

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T1.\"XCL_095\") FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_097\" = 'Ice Age' AND T2.\"XCL_092\" = 'Italian' AND NOT T2.\"XCL_094\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:472"
  ]
}
```

### A SQL program that retrieves the 'XCL_049' value for cards. It joins the 'cards' table with the 'sets' table on 'XCL_063' (card) to 'XCL_099' (set), f

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_050\" = 4",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:478"
  ]
}
```

### Full SQL program that joins cards and sets, filters for the 'Coldsnap' set, and computes the percentage of cards with XCL_011 = 7.

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN T1.\"XCL_011\" = 7 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Coldsnap'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:486"
  ]
}
```

### A SQL program that joins the 'cards' table (T1) with the 'sets' table (T2) on 'XCL_099' = 'XCL_063'. It filters for cards where 'XCL_049' is 'Evacuati

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_112\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Evacuation'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:495"
  ]
}
```

### A program that retrieves the identifier and name of cards legal in the Commander format. It joins the 'cards' table with the 'legalities' table on the

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_001\", T1.\"XCL_002\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T2.\"XCL_085\" = 'Legal' AND T2.\"XCL_084\" = 'commander' AND (T1.\"XCL_055\" IS NULL OR T1.\"XCL_055\" = '*')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:346"
  ]
}
```

### A query that joins 'sets' and 'set_translations' to find the 'XCL_095' identifier for the set with the maximum 'XCL_096' value that has a Russian tran

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_095\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_092\" = 'Russian' GROUP BY T1.\"XCL_096\" ORDER BY T1.\"XCL_096\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:432"
  ]
}
```

### Query XCL_053 for Ancestor's Chosen

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_053\" FROM cards WHERE \"XCL_049\" = 'Ancestor''s Chosen' AND NOT \"XCL_053\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:359"
  ]
}
```

### Executes a SELECT DISTINCT query on the cards table to retrieve unique XCL_004 entries matching specific conditions on XCL_002 and XCL_034.

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_004\" FROM cards WHERE \"XCL_002\" = 'Aleksi Briclot' AND \"XCL_034\" = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:508"
  ]
}
```

### A query that retrieves the distinct list of card identifiers from the 'cards' table where the 'XCL_018' field equals 'extendedart'.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_018\" = 'extendedart' GROUP BY \"XCL_001\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:436"
  ]
}
```

### A query that retrieves card identifiers from the 'cards' table where the card is available in 'mtgo,paper', has 'black' color, was released in 2003, a

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_041\" FROM cards WHERE \"XCL_004\" = 'mtgo,paper' AND \"XCL_005\" = 'black' AND \"XCL_019\" = 2003 AND \"XCL_037\" = 'normal'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:397"
  ]
}
```

### Full SQL program joining cards, legalities, and rulings. It counts cards (T1) where the legality format (T2.XCL_084) is 'premodern', the ruling text (

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" INNER JOIN rulings AS T3 ON T1.\"XCL_072\" = T3.\"XCL_090\" WHERE T2.\"XCL_084\" = 'premodern' AND T3.\"XCL_089\" = 'This is a triggered mana ability.' AND T1.\"XCL_064\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:409"
  ]
}
```

### Complete Card Records Query

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_001\" FROM cards WHERE NOT \"XCL_007\" IS NULL AND NOT \"XCL_006\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:378"
  ]
}
```

### Attribute (XCL_115) from the sets table representing the set that contains the card 'Samite Pilgrim'. This is the final output of the query.

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_115\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_115\" FROM sets WHERE \"XCL_099\" IN (SELECT \"XCL_063\" FROM cards WHERE \"XCL_049\" = 'Samite Pilgrim')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:503"
  ]
}
```

### NOT "cards"."XCL_006" IS NULL AND NOT "cards"."XCL_007" IS NULL

```json
{
  "kind": "predicate",
  "formula": "NOT \"cards\".\"XCL_006\" IS NULL AND NOT \"cards\".\"XCL_007\" IS NULL",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE NOT \"XCL_006\" IS NULL AND NOT \"XCL_007\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:340"
  ]
}
```

### "foreign_data"."XCL_077" = 'German' AND "cards"."XCL_030" = 1

```json
{
  "kind": "predicate",
  "formula": "\"foreign_data\".\"XCL_077\" = 'German' AND \"cards\".\"XCL_030\" = 1",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T2.\"XCL_077\" = 'German' AND T1.\"XCL_030\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:369"
  ]
}
```

### Set Translation Key

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_091\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_091\", \"XCL_092\" FROM set_translations WHERE \"XCL_091\" = (SELECT \"XCL_001\" FROM cards WHERE \"XCL_011\" = 5) AND \"XCL_093\" = '10E'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:388"
  ]
}
```

### Aggregates the total number of rows in the 'cards' table where the platform identifier 'XCL_004' is 'mtgo' and the color identifier 'XCL_005' is 'blac

```json
{
  "kind": "metric",
  "formula": "COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_004\" = 'mtgo' AND \"XCL_005\" = 'black'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_004\" = 'mtgo' AND \"r0\".\"XCL_005\" = 'black'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:374"
  ]
}
```

### Distinct values of the 'XCL_076' column from the 'foreign_data' table, restricted to records linked to cards where 'XCL_074' is 'colorpie'.

```json
{
  "kind": "binding",
  "formula": "\"foreign_data\".\"XCL_076\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_077\", T2.\"XCL_076\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_074\" = 'colorpie'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:445"
  ]
}
```

### "cards"."XCL_012" = 'a'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_012\" = 'a'",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_012\" = 'a'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:379"
  ]
}
```

### Battlebond Set ID

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_095\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_095\" FROM sets WHERE \"XCL_110\" = 'Battlebond'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_095\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_095\" AS \"value\" FROM sets AS \"r0\" WHERE \"r0\".\"XCL_110\" = 'Battlebond'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:519"
  ]
}
```

### "set_translations"."XCL_092" = 'Spanish'

```json
{
  "kind": "predicate",
  "formula": "\"set_translations\".\"XCL_092\" = 'Spanish'",
  "grain": [],
  "population_scope": "SELECT \"XCL_093\" FROM set_translations WHERE \"XCL_092\" = 'Spanish'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:400"
  ]
}
```

### "set_translations"."XCL_092" = 'Japanese' AND ("sets"."XCL_109" IS NULL OR "sets"."XCL_109" = '')

```json
{
  "kind": "predicate",
  "formula": "\"set_translations\".\"XCL_092\" = 'Japanese' AND (\"sets\".\"XCL_109\" IS NULL OR \"sets\".\"XCL_109\" = '')",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_095\") FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T2.\"XCL_092\" = 'Japanese' AND (T1.\"XCL_109\" IS NULL OR T1.\"XCL_109\" = '')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:434"
  ]
}
```

### NOT "set_translations"."XCL_094" IS NULL AND "sets"."XCL_096" < 100 AND "set_translations"."XCL_092" = 'Italian'

```json
{
  "kind": "predicate",
  "formula": "NOT \"set_translations\".\"XCL_094\" IS NULL AND \"sets\".\"XCL_096\" < 100 AND \"set_translations\".\"XCL_092\" = 'Italian'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_095\") FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE NOT T2.\"XCL_094\" IS NULL AND T1.\"XCL_096\" < 100 AND T2.\"XCL_092\" = 'Italian'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:474"
  ]
}
```

### The value of column XCL_002 from the cards table for the single record where XCL_064 is NULL, selected by the highest value of XCL_011.

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_002\" FROM cards WHERE \"XCL_064\" IS NULL ORDER BY \"XCL_011\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:510"
  ]
}
```

### "cards"."XCL_057" = 'bundle'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_057\" = 'bundle'",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_058\" FROM cards WHERE \"XCL_057\" = 'bundle'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:457"
  ]
}
```

### Set Identifier

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_115\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_115\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T2.\"XCL_094\" = 'Hauptset Zehnte Edition'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_115\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_115\" AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r1\".\"XCL_093\" = \"r0\".\"XCL_099\" WHERE \"r1\".\"XCL_094\" = 'Hauptset Zehnte Edition'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:471"
  ]
}
```

### "cards"."XCL_023" = 0 AND "cards"."XCL_012" = 'a'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_023\" = 0 AND \"cards\".\"XCL_012\" = 'a'",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN \"XCL_055\" = '*' OR \"XCL_055\" IS NULL THEN 1 ELSE 0 END) FROM cards WHERE \"XCL_023\" = 0 AND \"XCL_012\" = 'a'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:512"
  ]
}
```

### Set Translation Card ID

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_091\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_091\" FROM set_translations WHERE \"XCL_093\" = 'OGW'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_091\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_091\" AS \"value\" FROM set_translations AS \"r0\" WHERE \"r0\".\"XCL_093\" = 'OGW'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:387"
  ]
}
```

### "cards"."XCL_070" = 'Artifact' AND "legalities"."XCL_084" = 'vintage' AND "cards"."XCL_064" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_070\" = 'Artifact' AND \"legalities\".\"XCL_084\" = 'vintage' AND \"cards\".\"XCL_064\" IS NULL",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_085\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_070\" = 'Artifact' AND T2.\"XCL_084\" = 'vintage' AND T1.\"XCL_064\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:345"
  ]
}
```

### Returns the value of column XCL_108 from the sets table for rows where XCL_112 equals '2017-06-09'. The grain is individual matching rows.

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_108\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_108\" FROM sets WHERE \"XCL_112\" = '2017-06-09'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_108\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_108\" AS \"value\" FROM sets AS \"r0\" WHERE \"r0\".\"XCL_112\" = '2017-06-09'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:491"
  ]
}
```

### Distinct values of the card identifier (XCL_001) for cards that are classified as 'mythic' rarity and have a 'Banned' legality status in the 'gladiato

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_001\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T2.\"XCL_084\" = 'gladiator' AND T2.\"XCL_085\" = 'Banned' AND T1.\"XCL_059\" = 'mythic'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:344"
  ]
}
```

### "cards"."XCL_049" = 'Benalish Knight'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Benalish Knight'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_070\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_049\" = 'Benalish Knight'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:365"
  ]
}
```

### "legalities"."XCL_084" = 'premodern' AND "rulings"."XCL_089" = 'This is a triggered mana ability.' AND "cards"."XCL_064" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"legalities\".\"XCL_084\" = 'premodern' AND \"rulings\".\"XCL_089\" = 'This is a triggered mana ability.' AND \"cards\".\"XCL_064\" IS NULL",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" INNER JOIN rulings AS T3 ON T1.\"XCL_072\" = T3.\"XCL_090\" WHERE T2.\"XCL_084\" = 'premodern' AND T3.\"XCL_089\" = 'This is a triggered mana ability.' AND T1.\"XCL_064\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:409"
  ]
}
```

### Aggregated count of card records where the field XCL_055 is either null or contains the wildcard character '*'. The population is restricted to cards 

```json
{
  "kind": "metric",
  "formula": "SUM(CASE WHEN \"cards\".\"XCL_055\" LIKE '*' OR \"cards\".\"XCL_055\" IS NULL THEN 1 ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN T1.\"XCL_055\" LIKE '*' OR T1.\"XCL_055\" IS NULL THEN 1 ELSE 0 END) FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_011\" > 5",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(CASE WHEN \"r0\".\"XCL_055\" LIKE '*' OR \"r0\".\"XCL_055\" IS NULL THEN 1 ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT SUM(CASE WHEN \"r0\".\"XCL_055\" LIKE '*' OR \"r0\".\"XCL_055\" IS NULL THEN 1 ELSE 0 END) AS \"value\" FROM cards AS \"r0\" INNER JOIN sets AS \"r1\" ON \"r1\".\"XCL_099\" = \"r0\".\"XCL_063\" WHERE \"r1\".\"XCL_110\" = 'Coldsnap' AND \"r0\".\"XCL_011\" > 5",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:479"
  ]
}
```

### Card Attribute XCL_065

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_065\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_065\", T1.\"XCL_066\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T2.\"XCL_077\" = 'German' AND NOT T1.\"XCL_065\" IS NULL AND NOT T1.\"XCL_066\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_065\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "foreign_data"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_065\" AS \"value\" FROM cards AS \"r0\" INNER JOIN foreign_data AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_082\" WHERE \"r1\".\"XCL_077\" = 'German' AND NOT \"r0\".\"XCL_065\" IS NULL AND NOT \"r0\".\"XCL_066\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:407"
  ]
}
```

### "sets"."XCL_099" = 'PKHC'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_099\" = 'PKHC'",
  "grain": [],
  "population_scope": "SELECT \"XCL_105\" FROM sets WHERE \"XCL_099\" = 'PKHC'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:489"
  ]
}
```

### The value of column XCL_115 from the sets table, representing a specific attribute of the set entity.

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_115\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_092\", T1.\"XCL_115\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_091\" = 206",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_115\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_115\" AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r0\".\"XCL_099\" = \"r1\".\"XCL_093\" WHERE \"r1\".\"XCL_091\" = 206",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:429"
  ]
}
```

### A binary indicator ('YES' or 'NO') derived from the 'sets' table. It evaluates whether the column 'XCL_109' is non-null for the set associated with th

```json
{
  "kind": "binding",
  "formula": "IIF(NOT \"sets\".\"XCL_109\" IS NULL, 'YES', 'NO')",
  "grain": [],
  "population_scope": "SELECT IIF(NOT T2.\"XCL_109\" IS NULL, 'YES', 'NO') FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Angel of Mercy'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "IIF(NOT \"r1\".\"XCL_109\" IS NULL, 'YES', 'NO')",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT IIF(NOT \"r1\".\"XCL_109\" IS NULL, 'YES', 'NO') AS \"value\" FROM cards AS \"r0\" INNER JOIN sets AS \"r1\" ON \"r1\".\"XCL_099\" = \"r0\".\"XCL_063\" WHERE \"r0\".\"XCL_049\" = 'Angel of Mercy'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:469"
  ]
}
```

### "cards"."XCL_055" = '*'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_055\" = '*'",
  "grain": [],
  "population_scope": "SELECT COUNT(*) FROM cards WHERE \"XCL_055\" = '*'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:356"
  ]
}
```

### "sets"."XCL_110" = 'Coldsnap'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_110\" = 'Coldsnap'",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN T1.\"XCL_005\" = 'black' THEN 1 ELSE 0 END) FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Coldsnap'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:475"
  ]
}
```

### "sets"."XCL_099" = 'ALL'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_099\" = 'ALL'",
  "grain": [],
  "population_scope": "SELECT \"XCL_110\" FROM sets WHERE \"XCL_099\" = 'ALL'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:439"
  ]
}
```

### "cards"."XCL_004" = 'arena' AND "cards"."XCL_005" = 'black'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_004\" = 'arena' AND \"cards\".\"XCL_005\" = 'black'",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_002\" FROM cards WHERE \"XCL_004\" = 'arena' AND \"XCL_005\" = 'black'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:524"
  ]
}
```

### "set_translations"."XCL_094" = 'Rinascita di Alara'

```json
{
  "kind": "predicate",
  "formula": "\"set_translations\".\"XCL_094\" = 'Rinascita di Alara'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_096\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T2.\"XCL_094\" = 'Rinascita di Alara'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:496"
  ]
}
```

### Ruling Text

```json
{
  "kind": "binding",
  "formula": "\"rulings\".\"XCL_088\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T2.\"XCL_088\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_053\" = 'Creature - Elf'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_088\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "rulings"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_088\" AS \"value\" FROM cards AS \"r0\" INNER JOIN rulings AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_090\" WHERE \"r0\".\"XCL_053\" = 'Creature - Elf'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:389"
  ]
}
```

### "set_translations"."XCL_092" = 'Portuguese (Brazil)' AND "sets"."XCL_097" = 'Commander'

```json
{
  "kind": "predicate",
  "formula": "\"set_translations\".\"XCL_092\" = 'Portuguese (Brazil)' AND \"sets\".\"XCL_097\" = 'Commander'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_095\") FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_092\" = 'Portuguese (Brazil)' AND T1.\"XCL_097\" = 'Commander'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:405"
  ]
}
```

### Returns the value of the 'XCL_112' column from the 'sets' table for records linked to cards where the 'XCL_049' column equals 'Evacuation'. The grain 

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_112\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_112\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Evacuation'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_112\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_112\" AS \"value\" FROM cards AS \"r0\" INNER JOIN sets AS \"r1\" ON \"r1\".\"XCL_099\" = \"r0\".\"XCL_063\" WHERE \"r0\".\"XCL_049\" = 'Evacuation'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:495"
  ]
}
```

### "cards"."XCL_049" = 'Angel of Mercy'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Angel of Mercy'",
  "grain": [],
  "population_scope": "SELECT \"XCL_063\" FROM cards WHERE \"XCL_049\" = 'Angel of Mercy'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:463"
  ]
}
```

### Percentage of Spanish records in foreign_data

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"foreign_data\".\"XCL_077\" = 'Spanish' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*)",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN \"XCL_077\" = 'Spanish' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) FROM foreign_data",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r0\".\"XCL_077\" = 'Spanish' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "foreign_data"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r0\".\"XCL_077\" = 'Spanish' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) AS \"value\" FROM foreign_data AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:403"
  ]
}
```

### Ruling Text

```json
{
  "kind": "binding",
  "formula": "\"rulings\".\"XCL_089\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_089\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE (T1.\"XCL_055\" IS NULL OR T1.\"XCL_055\" = '*') AND T2.\"XCL_089\" LIKE '%triggered ability%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_089\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "rulings"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_089\" AS \"value\" FROM cards AS \"r0\" INNER JOIN rulings AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_090\" WHERE (\"r0\".\"XCL_055\" IS NULL OR \"r0\".\"XCL_055\" = '*') AND \"r1\".\"XCL_089\" LIKE '%triggered ability%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:408"
  ]
}
```

### Distinct XCL_049 values for Aaron Boyd

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_049\" FROM cards WHERE \"XCL_002\" = 'Aaron Boyd'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:373"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_049\" = 'Angel of Mercy'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_049\" = 'Angel of Mercy'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:360"
  ]
}
```

### Calculates the percentage of rows in the 'cards' table where 'XCL_027' equals 1, restricted to rows where 'XCL_018' is 'legendary'. The numerator coun

```json
{
  "kind": "metric",
  "formula": "SUM(CASE WHEN \"cards\".\"XCL_027\" = 1 THEN 1.0 ELSE 0 END) / COUNT(\"cards\".\"XCL_001\") * 100",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN \"XCL_027\" = 1 THEN 1.0 ELSE 0 END) / COUNT(\"XCL_001\") * 100 FROM cards WHERE \"XCL_018\" = 'legendary'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(CASE WHEN \"r0\".\"XCL_027\" = 1 THEN 1.0 ELSE 0 END) / COUNT(\"r0\".\"XCL_001\") * 100",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT SUM(CASE WHEN \"r0\".\"XCL_027\" = 1 THEN 1.0 ELSE 0 END) / COUNT(\"r0\".\"XCL_001\") * 100 AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_018\" = 'legendary'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:401"
  ]
}
```

### Calculates the percentage of cards in the 'Coldsnap' set that have non-null values in both XCL_006 and XCL_007. The numerator counts cards where both 

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN NOT \"cards\".\"XCL_006\" IS NULL AND NOT \"cards\".\"XCL_007\" IS NULL THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN NOT T1.\"XCL_006\" IS NULL AND NOT T1.\"XCL_007\" IS NULL THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Coldsnap'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN NOT \"r0\".\"XCL_006\" IS NULL AND NOT \"r0\".\"XCL_007\" IS NULL THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN NOT \"r0\".\"XCL_006\" IS NULL AND NOT \"r0\".\"XCL_007\" IS NULL THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" INNER JOIN sets AS \"r1\" ON \"r1\".\"XCL_099\" = \"r0\".\"XCL_063\" WHERE \"r1\".\"XCL_110\" = 'Coldsnap'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:487"
  ]
}
```

### Format Identifier (Result)

```json
{
  "kind": "binding",
  "formula": "T2.\"XCL_084\"",
  "grain": [],
  "population_scope": "WITH MaxBanned AS (SELECT \"XCL_084\", COUNT(*) AS count_banned FROM legalities WHERE \"XCL_085\" = 'Banned' GROUP BY \"XCL_084\" ORDER BY COUNT(*) DESC LIMIT 1) SELECT T2.\"XCL_084\", T1.\"XCL_049\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T2.\"XCL_086\" = T1.\"XCL_072\" INNER JOIN MaxBanned AS MB ON MB.\"XCL_084\" = T2.\"XCL_084\" WHERE T2.\"XCL_085\" = 'Banned'",
  "upstream_scopes": [
    "SELECT \"XCL_084\", COUNT(*) AS count_banned FROM legalities WHERE \"XCL_085\" = 'Banned' GROUP BY \"XCL_084\" ORDER BY COUNT(*) DESC LIMIT 1"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:518"
  ]
}
```

### Japanese Set ID

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_093\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_093\" FROM set_translations WHERE \"XCL_092\" = 'Japanese'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_093\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_093\" AS \"value\" FROM set_translations AS \"r0\" WHERE \"r0\".\"XCL_092\" = 'Japanese'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:506"
  ]
}
```

### The single most frequent value of column XCL_018 from the cards table, restricted to rows where both XCL_006 and XCL_007 are not null. Returns one row

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_018\"",
  "grain": [
    "\"cards\".\"XCL_018\""
  ],
  "population_scope": "SELECT \"XCL_018\" FROM cards WHERE NOT \"XCL_006\" IS NULL AND NOT \"XCL_007\" IS NULL GROUP BY \"XCL_018\" ORDER BY COUNT(\"XCL_018\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:511"
  ]
}
```

### "cards"."XCL_049" = 'Angel of Mercy'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Angel of Mercy'",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_036\" FROM cards WHERE \"XCL_049\" = 'Angel of Mercy'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:355"
  ]
}
```

### Distinct Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_002\" FROM cards WHERE \"XCL_004\" = 'arena' AND \"XCL_005\" = 'black'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:524"
  ]
}
```

### "legalities"."XCL_085" = 'Banned' AND "cards"."XCL_005" = 'white'

```json
{
  "kind": "predicate",
  "formula": "\"legalities\".\"XCL_085\" = 'Banned' AND \"cards\".\"XCL_005\" = 'white'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T2.\"XCL_085\" = 'Banned' AND T1.\"XCL_005\" = 'white'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:383"
  ]
}
```

### "sets"."XCL_096" = 309

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_096\" = 309",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_092\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T1.\"XCL_096\" = 309",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:404"
  ]
}
```

### "sets"."XCL_115" = 'expansion'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_115\" = 'expansion'",
  "grain": [
    "\"set_translations\".\"XCL_093\""
  ],
  "population_scope": "SELECT T2.\"XCL_093\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_115\" = 'expansion' GROUP BY T2.\"XCL_093\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:443"
  ]
}
```

### "cards"."XCL_004" = 'mtgo,paper' AND "cards"."XCL_005" = 'black' AND "cards"."XCL_019" = 2003 AND "cards"."XCL_037" = 'normal'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_004\" = 'mtgo,paper' AND \"cards\".\"XCL_005\" = 'black' AND \"cards\".\"XCL_019\" = 2003 AND \"cards\".\"XCL_037\" = 'normal'",
  "grain": [],
  "population_scope": "SELECT \"XCL_041\" FROM cards WHERE \"XCL_004\" = 'mtgo,paper' AND \"XCL_005\" = 'black' AND \"XCL_019\" = 2003 AND \"XCL_037\" = 'normal'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:397"
  ]
}
```

### "cards"."XCL_049" = 'Samite Pilgrim'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Samite Pilgrim'",
  "grain": [],
  "population_scope": "SELECT \"XCL_063\" FROM cards WHERE \"XCL_049\" = 'Samite Pilgrim'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:503"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE NOT \"XCL_006\" IS NULL AND NOT \"XCL_007\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM cards AS \"r0\" WHERE NOT \"r0\".\"XCL_006\" IS NULL AND NOT \"r0\".\"XCL_007\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:340"
  ]
}
```

### Calculates the percentage of rows in the filtered population where the column XCL_011 equals 10. The population is defined by the join between cards a

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"cards\".\"XCL_011\" = 10 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T1.\"XCL_011\" = 10 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\"), T1.\"XCL_049\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Abyssal Horror'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r0\".\"XCL_011\" = 10 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r0\".\"XCL_011\" = 10 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" INNER JOIN sets AS \"r1\" ON \"r1\".\"XCL_099\" = \"r0\".\"XCL_063\" WHERE \"r0\".\"XCL_049\" = 'Abyssal Horror'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:446"
  ]
}
```

### Aggregates the total number of rows in the 'cards' table where the value in column 'XCL_002' matches the literal 'Aaron Boyd'. The metric counts non-n

```json
{
  "kind": "metric",
  "formula": "COUNT(\"cards\".\"XCL_070\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_070\") FROM cards WHERE \"XCL_002\" = 'Aaron Boyd'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_070\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_070\") AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_002\" = 'Aaron Boyd'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:354"
  ]
}
```

### "set_translations"."XCL_092" = 'Portuguese (Brazil)'

```json
{
  "kind": "predicate",
  "formula": "\"set_translations\".\"XCL_092\" = 'Portuguese (Brazil)'",
  "grain": [],
  "population_scope": "SELECT \"XCL_093\" FROM set_translations WHERE \"XCL_092\" = 'Portuguese (Brazil)'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:507"
  ]
}
```

### "cards"."XCL_005" = 'black'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_005\" = 'black'",
  "grain": [
    "\"cards\".\"XCL_001\""
  ],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_005\" = 'black' GROUP BY \"XCL_001\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:435"
  ]
}
```

### "sets"."XCL_115" = 'expansion'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_115\" = 'expansion'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_092\" = 'Japanese' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_095\") FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T1.\"XCL_115\" = 'expansion'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:417"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_049\", T1.\"XCL_070\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_074\" = 'boros'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:444"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_002\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T2.\"XCL_076\" LIKE '%DAS perfekte Gegenmittel zu einer dichten Formation%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:411"
  ]
}
```

### "set_translations"."XCL_094" = 'Hauptset Zehnte Edition'

```json
{
  "kind": "predicate",
  "formula": "\"set_translations\".\"XCL_094\" = 'Hauptset Zehnte Edition'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_063\" WHERE T2.\"XCL_094\" = 'Hauptset Zehnte Edition'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:464"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_005\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_005\" FROM cards WHERE \"XCL_049\" = 'Ancestor''s Chosen'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:358"
  ]
}
```

### Identifier (XCL_093) from the set_translations table, filtered to records where the translation value (XCL_094) is 'Huitième édition'. Used to identif

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_093\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_093\" FROM set_translations WHERE \"XCL_094\" = 'Huitième édition'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_093\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_093\" AS \"value\" FROM set_translations AS \"r0\" WHERE \"r0\".\"XCL_094\" = 'Huitième édition'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:497"
  ]
}
```

### "legalities"."XCL_085" = 'Restricted' AND "cards"."XCL_034" = 0

```json
{
  "kind": "predicate",
  "formula": "\"legalities\".\"XCL_085\" = 'Restricted' AND \"cards\".\"XCL_034\" = 0",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T2.\"XCL_085\" = 'Restricted' AND T1.\"XCL_034\" = 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:361"
  ]
}
```

### "sets"."XCL_110" = 'World Championship Decks 2004'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_110\" = 'World Championship Decks 2004'",
  "grain": [],
  "population_scope": "SELECT \"XCL_099\" FROM sets WHERE \"XCL_110\" = 'World Championship Decks 2004'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:504"
  ]
}
```

### "sets"."XCL_112" = '2007-07-13'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_112\" = '2007-07-13'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_093\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_112\" = '2007-07-13'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:441"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [
    "\"cards\".\"XCL_049\"",
    "\"legalities\".\"XCL_084\""
  ],
  "population_scope": "SELECT T1.\"XCL_049\", T2.\"XCL_084\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T2.\"XCL_086\" = T1.\"XCL_072\" WHERE T1.\"XCL_013\" = 1 AND T2.\"XCL_085\" = 'Banned' GROUP BY T1.\"XCL_049\", T2.\"XCL_084\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_049\"",
    "grain": [
      "\"r0\".\"XCL_049\"",
      "\"r1\".\"XCL_084\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "legalities"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_049\" AS \"grain_0\", \"r1\".\"XCL_084\" AS \"grain_1\", \"r0\".\"XCL_049\" AS \"value\" FROM cards AS \"r0\" INNER JOIN legalities AS \"r1\" ON \"r1\".\"XCL_086\" = \"r0\".\"XCL_072\" WHERE \"r0\".\"XCL_013\" = 1 AND \"r1\".\"XCL_085\" = 'Banned' GROUP BY \"r0\".\"XCL_049\", \"r1\".\"XCL_084\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:522"
  ]
}
```

### Set Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_049\", T1.\"XCL_002\", T1.\"XCL_029\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_029\" = 1 AND T1.\"XCL_002\" = (SELECT \"XCL_002\" FROM cards WHERE \"XCL_029\" = 1 GROUP BY \"XCL_002\" HAVING COUNT(DISTINCT \"XCL_072\") = (SELECT MAX(\"count_uuid\") FROM (SELECT COUNT(DISTINCT \"XCL_072\") AS count_uuid FROM cards WHERE \"XCL_029\" = 1 GROUP BY \"XCL_002\"))) LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:349"
  ]
}
```

### "cards"."XCL_074" = 'abzan'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_074\" = 'abzan'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_049\", T1.\"XCL_070\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_074\" = 'abzan'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:448"
  ]
}
```

### Value of column XCL_106 from the sets table, filtered to rows where XCL_099 equals 'SS2'.

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_106\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_106\" FROM sets WHERE \"XCL_099\" = 'SS2'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_106\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_106\" AS \"value\" FROM sets AS \"r0\" WHERE \"r0\".\"XCL_099\" = 'SS2'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:490"
  ]
}
```

### "cards"."XCL_002" = 'Erica Yang' AND "legalities"."XCL_084" = 'pauper' AND "cards"."XCL_004" = 'paper'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_002\" = 'Erica Yang' AND \"legalities\".\"XCL_084\" = 'pauper' AND \"cards\".\"XCL_004\" = 'paper'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_002\" = 'Erica Yang' AND T2.\"XCL_084\" = 'pauper' AND T1.\"XCL_004\" = 'paper'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:410"
  ]
}
```

### The value of column XCL_092 from the set_translations table, filtered to rows where XCL_091 equals 174. Represents a specific translation or attribute

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_092\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_092\" FROM set_translations WHERE \"XCL_091\" = 174",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_092\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_092\" AS \"value\" FROM set_translations AS \"r0\" WHERE \"r0\".\"XCL_091\" = 174",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:438"
  ]
}
```

### "cards"."XCL_049" = 'Sublime Epiphany' AND "cards"."XCL_050" = '74s'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Sublime Epiphany' AND \"cards\".\"XCL_050\" = '74s'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_089\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_049\" = 'Sublime Epiphany' AND T1.\"XCL_050\" = '74s'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:348"
  ]
}
```

### Count of Distinct French Cards

```json
{
  "kind": "metric",
  "formula": "COUNT(T3.\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T3.\"XCL_001\") FROM (SELECT T1.\"XCL_001\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_002\" = 'Volkan Baǵa' AND T2.\"XCL_077\" = 'French' GROUP BY T1.\"XCL_001\") AS T3",
  "upstream_scopes": [
    "SELECT T1.\"XCL_001\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_002\" = 'Volkan Baǵa' AND T2.\"XCL_077\" = 'French' GROUP BY T1.\"XCL_001\""
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:516"
  ]
}
```

### Count of Cards with Attribute Value 3 in World Championship Decks 2004

```json
{
  "kind": "metric",
  "formula": "COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_063\" IN (SELECT \"XCL_099\" FROM sets WHERE \"XCL_110\" = 'World Championship Decks 2004') AND \"XCL_011\" = 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:504"
  ]
}
```

### Spanish Translation Value

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_093\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_093\" FROM set_translations WHERE \"XCL_092\" = 'Spanish'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_093\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_093\" AS \"value\" FROM set_translations AS \"r0\" WHERE \"r0\".\"XCL_092\" = 'Spanish'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:400"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_041\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_041\" FROM cards WHERE \"XCL_002\" = 'Rob Alexander'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_041\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_041\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_002\" = 'Rob Alexander'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:398"
  ]
}
```

### Distinct values of the legalities identifier (XCL_085) for cards designed by 'D. Alexander Gregory' in 1997 with a specific flag (XCL_022=1) that are 

```json
{
  "kind": "binding",
  "formula": "\"legalities\".\"XCL_085\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_085\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T2.\"XCL_086\" = T1.\"XCL_072\" WHERE T1.\"XCL_019\" = 1997 AND T1.\"XCL_022\" = 1 AND T1.\"XCL_002\" = 'D. Alexander Gregory' AND T2.\"XCL_084\" = 'legacy'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:521"
  ]
}
```

### "sets"."XCL_109" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_109\" IS NULL",
  "grain": [],
  "population_scope": "SELECT \"XCL_110\" FROM sets WHERE \"XCL_109\" IS NULL ORDER BY \"XCL_110\" LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:426"
  ]
}
```

### Card Attribute XCL_006

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_006\", \"XCL_007\" FROM cards WHERE NOT \"XCL_006\" IS NULL AND NOT \"XCL_007\" IS NULL ORDER BY \"XCL_006\" LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:423"
  ]
}
```

### Card ID

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\", \"XCL_010\" FROM cards WHERE \"XCL_001\" IN (SELECT \"XCL_091\" FROM set_translations WHERE \"XCL_093\" = 'OGW')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:387"
  ]
}
```

### Italian Translation of Set

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_094\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_094\" FROM set_translations WHERE \"XCL_093\" IN (SELECT \"XCL_063\" FROM cards WHERE \"XCL_049\" = 'Ancestor''s Chosen') AND \"XCL_092\" = 'Italian'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:462"
  ]
}
```

### "set_translations"."XCL_092" = 'Russian'

```json
{
  "kind": "predicate",
  "formula": "\"set_translations\".\"XCL_092\" = 'Russian'",
  "grain": [
    "\"sets\".\"XCL_096\""
  ],
  "population_scope": "SELECT T1.\"XCL_095\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_092\" = 'Russian' GROUP BY T1.\"XCL_096\" ORDER BY T1.\"XCL_096\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:432"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE NOT \"XCL_007\" IS NULL AND NOT \"XCL_006\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM cards AS \"r0\" WHERE NOT \"r0\".\"XCL_007\" IS NULL AND NOT \"r0\".\"XCL_006\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:378"
  ]
}
```

### Distinct non-null values of column XCL_065 from the cards table, restricted to rows where XCL_004 is 'arena' and XCL_066 is also non-null.

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_065\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_065\", \"XCL_066\" FROM cards WHERE \"XCL_004\" = 'arena' AND NOT \"XCL_065\" IS NULL AND NOT \"XCL_066\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:399"
  ]
}
```

### Set Name

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_095\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_110\", T1.\"XCL_095\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_092\" = 'Japanese' AND T1.\"XCL_100\" = 1 AND T1.\"XCL_101\" = 0",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_095\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_095\" AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r0\".\"XCL_099\" = \"r1\".\"XCL_093\" WHERE \"r1\".\"XCL_092\" = 'Japanese' AND \"r0\".\"XCL_100\" = 1 AND \"r0\".\"XCL_101\" = 0",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:431"
  ]
}
```

### "legalities"."XCL_084" = 'oldschool' AND ("legalities"."XCL_085" = 'Banned' OR "legalities"."XCL_085" = 'Restricted')

```json
{
  "kind": "predicate",
  "formula": "\"legalities\".\"XCL_084\" = 'oldschool' AND (\"legalities\".\"XCL_085\" = 'Banned' OR \"legalities\".\"XCL_085\" = 'Restricted')",
  "grain": [],
  "population_scope": "SELECT \"XCL_086\" FROM legalities WHERE \"XCL_084\" = 'oldschool' AND (\"XCL_085\" = 'Banned' OR \"XCL_085\" = 'Restricted')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:525"
  ]
}
```

### "sets"."XCL_097" = 'Ravnica' AND "sets"."XCL_096" = 180

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_097\" = 'Ravnica' AND \"sets\".\"XCL_096\" = 180",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_092\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T1.\"XCL_097\" = 'Ravnica' AND T1.\"XCL_096\" = 180",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:414"
  ]
}
```

### "cards"."XCL_002" = 'Stephen Daniele'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_002\" = 'Stephen Daniele'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T2.\"XCL_089\", T1.\"XCL_022\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_002\" = 'Stephen Daniele'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:347"
  ]
}
```

### Card identifier (XCL_086) from the legalities table where the format (XCL_084) is 'duel'. Used to filter cards that are legal in the duel format.

```json
{
  "kind": "binding",
  "formula": "\"legalities\".\"XCL_086\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_086\" FROM legalities WHERE \"XCL_084\" = 'duel'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_086\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "legalities"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_086\" AS \"value\" FROM legalities AS \"r0\" WHERE \"r0\".\"XCL_084\" = 'duel'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:514"
  ]
}
```

### Distinct Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_063\" WHERE T2.\"XCL_094\" = 'Hauptset Zehnte Edition'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:464"
  ]
}
```

### "cards"."XCL_049" = 'Molimo, Maro-Sorcerer'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Molimo, Maro-Sorcerer'",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_065\", \"XCL_066\" FROM cards WHERE \"XCL_049\" = 'Molimo, Maro-Sorcerer'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:456"
  ]
}
```

### An attribute of the card from the 'cards' table (XCL_022), likely representing a property such as type, set, or cost, for cards designed by 'Stephen D

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_022\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T2.\"XCL_089\", T1.\"XCL_022\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_002\" = 'Stephen Daniele'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_022\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "rulings"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_022\" AS \"value\" FROM cards AS \"r0\" INNER JOIN rulings AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_090\" WHERE \"r0\".\"XCL_002\" = 'Stephen Daniele'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:347"
  ]
}
```

### Identifier (XCL_099) of the set named 'Mirrodin' (XCL_110). Used to filter translations to a specific set.

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_099\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_099\" FROM sets WHERE \"XCL_110\" = 'Mirrodin'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_099\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_099\" AS \"value\" FROM sets AS \"r0\" WHERE \"r0\".\"XCL_110\" = 'Mirrodin'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:505"
  ]
}
```

### "sets"."XCL_110" LIKE '%FROM the Vault: Lore%'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_110\" LIKE '%FROM the Vault: Lore%'",
  "grain": [],
  "population_scope": "SELECT \"XCL_115\" FROM sets WHERE \"XCL_110\" LIKE '%FROM the Vault: Lore%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:492"
  ]
}
```

### Returns the value of the 'XCL_095' column from the 'sets' table. The population is restricted to sets that have a corresponding translation record in 

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_095\"",
  "grain": [
    "\"sets\".\"XCL_096\""
  ],
  "population_scope": "SELECT T1.\"XCL_095\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_092\" = 'Russian' GROUP BY T1.\"XCL_096\" ORDER BY T1.\"XCL_096\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:432"
  ]
}
```

### Aggregates the count of non-null values in the 'XCL_095' column from the 'sets' table. The population is restricted to sets that have a corresponding 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"sets\".\"XCL_095\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_095\") FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE NOT T2.\"XCL_094\" IS NULL AND T1.\"XCL_096\" < 100 AND T2.\"XCL_092\" = 'Italian'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_095\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_095\") AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r1\".\"XCL_093\" = \"r0\".\"XCL_099\" WHERE NOT \"r1\".\"XCL_094\" IS NULL AND \"r0\".\"XCL_096\" < 100 AND \"r1\".\"XCL_092\" = 'Italian'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:474"
  ]
}
```

### Attribute from the 'sets' table (T1) for sets that have an Italian translation. Grain: one row per set with an Italian translation.

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_114\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_110\", T1.\"XCL_114\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_092\" = 'Italian'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_114\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_114\" AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r0\".\"XCL_099\" = \"r1\".\"XCL_093\" WHERE \"r1\".\"XCL_092\" = 'Italian'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:353"
  ]
}
```

### "cards"."XCL_019" = 2015

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_019\" = 2015",
  "grain": [],
  "population_scope": "SELECT \"XCL_013\" FROM cards WHERE \"XCL_019\" = 2015",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:380"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_037\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_037\" FROM cards WHERE \"XCL_036\" = 'Flying'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_037\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_037\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_036\" = 'Flying'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:376"
  ]
}
```

### Distinct XCL_049 values

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_049\" FROM cards WHERE \"XCL_029\" = 1 AND NOT \"XCL_064\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:455"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_065\" = 'Angel,Wizard' AND \"XCL_064\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_065\" = 'Angel,Wizard' AND \"r0\".\"XCL_064\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:425"
  ]
}
```

### "legalities"."XCL_084" = 'legacy'

```json
{
  "kind": "predicate",
  "formula": "\"legalities\".\"XCL_084\" = 'legacy'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_072\", T3.\"XCL_077\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" INNER JOIN foreign_data AS T3 ON T1.\"XCL_072\" = T3.\"XCL_082\" WHERE T2.\"XCL_084\" = 'legacy'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:384"
  ]
}
```

### Card Name

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T1.\"XCL_002\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T2.\"XCL_085\" = 'Legal' AND T2.\"XCL_084\" = 'commander' AND (T1.\"XCL_055\" IS NULL OR T1.\"XCL_055\" = '*')",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_002\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "legalities"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_002\" AS \"value\" FROM cards AS \"r0\" INNER JOIN legalities AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_086\" WHERE \"r1\".\"XCL_085\" = 'Legal' AND \"r1\".\"XCL_084\" = 'commander' AND (\"r0\".\"XCL_055\" IS NULL OR \"r0\".\"XCL_055\" = '*')",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:346"
  ]
}
```

### Latest Commander Set Identifier

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_095\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_095\" FROM sets WHERE \"XCL_115\" = 'commander' ORDER BY \"XCL_114\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:513"
  ]
}
```

### "cards"."XCL_053" = 'Artifact' AND "cards"."XCL_010" = 'B'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_053\" = 'Artifact' AND \"cards\".\"XCL_010\" = 'B'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_053\" = 'Artifact' AND T1.\"XCL_010\" = 'B'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:391"
  ]
}
```

### "cards"."XCL_002" = 'Aaron Boyd'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_002\" = 'Aaron Boyd'",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_049\" FROM cards WHERE \"XCL_002\" = 'Aaron Boyd'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:373"
  ]
}
```

### Card Name or Title

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_070\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_049\", T1.\"XCL_070\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_074\" = 'abzan'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:448"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_005\" = 'black' AND \"XCL_026\" = 1",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_005\" = 'black' AND \"r0\".\"XCL_026\" = 1",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:437"
  ]
}
```

### "cards"."XCL_018" = 'extendedart'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_018\" = 'extendedart'",
  "grain": [
    "\"cards\".\"XCL_001\""
  ],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_018\" = 'extendedart' GROUP BY \"XCL_001\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:436"
  ]
}
```

### "sets"."XCL_110" = 'Coldsnap'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_110\" = 'Coldsnap'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Coldsnap' ORDER BY T1.\"XCL_011\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:476"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T1.\"XCL_002\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T2.\"XCL_085\" = 'Legal' AND T2.\"XCL_084\" = 'commander' AND (T1.\"XCL_055\" IS NULL OR T1.\"XCL_055\" = '*')",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "legalities"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM cards AS \"r0\" INNER JOIN legalities AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_086\" WHERE \"r1\".\"XCL_085\" = 'Legal' AND \"r1\".\"XCL_084\" = 'commander' AND (\"r0\".\"XCL_055\" IS NULL OR \"r0\".\"XCL_055\" = '*')",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:346"
  ]
}
```

### Set Translation Identifier

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_093\"",
  "grain": [
    "\"set_translations\".\"XCL_093\""
  ],
  "population_scope": "SELECT T2.\"XCL_093\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_115\" = 'expansion' GROUP BY T2.\"XCL_093\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_093\"",
    "grain": [
      "\"r1\".\"XCL_093\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_093\" AS \"grain_0\", \"r1\".\"XCL_093\" AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r1\".\"XCL_093\" = \"r0\".\"XCL_099\" WHERE \"r0\".\"XCL_115\" = 'expansion' GROUP BY \"r1\".\"XCL_093\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:443"
  ]
}
```

### Aggregates the total number of rows in the 'cards' table where the column 'XCL_055' contains the literal value '*'. The grain is a single scalar count

```json
{
  "kind": "metric",
  "formula": "COUNT(*)",
  "grain": [],
  "population_scope": "SELECT COUNT(*) FROM cards WHERE \"XCL_055\" = '*'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(*)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT COUNT(*) AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_055\" = '*'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:356"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_070\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_070\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_049\" = 'Benalish Knight'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:365"
  ]
}
```

### "sets"."XCL_110" = 'Coldsnap' AND "foreign_data"."XCL_077" = 'Italian'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_110\" = 'Coldsnap' AND \"foreign_data\".\"XCL_077\" = 'Italian'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_080\" FROM foreign_data AS T1 INNER JOIN cards AS T2 ON T2.\"XCL_072\" = T1.\"XCL_082\" INNER JOIN sets AS T3 ON T3.\"XCL_099\" = T2.\"XCL_063\" WHERE T3.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_077\" = 'Italian'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:483"
  ]
}
```

### "cards"."XCL_049" = 'Ancestor''s Chosen'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Ancestor''s Chosen'",
  "grain": [],
  "population_scope": "SELECT \"XCL_063\" FROM cards WHERE \"XCL_049\" = 'Ancestor''s Chosen'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:462"
  ]
}
```

### Card Name

```json
{
  "kind": "binding",
  "formula": "T1.\"XCL_049\"",
  "grain": [],
  "population_scope": "WITH MaxBanned AS (SELECT \"XCL_084\", COUNT(*) AS count_banned FROM legalities WHERE \"XCL_085\" = 'Banned' GROUP BY \"XCL_084\" ORDER BY COUNT(*) DESC LIMIT 1) SELECT T2.\"XCL_084\", T1.\"XCL_049\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T2.\"XCL_086\" = T1.\"XCL_072\" INNER JOIN MaxBanned AS MB ON MB.\"XCL_084\" = T2.\"XCL_084\" WHERE T2.\"XCL_085\" = 'Banned'",
  "upstream_scopes": [
    "SELECT \"XCL_084\", COUNT(*) AS count_banned FROM legalities WHERE \"XCL_085\" = 'Banned' GROUP BY \"XCL_084\" ORDER BY COUNT(*) DESC LIMIT 1"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:518"
  ]
}
```

### Card Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_002\" = 'Matthew D. Wilson' AND \"XCL_004\" = 'paper'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_002\" = 'Matthew D. Wilson' AND \"r0\".\"XCL_004\" = 'paper'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:526"
  ]
}
```

### Aggregates the total number of rows in the 'cards' table where 'XCL_002' is 'John Avon' and either 'XCL_007' or 'XCL_006' is NULL. Returns a single sc

```json
{
  "kind": "metric",
  "formula": "COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE (\"XCL_007\" IS NULL OR \"XCL_006\" IS NULL) AND \"XCL_002\" = 'John Avon'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" WHERE (\"r0\".\"XCL_007\" IS NULL OR \"r0\".\"XCL_006\" IS NULL) AND \"r0\".\"XCL_002\" = 'John Avon'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:393"
  ]
}
```

### Distinct non-null values of column XCL_066 from the cards table, restricted to rows where XCL_004 is 'arena' and XCL_065 is also non-null.

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_066\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_065\", \"XCL_066\" FROM cards WHERE \"XCL_004\" = 'arena' AND NOT \"XCL_065\" IS NULL AND NOT \"XCL_066\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:399"
  ]
}
```

### Card ID for 'Angel of Mercy'

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_063\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_063\" FROM cards WHERE \"XCL_049\" = 'Angel of Mercy'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_063\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_063\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_049\" = 'Angel of Mercy'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:463"
  ]
}
```

### A scalar metric representing the percentage of rows in the 'cards' table where the column 'XCL_034' equals 1 and the column 'XCL_037' equals 'normal'.

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"cards\".\"XCL_034\" = 1 AND \"cards\".\"XCL_037\" = 'normal' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*)",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN \"XCL_034\" = 1 AND \"XCL_037\" = 'normal' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) FROM cards",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r0\".\"XCL_034\" = 1 AND \"r0\".\"XCL_037\" = 'normal' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r0\".\"XCL_034\" = 1 AND \"r0\".\"XCL_037\" = 'normal' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) AS \"value\" FROM cards AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:424"
  ]
}
```

### "cards"."XCL_074" = 'boros'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_074\" = 'boros'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_049\", T1.\"XCL_070\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_074\" = 'boros'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:444"
  ]
}
```

### Aggregates the total number of rows in the 'cards' table where the column 'XCL_004' is 'paper' and the column 'XCL_020' is '3'. The grain is a single 

```json
{
  "kind": "metric",
  "formula": "SUM(CASE WHEN \"cards\".\"XCL_004\" = 'paper' AND \"cards\".\"XCL_020\" = '3' THEN 1 ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN \"XCL_004\" = 'paper' AND \"XCL_020\" = '3' THEN 1 ELSE 0 END) FROM cards",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(CASE WHEN \"r0\".\"XCL_004\" = 'paper' AND \"r0\".\"XCL_020\" = '3' THEN 1 ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT SUM(CASE WHEN \"r0\".\"XCL_004\" = 'paper' AND \"r0\".\"XCL_020\" = '3' THEN 1 ELSE 0 END) AS \"value\" FROM cards AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:451"
  ]
}
```

### "set_translations"."XCL_092" = 'Japanese'

```json
{
  "kind": "predicate",
  "formula": "\"set_translations\".\"XCL_092\" = 'Japanese'",
  "grain": [],
  "population_scope": "SELECT \"XCL_093\" FROM set_translations WHERE \"XCL_092\" = 'Japanese'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:506"
  ]
}
```

### "cards"."XCL_074" = 'colorpie'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_074\" = 'colorpie'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_077\", T2.\"XCL_076\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_074\" = 'colorpie'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:445"
  ]
}
```

### "cards"."XCL_049" = 'Ancestor''s Chosen' AND NOT "cards"."XCL_053" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Ancestor''s Chosen' AND NOT \"cards\".\"XCL_053\" IS NULL",
  "grain": [],
  "population_scope": "SELECT \"XCL_053\" FROM cards WHERE \"XCL_049\" = 'Ancestor''s Chosen' AND NOT \"XCL_053\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:359"
  ]
}
```

### The value of column XCL_013 from the cards table, filtered to rows where XCL_019 equals 2015.

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_013\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_013\" FROM cards WHERE \"XCL_019\" = 2015",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_013\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_013\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_019\" = 2015",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:380"
  ]
}
```

### "cards"."XCL_002" = 'Jim Pavelec'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_002\" = 'Jim Pavelec'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_089\", CASE WHEN T1.\"XCL_022\" = 1 THEN 'YES' ELSE 'NO' END FROM cards AS T1 INNER JOIN rulings AS T2 ON T2.\"XCL_090\" = T1.\"XCL_072\" WHERE T1.\"XCL_002\" = 'Jim Pavelec'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:494"
  ]
}
```

### "foreign_data"."XCL_077" = 'Phyrexian'

```json
{
  "kind": "predicate",
  "formula": "\"foreign_data\".\"XCL_077\" = 'Phyrexian'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_002\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T2.\"XCL_077\" = 'Phyrexian'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:367"
  ]
}
```

### "cards"."XCL_033" = 1

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_033\" = 1",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_077\" = 'French' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_033\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:371"
  ]
}
```

### The specific translation value (XCL_092) from the set_translations table for sets where the set identifier (XCL_096) is 309. Grain: one row per matchi

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_092\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_092\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T1.\"XCL_096\" = 309",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_092\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_092\" AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r0\".\"XCL_099\" = \"r1\".\"XCL_093\" WHERE \"r0\".\"XCL_096\" = 309",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:404"
  ]
}
```

### Card Name

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_019\", T1.\"XCL_049\", IIF(T2.\"XCL_085\" = 'Banned', T1.\"XCL_049\", 'NO') FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_002\" = 'Allen Williams'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:530"
  ]
}
```

### The value of column XCL_110 from the sets table, restricted to rows where XCL_109 is NULL, sorted ascending by XCL_110, and limited to the first 3 rec

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_110\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_110\" FROM sets WHERE \"XCL_109\" IS NULL ORDER BY \"XCL_110\" LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:426"
  ]
}
```

### "set_translations"."XCL_094" = 'Huitième édition'

```json
{
  "kind": "predicate",
  "formula": "\"set_translations\".\"XCL_094\" = 'Huitième édition'",
  "grain": [],
  "population_scope": "SELECT \"XCL_093\" FROM set_translations WHERE \"XCL_094\" = 'Huitième édition'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:497"
  ]
}
```

### Chinese Simplified Set Name

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_094\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_094\" FROM set_translations WHERE \"XCL_093\" IN (SELECT \"XCL_099\" FROM sets WHERE \"XCL_110\" = 'Mirrodin') AND \"XCL_092\" = 'Chinese Simplified'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:505"
  ]
}
```

### Aggregates the count of unique card identifiers (XCL_001) from the cards table where the card is not flagged (XCL_034 = 0) and is associated with a le

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T2.\"XCL_085\" = 'Restricted' AND T1.\"XCL_034\" = 0",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "legalities"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" INNER JOIN legalities AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_086\" WHERE \"r1\".\"XCL_085\" = 'Restricted' AND \"r0\".\"XCL_034\" = 0",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:361"
  ]
}
```

### The value of column XCL_115 from the 'sets' table, filtered to rows where column XCL_110 contains the substring 'FROM the Vault: Lore'.

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_115\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_115\" FROM sets WHERE \"XCL_110\" LIKE '%FROM the Vault: Lore%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_115\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_115\" AS \"value\" FROM sets AS \"r0\" WHERE \"r0\".\"XCL_110\" LIKE '%FROM the Vault: Lore%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:492"
  ]
}
```

### A conditional metric that returns the card name if its legality status in the 'legalities' table is 'Banned', otherwise returns the string 'NO'. This 

```json
{
  "kind": "binding",
  "formula": "IIF(\"legalities\".\"XCL_085\" = 'Banned', \"cards\".\"XCL_049\", 'NO')",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_019\", T1.\"XCL_049\", IIF(T2.\"XCL_085\" = 'Banned', T1.\"XCL_049\", 'NO') FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_002\" = 'Allen Williams'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:530"
  ]
}
```

### Card Name or Title

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_049\", T1.\"XCL_002\", T1.\"XCL_029\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_029\" = 1 AND T1.\"XCL_002\" = (SELECT \"XCL_002\" FROM cards WHERE \"XCL_029\" = 1 GROUP BY \"XCL_002\" HAVING COUNT(DISTINCT \"XCL_072\") = (SELECT MAX(\"count_uuid\") FROM (SELECT COUNT(DISTINCT \"XCL_072\") AS count_uuid FROM cards WHERE \"XCL_029\" = 1 GROUP BY \"XCL_002\"))) LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:349"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_002\" = 'Erica Yang' AND T2.\"XCL_084\" = 'pauper' AND T1.\"XCL_004\" = 'paper'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "legalities"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM cards AS \"r0\" INNER JOIN legalities AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_086\" WHERE \"r0\".\"XCL_002\" = 'Erica Yang' AND \"r1\".\"XCL_084\" = 'pauper' AND \"r0\".\"XCL_004\" = 'paper'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:410"
  ]
}
```

### Set Translation Key

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_093\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_093\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_115\" = 'commander'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_093\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_093\" AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r1\".\"XCL_093\" = \"r0\".\"XCL_099\" WHERE \"r0\".\"XCL_115\" = 'commander'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:447"
  ]
}
```

### Distinct XCL_058 for bundle cards

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_058\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_058\" FROM cards WHERE \"XCL_057\" = 'bundle'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:457"
  ]
}
```

### Distinct values of the set identifier column (XCL_112) from the sets table, filtered to sets containing the specific card 'Ancestor's Chosen'.

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_112\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_112\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Ancestor''s Chosen'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:470"
  ]
}
```

### "cards"."XCL_055" IS NULL OR "cards"."XCL_055" = '*'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_055\" IS NULL OR \"cards\".\"XCL_055\" = '*'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_077\" = 'French' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_055\" IS NULL OR T1.\"XCL_055\" = '*'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:416"
  ]
}
```

### Aggregates the total number of rows in the 'cards' table where the 'XCL_004' field contains the substring 'arena,mtgo' and the 'XCL_005' field is exac

```json
{
  "kind": "metric",
  "formula": "COUNT(CASE WHEN \"cards\".\"XCL_004\" LIKE '%arena,mtgo%' AND \"cards\".\"XCL_005\" = 'black' THEN 1 ELSE NULL END)",
  "grain": [],
  "population_scope": "SELECT COUNT(CASE WHEN \"XCL_004\" LIKE '%arena,mtgo%' AND \"XCL_005\" = 'black' THEN 1 ELSE NULL END) FROM cards",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(CASE WHEN \"r0\".\"XCL_004\" LIKE '%arena,mtgo%' AND \"r0\".\"XCL_005\" = 'black' THEN 1 ELSE NULL END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT COUNT(CASE WHEN \"r0\".\"XCL_004\" LIKE '%arena,mtgo%' AND \"r0\".\"XCL_005\" = 'black' THEN 1 ELSE NULL END) AS \"value\" FROM cards AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:458"
  ]
}
```

### "sets"."XCL_110" = 'Commander 2014 Oversized'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_110\" = 'Commander 2014 Oversized'",
  "grain": [],
  "population_scope": "SELECT \"XCL_111\" FROM sets WHERE \"XCL_110\" = 'Commander 2014 Oversized'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:493"
  ]
}
```

### "legalities"."XCL_084" = 'gladiator' AND "legalities"."XCL_085" = 'Banned' AND "cards"."XCL_059" = 'mythic'

```json
{
  "kind": "predicate",
  "formula": "\"legalities\".\"XCL_084\" = 'gladiator' AND \"legalities\".\"XCL_085\" = 'Banned' AND \"cards\".\"XCL_059\" = 'mythic'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_001\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T2.\"XCL_084\" = 'gladiator' AND T2.\"XCL_085\" = 'Banned' AND T1.\"XCL_059\" = 'mythic'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:344"
  ]
}
```

### "foreign_data"."XCL_077" = 'Chinese Simplified'

```json
{
  "kind": "predicate",
  "formula": "\"foreign_data\".\"XCL_077\" = 'Chinese Simplified'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_002\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T2.\"XCL_077\" = 'Chinese Simplified'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:381"
  ]
}
```

### "cards"."XCL_069" = 99

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_069\" = 99",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_069\" = 99",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:372"
  ]
}
```

### Distinct values of the foreign data identifier (XCL_080) for records associated with the 'Coldsnap' set and filtered by the 'Italian' attribute (XCL_0

```json
{
  "kind": "binding",
  "formula": "\"foreign_data\".\"XCL_080\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_080\" FROM foreign_data AS T1 INNER JOIN cards AS T2 ON T2.\"XCL_072\" = T1.\"XCL_082\" INNER JOIN sets AS T3 ON T3.\"XCL_099\" = T2.\"XCL_063\" WHERE T3.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_077\" = 'Italian'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:483"
  ]
}
```

### Card Attribute XCL_070

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_070\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_077\", T1.\"XCL_070\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_074\" = 'azorius'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:449"
  ]
}
```

### "sets"."XCL_110" = 'Battlebond'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_110\" = 'Battlebond'",
  "grain": [],
  "population_scope": "SELECT \"XCL_095\" FROM sets WHERE \"XCL_110\" = 'Battlebond'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:519"
  ]
}
```

### "cards"."XCL_019" = 1993 AND "cards"."XCL_004" = 'paper' AND "cards"."XCL_022" = 1

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_019\" = 1993 AND \"cards\".\"XCL_004\" = 'paper' AND \"cards\".\"XCL_022\" = 1",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_019\" = 1993 AND \"XCL_004\" = 'paper' AND \"XCL_022\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:396"
  ]
}
```

### Set Identifier

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_110\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_110\", T1.\"XCL_095\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_092\" = 'Japanese' AND T1.\"XCL_100\" = 1 AND T1.\"XCL_101\" = 0",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_110\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_110\" AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r0\".\"XCL_099\" = \"r1\".\"XCL_093\" WHERE \"r1\".\"XCL_092\" = 'Japanese' AND \"r0\".\"XCL_100\" = 1 AND \"r0\".\"XCL_101\" = 0",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:431"
  ]
}
```

### "cards"."XCL_049" = 'Condemn'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Condemn'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_089\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_049\" = 'Condemn'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:362"
  ]
}
```

### Distinct XCL_049 values

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_049\" FROM cards WHERE \"XCL_034\" = 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:452"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_049\", CASE WHEN T1.\"XCL_085\" = 'Legal' THEN T1.\"XCL_084\" ELSE NULL END FROM legalities AS T1 INNER JOIN cards AS T2 ON T2.\"XCL_072\" = T1.\"XCL_086\" WHERE T2.\"XCL_063\" IN (SELECT \"XCL_099\" FROM sets WHERE \"XCL_110\" = 'Hour of Devastation')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:528"
  ]
}
```

### Calculates the percentage of records in the joined population where the foreign_data.XCL_077 field equals 'French'. The numerator counts rows matching

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"foreign_data\".\"XCL_077\" = 'French' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_077\" = 'French' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_033\" = 1",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r1\".\"XCL_077\" = 'French' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "foreign_data"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r1\".\"XCL_077\" = 'French' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" INNER JOIN foreign_data AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_082\" WHERE \"r0\".\"XCL_033\" = 1",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:371"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_049\" FROM cards WHERE (\"XCL_055\" IS NULL OR \"XCL_055\" LIKE '%*%') AND \"XCL_057\" = 'arenaleague' ORDER BY \"XCL_049\" LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:421"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_001\"",
  "grain": [
    "\"cards\".\"XCL_001\""
  ],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_018\" = 'extendedart' GROUP BY \"XCL_001\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [
      "\"r0\".\"XCL_001\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"grain_0\", \"r0\".\"XCL_001\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_018\" = 'extendedart' GROUP BY \"r0\".\"XCL_001\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:436"
  ]
}
```

### "cards"."XCL_049" IN ('Serra Angel', 'Shrine Keeper')

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" IN ('Serra Angel', 'Shrine Keeper')",
  "grain": [],
  "population_scope": "SELECT \"XCL_049\" FROM cards WHERE \"XCL_049\" IN ('Serra Angel', 'Shrine Keeper') ORDER BY \"XCL_011\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:459"
  ]
}
```

### "cards"."XCL_029" = 1

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_029\" = 1",
  "grain": [
    "\"cards\".\"XCL_002\""
  ],
  "population_scope": "SELECT COUNT(DISTINCT \"XCL_072\") AS count_uuid FROM cards WHERE \"XCL_029\" = 1 GROUP BY \"XCL_002\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:349"
  ]
}
```

### Card Name

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_002\"",
  "grain": [
    "\"cards\".\"XCL_002\""
  ],
  "population_scope": "SELECT T1.\"XCL_002\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE (T2.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_002\" = 'Chippy') OR (T2.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_002\" = 'Aaron Miller') OR (T2.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_002\" = 'Jeremy Jarvis') GROUP BY T1.\"XCL_002\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_002\"",
    "grain": [
      "\"r0\".\"XCL_002\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_002\" AS \"grain_0\", \"r0\".\"XCL_002\" AS \"value\" FROM cards AS \"r0\" INNER JOIN sets AS \"r1\" ON \"r1\".\"XCL_099\" = \"r0\".\"XCL_063\" WHERE (\"r1\".\"XCL_110\" = 'Coldsnap' AND \"r0\".\"XCL_002\" = 'Chippy') OR (\"r1\".\"XCL_110\" = 'Coldsnap' AND \"r0\".\"XCL_002\" = 'Aaron Miller') OR (\"r1\".\"XCL_110\" = 'Coldsnap' AND \"r0\".\"XCL_002\" = 'Jeremy Jarvis') GROUP BY \"r0\".\"XCL_002\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:477"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_019\", T1.\"XCL_049\", IIF(T2.\"XCL_085\" = 'Banned', T1.\"XCL_049\", 'NO') FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_002\" = 'Allen Williams'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:530"
  ]
}
```

### Card Identifier (XCL_049)

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_049\" FROM cards WHERE \"XCL_019\" = 2003 ORDER BY \"XCL_011\" DESC LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:461"
  ]
}
```

### NOT "cards"."XCL_006" IS NULL AND NOT "cards"."XCL_007" IS NULL

```json
{
  "kind": "predicate",
  "formula": "NOT \"cards\".\"XCL_006\" IS NULL AND NOT \"cards\".\"XCL_007\" IS NULL",
  "grain": [
    "\"cards\".\"XCL_018\""
  ],
  "population_scope": "SELECT \"XCL_018\" FROM cards WHERE NOT \"XCL_006\" IS NULL AND NOT \"XCL_007\" IS NULL GROUP BY \"XCL_018\" ORDER BY COUNT(\"XCL_018\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:511"
  ]
}
```

### "cards"."XCL_049" = 'Tendo Ice Bridge' AND "set_translations"."XCL_092" = 'French' AND NOT "set_translations"."XCL_094" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Tendo Ice Bridge' AND \"set_translations\".\"XCL_092\" = 'French' AND NOT \"set_translations\".\"XCL_094\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_094\" FROM cards AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Tendo Ice Bridge' AND T2.\"XCL_092\" = 'French' AND NOT T2.\"XCL_094\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:498"
  ]
}
```

### Ruling Text

```json
{
  "kind": "binding",
  "formula": "\"rulings\".\"XCL_089\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T2.\"XCL_089\", T1.\"XCL_022\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_002\" = 'Stephen Daniele'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_089\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "rulings"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_089\" AS \"value\" FROM cards AS \"r0\" INNER JOIN rulings AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_090\" WHERE \"r0\".\"XCL_002\" = 'Stephen Daniele'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:347"
  ]
}
```

### "cards"."XCL_001" BETWEEN 1 AND 20

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_001\" BETWEEN 1 AND 20",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_010\", T2.\"XCL_084\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_001\" BETWEEN 1 AND 20",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:390"
  ]
}
```

### "cards"."XCL_059" = 'rare' AND "rulings"."XCL_088" = '2007-02-01'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_059\" = 'rare' AND \"rulings\".\"XCL_088\" = '2007-02-01'",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_001\") FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_059\" = 'rare' AND T2.\"XCL_088\" = '2007-02-01'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:413"
  ]
}
```

### "cards"."XCL_049" = 'Ancestor''s Chosen'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Ancestor''s Chosen'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_112\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Ancestor''s Chosen'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:470"
  ]
}
```

### "cards"."XCL_028" = 1 AND "cards"."XCL_030" = 1 AND "cards"."XCL_029" = 1

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_028\" = 1 AND \"cards\".\"XCL_030\" = 1 AND \"cards\".\"XCL_029\" = 1",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_028\" = 1 AND \"XCL_030\" = 1 AND \"XCL_029\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:420"
  ]
}
```

### Distinct values of the 'XCL_085' column from the 'legalities' table. Represents the specific legality record identifiers associated with Artifact card

```json
{
  "kind": "binding",
  "formula": "\"legalities\".\"XCL_085\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_085\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_070\" = 'Artifact' AND T2.\"XCL_084\" = 'vintage' AND T1.\"XCL_064\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:345"
  ]
}
```

### "set_translations"."XCL_092" = 'Korean' AND "set_translations"."XCL_092" NOT LIKE '%Japanese%'

```json
{
  "kind": "predicate",
  "formula": "\"set_translations\".\"XCL_092\" = 'Korean' AND \"set_translations\".\"XCL_092\" NOT LIKE '%Japanese%'",
  "grain": [],
  "population_scope": "SELECT \"XCL_093\" FROM set_translations WHERE \"XCL_092\" = 'Korean' AND \"XCL_092\" NOT LIKE '%Japanese%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:529"
  ]
}
```

### Card identifier XCL_049

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T1.\"XCL_011\" = 10 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\"), T1.\"XCL_049\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Abyssal Horror'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:446"
  ]
}
```

### Set Identifier for World Championship Decks 2004

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_099\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_099\" FROM sets WHERE \"XCL_110\" = 'World Championship Decks 2004'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_099\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_099\" AS \"value\" FROM sets AS \"r0\" WHERE \"r0\".\"XCL_110\" = 'World Championship Decks 2004'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:504"
  ]
}
```

### "sets"."XCL_110" = 'Coldsnap' AND "cards"."XCL_050" = 4

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_110\" = 'Coldsnap' AND \"cards\".\"XCL_050\" = 4",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_050\" = 4",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:478"
  ]
}
```

### Legality Attribute

```json
{
  "kind": "binding",
  "formula": "\"legalities\".\"XCL_084\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_010\", T2.\"XCL_084\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_001\" BETWEEN 1 AND 20",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_084\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "legalities"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_084\" AS \"value\" FROM cards AS \"r0\" INNER JOIN legalities AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_086\" WHERE \"r0\".\"XCL_001\" BETWEEN 1 AND 20",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:390"
  ]
}
```

### A specific attribute from the 'foreign_data' table associated with the card. The exact business meaning is unknown due to obfuscated column name, but 

```json
{
  "kind": "binding",
  "formula": "\"foreign_data\".\"XCL_077\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_072\", T3.\"XCL_077\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" INNER JOIN foreign_data AS T3 ON T1.\"XCL_072\" = T3.\"XCL_082\" WHERE T2.\"XCL_084\" = 'legacy'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_077\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "legalities"
      },
      {
        "role": "r2",
        "physical_table": "foreign_data"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_077\" AS \"value\" FROM cards AS \"r0\" INNER JOIN legalities AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_086\" INNER JOIN foreign_data AS \"r2\" ON \"r0\".\"XCL_072\" = \"r2\".\"XCL_082\" WHERE \"r1\".\"XCL_084\" = 'legacy'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:384"
  ]
}
```

### Foreign Data Attribute XCL_076

```json
{
  "kind": "binding",
  "formula": "\"foreign_data\".\"XCL_076\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_076\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_049\" = 'Ancestor''s Chosen' AND T2.\"XCL_077\" = 'Italian'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_076\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "foreign_data"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_076\" AS \"value\" FROM cards AS \"r0\" INNER JOIN foreign_data AS \"r1\" ON \"r1\".\"XCL_082\" = \"r0\".\"XCL_072\" WHERE \"r0\".\"XCL_049\" = 'Ancestor''s Chosen' AND \"r1\".\"XCL_077\" = 'Italian'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:480"
  ]
}
```

### "cards"."XCL_004" = 'arena' AND NOT "cards"."XCL_065" IS NULL AND NOT "cards"."XCL_066" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_004\" = 'arena' AND NOT \"cards\".\"XCL_065\" IS NULL AND NOT \"cards\".\"XCL_066\" IS NULL",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_065\", \"XCL_066\" FROM cards WHERE \"XCL_004\" = 'arena' AND NOT \"XCL_065\" IS NULL AND NOT \"XCL_066\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:399"
  ]
}
```

### Card Name

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_049\" FROM cards WHERE \"XCL_049\" IN ('Serra Angel', 'Shrine Keeper') ORDER BY \"XCL_011\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:459"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_057\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_057\" FROM cards WHERE \"XCL_049\" = 'Duress' AND NOT \"XCL_057\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_057\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_057\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_049\" = 'Duress' AND NOT \"r0\".\"XCL_057\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:357"
  ]
}
```

### Returns the single value of column XCL_095 from the sets table corresponding to the row with the maximum value in column XCL_096. The grain is a singl

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_095\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_095\" FROM sets ORDER BY \"XCL_096\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:509"
  ]
}
```

### Distinct Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_001\"",
  "grain": [
    "\"cards\".\"XCL_001\""
  ],
  "population_scope": "SELECT T1.\"XCL_001\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_002\" = 'Volkan Baǵa' AND T2.\"XCL_077\" = 'French' GROUP BY T1.\"XCL_001\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [
      "\"r0\".\"XCL_001\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "foreign_data"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"grain_0\", \"r0\".\"XCL_001\" AS \"value\" FROM cards AS \"r0\" INNER JOIN foreign_data AS \"r1\" ON \"r1\".\"XCL_082\" = \"r0\".\"XCL_072\" WHERE \"r0\".\"XCL_002\" = 'Volkan Baǵa' AND \"r1\".\"XCL_077\" = 'French' GROUP BY \"r0\".\"XCL_001\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:516"
  ]
}
```

### "cards"."XCL_053" = 'Creature - Elf'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_053\" = 'Creature - Elf'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T2.\"XCL_088\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_053\" = 'Creature - Elf'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:389"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_004\" = 'paper' AND T2.\"XCL_077\" = 'Japanese'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_049\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "foreign_data"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_049\" AS \"value\" FROM cards AS \"r0\" INNER JOIN foreign_data AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_082\" WHERE \"r0\".\"XCL_004\" = 'paper' AND \"r1\".\"XCL_077\" = 'Japanese'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:382"
  ]
}
```

### "sets"."XCL_112" = '2017-06-09'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_112\" = '2017-06-09'",
  "grain": [],
  "population_scope": "SELECT \"XCL_108\" FROM sets WHERE \"XCL_112\" = '2017-06-09'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:491"
  ]
}
```

### "set_translations"."XCL_092" = 'Italian'

```json
{
  "kind": "predicate",
  "formula": "\"set_translations\".\"XCL_092\" = 'Italian'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_110\", T1.\"XCL_114\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_092\" = 'Italian'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:353"
  ]
}
```

### "cards"."XCL_013" > 12000 AND "cards"."XCL_005" = 'borderless'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_013\" > 12000 AND \"cards\".\"XCL_005\" = 'borderless'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_013\" > 12000 AND \"XCL_005\" = 'borderless'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:419"
  ]
}
```

### Count of distinct cards with restricted legality

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T2.\"XCL_085\" = 'Restricted' AND T1.\"XCL_032\" = 1",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "legalities"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" INNER JOIN legalities AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_086\" WHERE \"r1\".\"XCL_085\" = 'Restricted' AND \"r0\".\"XCL_032\" = 1",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:363"
  ]
}
```

### Calculates the percentage of joined foreign_data records where XCL_077 is 'French' relative to the total count of cards records. The population is res

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"foreign_data\".\"XCL_077\" = 'French' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_077\" = 'French' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_055\" IS NULL OR T1.\"XCL_055\" = '*'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r1\".\"XCL_077\" = 'French' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "foreign_data"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r1\".\"XCL_077\" = 'French' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" INNER JOIN foreign_data AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_082\" WHERE \"r0\".\"XCL_055\" IS NULL OR \"r0\".\"XCL_055\" = '*'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:416"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" INNER JOIN legalities AS T3 ON T1.\"XCL_072\" = T3.\"XCL_086\" WHERE T3.\"XCL_085\" = 'Legal' AND T1.\"XCL_071\" = 'Creature'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "rulings"
      },
      {
        "role": "r2",
        "physical_table": "legalities"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM cards AS \"r0\" INNER JOIN rulings AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_090\" INNER JOIN legalities AS \"r2\" ON \"r0\".\"XCL_072\" = \"r2\".\"XCL_086\" WHERE \"r2\".\"XCL_085\" = 'Legal' AND \"r0\".\"XCL_071\" = 'Creature'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:406"
  ]
}
```

### "legalities"."XCL_084" = 'duel'

```json
{
  "kind": "predicate",
  "formula": "\"legalities\".\"XCL_084\" = 'duel'",
  "grain": [],
  "population_scope": "SELECT \"XCL_086\" FROM legalities WHERE \"XCL_084\" = 'duel'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:514"
  ]
}
```

### "cards"."XCL_002" = 'Volkan Baǵa' AND "foreign_data"."XCL_077" = 'French'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_002\" = 'Volkan Baǵa' AND \"foreign_data\".\"XCL_077\" = 'French'",
  "grain": [
    "\"cards\".\"XCL_001\""
  ],
  "population_scope": "SELECT T1.\"XCL_001\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_002\" = 'Volkan Baǵa' AND T2.\"XCL_077\" = 'French' GROUP BY T1.\"XCL_001\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:516"
  ]
}
```

### "sets"."XCL_115" = 'commander'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_115\" = 'commander'",
  "grain": [],
  "population_scope": "SELECT \"XCL_095\" FROM sets WHERE \"XCL_115\" = 'commander' ORDER BY \"XCL_114\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:513"
  ]
}
```

### Percentage of Sets with XCL_102 Flag

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"sets\".\"XCL_102\" = 1 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"sets\".\"XCL_095\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN \"XCL_102\" = 1 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"XCL_095\") FROM sets WHERE \"XCL_099\" IN (SELECT \"XCL_093\" FROM set_translations WHERE \"XCL_092\" = 'Japanese')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:506"
  ]
}
```

### Count of distinct sets (XCL_095) that have a non-null translation (XCL_094) in Italian (XCL_092) for the 'Ice Age' set (XCL_097). The grain is a singl

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"sets\".\"XCL_095\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_095\") FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_097\" = 'Ice Age' AND T2.\"XCL_092\" = 'Italian' AND NOT T2.\"XCL_094\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_095\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r0\".\"XCL_095\") AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r1\".\"XCL_093\" = \"r0\".\"XCL_099\" WHERE \"r0\".\"XCL_097\" = 'Ice Age' AND \"r1\".\"XCL_092\" = 'Italian' AND NOT \"r1\".\"XCL_094\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:472"
  ]
}
```

### A boolean indicator ('YES' or 'NO') determining if the specified card has at least one non-null Korean translation record. It aggregates across all ma

```json
{
  "kind": "metric",
  "formula": "IIF(SUM(CASE WHEN \"set_translations\".\"XCL_092\" = 'Korean' AND NOT \"set_translations\".\"XCL_094\" IS NULL THEN 1 ELSE 0 END) > 0, 'YES', 'NO')",
  "grain": [],
  "population_scope": "SELECT IIF(SUM(CASE WHEN T2.\"XCL_092\" = 'Korean' AND NOT T2.\"XCL_094\" IS NULL THEN 1 ELSE 0 END) > 0, 'YES', 'NO') FROM cards AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Ancestor''s Chosen'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "IIF(SUM(CASE WHEN \"r1\".\"XCL_092\" = 'Korean' AND NOT \"r1\".\"XCL_094\" IS NULL THEN 1 ELSE 0 END) > 0, 'YES', 'NO')",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT IIF(SUM(CASE WHEN \"r1\".\"XCL_092\" = 'Korean' AND NOT \"r1\".\"XCL_094\" IS NULL THEN 1 ELSE 0 END) > 0, 'YES', 'NO') AS \"value\" FROM cards AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r1\".\"XCL_093\" = \"r0\".\"XCL_063\" WHERE \"r0\".\"XCL_049\" = 'Ancestor''s Chosen'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:465"
  ]
}
```

### Identifier (XCL_099) of the set named 'Hour of Devastation' from the sets table. Used to filter cards belonging to this specific set.

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_099\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_099\" FROM sets WHERE \"XCL_110\" = 'Hour of Devastation'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_099\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_099\" AS \"value\" FROM sets AS \"r0\" WHERE \"r0\".\"XCL_110\" = 'Hour of Devastation'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:528"
  ]
}
```

### "cards"."XCL_029" = 1 AND NOT "cards"."XCL_064" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_029\" = 1 AND NOT \"cards\".\"XCL_064\" IS NULL",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_049\" FROM cards WHERE \"XCL_029\" = 1 AND NOT \"XCL_064\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:455"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_001\"",
  "grain": [
    "\"cards\".\"XCL_001\""
  ],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_005\" = 'black' GROUP BY \"XCL_001\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [
      "\"r0\".\"XCL_001\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"grain_0\", \"r0\".\"XCL_001\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_005\" = 'black' GROUP BY \"r0\".\"XCL_001\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:435"
  ]
}
```

### Distinct card name (XCL_049) from the cards table for cards whose ID (XCL_072) is present in the set of duel legal card IDs. Represents the top 10 car

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_049\" FROM cards WHERE \"XCL_072\" IN (SELECT \"XCL_086\" FROM legalities WHERE \"XCL_084\" = 'duel') ORDER BY \"XCL_041\" DESC LIMIT 10 OFFSET 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:514"
  ]
}
```

### Aggregates the total number of rows in the 'cards' table where 'XCL_020' is '-1', 'XCL_002' is 'UDON', and 'XCL_004' is 'mtgo'. Returns a single scala

```json
{
  "kind": "metric",
  "formula": "COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_020\" = '-1' AND \"XCL_002\" = 'UDON' AND \"XCL_004\" = 'mtgo'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_020\" = '-1' AND \"r0\".\"XCL_002\" = 'UDON' AND \"r0\".\"XCL_004\" = 'mtgo'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:395"
  ]
}
```

### "cards"."XCL_020" = '-1' AND "cards"."XCL_002" = 'UDON' AND "cards"."XCL_004" = 'mtgo'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_020\" = '-1' AND \"cards\".\"XCL_002\" = 'UDON' AND \"cards\".\"XCL_004\" = 'mtgo'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_020\" = '-1' AND \"XCL_002\" = 'UDON' AND \"XCL_004\" = 'mtgo'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:395"
  ]
}
```

### "cards"."XCL_019" = 'future'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_019\" = 'future'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_019\" = 'future'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:386"
  ]
}
```

### Set Translation Identifier

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_093\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_093\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_112\" = '2007-07-13'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_093\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_093\" AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r1\".\"XCL_093\" = \"r0\".\"XCL_099\" WHERE \"r0\".\"XCL_112\" = '2007-07-13'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:441"
  ]
}
```

### "sets"."XCL_110" = 'Mirrodin'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_110\" = 'Mirrodin'",
  "grain": [],
  "population_scope": "SELECT \"XCL_099\" FROM sets WHERE \"XCL_110\" = 'Mirrodin'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:505"
  ]
}
```

### Card Flag

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_029\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_049\", T1.\"XCL_002\", T1.\"XCL_029\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_029\" = 1 AND T1.\"XCL_002\" = (SELECT \"XCL_002\" FROM cards WHERE \"XCL_029\" = 1 GROUP BY \"XCL_002\" HAVING COUNT(DISTINCT \"XCL_072\") = (SELECT MAX(\"count_uuid\") FROM (SELECT COUNT(DISTINCT \"XCL_072\") AS count_uuid FROM cards WHERE \"XCL_029\" = 1 GROUP BY \"XCL_002\"))) LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:349"
  ]
}
```

### Card Identifier (XCL_049)

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_049\" FROM cards ORDER BY \"XCL_014\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:342"
  ]
}
```

### "cards"."XCL_033" = 1

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_033\" = 1",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN \"XCL_034\" = 0 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"XCL_001\") FROM cards WHERE \"XCL_033\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:402"
  ]
}
```

### The value of the 'XCL_049' column from the 'cards' table for the single record with the highest 'XCL_011' value, filtered to cards belonging to the se

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Journey into Nyx Hero''s Path' ORDER BY T1.\"XCL_011\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:501"
  ]
}
```

### The value of column XCL_077 from the foreign_data table, filtered to rows where XCL_078 equals 149934.

```json
{
  "kind": "binding",
  "formula": "\"foreign_data\".\"XCL_077\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_077\" FROM foreign_data WHERE \"XCL_078\" = 149934",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_077\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "foreign_data"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_077\" AS \"value\" FROM foreign_data AS \"r0\" WHERE \"r0\".\"XCL_078\" = 149934",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:422"
  ]
}
```

### Aggregates the total number of card records (identified by XCL_001) that are classified as 'white' (XCL_005) and have a legality status of 'Banned' (X

```json
{
  "kind": "metric",
  "formula": "COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T2.\"XCL_085\" = 'Banned' AND T1.\"XCL_005\" = 'white'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "legalities"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" INNER JOIN legalities AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_086\" WHERE \"r1\".\"XCL_085\" = 'Banned' AND \"r0\".\"XCL_005\" = 'white'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:383"
  ]
}
```

### "cards"."XCL_049" = 'Abyssal Horror'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Abyssal Horror'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T1.\"XCL_011\" = 10 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\"), T1.\"XCL_049\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Abyssal Horror'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:446"
  ]
}
```

### "sets"."XCL_110" = 'Tenth Edition' AND NOT "set_translations"."XCL_094" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_110\" = 'Tenth Edition' AND NOT \"set_translations\".\"XCL_094\" IS NULL",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T2.\"XCL_094\") FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_110\" = 'Tenth Edition' AND NOT T2.\"XCL_094\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:499"
  ]
}
```

### "set_translations"."XCL_094" = 'Hauptset Zehnte Edition' AND "cards"."XCL_002" = 'Adam Rex'

```json
{
  "kind": "predicate",
  "formula": "\"set_translations\".\"XCL_094\" = 'Hauptset Zehnte Edition' AND \"cards\".\"XCL_002\" = 'Adam Rex'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_063\" WHERE T2.\"XCL_094\" = 'Hauptset Zehnte Edition' AND T1.\"XCL_002\" = 'Adam Rex'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:466"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_011\" = 0",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_011\" = 0",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:375"
  ]
}
```

### Identifier from the 'set_translations' table (T2), representing the specific translation record. It is part of the output grain and is filtered by lan

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_094\"",
  "grain": [
    "\"sets\".\"XCL_110\"",
    "\"set_translations\".\"XCL_094\""
  ],
  "population_scope": "SELECT T1.\"XCL_110\", T2.\"XCL_094\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_091\" = 5 GROUP BY T1.\"XCL_110\", T2.\"XCL_094\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_094\"",
    "grain": [
      "\"r0\".\"XCL_110\"",
      "\"r1\".\"XCL_094\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_110\" AS \"grain_0\", \"r1\".\"XCL_094\" AS \"grain_1\", \"r1\".\"XCL_094\" AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r0\".\"XCL_099\" = \"r1\".\"XCL_093\" WHERE \"r1\".\"XCL_091\" = 5 GROUP BY \"r0\".\"XCL_110\", \"r1\".\"XCL_094\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:428"
  ]
}
```

### Aggregates the total number of rows in the 'sets' table that satisfy the join and filter conditions. The grain is a single scalar value representing t

```json
{
  "kind": "metric",
  "formula": "COUNT(\"sets\".\"XCL_095\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_095\") FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_092\" = 'Portuguese (Brazil)' AND T1.\"XCL_097\" = 'Commander'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_095\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_095\") AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r0\".\"XCL_099\" = \"r1\".\"XCL_093\" WHERE \"r1\".\"XCL_092\" = 'Portuguese (Brazil)' AND \"r0\".\"XCL_097\" = 'Commander'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:405"
  ]
}
```

### Set Identifier

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_111\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_111\" FROM sets WHERE \"XCL_110\" = 'Commander 2014 Oversized'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_111\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_111\" AS \"value\" FROM sets AS \"r0\" WHERE \"r0\".\"XCL_110\" = 'Commander 2014 Oversized'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:493"
  ]
}
```

### Aggregates the count of card records (cards.XCL_001) that satisfy specific rarity, type, name, and legality constraints. The population is restricted 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T2.\"XCL_086\" = T1.\"XCL_072\" WHERE T1.\"XCL_059\" = 'rare' AND T1.\"XCL_071\" = 'Enchantment' AND T1.\"XCL_049\" = 'Abundance' AND T2.\"XCL_085\" = 'Legal'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "legalities"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" INNER JOIN legalities AS \"r1\" ON \"r1\".\"XCL_086\" = \"r0\".\"XCL_072\" WHERE \"r0\".\"XCL_059\" = 'rare' AND \"r0\".\"XCL_071\" = 'Enchantment' AND \"r0\".\"XCL_049\" = 'Abundance' AND \"r1\".\"XCL_085\" = 'Legal'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:517"
  ]
}
```

### Aggregates the number of rows in the 'cards' table where the field 'XCL_055' is either the literal string '*' or NULL. This metric is calculated withi

```json
{
  "kind": "metric",
  "formula": "SUM(CASE WHEN \"cards\".\"XCL_055\" = '*' OR \"cards\".\"XCL_055\" IS NULL THEN 1 ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN \"XCL_055\" = '*' OR \"XCL_055\" IS NULL THEN 1 ELSE 0 END) FROM cards WHERE \"XCL_023\" = 0 AND \"XCL_012\" = 'a'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(CASE WHEN \"r0\".\"XCL_055\" = '*' OR \"r0\".\"XCL_055\" IS NULL THEN 1 ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT SUM(CASE WHEN \"r0\".\"XCL_055\" = '*' OR \"r0\".\"XCL_055\" IS NULL THEN 1 ELSE 0 END) AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_023\" = 0 AND \"r0\".\"XCL_012\" = 'a'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:512"
  ]
}
```

### Set Identifier

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_096\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_096\", T2.\"XCL_093\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_097\" IN ('Masques', 'Mirage')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:442"
  ]
}
```

### Aggregates the count of non-null values in the 'XCL_095' column from the 'sets' table. The population is restricted to sets that have an associated re

```json
{
  "kind": "metric",
  "formula": "COUNT(\"sets\".\"XCL_095\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_095\") FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T2.\"XCL_092\" = 'Japanese' AND (T1.\"XCL_109\" IS NULL OR T1.\"XCL_109\" = '')",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_095\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_095\") AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r1\".\"XCL_093\" = \"r0\".\"XCL_099\" WHERE \"r1\".\"XCL_092\" = 'Japanese' AND (\"r0\".\"XCL_109\" IS NULL OR \"r0\".\"XCL_109\" = '')",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:434"
  ]
}
```

### Count of unique card identifiers (XCL_001) from the cards table, filtered by rarity 'rare' and joined to rulings dated '2007-02-01'.

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_001\") FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_059\" = 'rare' AND T2.\"XCL_088\" = '2007-02-01'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "rulings"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" INNER JOIN rulings AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_090\" WHERE \"r0\".\"XCL_059\" = 'rare' AND \"r1\".\"XCL_088\" = '2007-02-01'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:413"
  ]
}
```

### Calculates the percentage of cards where the attribute XCL_011 is 7, relative to the total count of cards (XCL_001), within the filtered population.

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"cards\".\"XCL_011\" = 7 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T1.\"XCL_011\" = 7 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Coldsnap'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r0\".\"XCL_011\" = 7 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r0\".\"XCL_011\" = 7 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" INNER JOIN sets AS \"r1\" ON \"r1\".\"XCL_099\" = \"r0\".\"XCL_063\" WHERE \"r1\".\"XCL_110\" = 'Coldsnap'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:486"
  ]
}
```

### Returns the value of column XCL_094 from the set_translations table. The population is restricted to records where the associated set (via XCL_093 = X

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_094\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_094\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_110\" = 'Eighth Edition' AND T2.\"XCL_092\" = 'Chinese Simplified'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_094\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_094\" AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r1\".\"XCL_093\" = \"r0\".\"XCL_099\" WHERE \"r0\".\"XCL_110\" = 'Eighth Edition' AND \"r1\".\"XCL_092\" = 'Chinese Simplified'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:468"
  ]
}
```

### "foreign_data"."XCL_078" = 149934

```json
{
  "kind": "predicate",
  "formula": "\"foreign_data\".\"XCL_078\" = 149934",
  "grain": [],
  "population_scope": "SELECT \"XCL_077\" FROM foreign_data WHERE \"XCL_078\" = 149934",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:422"
  ]
}
```

### Card ID for 'Ancestor's Chosen'

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_063\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_063\" FROM cards WHERE \"XCL_049\" = 'Ancestor''s Chosen'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_063\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_063\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_049\" = 'Ancestor''s Chosen'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:462"
  ]
}
```

### "cards"."XCL_049" = 'Ancestor''s Chosen'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Ancestor''s Chosen'",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_041\" FROM cards WHERE \"XCL_049\" = 'Ancestor''s Chosen'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:453"
  ]
}
```

### Ruling Identifier

```json
{
  "kind": "binding",
  "formula": "\"rulings\".\"XCL_089\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_089\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T2.\"XCL_090\" = T1.\"XCL_072\" WHERE T1.\"XCL_002\" = 'Kev Walker' ORDER BY T2.\"XCL_088\" DESC",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_089\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "rulings"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_089\" AS \"value\" FROM cards AS \"r0\" INNER JOIN rulings AS \"r1\" ON \"r1\".\"XCL_090\" = \"r0\".\"XCL_072\" WHERE \"r0\".\"XCL_002\" = 'Kev Walker'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:527"
  ]
}
```

### Oldschool Banned or Restricted Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"legalities\".\"XCL_086\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_086\" FROM legalities WHERE \"XCL_084\" = 'oldschool' AND (\"XCL_085\" = 'Banned' OR \"XCL_085\" = 'Restricted')",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_086\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "legalities"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_086\" AS \"value\" FROM legalities AS \"r0\" WHERE \"r0\".\"XCL_084\" = 'oldschool' AND (\"r0\".\"XCL_085\" = 'Banned' OR \"r0\".\"XCL_085\" = 'Restricted')",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:525"
  ]
}
```

### "cards"."XCL_002" = 'Kev Walker'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_002\" = 'Kev Walker'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_089\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T2.\"XCL_090\" = T1.\"XCL_072\" WHERE T1.\"XCL_002\" = 'Kev Walker' ORDER BY T2.\"XCL_088\" DESC",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:527"
  ]
}
```

### Identifier from the 'sets' table (T1) for sets that have an Italian translation. Grain: one row per set with an Italian translation.

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_110\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_110\", T1.\"XCL_114\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_092\" = 'Italian'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_110\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_110\" AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r0\".\"XCL_099\" = \"r1\".\"XCL_093\" WHERE \"r1\".\"XCL_092\" = 'Italian'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:353"
  ]
}
```

### Aggregates the number of rows in the 'cards' table where the 'XCL_055' field contains an asterisk ('*') or is null, restricted to records where 'XCL_0

```json
{
  "kind": "metric",
  "formula": "SUM(CASE WHEN \"cards\".\"XCL_055\" LIKE '%*%' OR \"cards\".\"XCL_055\" IS NULL THEN 1 ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN \"XCL_055\" LIKE '%*%' OR \"XCL_055\" IS NULL THEN 1 ELSE 0 END) FROM cards WHERE \"XCL_005\" = 'white'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(CASE WHEN \"r0\".\"XCL_055\" LIKE '%*%' OR \"r0\".\"XCL_055\" IS NULL THEN 1 ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT SUM(CASE WHEN \"r0\".\"XCL_055\" LIKE '%*%' OR \"r0\".\"XCL_055\" IS NULL THEN 1 ELSE 0 END) AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_005\" = 'white'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:454"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_049\" FROM foreign_data AS T1 INNER JOIN cards AS T2 ON T2.\"XCL_072\" = T1.\"XCL_082\" INNER JOIN sets AS T3 ON T3.\"XCL_099\" = T2.\"XCL_063\" WHERE T3.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_077\" = 'Italian' ORDER BY T2.\"XCL_011\" DESC",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_049\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "foreign_data"
      },
      {
        "role": "r1",
        "physical_table": "cards"
      },
      {
        "role": "r2",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_049\" AS \"value\" FROM foreign_data AS \"r0\" INNER JOIN cards AS \"r1\" ON \"r1\".\"XCL_072\" = \"r0\".\"XCL_082\" INNER JOIN sets AS \"r2\" ON \"r2\".\"XCL_099\" = \"r1\".\"XCL_063\" WHERE \"r2\".\"XCL_110\" = 'Coldsnap' AND \"r0\".\"XCL_077\" = 'Italian'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:484"
  ]
}
```

### Card ID for Card Number 5

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_011\" = 5",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_011\" = 5",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:388"
  ]
}
```

### Returns the value of column XCL_110 from the sets table for rows where XCL_099 is 'ALL'. Grain is individual matching rows.

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_110\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_110\" FROM sets WHERE \"XCL_099\" = 'ALL'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_110\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_110\" AS \"value\" FROM sets AS \"r0\" WHERE \"r0\".\"XCL_099\" = 'ALL'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:439"
  ]
}
```

### "cards"."XCL_013" = 1 AND "legalities"."XCL_085" = 'Banned'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_013\" = 1 AND \"legalities\".\"XCL_085\" = 'Banned'",
  "grain": [
    "\"cards\".\"XCL_049\"",
    "\"legalities\".\"XCL_084\""
  ],
  "population_scope": "SELECT T1.\"XCL_049\", T2.\"XCL_084\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T2.\"XCL_086\" = T1.\"XCL_072\" WHERE T1.\"XCL_013\" = 1 AND T2.\"XCL_085\" = 'Banned' GROUP BY T1.\"XCL_049\", T2.\"XCL_084\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:522"
  ]
}
```

### Card Attribute XCL_066

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_066\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_065\", T1.\"XCL_066\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T2.\"XCL_077\" = 'German' AND NOT T1.\"XCL_065\" IS NULL AND NOT T1.\"XCL_066\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_066\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "foreign_data"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_066\" AS \"value\" FROM cards AS \"r0\" INNER JOIN foreign_data AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_082\" WHERE \"r1\".\"XCL_077\" = 'German' AND NOT \"r0\".\"XCL_065\" IS NULL AND NOT \"r0\".\"XCL_066\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:407"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_002\"",
  "grain": [
    "\"cards\".\"XCL_002\""
  ],
  "population_scope": "SELECT T1.\"XCL_002\", T2.\"XCL_084\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T2.\"XCL_086\" = T1.\"XCL_072\" GROUP BY T1.\"XCL_002\" ORDER BY COUNT(T1.\"XCL_001\") ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:520"
  ]
}
```

### Extracts the set identifier (XCL_093) from the set_translations table where the language code (XCL_092) is 'Portuguese (Brazil)'. This serves as the f

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_093\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_093\" FROM set_translations WHERE \"XCL_092\" = 'Portuguese (Brazil)'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_093\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_093\" AS \"value\" FROM set_translations AS \"r0\" WHERE \"r0\".\"XCL_092\" = 'Portuguese (Brazil)'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:507"
  ]
}
```

### Retrieves the `XCL_092` value from the `set_translations` table. This column is joined to the `sets` table via `XCL_091` and is used in the ordering l

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_092\"",
  "grain": [
    "\"sets\".\"XCL_112\""
  ],
  "population_scope": "SELECT (CAST(SUM(T1.\"XCL_095\") AS REAL) / COUNT(T1.\"XCL_095\")) / 4, T2.\"XCL_092\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_095\" = T2.\"XCL_091\" WHERE T1.\"XCL_112\" BETWEEN '2012-01-01' AND '2015-12-31' GROUP BY T1.\"XCL_112\" ORDER BY COUNT(T2.\"XCL_092\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:523"
  ]
}
```

### "sets"."XCL_110" = 'Hour of Devastation'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_110\" = 'Hour of Devastation'",
  "grain": [],
  "population_scope": "SELECT \"XCL_099\" FROM sets WHERE \"XCL_110\" = 'Hour of Devastation'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:528"
  ]
}
```

### Aggregates the total number of rows in the 'cards' table where the value in column 'XCL_002' is 'Aaron Miller' and both columns 'XCL_006' and 'XCL_007

```json
{
  "kind": "metric",
  "formula": "SUM(CASE WHEN \"cards\".\"XCL_002\" = 'Aaron Miller' AND NOT \"cards\".\"XCL_006\" IS NULL AND NOT \"cards\".\"XCL_007\" IS NULL THEN 1 ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN \"XCL_002\" = 'Aaron Miller' AND NOT \"XCL_006\" IS NULL AND NOT \"XCL_007\" IS NULL THEN 1 ELSE 0 END) FROM cards",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(CASE WHEN \"r0\".\"XCL_002\" = 'Aaron Miller' AND NOT \"r0\".\"XCL_006\" IS NULL AND NOT \"r0\".\"XCL_007\" IS NULL THEN 1 ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT SUM(CASE WHEN \"r0\".\"XCL_002\" = 'Aaron Miller' AND NOT \"r0\".\"XCL_006\" IS NULL AND NOT \"r0\".\"XCL_007\" IS NULL THEN 1 ELSE 0 END) AS \"value\" FROM cards AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:450"
  ]
}
```

### "cards"."XCL_002" = 'Matthew D. Wilson' AND "cards"."XCL_004" = 'paper'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_002\" = 'Matthew D. Wilson' AND \"cards\".\"XCL_004\" = 'paper'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_002\" = 'Matthew D. Wilson' AND \"XCL_004\" = 'paper'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:526"
  ]
}
```

### Ruling Text

```json
{
  "kind": "binding",
  "formula": "\"rulings\".\"XCL_089\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_089\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_049\" = 'Beacon of Immortality'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_089\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "rulings"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_089\" AS \"value\" FROM cards AS \"r0\" INNER JOIN rulings AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_090\" WHERE \"r0\".\"XCL_049\" = 'Beacon of Immortality'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:385"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_013\" < 100 AND \"XCL_019\" = 2015",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_013\" < 100 AND \"r0\".\"XCL_019\" = 2015",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:343"
  ]
}
```

### Returns the value of column XCL_105 from the sets table for rows where XCL_099 equals 'PKHC'. Grain is individual matching rows.

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_105\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_105\" FROM sets WHERE \"XCL_099\" = 'PKHC'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_105\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_105\" AS \"value\" FROM sets AS \"r0\" WHERE \"r0\".\"XCL_099\" = 'PKHC'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:489"
  ]
}
```

### Aggregates the total number of card records (count of XCL_001) from the cards table, filtered to a specific artist (XCL_002 = 'Adam Rex') and a specif

```json
{
  "kind": "metric",
  "formula": "COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_063\" WHERE T2.\"XCL_094\" = 'Hauptset Zehnte Edition' AND T1.\"XCL_002\" = 'Adam Rex'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r1\".\"XCL_093\" = \"r0\".\"XCL_063\" WHERE \"r1\".\"XCL_094\" = 'Hauptset Zehnte Edition' AND \"r0\".\"XCL_002\" = 'Adam Rex'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:466"
  ]
}
```

### Foreign Data Attribute XCL_077

```json
{
  "kind": "binding",
  "formula": "\"foreign_data\".\"XCL_077\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_077\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_049\" = 'Ancestor''s Chosen' AND NOT T2.\"XCL_076\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_077\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "foreign_data"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_077\" AS \"value\" FROM cards AS \"r0\" INNER JOIN foreign_data AS \"r1\" ON \"r1\".\"XCL_082\" = \"r0\".\"XCL_072\" WHERE \"r0\".\"XCL_049\" = 'Ancestor''s Chosen' AND NOT \"r1\".\"XCL_076\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:481"
  ]
}
```

### Legality Status

```json
{
  "kind": "binding",
  "formula": "\"legalities\".\"XCL_084\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_084\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_049\" = 'Benalish Knight'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_084\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "legalities"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_084\" AS \"value\" FROM cards AS \"r0\" INNER JOIN legalities AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_086\" WHERE \"r0\".\"XCL_049\" = 'Benalish Knight'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:366"
  ]
}
```

### Japanese Set Translation

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_094\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_094\" FROM cards AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Fellwar Stone' AND T2.\"XCL_092\" = 'Japanese' AND NOT T2.\"XCL_094\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_094\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_094\" AS \"value\" FROM cards AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r1\".\"XCL_093\" = \"r0\".\"XCL_063\" WHERE \"r0\".\"XCL_049\" = 'Fellwar Stone' AND \"r1\".\"XCL_092\" = 'Japanese' AND NOT \"r1\".\"XCL_094\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:500"
  ]
}
```

### Distinct Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_053\" = 'Artifact' AND T1.\"XCL_010\" = 'B'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:391"
  ]
}
```

### Calculates the percentage of rows where the column XCL_022 in the cards table is 0, relative to the total count of rows in the cards table, within the

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"cards\".\"XCL_022\" = 0 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T1.\"XCL_022\" = 0 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T2.\"XCL_084\" = 'commander' AND T2.\"XCL_085\" = 'Legal'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r0\".\"XCL_022\" = 0 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "legalities"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r0\".\"XCL_022\" = 0 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" INNER JOIN legalities AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_086\" WHERE \"r1\".\"XCL_084\" = 'commander' AND \"r1\".\"XCL_085\" = 'Legal'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:415"
  ]
}
```

### Set Identifier

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_096\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_096\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T2.\"XCL_094\" = 'Hauptset Zehnte Edition'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_096\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_096\" AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r1\".\"XCL_093\" = \"r0\".\"XCL_099\" WHERE \"r1\".\"XCL_094\" = 'Hauptset Zehnte Edition'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:467"
  ]
}
```

### Foreign Data Attribute XCL_077

```json
{
  "kind": "binding",
  "formula": "\"foreign_data\".\"XCL_077\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_077\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_049\" = 'Annul' AND T1.\"XCL_050\" = 29",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_077\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "foreign_data"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_077\" AS \"value\" FROM cards AS \"r0\" INNER JOIN foreign_data AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_082\" WHERE \"r0\".\"XCL_049\" = 'Annul' AND \"r0\".\"XCL_050\" = 29",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:350"
  ]
}
```

### "sets"."XCL_110" = 'Journey into Nyx Hero''s Path'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_110\" = 'Journey into Nyx Hero''s Path'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Journey into Nyx Hero''s Path' ORDER BY T1.\"XCL_011\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:501"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_036\" FROM cards WHERE \"XCL_049\" = 'Angel of Mercy'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:355"
  ]
}
```

### Card Legality Identifier

```json
{
  "kind": "binding",
  "formula": "\"legalities\".\"XCL_085\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_085\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_049\" = 'Cloudchaser Eagle'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:364"
  ]
}
```

### "legalities"."XCL_085" = 'Banned'

```json
{
  "kind": "predicate",
  "formula": "\"legalities\".\"XCL_085\" = 'Banned'",
  "grain": [
    "\"legalities\".\"XCL_084\""
  ],
  "population_scope": "SELECT \"XCL_084\", COUNT(*) AS count_banned FROM legalities WHERE \"XCL_085\" = 'Banned' GROUP BY \"XCL_084\" ORDER BY COUNT(*) DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:518"
  ]
}
```

### Set Identifier

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_110\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_110\" FROM sets WHERE \"XCL_099\" IN (SELECT \"XCL_093\" FROM set_translations WHERE \"XCL_092\" = 'Korean' AND \"XCL_092\" NOT LIKE '%Japanese%')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:529"
  ]
}
```

### "legalities"."XCL_084" = 'commander' AND "legalities"."XCL_085" = 'Legal'

```json
{
  "kind": "predicate",
  "formula": "\"legalities\".\"XCL_084\" = 'commander' AND \"legalities\".\"XCL_085\" = 'Legal'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T1.\"XCL_022\" = 0 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T2.\"XCL_084\" = 'commander' AND T2.\"XCL_085\" = 'Legal'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:415"
  ]
}
```

### "cards"."XCL_034" = 0

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_034\" = 0",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_049\" FROM cards WHERE \"XCL_034\" = 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:452"
  ]
}
```

### "sets"."XCL_110" = 'Coldsnap' AND "cards"."XCL_011" > 5

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_110\" = 'Coldsnap' AND \"cards\".\"XCL_011\" > 5",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN T1.\"XCL_055\" LIKE '*' OR T1.\"XCL_055\" IS NULL THEN 1 ELSE 0 END) FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_011\" > 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:479"
  ]
}
```

### "cards"."XCL_018" = 'legendary'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_018\" = 'legendary'",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN \"XCL_027\" = 1 THEN 1.0 ELSE 0 END) / COUNT(\"XCL_001\") * 100 FROM cards WHERE \"XCL_018\" = 'legendary'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:401"
  ]
}
```

### Filtered Card ID

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_072\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_072\" FROM cards WHERE \"XCL_071\" = 'Creature' AND \"XCL_037\" = 'normal' AND \"XCL_005\" = 'black' AND \"XCL_002\" = 'Matthew D. Wilson'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_072\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_072\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_071\" = 'Creature' AND \"r0\".\"XCL_037\" = 'normal' AND \"r0\".\"XCL_005\" = 'black' AND \"r0\".\"XCL_002\" = 'Matthew D. Wilson'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:412"
  ]
}
```

### "sets"."XCL_112" = '2017-07-14'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_112\" = '2017-07-14'",
  "grain": [
    "\"sets\".\"XCL_112\"",
    "\"sets\".\"XCL_099\""
  ],
  "population_scope": "SELECT \"XCL_099\" FROM sets WHERE \"XCL_112\" = '2017-07-14' GROUP BY \"XCL_112\", \"XCL_099\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:488"
  ]
}
```

### Identifier for the trading card game set, retrieved from the 'sets' table. In this context, it is filtered to the set named 'Shadowmoor'.

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_110\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_110\", T1.\"XCL_095\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T1.\"XCL_097\" = 'Shadowmoor' AND T2.\"XCL_092\" = 'Italian' ORDER BY T1.\"XCL_095\" LIMIT 2",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:430"
  ]
}
```

### "cards"."XCL_013" < 100 AND "cards"."XCL_019" = 2015

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_013\" < 100 AND \"cards\".\"XCL_019\" = 2015",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_013\" < 100 AND \"XCL_019\" = 2015",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:343"
  ]
}
```

### Aggregates the count of card identifiers (XCL_001) from the cards table. The population is restricted to cards that are legal in the 'premodern' forma

```json
{
  "kind": "metric",
  "formula": "COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" INNER JOIN rulings AS T3 ON T1.\"XCL_072\" = T3.\"XCL_090\" WHERE T2.\"XCL_084\" = 'premodern' AND T3.\"XCL_089\" = 'This is a triggered mana ability.' AND T1.\"XCL_064\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "legalities"
      },
      {
        "role": "r2",
        "physical_table": "rulings"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" INNER JOIN legalities AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_086\" INNER JOIN rulings AS \"r2\" ON \"r0\".\"XCL_072\" = \"r2\".\"XCL_090\" WHERE \"r1\".\"XCL_084\" = 'premodern' AND \"r2\".\"XCL_089\" = 'This is a triggered mana ability.' AND \"r0\".\"XCL_064\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:409"
  ]
}
```

### "legalities"."XCL_085" = 'Legal' AND "legalities"."XCL_084" = 'commander' AND ("cards"."XCL_055" IS NULL OR "cards"."XCL_055" = '*')

```json
{
  "kind": "predicate",
  "formula": "\"legalities\".\"XCL_085\" = 'Legal' AND \"legalities\".\"XCL_084\" = 'commander' AND (\"cards\".\"XCL_055\" IS NULL OR \"cards\".\"XCL_055\" = '*')",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T1.\"XCL_002\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T2.\"XCL_085\" = 'Legal' AND T2.\"XCL_084\" = 'commander' AND (T1.\"XCL_055\" IS NULL OR T1.\"XCL_055\" = '*')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:346"
  ]
}
```

### "cards"."XCL_019" = 2003

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_019\" = 2003",
  "grain": [],
  "population_scope": "SELECT \"XCL_049\" FROM cards WHERE \"XCL_019\" = 2003 ORDER BY \"XCL_011\" DESC LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:461"
  ]
}
```

### French Foreign Data Value

```json
{
  "kind": "binding",
  "formula": "\"foreign_data\".\"XCL_079\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_079\" FROM foreign_data WHERE \"XCL_082\" IN (SELECT \"XCL_072\" FROM cards WHERE \"XCL_071\" = 'Creature' AND \"XCL_037\" = 'normal' AND \"XCL_005\" = 'black' AND \"XCL_002\" = 'Matthew D. Wilson') AND \"XCL_077\" = 'French'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:412"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_049\", T1.\"XCL_070\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_074\" = 'abzan'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:448"
  ]
}
```

### Format Identifier

```json
{
  "kind": "binding",
  "formula": "\"legalities\".\"XCL_084\"",
  "grain": [
    "\"cards\".\"XCL_049\"",
    "\"legalities\".\"XCL_084\""
  ],
  "population_scope": "SELECT T1.\"XCL_049\", T2.\"XCL_084\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T2.\"XCL_086\" = T1.\"XCL_072\" WHERE T1.\"XCL_013\" = 1 AND T2.\"XCL_085\" = 'Banned' GROUP BY T1.\"XCL_049\", T2.\"XCL_084\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_084\"",
    "grain": [
      "\"r0\".\"XCL_049\"",
      "\"r1\".\"XCL_084\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "legalities"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_049\" AS \"grain_0\", \"r1\".\"XCL_084\" AS \"grain_1\", \"r1\".\"XCL_084\" AS \"value\" FROM cards AS \"r0\" INNER JOIN legalities AS \"r1\" ON \"r1\".\"XCL_086\" = \"r0\".\"XCL_072\" WHERE \"r0\".\"XCL_013\" = 1 AND \"r1\".\"XCL_085\" = 'Banned' GROUP BY \"r0\".\"XCL_049\", \"r1\".\"XCL_084\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:522"
  ]
}
```

### Legal Format Name

```json
{
  "kind": "binding",
  "formula": "CASE WHEN \"legalities\".\"XCL_085\" = 'Legal' THEN \"legalities\".\"XCL_084\" ELSE NULL END",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_049\", CASE WHEN T1.\"XCL_085\" = 'Legal' THEN T1.\"XCL_084\" ELSE NULL END FROM legalities AS T1 INNER JOIN cards AS T2 ON T2.\"XCL_072\" = T1.\"XCL_086\" WHERE T2.\"XCL_063\" IN (SELECT \"XCL_099\" FROM sets WHERE \"XCL_110\" = 'Hour of Devastation')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:528"
  ]
}
```

### "cards"."XCL_005" = 'black' AND "cards"."XCL_026" = 1

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_005\" = 'black' AND \"cards\".\"XCL_026\" = 1",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_005\" = 'black' AND \"XCL_026\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:437"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_041\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_041\" FROM cards WHERE \"XCL_004\" = 'mtgo,paper' AND \"XCL_005\" = 'black' AND \"XCL_019\" = 2003 AND \"XCL_037\" = 'normal'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_041\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_041\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_004\" = 'mtgo,paper' AND \"r0\".\"XCL_005\" = 'black' AND \"r0\".\"XCL_019\" = 2003 AND \"r0\".\"XCL_037\" = 'normal'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:397"
  ]
}
```

### Identifier from the 'sets' table (T1), representing the primary set entity. It is part of the output grain and is joined to translations via XCL_099.

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_110\"",
  "grain": [
    "\"sets\".\"XCL_110\"",
    "\"set_translations\".\"XCL_094\""
  ],
  "population_scope": "SELECT T1.\"XCL_110\", T2.\"XCL_094\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_091\" = 5 GROUP BY T1.\"XCL_110\", T2.\"XCL_094\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_110\"",
    "grain": [
      "\"r0\".\"XCL_110\"",
      "\"r1\".\"XCL_094\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_110\" AS \"grain_0\", \"r1\".\"XCL_094\" AS \"grain_1\", \"r0\".\"XCL_110\" AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r0\".\"XCL_099\" = \"r1\".\"XCL_093\" WHERE \"r1\".\"XCL_091\" = 5 GROUP BY \"r0\".\"XCL_110\", \"r1\".\"XCL_094\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:428"
  ]
}
```

### Set Translation Value

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_092\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_092\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T1.\"XCL_108\" = 'Archenemy' AND T2.\"XCL_093\" = 'ARC'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_092\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_092\" AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r0\".\"XCL_099\" = \"r1\".\"XCL_093\" WHERE \"r0\".\"XCL_108\" = 'Archenemy' AND \"r1\".\"XCL_093\" = 'ARC'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:427"
  ]
}
```

### Aggregates the total number of rows from the 'cards' table (T1) that satisfy the condition T1."XCL_030" = 1 and are joined to the 'foreign_data' table

```json
{
  "kind": "metric",
  "formula": "COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T2.\"XCL_077\" = 'German' AND T1.\"XCL_030\" = 1",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "foreign_data"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" INNER JOIN foreign_data AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_082\" WHERE \"r1\".\"XCL_077\" = 'German' AND \"r0\".\"XCL_030\" = 1",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:369"
  ]
}
```

### "cards"."XCL_049" = 'Annul' AND "cards"."XCL_050" = 29

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Annul' AND \"cards\".\"XCL_050\" = 29",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_077\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_049\" = 'Annul' AND T1.\"XCL_050\" = 29",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:350"
  ]
}
```

### "cards"."XCL_059" = 'rare' AND "cards"."XCL_071" = 'Enchantment' AND "cards"."XCL_049" = 'Abundance' AND "legalities"."XCL_085" = 'Legal'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_059\" = 'rare' AND \"cards\".\"XCL_071\" = 'Enchantment' AND \"cards\".\"XCL_049\" = 'Abundance' AND \"legalities\".\"XCL_085\" = 'Legal'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T2.\"XCL_086\" = T1.\"XCL_072\" WHERE T1.\"XCL_059\" = 'rare' AND T1.\"XCL_071\" = 'Enchantment' AND T1.\"XCL_049\" = 'Abundance' AND T2.\"XCL_085\" = 'Legal'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:517"
  ]
}
```

### Ruling Text

```json
{
  "kind": "binding",
  "formula": "\"rulings\".\"XCL_089\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_089\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_049\" = 'Condemn'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_089\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "rulings"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_089\" AS \"value\" FROM cards AS \"r0\" INNER JOIN rulings AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_090\" WHERE \"r0\".\"XCL_049\" = 'Condemn'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:362"
  ]
}
```

### "cards"."XCL_049" = 'Reminisce'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Reminisce'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_088\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T2.\"XCL_090\" = T1.\"XCL_072\" WHERE T1.\"XCL_049\" = 'Reminisce'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:485"
  ]
}
```

### Distinct XCL_004 values

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_004\" FROM cards WHERE \"XCL_002\" = 'Aleksi Briclot' AND \"XCL_034\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:508"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_051\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_051\", T2.\"XCL_084\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_059\" = 'mythic' AND NOT T1.\"XCL_051\" IS NULL AND T2.\"XCL_085\" = 'Legal' ORDER BY T1.\"XCL_051\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:515"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_059\" = 'uncommon' ORDER BY T2.\"XCL_088\" ASC LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:392"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_005\" = 'borderless' AND (\"XCL_007\" IS NULL OR \"XCL_007\" IS NULL)",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_005\" = 'borderless' AND (\"r0\".\"XCL_007\" IS NULL OR \"r0\".\"XCL_007\" IS NULL)",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:341"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_041\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_041\" FROM cards WHERE \"XCL_049\" = 'Ancestor''s Chosen'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:453"
  ]
}
```

### "cards"."XCL_005" = 'borderless' AND "foreign_data"."XCL_077" = 'Russian'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_005\" = 'borderless' AND \"foreign_data\".\"XCL_077\" = 'Russian'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_005\" = 'borderless' AND T2.\"XCL_077\" = 'Russian'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:370"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_002\" FROM cards WHERE \"XCL_016\" = 'Battra, Dark Destroyer'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_002\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_002\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_016\" = 'Battra, Dark Destroyer'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:460"
  ]
}
```

### "cards"."XCL_002" = 'Rob Alexander'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_002\" = 'Rob Alexander'",
  "grain": [],
  "population_scope": "SELECT \"XCL_041\" FROM cards WHERE \"XCL_002\" = 'Rob Alexander'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:398"
  ]
}
```

### "cards"."XCL_005" = 'borderless' AND ("cards"."XCL_007" IS NULL OR "cards"."XCL_007" IS NULL)

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_005\" = 'borderless' AND (\"cards\".\"XCL_007\" IS NULL OR \"cards\".\"XCL_007\" IS NULL)",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_005\" = 'borderless' AND (\"XCL_007\" IS NULL OR \"XCL_007\" IS NULL)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:341"
  ]
}
```

### "cards"."XCL_049" = 'Evacuation'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Evacuation'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_112\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Evacuation'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:495"
  ]
}
```

### Count of Banned Cards

```json
{
  "kind": "metric",
  "formula": "COUNT(*)",
  "grain": [
    "\"legalities\".\"XCL_084\""
  ],
  "population_scope": "SELECT \"XCL_084\", COUNT(*) AS count_banned FROM legalities WHERE \"XCL_085\" = 'Banned' GROUP BY \"XCL_084\" ORDER BY COUNT(*) DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:518"
  ]
}
```

### Aggregates the total number of rows in the 'cards' table where the columns 'XCL_028', 'XCL_030', and 'XCL_029' all equal 1. The grain is a single scal

```json
{
  "kind": "metric",
  "formula": "COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_028\" = 1 AND \"XCL_030\" = 1 AND \"XCL_029\" = 1",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_028\" = 1 AND \"r0\".\"XCL_030\" = 1 AND \"r0\".\"XCL_029\" = 1",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:420"
  ]
}
```

### Legality Identifier

```json
{
  "kind": "binding",
  "formula": "\"legalities\".\"XCL_084\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_051\", T2.\"XCL_084\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_059\" = 'mythic' AND NOT T1.\"XCL_051\" IS NULL AND T2.\"XCL_085\" = 'Legal' ORDER BY T1.\"XCL_051\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:515"
  ]
}
```

### "sets"."XCL_108" = 'Archenemy' AND "set_translations"."XCL_093" = 'ARC'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_108\" = 'Archenemy' AND \"set_translations\".\"XCL_093\" = 'ARC'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_092\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T1.\"XCL_108\" = 'Archenemy' AND T2.\"XCL_093\" = 'ARC'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:427"
  ]
}
```

### "foreign_data"."XCL_077" = 'German' AND NOT "cards"."XCL_065" IS NULL AND NOT "cards"."XCL_066" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"foreign_data\".\"XCL_077\" = 'German' AND NOT \"cards\".\"XCL_065\" IS NULL AND NOT \"cards\".\"XCL_066\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_065\", T1.\"XCL_066\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T2.\"XCL_077\" = 'German' AND NOT T1.\"XCL_065\" IS NULL AND NOT T1.\"XCL_066\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:407"
  ]
}
```

### "cards"."XCL_049" = 'Benalish Knight'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Benalish Knight'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_084\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_049\" = 'Benalish Knight'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:366"
  ]
}
```

### "cards"."XCL_049" = 'Duress' AND NOT "cards"."XCL_057" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Duress' AND NOT \"cards\".\"XCL_057\" IS NULL",
  "grain": [],
  "population_scope": "SELECT \"XCL_057\" FROM cards WHERE \"XCL_049\" = 'Duress' AND NOT \"XCL_057\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:357"
  ]
}
```

### Calculates the percentage of rows in the 'cards' table where 'XCL_034' is 0, relative to the total count of 'XCL_001', filtered to rows where 'XCL_033

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"cards\".\"XCL_034\" = 0 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN \"XCL_034\" = 0 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"XCL_001\") FROM cards WHERE \"XCL_033\" = 1",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r0\".\"XCL_034\" = 0 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r0\".\"XCL_034\" = 0 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_033\" = 1",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:402"
  ]
}
```

### "cards"."XCL_016" = 'Battra, Dark Destroyer'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_016\" = 'Battra, Dark Destroyer'",
  "grain": [],
  "population_scope": "SELECT \"XCL_002\" FROM cards WHERE \"XCL_016\" = 'Battra, Dark Destroyer'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:460"
  ]
}
```

### The value of the 'XCL_049' column from the 'cards' table for the single record with the highest 'XCL_011' value among cards belonging to the 'Coldsnap

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Coldsnap' ORDER BY T1.\"XCL_011\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:476"
  ]
}
```

### Aggregates the total number of card records (identified by XCL_001) from the 'cards' table that are classified as 'borderless' (XCL_005) and have a co

```json
{
  "kind": "metric",
  "formula": "COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_005\" = 'borderless' AND T2.\"XCL_077\" = 'Russian'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "foreign_data"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" INNER JOIN foreign_data AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_082\" WHERE \"r0\".\"XCL_005\" = 'borderless' AND \"r1\".\"XCL_077\" = 'Russian'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:370"
  ]
}
```

### Set Identifier

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_112\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_112\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T2.\"XCL_094\" = 'Ola de frío'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_112\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_112\" AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r1\".\"XCL_093\" = \"r0\".\"XCL_099\" WHERE \"r1\".\"XCL_094\" = 'Ola de frío'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:502"
  ]
}
```

### "cards"."XCL_005" = 'white'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_005\" = 'white'",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN \"XCL_055\" LIKE '%*%' OR \"XCL_055\" IS NULL THEN 1 ELSE 0 END) FROM cards WHERE \"XCL_005\" = 'white'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:454"
  ]
}
```

### "foreign_data"."XCL_077" = 'Spanish'

```json
{
  "kind": "predicate",
  "formula": "\"foreign_data\".\"XCL_077\" = 'Spanish'",
  "grain": [],
  "population_scope": "SELECT (SELECT CAST(SUM(CASE WHEN \"XCL_077\" = 'Spanish' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) FROM foreign_data), \"XCL_079\" FROM foreign_data WHERE \"XCL_077\" = 'Spanish'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:403"
  ]
}
```

### Calculates the percentage of rows in the 'cards' table where the 'XCL_005' column equals 'borderless'. The numerator counts rows matching the conditio

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"cards\".\"XCL_005\" = 'borderless' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN \"XCL_005\" = 'borderless' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"XCL_001\") FROM cards",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r0\".\"XCL_005\" = 'borderless' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r0\".\"XCL_005\" = 'borderless' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:368"
  ]
}
```

### "cards"."XCL_005" = 'white' AND NOT "cards"."XCL_007" IS NULL AND NOT "cards"."XCL_006" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_005\" = 'white' AND NOT \"cards\".\"XCL_007\" IS NULL AND NOT \"cards\".\"XCL_006\" IS NULL",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_005\" = 'white' AND NOT \"XCL_007\" IS NULL AND NOT \"XCL_006\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:394"
  ]
}
```

### Card Name or Title

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_070\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_049\", T1.\"XCL_070\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_074\" = 'boros'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:444"
  ]
}
```

### "sets"."XCL_115" = 'commander'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_115\" = 'commander'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_093\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_115\" = 'commander'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:447"
  ]
}
```

### Calculates the percentage of rows where the translation language is 'Japanese' relative to the total count of set identifiers, filtered to sets of typ

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"set_translations\".\"XCL_092\" = 'Japanese' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"sets\".\"XCL_095\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_092\" = 'Japanese' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_095\") FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T1.\"XCL_115\" = 'expansion'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r1\".\"XCL_092\" = 'Japanese' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_095\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r1\".\"XCL_092\" = 'Japanese' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_095\") AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r0\".\"XCL_099\" = \"r1\".\"XCL_093\" WHERE \"r0\".\"XCL_115\" = 'expansion'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:417"
  ]
}
```

### The translated name of a Magic: The Gathering set, retrieved from the set_translations table. The grain is one row per matching set translation, filte

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_092\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_092\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T1.\"XCL_097\" = 'Ravnica' AND T1.\"XCL_096\" = 180",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_092\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_092\" AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r0\".\"XCL_099\" = \"r1\".\"XCL_093\" WHERE \"r0\".\"XCL_097\" = 'Ravnica' AND \"r0\".\"XCL_096\" = 180",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:414"
  ]
}
```

### Average Set ID Divided by 4

```json
{
  "kind": "metric",
  "formula": "(CAST(SUM(\"sets\".\"XCL_095\") AS REAL) / COUNT(\"sets\".\"XCL_095\")) / 4",
  "grain": [
    "\"sets\".\"XCL_112\""
  ],
  "population_scope": "SELECT (CAST(SUM(T1.\"XCL_095\") AS REAL) / COUNT(T1.\"XCL_095\")) / 4, T2.\"XCL_092\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_095\" = T2.\"XCL_091\" WHERE T1.\"XCL_112\" BETWEEN '2012-01-01' AND '2015-12-31' GROUP BY T1.\"XCL_112\" ORDER BY COUNT(T2.\"XCL_092\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:523"
  ]
}
```

### A specific attribute or field (XCL_010) associated with the card in the cards table. Returned alongside the card ID for cards belonging to the 'OGW' s

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_010\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\", \"XCL_010\" FROM cards WHERE \"XCL_001\" IN (SELECT \"XCL_091\" FROM set_translations WHERE \"XCL_093\" = 'OGW')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:387"
  ]
}
```

### "foreign_data"."XCL_079" = 'A Pedra Fellwar'

```json
{
  "kind": "predicate",
  "formula": "\"foreign_data\".\"XCL_079\" = 'A Pedra Fellwar'",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_077\" FROM foreign_data WHERE \"XCL_079\" = 'A Pedra Fellwar'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:440"
  ]
}
```

### "set_translations"."XCL_092" = 'Japanese' AND "sets"."XCL_100" = 1 AND "sets"."XCL_101" = 0

```json
{
  "kind": "predicate",
  "formula": "\"set_translations\".\"XCL_092\" = 'Japanese' AND \"sets\".\"XCL_100\" = 1 AND \"sets\".\"XCL_101\" = 0",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_110\", T1.\"XCL_095\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_092\" = 'Japanese' AND T1.\"XCL_100\" = 1 AND T1.\"XCL_101\" = 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:431"
  ]
}
```

### French Translation Text

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_094\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_094\" FROM cards AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Tendo Ice Bridge' AND T2.\"XCL_092\" = 'French' AND NOT T2.\"XCL_094\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_094\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_094\" AS \"value\" FROM cards AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r1\".\"XCL_093\" = \"r0\".\"XCL_063\" WHERE \"r0\".\"XCL_049\" = 'Tendo Ice Bridge' AND \"r1\".\"XCL_092\" = 'French' AND NOT \"r1\".\"XCL_094\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:498"
  ]
}
```

### Card Identifier (XCL_049)

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T2.\"XCL_077\" = 'Japanese'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_049\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "foreign_data"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_049\" AS \"value\" FROM cards AS \"r0\" INNER JOIN foreign_data AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_082\" WHERE \"r1\".\"XCL_077\" = 'Japanese'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:351"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_012\" = 'a'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_012\" = 'a'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:379"
  ]
}
```

### "cards"."XCL_029" = 1

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_029\" = 1",
  "grain": [
    "\"cards\".\"XCL_002\""
  ],
  "population_scope": "SELECT \"XCL_002\" FROM cards WHERE \"XCL_029\" = 1 GROUP BY \"XCL_002\" HAVING COUNT(DISTINCT \"XCL_072\") = (SELECT MAX(\"count_uuid\") FROM (SELECT COUNT(DISTINCT \"XCL_072\") AS count_uuid FROM cards WHERE \"XCL_029\" = 1 GROUP BY \"XCL_002\"))",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:349"
  ]
}
```

### "cards"."XCL_059" = 'uncommon'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_059\" = 'uncommon'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_059\" = 'uncommon' ORDER BY T2.\"XCL_088\" ASC LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:392"
  ]
}
```

### "set_translations"."XCL_094" = 'Ola de frío'

```json
{
  "kind": "predicate",
  "formula": "\"set_translations\".\"XCL_094\" = 'Ola de frío'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_112\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T2.\"XCL_094\" = 'Ola de frío'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:502"
  ]
}
```

### NOT "cards"."XCL_007" IS NULL AND NOT "cards"."XCL_006" IS NULL

```json
{
  "kind": "predicate",
  "formula": "NOT \"cards\".\"XCL_007\" IS NULL AND NOT \"cards\".\"XCL_006\" IS NULL",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE NOT \"XCL_007\" IS NULL AND NOT \"XCL_006\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:378"
  ]
}
```

### Card Identifier (XCL_002)

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_002\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T2.\"XCL_077\" = 'Chinese Simplified'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_002\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "foreign_data"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_002\" AS \"value\" FROM cards AS \"r0\" INNER JOIN foreign_data AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_082\" WHERE \"r1\".\"XCL_077\" = 'Chinese Simplified'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:381"
  ]
}
```

### Ruling Text

```json
{
  "kind": "binding",
  "formula": "\"rulings\".\"XCL_089\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_089\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_049\" = 'Sublime Epiphany' AND T1.\"XCL_050\" = '74s'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_089\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "rulings"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_089\" AS \"value\" FROM cards AS \"r0\" INNER JOIN rulings AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_090\" WHERE \"r0\".\"XCL_049\" = 'Sublime Epiphany' AND \"r0\".\"XCL_050\" = '74s'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:348"
  ]
}
```

### "set_translations"."XCL_091" = 174

```json
{
  "kind": "predicate",
  "formula": "\"set_translations\".\"XCL_091\" = 174",
  "grain": [],
  "population_scope": "SELECT \"XCL_092\" FROM set_translations WHERE \"XCL_091\" = 174",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:438"
  ]
}
```

### "set_translations"."XCL_091" = 5

```json
{
  "kind": "predicate",
  "formula": "\"set_translations\".\"XCL_091\" = 5",
  "grain": [
    "\"sets\".\"XCL_110\"",
    "\"set_translations\".\"XCL_094\""
  ],
  "population_scope": "SELECT T1.\"XCL_110\", T2.\"XCL_094\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_091\" = 5 GROUP BY T1.\"XCL_110\", T2.\"XCL_094\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:428"
  ]
}
```

### Distinct values of column XCL_099 from the sets table, filtered to rows where XCL_112 equals '2017-07-14'. The grain is one row per unique combination

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_099\"",
  "grain": [
    "\"sets\".\"XCL_112\"",
    "\"sets\".\"XCL_099\""
  ],
  "population_scope": "SELECT \"XCL_099\" FROM sets WHERE \"XCL_112\" = '2017-07-14' GROUP BY \"XCL_112\", \"XCL_099\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_099\"",
    "grain": [
      "\"r0\".\"XCL_112\"",
      "\"r0\".\"XCL_099\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_112\" AS \"grain_0\", \"r0\".\"XCL_099\" AS \"grain_1\", \"r0\".\"XCL_099\" AS \"value\" FROM sets AS \"r0\" WHERE \"r0\".\"XCL_112\" = '2017-07-14' GROUP BY \"r0\".\"XCL_112\", \"r0\".\"XCL_099\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:488"
  ]
}
```

### "cards"."XCL_011" = 5

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_011\" = 5",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_011\" = 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:388"
  ]
}
```

### Aggregates the total number of rows in the 'cards' table where the column 'XCL_053' equals 'Summon - Angel' and the column 'XCL_065' is not equal to '

```json
{
  "kind": "metric",
  "formula": "COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_053\" = 'Summon - Angel' AND \"XCL_065\" <> 'Angel'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_053\" = 'Summon - Angel' AND \"r0\".\"XCL_065\" <> 'Angel'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:377"
  ]
}
```

### Identifier for a translation record from the 'set_translations' table, linked to the set via the join condition.

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_093\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_096\", T2.\"XCL_093\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_097\" IN ('Masques', 'Mirage')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:442"
  ]
}
```

### "cards"."XCL_049" = 'Fellwar Stone' AND "set_translations"."XCL_092" = 'Japanese' AND NOT "set_translations"."XCL_094" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Fellwar Stone' AND \"set_translations\".\"XCL_092\" = 'Japanese' AND NOT \"set_translations\".\"XCL_094\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_094\" FROM cards AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Fellwar Stone' AND T2.\"XCL_092\" = 'Japanese' AND NOT T2.\"XCL_094\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:500"
  ]
}
```

### "cards"."XCL_049" = 'Beacon of Immortality'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Beacon of Immortality'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_089\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_049\" = 'Beacon of Immortality'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:385"
  ]
}
```

### Battlebond Set Translation

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_092\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_092\" FROM set_translations WHERE \"XCL_091\" IN (SELECT \"XCL_095\" FROM sets WHERE \"XCL_110\" = 'Battlebond')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:519"
  ]
}
```

### The value of column XCL_092 from the set_translations table, representing a specific attribute or translation of a set.

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_092\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_092\", T1.\"XCL_115\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_091\" = 206",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_092\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_092\" AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r0\".\"XCL_099\" = \"r1\".\"XCL_093\" WHERE \"r1\".\"XCL_091\" = 206",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:429"
  ]
}
```

### "cards"."XCL_065" = 'Angel,Wizard' AND "cards"."XCL_064" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_065\" = 'Angel,Wizard' AND \"cards\".\"XCL_064\" IS NULL",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_065\" = 'Angel,Wizard' AND \"XCL_064\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:425"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_010\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_010\", T2.\"XCL_084\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_001\" BETWEEN 1 AND 20",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_010\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "legalities"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_010\" AS \"value\" FROM cards AS \"r0\" INNER JOIN legalities AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_086\" WHERE \"r0\".\"XCL_001\" BETWEEN 1 AND 20",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:390"
  ]
}
```

### Counts the number of distinct card identifiers (XCL_072) for each set identifier (XCL_002), restricted to cards where XCL_029 is 1. Grain is one row p

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"cards\".\"XCL_072\")",
  "grain": [
    "\"cards\".\"XCL_002\""
  ],
  "population_scope": "SELECT COUNT(DISTINCT \"XCL_072\") AS count_uuid FROM cards WHERE \"XCL_029\" = 1 GROUP BY \"XCL_002\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_072\")",
    "grain": [
      "\"r0\".\"XCL_002\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_002\" AS \"grain_0\", COUNT(DISTINCT \"r0\".\"XCL_072\") AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_029\" = 1 GROUP BY \"r0\".\"XCL_002\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:349"
  ]
}
```

### "cards"."XCL_049" = 'Ancestor''s Chosen' AND "foreign_data"."XCL_077" = 'Italian'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Ancestor''s Chosen' AND \"foreign_data\".\"XCL_077\" = 'Italian'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_076\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_049\" = 'Ancestor''s Chosen' AND T2.\"XCL_077\" = 'Italian'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:480"
  ]
}
```

### A scalar metric representing the percentage of joined set-translation records where the translation language is 'Chinese Simplified' and the set attri

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"set_translations\".\"XCL_092\" = 'Chinese Simplified' AND \"sets\".\"XCL_103\" = 1 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*)",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_092\" = 'Chinese Simplified' AND T1.\"XCL_103\" = 1 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r1\".\"XCL_092\" = 'Chinese Simplified' AND \"r0\".\"XCL_103\" = 1 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r1\".\"XCL_092\" = 'Chinese Simplified' AND \"r0\".\"XCL_103\" = 1 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r0\".\"XCL_099\" = \"r1\".\"XCL_093\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:433"
  ]
}
```

### Card Set Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_063\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_063\" FROM cards WHERE \"XCL_049\" = 'Samite Pilgrim'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_063\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_063\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_049\" = 'Samite Pilgrim'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:503"
  ]
}
```

### Card Identifier (XCL_002)

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_002\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T2.\"XCL_077\" = 'Phyrexian'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_002\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "foreign_data"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_002\" AS \"value\" FROM cards AS \"r0\" INNER JOIN foreign_data AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_082\" WHERE \"r1\".\"XCL_077\" = 'Phyrexian'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:367"
  ]
}
```

### "cards"."XCL_019" = 1997 AND "cards"."XCL_022" = 1 AND "cards"."XCL_002" = 'D. Alexander Gregory' AND "legalities"."XCL_084" = 'legacy'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_019\" = 1997 AND \"cards\".\"XCL_022\" = 1 AND \"cards\".\"XCL_002\" = 'D. Alexander Gregory' AND \"legalities\".\"XCL_084\" = 'legacy'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_085\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T2.\"XCL_086\" = T1.\"XCL_072\" WHERE T1.\"XCL_019\" = 1997 AND T1.\"XCL_022\" = 1 AND T1.\"XCL_002\" = 'D. Alexander Gregory' AND T2.\"XCL_084\" = 'legacy'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:521"
  ]
}
```

### Aggregates the count of distinct values in set_translations.XCL_094. The population is limited to rows where sets.XCL_110 equals 'Tenth Edition' and s

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"set_translations\".\"XCL_094\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T2.\"XCL_094\") FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_110\" = 'Tenth Edition' AND NOT T2.\"XCL_094\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r1\".\"XCL_094\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r1\".\"XCL_094\") AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r1\".\"XCL_093\" = \"r0\".\"XCL_099\" WHERE \"r0\".\"XCL_110\" = 'Tenth Edition' AND NOT \"r1\".\"XCL_094\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:499"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_070\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_070\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_049\" = 'Ancestor''s Chosen' AND T2.\"XCL_077\" = 'German'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:482"
  ]
}
```

### "sets"."XCL_110" = 'Coldsnap'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_110\" = 'Coldsnap'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T1.\"XCL_011\" = 7 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Coldsnap'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:486"
  ]
}
```

### "sets"."XCL_097" = 'Ice Age' AND "set_translations"."XCL_092" = 'Italian' AND NOT "set_translations"."XCL_094" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_097\" = 'Ice Age' AND \"set_translations\".\"XCL_092\" = 'Italian' AND NOT \"set_translations\".\"XCL_094\" IS NULL",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_095\") FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_097\" = 'Ice Age' AND T2.\"XCL_092\" = 'Italian' AND NOT T2.\"XCL_094\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:472"
  ]
}
```

### Set Translation Value

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_092\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_091\", \"XCL_092\" FROM set_translations WHERE \"XCL_091\" = (SELECT \"XCL_001\" FROM cards WHERE \"XCL_011\" = 5) AND \"XCL_093\" = '10E'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:388"
  ]
}
```

### ("cards"."XCL_007" IS NULL OR "cards"."XCL_006" IS NULL) AND "cards"."XCL_002" = 'John Avon'

```json
{
  "kind": "predicate",
  "formula": "(\"cards\".\"XCL_007\" IS NULL OR \"cards\".\"XCL_006\" IS NULL) AND \"cards\".\"XCL_002\" = 'John Avon'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE (\"XCL_007\" IS NULL OR \"XCL_006\" IS NULL) AND \"XCL_002\" = 'John Avon'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:393"
  ]
}
```

### "cards"."XCL_049" = 'Ancestor''s Chosen' AND "foreign_data"."XCL_077" = 'German'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Ancestor''s Chosen' AND \"foreign_data\".\"XCL_077\" = 'German'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_070\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_049\" = 'Ancestor''s Chosen' AND T2.\"XCL_077\" = 'German'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:482"
  ]
}
```

### Format Identifier (Max Banned)

```json
{
  "kind": "binding",
  "formula": "\"legalities\".\"XCL_084\"",
  "grain": [
    "\"legalities\".\"XCL_084\""
  ],
  "population_scope": "SELECT \"XCL_084\", COUNT(*) AS count_banned FROM legalities WHERE \"XCL_085\" = 'Banned' GROUP BY \"XCL_084\" ORDER BY COUNT(*) DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:518"
  ]
}
```

### "legalities"."XCL_085" = 'Banned'

```json
{
  "kind": "predicate",
  "formula": "\"legalities\".\"XCL_085\" = 'Banned'",
  "grain": [],
  "population_scope": "WITH MaxBanned AS (SELECT \"XCL_084\", COUNT(*) AS count_banned FROM legalities WHERE \"XCL_085\" = 'Banned' GROUP BY \"XCL_084\" ORDER BY COUNT(*) DESC LIMIT 1) SELECT T2.\"XCL_084\", T1.\"XCL_049\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T2.\"XCL_086\" = T1.\"XCL_072\" INNER JOIN MaxBanned AS MB ON MB.\"XCL_084\" = T2.\"XCL_084\" WHERE T2.\"XCL_085\" = 'Banned'",
  "upstream_scopes": [
    "SELECT \"XCL_084\", COUNT(*) AS count_banned FROM legalities WHERE \"XCL_085\" = 'Banned' GROUP BY \"XCL_084\" ORDER BY COUNT(*) DESC LIMIT 1"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:518"
  ]
}
```

### NOT "cards"."XCL_006" IS NULL AND NOT "cards"."XCL_007" IS NULL

```json
{
  "kind": "predicate",
  "formula": "NOT \"cards\".\"XCL_006\" IS NULL AND NOT \"cards\".\"XCL_007\" IS NULL",
  "grain": [],
  "population_scope": "SELECT \"XCL_006\", \"XCL_007\" FROM cards WHERE NOT \"XCL_006\" IS NULL AND NOT \"XCL_007\" IS NULL ORDER BY \"XCL_006\" LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:423"
  ]
}
```

### "foreign_data"."XCL_076" LIKE '%DAS perfekte Gegenmittel zu einer dichten Formation%'

```json
{
  "kind": "predicate",
  "formula": "\"foreign_data\".\"XCL_076\" LIKE '%DAS perfekte Gegenmittel zu einer dichten Formation%'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_002\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T2.\"XCL_076\" LIKE '%DAS perfekte Gegenmittel zu einer dichten Formation%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:411"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T2.\"XCL_089\", T1.\"XCL_022\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_002\" = 'Stephen Daniele'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "rulings"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM cards AS \"r0\" INNER JOIN rulings AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_090\" WHERE \"r0\".\"XCL_002\" = 'Stephen Daniele'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:347"
  ]
}
```

### "set_translations"."XCL_094" = 'Hauptset Zehnte Edition'

```json
{
  "kind": "predicate",
  "formula": "\"set_translations\".\"XCL_094\" = 'Hauptset Zehnte Edition'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_115\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T2.\"XCL_094\" = 'Hauptset Zehnte Edition'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:471"
  ]
}
```

### An attribute from the 'legalities' table associated with the card. It is selected alongside the card identifier. Due to the GROUP BY on the card ident

```json
{
  "kind": "binding",
  "formula": "\"legalities\".\"XCL_084\"",
  "grain": [
    "\"cards\".\"XCL_002\""
  ],
  "population_scope": "SELECT T1.\"XCL_002\", T2.\"XCL_084\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T2.\"XCL_086\" = T1.\"XCL_072\" GROUP BY T1.\"XCL_002\" ORDER BY COUNT(T1.\"XCL_001\") ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:520"
  ]
}
```

### Set Translation

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_092\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_092\" FROM set_translations WHERE \"XCL_091\" IN (SELECT \"XCL_001\" FROM cards WHERE \"XCL_049\" = 'Angel of Mercy')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:360"
  ]
}
```

### "sets"."XCL_110" = 'Coldsnap' AND "foreign_data"."XCL_077" = 'Italian'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_110\" = 'Coldsnap' AND \"foreign_data\".\"XCL_077\" = 'Italian'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_049\" FROM foreign_data AS T1 INNER JOIN cards AS T2 ON T2.\"XCL_072\" = T1.\"XCL_082\" INNER JOIN sets AS T3 ON T3.\"XCL_099\" = T2.\"XCL_063\" WHERE T3.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_077\" = 'Italian' ORDER BY T2.\"XCL_011\" DESC",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:484"
  ]
}
```

### "cards"."XCL_049" = 'Adarkar Valkyrie'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Adarkar Valkyrie'",
  "grain": [],
  "population_scope": "SELECT IIF(\"XCL_101\" = 1, 'YES', 'NO') FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Adarkar Valkyrie'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:473"
  ]
}
```

### "cards"."XCL_002" = 'Aleksi Briclot' AND "cards"."XCL_034" = 1

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_002\" = 'Aleksi Briclot' AND \"cards\".\"XCL_034\" = 1",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_004\" FROM cards WHERE \"XCL_002\" = 'Aleksi Briclot' AND \"XCL_034\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:508"
  ]
}
```

### "cards"."XCL_049" = 'Angel of Mercy'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Angel of Mercy'",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_049\" = 'Angel of Mercy'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:360"
  ]
}
```

### Ruling Identifier

```json
{
  "kind": "binding",
  "formula": "\"rulings\".\"XCL_089\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_089\", CASE WHEN T1.\"XCL_022\" = 1 THEN 'YES' ELSE 'NO' END FROM cards AS T1 INNER JOIN rulings AS T2 ON T2.\"XCL_090\" = T1.\"XCL_072\" WHERE T1.\"XCL_002\" = 'Jim Pavelec'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_089\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "rulings"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_089\" AS \"value\" FROM cards AS \"r0\" INNER JOIN rulings AS \"r1\" ON \"r1\".\"XCL_090\" = \"r0\".\"XCL_072\" WHERE \"r0\".\"XCL_002\" = 'Jim Pavelec'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:494"
  ]
}
```

### "cards"."XCL_049" = 'Ancestor''s Chosen' AND NOT "foreign_data"."XCL_076" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Ancestor''s Chosen' AND NOT \"foreign_data\".\"XCL_076\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_077\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_049\" = 'Ancestor''s Chosen' AND NOT T2.\"XCL_076\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:481"
  ]
}
```

### "cards"."XCL_004" = 'paper' AND "foreign_data"."XCL_077" = 'Japanese'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_004\" = 'paper' AND \"foreign_data\".\"XCL_077\" = 'Japanese'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T1.\"XCL_004\" = 'paper' AND T2.\"XCL_077\" = 'Japanese'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:382"
  ]
}
```

### "set_translations"."XCL_094" = 'Hauptset Zehnte Edition'

```json
{
  "kind": "predicate",
  "formula": "\"set_translations\".\"XCL_094\" = 'Hauptset Zehnte Edition'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_096\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T2.\"XCL_094\" = 'Hauptset Zehnte Edition'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:467"
  ]
}
```

### "cards"."XCL_059" = 'mythic' AND NOT "cards"."XCL_051" IS NULL AND "legalities"."XCL_085" = 'Legal'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_059\" = 'mythic' AND NOT \"cards\".\"XCL_051\" IS NULL AND \"legalities\".\"XCL_085\" = 'Legal'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_051\", T2.\"XCL_084\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_059\" = 'mythic' AND NOT T1.\"XCL_051\" IS NULL AND T2.\"XCL_085\" = 'Legal' ORDER BY T1.\"XCL_051\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:515"
  ]
}
```

### Distinct XCL_077 values

```json
{
  "kind": "binding",
  "formula": "\"foreign_data\".\"XCL_077\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_077\" FROM foreign_data WHERE \"XCL_079\" = 'A Pedra Fellwar'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:440"
  ]
}
```

### "sets"."XCL_112" BETWEEN '2012-01-01' AND '2015-12-31'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_112\" BETWEEN '2012-01-01' AND '2015-12-31'",
  "grain": [
    "\"sets\".\"XCL_112\""
  ],
  "population_scope": "SELECT (CAST(SUM(T1.\"XCL_095\") AS REAL) / COUNT(T1.\"XCL_095\")) / 4, T2.\"XCL_092\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_095\" = T2.\"XCL_091\" WHERE T1.\"XCL_112\" BETWEEN '2012-01-01' AND '2015-12-31' GROUP BY T1.\"XCL_112\" ORDER BY COUNT(T2.\"XCL_092\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:523"
  ]
}
```

### Distinct values of the 'XCL_077' column from the 'foreign_data' table, restricted to records linked to cards where 'XCL_074' is 'colorpie'.

```json
{
  "kind": "binding",
  "formula": "\"foreign_data\".\"XCL_077\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_077\", T2.\"XCL_076\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_074\" = 'colorpie'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:445"
  ]
}
```

### "foreign_data"."XCL_077" = 'Japanese'

```json
{
  "kind": "predicate",
  "formula": "\"foreign_data\".\"XCL_077\" = 'Japanese'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\" WHERE T2.\"XCL_077\" = 'Japanese'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:351"
  ]
}
```

### Distinct values of the 'XCL_077' column from the 'foreign_data' table, associated with cards filtered by the 'azorius' condition in the 'cards' table.

```json
{
  "kind": "binding",
  "formula": "\"foreign_data\".\"XCL_077\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_077\", T1.\"XCL_070\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_074\" = 'azorius'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:449"
  ]
}
```

### ("cards"."XCL_055" IS NULL OR "cards"."XCL_055" LIKE '%*%') AND "cards"."XCL_057" = 'arenaleague'

```json
{
  "kind": "predicate",
  "formula": "(\"cards\".\"XCL_055\" IS NULL OR \"cards\".\"XCL_055\" LIKE '%*%') AND \"cards\".\"XCL_057\" = 'arenaleague'",
  "grain": [],
  "population_scope": "SELECT \"XCL_049\" FROM cards WHERE (\"XCL_055\" IS NULL OR \"XCL_055\" LIKE '%*%') AND \"XCL_057\" = 'arenaleague' ORDER BY \"XCL_049\" LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:421"
  ]
}
```

### "set_translations"."XCL_093" = 'OGW'

```json
{
  "kind": "predicate",
  "formula": "\"set_translations\".\"XCL_093\" = 'OGW'",
  "grain": [],
  "population_scope": "SELECT \"XCL_091\" FROM set_translations WHERE \"XCL_093\" = 'OGW'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:387"
  ]
}
```

### "cards"."XCL_011" = 0

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_011\" = 0",
  "grain": [],
  "population_scope": "SELECT \"XCL_001\" FROM cards WHERE \"XCL_011\" = 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:375"
  ]
}
```

### "sets"."XCL_110" = 'Eighth Edition' AND "set_translations"."XCL_092" = 'Chinese Simplified'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_110\" = 'Eighth Edition' AND \"set_translations\".\"XCL_092\" = 'Chinese Simplified'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_094\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_110\" = 'Eighth Edition' AND T2.\"XCL_092\" = 'Chinese Simplified'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:468"
  ]
}
```

### "legalities"."XCL_085" = 'Restricted' AND "cards"."XCL_032" = 1

```json
{
  "kind": "predicate",
  "formula": "\"legalities\".\"XCL_085\" = 'Restricted' AND \"cards\".\"XCL_032\" = 1",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T2.\"XCL_085\" = 'Restricted' AND T1.\"XCL_032\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:363"
  ]
}
```

### Count of Distinct Non-Null Translation IDs

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"set_translations\".\"XCL_094\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT \"XCL_094\") FROM set_translations WHERE \"XCL_093\" IN (SELECT \"XCL_063\" FROM cards WHERE \"XCL_049\" = 'Angel of Mercy') AND NOT \"XCL_094\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:463"
  ]
}
```

### Identifies the highest value of the distinct card count (count_uuid) across all sets where XCL_029 is 1. This scalar value represents the size of the 

```json
{
  "kind": "metric",
  "formula": "MAX(\"count_uuid\")",
  "grain": [],
  "population_scope": "SELECT MAX(\"count_uuid\") FROM (SELECT COUNT(DISTINCT \"XCL_072\") AS count_uuid FROM cards WHERE \"XCL_029\" = 1 GROUP BY \"XCL_002\")",
  "upstream_scopes": [
    "SELECT COUNT(DISTINCT \"XCL_072\") AS count_uuid FROM cards WHERE \"XCL_029\" = 1 GROUP BY \"XCL_002\""
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:349"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_049\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_049\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_050\" = 4",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_049\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_049\" AS \"value\" FROM cards AS \"r0\" INNER JOIN sets AS \"r1\" ON \"r1\".\"XCL_099\" = \"r0\".\"XCL_063\" WHERE \"r1\".\"XCL_110\" = 'Coldsnap' AND \"r0\".\"XCL_050\" = 4",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:478"
  ]
}
```

### "cards"."XCL_071" = 'Creature' AND "cards"."XCL_037" = 'normal' AND "cards"."XCL_005" = 'black' AND "cards"."XCL_002" = 'Matthew D. Wilson'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_071\" = 'Creature' AND \"cards\".\"XCL_037\" = 'normal' AND \"cards\".\"XCL_005\" = 'black' AND \"cards\".\"XCL_002\" = 'Matthew D. Wilson'",
  "grain": [],
  "population_scope": "SELECT \"XCL_072\" FROM cards WHERE \"XCL_071\" = 'Creature' AND \"XCL_037\" = 'normal' AND \"XCL_005\" = 'black' AND \"XCL_002\" = 'Matthew D. Wilson'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:412"
  ]
}
```

### "cards"."XCL_036" = 'Flying'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_036\" = 'Flying'",
  "grain": [],
  "population_scope": "SELECT \"XCL_037\" FROM cards WHERE \"XCL_036\" = 'Flying'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:376"
  ]
}
```

### "cards"."XCL_049" = 'Cloudchaser Eagle'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Cloudchaser Eagle'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_085\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_049\" = 'Cloudchaser Eagle'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:364"
  ]
}
```

### Korean Set Translation ID

```json
{
  "kind": "binding",
  "formula": "\"set_translations\".\"XCL_093\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_093\" FROM set_translations WHERE \"XCL_092\" = 'Korean' AND \"XCL_092\" NOT LIKE '%Japanese%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_093\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_093\" AS \"value\" FROM set_translations AS \"r0\" WHERE \"r0\".\"XCL_092\" = 'Korean' AND \"r0\".\"XCL_092\" NOT LIKE '%Japanese%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:529"
  ]
}
```

### "cards"."XCL_002" = 'Aaron Boyd'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_002\" = 'Aaron Boyd'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_070\") FROM cards WHERE \"XCL_002\" = 'Aaron Boyd'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:354"
  ]
}
```

### "cards"."XCL_002" = 'Daren Bader'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_002\" = 'Daren Bader'",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_004\" FROM cards WHERE \"XCL_002\" = 'Daren Bader'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:418"
  ]
}
```

### Calculates the percentage of joined card records where the associated foreign data entry has 'Chinese Simplified' in column XCL_077. The numerator cou

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"foreign_data\".\"XCL_077\" = 'Chinese Simplified' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_077\" = 'Chinese Simplified' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.\"XCL_072\" = T2.\"XCL_082\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r1\".\"XCL_077\" = 'Chinese Simplified' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "foreign_data"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r1\".\"XCL_077\" = 'Chinese Simplified' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" INNER JOIN foreign_data AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_082\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:352"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_001\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\", T2.\"XCL_088\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE T1.\"XCL_053\" = 'Creature - Elf'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_001\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "rulings"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_001\" AS \"value\" FROM cards AS \"r0\" INNER JOIN rulings AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_090\" WHERE \"r0\".\"XCL_053\" = 'Creature - Elf'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:389"
  ]
}
```

### "set_translations"."XCL_091" = 206

```json
{
  "kind": "predicate",
  "formula": "\"set_translations\".\"XCL_091\" = 206",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_092\", T1.\"XCL_115\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T2.\"XCL_091\" = 206",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:429"
  ]
}
```

### Largest Set Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_002\"",
  "grain": [
    "\"cards\".\"XCL_002\""
  ],
  "population_scope": "SELECT \"XCL_002\" FROM cards WHERE \"XCL_029\" = 1 GROUP BY \"XCL_002\" HAVING COUNT(DISTINCT \"XCL_072\") = (SELECT MAX(\"count_uuid\") FROM (SELECT COUNT(DISTINCT \"XCL_072\") AS count_uuid FROM cards WHERE \"XCL_029\" = 1 GROUP BY \"XCL_002\"))",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:349"
  ]
}
```

### Card Attribute XCL_066

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_066\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_065\", \"XCL_066\" FROM cards WHERE \"XCL_049\" = 'Molimo, Maro-Sorcerer'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:456"
  ]
}
```

### "cards"."XCL_053" = 'Summon - Angel' AND "cards"."XCL_065" <> 'Angel'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_053\" = 'Summon - Angel' AND \"cards\".\"XCL_065\" <> 'Angel'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_053\" = 'Summon - Angel' AND \"XCL_065\" <> 'Angel'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:377"
  ]
}
```

### Aggregates the total number of card records where the attribute 'XCL_005' equals 'black', restricted to cards belonging to the set identified by 'XCL_

```json
{
  "kind": "metric",
  "formula": "SUM(CASE WHEN \"cards\".\"XCL_005\" = 'black' THEN 1 ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN T1.\"XCL_005\" = 'black' THEN 1 ELSE 0 END) FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Coldsnap'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(CASE WHEN \"r0\".\"XCL_005\" = 'black' THEN 1 ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "sets"
      }
    ],
    "scope_sql": "SELECT SUM(CASE WHEN \"r0\".\"XCL_005\" = 'black' THEN 1 ELSE 0 END) AS \"value\" FROM cards AS \"r0\" INNER JOIN sets AS \"r1\" ON \"r1\".\"XCL_099\" = \"r0\".\"XCL_063\" WHERE \"r1\".\"XCL_110\" = 'Coldsnap'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:475"
  ]
}
```

### "sets"."XCL_097" IN ('Masques', 'Mirage')

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_097\" IN ('Masques', 'Mirage')",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_096\", T2.\"XCL_093\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T1.\"XCL_097\" IN ('Masques', 'Mirage')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:442"
  ]
}
```

### Card Attribute XCL_007

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_006\", \"XCL_007\" FROM cards WHERE NOT \"XCL_006\" IS NULL AND NOT \"XCL_007\" IS NULL ORDER BY \"XCL_006\" LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:423"
  ]
}
```

### Aggregates the total number of non-null values in column XCL_001 from the cards table, restricted to rows where XCL_069 equals 99. Returns a single sc

```json
{
  "kind": "metric",
  "formula": "COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_069\" = 99",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_069\" = 99",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:372"
  ]
}
```

### ("sets"."XCL_110" = 'Coldsnap' AND "cards"."XCL_002" = 'Chippy') OR ("sets"."XCL_110" = 'Coldsnap' AND "cards"."XCL_002" = 'Aaron Miller') OR ("sets".

```json
{
  "kind": "predicate",
  "formula": "(\"sets\".\"XCL_110\" = 'Coldsnap' AND \"cards\".\"XCL_002\" = 'Chippy') OR (\"sets\".\"XCL_110\" = 'Coldsnap' AND \"cards\".\"XCL_002\" = 'Aaron Miller') OR (\"sets\".\"XCL_110\" = 'Coldsnap' AND \"cards\".\"XCL_002\" = 'Jeremy Jarvis')",
  "grain": [
    "\"cards\".\"XCL_002\""
  ],
  "population_scope": "SELECT T1.\"XCL_002\" FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE (T2.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_002\" = 'Chippy') OR (T2.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_002\" = 'Aaron Miller') OR (T2.\"XCL_110\" = 'Coldsnap' AND T1.\"XCL_002\" = 'Jeremy Jarvis') GROUP BY T1.\"XCL_002\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:477"
  ]
}
```

### Card Identifier

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_072\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_072\", T3.\"XCL_077\" FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" INNER JOIN foreign_data AS T3 ON T1.\"XCL_072\" = T3.\"XCL_082\" WHERE T2.\"XCL_084\" = 'legacy'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_072\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "legalities"
      },
      {
        "role": "r2",
        "physical_table": "foreign_data"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_072\" AS \"value\" FROM cards AS \"r0\" INNER JOIN legalities AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_086\" INNER JOIN foreign_data AS \"r2\" ON \"r0\".\"XCL_072\" = \"r2\".\"XCL_082\" WHERE \"r1\".\"XCL_084\" = 'legacy'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:384"
  ]
}
```

### "cards"."XCL_049" = 'Ancestor''s Chosen'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Ancestor''s Chosen'",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_005\" FROM cards WHERE \"XCL_049\" = 'Ancestor''s Chosen'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:358"
  ]
}
```

### "sets"."XCL_097" = 'Shadowmoor' AND "set_translations"."XCL_092" = 'Italian'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_097\" = 'Shadowmoor' AND \"set_translations\".\"XCL_092\" = 'Italian'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_110\", T1.\"XCL_095\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T1.\"XCL_097\" = 'Shadowmoor' AND T2.\"XCL_092\" = 'Italian' ORDER BY T1.\"XCL_095\" LIMIT 2",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:430"
  ]
}
```

### Card Attribute XCL_065

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_065\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_065\", \"XCL_066\" FROM cards WHERE \"XCL_049\" = 'Molimo, Maro-Sorcerer'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:456"
  ]
}
```

### Identifier (XCL_115) from the sets table, representing the final output population. The grain is individual sets that have a foreign key (XCL_099) mat

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_115\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_115\" FROM sets WHERE \"XCL_099\" IN (SELECT \"XCL_093\" FROM set_translations WHERE \"XCL_094\" = 'Huitième édition')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:497"
  ]
}
```

### Output column 'XCL_079' from the 'foreign_data' table. The grain is individual rows where 'XCL_077' equals 'Spanish'. This binding returns the specifi

```json
{
  "kind": "binding",
  "formula": "\"foreign_data\".\"XCL_079\"",
  "grain": [],
  "population_scope": "SELECT (SELECT CAST(SUM(CASE WHEN \"XCL_077\" = 'Spanish' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) FROM foreign_data), \"XCL_079\" FROM foreign_data WHERE \"XCL_077\" = 'Spanish'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:403"
  ]
}
```

### "sets"."XCL_099" = 'SS2'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_099\" = 'SS2'",
  "grain": [],
  "population_scope": "SELECT \"XCL_106\" FROM sets WHERE \"XCL_099\" = 'SS2'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:490"
  ]
}
```

### "sets"."XCL_110" = 'Coldsnap'

```json
{
  "kind": "predicate",
  "formula": "\"sets\".\"XCL_110\" = 'Coldsnap'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN NOT T1.\"XCL_006\" IS NULL AND NOT T1.\"XCL_007\" IS NULL THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T2.\"XCL_110\" = 'Coldsnap'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:487"
  ]
}
```

### "cards"."XCL_049" = 'Angel of Mercy'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Angel of Mercy'",
  "grain": [],
  "population_scope": "SELECT IIF(NOT T2.\"XCL_109\" IS NULL, 'YES', 'NO') FROM cards AS T1 INNER JOIN sets AS T2 ON T2.\"XCL_099\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Angel of Mercy'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:469"
  ]
}
```

### Aggregates the total number of rows in the 'cards' table where 'XCL_005' is 'white' and both 'XCL_006' and 'XCL_007' are not null. Returns a single sc

```json
{
  "kind": "metric",
  "formula": "COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_005\" = 'white' AND NOT \"XCL_007\" IS NULL AND NOT \"XCL_006\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_005\" = 'white' AND NOT \"r0\".\"XCL_007\" IS NULL AND NOT \"r0\".\"XCL_006\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:394"
  ]
}
```

### Date associated with the trading card game set, retrieved from the 'sets' table. Used for ordering results chronologically.

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_095\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_110\", T1.\"XCL_095\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.\"XCL_099\" = T2.\"XCL_093\" WHERE T1.\"XCL_097\" = 'Shadowmoor' AND T2.\"XCL_092\" = 'Italian' ORDER BY T1.\"XCL_095\" LIMIT 2",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:430"
  ]
}
```

### Aggregates the total number of rows in the 'cards' table where 'XCL_013' is greater than 12000 and 'XCL_005' equals 'borderless'. The grain is a singl

```json
{
  "kind": "metric",
  "formula": "COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_013\" > 12000 AND \"XCL_005\" = 'borderless'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_013\" > 12000 AND \"r0\".\"XCL_005\" = 'borderless'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:419"
  ]
}
```

### ("cards"."XCL_055" IS NULL OR "cards"."XCL_055" = '*') AND "rulings"."XCL_089" LIKE '%triggered ability%'

```json
{
  "kind": "predicate",
  "formula": "(\"cards\".\"XCL_055\" IS NULL OR \"cards\".\"XCL_055\" = '*') AND \"rulings\".\"XCL_089\" LIKE '%triggered ability%'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_089\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" WHERE (T1.\"XCL_055\" IS NULL OR T1.\"XCL_055\" = '*') AND T2.\"XCL_089\" LIKE '%triggered ability%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:408"
  ]
}
```

### Set Identifier

```json
{
  "kind": "binding",
  "formula": "\"sets\".\"XCL_096\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_096\" FROM sets AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_099\" WHERE T2.\"XCL_094\" = 'Rinascita di Alara'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_096\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "sets"
      },
      {
        "role": "r1",
        "physical_table": "set_translations"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_096\" AS \"value\" FROM sets AS \"r0\" INNER JOIN set_translations AS \"r1\" ON \"r1\".\"XCL_093\" = \"r0\".\"XCL_099\" WHERE \"r1\".\"XCL_094\" = 'Rinascita di Alara'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:496"
  ]
}
```

### "cards"."XCL_004" = 'mtgo' AND "cards"."XCL_005" = 'black'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_004\" = 'mtgo' AND \"cards\".\"XCL_005\" = 'black'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_004\" = 'mtgo' AND \"XCL_005\" = 'black'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:374"
  ]
}
```

### "legalities"."XCL_085" = 'Legal' AND "cards"."XCL_071" = 'Creature'

```json
{
  "kind": "predicate",
  "formula": "\"legalities\".\"XCL_085\" = 'Legal' AND \"cards\".\"XCL_071\" = 'Creature'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_001\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.\"XCL_072\" = T2.\"XCL_090\" INNER JOIN legalities AS T3 ON T1.\"XCL_072\" = T3.\"XCL_086\" WHERE T3.\"XCL_085\" = 'Legal' AND T1.\"XCL_071\" = 'Creature'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:406"
  ]
}
```

### A derived boolean indicator converting the card attribute XCL_022 into a 'YES'/'NO' string, where 1 maps to 'YES' and other values to 'NO'.

```json
{
  "kind": "binding",
  "formula": "CASE WHEN \"cards\".\"XCL_022\" = 1 THEN 'YES' ELSE 'NO' END",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_089\", CASE WHEN T1.\"XCL_022\" = 1 THEN 'YES' ELSE 'NO' END FROM cards AS T1 INNER JOIN rulings AS T2 ON T2.\"XCL_090\" = T1.\"XCL_072\" WHERE T1.\"XCL_002\" = 'Jim Pavelec'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CASE WHEN \"r0\".\"XCL_022\" = 1 THEN 'YES' ELSE 'NO' END",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "rulings"
      }
    ],
    "scope_sql": "SELECT CASE WHEN \"r0\".\"XCL_022\" = 1 THEN 'YES' ELSE 'NO' END AS \"value\" FROM cards AS \"r0\" INNER JOIN rulings AS \"r1\" ON \"r1\".\"XCL_090\" = \"r0\".\"XCL_072\" WHERE \"r0\".\"XCL_002\" = 'Jim Pavelec'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:494"
  ]
}
```

### Count of cards

```json
{
  "kind": "metric",
  "formula": "COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM cards WHERE \"XCL_019\" = 1993 AND \"XCL_004\" = 'paper' AND \"XCL_022\" = 1",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_019\" = 1993 AND \"r0\".\"XCL_004\" = 'paper' AND \"r0\".\"XCL_022\" = 1",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:396"
  ]
}
```

### Distinct values of the XCL_004 column from the cards table, filtered to rows where XCL_002 equals 'Daren Bader'.

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_004\" FROM cards WHERE \"XCL_002\" = 'Daren Bader'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:418"
  ]
}
```

### The value of column XCL_053 from the cards table, filtered to rows where XCL_049 is 'Ancestor's Chosen' and XCL_053 is not null.

```json
{
  "kind": "binding",
  "formula": "\"cards\".\"XCL_053\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_053\" FROM cards WHERE \"XCL_049\" = 'Ancestor''s Chosen' AND NOT \"XCL_053\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_053\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_053\" AS \"value\" FROM cards AS \"r0\" WHERE \"r0\".\"XCL_049\" = 'Ancestor''s Chosen' AND NOT \"r0\".\"XCL_053\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:359"
  ]
}
```

### Aggregates the count of card records (identified by XCL_001) from the cards table where the status (XCL_019) is 'future' and the card has a correspond

```json
{
  "kind": "metric",
  "formula": "COUNT(\"cards\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_019\" = 'future'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "legalities"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM cards AS \"r0\" INNER JOIN legalities AS \"r1\" ON \"r0\".\"XCL_072\" = \"r1\".\"XCL_086\" WHERE \"r0\".\"XCL_019\" = 'future'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:386"
  ]
}
```

### "cards"."XCL_002" = 'Allen Williams'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_002\" = 'Allen Williams'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_019\", T1.\"XCL_049\", IIF(T2.\"XCL_085\" = 'Banned', T1.\"XCL_049\", 'NO') FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.\"XCL_072\" = T2.\"XCL_086\" WHERE T1.\"XCL_002\" = 'Allen Williams'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:530"
  ]
}
```

### "cards"."XCL_064" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_064\" IS NULL",
  "grain": [],
  "population_scope": "SELECT \"XCL_002\" FROM cards WHERE \"XCL_064\" IS NULL ORDER BY \"XCL_011\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:510"
  ]
}
```

### "cards"."XCL_074" = 'azorius'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_074\" = 'azorius'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_077\", T1.\"XCL_070\" FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T2.\"XCL_082\" = T1.\"XCL_072\" WHERE T1.\"XCL_074\" = 'azorius'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:449"
  ]
}
```

### Calculates the percentage of sets (identified by XCL_095) that have a value of 1 in column XCL_103. The calculation is restricted to sets whose ID (XC

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"sets\".\"XCL_103\" = 1 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"sets\".\"XCL_095\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN \"XCL_103\" = 1 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(\"XCL_095\") FROM sets WHERE \"XCL_099\" IN (SELECT \"XCL_093\" FROM set_translations WHERE \"XCL_092\" = 'Portuguese (Brazil)')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:507"
  ]
}
```

### Ruling Text

```json
{
  "kind": "binding",
  "formula": "\"rulings\".\"XCL_088\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_088\" FROM cards AS T1 INNER JOIN rulings AS T2 ON T2.\"XCL_090\" = T1.\"XCL_072\" WHERE T1.\"XCL_049\" = 'Reminisce'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_088\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "cards"
      },
      {
        "role": "r1",
        "physical_table": "rulings"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_088\" AS \"value\" FROM cards AS \"r0\" INNER JOIN rulings AS \"r1\" ON \"r1\".\"XCL_090\" = \"r0\".\"XCL_072\" WHERE \"r0\".\"XCL_049\" = 'Reminisce'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:485"
  ]
}
```

### "cards"."XCL_049" = 'Ancestor''s Chosen'

```json
{
  "kind": "predicate",
  "formula": "\"cards\".\"XCL_049\" = 'Ancestor''s Chosen'",
  "grain": [],
  "population_scope": "SELECT IIF(SUM(CASE WHEN T2.\"XCL_092\" = 'Korean' AND NOT T2.\"XCL_094\" IS NULL THEN 1 ELSE 0 END) > 0, 'YES', 'NO') FROM cards AS T1 INNER JOIN set_translations AS T2 ON T2.\"XCL_093\" = T1.\"XCL_063\" WHERE T1.\"XCL_049\" = 'Ancestor''s Chosen'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:465"
  ]
}
```


## 增量维护事件

- Recorded alias revision · cards.XCL_057 · Archived superseded_alias_hypotheses → archived aliases
  - cards.XCL_057: set_code → frame_effect
- Recorded alias revision · sets.XCL_096 · Archived superseded_alias_hypotheses → archived aliases
  - sets.XCL_096: parent_set_id → base_set_size
- Recorded alias revision · cards.XCL_014 · Archived superseded_alias_hypotheses → archived aliases
  - cards.XCL_014: converted_mana_cost → edhrec_rank
