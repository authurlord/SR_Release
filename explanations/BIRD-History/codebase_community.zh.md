# BIRD-History / codebase_community — Schema 与业务口径解释

该数据库的存档目录包含 8 张表、63 个物理列、34 条关系，以及 186 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## badges

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, T3, T4, T5, b, b1, b2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| badges.XCL_001 | badge_id | unknown | bird_dev:591, bird_dev:641, bird_dev:593, bird_dev:598, bird_dev:554, bird_dev:597, bird_dev:615, bird_dev:605 |
| badges.XCL_002 | user_id | unknown | bird_dev:592, bird_dev:611, bird_dev:613, bird_dev:692, bird_dev:580, bird_dev:652, bird_dev:610, bird_dev:593 |
| badges.XCL_003 | badge_name | unknown | bird_dev:592, bird_dev:591, bird_dev:641, bird_dev:580, bird_dev:652, bird_dev:610, bird_dev:593, bird_dev:598 |
| badges.XCL_004 | date_awarded | unknown | bird_dev:611, bird_dev:591, bird_dev:641, bird_dev:613, bird_dev:692, bird_dev:652, bird_dev:598, bird_dev:606 |

## comments

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: C, T1, T2, T3, T4, c, c2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| comments.XCL_005 | comment_id | unknown | bird_dev:709, bird_dev:607, bird_dev:710, bird_dev:687, bird_dev:588, bird_dev:711, bird_dev:636, bird_dev:645 |
| comments.XCL_006 | post_id | unknown | bird_dev:594, bird_dev:709, bird_dev:694, bird_dev:712, bird_dev:617, bird_dev:563, bird_dev:561, bird_dev:562 |
| comments.XCL_007 | score | unknown | bird_dev:573, bird_dev:715, bird_dev:607, bird_dev:561, bird_dev:716, bird_dev:707, bird_dev:711, bird_dev:636 |
| comments.XCL_008 | text | unknown | bird_dev:694, bird_dev:573, bird_dev:712, bird_dev:705, bird_dev:617, bird_dev:577, bird_dev:707, bird_dev:714 |
| comments.XCL_009 | creation_date | unknown | bird_dev:617, bird_dev:563, bird_dev:616, bird_dev:608, bird_dev:565 |
| comments.XCL_010 | user_id | unknown | bird_dev:594, bird_dev:715, bird_dev:705, bird_dev:563, bird_dev:599, bird_dev:588, bird_dev:716, bird_dev:577 |
| comments.XCL_011 | 保留物理名称；存档没有恢复别名 | unknown | bird_dev:646 |

## postHistory

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, T3, T4, T5, h, ph, ph2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| postHistory.XCL_012 | Id | unknown | bird_dev:649, bird_dev:642 |
| postHistory.XCL_013 | PostHistoryTypeId | unknown | bird_dev:599, bird_dev:595 |
| postHistory.XCL_014 | PostId | unknown | bird_dev:649, bird_dev:635, bird_dev:602, bird_dev:652, bird_dev:685, bird_dev:599, bird_dev:639, bird_dev:595 |
| postHistory.XCL_016 | CreationDate | unknown | bird_dev:642, bird_dev:652, bird_dev:603 |
| postHistory.XCL_017 | UserId | unknown | bird_dev:635, bird_dev:602, bird_dev:652, bird_dev:639, bird_dev:595, bird_dev:633, bird_dev:631, bird_dev:637 |
| postHistory.XCL_018 | Comment | unknown | bird_dev:685 |
| postHistory.XCL_019 | Text | unknown | bird_dev:584 |
| postHistory.XCL_020 | UserName | unknown | bird_dev:652 |

## postLinks

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, pl

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| postLinks.XCL_021 | Link ID | unknown | bird_dev:665 |
| postLinks.XCL_022 | Creation Date | unknown | bird_dev:665 |
| postLinks.XCL_023 | Post ID | unknown | bird_dev:665, bird_dev:651, bird_dev:667, bird_dev:601, bird_dev:600, bird_dev:655 |
| postLinks.XCL_024 | Related Post ID | unknown | bird_dev:651, bird_dev:655 |
| postLinks.XCL_025 | Link Type ID | unknown | bird_dev:601, bird_dev:655 |

## posts

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, T3, T4, T5, c, owned, p, p1, p2, p3

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| posts.XCL_026 | post_id | unknown | bird_dev:709, bird_dev:537, bird_dev:694, bird_dev:549, bird_dev:712, bird_dev:702, bird_dev:649, bird_dev:665 |
| posts.XCL_029 | creation_date | unknown | bird_dev:683, bird_dev:677, bird_dev:681, bird_dev:667, bird_dev:670 |
| posts.XCL_030 | view_count | unknown | bird_dev:709, bird_dev:702, bird_dev:602, bird_dev:656, bird_dev:710, bird_dev:687, bird_dev:547, bird_dev:609 |
| posts.XCL_031 | score | unknown | bird_dev:709, bird_dev:678, bird_dev:653, bird_dev:562, bird_dev:685, bird_dev:681, bird_dev:707, bird_dev:595 |
| posts.XCL_032 | body | unknown | bird_dev:549, bird_dev:550 |
| posts.XCL_033 | owner_user_id | unknown | bird_dev:537, bird_dev:694, bird_dev:672, bird_dev:538, bird_dev:582, bird_dev:678, bird_dev:604, bird_dev:660 |
| posts.XCL_034 | last_activity_date | unknown | bird_dev:664 |
| posts.XCL_035 | title | unknown | bird_dev:694, bird_dev:712, bird_dev:649, bird_dev:538, bird_dev:582, bird_dev:678, bird_dev:586, bird_dev:561 |
| posts.XCL_036 | tags | unknown | bird_dev:637, bird_dev:587, bird_dev:630 |
| posts.XCL_037 | answer_count | unknown | bird_dev:665, bird_dev:633, bird_dev:698, bird_dev:543 |
| posts.XCL_038 | comment_count | unknown | bird_dev:710, bird_dev:542, bird_dev:637, bird_dev:688, bird_dev:698, bird_dev:564 |
| posts.XCL_039 | favorite_count | unknown | bird_dev:672, bird_dev:660, bird_dev:563, bird_dev:541, bird_dev:666, bird_dev:648, bird_dev:603, bird_dev:682 |
| posts.XCL_040 | parent_post_id | unknown | bird_dev:544, bird_dev:685, bird_dev:644, bird_dev:583 |
| posts.XCL_041 | last_edit_date | unknown | bird_dev:649, bird_dev:689, bird_dev:644 |
| posts.XCL_043 | 保留物理名称；存档没有恢复别名 | unknown | bird_dev:656, bird_dev:564, bird_dev:545 |
| posts.XCL_044 | close_date | unknown | bird_dev:546, bird_dev:565 |
| posts.post_count | 保留物理名称；存档没有恢复别名 | unknown | bird_dev:604 |

## tags

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T3, T5, t

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| tags.XCL_047 | tag_id | unknown | bird_dev:703, bird_dev:696, bird_dev:659 |
| tags.XCL_048 | tag_name | unknown | bird_dev:549, bird_dev:654, bird_dev:639, bird_dev:696, bird_dev:704 |
| tags.XCL_049 | count | unknown | bird_dev:703, bird_dev:550, bird_dev:659 |
| tags.XCL_050 | post_id | unknown | bird_dev:549, bird_dev:654, bird_dev:639, bird_dev:550, bird_dev:704 |
| tags.XCL_051 | 保留物理名称；存档没有恢复别名 | unknown | bird_dev:704 |

## users

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, T3, T4, creator, cu, u, u2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| users.XCL_052 | user_id | unknown | bird_dev:594, bird_dev:611, bird_dev:537, bird_dev:694, bird_dev:715, bird_dev:672, bird_dev:705, bird_dev:538 |
| users.XCL_053 | reputation | unknown | bird_dev:594, bird_dev:611, bird_dev:705, bird_dev:531, bird_dev:674, bird_dev:661, bird_dev:697, bird_dev:610 |
| users.XCL_054 | creation_date | unknown | bird_dev:694, bird_dev:692, bird_dev:532, bird_dev:693, bird_dev:536, bird_dev:699, bird_dev:708, bird_dev:682 |
| users.XCL_055 | display_name | unknown | bird_dev:537, bird_dev:694, bird_dev:643, bird_dev:715, bird_dev:538, bird_dev:582, bird_dev:678, bird_dev:531 |
| users.XCL_056 | last_access_date | unknown | bird_dev:650, bird_dev:533 |
| users.XCL_057 | website_url | unknown | bird_dev:574, bird_dev:648, bird_dev:583, bird_dev:657 |
| users.XCL_058 | location | unknown | bird_dev:672, bird_dev:613, bird_dev:593, bird_dev:618, bird_dev:654, bird_dev:597, bird_dev:689, bird_dev:625 |
| users.XCL_060 | views | unknown | bird_dev:643, bird_dev:697, bird_dev:534, bird_dev:590, bird_dev:675, bird_dev:620, bird_dev:536, bird_dev:628 |
| users.XCL_061 | up_votes | unknown | bird_dev:705, bird_dev:604, bird_dev:691, bird_dev:716, bird_dev:535, bird_dev:713 |
| users.XCL_062 | down_votes | unknown | bird_dev:715, bird_dev:535 |
| users.XCL_064 | age | unknown | bird_dev:643, bird_dev:684, bird_dev:604, bird_dev:691, bird_dev:661, bird_dev:619, bird_dev:618, bird_dev:623 |

## votes

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1, T2, T3, T4, v

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| votes.XCL_066 | vote_id | unknown | bird_dev:635, bird_dev:571, bird_dev:700, bird_dev:626, bird_dev:559, bird_dev:558, bird_dev:568 |
| votes.XCL_067 | post_id | unknown | bird_dev:635, bird_dev:586, bird_dev:666, bird_dev:632, bird_dev:662, bird_dev:585, bird_dev:569, bird_dev:673 |
| votes.XCL_068 | vote_type_id | unknown | bird_dev:657 |
| votes.XCL_069 | creation_date | unknown | bird_dev:629, bird_dev:669, bird_dev:662, bird_dev:626, bird_dev:559, bird_dev:558 |
| votes.XCL_070 | user_id | unknown | bird_dev:586, bird_dev:669, bird_dev:571, bird_dev:666, bird_dev:558, bird_dev:657, bird_dev:568 |
| votes.XCL_071 | score | unknown | bird_dev:586, bird_dev:662, bird_dev:700, bird_dev:585, bird_dev:657 |

## 表关系与连接依据

- badges.XCL_002 ↔ comments.XCL_010; target_disjoint_historical_join
- badges.XCL_002 ↔ postHistory.XCL_017; target_disjoint_historical_join
- badges.XCL_002 ↔ users.XCL_052; target_disjoint_historical_join
- comments.XCL_006 ↔ posts.XCL_026; target_disjoint_historical_join
- comments.XCL_010 ↔ users.XCL_052; target_disjoint_historical_join
- postHistory.XCL_014 ↔ posts.XCL_026; target_disjoint_historical_join
- postHistory.XCL_014 ↔ tags.XCL_050; target_disjoint_historical_join
- postHistory.XCL_014 ↔ votes.XCL_067; target_disjoint_historical_join
- postHistory.XCL_017 ↔ users.XCL_052; target_disjoint_historical_join
- postLinks.XCL_023 ↔ posts.XCL_026; target_disjoint_historical_join
- postLinks.XCL_024 ↔ posts.XCL_026; target_disjoint_historical_join
- posts.XCL_026 ↔ tags.XCL_050; target_disjoint_historical_join
- posts.XCL_026 ↔ votes.XCL_067; target_disjoint_historical_join
- posts.XCL_033 ↔ users.XCL_052; target_disjoint_historical_join
- posts.XCL_033 ↔ votes.XCL_070; target_disjoint_historical_join
- posts.XCL_040 ↔ users.XCL_052; target_disjoint_historical_join
- users.XCL_052 ↔ votes.XCL_070; target_disjoint_historical_join
- badges.XCL_002 ↔ comments.XCL_010; sql_workload_observed_join
- badges.XCL_002 ↔ postHistory.XCL_017; sql_workload_observed_join
- badges.XCL_002 ↔ users.XCL_052; sql_workload_observed_join
- comments.XCL_006 ↔ posts.XCL_026; sql_workload_observed_join
- comments.XCL_010 ↔ users.XCL_052; sql_workload_observed_join
- postHistory.XCL_014 ↔ posts.XCL_026; sql_workload_observed_join
- postHistory.XCL_014 ↔ tags.XCL_050; sql_workload_observed_join
- postHistory.XCL_014 ↔ votes.XCL_067; sql_workload_observed_join
- postHistory.XCL_017 ↔ users.XCL_052; sql_workload_observed_join
- postLinks.XCL_023 ↔ posts.XCL_026; sql_workload_observed_join
- postLinks.XCL_024 ↔ posts.XCL_026; sql_workload_observed_join
- posts.XCL_026 ↔ tags.XCL_050; sql_workload_observed_join
- posts.XCL_026 ↔ votes.XCL_067; sql_workload_observed_join
- posts.XCL_033 ↔ users.XCL_052; sql_workload_observed_join
- posts.XCL_033 ↔ votes.XCL_070; sql_workload_observed_join
- posts.XCL_040 ↔ users.XCL_052; sql_workload_observed_join
- users.XCL_052 ↔ votes.XCL_070; sql_workload_observed_join

## 业务口径、总体与粒度

### Executes an inner join between the users table (T1) and the badges table (T2) on the condition that users.XCL_052 equals badges.XCL_002. It applies fi

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_064\" > 65 AND T2.\"XCL_003\" = 'Supporter'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:623"
  ]
}
```

### A query that retrieves the "XCL_035" value from the posts table. It joins posts with postLinks where the link's "XCL_023" matches the post's "XCL_026"

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_035\" FROM posts AS T1 INNER JOIN postLinks AS T2 ON T2.\"XCL_023\" = T1.\"XCL_026\" ORDER BY T1.\"XCL_029\" LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:667"
  ]
}
```

### Full SQL program that joins badges (T1) to users (T2) on XCL_002 = XCL_052, filters for badges with XCL_003 = 'Organizer', and computes the ratio of u

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(IIF(T2.\"XCL_064\" BETWEEN 13 AND 18, 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T1.\"XCL_003\" = 'Organizer'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:615"
  ]
}
```

### A query that retrieves the "XCL_054" value from the users table where the "XCL_055" field is 'IrishStat'. Used to identify a specific user or record a

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_054\" FROM users WHERE \"XCL_055\" = 'IrishStat'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:699"
  ]
}
```

### High-Score Post History Query

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_014\", \"XCL_017\" FROM postHistory WHERE \"XCL_014\" IN (SELECT \"XCL_026\" FROM posts WHERE \"XCL_030\" > 60)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:602"
  ]
}
```

### A full SQL program that joins the 'users' table (T1) with the 'posts' table (T2) on user ID (XCL_052 = XCL_033) to compute the percentage of posts fro

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(IIF(STRFTIME('%Y', T2.\"XCL_029\") = '2011' AND T1.\"XCL_053\" > 1000, 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:683"
  ]
}
```

### A query that selects the XCL_052 value from the users table where the XCL_060 value is the minimum in the table. This identifies the user (or record) 

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_052\" FROM users WHERE \"XCL_060\" = (SELECT MIN(\"XCL_060\") FROM users)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:590"
  ]
}
```

### Executes an inner join between posts (T1) and comments (T2) on the post identifier (XCL_026 = XCL_006), filters posts where XCL_031 equals 1910, and r

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_026\" = T2.\"XCL_006\" WHERE T1.\"XCL_031\" = 1910",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:562"
  ]
}
```

### A SQL program that joins the users and posts tables on the user ID (XCL_052 = XCL_033) and filters for the user named 'Tiago Pasqualini' (XCL_055). It

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T1.\"XCL_055\" = 'Tiago Pasqualini'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:567"
  ]
}
```

### Full SQL program that joins the posts table (T1) with the users table (T2) on the foreign key relationship (XCL_033 = XCL_052) and filters for the use

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:537"
  ]
}
```

### Filtered Comment Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_005\") FROM comments WHERE \"XCL_010\" = 13 AND \"XCL_007\" < 60",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:645"
  ]
}
```

### A query that retrieves the "XCL_003" value from the "badges" table, filtered to records where the "XCL_004" column equals the literal timestamp '2010-

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_003\" FROM badges WHERE \"XCL_004\" = '2010-07-19 19:39:08.0'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:606"
  ]
}
```

### A SQL program that joins posts and users on XCL_033 = XCL_052, filters for posts where XCL_044 is not null, and selects the user's XCL_055 attribute.

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_055\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE NOT T1.\"XCL_044\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:546"
  ]
}
```

### Full SQL program that calculates the average of votes.XCL_067 for votes cast by the user (identified by users.XCL_052) who has the maximum users.XCL_0

```json
{
  "kind": "program",
  "formula": "SELECT AVG(\"XCL_067\") FROM votes WHERE \"XCL_070\" IN (SELECT \"XCL_052\" FROM users WHERE \"XCL_064\" = (SELECT MAX(\"XCL_064\") FROM users))",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:673"
  ]
}
```

### Calculates the percentage of users who possess a badge where 'XCL_003' is 'Teacher'. It joins 'users' and 'badges' on 'XCL_052' = 'XCL_002', filters f

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(T1.\"XCL_052\") AS REAL) * 100 / (SELECT COUNT(\"XCL_052\") FROM users) FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'Teacher'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:614"
  ]
}
```

### Face Detection Post Lookup

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_041\", \"XCL_040\" FROM posts WHERE \"XCL_035\" = 'Detecting a given face in a database of facial images'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:644"
  ]
}
```

### A query that retrieves the 'XCL_035' value from the 'posts' table for all posts where the associated user (joined via 'XCL_033' = 'XCL_052') has the n

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_035\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'Vebjorn Ljosa'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:582"
  ]
}
```

### A query that retrieves the 'XCL_029' value from the 'posts' table for the first matching record. It joins 'users' and 'posts' on 'XCL_052' = 'XCL_033'

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_029\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE NOT T1.\"XCL_064\" IS NULL ORDER BY T1.\"XCL_064\", T2.\"XCL_029\" LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:670"
  ]
}
```

### Executes a scalar aggregation on the 'posts' table. It applies a filter on 'XCL_030' (value 10) and returns a single count of 'XCL_026' entries. This 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_026\") FROM posts WHERE \"XCL_030\" = 10",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:609"
  ]
}
```

### Query for XCL_031 difference by user group

```json
{
  "kind": "program",
  "formula": "SELECT SUM(IIF(T1.\"XCL_055\" = 'Mornington', T3.\"XCL_031\", 0)) - SUM(IIF(T1.\"XCL_055\" = 'Amos', T3.\"XCL_031\", 0)) AS diff FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T3.\"XCL_026\" = T2.\"XCL_014\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:640"
  ]
}
```

### A full SQL program that retrieves post identifiers ('XCL_036') for a specific user. It joins 'users' to 'postHistory' on 'XCL_052' = 'XCL_017' and 'po

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_036\" FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T2.\"XCL_014\" = T3.\"XCL_026\" WHERE T1.\"XCL_055\" = 'John Salvatier'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:630"
  ]
}
```

### 2010 Post Link Aggregation Query

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(T1.\"XCL_021\") AS REAL) / 12 FROM postLinks AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_023\" = T2.\"XCL_026\" WHERE T2.\"XCL_037\" <= 2 AND STRFTIME('%Y', T1.\"XCL_022\") = '2010'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:665"
  ]
}
```

### Filtered User Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_052\") FROM users WHERE \"XCL_064\" BETWEEN 19 AND 65 AND \"XCL_061\" > 5000",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:691"
  ]
}
```

### A full SQL program that joins the users table (T1) with the postHistory table (T2) on the user identifier (XCL_052 = XCL_017). It filters the users ta

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" WHERE T1.\"XCL_055\" = 'Daniel Vassallo'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:631"
  ]
}
```

### Program that joins postHistory and posts on XCL_014 = XCL_026, filters posts where XCL_035 equals 'What is the best introductory Bayesian statistics t

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_012\", T2.\"XCL_041\" FROM postHistory AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_014\" = T2.\"XCL_026\" WHERE T2.\"XCL_035\" = 'What is the best introductory Bayesian statistics textbook?'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:649"
  ]
}
```

### Full SQL program that joins 'votes' and 'posts' tables on the post identifier ('XCL_070' = 'XCL_033'), filters for post ID 24, and computes the averag

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(T2.\"XCL_026\") AS REAL) / COUNT(DISTINCT T1.\"XCL_066\") FROM votes AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_070\" = T2.\"XCL_033\" WHERE T1.\"XCL_070\" = 24",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:571"
  ]
}
```

### SQL program that calculates the sum of XCL_030 from the posts table where the XCL_034 field matches the pattern '2010-07-19%'. This represents a speci

```json
{
  "kind": "program",
  "formula": "SELECT SUM(\"XCL_030\") FROM posts WHERE \"XCL_034\" LIKE '2010-07-19%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:664"
  ]
}
```

### A query that identifies users who have created posts associated with the tag 'hypothesis-testing'. It joins the tags, posts, and users tables, filteri

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_055\", T3.\"XCL_058\" FROM tags AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_050\" = T2.\"XCL_026\" INNER JOIN users AS T3 ON T3.\"XCL_052\" = T2.\"XCL_033\" WHERE T1.\"XCL_048\" = 'hypothesis-testing'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:654"
  ]
}
```

### Latest User Attributes

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_052\", \"XCL_055\" FROM users WHERE \"XCL_060\" = (SELECT MAX(\"XCL_060\") FROM users)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:628"
  ]
}
```

### Retrieves the user attribute XCL_055 corresponding to the post with the maximum XCL_039 value, joining posts and users on XCL_033 and XCL_052 respecti

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_055\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" ORDER BY T1.\"XCL_039\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:541"
  ]
}
```

### A query that retrieves the "XCL_008" value from the "comments" table for the exact moment defined by "XCL_009" = '2010-07-19 19:16:14.0'. It assumes a

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_008\" FROM comments WHERE \"XCL_009\" = '2010-07-19 19:16:14.0'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:608"
  ]
}
```

### Filtered User Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_052\") FROM users WHERE \"XCL_061\" > 100 AND \"XCL_062\" > 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:535"
  ]
}
```

### Joins the users table (T1) to the comments table (T2) on users.XCL_052 = comments.XCL_010. Filters the comments to those where comments.XCL_007 is bet

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(IIF(T1.\"XCL_061\" = 0, 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_052\") AS per FROM users AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_052\" = T2.\"XCL_010\" WHERE T2.\"XCL_007\" BETWEEN 5 AND 10",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:716"
  ]
}
```

### A query that retrieves the XCL_052 value from the users table for the record(s) having the maximum XCL_053 value. This effectively identifies the user

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_052\" FROM users WHERE \"XCL_053\" = (SELECT MAX(\"XCL_053\") FROM users)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:589"
  ]
}
```

### A program that retrieves the first 10 values of 'XCL_055' from the 'users' table by joining with the 'badges' table on 'XCL_052' = 'XCL_002'. It filte

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'Necromancer' LIMIT 10",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:580"
  ]
}
```

### A query that joins users and votes on XCL_052 = XCL_070 to retrieve the user identifier (XCL_055) for votes where XCL_066 equals 6347.

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN votes AS T2 ON T1.\"XCL_052\" = T2.\"XCL_070\" WHERE T2.\"XCL_066\" = 6347",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:568"
  ]
}
```

### Full SQL program that selects the count of 'XCL_001' from the 'badges' table, applying a filter on 'XCL_003' to include only records with the value 'R

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_001\") FROM badges WHERE \"XCL_003\" = 'Revival'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:560"
  ]
}
```

### Full SQL program that joins users and posts on the user ID, filters posts by the year 2010 (extracted from XCL_029) and users by the name 'Jay Stevens

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE STRFTIME('%Y', T2.\"XCL_029\") = '2010' AND T1.\"XCL_055\" = 'Jay Stevens'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:677"
  ]
}
```

### Full SQL program that computes the percentage point difference in badge counts for the years 2010 and 2011. It filters the 'badges' table for records 

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(IIF(STRFTIME('%Y', \"XCL_004\") = '2010', 1, 0)) AS REAL) * 100 / COUNT(\"XCL_001\") - CAST(SUM(IIF(STRFTIME('%Y', \"XCL_004\") = '2011', 1, 0)) AS REAL) * 100 / COUNT(\"XCL_001\") FROM badges WHERE \"XCL_003\" = 'Student'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:598"
  ]
}
```

### Executes a count on the 'badges' table, filtering for rows where 'XCL_003' equals 'Supporter' and the year extracted from 'XCL_004' is '2011'. Returns

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_001\") FROM badges WHERE STRFTIME('%Y', \"XCL_004\") = '2011' AND \"XCL_003\" = 'Supporter'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:591"
  ]
}
```

### A query that selects XCL_052 from the users table where XCL_064 is equal to the minimum XCL_064 value in the table. Returns the user identifier corres

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_052\" FROM users WHERE \"XCL_064\" = (SELECT MIN(\"XCL_064\") FROM users)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:663"
  ]
}
```

### A query that retrieves the XCL_064 value from the users table for the row(s) where XCL_053 is at its maximum value. This pattern is used to fetch a sp

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_064\" FROM users WHERE \"XCL_053\" = (SELECT MAX(\"XCL_053\") FROM users)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:661"
  ]
}
```

### A query that joins 'users' and 'posts' on 'XCL_052' = 'XCL_033', orders the results by 'XCL_030' in descending order, and limits the output to 1 row. 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_052\", T2.\"XCL_035\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" ORDER BY T2.\"XCL_030\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:679"
  ]
}
```

### A query that retrieves the "XCL_035" value from "posts" where "XCL_026" equals the "XCL_006" value from the most recent "comments" entry (ordered by "

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_035\" FROM posts WHERE \"XCL_026\" = (SELECT \"XCL_006\" FROM comments ORDER BY \"XCL_007\" DESC LIMIT 1)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:561"
  ]
}
```

### A query that joins 'users' and 'badges' on 'XCL_052' = 'XCL_002', orders the results by 'users.XCL_053' in descending order, and returns the 'badges.X

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_003\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" ORDER BY T1.\"XCL_053\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:610"
  ]
}
```

### Active Comment Count for Status 40 Users

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T1.\"XCL_005\") FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_007\" = 0 AND T2.\"XCL_064\" = 40",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:711"
  ]
}
```

### Retrieves all badge identifiers for a specific user by joining the users and badges tables on the user ID (XCL_052 = XCL_002) and filtering by the use

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_003\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_055\" = 'SilentGhost'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:575"
  ]
}
```

### Query returning user attributes XCL_055 and XCL_057 for users joined to posts where the post attribute XCL_039 exceeds 150.

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_055\", T1.\"XCL_057\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T2.\"XCL_039\" > 150",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:648"
  ]
}
```

### A full SQL program that retrieves the user identifier ("XCL_055") from the "users" table by matching "XCL_052" against the most recent post identifier

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_055\" FROM users WHERE \"XCL_052\" = (SELECT \"XCL_033\" FROM posts WHERE NOT \"XCL_043\" IS NULL ORDER BY \"XCL_030\" DESC LIMIT 1)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:656"
  ]
}
```

### Executes a count on the badges table, filtering for rows where the badge name column equals 'Commentator' and the year extracted from the date column 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_001\") FROM badges WHERE \"XCL_003\" = 'Commentator' AND STRFTIME('%Y', \"XCL_004\") = '2014'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:641"
  ]
}
```

### Executes a count on the votes table, filtering by a specific identifier value (58) and a specific date ('2010-07-19').

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_066\") FROM votes WHERE \"XCL_070\" = 58 AND \"XCL_069\" = '2010-07-19'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:558"
  ]
}
```

### 2010 Vote Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_066\") FROM votes WHERE STRFTIME('%Y', \"XCL_069\") = '2010'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:626"
  ]
}
```

### A query that retrieves badge identifiers for a specific user by joining the users and badges tables on the user ID (XCL_052 = XCL_002) and filtering b

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_003\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_055\" = 'Pierre'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:612"
  ]
}
```

### Returns the identifier (XCL_003) of the single badge associated with the highest number of comments. The computation joins badges to comments on the b

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_003\" FROM badges AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_002\" = t2.\"XCL_010\" GROUP BY T2.\"XCL_010\" ORDER BY COUNT(T2.\"XCL_010\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:596"
  ]
}
```

### A query that joins the posts table (T1) with the comments table (T2) using the condition T2.XCL_006 = T2.XCL_005. It filters for posts where T1.XCL_03

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_035\", T2.\"XCL_011\" FROM posts AS T1 INNER JOIN comments AS T2 ON T2.\"XCL_006\" = T2.\"XCL_005\" WHERE T1.\"XCL_030\" > 60",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:646"
  ]
}
```

### Community user tag ratio query

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(IIF(T3.\"XCL_048\" = 'r', 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN tags AS T3 ON T3.\"XCL_050\" = T2.\"XCL_014\" WHERE T1.\"XCL_055\" = 'Community'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:639"
  ]
}
```

### A query that retrieves the 'XCL_035' values from the 'posts' table for all posts created by the user with the identifier 'csgillespie' in the 'users' 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_035\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:538"
  ]
}
```

### Full SQL program that counts posts from the 'posts' table joined with 'users' on XCL_033 = XCL_052, filtered by posts.XCL_030 >= 20 and users.XCL_064 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T1.\"XCL_030\" >= 20 AND T2.\"XCL_064\" > 65",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:547"
  ]
}
```

### A full SQL program that joins the badges table (T1) with the users table (T2) on the user identifier (XCL_002 = XCL_052). It filters for badges of typ

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(DISTINCT T1.\"XCL_001\") FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T1.\"XCL_003\" IN ('Supporter', 'Teacher') AND T2.\"XCL_058\" = 'New York'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:593"
  ]
}
```

