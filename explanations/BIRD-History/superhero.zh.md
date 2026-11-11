# BIRD-History / superhero — Schema 与业务口径解释

该数据库的存档目录包含 10 张表、31 个物理列、22 条关系，以及 129 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## alignment

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: A, T2, T3, T4, T5, T7s, a, al

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| alignment.XCL_001 | alignment_id | unknown | bird_dev:822, bird_dev:818, bird_dev:835, bird_dev:813, bird_dev:815, bird_dev:842, bird_dev:811, bird_dev:795 |
| alignment.XCL_002 | alignment | unknown | bird_dev:822, bird_dev:818, bird_dev:835, bird_dev:813, bird_dev:815, bird_dev:842, bird_dev:811, bird_dev:795 |

## attribute

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: DA, SA, T2, T3, T4, T5, T5b, T6, T6b, T6s, T7, a, a2, at

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| attribute.XCL_003 | attribute_id | unknown | bird_dev:738, bird_dev:820, bird_dev:794, bird_dev:796, bird_dev:786, bird_dev:769, bird_dev:828, bird_dev:830 |
| attribute.XCL_004 | attribute_name | unknown | bird_dev:820, bird_dev:794, bird_dev:796, bird_dev:769, bird_dev:828, bird_dev:830, bird_dev:740, bird_dev:766 |

## colour

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: C1, C2, T2, T3, T4, T5, T6, c, c_eye, c_hair

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| colour.XCL_005 | colour_id | unknown | bird_dev:822, bird_dev:770, bird_dev:844, bird_dev:782, bird_dev:817, bird_dev:806, bird_dev:758, bird_dev:748 |
| colour.XCL_006 | colour_name | unknown | bird_dev:822, bird_dev:770, bird_dev:844, bird_dev:782, bird_dev:817, bird_dev:806, bird_dev:758, bird_dev:748 |

## gender

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: G, T2, T2b, T3, T4, g, g2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| gender.XCL_007 | gender_id | unknown | bird_dev:825, bird_dev:801, bird_dev:818, bird_dev:817, bird_dev:751, bird_dev:815, bird_dev:793, bird_dev:777 |
| gender.XCL_008 | gender_name | unknown | bird_dev:825, bird_dev:801, bird_dev:818, bird_dev:817, bird_dev:751, bird_dev:815, bird_dev:777, bird_dev:772 |

## hero_attribute

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: D, S, T1, T2, T3, T4, T4b, T5, T5b, T5s, T6, ha, ha2, s

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| hero_attribute.XCL_009 | hero_id | unknown | bird_dev:813, bird_dev:814, bird_dev:820, bird_dev:794, bird_dev:796, bird_dev:786, bird_dev:840, bird_dev:769 |
| hero_attribute.XCL_010 | attribute_id | unknown | bird_dev:738, bird_dev:820, bird_dev:794, bird_dev:796, bird_dev:786, bird_dev:769, bird_dev:828, bird_dev:830 |
| hero_attribute.XCL_011 | attribute_score | unknown | bird_dev:813, bird_dev:814, bird_dev:820, bird_dev:794, bird_dev:796, bird_dev:786, bird_dev:840, bird_dev:746 |

## hero_power

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, T3, T4, T5, T6, T7, hp, hp2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| hero_power.XCL_012 | hero_id | unknown | bird_dev:718, bird_dev:825, bird_dev:741, bird_dev:719, bird_dev:739, bird_dev:765, bird_dev:751, bird_dev:762 |
| hero_power.XCL_013 | power_id | unknown | bird_dev:718, bird_dev:825, bird_dev:719, bird_dev:739, bird_dev:730, bird_dev:765, bird_dev:751, bird_dev:762 |

## publisher

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, T3, T3b, T4, T5, T6, p, p2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| publisher.XCL_014 | publisher_id | unknown | bird_dev:799, bird_dev:835, bird_dev:729, bird_dev:827, bird_dev:809, bird_dev:826, bird_dev:772, bird_dev:769 |
| publisher.XCL_015 | publisher_name | unknown | bird_dev:835, bird_dev:729, bird_dev:827, bird_dev:809, bird_dev:826, bird_dev:772, bird_dev:769, bird_dev:773 |

## race

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: R, T2, T3, T5, T6, T7, r, r2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| race.XCL_016 | race_id | unknown | bird_dev:808, bird_dev:757, bird_dev:817, bird_dev:755, bird_dev:758, bird_dev:793, bird_dev:737, bird_dev:827 |
| race.XCL_017 | race_name | unknown | bird_dev:808, bird_dev:757, bird_dev:817, bird_dev:755, bird_dev:758, bird_dev:737, bird_dev:827, bird_dev:789 |

## superhero

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: S, T0, T1, T1b, T1s, T2, T3, T4, s, s2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| superhero.XCL_018 | superhero_id | unknown | bird_dev:799, bird_dev:822, bird_dev:825, bird_dev:801, bird_dev:818, bird_dev:835, bird_dev:836, bird_dev:741 |
| superhero.XCL_019 | superhero_name | unknown | bird_dev:844, bird_dev:782, bird_dev:802, bird_dev:741, bird_dev:739, bird_dev:738, bird_dev:730, bird_dev:753 |
| superhero.XCL_020 | full_name | unknown | bird_dev:805, bird_dev:770, bird_dev:790, bird_dev:836, bird_dev:755, bird_dev:806, bird_dev:807, bird_dev:839 |
| superhero.XCL_021 | gender_id | unknown | bird_dev:825, bird_dev:801, bird_dev:818, bird_dev:817, bird_dev:751, bird_dev:815, bird_dev:793, bird_dev:777 |
| superhero.XCL_022 | eye_colour_id | unknown | bird_dev:770, bird_dev:844, bird_dev:782, bird_dev:806, bird_dev:748, bird_dev:759, bird_dev:753, bird_dev:839 |
| superhero.XCL_023 | hair_colour_id | unknown | bird_dev:782, bird_dev:817, bird_dev:758, bird_dev:735, bird_dev:772, bird_dev:773, bird_dev:797, bird_dev:724 |
| superhero.XCL_024 | skin_colour_id | unknown | bird_dev:822, bird_dev:814, bird_dev:767, bird_dev:772, bird_dev:773, bird_dev:783, bird_dev:722, bird_dev:775 |
| superhero.XCL_025 | race_id | unknown | bird_dev:808, bird_dev:757, bird_dev:817, bird_dev:755, bird_dev:758, bird_dev:793, bird_dev:737, bird_dev:827 |
| superhero.XCL_026 | publisher_id | unknown | bird_dev:799, bird_dev:835, bird_dev:729, bird_dev:827, bird_dev:809, bird_dev:826, bird_dev:772, bird_dev:769 |
| superhero.XCL_027 | alignment_id | unknown | bird_dev:822, bird_dev:818, bird_dev:835, bird_dev:813, bird_dev:815, bird_dev:842, bird_dev:811, bird_dev:795 |
| superhero.XCL_028 | height_cm | unknown | bird_dev:808, bird_dev:802, bird_dev:719, bird_dev:758, bird_dev:753, bird_dev:842, bird_dev:729, bird_dev:827 |
| superhero.XCL_029 | weight_kg | unknown | bird_dev:805, bird_dev:808, bird_dev:790, bird_dev:757, bird_dev:759, bird_dev:839, bird_dev:789, bird_dev:826 |

## superpower

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T2, T3, T4, T5, T7, T8, sp

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| superpower.XCL_030 | superpower_id | unknown | bird_dev:718, bird_dev:825, bird_dev:719, bird_dev:739, bird_dev:730, bird_dev:765, bird_dev:751, bird_dev:762 |
| superpower.XCL_031 | superpower_name | unknown | bird_dev:718, bird_dev:825, bird_dev:719, bird_dev:739, bird_dev:765, bird_dev:751, bird_dev:762, bird_dev:807 |

## 表关系与连接依据

- alignment.XCL_001 ↔ superhero.XCL_027; target_disjoint_historical_join
- attribute.XCL_003 ↔ hero_attribute.XCL_010; target_disjoint_historical_join
- colour.XCL_005 ↔ superhero.XCL_022; target_disjoint_historical_join
- colour.XCL_005 ↔ superhero.XCL_023; target_disjoint_historical_join
- colour.XCL_005 ↔ superhero.XCL_024; target_disjoint_historical_join
- gender.XCL_007 ↔ superhero.XCL_021; target_disjoint_historical_join
- hero_attribute.XCL_009 ↔ superhero.XCL_018; target_disjoint_historical_join
- hero_power.XCL_012 ↔ superhero.XCL_018; target_disjoint_historical_join
- hero_power.XCL_013 ↔ superpower.XCL_030; target_disjoint_historical_join
- publisher.XCL_014 ↔ superhero.XCL_026; target_disjoint_historical_join
- race.XCL_016 ↔ superhero.XCL_025; target_disjoint_historical_join
- alignment.XCL_001 ↔ superhero.XCL_027; sql_workload_observed_join
- attribute.XCL_003 ↔ hero_attribute.XCL_010; sql_workload_observed_join
- colour.XCL_005 ↔ superhero.XCL_022; sql_workload_observed_join
- colour.XCL_005 ↔ superhero.XCL_023; sql_workload_observed_join
- colour.XCL_005 ↔ superhero.XCL_024; sql_workload_observed_join
- gender.XCL_007 ↔ superhero.XCL_021; sql_workload_observed_join
- hero_attribute.XCL_009 ↔ superhero.XCL_018; sql_workload_observed_join
- hero_power.XCL_012 ↔ superhero.XCL_018; sql_workload_observed_join
- hero_power.XCL_013 ↔ superpower.XCL_030; sql_workload_observed_join
- publisher.XCL_014 ↔ superhero.XCL_026; sql_workload_observed_join
- race.XCL_016 ↔ superhero.XCL_025; sql_workload_observed_join

## 业务口径、总体与粒度

### A query that joins superhero, hero_attribute, and attribute tables to find the attribute name with the minimum value for the superhero named 'Black Pa

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_004\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T1.\"XCL_019\" = 'Black Panther' ORDER BY T2.\"XCL_011\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:830"
  ]
}
```

### A full SQL program that selects the "XCL_019" field from the "superhero" table, ordered by "XCL_028" in descending order, and limits the result to the

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_019\" FROM superhero ORDER BY \"XCL_028\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:802",
    "bird_dev:832"
  ]
}
```

### A query that joins superhero, hero_power, and superpower tables to retrieve superpower identifiers (XCL_031) for superheroes whose XCL_028 value is gr

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T1.\"XCL_028\" * 100 > (SELECT AVG(\"XCL_028\") FROM superhero) * 80",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:845"
  ]
}
```

### Full program retrieving identifiers of superheroes who have 'Super Strength' and are published by 'Marvel Comics'. Uses correlated EXISTS subqueries t

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_019\" FROM superhero AS T1 WHERE EXISTS(SELECT 1 FROM hero_power AS T2 INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T3.\"XCL_031\" = 'Super Strength' AND T1.\"XCL_018\" = T2.\"XCL_012\") AND EXISTS(SELECT 1 FROM publisher AS T4 WHERE T4.\"XCL_015\" = 'Marvel Comics' AND T1.\"XCL_026\" = T4.\"XCL_014\")",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:730"
  ]
}
```

### Get Colour for Apocalypse

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_024\" = T2.\"XCL_005\" WHERE T1.\"XCL_019\" = 'Apocalypse'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:722"
  ]
}
```

### A query that joins the superhero table with the hero_attribute table on XCL_018 and XCL_009, filters for attribute scores (XCL_011) between 75 and 80,

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" WHERE T2.\"XCL_011\" BETWEEN 75 AND 80",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:816"
  ]
}
```

### Executes an inner join between the superhero and colour tables on the foreign key relationship (XCL_022 = XCL_005), filters for the specific colour va

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Blue'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:721"
  ]
}
```

### A query that joins the "superhero" and "race" tables on the foreign key relationship ("XCL_025" to "XCL_016") to retrieve the race identifier ("XCL_01

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_017\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T1.\"XCL_029\" = 169",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:757"
  ]
}
```

### A query that joins the superhero, race, and alignment tables to retrieve the race and alignment identifiers for a specific superhero identified by the

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_017\", T3.\"XCL_002\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" INNER JOIN alignment AS T3 ON T1.\"XCL_027\" = T3.\"XCL_001\" WHERE T1.\"XCL_019\" = 'Cameron Hicks'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:787"
  ]
}
```

### SELECT T2."XCL_015" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1."XCL_026" = T2."XCL_014" WHERE T1."XCL_019" = 'Sauron'

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_015\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_019\" = 'Sauron'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:727"
  ]
}
```

### A query that joins the superhero table with the race table to retrieve the race identifier for a specific superhero. It filters the superhero table fo

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_017\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T1.\"XCL_019\" = 'Copycat'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:737"
  ]
}
```

### Neutral Superhero Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" WHERE T2.\"XCL_002\" = 'Neutral'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:795"
  ]
}
```

### Full SQL program that joins the superhero table to the publisher table on the publisher ID (XCL_026 = XCL_014) and filters for publisher ID 1 to compu

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T2.\"XCL_014\" = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:799"
  ]
}
```

### A query that resolves the gender of a specific superhero by name. It joins the superhero table (T1) with the gender table (T2) on the gender reference

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_008\" FROM superhero AS T1 INNER JOIN gender AS T2 ON T1.\"XCL_021\" = T2.\"XCL_007\" WHERE T1.\"XCL_019\" = 'Agent 13'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:777"
  ]
}
```

### Full SQL program that joins superhero, publisher, hero_attribute, and attribute tables to identify the publisher of the superhero with the maximum 'Sp

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_015\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN hero_attribute AS T3 ON T1.\"XCL_018\" = T3.\"XCL_009\" INNER JOIN attribute AS T4 ON T3.\"XCL_010\" = T4.\"XCL_003\" WHERE T4.\"XCL_004\" = 'Speed' ORDER BY T3.\"XCL_011\" LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:732"
  ]
}
```

### A program that joins superhero, hero_attribute, and attribute tables to identify the superhero with the maximum Strength value. It filters for the att

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_020\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T3.\"XCL_004\" = 'Strength' ORDER BY T2.\"XCL_011\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:766"
  ]
}
```

### Full SQL program that joins the superhero table (T1) to the colour table (T2) on T1.XCL_022 = T2.XCL_005. It filters for superheroes where T1.XCL_029 

```json
{
  "kind": "program",
  "formula": "SELECT SUM(CASE WHEN T2.\"XCL_005\" = 7 THEN 1 ELSE 0 END) - SUM(CASE WHEN T2.\"XCL_005\" = 1 THEN 1 ELSE 0 END) FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_029\" = 0 OR T1.\"XCL_029\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:819"
  ]
}
```

### A query program that joins the superhero table (T1) with the publisher table (T2) on the publisher identifier (XCL_026 = XCL_014), filters for the spe

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T2.\"XCL_015\" = 'DC Comics'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:731"
  ]
}
```

### Executes an inner join between the superhero table (T1) and the alignment table (T2) on the alignment key (XCL_027 = XCL_001). It filters for alignmen

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" WHERE T2.\"XCL_002\" = 'Bad'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:756"
  ]
}
```

### Executes an inner join between hero_power (T1) and superpower (T2) on the foreign key relationship T1.XCL_013 = T2.XCL_030. Filters the result set to 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_012\") FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.\"XCL_013\" = T2.\"XCL_030\" WHERE T2.\"XCL_031\" = 'Super Strength'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:718"
  ]
}
```

### Bad Superhero Gender Distribution Query

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(CASE WHEN T3.\"XCL_008\" = 'Female' THEN T1.\"XCL_018\" ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" INNER JOIN gender AS T3 ON T1.\"XCL_021\" = T3.\"XCL_007\" WHERE T2.\"XCL_002\" = 'Bad'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:818"
  ]
}
```

### Full SQL program that joins superhero, hero_power, superpower, and colour tables to count superheroes possessing the 'Agility' power and having 'Blue'

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" INNER JOIN colour AS T4 ON T1.\"XCL_022\" = T4.\"XCL_005\" WHERE T3.\"XCL_031\" = 'Agility' AND T4.\"XCL_006\" = 'Blue'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:723"
  ]
}
```

### Executes an inner join between superhero, publisher, and colour tables. It filters for publishers named 'Marvel Comics' and colours named 'Gold', then

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN colour AS T3 ON T1.\"XCL_022\" = T3.\"XCL_005\" WHERE T2.\"XCL_015\" = 'Marvel Comics' AND T3.\"XCL_006\" = 'Gold'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:733"
  ]
}
```

### A program that retrieves the names of superpowers held by male superheroes. It joins the superhero, hero_power, superpower, and gender tables, filteri

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T3.\"XCL_030\" = T2.\"XCL_013\" INNER JOIN gender AS T4 ON T4.\"XCL_007\" = T1.\"XCL_021\" WHERE T4.\"XCL_008\" = 'Male' LIMIT 5",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:751"
  ]
}
```

### A query that retrieves the primary colour name for superheroes. It joins the superhero table to the colour table twice: once for the primary colour (v

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" INNER JOIN colour AS T3 ON T1.\"XCL_024\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = 'Gold'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:783"
  ]
}
```

### A query that joins the superhero and colour tables to retrieve distinct superhero identifiers where the superhero's height (XCL_028) is between 170 an

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_028\" BETWEEN 170 AND 190 AND T2.\"XCL_006\" = 'No Colour'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:753"
  ]
}
```

### A query that retrieves the value of "XCL_019" from the superhero table for the specific record where "XCL_020" is 'Charles Chandler'. This program act

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_019\" FROM superhero WHERE \"XCL_020\" = 'Charles Chandler'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:833"
  ]
}
```

### A program that joins the superhero, hero_attribute, and attribute tables to identify the superhero with the maximum Speed value. It filters for the 'S

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T3.\"XCL_004\" = 'Speed' ORDER BY T2.\"XCL_011\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:794"
  ]
}
```

### Executes a join between superhero, publisher, and gender tables to filter for female superheroes from Marvel Comics and returns their count. It binds 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN gender AS T3 ON T1.\"XCL_021\" = T3.\"XCL_007\" WHERE T2.\"XCL_015\" = 'Marvel Comics' AND T3.\"XCL_008\" = 'Female'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:823"
  ]
}
```

### A program that retrieves the names of superpowers for a specific superhero by joining the superhero, hero_power, and superpower tables. It filters for

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T1.\"XCL_020\" = 'Helen Parr'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:807"
  ]
}
```

### A query that joins the superhero table (T1) with the colour table (T2) on the foreign key XCL_022 to XCL_005. It filters for superheroes where the att

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_018\" = 75",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:748"
  ]
}
```

### A program that joins the superhero, hero_power, and superpower tables to retrieve the identifiers of superheroes associated with the superpower named 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T3.\"XCL_031\" = 'Death Touch'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:739"
  ]
}
```

### A program that retrieves the names of superpowers for a specific superhero by joining the superhero, hero_power, and superpower tables. It filters for

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T1.\"XCL_020\" = 'Hunter Zolomon'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:780"
  ]
}
```

### A query that joins hero_power and superpower tables to retrieve hero identifiers (XCL_012) where the associated superpower name (XCL_031) is 'Intellig

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_012\" FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.\"XCL_013\" = T2.\"XCL_030\" WHERE T2.\"XCL_031\" = 'Intelligence'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:843"
  ]
}
```

### A query that retrieves superhero identifiers (XCL_028) by joining the superhero and colour tables on XCL_022/XCL_005 and filtering for the color 'Ambe

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_028\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Amber'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:781"
  ]
}
```

### A query that retrieves up to 5 values from superhero.XCL_019 by joining the superhero table with the colour table on XCL_022 = XCL_005, filtered to re

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Blue' LIMIT 5",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:812"
  ]
}
```

### Female Superhero Average Query

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T1.\"XCL_029\") FROM superhero AS T1 INNER JOIN gender AS T2 ON T1.\"XCL_021\" = T2.\"XCL_007\" WHERE T2.\"XCL_008\" = 'Female'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:750"
  ]
}
```

