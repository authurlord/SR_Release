# Spider2-Lite / IPL — Schema and business semantics

The saved catalogue for this database contains 8 tables, 52 physical columns, 0 relationships and 8 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## ball_by_ball

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: b, bbb

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| ball_by_ball.match_id | Physical name retained; no saved recovered alias | INTEGER | schema / ball_by_ball |
| ball_by_ball.over_id | Physical name retained; no saved recovered alias | INTEGER | schema / ball_by_ball |
| ball_by_ball.ball_id | Physical name retained; no saved recovered alias | INTEGER | schema / ball_by_ball |
| ball_by_ball.innings_no | Physical name retained; no saved recovered alias | INTEGER | schema / ball_by_ball |
| ball_by_ball.team_batting | Physical name retained; no saved recovered alias | INTEGER | schema / ball_by_ball |
| ball_by_ball.team_bowling | Physical name retained; no saved recovered alias | INTEGER | schema / ball_by_ball |
| ball_by_ball.striker_batting_position | Physical name retained; no saved recovered alias | INTEGER | schema / ball_by_ball |
| ball_by_ball.striker | Physical name retained; no saved recovered alias | INTEGER | schema / ball_by_ball |
| ball_by_ball.non_striker | Physical name retained; no saved recovered alias | INTEGER | schema / ball_by_ball |
| ball_by_ball.bowler | Physical name retained; no saved recovered alias | INTEGER | schema / ball_by_ball |

## batsman_scored

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: bs, s

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| batsman_scored.match_id | Physical name retained; no saved recovered alias | INTEGER | schema / batsman_scored |
| batsman_scored.over_id | Physical name retained; no saved recovered alias | INTEGER | schema / batsman_scored |
| batsman_scored.ball_id | Physical name retained; no saved recovered alias | INTEGER | schema / batsman_scored |
| batsman_scored.runs_scored | Physical name retained; no saved recovered alias | INTEGER | schema / batsman_scored |
| batsman_scored.innings_no | Physical name retained; no saved recovered alias | INTEGER | schema / batsman_scored |

## extra_runs

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: er

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| extra_runs.match_id | Physical name retained; no saved recovered alias | INTEGER | schema / extra_runs |
| extra_runs.over_id | Physical name retained; no saved recovered alias | INTEGER | schema / extra_runs |
| extra_runs.ball_id | Physical name retained; no saved recovered alias | INTEGER | schema / extra_runs |
| extra_runs.extra_type | Physical name retained; no saved recovered alias | TEXT | schema / extra_runs |
| extra_runs.extra_runs | Physical name retained; no saved recovered alias | INTEGER | schema / extra_runs |
| extra_runs.innings_no | Physical name retained; no saved recovered alias | INTEGER | schema / extra_runs |

## match

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: m

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| match.match_id | Physical name retained; no saved recovered alias | INTEGER | schema / match |
| match.team_1 | Physical name retained; no saved recovered alias | INTEGER | schema / match |
| match.team_2 | Physical name retained; no saved recovered alias | INTEGER | schema / match |
| match.match_date | Physical name retained; no saved recovered alias | DATE | schema / match |
| match.season_id | Physical name retained; no saved recovered alias | INTEGER | schema / match |
| match.venue | Physical name retained; no saved recovered alias | TEXT | schema / match |
| match.toss_winner | Physical name retained; no saved recovered alias | INTEGER | schema / match |
| match.toss_decision | Physical name retained; no saved recovered alias | TEXT | schema / match |
| match.win_type | Physical name retained; no saved recovered alias | TEXT | schema / match |
| match.win_margin | Physical name retained; no saved recovered alias | INTEGER | schema / match |
| match.outcome_type | Physical name retained; no saved recovered alias | TEXT | schema / match |
| match.match_winner | Physical name retained; no saved recovered alias | INTEGER | schema / match |
| match.man_of_the_match | Physical name retained; no saved recovered alias | INTEGER | schema / match |

## player

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: p

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| player.player_id | Physical name retained; no saved recovered alias | INTEGER | schema / player |
| player.player_name | Physical name retained; no saved recovered alias | TEXT | schema / player |
| player.dob | Physical name retained; no saved recovered alias | DATE | schema / player |
| player.batting_hand | Physical name retained; no saved recovered alias | TEXT | schema / player |
| player.bowling_skill | Physical name retained; no saved recovered alias | TEXT | schema / player |
| player.country_name | Physical name retained; no saved recovered alias | TEXT | schema / player |

## player_match

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: pm

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| player_match.match_id | Physical name retained; no saved recovered alias | INTEGER | schema / player_match |
| player_match.player_id | Physical name retained; no saved recovered alias | INTEGER | schema / player_match |
| player_match.role | Physical name retained; no saved recovered alias | TEXT | schema / player_match |
| player_match.team_id | Physical name retained; no saved recovered alias | INTEGER | schema / player_match |

## team

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| team.team_id | Physical name retained; no saved recovered alias | INTEGER | schema / team |
| team.name | Physical name retained; no saved recovered alias | TEXT | schema / team |

## wicket_taken

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: w, wt

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| wicket_taken.match_id | Physical name retained; no saved recovered alias | INTEGER | schema / wicket_taken |
| wicket_taken.over_id | Physical name retained; no saved recovered alias | INTEGER | schema / wicket_taken |
| wicket_taken.ball_id | Physical name retained; no saved recovered alias | INTEGER | schema / wicket_taken |
| wicket_taken.player_out | Physical name retained; no saved recovered alias | INTEGER | schema / wicket_taken |
| wicket_taken.kind_out | Physical name retained; no saved recovered alias | TEXT | schema / wicket_taken |
| wicket_taken.innings_no | Physical name retained; no saved recovered alias | INTEGER | schema / wicket_taken |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

