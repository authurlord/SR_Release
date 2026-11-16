# BIRD-Mini / european_football_2 — Schema and business semantics

The saved catalogue for this database contains 7 tables, 199 physical columns, 29 relationships and 7 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## Player_Attributes

Stores periodic snapshots of player attribute ratings (e.g., from FIFA video game) including technical skills, physical abilities, mental attributes, and goalkeeper-specific stats, linked to players via API IDs.

Recovered table names: player attributes / player stats / player ratings / player skills / player characteristics / player abilities / player performance metrics / player attribute snapshots
SQL table aliases: pa, pa2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Player_Attributes.XCL_128 | id / identifier / attribute id / record id / row id / primary key | integer | schema / Player_Attributes |
| Player_Attributes.XCL_129 | player fifa api id / player fifa api identifier / fifa player id / fifa api id / fifa id | integer | schema / Player_Attributes |
| Player_Attributes.XCL_130 | player api id / player api identifier / player id / api player id | integer | schema / Player_Attributes |
| Player_Attributes.XCL_131 | date / snapshot date / attribute date / record date / rating date | text | schema / Player_Attributes |
| Player_Attributes.XCL_132 | overall rating / overall score / general rating / total rating | integer | schema / Player_Attributes |
| Player_Attributes.XCL_133 | potential / potential rating / future rating / upside / potential score | integer | schema / Player_Attributes |
| Player_Attributes.XCL_134 | preferred foot / strong foot / footedness | text | schema / Player_Attributes |
| Player_Attributes.XCL_135 | attacking work rate / offensive work rate / attack work rate | text | schema / Player_Attributes |
| Player_Attributes.XCL_136 | defensive work rate / defending work rate / defense work rate | text | schema / Player_Attributes |
| Player_Attributes.XCL_137 | crossing / crossing ability / crossing skill / crossing rating | integer | schema / Player_Attributes |
| Player_Attributes.XCL_138 | finishing / finishing ability / shooting accuracy / goal scoring / finishing skill | integer | schema / Player_Attributes |
| Player_Attributes.XCL_139 | heading accuracy / heading ability / aerial ability / header skill | integer | schema / Player_Attributes |
| Player_Attributes.XCL_140 | short passing / short pass accuracy / passing short | integer | schema / Player_Attributes |
| Player_Attributes.XCL_141 | volleys / volley ability / volley skill / volleying | integer | schema / Player_Attributes |
| Player_Attributes.XCL_142 | dribbling / dribbling ability / dribbling skill / ball control dribbling | integer | schema / Player_Attributes |
| Player_Attributes.XCL_143 | curve / curve rating / bend / shot curve / curve ability | integer | schema / Player_Attributes |
| Player_Attributes.XCL_144 | free kick accuracy / free kick ability / set piece accuracy / free kick skill | integer | schema / Player_Attributes |
| Player_Attributes.XCL_145 | long passing / long pass accuracy / passing long | integer | schema / Player_Attributes |
| Player_Attributes.XCL_146 | ball control / first touch / control ability | integer | schema / Player_Attributes |
| Player_Attributes.XCL_147 | acceleration / burst of speed / initial speed / quick start | integer | schema / Player_Attributes |
| Player_Attributes.XCL_148 | sprint speed / top speed / running speed / pace | integer | schema / Player_Attributes |
| Player_Attributes.XCL_149 | agility / quickness / nimbleness / change of direction | integer | schema / Player_Attributes |
| Player_Attributes.XCL_150 | reactions / reflexes / reaction time / responsiveness | integer | schema / Player_Attributes |
| Player_Attributes.XCL_151 | balance / stability / equilibrium / body control | integer | schema / Player_Attributes |
| Player_Attributes.XCL_152 | shot power / shooting power / power shot / strike power | integer | schema / Player_Attributes |
| Player_Attributes.XCL_153 | jumping / leaping ability / vertical jump / aerial ability | integer | schema / Player_Attributes |
| Player_Attributes.XCL_154 | stamina / endurance / fitness / staying power | integer | schema / Player_Attributes |
| Player_Attributes.XCL_155 | strength / physical strength / power / body strength | integer | schema / Player_Attributes |
| Player_Attributes.XCL_156 | long shots / long range shooting / distance shooting / long shot ability | integer | schema / Player_Attributes |
| Player_Attributes.XCL_157 | aggression / aggressiveness / toughness / combativeness | integer | schema / Player_Attributes |
| Player_Attributes.XCL_158 | interceptions / reading play / anticipation / intercepting | integer | schema / Player_Attributes |
| Player_Attributes.XCL_159 | positioning / off the ball movement / spatial awareness / positional sense | integer | schema / Player_Attributes |
| Player_Attributes.XCL_160 | vision / passing vision / awareness / field vision | integer | schema / Player_Attributes |
| Player_Attributes.XCL_161 | penalties / penalty taking / penalty skill / spot kick ability | integer | schema / Player_Attributes |
| Player_Attributes.XCL_162 | marking / defensive marking / man marking / tight marking | integer | schema / Player_Attributes |
| Player_Attributes.XCL_163 | standing tackle / tackling standing / defensive tackle / standing challenge | integer | schema / Player_Attributes |
| Player_Attributes.XCL_164 | sliding tackle / tackling sliding / slide tackle / sliding challenge | integer | schema / Player_Attributes |
| Player_Attributes.XCL_165 | gk diving / goalkeeper | integer | schema / Player_Attributes |
| Player_Attributes.XCL_166 | gk handling | integer | schema / Player_Attributes |
| Player_Attributes.XCL_167 | gk kicking | integer | schema / Player_Attributes |
| Player_Attributes.XCL_168 | gk positioning | integer | schema / Player_Attributes |
| Player_Attributes.XCL_169 | gk reflexes | integer | schema / Player_Attributes |