### A query that joins the superhero table (T1) with the publisher table (T2) on T1.XCL_026 = T2.XCL_014. It filters for superheroes where T1.XCL_022 equa

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_019\", T2.\"XCL_015\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_022\" = T1.\"XCL_023\" AND T1.\"XCL_022\" = T1.\"XCL_024\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:773"
  ]
}
```

### Full SQL program that joins the superhero table (T1) with the alignment table (T2) on the key XCL_027 = XCL_001. It filters for rows where T2.XCL_002 

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T1.\"XCL_028\") FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" WHERE T2.\"XCL_002\" = 'Neutral'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:842"
  ]
}
```

### Executes a join between superhero and race tables to filter for the 'Vampire' race and returns the count of matching superhero entries.

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_019\") FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T2.\"XCL_017\" = 'Vampire'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:742"
  ]
}
```

### A query that joins hero_power and superpower tables to retrieve the superpower identifier (XCL_031) for a specific hero (where hero_power.XCL_012 = 56

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_031\" FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.\"XCL_013\" = T2.\"XCL_030\" WHERE T1.\"XCL_012\" = 56",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:754"
  ]
}
```

### A SQL program that joins the superhero table with the publisher table to compute the net difference in superhero counts between Marvel Comics and DC C

```json
{
  "kind": "program",
  "formula": "SELECT SUM(CASE WHEN T2.\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE 0 END) - SUM(CASE WHEN T2.\"XCL_015\" = 'DC Comics' THEN 1 ELSE 0 END) FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:744"
  ]
}
```

### A query that calculates two metrics for superheroes with 'Bad' alignment: 1) The percentage of all superheroes that are 'Bad' (calculated as `COUNT(*)

```json
{
  "kind": "program",
  "formula": "SELECT (CAST(COUNT(*) AS REAL) * 100 / (SELECT COUNT(*) FROM superhero)), CAST(SUM(CASE WHEN T2.\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE 0 END) AS REAL) FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN alignment AS T3 ON T3.\"XCL_001\" = T1.\"XCL_027\" WHERE T3.\"XCL_002\" = 'Bad'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:743"
  ]
}
```

### A query that retrieves the publisher identifier ("XCL_014") from the publisher table where the title ("XCL_015") is exactly 'Star Trek'.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_014\" FROM publisher WHERE \"XCL_015\" = 'Star Trek'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:745"
  ]
}
```

### A query program that retrieves the colour name for a specific superhero. It performs an inner join between the 'superhero' table (T1) and the 'colour'

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_019\" = 'Blackwulf'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:844"
  ]
}
```

### A query that joins superhero, hero_power, superpower, and gender tables to retrieve the gender name for superheroes having the specific power 'Phoenix

```json
{
  "kind": "program",
  "formula": "SELECT T4.\"XCL_008\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" INNER JOIN gender AS T4 ON T1.\"XCL_021\" = T4.\"XCL_007\" WHERE T3.\"XCL_031\" = 'Phoenix Force'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:825"
  ]
}
```

### Full SQL program that joins superhero, hero_power, and superpower tables to filter superheroes by a specific power name ('Super Strength') and a numer

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T3.\"XCL_031\" = 'Super Strength' AND T1.\"XCL_028\" > 200",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:719"
  ]
}
```

### A query that joins the superhero and race tables to retrieve the race identifier (XCL_017) for the superhero named 'A-Bomb' (XCL_019).

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_017\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T1.\"XCL_019\" = 'A-Bomb'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:774"
  ]
}
```

### Full SQL program that joins superhero, gender, and colour tables to compute the percentage of female superheroes with blue colour. Filters for female 

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(CASE WHEN T3.\"XCL_006\" = 'Blue' THEN T1.\"XCL_018\" ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN gender AS T2 ON T1.\"XCL_021\" = T2.\"XCL_007\" INNER JOIN colour AS T3 ON T1.\"XCL_024\" = T3.\"XCL_005\" WHERE T2.\"XCL_008\" = 'Female'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:775"
  ]
}
```

### A SQL program that counts superheroes by joining the superhero table with race and gender tables. It filters for superheroes where the race identifier

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(*) FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" INNER JOIN gender AS T3 ON T3.\"XCL_007\" = T1.\"XCL_021\" WHERE T1.\"XCL_025\" = 21 AND T1.\"XCL_021\" = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:793"
  ]
}
```

### A query that retrieves the superpowers of a specific superhero by joining the superhero, hero_power, and superpower tables. It filters for the superhe

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T1.\"XCL_019\" = 'Abomination'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:792"
  ]
}
```

### Difference in XCL_029 between Emil Blonsky and Charles Chandler

```json
{
  "kind": "program",
  "formula": "SELECT (SELECT \"XCL_029\" FROM superhero WHERE \"XCL_020\" LIKE 'Emil Blonsky') - (SELECT \"XCL_029\" FROM superhero WHERE \"XCL_020\" LIKE 'Charles Chandler') AS CALCULATE",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:790"
  ]
}
```

### A query that retrieves superhero identifiers (XCL_019) by joining the superhero table with the race table on XCL_025 = XCL_016, filtered to include on

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T2.\"XCL_017\" = 'Alien'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:752"
  ]
}
```

### A full SQL program that joins 'hero_power' (T1) and 'superpower' (T2) on 'XCL_013' = 'XCL_030'. It filters for 'hero_power' records where 'XCL_012' = 

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_031\" FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.\"XCL_013\" = T2.\"XCL_030\" WHERE T1.\"XCL_012\" = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:764"
  ]
}
```

### Full SQL program joining superhero, publisher, and race tables. Filters for publisher name 'Dark Horse Comics' and race name not equal to 'Human'. Ret

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T1.\"XCL_028\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN race AS T3 ON T1.\"XCL_025\" = T3.\"XCL_016\" WHERE T2.\"XCL_015\" = 'Dark Horse Comics' AND T3.\"XCL_017\" <> 'Human'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:827"
  ]
}
```

### A query that retrieves the superpower names for a specific superhero by joining the superhero, hero_power, and superpower tables. It filters for the s

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T1.\"XCL_019\" = '3-D Man'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:717"
  ]
}
```

### Full SQL program that joins the superhero table (T1) with the colour table (T2) on the hair colour identifier (XCL_023 = XCL_005), filters for the col

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_023\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Blond'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:735"
  ]
}
```

### Full SQL program joining superhero and gender tables. Filters for male superheroes (T2.XCL_008 = 'Male') where XCL_029 * 100 exceeds 79 times the aver

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN gender AS T2 ON T1.\"XCL_021\" = T2.\"XCL_007\" WHERE T2.\"XCL_008\" = 'Male' AND T1.\"XCL_029\" * 100 > (SELECT AVG(\"XCL_029\") FROM superhero) * 79",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:761"
  ]
}
```

### A query that joins superhero, hero_attribute, attribute, and publisher tables to identify the single superhero with the maximum Durability value, filt

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T3.\"XCL_003\" = T2.\"XCL_010\" INNER JOIN publisher AS T4 ON T4.\"XCL_014\" = T1.\"XCL_026\" WHERE T4.\"XCL_015\" = 'Dark Horse Comics' AND T3.\"XCL_004\" = 'Durability' ORDER BY T2.\"XCL_011\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:769"
  ]
}
```

### A query that retrieves the names of all superheroes who have the 'Wind Control' superpower. It joins the superhero, hero_power, and superpower tables 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T3.\"XCL_031\" = 'Wind Control' ORDER BY T1.\"XCL_019\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:824"
  ]
}
```

### A query that joins the superhero and race tables on XCL_025 = XCL_016, filters for superheroes where XCL_018 is 40, and returns the superhero identifi

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_029\", T2.\"XCL_017\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T1.\"XCL_018\" = 40",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:841"
  ]
}
```

### A program that joins superhero, hero_attribute, and attribute tables to identify the superhero with the maximum Intelligence score. It filters for the

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T3.\"XCL_004\" = 'Intelligence' ORDER BY T2.\"XCL_011\" LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:736"
  ]
}
```

### A query that retrieves the colour name for a specific superhero by joining the superhero table to the colour table on the colour identifier, filtered 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_020\" = 'Abraham Sapien'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:770"
  ]
}
```

### Full SQL program that joins superhero, hero_attribute, and attribute tables to retrieve the attribute value for a specific hero (e.g., 'Hulk') and att

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_011\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T1.\"XCL_019\" = 'Hulk' AND T3.\"XCL_004\" = 'Strength'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:820"
  ]
}
```

### Executes an inner join between superhero and race tables on the race key (XCL_025 to XCL_016), filters superheroes by two specific attribute condition

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_017\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T1.\"XCL_029\" = 108 AND T1.\"XCL_028\" = 188",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:808"
  ]
}
```

### A query that retrieves the XCL_019 identifier for superheroes where either the XCL_022 or XCL_023 attribute corresponds to a color record with XCL_006

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" AND T1.\"XCL_023\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Black'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:782"
  ]
}
```

### A query that joins the superhero and publisher tables to retrieve the publisher name for the specific superhero identified as 'Blue Beetle II'. It fil

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_015\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_019\" = 'Blue Beetle II'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:734"
  ]
}
```

### A program that joins the superhero table (T1) with the colour table (T2) on the foreign key relationship T1.XCL_022 = T2.XCL_005. It orders the result

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" ORDER BY T1.\"XCL_029\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:759"
  ]
}
```

### Full query program that joins superhero, publisher, and gender tables to compute the female percentage for superheroes published by 'George Lucas'. It

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(CASE WHEN T3.\"XCL_008\" = 'Female' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN gender AS T3 ON T1.\"XCL_021\" = T3.\"XCL_007\" WHERE T2.\"XCL_015\" = 'George Lucas'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:834"
  ]
}
```

### A query that resolves the colour of a specific superhero by name. It joins the 'superhero' table (T1) with the 'colour' table (T2) using the foreign k

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_020\" = 'Karen Beecher-Duncan'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:806"
  ]
}
```

### A query that joins the superhero and publisher tables to retrieve the publisher names for a specific set of superheroes identified by the names 'Hawkm

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_015\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_019\" IN ('Hawkman', 'Karate Kid', 'Speedy')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:798"
  ]
}
```

### Computes the rank of superheroes by height in descending order, restricted to those published by 'Marvel Comics'. The grain is one row per superhero, 

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_019\", \"XCL_028\", RANK() OVER (ORDER BY \"XCL_028\" DESC) AS HeightRank FROM superhero INNER JOIN publisher ON superhero.\"XCL_026\" = publisher.\"XCL_014\" WHERE publisher.\"XCL_015\" = 'Marvel Comics'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:726"
  ]
}
```

### A program that joins the superhero table with the colour table twice to filter for superheroes with blue eyes and blond hair, returning their identifi

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" INNER JOIN colour AS T3 ON T1.\"XCL_023\" = T3.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Blue' AND T3.\"XCL_006\" = 'Blond'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:724"
  ]
}
```

### A query that joins superhero, colour, and publisher tables to calculate the count and popularity rank of eye colors for Marvel Comics superheroes.

```json
{
  "kind": "program",
  "formula": "SELECT colour.\"XCL_006\" AS EyeColor, COUNT(superhero.\"XCL_018\") AS Count, RANK() OVER (ORDER BY COUNT(superhero.\"XCL_018\") DESC) AS PopularityRank FROM superhero INNER JOIN colour ON superhero.\"XCL_022\" = colour.\"XCL_005\" INNER JOIN publisher ON superhero.\"XCL_026\" = publisher.\"XCL_014\" WHERE publisher.\"XCL_015\" = 'Marvel Comics' GROUP BY colour.\"XCL_006\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:728"
  ]
}
```

### A query that retrieves the superpowers of a specific superhero by joining the superhero, hero_power, and superpower tables. It filters for the superhe

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T1.\"XCL_019\" = 'Deathlok'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:749"
  ]
}
```

### Full SQL program that joins hero_attribute and attribute tables, filters for 'Strength' attributes with the maximum XCL_011 value, and returns the cou

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_009\") FROM hero_attribute AS T1 INNER JOIN attribute AS T2 ON T1.\"XCL_010\" = T2.\"XCL_003\" WHERE T2.\"XCL_004\" = 'Strength' AND T1.\"XCL_011\" = (SELECT MAX(\"XCL_011\") FROM hero_attribute)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:786"
  ]
}
```

### A SQL program that joins the 'superhero' table (T1) with the 'publisher' table (T2) on the foreign key relationship T1."XCL_026" = T2."XCL_014". It fi

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T1.\"XCL_028\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T2.\"XCL_015\" = 'Marvel Comics'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:729"
  ]
}
```

### A query that joins the superhero and race tables on XCL_025 = XCL_016, filters for race XCL_017 = 'Vampire', and returns the superhero identifier XCL_

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_020\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T2.\"XCL_017\" = 'Vampire'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:784"
  ]
}
```

### A query that joins the superhero and race tables on XCL_025 = XCL_016 to retrieve the superhero's XCL_019 and race's XCL_017, filtered specifically fo

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_019\", T2.\"XCL_017\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T1.\"XCL_020\" = 'Charles Chandler'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:776"
  ]
}
```

### A SQL program that joins the 'superhero' table (T1) with the 'publisher' table (T2) on the publisher ID (T1."XCL_026" = T2."XCL_014") to compute the n

```json
{
  "kind": "program",
  "formula": "SELECT SUM(CASE WHEN T2.\"XCL_015\" = 'DC Comics' THEN 1 ELSE 0 END) - SUM(CASE WHEN T2.\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE 0 END) FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:829"
  ]
}
```

### A query that retrieves the alignment and superpower names for a specific superhero. It joins the superhero table to hero_power, superpower, and alignm

```json
{
  "kind": "program",
  "formula": "SELECT T4.\"XCL_002\", T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T3.\"XCL_030\" = T2.\"XCL_013\" INNER JOIN alignment AS T4 ON T1.\"XCL_027\" = T4.\"XCL_001\" WHERE T1.\"XCL_019\" = 'Atom IV'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:811"
  ]
}
```

### Superhero Aggregate Query

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(\"XCL_028\") AS REAL) / COUNT(\"XCL_018\") FROM superhero",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:791"
  ]
}
```

### Full SQL program that joins the superhero table to alignment (on XCL_027 = XCL_001) and gender (on XCL_021 = XCL_007), filters for alignment 'Good' an

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" INNER JOIN gender AS T3 ON T1.\"XCL_021\" = T3.\"XCL_007\" WHERE T2.\"XCL_002\" = 'Good' AND T3.\"XCL_008\" = 'Female'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:815"
  ]
}
```

### Full SQL program that joins the superhero, publisher, and alignment tables. It filters for the publisher 'Marvel Comics' and computes the ratio of sup

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(CASE WHEN T3.\"XCL_002\" = 'Good' THEN T1.\"XCL_018\" ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN alignment AS T3 ON T1.\"XCL_027\" = T3.\"XCL_001\" WHERE T2.\"XCL_015\" = 'Marvel Comics'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:835"
  ]
}
```

### A query that joins superhero, hero_attribute, and race tables to identify the race of the superhero with the maximum value in hero_attribute.XCL_011. 

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_017\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN race AS T3 ON T1.\"XCL_025\" = T3.\"XCL_016\" ORDER BY T2.\"XCL_011\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:810"
  ]
}
```

### A full SQL program that selects "XCL_020" from the "superhero" table, applying a filter where "XCL_019" is 'Alien'. This represents the complete compu

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_020\" FROM superhero WHERE \"XCL_019\" = 'Alien'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:838"
  ]
}
```

### A query that retrieves the XCL_020 identifier for superheroes by joining the superhero table with the race table on XCL_025 = XCL_016 and filtering fo

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_020\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T2.\"XCL_017\" = 'Demi-God'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:755"
  ]
}
```

### A full SQL program that joins the superhero, colour, and hero_attribute tables. It filters for heroes where the attribute value (XCL_011) equals 100 a

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_024\" = T2.\"XCL_005\" INNER JOIN hero_attribute AS T3 ON T1.\"XCL_018\" = T3.\"XCL_009\" WHERE T3.\"XCL_011\" = 100",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:814"
  ]
}
```

### Full SQL program that joins the superhero table (T1) with the publisher table (T2) on the publisher ID (XCL_026 = XCL_014). It filters superheroes by 

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(CASE WHEN T2.\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_028\" BETWEEN 150 AND 180",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:760"
  ]
}
```

### Get Superpowers for Hero

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T1.\"XCL_019\" = 'Ajax'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:821"
  ]
}
```

### Executes an inner join between hero_power (T1) and superhero (T2) on the key columns XCL_012 and XCL_018. Filters the superhero table for the name 'Am

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_013\") FROM hero_power AS T1 INNER JOIN superhero AS T2 ON T1.\"XCL_012\" = T2.\"XCL_018\" WHERE T2.\"XCL_019\" = 'Amazo'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:779"
  ]
}
```

### A query that retrieves superhero identifiers (XCL_019) where the superhero is associated with two distinct color records: one with color name 'Blue' (

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" INNER JOIN colour AS T3 ON T1.\"XCL_023\" = T3.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Blue' AND T3.\"XCL_006\" = 'Brown'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:797"
  ]
}
```

### A query that retrieves the "XCL_009" value from the "hero_attribute" table for the record having the minimum "XCL_011" value. It uses a subquery to fi

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_009\" FROM hero_attribute WHERE \"XCL_011\" = (SELECT MIN(\"XCL_011\") FROM hero_attribute)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:837"
  ]
}
```

### A query program that retrieves XCL_019 from the superhero table, constrained to rows where XCL_018 is 294. This represents a point lookup or filter op

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_019\" FROM superhero WHERE \"XCL_018\" = 294",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:804"
  ]
}
```

### A query that retrieves the XCL_030 value from the superpower table filtered to records where XCL_031 is 'Cryokinesis'. Returns a single row (or multip

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_030\" FROM superpower WHERE \"XCL_031\" = 'Cryokinesis'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:803"
  ]
}
```

### A query that identifies superheroes with a high volume of associated powers. It joins the superhero table to the hero_power table on the superhero ID 

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T1.\"XCL_020\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" GROUP BY T1.\"XCL_020\" HAVING COUNT(T2.\"XCL_013\") > 15",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:720"
  ]
}
```

### Full SQL program that counts entries in the superhero table where the XCL_020 field matches the pattern 'John%'. Serves as the executable unit for thi

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_018\") FROM superhero WHERE \"XCL_020\" LIKE 'John%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:836"
  ]
}
```

### A SQL program that retrieves the attribute value (XCL_011) for the hero named 'Aquababy'. It performs an inner join between the 'superhero' table (T1)

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_011\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" WHERE T1.\"XCL_019\" = 'Aquababy'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:840"
  ]
}
```

### A query that joins the superhero, race, and colour tables to identify distinct hair colours. It filters for superheroes with a height of 185 and a rac

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT T3.\"XCL_006\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" INNER JOIN colour AS T3 ON T1.\"XCL_023\" = T3.\"XCL_005\" WHERE T1.\"XCL_028\" = 185 AND T2.\"XCL_017\" = 'Human'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:758"
  ]
}
```

### A full SQL program that joins the superhero table (T1) with the colour table (T2) on T1.XCL_024 = T2.XCL_005. It computes a single aggregate ratio: th

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(*) AS REAL) / SUM(CASE WHEN T2.\"XCL_005\" = 1 THEN 1 ELSE 0 END) FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_024\" = T2.\"XCL_005\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:767"
  ]
}
```

### Full SQL program retrieving the IDs of superheroes whose 'Durability' attribute score is less than 50. Uses an EXISTS subquery to filter the superhero

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_019\" FROM superhero AS T1 WHERE EXISTS(SELECT 1 FROM hero_attribute AS T2 INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T3.\"XCL_004\" = 'Durability' AND T2.\"XCL_011\" < 50 AND T1.\"XCL_018\" = T2.\"XCL_009\")",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:738"
  ]
}
```

### Full SQL program that joins the superhero table with the colour table on the colour identifier to compute the proportion of superheroes having the col

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(CASE WHEN T2.\"XCL_006\" = 'Blue' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:800"
  ]
}
```

