# Spider2-Lite / imdb_movies — Schema and business semantics

The saved catalogue for this database contains 7 tables, 38 physical columns, 0 relationships and 7 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## ERD

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| ERD.table | Physical name retained; no saved recovered alias | TEXT | schema / ERD |
| ERD.column | Physical name retained; no saved recovered alias | TEXT | schema / ERD |
| ERD.Unnamed: 2 | Physical name retained; no saved recovered alias | REAL | schema / ERD |
| ERD.Unnamed: 3 | Physical name retained; no saved recovered alias | REAL | schema / ERD |
| ERD.Unnamed: 4 | Physical name retained; no saved recovered alias | REAL | schema / ERD |
| ERD.Unnamed: 5 | Physical name retained; no saved recovered alias | REAL | schema / ERD |
| ERD.Unnamed: 6 | Physical name retained; no saved recovered alias | TEXT | schema / ERD |
| ERD.Unnamed: 7 | Physical name retained; no saved recovered alias | REAL | schema / ERD |
| ERD.Unnamed: 8 | Physical name retained; no saved recovered alias | REAL | schema / ERD |
| ERD.Unnamed: 9 | Physical name retained; no saved recovered alias | TEXT | schema / ERD |
| ERD.Unnamed: 10 | Physical name retained; no saved recovered alias | REAL | schema / ERD |
| ERD.Unnamed: 11 | Physical name retained; no saved recovered alias | REAL | schema / ERD |
| ERD.Unnamed: 12 | Physical name retained; no saved recovered alias | TEXT | schema / ERD |

## director_mapping

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: dm

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| director_mapping.movie_id | Physical name retained; no saved recovered alias | TEXT | schema / director_mapping |
| director_mapping.name_id | Physical name retained; no saved recovered alias | TEXT | schema / director_mapping |

## genre

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: g

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| genre.movie_id | Physical name retained; no saved recovered alias | TEXT | schema / genre |
| genre.genre | Physical name retained; no saved recovered alias | TEXT | schema / genre |

## movies

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: m

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| movies.id | Physical name retained; no saved recovered alias | TEXT | schema / movies |
| movies.title | Physical name retained; no saved recovered alias | TEXT | schema / movies |
| movies.year | Physical name retained; no saved recovered alias | INTEGER | schema / movies |
| movies.date_published | Physical name retained; no saved recovered alias | TIMESTAMP | schema / movies |
| movies.duration | Physical name retained; no saved recovered alias | INTEGER | schema / movies |
| movies.country | Physical name retained; no saved recovered alias | TEXT | schema / movies |
| movies.worlwide_gross_income | Physical name retained; no saved recovered alias | TEXT | schema / movies |
| movies.languages | Physical name retained; no saved recovered alias | TEXT | schema / movies |
| movies.production_company | Physical name retained; no saved recovered alias | TEXT | schema / movies |

## names

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: n

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| names.id | Physical name retained; no saved recovered alias | TEXT | schema / names |
| names.name | Physical name retained; no saved recovered alias | TEXT | schema / names |
| names.height | Physical name retained; no saved recovered alias | REAL | schema / names |
| names.date_of_birth | Physical name retained; no saved recovered alias | TEXT | schema / names |
| names.known_for_movies | Physical name retained; no saved recovered alias | TEXT | schema / names |

## ratings

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: r

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| ratings.movie_id | Physical name retained; no saved recovered alias | TEXT | schema / ratings |
| ratings.avg_rating | Physical name retained; no saved recovered alias | REAL | schema / ratings |
| ratings.total_votes | Physical name retained; no saved recovered alias | INTEGER | schema / ratings |
| ratings.median_rating | Physical name retained; no saved recovered alias | REAL | schema / ratings |

## role_mapping

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| role_mapping.movie_id | Physical name retained; no saved recovered alias | TEXT | schema / role_mapping |
| role_mapping.name_id | Physical name retained; no saved recovered alias | TEXT | schema / role_mapping |
| role_mapping.category | Physical name retained; no saved recovered alias | TEXT | schema / role_mapping |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

