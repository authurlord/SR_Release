# EvoSchema / evoschema::table_split::european_football_2::1042 — Schema and business semantics

The saved catalogue for this database contains 10 tables, 202 physical columns, 0 relationships and 10 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## BettingDetails

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| BettingDetails.id | Physical name retained; no saved recovered alias | INTEGER | schema / BettingDetails |
| BettingDetails.B365H | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.B365D | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.B365A | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.BWH | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.BWD | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.BWA | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.IWH | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.IWD | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.IWA | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.LBH | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.LBD | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.LBA | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.PSH | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.PSD | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.PSA | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.WHH | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.WHD | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.WHA | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.SJH | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.SJD | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.SJA | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.VCH | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.VCD | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.VCA | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.GBH | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.GBD | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.GBA | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.BSH | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.BSD | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |
| BettingDetails.BSA | Physical name retained; no saved recovered alias | REAL | schema / BettingDetails |

## Country

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Country.id | Physical name retained; no saved recovered alias | INTEGER | schema / Country |
| Country.name | Physical name retained; no saved recovered alias | TEXT | schema / Country |

## League

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| League.id | Physical name retained; no saved recovered alias | INTEGER | schema / League |
| League.country_id | Physical name retained; no saved recovered alias | INTEGER | schema / League |
| League.name | Physical name retained; no saved recovered alias | TEXT | schema / League |

## MatchDetails

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| MatchDetails.id | Physical name retained; no saved recovered alias | INTEGER | schema / MatchDetails |
| MatchDetails.country_id | Physical name retained; no saved recovered alias | INTEGER | schema / MatchDetails |
| MatchDetails.league_id | Physical name retained; no saved recovered alias | INTEGER | schema / MatchDetails |
| MatchDetails.season | Physical name retained; no saved recovered alias | TEXT | schema / MatchDetails |
| MatchDetails.stage | Physical name retained; no saved recovered alias | INTEGER | schema / MatchDetails |
| MatchDetails.date | Physical name retained; no saved recovered alias | TEXT | schema / MatchDetails |
| MatchDetails.match_api_id | Physical name retained; no saved recovered alias | INTEGER | schema / MatchDetails |
| MatchDetails.home_team_goal | Physical name retained; no saved recovered alias | INTEGER | schema / MatchDetails |
| MatchDetails.away_team_goal | Physical name retained; no saved recovered alias | INTEGER | schema / MatchDetails |
| MatchDetails.goal | Physical name retained; no saved recovered alias | TEXT | schema / MatchDetails |
| MatchDetails.shoton | Physical name retained; no saved recovered alias | TEXT | schema / MatchDetails |
| MatchDetails.shotoff | Physical name retained; no saved recovered alias | TEXT | schema / MatchDetails |
| MatchDetails.foulcommit | Physical name retained; no saved recovered alias | TEXT | schema / MatchDetails |
| MatchDetails.card | Physical name retained; no saved recovered alias | TEXT | schema / MatchDetails |
| MatchDetails.cross | Physical name retained; no saved recovered alias | TEXT | schema / MatchDetails |
| MatchDetails.corner | Physical name retained; no saved recovered alias | TEXT | schema / MatchDetails |
| MatchDetails.possession | Physical name retained; no saved recovered alias | TEXT | schema / MatchDetails |

## Player

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Player.id | Physical name retained; no saved recovered alias | INTEGER | schema / Player |
| Player.player_api_id | Physical name retained; no saved recovered alias | INTEGER | schema / Player |
| Player.player_name | Physical name retained; no saved recovered alias | TEXT | schema / Player |
| Player.player_fifa_api_id | Physical name retained; no saved recovered alias | INTEGER | schema / Player |
| Player.birthday | Physical name retained; no saved recovered alias | TEXT | schema / Player |
| Player.height | Physical name retained; no saved recovered alias | INTEGER | schema / Player |
| Player.weight | Physical name retained; no saved recovered alias | INTEGER | schema / Player |

## Player_Attributes

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Player_Attributes.id | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.player_fifa_api_id | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.player_api_id | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.date | Physical name retained; no saved recovered alias | TEXT | schema / Player_Attributes |
| Player_Attributes.overall_rating | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.potential | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.preferred_foot | Physical name retained; no saved recovered alias | TEXT | schema / Player_Attributes |
| Player_Attributes.attacking_work_rate | Physical name retained; no saved recovered alias | TEXT | schema / Player_Attributes |
| Player_Attributes.defensive_work_rate | Physical name retained; no saved recovered alias | TEXT | schema / Player_Attributes |
| Player_Attributes.crossing | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.finishing | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.heading_accuracy | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.short_passing | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.volleys | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.dribbling | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.curve | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.free_kick_accuracy | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.long_passing | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.ball_control | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.acceleration | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.sprint_speed | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.agility | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.reactions | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.balance | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.shot_power | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.jumping | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.stamina | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.strength | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.long_shots | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.aggression | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.interceptions | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.positioning | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.vision | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.penalties | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.marking | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.standing_tackle | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.sliding_tackle | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.gk_diving | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.gk_handling | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.gk_kicking | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.gk_positioning | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |
| Player_Attributes.gk_reflexes | Physical name retained; no saved recovered alias | INTEGER | schema / Player_Attributes |