### Executes a join between the superhero and publisher tables on the publisher identifier (XCL_026 = XCL_014) and filters for the specific publisher name

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T2.\"XCL_015\" = 'Marvel Comics'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:725"
  ]
}
```

### A SQL program that calculates the average value of the XCL_011 field from the hero_attribute table. It returns a single row containing the computed av

```json
{
  "kind": "program",
  "formula": "SELECT AVG(\"XCL_011\") FROM hero_attribute",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:746"
  ]
}
```

### A query that joins the superhero table with colour, race, and gender tables to retrieve the race name for superheroes filtered by blue eye colour and 

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_017\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_023\" = T2.\"XCL_005\" INNER JOIN race AS T3 ON T1.\"XCL_025\" = T3.\"XCL_016\" INNER JOIN gender AS T4 ON T1.\"XCL_021\" = T4.\"XCL_007\" WHERE T2.\"XCL_006\" = 'Blue' AND T4.\"XCL_008\" = 'Male'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:817"
  ]
}
```

### Full SQL program that joins the superhero table (T1) with the publisher table (T2) on the foreign key relationship T1.XCL_026 = T2.XCL_014. It filters

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T2.\"XCL_015\" = 'Dark Horse Comics'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:768"
  ]
}
```

### A program that retrieves the identifiers of all superheroes capable of flight. It joins the superhero, hero_power, and superpower tables to filter for

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T3.\"XCL_031\" = 'Flight'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:771"
  ]
}
```

### A query that retrieves XCL_020 from the superhero table where the associated colour (joined via XCL_022 to colour.XCL_005) is 'Brown' (colour.XCL_006)

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_020\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_029\" < 100 AND T2.\"XCL_006\" = 'Brown'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:839"
  ]
}
```

### Female Dark Horse Comics Superhero Details

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_022\", T1.\"XCL_023\", T1.\"XCL_024\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T2.\"XCL_014\" = T1.\"XCL_026\" INNER JOIN gender AS T3 ON T3.\"XCL_007\" = T1.\"XCL_021\" WHERE T2.\"XCL_015\" = 'Dark Horse Comics' AND T3.\"XCL_008\" = 'Female'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:772"
  ]
}
```

### A query that joins hero_power (T1) to superpower (T2) on hero_power.XCL_013 = superpower.XCL_030. It groups the results by superpower.XCL_031 and orde

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_031\" FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.\"XCL_013\" = T2.\"XCL_030\" GROUP BY T2.\"XCL_031\" ORDER BY COUNT(T1.\"XCL_012\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:762"
  ]
}
```

### Superhero Gender Ratio Query

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(CASE WHEN T2.\"XCL_008\" = 'Male' THEN T1.\"XCL_018\" ELSE NULL END) AS REAL) / COUNT(CASE WHEN T2.\"XCL_008\" = 'Female' THEN T1.\"XCL_018\" ELSE NULL END) FROM superhero AS T1 INNER JOIN gender AS T2 ON T1.\"XCL_021\" = T2.\"XCL_007\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:801"
  ]
}
```

### Full SQL program joining hero_attribute, attribute, and superhero tables. It filters for the specific attribute 'Speed' and a value of 100, then count

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T3.\"XCL_019\") FROM hero_attribute AS T1 INNER JOIN attribute AS T2 ON T1.\"XCL_010\" = T2.\"XCL_003\" INNER JOIN superhero AS T3 ON T1.\"XCL_009\" = T3.\"XCL_018\" WHERE T2.\"XCL_004\" = 'Speed' AND T1.\"XCL_011\" = 100",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:828"
  ]
}
```

### A SQL program that joins the superhero table (T1) with the alignment table (T2) on XCL_027 = XCL_001. It filters for alignments where XCL_002 is 'Neut

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" WHERE T2.\"XCL_002\" = 'Neutral'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:785"
  ]
}
```

### Full SQL program that selects the count of XCL_018 from the superhero table, restricted to rows where XCL_020 is NULL.

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_018\") FROM superhero WHERE \"XCL_020\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:747"
  ]
}
```

### Filtered Distinct XCL_020 Query

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_020\" FROM superhero WHERE NOT \"XCL_020\" IS NULL AND (\"XCL_029\" IS NULL OR \"XCL_029\" = 0)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:805"
  ]
}
```

### A query that joins the superhero and publisher tables to retrieve the publisher name for a specific superhero. It filters the superhero table where co

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_015\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_018\" = 38",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:809"
  ]
}
```

### Full SQL program that joins the superhero table with alignment and colour tables. It filters for superheroes where the alignment name is 'Bad' and the

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" INNER JOIN colour AS T3 ON T1.\"XCL_024\" = T3.\"XCL_005\" WHERE T2.\"XCL_002\" = 'Bad' AND T3.\"XCL_006\" = 'Green'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:822"
  ]
}
```

### Alien superhero XCL_029 to XCL_018 ratio query

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(T1.\"XCL_029\") AS REAL) / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T2.\"XCL_017\" = 'Alien'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:789"
  ]
}
```

### A query that joins the superhero table with the hero_attribute table to retrieve attribute values for the superhero identified by the name 'Abominatio

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_011\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" WHERE T1.\"XCL_019\" = 'Abomination'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:763"
  ]
}
```

### A query that retrieves the attribute names and their corresponding values for a specific superhero by joining the superhero, hero_attribute, and attri

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_004\", T2.\"XCL_011\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T1.\"XCL_019\" = '3-D Man'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:796"
  ]
}
```

### A query that joins the superhero and publisher tables to find the superhero (identified by "XCL_019") published by 'DC Comics' (where publisher."XCL_0

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T2.\"XCL_015\" = 'DC Comics' ORDER BY T1.\"XCL_029\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:826"
  ]
}
```

### Full SQL program that joins superhero, hero_attribute, attribute, and gender tables. It filters for the 'Strength' attribute, a hero_attribute value o

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" INNER JOIN gender AS T4 ON T1.\"XCL_021\" = T4.\"XCL_007\" WHERE T3.\"XCL_004\" = 'Strength' AND T2.\"XCL_011\" = 100 AND T4.\"XCL_008\" = 'Female'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:740"
  ]
}
```

### A query that identifies the single superhero with the most powers. It joins the 'superhero' table (T1) with the 'hero_power' table (T2) on the superhe

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" GROUP BY T1.\"XCL_019\" ORDER BY COUNT(T2.\"XCL_012\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:741"
  ]
}
```

### A SQL program that joins 'hero_attribute', 'superhero', and 'alignment' tables to calculate the average of 'XCL_011' for heroes with a 'Neutral' align

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T1.\"XCL_011\") FROM hero_attribute AS T1 INNER JOIN superhero AS T2 ON T1.\"XCL_009\" = T2.\"XCL_018\" INNER JOIN alignment AS T3 ON T2.\"XCL_027\" = T3.\"XCL_001\" WHERE T3.\"XCL_002\" = 'Neutral'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:813"
  ]
}
```

### Executes an inner join between hero_power (T1) and superpower (T2) on the foreign key relationship T1.XCL_013 = T2.XCL_030. Filters the results to inc

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_012\") FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.\"XCL_013\" = T2.\"XCL_030\" WHERE T2.\"XCL_031\" = 'Stealth'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:765"
  ]
}
```

### A full SQL program that joins the superhero, publisher, and gender tables to compute the proportion of female superheroes associated with Marvel Comic

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(CASE WHEN T2.\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN gender AS T3 ON T1.\"XCL_021\" = T3.\"XCL_007\" WHERE T3.\"XCL_008\" = 'Female'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:788"
  ]
}
```

### A query that joins the superhero table with the colour table to retrieve the colour name for a specific superhero. It filters for the superhero named 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_019\" = 'Abomination'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:831"
  ]
}
```

### A program that joins the superhero, hero_power, and superpower tables to retrieve the identifiers of superheroes associated with the superpower named 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T3.\"XCL_031\" = 'Adaptation'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:778"
  ]
}
```

### "publisher"."XCL_015" = 'Marvel Comics'

```json
{
  "kind": "predicate",
  "formula": "\"publisher\".\"XCL_015\" = 'Marvel Comics'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T2.\"XCL_015\" = 'Marvel Comics'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:725"
  ]
}
```

### Distinct values of the superhero identifier column (XCL_019) for superheroes who have a height between 170 and 190 and are associated with the 'No Col

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_028\" BETWEEN 170 AND 190 AND T2.\"XCL_006\" = 'No Colour'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:753"
  ]
}
```

### "colour"."XCL_006" = 'Blue' AND "colour"."XCL_006" = 'Blond'

```json
{
  "kind": "predicate",
  "formula": "\"colour\".\"XCL_006\" = 'Blue' AND \"colour\".\"XCL_006\" = 'Blond'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" INNER JOIN colour AS T3 ON T1.\"XCL_023\" = T3.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Blue' AND T3.\"XCL_006\" = 'Blond'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:724"
  ]
}
```

### Max Hero Attribute Value

```json
{
  "kind": "metric",
  "formula": "MAX(\"hero_attribute\".\"XCL_011\")",
  "grain": [],
  "population_scope": "SELECT MAX(\"XCL_011\") FROM hero_attribute",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MAX(\"r0\".\"XCL_011\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "hero_attribute"
      }
    ],
    "scope_sql": "SELECT MAX(\"r0\".\"XCL_011\") AS \"value\" FROM hero_attribute AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:786"
  ]
}
```

### "race"."XCL_017" = 'Vampire'

```json
{
  "kind": "predicate",
  "formula": "\"race\".\"XCL_017\" = 'Vampire'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_020\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T2.\"XCL_017\" = 'Vampire'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:784"
  ]
}
```

### Counts the number of superhero records (identified by XCL_018) that are associated with the publisher 'DC Comics' (identified by XCL_015). The grain i

```json
{
  "kind": "metric",
  "formula": "COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T2.\"XCL_015\" = 'DC Comics'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\" WHERE \"r1\".\"XCL_015\" = 'DC Comics'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:731"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T3.\"XCL_003\" = T2.\"XCL_010\" INNER JOIN publisher AS T4 ON T4.\"XCL_014\" = T1.\"XCL_026\" WHERE T4.\"XCL_015\" = 'Dark Horse Comics' AND T3.\"XCL_004\" = 'Durability' ORDER BY T2.\"XCL_011\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:769"
  ]
}
```

### The identifier (XCL_019) of the single superhero with the highest recorded Speed attribute value. The result is a single row representing the top-rank

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T3.\"XCL_004\" = 'Speed' ORDER BY T2.\"XCL_011\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:794"
  ]
}
```

### Count of Max Strength Attributes

```json
{
  "kind": "metric",
  "formula": "COUNT(\"hero_attribute\".\"XCL_009\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_009\") FROM hero_attribute AS T1 INNER JOIN attribute AS T2 ON T1.\"XCL_010\" = T2.\"XCL_003\" WHERE T2.\"XCL_004\" = 'Strength' AND T1.\"XCL_011\" = (SELECT MAX(\"XCL_011\") FROM hero_attribute)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:786"
  ]
}
```

### Aggregates the count of superhero records (identified by XCL_018) that are joined to an alignment of 'Bad' and a colour of 'Green'. The grain is a sin

```json
{
  "kind": "metric",
  "formula": "COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" INNER JOIN colour AS T3 ON T1.\"XCL_024\" = T3.\"XCL_005\" WHERE T2.\"XCL_002\" = 'Bad' AND T3.\"XCL_006\" = 'Green'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "alignment"
      },
      {
        "role": "r2",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN alignment AS \"r1\" ON \"r0\".\"XCL_027\" = \"r1\".\"XCL_001\" INNER JOIN colour AS \"r2\" ON \"r0\".\"XCL_024\" = \"r2\".\"XCL_005\" WHERE \"r1\".\"XCL_002\" = 'Bad' AND \"r2\".\"XCL_006\" = 'Green'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:822"
  ]
}
```

### Alignment Identifier

```json
{
  "kind": "binding",
  "formula": "\"alignment\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_017\", T3.\"XCL_002\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" INNER JOIN alignment AS T3 ON T1.\"XCL_027\" = T3.\"XCL_001\" WHERE T1.\"XCL_019\" = 'Cameron Hicks'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_002\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "race"
      },
      {
        "role": "r2",
        "physical_table": "alignment"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_002\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN race AS \"r1\" ON \"r0\".\"XCL_025\" = \"r1\".\"XCL_016\" INNER JOIN alignment AS \"r2\" ON \"r0\".\"XCL_027\" = \"r2\".\"XCL_001\" WHERE \"r0\".\"XCL_019\" = 'Cameron Hicks'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:787"
  ]
}
```

### Aggregates the count of rows in the superhero table where the column XCL_020 is NULL. The metric counts the values in column XCL_018 for this filtered

```json
{
  "kind": "metric",
  "formula": "COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_018\") FROM superhero WHERE \"XCL_020\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" WHERE \"r0\".\"XCL_020\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:747"
  ]
}
```

### "colour"."XCL_006" = 'Blue'

```json
{
  "kind": "predicate",
  "formula": "\"colour\".\"XCL_006\" = 'Blue'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Blue'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:721"
  ]
}
```

### Superpower Name

```json
{
  "kind": "binding",
  "formula": "\"superpower\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T3.\"XCL_030\" = T2.\"XCL_013\" INNER JOIN gender AS T4 ON T4.\"XCL_007\" = T1.\"XCL_021\" WHERE T4.\"XCL_008\" = 'Male' LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:751"
  ]
}
```

### Superpower Name

```json
{
  "kind": "binding",
  "formula": "\"superpower\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T1.\"XCL_019\" = 'Ajax'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_031\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_power"
      },
      {
        "role": "r2",
        "physical_table": "superpower"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_031\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_power AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_012\" INNER JOIN superpower AS \"r2\" ON \"r1\".\"XCL_013\" = \"r2\".\"XCL_030\" WHERE \"r0\".\"XCL_019\" = 'Ajax'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:821"
  ]
}
```

### "superhero"."XCL_020" = 'Karen Beecher-Duncan'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_020\" = 'Karen Beecher-Duncan'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_020\" = 'Karen Beecher-Duncan'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:806"
  ]
}
```

### "publisher"."XCL_015" = 'Marvel Comics'

```json
{
  "kind": "predicate",
  "formula": "\"publisher\".\"XCL_015\" = 'Marvel Comics'",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_028\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T2.\"XCL_015\" = 'Marvel Comics'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:729"
  ]
}
```

### Colour Name

```json
{
  "kind": "binding",
  "formula": "\"colour\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_018\" = 75",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_006\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN colour AS \"r1\" ON \"r0\".\"XCL_022\" = \"r1\".\"XCL_005\" WHERE \"r0\".\"XCL_018\" = 75",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:748"
  ]
}
```

### Superpower Identifier

```json
{
  "kind": "binding",
  "formula": "\"superpower\".\"XCL_030\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_030\" FROM superpower WHERE \"XCL_031\" = 'Cryokinesis'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_030\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superpower"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_030\" AS \"value\" FROM superpower AS \"r0\" WHERE \"r0\".\"XCL_031\" = 'Cryokinesis'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:803"
  ]
}
```

### "superhero"."XCL_019" = 'Hulk' AND "attribute"."XCL_004" = 'Strength'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = 'Hulk' AND \"attribute\".\"XCL_004\" = 'Strength'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T1.\"XCL_019\" = 'Hulk' AND T3.\"XCL_004\" = 'Strength'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:820"
  ]
}
```

### "superhero"."XCL_019" = 'Apocalypse'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = 'Apocalypse'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_024\" = T2.\"XCL_005\" WHERE T1.\"XCL_019\" = 'Apocalypse'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:722"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Blue' LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:812"
  ]
}
```

### "alignment"."XCL_002" = 'Bad' AND "colour"."XCL_006" = 'Green'

```json
{
  "kind": "predicate",
  "formula": "\"alignment\".\"XCL_002\" = 'Bad' AND \"colour\".\"XCL_006\" = 'Green'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" INNER JOIN colour AS T3 ON T1.\"XCL_024\" = T3.\"XCL_005\" WHERE T2.\"XCL_002\" = 'Bad' AND T3.\"XCL_006\" = 'Green'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:822"
  ]
}
```

### Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"race\".\"XCL_017\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_017\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T1.\"XCL_019\" = 'A-Bomb'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_017\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "race"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_017\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN race AS \"r1\" ON \"r0\".\"XCL_025\" = \"r1\".\"XCL_016\" WHERE \"r0\".\"XCL_019\" = 'A-Bomb'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:774"
  ]
}
```

### "colour"."XCL_006" = 'Black'

```json
{
  "kind": "predicate",
  "formula": "\"colour\".\"XCL_006\" = 'Black'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" AND T1.\"XCL_023\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Black'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:782"
  ]
}
```

### Publisher Name

```json
{
  "kind": "binding",
  "formula": "\"publisher\".\"XCL_015\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_015\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN hero_attribute AS T3 ON T1.\"XCL_018\" = T3.\"XCL_009\" INNER JOIN attribute AS T4 ON T3.\"XCL_010\" = T4.\"XCL_003\" WHERE T4.\"XCL_004\" = 'Speed' ORDER BY T3.\"XCL_011\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:732"
  ]
}
```

### "superhero"."XCL_029" = 169

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_029\" = 169",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_017\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T1.\"XCL_029\" = 169",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:757"
  ]
}
```

### "publisher"."XCL_014" = 1

```json
{
  "kind": "predicate",
  "formula": "\"publisher\".\"XCL_014\" = 1",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T2.\"XCL_014\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:799"
  ]
}
```

### "superhero"."XCL_019" = 'Abomination'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = 'Abomination'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_019\" = 'Abomination'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:831"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_019\" FROM superhero AS T1 WHERE EXISTS(SELECT 1 FROM hero_attribute AS T2 INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T3.\"XCL_004\" = 'Durability' AND T2.\"XCL_011\" < 50 AND T1.\"XCL_018\" = T2.\"XCL_009\")",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:738"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_028\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_028\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Amber'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_028\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_028\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN colour AS \"r1\" ON \"r0\".\"XCL_022\" = \"r1\".\"XCL_005\" WHERE \"r1\".\"XCL_006\" = 'Amber'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:781"
  ]
}
```

### The value of the column "XCL_009" from the row in "hero_attribute" where "XCL_011" equals the global minimum of "XCL_011". Returns the specific attrib

```json
{
  "kind": "binding",
  "formula": "\"hero_attribute\".\"XCL_009\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_009\" FROM hero_attribute WHERE \"XCL_011\" = (SELECT MIN(\"XCL_011\") FROM hero_attribute)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:837"
  ]
}
```

### "hero_power"."XCL_012" = 1

```json
{
  "kind": "predicate",
  "formula": "\"hero_power\".\"XCL_012\" = 1",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_031\" FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.\"XCL_013\" = T2.\"XCL_030\" WHERE T1.\"XCL_012\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:764"
  ]
}
```

### Aggregates the total number of rows in the hero_power table (T1) that are joined to the superhero 'Amazo' via the foreign key relationship XCL_012 = X

```json
{
  "kind": "metric",
  "formula": "COUNT(\"hero_power\".\"XCL_013\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_013\") FROM hero_power AS T1 INNER JOIN superhero AS T2 ON T1.\"XCL_012\" = T2.\"XCL_018\" WHERE T2.\"XCL_019\" = 'Amazo'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_013\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "hero_power"
      },
      {
        "role": "r1",
        "physical_table": "superhero"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_013\") AS \"value\" FROM hero_power AS \"r0\" INNER JOIN superhero AS \"r1\" ON \"r0\".\"XCL_012\" = \"r1\".\"XCL_018\" WHERE \"r1\".\"XCL_019\" = 'Amazo'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:779"
  ]
}
```

### Most Common Superpower

```json
{
  "kind": "binding",
  "formula": "\"superpower\".\"XCL_031\"",
  "grain": [
    "\"superpower\".\"XCL_031\""
  ],
  "population_scope": "SELECT T2.\"XCL_031\" FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.\"XCL_013\" = T2.\"XCL_030\" GROUP BY T2.\"XCL_031\" ORDER BY COUNT(T1.\"XCL_012\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:762"
  ]
}
```

### Superhero Name

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T3.\"XCL_031\" = 'Wind Control' ORDER BY T1.\"XCL_019\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_019\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_power"
      },
      {
        "role": "r2",
        "physical_table": "superpower"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_019\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_power AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_012\" INNER JOIN superpower AS \"r2\" ON \"r1\".\"XCL_013\" = \"r2\".\"XCL_030\" WHERE \"r2\".\"XCL_031\" = 'Wind Control'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:824"
  ]
}
```

