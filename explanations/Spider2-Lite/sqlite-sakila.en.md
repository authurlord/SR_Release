# Spider2-Lite / sqlite-sakila — Schema and business semantics

The saved catalogue for this database contains 16 tables, 89 physical columns, 0 relationships and 16 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## actor

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: a

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| actor.actor_id | Physical name retained; no saved recovered alias | numeric | schema / actor |
| actor.first_name | Physical name retained; no saved recovered alias | VARCHAR(45) | schema / actor |
| actor.last_name | Physical name retained; no saved recovered alias | VARCHAR(45) | schema / actor |
| actor.last_update | Physical name retained; no saved recovered alias | TIMESTAMP | schema / actor |

## address

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| address.address_id | Physical name retained; no saved recovered alias | INT | schema / address |
| address.address | Physical name retained; no saved recovered alias | VARCHAR(50) | schema / address |
| address.address2 | Physical name retained; no saved recovered alias | VARCHAR(50) | schema / address |
| address.district | Physical name retained; no saved recovered alias | VARCHAR(20) | schema / address |
| address.city_id | Physical name retained; no saved recovered alias | INT | schema / address |
| address.postal_code | Physical name retained; no saved recovered alias | VARCHAR(10) | schema / address |
| address.phone | Physical name retained; no saved recovered alias | VARCHAR(20) | schema / address |
| address.last_update | Physical name retained; no saved recovered alias | TIMESTAMP | schema / address |

## category

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| category.category_id | Physical name retained; no saved recovered alias | SMALLINT | schema / category |
| category.name | Physical name retained; no saved recovered alias | VARCHAR(25) | schema / category |
| category.last_update | Physical name retained; no saved recovered alias | TIMESTAMP | schema / category |

## city

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| city.city_id | Physical name retained; no saved recovered alias | INT | schema / city |
| city.city | Physical name retained; no saved recovered alias | VARCHAR(50) | schema / city |
| city.country_id | Physical name retained; no saved recovered alias | SMALLINT | schema / city |
| city.last_update | Physical name retained; no saved recovered alias | TIMESTAMP | schema / city |

## country

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| country.country_id | Physical name retained; no saved recovered alias | SMALLINT | schema / country |
| country.country | Physical name retained; no saved recovered alias | VARCHAR(50) | schema / country |
| country.last_update | Physical name retained; no saved recovered alias | TIMESTAMP | schema / country |

## customer

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: c

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| customer.customer_id | Physical name retained; no saved recovered alias | INT | schema / customer |
| customer.store_id | Physical name retained; no saved recovered alias | INT | schema / customer |
| customer.first_name | Physical name retained; no saved recovered alias | VARCHAR(45) | schema / customer |
| customer.last_name | Physical name retained; no saved recovered alias | VARCHAR(45) | schema / customer |
| customer.email | Physical name retained; no saved recovered alias | VARCHAR(50) | schema / customer |
| customer.address_id | Physical name retained; no saved recovered alias | INT | schema / customer |
| customer.active | Physical name retained; no saved recovered alias | CHAR(1) | schema / customer |
| customer.create_date | Physical name retained; no saved recovered alias | TIMESTAMP | schema / customer |
| customer.last_update | Physical name retained; no saved recovered alias | TIMESTAMP | schema / customer |

## film

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: f

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| film.film_id | Physical name retained; no saved recovered alias | INT | schema / film |
| film.title | Physical name retained; no saved recovered alias | VARCHAR(255) | schema / film |
| film.description | Physical name retained; no saved recovered alias | BLOB SUB_TYPE TEXT | schema / film |
| film.release_year | Physical name retained; no saved recovered alias | VARCHAR(4) | schema / film |
| film.language_id | Physical name retained; no saved recovered alias | SMALLINT | schema / film |
| film.original_language_id | Physical name retained; no saved recovered alias | SMALLINT | schema / film |
| film.rental_duration | Physical name retained; no saved recovered alias | SMALLINT | schema / film |
| film.rental_rate | Physical name retained; no saved recovered alias | DECIMAL(4,2) | schema / film |
| film.length | Physical name retained; no saved recovered alias | SMALLINT | schema / film |
| film.replacement_cost | Physical name retained; no saved recovered alias | DECIMAL(5,2) | schema / film |
| film.rating | Physical name retained; no saved recovered alias | VARCHAR(10) | schema / film |
| film.special_features | Physical name retained; no saved recovered alias | VARCHAR(100) | schema / film |
| film.last_update | Physical name retained; no saved recovered alias | TIMESTAMP | schema / film |

