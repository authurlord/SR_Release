# Spider2-Lite / Brazilian_E_Commerce — Schema and business semantics

The saved catalogue for this database contains 10 tables, 62 physical columns, 0 relationships and 10 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## olist_customers

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: c

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| olist_customers.customer_id | Physical name retained; no saved recovered alias | TEXT | schema / olist_customers |
| olist_customers.customer_unique_id | Physical name retained; no saved recovered alias | TEXT | schema / olist_customers |
| olist_customers.customer_zip_code_prefix | Physical name retained; no saved recovered alias | BIGINT | schema / olist_customers |
| olist_customers.customer_city | Physical name retained; no saved recovered alias | TEXT | schema / olist_customers |
| olist_customers.customer_state | Physical name retained; no saved recovered alias | TEXT | schema / olist_customers |

## olist_geolocation

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| olist_geolocation.geolocation_zip_code_prefix | Physical name retained; no saved recovered alias | BIGINT | schema / olist_geolocation |
| olist_geolocation.geolocation_lat | Physical name retained; no saved recovered alias | FLOAT | schema / olist_geolocation |
| olist_geolocation.geolocation_lng | Physical name retained; no saved recovered alias | FLOAT | schema / olist_geolocation |
| olist_geolocation.geolocation_city | Physical name retained; no saved recovered alias | TEXT | schema / olist_geolocation |
| olist_geolocation.geolocation_state | Physical name retained; no saved recovered alias | TEXT | schema / olist_geolocation |

## olist_order_items

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: oi

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| olist_order_items.order_id | Physical name retained; no saved recovered alias | TEXT | schema / olist_order_items |
| olist_order_items.order_item_id | Physical name retained; no saved recovered alias | BIGINT | schema / olist_order_items |
| olist_order_items.product_id | Physical name retained; no saved recovered alias | TEXT | schema / olist_order_items |
| olist_order_items.seller_id | Physical name retained; no saved recovered alias | TEXT | schema / olist_order_items |
| olist_order_items.shipping_limit_date | Physical name retained; no saved recovered alias | TEXT | schema / olist_order_items |
| olist_order_items.price | Physical name retained; no saved recovered alias | FLOAT | schema / olist_order_items |
| olist_order_items.freight_value | Physical name retained; no saved recovered alias | FLOAT | schema / olist_order_items |

## olist_order_payments

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: op, p

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| olist_order_payments.order_id | Physical name retained; no saved recovered alias | TEXT | schema / olist_order_payments |
| olist_order_payments.payment_sequential | Physical name retained; no saved recovered alias | BIGINT | schema / olist_order_payments |
| olist_order_payments.payment_type | Physical name retained; no saved recovered alias | TEXT | schema / olist_order_payments |
| olist_order_payments.payment_installments | Physical name retained; no saved recovered alias | BIGINT | schema / olist_order_payments |
| olist_order_payments.payment_value | Physical name retained; no saved recovered alias | FLOAT | schema / olist_order_payments |

## olist_order_reviews

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: r

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| olist_order_reviews.review_id | Physical name retained; no saved recovered alias | TEXT | schema / olist_order_reviews |
| olist_order_reviews.order_id | Physical name retained; no saved recovered alias | TEXT | schema / olist_order_reviews |
| olist_order_reviews.review_score | Physical name retained; no saved recovered alias | BIGINT | schema / olist_order_reviews |
| olist_order_reviews.review_comment_title | Physical name retained; no saved recovered alias | TEXT | schema / olist_order_reviews |
| olist_order_reviews.review_comment_message | Physical name retained; no saved recovered alias | TEXT | schema / olist_order_reviews |
| olist_order_reviews.review_creation_date | Physical name retained; no saved recovered alias | TEXT | schema / olist_order_reviews |
| olist_order_reviews.review_answer_timestamp | Physical name retained; no saved recovered alias | TEXT | schema / olist_order_reviews |

