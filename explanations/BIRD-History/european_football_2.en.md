# BIRD-History / european_football_2 — Schema and business semantics

The saved catalogue for this database contains 11 tables, 82 physical columns, 36 relationships and 129 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## Country

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: T3, c, t1, t4

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Country.XCL_001 | country_id | unknown | bird_dev:1101, bird_dev:1056, bird_dev:1126, bird_dev:1081, bird_dev:1127, bird_dev:1131, bird_dev:1128, bird_dev:1082 |
| Country.XCL_002 | country_name | unknown | bird_dev:1101, bird_dev:1056, bird_dev:1126, bird_dev:1081, bird_dev:1127, bird_dev:1131, bird_dev:1128, bird_dev:1082 |

## League

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: L, T4, l, l2, leagueData, t1, t2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| League.XCL_003 | league_id | unknown | bird_dev:1092, bird_dev:1139, bird_dev:1073, bird_dev:1145, bird_dev:1143, bird_dev:1038, bird_dev:1032, bird_dev:1025 |
| League.XCL_004 | country_id | unknown | bird_dev:1056, bird_dev:1081, bird_dev:1082, bird_dev:1070, bird_dev:1138 |
| League.XCL_005 | league_name | unknown | bird_dev:1056, bird_dev:1081, bird_dev:1092, bird_dev:1139, bird_dev:1073, bird_dev:1145, bird_dev:1143, bird_dev:1038 |

## Match

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: M, M2, T1, T2, T3, m, m2, m3, matchData, t1, t2, t3

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Match.XCL_006 | match_id | unknown | bird_dev:1101, bird_dev:1092, bird_dev:1073, bird_dev:1145, bird_dev:1131, bird_dev:1032, bird_dev:1142, bird_dev:1030 |
| Match.XCL_007 | country_id | unknown | bird_dev:1101, bird_dev:1126, bird_dev:1127, bird_dev:1131, bird_dev:1128, bird_dev:1057, bird_dev:1089 |
| Match.XCL_008 | league_id | unknown | bird_dev:1092, bird_dev:1139, bird_dev:1073, bird_dev:1145, bird_dev:1143, bird_dev:1038, bird_dev:1032, bird_dev:1025 |
| Match.XCL_009 | season | unknown | bird_dev:1092, bird_dev:1145, bird_dev:1025, bird_dev:1142, bird_dev:1030, bird_dev:1049, bird_dev:1028, bird_dev:1057 |
| Match.XCL_011 | match_date | unknown | bird_dev:1139, bird_dev:1073, bird_dev:1091 |
| Match.XCL_013 | home_team_id | unknown | bird_dev:1074, bird_dev:1026 |
| Match.XCL_014 | away_team_id | unknown | bird_dev:1101, bird_dev:1146, bird_dev:1028 |
| Match.XCL_015 | home_team_goals | unknown | bird_dev:1139, bird_dev:1143, bird_dev:1038, bird_dev:1025, bird_dev:1030, bird_dev:1074, bird_dev:1028, bird_dev:1057 |
| Match.XCL_016 | away_team_goals | unknown | bird_dev:1101, bird_dev:1146, bird_dev:1139, bird_dev:1038, bird_dev:1025, bird_dev:1030, bird_dev:1028, bird_dev:1026 |
| Match.XCL_061 | home_player_id | unknown | bird_dev:1126, bird_dev:1128 |
| Match.XCL_068 | away_player_id | unknown | bird_dev:1127 |

## Player

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: P, T0, T1, T1b, p, p2, t1, t1_inner, t2, t3

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Player.XCL_121 | player_id | unknown | bird_dev:1060, bird_dev:1064, bird_dev:1093, bird_dev:1040, bird_dev:1027, bird_dev:1131, bird_dev:1033, bird_dev:1133 |
| Player.XCL_122 | player_api_id | unknown | bird_dev:1122, bird_dev:1085, bird_dev:1094, bird_dev:1076, bird_dev:1120, bird_dev:1126, bird_dev:1064, bird_dev:1068 |
| Player.XCL_123 | player_name | unknown | bird_dev:1122, bird_dev:1085, bird_dev:1094, bird_dev:1115, bird_dev:1132, bird_dev:1076, bird_dev:1120, bird_dev:1106 |
| Player.XCL_124 | player_fifa_api_id | unknown | bird_dev:1115, bird_dev:1106, bird_dev:1114, bird_dev:1107 |
| Player.XCL_125 | date_of_birth | unknown | bird_dev:1060, bird_dev:1093, bird_dev:1050, bird_dev:1121, bird_dev:1044, bird_dev:1033, bird_dev:1084, bird_dev:1133 |
| Player.XCL_126 | height | unknown | bird_dev:1132, bird_dev:1068, bird_dev:1040, bird_dev:1058, bird_dev:1131, bird_dev:1033, bird_dev:1079, bird_dev:1021 |
| Player.XCL_127 | weight | unknown | bird_dev:1144, bird_dev:1061, bird_dev:1128, bird_dev:1117, bird_dev:1052 |

## Player_Attributes

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: PA, T2, T2b, T3, pa, pa2, pa3, pa4, t, t1, t2, t2_inner, t2_sub, t4

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Player_Attributes.XCL_128 | row_id | unknown | bird_dev:1076, bird_dev:1023, bird_dev:1068, bird_dev:1114, bird_dev:1135, bird_dev:1027, bird_dev:1144, bird_dev:1137 |
| Player_Attributes.XCL_129 | player_fifa_api_id | unknown | bird_dev:1115, bird_dev:1106, bird_dev:1040, bird_dev:1114, bird_dev:1107 |
| Player_Attributes.XCL_130 | player_api_id | unknown | bird_dev:1122, bird_dev:1085, bird_dev:1094, bird_dev:1080, bird_dev:1076, bird_dev:1064, bird_dev:1068, bird_dev:1097 |
| Player_Attributes.XCL_131 | date | unknown | bird_dev:1115, bird_dev:1106, bird_dev:1068, bird_dev:1034, bird_dev:1114, bird_dev:1047, bird_dev:1048, bird_dev:1102 |
| Player_Attributes.XCL_132 | overall_rating | unknown | bird_dev:1122, bird_dev:1094, bird_dev:1115, bird_dev:1023, bird_dev:1068, bird_dev:1093, bird_dev:1034, bird_dev:1114 |
| Player_Attributes.XCL_133 | potential | unknown | bird_dev:1135, bird_dev:1123, bird_dev:1075, bird_dev:1104, bird_dev:1022, bird_dev:1051, bird_dev:1063 |
| Player_Attributes.XCL_134 | preferred_foot | unknown | bird_dev:1080, bird_dev:1064, bird_dev:1050, bird_dev:1099, bird_dev:1135, bird_dev:1037, bird_dev:1052, bird_dev:1022 |
| Player_Attributes.XCL_135 | attacking_work_rate | unknown | bird_dev:1080, bird_dev:1124, bird_dev:1045, bird_dev:1105 |
| Player_Attributes.XCL_136 | defensive_work_rate | unknown | bird_dev:1106, bird_dev:1023, bird_dev:1084, bird_dev:1054 |
| Player_Attributes.XCL_137 | crossing | unknown | bird_dev:1085, bird_dev:1097, bird_dev:1024, bird_dev:1107, bird_dev:1136 |
| Player_Attributes.XCL_138 | finishing | unknown | bird_dev:1144, bird_dev:1125 |
| Player_Attributes.XCL_139 | heading_accuracy | unknown | bird_dev:1040, bird_dev:1047, bird_dev:1086 |
| Player_Attributes.XCL_141 | short_passing | unknown | bird_dev:1088, bird_dev:1087 |
| Player_Attributes.XCL_142 | volleys | unknown | bird_dev:1088 |
| Player_Attributes.XCL_143 | dribbling | unknown | bird_dev:1144 |
| Player_Attributes.XCL_145 | curve | unknown | bird_dev:1090 |
| Player_Attributes.XCL_146 | free_kick_accuracy | unknown | bird_dev:1076 |
| Player_Attributes.XCL_147 | long_passing | unknown | bird_dev:1140 |
| Player_Attributes.XCL_148 | ball_control | unknown | bird_dev:1140, bird_dev:1031 |
| Player_Attributes.XCL_149 | acceleration | unknown | bird_dev:1140 |
| Player_Attributes.XCL_151 | sprint_speed | unknown | bird_dev:1075 |
| Player_Attributes.XCL_153 | agility | unknown | bird_dev:1134 |
| Player_Attributes.XCL_154 | reactions | unknown | bird_dev:1137 |
| Player_Attributes.XCL_155 | balance | unknown | bird_dev:1137 |
| Player_Attributes.XCL_156 | shot_power | unknown | bird_dev:1039 |
| Player_Attributes.XCL_160 | jumping | unknown | bird_dev:1127 |
| Player_Attributes.XCL_161 | stamina | unknown | bird_dev:1027 |

## TEAM

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: T2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| TEAM.XCL_171 | team_id | unknown | bird_dev:1101 |
| TEAM.XCL_173 | team_name | unknown | bird_dev:1101 |

## Team

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: T, T1, t, t1, t2, t3, t4, teamDetails, teamInfo

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Team.XCL_170 | team_id | unknown | bird_dev:1041, bird_dev:1036 |
| Team.XCL_171 | team_api_id | unknown | bird_dev:1109, bird_dev:1129, bird_dev:1098, bird_dev:1041, bird_dev:1146, bird_dev:1071, bird_dev:1141, bird_dev:1113 |
| Team.XCL_172 | team_fifa_api_id | unknown | bird_dev:1046 |
| Team.XCL_173 | team_long_name | unknown | bird_dev:1129, bird_dev:1098, bird_dev:1041, bird_dev:1146, bird_dev:1141, bird_dev:1043, bird_dev:1113, bird_dev:1077 |
| Team.XCL_174 | team_short_name | unknown | bird_dev:1109, bird_dev:1071, bird_dev:1043, bird_dev:1077, bird_dev:1066, bird_dev:1067, bird_dev:1053, bird_dev:1074 |

## Team_Attributes

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: T2, TA, t1, t2, t3, t4, ta, ta2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Team_Attributes.XCL_175 | id | unknown | bird_dev:1095 |
| Team_Attributes.XCL_176 | team_id | unknown | bird_dev:1035 |
| Team_Attributes.XCL_177 | team_fifa_api_id | unknown | bird_dev:1109, bird_dev:1129, bird_dev:1098, bird_dev:1041, bird_dev:1071, bird_dev:1141, bird_dev:1113, bird_dev:1066 |
| Team_Attributes.XCL_178 | date | unknown | bird_dev:1109, bird_dev:1041, bird_dev:1113, bird_dev:1110, bird_dev:1108, bird_dev:1036, bird_dev:1112, bird_dev:1111 |
| Team_Attributes.XCL_179 | buildup_play_width | unknown | bird_dev:1071, bird_dev:1035, bird_dev:1029, bird_dev:1095 |
| Team_Attributes.XCL_180 | buildup_play_speed | unknown | bird_dev:1129, bird_dev:1141, bird_dev:1108, bird_dev:1065 |
| Team_Attributes.XCL_181 | buildup_play_passing | unknown | bird_dev:1071 |
| Team_Attributes.XCL_182 | buildup_play_passing_class | unknown | bird_dev:1109, bird_dev:1041 |
| Team_Attributes.XCL_183 | chance_creation_passing | unknown | bird_dev:1071, bird_dev:1067, bird_dev:1036 |
| Team_Attributes.XCL_184 | chance_creation_passing_class | unknown | bird_dev:1066, bird_dev:1110 |
| Team_Attributes.XCL_186 | chance_creation_crossing | unknown | bird_dev:1098, bird_dev:1041 |
| Team_Attributes.XCL_187 | chance_creation_crossing_class | unknown | bird_dev:1098, bird_dev:1111, bird_dev:1130 |
| Team_Attributes.XCL_189 | defence_pressure | unknown | bird_dev:1112 |
| Team_Attributes.XCL_191 | defence_aggression | unknown | bird_dev:1113 |

## Team_attributes

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: t2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Team_attributes.XCL_176 | team_id | unknown | bird_dev:1046 |
| Team_attributes.XCL_177 | team_api_id | unknown | bird_dev:1053 |
| Team_attributes.XCL_185 | defence_formation | unknown | bird_dev:1046 |
| Team_attributes.XCL_187 | defence_aggression | unknown | bird_dev:1053 |

## match

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: t2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| match.XCL_015 | home_team_goals | unknown | bird_dev:1121, bird_dev:1119 |
| match.XCL_016 | away_team_goals | unknown | bird_dev:1120 |
| match.XCL_072 | home_team_id | unknown | bird_dev:1121 |
| match.XCL_076 | away_team_id | unknown | bird_dev:1120 |
| match.XCL_080 | referee_id | unknown | bird_dev:1119 |

## player

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| player.XCL_123 | player_name | unknown | bird_dev:1069 |
| player.XCL_126 | height_cm | unknown | bird_dev:1069 |

## Relationships and join evidence

- Country.XCL_001 ↔ League.XCL_004; target_disjoint_historical_join
- Country.XCL_001 ↔ Match.XCL_007; target_disjoint_historical_join
- League.XCL_003 ↔ Match.XCL_008; target_disjoint_historical_join
- Match.XCL_006 ↔ Player.XCL_121; target_disjoint_historical_join
- Match.XCL_013 ↔ Team.XCL_171; target_disjoint_historical_join
- Match.XCL_014 ↔ TEAM.XCL_171; target_disjoint_historical_join
- Match.XCL_014 ↔ Team.XCL_171; target_disjoint_historical_join
- Match.XCL_061 ↔ Player.XCL_122; target_disjoint_historical_join
- Match.XCL_068 ↔ Player.XCL_122; target_disjoint_historical_join
- Player.XCL_121 ↔ Player_Attributes.XCL_128; target_disjoint_historical_join
- Player.XCL_122 ↔ Player_Attributes.XCL_130; target_disjoint_historical_join
- Player.XCL_122 ↔ match.XCL_072; target_disjoint_historical_join
- Player.XCL_122 ↔ match.XCL_076; target_disjoint_historical_join
- Player.XCL_122 ↔ match.XCL_080; target_disjoint_historical_join
- Player.XCL_124 ↔ Player_Attributes.XCL_129; target_disjoint_historical_join
- Team.XCL_171 ↔ Team_Attributes.XCL_177; target_disjoint_historical_join
- Team.XCL_171 ↔ Team_attributes.XCL_177; target_disjoint_historical_join
- Team.XCL_172 ↔ Team_attributes.XCL_176; target_disjoint_historical_join
- Country.XCL_001 ↔ League.XCL_004; sql_workload_observed_join
- Country.XCL_001 ↔ Match.XCL_007; sql_workload_observed_join
- League.XCL_003 ↔ Match.XCL_008; sql_workload_observed_join
- Match.XCL_006 ↔ Player.XCL_121; sql_workload_observed_join
- Match.XCL_013 ↔ Team.XCL_171; sql_workload_observed_join
- Match.XCL_014 ↔ TEAM.XCL_171; sql_workload_observed_join
- Match.XCL_014 ↔ Team.XCL_171; sql_workload_observed_join
- Match.XCL_061 ↔ Player.XCL_122; sql_workload_observed_join
- Match.XCL_068 ↔ Player.XCL_122; sql_workload_observed_join
- Player.XCL_121 ↔ Player_Attributes.XCL_128; sql_workload_observed_join
- Player.XCL_122 ↔ Player_Attributes.XCL_130; sql_workload_observed_join
- Player.XCL_122 ↔ match.XCL_072; sql_workload_observed_join
- Player.XCL_122 ↔ match.XCL_076; sql_workload_observed_join
- Player.XCL_122 ↔ match.XCL_080; sql_workload_observed_join
- Player.XCL_124 ↔ Player_Attributes.XCL_129; sql_workload_observed_join
- Team.XCL_171 ↔ Team_Attributes.XCL_177; sql_workload_observed_join
- Team.XCL_171 ↔ Team_attributes.XCL_177; sql_workload_observed_join
- Team.XCL_172 ↔ Team_attributes.XCL_176; sql_workload_observed_join

## Business definitions, population and grain

### A query that joins Player and Player_Attributes to find the highest attribute value (XCL_137) for a specific set of players (Alexis, Ariel Borysiuk, A

```json
{
  "kind": "program",
  "formula": "SELECT t1.\"XCL_123\", t2.\"XCL_137\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" IN ('Alexis', 'Ariel Borysiuk', 'Arouna Kone') ORDER BY t2.\"XCL_137\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1085"
  ]
}
```

### A query that joins Team and Team_Attributes to retrieve a specific attribute (XCL_191) for a given team name ('Hannover 96') and date prefix ('2015-09

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_191\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'Hannover 96' AND t2.\"XCL_178\" LIKE '2015-09-10%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1113"
  ]
}
```

### A SQL program that retrieves the cross passes attribute (XCL_139) for the player named 'Ariel Borysiuk'. It performs an inner join between the Player 

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_139\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Ariel Borysiuk'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1086"
  ]
}
```

### Full SQL program that joins Country and Match tables on Country.XCL_001 = Match.XCL_007. It filters for Country.XCL_002 = 'Poland' and Match.XCL_009 =

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(t2.\"XCL_015\") AS REAL) / COUNT(t2.\"XCL_006\") FROM Country AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_001\" = t2.\"XCL_007\" WHERE t1.\"XCL_002\" = 'Poland' AND t2.\"XCL_009\" = '2010/2011'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1057"
  ]
}
```

### A query that retrieves the "XCL_123" value from the "Player" table, ordered by "XCL_126" in descending order, limited to the first result.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_123\" FROM Player ORDER BY \"XCL_126\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1079",
    "bird_dev:1021"
  ]
}
```

### Full SQL program joining Player and Player_Attributes on XCL_122 = XCL_130, filtering Player records where XCL_126 < 180, and computing the percentage

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(CASE WHEN t2.\"XCL_132\" > 70 THEN t1.\"XCL_121\" ELSE NULL END) AS REAL) * 100 / COUNT(t1.\"XCL_121\") AS percent FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_126\" < 180",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1148"
  ]
}
```

### A SQL program that selects "XCL_173" from the Team table, restricted to rows where "XCL_174" is 'GEN'. This represents a specific subset of team data 

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_173\" FROM Team WHERE \"XCL_174\" = 'GEN'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1077"
  ]
}
```

### Latest Team_Attributes for Ajax

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_186\", t2.\"XCL_187\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'Ajax' ORDER BY t2.\"XCL_186\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1098"
  ]
}
```

### A query that retrieves the single player record from the player table with the lowest value in column "XCL_126" (ascending order). Returns the corresp

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_123\" FROM player ORDER BY \"XCL_126\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1069"
  ]
}
```

### A two-stage query that first identifies the most recent attribute record for a specific player (filtered by name 'Kevin Constant') by sorting on times

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_131\" FROM (SELECT t2.\"XCL_137\", t2.\"XCL_131\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_124\" = t2.\"XCL_129\" WHERE t1.\"XCL_123\" = 'Kevin Constant' ORDER BY t2.\"XCL_137\" DESC) ORDER BY \"XCL_131\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1107"
  ]
}
```

### A query that identifies the top 4 leagues based on the total number of matches recorded in the 2015/2016 season. It joins League and Match tables on t

```json
{
  "kind": "program",
  "formula": "SELECT t1.\"XCL_005\" FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t2.\"XCL_009\" = '2015/2016' GROUP BY t1.\"XCL_005\" ORDER BY COUNT(t2.\"XCL_006\") DESC LIMIT 4",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1145"
  ]
}
```

### Full SQL program that joins Player and Player_Attributes on XCL_124 = XCL_129, filters for player name 'Marko Arnautovic' and a date range on XCL_131,

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(t2.\"XCL_132\") AS REAL) / COUNT(t2.\"XCL_128\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_124\" = t2.\"XCL_129\" WHERE t1.\"XCL_123\" = 'Marko Arnautovic' AND SUBSTRING(t2.\"XCL_131\", 1, 10) BETWEEN '2007-02-22' AND '2016-04-21'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1114"
  ]
}
```

### A full SQL program that joins Country and League tables on XCL_001 = XCL_004, filters for League XCL_005 = 'Belgium Jupiler League', and selects Count

```json
{
  "kind": "program",
  "formula": "SELECT t1.\"XCL_002\" FROM Country AS t1 INNER JOIN League AS t2 ON t1.\"XCL_001\" = t2.\"XCL_004\" WHERE t2.\"XCL_005\" = 'Belgium Jupiler League'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1081"
  ]
}
```

### A SQL program that joins the 'Team' table (alias t1) with the 'Team_Attributes' table (alias t2) on the key 'XCL_171' = 'XCL_177'. It filters for the 

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(t2.\"XCL_179\") AS REAL) / COUNT(t2.\"XCL_175\") FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'Heart of Midlothian'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1095"
  ]
}
```

### A full SQL program that identifies the team with the most wins in a specific league and season. It joins League, Match, and Team tables, filters for '

```json
{
  "kind": "program",
  "formula": "SELECT teamInfo.\"XCL_173\" FROM League AS leagueData INNER JOIN Match AS matchData ON leagueData.\"XCL_003\" = matchData.\"XCL_008\" INNER JOIN Team AS teamInfo ON matchData.\"XCL_014\" = teamInfo.\"XCL_171\" WHERE leagueData.\"XCL_005\" = 'Scotland Premier League' AND matchData.\"XCL_009\" = '2009/2010' AND matchData.\"XCL_016\" - matchData.\"XCL_015\" > 0 GROUP BY matchData.\"XCL_014\" ORDER BY COUNT(*) DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1028"
  ]
}
```

### A query that identifies the league (XCL_005) with the highest number of matches (XCL_006) by aggregating match counts per league (XCL_008), finding th

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_005\", t1.\"max_count\" FROM League AS t2 JOIN (SELECT \"XCL_008\", MAX(\"cnt\") AS max_count FROM (SELECT \"XCL_008\", COUNT(\"XCL_006\") AS cnt FROM Match GROUP BY \"XCL_008\") AS subquery) AS t1 ON t1.\"XCL_008\" = t2.\"XCL_003\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1032"
  ]
}
```

### Player Attribute Lookup

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_132\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE SUBSTRING(t2.\"XCL_131\", 1, 10) = '2016-02-04' AND t1.\"XCL_123\" = 'Aaron Mooy'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1103"
  ]
}
```

### A SQL program that joins the Player table (t1) with the Player_Attributes table (t2) on the player identifier (XCL_122 = XCL_130). It filters for the 

```json
{
  "kind": "program",
  "formula": "SELECT MAX(t2.\"XCL_132\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Dorlan Pabon'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1100"
  ]
}
```

### A program that joins Match and League tables, filters for the 2015/2016 season and specific condition (XCL_015 = XCL_016), groups by league identifier

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_005\" FROM Match AS t1 INNER JOIN League AS t2 ON t1.\"XCL_008\" = t2.\"XCL_003\" WHERE t1.\"XCL_009\" = '2015/2016' AND t1.\"XCL_015\" = t1.\"XCL_016\" GROUP BY t2.\"XCL_005\" ORDER BY COUNT(t1.\"XCL_006\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1030"
  ]
}
```

### Full SQL program that joins Player and Player_Attributes tables to identify unique players meeting specific attribute thresholds and time period const

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_132\" > 80 AND SUBSTRING(t2.\"XCL_131\", 1, 4) BETWEEN '2008' AND '2010'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1062"
  ]
}
```

### A query that identifies leagues with a positive net goal difference for the 2009/2010 season. It joins League and Match tables, filters for the specif

```json
{
  "kind": "program",
  "formula": "SELECT t1.\"XCL_005\" FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t2.\"XCL_009\" = '2009/2010' GROUP BY t1.\"XCL_005\" HAVING (CAST(SUM(t2.\"XCL_015\") AS REAL) / COUNT(DISTINCT t2.\"XCL_006\")) - (CAST(SUM(t2.\"XCL_016\") AS REAL) / COUNT(DISTINCT t2.\"XCL_006\")) > 0",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1042"
  ]
}
```

### A query that joins Player and Player_Attributes tables to retrieve a specific attribute value for a named player on a specific date.

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_135\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_131\" LIKE '2015-05-01%' AND t1.\"XCL_123\" = 'Francesco Migliore'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1105"
  ]
}
```

### A SQL program that selects the XCL_123 identifier from the Player table, filtering for records where the difference between the current date and the d

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_123\" FROM Player WHERE CAST((JULIANDAY('now') - JULIANDAY(\"XCL_125\")) AS REAL) / 365 >= 35",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1118"
  ]
}
```

### A query that selects the XCL_128 column from the Player_Attributes table, sorts the results by XCL_137 in descending order, and limits the output to t

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_128\" FROM Player_Attributes ORDER BY \"XCL_137\" DESC LIMIT 5",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1024"
  ]
}
```

