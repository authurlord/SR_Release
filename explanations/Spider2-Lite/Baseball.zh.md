# Spider2-Lite / Baseball — Schema 与业务口径解释

该数据库的存档目录包含 26 张表、352 个物理列、0 条关系，以及 26 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## all_star

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| all_star.player_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / all_star |
| all_star.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / all_star |
| all_star.game_num | 保留物理名称；存档没有恢复别名 | INTEGER | schema / all_star |
| all_star.game_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / all_star |
| all_star.team_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / all_star |
| all_star.league_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / all_star |
| all_star.gp | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / all_star |
| all_star.starting_pos | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / all_star |

## appearances

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| appearances.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / appearances |
| appearances.team_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / appearances |
| appearances.league_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / appearances |
| appearances.player_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / appearances |
| appearances.g_all | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / appearances |
| appearances.gs | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / appearances |
| appearances.g_batting | 保留物理名称；存档没有恢复别名 | INTEGER | schema / appearances |
| appearances.g_defense | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / appearances |
| appearances.g_p | 保留物理名称；存档没有恢复别名 | INTEGER | schema / appearances |
| appearances.g_c | 保留物理名称；存档没有恢复别名 | INTEGER | schema / appearances |
| appearances.g_1b | 保留物理名称；存档没有恢复别名 | INTEGER | schema / appearances |
| appearances.g_2b | 保留物理名称；存档没有恢复别名 | INTEGER | schema / appearances |
| appearances.g_3b | 保留物理名称；存档没有恢复别名 | INTEGER | schema / appearances |
| appearances.g_ss | 保留物理名称；存档没有恢复别名 | INTEGER | schema / appearances |
| appearances.g_lf | 保留物理名称；存档没有恢复别名 | INTEGER | schema / appearances |
| appearances.g_cf | 保留物理名称；存档没有恢复别名 | INTEGER | schema / appearances |
| appearances.g_rf | 保留物理名称；存档没有恢复别名 | INTEGER | schema / appearances |
| appearances.g_of | 保留物理名称；存档没有恢复别名 | INTEGER | schema / appearances |
| appearances.g_dh | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / appearances |
| appearances.g_ph | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / appearances |
| appearances.g_pr | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / appearances |

## batting

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: b

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| batting.player_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / batting |
| batting.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / batting |
| batting.stint | 保留物理名称；存档没有恢复别名 | INTEGER | schema / batting |
| batting.team_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / batting |
| batting.league_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / batting |
| batting.g | 保留物理名称；存档没有恢复别名 | INTEGER | schema / batting |
| batting.ab | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting |
| batting.r | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting |
| batting.h | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting |
| batting.double | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting |
| batting.triple | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting |
| batting.hr | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting |
| batting.rbi | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting |
| batting.sb | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting |
| batting.cs | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting |
| batting.bb | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting |
| batting.so | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting |
| batting.ibb | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting |
| batting.hbp | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting |
| batting.sh | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting |
| batting.sf | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting |
| batting.g_idp | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting |

## batting_postseason

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| batting_postseason.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / batting_postseason |
| batting_postseason.round | 保留物理名称；存档没有恢复别名 | TEXT | schema / batting_postseason |
| batting_postseason.player_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / batting_postseason |
| batting_postseason.team_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / batting_postseason |
| batting_postseason.league_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / batting_postseason |
| batting_postseason.g | 保留物理名称；存档没有恢复别名 | INTEGER | schema / batting_postseason |
| batting_postseason.ab | 保留物理名称；存档没有恢复别名 | INTEGER | schema / batting_postseason |
| batting_postseason.r | 保留物理名称；存档没有恢复别名 | INTEGER | schema / batting_postseason |
| batting_postseason.h | 保留物理名称；存档没有恢复别名 | INTEGER | schema / batting_postseason |
| batting_postseason.double | 保留物理名称；存档没有恢复别名 | INTEGER | schema / batting_postseason |
| batting_postseason.triple | 保留物理名称；存档没有恢复别名 | INTEGER | schema / batting_postseason |
| batting_postseason.hr | 保留物理名称；存档没有恢复别名 | INTEGER | schema / batting_postseason |
| batting_postseason.rbi | 保留物理名称；存档没有恢复别名 | INTEGER | schema / batting_postseason |
| batting_postseason.sb | 保留物理名称；存档没有恢复别名 | INTEGER | schema / batting_postseason |
| batting_postseason.cs | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting_postseason |
| batting_postseason.bb | 保留物理名称；存档没有恢复别名 | INTEGER | schema / batting_postseason |
| batting_postseason.so | 保留物理名称；存档没有恢复别名 | INTEGER | schema / batting_postseason |
| batting_postseason.ibb | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting_postseason |
| batting_postseason.hbp | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting_postseason |
| batting_postseason.sh | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting_postseason |
| batting_postseason.sf | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting_postseason |
| batting_postseason.g_idp | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / batting_postseason |

