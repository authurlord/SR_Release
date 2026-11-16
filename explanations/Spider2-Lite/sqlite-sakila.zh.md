# Spider2-Lite / sqlite-sakila — Schema 与业务口径解释

该数据库的存档目录包含 16 张表、89 个物理列、0 条关系，以及 16 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## actor

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: a

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| actor.actor_id | 保留物理名称；存档没有恢复别名 | numeric | schema / actor |
| actor.first_name | 保留物理名称；存档没有恢复别名 | VARCHAR(45) | schema / actor |
| actor.last_name | 保留物理名称；存档没有恢复别名 | VARCHAR(45) | schema / actor |
| actor.last_update | 保留物理名称；存档没有恢复别名 | TIMESTAMP | schema / actor |

## address

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| address.address_id | 保留物理名称；存档没有恢复别名 | INT | schema / address |
| address.address | 保留物理名称；存档没有恢复别名 | VARCHAR(50) | schema / address |
| address.address2 | 保留物理名称；存档没有恢复别名 | VARCHAR(50) | schema / address |
| address.district | 保留物理名称；存档没有恢复别名 | VARCHAR(20) | schema / address |
| address.city_id | 保留物理名称；存档没有恢复别名 | INT | schema / address |
| address.postal_code | 保留物理名称；存档没有恢复别名 | VARCHAR(10) | schema / address |
| address.phone | 保留物理名称；存档没有恢复别名 | VARCHAR(20) | schema / address |
| address.last_update | 保留物理名称；存档没有恢复别名 | TIMESTAMP | schema / address |

## category

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| category.category_id | 保留物理名称；存档没有恢复别名 | SMALLINT | schema / category |
| category.name | 保留物理名称；存档没有恢复别名 | VARCHAR(25) | schema / category |
| category.last_update | 保留物理名称；存档没有恢复别名 | TIMESTAMP | schema / category |

## city

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| city.city_id | 保留物理名称；存档没有恢复别名 | INT | schema / city |
| city.city | 保留物理名称；存档没有恢复别名 | VARCHAR(50) | schema / city |
| city.country_id | 保留物理名称；存档没有恢复别名 | SMALLINT | schema / city |
| city.last_update | 保留物理名称；存档没有恢复别名 | TIMESTAMP | schema / city |

## country

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| country.country_id | 保留物理名称；存档没有恢复别名 | SMALLINT | schema / country |
| country.country | 保留物理名称；存档没有恢复别名 | VARCHAR(50) | schema / country |
| country.last_update | 保留物理名称；存档没有恢复别名 | TIMESTAMP | schema / country |

## customer

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: c

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| customer.customer_id | 保留物理名称；存档没有恢复别名 | INT | schema / customer |
| customer.store_id | 保留物理名称；存档没有恢复别名 | INT | schema / customer |
| customer.first_name | 保留物理名称；存档没有恢复别名 | VARCHAR(45) | schema / customer |
| customer.last_name | 保留物理名称；存档没有恢复别名 | VARCHAR(45) | schema / customer |
| customer.email | 保留物理名称；存档没有恢复别名 | VARCHAR(50) | schema / customer |
| customer.address_id | 保留物理名称；存档没有恢复别名 | INT | schema / customer |
| customer.active | 保留物理名称；存档没有恢复别名 | CHAR(1) | schema / customer |
| customer.create_date | 保留物理名称；存档没有恢复别名 | TIMESTAMP | schema / customer |
| customer.last_update | 保留物理名称；存档没有恢复别名 | TIMESTAMP | schema / customer |

## film

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: f

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| film.film_id | 保留物理名称；存档没有恢复别名 | INT | schema / film |
| film.title | 保留物理名称；存档没有恢复别名 | VARCHAR(255) | schema / film |
| film.description | 保留物理名称；存档没有恢复别名 | BLOB SUB_TYPE TEXT | schema / film |
| film.release_year | 保留物理名称；存档没有恢复别名 | VARCHAR(4) | schema / film |
| film.language_id | 保留物理名称；存档没有恢复别名 | SMALLINT | schema / film |
| film.original_language_id | 保留物理名称；存档没有恢复别名 | SMALLINT | schema / film |
| film.rental_duration | 保留物理名称；存档没有恢复别名 | SMALLINT | schema / film |
| film.rental_rate | 保留物理名称；存档没有恢复别名 | DECIMAL(4,2) | schema / film |
| film.length | 保留物理名称；存档没有恢复别名 | SMALLINT | schema / film |
| film.replacement_cost | 保留物理名称；存档没有恢复别名 | DECIMAL(5,2) | schema / film |
| film.rating | 保留物理名称；存档没有恢复别名 | VARCHAR(10) | schema / film |
| film.special_features | 保留物理名称；存档没有恢复别名 | VARCHAR(100) | schema / film |
| film.last_update | 保留物理名称；存档没有恢复别名 | TIMESTAMP | schema / film |

