# Spider2-Lite / BowlingLeague — Schema and business semantics

The saved catalogue for this database contains 11 tables, 54 physical columns, 0 relationships and 11 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## Bowler_Scores

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: bs, bs2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Bowler_Scores.MatchID | Physical name retained; no saved recovered alias | INT | schema / Bowler_Scores |
| Bowler_Scores.GameNumber | Physical name retained; no saved recovered alias | smallint | schema / Bowler_Scores |
| Bowler_Scores.BowlerID | Physical name retained; no saved recovered alias | INT | schema / Bowler_Scores |
| Bowler_Scores.RawScore | Physical name retained; no saved recovered alias | smallint | schema / Bowler_Scores |
| Bowler_Scores.HandiCapScore | Physical name retained; no saved recovered alias | smallint | schema / Bowler_Scores |
| Bowler_Scores.WonGame | Physical name retained; no saved recovered alias | BOOLEAN | schema / Bowler_Scores |

## Bowler_Scores_Archive

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Bowler_Scores_Archive.MatchID | Physical name retained; no saved recovered alias | INT | schema / Bowler_Scores_Archive |
| Bowler_Scores_Archive.GameNumber | Physical name retained; no saved recovered alias | smallint | schema / Bowler_Scores_Archive |
| Bowler_Scores_Archive.BowlerID | Physical name retained; no saved recovered alias | INT | schema / Bowler_Scores_Archive |
| Bowler_Scores_Archive.RawScore | Physical name retained; no saved recovered alias | smallint | schema / Bowler_Scores_Archive |
| Bowler_Scores_Archive.HandiCapScore | Physical name retained; no saved recovered alias | smallint | schema / Bowler_Scores_Archive |
| Bowler_Scores_Archive.WonGame | Physical name retained; no saved recovered alias | BOOLEAN | schema / Bowler_Scores_Archive |

## Bowlers

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: b

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Bowlers.BowlerID | Physical name retained; no saved recovered alias | INTEGER | schema / Bowlers |
| Bowlers.BowlerLastName | Physical name retained; no saved recovered alias | TEXT | schema / Bowlers |
| Bowlers.BowlerFirstName | Physical name retained; no saved recovered alias | TEXT | schema / Bowlers |
| Bowlers.BowlerMiddleInit | Physical name retained; no saved recovered alias | TEXT | schema / Bowlers |
| Bowlers.BowlerAddress | Physical name retained; no saved recovered alias | TEXT | schema / Bowlers |
| Bowlers.BowlerCity | Physical name retained; no saved recovered alias | TEXT | schema / Bowlers |
| Bowlers.BowlerState | Physical name retained; no saved recovered alias | TEXT | schema / Bowlers |
| Bowlers.BowlerZip | Physical name retained; no saved recovered alias | TEXT | schema / Bowlers |
| Bowlers.BowlerPhoneNumber | Physical name retained; no saved recovered alias | TEXT | schema / Bowlers |
| Bowlers.TeamID | Physical name retained; no saved recovered alias | INT | schema / Bowlers |
| Bowlers.BowlerTotalPins | Physical name retained; no saved recovered alias | INT | schema / Bowlers |
| Bowlers.BowlerGamesBowled | Physical name retained; no saved recovered alias | INT | schema / Bowlers |
| Bowlers.BowlerCurrentAverage | Physical name retained; no saved recovered alias | smallint | schema / Bowlers |
| Bowlers.BowlerCurrentHcp | Physical name retained; no saved recovered alias | smallint | schema / Bowlers |

## Match_Games

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Match_Games.MatchID | Physical name retained; no saved recovered alias | INT | schema / Match_Games |
| Match_Games.GameNumber | Physical name retained; no saved recovered alias | smallint | schema / Match_Games |
| Match_Games.WinningTeamID | Physical name retained; no saved recovered alias | INT | schema / Match_Games |

## Match_Games_Archive

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Match_Games_Archive.MatchID | Physical name retained; no saved recovered alias | INT | schema / Match_Games_Archive |
| Match_Games_Archive.GameNumber | Physical name retained; no saved recovered alias | smallint | schema / Match_Games_Archive |
| Match_Games_Archive.WinningTeamID | Physical name retained; no saved recovered alias | INT | schema / Match_Games_Archive |

## Teams

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Teams.TeamID | Physical name retained; no saved recovered alias | INTEGER | schema / Teams |
| Teams.TeamName | Physical name retained; no saved recovered alias | TEXT | schema / Teams |
| Teams.CaptainID | Physical name retained; no saved recovered alias | INT | schema / Teams |

## Tournaments

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: t, t2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Tournaments.TourneyID | Physical name retained; no saved recovered alias | INTEGER | schema / Tournaments |
| Tournaments.TourneyDate | Physical name retained; no saved recovered alias | DATE | schema / Tournaments |
| Tournaments.TourneyLocation | Physical name retained; no saved recovered alias | TEXT | schema / Tournaments |

## Tournaments_Archive

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Tournaments_Archive.TourneyID | Physical name retained; no saved recovered alias | INT | schema / Tournaments_Archive |
| Tournaments_Archive.TourneyDate | Physical name retained; no saved recovered alias | DATE | schema / Tournaments_Archive |
| Tournaments_Archive.TourneyLocation | Physical name retained; no saved recovered alias | TEXT | schema / Tournaments_Archive |

## Tourney_Matches

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: tm, tm2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Tourney_Matches.MatchID | Physical name retained; no saved recovered alias | INTEGER | schema / Tourney_Matches |
| Tourney_Matches.TourneyID | Physical name retained; no saved recovered alias | INT | schema / Tourney_Matches |
| Tourney_Matches.Lanes | Physical name retained; no saved recovered alias | TEXT | schema / Tourney_Matches |
| Tourney_Matches.OddLaneTeamID | Physical name retained; no saved recovered alias | INT | schema / Tourney_Matches |
| Tourney_Matches.EvenLaneTeamID | Physical name retained; no saved recovered alias | INT | schema / Tourney_Matches |

## Tourney_Matches_Archive

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Tourney_Matches_Archive.MatchID | Physical name retained; no saved recovered alias | INT | schema / Tourney_Matches_Archive |
| Tourney_Matches_Archive.TourneyID | Physical name retained; no saved recovered alias | INT | schema / Tourney_Matches_Archive |
| Tourney_Matches_Archive.Lanes | Physical name retained; no saved recovered alias | TEXT | schema / Tourney_Matches_Archive |
| Tourney_Matches_Archive.OddLaneTeamID | Physical name retained; no saved recovered alias | INT | schema / Tourney_Matches_Archive |
| Tourney_Matches_Archive.EvenLaneTeamID | Physical name retained; no saved recovered alias | INT | schema / Tourney_Matches_Archive |

## WAZips

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| WAZips.ZIP | Physical name retained; no saved recovered alias | TEXT | schema / WAZips |
| WAZips.City | Physical name retained; no saved recovered alias | TEXT | schema / WAZips |
| WAZips.State | Physical name retained; no saved recovered alias | TEXT | schema / WAZips |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