### Executes a count aggregation on the users table, filtering for records where the XCL_064 attribute falls within the range of 19 to 65.

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_052\") FROM users WHERE \"XCL_064\" BETWEEN 19 AND 65",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:627"
  ]
}
```

### A query that groups the "votes" table by "XCL_069", counts the occurrences of "XCL_066" within each group, sorts the groups in descending order by thi

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_069\" FROM votes GROUP BY \"XCL_069\" ORDER BY COUNT(\"XCL_066\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:559"
  ]
}
```

### A SQL program that joins posts and users on the user ID, filters for the username 'csgillespie', and returns the maximum post ID.

```json
{
  "kind": "program",
  "formula": "SELECT MAX(T1.\"XCL_037\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:543"
  ]
}
```

### A SQL program that joins 'posts' (T1) and 'users' (T2) on 'XCL_033' = 'XCL_052', filters for the user 'csgillespie', and computes the average of 'XCL_

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T1.\"XCL_030\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:555"
  ]
}
```

### A query that retrieves the XCL_055 value for users named 'Harlan' or 'Jarrod Dixon' where the XCL_053 value equals the maximum XCL_053 value found for

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_055\" FROM users WHERE \"XCL_055\" IN ('Harlan', 'Jarrod Dixon') AND \"XCL_053\" = (SELECT MAX(\"XCL_053\") FROM users WHERE \"XCL_055\" IN ('Harlan', 'Jarrod Dixon'))",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:531"
  ]
}
```

### A query that resolves the target post associated with a specific source post via the postLinks table. It joins posts (T1) to postLinks (T2) on the sou

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_035\", T2.\"XCL_025\" FROM posts AS T1 INNER JOIN postLinks AS T2 ON T1.\"XCL_026\" = T2.\"XCL_023\" INNER JOIN posts AS T3 ON T2.\"XCL_024\" = T3.\"XCL_026\" WHERE T1.\"XCL_035\" = 'What are principal component scores?'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:655"
  ]
}
```

### Full SQL program that joins 'users' and 'posts' to calculate the percentage of posts with a score > 50 for users having the maximum reputation value.

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_030\" > 50 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" INNER JOIN (SELECT MAX(\"XCL_053\") AS max_reputation FROM users) AS T3 ON T1.\"XCL_053\" = T3.\"max_reputation\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:701"
  ]
}
```

### Citizen Patrol Badge Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_001\") FROM badges WHERE \"XCL_003\" = 'Citizen Patrol'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:695"
  ]
}
```

### A query that joins the comments table to the users table on the user identifier (comments.XCL_010 = users.XCL_052), filters for comments where XCL_006

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_052\", T2.\"XCL_053\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_006\" = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:594"
  ]
}
```

### A query that retrieves the "XCL_055" value from the "users" table, filtered to include only rows where the "XCL_057" column equals 'http://stackoverfl

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_055\" FROM users WHERE \"XCL_057\" = 'http://stackoverflow.com'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:574"
  ]
}
```

### A query that joins 'posts' and 'users' on 'XCL_040' (post) to 'XCL_052' (user) to retrieve the user identifier ('XCL_055') for a specific post identif

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_055\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_040\" = T2.\"XCL_052\" WHERE T1.\"XCL_035\" = 'Examples for teaching: Correlation does not mean causation'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:544"
  ]
}
```

### A query that identifies the single user (from a specific set) who has the highest aggregate sum of the post metric XCL_031. It joins users to postHist

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T2.\"XCL_014\" = T3.\"XCL_026\" WHERE T1.\"XCL_055\" = 'Harvey Motulsky' OR T1.\"XCL_055\" = 'Noah Snyder' GROUP BY T1.\"XCL_055\" ORDER BY SUM(T3.\"XCL_031\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:634"
  ]
}
```

### A SQL program that identifies the user with the most badges. It joins the 'users' table (T1) with the 'badges' table (T2) on the condition that T1.'XC

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" GROUP BY T1.\"XCL_055\" ORDER BY COUNT(T1.\"XCL_052\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:668"
  ]
}
```

### A query that retrieves comment identifiers (XCL_008) by joining the posts and comments tables. It filters for a specific post (XCL_043 = 107829) where

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_008\" FROM posts AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_026\" = T2.\"XCL_006\" WHERE T1.\"XCL_043\" = 107829 AND T1.\"XCL_038\" = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:564"
  ]
}
```

### A query that joins postHistory, posts, and users to retrieve post and user identifiers for history records where the category (XCL_018) is 'Computer G

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_031\", T3.\"XCL_055\" FROM postHistory AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_014\" = T2.\"XCL_026\" INNER JOIN users AS T3 ON T2.\"XCL_040\" = T3.\"XCL_052\" WHERE T1.\"XCL_018\" = 'Computer Game Datasets'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:685"
  ]
}
```

### A query that retrieves the 'XCL_064' value for users from the 'users' table who are located in 'Vienna, Austria' (filtered by 'XCL_058') and have a co

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_064\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_058\" = 'Vienna, Austria'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:618"
  ]
}
```

### The full SQL program that computes the ratio of votes from 2010 to votes from 2011 based on the 'XCL_069' column in the 'votes' table.

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(IIF(STRFTIME('%Y', \"XCL_069\") = '2010', 1, 0)) AS REAL) / SUM(IIF(STRFTIME('%Y', \"XCL_069\") = '2011', 1, 0)) FROM votes",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:629"
  ]
}
```

### A query that retrieves comment identifiers (XCL_008) from the comments table. It joins comments to posts via XCL_006 = XCL_026 and filters for posts w

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_008\" FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T2.\"XCL_035\" LIKE '%linear regression%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:706"
  ]
}
```

### A query that joins users, postHistory, and posts to retrieve post identifiers. It filters for a specific user name ('Mark Meckes') and a specific post

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_036\" FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T3.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_055\" = 'Mark Meckes' AND T3.\"XCL_038\" = 0",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:637"
  ]
}
```

### A query that retrieves the 'XCL_039' value from 'posts' by joining with 'comments' on 'XCL_026' (post ID) and 'XCL_006' (comment post ID). It filters 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_039\" FROM posts AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_026\" = T2.\"XCL_006\" WHERE T2.\"XCL_009\" = '2014-04-23 20:29:39.0' AND T2.\"XCL_010\" = 3025",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:563"
  ]
}
```

### Executes a count aggregation on the 'posts' table, applying a filter condition that restricts results to rows where 'XCL_030' is less than 20.

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_026\") FROM posts WHERE \"XCL_030\" < 20",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:702"
  ]
}
```

### Full SQL program that joins users, postHistory, and votes tables. It filters users by the name 'Harlan' (XCL_055), links users to post history via use

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN votes AS T3 ON T3.\"XCL_067\" = T2.\"XCL_014\" WHERE T1.\"XCL_055\" = 'Harlan'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:632"
  ]
}
```

### A query program that selects "XCL_008" from the "comments" table, restricted to records where "XCL_007" is 17. This represents a point-in-time or spec

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_008\" FROM comments WHERE \"XCL_007\" = 17",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:573"
  ]
}
```

### A SQL program that selects "XCL_055" from the "users" table, applying a filter where "XCL_052" is equal to 30. This represents a specific subset of us

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_055\" FROM users WHERE \"XCL_052\" = 30",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:624"
  ]
}
```

### 2011 User ID Extraction

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_055\" FROM users WHERE STRFTIME('%Y', \"XCL_054\") = '2011'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:532"
  ]
}
```

### Executes a count aggregation on the votes table, filtering for records where the value in XCL_071 is at least 30.

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_066\") FROM votes WHERE \"XCL_071\" >= 30",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:700"
  ]
}
```

### A full SQL program that joins users, postHistory, posts, and votes to analyze voting patterns on posts by 'Matt Parker'. It groups results by post ID 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T2.\"XCL_014\" = T3.\"XCL_026\" INNER JOIN votes AS T4 ON T4.\"XCL_067\" = T3.\"XCL_026\" WHERE T1.\"XCL_055\" = 'Matt Parker' GROUP BY T2.\"XCL_014\", T4.\"XCL_066\" HAVING COUNT(T4.\"XCL_066\") > 4",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:635"
  ]
}
```

### A query that retrieves the top 5 rows from the posts table, sorted by the column XCL_031 in descending order, returning only the XCL_035 column.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_035\" FROM posts ORDER BY \"XCL_031\" DESC LIMIT 5",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:658"
  ]
}
```

### A full SQL program that joins post history data with a calculated metric. It selects 'XCL_013' from 'postHistory' filtered by 'XCL_014' = 3720, and in

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_013\", (SELECT COUNT(DISTINCT \"XCL_010\") FROM comments WHERE \"XCL_006\" = 3720) AS NumberOfUsers FROM postHistory AS T1 WHERE T1.\"XCL_014\" = 3720",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:599"
  ]
}
```

### Full SQL program that joins the 'badges' table (T1) with the 'users' table (T2) on the user identifier (T1.XCL_002 = T2.XCL_052). It filters for badge

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_001\") FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE STRFTIME('%Y', T1.\"XCL_004\") = '2011' AND T2.\"XCL_055\" = 'csgillespie'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:553"
  ]
}
```

### A full query program that joins posts and comments on post ID (T1."XCL_026" = T2."XCL_006"). It groups by post ID, calculates the count of comments, a

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_005\") FROM posts AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_026\" = T2.\"XCL_006\" GROUP BY T1.\"XCL_026\" ORDER BY SUM(T1.\"XCL_030\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:687"
  ]
}
```

### A query that joins the 'posts' and 'users' tables to retrieve the 'XCL_058' value for the user who authored or is associated with the post where 'XCL_

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_058\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T1.\"XCL_035\" = 'Eliciting priors from experts'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:548"
  ]
}
```

### Full SQL program that joins users, posts, and comments. It counts the number of posts (XCL_026) that have comments for each user, orders the results b

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T2.\"XCL_026\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" INNER JOIN comments AS T3 ON T3.\"XCL_006\" = T2.\"XCL_026\" ORDER BY T1.\"XCL_054\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:693"
  ]
}
```

### A query that joins 'posts' and 'users' tables to retrieve the 'XCL_055' value for the user who authored the post with the title 'Eliciting priors from

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_055\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T1.\"XCL_035\" = 'Eliciting priors from experts'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:539"
  ]
}
```

### A query that joins the badges table to the users table on the user ID (XCL_002 = XCL_052), filters for the user with the name 'Emmett' (XCL_055), orde

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_003\" FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'Emmett' ORDER BY T1.\"XCL_004\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:690"
  ]
}
```

### Full SQL program that joins the posts table (T1) with the users table (T2) on T1.XCL_033 = T2.XCL_052, filters for posts where T1.XCL_030 > 5, and com

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(IIF(T2.\"XCL_064\" > 65, 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T1.\"XCL_030\" > 5",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:557"
  ]
}
```

### Full program that identifies the highest-ranked comment (by XCL_007 DESC) associated with posts having a score (XCL_031) between 100 and 150.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_008\" FROM comments WHERE \"XCL_006\" IN (SELECT \"XCL_026\" FROM posts WHERE \"XCL_031\" BETWEEN 100 AND 150) ORDER BY \"XCL_007\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:707"
  ]
}
```

### A query that retrieves comment identifiers (XCL_008) by joining the users and comments tables. It filters for users where XCL_055 is 'A Lion' and matc

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_008\" FROM users AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_052\" = T2.\"XCL_010\" WHERE T1.\"XCL_055\" = 'A Lion'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:577"
  ]
}
```

### A full SQL program that joins the 'comments' table (T1) with the 'posts' table (T2) on 'XCL_006' = 'XCL_026'. It filters for a specific comment ID ('X

```json
{
  "kind": "program",
  "formula": "SELECT IIF(T2.\"XCL_044\" IS NULL, 'NOT well-finished', 'well-finished') AS resylt FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T1.\"XCL_010\" = 23853 AND T1.\"XCL_009\" = '2013-07-12 09:08:18.0'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:565"
  ]
}
```

### Badge for Min XCL_053 User

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_003\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_053\" = (SELECT MIN(\"XCL_053\") FROM users)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:621"
  ]
}
```

### A SQL program that joins 'badges' and 'users' on 'XCL_002' = 'XCL_052', groups by 'users.XCL_055', orders by the count of 'badges.XCL_001' in descendi

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_055\" FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" GROUP BY T2.\"XCL_055\" ORDER BY COUNT(T1.\"XCL_001\") DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:554"
  ]
}
```

### A query that retrieves the top 10 users (by XCL_054 descending) who commented on the post titled 'Analysing wind data with R'. It joins users, posts, 

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_008\", T1.\"XCL_055\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" INNER JOIN comments AS T3 ON T2.\"XCL_026\" = T3.\"XCL_006\" WHERE T2.\"XCL_035\" = 'Analysing wind data with R' ORDER BY T1.\"XCL_054\" DESC LIMIT 10",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:694"
  ]
}
```

### A query that selects "XCL_055" from the "users" table, applying a filter on "XCL_064" to include only values between 19 and 65 (inclusive). Returns a 

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_055\" FROM users WHERE \"XCL_064\" BETWEEN 19 AND 65",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:676"
  ]
}
```

### A query that retrieves the XCL_055 value from the users table for the row(s) having the maximum XCL_053 value. It uses a subquery to find the max XCL_

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_055\" FROM users WHERE \"XCL_053\" = (SELECT MAX(\"XCL_053\") FROM users)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:674"
  ]
}
```

### Full SQL program that joins users and badges on user ID (XCL_052 = XCL_002), filters for 'Supporter' badges and users aged 19-65, and returns the coun

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'Supporter' AND T1.\"XCL_064\" BETWEEN 19 AND 65",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:619"
  ]
}
```

### Comments for Specific Post Query

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_008\" FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T2.\"XCL_035\" = 'How does gentle boosting differ from AdaBoost?'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:579"
  ]
}
```

### Retrieves the XCL_055 and XCL_064 values for the user(s) with the highest XCL_060 value in the users table. The grain is the specific user record(s) m

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_055\", \"XCL_064\" FROM users WHERE \"XCL_060\" = (SELECT MAX(\"XCL_060\") FROM users)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:643"
  ]
}
```

### A query that retrieves the 'XCL_060' value from the 'users' table by joining it with the 'badges' table on 'XCL_052' (user ID) and 'XCL_002' (badge us

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_060\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_004\" = '2010-07-19 19:39:08.0'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:620"
  ]
}
```

### Average Attributes of High-Activity Users

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T1.\"XCL_061\"), AVG(T1.\"XCL_064\") FROM users AS T1 INNER JOIN (SELECT \"XCL_033\", COUNT(*) AS post_count FROM posts GROUP BY \"XCL_033\" HAVING post_count > 10) AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:604"
  ]
}
```

### Filtered Posts Query

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_038\", \"XCL_037\" FROM posts WHERE \"XCL_035\" = 'Clustering 1D data'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:698"
  ]
}
```

### Badge-to-user aggregation query

```json
{
  "kind": "program",
  "formula": "SELECT CAST(COUNT(T1.\"XCL_001\") AS REAL) / COUNT(DISTINCT T2.\"XCL_055\") FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T2.\"XCL_060\" > 200",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:556"
  ]
}
```

### A SQL program that joins the comments table (T1) to the users table (T2) on T1.XCL_010 = T2.XCL_052. It filters for comments where T1.XCL_008 equals '

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_061\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_008\" = 'R is also lazy evaluated.'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:713"
  ]
}
```

### A query that retrieves the XCL_033 value from the posts table where the XCL_039 value equals the maximum XCL_039 value in the table. This effectively 

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_033\" FROM posts WHERE \"XCL_039\" = (SELECT MAX(\"XCL_039\") FROM posts)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:660"
  ]
}
```

### Filtered Post Aggregation Query

```json
{
  "kind": "program",
  "formula": "SELECT SUM(DISTINCT \"XCL_039\") FROM posts WHERE \"XCL_026\" IN (SELECT \"XCL_014\" FROM postHistory WHERE \"XCL_017\" = 686 AND STRFTIME('%Y', \"XCL_016\") = '2011')",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:603"
  ]
}
```

### SQL program that joins 'posts' and 'users' on 'XCL_033' = 'XCL_052', filters for user 'csgillespie', and returns the sum of 'XCL_038'.

```json
{
  "kind": "program",
  "formula": "SELECT SUM(T1.\"XCL_038\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:542"
  ]
}
```

### Query that selects columns XCL_053 and XCL_060 from the users table where column XCL_055 equals 'Jarrod Dixon'. Returns a single row (or multiple if n

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_053\", \"XCL_060\" FROM users WHERE \"XCL_055\" = 'Jarrod Dixon'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:697"
  ]
}
```

### Retrieves XCL_050 and XCL_051 from the tags table for records where XCL_048 is 'sample'.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_050\", \"XCL_051\" FROM tags WHERE \"XCL_048\" = 'sample'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:704"
  ]
}
```

### A query that joins 'users' and 'posts' on the user ID ('XCL_052' = 'XCL_033') to retrieve user details ('XCL_055', 'XCL_053') for posts where the titl

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_055\", T1.\"XCL_053\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T2.\"XCL_035\" = 'Understanding what Dassault iSight is doing?'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:578"
  ]
}
```

### Executes an inner join between users and votes on users.XCL_052 = votes.XCL_070, filters for users with XCL_055 = 'chl', orders by votes.XCL_069 ascen

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_069\" FROM users AS T1 INNER JOIN votes AS T2 ON T1.\"XCL_052\" = T2.\"XCL_070\" WHERE T1.\"XCL_055\" = 'chl' ORDER BY T2.\"XCL_069\" LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:669"
  ]
}
```

### A query that retrieves the XCL_055 value from the users table for the row(s) having the maximum XCL_060 value. This effectively identifies the user as

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_055\" FROM users WHERE \"XCL_060\" = (SELECT MAX(\"XCL_060\") FROM users)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:534"
  ]
}
```

### Executes an inner join between comments (T1) and posts (T2) on the foreign key relationship (XCL_006 = XCL_026). Filters posts where XCL_031 is less t

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_005\") FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T2.\"XCL_031\" < 5 AND T2.\"XCL_030\" = 0",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:709"
  ]
}
```

### A query that retrieves the XCL_007 identifier from the comments table where the XCL_009 timestamp matches '2010-07-19 19:19:56.0', ensuring the commen

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_007\" FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T1.\"XCL_009\" = '2010-07-19 19:19:56.0'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:616"
  ]
}
```

### A query that retrieves post identifiers ('XCL_032') from the 'posts' table by joining with the 'tags' table. It filters for tags where the 'XCL_048' c

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_032\" FROM tags AS T1 INNER JOIN posts AS T2 ON T2.\"XCL_026\" = T1.\"XCL_050\" WHERE T1.\"XCL_048\" = 'bayesian'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:549"
  ]
}
```

### A query that joins posts, votes, and users to retrieve the user identifier and post title for posts containing 'variance' in the title that have recei

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_055\", T1.\"XCL_035\" FROM posts AS T1 INNER JOIN votes AS T2 ON T1.\"XCL_026\" = T2.\"XCL_067\" INNER JOIN users AS T3 ON T3.\"XCL_052\" = T2.\"XCL_070\" WHERE T2.\"XCL_071\" = 50 AND T1.\"XCL_035\" LIKE '%variance%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:586"
  ]
}
```

### Full SQL program that joins users, postHistory, and posts to retrieve the post ID from postHistory for a specific user nickname, ordered by a timestam

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_014\" FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T2.\"XCL_014\" = T3.\"XCL_026\" WHERE T1.\"XCL_055\" = 'slashnick' ORDER BY T3.\"XCL_037\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:633"
  ]
}
```

### Query returning specific user fields (XCL_056, XCL_058) for users joined to badges where the badge name is 'outliers'. Population: Users associated wi

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_056\", T1.\"XCL_058\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'outliers'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:650"
  ]
}
```

### A SQL program that joins the users table (T1) with the comments table (T2) on the condition that T1."XCL_052" equals T2."XCL_010". It filters for comm

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_052\" = T2.\"XCL_010\" WHERE T2.\"XCL_008\" = 'thank you user93!'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:576"
  ]
}
```

### Executes a count of XCL_047 entries in the tags table filtered by the range of XCL_049 values (5000 to 7000).

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_047\") FROM tags WHERE \"XCL_049\" BETWEEN 5000 AND 7000",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:659"
  ]
}
```

### A query that retrieves the 'XCL_031' value from the 'posts' table by joining it with the 'postLinks' table. The join condition matches 'posts.XCL_026'

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_031\" FROM posts AS T1 INNER JOIN postLinks AS T2 ON T1.\"XCL_026\" = T2.\"XCL_023\" WHERE T2.\"XCL_023\" = 61217",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:600"
  ]
}
```

### Full SQL program that joins 'posts' (T1) and 'votes' (T2) on 'XCL_026' = 'XCL_067', filters posts where 'XCL_035' LIKE '%data%', and computes the SUM 

```json
{
  "kind": "program",
  "formula": "SELECT SUM(T2.\"XCL_071\") FROM posts AS T1 INNER JOIN votes AS T2 ON T1.\"XCL_026\" = T2.\"XCL_067\" WHERE T1.\"XCL_035\" LIKE '%data%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:585"
  ]
}
```

### A query that retrieves badge identifiers for a specific user by joining the badges table to the users table on the user ID (XCL_002 = XCL_052) and fil

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_003\" FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:552"
  ]
}
```

### Executes a SELECT statement on the 'tags' table to compute the count of 'XCL_047' subject to the filters 'XCL_049' <= 20 and 'XCL_047' < 15.

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_047\") FROM tags WHERE \"XCL_049\" <= 20 AND \"XCL_047\" < 15",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:703"
  ]
}
```

### Executes a count aggregation on the comments table, applying a filter condition that XCL_007 must be greater than 60.

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_005\") FROM comments WHERE \"XCL_007\" > 60",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:607"
  ]
}
```

### A query that identifies the single post with the highest value in XCL_039, linked to users who have a date field (XCL_054) in the year 2010. It joins 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_033\", T1.\"XCL_055\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE STRFTIME('%Y', T1.\"XCL_054\") = '2010' ORDER BY T2.\"XCL_039\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:682"
  ]
}
```

### A query that identifies the user associated with the most recent post. It determines the latest post by ordering "posts" by "XCL_031" in descending or

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_055\" FROM users WHERE \"XCL_052\" = (SELECT \"XCL_033\" FROM posts ORDER BY \"XCL_031\" DESC LIMIT 1)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:653"
  ]
}
```

### A query that retrieves the post identifier ("XCL_032") for posts linked to the tag with the maximum value in "XCL_049". It joins the "posts" and "tags

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_032\" FROM posts WHERE \"XCL_026\" = (SELECT \"XCL_050\" FROM tags ORDER BY \"XCL_049\" DESC LIMIT 1)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:550"
  ]
}
```

### A query that retrieves the single post identifier ('XCL_035') from the 'posts' table for the user with username 'csgillespie' (identified by 'XCL_055'

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_035\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie' ORDER BY T1.\"XCL_031\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:540"
  ]
}
```

### A query that joins 'comments' to 'posts' on 'posts.XCL_026' = 'comments.XCL_006', filters for posts where 'XCL_036' is '<humor>', and aggregates the a

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T2.\"XCL_031\"), T2.\"XCL_035\", T1.\"XCL_008\" FROM comments AS T1 INNER JOIN posts AS T2 ON T2.\"XCL_026\" = T1.\"XCL_006\" WHERE T2.\"XCL_036\" = '<humor>' GROUP BY T2.\"XCL_035\", T1.\"XCL_008\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:587"
  ]
}
```

### A query that joins 'posts' and 'users' to retrieve the user identifier ('XCL_055') for a specific post. It filters for the post where 'XCL_035' equals

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_055\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T1.\"XCL_035\" = 'Open source tools for visualizing multi-dimensional data?'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:581"
  ]
}
```

### A complete SQL program that retrieves the count of users from the 'users' table. It applies a filter on the 'XCL_058' column to include only records w

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_052\") FROM users WHERE \"XCL_058\" = 'New York'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:625"
  ]
}
```

### Executes an inner join between posts (T1) and votes (T2) on the post identifier (XCL_026 = XCL_067), filters posts where XCL_035 matches '%data visual

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN votes AS T2 ON T1.\"XCL_026\" = T2.\"XCL_067\" WHERE T1.\"XCL_035\" LIKE '%data visualization%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:569"
  ]
}
```

### A query that retrieves badge identifiers for users in the 'North Pole' location, filtered to badges awarded in 2011. It joins the users and badges tab

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_003\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE STRFTIME('%Y', T2.\"XCL_004\") = '2011' AND T1.\"XCL_058\" = 'North Pole'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:647"
  ]
}
```

### A query that retrieves the 'XCL_055' value for users by joining the 'users' table with the 'badges' table on 'XCL_052' = 'XCL_002' and filtering for b

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'Organizer'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:638"
  ]
}
```

### Full SQL program that joins users and posts on user ID, filters for users in the United Kingdom and posts with a rating >= 4, and returns the count of

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T1.\"XCL_058\" = 'United Kingdom' AND T2.\"XCL_039\" >= 4",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:672"
  ]
}
```

### Comments for Specific Post

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_026\", T1.\"XCL_008\" FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T2.\"XCL_035\" = 'Group differences on a five point Likert item'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:712"
  ]
}
```

### A query that joins users and posts on XCL_052 = XCL_033, filters for posts where the year of XCL_029 is 2011 and XCL_031 is greater than 20000, and re

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE STRFTIME('%Y', T2.\"XCL_029\") = '2011' AND T2.\"XCL_031\" > 20000",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:681"
  ]
}
```

### A query that retrieves user identifiers ('XCL_053') from the 'users' table by joining with the 'posts' table on 'XCL_052' (user ID) and 'XCL_033' (pos

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_053\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T2.\"XCL_026\" = 65041",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:566"
  ]
}
```

### A two-stage aggregation program. First, it groups the "badges" table by "XCL_002" and counts "XCL_003" occurrences. Second, it filters these groups to

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_002\") FROM (SELECT \"XCL_002\", COUNT(\"XCL_003\") AS num FROM badges GROUP BY \"XCL_002\") AS T WHERE T.\"num\" > 5",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:592"
  ]
}
```

### Full SQL program that joins 'posts' and 'users' on 'XCL_040' = 'XCL_052', filters for users with 'XCL_055' = 'Yevgeny', and aggregates the sum of 'XCL

```json
{
  "kind": "program",
  "formula": "SELECT SUM(T1.\"XCL_030\"), T2.\"XCL_057\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_040\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'Yevgeny' GROUP BY T2.\"XCL_057\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:583"
  ]
}
```

### A query that retrieves the identifier of the single post with the highest score (XCL_039) that was voted on by a specific user (XCL_070 = 1465). It jo

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_026\" FROM votes AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_067\" = T2.\"XCL_026\" WHERE T1.\"XCL_070\" = 1465 ORDER BY T2.\"XCL_039\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:666"
  ]
}
```

### Filtered Comment Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_005\") FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T2.\"XCL_038\" = 1 AND T2.\"XCL_030\" = 0",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:710"
  ]
}
```

### Full SQL program joining badges and users to count teacher badges for users located in India. Uses an inner join on badge-user relationship and filter

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_001\") FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T2.\"XCL_058\" = 'India' AND T1.\"XCL_003\" = 'Teacher'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:597"
  ]
}
```

### Filtered User Count Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_052\") FROM users WHERE DATE(\"XCL_056\") > '2014-09-01'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:533"
  ]
}
```

### Executes a count on the 'posts' table applying filters: 'XCL_031' > 35000 and 'XCL_038' = 0. Represents the full computation logic for retrieving this

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_026\") FROM posts WHERE \"XCL_031\" > 35000 AND \"XCL_038\" = 0",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:688"
  ]
}
```

### Full SQL program that joins posts (T1) to users (T2) on the foreign key relationship (XCL_033 = XCL_052), filters for the specific user 'csgillespie' 

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie' AND T1.\"XCL_043\" IS NULL",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:545"
  ]
}
```

### Latest Post User Lookup

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_055\", T2.\"XCL_058\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T1.\"XCL_026\" = 183 ORDER BY T1.\"XCL_041\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:689"
  ]
}
```

### Full SQL program that selects the count of 'XCL_047' from the 'tags' table, applying a filter on 'XCL_048' to include only records with the value 'car

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_047\") FROM tags WHERE \"XCL_048\" = 'careers'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:696"
  ]
}
```

### Full SQL program that joins badges and users on XCL_002 = XCL_052, filters users where XCL_055 equals 'Zolomon', and returns the difference XCL_004 - 

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_004\" - T2.\"XCL_054\" FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'Zolomon'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:692"
  ]
}
```

### A query that retrieves the 'XCL_026' and 'XCL_035' values from the 'posts' table for the single most recent post (determined by descending order of 'X

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_026\", T2.\"XCL_035\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T1.\"XCL_055\" = 'Harvey Motulsky' ORDER BY T2.\"XCL_031\" DESC LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:678"
  ]
}
```

### A query that retrieves the XCL_008 identifier from the comments table where the XCL_009 timestamp matches '2010-07-19 19:37:33.0', joined with the pos

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_008\" FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T1.\"XCL_009\" = '2010-07-19 19:37:33.0'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:617"
  ]
}
```

### A query that retrieves badge identifiers ('XCL_003') for users ('users' table) where the user attribute 'XCL_055' equals 'Sharpie'. It joins the 'user

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_003\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_055\" = 'Sharpie'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:622"
  ]
}
```