## olist_orders

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: o

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| olist_orders.order_id | Physical name retained; no saved recovered alias | TEXT | schema / olist_orders |
| olist_orders.customer_id | Physical name retained; no saved recovered alias | TEXT | schema / olist_orders |
| olist_orders.order_status | Physical name retained; no saved recovered alias | TEXT | schema / olist_orders |
| olist_orders.order_purchase_timestamp | Physical name retained; no saved recovered alias | TEXT | schema / olist_orders |
| olist_orders.order_approved_at | Physical name retained; no saved recovered alias | TEXT | schema / olist_orders |
| olist_orders.order_delivered_carrier_date | Physical name retained; no saved recovered alias | TEXT | schema / olist_orders |
| olist_orders.order_delivered_customer_date | Physical name retained; no saved recovered alias | TEXT | schema / olist_orders |
| olist_orders.order_estimated_delivery_date | Physical name retained; no saved recovered alias | TEXT | schema / olist_orders |

## olist_products

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: p

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| olist_products.product_id | Physical name retained; no saved recovered alias | TEXT | schema / olist_products |
| olist_products.product_category_name | Physical name retained; no saved recovered alias | TEXT | schema / olist_products |
| olist_products.product_name_lenght | Physical name retained; no saved recovered alias | FLOAT | schema / olist_products |
| olist_products.product_description_lenght | Physical name retained; no saved recovered alias | FLOAT | schema / olist_products |
| olist_products.product_photos_qty | Physical name retained; no saved recovered alias | FLOAT | schema / olist_products |
| olist_products.product_weight_g | Physical name retained; no saved recovered alias | FLOAT | schema / olist_products |
| olist_products.product_length_cm | Physical name retained; no saved recovered alias | FLOAT | schema / olist_products |
| olist_products.product_height_cm | Physical name retained; no saved recovered alias | FLOAT | schema / olist_products |
| olist_products.product_width_cm | Physical name retained; no saved recovered alias | FLOAT | schema / olist_products |

## olist_products_dataset

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| olist_products_dataset.index | Physical name retained; no saved recovered alias | BIGINT | schema / olist_products_dataset |
| olist_products_dataset.product_id | Physical name retained; no saved recovered alias | TEXT | schema / olist_products_dataset |
| olist_products_dataset.product_category_name | Physical name retained; no saved recovered alias | TEXT | schema / olist_products_dataset |
| olist_products_dataset.product_name_lenght | Physical name retained; no saved recovered alias | FLOAT | schema / olist_products_dataset |
| olist_products_dataset.product_description_lenght | Physical name retained; no saved recovered alias | FLOAT | schema / olist_products_dataset |
| olist_products_dataset.product_photos_qty | Physical name retained; no saved recovered alias | FLOAT | schema / olist_products_dataset |
| olist_products_dataset.product_weight_g | Physical name retained; no saved recovered alias | FLOAT | schema / olist_products_dataset |
| olist_products_dataset.product_length_cm | Physical name retained; no saved recovered alias | FLOAT | schema / olist_products_dataset |
| olist_products_dataset.product_height_cm | Physical name retained; no saved recovered alias | FLOAT | schema / olist_products_dataset |
| olist_products_dataset.product_width_cm | Physical name retained; no saved recovered alias | FLOAT | schema / olist_products_dataset |

## olist_sellers

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| olist_sellers.seller_id | Physical name retained; no saved recovered alias | TEXT | schema / olist_sellers |
| olist_sellers.seller_zip_code_prefix | Physical name retained; no saved recovered alias | BIGINT | schema / olist_sellers |
| olist_sellers.seller_city | Physical name retained; no saved recovered alias | TEXT | schema / olist_sellers |
| olist_sellers.seller_state | Physical name retained; no saved recovered alias | TEXT | schema / olist_sellers |

## product_category_name_translation

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| product_category_name_translation.product_category_name | Physical name retained; no saved recovered alias | TEXT | schema / product_category_name_translation |
| product_category_name_translation.product_category_name_english | Physical name retained; no saved recovered alias | TEXT | schema / product_category_name_translation |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

