# BIRD-Mini / formula_1 — Schema and business semantics

The saved catalogue for this database contains 13 tables, 94 physical columns, 19 relationships and 13 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## circuits

Stores information about Formula 1 race circuits, including their names, locations, and geographical coordinates.

Recovered table names: circuits / tracks / race_circuits / grand_prix_circuits
SQL table aliases: c

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| circuits.XCL_001 | circuit id / circuit identifier / circuit_id / circuit_identifier / id / circuit_number | integer | schema / circuits |
| circuits.XCL_002 | circuit ref / circuit reference / circuit_reference / ref / short_name / abbreviation | text | schema / circuits |
| circuits.XCL_003 | name / circuit_name / full_name / track_name / circuit | text | schema / circuits |
| circuits.XCL_004 | location / city / town / place / locality | text | schema / circuits |
| circuits.XCL_005 | country / nation / state / country_name | text | schema / circuits |
| circuits.XCL_006 | lat / latitude / lat_coordinate / north_south | real | schema / circuits |
| circuits.XCL_007 | lng / longitude / lng_coordinate / east_west | real | schema / circuits |
| circuits.XCL_008 | alt / altitude / elevation / height / above_sea_level | integer | schema / circuits |
| circuits.XCL_009 | url / website / link / wikipedia_url / reference_url | text | schema / circuits |

## constructors

This table stores information about Formula 1 constructors (teams), including their unique identifiers, names, nationalities, and Wikipedia URLs.

Recovered table names: constructors / teams / f1_teams / racing_teams / constructors_table
SQL table aliases: c

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| constructors.XCL_022 | constructor id / constructor identifier / constructor_id / team_id / id / constructor_identifier / team_identifier | integer | schema / constructors |
| constructors.XCL_023 | constructor ref / constructor reference / constructor_ref / team_ref / constructor_reference / team_reference / short_name | text | schema / constructors |
| constructors.XCL_024 | name / constructor_name / team_name / full_name / constructor_full_name / team_full_name | text | schema / constructors |
| constructors.XCL_025 | nationality / constructor_nationality / team_nationality / country / origin / nation | text | schema / constructors |
| constructors.XCL_026 | url / wikipedia_url / wiki_url / constructor_url / team_url / link | text | schema / constructors |

## drivers

Stores biographical information about Formula 1 drivers, including their unique identifier, reference code, car number, three-letter code, name, date of birth, nationality, and Wikipedia URL.

Recovered table names: drivers / driver / F1 driver / Formula 1 driver / racing driver
SQL table aliases: d, d1

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| drivers.XCL_034 | driver id / driver identifier / driver number (internal) / driver key | integer | schema / drivers |
| drivers.XCL_035 | driver ref / driver reference / driver code (short) / driver abbreviation / driver handle | text | schema / drivers |
| drivers.XCL_036 | number / car number / driver number / racing number / permanent number | integer | schema / drivers |
| drivers.XCL_037 | code / three-letter code / driver code / abbreviation / initials | text | schema / drivers |
| drivers.XCL_038 | forename / first name / given name / driver first name | text | schema / drivers |
| drivers.XCL_039 | surname / last name / family name / driver last name | text | schema / drivers |
| drivers.XCL_040 | dob / date of birth / birth date / birthday / driver birth date | date | schema / drivers |
| drivers.XCL_041 | nationality / country / driver nationality / nationality code | text | schema / drivers |
| drivers.XCL_042 | url / Wikipedia URL / Wikipedia link / driver URL / biography link | text | schema / drivers |

## seasons

Stores each Formula 1 racing season identified by its year, along with a link to the corresponding Wikipedia article.

Recovered table names: seasons / Formula 1 seasons / F1 seasons / racing seasons / championship seasons
SQL table aliases: s

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| seasons.XCL_091 | year / season year / racing year / championship year / F1 year / season | integer | schema / seasons |
| seasons.XCL_092 | url / Wikipedia URL / article link / season page / reference link / source URL | text | schema / seasons |

## races

Stores information about each Formula 1 race event, including its name, date, time, circuit, and year.

Recovered table names: races / race / grand prix / grands prix / F1 race / F1 races
SQL table aliases: r, ra

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| races.XCL_065 | race id / race identifier / race number / race key | integer | schema / races |
| races.XCL_066 | year / race year / season year / year of race / race season | integer | schema / races |
| races.XCL_067 | round / race round / round number / race number in season / event round | integer | schema / races |
| races.XCL_068 | circuit id / circuit identifier / track id / track identifier | integer | schema / races |
| races.XCL_069 | name / race name / grand prix name / event name / race title | text | schema / races |
| races.XCL_070 | date / race date / event date / race day / date of race | date | schema / races |
| races.XCL_071 | time / race time / start time / event time / race start time | text | schema / races |
| races.XCL_072 | url / race url / wikipedia url / race link / race wikipedia page | text | schema / races |

## constructorResults

Stores the points and status for each constructor (team) in each race.

