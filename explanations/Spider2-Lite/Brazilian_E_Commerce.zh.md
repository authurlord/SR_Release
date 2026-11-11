# Spider2-Lite / Brazilian_E_Commerce — Schema 与业务口径解释

该数据库的存档目录包含 10 张表、62 个物理列、0 条关系，以及 10 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## olist_customers

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: c

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| olist_customers.customer_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_customers |
| olist_customers.customer_unique_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_customers |
| olist_customers.customer_zip_code_prefix | 保留物理名称；存档没有恢复别名 | BIGINT | schema / olist_customers |
| olist_customers.customer_city | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_customers |
| olist_customers.customer_state | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_customers |

## olist_geolocation

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| olist_geolocation.geolocation_zip_code_prefix | 保留物理名称；存档没有恢复别名 | BIGINT | schema / olist_geolocation |
| olist_geolocation.geolocation_lat | 保留物理名称；存档没有恢复别名 | FLOAT | schema / olist_geolocation |
| olist_geolocation.geolocation_lng | 保留物理名称；存档没有恢复别名 | FLOAT | schema / olist_geolocation |
| olist_geolocation.geolocation_city | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_geolocation |
| olist_geolocation.geolocation_state | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_geolocation |

## olist_order_items

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: oi

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| olist_order_items.order_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_order_items |
| olist_order_items.order_item_id | 保留物理名称；存档没有恢复别名 | BIGINT | schema / olist_order_items |
| olist_order_items.product_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_order_items |
| olist_order_items.seller_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_order_items |
| olist_order_items.shipping_limit_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_order_items |
| olist_order_items.price | 保留物理名称；存档没有恢复别名 | FLOAT | schema / olist_order_items |
| olist_order_items.freight_value | 保留物理名称；存档没有恢复别名 | FLOAT | schema / olist_order_items |

## olist_order_payments

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: op, p

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| olist_order_payments.order_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_order_payments |
| olist_order_payments.payment_sequential | 保留物理名称；存档没有恢复别名 | BIGINT | schema / olist_order_payments |
| olist_order_payments.payment_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_order_payments |
| olist_order_payments.payment_installments | 保留物理名称；存档没有恢复别名 | BIGINT | schema / olist_order_payments |
| olist_order_payments.payment_value | 保留物理名称；存档没有恢复别名 | FLOAT | schema / olist_order_payments |

## olist_order_reviews

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: r

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| olist_order_reviews.review_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_order_reviews |
| olist_order_reviews.order_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_order_reviews |
| olist_order_reviews.review_score | 保留物理名称；存档没有恢复别名 | BIGINT | schema / olist_order_reviews |
| olist_order_reviews.review_comment_title | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_order_reviews |
| olist_order_reviews.review_comment_message | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_order_reviews |
| olist_order_reviews.review_creation_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_order_reviews |
| olist_order_reviews.review_answer_timestamp | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_order_reviews |

## olist_orders

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: o

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| olist_orders.order_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_orders |
| olist_orders.customer_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_orders |
| olist_orders.order_status | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_orders |
| olist_orders.order_purchase_timestamp | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_orders |
| olist_orders.order_approved_at | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_orders |
| olist_orders.order_delivered_carrier_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_orders |
| olist_orders.order_delivered_customer_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_orders |
| olist_orders.order_estimated_delivery_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_orders |

## olist_products

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: p

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| olist_products.product_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_products |
| olist_products.product_category_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_products |
| olist_products.product_name_lenght | 保留物理名称；存档没有恢复别名 | FLOAT | schema / olist_products |
| olist_products.product_description_lenght | 保留物理名称；存档没有恢复别名 | FLOAT | schema / olist_products |
| olist_products.product_photos_qty | 保留物理名称；存档没有恢复别名 | FLOAT | schema / olist_products |
| olist_products.product_weight_g | 保留物理名称；存档没有恢复别名 | FLOAT | schema / olist_products |
| olist_products.product_length_cm | 保留物理名称；存档没有恢复别名 | FLOAT | schema / olist_products |
| olist_products.product_height_cm | 保留物理名称；存档没有恢复别名 | FLOAT | schema / olist_products |
| olist_products.product_width_cm | 保留物理名称；存档没有恢复别名 | FLOAT | schema / olist_products |

## olist_products_dataset

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| olist_products_dataset.index | 保留物理名称；存档没有恢复别名 | BIGINT | schema / olist_products_dataset |
| olist_products_dataset.product_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_products_dataset |
| olist_products_dataset.product_category_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_products_dataset |
| olist_products_dataset.product_name_lenght | 保留物理名称；存档没有恢复别名 | FLOAT | schema / olist_products_dataset |
| olist_products_dataset.product_description_lenght | 保留物理名称；存档没有恢复别名 | FLOAT | schema / olist_products_dataset |
| olist_products_dataset.product_photos_qty | 保留物理名称；存档没有恢复别名 | FLOAT | schema / olist_products_dataset |
| olist_products_dataset.product_weight_g | 保留物理名称；存档没有恢复别名 | FLOAT | schema / olist_products_dataset |
| olist_products_dataset.product_length_cm | 保留物理名称；存档没有恢复别名 | FLOAT | schema / olist_products_dataset |
| olist_products_dataset.product_height_cm | 保留物理名称；存档没有恢复别名 | FLOAT | schema / olist_products_dataset |
| olist_products_dataset.product_width_cm | 保留物理名称；存档没有恢复别名 | FLOAT | schema / olist_products_dataset |

## olist_sellers

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| olist_sellers.seller_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_sellers |
| olist_sellers.seller_zip_code_prefix | 保留物理名称；存档没有恢复别名 | BIGINT | schema / olist_sellers |
| olist_sellers.seller_city | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_sellers |
| olist_sellers.seller_state | 保留物理名称；存档没有恢复别名 | TEXT | schema / olist_sellers |

## product_category_name_translation

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| product_category_name_translation.product_category_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / product_category_name_translation |
| product_category_name_translation.product_category_name_english | 保留物理名称；存档没有恢复别名 | TEXT | schema / product_category_name_translation |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