### Player Attributes Query

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_148\", \"XCL_149\", \"XCL_147\" FROM Player_Attributes WHERE \"XCL_130\" IN (SELECT \"XCL_122\" FROM Player WHERE \"XCL_123\" = 'Alexis Blin')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1140"
  ]
}
```

### Risky Team Query

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t1.\"XCL_174\" FROM Team AS t1 INNER JOIN Team_attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_187\" = 'Risky'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1053"
  ]
}
```

### Full SQL program that joins Player and Player_Attributes on the player key (XCL_122 = XCL_130), filters for attribute values exceeding 70 in both XCL_

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_141\" > 70 AND t2.\"XCL_142\" > 70",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1088"
  ]
}
```

### Executes a count operation on the Player table, restricting the population to records where column XCL_127 is greater than 170 and column XCL_123 star

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_121\") FROM Player WHERE \"XCL_127\" > 170 AND \"XCL_123\" LIKE 'Adam%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1061"
  ]
}
```

### A query that joins Match and Team tables to retrieve the team identifier (XCL_173) for the match with the maximum value in column XCL_016, ordered in 

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_173\" FROM Match AS t1 INNER JOIN Team AS t2 ON t1.\"XCL_014\" = t2.\"XCL_171\" ORDER BY t1.\"XCL_016\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1146"
  ]
}
```

### A full SQL program that computes the percentage of Player_Attributes records satisfying the dual condition XCL_155 > 80 AND XCL_154 > 80. It aggregate

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(CASE WHEN \"XCL_155\" > 80 AND \"XCL_154\" > 80 THEN \"XCL_128\" ELSE NULL END) AS REAL) * 100 / COUNT(\"XCL_128\") FROM Player_Attributes AS t",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1137"
  ]
}
```

### A query that retrieves the distinct identifiers of players who have attribute data recorded on the most recent date present in the Player_Attributes t

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT (t1.\"XCL_123\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_133\" = (SELECT MAX(\"XCL_133\") FROM Player_Attributes)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1051"
  ]
}
```

### A query that retrieves "XCL_123" from the Player table where the first 7 characters of "XCL_125" equal '1970-10', effectively filtering for records as

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_123\" FROM Player WHERE SUBSTRING(\"XCL_125\", 1, 7) = '1970-10'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1044"
  ]
}
```

### Full SQL program that joins the 'Player' table (alias t1) with the 'match' table (alias t2) on 'XCL_122' = 'XCL_076'. It filters for specific player n

```json
{
  "kind": "program",
  "formula": "SELECT SUM(t2.\"XCL_016\") FROM Player AS t1 INNER JOIN match AS t2 ON t1.\"XCL_122\" = t2.\"XCL_076\" WHERE t1.\"XCL_123\" IN ('Daan Smith', 'Filipe Ferreira')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1120"
  ]
}
```

### A query that retrieves three specific attributes (XCL_128, XCL_138, XCL_143) for the player with the highest value in XCL_127. It uses a subquery to i

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_128\", \"XCL_138\", \"XCL_143\" FROM Player_Attributes WHERE \"XCL_130\" = (SELECT \"XCL_122\" FROM Player ORDER BY \"XCL_127\" DESC LIMIT 1) LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1144"
  ]
}
```

### A SQL program that joins Team and Team_Attributes to retrieve XCL_187 for the team 'PEC Zwolle' where the date prefix of XCL_178 is '2013-09-20'.

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_187\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'PEC Zwolle' AND SUBSTRING(t2.\"XCL_178\", 1, 10) = '2013-09-20'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1111"
  ]
}
```

### Executes a join between 'League' and 'Match' on 'XCL_003' = 'XCL_008', filters for the 'Netherlands Eredivisie' league, and aggregates the maximum 'XC

```json
{
  "kind": "program",
  "formula": "SELECT MAX(t2.\"XCL_015\") FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t1.\"XCL_005\" = 'Netherlands Eredivisie'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1143"
  ]
}
```

### Bundesliga Match Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(t2.\"XCL_006\") FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t1.\"XCL_005\" = 'Germany 1. Bundesliga' AND SUBSTRING(t2.\"XCL_011\", 1, 7) BETWEEN '2008-08' AND '2008-10'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1073"
  ]
}
```

### A query that joins Team and Team_Attributes to retrieve a specific attribute (XCL_184) for a given team name ('FC Lorient') and date prefix ('2010-02-

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_184\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'FC Lorient' AND t2.\"XCL_178\" LIKE '2010-02-22%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1110"
  ]
}
```

### A query that retrieves a specific attribute ('XCL_132') from the Player_Attributes table by joining with the Player table. It filters for a specific p

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_132\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Gabriel Tamas' AND STRFTIME('%Y', t2.\"XCL_131\") = '2011'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1048"
  ]
}
```

### A query that joins Player and Player_Attributes tables on the player ID (XCL_122 = XCL_130). It orders the results by the attribute value XCL_133 in d

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" ORDER BY t2.\"XCL_133\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1123"
  ]
}
```

### Executes a SELECT statement to count rows in Player_Attributes where column XCL_134 equals 'left' and column XCL_135 equals 'low'. This program encaps

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_130\") FROM Player_Attributes WHERE \"XCL_134\" = 'left' AND \"XCL_135\" = 'low'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1080"
  ]
}
```

### A query that retrieves the top 3 values of "XCL_123" from the Player table where "XCL_126" is greater than 180, sorted in ascending order by "XCL_123"

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_123\" FROM Player WHERE \"XCL_126\" > 180 ORDER BY \"XCL_123\" LIMIT 3",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1132"
  ]
}
```

### A query that joins Player and Player_Attributes tables to retrieve the XCL_134 attribute for the player ranked first by XCL_125 in descending order. I

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_134\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" ORDER BY t1.\"XCL_125\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1050"
  ]
}
```

### A query that retrieves distinct player identifiers and names from the Player table by joining with Player_Attributes on the player ID, filtered to inc

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t1.\"XCL_121\", t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_134\" = 'left'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1064"
  ]
}
```

### A query that joins the Player table with the Player_Attributes table on the player ID (XCL_122 = XCL_130) and filters for the player named 'Aaron Dora

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_133\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Aaron Doran'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1063"
  ]
}
```

### Query Top 2010 Attribute

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_130\" FROM Player_Attributes WHERE SUBSTRING(\"XCL_131\", 1, 4) = '2010' ORDER BY \"XCL_132\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1034"
  ]
}
```

### A query that retrieves a specific attribute (XCL_136) for a player identified by name ('Kevin Berigaud') on a specific date ('2013-02-22'). It joins t

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_136\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_124\" = t2.\"XCL_129\" WHERE SUBSTRING(t2.\"XCL_131\", 1, 10) = '2013-02-22' AND t1.\"XCL_123\" = 'Kevin Berigaud'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1106"
  ]
}
```

### Filtered Team List Query

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t1.\"XCL_174\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_179\" = 31 AND t2.\"XCL_181\" = 53 AND t2.\"XCL_183\" = 32",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1071"
  ]
}
```

### A query that retrieves the top 5 records from Player_Attributes where XCL_134 is 'right', ordered by XCL_133 in descending order, returning the XCL_12

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_128\" FROM Player_Attributes WHERE \"XCL_134\" = 'right' ORDER BY \"XCL_133\" DESC LIMIT 5",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1135"
  ]
}
```

### A query that joins Country, Match, and Player tables to calculate the average of Player.XCL_127 for each Country. It returns the Country.XCL_002 of th

```json
{
  "kind": "program",
  "formula": "SELECT t1.\"XCL_002\" FROM Country AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_001\" = t2.\"XCL_007\" INNER JOIN Player AS t3 ON t2.\"XCL_061\" = t3.\"XCL_122\" GROUP BY t1.\"XCL_002\" ORDER BY AVG(t3.\"XCL_127\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1128"
  ]
}
```

### Query: Attribute Values for David Wilson

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t2.\"XCL_136\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'David Wilson'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1054"
  ]
}
```

### A SQL program that joins the Player and Player_Attributes tables on 'XCL_122' and 'XCL_130'. It filters records where 'XCL_133' equals '61', orders th

```json
{
  "kind": "program",
  "formula": "SELECT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_133\" = '61' ORDER BY t2.\"XCL_151\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1075"
  ]
}
```

### Player_Attributes XCL_128 6 vs 23 Difference Query

```json
{
  "kind": "program",
  "formula": "SELECT SUM(CASE WHEN t1.\"XCL_128\" = 6 THEN t1.\"XCL_153\" ELSE 0 END) - SUM(CASE WHEN t1.\"XCL_128\" = 23 THEN t1.\"XCL_153\" ELSE 0 END) FROM Player_Attributes AS t1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1134"
  ]
}
```

### Full SQL program that joins the Player table (t1) with the Player_Attributes table (t2) on the key XCL_122 = XCL_130, filters for the player named 'Aa

```json
{
  "kind": "program",
  "formula": "SELECT SUM(t2.\"XCL_137\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Aaron Lennox'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1097"
  ]
}
```

### A SQL program that calculates the number of players with a 'left' preference (XCL_134) in the latest available data version (determined by MAX XCL_137

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(t1.\"XCL_128\") FROM Player_Attributes AS t1 WHERE t1.\"XCL_134\" = 'left' AND t1.\"XCL_137\" = (SELECT MAX(\"XCL_137\") FROM Player_Attributes)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1136"
  ]
}
```

### A program that finds the league(s) with the highest number of matches in the 2008/2009 season. It joins League and Match tables, filters by season, gr

```json
{
  "kind": "program",
  "formula": "SELECT t1.\"XCL_005\" FROM League AS t1 JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t2.\"XCL_009\" = '2008/2009' GROUP BY t1.\"XCL_005\" HAVING COUNT(t2.\"XCL_006\") = (SELECT MAX(\"match_count\") FROM (SELECT COUNT(t2.\"XCL_006\") AS match_count FROM Match AS t2 WHERE t2.\"XCL_009\" = '2008/2009' GROUP BY t2.\"XCL_008\"))",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1092"
  ]
}
```

### League Match Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(t2.\"XCL_006\") FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t1.\"XCL_005\" = 'Belgium Jupiler League' AND SUBSTRING(t2.\"XCL_011\", 1, 7) = '2009-04'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1091"
  ]
}
```

### Full query program that joins Team and Team_Attributes on the team key (XCL_171 = XCL_177), filters for attribute values (XCL_183) exceeding 70, and r

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t1.\"XCL_174\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_183\" > 70",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1067"
  ]
}
```

### A program that joins Match and League tables on XCL_008 = XCL_003, filters for the '2015/2016' season, groups by league identifier, and returns the le

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_005\" FROM Match AS t1 INNER JOIN League AS t2 ON t1.\"XCL_008\" = t2.\"XCL_003\" WHERE t1.\"XCL_009\" = '2015/2016' GROUP BY t2.\"XCL_005\" ORDER BY SUM(t1.\"XCL_015\" + t1.\"XCL_016\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1025"
  ]
}
```

### A query that joins Player and Player_Attributes on 'XCL_122' and 'XCL_130', orders by 'XCL_132' in descending order, and returns the first row's 'XCL_

```json
{
  "kind": "program",
  "formula": "SELECT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" ORDER BY t2.\"XCL_132\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1083"
  ]
}
```

### Post-1990 Player Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_121\") FROM Player WHERE STRFTIME('%Y', \"XCL_125\") > '1990'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1060"
  ]
}
```

### A query that joins Country and League tables on XCL_001 = XCL_004, filters for League XCL_005 = 'Italy Serie A', and selects Country XCL_002. It ident

```json
{
  "kind": "program",
  "formula": "SELECT t1.\"XCL_002\" FROM Country AS t1 INNER JOIN League AS t2 ON t1.\"XCL_001\" = t2.\"XCL_004\" WHERE t2.\"XCL_005\" = 'Italy Serie A'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1070"
  ]
}
```

### A query that joins Player and Player_Attributes, filters for players with a value in XCL_126 greater than 180, groups by player ID (XCL_121), and retu

```json
{
  "kind": "program",
  "formula": "SELECT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_126\" > 180 GROUP BY t1.\"XCL_121\" ORDER BY CAST(SUM(t2.\"XCL_139\") AS REAL) / COUNT(t2.\"XCL_129\") DESC LIMIT 10",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1040"
  ]
}
```

### Full SQL program that joins Player (t1) and Player_Attributes (t2) on Player.XCL_122 = Player_Attributes.XCL_130. It computes a single scalar value re

```json
{
  "kind": "program",
  "formula": "SELECT (SUM(CASE WHEN t1.\"XCL_123\" = 'Ariel Borysiuk' THEN t2.\"XCL_132\" ELSE 0 END) * 1.0 - SUM(CASE WHEN t1.\"XCL_123\" = 'Paulin Puel' THEN t2.\"XCL_132\" ELSE 0 END)) * 100 / SUM(CASE WHEN t1.\"XCL_123\" = 'Paulin Puel' THEN t2.\"XCL_132\" ELSE 0 END) FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1094"
  ]
}
```

### Full SQL program that joins Player and Player_Attributes tables to compute the difference in average attribute values (XCL_146) between two specific p

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN t1.\"XCL_123\" = 'Abdou Diallo' THEN t2.\"XCL_146\" ELSE 0 END) AS REAL) / COUNT(CASE WHEN t1.\"XCL_123\" = 'Abdou Diallo' THEN t2.\"XCL_128\" ELSE NULL END) - CAST(SUM(CASE WHEN t1.\"XCL_123\" = 'Aaron Appindangoye' THEN t2.\"XCL_146\" ELSE 0 END) AS REAL) / COUNT(CASE WHEN t1.\"XCL_123\" = 'Aaron Appindangoye' THEN t2.\"XCL_128\" ELSE NULL END) FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1076"
  ]
}
```

### Full SQL program that calculates the average of XCL_126 divided by the count of XCL_121 for players filtered by the year prefix of XCL_125.

```json
{
  "kind": "program",
  "formula": "SELECT SUM(\"XCL_126\") / COUNT(\"XCL_121\") FROM Player WHERE SUBSTRING(\"XCL_125\", 1, 4) BETWEEN '1990' AND '1995'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1033"
  ]
}
```

### Full SQL program that joins 'Player' (t1) and 'Player_Attributes' (t2) on 'XCL_122' = 'XCL_130', filters for 'XCL_123' = 'Aaron Doran', and calculates

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(t2.\"XCL_132\") AS REAL) / COUNT(t2.\"XCL_128\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Aaron Doran'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1072"
  ]
}
```

### Executes an inner join between Player (t1) and Player_Attributes (t2) on Player.XCL_122 = Player_Attributes.XCL_130. Applies filters: Player.XCL_126 >

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(t2.\"XCL_132\") AS REAL) / COUNT(t2.\"XCL_128\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_126\" > 170 AND STRFTIME('%Y', t2.\"XCL_131\") >= '2010' AND STRFTIME('%Y', t2.\"XCL_131\") <= '2015'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1068"
  ]
}
```

### A query that joins the Player and Player_Attributes tables on 'XCL_122' and 'XCL_130', orders the results by 'XCL_132' in descending order, and return

```json
{
  "kind": "program",
  "formula": "SELECT t1.\"XCL_125\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" ORDER BY t2.\"XCL_132\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1055"
  ]
}
```

### Full program that calculates the average of XCL_138 for players with the maximum and minimum XCL_126 values, joins Player and Player_Attributes on XCL

```json
{
  "kind": "program",
  "formula": "SELECT \"A\" FROM (SELECT AVG(\"XCL_138\") AS result, 'Max' AS A FROM Player AS T1 INNER JOIN Player_Attributes AS T2 ON T1.\"XCL_122\" = T2.\"XCL_130\" WHERE T1.\"XCL_126\" = (SELECT MAX(\"XCL_126\") FROM Player) UNION SELECT AVG(\"XCL_138\") AS result, 'Min' AS A FROM Player AS T1 INNER JOIN Player_Attributes AS T2 ON T1.\"XCL_122\" = T2.\"XCL_130\" WHERE T1.\"XCL_126\" = (SELECT MIN(\"XCL_126\") FROM Player)) ORDER BY \"result\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1058"
  ]
}
```

### Full SQL program that joins Player and Player_Attributes tables on player ID (XCL_124 = XCL_129), filters for the date 2013-07-12, and computes the pe

```json
{
  "kind": "program",
  "formula": "SELECT (SUM(CASE WHEN t1.\"XCL_123\" = 'Landon Donovan' THEN t2.\"XCL_132\" ELSE 0 END) * 1.0 - SUM(CASE WHEN t1.\"XCL_123\" = 'Jordan Bowery' THEN t2.\"XCL_132\" ELSE 0 END)) * 100 / SUM(CASE WHEN t1.\"XCL_123\" = 'Landon Donovan' THEN t2.\"XCL_132\" ELSE 0 END) AS LvsJ_percent FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_124\" = t2.\"XCL_129\" WHERE SUBSTRING(t2.\"XCL_131\", 1, 10) = '2013-07-12'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1115"
  ]
}
```

### A query that joins Player and Player_Attributes to retrieve a specific attribute value for a named player on a specific date. It filters by player nam

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_139\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Francois Affolter' AND SUBSTRING(t2.\"XCL_131\", 1, 10) = '2014-09-18'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1047"
  ]
}
```

### A query that retrieves the name of the first player (ordered by XCL_125 ascending) from a specific subset of players (Aaron Lennon, Abdelaziz Barrada)

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_123\" FROM Player WHERE \"XCL_123\" IN ('Aaron Lennon', 'Abdelaziz Barrada') ORDER BY \"XCL_125\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1078"
  ]
}
```

### Executes a SELECT DISTINCT query on Team_Attributes to retrieve unique "XCL_176" entries where "XCL_179" is greater than 50 and less than 60.

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT \"XCL_176\" FROM Team_Attributes WHERE \"XCL_179\" > 50 AND \"XCL_179\" < 60",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1035"
  ]
}
```

### A query that joins Country and League tables to retrieve the league identifier (XCL_005) for the country where XCL_002 is 'Netherlands'. The join cond

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_005\" FROM Country AS t1 INNER JOIN League AS t2 ON t1.\"XCL_001\" = t2.\"XCL_004\" WHERE t1.\"XCL_002\" = 'Netherlands'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1056"
  ]
}
```

### Full SQL program that joins Player and Player_Attributes tables on XCL_122 = XCL_130, filters for the player named 'Ahmed Samir Farag' (XCL_123), and 

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(t2.\"XCL_156\") AS REAL) / COUNT(t2.\"XCL_131\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Ahmed Samir Farag'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1039"
  ]
}
```

### Full SQL program that joins Team and Team_Attributes on the team key (XCL_171 = XCL_177), filters for attributes where XCL_180 is 'Slow', and returns 

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t1.\"XCL_173\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_180\" = 'Slow'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1129"
  ]
}
```

### Executes a join between 'Team' and 'Team_Attributes' on the key columns 'XCL_171' and 'XCL_177'. Filters for the specific team code 'CLB' and selects 

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t2.\"XCL_184\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_174\" = 'CLB'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1066"
  ]
}
```

### A query that joins Player and Player_Attributes to find a specific player. It filters for records where the date (XCL_131) starts with '2016-06-23' an

```json
{
  "kind": "program",
  "formula": "SELECT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE SUBSTRING(t2.\"XCL_131\", 1, 10) = '2016-06-23' AND t2.\"XCL_132\" = 77 ORDER BY t1.\"XCL_125\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1102"
  ]
}
```

### A full SQL program that joins Country, Match, and Player tables. It filters for the country 'Belgium' and retrieves the Player column XCL_123 for all 

```json
{
  "kind": "program",
  "formula": "SELECT t3.\"XCL_123\" FROM Country AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_001\" = t2.\"XCL_007\" INNER JOIN Player AS t3 ON t2.\"XCL_061\" = t3.\"XCL_122\" WHERE t1.\"XCL_002\" = 'Belgium'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1126"
  ]
}
```

### A query that joins the Team and Team_Attributes tables to retrieve a specific attribute (XCL_182) for a team. It filters for the team with code 'LEI' 

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_182\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_174\" = 'LEI' AND SUBSTRING(t2.\"XCL_178\", 1, 10) = '2015-09-10'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1109"
  ]
}
```

### Query that retrieves the identifier of the player(s) with the maximum XCL_126 value from the Player table using dense ranking.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_123\" FROM (SELECT \"XCL_123\", \"XCL_126\", DENSE_RANK() OVER (ORDER BY \"XCL_126\" DESC) AS rank FROM Player) WHERE \"rank\" = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1116"
  ]
}
```

### A query that joins Player_Attributes (t1) with Player (t2) on the key "XCL_128" = "XCL_121". It retrieves the "XCL_123" value from the Player table fo

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_123\" FROM Player_Attributes AS t1 INNER JOIN Player AS t2 ON t1.\"XCL_128\" = t2.\"XCL_121\" ORDER BY t1.\"XCL_161\" DESC LIMIT 10",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1027"
  ]
}
```

### League Match Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(t2.\"XCL_006\") FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t2.\"XCL_009\" = '2015/2016' AND t1.\"XCL_005\" = 'Scotland Premier League'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1049"
  ]
}
```

### A query that joins Team and Team_Attributes to retrieve a specific attribute (XCL_189) for a given team (Hull City) on a specific date (2010-02-22). I

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_189\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'Hull City' AND SUBSTRING(t2.\"XCL_178\", 1, 10) = '2010-02-22'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1112"
  ]
}
```

### Full SQL program that joins League and Match tables on XCL_003/XCL_008, filters for 'Italy Serie A' and season '2015/2016', and returns the count of m

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(t2.\"XCL_006\") FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t1.\"XCL_005\" = 'Italy Serie A' AND t2.\"XCL_009\" = '2015/2016'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1142"
  ]
}
```

### Full SQL program that joins the Player table (t1) with the Player_Attributes table (t2) on the player identifier (XCL_122 = XCL_130). It filters for t

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(t2.\"XCL_132\") AS REAL) / COUNT(t2.\"XCL_128\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Pietro Marino'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1096"
  ]
}
```

### Fast Team Lookup

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t1.\"XCL_173\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_180\" = 'Fast'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1065"
  ]
}
```

### Full SQL program joining Player and Player_Attributes to count distinct players (XCL_123) where the birth year (XCL_125) is before 1986 and the attrib

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT t1.\"XCL_123\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE STRFTIME('%Y', t1.\"XCL_125\") < '1986' AND t2.\"XCL_136\" = 'high'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1084"
  ]
}
```

### Full SQL program that joins Team and Team_Attributes on the team key (XCL_171 = XCL_177), filters for attribute value 'Safe' in XCL_187, and returns d

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t1.\"XCL_174\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_187\" = 'Safe'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1130"
  ]
}
```

### A query that joins the Team table with the Team_Attributes table to retrieve a specific attribute (XCL_180). It filters for the team named 'Willem II'

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_180\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'Willem II' AND SUBSTRING(t2.\"XCL_178\", 1, 10) = '2011-02-22'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1108"
  ]
}
```

### Full SQL program that joins Player and Player_Attributes tables to count distinct players with a 'left' attribute value and a specific threshold on XC

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT t1.\"XCL_121\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_127\" < 130 AND t2.\"XCL_134\" = 'left'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1052"
  ]
}
```

### Executes a SELECT statement on the Player table to compute the count of records matching specific criteria: XCL_125 > '1990' and XCL_123 LIKE 'Aaron%'

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_121\") FROM Player WHERE \"XCL_125\" > '1990' AND \"XCL_123\" LIKE 'Aaron%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1133"
  ]
}
```

### A query that retrieves the 'XCL_174' value for teams. It joins the Team table with the Match table on 'XCL_171' (Team) to 'XCL_013' (Match) and filter

```json
{
  "kind": "program",
  "formula": "SELECT t1.\"XCL_174\" FROM Team AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_171\" = t2.\"XCL_013\" WHERE t2.\"XCL_015\" = 10",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1074"
  ]
}
```

### A query that joins Player and Player_Attributes to retrieve a specific attribute value for a named player on a specific date. It filters by player nam

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_133\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE SUBSTRING(t2.\"XCL_131\", 1, 10) = '2010-08-30' AND t1.\"XCL_123\" = 'Francesco Parravicini'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1104"
  ]
}
```

### Player Attribute Lookup

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t2.\"XCL_134\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Abdou Diallo'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1099"
  ]
}
```

### A query that joins League and Match tables on the league key (XCL_003 = XCL_008), groups by league identifier (XCL_005), calculates the sum of XCL_015

```json
{
  "kind": "program",
  "formula": "SELECT t1.\"XCL_005\", SUM(t2.\"XCL_015\") + SUM(t2.\"XCL_016\") FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" GROUP BY t1.\"XCL_005\" ORDER BY SUM(t2.\"XCL_015\") + SUM(t2.\"XCL_016\") ASC LIMIT 5",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1038"
  ]
}
```