### Superpower Name

```json
{
  "kind": "binding",
  "formula": "\"superpower\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T1.\"XCL_019\" = '3-D Man'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_031\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_power"
      },
      {
        "role": "r2",
        "physical_table": "superpower"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_031\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_power AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_012\" INNER JOIN superpower AS \"r2\" ON \"r1\".\"XCL_013\" = \"r2\".\"XCL_030\" WHERE \"r0\".\"XCL_019\" = '3-D Man'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:717"
  ]
}
```

### Average XCL_029 across all superheroes

```json
{
  "kind": "metric",
  "formula": "AVG(\"superhero\".\"XCL_029\")",
  "grain": [],
  "population_scope": "SELECT AVG(\"XCL_029\") FROM superhero",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_029\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_029\") AS \"value\" FROM superhero AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:761"
  ]
}
```

### Count of Bad Marvel Superheroes

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"publisher\".\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE 0 END) AS REAL)",
  "grain": [],
  "population_scope": "SELECT (CAST(COUNT(*) AS REAL) * 100 / (SELECT COUNT(*) FROM superhero)), CAST(SUM(CASE WHEN T2.\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE 0 END) AS REAL) FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN alignment AS T3 ON T3.\"XCL_001\" = T1.\"XCL_027\" WHERE T3.\"XCL_002\" = 'Bad'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r1\".\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE 0 END) AS REAL)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      },
      {
        "role": "r2",
        "physical_table": "alignment"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r1\".\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE 0 END) AS REAL) AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\" INNER JOIN alignment AS \"r2\" ON \"r2\".\"XCL_001\" = \"r0\".\"XCL_027\" WHERE \"r2\".\"XCL_002\" = 'Bad'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:743"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_019\" FROM superhero WHERE \"XCL_020\" = 'Charles Chandler'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_019\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_019\" AS \"value\" FROM superhero AS \"r0\" WHERE \"r0\".\"XCL_020\" = 'Charles Chandler'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:833"
  ]
}
```

### Superpower XCL_031

```json
{
  "kind": "binding",
  "formula": "\"superpower\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T1.\"XCL_028\" * 100 > (SELECT AVG(\"XCL_028\") FROM superhero) * 80",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:845"
  ]
}
```

### "superhero"."XCL_025" = 21 AND "superhero"."XCL_021" = 1

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_025\" = 21 AND \"superhero\".\"XCL_021\" = 1",
  "grain": [],
  "population_scope": "SELECT COUNT(*) FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" INNER JOIN gender AS T3 ON T3.\"XCL_007\" = T1.\"XCL_021\" WHERE T1.\"XCL_025\" = 21 AND T1.\"XCL_021\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:793"
  ]
}
```

### "superhero"."XCL_019" = '3-D Man'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = '3-D Man'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_004\", T2.\"XCL_011\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T1.\"XCL_019\" = '3-D Man'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:796"
  ]
}
```

### "race"."XCL_017" = 'Vampire'

```json
{
  "kind": "predicate",
  "formula": "\"race\".\"XCL_017\" = 'Vampire'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_019\") FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T2.\"XCL_017\" = 'Vampire'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:742"
  ]
}
```

### "publisher"."XCL_015" = 'Marvel Comics' AND "colour"."XCL_006" = 'Gold'

```json
{
  "kind": "predicate",
  "formula": "\"publisher\".\"XCL_015\" = 'Marvel Comics' AND \"colour\".\"XCL_006\" = 'Gold'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN colour AS T3 ON T1.\"XCL_022\" = T3.\"XCL_005\" WHERE T2.\"XCL_015\" = 'Marvel Comics' AND T3.\"XCL_006\" = 'Gold'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:733"
  ]
}
```

### "colour"."XCL_006" = 'Gold'

```json
{
  "kind": "predicate",
  "formula": "\"colour\".\"XCL_006\" = 'Gold'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" INNER JOIN colour AS T3 ON T1.\"XCL_024\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = 'Gold'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:783"
  ]
}
```

### "superhero"."XCL_019" = 'Ajax'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = 'Ajax'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T1.\"XCL_019\" = 'Ajax'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:821"
  ]
}
```

### Average XCL_011

```json
{
  "kind": "metric",
  "formula": "AVG(\"hero_attribute\".\"XCL_011\")",
  "grain": [],
  "population_scope": "SELECT AVG(\"XCL_011\") FROM hero_attribute",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_011\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "hero_attribute"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_011\") AS \"value\" FROM hero_attribute AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:746"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_020\"",
  "grain": [
    "\"superhero\".\"XCL_020\""
  ],
  "population_scope": "SELECT DISTINCT T1.\"XCL_020\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" GROUP BY T1.\"XCL_020\" HAVING COUNT(T2.\"XCL_013\") > 15",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:720"
  ]
}
```

### Gender Name

```json
{
  "kind": "binding",
  "formula": "\"gender\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T4.\"XCL_008\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" INNER JOIN gender AS T4 ON T1.\"XCL_021\" = T4.\"XCL_007\" WHERE T3.\"XCL_031\" = 'Phoenix Force'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r3\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_power"
      },
      {
        "role": "r2",
        "physical_table": "superpower"
      },
      {
        "role": "r3",
        "physical_table": "gender"
      }
    ],
    "scope_sql": "SELECT \"r3\".\"XCL_008\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_power AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_012\" INNER JOIN superpower AS \"r2\" ON \"r1\".\"XCL_013\" = \"r2\".\"XCL_030\" INNER JOIN gender AS \"r3\" ON \"r0\".\"XCL_021\" = \"r3\".\"XCL_007\" WHERE \"r2\".\"XCL_031\" = 'Phoenix Force'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:825"
  ]
}
```

### "publisher"."XCL_015" = 'Dark Horse Comics' AND "attribute"."XCL_004" = 'Durability'

```json
{
  "kind": "predicate",
  "formula": "\"publisher\".\"XCL_015\" = 'Dark Horse Comics' AND \"attribute\".\"XCL_004\" = 'Durability'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T3.\"XCL_003\" = T2.\"XCL_010\" INNER JOIN publisher AS T4 ON T4.\"XCL_014\" = T1.\"XCL_026\" WHERE T4.\"XCL_015\" = 'Dark Horse Comics' AND T3.\"XCL_004\" = 'Durability' ORDER BY T2.\"XCL_011\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:769"
  ]
}
```

### "publisher"."XCL_015" = 'Marvel Comics'

```json
{
  "kind": "predicate",
  "formula": "\"publisher\".\"XCL_015\" = 'Marvel Comics'",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T3.\"XCL_002\" = 'Good' THEN T1.\"XCL_018\" ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN alignment AS T3 ON T1.\"XCL_027\" = T3.\"XCL_001\" WHERE T2.\"XCL_015\" = 'Marvel Comics'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:835"
  ]
}
```

### "superhero"."XCL_020" = 'Charles Chandler'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_020\" = 'Charles Chandler'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\", T2.\"XCL_017\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T1.\"XCL_020\" = 'Charles Chandler'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:776"
  ]
}
```

### "attribute"."XCL_004" = 'Speed'

```json
{
  "kind": "predicate",
  "formula": "\"attribute\".\"XCL_004\" = 'Speed'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_015\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN hero_attribute AS T3 ON T1.\"XCL_018\" = T3.\"XCL_009\" INNER JOIN attribute AS T4 ON T3.\"XCL_010\" = T4.\"XCL_003\" WHERE T4.\"XCL_004\" = 'Speed' ORDER BY T3.\"XCL_011\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:732"
  ]
}
```

### "superhero"."XCL_020" LIKE 'John%'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_020\" LIKE 'John%'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_018\") FROM superhero WHERE \"XCL_020\" LIKE 'John%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:836"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T3.\"XCL_031\" = 'Death Touch'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_019\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_power"
      },
      {
        "role": "r2",
        "physical_table": "superpower"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_019\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_power AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_012\" INNER JOIN superpower AS \"r2\" ON \"r1\".\"XCL_013\" = \"r2\".\"XCL_030\" WHERE \"r2\".\"XCL_031\" = 'Death Touch'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:739"
  ]
}
```

### Returns the value of column XCL_019 for superhero records where column XCL_018 equals 294. The grain is individual superhero rows filtered by the spec

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_019\" FROM superhero WHERE \"XCL_018\" = 294",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_019\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_019\" AS \"value\" FROM superhero AS \"r0\" WHERE \"r0\".\"XCL_018\" = 294",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:804"
  ]
}
```

### "alignment"."XCL_002" = 'Bad'

```json
{
  "kind": "predicate",
  "formula": "\"alignment\".\"XCL_002\" = 'Bad'",
  "grain": [],
  "population_scope": "SELECT (CAST(COUNT(*) AS REAL) * 100 / (SELECT COUNT(*) FROM superhero)), CAST(SUM(CASE WHEN T2.\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE 0 END) AS REAL) FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN alignment AS T3 ON T3.\"XCL_001\" = T1.\"XCL_027\" WHERE T3.\"XCL_002\" = 'Bad'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:743"
  ]
}
```

### Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"race\".\"XCL_017\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_017\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T1.\"XCL_019\" = 'Copycat'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_017\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "race"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_017\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN race AS \"r1\" ON \"r0\".\"XCL_025\" = \"r1\".\"XCL_016\" WHERE \"r0\".\"XCL_019\" = 'Copycat'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:737"
  ]
}
```

### "superhero"."XCL_019" = 'Deathlok'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = 'Deathlok'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T1.\"XCL_019\" = 'Deathlok'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:749"
  ]
}
```

### Boolean indicator verifying if a superhero has at least one 'Durability' attribute with a value less than 50. Joins hero_attribute and attribute table

```json
{
  "kind": "binding",
  "formula": "1",
  "grain": [],
  "population_scope": "SELECT 1 FROM hero_attribute AS T2 INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T3.\"XCL_004\" = 'Durability' AND T2.\"XCL_011\" < 50 AND T1.\"XCL_018\" = T2.\"XCL_009\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:738"
  ]
}
```

### "superhero"."XCL_019" = 'Agent 13'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = 'Agent 13'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_008\" FROM superhero AS T1 INNER JOIN gender AS T2 ON T1.\"XCL_021\" = T2.\"XCL_007\" WHERE T1.\"XCL_019\" = 'Agent 13'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:777"
  ]
}
```

### "superhero"."XCL_019" = 'Copycat'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = 'Copycat'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_017\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T1.\"XCL_019\" = 'Copycat'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:737"
  ]
}
```

### "superhero"."XCL_028" BETWEEN 150 AND 180

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_028\" BETWEEN 150 AND 180",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T2.\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_028\" BETWEEN 150 AND 180",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:760"
  ]
}
```

### Average XCL_029 per XCL_018 for Alien race

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"superhero\".\"XCL_029\") AS REAL) / COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(T1.\"XCL_029\") AS REAL) / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T2.\"XCL_017\" = 'Alien'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(\"r0\".\"XCL_029\") AS REAL) / COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "race"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(\"r0\".\"XCL_029\") AS REAL) / COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN race AS \"r1\" ON \"r0\".\"XCL_025\" = \"r1\".\"XCL_016\" WHERE \"r1\".\"XCL_017\" = 'Alien'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:789"
  ]
}
```

### Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"race\".\"XCL_017\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_017\", T3.\"XCL_002\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" INNER JOIN alignment AS T3 ON T1.\"XCL_027\" = T3.\"XCL_001\" WHERE T1.\"XCL_019\" = 'Cameron Hicks'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_017\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "race"
      },
      {
        "role": "r2",
        "physical_table": "alignment"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_017\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN race AS \"r1\" ON \"r0\".\"XCL_025\" = \"r1\".\"XCL_016\" INNER JOIN alignment AS \"r2\" ON \"r0\".\"XCL_027\" = \"r2\".\"XCL_001\" WHERE \"r0\".\"XCL_019\" = 'Cameron Hicks'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:787"
  ]
}
```

### Race Name

```json
{
  "kind": "binding",
  "formula": "\"race\".\"XCL_017\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_017\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_023\" = T2.\"XCL_005\" INNER JOIN race AS T3 ON T1.\"XCL_025\" = T3.\"XCL_016\" INNER JOIN gender AS T4 ON T1.\"XCL_021\" = T4.\"XCL_007\" WHERE T2.\"XCL_006\" = 'Blue' AND T4.\"XCL_008\" = 'Male'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_017\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "colour"
      },
      {
        "role": "r2",
        "physical_table": "race"
      },
      {
        "role": "r3",
        "physical_table": "gender"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_017\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN colour AS \"r1\" ON \"r0\".\"XCL_023\" = \"r1\".\"XCL_005\" INNER JOIN race AS \"r2\" ON \"r0\".\"XCL_025\" = \"r2\".\"XCL_016\" INNER JOIN gender AS \"r3\" ON \"r0\".\"XCL_021\" = \"r3\".\"XCL_007\" WHERE \"r1\".\"XCL_006\" = 'Blue' AND \"r3\".\"XCL_008\" = 'Male'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:817"
  ]
}
```

### Aggregates the count of non-null values in the hero_power.XCL_012 column. The population is restricted to hero_power rows that have an associated supe

```json
{
  "kind": "metric",
  "formula": "COUNT(\"hero_power\".\"XCL_012\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_012\") FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.\"XCL_013\" = T2.\"XCL_030\" WHERE T2.\"XCL_031\" = 'Super Strength'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_012\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "hero_power"
      },
      {
        "role": "r1",
        "physical_table": "superpower"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_012\") AS \"value\" FROM hero_power AS \"r0\" INNER JOIN superpower AS \"r1\" ON \"r0\".\"XCL_013\" = \"r1\".\"XCL_030\" WHERE \"r1\".\"XCL_031\" = 'Super Strength'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:718"
  ]
}
```

### "gender"."XCL_008" = 'Male'

```json
{
  "kind": "predicate",
  "formula": "\"gender\".\"XCL_008\" = 'Male'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T3.\"XCL_030\" = T2.\"XCL_013\" INNER JOIN gender AS T4 ON T4.\"XCL_007\" = T1.\"XCL_021\" WHERE T4.\"XCL_008\" = 'Male' LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:751"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" WHERE T2.\"XCL_011\" BETWEEN 75 AND 80",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_019\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_attribute"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_019\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_attribute AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_009\" WHERE \"r1\".\"XCL_011\" BETWEEN 75 AND 80",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:816"
  ]
}
```

### "attribute"."XCL_004" = 'Strength'

```json
{
  "kind": "predicate",
  "formula": "\"attribute\".\"XCL_004\" = 'Strength'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_020\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T3.\"XCL_004\" = 'Strength' ORDER BY T2.\"XCL_011\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:766"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" INNER JOIN colour AS T3 ON T1.\"XCL_023\" = T3.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Blue' AND T3.\"XCL_006\" = 'Brown'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_019\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "colour"
      },
      {
        "role": "r2",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_019\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN colour AS \"r1\" ON \"r0\".\"XCL_022\" = \"r1\".\"XCL_005\" INNER JOIN colour AS \"r2\" ON \"r0\".\"XCL_023\" = \"r2\".\"XCL_005\" WHERE \"r1\".\"XCL_006\" = 'Blue' AND \"r2\".\"XCL_006\" = 'Brown'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:797"
  ]
}
```

### "gender"."XCL_008" = 'Female'

```json
{
  "kind": "predicate",
  "formula": "\"gender\".\"XCL_008\" = 'Female'",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T2.\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN gender AS T3 ON T1.\"XCL_021\" = T3.\"XCL_007\" WHERE T3.\"XCL_008\" = 'Female'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:788"
  ]
}
```

### Primary Colour Name

```json
{
  "kind": "binding",
  "formula": "\"colour\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" INNER JOIN colour AS T3 ON T1.\"XCL_024\" = T3.\"XCL_005\" WHERE T3.\"XCL_006\" = 'Gold'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "colour"
      },
      {
        "role": "r2",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_006\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN colour AS \"r1\" ON \"r0\".\"XCL_022\" = \"r1\".\"XCL_005\" INNER JOIN colour AS \"r2\" ON \"r0\".\"XCL_024\" = \"r2\".\"XCL_005\" WHERE \"r2\".\"XCL_006\" = 'Gold'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:783"
  ]
}
```

### Publisher Name

```json
{
  "kind": "binding",
  "formula": "\"publisher\".\"XCL_015\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_015\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_019\" = 'Blue Beetle II'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_015\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_015\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\" WHERE \"r0\".\"XCL_019\" = 'Blue Beetle II'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:734"
  ]
}
```

### "publisher"."XCL_015" = 'Dark Horse Comics'

```json
{
  "kind": "predicate",
  "formula": "\"publisher\".\"XCL_015\" = 'Dark Horse Comics'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T2.\"XCL_015\" = 'Dark Horse Comics'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:768"
  ]
}
```

### "superhero"."XCL_019" = 'Abomination'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = 'Abomination'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" WHERE T1.\"XCL_019\" = 'Abomination'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:763"
  ]
}
```

### Boolean existence check verifying if a superhero possesses the 'Super Strength' power. Joins hero_power and superpower tables to match the specific po

```json
{
  "kind": "binding",
  "formula": "1",
  "grain": [],
  "population_scope": "SELECT 1 FROM hero_power AS T2 INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T3.\"XCL_031\" = 'Super Strength' AND T1.\"XCL_018\" = T2.\"XCL_012\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:730"
  ]
}
```

### Attribute Name

```json
{
  "kind": "binding",
  "formula": "\"attribute\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_004\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T1.\"XCL_019\" = 'Black Panther' ORDER BY T2.\"XCL_011\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:830"
  ]
}
```

### Colour Name

```json
{
  "kind": "binding",
  "formula": "\"colour\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_019\" = 'Blackwulf'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_006\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN colour AS \"r1\" ON \"r0\".\"XCL_022\" = \"r1\".\"XCL_005\" WHERE \"r0\".\"XCL_019\" = 'Blackwulf'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:844"
  ]
}
```

### Average Superhero XCL_028

```json
{
  "kind": "metric",
  "formula": "AVG(\"superhero\".\"XCL_028\")",
  "grain": [],
  "population_scope": "SELECT AVG(\"XCL_028\") FROM superhero",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_028\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_028\") AS \"value\" FROM superhero AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:845"
  ]
}
```

### Aggregates the total number of superhero records (identified by XCL_018) that are associated with the publisher 'Marvel Comics' (identified by XCL_015

```json
{
  "kind": "metric",
  "formula": "COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T2.\"XCL_015\" = 'Marvel Comics'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\" WHERE \"r1\".\"XCL_015\" = 'Marvel Comics'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:725"
  ]
}
```

### "publisher"."XCL_015" = 'Marvel Comics'

```json
{
  "kind": "predicate",
  "formula": "\"publisher\".\"XCL_015\" = 'Marvel Comics'",
  "grain": [
    "\"colour\".\"XCL_006\""
  ],
  "population_scope": "SELECT colour.\"XCL_006\" AS EyeColor, COUNT(superhero.\"XCL_018\") AS Count, RANK() OVER (ORDER BY COUNT(superhero.\"XCL_018\") DESC) AS PopularityRank FROM superhero INNER JOIN colour ON superhero.\"XCL_022\" = colour.\"XCL_005\" INNER JOIN publisher ON superhero.\"XCL_026\" = publisher.\"XCL_014\" WHERE publisher.\"XCL_015\" = 'Marvel Comics' GROUP BY colour.\"XCL_006\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:728"
  ]
}
```

### "superpower"."XCL_031" = 'Intelligence'

```json
{
  "kind": "predicate",
  "formula": "\"superpower\".\"XCL_031\" = 'Intelligence'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_012\" FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.\"XCL_013\" = T2.\"XCL_030\" WHERE T2.\"XCL_031\" = 'Intelligence'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:843"
  ]
}
```

### "superpower"."XCL_031" = 'Flight'

```json
{
  "kind": "predicate",
  "formula": "\"superpower\".\"XCL_031\" = 'Flight'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T3.\"XCL_031\" = 'Flight'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:771"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T3.\"XCL_004\" = 'Intelligence' ORDER BY T2.\"XCL_011\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:736"
  ]
}
```

### Calculates the percentage of superheroes identified as 'Female' relative to the total number of superheroes, filtered by a specific publisher. The num

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN \"gender\".\"XCL_008\" = 'Female' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T3.\"XCL_008\" = 'Female' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN gender AS T3 ON T1.\"XCL_021\" = T3.\"XCL_007\" WHERE T2.\"XCL_015\" = 'George Lucas'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(CASE WHEN \"r2\".\"XCL_008\" = 'Female' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      },
      {
        "role": "r2",
        "physical_table": "gender"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(CASE WHEN \"r2\".\"XCL_008\" = 'Female' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\" INNER JOIN gender AS \"r2\" ON \"r0\".\"XCL_021\" = \"r2\".\"XCL_007\" WHERE \"r1\".\"XCL_015\" = 'George Lucas'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:834"
  ]
}
```