## college

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| college.college_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / college |
| college.name_full | 保留物理名称；存档没有恢复别名 | TEXT | schema / college |
| college.city | 保留物理名称；存档没有恢复别名 | TEXT | schema / college |
| college.state | 保留物理名称；存档没有恢复别名 | TEXT | schema / college |
| college.country | 保留物理名称；存档没有恢复别名 | TEXT | schema / college |

## fielding

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| fielding.player_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / fielding |
| fielding.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / fielding |
| fielding.stint | 保留物理名称；存档没有恢复别名 | INTEGER | schema / fielding |
| fielding.team_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / fielding |
| fielding.league_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / fielding |
| fielding.pos | 保留物理名称；存档没有恢复别名 | TEXT | schema / fielding |
| fielding.g | 保留物理名称；存档没有恢复别名 | INTEGER | schema / fielding |
| fielding.gs | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / fielding |
| fielding.inn_outs | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / fielding |
| fielding.po | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / fielding |
| fielding.a | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / fielding |
| fielding.e | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / fielding |
| fielding.dp | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / fielding |
| fielding.pb | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / fielding |
| fielding.wp | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / fielding |
| fielding.sb | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / fielding |
| fielding.cs | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / fielding |
| fielding.zr | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / fielding |

## fielding_outfield

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| fielding_outfield.player_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / fielding_outfield |
| fielding_outfield.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / fielding_outfield |
| fielding_outfield.stint | 保留物理名称；存档没有恢复别名 | INTEGER | schema / fielding_outfield |
| fielding_outfield.glf | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / fielding_outfield |
| fielding_outfield.gcf | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / fielding_outfield |
| fielding_outfield.grf | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / fielding_outfield |

## fielding_postseason

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| fielding_postseason.player_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / fielding_postseason |
| fielding_postseason.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / fielding_postseason |
| fielding_postseason.team_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / fielding_postseason |
| fielding_postseason.league_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / fielding_postseason |
| fielding_postseason.round | 保留物理名称；存档没有恢复别名 | TEXT | schema / fielding_postseason |
| fielding_postseason.pos | 保留物理名称；存档没有恢复别名 | TEXT | schema / fielding_postseason |
| fielding_postseason.g | 保留物理名称；存档没有恢复别名 | INTEGER | schema / fielding_postseason |
| fielding_postseason.gs | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / fielding_postseason |
| fielding_postseason.inn_outs | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / fielding_postseason |
| fielding_postseason.po | 保留物理名称；存档没有恢复别名 | INTEGER | schema / fielding_postseason |
| fielding_postseason.a | 保留物理名称；存档没有恢复别名 | INTEGER | schema / fielding_postseason |
| fielding_postseason.e | 保留物理名称；存档没有恢复别名 | INTEGER | schema / fielding_postseason |
| fielding_postseason.dp | 保留物理名称；存档没有恢复别名 | INTEGER | schema / fielding_postseason |
| fielding_postseason.tp | 保留物理名称；存档没有恢复别名 | INTEGER | schema / fielding_postseason |
| fielding_postseason.pb | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / fielding_postseason |
| fielding_postseason.sb | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / fielding_postseason |
| fielding_postseason.cs | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / fielding_postseason |