## film_actor

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: fa

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| film_actor.actor_id | Physical name retained; no saved recovered alias | INT | schema / film_actor |
| film_actor.film_id | Physical name retained; no saved recovered alias | INT | schema / film_actor |
| film_actor.last_update | Physical name retained; no saved recovered alias | TIMESTAMP | schema / film_actor |

## film_category

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| film_category.film_id | Physical name retained; no saved recovered alias | INT | schema / film_category |
| film_category.category_id | Physical name retained; no saved recovered alias | SMALLINT | schema / film_category |
| film_category.last_update | Physical name retained; no saved recovered alias | TIMESTAMP | schema / film_category |

## film_text

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| film_text.film_id | Physical name retained; no saved recovered alias | SMALLINT | schema / film_text |
| film_text.title | Physical name retained; no saved recovered alias | VARCHAR(255) | schema / film_text |
| film_text.description | Physical name retained; no saved recovered alias | BLOB SUB_TYPE TEXT | schema / film_text |

## inventory

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: i

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| inventory.inventory_id | Physical name retained; no saved recovered alias | INT | schema / inventory |
| inventory.film_id | Physical name retained; no saved recovered alias | INT | schema / inventory |
| inventory.store_id | Physical name retained; no saved recovered alias | INT | schema / inventory |
| inventory.last_update | Physical name retained; no saved recovered alias | TIMESTAMP | schema / inventory |

## language

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| language.language_id | Physical name retained; no saved recovered alias | SMALLINT | schema / language |
| language.name | Physical name retained; no saved recovered alias | CHAR(20) | schema / language |
| language.last_update | Physical name retained; no saved recovered alias | TIMESTAMP | schema / language |

## payment

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: p

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| payment.payment_id | Physical name retained; no saved recovered alias | INT | schema / payment |
| payment.customer_id | Physical name retained; no saved recovered alias | INT | schema / payment |
| payment.staff_id | Physical name retained; no saved recovered alias | SMALLINT | schema / payment |
| payment.rental_id | Physical name retained; no saved recovered alias | INT | schema / payment |
| payment.amount | Physical name retained; no saved recovered alias | DECIMAL(5,2) | schema / payment |
| payment.payment_date | Physical name retained; no saved recovered alias | TIMESTAMP | schema / payment |
| payment.last_update | Physical name retained; no saved recovered alias | TIMESTAMP | schema / payment |

## rental

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: r

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| rental.rental_id | Physical name retained; no saved recovered alias | INT | schema / rental |
| rental.rental_date | Physical name retained; no saved recovered alias | TIMESTAMP | schema / rental |
| rental.inventory_id | Physical name retained; no saved recovered alias | INT | schema / rental |
| rental.customer_id | Physical name retained; no saved recovered alias | INT | schema / rental |
| rental.return_date | Physical name retained; no saved recovered alias | TIMESTAMP | schema / rental |
| rental.staff_id | Physical name retained; no saved recovered alias | SMALLINT | schema / rental |
| rental.last_update | Physical name retained; no saved recovered alias | TIMESTAMP | schema / rental |

## staff

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: st

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| staff.staff_id | Physical name retained; no saved recovered alias | SMALLINT | schema / staff |
| staff.first_name | Physical name retained; no saved recovered alias | VARCHAR(45) | schema / staff |
| staff.last_name | Physical name retained; no saved recovered alias | VARCHAR(45) | schema / staff |
| staff.address_id | Physical name retained; no saved recovered alias | INT | schema / staff |
| staff.picture | Physical name retained; no saved recovered alias | BLOB | schema / staff |
| staff.email | Physical name retained; no saved recovered alias | VARCHAR(50) | schema / staff |
| staff.store_id | Physical name retained; no saved recovered alias | INT | schema / staff |
| staff.active | Physical name retained; no saved recovered alias | SMALLINT | schema / staff |
| staff.username | Physical name retained; no saved recovered alias | VARCHAR(16) | schema / staff |
| staff.password | Physical name retained; no saved recovered alias | VARCHAR(40) | schema / staff |
| staff.last_update | Physical name retained; no saved recovered alias | TIMESTAMP | schema / staff |

## store

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: s

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| store.store_id | Physical name retained; no saved recovered alias | INT | schema / store |
| store.manager_staff_id | Physical name retained; no saved recovered alias | SMALLINT | schema / store |
| store.address_id | Physical name retained; no saved recovered alias | INT | schema / store |
| store.last_update | Physical name retained; no saved recovered alias | TIMESTAMP | schema / store |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