### 2013 Samuel Post-Badge Association Query

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_014\", T2.\"XCL_003\" FROM postHistory AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE T1.\"XCL_020\" = 'Samuel' AND STRFTIME('%Y', T1.\"XCL_016\") = '2013' AND STRFTIME('%Y', T2.\"XCL_004\") = '2013'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:652"
  ]
}
```

### Executes a join between badges and users tables to count badges for a specific user identified by the literal 'csgillespie'.

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_001\") FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:551"
  ]
}
```

### A query that joins the comments table to the users table on the user ID (XCL_010 in comments to XCL_052 in users) and filters for comments where the c

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_053\", T2.\"XCL_061\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_008\" = 'fine, you win :)'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:705"
  ]
}
```

### A query that retrieves badge identifiers for a specific user by joining the users and badges tables on the user ID (XCL_052 = XCL_002) and filtering b

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_003\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_055\" = 'DatEpicCoderGuyWhoPrograms'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:570"
  ]
}
```

### Executes a scalar aggregation on the 'comments' table. It applies a filter on 'XCL_010' (value 13) and returns a single count of 'XCL_005' entries mat

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_005\") FROM comments WHERE \"XCL_010\" = 13",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:588"
  ]
}
```

### A query that joins users and badges to find the user associated with the 'Autobiographer' badge. It filters for the specific badge name, orders the re

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'Autobiographer' ORDER BY T2.\"XCL_004\" LIMIT 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:671"
  ]
}
```

### A query that retrieves the XCL_026 values from the posts table for records where the XCL_031 value exceeds the global average of XCL_031.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_026\" FROM posts WHERE \"XCL_031\" > (SELECT AVG(\"XCL_031\") FROM posts)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:686"
  ]
}
```

### A program that joins the posts table (T1) with the postHistory table (T2) on T1.XCL_026 = T2.XCL_014. It filters for the post where T1.XCL_035 equals 

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_019\" FROM posts AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_035\" = 'Why square the difference instead of taking the absolute value in standard deviation?'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:584"
  ]
}
```

### A query that identifies the user (by "XCL_055" and "XCL_057") who cast the highest-ranked vote (by "XCL_071" DESC) for the entity where "XCL_068" is 8

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_055\", \"XCL_057\" FROM users WHERE \"XCL_052\" = (SELECT \"XCL_070\" FROM votes WHERE \"XCL_068\" = 8 ORDER BY \"XCL_071\" DESC LIMIT 1)",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:657"
  ]
}
```

### Full SQL program that selects the count of 'XCL_001' from the 'badges' table, applying a filter on 'XCL_003' to include only records with the value 'A

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_001\") FROM badges WHERE \"XCL_003\" = 'Announcer'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:605"
  ]
}
```

### Executes a count on the users table, applying filters on the year of XCL_054 (> 2013) and the value of XCL_060 (> 10).

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_052\") FROM users WHERE STRFTIME('%Y', \"XCL_054\") > '2013' AND \"XCL_060\" > 10",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:536"
  ]
}
```

### A SQL program that joins 'users' and 'posts' on 'XCL_052' = 'XCL_033', filters for the user 'Stephen Turner' via 'XCL_055', and computes the average o

```json
{
  "kind": "program",
  "formula": "SELECT AVG(T2.\"XCL_030\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T1.\"XCL_055\" = 'Stephen Turner'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:680"
  ]
}
```

### Full SQL program that joins posts and votes on post ID, filters for votes with value 50 in 2011, and returns the total count of matching posts.

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN votes AS T2 ON T1.\"XCL_026\" = T2.\"XCL_067\" WHERE T2.\"XCL_071\" = 50 AND STRFTIME('%Y', T2.\"XCL_069\") = '2011'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:662"
  ]
}
```

### Daily Post History Query

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_012\") FROM postHistory WHERE DATE(\"XCL_016\") = '2010-07-21'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:642"
  ]
}
```

### A query that joins posts (T1) and postLinks (T2) on T1.XCL_026 = T2.XCL_023. It filters for records where T2.XCL_023 is 395 and returns the correspond

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_030\", T2.\"XCL_025\" FROM posts AS T1 INNER JOIN postLinks AS T2 ON T1.\"XCL_026\" = T2.\"XCL_023\" WHERE T2.\"XCL_023\" = 395",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:601"
  ]
}
```

### A query that retrieves badge identifiers for users whose location (XCL_058) is 'Rochester, NY'. It joins the users table (T1) with the badges table (T

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_004\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_058\" = 'Rochester, NY'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:613"
  ]
}
```

### Full SQL program joining comments (T1) and users (T2) on T1.XCL_010 = T2.XCL_052, filtering for comments where T1.XCL_008 contains 'http://', and sele

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_054\", T2.\"XCL_064\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_008\" LIKE '%http://%'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:708"
  ]
}
```

### Executes a full-table scan on the 'users' table to compute the percentage of records where 'XCL_064' falls within the range [13, 18]. It uses conditio

```json
{
  "kind": "program",
  "formula": "SELECT CAST(SUM(IIF(\"XCL_064\" BETWEEN 13 AND 18, 1, 0)) AS REAL) * 100 / COUNT(\"XCL_052\") FROM users",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:684"
  ]
}
```

### A query that retrieves the titles of all posts linked to by a specific source post. It joins the postLinks table to the posts table twice: once to ide

```json
{
  "kind": "program",
  "formula": "SELECT T3.\"XCL_035\" FROM postLinks AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_023\" = T2.\"XCL_026\" INNER JOIN posts AS T3 ON T1.\"XCL_024\" = T3.\"XCL_026\" WHERE T2.\"XCL_035\" = 'How to tell if something happened in a data set which monitors a value over time'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:651"
  ]
}
```

### A query that retrieves user identifiers ('XCL_055') from the 'users' table. It joins 'comments' to 'users' on 'XCL_010' (comment author) and 'XCL_052'

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_055\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_007\" BETWEEN 1 AND 5 AND T2.\"XCL_062\" = 0",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:715"
  ]
}
```

### SQL program that calculates the count of users from the 'users' table, applying filters on columns 'XCL_053' (> 2000) and 'XCL_060' (> 1000).

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(\"XCL_052\") FROM users WHERE \"XCL_053\" > 2000 AND \"XCL_060\" > 1000",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:675"
  ]
}
```

### Full SQL program joining users, posts, and comments to count comments where the user name is 'Neil McGuigan' and the comment attribute XCL_007 is less

```json
{
  "kind": "program",
  "formula": "SELECT COUNT(T3.\"XCL_005\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" INNER JOIN comments AS T3 ON T2.\"XCL_026\" = T3.\"XCL_006\" WHERE T1.\"XCL_055\" = 'Neil McGuigan' AND T3.\"XCL_007\" < 60",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:636"
  ]
}
```

### A program that joins users, postHistory, and posts to identify users who have contributed to high-scoring posts (score >= 1000) but have only one dist

```json
{
  "kind": "program",
  "formula": "SELECT T2.\"XCL_017\" FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T2.\"XCL_014\" = T3.\"XCL_026\" WHERE T3.\"XCL_031\" >= 1000 GROUP BY T2.\"XCL_017\" HAVING COUNT(DISTINCT T2.\"XCL_013\") = 1",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:595"
  ]
}
```

### A query that retrieves the 'XCL_008' values from the 'comments' table for all comments made by the user whose 'XCL_055' value is 'Harvey Motulsky'. It

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_008\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'Harvey Motulsky'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:714"
  ]
}
```

### A query that retrieves the identifier of a specific post from the 'posts' table by matching the exact string value in column XCL_035.

```json
{
  "kind": "program",
  "formula": "SELECT \"XCL_031\" FROM posts WHERE \"XCL_035\" = 'Integration of Weka and/or RapidMiner into Informatica PowerCenter/Developer'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:572"
  ]
}
```

### A query that joins the 'users' and 'badges' tables on the user ID ('XCL_052' in users, 'XCL_002' in badges). It filters for badges awarded at the spec

```json
{
  "kind": "program",
  "formula": "SELECT T1.\"XCL_053\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_004\" = '2010-07-19 19:39:08.0'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:611"
  ]
}
```

### Post Attribute

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_052\", T2.\"XCL_035\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" ORDER BY T2.\"XCL_030\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:679"
  ]
}
```

### STRFTIME('%Y', "posts"."XCL_029") = '2011' AND "posts"."XCL_031" > 20000

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"posts\".\"XCL_029\") = '2011' AND \"posts\".\"XCL_031\" > 20000",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE STRFTIME('%Y', T2.\"XCL_029\") = '2011' AND T2.\"XCL_031\" > 20000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:681"
  ]
}
```

### Post Identifier

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_031\" FROM posts WHERE \"XCL_035\" = 'Integration of Weka and/or RapidMiner into Informatica PowerCenter/Developer'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_031\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_031\" AS \"value\" FROM posts AS \"r0\" WHERE \"r0\".\"XCL_035\" = 'Integration of Weka and/or RapidMiner into Informatica PowerCenter/Developer'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:572"
  ]
}
```

### Post ID in Score Range

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_026\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_026\" FROM posts WHERE \"XCL_031\" BETWEEN 100 AND 150",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_026\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_026\" AS \"value\" FROM posts AS \"r0\" WHERE \"r0\".\"XCL_031\" BETWEEN 100 AND 150",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:707"
  ]
}
```

### Calculates the percentage of post history entries associated with tags where 'XCL_048' is 'r', relative to the total count of user IDs ('XCL_052') in 

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(\"tags\".\"XCL_048\" = 'r', 1, 0)) AS REAL) * 100 / COUNT(\"users\".\"XCL_052\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(T3.\"XCL_048\" = 'r', 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN tags AS T3 ON T3.\"XCL_050\" = T2.\"XCL_014\" WHERE T1.\"XCL_055\" = 'Community'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(IIF(\"r2\".\"XCL_048\" = 'r', 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_052\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "postHistory"
      },
      {
        "role": "r2",
        "physical_table": "tags"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(IIF(\"r2\".\"XCL_048\" = 'r', 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_052\") AS \"value\" FROM users AS \"r0\" INNER JOIN postHistory AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_017\" INNER JOIN tags AS \"r2\" ON \"r2\".\"XCL_050\" = \"r1\".\"XCL_014\" WHERE \"r0\".\"XCL_055\" = 'Community'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:639"
  ]
}
```

### "posts"."XCL_035" = 'Why square the difference instead of taking the absolute value in standard deviation?'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_035\" = 'Why square the difference instead of taking the absolute value in standard deviation?'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_019\" FROM posts AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_035\" = 'Why square the difference instead of taking the absolute value in standard deviation?'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:584"
  ]
}
```

### Badge Identifier

```json
{
  "kind": "binding",
  "formula": "\"badges\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_055\" = 'DatEpicCoderGuyWhoPrograms'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_003\" AS \"value\" FROM users AS \"r0\" INNER JOIN badges AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_002\" WHERE \"r0\".\"XCL_055\" = 'DatEpicCoderGuyWhoPrograms'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:570"
  ]
}
```

### "users"."XCL_058" = 'Rochester, NY'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_058\" = 'Rochester, NY'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_004\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_058\" = 'Rochester, NY'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:613"
  ]
}
```

### The value of the 'XCL_055' column from the 'users' table. This represents a specific user attribute (likely a user ID or name) for users who have auth

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_055\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_007\" BETWEEN 1 AND 5 AND T2.\"XCL_062\" = 0",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_055\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_055\" AS \"value\" FROM comments AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_052\" WHERE \"r0\".\"XCL_007\" BETWEEN 1 AND 5 AND \"r1\".\"XCL_062\" = 0",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:715"
  ]
}
```

### "votes"."XCL_070" = 58 AND "votes"."XCL_069" = '2010-07-19'

```json
{
  "kind": "predicate",
  "formula": "\"votes\".\"XCL_070\" = 58 AND \"votes\".\"XCL_069\" = '2010-07-19'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_066\") FROM votes WHERE \"XCL_070\" = 58 AND \"XCL_069\" = '2010-07-19'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:558"
  ]
}
```

### Calculates the difference in percentage points between the proportion of badges issued in 2010 and the proportion issued in 2011. The population is re

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(STRFTIME('%Y', \"badges\".\"XCL_004\") = '2010', 1, 0)) AS REAL) * 100 / COUNT(\"badges\".\"XCL_001\") - CAST(SUM(IIF(STRFTIME('%Y', \"badges\".\"XCL_004\") = '2011', 1, 0)) AS REAL) * 100 / COUNT(\"badges\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(STRFTIME('%Y', \"XCL_004\") = '2010', 1, 0)) AS REAL) * 100 / COUNT(\"XCL_001\") - CAST(SUM(IIF(STRFTIME('%Y', \"XCL_004\") = '2011', 1, 0)) AS REAL) * 100 / COUNT(\"XCL_001\") FROM badges WHERE \"XCL_003\" = 'Student'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(IIF(STRFTIME('%Y', \"r0\".\"XCL_004\") = '2010', 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\") - CAST(SUM(IIF(STRFTIME('%Y', \"r0\".\"XCL_004\") = '2011', 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(IIF(STRFTIME('%Y', \"r0\".\"XCL_004\") = '2010', 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\") - CAST(SUM(IIF(STRFTIME('%Y', \"r0\".\"XCL_004\") = '2011', 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM badges AS \"r0\" WHERE \"r0\".\"XCL_003\" = 'Student'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:598"
  ]
}
```

### Returns the single comment identifier (XCL_008) from the comments table that belongs to a post in the filtered set, ordered by the comment's ranking f

```json
{
  "kind": "binding",
  "formula": "\"comments\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_008\" FROM comments WHERE \"XCL_006\" IN (SELECT \"XCL_026\" FROM posts WHERE \"XCL_031\" BETWEEN 100 AND 150) ORDER BY \"XCL_007\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:707"
  ]
}
```

### Badge Identifier

```json
{
  "kind": "binding",
  "formula": "\"badges\".\"XCL_004\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_004\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_058\" = 'Rochester, NY'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_004\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_004\" AS \"value\" FROM users AS \"r0\" INNER JOIN badges AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_002\" WHERE \"r0\".\"XCL_058\" = 'Rochester, NY'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:613"
  ]
}
```

### Aggregates the count of post identifiers (XCL_026) from the posts table that have at least one matching record in the comments table via the join cond

```json
{
  "kind": "metric",
  "formula": "COUNT(\"posts\".\"XCL_026\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_026\" = T2.\"XCL_006\" WHERE T1.\"XCL_031\" = 1910",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_026\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "comments"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_026\") AS \"value\" FROM posts AS \"r0\" INNER JOIN comments AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_006\" WHERE \"r0\".\"XCL_031\" = 1910",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:562"
  ]
}
```

### Aggregates the total number of comment records (identified by XCL_005) associated with posts that have a score (XCL_031) less than 5 and an active sta

```json
{
  "kind": "metric",
  "formula": "COUNT(\"comments\".\"XCL_005\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_005\") FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T2.\"XCL_031\" < 5 AND T2.\"XCL_030\" = 0",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_005\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_005\") AS \"value\" FROM comments AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_006\" = \"r1\".\"XCL_026\" WHERE \"r1\".\"XCL_031\" < 5 AND \"r1\".\"XCL_030\" = 0",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:709"
  ]
}
```

### "users"."XCL_055" = 'csgillespie'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'csgillespie'",
  "grain": [],
  "population_scope": "SELECT SUM(T1.\"XCL_038\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:542"
  ]
}
```

### A set of post identifiers (XCL_014) extracted from the postHistory table. The population is restricted to history records where XCL_017 equals 686 and

```json
{
  "kind": "binding",
  "formula": "\"postHistory\".\"XCL_014\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_014\" FROM postHistory WHERE \"XCL_017\" = 686 AND STRFTIME('%Y', \"XCL_016\") = '2011'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_014\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "postHistory"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_014\" AS \"value\" FROM postHistory AS \"r0\" WHERE \"r0\".\"XCL_017\" = 686 AND STRFTIME('%Y', \"r0\".\"XCL_016\") = '2011'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:603"
  ]
}
```

### "badges"."XCL_003" = 'Teacher'

```json
{
  "kind": "predicate",
  "formula": "\"badges\".\"XCL_003\" = 'Teacher'",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(T1.\"XCL_052\") AS REAL) * 100 / (SELECT COUNT(\"XCL_052\") FROM users) FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'Teacher'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:614"
  ]
}
```

### Aggregates the total number of rows in the 'posts' table where the value in column 'XCL_030' is strictly less than 20. The metric counts non-null valu

```json
{
  "kind": "metric",
  "formula": "COUNT(\"posts\".\"XCL_026\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_026\") FROM posts WHERE \"XCL_030\" < 20",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_026\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_026\") AS \"value\" FROM posts AS \"r0\" WHERE \"r0\".\"XCL_030\" < 20",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:702"
  ]
}
```

### The value of column "XCL_069" from the "votes" table that corresponds to the group with the highest count of "XCL_066" entries. Returns a single scala

```json
{
  "kind": "binding",
  "formula": "\"votes\".\"XCL_069\"",
  "grain": [
    "\"votes\".\"XCL_069\""
  ],
  "population_scope": "SELECT \"XCL_069\" FROM votes GROUP BY \"XCL_069\" ORDER BY COUNT(\"XCL_066\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:559"
  ]
}
```

### A scalar metric representing the sum of distinct values of XCL_039 from the posts table. The population is limited to posts where XCL_026 matches any 

```json
{
  "kind": "metric",
  "formula": "SUM(DISTINCT \"posts\".\"XCL_039\")",
  "grain": [],
  "population_scope": "SELECT SUM(DISTINCT \"XCL_039\") FROM posts WHERE \"XCL_026\" IN (SELECT \"XCL_014\" FROM postHistory WHERE \"XCL_017\" = 686 AND STRFTIME('%Y', \"XCL_016\") = '2011')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:603"
  ]
}
```

### "comments"."XCL_008" LIKE '%http://%'

```json
{
  "kind": "predicate",
  "formula": "\"comments\".\"XCL_008\" LIKE '%http://%'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_054\", T2.\"XCL_064\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_008\" LIKE '%http://%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:708"
  ]
}
```

### "badges"."XCL_003" = 'Citizen Patrol'

```json
{
  "kind": "predicate",
  "formula": "\"badges\".\"XCL_003\" = 'Citizen Patrol'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM badges WHERE \"XCL_003\" = 'Citizen Patrol'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:695"
  ]
}
```

### "users"."XCL_055" = 'Stephen Turner'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'Stephen Turner'",
  "grain": [],
  "population_scope": "SELECT AVG(T2.\"XCL_030\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T1.\"XCL_055\" = 'Stephen Turner'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:680"
  ]
}
```

### Post Identifier

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T2.\"XCL_011\" FROM posts AS T1 INNER JOIN comments AS T2 ON T2.\"XCL_006\" = T2.\"XCL_005\" WHERE T1.\"XCL_030\" > 60",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "comments"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_035\" AS \"value\" FROM posts AS \"r0\" INNER JOIN comments AS \"r1\" ON \"r1\".\"XCL_006\" = \"r1\".\"XCL_005\" WHERE \"r0\".\"XCL_030\" > 60",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:646"
  ]
}
```

### "users"."XCL_052" = 30

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_052\" = 30",
  "grain": [],
  "population_scope": "SELECT \"XCL_055\" FROM users WHERE \"XCL_052\" = 30",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:624"
  ]
}
```

### Average User Attribute XCL_061

```json
{
  "kind": "metric",
  "formula": "AVG(T1.\"XCL_061\")",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_061\"), AVG(T1.\"XCL_064\") FROM users AS T1 INNER JOIN (SELECT \"XCL_033\", COUNT(*) AS post_count FROM posts GROUP BY \"XCL_033\" HAVING post_count > 10) AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\"",
  "upstream_scopes": [
    "SELECT \"XCL_033\", COUNT(*) AS post_count FROM posts GROUP BY \"XCL_033\" HAVING post_count > 10"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:604"
  ]
}
```

### The value of column XCL_055 from the users table, representing the user associated with the post.

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_031\", T3.\"XCL_055\" FROM postHistory AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_014\" = T2.\"XCL_026\" INNER JOIN users AS T3 ON T2.\"XCL_040\" = T3.\"XCL_052\" WHERE T1.\"XCL_018\" = 'Computer Game Datasets'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_055\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "postHistory"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      },
      {
        "role": "r2",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_055\" AS \"value\" FROM postHistory AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_014\" = \"r1\".\"XCL_026\" INNER JOIN users AS \"r2\" ON \"r1\".\"XCL_040\" = \"r2\".\"XCL_052\" WHERE \"r0\".\"XCL_018\" = 'Computer Game Datasets'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:685"
  ]
}
```

### Counts the number of unique badge identifiers (XCL_001) from the badges table. The population is restricted to badges with a type (XCL_003) of 'Suppor

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"badges\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_001\") FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T1.\"XCL_003\" IN ('Supporter', 'Teacher') AND T2.\"XCL_058\" = 'New York'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "badges"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r0\".\"XCL_001\") AS \"value\" FROM badges AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_052\" WHERE \"r0\".\"XCL_003\" IN ('Supporter', 'Teacher') AND \"r1\".\"XCL_058\" = 'New York'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:593"
  ]
}
```

### The value of attribute XCL_053 for users who have authored at least one comment where the comment attribute XCL_006 equals 1. Returned at the grain of

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_053\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_052\", T2.\"XCL_053\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_006\" = 1",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_053\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_053\" AS \"value\" FROM comments AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_052\" WHERE \"r0\".\"XCL_006\" = 1",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:594"
  ]
}
```

### Badge Identifier

```json
{
  "kind": "binding",
  "formula": "\"badges\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" ORDER BY T1.\"XCL_053\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:610"
  ]
}
```

### "comments"."XCL_009" = '2010-07-19 19:37:33.0'

```json
{
  "kind": "predicate",
  "formula": "\"comments\".\"XCL_009\" = '2010-07-19 19:37:33.0'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_008\" FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T1.\"XCL_009\" = '2010-07-19 19:37:33.0'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:617"
  ]
}
```

### "badges"."XCL_003" = 'Commentator' AND STRFTIME('%Y', "badges"."XCL_004") = '2014'

```json
{
  "kind": "predicate",
  "formula": "\"badges\".\"XCL_003\" = 'Commentator' AND STRFTIME('%Y', \"badges\".\"XCL_004\") = '2014'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM badges WHERE \"XCL_003\" = 'Commentator' AND STRFTIME('%Y', \"XCL_004\") = '2014'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:641"
  ]
}
```

### NOT "posts"."XCL_043" IS NULL

```json
{
  "kind": "predicate",
  "formula": "NOT \"posts\".\"XCL_043\" IS NULL",
  "grain": [],
  "population_scope": "SELECT \"XCL_033\" FROM posts WHERE NOT \"XCL_043\" IS NULL ORDER BY \"XCL_030\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:656"
  ]
}
```

### "votes"."XCL_066" = 6347

```json
{
  "kind": "predicate",
  "formula": "\"votes\".\"XCL_066\" = 6347",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN votes AS T2 ON T1.\"XCL_052\" = T2.\"XCL_070\" WHERE T2.\"XCL_066\" = 6347",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:568"
  ]
}
```

### Aggregated sum of the 'XCL_038' column from the 'posts' table, filtered to posts associated with the user identified by 'XCL_055' = 'csgillespie' in t

```json
{
  "kind": "metric",
  "formula": "SUM(\"posts\".\"XCL_038\")",
  "grain": [],
  "population_scope": "SELECT SUM(T1.\"XCL_038\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r0\".\"XCL_038\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT SUM(\"r0\".\"XCL_038\") AS \"value\" FROM posts AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_033\" = \"r1\".\"XCL_052\" WHERE \"r1\".\"XCL_055\" = 'csgillespie'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:542"
  ]
}
```

### Returns the value of column "XCL_055" from the "users" table for records where "XCL_052" equals 30. The grain is individual user records filtered by t

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_055\" FROM users WHERE \"XCL_052\" = 30",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_055\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_055\" AS \"value\" FROM users AS \"r0\" WHERE \"r0\".\"XCL_052\" = 30",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:624"
  ]
}
```

### The value of column XCL_055 from the users table, representing the specific user associated with the vote filtered by XCL_066 = 6347.

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN votes AS T2 ON T1.\"XCL_052\" = T2.\"XCL_070\" WHERE T2.\"XCL_066\" = 6347",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_055\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "votes"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_055\" AS \"value\" FROM users AS \"r0\" INNER JOIN votes AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_070\" WHERE \"r1\".\"XCL_066\" = 6347",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:568"
  ]
}
```

### Minimum XCL_060 Value

```json
{
  "kind": "metric",
  "formula": "MIN(\"users\".\"XCL_060\")",
  "grain": [],
  "population_scope": "SELECT MIN(\"XCL_060\") FROM users",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MIN(\"r0\".\"XCL_060\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT MIN(\"r0\".\"XCL_060\") AS \"value\" FROM users AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:590"
  ]
}
```

### The value of the 'XCL_055' column from the 'users' table. It represents the specific user associated with the post filtered by the title 'Examples for

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_055\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_040\" = T2.\"XCL_052\" WHERE T1.\"XCL_035\" = 'Examples for teaching: Correlation does not mean causation'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_055\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_055\" AS \"value\" FROM posts AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_040\" = \"r1\".\"XCL_052\" WHERE \"r0\".\"XCL_035\" = 'Examples for teaching: Correlation does not mean causation'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:544"
  ]
}
```

### Comment Count per Post

```json
{
  "kind": "metric",
  "formula": "COUNT(\"comments\".\"XCL_005\")",
  "grain": [
    "\"posts\".\"XCL_026\""
  ],
  "population_scope": "SELECT COUNT(T2.\"XCL_005\") FROM posts AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_026\" = T2.\"XCL_006\" GROUP BY T1.\"XCL_026\" ORDER BY SUM(T1.\"XCL_030\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:687"
  ]
}
```

### Attribute from the 'postHistory' table (column XCL_017) associated with the filtered history records.

```json
{
  "kind": "binding",
  "formula": "\"postHistory\".\"XCL_017\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_014\", \"XCL_017\" FROM postHistory WHERE \"XCL_014\" IN (SELECT \"XCL_026\" FROM posts WHERE \"XCL_030\" > 60)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:602"
  ]
}
```

### Aggregates the total number of rows in the 'posts' table where 'XCL_031' is greater than 35000 and 'XCL_038' equals 0. Returns a single scalar count.

```json
{
  "kind": "metric",
  "formula": "COUNT(\"posts\".\"XCL_026\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_026\") FROM posts WHERE \"XCL_031\" > 35000 AND \"XCL_038\" = 0",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_026\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_026\") AS \"value\" FROM posts AS \"r0\" WHERE \"r0\".\"XCL_031\" > 35000 AND \"r0\".\"XCL_038\" = 0",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:688"
  ]
}
```

### Post Identifier

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_031\" FROM posts AS T1 INNER JOIN postLinks AS T2 ON T1.\"XCL_026\" = T2.\"XCL_023\" WHERE T2.\"XCL_023\" = 61217",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_031\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "postLinks"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_031\" AS \"value\" FROM posts AS \"r0\" INNER JOIN postLinks AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_023\" WHERE \"r1\".\"XCL_023\" = 61217",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:600"
  ]
}
```

### "users"."XCL_055" = 'Emmett'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'Emmett'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\" FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'Emmett' ORDER BY T1.\"XCL_004\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:690"
  ]
}
```

### "users"."XCL_064" BETWEEN 19 AND 65

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_064\" BETWEEN 19 AND 65",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_052\") FROM users WHERE \"XCL_064\" BETWEEN 19 AND 65",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:627"
  ]
}
```

### Post Identifier

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_032\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_032\" FROM tags AS T1 INNER JOIN posts AS T2 ON T2.\"XCL_026\" = T1.\"XCL_050\" WHERE T1.\"XCL_048\" = 'bayesian'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_032\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "tags"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_032\" AS \"value\" FROM tags AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r1\".\"XCL_026\" = \"r0\".\"XCL_050\" WHERE \"r0\".\"XCL_048\" = 'bayesian'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:549"
  ]
}
```

### "posts"."XCL_031" > 35000 AND "posts"."XCL_038" = 0

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_031\" > 35000 AND \"posts\".\"XCL_038\" = 0",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_026\") FROM posts WHERE \"XCL_031\" > 35000 AND \"XCL_038\" = 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:688"
  ]
}
```

### COUNT("votes"."XCL_066") > 4

```json
{
  "kind": "predicate",
  "formula": "COUNT(\"votes\".\"XCL_066\") > 4",
  "grain": [
    "\"postHistory\".\"XCL_014\"",
    "\"votes\".\"XCL_066\""
  ],
  "population_scope": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T2.\"XCL_014\" = T3.\"XCL_026\" INNER JOIN votes AS T4 ON T4.\"XCL_067\" = T3.\"XCL_026\" WHERE T1.\"XCL_055\" = 'Matt Parker' GROUP BY T2.\"XCL_014\", T4.\"XCL_066\" HAVING COUNT(T4.\"XCL_066\") > 4",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:635"
  ]
}
```

### Value of column XCL_012 from the postHistory table, representing a specific attribute of the post history record associated with the filtered post.

```json
{
  "kind": "binding",
  "formula": "\"postHistory\".\"XCL_012\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_012\", T2.\"XCL_041\" FROM postHistory AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_014\" = T2.\"XCL_026\" WHERE T2.\"XCL_035\" = 'What is the best introductory Bayesian statistics textbook?'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_012\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "postHistory"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_012\" AS \"value\" FROM postHistory AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_014\" = \"r1\".\"XCL_026\" WHERE \"r1\".\"XCL_035\" = 'What is the best introductory Bayesian statistics textbook?'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:649"
  ]
}
```

### Post Identifier

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_031\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_031\", T3.\"XCL_055\" FROM postHistory AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_014\" = T2.\"XCL_026\" INNER JOIN users AS T3 ON T2.\"XCL_040\" = T3.\"XCL_052\" WHERE T1.\"XCL_018\" = 'Computer Game Datasets'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_031\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "postHistory"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      },
      {
        "role": "r2",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_031\" AS \"value\" FROM postHistory AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_014\" = \"r1\".\"XCL_026\" INNER JOIN users AS \"r2\" ON \"r1\".\"XCL_040\" = \"r2\".\"XCL_052\" WHERE \"r0\".\"XCL_018\" = 'Computer Game Datasets'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:685"
  ]
}
```