### The total number of rows in the `superhero` table. Used as the denominator in the percentage calculation to represent the entire population of superhe

```json
{
  "kind": "metric",
  "formula": "COUNT(*)",
  "grain": [],
  "population_scope": "SELECT COUNT(*) FROM superhero",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(*)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      }
    ],
    "scope_sql": "SELECT COUNT(*) AS \"value\" FROM superhero AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:743"
  ]
}
```

### "publisher"."XCL_015" = 'George Lucas'

```json
{
  "kind": "predicate",
  "formula": "\"publisher\".\"XCL_015\" = 'George Lucas'",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T3.\"XCL_008\" = 'Female' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN gender AS T3 ON T1.\"XCL_021\" = T3.\"XCL_007\" WHERE T2.\"XCL_015\" = 'George Lucas'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:834"
  ]
}
```

### "colour"."XCL_006" = 'Blue' AND "colour"."XCL_006" = 'Brown'

```json
{
  "kind": "predicate",
  "formula": "\"colour\".\"XCL_006\" = 'Blue' AND \"colour\".\"XCL_006\" = 'Brown'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" INNER JOIN colour AS T3 ON T1.\"XCL_023\" = T3.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Blue' AND T3.\"XCL_006\" = 'Brown'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:797"
  ]
}
```

### "hero_attribute"."XCL_011" = 100

```json
{
  "kind": "predicate",
  "formula": "\"hero_attribute\".\"XCL_011\" = 100",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_024\" = T2.\"XCL_005\" INNER JOIN hero_attribute AS T3 ON T1.\"XCL_018\" = T3.\"XCL_009\" WHERE T3.\"XCL_011\" = 100",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:814"
  ]
}
```

### "superhero"."XCL_020" = 'Abraham Sapien'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_020\" = 'Abraham Sapien'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_020\" = 'Abraham Sapien'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:770"
  ]
}
```

### Colour Name

```json
{
  "kind": "binding",
  "formula": "\"colour\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" ORDER BY T1.\"XCL_029\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:759"
  ]
}
```

### "publisher"."XCL_015" = 'DC Comics'

```json
{
  "kind": "predicate",
  "formula": "\"publisher\".\"XCL_015\" = 'DC Comics'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T2.\"XCL_015\" = 'DC Comics'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:731"
  ]
}
```

### "alignment"."XCL_002" = 'Neutral'

```json
{
  "kind": "predicate",
  "formula": "\"alignment\".\"XCL_002\" = 'Neutral'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" WHERE T2.\"XCL_002\" = 'Neutral'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:795"
  ]
}
```

### "superhero"."XCL_019" = 'Amazo'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = 'Amazo'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_013\") FROM hero_power AS T1 INNER JOIN superhero AS T2 ON T1.\"XCL_012\" = T2.\"XCL_018\" WHERE T2.\"XCL_019\" = 'Amazo'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:779"
  ]
}
```

### "superhero"."XCL_029" = 0 OR "superhero"."XCL_029" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_029\" = 0 OR \"superhero\".\"XCL_029\" IS NULL",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN T2.\"XCL_005\" = 7 THEN 1 ELSE 0 END) - SUM(CASE WHEN T2.\"XCL_005\" = 1 THEN 1 ELSE 0 END) FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_029\" = 0 OR T1.\"XCL_029\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:819"
  ]
}
```

### Aggregates the count of superhero records (identified by XCL_018) that possess the 'Super Strength' power and have a value in column XCL_028 greater t

```json
{
  "kind": "metric",
  "formula": "COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T3.\"XCL_031\" = 'Super Strength' AND T1.\"XCL_028\" > 200",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_power"
      },
      {
        "role": "r2",
        "physical_table": "superpower"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_power AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_012\" INNER JOIN superpower AS \"r2\" ON \"r1\".\"XCL_013\" = \"r2\".\"XCL_030\" WHERE \"r2\".\"XCL_031\" = 'Super Strength' AND \"r0\".\"XCL_028\" > 200",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:719"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_020\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_020\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T3.\"XCL_004\" = 'Strength' ORDER BY T2.\"XCL_011\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:766"
  ]
}
```

### Aggregates the total number of superhero records (counting non-null XCL_018 values) associated with the publisher identified by XCL_014 = 1. The grain

```json
{
  "kind": "metric",
  "formula": "COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T2.\"XCL_014\" = 1",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\" WHERE \"r1\".\"XCL_014\" = 1",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:799"
  ]
}
```

### "superhero"."XCL_018" = 75

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_018\" = 75",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_018\" = 75",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:748"
  ]
}
```

### "superhero"."XCL_020" LIKE 'Emil Blonsky'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_020\" LIKE 'Emil Blonsky'",
  "grain": [],
  "population_scope": "SELECT \"XCL_029\" FROM superhero WHERE \"XCL_020\" LIKE 'Emil Blonsky'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:790"
  ]
}
```

### "attribute"."XCL_004" = 'Strength' AND "hero_attribute"."XCL_011" = 100 AND "gender"."XCL_008" = 'Female'

```json
{
  "kind": "predicate",
  "formula": "\"attribute\".\"XCL_004\" = 'Strength' AND \"hero_attribute\".\"XCL_011\" = 100 AND \"gender\".\"XCL_008\" = 'Female'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" INNER JOIN gender AS T4 ON T1.\"XCL_021\" = T4.\"XCL_007\" WHERE T3.\"XCL_004\" = 'Strength' AND T2.\"XCL_011\" = 100 AND T4.\"XCL_008\" = 'Female'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:740"
  ]
}
```

### Distinct Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"race\".\"XCL_017\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_017\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T1.\"XCL_029\" = 108 AND T1.\"XCL_028\" = 188",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:808"
  ]
}
```

### Colour Name

```json
{
  "kind": "binding",
  "formula": "\"colour\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_019\" = 'Abomination'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_006\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN colour AS \"r1\" ON \"r0\".\"XCL_022\" = \"r1\".\"XCL_005\" WHERE \"r0\".\"XCL_019\" = 'Abomination'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:831"
  ]
}
```

### Gender Identifier

```json
{
  "kind": "binding",
  "formula": "\"gender\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_008\" FROM superhero AS T1 INNER JOIN gender AS T2 ON T1.\"XCL_021\" = T2.\"XCL_007\" WHERE T1.\"XCL_019\" = 'Agent 13'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "gender"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_008\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN gender AS \"r1\" ON \"r0\".\"XCL_021\" = \"r1\".\"XCL_007\" WHERE \"r0\".\"XCL_019\" = 'Agent 13'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:777"
  ]
}
```

### Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"hero_attribute\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_004\", T2.\"XCL_011\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T1.\"XCL_019\" = '3-D Man'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_011\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_attribute"
      },
      {
        "role": "r2",
        "physical_table": "attribute"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_011\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_attribute AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_009\" INNER JOIN attribute AS \"r2\" ON \"r1\".\"XCL_010\" = \"r2\".\"XCL_003\" WHERE \"r0\".\"XCL_019\" = '3-D Man'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:796"
  ]
}
```

### Aggregates the count of superhero records (identified by XCL_018) that are associated with a specific publisher. The population is restricted to super

```json
{
  "kind": "metric",
  "formula": "COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T2.\"XCL_015\" = 'Dark Horse Comics'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\" WHERE \"r1\".\"XCL_015\" = 'Dark Horse Comics'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:768"
  ]
}
```

### Returns the value of column "XCL_020" for each row in the "superhero" table where "XCL_019" equals 'Alien'. The grain is individual superhero records 

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_020\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_020\" FROM superhero WHERE \"XCL_019\" = 'Alien'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_020\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_020\" AS \"value\" FROM superhero AS \"r0\" WHERE \"r0\".\"XCL_019\" = 'Alien'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:838"
  ]
}
```

### "alignment"."XCL_002" = 'Bad'

```json
{
  "kind": "predicate",
  "formula": "\"alignment\".\"XCL_002\" = 'Bad'",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T3.\"XCL_008\" = 'Female' THEN T1.\"XCL_018\" ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" INNER JOIN gender AS T3 ON T1.\"XCL_021\" = T3.\"XCL_007\" WHERE T2.\"XCL_002\" = 'Bad'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:818"
  ]
}
```

### Value of column XCL_024 from the superhero table for female superheroes published by Dark Horse Comics.

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_024\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_022\", T1.\"XCL_023\", T1.\"XCL_024\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T2.\"XCL_014\" = T1.\"XCL_026\" INNER JOIN gender AS T3 ON T3.\"XCL_007\" = T1.\"XCL_021\" WHERE T2.\"XCL_015\" = 'Dark Horse Comics' AND T3.\"XCL_008\" = 'Female'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_024\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      },
      {
        "role": "r2",
        "physical_table": "gender"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_024\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r1\".\"XCL_014\" = \"r0\".\"XCL_026\" INNER JOIN gender AS \"r2\" ON \"r2\".\"XCL_007\" = \"r0\".\"XCL_021\" WHERE \"r1\".\"XCL_015\" = 'Dark Horse Comics' AND \"r2\".\"XCL_008\" = 'Female'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:772"
  ]
}
```

### DC vs Marvel Superhero Count Difference

```json
{
  "kind": "metric",
  "formula": "SUM(CASE WHEN \"publisher\".\"XCL_015\" = 'DC Comics' THEN 1 ELSE 0 END) - SUM(CASE WHEN \"publisher\".\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN T2.\"XCL_015\" = 'DC Comics' THEN 1 ELSE 0 END) - SUM(CASE WHEN T2.\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE 0 END) FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(CASE WHEN \"r1\".\"XCL_015\" = 'DC Comics' THEN 1 ELSE 0 END) - SUM(CASE WHEN \"r1\".\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      }
    ],
    "scope_sql": "SELECT SUM(CASE WHEN \"r1\".\"XCL_015\" = 'DC Comics' THEN 1 ELSE 0 END) - SUM(CASE WHEN \"r1\".\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE 0 END) AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:829"
  ]
}
```

### Marvel vs DC Superhero Count Difference

```json
{
  "kind": "metric",
  "formula": "SUM(CASE WHEN \"publisher\".\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE 0 END) - SUM(CASE WHEN \"publisher\".\"XCL_015\" = 'DC Comics' THEN 1 ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN T2.\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE 0 END) - SUM(CASE WHEN T2.\"XCL_015\" = 'DC Comics' THEN 1 ELSE 0 END) FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(CASE WHEN \"r1\".\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE 0 END) - SUM(CASE WHEN \"r1\".\"XCL_015\" = 'DC Comics' THEN 1 ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      }
    ],
    "scope_sql": "SELECT SUM(CASE WHEN \"r1\".\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE 0 END) - SUM(CASE WHEN \"r1\".\"XCL_015\" = 'DC Comics' THEN 1 ELSE 0 END) AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:744"
  ]
}
```

### "superhero"."XCL_028" = 185 AND "race"."XCL_017" = 'Human'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_028\" = 185 AND \"race\".\"XCL_017\" = 'Human'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_006\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" INNER JOIN colour AS T3 ON T1.\"XCL_023\" = T3.\"XCL_005\" WHERE T1.\"XCL_028\" = 185 AND T2.\"XCL_017\" = 'Human'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:758"
  ]
}
```

### Publisher Name

```json
{
  "kind": "binding",
  "formula": "\"publisher\".\"XCL_015\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_015\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_019\" IN ('Hawkman', 'Karate Kid', 'Speedy')",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_015\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_015\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\" WHERE \"r0\".\"XCL_019\" IN ('Hawkman', 'Karate Kid', 'Speedy')",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:798"
  ]
}
```

### Distinct Colour Identifier

```json
{
  "kind": "binding",
  "formula": "\"colour\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_024\" = T2.\"XCL_005\" INNER JOIN hero_attribute AS T3 ON T1.\"XCL_018\" = T3.\"XCL_009\" WHERE T3.\"XCL_011\" = 100",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:814"
  ]
}
```

### "superpower"."XCL_031" = 'Wind Control'

```json
{
  "kind": "predicate",
  "formula": "\"superpower\".\"XCL_031\" = 'Wind Control'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T3.\"XCL_031\" = 'Wind Control' ORDER BY T1.\"XCL_019\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:824"
  ]
}
```

### Publisher Identifier

```json
{
  "kind": "binding",
  "formula": "\"publisher\".\"XCL_014\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_014\" FROM publisher WHERE \"XCL_015\" = 'Star Trek'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_014\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "publisher"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_014\" AS \"value\" FROM publisher AS \"r0\" WHERE \"r0\".\"XCL_015\" = 'Star Trek'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:745"
  ]
}
```

### "superpower"."XCL_031" = 'Agility' AND "colour"."XCL_006" = 'Blue'

```json
{
  "kind": "predicate",
  "formula": "\"superpower\".\"XCL_031\" = 'Agility' AND \"colour\".\"XCL_006\" = 'Blue'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" INNER JOIN colour AS T4 ON T1.\"XCL_022\" = T4.\"XCL_005\" WHERE T3.\"XCL_031\" = 'Agility' AND T4.\"XCL_006\" = 'Blue'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:723"
  ]
}
```

### "race"."XCL_017" = 'Alien'

```json
{
  "kind": "predicate",
  "formula": "\"race\".\"XCL_017\" = 'Alien'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T2.\"XCL_017\" = 'Alien'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:752"
  ]
}
```

### Hero Identifier

```json
{
  "kind": "binding",
  "formula": "\"hero_power\".\"XCL_012\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_012\" FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.\"XCL_013\" = T2.\"XCL_030\" WHERE T2.\"XCL_031\" = 'Intelligence'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_012\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "hero_power"
      },
      {
        "role": "r1",
        "physical_table": "superpower"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_012\" AS \"value\" FROM hero_power AS \"r0\" INNER JOIN superpower AS \"r1\" ON \"r0\".\"XCL_013\" = \"r1\".\"XCL_030\" WHERE \"r1\".\"XCL_031\" = 'Intelligence'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:843"
  ]
}
```

### "attribute"."XCL_004" = 'Intelligence'

```json
{
  "kind": "predicate",
  "formula": "\"attribute\".\"XCL_004\" = 'Intelligence'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T3.\"XCL_004\" = 'Intelligence' ORDER BY T2.\"XCL_011\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:736"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_019\" FROM superhero AS T1 WHERE EXISTS(SELECT 1 FROM hero_power AS T2 INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T3.\"XCL_031\" = 'Super Strength' AND T1.\"XCL_018\" = T2.\"XCL_012\") AND EXISTS(SELECT 1 FROM publisher AS T4 WHERE T4.\"XCL_015\" = 'Marvel Comics' AND T1.\"XCL_026\" = T4.\"XCL_014\")",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:730"
  ]
}
```

### "superhero"."XCL_028" BETWEEN 170 AND 190 AND "colour"."XCL_006" = 'No Colour'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_028\" BETWEEN 170 AND 190 AND \"colour\".\"XCL_006\" = 'No Colour'",
  "grain": [],
  "population_scope": "SELECT DISTINCT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_028\" BETWEEN 170 AND 190 AND T2.\"XCL_006\" = 'No Colour'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:753"
  ]
}
```

### Alignment Name

```json
{
  "kind": "binding",
  "formula": "\"alignment\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT T4.\"XCL_002\", T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T3.\"XCL_030\" = T2.\"XCL_013\" INNER JOIN alignment AS T4 ON T1.\"XCL_027\" = T4.\"XCL_001\" WHERE T1.\"XCL_019\" = 'Atom IV'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r3\".\"XCL_002\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_power"
      },
      {
        "role": "r2",
        "physical_table": "superpower"
      },
      {
        "role": "r3",
        "physical_table": "alignment"
      }
    ],
    "scope_sql": "SELECT \"r3\".\"XCL_002\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_power AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_012\" INNER JOIN superpower AS \"r2\" ON \"r2\".\"XCL_030\" = \"r1\".\"XCL_013\" INNER JOIN alignment AS \"r3\" ON \"r0\".\"XCL_027\" = \"r3\".\"XCL_001\" WHERE \"r0\".\"XCL_019\" = 'Atom IV'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:811"
  ]
}
```

### "publisher"."XCL_015" = 'Dark Horse Comics' AND "race"."XCL_017" <> 'Human'

```json
{
  "kind": "predicate",
  "formula": "\"publisher\".\"XCL_015\" = 'Dark Horse Comics' AND \"race\".\"XCL_017\" <> 'Human'",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_028\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN race AS T3 ON T1.\"XCL_025\" = T3.\"XCL_016\" WHERE T2.\"XCL_015\" = 'Dark Horse Comics' AND T3.\"XCL_017\" <> 'Human'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:827"
  ]
}
```

### "superhero"."XCL_019" = 'Abomination'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = 'Abomination'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T1.\"XCL_019\" = 'Abomination'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:792"
  ]
}
```

### "superhero"."XCL_019" = 'Aquababy'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = 'Aquababy'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" WHERE T1.\"XCL_019\" = 'Aquababy'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:840"
  ]
}
```

### Hero Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"hero_attribute\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" WHERE T1.\"XCL_019\" = 'Abomination'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_011\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_attribute"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_011\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_attribute AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_009\" WHERE \"r0\".\"XCL_019\" = 'Abomination'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:763"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_020\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_020\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T2.\"XCL_017\" = 'Demi-God'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_020\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "race"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_020\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN race AS \"r1\" ON \"r0\".\"XCL_025\" = \"r1\".\"XCL_016\" WHERE \"r1\".\"XCL_017\" = 'Demi-God'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:755"
  ]
}
```

### "superpower"."XCL_031" = 'Super Strength' AND "superhero"."XCL_028" > 200

```json
{
  "kind": "predicate",
  "formula": "\"superpower\".\"XCL_031\" = 'Super Strength' AND \"superhero\".\"XCL_028\" > 200",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T3.\"XCL_031\" = 'Super Strength' AND T1.\"XCL_028\" > 200",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:719"
  ]
}
```

### Average XCL_028 for Dark Horse non-Human superheroes

```json
{
  "kind": "metric",
  "formula": "AVG(\"superhero\".\"XCL_028\")",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_028\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN race AS T3 ON T1.\"XCL_025\" = T3.\"XCL_016\" WHERE T2.\"XCL_015\" = 'Dark Horse Comics' AND T3.\"XCL_017\" <> 'Human'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_028\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      },
      {
        "role": "r2",
        "physical_table": "race"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_028\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\" INNER JOIN race AS \"r2\" ON \"r0\".\"XCL_025\" = \"r2\".\"XCL_016\" WHERE \"r1\".\"XCL_015\" = 'Dark Horse Comics' AND \"r2\".\"XCL_017\" <> 'Human'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:827"
  ]
}
```