## PlayerDetails

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| PlayerDetails.id | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.home_player_1 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.home_player_2 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.home_player_3 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.home_player_4 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.home_player_5 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.home_player_6 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.home_player_7 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.home_player_8 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.home_player_9 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.home_player_10 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.home_player_11 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.away_player_1 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.away_player_2 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.away_player_3 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.away_player_4 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.away_player_5 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.away_player_6 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.away_player_7 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.away_player_8 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.away_player_9 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.away_player_10 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |
| PlayerDetails.away_player_11 | Physical name retained; no saved recovered alias | INTEGER | schema / PlayerDetails |

## Team

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Team.id | Physical name retained; no saved recovered alias | INTEGER | schema / Team |
| Team.team_api_id | Physical name retained; no saved recovered alias | INTEGER | schema / Team |
| Team.team_fifa_api_id | Physical name retained; no saved recovered alias | INTEGER | schema / Team |
| Team.team_long_name | Physical name retained; no saved recovered alias | TEXT | schema / Team |
| Team.team_short_name | Physical name retained; no saved recovered alias | TEXT | schema / Team |

## Team_Attributes

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Team_Attributes.id | Physical name retained; no saved recovered alias | INTEGER | schema / Team_Attributes |
| Team_Attributes.team_fifa_api_id | Physical name retained; no saved recovered alias | INTEGER | schema / Team_Attributes |
| Team_Attributes.team_api_id | Physical name retained; no saved recovered alias | INTEGER | schema / Team_Attributes |
| Team_Attributes.date | Physical name retained; no saved recovered alias | TEXT | schema / Team_Attributes |
| Team_Attributes.buildUpPlaySpeed | Physical name retained; no saved recovered alias | INTEGER | schema / Team_Attributes |
| Team_Attributes.buildUpPlaySpeedClass | Physical name retained; no saved recovered alias | TEXT | schema / Team_Attributes |
| Team_Attributes.buildUpPlayDribbling | Physical name retained; no saved recovered alias | INTEGER | schema / Team_Attributes |
| Team_Attributes.buildUpPlayDribblingClass | Physical name retained; no saved recovered alias | TEXT | schema / Team_Attributes |
| Team_Attributes.buildUpPlayPassing | Physical name retained; no saved recovered alias | INTEGER | schema / Team_Attributes |
| Team_Attributes.buildUpPlayPassingClass | Physical name retained; no saved recovered alias | TEXT | schema / Team_Attributes |
| Team_Attributes.buildUpPlayPositioningClass | Physical name retained; no saved recovered alias | TEXT | schema / Team_Attributes |
| Team_Attributes.chanceCreationPassing | Physical name retained; no saved recovered alias | INTEGER | schema / Team_Attributes |
| Team_Attributes.chanceCreationPassingClass | Physical name retained; no saved recovered alias | TEXT | schema / Team_Attributes |
| Team_Attributes.chanceCreationCrossing | Physical name retained; no saved recovered alias | INTEGER | schema / Team_Attributes |
| Team_Attributes.chanceCreationCrossingClass | Physical name retained; no saved recovered alias | TEXT | schema / Team_Attributes |
| Team_Attributes.chanceCreationShooting | Physical name retained; no saved recovered alias | INTEGER | schema / Team_Attributes |
| Team_Attributes.chanceCreationShootingClass | Physical name retained; no saved recovered alias | TEXT | schema / Team_Attributes |
| Team_Attributes.chanceCreationPositioningClass | Physical name retained; no saved recovered alias | TEXT | schema / Team_Attributes |
| Team_Attributes.defencePressure | Physical name retained; no saved recovered alias | INTEGER | schema / Team_Attributes |
| Team_Attributes.defencePressureClass | Physical name retained; no saved recovered alias | TEXT | schema / Team_Attributes |
| Team_Attributes.defenceAggression | Physical name retained; no saved recovered alias | INTEGER | schema / Team_Attributes |
| Team_Attributes.defenceAggressionClass | Physical name retained; no saved recovered alias | TEXT | schema / Team_Attributes |
| Team_Attributes.defenceTeamWidth | Physical name retained; no saved recovered alias | INTEGER | schema / Team_Attributes |
| Team_Attributes.defenceTeamWidthClass | Physical name retained; no saved recovered alias | TEXT | schema / Team_Attributes |
| Team_Attributes.defenceDefenderLineClass | Physical name retained; no saved recovered alias | TEXT | schema / Team_Attributes |

## TeamDetails

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| TeamDetails.id | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_team_api_id | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_team_api_id | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_X1 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_X2 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_X3 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_X4 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_X5 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_X6 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_X7 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_X8 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_X9 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_X10 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_X11 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_X1 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_X2 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_X3 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_X4 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_X5 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_X6 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_X7 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_X8 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_X9 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_X10 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_X11 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_Y1 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_Y2 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_Y3 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_Y4 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_Y5 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_Y6 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_Y7 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_Y8 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_Y9 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_Y10 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.home_player_Y11 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_Y1 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_Y2 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_Y3 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_Y4 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_Y5 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_Y6 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_Y7 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_Y8 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_Y9 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_Y10 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |
| TeamDetails.away_player_Y11 | Physical name retained; no saved recovered alias | INTEGER | schema / TeamDetails |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