### A query that retrieves the top 10 rows from the Player table, sorted by column XCL_127 in descending order, returning only column XCL_122.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_122\" FROM Player ORDER BY \"XCL_127\" DESC LIMIT 10",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1117"
  ]
}
```

### Executes a join between Team_Attributes and Team on keys XCL_177 and XCL_171, filters for the team name 'KSV Cercle Brugge', and selects distinct valu

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t1.\"XCL_180\" FROM Team_Attributes AS t1 INNER JOIN Team AS t2 ON t1.\"XCL_177\" = t2.\"XCL_171\" WHERE t2.\"XCL_173\" = 'KSV Cercle Brugge'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1141"
  ]
}
```

### A query that returns the distinct player identifiers (XCL_123) from the Player table who are linked via XCL_122 to Player_Attributes records where the

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_132\" = (SELECT MAX(\"XCL_132\") FROM Player_Attributes)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1122",
    "bird_dev:1147"
  ]
}
```

### Filter Players by XCL_126 > 180

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_123\" FROM Player WHERE \"XCL_126\" > 180",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1059"
  ]
}
```

### A query that joins Player and Player_Attributes tables on XCL_122 = XCL_130, orders by Player.XCL_125 ascending, and returns the first record's Player

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_145\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" ORDER BY t1.\"XCL_125\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1090"
  ]
}
```

### A query that identifies a single player by joining the Player and Player_Attributes tables. It filters for players who have an attribute record where 

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_138\" = 1 ORDER BY t1.\"XCL_125\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1125"
  ]
}
```

### Full SQL program that joins Player and Player_Attributes tables on the player ID (XCL_122 = XCL_130), filters for attribute value 'high' (XCL_135), an

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_135\" = 'high'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1124"
  ]
}
```

### Query: Attributes for ADO Den Haag

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t2.\"XCL_185\" FROM Team AS t1 INNER JOIN Team_attributes AS t2 ON t1.\"XCL_172\" = t2.\"XCL_176\" WHERE t1.\"XCL_173\" = 'ADO Den Haag'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1046"
  ]
}
```

### Belgium Jupiler League Match Details Query

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_015\", t2.\"XCL_016\" FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t1.\"XCL_005\" = 'Belgium Jupiler League' AND t2.\"XCL_011\" LIKE '2008-09-24%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1139"
  ]
}
```

### A query that resolves the country associated with the 'Poland Ekstraklasa' league by joining the Country and League tables on their respective identif

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_002\" FROM Country WHERE \"XCL_001\" IN (SELECT \"XCL_004\" FROM League WHERE \"XCL_005\" = 'Poland Ekstraklasa')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1138"
  ]
}
```

### A query that identifies the team with the fewest matches where the score difference (XCL_015 - XCL_016) was negative (indicating a loss) during the 20

```json
{
  "kind": "program",
  "formula": "SELECT teamDetails.\"XCL_173\" FROM Match AS matchData INNER JOIN Team AS teamDetails ON matchData.\"XCL_013\" = teamDetails.\"XCL_171\" WHERE matchData.\"XCL_009\" = '2015/2016' AND matchData.\"XCL_015\" - matchData.\"XCL_016\" < 0 GROUP BY matchData.\"XCL_013\" ORDER BY COUNT(*) ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1026"
  ]
}
```

### A query that identifies distinct countries where matches were played by players possessing a specific attribute (XCL_160) exceeding 89. It joins Playe

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t4.\"XCL_002\" FROM Player_Attributes AS t1 INNER JOIN Player AS t2 ON t1.\"XCL_130\" = t2.\"XCL_122\" INNER JOIN Match AS t3 ON t2.\"XCL_122\" = t3.\"XCL_068\" INNER JOIN Country AS t4 ON t3.\"XCL_007\" = t4.\"XCL_001\" WHERE t1.\"XCL_160\" > 89",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1127"
  ]
}
```

### Min XCL_133 Attribute Lookup

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_134\" FROM Player_Attributes WHERE NOT \"XCL_133\" IS NULL ORDER BY \"XCL_133\" ASC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1022"
  ]
}
```

### Query: Attribute Values for Franco Zennaro

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t2.\"XCL_135\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Franco Zennaro'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1045"
  ]
}
```

### Full program that identifies distinct Team.XCL_173 values where the associated Team_Attributes.XCL_183 in 2012 exceeds the global 2012 average of XCL_

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT t4.\"XCL_173\" FROM Team_Attributes AS t3 INNER JOIN Team AS t4 ON t3.\"XCL_177\" = t4.\"XCL_171\" WHERE SUBSTRING(t3.\"XCL_178\", 1, 4) = '2012' AND t3.\"XCL_183\" > (SELECT CAST(SUM(t2.\"XCL_183\") AS REAL) / COUNT(t1.\"XCL_170\") FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE STRFTIME('%Y', t2.\"XCL_178\") = '2012')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1036"
  ]
}
```

### Filtered Player Attribute Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT t1.\"XCL_121\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_126\" > 180 AND t2.\"XCL_141\" > 70",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1087"
  ]
}
```

### A query that retrieves the top-ranked record from the Player_Attributes table by sorting in descending order on column XCL_132 and limiting the result

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_130\" FROM Player_Attributes ORDER BY \"XCL_132\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1020"
  ]
}
```

### A program that retrieves the 4 lowest values of the attribute XCL_179 from the Team_Attributes table. It joins with the Team table on XCL_177 = XCL_17

```json
{
  "kind": "program",
  "formula": "SELECT t1.\"XCL_179\" FROM Team_Attributes AS t1 INNER JOIN Team AS t2 ON t1.\"XCL_177\" = t2.\"XCL_171\" ORDER BY t1.\"XCL_179\" ASC LIMIT 4",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1029"
  ]
}
```

### Full SQL program joining Player, Match, and Country tables. It filters for Country.XCL_002 = 'Italy' and calculates the ratio of SUM(Player.XCL_126) t

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(T1.\"XCL_126\") AS REAL) / COUNT(T1.\"XCL_121\") FROM Player AS T1 INNER JOIN Match AS T2 ON T1.\"XCL_121\" = T2.\"XCL_006\" INNER JOIN Country AS T3 ON T2.\"XCL_007\" = T3.\"XCL_001\" WHERE T3.\"XCL_002\" = 'Italy'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1131"
  ]
}
```

### A query that joins Country and League tables to retrieve the league identifier ('XCL_005') for the country where 'XCL_002' is 'Germany'.

```json
{
  "kind": "program",
  "formula": "SELECT t2.\"XCL_005\" FROM Country AS t1 INNER JOIN League AS t2 ON t1.\"XCL_001\" = t2.\"XCL_004\" WHERE t1.\"XCL_002\" = 'Germany'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1082"
  ]
}
```

### A query that retrieves a specific attribute ("XCL_174") from the Team table by filtering on the team name ("XCL_173") being 'Queens Park Rangers'. Thi

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_174\" FROM Team WHERE \"XCL_173\" = 'Queens Park Rangers'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1043"
  ]
}
```

### Executes a count aggregation on Player_Attributes.XCL_128 with specific range and equality filters on XCL_132 and XCL_136.

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_128\") FROM Player_Attributes WHERE \"XCL_132\" BETWEEN 60 AND 65 AND \"XCL_136\" = 'low'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1023"
  ]
}
```

### Executes an inner join of Match (T1) to TEAM (T2) on Match.XCL_014 = TEAM.XCL_171 and to Country (T3) on Match.XCL_007 = Country.XCL_001. Applies filt

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(T1.\"XCL_016\") AS REAL) / COUNT(T1.\"XCL_006\") FROM \"Match\" AS T1 INNER JOIN TEAM AS T2 ON T1.\"XCL_014\" = T2.\"XCL_171\" INNER JOIN Country AS T3 ON T1.\"XCL_007\" = T3.\"XCL_001\" WHERE T2.\"XCL_173\" = 'Parma' AND T3.\"XCL_002\" = 'Italy'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1101"
  ]
}
```

### Full SQL query for pre-1986 player attribute average

```json
{
  "kind": "program",
  "formula": "SELECT SUM(t2.\"XCL_132\") / COUNT(t1.\"XCL_121\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE SUBSTRING(t1.\"XCL_125\", 1, 4) < '1986'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1093"
  ]
}
```

### Full SQL program that joins the 'Player' table (alias t1) with the 'match' table (alias t2) on 'XCL_122' = 'XCL_072'. It filters for players where the

```json
{
  "kind": "program",
  "formula": "SELECT SUM(t2.\"XCL_015\") FROM Player AS t1 INNER JOIN match AS t2 ON t1.\"XCL_122\" = t2.\"XCL_072\" WHERE DATETIME(CURRENT_TIMESTAMP, 'localtime') - DATETIME(T1.\"XCL_125\") < 31",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1121"
  ]
}
```

### Belgium 2008/2009 Match Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(t2.\"XCL_006\") FROM Country AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_001\" = t2.\"XCL_007\" WHERE t1.\"XCL_002\" = 'Belgium' AND t2.\"XCL_009\" = '2008/2009'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1089"
  ]
}
```

### Full SQL program that joins the 'Player' table (t1) with the 'match' table (t2) on 'XCL_122' = 'XCL_080', filters for the specific player 'Aaron Lenno

```json
{
  "kind": "program",
  "formula": "SELECT SUM(t2.\"XCL_015\") FROM Player AS t1 INNER JOIN match AS t2 ON t1.\"XCL_122\" = t2.\"XCL_080\" WHERE t1.\"XCL_123\" = 'Aaron Lennon'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1119"
  ]
}
```

### Full SQL program that joins Player and Player_Attributes tables on player ID, filters players by birth year (1987-1992) using the first 4 characters o

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(CASE WHEN t2.\"XCL_134\" = 'left' THEN t1.\"XCL_121\" ELSE NULL END) AS REAL) * 100 / COUNT(t1.\"XCL_121\") AS percent FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE SUBSTRING(t1.\"XCL_125\", 1, 4) BETWEEN '1987' AND '1992'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1037"
  ]
}
```

### High-Attribute Player Age Query

```json
{
  "kind": "program",
  "formula": "SELECT DISTINCT DATETIME() - T2.\"XCL_125\" AS age FROM Player_Attributes AS t1 INNER JOIN Player AS t2 ON t1.\"XCL_130\" = t2.\"XCL_122\" WHERE STRFTIME('%Y', t1.\"XCL_131\") >= '2013' AND STRFTIME('%Y', t1.\"XCL_131\") <= '2015' AND t1.\"XCL_148\" >= 97",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1031"
  ]
}
```

### Full program that joins Team and Team_Attributes to identify teams where the attribute XCL_182 is 'Normal' and the value of XCL_186 is strictly less t

```json
{
  "kind": "program",
  "formula": "SELECT t3.\"XCL_173\" FROM Team AS t3 INNER JOIN Team_Attributes AS t4 ON t3.\"XCL_171\" = t4.\"XCL_177\" WHERE t4.\"XCL_182\" = 'Normal' AND t4.\"XCL_186\" < (SELECT CAST(SUM(t2.\"XCL_186\") AS REAL) / COUNT(t1.\"XCL_170\") FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_182\" = 'Normal' AND SUBSTRING(t2.\"XCL_178\", 1, 4) = '2014') ORDER BY t4.\"XCL_186\" DESC",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1041"
  ]
}
```

### League Identifier

```json
{
  "kind": "binding",
  "formula": "\"League\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_004\" FROM League WHERE \"XCL_005\" = 'Poland Ekstraklasa'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_004\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "League"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_004\" AS \"value\" FROM League AS \"r0\" WHERE \"r0\".\"XCL_005\" = 'Poland Ekstraklasa'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1138"
  ]
}
```

### Player Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_139\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_139\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Francois Affolter' AND SUBSTRING(t2.\"XCL_131\", 1, 10) = '2014-09-18'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_139\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_139\" AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\" WHERE \"r0\".\"XCL_123\" = 'Francois Affolter' AND SUBSTRING(\"r1\".\"XCL_131\", 1, 10) = '2014-09-18'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1047"
  ]
}
```

### "Match"."XCL_009" = '2015/2016' AND "League"."XCL_005" = 'Scotland Premier League'

```json
{
  "kind": "predicate",
  "formula": "\"Match\".\"XCL_009\" = '2015/2016' AND \"League\".\"XCL_005\" = 'Scotland Premier League'",
  "grain": [],
  "population_scope": "SELECT COUNT(t2.\"XCL_006\") FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t2.\"XCL_009\" = '2015/2016' AND t1.\"XCL_005\" = 'Scotland Premier League'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1049"
  ]
}
```

### "Country"."XCL_002" = 'Italy'

```json
{
  "kind": "predicate",
  "formula": "\"Country\".\"XCL_002\" = 'Italy'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(T1.\"XCL_126\") AS REAL) / COUNT(T1.\"XCL_121\") FROM Player AS T1 INNER JOIN Match AS T2 ON T1.\"XCL_121\" = T2.\"XCL_006\" INNER JOIN Country AS T3 ON T2.\"XCL_007\" = T3.\"XCL_001\" WHERE T3.\"XCL_002\" = 'Italy'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1131"
  ]
}
```

### Player Identifier

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_121\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_121\", t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_134\" = 'left'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1064"
  ]
}
```

### Average XCL_186 for Normal teams in 2014

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"Team_Attributes\".\"XCL_186\") AS REAL) / COUNT(\"Team\".\"XCL_170\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(t2.\"XCL_186\") AS REAL) / COUNT(t1.\"XCL_170\") FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_182\" = 'Normal' AND SUBSTRING(t2.\"XCL_178\", 1, 4) = '2014'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(\"r1\".\"XCL_186\") AS REAL) / COUNT(\"r0\".\"XCL_170\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Team"
      },
      {
        "role": "r1",
        "physical_table": "Team_Attributes"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(\"r1\".\"XCL_186\") AS REAL) / COUNT(\"r0\".\"XCL_170\") AS \"value\" FROM Team AS \"r0\" INNER JOIN Team_Attributes AS \"r1\" ON \"r0\".\"XCL_171\" = \"r1\".\"XCL_177\" WHERE \"r1\".\"XCL_182\" = 'Normal' AND SUBSTRING(\"r1\".\"XCL_178\", 1, 4) = '2014'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1041"
  ]
}
```

### "Player"."XCL_123" = 'Gabriel Tamas' AND STRFTIME('%Y', "Player_Attributes"."XCL_131") = '2011'

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_123\" = 'Gabriel Tamas' AND STRFTIME('%Y', \"Player_Attributes\".\"XCL_131\") = '2011'",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_132\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Gabriel Tamas' AND STRFTIME('%Y', t2.\"XCL_131\") = '2011'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1048"
  ]
}
```

### "League"."XCL_005" = 'Belgium Jupiler League' AND SUBSTRING("Match"."XCL_011", 1, 7) = '2009-04'

```json
{
  "kind": "predicate",
  "formula": "\"League\".\"XCL_005\" = 'Belgium Jupiler League' AND SUBSTRING(\"Match\".\"XCL_011\", 1, 7) = '2009-04'",
  "grain": [],
  "population_scope": "SELECT COUNT(t2.\"XCL_006\") FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t1.\"XCL_005\" = 'Belgium Jupiler League' AND SUBSTRING(t2.\"XCL_011\", 1, 7) = '2009-04'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1091"
  ]
}
```

### Aggregates the total number of rows in the Player table where the value in column XCL_125 is greater than '1990' and the value in column XCL_123 start

```json
{
  "kind": "metric",
  "formula": "COUNT(\"Player\".\"XCL_121\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_121\") FROM Player WHERE \"XCL_125\" > '1990' AND \"XCL_123\" LIKE 'Aaron%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_121\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_121\") AS \"value\" FROM Player AS \"r0\" WHERE \"r0\".\"XCL_125\" > '1990' AND \"r0\".\"XCL_123\" LIKE 'Aaron%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1133"
  ]
}
```

### Distinct values of the Team identifier column (XCL_173) for teams that have at least one attribute record marked as 'Fast'.

```json
{
  "kind": "binding",
  "formula": "\"Team\".\"XCL_173\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_173\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_180\" = 'Fast'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1065"
  ]
}
```

### Average XCL_132 per XCL_128

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"Player_Attributes\".\"XCL_132\") AS REAL) / COUNT(\"Player_Attributes\".\"XCL_128\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(t2.\"XCL_132\") AS REAL) / COUNT(t2.\"XCL_128\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Aaron Doran'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(\"r1\".\"XCL_132\") AS REAL) / COUNT(\"r1\".\"XCL_128\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(\"r1\".\"XCL_132\") AS REAL) / COUNT(\"r1\".\"XCL_128\") AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\" WHERE \"r0\".\"XCL_123\" = 'Aaron Doran'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1072"
  ]
}
```

### Aggregates the sum of the XCL_137 column from the Player_Attributes table for all records associated with the player identified by the name 'Aaron Len

```json
{
  "kind": "metric",
  "formula": "SUM(\"Player_Attributes\".\"XCL_137\")",
  "grain": [],
  "population_scope": "SELECT SUM(t2.\"XCL_137\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Aaron Lennox'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r1\".\"XCL_137\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT SUM(\"r1\".\"XCL_137\") AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\" WHERE \"r0\".\"XCL_123\" = 'Aaron Lennox'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1097"
  ]
}
```

### "Player"."XCL_123" IN ('Alexis', 'Ariel Borysiuk', 'Arouna Kone')

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_123\" IN ('Alexis', 'Ariel Borysiuk', 'Arouna Kone')",
  "grain": [],
  "population_scope": "SELECT t1.\"XCL_123\", t2.\"XCL_137\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" IN ('Alexis', 'Ariel Borysiuk', 'Arouna Kone') ORDER BY t2.\"XCL_137\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1085"
  ]
}
```

### Max Attribute Value

```json
{
  "kind": "metric",
  "formula": "MAX(\"Player_Attributes\".\"XCL_132\")",
  "grain": [],
  "population_scope": "SELECT MAX(\"XCL_132\") FROM Player_Attributes",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MAX(\"r0\".\"XCL_132\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT MAX(\"r0\".\"XCL_132\") AS \"value\" FROM Player_Attributes AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1122",
    "bird_dev:1147"
  ]
}
```

### "Team"."XCL_173" = 'FC Lorient' AND "Team_Attributes"."XCL_178" LIKE '2010-02-22%'

```json
{
  "kind": "predicate",
  "formula": "\"Team\".\"XCL_173\" = 'FC Lorient' AND \"Team_Attributes\".\"XCL_178\" LIKE '2010-02-22%'",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_184\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'FC Lorient' AND t2.\"XCL_178\" LIKE '2010-02-22%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1110"
  ]
}
```

### "Player_Attributes"."XCL_135" = 'high'

```json
{
  "kind": "predicate",
  "formula": "\"Player_Attributes\".\"XCL_135\" = 'high'",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_135\" = 'high'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1124"
  ]
}
```

### "Team_Attributes"."XCL_187" = 'Safe'

```json
{
  "kind": "predicate",
  "formula": "\"Team_Attributes\".\"XCL_187\" = 'Safe'",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_174\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_187\" = 'Safe'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1130"
  ]
}
```

### Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_131\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_137\", t2.\"XCL_131\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_124\" = t2.\"XCL_129\" WHERE t1.\"XCL_123\" = 'Kevin Constant' ORDER BY t2.\"XCL_137\" DESC",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_131\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_131\" AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_124\" = \"r1\".\"XCL_129\" WHERE \"r0\".\"XCL_123\" = 'Kevin Constant'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1107"
  ]
}
```

### The identifier (XCL_123) of the player(s) with the highest XCL_126 value, filtered by rank = 1.

```json
{
  "kind": "binding",
  "formula": "\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_123\" FROM (SELECT \"XCL_123\", \"XCL_126\", DENSE_RANK() OVER (ORDER BY \"XCL_126\" DESC) AS rank FROM Player) WHERE \"rank\" = 1",
  "upstream_scopes": [
    "SELECT \"XCL_123\", \"XCL_126\", DENSE_RANK() OVER (ORDER BY \"XCL_126\" DESC) AS rank FROM Player"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1116"
  ]
}
```

### SUBSTRING("Player_Attributes"."XCL_131", 1, 10) = '2010-08-30' AND "Player"."XCL_123" = 'Francesco Parravicini'

```json
{
  "kind": "predicate",
  "formula": "SUBSTRING(\"Player_Attributes\".\"XCL_131\", 1, 10) = '2010-08-30' AND \"Player\".\"XCL_123\" = 'Francesco Parravicini'",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_133\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE SUBSTRING(t2.\"XCL_131\", 1, 10) = '2010-08-30' AND t1.\"XCL_123\" = 'Francesco Parravicini'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1104"
  ]
}
```

### Average Player XCL_126 for Italian Matches

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"Player\".\"XCL_126\") AS REAL) / COUNT(\"Player\".\"XCL_121\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(T1.\"XCL_126\") AS REAL) / COUNT(T1.\"XCL_121\") FROM Player AS T1 INNER JOIN Match AS T2 ON T1.\"XCL_121\" = T2.\"XCL_006\" INNER JOIN Country AS T3 ON T2.\"XCL_007\" = T3.\"XCL_001\" WHERE T3.\"XCL_002\" = 'Italy'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(\"r0\".\"XCL_126\") AS REAL) / COUNT(\"r0\".\"XCL_121\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Match"
      },
      {
        "role": "r2",
        "physical_table": "Country"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(\"r0\".\"XCL_126\") AS REAL) / COUNT(\"r0\".\"XCL_121\") AS \"value\" FROM Player AS \"r0\" INNER JOIN Match AS \"r1\" ON \"r0\".\"XCL_121\" = \"r1\".\"XCL_006\" INNER JOIN Country AS \"r2\" ON \"r1\".\"XCL_007\" = \"r2\".\"XCL_001\" WHERE \"r2\".\"XCL_002\" = 'Italy'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1131"
  ]
}
```

### "Player"."XCL_123" = 'Aaron Lennon'

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_123\" = 'Aaron Lennon'",
  "grain": [],
  "population_scope": "SELECT SUM(t2.\"XCL_015\") FROM Player AS t1 INNER JOIN match AS t2 ON t1.\"XCL_122\" = t2.\"XCL_080\" WHERE t1.\"XCL_123\" = 'Aaron Lennon'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1119"
  ]
}
```

### Player Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_132\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_132\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE SUBSTRING(t2.\"XCL_131\", 1, 10) = '2016-02-04' AND t1.\"XCL_123\" = 'Aaron Mooy'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_132\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_132\" AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\" WHERE SUBSTRING(\"r1\".\"XCL_131\", 1, 10) = '2016-02-04' AND \"r0\".\"XCL_123\" = 'Aaron Mooy'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1103"
  ]
}
```

### Player Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_135\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_135\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_131\" LIKE '2015-05-01%' AND t1.\"XCL_123\" = 'Francesco Migliore'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_135\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_135\" AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\" WHERE \"r1\".\"XCL_131\" LIKE '2015-05-01%' AND \"r0\".\"XCL_123\" = 'Francesco Migliore'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1105"
  ]
}
```

### Team XCL_173

```json
{
  "kind": "binding",
  "formula": "\"Team\".\"XCL_173\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t4.\"XCL_173\" FROM Team_Attributes AS t3 INNER JOIN Team AS t4 ON t3.\"XCL_177\" = t4.\"XCL_171\" WHERE SUBSTRING(t3.\"XCL_178\", 1, 4) = '2012' AND t3.\"XCL_183\" > (SELECT CAST(SUM(t2.\"XCL_183\") AS REAL) / COUNT(t1.\"XCL_170\") FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE STRFTIME('%Y', t2.\"XCL_178\") = '2012')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1036"
  ]
}
```

### NOT "Player_Attributes"."XCL_133" IS NULL

```json
{
  "kind": "predicate",
  "formula": "NOT \"Player_Attributes\".\"XCL_133\" IS NULL",
  "grain": [],
  "population_scope": "SELECT \"XCL_134\" FROM Player_Attributes WHERE NOT \"XCL_133\" IS NULL ORDER BY \"XCL_133\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1022"
  ]
}
```

### Aggregates the total number of non-null values in column XCL_128 from the Player_Attributes table, filtered to rows where XCL_132 is between 60 and 65

```json
{
  "kind": "metric",
  "formula": "COUNT(\"Player_Attributes\".\"XCL_128\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_128\") FROM Player_Attributes WHERE \"XCL_132\" BETWEEN 60 AND 65 AND \"XCL_136\" = 'low'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_128\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_128\") AS \"value\" FROM Player_Attributes AS \"r0\" WHERE \"r0\".\"XCL_132\" BETWEEN 60 AND 65 AND \"r0\".\"XCL_136\" = 'low'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1023"
  ]
}
```

### Identifies the highest number of matches played by any single league in the 2008/2009 season. This value serves as the threshold for the HAVING clause

```json
{
  "kind": "metric",
  "formula": "MAX(\"match_count\")",
  "grain": [],
  "population_scope": "SELECT MAX(\"match_count\") FROM (SELECT COUNT(t2.\"XCL_006\") AS match_count FROM Match AS t2 WHERE t2.\"XCL_009\" = '2008/2009' GROUP BY t2.\"XCL_008\")",
  "upstream_scopes": [
    "SELECT COUNT(t2.\"XCL_006\") AS match_count FROM Match AS t2 WHERE t2.\"XCL_009\" = '2008/2009' GROUP BY t2.\"XCL_008\""
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1092"
  ]
}
```

### Max Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_131\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_131\" FROM (SELECT t2.\"XCL_137\", t2.\"XCL_131\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_124\" = t2.\"XCL_129\" WHERE t1.\"XCL_123\" = 'Kevin Constant' ORDER BY t2.\"XCL_137\" DESC) ORDER BY \"XCL_131\" DESC LIMIT 1",
  "upstream_scopes": [
    "SELECT t2.\"XCL_137\", t2.\"XCL_131\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_124\" = t2.\"XCL_129\" WHERE t1.\"XCL_123\" = 'Kevin Constant' ORDER BY t2.\"XCL_137\" DESC"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1107"
  ]
}
```

