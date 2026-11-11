# Spider2-Lite / BowlingLeague — Schema 与业务口径解释

该数据库的存档目录包含 11 张表、54 个物理列、0 条关系，以及 11 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## Bowler_Scores

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: bs, bs2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Bowler_Scores.MatchID | 保留物理名称；存档没有恢复别名 | INT | schema / Bowler_Scores |
| Bowler_Scores.GameNumber | 保留物理名称；存档没有恢复别名 | smallint | schema / Bowler_Scores |
| Bowler_Scores.BowlerID | 保留物理名称；存档没有恢复别名 | INT | schema / Bowler_Scores |
| Bowler_Scores.RawScore | 保留物理名称；存档没有恢复别名 | smallint | schema / Bowler_Scores |
| Bowler_Scores.HandiCapScore | 保留物理名称；存档没有恢复别名 | smallint | schema / Bowler_Scores |
| Bowler_Scores.WonGame | 保留物理名称；存档没有恢复别名 | BOOLEAN | schema / Bowler_Scores |

## Bowler_Scores_Archive

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Bowler_Scores_Archive.MatchID | 保留物理名称；存档没有恢复别名 | INT | schema / Bowler_Scores_Archive |
| Bowler_Scores_Archive.GameNumber | 保留物理名称；存档没有恢复别名 | smallint | schema / Bowler_Scores_Archive |
| Bowler_Scores_Archive.BowlerID | 保留物理名称；存档没有恢复别名 | INT | schema / Bowler_Scores_Archive |
| Bowler_Scores_Archive.RawScore | 保留物理名称；存档没有恢复别名 | smallint | schema / Bowler_Scores_Archive |
| Bowler_Scores_Archive.HandiCapScore | 保留物理名称；存档没有恢复别名 | smallint | schema / Bowler_Scores_Archive |
| Bowler_Scores_Archive.WonGame | 保留物理名称；存档没有恢复别名 | BOOLEAN | schema / Bowler_Scores_Archive |

## Bowlers

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: b

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Bowlers.BowlerID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Bowlers |
| Bowlers.BowlerLastName | 保留物理名称；存档没有恢复别名 | TEXT | schema / Bowlers |
| Bowlers.BowlerFirstName | 保留物理名称；存档没有恢复别名 | TEXT | schema / Bowlers |
| Bowlers.BowlerMiddleInit | 保留物理名称；存档没有恢复别名 | TEXT | schema / Bowlers |
| Bowlers.BowlerAddress | 保留物理名称；存档没有恢复别名 | TEXT | schema / Bowlers |
| Bowlers.BowlerCity | 保留物理名称；存档没有恢复别名 | TEXT | schema / Bowlers |
| Bowlers.BowlerState | 保留物理名称；存档没有恢复别名 | TEXT | schema / Bowlers |
| Bowlers.BowlerZip | 保留物理名称；存档没有恢复别名 | TEXT | schema / Bowlers |
| Bowlers.BowlerPhoneNumber | 保留物理名称；存档没有恢复别名 | TEXT | schema / Bowlers |
| Bowlers.TeamID | 保留物理名称；存档没有恢复别名 | INT | schema / Bowlers |
| Bowlers.BowlerTotalPins | 保留物理名称；存档没有恢复别名 | INT | schema / Bowlers |
| Bowlers.BowlerGamesBowled | 保留物理名称；存档没有恢复别名 | INT | schema / Bowlers |
| Bowlers.BowlerCurrentAverage | 保留物理名称；存档没有恢复别名 | smallint | schema / Bowlers |
| Bowlers.BowlerCurrentHcp | 保留物理名称；存档没有恢复别名 | smallint | schema / Bowlers |

## Match_Games

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Match_Games.MatchID | 保留物理名称；存档没有恢复别名 | INT | schema / Match_Games |
| Match_Games.GameNumber | 保留物理名称；存档没有恢复别名 | smallint | schema / Match_Games |
| Match_Games.WinningTeamID | 保留物理名称；存档没有恢复别名 | INT | schema / Match_Games |

## Match_Games_Archive

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Match_Games_Archive.MatchID | 保留物理名称；存档没有恢复别名 | INT | schema / Match_Games_Archive |
| Match_Games_Archive.GameNumber | 保留物理名称；存档没有恢复别名 | smallint | schema / Match_Games_Archive |
| Match_Games_Archive.WinningTeamID | 保留物理名称；存档没有恢复别名 | INT | schema / Match_Games_Archive |

## Teams

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Teams.TeamID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Teams |
| Teams.TeamName | 保留物理名称；存档没有恢复别名 | TEXT | schema / Teams |
| Teams.CaptainID | 保留物理名称；存档没有恢复别名 | INT | schema / Teams |

## Tournaments

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: t, t2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Tournaments.TourneyID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Tournaments |
| Tournaments.TourneyDate | 保留物理名称；存档没有恢复别名 | DATE | schema / Tournaments |
| Tournaments.TourneyLocation | 保留物理名称；存档没有恢复别名 | TEXT | schema / Tournaments |

## Tournaments_Archive

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Tournaments_Archive.TourneyID | 保留物理名称；存档没有恢复别名 | INT | schema / Tournaments_Archive |
| Tournaments_Archive.TourneyDate | 保留物理名称；存档没有恢复别名 | DATE | schema / Tournaments_Archive |
| Tournaments_Archive.TourneyLocation | 保留物理名称；存档没有恢复别名 | TEXT | schema / Tournaments_Archive |

## Tourney_Matches

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: tm, tm2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Tourney_Matches.MatchID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Tourney_Matches |
| Tourney_Matches.TourneyID | 保留物理名称；存档没有恢复别名 | INT | schema / Tourney_Matches |
| Tourney_Matches.Lanes | 保留物理名称；存档没有恢复别名 | TEXT | schema / Tourney_Matches |
| Tourney_Matches.OddLaneTeamID | 保留物理名称；存档没有恢复别名 | INT | schema / Tourney_Matches |
| Tourney_Matches.EvenLaneTeamID | 保留物理名称；存档没有恢复别名 | INT | schema / Tourney_Matches |

## Tourney_Matches_Archive

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Tourney_Matches_Archive.MatchID | 保留物理名称；存档没有恢复别名 | INT | schema / Tourney_Matches_Archive |
| Tourney_Matches_Archive.TourneyID | 保留物理名称；存档没有恢复别名 | INT | schema / Tourney_Matches_Archive |
| Tourney_Matches_Archive.Lanes | 保留物理名称；存档没有恢复别名 | TEXT | schema / Tourney_Matches_Archive |
| Tourney_Matches_Archive.OddLaneTeamID | 保留物理名称；存档没有恢复别名 | INT | schema / Tourney_Matches_Archive |
| Tourney_Matches_Archive.EvenLaneTeamID | 保留物理名称；存档没有恢复别名 | INT | schema / Tourney_Matches_Archive |

## WAZips

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| WAZips.ZIP | 保留物理名称；存档没有恢复别名 | TEXT | schema / WAZips |
| WAZips.City | 保留物理名称；存档没有恢复别名 | TEXT | schema / WAZips |
| WAZips.State | 保留物理名称；存档没有恢复别名 | TEXT | schema / WAZips |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

