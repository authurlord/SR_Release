# Spider2-Lite / Db-IMDB — Schema and business semantics

The saved catalogue for this database contains 13 tables, 50 physical columns, 0 relationships and 13 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## Country

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Country.index | Physical name retained; no saved recovered alias | INTEGER | schema / Country |
| Country.Name | Physical name retained; no saved recovered alias | TEXT | schema / Country |
| Country.CID | Physical name retained; no saved recovered alias | INTEGER | schema / Country |

## Genre

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Genre.index | Physical name retained; no saved recovered alias | INTEGER | schema / Genre |
| Genre.Name | Physical name retained; no saved recovered alias | TEXT | schema / Genre |
| Genre.GID | Physical name retained; no saved recovered alias | INTEGER | schema / Genre |

## Language

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Language.index | Physical name retained; no saved recovered alias | INTEGER | schema / Language |
| Language.Name | Physical name retained; no saved recovered alias | TEXT | schema / Language |
| Language.LAID | Physical name retained; no saved recovered alias | INTEGER | schema / Language |

## Location

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Location.index | Physical name retained; no saved recovered alias | INTEGER | schema / Location |
| Location.Name | Physical name retained; no saved recovered alias | TEXT | schema / Location |
| Location.LID | Physical name retained; no saved recovered alias | INTEGER | schema / Location |

## M_Cast

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: c

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| M_Cast.index | Physical name retained; no saved recovered alias | INTEGER | schema / M_Cast |
| M_Cast.MID | Physical name retained; no saved recovered alias | TEXT | schema / M_Cast |
| M_Cast.PID | Physical name retained; no saved recovered alias | TEXT | schema / M_Cast |
| M_Cast.ID | Physical name retained; no saved recovered alias | INTEGER | schema / M_Cast |

## M_Country

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| M_Country.index | Physical name retained; no saved recovered alias | INTEGER | schema / M_Country |
| M_Country.MID | Physical name retained; no saved recovered alias | TEXT | schema / M_Country |
| M_Country.CID | Physical name retained; no saved recovered alias | REAL | schema / M_Country |
| M_Country.ID | Physical name retained; no saved recovered alias | INTEGER | schema / M_Country |

## M_Director

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: d

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| M_Director.index | Physical name retained; no saved recovered alias | INTEGER | schema / M_Director |
| M_Director.MID | Physical name retained; no saved recovered alias | TEXT | schema / M_Director |
| M_Director.PID | Physical name retained; no saved recovered alias | TEXT | schema / M_Director |
| M_Director.ID | Physical name retained; no saved recovered alias | INTEGER | schema / M_Director |

## M_Genre

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| M_Genre.index | Physical name retained; no saved recovered alias | INTEGER | schema / M_Genre |
| M_Genre.MID | Physical name retained; no saved recovered alias | TEXT | schema / M_Genre |
| M_Genre.GID | Physical name retained; no saved recovered alias | INTEGER | schema / M_Genre |
| M_Genre.ID | Physical name retained; no saved recovered alias | INTEGER | schema / M_Genre |

## M_Language

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| M_Language.index | Physical name retained; no saved recovered alias | INTEGER | schema / M_Language |
| M_Language.MID | Physical name retained; no saved recovered alias | TEXT | schema / M_Language |
| M_Language.LAID | Physical name retained; no saved recovered alias | INTEGER | schema / M_Language |
| M_Language.ID | Physical name retained; no saved recovered alias | INTEGER | schema / M_Language |

## M_Location

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| M_Location.index | Physical name retained; no saved recovered alias | INTEGER | schema / M_Location |
| M_Location.MID | Physical name retained; no saved recovered alias | TEXT | schema / M_Location |
| M_Location.LID | Physical name retained; no saved recovered alias | REAL | schema / M_Location |
| M_Location.ID | Physical name retained; no saved recovered alias | INTEGER | schema / M_Location |

## M_Producer

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| M_Producer.index | Physical name retained; no saved recovered alias | INTEGER | schema / M_Producer |
| M_Producer.MID | Physical name retained; no saved recovered alias | TEXT | schema / M_Producer |
| M_Producer.PID | Physical name retained; no saved recovered alias | TEXT | schema / M_Producer |
| M_Producer.ID | Physical name retained; no saved recovered alias | INTEGER | schema / M_Producer |

## Movie

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: m

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Movie.index | Physical name retained; no saved recovered alias | INTEGER | schema / Movie |
| Movie.MID | Physical name retained; no saved recovered alias | TEXT | schema / Movie |
| Movie.title | Physical name retained; no saved recovered alias | TEXT | schema / Movie |
| Movie.year | Physical name retained; no saved recovered alias | TEXT | schema / Movie |
| Movie.rating | Physical name retained; no saved recovered alias | REAL | schema / Movie |
| Movie.num_votes | Physical name retained; no saved recovered alias | INTEGER | schema / Movie |

## Person

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: p

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Person.index | Physical name retained; no saved recovered alias | INTEGER | schema / Person |
| Person.PID | Physical name retained; no saved recovered alias | TEXT | schema / Person |
| Person.Name | Physical name retained; no saved recovered alias | TEXT | schema / Person |
| Person.Gender | Physical name retained; no saved recovered alias | TEXT | schema / Person |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