### SUBSTRING("Player"."XCL_125", 1, 4) BETWEEN '1987' AND '1992'

```json
{
  "kind": "predicate",
  "formula": "SUBSTRING(\"Player\".\"XCL_125\", 1, 4) BETWEEN '1987' AND '1992'",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN t2.\"XCL_134\" = 'left' THEN t1.\"XCL_121\" ELSE NULL END) AS REAL) * 100 / COUNT(t1.\"XCL_121\") AS percent FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE SUBSTRING(t1.\"XCL_125\", 1, 4) BETWEEN '1987' AND '1992'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1037"
  ]
}
```

### (CAST(SUM("Match"."XCL_015") AS REAL) / COUNT(DISTINCT "Match"."XCL_006")) - (CAST(SUM("Match"."XCL_016") AS REAL) / COUNT(DISTINCT "Match"."XCL_006")

```json
{
  "kind": "predicate",
  "formula": "(CAST(SUM(\"Match\".\"XCL_015\") AS REAL) / COUNT(DISTINCT \"Match\".\"XCL_006\")) - (CAST(SUM(\"Match\".\"XCL_016\") AS REAL) / COUNT(DISTINCT \"Match\".\"XCL_006\")) > 0",
  "grain": [
    "\"League\".\"XCL_005\""
  ],
  "population_scope": "SELECT t1.\"XCL_005\" FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t2.\"XCL_009\" = '2009/2010' GROUP BY t1.\"XCL_005\" HAVING (CAST(SUM(t2.\"XCL_015\") AS REAL) / COUNT(DISTINCT t2.\"XCL_006\")) - (CAST(SUM(t2.\"XCL_016\") AS REAL) / COUNT(DISTINCT t2.\"XCL_006\")) > 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1042"
  ]
}
```

### Player Identifier

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_132\" = (SELECT MAX(\"XCL_132\") FROM Player_Attributes)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1122",
    "bird_dev:1147"
  ]
}
```

### "TEAM"."XCL_173" = 'Parma' AND "Country"."XCL_002" = 'Italy'

```json
{
  "kind": "predicate",
  "formula": "\"TEAM\".\"XCL_173\" = 'Parma' AND \"Country\".\"XCL_002\" = 'Italy'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(T1.\"XCL_016\") AS REAL) / COUNT(T1.\"XCL_006\") FROM \"Match\" AS T1 INNER JOIN TEAM AS T2 ON T1.\"XCL_014\" = T2.\"XCL_171\" INNER JOIN Country AS T3 ON T1.\"XCL_007\" = T3.\"XCL_001\" WHERE T2.\"XCL_173\" = 'Parma' AND T3.\"XCL_002\" = 'Italy'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1101"
  ]
}
```

### Max Player XCL_126

```json
{
  "kind": "metric",
  "formula": "MAX(\"Player\".\"XCL_126\")",
  "grain": [],
  "population_scope": "SELECT MAX(\"XCL_126\") FROM Player",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MAX(\"r0\".\"XCL_126\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      }
    ],
    "scope_sql": "SELECT MAX(\"r0\".\"XCL_126\") AS \"value\" FROM Player AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1058"
  ]
}
```

### "Player_Attributes"."XCL_132" > 80 AND SUBSTRING("Player_Attributes"."XCL_131", 1, 4) BETWEEN '2008' AND '2010'

```json
{
  "kind": "predicate",
  "formula": "\"Player_Attributes\".\"XCL_132\" > 80 AND SUBSTRING(\"Player_Attributes\".\"XCL_131\", 1, 4) BETWEEN '2008' AND '2010'",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_132\" > 80 AND SUBSTRING(t2.\"XCL_131\", 1, 4) BETWEEN '2008' AND '2010'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1062"
  ]
}
```

### "Player_Attributes"."XCL_134" = 'left'

```json
{
  "kind": "predicate",
  "formula": "\"Player_Attributes\".\"XCL_134\" = 'left'",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_121\", t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_134\" = 'left'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1064"
  ]
}
```

### Distinct values of the Player identifier column (XCL_123) for players who have at least one attribute record where the attribute value (XCL_135) is 'h

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_135\" = 'high'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1124"
  ]
}
```

### Player Attribute XCL_128

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_128\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_128\", \"XCL_138\", \"XCL_143\" FROM Player_Attributes WHERE \"XCL_130\" = (SELECT \"XCL_122\" FROM Player ORDER BY \"XCL_127\" DESC LIMIT 1) LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1144"
  ]
}
```

### "Player_Attributes"."XCL_160" > 89

```json
{
  "kind": "predicate",
  "formula": "\"Player_Attributes\".\"XCL_160\" > 89",
  "grain": [],
  "population_scope": "SELECT DISTINCT t4.\"XCL_002\" FROM Player_Attributes AS t1 INNER JOIN Player AS t2 ON t1.\"XCL_130\" = t2.\"XCL_122\" INNER JOIN Match AS t3 ON t2.\"XCL_122\" = t3.\"XCL_068\" INNER JOIN Country AS t4 ON t3.\"XCL_007\" = t4.\"XCL_001\" WHERE t1.\"XCL_160\" > 89",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1127"
  ]
}
```

### "Player_Attributes"."XCL_132" BETWEEN 60 AND 65 AND "Player_Attributes"."XCL_136" = 'low'

```json
{
  "kind": "predicate",
  "formula": "\"Player_Attributes\".\"XCL_132\" BETWEEN 60 AND 65 AND \"Player_Attributes\".\"XCL_136\" = 'low'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_128\") FROM Player_Attributes WHERE \"XCL_132\" BETWEEN 60 AND 65 AND \"XCL_136\" = 'low'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1023"
  ]
}
```

### "League"."XCL_005" = 'Poland Ekstraklasa'

```json
{
  "kind": "predicate",
  "formula": "\"League\".\"XCL_005\" = 'Poland Ekstraklasa'",
  "grain": [],
  "population_scope": "SELECT \"XCL_004\" FROM League WHERE \"XCL_005\" = 'Poland Ekstraklasa'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1138"
  ]
}
```

### Match League Identifier

```json
{
  "kind": "binding",
  "formula": "\"Match\".\"XCL_008\"",
  "grain": [
    "\"Match\".\"XCL_008\""
  ],
  "population_scope": "SELECT \"XCL_008\", COUNT(\"XCL_006\") AS cnt FROM Match GROUP BY \"XCL_008\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_008\"",
    "grain": [
      "\"r0\".\"XCL_008\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Match"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_008\" AS \"grain_0\", \"r0\".\"XCL_008\" AS \"value\" FROM Match AS \"r0\" GROUP BY \"r0\".\"XCL_008\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1032"
  ]
}
```

### League Identifier

```json
{
  "kind": "binding",
  "formula": "\"League\".\"XCL_005\"",
  "grain": [
    "\"League\".\"XCL_005\""
  ],
  "population_scope": "SELECT t1.\"XCL_005\" FROM League AS t1 JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t2.\"XCL_009\" = '2008/2009' GROUP BY t1.\"XCL_005\" HAVING COUNT(t2.\"XCL_006\") = (SELECT MAX(\"match_count\") FROM (SELECT COUNT(t2.\"XCL_006\") AS match_count FROM Match AS t2 WHERE t2.\"XCL_009\" = '2008/2009' GROUP BY t2.\"XCL_008\"))",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1092"
  ]
}
```

### SUBSTRING("Player_Attributes"."XCL_131", 1, 4) = '2010'

```json
{
  "kind": "predicate",
  "formula": "SUBSTRING(\"Player_Attributes\".\"XCL_131\", 1, 4) = '2010'",
  "grain": [],
  "population_scope": "SELECT \"XCL_130\" FROM Player_Attributes WHERE SUBSTRING(\"XCL_131\", 1, 4) = '2010' ORDER BY \"XCL_132\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1034"
  ]
}
```

### League Identifier

```json
{
  "kind": "binding",
  "formula": "\"League\".\"XCL_005\"",
  "grain": [
    "\"League\".\"XCL_005\""
  ],
  "population_scope": "SELECT t1.\"XCL_005\", SUM(t2.\"XCL_015\") + SUM(t2.\"XCL_016\") FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" GROUP BY t1.\"XCL_005\" ORDER BY SUM(t2.\"XCL_015\") + SUM(t2.\"XCL_016\") ASC LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1038"
  ]
}
```

### Maximum Match Count

```json
{
  "kind": "metric",
  "formula": "MAX(\"cnt\")",
  "grain": [],
  "population_scope": "SELECT \"XCL_008\", MAX(\"cnt\") AS max_count FROM (SELECT \"XCL_008\", COUNT(\"XCL_006\") AS cnt FROM Match GROUP BY \"XCL_008\") AS subquery",
  "upstream_scopes": [
    "SELECT \"XCL_008\", COUNT(\"XCL_006\") AS cnt FROM Match GROUP BY \"XCL_008\""
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1032"
  ]
}
```

### "Country"."XCL_002" = 'Belgium' AND "Match"."XCL_009" = '2008/2009'

```json
{
  "kind": "predicate",
  "formula": "\"Country\".\"XCL_002\" = 'Belgium' AND \"Match\".\"XCL_009\" = '2008/2009'",
  "grain": [],
  "population_scope": "SELECT COUNT(t2.\"XCL_006\") FROM Country AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_001\" = t2.\"XCL_007\" WHERE t1.\"XCL_002\" = 'Belgium' AND t2.\"XCL_009\" = '2008/2009'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1089"
  ]
}
```

### "Team"."XCL_173" = 'Hull City' AND SUBSTRING("Team_Attributes"."XCL_178", 1, 10) = '2010-02-22'

```json
{
  "kind": "predicate",
  "formula": "\"Team\".\"XCL_173\" = 'Hull City' AND SUBSTRING(\"Team_Attributes\".\"XCL_178\", 1, 10) = '2010-02-22'",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_189\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'Hull City' AND SUBSTRING(t2.\"XCL_178\", 1, 10) = '2010-02-22'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1112"
  ]
}
```

### Net XCL_153 for XCL_128 6 vs 23

```json
{
  "kind": "metric",
  "formula": "SUM(CASE WHEN \"Player_Attributes\".\"XCL_128\" = 6 THEN \"Player_Attributes\".\"XCL_153\" ELSE 0 END) - SUM(CASE WHEN \"Player_Attributes\".\"XCL_128\" = 23 THEN \"Player_Attributes\".\"XCL_153\" ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT SUM(CASE WHEN t1.\"XCL_128\" = 6 THEN t1.\"XCL_153\" ELSE 0 END) - SUM(CASE WHEN t1.\"XCL_128\" = 23 THEN t1.\"XCL_153\" ELSE 0 END) FROM Player_Attributes AS t1",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(CASE WHEN \"r0\".\"XCL_128\" = 6 THEN \"r0\".\"XCL_153\" ELSE 0 END) - SUM(CASE WHEN \"r0\".\"XCL_128\" = 23 THEN \"r0\".\"XCL_153\" ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT SUM(CASE WHEN \"r0\".\"XCL_128\" = 6 THEN \"r0\".\"XCL_153\" ELSE 0 END) - SUM(CASE WHEN \"r0\".\"XCL_128\" = 23 THEN \"r0\".\"XCL_153\" ELSE 0 END) AS \"value\" FROM Player_Attributes AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1134"
  ]
}
```

### Match Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"Match\".\"XCL_006\")",
  "grain": [],
  "population_scope": "SELECT COUNT(t2.\"XCL_006\") FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t1.\"XCL_005\" = 'Germany 1. Bundesliga' AND SUBSTRING(t2.\"XCL_011\", 1, 7) BETWEEN '2008-08' AND '2008-10'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_006\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "League"
      },
      {
        "role": "r1",
        "physical_table": "Match"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_006\") AS \"value\" FROM League AS \"r0\" INNER JOIN Match AS \"r1\" ON \"r0\".\"XCL_003\" = \"r1\".\"XCL_008\" WHERE \"r0\".\"XCL_005\" = 'Germany 1. Bundesliga' AND SUBSTRING(\"r1\".\"XCL_011\", 1, 7) BETWEEN '2008-08' AND '2008-10'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1073"
  ]
}
```

### Team Identifier

```json
{
  "kind": "binding",
  "formula": "\"Team\".\"XCL_174\"",
  "grain": [],
  "population_scope": "SELECT t1.\"XCL_174\" FROM Team AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_171\" = t2.\"XCL_013\" WHERE t2.\"XCL_015\" = 10",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_174\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Team"
      },
      {
        "role": "r1",
        "physical_table": "Match"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_174\" AS \"value\" FROM Team AS \"r0\" INNER JOIN Match AS \"r1\" ON \"r0\".\"XCL_171\" = \"r1\".\"XCL_013\" WHERE \"r1\".\"XCL_015\" = 10",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1074"
  ]
}
```

### Returns the value of column "XCL_173" from the Team table for rows where "XCL_174" equals 'GEN'. The grain is individual team records filtered by the 

```json
{
  "kind": "binding",
  "formula": "\"Team\".\"XCL_173\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_173\" FROM Team WHERE \"XCL_174\" = 'GEN'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_173\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Team"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_173\" AS \"value\" FROM Team AS \"r0\" WHERE \"r0\".\"XCL_174\" = 'GEN'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1077"
  ]
}
```

### "Player"."XCL_123" = 'Ahmed Samir Farag'

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_123\" = 'Ahmed Samir Farag'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(t2.\"XCL_156\") AS REAL) / COUNT(t2.\"XCL_131\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Ahmed Samir Farag'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1039"
  ]
}
```

### Player Name

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_121\", t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_134\" = 'left'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1064"
  ]
}
```

### Average XCL_132 per XCL_128

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"Player_Attributes\".\"XCL_132\") AS REAL) / COUNT(\"Player_Attributes\".\"XCL_128\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(t2.\"XCL_132\") AS REAL) / COUNT(t2.\"XCL_128\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_124\" = t2.\"XCL_129\" WHERE t1.\"XCL_123\" = 'Marko Arnautovic' AND SUBSTRING(t2.\"XCL_131\", 1, 10) BETWEEN '2007-02-22' AND '2016-04-21'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(\"r1\".\"XCL_132\") AS REAL) / COUNT(\"r1\".\"XCL_128\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(\"r1\".\"XCL_132\") AS REAL) / COUNT(\"r1\".\"XCL_128\") AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_124\" = \"r1\".\"XCL_129\" WHERE \"r0\".\"XCL_123\" = 'Marko Arnautovic' AND SUBSTRING(\"r1\".\"XCL_131\", 1, 10) BETWEEN '2007-02-22' AND '2016-04-21'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1114"
  ]
}
```

### "League"."XCL_005" = 'Netherlands Eredivisie'

```json
{
  "kind": "predicate",
  "formula": "\"League\".\"XCL_005\" = 'Netherlands Eredivisie'",
  "grain": [],
  "population_scope": "SELECT MAX(t2.\"XCL_015\") FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t1.\"XCL_005\" = 'Netherlands Eredivisie'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1143"
  ]
}
```

### "Player"."XCL_126" > 170 AND STRFTIME('%Y', "Player_Attributes"."XCL_131") >= '2010' AND STRFTIME('%Y', "Player_Attributes"."XCL_131") <= '2015'

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_126\" > 170 AND STRFTIME('%Y', \"Player_Attributes\".\"XCL_131\") >= '2010' AND STRFTIME('%Y', \"Player_Attributes\".\"XCL_131\") <= '2015'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(t2.\"XCL_132\") AS REAL) / COUNT(t2.\"XCL_128\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_126\" > 170 AND STRFTIME('%Y', t2.\"XCL_131\") >= '2010' AND STRFTIME('%Y', t2.\"XCL_131\") <= '2015'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1068"
  ]
}
```

### Average XCL_132 per Player for pre-1986 birth year

```json
{
  "kind": "metric",
  "formula": "SUM(\"Player_Attributes\".\"XCL_132\") / COUNT(\"Player\".\"XCL_121\")",
  "grain": [],
  "population_scope": "SELECT SUM(t2.\"XCL_132\") / COUNT(t1.\"XCL_121\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE SUBSTRING(t1.\"XCL_125\", 1, 4) < '1986'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r1\".\"XCL_132\") / COUNT(\"r0\".\"XCL_121\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT SUM(\"r1\".\"XCL_132\") / COUNT(\"r0\".\"XCL_121\") AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\" WHERE SUBSTRING(\"r0\".\"XCL_125\", 1, 4) < '1986'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1093"
  ]
}
```

### Player Identifier

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" ORDER BY t2.\"XCL_133\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1123"
  ]
}
```

### "Player_Attributes"."XCL_134" = 'left' AND "Player_Attributes"."XCL_135" = 'low'

```json
{
  "kind": "predicate",
  "formula": "\"Player_Attributes\".\"XCL_134\" = 'left' AND \"Player_Attributes\".\"XCL_135\" = 'low'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_130\") FROM Player_Attributes WHERE \"XCL_134\" = 'left' AND \"XCL_135\" = 'low'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1080"
  ]
}
```

### "Player"."XCL_123" = 'Francois Affolter' AND SUBSTRING("Player_Attributes"."XCL_131", 1, 10) = '2014-09-18'

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_123\" = 'Francois Affolter' AND SUBSTRING(\"Player_Attributes\".\"XCL_131\", 1, 10) = '2014-09-18'",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_139\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Francois Affolter' AND SUBSTRING(t2.\"XCL_131\", 1, 10) = '2014-09-18'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1047"
  ]
}
```

### "Player"."XCL_123" = 'Franco Zennaro'

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_123\" = 'Franco Zennaro'",
  "grain": [],
  "population_scope": "SELECT DISTINCT t2.\"XCL_135\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Franco Zennaro'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1045"
  ]
}
```

### A specific attribute value from the Player_Attributes table. Used for descending ordering to identify the maximum value among the filtered players and

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_137\"",
  "grain": [],
  "population_scope": "SELECT t1.\"XCL_123\", t2.\"XCL_137\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" IN ('Alexis', 'Ariel Borysiuk', 'Arouna Kone') ORDER BY t2.\"XCL_137\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1085"
  ]
}
```

### Average XCL_132 per XCL_128

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"Player_Attributes\".\"XCL_132\") AS REAL) / COUNT(\"Player_Attributes\".\"XCL_128\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(t2.\"XCL_132\") AS REAL) / COUNT(t2.\"XCL_128\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_126\" > 170 AND STRFTIME('%Y', t2.\"XCL_131\") >= '2010' AND STRFTIME('%Y', t2.\"XCL_131\") <= '2015'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(\"r1\".\"XCL_132\") AS REAL) / COUNT(\"r1\".\"XCL_128\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(\"r1\".\"XCL_132\") AS REAL) / COUNT(\"r1\".\"XCL_128\") AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\" WHERE \"r0\".\"XCL_126\" > 170 AND STRFTIME('%Y', \"r1\".\"XCL_131\") >= '2010' AND STRFTIME('%Y', \"r1\".\"XCL_131\") <= '2015'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1068"
  ]
}
```

### STRFTIME('%Y', "Player"."XCL_125") > '1990'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"Player\".\"XCL_125\") > '1990'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_121\") FROM Player WHERE STRFTIME('%Y', \"XCL_125\") > '1990'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1060"
  ]
}
```

### Distinct values of the attribute column XCL_185 from the Team_attributes table, filtered to those associated with the team 'ADO Den Haag' via the join

```json
{
  "kind": "binding",
  "formula": "\"Team_attributes\".\"XCL_185\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t2.\"XCL_185\" FROM Team AS t1 INNER JOIN Team_attributes AS t2 ON t1.\"XCL_172\" = t2.\"XCL_176\" WHERE t1.\"XCL_173\" = 'ADO Den Haag'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1046"
  ]
}
```

### "Player"."XCL_123" = 'Marko Arnautovic' AND SUBSTRING("Player_Attributes"."XCL_131", 1, 10) BETWEEN '2007-02-22' AND '2016-04-21'

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_123\" = 'Marko Arnautovic' AND SUBSTRING(\"Player_Attributes\".\"XCL_131\", 1, 10) BETWEEN '2007-02-22' AND '2016-04-21'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(t2.\"XCL_132\") AS REAL) / COUNT(t2.\"XCL_128\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_124\" = t2.\"XCL_129\" WHERE t1.\"XCL_123\" = 'Marko Arnautovic' AND SUBSTRING(t2.\"XCL_131\", 1, 10) BETWEEN '2007-02-22' AND '2016-04-21'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1114"
  ]
}
```

### "Player_Attributes"."XCL_133" = '61'

```json
{
  "kind": "predicate",
  "formula": "\"Player_Attributes\".\"XCL_133\" = '61'",
  "grain": [],
  "population_scope": "SELECT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_133\" = '61' ORDER BY t2.\"XCL_151\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1075"
  ]
}
```

### Dense rank assigned to each player based on XCL_126 in descending order. Rank 1 indicates the highest value(s) for XCL_126.

```json
{
  "kind": "metric",
  "formula": "DENSE_RANK() OVER (ORDER BY \"Player\".\"XCL_126\" DESC)",
  "grain": [],
  "population_scope": "SELECT \"XCL_123\", \"XCL_126\", DENSE_RANK() OVER (ORDER BY \"XCL_126\" DESC) AS rank FROM Player",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "DENSE_RANK() OVER (ORDER BY \"r0\".\"XCL_126\" DESC)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      }
    ],
    "scope_sql": "SELECT DENSE_RANK() OVER (ORDER BY \"r0\".\"XCL_126\" DESC) AS \"value\" FROM Player AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1116"
  ]
}
```

### Team Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"Team_Attributes\".\"XCL_179\"",
  "grain": [],
  "population_scope": "SELECT t1.\"XCL_179\" FROM Team_Attributes AS t1 INNER JOIN Team AS t2 ON t1.\"XCL_177\" = t2.\"XCL_171\" ORDER BY t1.\"XCL_179\" ASC LIMIT 4",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1029"
  ]
}
```

### "Player"."XCL_123" = 'David Wilson'

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_123\" = 'David Wilson'",
  "grain": [],
  "population_scope": "SELECT DISTINCT t2.\"XCL_136\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'David Wilson'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1054"
  ]
}
```

### Distinct values of the Player identifier column (XCL_123) for players who have at least one attribute record with a value greater than 80 (XCL_132) re

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_132\" > 80 AND SUBSTRING(t2.\"XCL_131\", 1, 4) BETWEEN '2008' AND '2010'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1062"
  ]
}
```

### "Team_Attributes"."XCL_179" > 50 AND "Team_Attributes"."XCL_179" < 60

```json
{
  "kind": "predicate",
  "formula": "\"Team_Attributes\".\"XCL_179\" > 50 AND \"Team_Attributes\".\"XCL_179\" < 60",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_176\" FROM Team_Attributes WHERE \"XCL_179\" > 50 AND \"XCL_179\" < 60",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1035"
  ]
}
```