### Output column from the superhero table (alias T1). Represents the specific superhero record selected after filtering for male gender and high XCL_029 

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN gender AS T2 ON T1.\"XCL_021\" = T2.\"XCL_007\" WHERE T2.\"XCL_008\" = 'Male' AND T1.\"XCL_029\" * 100 > (SELECT AVG(\"XCL_029\") FROM superhero) * 79",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:761"
  ]
}
```

### Race Name

```json
{
  "kind": "binding",
  "formula": "\"race\".\"XCL_017\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_017\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN race AS T3 ON T1.\"XCL_025\" = T3.\"XCL_016\" ORDER BY T2.\"XCL_011\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:810"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_020\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_020\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_029\" < 100 AND T2.\"XCL_006\" = 'Brown'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_020\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_020\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN colour AS \"r1\" ON \"r0\".\"XCL_022\" = \"r1\".\"XCL_005\" WHERE \"r0\".\"XCL_029\" < 100 AND \"r1\".\"XCL_006\" = 'Brown'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:839"
  ]
}
```

### Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"race\".\"XCL_017\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_017\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T1.\"XCL_029\" = 169",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_017\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "race"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_017\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN race AS \"r1\" ON \"r0\".\"XCL_025\" = \"r1\".\"XCL_016\" WHERE \"r0\".\"XCL_029\" = 169",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:757"
  ]
}
```

### "superhero"."XCL_019" = 'Blue Beetle II'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = 'Blue Beetle II'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_015\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_019\" = 'Blue Beetle II'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:734"
  ]
}
```

### Aggregates the total number of superhero records (identified by XCL_018) that are published by 'Marvel Comics' and have the colour 'Gold'. The grain i

```json
{
  "kind": "metric",
  "formula": "COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN colour AS T3 ON T1.\"XCL_022\" = T3.\"XCL_005\" WHERE T2.\"XCL_015\" = 'Marvel Comics' AND T3.\"XCL_006\" = 'Gold'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      },
      {
        "role": "r2",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\" INNER JOIN colour AS \"r2\" ON \"r0\".\"XCL_022\" = \"r2\".\"XCL_005\" WHERE \"r1\".\"XCL_015\" = 'Marvel Comics' AND \"r2\".\"XCL_006\" = 'Gold'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:733"
  ]
}
```

### Calculates the percentage of superheroes published by Marvel Comics who have a 'Good' alignment. The numerator counts superheroes where the alignment 

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN \"alignment\".\"XCL_002\" = 'Good' THEN \"superhero\".\"XCL_018\" ELSE NULL END) AS REAL) * 100 / COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T3.\"XCL_002\" = 'Good' THEN T1.\"XCL_018\" ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN alignment AS T3 ON T1.\"XCL_027\" = T3.\"XCL_001\" WHERE T2.\"XCL_015\" = 'Marvel Comics'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(CASE WHEN \"r2\".\"XCL_002\" = 'Good' THEN \"r0\".\"XCL_018\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      },
      {
        "role": "r2",
        "physical_table": "alignment"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(CASE WHEN \"r2\".\"XCL_002\" = 'Good' THEN \"r0\".\"XCL_018\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\" INNER JOIN alignment AS \"r2\" ON \"r0\".\"XCL_027\" = \"r2\".\"XCL_001\" WHERE \"r1\".\"XCL_015\" = 'Marvel Comics'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:835"
  ]
}
```

### "superhero"."XCL_019" = 'Blackwulf'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = 'Blackwulf'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_019\" = 'Blackwulf'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:844"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_029\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_029\", T2.\"XCL_017\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T1.\"XCL_018\" = 40",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_029\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "race"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_029\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN race AS \"r1\" ON \"r0\".\"XCL_025\" = \"r1\".\"XCL_016\" WHERE \"r0\".\"XCL_018\" = 40",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:841"
  ]
}
```

### "superhero"."XCL_020" = 'Hunter Zolomon'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_020\" = 'Hunter Zolomon'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T1.\"XCL_020\" = 'Hunter Zolomon'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:780"
  ]
}
```

### "publisher"."XCL_015" = 'Dark Horse Comics' AND "gender"."XCL_008" = 'Female'

```json
{
  "kind": "predicate",
  "formula": "\"publisher\".\"XCL_015\" = 'Dark Horse Comics' AND \"gender\".\"XCL_008\" = 'Female'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_022\", T1.\"XCL_023\", T1.\"XCL_024\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T2.\"XCL_014\" = T1.\"XCL_026\" INNER JOIN gender AS T3 ON T3.\"XCL_007\" = T1.\"XCL_021\" WHERE T2.\"XCL_015\" = 'Dark Horse Comics' AND T3.\"XCL_008\" = 'Female'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:772"
  ]
}
```

### Aggregates the count of non-null values in column XCL_018 from the superhero table, restricted to rows where column XCL_020 starts with 'John'. Return

```json
{
  "kind": "metric",
  "formula": "COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_018\") FROM superhero WHERE \"XCL_020\" LIKE 'John%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" WHERE \"r0\".\"XCL_020\" LIKE 'John%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:836"
  ]
}
```

### "attribute"."XCL_004" = 'Speed' AND "hero_attribute"."XCL_011" = 100

```json
{
  "kind": "predicate",
  "formula": "\"attribute\".\"XCL_004\" = 'Speed' AND \"hero_attribute\".\"XCL_011\" = 100",
  "grain": [],
  "population_scope": "SELECT COUNT(T3.\"XCL_019\") FROM hero_attribute AS T1 INNER JOIN attribute AS T2 ON T1.\"XCL_010\" = T2.\"XCL_003\" INNER JOIN superhero AS T3 ON T1.\"XCL_009\" = T3.\"XCL_018\" WHERE T2.\"XCL_004\" = 'Speed' AND T1.\"XCL_011\" = 100",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:828"
  ]
}
```

### "superhero"."XCL_029" = 108 AND "superhero"."XCL_028" = 188

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_029\" = 108 AND \"superhero\".\"XCL_028\" = 188",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_017\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T1.\"XCL_029\" = 108 AND T1.\"XCL_028\" = 188",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:808"
  ]
}
```

### Net count of colour value 7 vs 1

```json
{
  "kind": "metric",
  "formula": "SUM(CASE WHEN \"colour\".\"XCL_005\" = 7 THEN 1 ELSE 0 END) - SUM(CASE WHEN \"colour\".\"XCL_005\" = 1 THEN 1 ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN T2.\"XCL_005\" = 7 THEN 1 ELSE 0 END) - SUM(CASE WHEN T2.\"XCL_005\" = 1 THEN 1 ELSE 0 END) FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_029\" = 0 OR T1.\"XCL_029\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(CASE WHEN \"r1\".\"XCL_005\" = 7 THEN 1 ELSE 0 END) - SUM(CASE WHEN \"r1\".\"XCL_005\" = 1 THEN 1 ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT SUM(CASE WHEN \"r1\".\"XCL_005\" = 7 THEN 1 ELSE 0 END) - SUM(CASE WHEN \"r1\".\"XCL_005\" = 1 THEN 1 ELSE 0 END) AS \"value\" FROM superhero AS \"r0\" INNER JOIN colour AS \"r1\" ON \"r0\".\"XCL_022\" = \"r1\".\"XCL_005\" WHERE \"r0\".\"XCL_029\" = 0 OR \"r0\".\"XCL_029\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:819"
  ]
}
```

### Aggregates the total number of superhero records (identified by XCL_019) that are associated with the race 'Vampire' via an inner join on race identif

```json
{
  "kind": "metric",
  "formula": "COUNT(\"superhero\".\"XCL_019\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_019\") FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T2.\"XCL_017\" = 'Vampire'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_019\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "race"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_019\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN race AS \"r1\" ON \"r0\".\"XCL_025\" = \"r1\".\"XCL_016\" WHERE \"r1\".\"XCL_017\" = 'Vampire'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:742"
  ]
}
```

### Superpower Name

```json
{
  "kind": "binding",
  "formula": "\"superpower\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T1.\"XCL_020\" = 'Hunter Zolomon'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_031\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_power"
      },
      {
        "role": "r2",
        "physical_table": "superpower"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_031\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_power AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_012\" INNER JOIN superpower AS \"r2\" ON \"r1\".\"XCL_013\" = \"r2\".\"XCL_030\" WHERE \"r0\".\"XCL_020\" = 'Hunter Zolomon'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:780"
  ]
}
```

### "alignment"."XCL_002" = 'Neutral'

```json
{
  "kind": "predicate",
  "formula": "\"alignment\".\"XCL_002\" = 'Neutral'",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_028\") FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" WHERE T2.\"XCL_002\" = 'Neutral'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:842"
  ]
}
```

### Publisher Identifier

```json
{
  "kind": "binding",
  "formula": "\"publisher\".\"XCL_015\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\", T2.\"XCL_015\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_022\" = T1.\"XCL_023\" AND T1.\"XCL_022\" = T1.\"XCL_024\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_015\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_015\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\" WHERE \"r0\".\"XCL_022\" = \"r0\".\"XCL_023\" AND \"r0\".\"XCL_022\" = \"r0\".\"XCL_024\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:773"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_020\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_020\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T2.\"XCL_017\" = 'Vampire'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_020\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "race"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_020\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN race AS \"r1\" ON \"r0\".\"XCL_025\" = \"r1\".\"XCL_016\" WHERE \"r1\".\"XCL_017\" = 'Vampire'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:784"
  ]
}
```

### A list of unique, non-null values from the 'XCL_020' column in the 'superhero' table, filtered to include only rows where 'XCL_029' is null or zero.

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_020\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_020\" FROM superhero WHERE NOT \"XCL_020\" IS NULL AND (\"XCL_029\" IS NULL OR \"XCL_029\" = 0)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:805"
  ]
}
```

### "colour"."XCL_006" = 'Blue'

```json
{
  "kind": "predicate",
  "formula": "\"colour\".\"XCL_006\" = 'Blue'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Blue' LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:812"
  ]
}
```

### Colour Name

```json
{
  "kind": "binding",
  "formula": "\"colour\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_020\" = 'Karen Beecher-Duncan'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_006\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN colour AS \"r1\" ON \"r0\".\"XCL_022\" = \"r1\".\"XCL_005\" WHERE \"r0\".\"XCL_020\" = 'Karen Beecher-Duncan'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:806"
  ]
}
```

### Aggregates the total number of superhero records (identified by XCL_018) that are linked to the colour 'Blond' via the join condition on XCL_023 and X

```json
{
  "kind": "metric",
  "formula": "COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_023\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Blond'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN colour AS \"r1\" ON \"r0\".\"XCL_023\" = \"r1\".\"XCL_005\" WHERE \"r1\".\"XCL_006\" = 'Blond'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:735"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\", T2.\"XCL_017\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T1.\"XCL_020\" = 'Charles Chandler'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_019\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "race"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_019\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN race AS \"r1\" ON \"r0\".\"XCL_025\" = \"r1\".\"XCL_016\" WHERE \"r0\".\"XCL_020\" = 'Charles Chandler'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:776"
  ]
}
```

### Aggregates the total number of superhero records (identified by XCL_018) that are associated with the 'Bad' alignment. The grain is a single scalar va

```json
{
  "kind": "metric",
  "formula": "COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" WHERE T2.\"XCL_002\" = 'Bad'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "alignment"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN alignment AS \"r1\" ON \"r0\".\"XCL_027\" = \"r1\".\"XCL_001\" WHERE \"r1\".\"XCL_002\" = 'Bad'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:756"
  ]
}
```

### Average XCL_029 for Female Superheroes

```json
{
  "kind": "metric",
  "formula": "AVG(\"superhero\".\"XCL_029\")",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_029\") FROM superhero AS T1 INNER JOIN gender AS T2 ON T1.\"XCL_021\" = T2.\"XCL_007\" WHERE T2.\"XCL_008\" = 'Female'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_029\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "gender"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_029\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN gender AS \"r1\" ON \"r0\".\"XCL_021\" = \"r1\".\"XCL_007\" WHERE \"r1\".\"XCL_008\" = 'Female'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:750"
  ]
}
```

### "publisher"."XCL_015" = 'DC Comics'

```json
{
  "kind": "predicate",
  "formula": "\"publisher\".\"XCL_015\" = 'DC Comics'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T2.\"XCL_015\" = 'DC Comics' ORDER BY T1.\"XCL_029\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:826"
  ]
}
```

### Aggregated count of superhero records (T3) that possess the 'Speed' attribute (T2) with a value of 100 (T1). The grain is a single scalar value repres

```json
{
  "kind": "metric",
  "formula": "COUNT(\"superhero\".\"XCL_019\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T3.\"XCL_019\") FROM hero_attribute AS T1 INNER JOIN attribute AS T2 ON T1.\"XCL_010\" = T2.\"XCL_003\" INNER JOIN superhero AS T3 ON T1.\"XCL_009\" = T3.\"XCL_018\" WHERE T2.\"XCL_004\" = 'Speed' AND T1.\"XCL_011\" = 100",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r2\".\"XCL_019\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "hero_attribute"
      },
      {
        "role": "r1",
        "physical_table": "attribute"
      },
      {
        "role": "r2",
        "physical_table": "superhero"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r2\".\"XCL_019\") AS \"value\" FROM hero_attribute AS \"r0\" INNER JOIN attribute AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_003\" INNER JOIN superhero AS \"r2\" ON \"r0\".\"XCL_009\" = \"r2\".\"XCL_018\" WHERE \"r1\".\"XCL_004\" = 'Speed' AND \"r0\".\"XCL_011\" = 100",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:828"
  ]
}
```

### Minimum XCL_011 Value

```json
{
  "kind": "metric",
  "formula": "MIN(\"hero_attribute\".\"XCL_011\")",
  "grain": [],
  "population_scope": "SELECT MIN(\"XCL_011\") FROM hero_attribute",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MIN(\"r0\".\"XCL_011\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "hero_attribute"
      }
    ],
    "scope_sql": "SELECT MIN(\"r0\".\"XCL_011\") AS \"value\" FROM hero_attribute AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:837"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T2.\"XCL_015\" = 'DC Comics' ORDER BY T1.\"XCL_029\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:826"
  ]
}
```

### "alignment"."XCL_002" = 'Good' AND "gender"."XCL_008" = 'Female'

```json
{
  "kind": "predicate",
  "formula": "\"alignment\".\"XCL_002\" = 'Good' AND \"gender\".\"XCL_008\" = 'Female'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" INNER JOIN gender AS T3 ON T1.\"XCL_021\" = T3.\"XCL_007\" WHERE T2.\"XCL_002\" = 'Good' AND T3.\"XCL_008\" = 'Female'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:815"
  ]
}
```

### "superpower"."XCL_031" = 'Adaptation'

```json
{
  "kind": "predicate",
  "formula": "\"superpower\".\"XCL_031\" = 'Adaptation'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T3.\"XCL_031\" = 'Adaptation'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:778"
  ]
}
```

### Average XCL_028 for Neutral Superheroes

```json
{
  "kind": "metric",
  "formula": "AVG(\"superhero\".\"XCL_028\")",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_028\") FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" WHERE T2.\"XCL_002\" = 'Neutral'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_028\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "alignment"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_028\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN alignment AS \"r1\" ON \"r0\".\"XCL_027\" = \"r1\".\"XCL_001\" WHERE \"r1\".\"XCL_002\" = 'Neutral'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:842"
  ]
}
```

### "superpower"."XCL_031" = 'Stealth'

```json
{
  "kind": "predicate",
  "formula": "\"superpower\".\"XCL_031\" = 'Stealth'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_012\") FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.\"XCL_013\" = T2.\"XCL_030\" WHERE T2.\"XCL_031\" = 'Stealth'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:765"
  ]
}
```

### "gender"."XCL_008" = 'Female'

```json
{
  "kind": "predicate",
  "formula": "\"gender\".\"XCL_008\" = 'Female'",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_029\") FROM superhero AS T1 INNER JOIN gender AS T2 ON T1.\"XCL_021\" = T2.\"XCL_007\" WHERE T2.\"XCL_008\" = 'Female'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:750"
  ]
}
```

### Calculates the percentage of superheroes with a height (XCL_028) between 150 and 180 who are published by 'Marvel Comics'. The numerator counts superh

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN \"publisher\".\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T2.\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_028\" BETWEEN 150 AND 180",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(CASE WHEN \"r1\".\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(CASE WHEN \"r1\".\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\" WHERE \"r0\".\"XCL_028\" BETWEEN 150 AND 180",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:760"
  ]
}
```

### Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"race\".\"XCL_017\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_029\", T2.\"XCL_017\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T1.\"XCL_018\" = 40",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_017\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "race"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_017\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN race AS \"r1\" ON \"r0\".\"XCL_025\" = \"r1\".\"XCL_016\" WHERE \"r0\".\"XCL_018\" = 40",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:841"
  ]
}
```

### "race"."XCL_017" = 'Demi-God'

```json
{
  "kind": "predicate",
  "formula": "\"race\".\"XCL_017\" = 'Demi-God'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_020\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T2.\"XCL_017\" = 'Demi-God'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:755"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T3.\"XCL_031\" = 'Adaptation'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_019\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_power"
      },
      {
        "role": "r2",
        "physical_table": "superpower"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_019\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_power AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_012\" INNER JOIN superpower AS \"r2\" ON \"r1\".\"XCL_013\" = \"r2\".\"XCL_030\" WHERE \"r2\".\"XCL_031\" = 'Adaptation'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:778"
  ]
}
```

### A scalar metric representing the ratio of the count of superheroes identified as 'Male' to the count of superheroes identified as 'Female'. The popula

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN \"gender\".\"XCL_008\" = 'Male' THEN \"superhero\".\"XCL_018\" ELSE NULL END) AS REAL) / COUNT(CASE WHEN \"gender\".\"XCL_008\" = 'Female' THEN \"superhero\".\"XCL_018\" ELSE NULL END)",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T2.\"XCL_008\" = 'Male' THEN T1.\"XCL_018\" ELSE NULL END) AS REAL) / COUNT(CASE WHEN T2.\"XCL_008\" = 'Female' THEN T1.\"XCL_018\" ELSE NULL END) FROM superhero AS T1 INNER JOIN gender AS T2 ON T1.\"XCL_021\" = T2.\"XCL_007\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(CASE WHEN \"r1\".\"XCL_008\" = 'Male' THEN \"r0\".\"XCL_018\" ELSE NULL END) AS REAL) / COUNT(CASE WHEN \"r1\".\"XCL_008\" = 'Female' THEN \"r0\".\"XCL_018\" ELSE NULL END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "gender"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(CASE WHEN \"r1\".\"XCL_008\" = 'Male' THEN \"r0\".\"XCL_018\" ELSE NULL END) AS REAL) / COUNT(CASE WHEN \"r1\".\"XCL_008\" = 'Female' THEN \"r0\".\"XCL_018\" ELSE NULL END) AS \"value\" FROM superhero AS \"r0\" INNER JOIN gender AS \"r1\" ON \"r0\".\"XCL_021\" = \"r1\".\"XCL_007\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:801"
  ]
}
```

### "superhero"."XCL_019" = '3-D Man'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = '3-D Man'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T1.\"XCL_019\" = '3-D Man'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:717"
  ]
}
```

### "alignment"."XCL_002" = 'Bad'

```json
{
  "kind": "predicate",
  "formula": "\"alignment\".\"XCL_002\" = 'Bad'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" WHERE T2.\"XCL_002\" = 'Bad'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:756"
  ]
}
```

### Scalar value of column XCL_029 from the superhero table where XCL_020 matches 'Emil Blonsky'. Acts as the minuend in the final subtraction.

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_029\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_029\" FROM superhero WHERE \"XCL_020\" LIKE 'Emil Blonsky'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_029\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_029\" AS \"value\" FROM superhero AS \"r0\" WHERE \"r0\".\"XCL_020\" LIKE 'Emil Blonsky'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:790"
  ]
}
```

### "superhero"."XCL_020" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_020\" IS NULL",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_018\") FROM superhero WHERE \"XCL_020\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:747"
  ]
}
```

### "superhero"."XCL_020" = 'Helen Parr'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_020\" = 'Helen Parr'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T1.\"XCL_020\" = 'Helen Parr'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:807"
  ]
}
```

### "superhero"."XCL_019" = 'Alien'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = 'Alien'",
  "grain": [],
  "population_scope": "SELECT \"XCL_020\" FROM superhero WHERE \"XCL_019\" = 'Alien'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:838"
  ]
}
```

### "publisher"."XCL_015" = 'Marvel Comics' AND "gender"."XCL_008" = 'Female'