### Aggregates the total number of rows in the 'posts' table where the column 'XCL_030' equals 10. The metric counts the 'XCL_026' identifier, effectively

```json
{
  "kind": "metric",
  "formula": "COUNT(\"posts\".\"XCL_026\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_026\") FROM posts WHERE \"XCL_030\" = 10",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_026\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_026\") AS \"value\" FROM posts AS \"r0\" WHERE \"r0\".\"XCL_030\" = 10",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:609"
  ]
}
```

### Max Post ID for User

```json
{
  "kind": "metric",
  "formula": "MAX(\"posts\".\"XCL_037\")",
  "grain": [],
  "population_scope": "SELECT MAX(T1.\"XCL_037\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MAX(\"r0\".\"XCL_037\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT MAX(\"r0\".\"XCL_037\") AS \"value\" FROM posts AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_033\" = \"r1\".\"XCL_052\" WHERE \"r1\".\"XCL_055\" = 'csgillespie'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:543"
  ]
}
```

### Badge Identifier

```json
{
  "kind": "binding",
  "formula": "\"badges\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_003\" FROM badges WHERE \"XCL_004\" = '2010-07-19 19:39:08.0'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_003\" AS \"value\" FROM badges AS \"r0\" WHERE \"r0\".\"XCL_004\" = '2010-07-19 19:39:08.0'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:606"
  ]
}
```

### DATE("postHistory"."XCL_016") = '2010-07-21'

```json
{
  "kind": "predicate",
  "formula": "DATE(\"postHistory\".\"XCL_016\") = '2010-07-21'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_012\") FROM postHistory WHERE DATE(\"XCL_016\") = '2010-07-21'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:642"
  ]
}
```

### Calculates the percentage of rows in the 'users' table where the value of column 'XCL_064' is between 13 and 18 (inclusive). The numerator counts rows

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(\"users\".\"XCL_064\" BETWEEN 13 AND 18, 1, 0)) AS REAL) * 100 / COUNT(\"users\".\"XCL_052\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(\"XCL_064\" BETWEEN 13 AND 18, 1, 0)) AS REAL) * 100 / COUNT(\"XCL_052\") FROM users",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(IIF(\"r0\".\"XCL_064\" BETWEEN 13 AND 18, 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_052\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(IIF(\"r0\".\"XCL_064\" BETWEEN 13 AND 18, 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_052\") AS \"value\" FROM users AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:684"
  ]
}
```

### "posts"."XCL_035" = 'Eliciting priors from experts'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_035\" = 'Eliciting priors from experts'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_055\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T1.\"XCL_035\" = 'Eliciting priors from experts'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:539"
  ]
}
```

### The value of column "XCL_055" from the "users" table for the specific user whose "XCL_052" matches the latest post identifier. This returns the user i

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_055\" FROM users WHERE \"XCL_052\" = (SELECT \"XCL_033\" FROM posts ORDER BY \"XCL_031\" DESC LIMIT 1)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:653"
  ]
}
```

### Returns the value of "XCL_070" from the "votes" table for the single row where "XCL_068" equals 8, ordered by "XCL_071" in descending order. This repr

```json
{
  "kind": "binding",
  "formula": "\"votes\".\"XCL_070\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_070\" FROM votes WHERE \"XCL_068\" = 8 ORDER BY \"XCL_071\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:657"
  ]
}
```

### Max XCL_060

```json
{
  "kind": "metric",
  "formula": "MAX(\"users\".\"XCL_060\")",
  "grain": [],
  "population_scope": "SELECT MAX(\"XCL_060\") FROM users",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MAX(\"r0\".\"XCL_060\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT MAX(\"r0\".\"XCL_060\") AS \"value\" FROM users AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:643",
    "bird_dev:534",
    "bird_dev:628"
  ]
}
```

### "badges"."XCL_003" = 'Autobiographer'

```json
{
  "kind": "predicate",
  "formula": "\"badges\".\"XCL_003\" = 'Autobiographer'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'Autobiographer' ORDER BY T2.\"XCL_004\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:671"
  ]
}
```

### STRFTIME('%Y', "posts"."XCL_029") = '2010' AND "users"."XCL_055" = 'Jay Stevens'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"posts\".\"XCL_029\") = '2010' AND \"users\".\"XCL_055\" = 'Jay Stevens'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE STRFTIME('%Y', T2.\"XCL_029\") = '2010' AND T1.\"XCL_055\" = 'Jay Stevens'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:677"
  ]
}
```

### DATE("users"."XCL_056") > '2014-09-01'

```json
{
  "kind": "predicate",
  "formula": "DATE(\"users\".\"XCL_056\") > '2014-09-01'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_052\") FROM users WHERE DATE(\"XCL_056\") > '2014-09-01'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:533"
  ]
}
```

### Post Identifier

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_035\" FROM posts WHERE \"XCL_026\" = (SELECT \"XCL_006\" FROM comments ORDER BY \"XCL_007\" DESC LIMIT 1)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:561"
  ]
}
```

### Post Identifier

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie' ORDER BY T1.\"XCL_031\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:540"
  ]
}
```

### Aggregates the total number of comments (counting XCL_005) associated with posts that satisfy specific status conditions (XCL_038 = 1 and XCL_030 = 0)

```json
{
  "kind": "metric",
  "formula": "COUNT(\"comments\".\"XCL_005\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_005\") FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T2.\"XCL_038\" = 1 AND T2.\"XCL_030\" = 0",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_005\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_005\") AS \"value\" FROM comments AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_006\" = \"r1\".\"XCL_026\" WHERE \"r1\".\"XCL_038\" = 1 AND \"r1\".\"XCL_030\" = 0",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:710"
  ]
}
```

### Average votes per post for post 24

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(\"posts\".\"XCL_026\") AS REAL) / COUNT(DISTINCT \"votes\".\"XCL_066\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(T2.\"XCL_026\") AS REAL) / COUNT(DISTINCT T1.\"XCL_066\") FROM votes AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_070\" = T2.\"XCL_033\" WHERE T1.\"XCL_070\" = 24",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(\"r1\".\"XCL_026\") AS REAL) / COUNT(DISTINCT \"r0\".\"XCL_066\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "votes"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(\"r1\".\"XCL_026\") AS REAL) / COUNT(DISTINCT \"r0\".\"XCL_066\") AS \"value\" FROM votes AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_070\" = \"r1\".\"XCL_033\" WHERE \"r0\".\"XCL_070\" = 24",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:571"
  ]
}
```

### STRFTIME('%Y', "badges"."XCL_004") = '2011' AND "users"."XCL_055" = 'csgillespie'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"badges\".\"XCL_004\") = '2011' AND \"users\".\"XCL_055\" = 'csgillespie'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE STRFTIME('%Y', T1.\"XCL_004\") = '2011' AND T2.\"XCL_055\" = 'csgillespie'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:553"
  ]
}
```

### "users"."XCL_055" = 'Matt Parker'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'Matt Parker'",
  "grain": [
    "\"postHistory\".\"XCL_014\"",
    "\"votes\".\"XCL_066\""
  ],
  "population_scope": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T2.\"XCL_014\" = T3.\"XCL_026\" INNER JOIN votes AS T4 ON T4.\"XCL_067\" = T3.\"XCL_026\" WHERE T1.\"XCL_055\" = 'Matt Parker' GROUP BY T2.\"XCL_014\", T4.\"XCL_066\" HAVING COUNT(T4.\"XCL_066\") > 4",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:635"
  ]
}
```

### Aggregates the total number of rows in the 'comments' table where the column 'XCL_010' equals 13. The metric counts the 'XCL_005' identifier, effectiv

```json
{
  "kind": "metric",
  "formula": "COUNT(\"comments\".\"XCL_005\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_005\") FROM comments WHERE \"XCL_010\" = 13",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_005\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_005\") AS \"value\" FROM comments AS \"r0\" WHERE \"r0\".\"XCL_010\" = 13",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:588"
  ]
}
```

### Aggregated count of rows in the postHistory table where the date portion of XCL_016 matches a specific date. Returns a single scalar value representin

```json
{
  "kind": "metric",
  "formula": "COUNT(\"postHistory\".\"XCL_012\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_012\") FROM postHistory WHERE DATE(\"XCL_016\") = '2010-07-21'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_012\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "postHistory"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_012\") AS \"value\" FROM postHistory AS \"r0\" WHERE DATE(\"r0\".\"XCL_016\") = '2010-07-21'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:642"
  ]
}
```

### Link Metadata

```json
{
  "kind": "binding",
  "formula": "\"postLinks\".\"XCL_025\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_035\", T2.\"XCL_025\" FROM posts AS T1 INNER JOIN postLinks AS T2 ON T1.\"XCL_026\" = T2.\"XCL_023\" INNER JOIN posts AS T3 ON T2.\"XCL_024\" = T3.\"XCL_026\" WHERE T1.\"XCL_035\" = 'What are principal component scores?'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_025\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "postLinks"
      },
      {
        "role": "r2",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_025\" AS \"value\" FROM posts AS \"r0\" INNER JOIN postLinks AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_023\" INNER JOIN posts AS \"r2\" ON \"r1\".\"XCL_024\" = \"r2\".\"XCL_026\" WHERE \"r0\".\"XCL_035\" = 'What are principal component scores?'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:655"
  ]
}
```

### The value of column XCL_055 for the user record(s) where XCL_060 equals the maximum XCL_060 in the table. Represents an attribute of the latest user.

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_052\", \"XCL_055\" FROM users WHERE \"XCL_060\" = (SELECT MAX(\"XCL_060\") FROM users)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:628"
  ]
}
```

### The identifier (XCL_055) of the user from the 'users' table. In this specific computation, it is filtered to 'Harvey Motulsky' or 'Noah Snyder' and re

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [
    "\"users\".\"XCL_055\""
  ],
  "population_scope": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T2.\"XCL_014\" = T3.\"XCL_026\" WHERE T1.\"XCL_055\" = 'Harvey Motulsky' OR T1.\"XCL_055\" = 'Noah Snyder' GROUP BY T1.\"XCL_055\" ORDER BY SUM(T3.\"XCL_031\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:634"
  ]
}
```

### "comments"."XCL_006" = 3720

```json
{
  "kind": "predicate",
  "formula": "\"comments\".\"XCL_006\" = 3720",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT \"XCL_010\") FROM comments WHERE \"XCL_006\" = 3720",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:599"
  ]
}
```

### A scalar metric calculated by dividing the count of rows in the 'votes' table where the year of 'XCL_069' is 2010 by the count of rows where the year 

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(STRFTIME('%Y', \"votes\".\"XCL_069\") = '2010', 1, 0)) AS REAL) / SUM(IIF(STRFTIME('%Y', \"votes\".\"XCL_069\") = '2011', 1, 0))",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(STRFTIME('%Y', \"XCL_069\") = '2010', 1, 0)) AS REAL) / SUM(IIF(STRFTIME('%Y', \"XCL_069\") = '2011', 1, 0)) FROM votes",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(IIF(STRFTIME('%Y', \"r0\".\"XCL_069\") = '2010', 1, 0)) AS REAL) / SUM(IIF(STRFTIME('%Y', \"r0\".\"XCL_069\") = '2011', 1, 0))",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "votes"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(IIF(STRFTIME('%Y', \"r0\".\"XCL_069\") = '2010', 1, 0)) AS REAL) / SUM(IIF(STRFTIME('%Y', \"r0\".\"XCL_069\") = '2011', 1, 0)) AS \"value\" FROM votes AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:629"
  ]
}
```

### "posts"."XCL_035" = 'Group differences on a five point Likert item'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_035\" = 'Group differences on a five point Likert item'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_026\", T1.\"XCL_008\" FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T2.\"XCL_035\" = 'Group differences on a five point Likert item'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:712"
  ]
}
```

### Post Title

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_055\", T1.\"XCL_035\" FROM posts AS T1 INNER JOIN votes AS T2 ON T1.\"XCL_026\" = T2.\"XCL_067\" INNER JOIN users AS T3 ON T3.\"XCL_052\" = T2.\"XCL_070\" WHERE T2.\"XCL_071\" = 50 AND T1.\"XCL_035\" LIKE '%variance%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "votes"
      },
      {
        "role": "r2",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_035\" AS \"value\" FROM posts AS \"r0\" INNER JOIN votes AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_067\" INNER JOIN users AS \"r2\" ON \"r2\".\"XCL_052\" = \"r1\".\"XCL_070\" WHERE \"r1\".\"XCL_071\" = 50 AND \"r0\".\"XCL_035\" LIKE '%variance%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:586"
  ]
}
```

### "badges"."XCL_003" = 'Organizer'

```json
{
  "kind": "predicate",
  "formula": "\"badges\".\"XCL_003\" = 'Organizer'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(T2.\"XCL_064\" BETWEEN 13 AND 18, 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T1.\"XCL_003\" = 'Organizer'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:615"
  ]
}
```

### Identifier from the users table for users who hold the 'outliers' badge. Grain: one row per user-badge match.

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_056\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_056\", T1.\"XCL_058\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'outliers'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_056\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_056\" AS \"value\" FROM users AS \"r0\" INNER JOIN badges AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_002\" WHERE \"r1\".\"XCL_003\" = 'outliers'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:650"
  ]
}
```

### "votes"."XCL_070" = 24

```json
{
  "kind": "predicate",
  "formula": "\"votes\".\"XCL_070\" = 24",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(T2.\"XCL_026\") AS REAL) / COUNT(DISTINCT T1.\"XCL_066\") FROM votes AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_070\" = T2.\"XCL_033\" WHERE T1.\"XCL_070\" = 24",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:571"
  ]
}
```

### "posts"."XCL_036" = '<humor>'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_036\" = '<humor>'",
  "grain": [
    "\"posts\".\"XCL_035\"",
    "\"comments\".\"XCL_008\""
  ],
  "population_scope": "SELECT AVG(T2.\"XCL_031\"), T2.\"XCL_035\", T1.\"XCL_008\" FROM comments AS T1 INNER JOIN posts AS T2 ON T2.\"XCL_026\" = T1.\"XCL_006\" WHERE T2.\"XCL_036\" = '<humor>' GROUP BY T2.\"XCL_035\", T1.\"XCL_008\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:587"
  ]
}
```

### Max User XCL_064

```json
{
  "kind": "metric",
  "formula": "MAX(\"users\".\"XCL_064\")",
  "grain": [],
  "population_scope": "SELECT MAX(\"XCL_064\") FROM users",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MAX(\"r0\".\"XCL_064\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT MAX(\"r0\".\"XCL_064\") AS \"value\" FROM users AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:673"
  ]
}
```

### "posts"."XCL_035" = 'What is the best introductory Bayesian statistics textbook?'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_035\" = 'What is the best introductory Bayesian statistics textbook?'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_012\", T2.\"XCL_041\" FROM postHistory AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_014\" = T2.\"XCL_026\" WHERE T2.\"XCL_035\" = 'What is the best introductory Bayesian statistics textbook?'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:649"
  ]
}
```

### "users"."XCL_057" = 'http://stackoverflow.com'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_057\" = 'http://stackoverflow.com'",
  "grain": [],
  "population_scope": "SELECT \"XCL_055\" FROM users WHERE \"XCL_057\" = 'http://stackoverflow.com'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:574"
  ]
}
```

### "users"."XCL_055" = 'Jarrod Dixon'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'Jarrod Dixon'",
  "grain": [],
  "population_scope": "SELECT \"XCL_053\", \"XCL_060\" FROM users WHERE \"XCL_055\" = 'Jarrod Dixon'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:697"
  ]
}
```

### "tags"."XCL_048" = 'bayesian'

```json
{
  "kind": "predicate",
  "formula": "\"tags\".\"XCL_048\" = 'bayesian'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_032\" FROM tags AS T1 INNER JOIN posts AS T2 ON T2.\"XCL_026\" = T1.\"XCL_050\" WHERE T1.\"XCL_048\" = 'bayesian'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:549"
  ]
}
```

### The display name or username (XCL_058) for users who have authored posts tagged with 'hypothesis-testing'. Returns one row per matching user-post asso

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_058\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_055\", T3.\"XCL_058\" FROM tags AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_050\" = T2.\"XCL_026\" INNER JOIN users AS T3 ON T3.\"XCL_052\" = T2.\"XCL_033\" WHERE T1.\"XCL_048\" = 'hypothesis-testing'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_058\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "tags"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      },
      {
        "role": "r2",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_058\" AS \"value\" FROM tags AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_050\" = \"r1\".\"XCL_026\" INNER JOIN users AS \"r2\" ON \"r2\".\"XCL_052\" = \"r1\".\"XCL_033\" WHERE \"r0\".\"XCL_048\" = 'hypothesis-testing'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:654"
  ]
}
```

### The value of the 'XCL_053' column from the 'users' table. It represents a secondary user attribute, potentially a display name or email, for users who

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_053\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_055\", T1.\"XCL_053\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T2.\"XCL_035\" = 'Understanding what Dassault iSight is doing?'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_053\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_053\" AS \"value\" FROM users AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_033\" WHERE \"r1\".\"XCL_035\" = 'Understanding what Dassault iSight is doing?'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:578"
  ]
}
```

### Aggregated sum of the XCL_030 column from the posts table, filtered to records where XCL_034 starts with '2010-07-19'. Returns a single scalar value r

```json
{
  "kind": "metric",
  "formula": "SUM(\"posts\".\"XCL_030\")",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_030\") FROM posts WHERE \"XCL_034\" LIKE '2010-07-19%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r0\".\"XCL_030\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT SUM(\"r0\".\"XCL_030\") AS \"value\" FROM posts AS \"r0\" WHERE \"r0\".\"XCL_034\" LIKE '2010-07-19%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:664"
  ]
}
```

### "users"."XCL_058" = 'United Kingdom' AND "posts"."XCL_039" >= 4

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_058\" = 'United Kingdom' AND \"posts\".\"XCL_039\" >= 4",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T1.\"XCL_058\" = 'United Kingdom' AND T2.\"XCL_039\" >= 4",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:672"
  ]
}
```

### "badges"."XCL_004" = '2010-07-19 19:39:08.0'

```json
{
  "kind": "predicate",
  "formula": "\"badges\".\"XCL_004\" = '2010-07-19 19:39:08.0'",
  "grain": [],
  "population_scope": "SELECT \"XCL_003\" FROM badges WHERE \"XCL_004\" = '2010-07-19 19:39:08.0'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:606"
  ]
}
```

### The value of the badge identifier column (XCL_003) from the badges table. It represents the single badge associated with the user named 'Emmett' that 

```json
{
  "kind": "binding",
  "formula": "\"badges\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\" FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'Emmett' ORDER BY T1.\"XCL_004\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:690"
  ]
}
```

### The value of the 'XCL_060' column from the 'users' table. This represents a specific user attribute (likely a user ID or name) for users who have earn

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_060\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_060\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_004\" = '2010-07-19 19:39:08.0'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_060\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_060\" AS \"value\" FROM users AS \"r0\" INNER JOIN badges AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_002\" WHERE \"r1\".\"XCL_004\" = '2010-07-19 19:39:08.0'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:620"
  ]
}
```

### "comments"."XCL_009" = '2014-04-23 20:29:39.0' AND "comments"."XCL_010" = 3025

```json
{
  "kind": "predicate",
  "formula": "\"comments\".\"XCL_009\" = '2014-04-23 20:29:39.0' AND \"comments\".\"XCL_010\" = 3025",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_039\" FROM posts AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_026\" = T2.\"XCL_006\" WHERE T2.\"XCL_009\" = '2014-04-23 20:29:39.0' AND T2.\"XCL_010\" = 3025",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:563"
  ]
}
```

### Calculates the percentage of rows in the joined population where users.XCL_061 is 0. The numerator counts occurrences of XCL_061 = 0, and the denomina

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(\"users\".\"XCL_061\" = 0, 1, 0)) AS REAL) * 100 / COUNT(\"users\".\"XCL_052\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(T1.\"XCL_061\" = 0, 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_052\") AS per FROM users AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_052\" = T2.\"XCL_010\" WHERE T2.\"XCL_007\" BETWEEN 5 AND 10",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(IIF(\"r0\".\"XCL_061\" = 0, 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_052\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "comments"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(IIF(\"r0\".\"XCL_061\" = 0, 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_052\") AS \"value\" FROM users AS \"r0\" INNER JOIN comments AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_010\" WHERE \"r1\".\"XCL_007\" BETWEEN 5 AND 10",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:716"
  ]
}
```

### "users"."XCL_055" = 'Yevgeny'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'Yevgeny'",
  "grain": [
    "\"users\".\"XCL_057\""
  ],
  "population_scope": "SELECT SUM(T1.\"XCL_030\"), T2.\"XCL_057\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_040\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'Yevgeny' GROUP BY T2.\"XCL_057\"",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:583"
  ]
}
```

### "badges"."XCL_003" = 'Revival'

```json
{
  "kind": "predicate",
  "formula": "\"badges\".\"XCL_003\" = 'Revival'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM badges WHERE \"XCL_003\" = 'Revival'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:560"
  ]
}
```

### Aggregates the count of post identifiers (XCL_026) from the posts table where the post is joined to at least one vote record and the post's XCL_035 fi

```json
{
  "kind": "metric",
  "formula": "COUNT(\"posts\".\"XCL_026\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN votes AS T2 ON T1.\"XCL_026\" = T2.\"XCL_067\" WHERE T1.\"XCL_035\" LIKE '%data visualization%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_026\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "votes"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_026\") AS \"value\" FROM posts AS \"r0\" INNER JOIN votes AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_067\" WHERE \"r0\".\"XCL_035\" LIKE '%data visualization%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:569"
  ]
}
```

### The percentage of posts associated with users who have the maximum reputation ('XCL_053') that have a score ('XCL_030') greater than 50. Calculated as

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(CASE WHEN T2.\"XCL_030\" > 50 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_052\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(CASE WHEN T2.\"XCL_030\" > 50 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" INNER JOIN (SELECT MAX(\"XCL_053\") AS max_reputation FROM users) AS T3 ON T1.\"XCL_053\" = T3.\"max_reputation\"",
  "upstream_scopes": [
    "SELECT MAX(\"XCL_053\") AS max_reputation FROM users"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:701"
  ]
}
```

### Comment Identifier

```json
{
  "kind": "binding",
  "formula": "\"comments\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_008\" FROM users AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_052\" = T2.\"XCL_010\" WHERE T1.\"XCL_055\" = 'A Lion'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "comments"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_008\" AS \"value\" FROM users AS \"r0\" INNER JOIN comments AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_010\" WHERE \"r0\".\"XCL_055\" = 'A Lion'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:577"
  ]
}
```

### The value of the 'XCL_053' column from the 'users' table. This represents a specific user attribute, likely a unique identifier or key, for users who 

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_053\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_053\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T2.\"XCL_026\" = 65041",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_053\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_053\" AS \"value\" FROM users AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_033\" WHERE \"r1\".\"XCL_026\" = 65041",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:566"
  ]
}
```

### "badges"."XCL_003" = 'Supporter' AND "users"."XCL_064" BETWEEN 19 AND 65

```json
{
  "kind": "predicate",
  "formula": "\"badges\".\"XCL_003\" = 'Supporter' AND \"users\".\"XCL_064\" BETWEEN 19 AND 65",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'Supporter' AND T1.\"XCL_064\" BETWEEN 19 AND 65",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:619"
  ]
}
```

### The value of the column "XCL_055" from the "users" table, filtered to records where "XCL_064" is between 19 and 65. Grain: one row per matching user r

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_055\" FROM users WHERE \"XCL_064\" BETWEEN 19 AND 65",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_055\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_055\" AS \"value\" FROM users AS \"r0\" WHERE \"r0\".\"XCL_064\" BETWEEN 19 AND 65",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:676"
  ]
}
```

### "postHistory"."XCL_018" = 'Computer Game Datasets'

```json
{
  "kind": "predicate",
  "formula": "\"postHistory\".\"XCL_018\" = 'Computer Game Datasets'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_031\", T3.\"XCL_055\" FROM postHistory AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_014\" = T2.\"XCL_026\" INNER JOIN users AS T3 ON T2.\"XCL_040\" = T3.\"XCL_052\" WHERE T1.\"XCL_018\" = 'Computer Game Datasets'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:685"
  ]
}
```

### Post Identifier (XCL_030)

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_030\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_030\", T2.\"XCL_025\" FROM posts AS T1 INNER JOIN postLinks AS T2 ON T1.\"XCL_026\" = T2.\"XCL_023\" WHERE T2.\"XCL_023\" = 395",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_030\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "postLinks"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_030\" AS \"value\" FROM posts AS \"r0\" INNER JOIN postLinks AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_023\" WHERE \"r1\".\"XCL_023\" = 395",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:601"
  ]
}
```

### "users"."XCL_055" = 'Pierre'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'Pierre'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_055\" = 'Pierre'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:612"
  ]
}
```

### Post Identifier

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_032\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_032\" FROM posts WHERE \"XCL_026\" = (SELECT \"XCL_050\" FROM tags ORDER BY \"XCL_049\" DESC LIMIT 1)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:550"
  ]
}
```

### Comment Identifier

```json
{
  "kind": "binding",
  "formula": "\"comments\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_008\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'Harvey Motulsky'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_008\" AS \"value\" FROM comments AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_052\" WHERE \"r1\".\"XCL_055\" = 'Harvey Motulsky'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:714"
  ]
}
```

### "comments"."XCL_007" > 60

```json
{
  "kind": "predicate",
  "formula": "\"comments\".\"XCL_007\" > 60",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_005\") FROM comments WHERE \"XCL_007\" > 60",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:607"
  ]
}
```

### "users"."XCL_055" = 'A Lion'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'A Lion'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_008\" FROM users AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_052\" = T2.\"XCL_010\" WHERE T1.\"XCL_055\" = 'A Lion'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:577"
  ]
}
```

### A derived categorical metric indicating whether a post is 'well-finished' or 'NOT well-finished'. It is computed by checking if the 'XCL_044' column i

```json
{
  "kind": "binding",
  "formula": "IIF(\"posts\".\"XCL_044\" IS NULL, 'NOT well-finished', 'well-finished')",
  "grain": [],
  "population_scope": "SELECT IIF(T2.\"XCL_044\" IS NULL, 'NOT well-finished', 'well-finished') AS resylt FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T1.\"XCL_010\" = 23853 AND T1.\"XCL_009\" = '2013-07-12 09:08:18.0'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "IIF(\"r1\".\"XCL_044\" IS NULL, 'NOT well-finished', 'well-finished')",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT IIF(\"r1\".\"XCL_044\" IS NULL, 'NOT well-finished', 'well-finished') AS \"value\" FROM comments AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_006\" = \"r1\".\"XCL_026\" WHERE \"r0\".\"XCL_010\" = 23853 AND \"r0\".\"XCL_009\" = '2013-07-12 09:08:18.0'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:565"
  ]
}
```

### NOT "posts"."XCL_044" IS NULL

```json
{
  "kind": "predicate",
  "formula": "NOT \"posts\".\"XCL_044\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_055\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE NOT T1.\"XCL_044\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:546"
  ]
}
```

### "votes"."XCL_071" = 50 AND "posts"."XCL_035" LIKE '%variance%'

```json
{
  "kind": "predicate",
  "formula": "\"votes\".\"XCL_071\" = 50 AND \"posts\".\"XCL_035\" LIKE '%variance%'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_055\", T1.\"XCL_035\" FROM posts AS T1 INNER JOIN votes AS T2 ON T1.\"XCL_026\" = T2.\"XCL_067\" INNER JOIN users AS T3 ON T3.\"XCL_052\" = T2.\"XCL_070\" WHERE T2.\"XCL_071\" = 50 AND T1.\"XCL_035\" LIKE '%variance%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:586"
  ]
}
```

### Comment Identifier

```json
{
  "kind": "binding",
  "formula": "\"comments\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_008\", T1.\"XCL_055\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" INNER JOIN comments AS T3 ON T2.\"XCL_026\" = T3.\"XCL_006\" WHERE T2.\"XCL_035\" = 'Analysing wind data with R' ORDER BY T1.\"XCL_054\" DESC LIMIT 10",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:694"
  ]
}
```