### Average XCL_016 per XCL_006

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"Match\".\"XCL_016\") AS REAL) / COUNT(\"Match\".\"XCL_006\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(T1.\"XCL_016\") AS REAL) / COUNT(T1.\"XCL_006\") FROM \"Match\" AS T1 INNER JOIN TEAM AS T2 ON T1.\"XCL_014\" = T2.\"XCL_171\" INNER JOIN Country AS T3 ON T1.\"XCL_007\" = T3.\"XCL_001\" WHERE T2.\"XCL_173\" = 'Parma' AND T3.\"XCL_002\" = 'Italy'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(\"r0\".\"XCL_016\") AS REAL) / COUNT(\"r0\".\"XCL_006\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Match"
      },
      {
        "role": "r1",
        "physical_table": "TEAM"
      },
      {
        "role": "r2",
        "physical_table": "Country"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(\"r0\".\"XCL_016\") AS REAL) / COUNT(\"r0\".\"XCL_006\") AS \"value\" FROM \"Match\" AS \"r0\" INNER JOIN TEAM AS \"r1\" ON \"r0\".\"XCL_014\" = \"r1\".\"XCL_171\" INNER JOIN Country AS \"r2\" ON \"r0\".\"XCL_007\" = \"r2\".\"XCL_001\" WHERE \"r1\".\"XCL_173\" = 'Parma' AND \"r2\".\"XCL_002\" = 'Italy'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1101"
  ]
}
```

### "Player"."XCL_126" > 180 AND "Player_Attributes"."XCL_141" > 70

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_126\" > 180 AND \"Player_Attributes\".\"XCL_141\" > 70",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT t1.\"XCL_121\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_126\" > 180 AND t2.\"XCL_141\" > 70",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1087"
  ]
}
```

### Counts the number of matches (XCL_006) for each league (XCL_008) within the 2008/2009 season. This metric is calculated in a subquery to determine the

```json
{
  "kind": "metric",
  "formula": "COUNT(\"Match\".\"XCL_006\")",
  "grain": [
    "\"Match\".\"XCL_008\""
  ],
  "population_scope": "SELECT COUNT(t2.\"XCL_006\") AS match_count FROM Match AS t2 WHERE t2.\"XCL_009\" = '2008/2009' GROUP BY t2.\"XCL_008\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_006\")",
    "grain": [
      "\"r0\".\"XCL_008\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Match"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_008\" AS \"grain_0\", COUNT(\"r0\".\"XCL_006\") AS \"value\" FROM Match AS \"r0\" WHERE \"r0\".\"XCL_009\" = '2008/2009' GROUP BY \"r0\".\"XCL_008\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1092"
  ]
}
```

### "League"."XCL_005" = 'Germany 1. Bundesliga' AND SUBSTRING("Match"."XCL_011", 1, 7) BETWEEN '2008-08' AND '2008-10'

```json
{
  "kind": "predicate",
  "formula": "\"League\".\"XCL_005\" = 'Germany 1. Bundesliga' AND SUBSTRING(\"Match\".\"XCL_011\", 1, 7) BETWEEN '2008-08' AND '2008-10'",
  "grain": [],
  "population_scope": "SELECT COUNT(t2.\"XCL_006\") FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t1.\"XCL_005\" = 'Germany 1. Bundesliga' AND SUBSTRING(t2.\"XCL_011\", 1, 7) BETWEEN '2008-08' AND '2008-10'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1073"
  ]
}
```

### Identifier (XCL_122) for the player named 'Alexis Blin' (XCL_123) from the Player table. Used to filter Player_Attributes.

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_122\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_122\" FROM Player WHERE \"XCL_123\" = 'Alexis Blin'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_122\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_122\" AS \"value\" FROM Player AS \"r0\" WHERE \"r0\".\"XCL_123\" = 'Alexis Blin'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1140"
  ]
}
```

### DENSE_RANK() OVER (ORDER BY "Player"."XCL_126" DESC) = 1

```json
{
  "kind": "predicate",
  "formula": "DENSE_RANK() OVER (ORDER BY \"Player\".\"XCL_126\" DESC) = 1",
  "grain": [],
  "population_scope": "SELECT \"XCL_123\" FROM (SELECT \"XCL_123\", \"XCL_126\", DENSE_RANK() OVER (ORDER BY \"XCL_126\" DESC) AS rank FROM Player) WHERE \"rank\" = 1",
  "upstream_scopes": [
    "SELECT \"XCL_123\", \"XCL_126\", DENSE_RANK() OVER (ORDER BY \"XCL_126\" DESC) AS rank FROM Player"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1116"
  ]
}
```

### A scalar metric representing the percentage of rows in the Player_Attributes table where both XCL_155 and XCL_154 are greater than 80, relative to the

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN \"Player_Attributes\".\"XCL_155\" > 80 AND \"Player_Attributes\".\"XCL_154\" > 80 THEN \"Player_Attributes\".\"XCL_128\" ELSE NULL END) AS REAL) * 100 / COUNT(\"Player_Attributes\".\"XCL_128\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN \"XCL_155\" > 80 AND \"XCL_154\" > 80 THEN \"XCL_128\" ELSE NULL END) AS REAL) * 100 / COUNT(\"XCL_128\") FROM Player_Attributes AS t",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(CASE WHEN \"r0\".\"XCL_155\" > 80 AND \"r0\".\"XCL_154\" > 80 THEN \"r0\".\"XCL_128\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_128\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(CASE WHEN \"r0\".\"XCL_155\" > 80 AND \"r0\".\"XCL_154\" > 80 THEN \"r0\".\"XCL_128\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_128\") AS \"value\" FROM Player_Attributes AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1137"
  ]
}
```

### Country Name

```json
{
  "kind": "binding",
  "formula": "\"Country\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_002\" FROM Country WHERE \"XCL_001\" IN (SELECT \"XCL_004\" FROM League WHERE \"XCL_005\" = 'Poland Ekstraklasa')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1138"
  ]
}
```

### "Player"."XCL_126" > 180

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_126\" > 180",
  "grain": [
    "\"Player\".\"XCL_121\""
  ],
  "population_scope": "SELECT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_126\" > 180 GROUP BY t1.\"XCL_121\" ORDER BY CAST(SUM(t2.\"XCL_139\") AS REAL) / COUNT(t2.\"XCL_129\") DESC LIMIT 10",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1040"
  ]
}
```

### Player Identifier

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_125\"",
  "grain": [],
  "population_scope": "SELECT t1.\"XCL_125\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" ORDER BY t2.\"XCL_132\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1055"
  ]
}
```

### "League"."XCL_005" = 'Italy Serie A'

```json
{
  "kind": "predicate",
  "formula": "\"League\".\"XCL_005\" = 'Italy Serie A'",
  "grain": [],
  "population_scope": "SELECT t1.\"XCL_002\" FROM Country AS t1 INNER JOIN League AS t2 ON t1.\"XCL_001\" = t2.\"XCL_004\" WHERE t2.\"XCL_005\" = 'Italy Serie A'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1070"
  ]
}
```

### Country Identifier

```json
{
  "kind": "binding",
  "formula": "\"Country\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT t1.\"XCL_002\" FROM Country AS t1 INNER JOIN League AS t2 ON t1.\"XCL_001\" = t2.\"XCL_004\" WHERE t2.\"XCL_005\" = 'Belgium Jupiler League'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_002\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Country"
      },
      {
        "role": "r1",
        "physical_table": "League"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_002\" AS \"value\" FROM Country AS \"r0\" INNER JOIN League AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_004\" WHERE \"r1\".\"XCL_005\" = 'Belgium Jupiler League'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1081"
  ]
}
```

### The sum of column XCL_015 and column XCL_016 from the Match table, aggregated per league. Represents a combined metric of two match-related attributes

```json
{
  "kind": "metric",
  "formula": "SUM(\"Match\".\"XCL_015\") + SUM(\"Match\".\"XCL_016\")",
  "grain": [
    "\"League\".\"XCL_005\""
  ],
  "population_scope": "SELECT t1.\"XCL_005\", SUM(t2.\"XCL_015\") + SUM(t2.\"XCL_016\") FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" GROUP BY t1.\"XCL_005\" ORDER BY SUM(t2.\"XCL_015\") + SUM(t2.\"XCL_016\") ASC LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1038"
  ]
}
```

### Player Attribute XCL_138

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_138\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_128\", \"XCL_138\", \"XCL_143\" FROM Player_Attributes WHERE \"XCL_130\" = (SELECT \"XCL_122\" FROM Player ORDER BY \"XCL_127\" DESC LIMIT 1) LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1144"
  ]
}
```

### Distinct values of the Team identifier column (XCL_174) for teams that have associated attributes matching specific criteria.

```json
{
  "kind": "binding",
  "formula": "\"Team\".\"XCL_174\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_174\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_179\" = 31 AND t2.\"XCL_181\" = 53 AND t2.\"XCL_183\" = 32",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1071"
  ]
}
```

### "Team_Attributes"."XCL_183" > 70

```json
{
  "kind": "predicate",
  "formula": "\"Team_Attributes\".\"XCL_183\" > 70",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_174\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_183\" > 70",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1067"
  ]
}
```

### Player Identifier

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [
    "\"Player\".\"XCL_121\""
  ],
  "population_scope": "SELECT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_126\" > 180 GROUP BY t1.\"XCL_121\" ORDER BY CAST(SUM(t2.\"XCL_139\") AS REAL) / COUNT(t2.\"XCL_129\") DESC LIMIT 10",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1040"
  ]
}
```

### Player Identifier

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_133\" = '61' ORDER BY t2.\"XCL_151\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1075"
  ]
}
```

### Distinct Team Attribute XCL_180

```json
{
  "kind": "binding",
  "formula": "\"Team_Attributes\".\"XCL_180\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_180\" FROM Team_Attributes AS t1 INNER JOIN Team AS t2 ON t1.\"XCL_177\" = t2.\"XCL_171\" WHERE t2.\"XCL_173\" = 'KSV Cercle Brugge'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1141"
  ]
}
```

### Player Attribute XCL_143

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_143\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_128\", \"XCL_138\", \"XCL_143\" FROM Player_Attributes WHERE \"XCL_130\" = (SELECT \"XCL_122\" FROM Player ORDER BY \"XCL_127\" DESC LIMIT 1) LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1144"
  ]
}
```

### "Player_Attributes"."XCL_131" LIKE '2015-05-01%' AND "Player"."XCL_123" = 'Francesco Migliore'

```json
{
  "kind": "predicate",
  "formula": "\"Player_Attributes\".\"XCL_131\" LIKE '2015-05-01%' AND \"Player\".\"XCL_123\" = 'Francesco Migliore'",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_135\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_131\" LIKE '2015-05-01%' AND t1.\"XCL_123\" = 'Francesco Migliore'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1105"
  ]
}
```

### Min Player XCL_126

```json
{
  "kind": "metric",
  "formula": "MIN(\"Player\".\"XCL_126\")",
  "grain": [],
  "population_scope": "SELECT MIN(\"XCL_126\") FROM Player",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MIN(\"r0\".\"XCL_126\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      }
    ],
    "scope_sql": "SELECT MIN(\"r0\".\"XCL_126\") AS \"value\" FROM Player AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1058"
  ]
}
```

### Aggregates the total number of rows in the Player table that satisfy the specified filter conditions. The grain is a single scalar value representing 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"Player\".\"XCL_121\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_121\") FROM Player WHERE \"XCL_127\" > 170 AND \"XCL_123\" LIKE 'Adam%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_121\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_121\") AS \"value\" FROM Player AS \"r0\" WHERE \"r0\".\"XCL_127\" > 170 AND \"r0\".\"XCL_123\" LIKE 'Adam%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1061"
  ]
}
```

### Country Identifier

```json
{
  "kind": "binding",
  "formula": "\"Country\".\"XCL_002\"",
  "grain": [
    "\"Country\".\"XCL_002\""
  ],
  "population_scope": "SELECT t1.\"XCL_002\" FROM Country AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_001\" = t2.\"XCL_007\" INNER JOIN Player AS t3 ON t2.\"XCL_061\" = t3.\"XCL_122\" GROUP BY t1.\"XCL_002\" ORDER BY AVG(t3.\"XCL_127\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1128"
  ]
}
```

### Team Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"Team_Attributes\".\"XCL_184\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_184\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'FC Lorient' AND t2.\"XCL_178\" LIKE '2010-02-22%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_184\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Team"
      },
      {
        "role": "r1",
        "physical_table": "Team_Attributes"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_184\" AS \"value\" FROM Team AS \"r0\" INNER JOIN Team_Attributes AS \"r1\" ON \"r0\".\"XCL_171\" = \"r1\".\"XCL_177\" WHERE \"r0\".\"XCL_173\" = 'FC Lorient' AND \"r1\".\"XCL_178\" LIKE '2010-02-22%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1110"
  ]
}
```

### "Team_Attributes"."XCL_179" = 31 AND "Team_Attributes"."XCL_181" = 53 AND "Team_Attributes"."XCL_183" = 32

```json
{
  "kind": "predicate",
  "formula": "\"Team_Attributes\".\"XCL_179\" = 31 AND \"Team_Attributes\".\"XCL_181\" = 53 AND \"Team_Attributes\".\"XCL_183\" = 32",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_174\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_179\" = 31 AND t2.\"XCL_181\" = 53 AND t2.\"XCL_183\" = 32",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1071"
  ]
}
```

### Player Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_133\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_133\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Aaron Doran'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_133\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_133\" AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\" WHERE \"r0\".\"XCL_123\" = 'Aaron Doran'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1063"
  ]
}
```

### "Team"."XCL_173" = 'PEC Zwolle' AND SUBSTRING("Team_Attributes"."XCL_178", 1, 10) = '2013-09-20'

```json
{
  "kind": "predicate",
  "formula": "\"Team\".\"XCL_173\" = 'PEC Zwolle' AND SUBSTRING(\"Team_Attributes\".\"XCL_178\", 1, 10) = '2013-09-20'",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_187\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'PEC Zwolle' AND SUBSTRING(t2.\"XCL_178\", 1, 10) = '2013-09-20'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1111"
  ]
}
```

### Player Identifier

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_122\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_122\" FROM Player ORDER BY \"XCL_127\" DESC LIMIT 10",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1117"
  ]
}
```

### Calculates the percentage difference between the sum of Player_Attributes.XCL_132 for 'Landon Donovan' and 'Jordan Bowery'. The formula is ((Sum_Donov

```json
{
  "kind": "metric",
  "formula": "(SUM(CASE WHEN \"Player\".\"XCL_123\" = 'Landon Donovan' THEN \"Player_Attributes\".\"XCL_132\" ELSE 0 END) * 1.0 - SUM(CASE WHEN \"Player\".\"XCL_123\" = 'Jordan Bowery' THEN \"Player_Attributes\".\"XCL_132\" ELSE 0 END)) * 100 / SUM(CASE WHEN \"Player\".\"XCL_123\" = 'Landon Donovan' THEN \"Player_Attributes\".\"XCL_132\" ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT (SUM(CASE WHEN t1.\"XCL_123\" = 'Landon Donovan' THEN t2.\"XCL_132\" ELSE 0 END) * 1.0 - SUM(CASE WHEN t1.\"XCL_123\" = 'Jordan Bowery' THEN t2.\"XCL_132\" ELSE 0 END)) * 100 / SUM(CASE WHEN t1.\"XCL_123\" = 'Landon Donovan' THEN t2.\"XCL_132\" ELSE 0 END) AS LvsJ_percent FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_124\" = t2.\"XCL_129\" WHERE SUBSTRING(t2.\"XCL_131\", 1, 10) = '2013-07-12'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "(SUM(CASE WHEN \"r0\".\"XCL_123\" = 'Landon Donovan' THEN \"r1\".\"XCL_132\" ELSE 0 END) * 1.0 - SUM(CASE WHEN \"r0\".\"XCL_123\" = 'Jordan Bowery' THEN \"r1\".\"XCL_132\" ELSE 0 END)) * 100 / SUM(CASE WHEN \"r0\".\"XCL_123\" = 'Landon Donovan' THEN \"r1\".\"XCL_132\" ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT (SUM(CASE WHEN \"r0\".\"XCL_123\" = 'Landon Donovan' THEN \"r1\".\"XCL_132\" ELSE 0 END) * 1.0 - SUM(CASE WHEN \"r0\".\"XCL_123\" = 'Jordan Bowery' THEN \"r1\".\"XCL_132\" ELSE 0 END)) * 100 / SUM(CASE WHEN \"r0\".\"XCL_123\" = 'Landon Donovan' THEN \"r1\".\"XCL_132\" ELSE 0 END) AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_124\" = \"r1\".\"XCL_129\" WHERE SUBSTRING(\"r1\".\"XCL_131\", 1, 10) = '2013-07-12'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1115"
  ]
}
```

### Distinct values of the attribute column XCL_136 from the Player_Attributes table, filtered to records associated with the player named 'David Wilson' 

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_136\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t2.\"XCL_136\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'David Wilson'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1054"
  ]
}
```

### Player Identifier

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_123\" FROM Player WHERE \"XCL_126\" > 180 ORDER BY \"XCL_123\" LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1132"
  ]
}
```

### Latest Attribute Timestamp

```json
{
  "kind": "metric",
  "formula": "MAX(\"Player_Attributes\".\"XCL_137\")",
  "grain": [],
  "population_scope": "SELECT MAX(\"XCL_137\") FROM Player_Attributes",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MAX(\"r0\".\"XCL_137\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT MAX(\"r0\".\"XCL_137\") AS \"value\" FROM Player_Attributes AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1136"
  ]
}
```

### Distinct values of the Player identifier column (XCL_123) for players who have at least one record in Player_Attributes where both attribute columns X

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_141\" > 70 AND t2.\"XCL_142\" > 70",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1088"
  ]
}
```

### "Team"."XCL_173" = 'Queens Park Rangers'

```json
{
  "kind": "predicate",
  "formula": "\"Team\".\"XCL_173\" = 'Queens Park Rangers'",
  "grain": [],
  "population_scope": "SELECT \"XCL_174\" FROM Team WHERE \"XCL_173\" = 'Queens Park Rangers'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1043"
  ]
}
```

### Calculates the age of a player by subtracting the player's birth date (Player.XCL_125) from the current system date (DATETIME()). The result is distin

```json
{
  "kind": "binding",
  "formula": "DATETIME() - \"Player\".\"XCL_125\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT DATETIME() - T2.\"XCL_125\" AS age FROM Player_Attributes AS t1 INNER JOIN Player AS t2 ON t1.\"XCL_130\" = t2.\"XCL_122\" WHERE STRFTIME('%Y', t1.\"XCL_131\") >= '2013' AND STRFTIME('%Y', t1.\"XCL_131\") <= '2015' AND t1.\"XCL_148\" >= 97",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1031"
  ]
}
```

### "Player"."XCL_123" = 'Ariel Borysiuk'

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_123\" = 'Ariel Borysiuk'",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_139\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Ariel Borysiuk'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1086"
  ]
}
```

### Match Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"Match\".\"XCL_006\")",
  "grain": [],
  "population_scope": "SELECT COUNT(t2.\"XCL_006\") FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t2.\"XCL_009\" = '2015/2016' AND t1.\"XCL_005\" = 'Scotland Premier League'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_006\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "League"
      },
      {
        "role": "r1",
        "physical_table": "Match"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_006\") AS \"value\" FROM League AS \"r0\" INNER JOIN Match AS \"r1\" ON \"r0\".\"XCL_003\" = \"r1\".\"XCL_008\" WHERE \"r1\".\"XCL_009\" = '2015/2016' AND \"r0\".\"XCL_005\" = 'Scotland Premier League'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1049"
  ]
}
```

### Average Attribute Value

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"Player_Attributes\".\"XCL_132\") AS REAL) / COUNT(\"Player_Attributes\".\"XCL_128\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(t2.\"XCL_132\") AS REAL) / COUNT(t2.\"XCL_128\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Pietro Marino'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(\"r1\".\"XCL_132\") AS REAL) / COUNT(\"r1\".\"XCL_128\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(\"r1\".\"XCL_132\") AS REAL) / COUNT(\"r1\".\"XCL_128\") AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\" WHERE \"r0\".\"XCL_123\" = 'Pietro Marino'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1096"
  ]
}
```

### "Player_Attributes"."XCL_134" = 'right'

```json
{
  "kind": "predicate",
  "formula": "\"Player_Attributes\".\"XCL_134\" = 'right'",
  "grain": [],
  "population_scope": "SELECT \"XCL_128\" FROM Player_Attributes WHERE \"XCL_134\" = 'right' ORDER BY \"XCL_133\" DESC LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1135"
  ]
}
```

### SUBSTRING("Player_Attributes"."XCL_131", 1, 10) = '2016-06-23' AND "Player_Attributes"."XCL_132" = 77

```json
{
  "kind": "predicate",
  "formula": "SUBSTRING(\"Player_Attributes\".\"XCL_131\", 1, 10) = '2016-06-23' AND \"Player_Attributes\".\"XCL_132\" = 77",
  "grain": [],
  "population_scope": "SELECT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE SUBSTRING(t2.\"XCL_131\", 1, 10) = '2016-06-23' AND t2.\"XCL_132\" = 77 ORDER BY t1.\"XCL_125\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1102"
  ]
}
```

### League Name or Identifier

```json
{
  "kind": "binding",
  "formula": "t2.\"XCL_005\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_005\", t1.\"max_count\" FROM League AS t2 JOIN (SELECT \"XCL_008\", MAX(\"cnt\") AS max_count FROM (SELECT \"XCL_008\", COUNT(\"XCL_006\") AS cnt FROM Match GROUP BY \"XCL_008\") AS subquery) AS t1 ON t1.\"XCL_008\" = t2.\"XCL_003\"",
  "upstream_scopes": [
    "SELECT \"XCL_008\", COUNT(\"XCL_006\") AS cnt FROM Match GROUP BY \"XCL_008\"",
    "SELECT \"XCL_008\", MAX(\"cnt\") AS max_count FROM (SELECT \"XCL_008\", COUNT(\"XCL_006\") AS cnt FROM Match GROUP BY \"XCL_008\") AS subquery"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1032"
  ]
}
```

### Team Identifier

```json
{
  "kind": "binding",
  "formula": "\"Team\".\"XCL_173\"",
  "grain": [
    "\"Match\".\"XCL_013\""
  ],
  "population_scope": "SELECT teamDetails.\"XCL_173\" FROM Match AS matchData INNER JOIN Team AS teamDetails ON matchData.\"XCL_013\" = teamDetails.\"XCL_171\" WHERE matchData.\"XCL_009\" = '2015/2016' AND matchData.\"XCL_015\" - matchData.\"XCL_016\" < 0 GROUP BY matchData.\"XCL_013\" ORDER BY COUNT(*) ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1026"
  ]
}
```

### League Identifier

```json
{
  "kind": "binding",
  "formula": "\"League\".\"XCL_005\"",
  "grain": [
    "\"League\".\"XCL_005\""
  ],
  "population_scope": "SELECT t2.\"XCL_005\" FROM Match AS t1 INNER JOIN League AS t2 ON t1.\"XCL_008\" = t2.\"XCL_003\" WHERE t1.\"XCL_009\" = '2015/2016' AND t1.\"XCL_015\" = t1.\"XCL_016\" GROUP BY t2.\"XCL_005\" ORDER BY COUNT(t1.\"XCL_006\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1030"
  ]
}
```

### Player Identifier for Belgium Matches

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT t3.\"XCL_123\" FROM Country AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_001\" = t2.\"XCL_007\" INNER JOIN Player AS t3 ON t2.\"XCL_061\" = t3.\"XCL_122\" WHERE t1.\"XCL_002\" = 'Belgium'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_123\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Country"
      },
      {
        "role": "r1",
        "physical_table": "Match"
      },
      {
        "role": "r2",
        "physical_table": "Player"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_123\" AS \"value\" FROM Country AS \"r0\" INNER JOIN Match AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_007\" INNER JOIN Player AS \"r2\" ON \"r1\".\"XCL_061\" = \"r2\".\"XCL_122\" WHERE \"r0\".\"XCL_002\" = 'Belgium'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1126"
  ]
}
```

### The identifier (XCL_005) of the single league with the highest total score in the 2015/2016 season. The population is leagues associated with matches 

```json
{
  "kind": "binding",
  "formula": "\"League\".\"XCL_005\"",
  "grain": [
    "\"League\".\"XCL_005\""
  ],
  "population_scope": "SELECT t2.\"XCL_005\" FROM Match AS t1 INNER JOIN League AS t2 ON t1.\"XCL_008\" = t2.\"XCL_003\" WHERE t1.\"XCL_009\" = '2015/2016' GROUP BY t2.\"XCL_005\" ORDER BY SUM(t1.\"XCL_015\" + t1.\"XCL_016\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1025"
  ]
}
```

### SUBSTRING("Player"."XCL_125", 1, 4) BETWEEN '1990' AND '1995'

```json
{
  "kind": "predicate",
  "formula": "SUBSTRING(\"Player\".\"XCL_125\", 1, 4) BETWEEN '1990' AND '1995'",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_126\") / COUNT(\"XCL_121\") FROM Player WHERE SUBSTRING(\"XCL_125\", 1, 4) BETWEEN '1990' AND '1995'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1033"
  ]
}
```

### "Player"."XCL_123" = 'Aaron Doran'

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_123\" = 'Aaron Doran'",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_133\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Aaron Doran'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1063"
  ]
}
```