Recovered table names: constructor results / team results / constructor race results
SQL table aliases: cr

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| constructorResults.XCL_010 | constructor results id / constructor results identifier / constructor result ID / result ID | integer | schema / constructorResults |
| constructorResults.XCL_011 | race id / race identifier / race number | integer | schema / constructorResults |
| constructorResults.XCL_012 | constructor id / constructor identifier / team ID / team identifier | integer | schema / constructorResults |
| constructorResults.XCL_013 | points / score / championship points / race points | real | schema / constructorResults |
| constructorResults.XCL_014 | status / result status / finish status / classification | text | schema / constructorResults |

## constructorStandings

Stores the championship standings for constructors (teams) per race, including points, position, and wins.

Recovered table names: constructor standings / team standings / constructor championship standings / team championship standings / constructor rankings / team rankings
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| constructorStandings.XCL_015 | constructor standings id / constructor standings identifier / standings ID / standings record ID / standings identifier | integer | schema / constructorStandings |
| constructorStandings.XCL_016 | race id / race identifier / race number / grand prix ID | integer | schema / constructorStandings |
| constructorStandings.XCL_017 | constructor id / constructor identifier / team ID / team identifier | integer | schema / constructorStandings |
| constructorStandings.XCL_018 | points / total points / championship points / score | real | schema / constructorStandings |
| constructorStandings.XCL_019 | position / rank / standing position / championship position / place | integer | schema / constructorStandings |
| constructorStandings.XCL_020 | position text / position label / rank text / standing text | text | schema / constructorStandings |
| constructorStandings.XCL_021 | wins / race wins / victories / number of wins | integer | schema / constructorStandings |

## driverStandings

Stores the points, position, and win count for each driver in each race, forming the basis for driver championship standings.

Recovered table names: driver standings / driver championship standings / driver points table / driver ranking / driver positions
SQL table aliases: ds

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| driverStandings.XCL_027 | driver standings id / driver standings identifier / standings ID / record ID / standings record number | integer | schema / driverStandings |
| driverStandings.XCL_028 | race id / race identifier / grand prix ID / event ID | integer | schema / driverStandings |
| driverStandings.XCL_029 | driver id / driver identifier / driver number / competitor ID | integer | schema / driverStandings |
| driverStandings.XCL_030 | points / championship points / score / total points | real | schema / driverStandings |
| driverStandings.XCL_031 | position / race position / finishing position / rank / place | integer | schema / driverStandings |
| driverStandings.XCL_032 | position text / position string / finishing position text / rank text | text | schema / driverStandings |
| driverStandings.XCL_033 | wins / race wins / victories / number of wins | integer | schema / driverStandings |

## lapTimes

Stores per-lap timing data for each driver in each race, including lap number, position, and time.

Recovered table names: lap times / lap records / lap data / lap information
SQL table aliases: l, lt

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| lapTimes.XCL_043 | race id / race identifier / race number / race | integer | schema / lapTimes |
| lapTimes.XCL_044 | driver id / driver identifier / driver number / driver | integer | schema / lapTimes |
| lapTimes.XCL_045 | lap / lap number / lap count / lap index / laps | integer | schema / lapTimes |
| lapTimes.XCL_046 | position / race position / standing / rank / place / position in lap | integer | schema / lapTimes |
| lapTimes.XCL_047 | time / lap time / lap duration / time string / time formatted | text | schema / lapTimes |
| lapTimes.XCL_048 | milliseconds / lap time in milliseconds / time in ms / duration in milliseconds | integer | schema / lapTimes |

## pitStops

Records each pit stop made by a driver during a race, including the stop number, lap, time, and duration.

Recovered table names: pit stops / pitstop / pit_stops / pits
SQL table aliases: p

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| pitStops.XCL_049 | race id / race identifier / race number / grand prix id | integer | schema / pitStops |
| pitStops.XCL_050 | driver id / driver identifier / driver number / pilot id | integer | schema / pitStops |
| pitStops.XCL_051 | stop / stop number / pit stop number / stop count / pit visit number | integer | schema / pitStops |
| pitStops.XCL_052 | lap / lap number / lap count / race lap / circuit lap | integer | schema / pitStops |
| pitStops.XCL_053 | time / pit stop time / stop time / time of day / clock time | text | schema / pitStops |
| pitStops.XCL_054 | duration / pit stop duration / stop duration / pit time / stop length / pit stop time in seconds | text | schema / pitStops |
| pitStops.XCL_055 | milliseconds / duration in milliseconds / pit stop milliseconds / stop milliseconds / pit time ms | integer | schema / pitStops |

## qualifying

Stores the results of Formula 1 qualifying sessions, including driver, constructor, position, and lap times for each qualifying round (Q1, Q2, Q3).