### "posts"."XCL_035" LIKE '%linear regression%'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_035\" LIKE '%linear regression%'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_008\" FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T2.\"XCL_035\" LIKE '%linear regression%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:706"
  ]
}
```

### Comment Identifier

```json
{
  "kind": "binding",
  "formula": "\"comments\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_008\" FROM posts AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_026\" = T2.\"XCL_006\" WHERE T1.\"XCL_043\" = 107829 AND T1.\"XCL_038\" = 1",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "comments"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_008\" AS \"value\" FROM posts AS \"r0\" INNER JOIN comments AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_006\" WHERE \"r0\".\"XCL_043\" = 107829 AND \"r0\".\"XCL_038\" = 1",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:564"
  ]
}
```

### Count of non-null values in column XCL_052 from the users table, restricted to rows where XCL_061 is greater than 100 and XCL_062 is greater than 1.

```json
{
  "kind": "metric",
  "formula": "COUNT(\"users\".\"XCL_052\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_052\") FROM users WHERE \"XCL_061\" > 100 AND \"XCL_062\" > 1",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_052\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_052\") AS \"value\" FROM users AS \"r0\" WHERE \"r0\".\"XCL_061\" > 100 AND \"r0\".\"XCL_062\" > 1",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:535"
  ]
}
```

### Aggregates the total number of rows in the 'users' table where the column 'XCL_058' equals 'New York'. The metric counts the 'XCL_052' column, which s

```json
{
  "kind": "metric",
  "formula": "COUNT(\"users\".\"XCL_052\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_052\") FROM users WHERE \"XCL_058\" = 'New York'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_052\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_052\") AS \"value\" FROM users AS \"r0\" WHERE \"r0\".\"XCL_058\" = 'New York'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:625"
  ]
}
```

### NOT "users"."XCL_064" IS NULL

```json
{
  "kind": "predicate",
  "formula": "NOT \"users\".\"XCL_064\" IS NULL",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_029\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE NOT T1.\"XCL_064\" IS NULL ORDER BY T1.\"XCL_064\", T2.\"XCL_029\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:670"
  ]
}
```

### The value of the XCL_055 column for the user record where XCL_060 equals the maximum XCL_060 in the table. Represents an attribute of the top-ranked u

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_055\", \"XCL_064\" FROM users WHERE \"XCL_060\" = (SELECT MAX(\"XCL_060\") FROM users)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:643"
  ]
}
```

### User Attribute XCL_057

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_057\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_055\", T1.\"XCL_057\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T2.\"XCL_039\" > 150",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_057\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_057\" AS \"value\" FROM users AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_033\" WHERE \"r1\".\"XCL_039\" > 150",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:648"
  ]
}
```

### The value of column XCL_052 for the user record(s) where XCL_060 equals the maximum XCL_060 in the table. Represents an attribute of the latest user.

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_052\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_052\", \"XCL_055\" FROM users WHERE \"XCL_060\" = (SELECT MAX(\"XCL_060\") FROM users)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:628"
  ]
}
```

### "posts"."XCL_037" <= 2 AND STRFTIME('%Y', "postLinks"."XCL_022") = '2010'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_037\" <= 2 AND STRFTIME('%Y', \"postLinks\".\"XCL_022\") = '2010'",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(T1.\"XCL_021\") AS REAL) / 12 FROM postLinks AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_023\" = T2.\"XCL_026\" WHERE T2.\"XCL_037\" <= 2 AND STRFTIME('%Y', T1.\"XCL_022\") = '2010'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:665"
  ]
}
```

### "badges"."XCL_003" = 'outliers'

```json
{
  "kind": "predicate",
  "formula": "\"badges\".\"XCL_003\" = 'outliers'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_056\", T1.\"XCL_058\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'outliers'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:650"
  ]
}
```

### Returns the value of "XCL_055" from the "users" table for the user whose "XCL_052" matches the top vote identifier derived from the "votes" table. Thi

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_055\", \"XCL_057\" FROM users WHERE \"XCL_052\" = (SELECT \"XCL_070\" FROM votes WHERE \"XCL_068\" = 8 ORDER BY \"XCL_071\" DESC LIMIT 1)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:657"
  ]
}
```

### "comments"."XCL_008" = 'R is also lazy evaluated.'

```json
{
  "kind": "predicate",
  "formula": "\"comments\".\"XCL_008\" = 'R is also lazy evaluated.'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_061\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_008\" = 'R is also lazy evaluated.'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:713"
  ]
}
```

### "users"."XCL_055" = 'John Salvatier'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'John Salvatier'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_036\" FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T2.\"XCL_014\" = T3.\"XCL_026\" WHERE T1.\"XCL_055\" = 'John Salvatier'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:630"
  ]
}
```

### COUNT("badges"."XCL_003") > 5

```json
{
  "kind": "predicate",
  "formula": "COUNT(\"badges\".\"XCL_003\") > 5",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_002\") FROM (SELECT \"XCL_002\", COUNT(\"XCL_003\") AS num FROM badges GROUP BY \"XCL_002\") AS T WHERE T.\"num\" > 5",
  "upstream_scopes": [
    "SELECT \"XCL_002\", COUNT(\"XCL_003\") AS num FROM badges GROUP BY \"XCL_002\""
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:592"
  ]
}
```

### A scalar metric representing the percentage of joined user-post records where the post date (XCL_029) is in the year 2011 and the user attribute XCL_0

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(STRFTIME('%Y', \"posts\".\"XCL_029\") = '2011' AND \"users\".\"XCL_053\" > 1000, 1, 0)) AS REAL) * 100 / COUNT(\"users\".\"XCL_052\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(STRFTIME('%Y', T2.\"XCL_029\") = '2011' AND T1.\"XCL_053\" > 1000, 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(IIF(STRFTIME('%Y', \"r1\".\"XCL_029\") = '2011' AND \"r0\".\"XCL_053\" > 1000, 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_052\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(IIF(STRFTIME('%Y', \"r1\".\"XCL_029\") = '2011' AND \"r0\".\"XCL_053\" > 1000, 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_052\") AS \"value\" FROM users AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_033\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:683"
  ]
}
```

### "users"."XCL_055" = 'csgillespie'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'csgillespie'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:537"
  ]
}
```

### Value of column XCL_050 from the tags table, restricted to rows where XCL_048 equals 'sample'.

```json
{
  "kind": "binding",
  "formula": "\"tags\".\"XCL_050\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_050\", \"XCL_051\" FROM tags WHERE \"XCL_048\" = 'sample'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_050\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "tags"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_050\" AS \"value\" FROM tags AS \"r0\" WHERE \"r0\".\"XCL_048\" = 'sample'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:704"
  ]
}
```

### Post Identifier

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_035\" AS \"value\" FROM posts AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_033\" = \"r1\".\"XCL_052\" WHERE \"r1\".\"XCL_055\" = 'csgillespie'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:538"
  ]
}
```

### "badges"."XCL_003" = 'Necromancer'

```json
{
  "kind": "predicate",
  "formula": "\"badges\".\"XCL_003\" = 'Necromancer'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'Necromancer' LIMIT 10",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:580"
  ]
}
```

### Difference in XCL_031 between Mornington and Amos users

```json
{
  "kind": "metric",
  "formula": "SUM(IIF(\"users\".\"XCL_055\" = 'Mornington', \"posts\".\"XCL_031\", 0)) - SUM(IIF(\"users\".\"XCL_055\" = 'Amos', \"posts\".\"XCL_031\", 0))",
  "grain": [],
  "population_scope": "SELECT SUM(IIF(T1.\"XCL_055\" = 'Mornington', T3.\"XCL_031\", 0)) - SUM(IIF(T1.\"XCL_055\" = 'Amos', T3.\"XCL_031\", 0)) AS diff FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T3.\"XCL_026\" = T2.\"XCL_014\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(IIF(\"r0\".\"XCL_055\" = 'Mornington', \"r2\".\"XCL_031\", 0)) - SUM(IIF(\"r0\".\"XCL_055\" = 'Amos', \"r2\".\"XCL_031\", 0))",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "postHistory"
      },
      {
        "role": "r2",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT SUM(IIF(\"r0\".\"XCL_055\" = 'Mornington', \"r2\".\"XCL_031\", 0)) - SUM(IIF(\"r0\".\"XCL_055\" = 'Amos', \"r2\".\"XCL_031\", 0)) AS \"value\" FROM users AS \"r0\" INNER JOIN postHistory AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_017\" INNER JOIN posts AS \"r2\" ON \"r2\".\"XCL_026\" = \"r1\".\"XCL_014\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:640"
  ]
}
```

### "users"."XCL_055" = 'Vebjorn Ljosa'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'Vebjorn Ljosa'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'Vebjorn Ljosa'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:582"
  ]
}
```

### Identifier from the 'posts' table (column XCL_026) for records where the score (XCL_030) exceeds 60. Used as the filter set for the main query.

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_026\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_026\" FROM posts WHERE \"XCL_030\" > 60",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_026\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_026\" AS \"value\" FROM posts AS \"r0\" WHERE \"r0\".\"XCL_030\" > 60",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:602"
  ]
}
```

### "posts"."XCL_030" = 10

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_030\" = 10",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_026\") FROM posts WHERE \"XCL_030\" = 10",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:609"
  ]
}
```

### "badges"."XCL_003" = 'Organizer'

```json
{
  "kind": "predicate",
  "formula": "\"badges\".\"XCL_003\" = 'Organizer'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'Organizer'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:638"
  ]
}
```

### Value of column XCL_041 from the posts table, representing a specific attribute of the post identified by the title filter.

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_041\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_012\", T2.\"XCL_041\" FROM postHistory AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_014\" = T2.\"XCL_026\" WHERE T2.\"XCL_035\" = 'What is the best introductory Bayesian statistics textbook?'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_041\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "postHistory"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_041\" AS \"value\" FROM postHistory AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_014\" = \"r1\".\"XCL_026\" WHERE \"r1\".\"XCL_035\" = 'What is the best introductory Bayesian statistics textbook?'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:649"
  ]
}
```

### "comments"."XCL_009" = '2010-07-19 19:16:14.0'

```json
{
  "kind": "predicate",
  "formula": "\"comments\".\"XCL_009\" = '2010-07-19 19:16:14.0'",
  "grain": [],
  "population_scope": "SELECT \"XCL_008\" FROM comments WHERE \"XCL_009\" = '2010-07-19 19:16:14.0'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:608"
  ]
}
```

### User Attribute XCL_060

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_060\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_053\", \"XCL_060\" FROM users WHERE \"XCL_055\" = 'Jarrod Dixon'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_060\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_060\" AS \"value\" FROM users AS \"r0\" WHERE \"r0\".\"XCL_055\" = 'Jarrod Dixon'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:697"
  ]
}
```

### "posts"."XCL_030" < 20

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_030\" < 20",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_026\") FROM posts WHERE \"XCL_030\" < 20",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:702"
  ]
}
```

### The identifier (XCL_052) of users who have authored at least one comment where the comment attribute XCL_006 equals 1. Returned at the grain of the jo

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_052\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_052\", T2.\"XCL_053\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_006\" = 1",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_052\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_052\" AS \"value\" FROM comments AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_052\" WHERE \"r0\".\"XCL_006\" = 1",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:594"
  ]
}
```

### Average XCL_030 for user csgillespie

```json
{
  "kind": "metric",
  "formula": "AVG(\"posts\".\"XCL_030\")",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_030\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_030\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_030\") AS \"value\" FROM posts AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_033\" = \"r1\".\"XCL_052\" WHERE \"r1\".\"XCL_055\" = 'csgillespie'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:555"
  ]
}
```

### "posts"."XCL_035" = 'How to tell if something happened in a data set which monitors a value over time'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_035\" = 'How to tell if something happened in a data set which monitors a value over time'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_035\" FROM postLinks AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_023\" = T2.\"XCL_026\" INNER JOIN posts AS T3 ON T1.\"XCL_024\" = T3.\"XCL_026\" WHERE T2.\"XCL_035\" = 'How to tell if something happened in a data set which monitors a value over time'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:651"
  ]
}
```

### "users"."XCL_055" = 'IrishStat'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'IrishStat'",
  "grain": [],
  "population_scope": "SELECT \"XCL_054\" FROM users WHERE \"XCL_055\" = 'IrishStat'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:699"
  ]
}
```

### "users"."XCL_055" = 'csgillespie' AND "posts"."XCL_043" IS NULL

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'csgillespie' AND \"posts\".\"XCL_043\" IS NULL",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie' AND T1.\"XCL_043\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:545"
  ]
}
```

### Post Identifier XCL_035

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_035\" FROM posts ORDER BY \"XCL_031\" DESC LIMIT 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:658"
  ]
}
```

### "badges"."XCL_003" = 'Student'

```json
{
  "kind": "predicate",
  "formula": "\"badges\".\"XCL_003\" = 'Student'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(STRFTIME('%Y', \"XCL_004\") = '2010', 1, 0)) AS REAL) * 100 / COUNT(\"XCL_001\") - CAST(SUM(IIF(STRFTIME('%Y', \"XCL_004\") = '2011', 1, 0)) AS REAL) * 100 / COUNT(\"XCL_001\") FROM badges WHERE \"XCL_003\" = 'Student'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:598"
  ]
}
```

### Comment Identifier

```json
{
  "kind": "binding",
  "formula": "\"comments\".\"XCL_011\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T2.\"XCL_011\" FROM posts AS T1 INNER JOIN comments AS T2 ON T2.\"XCL_006\" = T2.\"XCL_005\" WHERE T1.\"XCL_030\" > 60",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_011\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "comments"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_011\" AS \"value\" FROM posts AS \"r0\" INNER JOIN comments AS \"r1\" ON \"r1\".\"XCL_006\" = \"r1\".\"XCL_005\" WHERE \"r0\".\"XCL_030\" > 60",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:646"
  ]
}
```

### Minimum vote value for 'chl' users

```json
{
  "kind": "binding",
  "formula": "\"votes\".\"XCL_069\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_069\" FROM users AS T1 INNER JOIN votes AS T2 ON T1.\"XCL_052\" = T2.\"XCL_070\" WHERE T1.\"XCL_055\" = 'chl' ORDER BY T2.\"XCL_069\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:669"
  ]
}
```

### Latest Post Identifier

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_033\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_033\" FROM posts ORDER BY \"XCL_031\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:653"
  ]
}
```

### STRFTIME('%Y', "users"."XCL_054") = '2011'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"users\".\"XCL_054\") = '2011'",
  "grain": [],
  "population_scope": "SELECT \"XCL_055\" FROM users WHERE STRFTIME('%Y', \"XCL_054\") = '2011'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:532"
  ]
}
```

### Attribute from the users table (T2) for users who have authored at least one comment containing an HTTP URL. Grain: one row per matching user-comment 

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_064\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_054\", T2.\"XCL_064\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_008\" LIKE '%http://%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_064\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_064\" AS \"value\" FROM comments AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_052\" WHERE \"r0\".\"XCL_008\" LIKE '%http://%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:708"
  ]
}
```

### "postLinks"."XCL_023" = 61217

```json
{
  "kind": "predicate",
  "formula": "\"postLinks\".\"XCL_023\" = 61217",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_031\" FROM posts AS T1 INNER JOIN postLinks AS T2 ON T1.\"XCL_026\" = T2.\"XCL_023\" WHERE T2.\"XCL_023\" = 61217",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:600"
  ]
}
```

### The value of the 'XCL_053' column from the 'users' table. This represents a specific user attribute (likely a user ID or name) for users who have earn

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_053\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_053\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_004\" = '2010-07-19 19:39:08.0'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_053\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_053\" AS \"value\" FROM users AS \"r0\" INNER JOIN badges AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_002\" WHERE \"r1\".\"XCL_004\" = '2010-07-19 19:39:08.0'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:611"
  ]
}
```

### "users"."XCL_055" = 'SilentGhost'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'SilentGhost'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_055\" = 'SilentGhost'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:575"
  ]
}
```

### "users"."XCL_055" = 'csgillespie'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'csgillespie'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie' ORDER BY T1.\"XCL_031\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:540"
  ]
}
```

### Counts the number of posts (identified by column XCL_026) associated with a specific user, filtered by the user identifier 'csgillespie' in column XCL

```json
{
  "kind": "metric",
  "formula": "COUNT(\"posts\".\"XCL_026\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_026\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_026\") AS \"value\" FROM posts AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_033\" = \"r1\".\"XCL_052\" WHERE \"r1\".\"XCL_055\" = 'csgillespie'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:537"
  ]
}
```

### Post Identifier

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_026\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_026\", T2.\"XCL_035\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T1.\"XCL_055\" = 'Harvey Motulsky' ORDER BY T2.\"XCL_031\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:678"
  ]
}
```

### Aggregates the total number of non-null values in column XCL_066 from the votes table, restricted to rows where XCL_071 is greater than or equal to 30

```json
{
  "kind": "metric",
  "formula": "COUNT(\"votes\".\"XCL_066\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_066\") FROM votes WHERE \"XCL_071\" >= 30",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_066\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "votes"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_066\") AS \"value\" FROM votes AS \"r0\" WHERE \"r0\".\"XCL_071\" >= 30",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:700"
  ]
}
```

### "posts"."XCL_030" >= 20 AND "users"."XCL_064" > 65

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_030\" >= 20 AND \"users\".\"XCL_064\" > 65",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T1.\"XCL_030\" >= 20 AND T2.\"XCL_064\" > 65",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:547"
  ]
}
```

### Avg Vote XCL_067 for Max User

```json
{
  "kind": "metric",
  "formula": "AVG(\"votes\".\"XCL_067\")",
  "grain": [],
  "population_scope": "SELECT AVG(\"XCL_067\") FROM votes WHERE \"XCL_070\" IN (SELECT \"XCL_052\" FROM users WHERE \"XCL_064\" = (SELECT MAX(\"XCL_064\") FROM users))",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:673"
  ]
}
```

### "badges"."XCL_003" = 'Announcer'

```json
{
  "kind": "predicate",
  "formula": "\"badges\".\"XCL_003\" = 'Announcer'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM badges WHERE \"XCL_003\" = 'Announcer'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:605"
  ]
}
```

### "posts"."XCL_035" LIKE '%data%'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_035\" LIKE '%data%'",
  "grain": [],
  "population_scope": "SELECT SUM(T2.\"XCL_071\") FROM posts AS T1 INNER JOIN votes AS T2 ON T1.\"XCL_026\" = T2.\"XCL_067\" WHERE T1.\"XCL_035\" LIKE '%data%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:585"
  ]
}
```

### "posts"."XCL_035" = 'Integration of Weka and/or RapidMiner into Informatica PowerCenter/Developer'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_035\" = 'Integration of Weka and/or RapidMiner into Informatica PowerCenter/Developer'",
  "grain": [],
  "population_scope": "SELECT \"XCL_031\" FROM posts WHERE \"XCL_035\" = 'Integration of Weka and/or RapidMiner into Informatica PowerCenter/Developer'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:572"
  ]
}
```

### "posts"."XCL_031" < 5 AND "posts"."XCL_030" = 0

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_031\" < 5 AND \"posts\".\"XCL_030\" = 0",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_005\") FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T2.\"XCL_031\" < 5 AND T2.\"XCL_030\" = 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:709"
  ]
}
```

### The value of column XCL_055 from the users table, representing the specific user associated with posts created in 2011 that have a value in XCL_031 gr

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE STRFTIME('%Y', T2.\"XCL_029\") = '2011' AND T2.\"XCL_031\" > 20000",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_055\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_055\" AS \"value\" FROM users AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_033\" WHERE STRFTIME('%Y', \"r1\".\"XCL_029\") = '2011' AND \"r1\".\"XCL_031\" > 20000",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:681"
  ]
}
```

### Counts the number of posts (via join key XCL_033) associated with a specific user (XCL_052) for a given year. The grain is a single scalar value repre

```json
{
  "kind": "metric",
  "formula": "COUNT(\"users\".\"XCL_052\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE STRFTIME('%Y', T2.\"XCL_029\") = '2010' AND T1.\"XCL_055\" = 'Jay Stevens'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_052\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_052\") AS \"value\" FROM users AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_033\" WHERE STRFTIME('%Y', \"r1\".\"XCL_029\") = '2010' AND \"r0\".\"XCL_055\" = 'Jay Stevens'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:677"
  ]
}
```

### Average User Attribute XCL_064

```json
{
  "kind": "metric",
  "formula": "AVG(T1.\"XCL_064\")",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_061\"), AVG(T1.\"XCL_064\") FROM users AS T1 INNER JOIN (SELECT \"XCL_033\", COUNT(*) AS post_count FROM posts GROUP BY \"XCL_033\" HAVING post_count > 10) AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\"",
  "upstream_scopes": [
    "SELECT \"XCL_033\", COUNT(*) AS post_count FROM posts GROUP BY \"XCL_033\" HAVING post_count > 10"
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:604"
  ]
}
```

### Aggregates the total number of rows in the 'users' table where the date portion of column 'XCL_056' is strictly greater than '2014-09-01'. The metric 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"users\".\"XCL_052\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_052\") FROM users WHERE DATE(\"XCL_056\") > '2014-09-01'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_052\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_052\") AS \"value\" FROM users AS \"r0\" WHERE DATE(\"r0\".\"XCL_056\") > '2014-09-01'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:533"
  ]
}
```

### "posts"."XCL_030" > 60

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_030\" > 60",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\", T2.\"XCL_011\" FROM posts AS T1 INNER JOIN comments AS T2 ON T2.\"XCL_006\" = T2.\"XCL_005\" WHERE T1.\"XCL_030\" > 60",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:646"
  ]
}
```

### "votes"."XCL_068" = 8

```json
{
  "kind": "predicate",
  "formula": "\"votes\".\"XCL_068\" = 8",
  "grain": [],
  "population_scope": "SELECT \"XCL_070\" FROM votes WHERE \"XCL_068\" = 8 ORDER BY \"XCL_071\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:657"
  ]
}
```

### "users"."XCL_064" BETWEEN 19 AND 65

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_064\" BETWEEN 19 AND 65",
  "grain": [],
  "population_scope": "SELECT \"XCL_055\" FROM users WHERE \"XCL_064\" BETWEEN 19 AND 65",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:676"
  ]
}
```

### The value of the 'XCL_055' column from the 'users' table for the single user with the highest count of associated 'badges' records. The grain is one r

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [
    "\"users\".\"XCL_055\""
  ],
  "population_scope": "SELECT T2.\"XCL_055\" FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" GROUP BY T2.\"XCL_055\" ORDER BY COUNT(T1.\"XCL_001\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:554"
  ]
}
```

### Count of High-Frequency Groups

```json
{
  "kind": "metric",
  "formula": "COUNT(\"XCL_002\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_002\") FROM (SELECT \"XCL_002\", COUNT(\"XCL_003\") AS num FROM badges GROUP BY \"XCL_002\") AS T WHERE T.\"num\" > 5",
  "upstream_scopes": [
    "SELECT \"XCL_002\", COUNT(\"XCL_003\") AS num FROM badges GROUP BY \"XCL_002\""
  ],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:592"
  ]
}
```

### History Post Reference

```json
{
  "kind": "binding",
  "formula": "\"postHistory\".\"XCL_014\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_014\", \"XCL_017\" FROM postHistory WHERE \"XCL_014\" IN (SELECT \"XCL_026\" FROM posts WHERE \"XCL_030\" > 60)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:602"
  ]
}
```

### The value of the 'XCL_058' column from the 'users' table. This represents a specific attribute of the user associated with the post titled 'Eliciting 

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_058\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_058\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T1.\"XCL_035\" = 'Eliciting priors from experts'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_058\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_058\" AS \"value\" FROM posts AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_033\" = \"r1\".\"XCL_052\" WHERE \"r0\".\"XCL_035\" = 'Eliciting priors from experts'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:548"
  ]
}
```

### Aggregates the count of post identifiers (XCL_026) from the posts table, restricted to rows joined with votes where the vote value (XCL_071) is 50 and

```json
{
  "kind": "metric",
  "formula": "COUNT(\"posts\".\"XCL_026\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN votes AS T2 ON T1.\"XCL_026\" = T2.\"XCL_067\" WHERE T2.\"XCL_071\" = 50 AND STRFTIME('%Y', T2.\"XCL_069\") = '2011'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_026\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "votes"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_026\") AS \"value\" FROM posts AS \"r0\" INNER JOIN votes AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_067\" WHERE \"r1\".\"XCL_071\" = 50 AND STRFTIME('%Y', \"r1\".\"XCL_069\") = '2011'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:662"
  ]
}
```

### Aggregated sum of the 'XCL_030' column from the 'posts' table. The population is restricted to posts associated with users where 'XCL_055' equals 'Yev

```json
{
  "kind": "metric",
  "formula": "SUM(\"posts\".\"XCL_030\")",
  "grain": [
    "\"users\".\"XCL_057\""
  ],
  "population_scope": "SELECT SUM(T1.\"XCL_030\"), T2.\"XCL_057\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_040\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'Yevgeny' GROUP BY T2.\"XCL_057\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r0\".\"XCL_030\")",
    "grain": [
      "\"r1\".\"XCL_057\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_057\" AS \"grain_0\", SUM(\"r0\".\"XCL_030\") AS \"value\" FROM posts AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_040\" = \"r1\".\"XCL_052\" WHERE \"r1\".\"XCL_055\" = 'Yevgeny' GROUP BY \"r1\".\"XCL_057\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:583"
  ]
}
```

### "users"."XCL_055" = 'csgillespie'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'csgillespie'",
  "grain": [],
  "population_scope": "SELECT AVG(T1.\"XCL_030\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:555"
  ]
}
```

### Value of column XCL_051 from the tags table, restricted to rows where XCL_048 equals 'sample'.

```json
{
  "kind": "binding",
  "formula": "\"tags\".\"XCL_051\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_050\", \"XCL_051\" FROM tags WHERE \"XCL_048\" = 'sample'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_051\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "tags"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_051\" AS \"value\" FROM tags AS \"r0\" WHERE \"r0\".\"XCL_048\" = 'sample'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:704"
  ]
}
```

### "badges"."XCL_004" = '2010-07-19 19:39:08.0'

```json
{
  "kind": "predicate",
  "formula": "\"badges\".\"XCL_004\" = '2010-07-19 19:39:08.0'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_053\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_004\" = '2010-07-19 19:39:08.0'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:611"
  ]
}
```

### The value of the 'XCL_052' column from the 'users' table. In this context, it serves as the foreign key linking to the 'posts' table and is returned a

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_052\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_052\", T2.\"XCL_035\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" ORDER BY T2.\"XCL_030\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:679"
  ]
}
```

### Post History Field XCL_013

```json
{
  "kind": "binding",
  "formula": "\"postHistory\".\"XCL_013\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_013\", (SELECT COUNT(DISTINCT \"XCL_010\") FROM comments WHERE \"XCL_006\" = 3720) AS NumberOfUsers FROM postHistory AS T1 WHERE T1.\"XCL_014\" = 3720",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:599"
  ]
}
```

### The value of the XCL_064 column for the user record where XCL_060 equals the maximum XCL_060 in the table. Represents an attribute of the top-ranked u

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_064\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_055\", \"XCL_064\" FROM users WHERE \"XCL_060\" = (SELECT MAX(\"XCL_060\") FROM users)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:643"
  ]
}
```

### "users"."XCL_055" = 'csgillespie'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'csgillespie'",
  "grain": [],
  "population_scope": "SELECT MAX(T1.\"XCL_037\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:543"
  ]
}
```

### The value of column XCL_052 for the user(s) in the users table where XCL_053 equals the maximum XCL_053. Represents the identifier or attribute of the

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_052\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_052\" FROM users WHERE \"XCL_053\" = (SELECT MAX(\"XCL_053\") FROM users)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:589"
  ]
}
```

### Badge Identifier

```json
{
  "kind": "binding",
  "formula": "\"badges\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE STRFTIME('%Y', T2.\"XCL_004\") = '2011' AND T1.\"XCL_058\" = 'North Pole'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_003\" AS \"value\" FROM users AS \"r0\" INNER JOIN badges AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_002\" WHERE STRFTIME('%Y', \"r1\".\"XCL_004\") = '2011' AND \"r0\".\"XCL_058\" = 'North Pole'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:647"
  ]
}
```

### "posts"."XCL_035" = 'Examples for teaching: Correlation does not mean causation'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_035\" = 'Examples for teaching: Correlation does not mean causation'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_055\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_040\" = T2.\"XCL_052\" WHERE T1.\"XCL_035\" = 'Examples for teaching: Correlation does not mean causation'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:544"
  ]
}
```

### "comments"."XCL_010" = 23853 AND "comments"."XCL_009" = '2013-07-12 09:08:18.0'

```json
{
  "kind": "predicate",
  "formula": "\"comments\".\"XCL_010\" = 23853 AND \"comments\".\"XCL_009\" = '2013-07-12 09:08:18.0'",
  "grain": [],
  "population_scope": "SELECT IIF(T2.\"XCL_044\" IS NULL, 'NOT well-finished', 'well-finished') AS resylt FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T1.\"XCL_010\" = 23853 AND T1.\"XCL_009\" = '2013-07-12 09:08:18.0'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:565"
  ]
}
```

### Badge Identifier

```json
{
  "kind": "binding",
  "formula": "\"badges\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_014\", T2.\"XCL_003\" FROM postHistory AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE T1.\"XCL_020\" = 'Samuel' AND STRFTIME('%Y', T1.\"XCL_016\") = '2013' AND STRFTIME('%Y', T2.\"XCL_004\") = '2013'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "postHistory"
      },
      {
        "role": "r1",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_003\" AS \"value\" FROM postHistory AS \"r0\" INNER JOIN badges AS \"r1\" ON \"r0\".\"XCL_017\" = \"r1\".\"XCL_002\" WHERE \"r0\".\"XCL_020\" = 'Samuel' AND STRFTIME('%Y', \"r0\".\"XCL_016\") = '2013' AND STRFTIME('%Y', \"r1\".\"XCL_004\") = '2013'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:652"
  ]
}
```

### "tags"."XCL_048" = 'careers'