### Player Identifier

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE SUBSTRING(t2.\"XCL_131\", 1, 10) = '2016-06-23' AND t2.\"XCL_132\" = 77 ORDER BY t1.\"XCL_125\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1102"
  ]
}
```

### DATETIME(CURRENT_TIMESTAMP, 'localtime') - DATETIME("Player"."XCL_125") < 31

```json
{
  "kind": "predicate",
  "formula": "DATETIME(CURRENT_TIMESTAMP, 'localtime') - DATETIME(\"Player\".\"XCL_125\") < 31",
  "grain": [],
  "population_scope": "SELECT SUM(t2.\"XCL_015\") FROM Player AS t1 INNER JOIN match AS t2 ON t1.\"XCL_122\" = t2.\"XCL_072\" WHERE DATETIME(CURRENT_TIMESTAMP, 'localtime') - DATETIME(T1.\"XCL_125\") < 31",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1121"
  ]
}
```

### "Player_Attributes"."XCL_138" = 1

```json
{
  "kind": "predicate",
  "formula": "\"Player_Attributes\".\"XCL_138\" = 1",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_138\" = 1 ORDER BY t1.\"XCL_125\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1125"
  ]
}
```

### "Player"."XCL_123" = 'Dorlan Pabon'

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_123\" = 'Dorlan Pabon'",
  "grain": [],
  "population_scope": "SELECT MAX(t2.\"XCL_132\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Dorlan Pabon'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1100"
  ]
}
```

### Team Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"Team_Attributes\".\"XCL_180\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_180\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'Willem II' AND SUBSTRING(t2.\"XCL_178\", 1, 10) = '2011-02-22'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_180\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Team"
      },
      {
        "role": "r1",
        "physical_table": "Team_Attributes"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_180\" AS \"value\" FROM Team AS \"r0\" INNER JOIN Team_Attributes AS \"r1\" ON \"r0\".\"XCL_171\" = \"r1\".\"XCL_177\" WHERE \"r0\".\"XCL_173\" = 'Willem II' AND SUBSTRING(\"r1\".\"XCL_178\", 1, 10) = '2011-02-22'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1108"
  ]
}
```

### The value of the attribute column XCL_130 for the single record in Player_Attributes that has the highest value in the ordering column XCL_132. This r

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_130\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_130\" FROM Player_Attributes ORDER BY \"XCL_132\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1020"
  ]
}
```

### Match Count per League

```json
{
  "kind": "metric",
  "formula": "COUNT(\"Match\".\"XCL_006\")",
  "grain": [
    "\"Match\".\"XCL_008\""
  ],
  "population_scope": "SELECT \"XCL_008\", COUNT(\"XCL_006\") AS cnt FROM Match GROUP BY \"XCL_008\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_006\")",
    "grain": [
      "\"r0\".\"XCL_008\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Match"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_008\" AS \"grain_0\", COUNT(\"r0\".\"XCL_006\") AS \"value\" FROM Match AS \"r0\" GROUP BY \"r0\".\"XCL_008\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1032"
  ]
}
```

### Average XCL_156 per XCL_131

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"Player_Attributes\".\"XCL_156\") AS REAL) / COUNT(\"Player_Attributes\".\"XCL_131\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(t2.\"XCL_156\") AS REAL) / COUNT(t2.\"XCL_131\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Ahmed Samir Farag'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(\"r1\".\"XCL_156\") AS REAL) / COUNT(\"r1\".\"XCL_131\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(\"r1\".\"XCL_156\") AS REAL) / COUNT(\"r1\".\"XCL_131\") AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\" WHERE \"r0\".\"XCL_123\" = 'Ahmed Samir Farag'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1039"
  ]
}
```

### Distinct values of the Team identifier column (XCL_174) for teams that have at least one associated Team_Attributes record where the attribute value (

```json
{
  "kind": "binding",
  "formula": "\"Team\".\"XCL_174\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_174\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_183\" > 70",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1067"
  ]
}
```

### "Player"."XCL_125" > '1990' AND "Player"."XCL_123" LIKE 'Aaron%'

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_125\" > '1990' AND \"Player\".\"XCL_123\" LIKE 'Aaron%'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_121\") FROM Player WHERE \"XCL_125\" > '1990' AND \"XCL_123\" LIKE 'Aaron%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1133"
  ]
}
```

### Average XCL_126 per XCL_121

```json
{
  "kind": "metric",
  "formula": "SUM(\"Player\".\"XCL_126\") / COUNT(\"Player\".\"XCL_121\")",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_126\") / COUNT(\"XCL_121\") FROM Player WHERE SUBSTRING(\"XCL_125\", 1, 4) BETWEEN '1990' AND '1995'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r0\".\"XCL_126\") / COUNT(\"r0\".\"XCL_121\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      }
    ],
    "scope_sql": "SELECT SUM(\"r0\".\"XCL_126\") / COUNT(\"r0\".\"XCL_121\") AS \"value\" FROM Player AS \"r0\" WHERE SUBSTRING(\"r0\".\"XCL_125\", 1, 4) BETWEEN '1990' AND '1995'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1033"
  ]
}
```

### "Player"."XCL_127" < 130 AND "Player_Attributes"."XCL_134" = 'left'

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_127\" < 130 AND \"Player_Attributes\".\"XCL_134\" = 'left'",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT t1.\"XCL_121\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_127\" < 130 AND t2.\"XCL_134\" = 'left'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1052"
  ]
}
```

### "Player_Attributes"."XCL_141" > 70 AND "Player_Attributes"."XCL_142" > 70

```json
{
  "kind": "predicate",
  "formula": "\"Player_Attributes\".\"XCL_141\" > 70 AND \"Player_Attributes\".\"XCL_142\" > 70",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_141\" > 70 AND t2.\"XCL_142\" > 70",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1088"
  ]
}
```

### Attribute value from Team_Attributes returned alongside XCL_186; represents the associated data point for the record with the maximum XCL_186 value fo

```json
{
  "kind": "binding",
  "formula": "\"Team_Attributes\".\"XCL_187\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_186\", t2.\"XCL_187\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'Ajax' ORDER BY t2.\"XCL_186\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1098"
  ]
}
```

### Player Identifier

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_123\" FROM Player_Attributes AS t1 INNER JOIN Player AS t2 ON t1.\"XCL_128\" = t2.\"XCL_121\" ORDER BY t1.\"XCL_161\" DESC LIMIT 10",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1027"
  ]
}
```

### Player Identifier

```json
{
  "kind": "binding",
  "formula": "\"player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_123\" FROM player ORDER BY \"XCL_126\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1069"
  ]
}
```

### The value of column "XCL_123" from the "Player" table for the single row with the highest value in column "XCL_126".

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_123\" FROM Player ORDER BY \"XCL_126\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1079",
    "bird_dev:1021"
  ]
}
```

### A

```json
{
  "kind": "binding",
  "formula": "'Max'",
  "grain": [],
  "population_scope": "SELECT AVG(\"XCL_138\") AS result, 'Max' AS A FROM Player AS T1 INNER JOIN Player_Attributes AS T2 ON T1.\"XCL_122\" = T2.\"XCL_130\" WHERE T1.\"XCL_126\" = (SELECT MAX(\"XCL_126\") FROM Player)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1058"
  ]
}
```

### "Player"."XCL_123" = 'Pietro Marino'

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_123\" = 'Pietro Marino'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(t2.\"XCL_132\") AS REAL) / COUNT(t2.\"XCL_128\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Pietro Marino'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1096"
  ]
}
```

### Team_Attributes.XCL_187

```json
{
  "kind": "binding",
  "formula": "\"Team_Attributes\".\"XCL_187\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_187\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'PEC Zwolle' AND SUBSTRING(t2.\"XCL_178\", 1, 10) = '2013-09-20'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_187\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Team"
      },
      {
        "role": "r1",
        "physical_table": "Team_Attributes"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_187\" AS \"value\" FROM Team AS \"r0\" INNER JOIN Team_Attributes AS \"r1\" ON \"r0\".\"XCL_171\" = \"r1\".\"XCL_177\" WHERE \"r0\".\"XCL_173\" = 'PEC Zwolle' AND SUBSTRING(\"r1\".\"XCL_178\", 1, 10) = '2013-09-20'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1111"
  ]
}
```

### Aggregated sum of the 'XCL_015' column from the 'match' table. The population is restricted to matches associated with players whose 'XCL_125' timesta

```json
{
  "kind": "metric",
  "formula": "SUM(\"match\".\"XCL_015\")",
  "grain": [],
  "population_scope": "SELECT SUM(t2.\"XCL_015\") FROM Player AS t1 INNER JOIN match AS t2 ON t1.\"XCL_122\" = t2.\"XCL_072\" WHERE DATETIME(CURRENT_TIMESTAMP, 'localtime') - DATETIME(T1.\"XCL_125\") < 31",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r1\".\"XCL_015\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "match"
      }
    ],
    "scope_sql": "SELECT SUM(\"r1\".\"XCL_015\") AS \"value\" FROM Player AS \"r0\" INNER JOIN match AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_072\" WHERE DATETIME(CURRENT_TIMESTAMP, 'localtime') - DATETIME(\"r0\".\"XCL_125\") < 31",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1121"
  ]
}
```

### Player Name

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_123\" FROM Player WHERE \"XCL_123\" IN ('Aaron Lennon', 'Abdelaziz Barrada') ORDER BY \"XCL_125\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1078"
  ]
}
```

### Calculates the percentage of players with a 'left' preferred foot among those born between 1987 and 1992. The numerator counts players where Player_At

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN \"Player_Attributes\".\"XCL_134\" = 'left' THEN \"Player\".\"XCL_121\" ELSE NULL END) AS REAL) * 100 / COUNT(\"Player\".\"XCL_121\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN t2.\"XCL_134\" = 'left' THEN t1.\"XCL_121\" ELSE NULL END) AS REAL) * 100 / COUNT(t1.\"XCL_121\") AS percent FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE SUBSTRING(t1.\"XCL_125\", 1, 4) BETWEEN '1987' AND '1992'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(CASE WHEN \"r1\".\"XCL_134\" = 'left' THEN \"r0\".\"XCL_121\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_121\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(CASE WHEN \"r1\".\"XCL_134\" = 'left' THEN \"r0\".\"XCL_121\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_121\") AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\" WHERE SUBSTRING(\"r0\".\"XCL_125\", 1, 4) BETWEEN '1987' AND '1992'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1037"
  ]
}
```

### "Team"."XCL_173" = 'Hannover 96' AND "Team_Attributes"."XCL_178" LIKE '2015-09-10%'

```json
{
  "kind": "predicate",
  "formula": "\"Team\".\"XCL_173\" = 'Hannover 96' AND \"Team_Attributes\".\"XCL_178\" LIKE '2015-09-10%'",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_191\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'Hannover 96' AND t2.\"XCL_178\" LIKE '2015-09-10%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1113"
  ]
}
```

### Player Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_133\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_133\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE SUBSTRING(t2.\"XCL_131\", 1, 10) = '2010-08-30' AND t1.\"XCL_123\" = 'Francesco Parravicini'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_133\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_133\" AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\" WHERE SUBSTRING(\"r1\".\"XCL_131\", 1, 10) = '2010-08-30' AND \"r0\".\"XCL_123\" = 'Francesco Parravicini'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1104"
  ]
}
```

### "Team_attributes"."XCL_187" = 'Risky'

```json
{
  "kind": "predicate",
  "formula": "\"Team_attributes\".\"XCL_187\" = 'Risky'",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_174\" FROM Team AS t1 INNER JOIN Team_attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_187\" = 'Risky'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1053"
  ]
}
```

### The value of the 'XCL_123' column from the Player table for the single record with the highest 'XCL_132' value in the joined Player_Attributes table.

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" ORDER BY t2.\"XCL_132\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1083"
  ]
}
```

### Team Identifier

```json
{
  "kind": "binding",
  "formula": "\"Team\".\"XCL_174\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_174\" FROM Team WHERE \"XCL_173\" = 'Queens Park Rangers'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_174\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Team"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_174\" AS \"value\" FROM Team AS \"r0\" WHERE \"r0\".\"XCL_173\" = 'Queens Park Rangers'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1043"
  ]
}
```

### SUBSTRING("Player_Attributes"."XCL_131", 1, 10) = '2013-02-22' AND "Player"."XCL_123" = 'Kevin Berigaud'

```json
{
  "kind": "predicate",
  "formula": "SUBSTRING(\"Player_Attributes\".\"XCL_131\", 1, 10) = '2013-02-22' AND \"Player\".\"XCL_123\" = 'Kevin Berigaud'",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_136\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_124\" = t2.\"XCL_129\" WHERE SUBSTRING(t2.\"XCL_131\", 1, 10) = '2013-02-22' AND t1.\"XCL_123\" = 'Kevin Berigaud'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1106"
  ]
}
```

### Identifier column XCL_123 from the Player table, representing the unique key or ID for each player record.

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_123\", \"XCL_126\", DENSE_RANK() OVER (ORDER BY \"XCL_126\" DESC) AS rank FROM Player",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_123\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_123\" AS \"value\" FROM Player AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1116"
  ]
}
```

### STRFTIME('%Y', "Player"."XCL_125") < '1986' AND "Player_Attributes"."XCL_136" = 'high'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"Player\".\"XCL_125\") < '1986' AND \"Player_Attributes\".\"XCL_136\" = 'high'",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT t1.\"XCL_123\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE STRFTIME('%Y', t1.\"XCL_125\") < '1986' AND t2.\"XCL_136\" = 'high'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1084"
  ]
}
```

### "League"."XCL_005" = 'Belgium Jupiler League' AND "Match"."XCL_011" LIKE '2008-09-24%'

```json
{
  "kind": "predicate",
  "formula": "\"League\".\"XCL_005\" = 'Belgium Jupiler League' AND \"Match\".\"XCL_011\" LIKE '2008-09-24%'",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_015\", t2.\"XCL_016\" FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t1.\"XCL_005\" = 'Belgium Jupiler League' AND t2.\"XCL_011\" LIKE '2008-09-24%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1139"
  ]
}
```

### Player Attribute XCL_134

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_134\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_134\" FROM Player_Attributes WHERE NOT \"XCL_133\" IS NULL ORDER BY \"XCL_133\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1022"
  ]
}
```

### Distinct values of the attribute column XCL_134 from the Player_Attributes table, filtered to records associated with the player named 'Abdou Diallo' 

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_134\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t2.\"XCL_134\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Abdou Diallo'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1099"
  ]
}
```

### "Team"."XCL_174" = 'LEI' AND SUBSTRING("Team_Attributes"."XCL_178", 1, 10) = '2015-09-10'

```json
{
  "kind": "predicate",
  "formula": "\"Team\".\"XCL_174\" = 'LEI' AND SUBSTRING(\"Team_Attributes\".\"XCL_178\", 1, 10) = '2015-09-10'",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_182\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_174\" = 'LEI' AND SUBSTRING(t2.\"XCL_178\", 1, 10) = '2015-09-10'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1109"
  ]
}
```

### "League"."XCL_005" = 'Italy Serie A' AND "Match"."XCL_009" = '2015/2016'

```json
{
  "kind": "predicate",
  "formula": "\"League\".\"XCL_005\" = 'Italy Serie A' AND \"Match\".\"XCL_009\" = '2015/2016'",
  "grain": [],
  "population_scope": "SELECT COUNT(t2.\"XCL_006\") FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t1.\"XCL_005\" = 'Italy Serie A' AND t2.\"XCL_009\" = '2015/2016'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1142"
  ]
}
```

### Returns the top 5 values of the column XCL_128 from the Player_Attributes table, ordered by XCL_137 in descending order. The grain is individual rows 

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_128\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_128\" FROM Player_Attributes ORDER BY \"XCL_137\" DESC LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1024"
  ]
}
```

### "Country"."XCL_002" = 'Belgium'

```json
{
  "kind": "predicate",
  "formula": "\"Country\".\"XCL_002\" = 'Belgium'",
  "grain": [],
  "population_scope": "SELECT t3.\"XCL_123\" FROM Country AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_001\" = t2.\"XCL_007\" INNER JOIN Player AS t3 ON t2.\"XCL_061\" = t3.\"XCL_122\" WHERE t1.\"XCL_002\" = 'Belgium'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1126"
  ]
}
```

### Counts the number of unique players (identified by XCL_121) who have a recorded attribute of 'left' (XCL_134) and meet the condition that XCL_127 is l

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"Player\".\"XCL_121\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT t1.\"XCL_121\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_127\" < 130 AND t2.\"XCL_134\" = 'left'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_121\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r0\".\"XCL_121\") AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\" WHERE \"r0\".\"XCL_127\" < 130 AND \"r1\".\"XCL_134\" = 'left'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1052"
  ]
}
```

### SUBSTRING("Player_Attributes"."XCL_131", 1, 10) = '2016-02-04' AND "Player"."XCL_123" = 'Aaron Mooy'

```json
{
  "kind": "predicate",
  "formula": "SUBSTRING(\"Player_Attributes\".\"XCL_131\", 1, 10) = '2016-02-04' AND \"Player\".\"XCL_123\" = 'Aaron Mooy'",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_132\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE SUBSTRING(t2.\"XCL_131\", 1, 10) = '2016-02-04' AND t1.\"XCL_123\" = 'Aaron Mooy'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1103"
  ]
}
```

### Player Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"Player\".\"XCL_121\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_121\") FROM Player WHERE STRFTIME('%Y', \"XCL_125\") > '1990'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_121\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_121\") AS \"value\" FROM Player AS \"r0\" WHERE STRFTIME('%Y', \"r0\".\"XCL_125\") > '1990'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1060"
  ]
}
```

### "Player"."XCL_127" > 170 AND "Player"."XCL_123" LIKE 'Adam%'

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_127\" > 170 AND \"Player\".\"XCL_123\" LIKE 'Adam%'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_121\") FROM Player WHERE \"XCL_127\" > 170 AND \"XCL_123\" LIKE 'Adam%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1061"
  ]
}
```

### Crossing Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_136\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_136\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_124\" = t2.\"XCL_129\" WHERE SUBSTRING(t2.\"XCL_131\", 1, 10) = '2013-02-22' AND t1.\"XCL_123\" = 'Kevin Berigaud'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_136\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_136\" AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_124\" = \"r1\".\"XCL_129\" WHERE SUBSTRING(\"r1\".\"XCL_131\", 1, 10) = '2013-02-22' AND \"r0\".\"XCL_123\" = 'Kevin Berigaud'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1106"
  ]
}
```

### "Match"."XCL_009" = '2015/2016' AND "Match"."XCL_015" = "Match"."XCL_016"

```json
{
  "kind": "predicate",
  "formula": "\"Match\".\"XCL_009\" = '2015/2016' AND \"Match\".\"XCL_015\" = \"Match\".\"XCL_016\"",
  "grain": [
    "\"League\".\"XCL_005\""
  ],
  "population_scope": "SELECT t2.\"XCL_005\" FROM Match AS t1 INNER JOIN League AS t2 ON t1.\"XCL_008\" = t2.\"XCL_003\" WHERE t1.\"XCL_009\" = '2015/2016' AND t1.\"XCL_015\" = t1.\"XCL_016\" GROUP BY t2.\"XCL_005\" ORDER BY COUNT(t1.\"XCL_006\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1030"
  ]
}
```

### Country Identifier

```json
{
  "kind": "binding",
  "formula": "\"Country\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT t1.\"XCL_002\" FROM Country AS t1 INNER JOIN League AS t2 ON t1.\"XCL_001\" = t2.\"XCL_004\" WHERE t2.\"XCL_005\" = 'Italy Serie A'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_002\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Country"
      },
      {
        "role": "r1",
        "physical_table": "League"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_002\" AS \"value\" FROM Country AS \"r0\" INNER JOIN League AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_004\" WHERE \"r1\".\"XCL_005\" = 'Italy Serie A'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1070"
  ]
}
```

### "Match"."XCL_009" = '2015/2016' AND "Match"."XCL_015" - "Match"."XCL_016" < 0

```json
{
  "kind": "predicate",
  "formula": "\"Match\".\"XCL_009\" = '2015/2016' AND \"Match\".\"XCL_015\" - \"Match\".\"XCL_016\" < 0",
  "grain": [
    "\"Match\".\"XCL_013\""
  ],
  "population_scope": "SELECT teamDetails.\"XCL_173\" FROM Match AS matchData INNER JOIN Team AS teamDetails ON matchData.\"XCL_013\" = teamDetails.\"XCL_171\" WHERE matchData.\"XCL_009\" = '2015/2016' AND matchData.\"XCL_015\" - matchData.\"XCL_016\" < 0 GROUP BY matchData.\"XCL_013\" ORDER BY COUNT(*) ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1026"
  ]
}
```

### "Player"."XCL_126" > 180

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_126\" > 180",
  "grain": [],
  "population_scope": "SELECT \"XCL_123\" FROM Player WHERE \"XCL_126\" > 180",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1059"
  ]
}
```

### Calculates the percentage of players (filtered by XCL_126 < 180) who have a corresponding Player_Attributes record where XCL_132 is greater than 70. T

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(CASE WHEN \"Player_Attributes\".\"XCL_132\" > 70 THEN \"Player\".\"XCL_121\" ELSE NULL END) AS REAL) * 100 / COUNT(\"Player\".\"XCL_121\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN t2.\"XCL_132\" > 70 THEN t1.\"XCL_121\" ELSE NULL END) AS REAL) * 100 / COUNT(t1.\"XCL_121\") AS percent FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_126\" < 180",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(CASE WHEN \"r1\".\"XCL_132\" > 70 THEN \"r0\".\"XCL_121\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_121\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(CASE WHEN \"r1\".\"XCL_132\" > 70 THEN \"r0\".\"XCL_121\" ELSE NULL END) AS REAL) * 100 / COUNT(\"r0\".\"XCL_121\") AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\" WHERE \"r0\".\"XCL_126\" < 180",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1148"
  ]
}
```

### "Player"."XCL_126" < 180

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_126\" < 180",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(CASE WHEN t2.\"XCL_132\" > 70 THEN t1.\"XCL_121\" ELSE NULL END) AS REAL) * 100 / COUNT(t1.\"XCL_121\") AS percent FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_126\" < 180",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1148"
  ]
}
```

### Aggregated count of match records (XCL_006) for a specific country and season. The population is restricted to matches where the country name is 'Belg

```json
{
  "kind": "metric",
  "formula": "COUNT(\"Match\".\"XCL_006\")",
  "grain": [],
  "population_scope": "SELECT COUNT(t2.\"XCL_006\") FROM Country AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_001\" = t2.\"XCL_007\" WHERE t1.\"XCL_002\" = 'Belgium' AND t2.\"XCL_009\" = '2008/2009'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_006\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Country"
      },
      {
        "role": "r1",
        "physical_table": "Match"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_006\") AS \"value\" FROM Country AS \"r0\" INNER JOIN Match AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_007\" WHERE \"r0\".\"XCL_002\" = 'Belgium' AND \"r1\".\"XCL_009\" = '2008/2009'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1089"
  ]
}
```

### STRFTIME('%Y', "Player_Attributes"."XCL_131") >= '2013' AND STRFTIME('%Y', "Player_Attributes"."XCL_131") <= '2015' AND "Player_Attributes"."XCL_148" 

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"Player_Attributes\".\"XCL_131\") >= '2013' AND STRFTIME('%Y', \"Player_Attributes\".\"XCL_131\") <= '2015' AND \"Player_Attributes\".\"XCL_148\" >= 97",
  "grain": [],
  "population_scope": "SELECT DISTINCT DATETIME() - T2.\"XCL_125\" AS age FROM Player_Attributes AS t1 INNER JOIN Player AS t2 ON t1.\"XCL_130\" = t2.\"XCL_122\" WHERE STRFTIME('%Y', t1.\"XCL_131\") >= '2013' AND STRFTIME('%Y', t1.\"XCL_131\") <= '2015' AND t1.\"XCL_148\" >= 97",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1031"
  ]
}
```

### "Match"."XCL_009" = '2008/2009'

```json
{
  "kind": "predicate",
  "formula": "\"Match\".\"XCL_009\" = '2008/2009'",
  "grain": [
    "\"League\".\"XCL_005\""
  ],
  "population_scope": "SELECT t1.\"XCL_005\" FROM League AS t1 JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t2.\"XCL_009\" = '2008/2009' GROUP BY t1.\"XCL_005\" HAVING COUNT(t2.\"XCL_006\") = (SELECT MAX(\"match_count\") FROM (SELECT COUNT(t2.\"XCL_006\") AS match_count FROM Match AS t2 WHERE t2.\"XCL_009\" = '2008/2009' GROUP BY t2.\"XCL_008\"))",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1092"
  ]
}
```

### "Player"."XCL_123" = 'Aaron Lennox'

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_123\" = 'Aaron Lennox'",
  "grain": [],
  "population_scope": "SELECT SUM(t2.\"XCL_137\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Aaron Lennox'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1097"
  ]
}
```