## Player

Stores biographical and physical information about individual football (soccer) players, including identifiers, name, birthday, height, and weight.

Recovered table names: player / players / footballers / soccer players
SQL table aliases: p, p2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Player.XCL_121 | id / identifier / player id / primary key / row id / unique identifier | integer | schema / Player |
| Player.XCL_122 | player api id / player api identifier / api player id / external player id / player API key / player identifier | integer | schema / Player |
| Player.XCL_123 | player name / name / full name / player full name / footballer name | text | schema / Player |
| Player.XCL_124 | player fifa api id / player fifa api identifier / fifa player id / fifa api id / FIFA identifier / video game id | integer | schema / Player |
| Player.XCL_125 | birthday / date of birth / birth date / DOB / born on | text | schema / Player |
| Player.XCL_126 | height / height in cm / centimeters / player height / stature | integer | schema / Player |
| Player.XCL_127 | weight / weight in pounds / lbs / player weight / body mass | integer | schema / Player |

## League

Stores information about football leagues, including their names and associated countries.

Recovered table names: league / Leagues / Competitions / Divisions
SQL table aliases: L, l

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| League.XCL_003 | id / identifier / league_id / league_identifier / league_number / league_code | integer | schema / League |
| League.XCL_004 | country id / country identifier / country_identifier / nation_id / country_number / country_code | integer | schema / League |
| League.XCL_005 | name / league_name / competition_name / division_name / league_title / league | text | schema / League |

## Country

Stores information about countries participating in European football leagues.

Recovered table names: country / countries / nations / national teams
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Country.XCL_001 | id / identifier / country_id / country identifier / nation id / team country id | integer | schema / Country |
| Country.XCL_002 | name / country name / nation name / country / nation / team country | text | schema / Country |

## Team

Stores information about football teams, including unique identifiers and names.

Recovered table names: team / teams / soccer teams / football clubs
SQL table aliases: T, t

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Team.XCL_170 | id / identifier / team id / primary key / internal id | integer | schema / Team |
| Team.XCL_171 | team api id / team api identifier / api team id / external team id / team identifier | integer | schema / Team |
| Team.XCL_172 | team fifa api id / team fifa api identifier / fifa team id / fifa api id / fifa identifier | integer | schema / Team |
| Team.XCL_173 | team long name / team name / full team name / club name | text | schema / Team |
| Team.XCL_174 | team short name / short name / abbreviation / team code / acronym | text | schema / Team |

## Team_Attributes

Stores FIFA video game team attribute ratings and classifications for build-up play, chance creation, and defence at various points in time.