Recovered table names: qualifying / qualifying sessions / qualifying results / qualifying rounds
SQL table aliases: q

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| qualifying.XCL_056 | qualify id / qualify identifier / qualifying ID / qualifying session ID / qualifying record ID | integer | schema / qualifying |
| qualifying.XCL_057 | race id / race identifier / race number / race event ID | integer | schema / qualifying |
| qualifying.XCL_058 | driver id / driver identifier / driver number / driver code | integer | schema / qualifying |
| qualifying.XCL_059 | constructor id / constructor identifier / team ID / team identifier | integer | schema / qualifying |
| qualifying.XCL_060 | number / car number / driver number / racing number / car identifier | integer | schema / qualifying |
| qualifying.XCL_061 | position / qualifying position / grid position / starting position / rank / place | integer | schema / qualifying |
| qualifying.XCL_062 | q1 / Q1 time / first qualifying session time / qualifying round 1 time / Q1 lap time | text | schema / qualifying |
| qualifying.XCL_063 | q2 / Q2 time / second qualifying session time / qualifying round 2 time / Q2 lap time | text | schema / qualifying |
| qualifying.XCL_064 | q3 / Q3 time / third qualifying session time / qualifying round 3 time / Q3 lap time | text | schema / qualifying |

## status

Stores the possible status outcomes for a race result, such as finished, disqualified, or accident.

Recovered table names: status / statuses / race_statuses / finish_statuses / result_statuses
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| status.XCL_093 | status id / status identifier / status_id / status code / status number / id | integer | schema / status |
| status.XCL_094 | status / status_name / status_label / finish_status / race_outcome / result_status / status_description | text | schema / status |

## results

Stores the outcome of each driver in each race, including finishing position, points, laps completed, and fastest lap details.

Recovered table names: results / race_results / finishing_positions / race_outcomes
SQL table aliases: champ, last, r, r1, r2, res, res2, t

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| results.XCL_073 | result id / result identifier / result number / result key | integer | schema / results |
| results.XCL_074 | race id / race identifier / race number / race key | integer | schema / results |
| results.XCL_075 | driver id / driver identifier / driver number / driver key | integer | schema / results |
| results.XCL_076 | constructor id / constructor identifier / team ID / team identifier / team key | integer | schema / results |
| results.XCL_077 | number / car number / driver number / race number / entry number | integer | schema / results |
| results.XCL_078 | grid / starting grid position / grid position / starting position / qualifying position | integer | schema / results |
| results.XCL_079 | position / finishing position / race position / final position / result position | integer | schema / results |
| results.XCL_080 | position text / finishing position text / position string / result text | text | schema / results |
| results.XCL_081 | position order / finishing order / race order / classification order | integer | schema / results |
| results.XCL_082 | points / race points / championship points / score | real | schema / results |
| results.XCL_083 | laps / laps completed / number of laps / race laps | integer | schema / results |
| results.XCL_084 | time / race time / finish time / time string / total time | text | schema / results |
| results.XCL_085 | milliseconds / race time in ms / total milliseconds / time in milliseconds | integer | schema / results |
| results.XCL_086 | fastest lap / fastest lap number / fastest lap index / fastest lap lap number | integer | schema / results |
| results.XCL_087 | rank / fastest lap rank / rank of fastest lap / fastest lap position / speed rank | integer | schema / results |
| results.XCL_088 | fastest lap time / fastest lap time string / best lap time / quickest lap time | text | schema / results |
| results.XCL_089 | fastest lap speed / top speed / maximum speed / fastest speed | text | schema / results |
| results.XCL_090 | status id / status identifier / finish status ID / result status ID | integer | schema / results |

## Relationships and join evidence

- circuits.XCL_001 ↔ races.XCL_068; declared_or_materialized_relationship
- constructorResults.XCL_011 ↔ races.XCL_065; declared_or_materialized_relationship
- constructorResults.XCL_012 ↔ constructors.XCL_022; declared_or_materialized_relationship
- constructorStandings.XCL_016 ↔ races.XCL_065; declared_or_materialized_relationship
- constructorStandings.XCL_017 ↔ constructors.XCL_022; declared_or_materialized_relationship
- constructors.XCL_022 ↔ qualifying.XCL_059; declared_or_materialized_relationship
- constructors.XCL_022 ↔ results.XCL_076; declared_or_materialized_relationship
- driverStandings.XCL_028 ↔ races.XCL_065; declared_or_materialized_relationship
- driverStandings.XCL_029 ↔ drivers.XCL_034; declared_or_materialized_relationship
- drivers.XCL_034 ↔ lapTimes.XCL_044; declared_or_materialized_relationship
- drivers.XCL_034 ↔ pitStops.XCL_050; declared_or_materialized_relationship
- drivers.XCL_034 ↔ qualifying.XCL_058; declared_or_materialized_relationship
- drivers.XCL_034 ↔ results.XCL_075; declared_or_materialized_relationship
- lapTimes.XCL_043 ↔ races.XCL_065; declared_or_materialized_relationship
- pitStops.XCL_049 ↔ races.XCL_065; declared_or_materialized_relationship
- qualifying.XCL_057 ↔ races.XCL_065; declared_or_materialized_relationship
- races.XCL_065 ↔ results.XCL_074; declared_or_materialized_relationship
- races.XCL_066 ↔ seasons.XCL_091; declared_or_materialized_relationship
- results.XCL_090 ↔ status.XCL_093; declared_or_materialized_relationship

## Business definitions, population and grain


## Incremental maintenance events