### "Team"."XCL_173" = 'Ajax'

```json
{
  "kind": "predicate",
  "formula": "\"Team\".\"XCL_173\" = 'Ajax'",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_186\", t2.\"XCL_187\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'Ajax' ORDER BY t2.\"XCL_186\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1098"
  ]
}
```

### "Team"."XCL_174" = 'GEN'

```json
{
  "kind": "predicate",
  "formula": "\"Team\".\"XCL_174\" = 'GEN'",
  "grain": [],
  "population_scope": "SELECT \"XCL_173\" FROM Team WHERE \"XCL_174\" = 'GEN'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1077"
  ]
}
```

### Player Attribute XCL_128

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_128\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_128\" FROM Player_Attributes WHERE \"XCL_134\" = 'right' ORDER BY \"XCL_133\" DESC LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1135"
  ]
}
```

### CAST((JULIANDAY('now') - JULIANDAY("Player"."XCL_125")) AS REAL) / 365 >= 35

```json
{
  "kind": "predicate",
  "formula": "CAST((JULIANDAY('now') - JULIANDAY(\"Player\".\"XCL_125\")) AS REAL) / 365 >= 35",
  "grain": [],
  "population_scope": "SELECT \"XCL_123\" FROM Player WHERE CAST((JULIANDAY('now') - JULIANDAY(\"XCL_125\")) AS REAL) / 365 >= 35",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1118"
  ]
}
```

### League Identifier

```json
{
  "kind": "binding",
  "formula": "\"League\".\"XCL_005\"",
  "grain": [
    "\"League\".\"XCL_005\""
  ],
  "population_scope": "SELECT t1.\"XCL_005\" FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t2.\"XCL_009\" = '2009/2010' GROUP BY t1.\"XCL_005\" HAVING (CAST(SUM(t2.\"XCL_015\") AS REAL) / COUNT(DISTINCT t2.\"XCL_006\")) - (CAST(SUM(t2.\"XCL_016\") AS REAL) / COUNT(DISTINCT t2.\"XCL_006\")) > 0",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_005\"",
    "grain": [
      "\"r0\".\"XCL_005\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "League"
      },
      {
        "role": "r1",
        "physical_table": "Match"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_005\" AS \"grain_0\", \"r0\".\"XCL_005\" AS \"value\" FROM League AS \"r0\" INNER JOIN Match AS \"r1\" ON \"r0\".\"XCL_003\" = \"r1\".\"XCL_008\" WHERE \"r1\".\"XCL_009\" = '2009/2010' GROUP BY \"r0\".\"XCL_005\" HAVING (CAST(SUM(\"r1\".\"XCL_015\") AS REAL) / COUNT(DISTINCT \"r1\".\"XCL_006\")) - (CAST(SUM(\"r1\".\"XCL_016\") AS REAL) / COUNT(DISTINCT \"r1\".\"XCL_006\")) > 0",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1042"
  ]
}
```

### Distinct values of the Team identifier column (XCL_174) for teams whose associated attributes record a 'Safe' value in column XCL_187.

```json
{
  "kind": "binding",
  "formula": "\"Team\".\"XCL_174\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_174\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_187\" = 'Safe'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1130"
  ]
}
```

### "Team_Attributes"."XCL_182" = 'Normal' AND SUBSTRING("Team_Attributes"."XCL_178", 1, 4) = '2014'

```json
{
  "kind": "predicate",
  "formula": "\"Team_Attributes\".\"XCL_182\" = 'Normal' AND SUBSTRING(\"Team_Attributes\".\"XCL_178\", 1, 4) = '2014'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(t2.\"XCL_186\") AS REAL) / COUNT(t1.\"XCL_170\") FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_182\" = 'Normal' AND SUBSTRING(t2.\"XCL_178\", 1, 4) = '2014'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1041"
  ]
}
```

### Match Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"Match\".\"XCL_006\")",
  "grain": [],
  "population_scope": "SELECT COUNT(t2.\"XCL_006\") FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t1.\"XCL_005\" = 'Italy Serie A' AND t2.\"XCL_009\" = '2015/2016'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_006\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "League"
      },
      {
        "role": "r1",
        "physical_table": "Match"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_006\") AS \"value\" FROM League AS \"r0\" INNER JOIN Match AS \"r1\" ON \"r0\".\"XCL_003\" = \"r1\".\"XCL_008\" WHERE \"r0\".\"XCL_005\" = 'Italy Serie A' AND \"r1\".\"XCL_009\" = '2015/2016'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1142"
  ]
}
```

### Player Identifier

```json
{
  "kind": "binding",
  "formula": "(\"Player\".\"XCL_123\")",
  "grain": [],
  "population_scope": "SELECT DISTINCT (t1.\"XCL_123\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_133\" = (SELECT MAX(\"XCL_133\") FROM Player_Attributes)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1051"
  ]
}
```

### League Identifier

```json
{
  "kind": "binding",
  "formula": "\"League\".\"XCL_005\"",
  "grain": [
    "\"League\".\"XCL_005\""
  ],
  "population_scope": "SELECT t1.\"XCL_005\" FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t2.\"XCL_009\" = '2015/2016' GROUP BY t1.\"XCL_005\" ORDER BY COUNT(t2.\"XCL_006\") DESC LIMIT 4",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1145"
  ]
}
```

### Average XCL_015 per XCL_006

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"Match\".\"XCL_015\") AS REAL) / COUNT(\"Match\".\"XCL_006\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(t2.\"XCL_015\") AS REAL) / COUNT(t2.\"XCL_006\") FROM Country AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_001\" = t2.\"XCL_007\" WHERE t1.\"XCL_002\" = 'Poland' AND t2.\"XCL_009\" = '2010/2011'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(\"r1\".\"XCL_015\") AS REAL) / COUNT(\"r1\".\"XCL_006\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Country"
      },
      {
        "role": "r1",
        "physical_table": "Match"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(\"r1\".\"XCL_015\") AS REAL) / COUNT(\"r1\".\"XCL_006\") AS \"value\" FROM Country AS \"r0\" INNER JOIN Match AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_007\" WHERE \"r0\".\"XCL_002\" = 'Poland' AND \"r1\".\"XCL_009\" = '2010/2011'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1057"
  ]
}
```

### Player Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_145\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_145\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" ORDER BY t1.\"XCL_125\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1090"
  ]
}
```

### Average Attribute Difference (Diallo vs Appindangoye)

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN \"Player\".\"XCL_123\" = 'Abdou Diallo' THEN \"Player_Attributes\".\"XCL_146\" ELSE 0 END) AS REAL) / COUNT(CASE WHEN \"Player\".\"XCL_123\" = 'Abdou Diallo' THEN \"Player_Attributes\".\"XCL_128\" ELSE NULL END) - CAST(SUM(CASE WHEN \"Player\".\"XCL_123\" = 'Aaron Appindangoye' THEN \"Player_Attributes\".\"XCL_146\" ELSE 0 END) AS REAL) / COUNT(CASE WHEN \"Player\".\"XCL_123\" = 'Aaron Appindangoye' THEN \"Player_Attributes\".\"XCL_128\" ELSE NULL END)",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN t1.\"XCL_123\" = 'Abdou Diallo' THEN t2.\"XCL_146\" ELSE 0 END) AS REAL) / COUNT(CASE WHEN t1.\"XCL_123\" = 'Abdou Diallo' THEN t2.\"XCL_128\" ELSE NULL END) - CAST(SUM(CASE WHEN t1.\"XCL_123\" = 'Aaron Appindangoye' THEN t2.\"XCL_146\" ELSE 0 END) AS REAL) / COUNT(CASE WHEN t1.\"XCL_123\" = 'Aaron Appindangoye' THEN t2.\"XCL_128\" ELSE NULL END) FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(CASE WHEN \"r0\".\"XCL_123\" = 'Abdou Diallo' THEN \"r1\".\"XCL_146\" ELSE 0 END) AS REAL) / COUNT(CASE WHEN \"r0\".\"XCL_123\" = 'Abdou Diallo' THEN \"r1\".\"XCL_128\" ELSE NULL END) - CAST(SUM(CASE WHEN \"r0\".\"XCL_123\" = 'Aaron Appindangoye' THEN \"r1\".\"XCL_146\" ELSE 0 END) AS REAL) / COUNT(CASE WHEN \"r0\".\"XCL_123\" = 'Aaron Appindangoye' THEN \"r1\".\"XCL_128\" ELSE NULL END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(CASE WHEN \"r0\".\"XCL_123\" = 'Abdou Diallo' THEN \"r1\".\"XCL_146\" ELSE 0 END) AS REAL) / COUNT(CASE WHEN \"r0\".\"XCL_123\" = 'Abdou Diallo' THEN \"r1\".\"XCL_128\" ELSE NULL END) - CAST(SUM(CASE WHEN \"r0\".\"XCL_123\" = 'Aaron Appindangoye' THEN \"r1\".\"XCL_146\" ELSE 0 END) AS REAL) / COUNT(CASE WHEN \"r0\".\"XCL_123\" = 'Aaron Appindangoye' THEN \"r1\".\"XCL_128\" ELSE NULL END) AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1076"
  ]
}
```

### "Player"."XCL_123" = 'Alexis Blin'

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_123\" = 'Alexis Blin'",
  "grain": [],
  "population_scope": "SELECT \"XCL_122\" FROM Player WHERE \"XCL_123\" = 'Alexis Blin'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1140"
  ]
}
```

### Calculates the percentage difference of the sum of Player_Attributes.XCL_132 for player 'Ariel Borysiuk' relative to player 'Paulin Puel'. The formula

```json
{
  "kind": "metric",
  "formula": "(SUM(CASE WHEN \"Player\".\"XCL_123\" = 'Ariel Borysiuk' THEN \"Player_Attributes\".\"XCL_132\" ELSE 0 END) * 1.0 - SUM(CASE WHEN \"Player\".\"XCL_123\" = 'Paulin Puel' THEN \"Player_Attributes\".\"XCL_132\" ELSE 0 END)) * 100 / SUM(CASE WHEN \"Player\".\"XCL_123\" = 'Paulin Puel' THEN \"Player_Attributes\".\"XCL_132\" ELSE 0 END)",
  "grain": [],
  "population_scope": "SELECT (SUM(CASE WHEN t1.\"XCL_123\" = 'Ariel Borysiuk' THEN t2.\"XCL_132\" ELSE 0 END) * 1.0 - SUM(CASE WHEN t1.\"XCL_123\" = 'Paulin Puel' THEN t2.\"XCL_132\" ELSE 0 END)) * 100 / SUM(CASE WHEN t1.\"XCL_123\" = 'Paulin Puel' THEN t2.\"XCL_132\" ELSE 0 END) FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "(SUM(CASE WHEN \"r0\".\"XCL_123\" = 'Ariel Borysiuk' THEN \"r1\".\"XCL_132\" ELSE 0 END) * 1.0 - SUM(CASE WHEN \"r0\".\"XCL_123\" = 'Paulin Puel' THEN \"r1\".\"XCL_132\" ELSE 0 END)) * 100 / SUM(CASE WHEN \"r0\".\"XCL_123\" = 'Paulin Puel' THEN \"r1\".\"XCL_132\" ELSE 0 END)",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT (SUM(CASE WHEN \"r0\".\"XCL_123\" = 'Ariel Borysiuk' THEN \"r1\".\"XCL_132\" ELSE 0 END) * 1.0 - SUM(CASE WHEN \"r0\".\"XCL_123\" = 'Paulin Puel' THEN \"r1\".\"XCL_132\" ELSE 0 END)) * 100 / SUM(CASE WHEN \"r0\".\"XCL_123\" = 'Paulin Puel' THEN \"r1\".\"XCL_132\" ELSE 0 END) AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1094"
  ]
}
```

### Average XCL_179 per XCL_175 record

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"Team_Attributes\".\"XCL_179\") AS REAL) / COUNT(\"Team_Attributes\".\"XCL_175\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(t2.\"XCL_179\") AS REAL) / COUNT(t2.\"XCL_175\") FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'Heart of Midlothian'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(\"r1\".\"XCL_179\") AS REAL) / COUNT(\"r1\".\"XCL_175\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Team"
      },
      {
        "role": "r1",
        "physical_table": "Team_Attributes"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(\"r1\".\"XCL_179\") AS REAL) / COUNT(\"r1\".\"XCL_175\") AS \"value\" FROM Team AS \"r0\" INNER JOIN Team_Attributes AS \"r1\" ON \"r0\".\"XCL_171\" = \"r1\".\"XCL_177\" WHERE \"r0\".\"XCL_173\" = 'Heart of Midlothian'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1095"
  ]
}
```

### Team Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"Team_Attributes\".\"XCL_189\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_189\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'Hull City' AND SUBSTRING(t2.\"XCL_178\", 1, 10) = '2010-02-22'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_189\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Team"
      },
      {
        "role": "r1",
        "physical_table": "Team_Attributes"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_189\" AS \"value\" FROM Team AS \"r0\" INNER JOIN Team_Attributes AS \"r1\" ON \"r0\".\"XCL_171\" = \"r1\".\"XCL_177\" WHERE \"r0\".\"XCL_173\" = 'Hull City' AND SUBSTRING(\"r1\".\"XCL_178\", 1, 10) = '2010-02-22'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1112"
  ]
}
```

### Average Team_Attributes XCL_183 for 2012

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(\"Team_Attributes\".\"XCL_183\") AS REAL) / COUNT(\"Team\".\"XCL_170\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(t2.\"XCL_183\") AS REAL) / COUNT(t1.\"XCL_170\") FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE STRFTIME('%Y', t2.\"XCL_178\") = '2012'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(\"r1\".\"XCL_183\") AS REAL) / COUNT(\"r0\".\"XCL_170\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Team"
      },
      {
        "role": "r1",
        "physical_table": "Team_Attributes"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(\"r1\".\"XCL_183\") AS REAL) / COUNT(\"r0\".\"XCL_170\") AS \"value\" FROM Team AS \"r0\" INNER JOIN Team_Attributes AS \"r1\" ON \"r0\".\"XCL_171\" = \"r1\".\"XCL_177\" WHERE STRFTIME('%Y', \"r1\".\"XCL_178\") = '2012'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1036"
  ]
}
```

### Player XCL_123

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_123\" FROM Player WHERE \"XCL_126\" > 180",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_123\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_123\" AS \"value\" FROM Player AS \"r0\" WHERE \"r0\".\"XCL_126\" > 180",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1059"
  ]
}
```

### "Country"."XCL_002" = 'Germany'

```json
{
  "kind": "predicate",
  "formula": "\"Country\".\"XCL_002\" = 'Germany'",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_005\" FROM Country AS t1 INNER JOIN League AS t2 ON t1.\"XCL_001\" = t2.\"XCL_004\" WHERE t1.\"XCL_002\" = 'Germany'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1082"
  ]
}
```

### Count of Left-Footed Players (Latest Snapshot)

```json
{
  "kind": "metric",
  "formula": "COUNT(\"Player_Attributes\".\"XCL_128\")",
  "grain": [],
  "population_scope": "SELECT COUNT(t1.\"XCL_128\") FROM Player_Attributes AS t1 WHERE t1.\"XCL_134\" = 'left' AND t1.\"XCL_137\" = (SELECT MAX(\"XCL_137\") FROM Player_Attributes)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1136"
  ]
}
```

### Attribute XCL_149

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_149\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_148\", \"XCL_149\", \"XCL_147\" FROM Player_Attributes WHERE \"XCL_130\" IN (SELECT \"XCL_122\" FROM Player WHERE \"XCL_123\" = 'Alexis Blin')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1140"
  ]
}
```

### Latest Attribute Timestamp

```json
{
  "kind": "metric",
  "formula": "MAX(\"Player_Attributes\".\"XCL_133\")",
  "grain": [],
  "population_scope": "SELECT MAX(\"XCL_133\") FROM Player_Attributes",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MAX(\"r0\".\"XCL_133\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT MAX(\"r0\".\"XCL_133\") AS \"value\" FROM Player_Attributes AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1051"
  ]
}
```

### "Match"."XCL_009" = '2009/2010'

```json
{
  "kind": "predicate",
  "formula": "\"Match\".\"XCL_009\" = '2009/2010'",
  "grain": [
    "\"League\".\"XCL_005\""
  ],
  "population_scope": "SELECT t1.\"XCL_005\" FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t2.\"XCL_009\" = '2009/2010' GROUP BY t1.\"XCL_005\" HAVING (CAST(SUM(t2.\"XCL_015\") AS REAL) / COUNT(DISTINCT t2.\"XCL_006\")) - (CAST(SUM(t2.\"XCL_016\") AS REAL) / COUNT(DISTINCT t2.\"XCL_006\")) > 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1042"
  ]
}
```

### Team Attack Rating

```json
{
  "kind": "binding",
  "formula": "\"Team_Attributes\".\"XCL_182\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_182\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_174\" = 'LEI' AND SUBSTRING(t2.\"XCL_178\", 1, 10) = '2015-09-10'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_182\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Team"
      },
      {
        "role": "r1",
        "physical_table": "Team_Attributes"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_182\" AS \"value\" FROM Team AS \"r0\" INNER JOIN Team_Attributes AS \"r1\" ON \"r0\".\"XCL_171\" = \"r1\".\"XCL_177\" WHERE \"r0\".\"XCL_174\" = 'LEI' AND SUBSTRING(\"r1\".\"XCL_178\", 1, 10) = '2015-09-10'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1109"
  ]
}
```

### "Country"."XCL_002" = 'Netherlands'

```json
{
  "kind": "predicate",
  "formula": "\"Country\".\"XCL_002\" = 'Netherlands'",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_005\" FROM Country AS t1 INNER JOIN League AS t2 ON t1.\"XCL_001\" = t2.\"XCL_004\" WHERE t1.\"XCL_002\" = 'Netherlands'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1056"
  ]
}
```

### Aggregated sum of the 'XCL_015' column from the 'match' table, filtered to matches associated with the player named 'Aaron Lennon' (identified by 'XCL

```json
{
  "kind": "metric",
  "formula": "SUM(\"match\".\"XCL_015\")",
  "grain": [],
  "population_scope": "SELECT SUM(t2.\"XCL_015\") FROM Player AS t1 INNER JOIN match AS t2 ON t1.\"XCL_122\" = t2.\"XCL_080\" WHERE t1.\"XCL_123\" = 'Aaron Lennon'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r1\".\"XCL_015\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "match"
      }
    ],
    "scope_sql": "SELECT SUM(\"r1\".\"XCL_015\") AS \"value\" FROM Player AS \"r0\" INNER JOIN match AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_080\" WHERE \"r0\".\"XCL_123\" = 'Aaron Lennon'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1119"
  ]
}
```

### Attribute XCL_148

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_148\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_148\", \"XCL_149\", \"XCL_147\" FROM Player_Attributes WHERE \"XCL_130\" IN (SELECT \"XCL_122\" FROM Player WHERE \"XCL_123\" = 'Alexis Blin')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1140"
  ]
}
```

### Match Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"Match\".\"XCL_006\")",
  "grain": [],
  "population_scope": "SELECT COUNT(t2.\"XCL_006\") FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t1.\"XCL_005\" = 'Belgium Jupiler League' AND SUBSTRING(t2.\"XCL_011\", 1, 7) = '2009-04'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r1\".\"XCL_006\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "League"
      },
      {
        "role": "r1",
        "physical_table": "Match"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r1\".\"XCL_006\") AS \"value\" FROM League AS \"r0\" INNER JOIN Match AS \"r1\" ON \"r0\".\"XCL_003\" = \"r1\".\"XCL_008\" WHERE \"r0\".\"XCL_005\" = 'Belgium Jupiler League' AND SUBSTRING(\"r1\".\"XCL_011\", 1, 7) = '2009-04'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1091"
  ]
}
```

### Player Identifier

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_123\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t2.\"XCL_138\" = 1 ORDER BY t1.\"XCL_125\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1125"
  ]
}
```

### "Team_Attributes"."XCL_180" = 'Fast'

```json
{
  "kind": "predicate",
  "formula": "\"Team_Attributes\".\"XCL_180\" = 'Fast'",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_173\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_180\" = 'Fast'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1065"
  ]
}
```

### Player Cross Passes Attribute

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_139\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_139\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Ariel Borysiuk'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_139\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_139\" AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\" WHERE \"r0\".\"XCL_123\" = 'Ariel Borysiuk'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1086"
  ]
}
```

### "Team"."XCL_173" = 'KSV Cercle Brugge'

```json
{
  "kind": "predicate",
  "formula": "\"Team\".\"XCL_173\" = 'KSV Cercle Brugge'",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_180\" FROM Team_Attributes AS t1 INNER JOIN Team AS t2 ON t1.\"XCL_177\" = t2.\"XCL_171\" WHERE t2.\"XCL_173\" = 'KSV Cercle Brugge'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1141"
  ]
}
```

### League Identifier

```json
{
  "kind": "binding",
  "formula": "\"League\".\"XCL_005\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_005\" FROM Country AS t1 INNER JOIN League AS t2 ON t1.\"XCL_001\" = t2.\"XCL_004\" WHERE t1.\"XCL_002\" = 'Germany'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_005\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Country"
      },
      {
        "role": "r1",
        "physical_table": "League"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_005\" AS \"value\" FROM Country AS \"r0\" INNER JOIN League AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_004\" WHERE \"r0\".\"XCL_002\" = 'Germany'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1082"
  ]
}
```

### "Player"."XCL_123" = 'Kevin Constant'

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_123\" = 'Kevin Constant'",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_137\", t2.\"XCL_131\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_124\" = t2.\"XCL_129\" WHERE t1.\"XCL_123\" = 'Kevin Constant' ORDER BY t2.\"XCL_137\" DESC",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1107"
  ]
}
```

### Team Identifier

```json
{
  "kind": "binding",
  "formula": "\"Team\".\"XCL_173\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_173\" FROM Match AS t1 INNER JOIN Team AS t2 ON t1.\"XCL_014\" = t2.\"XCL_171\" ORDER BY t1.\"XCL_016\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1146"
  ]
}
```

### Distinct values of the Team identifier column (XCL_173) for teams whose associated attributes indicate a 'Slow' pace (XCL_180). The grain is unique te

```json
{
  "kind": "binding",
  "formula": "\"Team\".\"XCL_173\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_173\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_180\" = 'Slow'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1129"
  ]
}
```

### Team Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"Team_Attributes\".\"XCL_191\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_191\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'Hannover 96' AND t2.\"XCL_178\" LIKE '2015-09-10%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_191\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Team"
      },
      {
        "role": "r1",
        "physical_table": "Team_Attributes"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_191\" AS \"value\" FROM Team AS \"r0\" INNER JOIN Team_Attributes AS \"r1\" ON \"r0\".\"XCL_171\" = \"r1\".\"XCL_177\" WHERE \"r0\".\"XCL_173\" = 'Hannover 96' AND \"r1\".\"XCL_178\" LIKE '2015-09-10%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1113"
  ]
}
```

### Max XCL_132 for Dorlan Pabon

```json
{
  "kind": "metric",
  "formula": "MAX(\"Player_Attributes\".\"XCL_132\")",
  "grain": [],
  "population_scope": "SELECT MAX(t2.\"XCL_132\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Dorlan Pabon'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MAX(\"r1\".\"XCL_132\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT MAX(\"r1\".\"XCL_132\") AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\" WHERE \"r0\".\"XCL_123\" = 'Dorlan Pabon'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1100"
  ]
}
```

### Attribute Timestamp

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_137\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_137\", t2.\"XCL_131\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_124\" = t2.\"XCL_129\" WHERE t1.\"XCL_123\" = 'Kevin Constant' ORDER BY t2.\"XCL_137\" DESC",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_137\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_137\" AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_124\" = \"r1\".\"XCL_129\" WHERE \"r0\".\"XCL_123\" = 'Kevin Constant'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1107"
  ]
}
```

### "Player"."XCL_123" = 'Abdou Diallo'

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_123\" = 'Abdou Diallo'",
  "grain": [],
  "population_scope": "SELECT DISTINCT t2.\"XCL_134\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Abdou Diallo'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1099"
  ]
}
```

### "League"."XCL_005" = 'Belgium Jupiler League'

```json
{
  "kind": "predicate",
  "formula": "\"League\".\"XCL_005\" = 'Belgium Jupiler League'",
  "grain": [],
  "population_scope": "SELECT t1.\"XCL_002\" FROM Country AS t1 INNER JOIN League AS t2 ON t1.\"XCL_001\" = t2.\"XCL_004\" WHERE t2.\"XCL_005\" = 'Belgium Jupiler League'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1081"
  ]
}
```

### The identifier (XCL_122) of the single player ranked first by the descending order of XCL_127 in the Player table. Used as a filter key to join with P

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_122\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_122\" FROM Player ORDER BY \"XCL_127\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1144"
  ]
}
```

