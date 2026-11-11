# Spider2-Lite / IPL — Schema 与业务口径解释

该数据库的存档目录包含 8 张表、52 个物理列、0 条关系，以及 8 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## ball_by_ball

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: b, bbb

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ball_by_ball.match_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / ball_by_ball |
| ball_by_ball.over_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / ball_by_ball |
| ball_by_ball.ball_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / ball_by_ball |
| ball_by_ball.innings_no | 保留物理名称；存档没有恢复别名 | INTEGER | schema / ball_by_ball |
| ball_by_ball.team_batting | 保留物理名称；存档没有恢复别名 | INTEGER | schema / ball_by_ball |
| ball_by_ball.team_bowling | 保留物理名称；存档没有恢复别名 | INTEGER | schema / ball_by_ball |
| ball_by_ball.striker_batting_position | 保留物理名称；存档没有恢复别名 | INTEGER | schema / ball_by_ball |
| ball_by_ball.striker | 保留物理名称；存档没有恢复别名 | INTEGER | schema / ball_by_ball |
| ball_by_ball.non_striker | 保留物理名称；存档没有恢复别名 | INTEGER | schema / ball_by_ball |
| ball_by_ball.bowler | 保留物理名称；存档没有恢复别名 | INTEGER | schema / ball_by_ball |

## batsman_scored

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: bs, s

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| batsman_scored.match_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / batsman_scored |
| batsman_scored.over_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / batsman_scored |
| batsman_scored.ball_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / batsman_scored |
| batsman_scored.runs_scored | 保留物理名称；存档没有恢复别名 | INTEGER | schema / batsman_scored |
| batsman_scored.innings_no | 保留物理名称；存档没有恢复别名 | INTEGER | schema / batsman_scored |

## extra_runs

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: er

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| extra_runs.match_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / extra_runs |
| extra_runs.over_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / extra_runs |
| extra_runs.ball_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / extra_runs |
| extra_runs.extra_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / extra_runs |
| extra_runs.extra_runs | 保留物理名称；存档没有恢复别名 | INTEGER | schema / extra_runs |
| extra_runs.innings_no | 保留物理名称；存档没有恢复别名 | INTEGER | schema / extra_runs |

## match

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: m

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| match.match_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / match |
| match.team_1 | 保留物理名称；存档没有恢复别名 | INTEGER | schema / match |
| match.team_2 | 保留物理名称；存档没有恢复别名 | INTEGER | schema / match |
| match.match_date | 保留物理名称；存档没有恢复别名 | DATE | schema / match |
| match.season_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / match |
| match.venue | 保留物理名称；存档没有恢复别名 | TEXT | schema / match |
| match.toss_winner | 保留物理名称；存档没有恢复别名 | INTEGER | schema / match |
| match.toss_decision | 保留物理名称；存档没有恢复别名 | TEXT | schema / match |
| match.win_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / match |
| match.win_margin | 保留物理名称；存档没有恢复别名 | INTEGER | schema / match |
| match.outcome_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / match |
| match.match_winner | 保留物理名称；存档没有恢复别名 | INTEGER | schema / match |
| match.man_of_the_match | 保留物理名称；存档没有恢复别名 | INTEGER | schema / match |

## player

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: p

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| player.player_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / player |
| player.player_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / player |
| player.dob | 保留物理名称；存档没有恢复别名 | DATE | schema / player |
| player.batting_hand | 保留物理名称；存档没有恢复别名 | TEXT | schema / player |
| player.bowling_skill | 保留物理名称；存档没有恢复别名 | TEXT | schema / player |
| player.country_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / player |

## player_match

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: pm

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| player_match.match_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / player_match |
| player_match.player_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / player_match |
| player_match.role | 保留物理名称；存档没有恢复别名 | TEXT | schema / player_match |
| player_match.team_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / player_match |

## team

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| team.team_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.name | 保留物理名称；存档没有恢复别名 | TEXT | schema / team |

## wicket_taken

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: w, wt

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| wicket_taken.match_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / wicket_taken |
| wicket_taken.over_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / wicket_taken |
| wicket_taken.ball_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / wicket_taken |
| wicket_taken.player_out | 保留物理名称；存档没有恢复别名 | INTEGER | schema / wicket_taken |
| wicket_taken.kind_out | 保留物理名称；存档没有恢复别名 | TEXT | schema / wicket_taken |
| wicket_taken.innings_no | 保留物理名称；存档没有恢复别名 | INTEGER | schema / wicket_taken |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