Recovered table names: team attributes / team characteristics / team stats / team properties / team parameters
SQL table aliases: TA, ta

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Team_Attributes.XCL_175 | id / identifier / record id / row id / attribute id / primary key | integer | schema / Team_Attributes |
| Team_Attributes.XCL_176 | team fifa api id / team fifa api identifier / fifa team id / fifa api team id / fifa team identifier / fifa id | integer | schema / Team_Attributes |
| Team_Attributes.XCL_177 | team api id / team api identifier / team id / api team id / team identifier | integer | schema / Team_Attributes |
| Team_Attributes.XCL_178 | date / attribute date / record date / snapshot date / timestamp | text | schema / Team_Attributes |
| Team_Attributes.XCL_179 | build up play speed / buildup speed / attack speed / speed rating | integer | schema / Team_Attributes |
| Team_Attributes.XCL_180 | build up play speed class / buildup speed category / speed classification / speed class | text | schema / Team_Attributes |
| Team_Attributes.XCL_181 | build up play dribbling / buildup dribbling / dribbling rating / dribbling | integer | schema / Team_Attributes |
| Team_Attributes.XCL_182 | build up play dribbling class / buildup dribbling category / dribbling classification / dribbling class | text | schema / Team_Attributes |
| Team_Attributes.XCL_183 | build up play passing / buildup passing / passing rating / passing | integer | schema / Team_Attributes |
| Team_Attributes.XCL_184 | build up play passing class / buildup passing category / passing classification / passing class | text | schema / Team_Attributes |
| Team_Attributes.XCL_185 | build up play positioning class / buildup positioning / positioning classification / positioning class | text | schema / Team_Attributes |
| Team_Attributes.XCL_186 | chance creation passing / chance creation passing rating / creative passing / passing in chance creation | integer | schema / Team_Attributes |
| Team_Attributes.XCL_187 | chance creation passing class / creative passing category / passing classification in chance creation / passing class | text | schema / Team_Attributes |
| Team_Attributes.XCL_188 | chance creation crossing / crossing rating / crossing in chance creation / creative crossing | integer | schema / Team_Attributes |
| Team_Attributes.XCL_189 | chance creation crossing class / crossing category / crossing classification / crossing class | text | schema / Team_Attributes |
| Team_Attributes.XCL_190 | chance creation shooting / shooting rating / shooting in chance creation / creative shooting | integer | schema / Team_Attributes |
| Team_Attributes.XCL_191 | chance creation shooting class / shooting category / shooting classification / shooting class | text | schema / Team_Attributes |
| Team_Attributes.XCL_192 | chance creation positioning class / creative positioning / positioning in chance creation / positioning class | text | schema / Team_Attributes |
| Team_Attributes.XCL_193 | defence pressure / defensive pressure / defence pressure rating / pressure rating | integer | schema / Team_Attributes |
| Team_Attributes.XCL_194 | defence pressure class / defensive pressure class / pressure category / pressure classification / pressure class | text | schema / Team_Attributes |
| Team_Attributes.XCL_195 | defence aggression / defensive aggression / defence aggression rating / aggression rating | integer | schema / Team_Attributes |
| Team_Attributes.XCL_196 | defence aggression class / defensive aggression class / aggression category / aggression classification / aggression class | text | schema / Team_Attributes |
| Team_Attributes.XCL_197 | defence team width / defensive team width / defence width rating / team width rating / defensive width | integer | schema / Team_Attributes |
| Team_Attributes.XCL_198 | defence team width class / defensive team width class / width category / width classification / width class | text | schema / Team_Attributes |
| Team_Attributes.XCL_199 | defence defender line class / defensive line class / defender line classification / defensive line type / defender line class | text | schema / Team_Attributes |

## Match

This table stores detailed information about each football match, including teams, scores, player lineups, match events, and betting odds from various bookmakers.