## hall_of_fame

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| hall_of_fame.player_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / hall_of_fame |
| hall_of_fame.yearid | 保留物理名称；存档没有恢复别名 | INTEGER | schema / hall_of_fame |
| hall_of_fame.votedby | 保留物理名称；存档没有恢复别名 | TEXT | schema / hall_of_fame |
| hall_of_fame.ballots | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / hall_of_fame |
| hall_of_fame.needed | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / hall_of_fame |
| hall_of_fame.votes | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / hall_of_fame |
| hall_of_fame.inducted | 保留物理名称；存档没有恢复别名 | TEXT | schema / hall_of_fame |
| hall_of_fame.category | 保留物理名称；存档没有恢复别名 | TEXT | schema / hall_of_fame |
| hall_of_fame.needed_note | 保留物理名称；存档没有恢复别名 | TEXT | schema / hall_of_fame |

## home_game

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| home_game.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / home_game |
| home_game.league_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / home_game |
| home_game.team_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / home_game |
| home_game.park_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / home_game |
| home_game.span_first | 保留物理名称；存档没有恢复别名 | TEXT | schema / home_game |
| home_game.span_last | 保留物理名称；存档没有恢复别名 | TEXT | schema / home_game |
| home_game.games | 保留物理名称；存档没有恢复别名 | INTEGER | schema / home_game |
| home_game.openings | 保留物理名称；存档没有恢复别名 | INTEGER | schema / home_game |
| home_game.attendance | 保留物理名称；存档没有恢复别名 | INTEGER | schema / home_game |

## manager

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| manager.player_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / manager |
| manager.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / manager |
| manager.team_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / manager |
| manager.league_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / manager |
| manager.inseason | 保留物理名称；存档没有恢复别名 | INTEGER | schema / manager |
| manager.g | 保留物理名称；存档没有恢复别名 | INTEGER | schema / manager |
| manager.w | 保留物理名称；存档没有恢复别名 | INTEGER | schema / manager |
| manager.l | 保留物理名称；存档没有恢复别名 | INTEGER | schema / manager |
| manager.rank | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / manager |
| manager.plyr_mgr | 保留物理名称；存档没有恢复别名 | TEXT | schema / manager |

## manager_award

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| manager_award.player_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / manager_award |
| manager_award.award_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / manager_award |
| manager_award.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / manager_award |
| manager_award.league_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / manager_award |
| manager_award.tie | 保留物理名称；存档没有恢复别名 | TEXT | schema / manager_award |
| manager_award.notes | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / manager_award |

## manager_award_vote

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| manager_award_vote.award_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / manager_award_vote |
| manager_award_vote.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / manager_award_vote |
| manager_award_vote.league_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / manager_award_vote |
| manager_award_vote.player_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / manager_award_vote |
| manager_award_vote.points_won | 保留物理名称；存档没有恢复别名 | INTEGER | schema / manager_award_vote |
| manager_award_vote.points_max | 保留物理名称；存档没有恢复别名 | INTEGER | schema / manager_award_vote |
| manager_award_vote.votes_first | 保留物理名称；存档没有恢复别名 | INTEGER | schema / manager_award_vote |

## manager_half

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| manager_half.player_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / manager_half |
| manager_half.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / manager_half |
| manager_half.team_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / manager_half |
| manager_half.league_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / manager_half |
| manager_half.inseason | 保留物理名称；存档没有恢复别名 | INTEGER | schema / manager_half |
| manager_half.half | 保留物理名称；存档没有恢复别名 | INTEGER | schema / manager_half |
| manager_half.g | 保留物理名称；存档没有恢复别名 | INTEGER | schema / manager_half |
| manager_half.w | 保留物理名称；存档没有恢复别名 | INTEGER | schema / manager_half |
| manager_half.l | 保留物理名称；存档没有恢复别名 | INTEGER | schema / manager_half |
| manager_half.rank | 保留物理名称；存档没有恢复别名 | INTEGER | schema / manager_half |

## park

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| park.park_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / park |
| park.park_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / park |
| park.park_alias | 保留物理名称；存档没有恢复别名 | TEXT | schema / park |
| park.city | 保留物理名称；存档没有恢复别名 | TEXT | schema / park |
| park.state | 保留物理名称；存档没有恢复别名 | TEXT | schema / park |
| park.country | 保留物理名称；存档没有恢复别名 | TEXT | schema / park |