```json
{
  "kind": "predicate",
  "formula": "\"publisher\".\"XCL_015\" = 'Marvel Comics' AND \"gender\".\"XCL_008\" = 'Female'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN gender AS T3 ON T1.\"XCL_021\" = T3.\"XCL_007\" WHERE T2.\"XCL_015\" = 'Marvel Comics' AND T3.\"XCL_008\" = 'Female'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:823"
  ]
}
```

### "publisher"."XCL_015" = 'Star Trek'

```json
{
  "kind": "predicate",
  "formula": "\"publisher\".\"XCL_015\" = 'Star Trek'",
  "grain": [],
  "population_scope": "SELECT \"XCL_014\" FROM publisher WHERE \"XCL_015\" = 'Star Trek'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:745"
  ]
}
```

### "superhero"."XCL_019" = 'A-Bomb'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = 'A-Bomb'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_017\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T1.\"XCL_019\" = 'A-Bomb'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:774"
  ]
}
```

### Value of column XCL_022 from the superhero table for female superheroes published by Dark Horse Comics.

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_022\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_022\", T1.\"XCL_023\", T1.\"XCL_024\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T2.\"XCL_014\" = T1.\"XCL_026\" INNER JOIN gender AS T3 ON T3.\"XCL_007\" = T1.\"XCL_021\" WHERE T2.\"XCL_015\" = 'Dark Horse Comics' AND T3.\"XCL_008\" = 'Female'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_022\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      },
      {
        "role": "r2",
        "physical_table": "gender"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_022\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r1\".\"XCL_014\" = \"r0\".\"XCL_026\" INNER JOIN gender AS \"r2\" ON \"r2\".\"XCL_007\" = \"r0\".\"XCL_021\" WHERE \"r1\".\"XCL_015\" = 'Dark Horse Comics' AND \"r2\".\"XCL_008\" = 'Female'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:772"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [
    "\"superhero\".\"XCL_019\""
  ],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" GROUP BY T1.\"XCL_019\" ORDER BY COUNT(T2.\"XCL_012\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:741"
  ]
}
```

### Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"superhero\".\"XCL_018\")",
  "grain": [
    "\"colour\".\"XCL_006\""
  ],
  "population_scope": "SELECT colour.\"XCL_006\" AS EyeColor, COUNT(superhero.\"XCL_018\") AS Count, RANK() OVER (ORDER BY COUNT(superhero.\"XCL_018\") DESC) AS PopularityRank FROM superhero INNER JOIN colour ON superhero.\"XCL_022\" = colour.\"XCL_005\" INNER JOIN publisher ON superhero.\"XCL_026\" = publisher.\"XCL_014\" WHERE publisher.\"XCL_015\" = 'Marvel Comics' GROUP BY colour.\"XCL_006\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_018\")",
    "grain": [
      "\"r1\".\"XCL_006\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "colour"
      },
      {
        "role": "r2",
        "physical_table": "publisher"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_006\" AS \"grain_0\", COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN colour AS \"r1\" ON \"r0\".\"XCL_022\" = \"r1\".\"XCL_005\" INNER JOIN publisher AS \"r2\" ON \"r0\".\"XCL_026\" = \"r2\".\"XCL_014\" WHERE \"r2\".\"XCL_015\" = 'Marvel Comics' GROUP BY \"r1\".\"XCL_006\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:728"
  ]
}
```

### Aggregates the count of superhero records (identified by XCL_018) that are joined to the 'Strength' attribute with a value of 100 and belong to the 'F

```json
{
  "kind": "metric",
  "formula": "COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" INNER JOIN gender AS T4 ON T1.\"XCL_021\" = T4.\"XCL_007\" WHERE T3.\"XCL_004\" = 'Strength' AND T2.\"XCL_011\" = 100 AND T4.\"XCL_008\" = 'Female'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_attribute"
      },
      {
        "role": "r2",
        "physical_table": "attribute"
      },
      {
        "role": "r3",
        "physical_table": "gender"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_attribute AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_009\" INNER JOIN attribute AS \"r2\" ON \"r1\".\"XCL_010\" = \"r2\".\"XCL_003\" INNER JOIN gender AS \"r3\" ON \"r0\".\"XCL_021\" = \"r3\".\"XCL_007\" WHERE \"r2\".\"XCL_004\" = 'Strength' AND \"r1\".\"XCL_011\" = 100 AND \"r3\".\"XCL_008\" = 'Female'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:740"
  ]
}
```

### Calculates the percentage of female superheroes published by Marvel Comics relative to the total number of female superheroes. The numerator counts fe

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN \"publisher\".\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T2.\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN gender AS T3 ON T1.\"XCL_021\" = T3.\"XCL_007\" WHERE T3.\"XCL_008\" = 'Female'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(CASE WHEN \"r1\".\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      },
      {
        "role": "r2",
        "physical_table": "gender"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(CASE WHEN \"r1\".\"XCL_015\" = 'Marvel Comics' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\" INNER JOIN gender AS \"r2\" ON \"r0\".\"XCL_021\" = \"r2\".\"XCL_007\" WHERE \"r2\".\"XCL_008\" = 'Female'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:788"
  ]
}
```

### "superhero"."XCL_019" IN ('Hawkman', 'Karate Kid', 'Speedy')

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" IN ('Hawkman', 'Karate Kid', 'Speedy')",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_015\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_019\" IN ('Hawkman', 'Karate Kid', 'Speedy')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:798"
  ]
}
```

### Count of Superheroes

```json
{
  "kind": "metric",
  "formula": "COUNT(*)",
  "grain": [],
  "population_scope": "SELECT COUNT(*) FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" INNER JOIN gender AS T3 ON T3.\"XCL_007\" = T1.\"XCL_021\" WHERE T1.\"XCL_025\" = 21 AND T1.\"XCL_021\" = 1",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(*)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "race"
      },
      {
        "role": "r2",
        "physical_table": "gender"
      }
    ],
    "scope_sql": "SELECT COUNT(*) AS \"value\" FROM superhero AS \"r0\" INNER JOIN race AS \"r1\" ON \"r0\".\"XCL_025\" = \"r1\".\"XCL_016\" INNER JOIN gender AS \"r2\" ON \"r2\".\"XCL_007\" = \"r0\".\"XCL_021\" WHERE \"r0\".\"XCL_025\" = 21 AND \"r0\".\"XCL_021\" = 1",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:793"
  ]
}
```

### "hero_power"."XCL_012" = 56

```json
{
  "kind": "predicate",
  "formula": "\"hero_power\".\"XCL_012\" = 56",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_031\" FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.\"XCL_013\" = T2.\"XCL_030\" WHERE T1.\"XCL_012\" = 56",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:754"
  ]
}
```

### Superpower Identifier

```json
{
  "kind": "binding",
  "formula": "\"superpower\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_031\" FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.\"XCL_013\" = T2.\"XCL_030\" WHERE T1.\"XCL_012\" = 56",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_031\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "hero_power"
      },
      {
        "role": "r1",
        "physical_table": "superpower"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_031\" AS \"value\" FROM hero_power AS \"r0\" INNER JOIN superpower AS \"r1\" ON \"r0\".\"XCL_013\" = \"r1\".\"XCL_030\" WHERE \"r0\".\"XCL_012\" = 56",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:754"
  ]
}
```

### "hero_attribute"."XCL_011" BETWEEN 75 AND 80

```json
{
  "kind": "predicate",
  "formula": "\"hero_attribute\".\"XCL_011\" BETWEEN 75 AND 80",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" WHERE T2.\"XCL_011\" BETWEEN 75 AND 80",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:816"
  ]
}
```

### COUNT("hero_power"."XCL_013") > 15

```json
{
  "kind": "predicate",
  "formula": "COUNT(\"hero_power\".\"XCL_013\") > 15",
  "grain": [
    "\"superhero\".\"XCL_020\""
  ],
  "population_scope": "SELECT DISTINCT T1.\"XCL_020\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" GROUP BY T1.\"XCL_020\" HAVING COUNT(T2.\"XCL_013\") > 15",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:720"
  ]
}
```

### "gender"."XCL_008" = 'Female'

```json
{
  "kind": "predicate",
  "formula": "\"gender\".\"XCL_008\" = 'Female'",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T3.\"XCL_006\" = 'Blue' THEN T1.\"XCL_018\" ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN gender AS T2 ON T1.\"XCL_021\" = T2.\"XCL_007\" INNER JOIN colour AS T3 ON T1.\"XCL_024\" = T3.\"XCL_005\" WHERE T2.\"XCL_008\" = 'Female'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:775"
  ]
}
```

### Aggregates the total number of rows in the hero_power table (T1) that are joined to the superpower table (T2) where the superpower name (T2.XCL_031) i

```json
{
  "kind": "metric",
  "formula": "COUNT(\"hero_power\".\"XCL_012\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_012\") FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.\"XCL_013\" = T2.\"XCL_030\" WHERE T2.\"XCL_031\" = 'Stealth'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_012\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "hero_power"
      },
      {
        "role": "r1",
        "physical_table": "superpower"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_012\") AS \"value\" FROM hero_power AS \"r0\" INNER JOIN superpower AS \"r1\" ON \"r0\".\"XCL_013\" = \"r1\".\"XCL_030\" WHERE \"r1\".\"XCL_031\" = 'Stealth'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:765"
  ]
}
```

### "superhero"."XCL_019" = 'Atom IV'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = 'Atom IV'",
  "grain": [],
  "population_scope": "SELECT T4.\"XCL_002\", T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T3.\"XCL_030\" = T2.\"XCL_013\" INNER JOIN alignment AS T4 ON T1.\"XCL_027\" = T4.\"XCL_001\" WHERE T1.\"XCL_019\" = 'Atom IV'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:811"
  ]
}
```

### "alignment"."XCL_002" = 'Neutral'

```json
{
  "kind": "predicate",
  "formula": "\"alignment\".\"XCL_002\" = 'Neutral'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" WHERE T2.\"XCL_002\" = 'Neutral'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:785"
  ]
}
```

### Calculates the percentage of female superheroes among all bad superheroes. The population is restricted to superheroes with alignment 'Bad' (via T2."X

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN \"gender\".\"XCL_008\" = 'Female' THEN \"superhero\".\"XCL_018\" ELSE NULL END) AS REAL) * 100 / COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T3.\"XCL_008\" = 'Female' THEN T1.\"XCL_018\" ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" INNER JOIN gender AS T3 ON T1.\"XCL_021\" = T3.\"XCL_007\" WHERE T2.\"XCL_002\" = 'Bad'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(CASE WHEN \"r2\".\"XCL_008\" = 'Female' THEN \"r0\".\"XCL_018\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "alignment"
      },
      {
        "role": "r2",
        "physical_table": "gender"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(CASE WHEN \"r2\".\"XCL_008\" = 'Female' THEN \"r0\".\"XCL_018\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN alignment AS \"r1\" ON \"r0\".\"XCL_027\" = \"r1\".\"XCL_001\" INNER JOIN gender AS \"r2\" ON \"r0\".\"XCL_021\" = \"r2\".\"XCL_007\" WHERE \"r1\".\"XCL_002\" = 'Bad'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:818"
  ]
}
```

### "superhero"."XCL_019" = 'Black Panther'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = 'Black Panther'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_004\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T1.\"XCL_019\" = 'Black Panther' ORDER BY T2.\"XCL_011\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:830"
  ]
}
```

### Publisher Name

```json
{
  "kind": "binding",
  "formula": "\"publisher\".\"XCL_015\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_015\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_018\" = 38",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_015\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_015\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\" WHERE \"r0\".\"XCL_018\" = 38",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:809"
  ]
}
```

### Superpower Name

```json
{
  "kind": "binding",
  "formula": "\"superpower\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T1.\"XCL_020\" = 'Helen Parr'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_031\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_power"
      },
      {
        "role": "r2",
        "physical_table": "superpower"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_031\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_power AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_012\" INNER JOIN superpower AS \"r2\" ON \"r1\".\"XCL_013\" = \"r2\".\"XCL_030\" WHERE \"r0\".\"XCL_020\" = 'Helen Parr'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:807"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" INNER JOIN colour AS T3 ON T1.\"XCL_023\" = T3.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Blue' AND T3.\"XCL_006\" = 'Blond'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_019\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "colour"
      },
      {
        "role": "r2",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_019\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN colour AS \"r1\" ON \"r0\".\"XCL_022\" = \"r1\".\"XCL_005\" INNER JOIN colour AS \"r2\" ON \"r0\".\"XCL_023\" = \"r2\".\"XCL_005\" WHERE \"r1\".\"XCL_006\" = 'Blue' AND \"r2\".\"XCL_006\" = 'Blond'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:724"
  ]
}
```

### "colour"."XCL_006" = 'Blue' AND "gender"."XCL_008" = 'Male'

```json
{
  "kind": "predicate",
  "formula": "\"colour\".\"XCL_006\" = 'Blue' AND \"gender\".\"XCL_008\" = 'Male'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_017\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_023\" = T2.\"XCL_005\" INNER JOIN race AS T3 ON T1.\"XCL_025\" = T3.\"XCL_016\" INNER JOIN gender AS T4 ON T1.\"XCL_021\" = T4.\"XCL_007\" WHERE T2.\"XCL_006\" = 'Blue' AND T4.\"XCL_008\" = 'Male'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:817"
  ]
}
```

### NOT "superhero"."XCL_020" IS NULL AND ("superhero"."XCL_029" IS NULL OR "superhero"."XCL_029" = 0)

```json
{
  "kind": "predicate",
  "formula": "NOT \"superhero\".\"XCL_020\" IS NULL AND (\"superhero\".\"XCL_029\" IS NULL OR \"superhero\".\"XCL_029\" = 0)",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_020\" FROM superhero WHERE NOT \"XCL_020\" IS NULL AND (\"XCL_029\" IS NULL OR \"XCL_029\" = 0)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:805"
  ]
}
```

### Attribute Name

```json
{
  "kind": "binding",
  "formula": "\"attribute\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_004\", T2.\"XCL_011\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T1.\"XCL_019\" = '3-D Man'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_004\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_attribute"
      },
      {
        "role": "r2",
        "physical_table": "attribute"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_004\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_attribute AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_009\" INNER JOIN attribute AS \"r2\" ON \"r1\".\"XCL_010\" = \"r2\".\"XCL_003\" WHERE \"r0\".\"XCL_019\" = '3-D Man'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:796"
  ]
}
```

### Distinct Hair Colour

```json
{
  "kind": "binding",
  "formula": "\"colour\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T3.\"XCL_006\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" INNER JOIN colour AS T3 ON T1.\"XCL_023\" = T3.\"XCL_005\" WHERE T1.\"XCL_028\" = 185 AND T2.\"XCL_017\" = 'Human'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:758"
  ]
}
```

### Aggregates the total number of superhero records (identified by XCL_018) that are joined to the alignment table with value 'Good' and the gender table

```json
{
  "kind": "metric",
  "formula": "COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" INNER JOIN gender AS T3 ON T1.\"XCL_021\" = T3.\"XCL_007\" WHERE T2.\"XCL_002\" = 'Good' AND T3.\"XCL_008\" = 'Female'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "alignment"
      },
      {
        "role": "r2",
        "physical_table": "gender"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN alignment AS \"r1\" ON \"r0\".\"XCL_027\" = \"r1\".\"XCL_001\" INNER JOIN gender AS \"r2\" ON \"r0\".\"XCL_021\" = \"r2\".\"XCL_007\" WHERE \"r1\".\"XCL_002\" = 'Good' AND \"r2\".\"XCL_008\" = 'Female'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:815"
  ]
}
```

### Returns the value of column XCL_019 from the superhero table for records where the associated alignment is 'Neutral'. The grain is one row per superhe

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" WHERE T2.\"XCL_002\" = 'Neutral'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_019\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "alignment"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_019\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN alignment AS \"r1\" ON \"r0\".\"XCL_027\" = \"r1\".\"XCL_001\" WHERE \"r1\".\"XCL_002\" = 'Neutral'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:785"
  ]
}
```

### "superhero"."XCL_018" = 40

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_018\" = 40",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_029\", T2.\"XCL_017\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T1.\"XCL_018\" = 40",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:841"
  ]
}
```

### Superpower Name

```json
{
  "kind": "binding",
  "formula": "\"superpower\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T4.\"XCL_002\", T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T3.\"XCL_030\" = T2.\"XCL_013\" INNER JOIN alignment AS T4 ON T1.\"XCL_027\" = T4.\"XCL_001\" WHERE T1.\"XCL_019\" = 'Atom IV'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_031\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_power"
      },
      {
        "role": "r2",
        "physical_table": "superpower"
      },
      {
        "role": "r3",
        "physical_table": "alignment"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_031\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_power AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_012\" INNER JOIN superpower AS \"r2\" ON \"r2\".\"XCL_030\" = \"r1\".\"XCL_013\" INNER JOIN alignment AS \"r3\" ON \"r0\".\"XCL_027\" = \"r3\".\"XCL_001\" WHERE \"r0\".\"XCL_019\" = 'Atom IV'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:811"
  ]
}
```

### "superhero"."XCL_020" = 'Charles Chandler'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_020\" = 'Charles Chandler'",
  "grain": [],
  "population_scope": "SELECT \"XCL_019\" FROM superhero WHERE \"XCL_020\" = 'Charles Chandler'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:833"
  ]
}
```

### Eye Color

```json
{
  "kind": "binding",
  "formula": "\"colour\".\"XCL_006\"",
  "grain": [
    "\"colour\".\"XCL_006\""
  ],
  "population_scope": "SELECT colour.\"XCL_006\" AS EyeColor, COUNT(superhero.\"XCL_018\") AS Count, RANK() OVER (ORDER BY COUNT(superhero.\"XCL_018\") DESC) AS PopularityRank FROM superhero INNER JOIN colour ON superhero.\"XCL_022\" = colour.\"XCL_005\" INNER JOIN publisher ON superhero.\"XCL_026\" = publisher.\"XCL_014\" WHERE publisher.\"XCL_015\" = 'Marvel Comics' GROUP BY colour.\"XCL_006\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_006\"",
    "grain": [
      "\"r1\".\"XCL_006\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "colour"
      },
      {
        "role": "r2",
        "physical_table": "publisher"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_006\" AS \"grain_0\", \"r1\".\"XCL_006\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN colour AS \"r1\" ON \"r0\".\"XCL_022\" = \"r1\".\"XCL_005\" INNER JOIN publisher AS \"r2\" ON \"r0\".\"XCL_026\" = \"r2\".\"XCL_014\" WHERE \"r2\".\"XCL_015\" = 'Marvel Comics' GROUP BY \"r1\".\"XCL_006\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:728"
  ]
}
```

### "superhero"."XCL_019" = 'Cameron Hicks'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = 'Cameron Hicks'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_017\", T3.\"XCL_002\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" INNER JOIN alignment AS T3 ON T1.\"XCL_027\" = T3.\"XCL_001\" WHERE T1.\"XCL_019\" = 'Cameron Hicks'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:787"
  ]
}
```

### Popularity Rank

```json
{
  "kind": "metric",
  "formula": "RANK() OVER (ORDER BY COUNT(\"superhero\".\"XCL_018\") DESC)",
  "grain": [
    "\"colour\".\"XCL_006\""
  ],
  "population_scope": "SELECT colour.\"XCL_006\" AS EyeColor, COUNT(superhero.\"XCL_018\") AS Count, RANK() OVER (ORDER BY COUNT(superhero.\"XCL_018\") DESC) AS PopularityRank FROM superhero INNER JOIN colour ON superhero.\"XCL_022\" = colour.\"XCL_005\" INNER JOIN publisher ON superhero.\"XCL_026\" = publisher.\"XCL_014\" WHERE publisher.\"XCL_015\" = 'Marvel Comics' GROUP BY colour.\"XCL_006\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:728"
  ]
}
```

### "superpower"."XCL_031" = 'Super Strength'

```json
{
  "kind": "predicate",
  "formula": "\"superpower\".\"XCL_031\" = 'Super Strength'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_012\") FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.\"XCL_013\" = T2.\"XCL_030\" WHERE T2.\"XCL_031\" = 'Super Strength'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:718"
  ]
}
```

### "colour"."XCL_006" = 'Blond'