### "Country"."XCL_002" = 'Poland' AND "Match"."XCL_009" = '2010/2011'

```json
{
  "kind": "predicate",
  "formula": "\"Country\".\"XCL_002\" = 'Poland' AND \"Match\".\"XCL_009\" = '2010/2011'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(t2.\"XCL_015\") AS REAL) / COUNT(t2.\"XCL_006\") FROM Country AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_001\" = t2.\"XCL_007\" WHERE t1.\"XCL_002\" = 'Poland' AND t2.\"XCL_009\" = '2010/2011'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1057"
  ]
}
```

### Match Attribute XCL_015

```json
{
  "kind": "binding",
  "formula": "\"Match\".\"XCL_015\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_015\", t2.\"XCL_016\" FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t1.\"XCL_005\" = 'Belgium Jupiler League' AND t2.\"XCL_011\" LIKE '2008-09-24%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_015\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "League"
      },
      {
        "role": "r1",
        "physical_table": "Match"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_015\" AS \"value\" FROM League AS \"r0\" INNER JOIN Match AS \"r1\" ON \"r0\".\"XCL_003\" = \"r1\".\"XCL_008\" WHERE \"r0\".\"XCL_005\" = 'Belgium Jupiler League' AND \"r1\".\"XCL_011\" LIKE '2008-09-24%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1139"
  ]
}
```

### Player Identifier

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_123\" FROM Player WHERE SUBSTRING(\"XCL_125\", 1, 7) = '1970-10'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_123\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_123\" AS \"value\" FROM Player AS \"r0\" WHERE SUBSTRING(\"r0\".\"XCL_125\", 1, 7) = '1970-10'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1044"
  ]
}
```

### "Player"."XCL_126" > 180

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_126\" > 180",
  "grain": [],
  "population_scope": "SELECT \"XCL_123\" FROM Player WHERE \"XCL_126\" > 180 ORDER BY \"XCL_123\" LIMIT 3",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1132"
  ]
}
```

### Attribute value from Team_Attributes used for descending sort and output; represents the metric determining the latest or highest-ranked record for th

```json
{
  "kind": "binding",
  "formula": "\"Team_Attributes\".\"XCL_186\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_186\", t2.\"XCL_187\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'Ajax' ORDER BY t2.\"XCL_186\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1098"
  ]
}
```

### "Team"."XCL_174" = 'CLB'

```json
{
  "kind": "predicate",
  "formula": "\"Team\".\"XCL_174\" = 'CLB'",
  "grain": [],
  "population_scope": "SELECT DISTINCT t2.\"XCL_184\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_174\" = 'CLB'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1066"
  ]
}
```

### Aggregates the total number of rows in the Player_Attributes table that satisfy the specified filter conditions. The grain is a single scalar value re

```json
{
  "kind": "metric",
  "formula": "COUNT(\"Player_Attributes\".\"XCL_130\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_130\") FROM Player_Attributes WHERE \"XCL_134\" = 'left' AND \"XCL_135\" = 'low'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_130\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_130\") AS \"value\" FROM Player_Attributes AS \"r0\" WHERE \"r0\".\"XCL_134\" = 'left' AND \"r0\".\"XCL_135\" = 'low'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1080"
  ]
}
```

### Subquery League Identifier

```json
{
  "kind": "binding",
  "formula": "\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_008\", MAX(\"cnt\") AS max_count FROM (SELECT \"XCL_008\", COUNT(\"XCL_006\") AS cnt FROM Match GROUP BY \"XCL_008\") AS subquery",
  "upstream_scopes": [
    "SELECT \"XCL_008\", COUNT(\"XCL_006\") AS cnt FROM Match GROUP BY \"XCL_008\""
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1032"
  ]
}
```

### "League"."XCL_005" = 'Scotland Premier League' AND "Match"."XCL_009" = '2009/2010' AND "Match"."XCL_016" - "Match"."XCL_015" > 0

```json
{
  "kind": "predicate",
  "formula": "\"League\".\"XCL_005\" = 'Scotland Premier League' AND \"Match\".\"XCL_009\" = '2009/2010' AND \"Match\".\"XCL_016\" - \"Match\".\"XCL_015\" > 0",
  "grain": [
    "\"Match\".\"XCL_014\""
  ],
  "population_scope": "SELECT teamInfo.\"XCL_173\" FROM League AS leagueData INNER JOIN Match AS matchData ON leagueData.\"XCL_003\" = matchData.\"XCL_008\" INNER JOIN Team AS teamInfo ON matchData.\"XCL_014\" = teamInfo.\"XCL_171\" WHERE leagueData.\"XCL_005\" = 'Scotland Premier League' AND matchData.\"XCL_009\" = '2009/2010' AND matchData.\"XCL_016\" - matchData.\"XCL_015\" > 0 GROUP BY matchData.\"XCL_014\" ORDER BY COUNT(*) DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1028"
  ]
}
```

### "Team"."XCL_173" = 'Heart of Midlothian'

```json
{
  "kind": "predicate",
  "formula": "\"Team\".\"XCL_173\" = 'Heart of Midlothian'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(t2.\"XCL_179\") AS REAL) / COUNT(t2.\"XCL_175\") FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'Heart of Midlothian'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1095"
  ]
}
```

### SUBSTRING("Player"."XCL_125", 1, 7) = '1970-10'

```json
{
  "kind": "predicate",
  "formula": "SUBSTRING(\"Player\".\"XCL_125\", 1, 7) = '1970-10'",
  "grain": [],
  "population_scope": "SELECT \"XCL_123\" FROM Player WHERE SUBSTRING(\"XCL_125\", 1, 7) = '1970-10'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1044"
  ]
}
```

### Distinct XCL_176

```json
{
  "kind": "binding",
  "formula": "\"Team_Attributes\".\"XCL_176\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT \"XCL_176\" FROM Team_Attributes WHERE \"XCL_179\" > 50 AND \"XCL_179\" < 60",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1035"
  ]
}
```

### SUBSTRING("Player_Attributes"."XCL_131", 1, 10) = '2013-07-12'

```json
{
  "kind": "predicate",
  "formula": "SUBSTRING(\"Player_Attributes\".\"XCL_131\", 1, 10) = '2013-07-12'",
  "grain": [],
  "population_scope": "SELECT (SUM(CASE WHEN t1.\"XCL_123\" = 'Landon Donovan' THEN t2.\"XCL_132\" ELSE 0 END) * 1.0 - SUM(CASE WHEN t1.\"XCL_123\" = 'Jordan Bowery' THEN t2.\"XCL_132\" ELSE 0 END)) * 100 / SUM(CASE WHEN t1.\"XCL_123\" = 'Landon Donovan' THEN t2.\"XCL_132\" ELSE 0 END) AS LvsJ_percent FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_124\" = t2.\"XCL_129\" WHERE SUBSTRING(t2.\"XCL_131\", 1, 10) = '2013-07-12'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1115"
  ]
}
```

### "Team_Attributes"."XCL_180" = 'Slow'

```json
{
  "kind": "predicate",
  "formula": "\"Team_Attributes\".\"XCL_180\" = 'Slow'",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_173\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_180\" = 'Slow'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1129"
  ]
}
```

### Count of unique values in Player.XCL_123 for players born before 1986 (based on XCL_125) who have a 'high' attribute in Player_Attributes.XCL_136.

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"Player\".\"XCL_123\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT t1.\"XCL_123\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE STRFTIME('%Y', t1.\"XCL_125\") < '1986' AND t2.\"XCL_136\" = 'high'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_123\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r0\".\"XCL_123\") AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\" WHERE STRFTIME('%Y', \"r0\".\"XCL_125\") < '1986' AND \"r1\".\"XCL_136\" = 'high'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1084"
  ]
}
```

### Aggregated sum of the 'XCL_016' column from the 'match' table. The population is restricted to matches associated with players named 'Daan Smith' or '

```json
{
  "kind": "metric",
  "formula": "SUM(\"match\".\"XCL_016\")",
  "grain": [],
  "population_scope": "SELECT SUM(t2.\"XCL_016\") FROM Player AS t1 INNER JOIN match AS t2 ON t1.\"XCL_122\" = t2.\"XCL_076\" WHERE t1.\"XCL_123\" IN ('Daan Smith', 'Filipe Ferreira')",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r1\".\"XCL_016\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "match"
      }
    ],
    "scope_sql": "SELECT SUM(\"r1\".\"XCL_016\") AS \"value\" FROM Player AS \"r0\" INNER JOIN match AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_076\" WHERE \"r0\".\"XCL_123\" IN ('Daan Smith', 'Filipe Ferreira')",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1120"
  ]
}
```

### "Match"."XCL_009" = '2015/2016'

```json
{
  "kind": "predicate",
  "formula": "\"Match\".\"XCL_009\" = '2015/2016'",
  "grain": [
    "\"League\".\"XCL_005\""
  ],
  "population_scope": "SELECT t2.\"XCL_005\" FROM Match AS t1 INNER JOIN League AS t2 ON t1.\"XCL_008\" = t2.\"XCL_003\" WHERE t1.\"XCL_009\" = '2015/2016' GROUP BY t2.\"XCL_005\" ORDER BY SUM(t1.\"XCL_015\" + t1.\"XCL_016\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1025"
  ]
}
```

### Crossing Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_132\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_132\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Gabriel Tamas' AND STRFTIME('%Y', t2.\"XCL_131\") = '2011'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_132\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_132\" AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\" WHERE \"r0\".\"XCL_123\" = 'Gabriel Tamas' AND STRFTIME('%Y', \"r1\".\"XCL_131\") = '2011'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1048"
  ]
}
```

### "Player"."XCL_123" IN ('Aaron Lennon', 'Abdelaziz Barrada')

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_123\" IN ('Aaron Lennon', 'Abdelaziz Barrada')",
  "grain": [],
  "population_scope": "SELECT \"XCL_123\" FROM Player WHERE \"XCL_123\" IN ('Aaron Lennon', 'Abdelaziz Barrada') ORDER BY \"XCL_125\" ASC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1078"
  ]
}
```

### SUBSTRING("Player"."XCL_125", 1, 4) < '1986'

```json
{
  "kind": "predicate",
  "formula": "SUBSTRING(\"Player\".\"XCL_125\", 1, 4) < '1986'",
  "grain": [],
  "population_scope": "SELECT SUM(t2.\"XCL_132\") / COUNT(t1.\"XCL_121\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE SUBSTRING(t1.\"XCL_125\", 1, 4) < '1986'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1093"
  ]
}
```

### Distinct Team Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"Team_Attributes\".\"XCL_184\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t2.\"XCL_184\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_174\" = 'CLB'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1066"
  ]
}
```

### League Identifier

```json
{
  "kind": "binding",
  "formula": "\"League\".\"XCL_005\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_005\" FROM Country AS t1 INNER JOIN League AS t2 ON t1.\"XCL_001\" = t2.\"XCL_004\" WHERE t1.\"XCL_002\" = 'Netherlands'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_005\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Country"
      },
      {
        "role": "r1",
        "physical_table": "League"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_005\" AS \"value\" FROM Country AS \"r0\" INNER JOIN League AS \"r1\" ON \"r0\".\"XCL_001\" = \"r1\".\"XCL_004\" WHERE \"r0\".\"XCL_002\" = 'Netherlands'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1056"
  ]
}
```

### Final Maximum Match Count

```json
{
  "kind": "metric",
  "formula": "t1.\"max_count\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_005\", t1.\"max_count\" FROM League AS t2 JOIN (SELECT \"XCL_008\", MAX(\"cnt\") AS max_count FROM (SELECT \"XCL_008\", COUNT(\"XCL_006\") AS cnt FROM Match GROUP BY \"XCL_008\") AS subquery) AS t1 ON t1.\"XCL_008\" = t2.\"XCL_003\"",
  "upstream_scopes": [
    "SELECT \"XCL_008\", COUNT(\"XCL_006\") AS cnt FROM Match GROUP BY \"XCL_008\"",
    "SELECT \"XCL_008\", MAX(\"cnt\") AS max_count FROM (SELECT \"XCL_008\", COUNT(\"XCL_006\") AS cnt FROM Match GROUP BY \"XCL_008\") AS subquery"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1032"
  ]
}
```

### Match Attribute XCL_016

```json
{
  "kind": "binding",
  "formula": "\"Match\".\"XCL_016\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_015\", t2.\"XCL_016\" FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t1.\"XCL_005\" = 'Belgium Jupiler League' AND t2.\"XCL_011\" LIKE '2008-09-24%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_016\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "League"
      },
      {
        "role": "r1",
        "physical_table": "Match"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_016\" AS \"value\" FROM League AS \"r0\" INNER JOIN Match AS \"r1\" ON \"r0\".\"XCL_003\" = \"r1\".\"XCL_008\" WHERE \"r0\".\"XCL_005\" = 'Belgium Jupiler League' AND \"r1\".\"XCL_011\" LIKE '2008-09-24%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1139"
  ]
}
```

### Distinct values of the Team identifier column (XCL_174) for teams that have at least one attribute record with the value 'Risky' in column XCL_187.

```json
{
  "kind": "binding",
  "formula": "\"Team\".\"XCL_174\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t1.\"XCL_174\" FROM Team AS t1 INNER JOIN Team_attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_187\" = 'Risky'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1053"
  ]
}
```

### Country Name

```json
{
  "kind": "binding",
  "formula": "\"Country\".\"XCL_002\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t4.\"XCL_002\" FROM Player_Attributes AS t1 INNER JOIN Player AS t2 ON t1.\"XCL_130\" = t2.\"XCL_122\" INNER JOIN Match AS t3 ON t2.\"XCL_122\" = t3.\"XCL_068\" INNER JOIN Country AS t4 ON t3.\"XCL_007\" = t4.\"XCL_001\" WHERE t1.\"XCL_160\" > 89",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1127"
  ]
}
```

### Attribute XCL_147

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_147\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_148\", \"XCL_149\", \"XCL_147\" FROM Player_Attributes WHERE \"XCL_130\" IN (SELECT \"XCL_122\" FROM Player WHERE \"XCL_123\" = 'Alexis Blin')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1140"
  ]
}
```

### "Player"."XCL_123" IN ('Daan Smith', 'Filipe Ferreira')

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_123\" IN ('Daan Smith', 'Filipe Ferreira')",
  "grain": [],
  "population_scope": "SELECT SUM(t2.\"XCL_016\") FROM Player AS t1 INNER JOIN match AS t2 ON t1.\"XCL_122\" = t2.\"XCL_076\" WHERE t1.\"XCL_123\" IN ('Daan Smith', 'Filipe Ferreira')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1120"
  ]
}
```

### Numeric or comparable column XCL_126 from the Player table, used as the basis for ranking players in descending order.

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_126\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_123\", \"XCL_126\", DENSE_RANK() OVER (ORDER BY \"XCL_126\" DESC) AS rank FROM Player",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_126\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_126\" AS \"value\" FROM Player AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1116"
  ]
}
```

### "Match"."XCL_015" = 10

```json
{
  "kind": "predicate",
  "formula": "\"Match\".\"XCL_015\" = 10",
  "grain": [],
  "population_scope": "SELECT t1.\"XCL_174\" FROM Team AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_171\" = t2.\"XCL_013\" WHERE t2.\"XCL_015\" = 10",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1074"
  ]
}
```

### Max Match XCL_015 for Netherlands Eredivisie

```json
{
  "kind": "metric",
  "formula": "MAX(\"Match\".\"XCL_015\")",
  "grain": [],
  "population_scope": "SELECT MAX(t2.\"XCL_015\") FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t1.\"XCL_005\" = 'Netherlands Eredivisie'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MAX(\"r1\".\"XCL_015\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "League"
      },
      {
        "role": "r1",
        "physical_table": "Match"
      }
    ],
    "scope_sql": "SELECT MAX(\"r1\".\"XCL_015\") AS \"value\" FROM League AS \"r0\" INNER JOIN Match AS \"r1\" ON \"r0\".\"XCL_003\" = \"r1\".\"XCL_008\" WHERE \"r0\".\"XCL_005\" = 'Netherlands Eredivisie'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1143"
  ]
}
```

### Player Name

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT t1.\"XCL_123\", t2.\"XCL_137\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" IN ('Alexis', 'Ariel Borysiuk', 'Arouna Kone') ORDER BY t2.\"XCL_137\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1085"
  ]
}
```

### STRFTIME('%Y', "Team_Attributes"."XCL_178") = '2012'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"Team_Attributes\".\"XCL_178\") = '2012'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(t2.\"XCL_183\") AS REAL) / COUNT(t1.\"XCL_170\") FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE STRFTIME('%Y', t2.\"XCL_178\") = '2012'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1036"
  ]
}
```

### "Match"."XCL_009" = '2015/2016'

```json
{
  "kind": "predicate",
  "formula": "\"Match\".\"XCL_009\" = '2015/2016'",
  "grain": [
    "\"League\".\"XCL_005\""
  ],
  "population_scope": "SELECT t1.\"XCL_005\" FROM League AS t1 INNER JOIN Match AS t2 ON t1.\"XCL_003\" = t2.\"XCL_008\" WHERE t2.\"XCL_009\" = '2015/2016' GROUP BY t1.\"XCL_005\" ORDER BY COUNT(t2.\"XCL_006\") DESC LIMIT 4",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1145"
  ]
}
```

### "Player"."XCL_123" = 'Aaron Doran'

```json
{
  "kind": "predicate",
  "formula": "\"Player\".\"XCL_123\" = 'Aaron Doran'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(t2.\"XCL_132\") AS REAL) / COUNT(t2.\"XCL_128\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Aaron Doran'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1072"
  ]
}
```

### Counts the number of unique players (identified by XCL_121) who have at least one attribute record where XCL_141 exceeds 70, restricted to players whe

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"Player\".\"XCL_121\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT t1.\"XCL_121\") FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_126\" > 180 AND t2.\"XCL_141\" > 70",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_121\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      },
      {
        "role": "r1",
        "physical_table": "Player_Attributes"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r0\".\"XCL_121\") AS \"value\" FROM Player AS \"r0\" INNER JOIN Player_Attributes AS \"r1\" ON \"r0\".\"XCL_122\" = \"r1\".\"XCL_130\" WHERE \"r0\".\"XCL_126\" > 180 AND \"r1\".\"XCL_141\" > 70",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1087"
  ]
}
```

### The name of the team (Team.XCL_173) that recorded the highest number of wins in the Scotland Premier League during the 2009/2010 season. A win is defi

```json
{
  "kind": "binding",
  "formula": "\"Team\".\"XCL_173\"",
  "grain": [
    "\"Match\".\"XCL_014\""
  ],
  "population_scope": "SELECT teamInfo.\"XCL_173\" FROM League AS leagueData INNER JOIN Match AS matchData ON leagueData.\"XCL_003\" = matchData.\"XCL_008\" INNER JOIN Team AS teamInfo ON matchData.\"XCL_014\" = teamInfo.\"XCL_171\" WHERE leagueData.\"XCL_005\" = 'Scotland Premier League' AND matchData.\"XCL_009\" = '2009/2010' AND matchData.\"XCL_016\" - matchData.\"XCL_015\" > 0 GROUP BY matchData.\"XCL_014\" ORDER BY COUNT(*) DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1028"
  ]
}
```

### The value of column XCL_130 for the single record in Player_Attributes with the highest XCL_132 value, restricted to rows where the first four charact

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_130\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_130\" FROM Player_Attributes WHERE SUBSTRING(\"XCL_131\", 1, 4) = '2010' ORDER BY \"XCL_132\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1034"
  ]
}
```

### "Match"."XCL_009" = '2008/2009'

```json
{
  "kind": "predicate",
  "formula": "\"Match\".\"XCL_009\" = '2008/2009'",
  "grain": [
    "\"Match\".\"XCL_008\""
  ],
  "population_scope": "SELECT COUNT(t2.\"XCL_006\") AS match_count FROM Match AS t2 WHERE t2.\"XCL_009\" = '2008/2009' GROUP BY t2.\"XCL_008\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1092"
  ]
}
```

### Team Identifier (XCL_173)

```json
{
  "kind": "binding",
  "formula": "\"Team\".\"XCL_173\"",
  "grain": [],
  "population_scope": "SELECT t3.\"XCL_173\" FROM Team AS t3 INNER JOIN Team_Attributes AS t4 ON t3.\"XCL_171\" = t4.\"XCL_177\" WHERE t4.\"XCL_182\" = 'Normal' AND t4.\"XCL_186\" < (SELECT CAST(SUM(t2.\"XCL_186\") AS REAL) / COUNT(t1.\"XCL_170\") FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t2.\"XCL_182\" = 'Normal' AND SUBSTRING(t2.\"XCL_178\", 1, 4) = '2014') ORDER BY t4.\"XCL_186\" DESC",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1041"
  ]
}
```

### Distinct values of the attribute column XCL_135 from the Player_Attributes table, filtered to records associated with the player named 'Franco Zennaro

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_135\"",
  "grain": [],
  "population_scope": "SELECT DISTINCT t2.\"XCL_135\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" WHERE t1.\"XCL_123\" = 'Franco Zennaro'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1045"
  ]
}
```

### A

```json
{
  "kind": "binding",
  "formula": "'Min'",
  "grain": [],
  "population_scope": "SELECT AVG(\"XCL_138\") AS result, 'Min' AS A FROM Player AS T1 INNER JOIN Player_Attributes AS T2 ON T1.\"XCL_122\" = T2.\"XCL_130\" WHERE T1.\"XCL_126\" = (SELECT MIN(\"XCL_126\") FROM Player)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1058"
  ]
}
```

### Player Identifier

```json
{
  "kind": "binding",
  "formula": "\"Player\".\"XCL_123\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_123\" FROM Player WHERE CAST((JULIANDAY('now') - JULIANDAY(\"XCL_125\")) AS REAL) / 365 >= 35",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_123\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "Player"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_123\" AS \"value\" FROM Player AS \"r0\" WHERE CAST((JULIANDAY('now') - JULIANDAY(\"r0\".\"XCL_125\")) AS REAL) / 365 >= 35",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:1118"
  ]
}
```

### Player Attribute Value

```json
{
  "kind": "binding",
  "formula": "\"Player_Attributes\".\"XCL_134\"",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_134\" FROM Player AS t1 INNER JOIN Player_Attributes AS t2 ON t1.\"XCL_122\" = t2.\"XCL_130\" ORDER BY t1.\"XCL_125\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1050"
  ]
}
```

### "Team"."XCL_173" = 'ADO Den Haag'

```json
{
  "kind": "predicate",
  "formula": "\"Team\".\"XCL_173\" = 'ADO Den Haag'",
  "grain": [],
  "population_scope": "SELECT DISTINCT t2.\"XCL_185\" FROM Team AS t1 INNER JOIN Team_attributes AS t2 ON t1.\"XCL_172\" = t2.\"XCL_176\" WHERE t1.\"XCL_173\" = 'ADO Den Haag'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1046"
  ]
}
```

### "Team"."XCL_173" = 'Willem II' AND SUBSTRING("Team_Attributes"."XCL_178", 1, 10) = '2011-02-22'

```json
{
  "kind": "predicate",
  "formula": "\"Team\".\"XCL_173\" = 'Willem II' AND SUBSTRING(\"Team_Attributes\".\"XCL_178\", 1, 10) = '2011-02-22'",
  "grain": [],
  "population_scope": "SELECT t2.\"XCL_180\" FROM Team AS t1 INNER JOIN Team_Attributes AS t2 ON t1.\"XCL_171\" = t2.\"XCL_177\" WHERE t1.\"XCL_173\" = 'Willem II' AND SUBSTRING(t2.\"XCL_178\", 1, 10) = '2011-02-22'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:1108"
  ]
}
```


## Incremental maintenance events

- Recorded alias revision · Team_Attributes.XCL_187 · Archived superseded_alias_hypotheses → archived aliases
  - Team_Attributes.XCL_187: chancecreationcrossingclass → chance_creation_crossing_class
- Recorded alias revision · Team_Attributes.XCL_184 · Archived superseded_alias_hypotheses → archived aliases
  - Team_Attributes.XCL_184: chancecreationpassingclass → chance_creation_passing_class
- Recorded alias revision · Team_Attributes.XCL_180 · Archived superseded_alias_hypotheses → archived aliases
  - Team_Attributes.XCL_180: buildupplayspeed → buildup_play_speed