## pitching

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| pitching.player_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / pitching |
| pitching.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching |
| pitching.stint | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching |
| pitching.team_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / pitching |
| pitching.league_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / pitching |
| pitching.w | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching |
| pitching.l | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching |
| pitching.g | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching |
| pitching.gs | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching |
| pitching.cg | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching |
| pitching.sho | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching |
| pitching.sv | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching |
| pitching.ipouts | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / pitching |
| pitching.h | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching |
| pitching.er | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching |
| pitching.hr | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching |
| pitching.bb | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching |
| pitching.so | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching |
| pitching.baopp | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / pitching |
| pitching.era | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / pitching |
| pitching.ibb | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / pitching |
| pitching.wp | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / pitching |
| pitching.hbp | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / pitching |
| pitching.bk | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching |
| pitching.bfp | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / pitching |
| pitching.gf | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / pitching |
| pitching.r | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching |
| pitching.sh | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / pitching |
| pitching.sf | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / pitching |
| pitching.g_idp | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / pitching |

## pitching_postseason

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| pitching_postseason.player_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / pitching_postseason |
| pitching_postseason.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching_postseason |
| pitching_postseason.round | 保留物理名称；存档没有恢复别名 | TEXT | schema / pitching_postseason |
| pitching_postseason.team_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / pitching_postseason |
| pitching_postseason.league_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / pitching_postseason |
| pitching_postseason.w | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching_postseason |
| pitching_postseason.l | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching_postseason |
| pitching_postseason.g | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching_postseason |
| pitching_postseason.gs | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching_postseason |
| pitching_postseason.cg | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching_postseason |
| pitching_postseason.sho | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching_postseason |
| pitching_postseason.sv | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching_postseason |
| pitching_postseason.ipouts | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching_postseason |
| pitching_postseason.h | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching_postseason |
| pitching_postseason.er | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching_postseason |
| pitching_postseason.hr | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching_postseason |
| pitching_postseason.bb | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching_postseason |
| pitching_postseason.so | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching_postseason |
| pitching_postseason.baopp | 保留物理名称；存档没有恢复别名 | TEXT | schema / pitching_postseason |
| pitching_postseason.era | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / pitching_postseason |
| pitching_postseason.ibb | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / pitching_postseason |
| pitching_postseason.wp | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / pitching_postseason |
| pitching_postseason.hbp | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / pitching_postseason |
| pitching_postseason.bk | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / pitching_postseason |
| pitching_postseason.bfp | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / pitching_postseason |
| pitching_postseason.gf | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching_postseason |
| pitching_postseason.r | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pitching_postseason |
| pitching_postseason.sh | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / pitching_postseason |
| pitching_postseason.sf | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / pitching_postseason |
| pitching_postseason.g_idp | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / pitching_postseason |

## player

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: p

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| player.player_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / player |
| player.birth_year | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / player |
| player.birth_month | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / player |
| player.birth_day | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / player |
| player.birth_country | 保留物理名称；存档没有恢复别名 | TEXT | schema / player |
| player.birth_state | 保留物理名称；存档没有恢复别名 | TEXT | schema / player |
| player.birth_city | 保留物理名称；存档没有恢复别名 | TEXT | schema / player |
| player.death_year | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / player |
| player.death_month | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / player |
| player.death_day | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / player |
| player.death_country | 保留物理名称；存档没有恢复别名 | TEXT | schema / player |
| player.death_state | 保留物理名称；存档没有恢复别名 | TEXT | schema / player |
| player.death_city | 保留物理名称；存档没有恢复别名 | TEXT | schema / player |
| player.name_first | 保留物理名称；存档没有恢复别名 | TEXT | schema / player |
| player.name_last | 保留物理名称；存档没有恢复别名 | TEXT | schema / player |
| player.name_given | 保留物理名称；存档没有恢复别名 | TEXT | schema / player |
| player.weight | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / player |
| player.height | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / player |
| player.bats | 保留物理名称；存档没有恢复别名 | TEXT | schema / player |
| player.throws | 保留物理名称；存档没有恢复别名 | TEXT | schema / player |
| player.debut | 保留物理名称；存档没有恢复别名 | TEXT | schema / player |
| player.final_game | 保留物理名称；存档没有恢复别名 | TEXT | schema / player |
| player.retro_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / player |
| player.bbref_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / player |

## player_award

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| player_award.player_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / player_award |
| player_award.award_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / player_award |
| player_award.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / player_award |
| player_award.league_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / player_award |
| player_award.tie | 保留物理名称；存档没有恢复别名 | TEXT | schema / player_award |
| player_award.notes | 保留物理名称；存档没有恢复别名 | TEXT | schema / player_award |