## film_actor

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: fa

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| film_actor.actor_id | 保留物理名称；存档没有恢复别名 | INT | schema / film_actor |
| film_actor.film_id | 保留物理名称；存档没有恢复别名 | INT | schema / film_actor |
| film_actor.last_update | 保留物理名称；存档没有恢复别名 | TIMESTAMP | schema / film_actor |

## film_category

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| film_category.film_id | 保留物理名称；存档没有恢复别名 | INT | schema / film_category |
| film_category.category_id | 保留物理名称；存档没有恢复别名 | SMALLINT | schema / film_category |
| film_category.last_update | 保留物理名称；存档没有恢复别名 | TIMESTAMP | schema / film_category |

## film_text

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| film_text.film_id | 保留物理名称；存档没有恢复别名 | SMALLINT | schema / film_text |
| film_text.title | 保留物理名称；存档没有恢复别名 | VARCHAR(255) | schema / film_text |
| film_text.description | 保留物理名称；存档没有恢复别名 | BLOB SUB_TYPE TEXT | schema / film_text |

## inventory

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: i

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| inventory.inventory_id | 保留物理名称；存档没有恢复别名 | INT | schema / inventory |
| inventory.film_id | 保留物理名称；存档没有恢复别名 | INT | schema / inventory |
| inventory.store_id | 保留物理名称；存档没有恢复别名 | INT | schema / inventory |
| inventory.last_update | 保留物理名称；存档没有恢复别名 | TIMESTAMP | schema / inventory |

## language

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| language.language_id | 保留物理名称；存档没有恢复别名 | SMALLINT | schema / language |
| language.name | 保留物理名称；存档没有恢复别名 | CHAR(20) | schema / language |
| language.last_update | 保留物理名称；存档没有恢复别名 | TIMESTAMP | schema / language |

## payment

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: p

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| payment.payment_id | 保留物理名称；存档没有恢复别名 | INT | schema / payment |
| payment.customer_id | 保留物理名称；存档没有恢复别名 | INT | schema / payment |
| payment.staff_id | 保留物理名称；存档没有恢复别名 | SMALLINT | schema / payment |
| payment.rental_id | 保留物理名称；存档没有恢复别名 | INT | schema / payment |
| payment.amount | 保留物理名称；存档没有恢复别名 | DECIMAL(5,2) | schema / payment |
| payment.payment_date | 保留物理名称；存档没有恢复别名 | TIMESTAMP | schema / payment |
| payment.last_update | 保留物理名称；存档没有恢复别名 | TIMESTAMP | schema / payment |

## rental

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: r

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| rental.rental_id | 保留物理名称；存档没有恢复别名 | INT | schema / rental |
| rental.rental_date | 保留物理名称；存档没有恢复别名 | TIMESTAMP | schema / rental |
| rental.inventory_id | 保留物理名称；存档没有恢复别名 | INT | schema / rental |
| rental.customer_id | 保留物理名称；存档没有恢复别名 | INT | schema / rental |
| rental.return_date | 保留物理名称；存档没有恢复别名 | TIMESTAMP | schema / rental |
| rental.staff_id | 保留物理名称；存档没有恢复别名 | SMALLINT | schema / rental |
| rental.last_update | 保留物理名称；存档没有恢复别名 | TIMESTAMP | schema / rental |

## staff

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: st

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| staff.staff_id | 保留物理名称；存档没有恢复别名 | SMALLINT | schema / staff |
| staff.first_name | 保留物理名称；存档没有恢复别名 | VARCHAR(45) | schema / staff |
| staff.last_name | 保留物理名称；存档没有恢复别名 | VARCHAR(45) | schema / staff |
| staff.address_id | 保留物理名称；存档没有恢复别名 | INT | schema / staff |
| staff.picture | 保留物理名称；存档没有恢复别名 | BLOB | schema / staff |
| staff.email | 保留物理名称；存档没有恢复别名 | VARCHAR(50) | schema / staff |
| staff.store_id | 保留物理名称；存档没有恢复别名 | INT | schema / staff |
| staff.active | 保留物理名称；存档没有恢复别名 | SMALLINT | schema / staff |
| staff.username | 保留物理名称；存档没有恢复别名 | VARCHAR(16) | schema / staff |
| staff.password | 保留物理名称；存档没有恢复别名 | VARCHAR(40) | schema / staff |
| staff.last_update | 保留物理名称；存档没有恢复别名 | TIMESTAMP | schema / staff |

## store

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: s

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| store.store_id | 保留物理名称；存档没有恢复别名 | INT | schema / store |
| store.manager_staff_id | 保留物理名称；存档没有恢复别名 | SMALLINT | schema / store |
| store.address_id | 保留物理名称；存档没有恢复别名 | INT | schema / store |
| store.last_update | 保留物理名称；存档没有恢复别名 | TIMESTAMP | schema / store |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