```json
{
  "kind": "predicate",
  "formula": "\"tags\".\"XCL_048\" = 'careers'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_047\") FROM tags WHERE \"XCL_048\" = 'careers'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:696"
  ]
}
```

### "posts"."XCL_035" = 'Eliciting priors from experts'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_035\" = 'Eliciting priors from experts'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_058\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T1.\"XCL_035\" = 'Eliciting priors from experts'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:548"
  ]
}
```

### Minimum User XCL_053

```json
{
  "kind": "metric",
  "formula": "MIN(\"users\".\"XCL_053\")",
  "grain": [],
  "population_scope": "SELECT MIN(\"XCL_053\") FROM users",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MIN(\"r0\".\"XCL_053\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT MIN(\"r0\".\"XCL_053\") AS \"value\" FROM users AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:621"
  ]
}
```

### Latest Post ID for User

```json
{
  "kind": "binding",
  "formula": "\"postHistory\".\"XCL_014\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_014\" FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T2.\"XCL_014\" = T3.\"XCL_026\" WHERE T1.\"XCL_055\" = 'slashnick' ORDER BY T3.\"XCL_037\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:633"
  ]
}
```

### "posts"."XCL_034" LIKE '2010-07-19%'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_034\" LIKE '2010-07-19%'",
  "grain": [],
  "population_scope": "SELECT SUM(\"XCL_030\") FROM posts WHERE \"XCL_034\" LIKE '2010-07-19%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:664"
  ]
}
```

### Post Identifier

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'Vebjorn Ljosa'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_035\" AS \"value\" FROM posts AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_033\" = \"r1\".\"XCL_052\" WHERE \"r1\".\"XCL_055\" = 'Vebjorn Ljosa'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:582"
  ]
}
```

### Aggregates the total number of badge records (XCL_001) where the badge type (XCL_003) is 'Teacher' and the associated user (via XCL_002 = XCL_052) has

```json
{
  "kind": "metric",
  "formula": "COUNT(\"badges\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T2.\"XCL_058\" = 'India' AND T1.\"XCL_003\" = 'Teacher'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "badges"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM badges AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_052\" WHERE \"r1\".\"XCL_058\" = 'India' AND \"r0\".\"XCL_003\" = 'Teacher'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:597"
  ]
}
```

### Badge Identifier

```json
{
  "kind": "binding",
  "formula": "\"badges\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_055\" = 'Sharpie'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_003\" AS \"value\" FROM users AS \"r0\" INNER JOIN badges AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_002\" WHERE \"r0\".\"XCL_055\" = 'Sharpie'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:622"
  ]
}
```

### "users"."XCL_055" = 'Tiago Pasqualini'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'Tiago Pasqualini'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T1.\"XCL_055\" = 'Tiago Pasqualini'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:567"
  ]
}
```

### Max XCL_053 for Harlan/Jarrod Dixon

```json
{
  "kind": "metric",
  "formula": "MAX(\"users\".\"XCL_053\")",
  "grain": [],
  "population_scope": "SELECT MAX(\"XCL_053\") FROM users WHERE \"XCL_055\" IN ('Harlan', 'Jarrod Dixon')",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MAX(\"r0\".\"XCL_053\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT MAX(\"r0\".\"XCL_053\") AS \"value\" FROM users AS \"r0\" WHERE \"r0\".\"XCL_055\" IN ('Harlan', 'Jarrod Dixon')",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:531"
  ]
}
```

### Post Link Identifier (XCL_025)

```json
{
  "kind": "binding",
  "formula": "\"postLinks\".\"XCL_025\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_030\", T2.\"XCL_025\" FROM posts AS T1 INNER JOIN postLinks AS T2 ON T1.\"XCL_026\" = T2.\"XCL_023\" WHERE T2.\"XCL_023\" = 395",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_025\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "postLinks"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_025\" AS \"value\" FROM posts AS \"r0\" INNER JOIN postLinks AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_023\" WHERE \"r1\".\"XCL_023\" = 395",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:601"
  ]
}
```

### Aggregates the count of user identifiers (XCL_052) from the users table. The population is restricted to users where XCL_064 is greater than 65 and wh

```json
{
  "kind": "metric",
  "formula": "COUNT(\"users\".\"XCL_052\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_064\" > 65 AND T2.\"XCL_003\" = 'Supporter'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_052\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_052\") AS \"value\" FROM users AS \"r0\" INNER JOIN badges AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_002\" WHERE \"r0\".\"XCL_064\" > 65 AND \"r1\".\"XCL_003\" = 'Supporter'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:623"
  ]
}
```

### Counts the number of user IDs (users.XCL_052) associated with posts that have a specific vote type (votes.XCL_066). The population is restricted to po

```json
{
  "kind": "metric",
  "formula": "COUNT(\"users\".\"XCL_052\")",
  "grain": [
    "\"postHistory\".\"XCL_014\"",
    "\"votes\".\"XCL_066\""
  ],
  "population_scope": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T2.\"XCL_014\" = T3.\"XCL_026\" INNER JOIN votes AS T4 ON T4.\"XCL_067\" = T3.\"XCL_026\" WHERE T1.\"XCL_055\" = 'Matt Parker' GROUP BY T2.\"XCL_014\", T4.\"XCL_066\" HAVING COUNT(T4.\"XCL_066\") > 4",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_052\")",
    "grain": [
      "\"r1\".\"XCL_014\"",
      "\"r3\".\"XCL_066\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "postHistory"
      },
      {
        "role": "r2",
        "physical_table": "posts"
      },
      {
        "role": "r3",
        "physical_table": "votes"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_014\" AS \"grain_0\", \"r3\".\"XCL_066\" AS \"grain_1\", COUNT(\"r0\".\"XCL_052\") AS \"value\" FROM users AS \"r0\" INNER JOIN postHistory AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_017\" INNER JOIN posts AS \"r2\" ON \"r1\".\"XCL_014\" = \"r2\".\"XCL_026\" INNER JOIN votes AS \"r3\" ON \"r3\".\"XCL_067\" = \"r2\".\"XCL_026\" WHERE \"r0\".\"XCL_055\" = 'Matt Parker' GROUP BY \"r1\".\"XCL_014\", \"r3\".\"XCL_066\" HAVING COUNT(\"r3\".\"XCL_066\") > 4",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:635"
  ]
}
```

### Post Identifier

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_039\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_039\" FROM posts AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_026\" = T2.\"XCL_006\" WHERE T2.\"XCL_009\" = '2014-04-23 20:29:39.0' AND T2.\"XCL_010\" = 3025",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_039\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "comments"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_039\" AS \"value\" FROM posts AS \"r0\" INNER JOIN comments AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_006\" WHERE \"r1\".\"XCL_009\" = '2014-04-23 20:29:39.0' AND \"r1\".\"XCL_010\" = 3025",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:563"
  ]
}
```

### Badge Identifier

```json
{
  "kind": "binding",
  "formula": "\"badges\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\" FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "badges"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_003\" AS \"value\" FROM badges AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_052\" WHERE \"r1\".\"XCL_055\" = 'csgillespie'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:552"
  ]
}
```

### Post Identifier

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_026\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_026\" FROM votes AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_067\" = T2.\"XCL_026\" WHERE T1.\"XCL_070\" = 1465 ORDER BY T2.\"XCL_039\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:666"
  ]
}
```

### "votes"."XCL_071" = 50 AND STRFTIME('%Y', "votes"."XCL_069") = '2011'

```json
{
  "kind": "predicate",
  "formula": "\"votes\".\"XCL_071\" = 50 AND STRFTIME('%Y', \"votes\".\"XCL_069\") = '2011'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN votes AS T2 ON T1.\"XCL_026\" = T2.\"XCL_067\" WHERE T2.\"XCL_071\" = 50 AND STRFTIME('%Y', T2.\"XCL_069\") = '2011'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:662"
  ]
}
```

### Counts the number of rows in the postHistory table that are linked to a specific user via the join condition. The population is restricted to post his

```json
{
  "kind": "metric",
  "formula": "COUNT(\"users\".\"XCL_052\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" WHERE T1.\"XCL_055\" = 'Daniel Vassallo'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_052\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "postHistory"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_052\") AS \"value\" FROM users AS \"r0\" INNER JOIN postHistory AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_017\" WHERE \"r0\".\"XCL_055\" = 'Daniel Vassallo'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:631"
  ]
}
```

### Aggregates the total number of badge records where the class is 'Supporter' and the date falls within the year 2011. The grain is a single scalar valu

```json
{
  "kind": "metric",
  "formula": "COUNT(\"badges\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM badges WHERE STRFTIME('%Y', \"XCL_004\") = '2011' AND \"XCL_003\" = 'Supporter'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM badges AS \"r0\" WHERE STRFTIME('%Y', \"r0\".\"XCL_004\") = '2011' AND \"r0\".\"XCL_003\" = 'Supporter'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:591"
  ]
}
```

### Aggregates the total number of post records (identified by XCL_026) belonging to the user with username 'csgillespie' where the post attribute XCL_043

```json
{
  "kind": "metric",
  "formula": "COUNT(\"posts\".\"XCL_026\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie' AND T1.\"XCL_043\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_026\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_026\") AS \"value\" FROM posts AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_033\" = \"r1\".\"XCL_052\" WHERE \"r1\".\"XCL_055\" = 'csgillespie' AND \"r0\".\"XCL_043\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:545"
  ]
}
```

### "comments"."XCL_010" = 13

```json
{
  "kind": "predicate",
  "formula": "\"comments\".\"XCL_010\" = 13",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_005\") FROM comments WHERE \"XCL_010\" = 13",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:588"
  ]
}
```

### "posts"."XCL_035" = 'Analysing wind data with R'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_035\" = 'Analysing wind data with R'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_008\", T1.\"XCL_055\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" INNER JOIN comments AS T3 ON T2.\"XCL_026\" = T3.\"XCL_006\" WHERE T2.\"XCL_035\" = 'Analysing wind data with R' ORDER BY T1.\"XCL_054\" DESC LIMIT 10",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:694"
  ]
}
```

### "posts"."XCL_030" > 60

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_030\" > 60",
  "grain": [],
  "population_scope": "SELECT \"XCL_026\" FROM posts WHERE \"XCL_030\" > 60",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:602"
  ]
}
```

### The value of the column "XCL_054" from the users table, filtered to rows where "XCL_055" equals 'IrishStat'. Returns a single identifier or list of id

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_054\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_054\" FROM users WHERE \"XCL_055\" = 'IrishStat'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_054\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_054\" AS \"value\" FROM users AS \"r0\" WHERE \"r0\".\"XCL_055\" = 'IrishStat'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:699"
  ]
}
```

### "posts"."XCL_031" >= 1000

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_031\" >= 1000",
  "grain": [
    "\"postHistory\".\"XCL_017\""
  ],
  "population_scope": "SELECT T2.\"XCL_017\" FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T2.\"XCL_014\" = T3.\"XCL_026\" WHERE T3.\"XCL_031\" >= 1000 GROUP BY T2.\"XCL_017\" HAVING COUNT(DISTINCT T2.\"XCL_013\") = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:595"
  ]
}
```

### Latest non-null post identifier

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_033\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_033\" FROM posts WHERE NOT \"XCL_043\" IS NULL ORDER BY \"XCL_030\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:656"
  ]
}
```

### Badge XCL_003

```json
{
  "kind": "binding",
  "formula": "\"badges\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_053\" = (SELECT MIN(\"XCL_053\") FROM users)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:621"
  ]
}
```

### Returns the value of column XCL_061 from the users table for users who have authored a comment with the specific text 'fine, you win :)'. The grain is

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_061\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_053\", T2.\"XCL_061\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_008\" = 'fine, you win :)'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_061\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_061\" AS \"value\" FROM comments AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_052\" WHERE \"r0\".\"XCL_008\" = 'fine, you win :)'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:705"
  ]
}
```

### Calculates the percentage of badge records where the associated user's XCL_064 value is between 13 and 18, relative to the total count of badge record

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(\"users\".\"XCL_064\" BETWEEN 13 AND 18, 1, 0)) AS REAL) * 100 / COUNT(\"badges\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(T2.\"XCL_064\" BETWEEN 13 AND 18, 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_001\") FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T1.\"XCL_003\" = 'Organizer'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(IIF(\"r1\".\"XCL_064\" BETWEEN 13 AND 18, 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "badges"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(IIF(\"r1\".\"XCL_064\" BETWEEN 13 AND 18, 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM badges AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_052\" WHERE \"r0\".\"XCL_003\" = 'Organizer'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:615"
  ]
}
```

### Comment Identifier

```json
{
  "kind": "binding",
  "formula": "\"comments\".\"XCL_007\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_007\" FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T1.\"XCL_009\" = '2010-07-19 19:19:56.0'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_007\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_007\" AS \"value\" FROM comments AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_006\" = \"r1\".\"XCL_026\" WHERE \"r0\".\"XCL_009\" = '2010-07-19 19:19:56.0'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:616"
  ]
}
```

### Aggregates the total number of rows in the 'badges' table where the column 'XCL_003' equals the literal 'Revival'. The metric counts the values in col

```json
{
  "kind": "metric",
  "formula": "COUNT(\"badges\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM badges WHERE \"XCL_003\" = 'Revival'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM badges AS \"r0\" WHERE \"r0\".\"XCL_003\" = 'Revival'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:560"
  ]
}
```

### "posts"."XCL_043" = 107829 AND "posts"."XCL_038" = 1

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_043\" = 107829 AND \"posts\".\"XCL_038\" = 1",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_008\" FROM posts AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_026\" = T2.\"XCL_006\" WHERE T1.\"XCL_043\" = 107829 AND T1.\"XCL_038\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:564"
  ]
}
```

### "postHistory"."XCL_014" = 3720

```json
{
  "kind": "predicate",
  "formula": "\"postHistory\".\"XCL_014\" = 3720",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_013\", (SELECT COUNT(DISTINCT \"XCL_010\") FROM comments WHERE \"XCL_006\" = 3720) AS NumberOfUsers FROM postHistory AS T1 WHERE T1.\"XCL_014\" = 3720",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:599"
  ]
}
```

### "posts"."XCL_035" = 'What are principal component scores?'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_035\" = 'What are principal component scores?'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_035\", T2.\"XCL_025\" FROM posts AS T1 INNER JOIN postLinks AS T2 ON T1.\"XCL_026\" = T2.\"XCL_023\" INNER JOIN posts AS T3 ON T2.\"XCL_024\" = T3.\"XCL_026\" WHERE T1.\"XCL_035\" = 'What are principal component scores?'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:655"
  ]
}
```

### Badge Count per Group

```json
{
  "kind": "metric",
  "formula": "COUNT(\"badges\".\"XCL_003\")",
  "grain": [
    "\"badges\".\"XCL_002\""
  ],
  "population_scope": "SELECT \"XCL_002\", COUNT(\"XCL_003\") AS num FROM badges GROUP BY \"XCL_002\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_003\")",
    "grain": [
      "\"r0\".\"XCL_002\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_002\" AS \"grain_0\", COUNT(\"r0\".\"XCL_003\") AS \"value\" FROM badges AS \"r0\" GROUP BY \"r0\".\"XCL_002\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:592"
  ]
}
```

### "tags"."XCL_049" BETWEEN 5000 AND 7000

```json
{
  "kind": "predicate",
  "formula": "\"tags\".\"XCL_049\" BETWEEN 5000 AND 7000",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_047\") FROM tags WHERE \"XCL_049\" BETWEEN 5000 AND 7000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:659"
  ]
}
```

### "users"."XCL_055" = 'Daniel Vassallo'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'Daniel Vassallo'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" WHERE T1.\"XCL_055\" = 'Daniel Vassallo'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:631"
  ]
}
```

### "users"."XCL_058" = 'Vienna, Austria'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_058\" = 'Vienna, Austria'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_064\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_058\" = 'Vienna, Austria'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:618"
  ]
}
```

### "badges"."XCL_004" = '2010-07-19 19:39:08.0'

```json
{
  "kind": "predicate",
  "formula": "\"badges\".\"XCL_004\" = '2010-07-19 19:39:08.0'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_060\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_004\" = '2010-07-19 19:39:08.0'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:620"
  ]
}
```

### Average XCL_031

```json
{
  "kind": "metric",
  "formula": "AVG(\"posts\".\"XCL_031\")",
  "grain": [],
  "population_scope": "SELECT AVG(\"XCL_031\") FROM posts",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r0\".\"XCL_031\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT AVG(\"r0\".\"XCL_031\") AS \"value\" FROM posts AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:686"
  ]
}
```

### "users"."XCL_064" BETWEEN 19 AND 65 AND "users"."XCL_061" > 5000

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_064\" BETWEEN 19 AND 65 AND \"users\".\"XCL_061\" > 5000",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_052\") FROM users WHERE \"XCL_064\" BETWEEN 19 AND 65 AND \"XCL_061\" > 5000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:691"
  ]
}
```

### Comment Identifier XCL_008

```json
{
  "kind": "binding",
  "formula": "\"comments\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_008\" FROM comments WHERE \"XCL_007\" = 17",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_008\" AS \"value\" FROM comments AS \"r0\" WHERE \"r0\".\"XCL_007\" = 17",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:573"
  ]
}
```

### The value of column XCL_052 from the users table for the row where XCL_064 equals the maximum XCL_064. This identifies the specific user associated wi

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_052\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_052\" FROM users WHERE \"XCL_064\" = (SELECT MAX(\"XCL_064\") FROM users)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:673"
  ]
}
```

### Average Post XCL_031

```json
{
  "kind": "metric",
  "formula": "AVG(\"posts\".\"XCL_031\")",
  "grain": [
    "\"posts\".\"XCL_035\"",
    "\"comments\".\"XCL_008\""
  ],
  "population_scope": "SELECT AVG(T2.\"XCL_031\"), T2.\"XCL_035\", T1.\"XCL_008\" FROM comments AS T1 INNER JOIN posts AS T2 ON T2.\"XCL_026\" = T1.\"XCL_006\" WHERE T2.\"XCL_036\" = '<humor>' GROUP BY T2.\"XCL_035\", T1.\"XCL_008\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r1\".\"XCL_031\")",
    "grain": [
      "\"r1\".\"XCL_035\"",
      "\"r0\".\"XCL_008\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_035\" AS \"grain_0\", \"r0\".\"XCL_008\" AS \"grain_1\", AVG(\"r1\".\"XCL_031\") AS \"value\" FROM comments AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r1\".\"XCL_026\" = \"r0\".\"XCL_006\" WHERE \"r1\".\"XCL_036\" = '<humor>' GROUP BY \"r1\".\"XCL_035\", \"r0\".\"XCL_008\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:587"
  ]
}
```

### "posts"."XCL_031" BETWEEN 100 AND 150

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_031\" BETWEEN 100 AND 150",
  "grain": [],
  "population_scope": "SELECT \"XCL_026\" FROM posts WHERE \"XCL_031\" BETWEEN 100 AND 150",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:707"
  ]
}
```

### STRFTIME('%Y', "badges"."XCL_004") = '2011' AND "badges"."XCL_003" = 'Supporter'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"badges\".\"XCL_004\") = '2011' AND \"badges\".\"XCL_003\" = 'Supporter'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM badges WHERE STRFTIME('%Y', \"XCL_004\") = '2011' AND \"XCL_003\" = 'Supporter'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:591"
  ]
}
```

### The value of the 'XCL_055' column from the 'users' table. This represents a specific attribute of the user associated with the post titled 'Eliciting 

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_055\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T1.\"XCL_035\" = 'Eliciting priors from experts'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_055\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_055\" AS \"value\" FROM posts AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_033\" = \"r1\".\"XCL_052\" WHERE \"r0\".\"XCL_035\" = 'Eliciting priors from experts'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:539"
  ]
}
```

### User Attribute XCL_058

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_058\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_055\", T2.\"XCL_058\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T1.\"XCL_026\" = 183 ORDER BY T1.\"XCL_041\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:689"
  ]
}
```

### Count of users filtered by age between 19 and 65 and a value in XCL_061 greater than 5000.

```json
{
  "kind": "metric",
  "formula": "COUNT(\"users\".\"XCL_052\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_052\") FROM users WHERE \"XCL_064\" BETWEEN 19 AND 65 AND \"XCL_061\" > 5000",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_052\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_052\") AS \"value\" FROM users AS \"r0\" WHERE \"r0\".\"XCL_064\" BETWEEN 19 AND 65 AND \"r0\".\"XCL_061\" > 5000",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:691"
  ]
}
```

### "users"."XCL_060" > 200

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_060\" > 200",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(T1.\"XCL_001\") AS REAL) / COUNT(DISTINCT T2.\"XCL_055\") FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T2.\"XCL_060\" > 200",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:556"
  ]
}
```

### Counts the number of posts associated with a specific user. The population is restricted to posts linked to the user identified by the name 'Tiago Pas

```json
{
  "kind": "metric",
  "formula": "COUNT(\"users\".\"XCL_052\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T1.\"XCL_055\" = 'Tiago Pasqualini'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_052\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_052\") AS \"value\" FROM users AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_033\" WHERE \"r0\".\"XCL_055\" = 'Tiago Pasqualini'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:567"
  ]
}
```

### "comments"."XCL_007" BETWEEN 5 AND 10

```json
{
  "kind": "predicate",
  "formula": "\"comments\".\"XCL_007\" BETWEEN 5 AND 10",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(T1.\"XCL_061\" = 0, 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_052\") AS per FROM users AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_052\" = T2.\"XCL_010\" WHERE T2.\"XCL_007\" BETWEEN 5 AND 10",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:716"
  ]
}
```

### Post Identifier

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_036\" FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T2.\"XCL_014\" = T3.\"XCL_026\" WHERE T1.\"XCL_055\" = 'John Salvatier'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "postHistory"
      },
      {
        "role": "r2",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_036\" AS \"value\" FROM users AS \"r0\" INNER JOIN postHistory AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_017\" INNER JOIN posts AS \"r2\" ON \"r1\".\"XCL_014\" = \"r2\".\"XCL_026\" WHERE \"r0\".\"XCL_055\" = 'John Salvatier'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:630"
  ]
}
```

### The value of column XCL_055 for the user(s) where XCL_053 equals the maximum XCL_053 in the table. Returns the XCL_055 associated with the peak XCL_05

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_055\" FROM users WHERE \"XCL_053\" = (SELECT MAX(\"XCL_053\") FROM users)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:674"
  ]
}
```

### Returns the value of column XCL_053 from the users table for users who have authored a comment with the specific text 'fine, you win :)'. The grain is

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_053\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_053\", T2.\"XCL_061\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_008\" = 'fine, you win :)'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_053\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_053\" AS \"value\" FROM comments AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_052\" WHERE \"r0\".\"XCL_008\" = 'fine, you win :)'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:705"
  ]
}
```

### "comments"."XCL_007" = 0 AND "users"."XCL_064" = 40

```json
{
  "kind": "predicate",
  "formula": "\"comments\".\"XCL_007\" = 0 AND \"users\".\"XCL_064\" = 40",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_005\") FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_007\" = 0 AND T2.\"XCL_064\" = 40",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:711"
  ]
}
```

### Identifier for the post (XCL_026) associated with comments, filtered to the specific post titled 'Group differences on a five point Likert item'.

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_026\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_026\", T1.\"XCL_008\" FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T2.\"XCL_035\" = 'Group differences on a five point Likert item'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_026\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_026\" AS \"value\" FROM comments AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_006\" = \"r1\".\"XCL_026\" WHERE \"r1\".\"XCL_035\" = 'Group differences on a five point Likert item'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:712"
  ]
}
```

### "users"."XCL_055" = 'Harvey Motulsky'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'Harvey Motulsky'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_008\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'Harvey Motulsky'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:714"
  ]
}
```

### The identifier (XCL_055) of the user who authored the comment. This is an output field linking the comment back to the user entity.

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_008\", T1.\"XCL_055\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" INNER JOIN comments AS T3 ON T2.\"XCL_026\" = T3.\"XCL_006\" WHERE T2.\"XCL_035\" = 'Analysing wind data with R' ORDER BY T1.\"XCL_054\" DESC LIMIT 10",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:694"
  ]
}
```

### Aggregates the count of user identifiers (XCL_052) from the users table. The population is restricted to users who have an associated badge of type 'S

```json
{
  "kind": "metric",
  "formula": "COUNT(\"users\".\"XCL_052\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'Supporter' AND T1.\"XCL_064\" BETWEEN 19 AND 65",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_052\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_052\") AS \"value\" FROM users AS \"r0\" INNER JOIN badges AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_002\" WHERE \"r1\".\"XCL_003\" = 'Supporter' AND \"r0\".\"XCL_064\" BETWEEN 19 AND 65",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:619"
  ]
}
```

### Post Identifier XCL_026

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_026\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_026\" FROM posts WHERE \"XCL_031\" > (SELECT AVG(\"XCL_031\") FROM posts)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:686"
  ]
}
```

### Identifier from the users table (T2) for users who have authored at least one comment containing an HTTP URL. Grain: one row per matching user-comment

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_054\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_054\", T2.\"XCL_064\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_008\" LIKE '%http://%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_054\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_054\" AS \"value\" FROM comments AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_052\" WHERE \"r0\".\"XCL_008\" LIKE '%http://%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:708"
  ]
}
```

### "users"."XCL_061" > 100 AND "users"."XCL_062" > 1

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_061\" > 100 AND \"users\".\"XCL_062\" > 1",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_052\") FROM users WHERE \"XCL_061\" > 100 AND \"XCL_062\" > 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:535"
  ]
}
```

### Comment Identifier

```json
{
  "kind": "binding",
  "formula": "\"comments\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_008\" FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T2.\"XCL_035\" LIKE '%linear regression%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_008\" AS \"value\" FROM comments AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_006\" = \"r1\".\"XCL_026\" WHERE \"r1\".\"XCL_035\" LIKE '%linear regression%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:706"
  ]
}
```

### Post Attribute

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_026\", T2.\"XCL_035\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T1.\"XCL_055\" = 'Harvey Motulsky' ORDER BY T2.\"XCL_031\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:678"
  ]
}
```

### User Attribute XCL_053

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_053\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_053\", \"XCL_060\" FROM users WHERE \"XCL_055\" = 'Jarrod Dixon'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_053\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_053\" AS \"value\" FROM users AS \"r0\" WHERE \"r0\".\"XCL_055\" = 'Jarrod Dixon'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:697"
  ]
}
```

### "users"."XCL_058" = 'New York'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_058\" = 'New York'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_052\") FROM users WHERE \"XCL_058\" = 'New York'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:625"
  ]
}
```

### Aggregates the count of user identifiers (XCL_052) from the users table, restricted to records where the user name (XCL_055) is 'Harlan' and the user 

```json
{
  "kind": "metric",
  "formula": "COUNT(\"users\".\"XCL_052\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN votes AS T3 ON T3.\"XCL_067\" = T2.\"XCL_014\" WHERE T1.\"XCL_055\" = 'Harlan'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_052\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "postHistory"
      },
      {
        "role": "r2",
        "physical_table": "votes"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_052\") AS \"value\" FROM users AS \"r0\" INNER JOIN postHistory AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_017\" INNER JOIN votes AS \"r2\" ON \"r2\".\"XCL_067\" = \"r1\".\"XCL_014\" WHERE \"r0\".\"XCL_055\" = 'Harlan'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:632"
  ]
}
```

### Aggregates the total number of badge records associated with a specific user, filtered by the user's identifier value 'csgillespie'.

```json
{
  "kind": "metric",
  "formula": "COUNT(\"badges\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "badges"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM badges AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_052\" WHERE \"r1\".\"XCL_055\" = 'csgillespie'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:551"
  ]
}
```

### Badge Identifier

```json
{
  "kind": "binding",
  "formula": "\"badges\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_055\" = 'SilentGhost'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_003\" AS \"value\" FROM users AS \"r0\" INNER JOIN badges AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_002\" WHERE \"r0\".\"XCL_055\" = 'SilentGhost'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:575"
  ]
}
```

### Aggregates the total number of badge records (count of XCL_001) for a specific user (XCL_055 = 'csgillespie') where the badge date (XCL_004) falls wit

```json
{
  "kind": "metric",
  "formula": "COUNT(\"badges\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE STRFTIME('%Y', T1.\"XCL_004\") = '2011' AND T2.\"XCL_055\" = 'csgillespie'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "badges"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM badges AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_052\" WHERE STRFTIME('%Y', \"r0\".\"XCL_004\") = '2011' AND \"r1\".\"XCL_055\" = 'csgillespie'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:553"
  ]
}
```

### "users"."XCL_055" = 'chl'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'chl'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_069\" FROM users AS T1 INNER JOIN votes AS T2 ON T1.\"XCL_052\" = T2.\"XCL_070\" WHERE T1.\"XCL_055\" = 'chl' ORDER BY T2.\"XCL_069\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:669"
  ]
}
```

### The identifier (XCL_017) of users who have exactly one distinct post history entry (XCL_013) associated with posts that have a score (XCL_031) of at l

```json
{
  "kind": "binding",
  "formula": "\"postHistory\".\"XCL_017\"",
  "grain": [
    "\"postHistory\".\"XCL_017\""
  ],
  "population_scope": "SELECT T2.\"XCL_017\" FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T2.\"XCL_014\" = T3.\"XCL_026\" WHERE T3.\"XCL_031\" >= 1000 GROUP BY T2.\"XCL_017\" HAVING COUNT(DISTINCT T2.\"XCL_013\") = 1",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_017\"",
    "grain": [
      "\"r1\".\"XCL_017\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "postHistory"
      },
      {
        "role": "r2",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_017\" AS \"grain_0\", \"r1\".\"XCL_017\" AS \"value\" FROM users AS \"r0\" INNER JOIN postHistory AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_017\" INNER JOIN posts AS \"r2\" ON \"r1\".\"XCL_014\" = \"r2\".\"XCL_026\" WHERE \"r2\".\"XCL_031\" >= 1000 GROUP BY \"r1\".\"XCL_017\" HAVING COUNT(DISTINCT \"r1\".\"XCL_013\") = 1",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:595"
  ]
}
```

### "posts"."XCL_038" = 1 AND "posts"."XCL_030" = 0

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_038\" = 1 AND \"posts\".\"XCL_030\" = 0",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_005\") FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T2.\"XCL_038\" = 1 AND T2.\"XCL_030\" = 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:710"
  ]
}
```

