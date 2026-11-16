# Spider2-Lite / Airlines — Schema and business semantics

The saved catalogue for this database contains 8 tables, 35 physical columns, 0 relationships and 8 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## aircrafts_data

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| aircrafts_data.aircraft_code | Physical name retained; no saved recovered alias | character(3) | schema / aircrafts_data |
| aircrafts_data.model | Physical name retained; no saved recovered alias | jsonb | schema / aircrafts_data |
| aircrafts_data.range | Physical name retained; no saved recovered alias | INTEGER | schema / aircrafts_data |

## airports_data

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| airports_data.airport_code | Physical name retained; no saved recovered alias | character(3) | schema / airports_data |
| airports_data.airport_name | Physical name retained; no saved recovered alias | jsonb | schema / airports_data |
| airports_data.city | Physical name retained; no saved recovered alias | jsonb | schema / airports_data |
| airports_data.coordinates | Physical name retained; no saved recovered alias | point | schema / airports_data |
| airports_data.timezone | Physical name retained; no saved recovered alias | TEXT | schema / airports_data |

## boarding_passes

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| boarding_passes.ticket_no | Physical name retained; no saved recovered alias | character(13) | schema / boarding_passes |
| boarding_passes.flight_id | Physical name retained; no saved recovered alias | INTEGER | schema / boarding_passes |
| boarding_passes.boarding_no | Physical name retained; no saved recovered alias | INTEGER | schema / boarding_passes |
| boarding_passes.seat_no | Physical name retained; no saved recovered alias | character varying(4) | schema / boarding_passes |

## bookings

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| bookings.book_ref | Physical name retained; no saved recovered alias | character(6) | schema / bookings |
| bookings.book_date | Physical name retained; no saved recovered alias | timestamp with time zone | schema / bookings |
| bookings.total_amount | Physical name retained; no saved recovered alias | numeric(10,2) | schema / bookings |

## flights

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: f

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| flights.flight_id | Physical name retained; no saved recovered alias | INTEGER | schema / flights |
| flights.flight_no | Physical name retained; no saved recovered alias | character(6) | schema / flights |
| flights.scheduled_departure | Physical name retained; no saved recovered alias | timestamp with time zone | schema / flights |
| flights.scheduled_arrival | Physical name retained; no saved recovered alias | timestamp with time zone | schema / flights |
| flights.departure_airport | Physical name retained; no saved recovered alias | character(3) | schema / flights |
| flights.arrival_airport | Physical name retained; no saved recovered alias | character(3) | schema / flights |
| flights.status | Physical name retained; no saved recovered alias | character varying(20) | schema / flights |
| flights.aircraft_code | Physical name retained; no saved recovered alias | character(3) | schema / flights |
| flights.actual_departure | Physical name retained; no saved recovered alias | timestamp with time zone | schema / flights |
| flights.actual_arrival | Physical name retained; no saved recovered alias | timestamp with time zone | schema / flights |

## seats

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| seats.aircraft_code | Physical name retained; no saved recovered alias | character(3) | schema / seats |
| seats.seat_no | Physical name retained; no saved recovered alias | character varying(4) | schema / seats |
| seats.fare_conditions | Physical name retained; no saved recovered alias | character varying(10) | schema / seats |

## ticket_flights

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| ticket_flights.ticket_no | Physical name retained; no saved recovered alias | character(13) | schema / ticket_flights |
| ticket_flights.flight_id | Physical name retained; no saved recovered alias | INTEGER | schema / ticket_flights |
| ticket_flights.fare_conditions | Physical name retained; no saved recovered alias | character varying(10) | schema / ticket_flights |
| ticket_flights.amount | Physical name retained; no saved recovered alias | numeric(10,2) | schema / ticket_flights |

## tickets

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| tickets.ticket_no | Physical name retained; no saved recovered alias | character(13) | schema / tickets |
| tickets.book_ref | Physical name retained; no saved recovered alias | character(6) | schema / tickets |
| tickets.passenger_id | Physical name retained; no saved recovered alias | character varying(20) | schema / tickets |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