## player_award_vote

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| player_award_vote.award_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / player_award_vote |
| player_award_vote.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / player_award_vote |
| player_award_vote.league_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / player_award_vote |
| player_award_vote.player_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / player_award_vote |
| player_award_vote.points_won | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / player_award_vote |
| player_award_vote.points_max | 保留物理名称；存档没有恢复别名 | INTEGER | schema / player_award_vote |
| player_award_vote.votes_first | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / player_award_vote |

## player_college

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| player_college.player_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / player_college |
| player_college.college_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / player_college |
| player_college.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / player_college |

## postseason

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| postseason.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / postseason |
| postseason.round | 保留物理名称；存档没有恢复别名 | TEXT | schema / postseason |
| postseason.team_id_winner | 保留物理名称；存档没有恢复别名 | TEXT | schema / postseason |
| postseason.league_id_winner | 保留物理名称；存档没有恢复别名 | TEXT | schema / postseason |
| postseason.team_id_loser | 保留物理名称；存档没有恢复别名 | TEXT | schema / postseason |
| postseason.league_id_loser | 保留物理名称；存档没有恢复别名 | TEXT | schema / postseason |
| postseason.wins | 保留物理名称；存档没有恢复别名 | INTEGER | schema / postseason |
| postseason.losses | 保留物理名称；存档没有恢复别名 | INTEGER | schema / postseason |
| postseason.ties | 保留物理名称；存档没有恢复别名 | INTEGER | schema / postseason |

## salary

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| salary.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / salary |
| salary.team_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / salary |
| salary.league_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / salary |
| salary.player_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / salary |
| salary.salary | 保留物理名称；存档没有恢复别名 | INTEGER | schema / salary |

## team

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| team.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.league_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / team |
| team.team_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / team |
| team.franchise_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / team |
| team.div_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / team |
| team.rank | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.g | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.ghome | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / team |
| team.w | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.l | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.div_win | 保留物理名称；存档没有恢复别名 | TEXT | schema / team |
| team.wc_win | 保留物理名称；存档没有恢复别名 | TEXT | schema / team |
| team.lg_win | 保留物理名称；存档没有恢复别名 | TEXT | schema / team |
| team.ws_win | 保留物理名称；存档没有恢复别名 | TEXT | schema / team |
| team.r | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.ab | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.h | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.double | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.triple | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.hr | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.bb | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.so | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / team |
| team.sb | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / team |
| team.cs | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / team |
| team.hbp | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / team |
| team.sf | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / team |
| team.ra | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.er | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.era | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / team |
| team.cg | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.sho | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.sv | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.ipouts | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.ha | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.hra | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.bba | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.soa | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.e | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.dp | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / team |
| team.fp | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / team |
| team.name | 保留物理名称；存档没有恢复别名 | TEXT | schema / team |
| team.park | 保留物理名称；存档没有恢复别名 | TEXT | schema / team |
| team.attendance | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / team |
| team.bpf | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.ppf | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team |
| team.team_id_br | 保留物理名称；存档没有恢复别名 | TEXT | schema / team |
| team.team_id_lahman45 | 保留物理名称；存档没有恢复别名 | TEXT | schema / team |
| team.team_id_retro | 保留物理名称；存档没有恢复别名 | TEXT | schema / team |

## team_franchise

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| team_franchise.franchise_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / team_franchise |
| team_franchise.franchise_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / team_franchise |
| team_franchise.active | 保留物理名称；存档没有恢复别名 | TEXT | schema / team_franchise |
| team_franchise.na_assoc | 保留物理名称；存档没有恢复别名 | TEXT | schema / team_franchise |

## team_half

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| team_half.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team_half |
| team_half.league_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / team_half |
| team_half.team_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / team_half |
| team_half.half | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team_half |
| team_half.div_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / team_half |
| team_half.div_win | 保留物理名称；存档没有恢复别名 | TEXT | schema / team_half |
| team_half.rank | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team_half |
| team_half.g | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team_half |
| team_half.w | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team_half |
| team_half.l | 保留物理名称；存档没有恢复别名 | INTEGER | schema / team_half |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