### The value of column XCL_055 from the users table for the single user associated with the post having the highest value in column XCL_039.

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_055\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" ORDER BY T1.\"XCL_039\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:541"
  ]
}
```

### The value of column "XCL_050" from the "tags" table for the single row with the highest value in column "XCL_049". This subquery acts as a filter cond

```json
{
  "kind": "binding",
  "formula": "\"tags\".\"XCL_050\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_050\" FROM tags ORDER BY \"XCL_049\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:550"
  ]
}
```

### Aggregates the total number of rows in the 'badges' table where the column 'XCL_003' equals the literal 'Announcer'. The metric counts the values in c

```json
{
  "kind": "metric",
  "formula": "COUNT(\"badges\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM badges WHERE \"XCL_003\" = 'Announcer'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM badges AS \"r0\" WHERE \"r0\".\"XCL_003\" = 'Announcer'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:605"
  ]
}
```

### The total number of rows in the 'users' table, calculated by counting the 'XCL_052' column. This serves as the denominator for the percentage calculat

```json
{
  "kind": "metric",
  "formula": "COUNT(\"users\".\"XCL_052\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_052\") FROM users",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_052\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_052\") AS \"value\" FROM users AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:614"
  ]
}
```

### The value of the 'XCL_055' column from the 'users' table. This represents the specific user associated with the post titled 'Open source tools for vis

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_055\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T1.\"XCL_035\" = 'Open source tools for visualizing multi-dimensional data?'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_055\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_055\" AS \"value\" FROM posts AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_033\" = \"r1\".\"XCL_052\" WHERE \"r0\".\"XCL_035\" = 'Open source tools for visualizing multi-dimensional data?'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:581"
  ]
}
```

### The value of column XCL_064 for the user(s) in the users table where XCL_053 equals the maximum XCL_053 value. Returns the specific attribute associat

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_064\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_064\" FROM users WHERE \"XCL_053\" = (SELECT MAX(\"XCL_053\") FROM users)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:661"
  ]
}
```

### "users"."XCL_055" = 'Community'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'Community'",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(T3.\"XCL_048\" = 'r', 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN tags AS T3 ON T3.\"XCL_050\" = T2.\"XCL_014\" WHERE T1.\"XCL_055\" = 'Community'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:639"
  ]
}
```

### Count of unique comment identifiers (XCL_005) from the comments table, filtered to active comments (XCL_007 = 0) and joined to users with status 40 (X

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"comments\".\"XCL_005\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_005\") FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_007\" = 0 AND T2.\"XCL_064\" = 40",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_005\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r0\".\"XCL_005\") AS \"value\" FROM comments AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_052\" WHERE \"r0\".\"XCL_007\" = 0 AND \"r1\".\"XCL_064\" = 40",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:711"
  ]
}
```

### "badges"."XCL_003" IN ('Supporter', 'Teacher') AND "users"."XCL_058" = 'New York'

```json
{
  "kind": "predicate",
  "formula": "\"badges\".\"XCL_003\" IN ('Supporter', 'Teacher') AND \"users\".\"XCL_058\" = 'New York'",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT T1.\"XCL_001\") FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T1.\"XCL_003\" IN ('Supporter', 'Teacher') AND T2.\"XCL_058\" = 'New York'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:593"
  ]
}
```

### Aggregates the count of non-null values in column XCL_052 from the users table, filtered to rows where the year extracted from XCL_054 is greater than

```json
{
  "kind": "metric",
  "formula": "COUNT(\"users\".\"XCL_052\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_052\") FROM users WHERE STRFTIME('%Y', \"XCL_054\") > '2013' AND \"XCL_060\" > 10",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_052\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_052\") AS \"value\" FROM users AS \"r0\" WHERE STRFTIME('%Y', \"r0\".\"XCL_054\") > '2013' AND \"r0\".\"XCL_060\" > 10",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:536"
  ]
}
```

### Post Identifier

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\" FROM posts AS T1 INNER JOIN postLinks AS T2 ON T2.\"XCL_023\" = T1.\"XCL_026\" ORDER BY T1.\"XCL_029\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:667"
  ]
}
```

### Comment Content

```json
{
  "kind": "binding",
  "formula": "\"comments\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_026\", T1.\"XCL_008\" FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T2.\"XCL_035\" = 'Group differences on a five point Likert item'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_008\" AS \"value\" FROM comments AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_006\" = \"r1\".\"XCL_026\" WHERE \"r1\".\"XCL_035\" = 'Group differences on a five point Likert item'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:712"
  ]
}
```

### "posts"."XCL_035" = 'Open source tools for visualizing multi-dimensional data?'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_035\" = 'Open source tools for visualizing multi-dimensional data?'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_055\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T1.\"XCL_035\" = 'Open source tools for visualizing multi-dimensional data?'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:581"
  ]
}
```

### "posts"."XCL_035" = 'How does gentle boosting differ from AdaBoost?'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_035\" = 'How does gentle boosting differ from AdaBoost?'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_008\" FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T2.\"XCL_035\" = 'How does gentle boosting differ from AdaBoost?'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:579"
  ]
}
```

### The value of column XCL_055 from the users table, filtered to records where the year component of XCL_054 is 2011. Grain: one row per matching user re

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_055\" FROM users WHERE STRFTIME('%Y', \"XCL_054\") = '2011'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_055\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_055\" AS \"value\" FROM users AS \"r0\" WHERE STRFTIME('%Y', \"r0\".\"XCL_054\") = '2011'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:532"
  ]
}
```

### "users"."XCL_055" = 'Harvey Motulsky' OR "users"."XCL_055" = 'Noah Snyder'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'Harvey Motulsky' OR \"users\".\"XCL_055\" = 'Noah Snyder'",
  "grain": [
    "\"users\".\"XCL_055\""
  ],
  "population_scope": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T2.\"XCL_014\" = T3.\"XCL_026\" WHERE T1.\"XCL_055\" = 'Harvey Motulsky' OR T1.\"XCL_055\" = 'Noah Snyder' GROUP BY T1.\"XCL_055\" ORDER BY SUM(T3.\"XCL_031\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:634"
  ]
}
```

### STRFTIME('%Y', "users"."XCL_054") > '2013' AND "users"."XCL_060" > 10

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"users\".\"XCL_054\") > '2013' AND \"users\".\"XCL_060\" > 10",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_052\") FROM users WHERE STRFTIME('%Y', \"XCL_054\") > '2013' AND \"XCL_060\" > 10",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:536"
  ]
}
```

### STRFTIME('%Y', "users"."XCL_054") = '2010'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"users\".\"XCL_054\") = '2010'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_033\", T1.\"XCL_055\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE STRFTIME('%Y', T1.\"XCL_054\") = '2010' ORDER BY T2.\"XCL_039\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:682"
  ]
}
```

### "users"."XCL_055" = 'Harvey Motulsky'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'Harvey Motulsky'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_026\", T2.\"XCL_035\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T1.\"XCL_055\" = 'Harvey Motulsky' ORDER BY T2.\"XCL_031\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:678"
  ]
}
```

### Badge User Numeric Difference

```json
{
  "kind": "binding",
  "formula": "\"badges\".\"XCL_004\" - \"users\".\"XCL_054\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_004\" - T2.\"XCL_054\" FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'Zolomon'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_004\" - \"r1\".\"XCL_054\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "badges"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_004\" - \"r1\".\"XCL_054\" AS \"value\" FROM badges AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_052\" WHERE \"r1\".\"XCL_055\" = 'Zolomon'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:692"
  ]
}
```

### Aggregated sum of the 'XCL_071' column from the 'votes' table, restricted to votes associated with 'posts' where the 'XCL_035' column contains the sub

```json
{
  "kind": "metric",
  "formula": "SUM(\"votes\".\"XCL_071\")",
  "grain": [],
  "population_scope": "SELECT SUM(T2.\"XCL_071\") FROM posts AS T1 INNER JOIN votes AS T2 ON T1.\"XCL_026\" = T2.\"XCL_067\" WHERE T1.\"XCL_035\" LIKE '%data%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "SUM(\"r1\".\"XCL_071\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "votes"
      }
    ],
    "scope_sql": "SELECT SUM(\"r1\".\"XCL_071\") AS \"value\" FROM posts AS \"r0\" INNER JOIN votes AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_067\" WHERE \"r0\".\"XCL_035\" LIKE '%data%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:585"
  ]
}
```

### "users"."XCL_055" = 'Mark Meckes' AND "posts"."XCL_038" = 0

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'Mark Meckes' AND \"posts\".\"XCL_038\" = 0",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_036\" FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T3.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_055\" = 'Mark Meckes' AND T3.\"XCL_038\" = 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:637"
  ]
}
```

### Badge Count

```json
{
  "kind": "metric",
  "formula": "COUNT(\"badges\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM badges WHERE \"XCL_003\" = 'Citizen Patrol'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM badges AS \"r0\" WHERE \"r0\".\"XCL_003\" = 'Citizen Patrol'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:695"
  ]
}
```

### Post Identifier

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_033\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_033\", T1.\"XCL_055\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE STRFTIME('%Y', T1.\"XCL_054\") = '2010' ORDER BY T2.\"XCL_039\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:682"
  ]
}
```

### Average Monthly Post Link Count

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(\"postLinks\".\"XCL_021\") AS REAL) / 12",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(T1.\"XCL_021\") AS REAL) / 12 FROM postLinks AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_023\" = T2.\"XCL_026\" WHERE T2.\"XCL_037\" <= 2 AND STRFTIME('%Y', T1.\"XCL_022\") = '2010'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(\"r0\".\"XCL_021\") AS REAL) / 12",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "postLinks"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(\"r0\".\"XCL_021\") AS REAL) / 12 AS \"value\" FROM postLinks AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_023\" = \"r1\".\"XCL_026\" WHERE \"r1\".\"XCL_037\" <= 2 AND STRFTIME('%Y', \"r0\".\"XCL_022\") = '2010'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:665"
  ]
}
```

### Aggregates the total number of rows in the 'votes' table where the year extracted from the 'XCL_069' timestamp column is '2010'. The grain is a single

```json
{
  "kind": "metric",
  "formula": "COUNT(\"votes\".\"XCL_066\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_066\") FROM votes WHERE STRFTIME('%Y', \"XCL_069\") = '2010'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_066\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "votes"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_066\") AS \"value\" FROM votes AS \"r0\" WHERE STRFTIME('%Y', \"r0\".\"XCL_069\") = '2010'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:626"
  ]
}
```

### The value of the 'XCL_055' column from the 'users' table. This represents a specific user attribute (likely a user ID or name) for users who have been

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'Organizer'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_055\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_055\" AS \"value\" FROM users AS \"r0\" INNER JOIN badges AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_002\" WHERE \"r1\".\"XCL_003\" = 'Organizer'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:638"
  ]
}
```

### "posts"."XCL_026" = 183

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_026\" = 183",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_055\", T2.\"XCL_058\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T1.\"XCL_026\" = 183 ORDER BY T1.\"XCL_041\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:689"
  ]
}
```

### The unique identifier (XCL_055) for users who have authored posts tagged with 'hypothesis-testing'. Returns one row per matching user-post association

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_055\", T3.\"XCL_058\" FROM tags AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_050\" = T2.\"XCL_026\" INNER JOIN users AS T3 ON T3.\"XCL_052\" = T2.\"XCL_033\" WHERE T1.\"XCL_048\" = 'hypothesis-testing'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_055\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "tags"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      },
      {
        "role": "r2",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_055\" AS \"value\" FROM tags AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_050\" = \"r1\".\"XCL_026\" INNER JOIN users AS \"r2\" ON \"r2\".\"XCL_052\" = \"r1\".\"XCL_033\" WHERE \"r0\".\"XCL_048\" = 'hypothesis-testing'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:654"
  ]
}
```

### Aggregates the total number of vote records (count of XCL_066) for a specific entity (XCL_070 = 58) on a specific date (XCL_069 = '2010-07-19').

```json
{
  "kind": "metric",
  "formula": "COUNT(\"votes\".\"XCL_066\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_066\") FROM votes WHERE \"XCL_070\" = 58 AND \"XCL_069\" = '2010-07-19'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_066\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "votes"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_066\") AS \"value\" FROM votes AS \"r0\" WHERE \"r0\".\"XCL_070\" = 58 AND \"r0\".\"XCL_069\" = '2010-07-19'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:558"
  ]
}
```

### User Attribute XCL_055

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_055\", T1.\"XCL_057\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T2.\"XCL_039\" > 150",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_055\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_055\" AS \"value\" FROM users AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_033\" WHERE \"r1\".\"XCL_039\" > 150",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:648"
  ]
}
```

### Badges Group Key

```json
{
  "kind": "binding",
  "formula": "\"badges\".\"XCL_002\"",
  "grain": [
    "\"badges\".\"XCL_002\""
  ],
  "population_scope": "SELECT \"XCL_002\", COUNT(\"XCL_003\") AS num FROM badges GROUP BY \"XCL_002\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_002\"",
    "grain": [
      "\"r0\".\"XCL_002\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_002\" AS \"grain_0\", \"r0\".\"XCL_002\" AS \"value\" FROM badges AS \"r0\" GROUP BY \"r0\".\"XCL_002\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:592"
  ]
}
```

### Aggregates the total number of non-null values in column XCL_052 from the users table, restricted to rows where XCL_064 is between 19 and 65 inclusive

```json
{
  "kind": "metric",
  "formula": "COUNT(\"users\".\"XCL_052\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_052\") FROM users WHERE \"XCL_064\" BETWEEN 19 AND 65",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_052\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_052\") AS \"value\" FROM users AS \"r0\" WHERE \"r0\".\"XCL_064\" BETWEEN 19 AND 65",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:627"
  ]
}
```

### Aggregates the total number of comment records (identified by XCL_005) that belong to posts by a specific user and meet a numeric threshold on XCL_007

```json
{
  "kind": "metric",
  "formula": "COUNT(\"comments\".\"XCL_005\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T3.\"XCL_005\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" INNER JOIN comments AS T3 ON T2.\"XCL_026\" = T3.\"XCL_006\" WHERE T1.\"XCL_055\" = 'Neil McGuigan' AND T3.\"XCL_007\" < 60",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r2\".\"XCL_005\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      },
      {
        "role": "r2",
        "physical_table": "comments"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r2\".\"XCL_005\") AS \"value\" FROM users AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_033\" INNER JOIN comments AS \"r2\" ON \"r1\".\"XCL_026\" = \"r2\".\"XCL_006\" WHERE \"r0\".\"XCL_055\" = 'Neil McGuigan' AND \"r2\".\"XCL_007\" < 60",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:636"
  ]
}
```

### Aggregated count of rows in the 'comments' table where 'XCL_010' equals 13 and 'XCL_007' is less than 60. Returns a single scalar value representing t

```json
{
  "kind": "metric",
  "formula": "COUNT(\"comments\".\"XCL_005\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_005\") FROM comments WHERE \"XCL_010\" = 13 AND \"XCL_007\" < 60",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_005\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_005\") AS \"value\" FROM comments AS \"r0\" WHERE \"r0\".\"XCL_010\" = 13 AND \"r0\".\"XCL_007\" < 60",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:645"
  ]
}
```

### Comment Identifier

```json
{
  "kind": "binding",
  "formula": "\"comments\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_008\" FROM comments WHERE \"XCL_009\" = '2010-07-19 19:16:14.0'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_008\" AS \"value\" FROM comments AS \"r0\" WHERE \"r0\".\"XCL_009\" = '2010-07-19 19:16:14.0'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:608"
  ]
}
```

### Returns the value of column XCL_055 from the users table for users who have at least one associated post where the post's XCL_044 field is not null. T

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_055\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE NOT T1.\"XCL_044\" IS NULL",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_055\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_055\" AS \"value\" FROM posts AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_033\" = \"r1\".\"XCL_052\" WHERE NOT \"r0\".\"XCL_044\" IS NULL",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:546"
  ]
}
```

### Aggregates the total number of rows in the 'tags' table where 'XCL_049' is less than or equal to 20 and 'XCL_047' is less than 15. Returns a single sc

```json
{
  "kind": "metric",
  "formula": "COUNT(\"tags\".\"XCL_047\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_047\") FROM tags WHERE \"XCL_049\" <= 20 AND \"XCL_047\" < 15",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_047\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "tags"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_047\") AS \"value\" FROM tags AS \"r0\" WHERE \"r0\".\"XCL_049\" <= 20 AND \"r0\".\"XCL_047\" < 15",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:703"
  ]
}
```

### The attribute (XCL_055) of the user associated with the top-ranked post. It is returned alongside the post identifier to identify the specific user re

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_033\", T1.\"XCL_055\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE STRFTIME('%Y', T1.\"XCL_054\") = '2010' ORDER BY T2.\"XCL_039\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:682"
  ]
}
```

### "users"."XCL_055" = 'DatEpicCoderGuyWhoPrograms'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'DatEpicCoderGuyWhoPrograms'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_055\" = 'DatEpicCoderGuyWhoPrograms'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:570"
  ]
}
```

### "comments"."XCL_010" = 13 AND "comments"."XCL_007" < 60

```json
{
  "kind": "predicate",
  "formula": "\"comments\".\"XCL_010\" = 13 AND \"comments\".\"XCL_007\" < 60",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_005\") FROM comments WHERE \"XCL_010\" = 13 AND \"XCL_007\" < 60",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:645"
  ]
}
```

### "users"."XCL_053" > 2000 AND "users"."XCL_060" > 1000

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_053\" > 2000 AND \"users\".\"XCL_060\" > 1000",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_052\") FROM users WHERE \"XCL_053\" > 2000 AND \"XCL_060\" > 1000",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:675"
  ]
}
```

### "users"."XCL_055" = 'Zolomon'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'Zolomon'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_004\" - T2.\"XCL_054\" FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'Zolomon'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:692"
  ]
}
```

### "comments"."XCL_008" = 'fine, you win :)'

```json
{
  "kind": "predicate",
  "formula": "\"comments\".\"XCL_008\" = 'fine, you win :)'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_053\", T2.\"XCL_061\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_008\" = 'fine, you win :)'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:705"
  ]
}
```

### The value of the column XCL_055 from the users table. In this context, it represents the identifier of the user who holds the 'Autobiographer' badge w

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'Autobiographer' ORDER BY T2.\"XCL_004\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:671"
  ]
}
```

### Aggregates the total number of rows in the 'tags' table where the column 'XCL_048' equals the literal 'careers'. The metric counts the values in colum

```json
{
  "kind": "metric",
  "formula": "COUNT(\"tags\".\"XCL_047\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_047\") FROM tags WHERE \"XCL_048\" = 'careers'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_047\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "tags"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_047\") AS \"value\" FROM tags AS \"r0\" WHERE \"r0\".\"XCL_048\" = 'careers'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:696"
  ]
}
```

### STRFTIME('%Y', "votes"."XCL_069") = '2010'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"votes\".\"XCL_069\") = '2010'",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_066\") FROM votes WHERE STRFTIME('%Y', \"XCL_069\") = '2010'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:626"
  ]
}
```

### The value of the column "XCL_055" from the "users" table, representing a specific user attribute (likely an ID or name) for records where the associat

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_055\" FROM users WHERE \"XCL_057\" = 'http://stackoverflow.com'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_055\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_055\" AS \"value\" FROM users AS \"r0\" WHERE \"r0\".\"XCL_057\" = 'http://stackoverflow.com'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:574"
  ]
}
```

### COUNT(DISTINCT "postHistory"."XCL_013") = 1

```json
{
  "kind": "predicate",
  "formula": "COUNT(DISTINCT \"postHistory\".\"XCL_013\") = 1",
  "grain": [
    "\"postHistory\".\"XCL_017\""
  ],
  "population_scope": "SELECT T2.\"XCL_017\" FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T2.\"XCL_014\" = T3.\"XCL_026\" WHERE T3.\"XCL_031\" >= 1000 GROUP BY T2.\"XCL_017\" HAVING COUNT(DISTINCT T2.\"XCL_013\") = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:595"
  ]
}
```

### Target Post Title

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_035\" FROM postLinks AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_023\" = T2.\"XCL_026\" INNER JOIN posts AS T3 ON T1.\"XCL_024\" = T3.\"XCL_026\" WHERE T2.\"XCL_035\" = 'How to tell if something happened in a data set which monitors a value over time'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "postLinks"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      },
      {
        "role": "r2",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_035\" AS \"value\" FROM postLinks AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_023\" = \"r1\".\"XCL_026\" INNER JOIN posts AS \"r2\" ON \"r0\".\"XCL_024\" = \"r2\".\"XCL_026\" WHERE \"r1\".\"XCL_035\" = 'How to tell if something happened in a data set which monitors a value over time'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:651"
  ]
}
```

### "users"."XCL_055" IN ('Harlan', 'Jarrod Dixon')

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" IN ('Harlan', 'Jarrod Dixon')",
  "grain": [],
  "population_scope": "SELECT MAX(\"XCL_053\") FROM users WHERE \"XCL_055\" IN ('Harlan', 'Jarrod Dixon')",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:531"
  ]
}
```

### The value of column XCL_055 from the users table. In this context, it represents the identifier for users named 'Harlan' or 'Jarrod Dixon' who have th

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_055\" FROM users WHERE \"XCL_055\" IN ('Harlan', 'Jarrod Dixon') AND \"XCL_053\" = (SELECT MAX(\"XCL_053\") FROM users WHERE \"XCL_055\" IN ('Harlan', 'Jarrod Dixon'))",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:531"
  ]
}
```

### The value of the column "XCL_055" from the users table. This represents a specific user attribute (likely a user ID or name) for users who have author

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_052\" = T2.\"XCL_010\" WHERE T2.\"XCL_008\" = 'thank you user93!'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_055\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "comments"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_055\" AS \"value\" FROM users AS \"r0\" INNER JOIN comments AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_010\" WHERE \"r1\".\"XCL_008\" = 'thank you user93!'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:576"
  ]
}
```

### "posts"."XCL_030" > 5

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_030\" > 5",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(T2.\"XCL_064\" > 65, 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T1.\"XCL_030\" > 5",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:557"
  ]
}
```

### Average XCL_030 for Stephen Turner's posts

```json
{
  "kind": "metric",
  "formula": "AVG(\"posts\".\"XCL_030\")",
  "grain": [],
  "population_scope": "SELECT AVG(T2.\"XCL_030\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T1.\"XCL_055\" = 'Stephen Turner'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "AVG(\"r1\".\"XCL_030\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT AVG(\"r1\".\"XCL_030\") AS \"value\" FROM users AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_033\" WHERE \"r0\".\"XCL_055\" = 'Stephen Turner'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:680"
  ]
}
```

### Returns the value of "XCL_055" from the "users" table for the row where "XCL_052" equals the latest non-null post identifier ("XCL_033") derived from 

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_055\" FROM users WHERE \"XCL_052\" = (SELECT \"XCL_033\" FROM posts WHERE NOT \"XCL_043\" IS NULL ORDER BY \"XCL_030\" DESC LIMIT 1)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:656"
  ]
}
```

### "posts"."XCL_035" LIKE '%data visualization%'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_035\" LIKE '%data visualization%'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN votes AS T2 ON T1.\"XCL_026\" = T2.\"XCL_067\" WHERE T1.\"XCL_035\" LIKE '%data visualization%'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:569"
  ]
}
```

### User Attribute XCL_055

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_055\", T2.\"XCL_058\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T1.\"XCL_026\" = 183 ORDER BY T1.\"XCL_041\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:689"
  ]
}
```

### The value of column XCL_052 from the users table for the record(s) where XCL_064 equals the minimum XCL_064 in the table. Returns the identifier assoc

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_052\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_052\" FROM users WHERE \"XCL_064\" = (SELECT MIN(\"XCL_064\") FROM users)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:663"
  ]
}
```

### "tags"."XCL_048" = 'sample'

```json
{
  "kind": "predicate",
  "formula": "\"tags\".\"XCL_048\" = 'sample'",
  "grain": [],
  "population_scope": "SELECT \"XCL_050\", \"XCL_051\" FROM tags WHERE \"XCL_048\" = 'sample'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:704"
  ]
}
```

### "tags"."XCL_049" <= 20 AND "tags"."XCL_047" < 15

```json
{
  "kind": "predicate",
  "formula": "\"tags\".\"XCL_049\" <= 20 AND \"tags\".\"XCL_047\" < 15",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_047\") FROM tags WHERE \"XCL_049\" <= 20 AND \"XCL_047\" < 15",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:703"
  ]
}
```

### Badge Identifier

```json
{
  "kind": "binding",
  "formula": "\"badges\".\"XCL_003\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_055\" = 'Pierre'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_003\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_003\" AS \"value\" FROM users AS \"r0\" INNER JOIN badges AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_002\" WHERE \"r0\".\"XCL_055\" = 'Pierre'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:612"
  ]
}
```

### Post Attribute XCL_037

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_037\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_038\", \"XCL_037\" FROM posts WHERE \"XCL_035\" = 'Clustering 1D data'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_037\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_037\" AS \"value\" FROM posts AS \"r0\" WHERE \"r0\".\"XCL_035\" = 'Clustering 1D data'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:698"
  ]
}
```

### "comments"."XCL_009" = '2010-07-19 19:19:56.0'

```json
{
  "kind": "predicate",
  "formula": "\"comments\".\"XCL_009\" = '2010-07-19 19:19:56.0'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_007\" FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T1.\"XCL_009\" = '2010-07-19 19:19:56.0'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:616"
  ]
}
```

### The value of column XCL_052 from the users table for the row where XCL_060 equals the minimum XCL_060 in the table. Returns the identifier associated 

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_052\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_052\" FROM users WHERE \"XCL_060\" = (SELECT MIN(\"XCL_060\") FROM users)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:590"
  ]
}
```

### The value of column XCL_061 from the users table, filtered to users who have authored a comment with the exact text 'R is also lazy evaluated.' in col

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_061\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_061\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_008\" = 'R is also lazy evaluated.'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_061\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_061\" AS \"value\" FROM comments AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_010\" = \"r1\".\"XCL_052\" WHERE \"r0\".\"XCL_008\" = 'R is also lazy evaluated.'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:713"
  ]
}
```

### "users"."XCL_055" = 'slashnick'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'slashnick'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_014\" FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T2.\"XCL_014\" = T3.\"XCL_026\" WHERE T1.\"XCL_055\" = 'slashnick' ORDER BY T3.\"XCL_037\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:633"
  ]
}
```

### Aggregates the count of user identifiers (XCL_052) from the users table, restricted to users located in the United Kingdom (XCL_058) who have associat

```json
{
  "kind": "metric",
  "formula": "COUNT(\"users\".\"XCL_052\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T1.\"XCL_058\" = 'United Kingdom' AND T2.\"XCL_039\" >= 4",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_052\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_052\") AS \"value\" FROM users AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_033\" WHERE \"r0\".\"XCL_058\" = 'United Kingdom' AND \"r1\".\"XCL_039\" >= 4",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:672"
  ]
}
```

### Post Identifier XCL_033

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_033\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_033\" FROM posts WHERE \"XCL_039\" = (SELECT MAX(\"XCL_039\") FROM posts)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:660"
  ]
}
```

### Post History Field XCL_019

```json
{
  "kind": "binding",
  "formula": "\"postHistory\".\"XCL_019\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_019\" FROM posts AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_035\" = 'Why square the difference instead of taking the absolute value in standard deviation?'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_019\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "postHistory"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_019\" AS \"value\" FROM posts AS \"r0\" INNER JOIN postHistory AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_014\" WHERE \"r0\".\"XCL_035\" = 'Why square the difference instead of taking the absolute value in standard deviation?'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:584"
  ]
}
```

### Count of posts for each author (XCL_033). Used in a HAVING clause to filter for authors with more than 10 posts.

```json
{
  "kind": "metric",
  "formula": "COUNT(*)",
  "grain": [
    "\"posts\".\"XCL_033\""
  ],
  "population_scope": "SELECT \"XCL_033\", COUNT(*) AS post_count FROM posts GROUP BY \"XCL_033\" HAVING post_count > 10",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(*)",
    "grain": [
      "\"r0\".\"XCL_033\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_033\" AS \"grain_0\", COUNT(*) AS \"value\" FROM posts AS \"r0\" GROUP BY \"r0\".\"XCL_033\" HAVING COUNT(*) > 10",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:604"
  ]
}
```