Recovered table names: match / matches / games / fixtures / soccer matches / football matches
SQL table aliases: M, m

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Match.XCL_006 | id / identifier / match id / match identifier / primary key | integer | schema / Match |
| Match.XCL_007 | country id / country identifier / nation id | integer | schema / Match |
| Match.XCL_008 | league id / league identifier / competition id | integer | schema / Match |
| Match.XCL_009 | season / season name / season label | text | schema / Match |
| Match.XCL_010 | stage / matchday / round / gameweek | integer | schema / Match |
| Match.XCL_011 | date / match date / game date / kickoff date | text | schema / Match |
| Match.XCL_012 | match api id / match api identifier / api match id / external match id | integer | schema / Match |
| Match.XCL_013 | home team api id / home team api identifier / home team id | integer | schema / Match |
| Match.XCL_014 | away team api id / away team api identifier / away team id | integer | schema / Match |
| Match.XCL_015 | home team goal / home goals / home score / home team goals | integer | schema / Match |
| Match.XCL_016 | away team goal / away goals / away score / away team goals | integer | schema / Match |
| Match.XCL_017 | home player x1 / home player 1 x coordinate / home player 1 position x | integer | schema / Match |
| Match.XCL_018 | home player x2 / home player 2 x coordinate / home player 2 position x | integer | schema / Match |
| Match.XCL_019 | home player x3 / home player 3 x coordinate / home player 3 position x | integer | schema / Match |
| Match.XCL_020 | home player x4 / home player 4 x coordinate / home player 4 position x | integer | schema / Match |
| Match.XCL_021 | home player x5 / home player 5 x coordinate / home player 5 position x | integer | schema / Match |
| Match.XCL_022 | home player x6 / home player 6 x coordinate / home player 6 position x | integer | schema / Match |
| Match.XCL_023 | home player x7 / home player 7 x coordinate / home player 7 position x | integer | schema / Match |
| Match.XCL_024 | home player x8 / home player 8 x coordinate / home player 8 position x | integer | schema / Match |
| Match.XCL_025 | home player x9 / home player 9 x coordinate / home player 9 position x | integer | schema / Match |
| Match.XCL_026 | home player x10 / home player 10 x coordinate / home player 10 position x | integer | schema / Match |
| Match.XCL_027 | home player x11 / home player 11 x coordinate / home player 11 position x | integer | schema / Match |
| Match.XCL_028 | away player x1 / away player 1 x coordinate / away player 1 position x | integer | schema / Match |
| Match.XCL_029 | away player x2 / away player 2 x coordinate / away player 2 position x | integer | schema / Match |
| Match.XCL_030 | away player x3 / away player 3 x coordinate / away player 3 position x | integer | schema / Match |
| Match.XCL_031 | away player x4 / away player 4 x coordinate / away player 4 position x | integer | schema / Match |
| Match.XCL_032 | away player x5 / away player 5 x coordinate / away player 5 position x | integer | schema / Match |
| Match.XCL_033 | away player x6 / away player 6 x coordinate / away player 6 position x | integer | schema / Match |
| Match.XCL_034 | away player x7 / away player 7 x coordinate / away player 7 position x | integer | schema / Match |
| Match.XCL_035 | away player x8 / away player 8 x coordinate / away player 8 position x | integer | schema / Match |
| Match.XCL_036 | away player x9 / away player 9 x coordinate / away player 9 position x | integer | schema / Match |
| Match.XCL_037 | away player x10 / away player 10 x coordinate / away player 10 position x | integer | schema / Match |
| Match.XCL_038 | away player x11 / away player 11 x coordinate / away player 11 position x | integer | schema / Match |
| Match.XCL_039 | home player y1 / home player 1 y coordinate / home player 1 position y | integer | schema / Match |
| Match.XCL_040 | home player y2 / home player 2 y coordinate / home player 2 position y | integer | schema / Match |
| Match.XCL_041 | home player y3 / home player 3 y coordinate / home player 3 position y | integer | schema / Match |
| Match.XCL_042 | home player y4 / home player 4 y coordinate / home player 4 position y | integer | schema / Match |
| Match.XCL_043 | home player y5 / home player 5 y coordinate / home player 5 position y | integer | schema / Match |
| Match.XCL_044 | home player y6 / home player 6 y coordinate / home player 6 position y | integer | schema / Match |
| Match.XCL_045 | home player y7 / home player 7 y coordinate / home player 7 position y | integer | schema / Match |
| Match.XCL_046 | home player y8 / home player 8 y coordinate / home player 8 position y | integer | schema / Match |
| Match.XCL_047 | home player y9 / home player 9 y coordinate / home player 9 position y | integer | schema / Match |
| Match.XCL_048 | home player y10 / home player 10 y coordinate / home player 10 position y | integer | schema / Match |
| Match.XCL_049 | home player y11 | integer | schema / Match |
| Match.XCL_050 | away player y1 | integer | schema / Match |
| Match.XCL_051 | away player y2 | integer | schema / Match |
| Match.XCL_052 | away player y3 | integer | schema / Match |
| Match.XCL_053 | away player y4 | integer | schema / Match |
| Match.XCL_054 | away player y5 | integer | schema / Match |
| Match.XCL_055 | away player y6 | integer | schema / Match |
| Match.XCL_056 | away player y7 | integer | schema / Match |
| Match.XCL_057 | away player y8 | integer | schema / Match |
| Match.XCL_058 | away player y9 | integer | schema / Match |
| Match.XCL_059 | away player y10 | integer | schema / Match |
| Match.XCL_060 | away player y11 | integer | schema / Match |
| Match.XCL_061 | home player 1 | integer | schema / Match |
| Match.XCL_062 | home player 2 | integer | schema / Match |
| Match.XCL_063 | home player 3 | integer | schema / Match |
| Match.XCL_064 | home player 4 | integer | schema / Match |
| Match.XCL_065 | home player 5 | integer | schema / Match |
| Match.XCL_066 | home player 6 | integer | schema / Match |
| Match.XCL_067 | home player 7 | integer | schema / Match |
| Match.XCL_068 | home player 8 | integer | schema / Match |
| Match.XCL_069 | home player 9 | integer | schema / Match |
| Match.XCL_070 | home player 10 | integer | schema / Match |
| Match.XCL_071 | home player 11 | integer | schema / Match |
| Match.XCL_072 | away player 1 | integer | schema / Match |
| Match.XCL_073 | away player 2 | integer | schema / Match |
| Match.XCL_074 | away player 3 | integer | schema / Match |
| Match.XCL_075 | away player 4 | integer | schema / Match |
| Match.XCL_076 | away player 5 | integer | schema / Match |
| Match.XCL_077 | away player 6 | integer | schema / Match |
| Match.XCL_078 | away player 7 | integer | schema / Match |
| Match.XCL_079 | away player 8 | integer | schema / Match |
| Match.XCL_080 | away player 9 | integer | schema / Match |
| Match.XCL_081 | away player 10 | integer | schema / Match |
| Match.XCL_082 | away player 11 | integer | schema / Match |
| Match.XCL_083 | goal | text | schema / Match |
| Match.XCL_084 | shoton | text | schema / Match |
| Match.XCL_085 | shotoff | text | schema / Match |
| Match.XCL_086 | foulcommit | text | schema / Match |
| Match.XCL_087 | card | text | schema / Match |
| Match.XCL_088 | cross | text | schema / Match |
| Match.XCL_089 | corner | text | schema / Match |
| Match.XCL_090 | possession | text | schema / Match |
| Match.XCL_091 | b365 h | real | schema / Match |
| Match.XCL_092 | b365 d | real | schema / Match |
| Match.XCL_093 | b365 a | real | schema / Match |
| Match.XCL_094 | bwh | real | schema / Match |
| Match.XCL_095 | bwd | real | schema / Match |
| Match.XCL_096 | bwa | real | schema / Match |
| Match.XCL_097 | iwh | real | schema / Match |
| Match.XCL_098 | iwd | real | schema / Match |
| Match.XCL_099 | iwa | real | schema / Match |
| Match.XCL_100 | lbh | real | schema / Match |
| Match.XCL_101 | lbd | real | schema / Match |
| Match.XCL_102 | lba | real | schema / Match |
| Match.XCL_103 | psh | real | schema / Match |
| Match.XCL_104 | psd | real | schema / Match |
| Match.XCL_105 | psa | real | schema / Match |
| Match.XCL_106 | whh | real | schema / Match |
| Match.XCL_107 | whd | real | schema / Match |
| Match.XCL_108 | wha | real | schema / Match |
| Match.XCL_109 | sjh | real | schema / Match |
| Match.XCL_110 | sjd | real | schema / Match |
| Match.XCL_111 | sja | real | schema / Match |
| Match.XCL_112 | vch | real | schema / Match |
| Match.XCL_113 | vcd | real | schema / Match |
| Match.XCL_114 | vca | real | schema / Match |
| Match.XCL_115 | gbh | real | schema / Match |
| Match.XCL_116 | gbd | real | schema / Match |
| Match.XCL_117 | gba | real | schema / Match |
| Match.XCL_118 | bsh | real | schema / Match |
| Match.XCL_119 | bsd | real | schema / Match |
| Match.XCL_120 | bsa | real | schema / Match |

## Relationships and join evidence

- Country.XCL_001 ↔ League.XCL_004; declared_or_materialized_relationship
- Match.XCL_013 ↔ Team.XCL_171; declared_or_materialized_relationship
- Match.XCL_014 ↔ Team.XCL_171; declared_or_materialized_relationship
- Match.XCL_061 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_062 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_063 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_064 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_065 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_066 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_067 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_068 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_069 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_070 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_071 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_072 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_073 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_074 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_075 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_076 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_077 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_078 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_079 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_080 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_081 ↔ Player.XCL_122; declared_or_materialized_relationship
- Match.XCL_082 ↔ Player.XCL_122; declared_or_materialized_relationship
- Player.XCL_122 ↔ Player_Attributes.XCL_130; declared_or_materialized_relationship
- Player.XCL_124 ↔ Player_Attributes.XCL_129; declared_or_materialized_relationship
- Team.XCL_171 ↔ Team_Attributes.XCL_177; declared_or_materialized_relationship
- Team.XCL_172 ↔ Team_Attributes.XCL_176; declared_or_materialized_relationship

## Business definitions, population and grain


## Incremental maintenance events

