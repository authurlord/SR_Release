# Spider2-Lite / delivery_center — Schema and business semantics

The saved catalogue for this database contains 7 tables, 59 physical columns, 0 relationships and 7 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## channels

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| channels.channel_id | Physical name retained; no saved recovered alias | INTEGER | schema / channels |
| channels.channel_name | Physical name retained; no saved recovered alias | VARCHAR(50) | schema / channels |
| channels.channel_type | Physical name retained; no saved recovered alias | VARCHAR(50) | schema / channels |

## deliveries

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: d, del

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| deliveries.delivery_id | Physical name retained; no saved recovered alias | INTEGER | schema / deliveries |
| deliveries.delivery_order_id | Physical name retained; no saved recovered alias | INTEGER | schema / deliveries |
| deliveries.driver_id | Physical name retained; no saved recovered alias | INTEGER | schema / deliveries |
| deliveries.delivery_distance_meters | Physical name retained; no saved recovered alias | DECIMAL(10, 2) | schema / deliveries |
| deliveries.delivery_status | Physical name retained; no saved recovered alias | VARCHAR(50) | schema / deliveries |

## drivers

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: d

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| drivers.driver_id | Physical name retained; no saved recovered alias | INTEGER | schema / drivers |
| drivers.driver_modal | Physical name retained; no saved recovered alias | VARCHAR(50) | schema / drivers |
| drivers.driver_type | Physical name retained; no saved recovered alias | VARCHAR(50) | schema / drivers |

## hubs

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: h

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| hubs.hub_id | Physical name retained; no saved recovered alias | INTEGER | schema / hubs |
| hubs.hub_name | Physical name retained; no saved recovered alias | VARCHAR(50) | schema / hubs |
| hubs.hub_city | Physical name retained; no saved recovered alias | VARCHAR(50) | schema / hubs |
| hubs.hub_state | Physical name retained; no saved recovered alias | CHAR(2) | schema / hubs |
| hubs.hub_latitude | Physical name retained; no saved recovered alias | DECIMAL(9, 6) | schema / hubs |
| hubs.hub_longitude | Physical name retained; no saved recovered alias | DECIMAL(9, 6) | schema / hubs |

## orders

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: o

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| orders.order_id | Physical name retained; no saved recovered alias | INTEGER | schema / orders |
| orders.store_id | Physical name retained; no saved recovered alias | INTEGER | schema / orders |
| orders.channel_id | Physical name retained; no saved recovered alias | INTEGER | schema / orders |
| orders.payment_order_id | Physical name retained; no saved recovered alias | INTEGER | schema / orders |
| orders.delivery_order_id | Physical name retained; no saved recovered alias | INTEGER | schema / orders |
| orders.order_status | Physical name retained; no saved recovered alias | VARCHAR(50) | schema / orders |
| orders.order_amount | Physical name retained; no saved recovered alias | DECIMAL(10, 2) | schema / orders |
| orders.order_delivery_fee | Physical name retained; no saved recovered alias | DECIMAL(10, 2) | schema / orders |
| orders.order_delivery_cost | Physical name retained; no saved recovered alias | DECIMAL(10, 2) | schema / orders |
| orders.order_created_hour | Physical name retained; no saved recovered alias | INTEGER | schema / orders |
| orders.order_created_minute | Physical name retained; no saved recovered alias | INTEGER | schema / orders |
| orders.order_created_day | Physical name retained; no saved recovered alias | INTEGER | schema / orders |
| orders.order_created_month | Physical name retained; no saved recovered alias | INTEGER | schema / orders |
| orders.order_created_year | Physical name retained; no saved recovered alias | INTEGER | schema / orders |
| orders.order_moment_created | Physical name retained; no saved recovered alias | DATETIME | schema / orders |
| orders.order_moment_accepted | Physical name retained; no saved recovered alias | DATETIME | schema / orders |
| orders.order_moment_ready | Physical name retained; no saved recovered alias | DATETIME | schema / orders |
| orders.order_moment_collected | Physical name retained; no saved recovered alias | DATETIME | schema / orders |
| orders.order_moment_in_expedition | Physical name retained; no saved recovered alias | DATETIME | schema / orders |
| orders.order_moment_delivering | Physical name retained; no saved recovered alias | DATETIME | schema / orders |
| orders.order_moment_delivered | Physical name retained; no saved recovered alias | DATETIME | schema / orders |
| orders.order_moment_finished | Physical name retained; no saved recovered alias | DATETIME | schema / orders |
| orders.order_metric_collected_time | Physical name retained; no saved recovered alias | DECIMAL(10, 2) | schema / orders |
| orders.order_metric_paused_time | Physical name retained; no saved recovered alias | DECIMAL(10, 2) | schema / orders |
| orders.order_metric_production_time | Physical name retained; no saved recovered alias | DECIMAL(10, 2) | schema / orders |
| orders.order_metric_walking_time | Physical name retained; no saved recovered alias | DECIMAL(10, 2) | schema / orders |
| orders.order_metric_expediton_speed_time | Physical name retained; no saved recovered alias | DECIMAL(10, 2) | schema / orders |
| orders.order_metric_transit_time | Physical name retained; no saved recovered alias | DECIMAL(10, 2) | schema / orders |
| orders.order_metric_cycle_time | Physical name retained; no saved recovered alias | DECIMAL(10, 2) | schema / orders |

## payments

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| payments.payment_id | Physical name retained; no saved recovered alias | INTEGER | schema / payments |
| payments.payment_order_id | Physical name retained; no saved recovered alias | INTEGER | schema / payments |
| payments.payment_amount | Physical name retained; no saved recovered alias | DECIMAL(10, 2) | schema / payments |
| payments.payment_fee | Physical name retained; no saved recovered alias | DECIMAL(10, 2) | schema / payments |
| payments.payment_method | Physical name retained; no saved recovered alias | VARCHAR(50) | schema / payments |
| payments.payment_status | Physical name retained; no saved recovered alias | VARCHAR(50) | schema / payments |

## stores

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: s

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| stores.store_id | Physical name retained; no saved recovered alias | INTEGER | schema / stores |
| stores.hub_id | Physical name retained; no saved recovered alias | INTEGER | schema / stores |
| stores.store_name | Physical name retained; no saved recovered alias | VARCHAR(50) | schema / stores |
| stores.store_segment | Physical name retained; no saved recovered alias | VARCHAR(50) | schema / stores |
| stores.store_plan_price | Physical name retained; no saved recovered alias | DECIMAL(10, 2) | schema / stores |
| stores.store_latitude | Physical name retained; no saved recovered alias | DECIMAL(9, 6) | schema / stores |
| stores.store_longitude | Physical name retained; no saved recovered alias | DECIMAL(9, 6) | schema / stores |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

