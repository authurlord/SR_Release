# Spider2-Lite / delivery_center — Schema 与业务口径解释

该数据库的存档目录包含 7 张表、59 个物理列、0 条关系，以及 7 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## channels

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| channels.channel_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / channels |
| channels.channel_name | 保留物理名称；存档没有恢复别名 | VARCHAR(50) | schema / channels |
| channels.channel_type | 保留物理名称；存档没有恢复别名 | VARCHAR(50) | schema / channels |

## deliveries

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: d, del

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| deliveries.delivery_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / deliveries |
| deliveries.delivery_order_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / deliveries |
| deliveries.driver_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / deliveries |
| deliveries.delivery_distance_meters | 保留物理名称；存档没有恢复别名 | DECIMAL(10, 2) | schema / deliveries |
| deliveries.delivery_status | 保留物理名称；存档没有恢复别名 | VARCHAR(50) | schema / deliveries |

## drivers

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: d

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| drivers.driver_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / drivers |
| drivers.driver_modal | 保留物理名称；存档没有恢复别名 | VARCHAR(50) | schema / drivers |
| drivers.driver_type | 保留物理名称；存档没有恢复别名 | VARCHAR(50) | schema / drivers |

## hubs

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: h

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| hubs.hub_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / hubs |
| hubs.hub_name | 保留物理名称；存档没有恢复别名 | VARCHAR(50) | schema / hubs |
| hubs.hub_city | 保留物理名称；存档没有恢复别名 | VARCHAR(50) | schema / hubs |
| hubs.hub_state | 保留物理名称；存档没有恢复别名 | CHAR(2) | schema / hubs |
| hubs.hub_latitude | 保留物理名称；存档没有恢复别名 | DECIMAL(9, 6) | schema / hubs |
| hubs.hub_longitude | 保留物理名称；存档没有恢复别名 | DECIMAL(9, 6) | schema / hubs |

## orders

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: o

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| orders.order_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / orders |
| orders.store_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / orders |
| orders.channel_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / orders |
| orders.payment_order_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / orders |
| orders.delivery_order_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / orders |
| orders.order_status | 保留物理名称；存档没有恢复别名 | VARCHAR(50) | schema / orders |
| orders.order_amount | 保留物理名称；存档没有恢复别名 | DECIMAL(10, 2) | schema / orders |
| orders.order_delivery_fee | 保留物理名称；存档没有恢复别名 | DECIMAL(10, 2) | schema / orders |
| orders.order_delivery_cost | 保留物理名称；存档没有恢复别名 | DECIMAL(10, 2) | schema / orders |
| orders.order_created_hour | 保留物理名称；存档没有恢复别名 | INTEGER | schema / orders |
| orders.order_created_minute | 保留物理名称；存档没有恢复别名 | INTEGER | schema / orders |
| orders.order_created_day | 保留物理名称；存档没有恢复别名 | INTEGER | schema / orders |
| orders.order_created_month | 保留物理名称；存档没有恢复别名 | INTEGER | schema / orders |
| orders.order_created_year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / orders |
| orders.order_moment_created | 保留物理名称；存档没有恢复别名 | DATETIME | schema / orders |
| orders.order_moment_accepted | 保留物理名称；存档没有恢复别名 | DATETIME | schema / orders |
| orders.order_moment_ready | 保留物理名称；存档没有恢复别名 | DATETIME | schema / orders |
| orders.order_moment_collected | 保留物理名称；存档没有恢复别名 | DATETIME | schema / orders |
| orders.order_moment_in_expedition | 保留物理名称；存档没有恢复别名 | DATETIME | schema / orders |
| orders.order_moment_delivering | 保留物理名称；存档没有恢复别名 | DATETIME | schema / orders |
| orders.order_moment_delivered | 保留物理名称；存档没有恢复别名 | DATETIME | schema / orders |
| orders.order_moment_finished | 保留物理名称；存档没有恢复别名 | DATETIME | schema / orders |
| orders.order_metric_collected_time | 保留物理名称；存档没有恢复别名 | DECIMAL(10, 2) | schema / orders |
| orders.order_metric_paused_time | 保留物理名称；存档没有恢复别名 | DECIMAL(10, 2) | schema / orders |
| orders.order_metric_production_time | 保留物理名称；存档没有恢复别名 | DECIMAL(10, 2) | schema / orders |
| orders.order_metric_walking_time | 保留物理名称；存档没有恢复别名 | DECIMAL(10, 2) | schema / orders |
| orders.order_metric_expediton_speed_time | 保留物理名称；存档没有恢复别名 | DECIMAL(10, 2) | schema / orders |
| orders.order_metric_transit_time | 保留物理名称；存档没有恢复别名 | DECIMAL(10, 2) | schema / orders |
| orders.order_metric_cycle_time | 保留物理名称；存档没有恢复别名 | DECIMAL(10, 2) | schema / orders |

## payments

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| payments.payment_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / payments |
| payments.payment_order_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / payments |
| payments.payment_amount | 保留物理名称；存档没有恢复别名 | DECIMAL(10, 2) | schema / payments |
| payments.payment_fee | 保留物理名称；存档没有恢复别名 | DECIMAL(10, 2) | schema / payments |
| payments.payment_method | 保留物理名称；存档没有恢复别名 | VARCHAR(50) | schema / payments |
| payments.payment_status | 保留物理名称；存档没有恢复别名 | VARCHAR(50) | schema / payments |

## stores

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: s

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| stores.store_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / stores |
| stores.hub_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / stores |
| stores.store_name | 保留物理名称；存档没有恢复别名 | VARCHAR(50) | schema / stores |
| stores.store_segment | 保留物理名称；存档没有恢复别名 | VARCHAR(50) | schema / stores |
| stores.store_plan_price | 保留物理名称；存档没有恢复别名 | DECIMAL(10, 2) | schema / stores |
| stores.store_latitude | 保留物理名称；存档没有恢复别名 | DECIMAL(9, 6) | schema / stores |
| stores.store_longitude | 保留物理名称；存档没有恢复别名 | DECIMAL(9, 6) | schema / stores |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