### The value of the 'XCL_055' column from the 'users' table for the single user with the highest count of associated badge records. The population is res

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [
    "\"users\".\"XCL_055\""
  ],
  "population_scope": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" GROUP BY T1.\"XCL_055\" ORDER BY COUNT(T1.\"XCL_052\") DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:668"
  ]
}
```

### Average badge count per user

```json
{
  "kind": "metric",
  "formula": "CAST(COUNT(\"badges\".\"XCL_001\") AS REAL) / COUNT(DISTINCT \"users\".\"XCL_055\")",
  "grain": [],
  "population_scope": "SELECT CAST(COUNT(T1.\"XCL_001\") AS REAL) / COUNT(DISTINCT T2.\"XCL_055\") FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T2.\"XCL_060\" > 200",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(COUNT(\"r0\".\"XCL_001\") AS REAL) / COUNT(DISTINCT \"r1\".\"XCL_055\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "badges"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT CAST(COUNT(\"r0\".\"XCL_001\") AS REAL) / COUNT(DISTINCT \"r1\".\"XCL_055\") AS \"value\" FROM badges AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_002\" = \"r1\".\"XCL_052\" WHERE \"r1\".\"XCL_060\" > 200",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:556"
  ]
}
```

### "comments"."XCL_008" = 'thank you user93!'

```json
{
  "kind": "predicate",
  "formula": "\"comments\".\"XCL_008\" = 'thank you user93!'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_052\" = T2.\"XCL_010\" WHERE T2.\"XCL_008\" = 'thank you user93!'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:576"
  ]
}
```

### "postLinks"."XCL_023" = 395

```json
{
  "kind": "predicate",
  "formula": "\"postLinks\".\"XCL_023\" = 395",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_030\", T2.\"XCL_025\" FROM posts AS T1 INNER JOIN postLinks AS T2 ON T1.\"XCL_026\" = T2.\"XCL_023\" WHERE T2.\"XCL_023\" = 395",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:601"
  ]
}
```

### Attribute from the users table for users who hold the 'outliers' badge. Grain: one row per user-badge match.

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_058\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_056\", T1.\"XCL_058\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'outliers'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_058\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_058\" AS \"value\" FROM users AS \"r0\" INNER JOIN badges AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_002\" WHERE \"r1\".\"XCL_003\" = 'outliers'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:650"
  ]
}
```

### "posts"."post_count" > 10

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"post_count\" > 10",
  "grain": [
    "\"posts\".\"XCL_033\""
  ],
  "population_scope": "SELECT \"XCL_033\", COUNT(*) AS post_count FROM posts GROUP BY \"XCL_033\" HAVING post_count > 10",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:604"
  ]
}
```

### Post Identifier XCL_038

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_038\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_038\", \"XCL_037\" FROM posts WHERE \"XCL_035\" = 'Clustering 1D data'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_038\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_038\" AS \"value\" FROM posts AS \"r0\" WHERE \"r0\".\"XCL_035\" = 'Clustering 1D data'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:698"
  ]
}
```

### Count of rows in the 'users' table where 'XCL_053' is greater than 2000 and 'XCL_060' is greater than 1000. The grain is a single aggregate value repr

```json
{
  "kind": "metric",
  "formula": "COUNT(\"users\".\"XCL_052\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_052\") FROM users WHERE \"XCL_053\" > 2000 AND \"XCL_060\" > 1000",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_052\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_052\") AS \"value\" FROM users AS \"r0\" WHERE \"r0\".\"XCL_053\" > 2000 AND \"r0\".\"XCL_060\" > 1000",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:675"
  ]
}
```

### "posts"."XCL_035" = 'Clustering 1D data'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_035\" = 'Clustering 1D data'",
  "grain": [],
  "population_scope": "SELECT \"XCL_038\", \"XCL_037\" FROM posts WHERE \"XCL_035\" = 'Clustering 1D data'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:698"
  ]
}
```

### "users"."XCL_058" = 'India' AND "badges"."XCL_003" = 'Teacher'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_058\" = 'India' AND \"badges\".\"XCL_003\" = 'Teacher'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T2.\"XCL_058\" = 'India' AND T1.\"XCL_003\" = 'Teacher'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:597"
  ]
}
```

### "tags"."XCL_048" = 'hypothesis-testing'

```json
{
  "kind": "predicate",
  "formula": "\"tags\".\"XCL_048\" = 'hypothesis-testing'",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_055\", T3.\"XCL_058\" FROM tags AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_050\" = T2.\"XCL_026\" INNER JOIN users AS T3 ON T3.\"XCL_052\" = T2.\"XCL_033\" WHERE T1.\"XCL_048\" = 'hypothesis-testing'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:654"
  ]
}
```

### "posts"."XCL_035" = 'Detecting a given face in a database of facial images'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_035\" = 'Detecting a given face in a database of facial images'",
  "grain": [],
  "population_scope": "SELECT \"XCL_041\", \"XCL_040\" FROM posts WHERE \"XCL_035\" = 'Detecting a given face in a database of facial images'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:644"
  ]
}
```

### "postHistory"."XCL_017" = 686 AND STRFTIME('%Y', "postHistory"."XCL_016") = '2011'

```json
{
  "kind": "predicate",
  "formula": "\"postHistory\".\"XCL_017\" = 686 AND STRFTIME('%Y', \"postHistory\".\"XCL_016\") = '2011'",
  "grain": [],
  "population_scope": "SELECT \"XCL_014\" FROM postHistory WHERE \"XCL_017\" = 686 AND STRFTIME('%Y', \"XCL_016\") = '2011'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:603"
  ]
}
```

### Post Identifier XCL_041

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_041\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_041\", \"XCL_040\" FROM posts WHERE \"XCL_035\" = 'Detecting a given face in a database of facial images'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_041\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_041\" AS \"value\" FROM posts AS \"r0\" WHERE \"r0\".\"XCL_035\" = 'Detecting a given face in a database of facial images'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:644"
  ]
}
```

### Count of posts

```json
{
  "kind": "metric",
  "formula": "COUNT(\"posts\".\"XCL_026\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T1.\"XCL_030\" >= 20 AND T2.\"XCL_064\" > 65",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_026\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_026\") AS \"value\" FROM posts AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_033\" = \"r1\".\"XCL_052\" WHERE \"r0\".\"XCL_030\" >= 20 AND \"r1\".\"XCL_064\" > 65",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:547"
  ]
}
```

### Aggregates the total number of non-null values in the XCL_005 column from the comments table, restricted to rows where XCL_007 is greater than 60.

```json
{
  "kind": "metric",
  "formula": "COUNT(\"comments\".\"XCL_005\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_005\") FROM comments WHERE \"XCL_007\" > 60",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_005\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_005\") AS \"value\" FROM comments AS \"r0\" WHERE \"r0\".\"XCL_007\" > 60",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:607"
  ]
}
```

### Max XCL_053

```json
{
  "kind": "metric",
  "formula": "MAX(\"users\".\"XCL_053\")",
  "grain": [],
  "population_scope": "SELECT MAX(\"XCL_053\") FROM users",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MAX(\"r0\".\"XCL_053\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT MAX(\"r0\".\"XCL_053\") AS \"value\" FROM users AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:674",
    "bird_dev:661",
    "bird_dev:589",
    "bird_dev:701"
  ]
}
```

### Identifier from the posts table (XCL_033) used to group posts and join to users. Represents the author or owner of a post.

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_033\"",
  "grain": [
    "\"posts\".\"XCL_033\""
  ],
  "population_scope": "SELECT \"XCL_033\", COUNT(*) AS post_count FROM posts GROUP BY \"XCL_033\" HAVING post_count > 10",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_033\"",
    "grain": [
      "\"r0\".\"XCL_033\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_033\" AS \"grain_0\", \"r0\".\"XCL_033\" AS \"value\" FROM posts AS \"r0\" GROUP BY \"r0\".\"XCL_033\" HAVING COUNT(*) > 10",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:604"
  ]
}
```

### Counts the number of distinct values in the 'XCL_010' column from the 'comments' table where 'XCL_006' equals 3720. This scalar subquery returns a sin

```json
{
  "kind": "metric",
  "formula": "COUNT(DISTINCT \"comments\".\"XCL_010\")",
  "grain": [],
  "population_scope": "SELECT COUNT(DISTINCT \"XCL_010\") FROM comments WHERE \"XCL_006\" = 3720",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(DISTINCT \"r0\".\"XCL_010\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      }
    ],
    "scope_sql": "SELECT COUNT(DISTINCT \"r0\".\"XCL_010\") AS \"value\" FROM comments AS \"r0\" WHERE \"r0\".\"XCL_006\" = 3720",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:599"
  ]
}
```

### The identifier (XCL_055) of the user who cast a vote of value 50 on a post containing 'variance' in its title (XCL_035). Grain: one row per matching u

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_055\", T1.\"XCL_035\" FROM posts AS T1 INNER JOIN votes AS T2 ON T1.\"XCL_026\" = T2.\"XCL_067\" INNER JOIN users AS T3 ON T3.\"XCL_052\" = T2.\"XCL_070\" WHERE T2.\"XCL_071\" = 50 AND T1.\"XCL_035\" LIKE '%variance%'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_055\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "votes"
      },
      {
        "role": "r2",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_055\" AS \"value\" FROM posts AS \"r0\" INNER JOIN votes AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_067\" INNER JOIN users AS \"r2\" ON \"r2\".\"XCL_052\" = \"r1\".\"XCL_070\" WHERE \"r1\".\"XCL_071\" = 50 AND \"r0\".\"XCL_035\" LIKE '%variance%'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:586"
  ]
}
```

### "postHistory"."XCL_020" = 'Samuel' AND STRFTIME('%Y', "postHistory"."XCL_016") = '2013' AND STRFTIME('%Y', "badges"."XCL_004") = '2013'

```json
{
  "kind": "predicate",
  "formula": "\"postHistory\".\"XCL_020\" = 'Samuel' AND STRFTIME('%Y', \"postHistory\".\"XCL_016\") = '2013' AND STRFTIME('%Y', \"badges\".\"XCL_004\") = '2013'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_014\", T2.\"XCL_003\" FROM postHistory AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE T1.\"XCL_020\" = 'Samuel' AND STRFTIME('%Y', T1.\"XCL_016\") = '2013' AND STRFTIME('%Y', T2.\"XCL_004\") = '2013'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:652"
  ]
}
```

### "users"."XCL_055" = 'Neil McGuigan' AND "comments"."XCL_007" < 60

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'Neil McGuigan' AND \"comments\".\"XCL_007\" < 60",
  "grain": [],
  "population_scope": "SELECT COUNT(T3.\"XCL_005\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" INNER JOIN comments AS T3 ON T2.\"XCL_026\" = T3.\"XCL_006\" WHERE T1.\"XCL_055\" = 'Neil McGuigan' AND T3.\"XCL_007\" < 60",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:636"
  ]
}
```

### The value of the 'XCL_055' column from the 'users' table. This represents a specific user attribute (likely a user ID or name) for users who have earn

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_055\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T2.\"XCL_003\" = 'Necromancer' LIMIT 10",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:580"
  ]
}
```

### "posts"."XCL_026" = 65041

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_026\" = 65041",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_053\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T2.\"XCL_026\" = 65041",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:566"
  ]
}
```

### Latest Comment Identifier

```json
{
  "kind": "binding",
  "formula": "\"comments\".\"XCL_006\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_006\" FROM comments ORDER BY \"XCL_007\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:561"
  ]
}
```

### "votes"."XCL_071" >= 30

```json
{
  "kind": "predicate",
  "formula": "\"votes\".\"XCL_071\" >= 30",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_066\") FROM votes WHERE \"XCL_071\" >= 30",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:700"
  ]
}
```

### Minimum XCL_064 Value

```json
{
  "kind": "metric",
  "formula": "MIN(\"users\".\"XCL_064\")",
  "grain": [],
  "population_scope": "SELECT MIN(\"XCL_064\") FROM users",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MIN(\"r0\".\"XCL_064\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT MIN(\"r0\".\"XCL_064\") AS \"value\" FROM users AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:663"
  ]
}
```

### "posts"."XCL_031" = 1910

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_031\" = 1910",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN comments AS T2 ON T1.\"XCL_026\" = T2.\"XCL_006\" WHERE T1.\"XCL_031\" = 1910",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:562"
  ]
}
```

### "comments"."XCL_007" = 17

```json
{
  "kind": "predicate",
  "formula": "\"comments\".\"XCL_007\" = 17",
  "grain": [],
  "population_scope": "SELECT \"XCL_008\" FROM comments WHERE \"XCL_007\" = 17",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:573"
  ]
}
```

### STRFTIME('%Y', "badges"."XCL_004") = '2011' AND "users"."XCL_058" = 'North Pole'

```json
{
  "kind": "predicate",
  "formula": "STRFTIME('%Y', \"badges\".\"XCL_004\") = '2011' AND \"users\".\"XCL_058\" = 'North Pole'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE STRFTIME('%Y', T2.\"XCL_004\") = '2011' AND T1.\"XCL_058\" = 'North Pole'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:647"
  ]
}
```

### "users"."XCL_055" = 'csgillespie'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'csgillespie'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_003\" FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:552"
  ]
}
```

### "users"."XCL_055" = 'Sharpie'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'Sharpie'",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_003\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_055\" = 'Sharpie'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:622"
  ]
}
```

### "users"."XCL_064" > 65 AND "badges"."XCL_003" = 'Supporter'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_064\" > 65 AND \"badges\".\"XCL_003\" = 'Supporter'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_064\" > 65 AND T2.\"XCL_003\" = 'Supporter'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:623"
  ]
}
```

### A grouping dimension from the 'comments' table. It defines the second level of the aggregation grain, representing a specific comment attribute or ide

```json
{
  "kind": "binding",
  "formula": "\"comments\".\"XCL_008\"",
  "grain": [
    "\"posts\".\"XCL_035\"",
    "\"comments\".\"XCL_008\""
  ],
  "population_scope": "SELECT AVG(T2.\"XCL_031\"), T2.\"XCL_035\", T1.\"XCL_008\" FROM comments AS T1 INNER JOIN posts AS T2 ON T2.\"XCL_026\" = T1.\"XCL_006\" WHERE T2.\"XCL_036\" = '<humor>' GROUP BY T2.\"XCL_035\", T1.\"XCL_008\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_008\"",
    "grain": [
      "\"r1\".\"XCL_035\"",
      "\"r0\".\"XCL_008\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_035\" AS \"grain_0\", \"r0\".\"XCL_008\" AS \"grain_1\", \"r0\".\"XCL_008\" AS \"value\" FROM comments AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r1\".\"XCL_026\" = \"r0\".\"XCL_006\" WHERE \"r1\".\"XCL_036\" = '<humor>' GROUP BY \"r1\".\"XCL_035\", \"r0\".\"XCL_008\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:587"
  ]
}
```

### Maximum XCL_039 Value

```json
{
  "kind": "metric",
  "formula": "MAX(\"posts\".\"XCL_039\")",
  "grain": [],
  "population_scope": "SELECT MAX(\"XCL_039\") FROM posts",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "MAX(\"r0\".\"XCL_039\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT MAX(\"r0\".\"XCL_039\") AS \"value\" FROM posts AS \"r0\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:660"
  ]
}
```

### The value of the 'XCL_064' column from the 'users' table. This represents a specific user attribute (likely a unique ID or name) for users located in 

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_064\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_064\" FROM users AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_052\" = T2.\"XCL_002\" WHERE T1.\"XCL_058\" = 'Vienna, Austria'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_064\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_064\" AS \"value\" FROM users AS \"r0\" INNER JOIN badges AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_002\" WHERE \"r0\".\"XCL_058\" = 'Vienna, Austria'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:618"
  ]
}
```

### Aggregates the total number of non-null values in the XCL_047 column from the tags table, restricted to rows where XCL_049 is between 5000 and 7000.

```json
{
  "kind": "metric",
  "formula": "COUNT(\"tags\".\"XCL_047\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_047\") FROM tags WHERE \"XCL_049\" BETWEEN 5000 AND 7000",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_047\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "tags"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_047\") AS \"value\" FROM tags AS \"r0\" WHERE \"r0\".\"XCL_049\" BETWEEN 5000 AND 7000",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:659"
  ]
}
```

### Source Post Title

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_035\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_035\", T2.\"XCL_025\" FROM posts AS T1 INNER JOIN postLinks AS T2 ON T1.\"XCL_026\" = T2.\"XCL_023\" INNER JOIN posts AS T3 ON T2.\"XCL_024\" = T3.\"XCL_026\" WHERE T1.\"XCL_035\" = 'What are principal component scores?'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_035\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "postLinks"
      },
      {
        "role": "r2",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_035\" AS \"value\" FROM posts AS \"r0\" INNER JOIN postLinks AS \"r1\" ON \"r0\".\"XCL_026\" = \"r1\".\"XCL_023\" INNER JOIN posts AS \"r2\" ON \"r1\".\"XCL_024\" = \"r2\".\"XCL_026\" WHERE \"r0\".\"XCL_035\" = 'What are principal component scores?'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:655"
  ]
}
```

### Comment Identifier

```json
{
  "kind": "binding",
  "formula": "\"comments\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_008\" FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T2.\"XCL_035\" = 'How does gentle boosting differ from AdaBoost?'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_008\" AS \"value\" FROM comments AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_006\" = \"r1\".\"XCL_026\" WHERE \"r1\".\"XCL_035\" = 'How does gentle boosting differ from AdaBoost?'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:579"
  ]
}
```

### Post Identifier XCL_040

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_040\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_041\", \"XCL_040\" FROM posts WHERE \"XCL_035\" = 'Detecting a given face in a database of facial images'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_040\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_040\" AS \"value\" FROM posts AS \"r0\" WHERE \"r0\".\"XCL_035\" = 'Detecting a given face in a database of facial images'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:644"
  ]
}
```

### Calculates the percentage of post records (identified by XCL_026) associated with users where the user attribute XCL_064 is greater than 65, among pos

```json
{
  "kind": "metric",
  "formula": "CAST(SUM(IIF(\"users\".\"XCL_064\" > 65, 1, 0)) AS REAL) * 100 / COUNT(\"posts\".\"XCL_026\")",
  "grain": [],
  "population_scope": "SELECT CAST(SUM(IIF(T2.\"XCL_064\" > 65, 1, 0)) AS REAL) * 100 / COUNT(T1.\"XCL_026\") FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T1.\"XCL_030\" > 5",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "CAST(SUM(IIF(\"r1\".\"XCL_064\" > 65, 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_026\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT CAST(SUM(IIF(\"r1\".\"XCL_064\" > 65, 1, 0)) AS REAL) * 100 / COUNT(\"r0\".\"XCL_026\") AS \"value\" FROM posts AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_033\" = \"r1\".\"XCL_052\" WHERE \"r0\".\"XCL_030\" > 5",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:557"
  ]
}
```

### Aggregates the count of post identifiers (XCL_026) from the posts table. The population is restricted to posts that have at least one associated comme

```json
{
  "kind": "metric",
  "formula": "COUNT(\"posts\".\"XCL_026\")",
  "grain": [],
  "population_scope": "SELECT COUNT(T2.\"XCL_026\") FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" INNER JOIN comments AS T3 ON T3.\"XCL_006\" = T2.\"XCL_026\" ORDER BY T1.\"XCL_054\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:693"
  ]
}
```

### "comments"."XCL_007" BETWEEN 1 AND 5 AND "users"."XCL_062" = 0

```json
{
  "kind": "predicate",
  "formula": "\"comments\".\"XCL_007\" BETWEEN 1 AND 5 AND \"users\".\"XCL_062\" = 0",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_055\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_007\" BETWEEN 1 AND 5 AND T2.\"XCL_062\" = 0",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:715"
  ]
}
```

### A grouping dimension from the 'posts' table. It defines one level of the aggregation grain, representing a specific post attribute or category associa

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_035\"",
  "grain": [
    "\"posts\".\"XCL_035\"",
    "\"comments\".\"XCL_008\""
  ],
  "population_scope": "SELECT AVG(T2.\"XCL_031\"), T2.\"XCL_035\", T1.\"XCL_008\" FROM comments AS T1 INNER JOIN posts AS T2 ON T2.\"XCL_026\" = T1.\"XCL_006\" WHERE T2.\"XCL_036\" = '<humor>' GROUP BY T2.\"XCL_035\", T1.\"XCL_008\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_035\"",
    "grain": [
      "\"r1\".\"XCL_035\"",
      "\"r0\".\"XCL_008\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_035\" AS \"grain_0\", \"r0\".\"XCL_008\" AS \"grain_1\", \"r1\".\"XCL_035\" AS \"value\" FROM comments AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r1\".\"XCL_026\" = \"r0\".\"XCL_006\" WHERE \"r1\".\"XCL_036\" = '<humor>' GROUP BY \"r1\".\"XCL_035\", \"r0\".\"XCL_008\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:587"
  ]
}
```

### Post History Identifier

```json
{
  "kind": "binding",
  "formula": "\"postHistory\".\"XCL_014\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_014\", T2.\"XCL_003\" FROM postHistory AS T1 INNER JOIN badges AS T2 ON T1.\"XCL_017\" = T2.\"XCL_002\" WHERE T1.\"XCL_020\" = 'Samuel' AND STRFTIME('%Y', T1.\"XCL_016\") = '2013' AND STRFTIME('%Y', T2.\"XCL_004\") = '2013'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_014\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "postHistory"
      },
      {
        "role": "r1",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_014\" AS \"value\" FROM postHistory AS \"r0\" INNER JOIN badges AS \"r1\" ON \"r0\".\"XCL_017\" = \"r1\".\"XCL_002\" WHERE \"r0\".\"XCL_020\" = 'Samuel' AND STRFTIME('%Y', \"r0\".\"XCL_016\") = '2013' AND STRFTIME('%Y', \"r1\".\"XCL_004\") = '2013'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:652"
  ]
}
```

### "comments"."XCL_006" = 1

```json
{
  "kind": "predicate",
  "formula": "\"comments\".\"XCL_006\" = 1",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_052\", T2.\"XCL_053\" FROM comments AS T1 INNER JOIN users AS T2 ON T1.\"XCL_010\" = T2.\"XCL_052\" WHERE T1.\"XCL_006\" = 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:594"
  ]
}
```

### Comment Identifier

```json
{
  "kind": "binding",
  "formula": "\"comments\".\"XCL_008\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_008\" FROM comments AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_006\" = T2.\"XCL_026\" WHERE T1.\"XCL_009\" = '2010-07-19 19:37:33.0'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_008\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "comments"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_008\" AS \"value\" FROM comments AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_006\" = \"r1\".\"XCL_026\" WHERE \"r0\".\"XCL_009\" = '2010-07-19 19:37:33.0'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:617"
  ]
}
```

### The value of the 'XCL_055' column from the 'users' table. It represents a user attribute, likely a unique identifier or name, for users who have autho

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_055\", T1.\"XCL_053\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T2.\"XCL_035\" = 'Understanding what Dassault iSight is doing?'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r0\".\"XCL_055\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r0\".\"XCL_055\" AS \"value\" FROM users AS \"r0\" INNER JOIN posts AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_033\" WHERE \"r1\".\"XCL_035\" = 'Understanding what Dassault iSight is doing?'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:578"
  ]
}
```

### The 'XCL_057' attribute from the 'users' table, serving as the grouping dimension. The population is restricted to users where 'XCL_055' equals 'Yevge

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_057\"",
  "grain": [
    "\"users\".\"XCL_057\""
  ],
  "population_scope": "SELECT SUM(T1.\"XCL_030\"), T2.\"XCL_057\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_040\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'Yevgeny' GROUP BY T2.\"XCL_057\"",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r1\".\"XCL_057\"",
    "grain": [
      "\"r1\".\"XCL_057\""
    ],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "posts"
      },
      {
        "role": "r1",
        "physical_table": "users"
      }
    ],
    "scope_sql": "SELECT \"r1\".\"XCL_057\" AS \"grain_0\", \"r1\".\"XCL_057\" AS \"value\" FROM posts AS \"r0\" INNER JOIN users AS \"r1\" ON \"r0\".\"XCL_040\" = \"r1\".\"XCL_052\" WHERE \"r1\".\"XCL_055\" = 'Yevgeny' GROUP BY \"r1\".\"XCL_057\"",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:583"
  ]
}
```

### "users"."XCL_055" = 'Harlan'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'Harlan'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_052\") FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN votes AS T3 ON T3.\"XCL_067\" = T2.\"XCL_014\" WHERE T1.\"XCL_055\" = 'Harlan'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:632"
  ]
}
```

### "posts"."XCL_039" > 150

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_039\" > 150",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_055\", T1.\"XCL_057\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T2.\"XCL_039\" > 150",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:648"
  ]
}
```

### "users"."XCL_055" = 'csgillespie'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'csgillespie'",
  "grain": [],
  "population_scope": "SELECT COUNT(T1.\"XCL_001\") FROM badges AS T1 INNER JOIN users AS T2 ON T1.\"XCL_002\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:551"
  ]
}
```

### "posts"."XCL_035" = 'Understanding what Dassault iSight is doing?'

```json
{
  "kind": "predicate",
  "formula": "\"posts\".\"XCL_035\" = 'Understanding what Dassault iSight is doing?'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_055\", T1.\"XCL_053\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE T2.\"XCL_035\" = 'Understanding what Dassault iSight is doing?'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:578"
  ]
}
```

### Aggregates the total number of badge records where the badge name is 'Commentator' and the year of the date field is 2014. The grain is a single scala

```json
{
  "kind": "metric",
  "formula": "COUNT(\"badges\".\"XCL_001\")",
  "grain": [],
  "population_scope": "SELECT COUNT(\"XCL_001\") FROM badges WHERE \"XCL_003\" = 'Commentator' AND STRFTIME('%Y', \"XCL_004\") = '2014'",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "COUNT(\"r0\".\"XCL_001\")",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "badges"
      }
    ],
    "scope_sql": "SELECT COUNT(\"r0\".\"XCL_001\") AS \"value\" FROM badges AS \"r0\" WHERE \"r0\".\"XCL_003\" = 'Commentator' AND STRFTIME('%Y', \"r0\".\"XCL_004\") = '2014'",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:641"
  ]
}
```

### Post Identifier

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_036\"",
  "grain": [],
  "population_scope": "SELECT T3.\"XCL_036\" FROM users AS T1 INNER JOIN postHistory AS T2 ON T1.\"XCL_052\" = T2.\"XCL_017\" INNER JOIN posts AS T3 ON T3.\"XCL_026\" = T2.\"XCL_014\" WHERE T1.\"XCL_055\" = 'Mark Meckes' AND T3.\"XCL_038\" = 0",
  "upstream_scopes": [],
  "execution_contract": {
    "formula": "\"r2\".\"XCL_036\"",
    "grain": [],
    "role_bindings": [
      {
        "role": "r0",
        "physical_table": "users"
      },
      {
        "role": "r1",
        "physical_table": "postHistory"
      },
      {
        "role": "r2",
        "physical_table": "posts"
      }
    ],
    "scope_sql": "SELECT \"r2\".\"XCL_036\" AS \"value\" FROM users AS \"r0\" INNER JOIN postHistory AS \"r1\" ON \"r0\".\"XCL_052\" = \"r1\".\"XCL_017\" INNER JOIN posts AS \"r2\" ON \"r2\".\"XCL_026\" = \"r1\".\"XCL_014\" WHERE \"r0\".\"XCL_055\" = 'Mark Meckes' AND \"r2\".\"XCL_038\" = 0",
    "requires_staged_execution": false
  },
  "source_history_ids": [
    "bird_dev:637"
  ]
}
```

### The value of column XCL_055 for the user record(s) where XCL_060 equals the maximum XCL_060 in the table. Represents the identifier or attribute of th

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_055\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_055\" FROM users WHERE \"XCL_060\" = (SELECT MAX(\"XCL_060\") FROM users)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:534"
  ]
}
```

### Post Identifier

```json
{
  "kind": "binding",
  "formula": "\"posts\".\"XCL_029\"",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_029\" FROM users AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_052\" = T2.\"XCL_033\" WHERE NOT T1.\"XCL_064\" IS NULL ORDER BY T1.\"XCL_064\", T2.\"XCL_029\" LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:670"
  ]
}
```

### "users"."XCL_055" = 'csgillespie'

```json
{
  "kind": "predicate",
  "formula": "\"users\".\"XCL_055\" = 'csgillespie'",
  "grain": [],
  "population_scope": "SELECT T1.\"XCL_035\" FROM posts AS T1 INNER JOIN users AS T2 ON T1.\"XCL_033\" = T2.\"XCL_052\" WHERE T2.\"XCL_055\" = 'csgillespie'",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:538"
  ]
}
```

### "votes"."XCL_070" = 1465

```json
{
  "kind": "predicate",
  "formula": "\"votes\".\"XCL_070\" = 1465",
  "grain": [],
  "population_scope": "SELECT T2.\"XCL_026\" FROM votes AS T1 INNER JOIN posts AS T2 ON T1.\"XCL_067\" = T2.\"XCL_026\" WHERE T1.\"XCL_070\" = 1465 ORDER BY T2.\"XCL_039\" DESC LIMIT 1",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:666"
  ]
}
```

### Returns the value of "XCL_057" from the "users" table for the user whose "XCL_052" matches the top vote identifier derived from the "votes" table. Thi

```json
{
  "kind": "binding",
  "formula": "\"users\".\"XCL_057\"",
  "grain": [],
  "population_scope": "SELECT \"XCL_055\", \"XCL_057\" FROM users WHERE \"XCL_052\" = (SELECT \"XCL_070\" FROM votes WHERE \"XCL_068\" = 8 ORDER BY \"XCL_071\" DESC LIMIT 1)",
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "bird_dev:657"
  ]
}
```


## 增量维护事件

- Recorded alias revision · postLinks.XCL_023 · Archived superseded_alias_hypotheses → archived aliases
  - postLinks.XCL_023: PostId → Post ID
- Recorded alias revision · users.XCL_060 · Archived superseded_alias_hypotheses → archived aliases
  - users.XCL_060: views_count → views
- Recorded alias revision · users.XCL_061 · Archived superseded_alias_hypotheses → archived aliases
  - users.XCL_061: comments_count → up_votes
