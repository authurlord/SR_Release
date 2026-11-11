# Spider2-Lite / electronic_sales — Schema and business semantics

The saved catalogue for this database contains 9 tables, 61 physical columns, 0 relationships and 9 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## customers

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| customers.index | Physical name retained; no saved recovered alias | INTEGER | schema / customers |
| customers.customer_id | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.customer_unique_id | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.customer_zip_code_prefix | Physical name retained; no saved recovered alias | INTEGER | schema / customers |
| customers.customer_city | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.customer_state | Physical name retained; no saved recovered alias | TEXT | schema / customers |

## geolocation

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| geolocation.index | Physical name retained; no saved recovered alias | INTEGER | schema / geolocation |
| geolocation.geolocation_zip_code_prefix | Physical name retained; no saved recovered alias | INTEGER | schema / geolocation |
| geolocation.geolocation_lat | Physical name retained; no saved recovered alias | REAL | schema / geolocation |
| geolocation.geolocation_lng | Physical name retained; no saved recovered alias | REAL | schema / geolocation |
| geolocation.geolocation_city | Physical name retained; no saved recovered alias | TEXT | schema / geolocation |
| geolocation.geolocation_state | Physical name retained; no saved recovered alias | TEXT | schema / geolocation |

## order_items

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: oi

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| order_items.index | Physical name retained; no saved recovered alias | INTEGER | schema / order_items |
| order_items.order_id | Physical name retained; no saved recovered alias | TEXT | schema / order_items |
| order_items.order_item_id | Physical name retained; no saved recovered alias | INTEGER | schema / order_items |
| order_items.product_id | Physical name retained; no saved recovered alias | TEXT | schema / order_items |
| order_items.seller_id | Physical name retained; no saved recovered alias | TEXT | schema / order_items |
| order_items.shipping_limit_date | Physical name retained; no saved recovered alias | TEXT | schema / order_items |
| order_items.price | Physical name retained; no saved recovered alias | REAL | schema / order_items |
| order_items.freight_value | Physical name retained; no saved recovered alias | REAL | schema / order_items |

## order_payments

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| order_payments.index | Physical name retained; no saved recovered alias | INTEGER | schema / order_payments |
| order_payments.order_id | Physical name retained; no saved recovered alias | TEXT | schema / order_payments |
| order_payments.payment_sequential | Physical name retained; no saved recovered alias | INTEGER | schema / order_payments |
| order_payments.payment_type | Physical name retained; no saved recovered alias | TEXT | schema / order_payments |
| order_payments.payment_installments | Physical name retained; no saved recovered alias | INTEGER | schema / order_payments |
| order_payments.payment_value | Physical name retained; no saved recovered alias | REAL | schema / order_payments |

## order_reviews

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: r

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| order_reviews.index | Physical name retained; no saved recovered alias | INTEGER | schema / order_reviews |
| order_reviews.review_id | Physical name retained; no saved recovered alias | TEXT | schema / order_reviews |
| order_reviews.order_id | Physical name retained; no saved recovered alias | TEXT | schema / order_reviews |
| order_reviews.review_score | Physical name retained; no saved recovered alias | INTEGER | schema / order_reviews |
| order_reviews.review_comment_title | Physical name retained; no saved recovered alias | TEXT | schema / order_reviews |
| order_reviews.review_comment_message | Physical name retained; no saved recovered alias | TEXT | schema / order_reviews |
| order_reviews.review_creation_date | Physical name retained; no saved recovered alias | TEXT | schema / order_reviews |
| order_reviews.review_answer_timestamp | Physical name retained; no saved recovered alias | TEXT | schema / order_reviews |

## orders

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: o

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| orders.index | Physical name retained; no saved recovered alias | INTEGER | schema / orders |
| orders.order_id | Physical name retained; no saved recovered alias | TEXT | schema / orders |
| orders.customer_id | Physical name retained; no saved recovered alias | TEXT | schema / orders |
| orders.order_status | Physical name retained; no saved recovered alias | TEXT | schema / orders |
| orders.order_purchase_timestamp | Physical name retained; no saved recovered alias | TEXT | schema / orders |
| orders.order_approved_at | Physical name retained; no saved recovered alias | TEXT | schema / orders |
| orders.order_delivered_carrier_date | Physical name retained; no saved recovered alias | TEXT | schema / orders |
| orders.order_delivered_customer_date | Physical name retained; no saved recovered alias | TEXT | schema / orders |
| orders.order_estimated_delivery_date | Physical name retained; no saved recovered alias | TEXT | schema / orders |

## product_category_name_translation

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: t

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| product_category_name_translation.index | Physical name retained; no saved recovered alias | INTEGER | schema / product_category_name_translation |
| product_category_name_translation.product_category_name | Physical name retained; no saved recovered alias | TEXT | schema / product_category_name_translation |
| product_category_name_translation.product_category_name_english | Physical name retained; no saved recovered alias | TEXT | schema / product_category_name_translation |

## products

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: p

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| products.index | Physical name retained; no saved recovered alias | INTEGER | schema / products |
| products.product_id | Physical name retained; no saved recovered alias | TEXT | schema / products |
| products.product_category_name | Physical name retained; no saved recovered alias | TEXT | schema / products |
| products.product_name_lenght | Physical name retained; no saved recovered alias | REAL | schema / products |
| products.product_description_lenght | Physical name retained; no saved recovered alias | REAL | schema / products |
| products.product_photos_qty | Physical name retained; no saved recovered alias | REAL | schema / products |
| products.product_weight_g | Physical name retained; no saved recovered alias | REAL | schema / products |
| products.product_length_cm | Physical name retained; no saved recovered alias | REAL | schema / products |
| products.product_height_cm | Physical name retained; no saved recovered alias | REAL | schema / products |
| products.product_width_cm | Physical name retained; no saved recovered alias | REAL | schema / products |

## sellers

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: s

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| sellers.index | Physical name retained; no saved recovered alias | INTEGER | schema / sellers |
| sellers.seller_id | Physical name retained; no saved recovered alias | TEXT | schema / sellers |
| sellers.seller_zip_code_prefix | Physical name retained; no saved recovered alias | INTEGER | schema / sellers |
| sellers.seller_city | Physical name retained; no saved recovered alias | TEXT | schema / sellers |
| sellers.seller_state | Physical name retained; no saved recovered alias | TEXT | schema / sellers |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