```json
{
  "kind": "predicate",
  "formula": "\"colour\".\"XCL_006\" = 'Blond'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_023\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Blond'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:735"
  ]
}
```

### Superpower Name

```json
{
  "kind": "binding",
  "formula": "\"superpower\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T1.\"XCL_019\" = 'Deathlok'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_031\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_power"
      },
      {
        "role": "r2",
        "physical_table": "superpower"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_031\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_power AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_012\" INNER JOIN superpower AS \"r2\" ON \"r1\".\"XCL_013\" = \"r2\".\"XCL_030\" WHERE \"r0\".\"XCL_019\" = 'Deathlok'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:749"
  ]
}
```

### Average Hero Attribute Value

```json
{
  "kind": "metric",
  "formula": "AVG(\"hero_attribute\".\"XCL_011\")",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_011\") FROM hero_attribute AS T1 INNER JOIN superhero AS T2 ON T1.\"XCL_009\" = T2.\"XCL_018\" INNER JOIN alignment AS T3 ON T2.\"XCL_027\" = T3.\"XCL_001\" WHERE T3.\"XCL_002\" = 'Neutral'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_011\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "hero_attribute"
      },
      {
        "role": "r1",
        "physical_table": "superhero"
      },
      {
        "role": "r2",
        "physical_table": "alignment"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_011\") AS \"value\" FROM hero_attribute AS \"r0\" INNER JOIN superhero AS \"r1\" ON \"r0\".\"XCL_009\" = \"r1\".\"XCL_018\" INNER JOIN alignment AS \"r2\" ON \"r1\".\"XCL_027\" = \"r2\".\"XCL_001\" WHERE \"r2\".\"XCL_002\" = 'Neutral'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:813"
  ]
}
```

### "superpower"."XCL_031" = 'Cryokinesis'

```json
{
  "kind": "predicate",
  "formula": "\"superpower\".\"XCL_031\" = 'Cryokinesis'",
  "grain": [],
  "population_scope": "SELECT \"XCL_030\" FROM superpower WHERE \"XCL_031\" = 'Cryokinesis'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:803"
  ]
}
```

### A scalar metric computed by dividing the sum of column XCL_028 by the count of column XCL_018 across all rows in the superhero table. The numerator is

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"superhero\".\"XCL_028\") AS REAL) / COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(\"XCL_028\") AS REAL) / COUNT(\"XCL_018\") FROM superhero",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(\"r0\".\"XCL_028\") AS REAL) / COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(\"r0\".\"XCL_028\") AS REAL) / COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:791"
  ]
}
```

### "race"."XCL_017" = 'Alien'

```json
{
  "kind": "predicate",
  "formula": "\"race\".\"XCL_017\" = 'Alien'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(T1.\"XCL_029\") AS REAL) / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T2.\"XCL_017\" = 'Alien'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:789"
  ]
}
```

### "superhero"."XCL_018" = 38

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_018\" = 38",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_015\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_018\" = 38",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:809"
  ]
}
```

### "colour"."XCL_006" = 'Amber'

```json
{
  "kind": "predicate",
  "formula": "\"colour\".\"XCL_006\" = 'Amber'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_028\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Amber'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:781"
  ]
}
```

### Publisher Name

```json
{
  "kind": "binding",
  "formula": "\"publisher\".\"XCL_015\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_015\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_019\" = 'Sauron'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_015\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_015\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\" WHERE \"r0\".\"XCL_019\" = 'Sauron'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:727"
  ]
}
```

### Count of Neutral Superheroes

```json
{
  "kind": "metric",
  "formula": "COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.\"XCL_027\" = T2.\"XCL_001\" WHERE T2.\"XCL_002\" = 'Neutral'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "alignment"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN alignment AS \"r1\" ON \"r0\".\"XCL_027\" = \"r1\".\"XCL_001\" WHERE \"r1\".\"XCL_002\" = 'Neutral'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:795"
  ]
}
```

### Hero Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"hero_attribute\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T1.\"XCL_019\" = 'Hulk' AND T3.\"XCL_004\" = 'Strength'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_011\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_attribute"
      },
      {
        "role": "r2",
        "physical_table": "attribute"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_011\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_attribute AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_009\" INNER JOIN attribute AS \"r2\" ON \"r1\".\"XCL_010\" = \"r2\".\"XCL_003\" WHERE \"r0\".\"XCL_019\" = 'Hulk' AND \"r2\".\"XCL_004\" = 'Strength'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:820"
  ]
}
```

### Calculates the percentage of superheroes associated with the colour 'Blue'. The numerator counts superheroes where the joined colour name is 'Blue', a

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN \"colour\".\"XCL_006\" = 'Blue' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T2.\"XCL_006\" = 'Blue' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(CASE WHEN \"r1\".\"XCL_006\" = 'Blue' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(CASE WHEN \"r1\".\"XCL_006\" = 'Blue' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN colour AS \"r1\" ON \"r0\".\"XCL_022\" = \"r1\".\"XCL_005\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:800"
  ]
}
```

### Calculates the percentage of female superheroes whose associated colour is 'Blue'. The numerator counts female superheroes with blue colour, and the d

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN \"colour\".\"XCL_006\" = 'Blue' THEN \"superhero\".\"XCL_018\" ELSE NULL END) AS REAL) * 100 / COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN T3.\"XCL_006\" = 'Blue' THEN T1.\"XCL_018\" ELSE NULL END) AS REAL) * 100 / COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN gender AS T2 ON T1.\"XCL_021\" = T2.\"XCL_007\" INNER JOIN colour AS T3 ON T1.\"XCL_024\" = T3.\"XCL_005\" WHERE T2.\"XCL_008\" = 'Female'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(CASE WHEN \"r2\".\"XCL_006\" = 'Blue' THEN \"r0\".\"XCL_018\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "gender"
      },
      {
        "role": "r2",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(CASE WHEN \"r2\".\"XCL_006\" = 'Blue' THEN \"r0\".\"XCL_018\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN gender AS \"r1\" ON \"r0\".\"XCL_021\" = \"r1\".\"XCL_007\" INNER JOIN colour AS \"r2\" ON \"r0\".\"XCL_024\" = \"r2\".\"XCL_005\" WHERE \"r1\".\"XCL_008\" = 'Female'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:775"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T3.\"XCL_031\" = 'Flight'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_019\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_power"
      },
      {
        "role": "r2",
        "physical_table": "superpower"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_019\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_power AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_012\" INNER JOIN superpower AS \"r2\" ON \"r1\".\"XCL_013\" = \"r2\".\"XCL_030\" WHERE \"r2\".\"XCL_031\" = 'Flight'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:771"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\", T2.\"XCL_015\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_022\" = T1.\"XCL_023\" AND T1.\"XCL_022\" = T1.\"XCL_024\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_019\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_019\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\" WHERE \"r0\".\"XCL_022\" = \"r0\".\"XCL_023\" AND \"r0\".\"XCL_022\" = \"r0\".\"XCL_024\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:773"
  ]
}
```

### Hero Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"hero_attribute\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_011\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" WHERE T1.\"XCL_019\" = 'Aquababy'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_011\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_attribute"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_011\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_attribute AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_009\" WHERE \"r0\".\"XCL_019\" = 'Aquababy'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:840"
  ]
}
```

### Aggregates the total number of superhero records (identified by XCL_018) that are published by 'Marvel Comics' and have a gender of 'Female'. The grai

```json
{
  "kind": "metric",
  "formula": "COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" INNER JOIN gender AS T3 ON T1.\"XCL_021\" = T3.\"XCL_007\" WHERE T2.\"XCL_015\" = 'Marvel Comics' AND T3.\"XCL_008\" = 'Female'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      },
      {
        "role": "r2",
        "physical_table": "gender"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\" INNER JOIN gender AS \"r2\" ON \"r0\".\"XCL_021\" = \"r2\".\"XCL_007\" WHERE \"r1\".\"XCL_015\" = 'Marvel Comics' AND \"r2\".\"XCL_008\" = 'Female'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:823"
  ]
}
```

### Value of column XCL_023 from the superhero table for female superheroes published by Dark Horse Comics.

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_023\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_022\", T1.\"XCL_023\", T1.\"XCL_024\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T2.\"XCL_014\" = T1.\"XCL_026\" INNER JOIN gender AS T3 ON T3.\"XCL_007\" = T1.\"XCL_021\" WHERE T2.\"XCL_015\" = 'Dark Horse Comics' AND T3.\"XCL_008\" = 'Female'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_023\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      },
      {
        "role": "r2",
        "physical_table": "gender"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_023\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r1\".\"XCL_014\" = \"r0\".\"XCL_026\" INNER JOIN gender AS \"r2\" ON \"r2\".\"XCL_007\" = \"r0\".\"XCL_021\" WHERE \"r1\".\"XCL_015\" = 'Dark Horse Comics' AND \"r2\".\"XCL_008\" = 'Female'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:772"
  ]
}
```

### A scalar metric computed over the joined population of superhero and colour tables. It divides the total count of joined rows by the count of rows whe

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(*) AS REAL) / SUM(CASE WHEN \"colour\".\"XCL_005\" = 1 THEN 1 ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(*) AS REAL) / SUM(CASE WHEN T2.\"XCL_005\" = 1 THEN 1 ELSE 0 END) FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_024\" = T2.\"XCL_005\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(*) AS REAL) / SUM(CASE WHEN \"r1\".\"XCL_005\" = 1 THEN 1 ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(*) AS REAL) / SUM(CASE WHEN \"r1\".\"XCL_005\" = 1 THEN 1 ELSE 0 END) AS \"value\" FROM superhero AS \"r0\" INNER JOIN colour AS \"r1\" ON \"r0\".\"XCL_024\" = \"r1\".\"XCL_005\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:767"
  ]
}
```

### Scalar value of column XCL_029 from the superhero table where XCL_020 matches 'Charles Chandler'. Acts as the subtrahend in the final subtraction.

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_029\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_029\" FROM superhero WHERE \"XCL_020\" LIKE 'Charles Chandler'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_029\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_029\" AS \"value\" FROM superhero AS \"r0\" WHERE \"r0\".\"XCL_020\" LIKE 'Charles Chandler'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:790"
  ]
}
```

### "attribute"."XCL_004" = 'Speed'

```json
{
  "kind": "predicate",
  "formula": "\"attribute\".\"XCL_004\" = 'Speed'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.\"XCL_018\" = T2.\"XCL_009\" INNER JOIN attribute AS T3 ON T2.\"XCL_010\" = T3.\"XCL_003\" WHERE T3.\"XCL_004\" = 'Speed' ORDER BY T2.\"XCL_011\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:794"
  ]
}
```

### "superhero"."XCL_019" = 'Sauron'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_019\" = 'Sauron'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_015\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_019\" = 'Sauron'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:727"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T2.\"XCL_017\" = 'Alien'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_019\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "race"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_019\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN race AS \"r1\" ON \"r0\".\"XCL_025\" = \"r1\".\"XCL_016\" WHERE \"r1\".\"XCL_017\" = 'Alien'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:752"
  ]
}
```

### Superpower Name

```json
{
  "kind": "binding",
  "formula": "\"superpower\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_031\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T1.\"XCL_019\" = 'Abomination'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_031\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_power"
      },
      {
        "role": "r2",
        "physical_table": "superpower"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_031\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_power AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_012\" INNER JOIN superpower AS \"r2\" ON \"r1\".\"XCL_013\" = \"r2\".\"XCL_030\" WHERE \"r0\".\"XCL_019\" = 'Abomination'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:792"
  ]
}
```

### "superpower"."XCL_031" = 'Phoenix Force'

```json
{
  "kind": "predicate",
  "formula": "\"superpower\".\"XCL_031\" = 'Phoenix Force'",
  "grain": [],
  "population_scope": "SELECT T4.\"XCL_008\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" INNER JOIN gender AS T4 ON T1.\"XCL_021\" = T4.\"XCL_007\" WHERE T3.\"XCL_031\" = 'Phoenix Force'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:825"
  ]
}
```

### "superhero"."XCL_020" LIKE 'Charles Chandler'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_020\" LIKE 'Charles Chandler'",
  "grain": [],
  "population_scope": "SELECT \"XCL_029\" FROM superhero WHERE \"XCL_020\" LIKE 'Charles Chandler'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:790"
  ]
}
```

### Colour Name

```json
{
  "kind": "binding",
  "formula": "\"colour\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_020\" = 'Abraham Sapien'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_006\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN colour AS \"r1\" ON \"r0\".\"XCL_022\" = \"r1\".\"XCL_005\" WHERE \"r0\".\"XCL_020\" = 'Abraham Sapien'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:770"
  ]
}
```

### "superhero"."XCL_029" < 100 AND "colour"."XCL_006" = 'Brown'

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_029\" < 100 AND \"colour\".\"XCL_006\" = 'Brown'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_020\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T1.\"XCL_029\" < 100 AND T2.\"XCL_006\" = 'Brown'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:839"
  ]
}
```

### "superpower"."XCL_031" = 'Death Touch'

```json
{
  "kind": "predicate",
  "formula": "\"superpower\".\"XCL_031\" = 'Death Touch'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" WHERE T3.\"XCL_031\" = 'Death Touch'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:739"
  ]
}
```

### Aggregates the total number of superhero records (identified by XCL_018) that are associated with the colour 'Blue' via the join condition on XCL_022 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Blue'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN colour AS \"r1\" ON \"r0\".\"XCL_022\" = \"r1\".\"XCL_005\" WHERE \"r1\".\"XCL_006\" = 'Blue'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:721"
  ]
}
```

### Race Identifier

```json
{
  "kind": "binding",
  "formula": "\"race\".\"XCL_017\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\", T2.\"XCL_017\" FROM superhero AS T1 INNER JOIN race AS T2 ON T1.\"XCL_025\" = T2.\"XCL_016\" WHERE T1.\"XCL_020\" = 'Charles Chandler'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_017\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "race"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_017\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN race AS \"r1\" ON \"r0\".\"XCL_025\" = \"r1\".\"XCL_016\" WHERE \"r0\".\"XCL_020\" = 'Charles Chandler'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:776"
  ]
}
```

### Superhero Identifier

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_022\" = T2.\"XCL_005\" AND T1.\"XCL_023\" = T2.\"XCL_005\" WHERE T2.\"XCL_006\" = 'Black'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_019\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_019\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN colour AS \"r1\" ON \"r0\".\"XCL_022\" = \"r1\".\"XCL_005\" AND \"r0\".\"XCL_023\" = \"r1\".\"XCL_005\" WHERE \"r1\".\"XCL_006\" = 'Black'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:782"
  ]
}
```

### "alignment"."XCL_002" = 'Neutral'

```json
{
  "kind": "predicate",
  "formula": "\"alignment\".\"XCL_002\" = 'Neutral'",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_011\") FROM hero_attribute AS T1 INNER JOIN superhero AS T2 ON T1.\"XCL_009\" = T2.\"XCL_018\" INNER JOIN alignment AS T3 ON T2.\"XCL_027\" = T3.\"XCL_001\" WHERE T3.\"XCL_002\" = 'Neutral'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:813"
  ]
}
```

### Colour Name

```json
{
  "kind": "binding",
  "formula": "\"colour\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_006\" FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.\"XCL_024\" = T2.\"XCL_005\" WHERE T1.\"XCL_019\" = 'Apocalypse'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_006\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_006\" AS \"value\" FROM superhero AS \"r0\" INNER JOIN colour AS \"r1\" ON \"r0\".\"XCL_024\" = \"r1\".\"XCL_005\" WHERE \"r0\".\"XCL_019\" = 'Apocalypse'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:722"
  ]
}
```

### Aggregates the count of superhero identifiers (XCL_018) for records where the associated superpower is 'Agility' and the associated colour is 'Blue'. 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"superhero\".\"XCL_018\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_018\") FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.\"XCL_018\" = T2.\"XCL_012\" INNER JOIN superpower AS T3 ON T2.\"XCL_013\" = T3.\"XCL_030\" INNER JOIN colour AS T4 ON T1.\"XCL_022\" = T4.\"XCL_005\" WHERE T3.\"XCL_031\" = 'Agility' AND T4.\"XCL_006\" = 'Blue'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_018\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "hero_power"
      },
      {
        "role": "r2",
        "physical_table": "superpower"
      },
      {
        "role": "r3",
        "physical_table": "colour"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_018\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN hero_power AS \"r1\" ON \"r0\".\"XCL_018\" = \"r1\".\"XCL_012\" INNER JOIN superpower AS \"r2\" ON \"r1\".\"XCL_013\" = \"r2\".\"XCL_030\" INNER JOIN colour AS \"r3\" ON \"r0\".\"XCL_022\" = \"r3\".\"XCL_005\" WHERE \"r2\".\"XCL_031\" = 'Agility' AND \"r3\".\"XCL_006\" = 'Blue'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:723"
  ]
}
```

### "superhero"."XCL_018" = 294

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_018\" = 294",
  "grain": [],
  "population_scope": "SELECT \"XCL_019\" FROM superhero WHERE \"XCL_018\" = 294",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:804"
  ]
}
```

### Returns the value of column "XCL_019" for the single row in the "superhero" table that has the highest value in column "XCL_028". The grain is a singl

```json
{
  "kind": "binding",
  "formula": "\"superhero\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_019\" FROM superhero ORDER BY \"XCL_028\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:802",
    "bird_dev:832"
  ]
}
```

### Boolean existence check verifying if a superhero is published by 'Marvel Comics'. Joins the publisher table to match the specific publisher name.

```json
{
  "kind": "binding",
  "formula": "1",
  "grain": [],
  "population_scope": "SELECT 1 FROM publisher AS T4 WHERE T4.\"XCL_015\" = 'Marvel Comics' AND T1.\"XCL_026\" = T4.\"XCL_014\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:730"
  ]
}
```

### "publisher"."XCL_015" = 'Marvel Comics'

```json
{
  "kind": "predicate",
  "formula": "\"publisher\".\"XCL_015\" = 'Marvel Comics'",
  "grain": [],
  "population_scope": "SELECT \"XCL_019\", \"XCL_028\", RANK() OVER (ORDER BY \"XCL_028\" DESC) AS HeightRank FROM superhero INNER JOIN publisher ON superhero.\"XCL_026\" = publisher.\"XCL_014\" WHERE publisher.\"XCL_015\" = 'Marvel Comics'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:726"
  ]
}
```

### Distinct Superpower Identifier

```json
{
  "kind": "binding",
  "formula": "\"superpower\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT T2.\"XCL_031\" FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.\"XCL_013\" = T2.\"XCL_030\" WHERE T1.\"XCL_012\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:764"
  ]
}
```

### "superhero"."XCL_022" = "superhero"."XCL_023" AND "superhero"."XCL_022" = "superhero"."XCL_024"

```json
{
  "kind": "predicate",
  "formula": "\"superhero\".\"XCL_022\" = \"superhero\".\"XCL_023\" AND \"superhero\".\"XCL_022\" = \"superhero\".\"XCL_024\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_019\", T2.\"XCL_015\" FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_022\" = T1.\"XCL_023\" AND T1.\"XCL_022\" = T1.\"XCL_024\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:773"
  ]
}
```

### Average XCL_028 for Marvel Comics Superheroes

```json
{
  "kind": "metric",
  "formula": "AVG(\"superhero\".\"XCL_028\")",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_028\") FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T2.\"XCL_015\" = 'Marvel Comics'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_028\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "superhero"
      },
      {
        "role": "r1",
        "physical_table": "publisher"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_028\") AS \"value\" FROM superhero AS \"r0\" INNER JOIN publisher AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\" WHERE \"r1\".\"XCL_015\" = 'Marvel Comics'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:729"
  ]
}
```


## 增量维护事件

- Source withdrawal preview · bird_dev:717 · Review event: withdraw this archived SQL source on a copied ontology
  - superpower.XCL_031: superpower_name → superpower_name
  - superhero.XCL_019: superhero_name → superhero_name
  - hero_power.XCL_012: hero_id → hero_id
  - superpower.XCL_030: superpower_id → superpower_id
  - hero_power.XCL_013: power_id → power_id
  - superhero.XCL_018: superhero_id → superhero_id
