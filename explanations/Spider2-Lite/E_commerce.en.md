# Spider2-Lite / E_commerce — Schema and business semantics

The saved catalogue for this database contains 11 tables, 70 physical columns, 0 relationships and 11 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## customers

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: c

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
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
| geolocation.geolocation_zip_code_prefix | Physical name retained; no saved recovered alias | INTEGER | schema / geolocation |
| geolocation.geolocation_lat | Physical name retained; no saved recovered alias | REAL | schema / geolocation |
| geolocation.geolocation_lng | Physical name retained; no saved recovered alias | REAL | schema / geolocation |
| geolocation.geolocation_city | Physical name retained; no saved recovered alias | TEXT | schema / geolocation |
| geolocation.geolocation_state | Physical name retained; no saved recovered alias | TEXT | schema / geolocation |

## leads_closed

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| leads_closed.mql_id | Physical name retained; no saved recovered alias | TEXT | schema / leads_closed |
| leads_closed.seller_id | Physical name retained; no saved recovered alias | TEXT | schema / leads_closed |
| leads_closed.sdr_id | Physical name retained; no saved recovered alias | TEXT | schema / leads_closed |
| leads_closed.sr_id | Physical name retained; no saved recovered alias | TEXT | schema / leads_closed |
| leads_closed.won_date | Physical name retained; no saved recovered alias | TEXT | schema / leads_closed |
| leads_closed.business_segment | Physical name retained; no saved recovered alias | TEXT | schema / leads_closed |
| leads_closed.lead_type | Physical name retained; no saved recovered alias | TEXT | schema / leads_closed |
| leads_closed.lead_behaviour_profile | Physical name retained; no saved recovered alias | TEXT | schema / leads_closed |
| leads_closed.has_company | Physical name retained; no saved recovered alias | INTEGER | schema / leads_closed |
| leads_closed.has_gtin | Physical name retained; no saved recovered alias | INTEGER | schema / leads_closed |
| leads_closed.average_stock | Physical name retained; no saved recovered alias | TEXT | schema / leads_closed |
| leads_closed.business_type | Physical name retained; no saved recovered alias | TEXT | schema / leads_closed |
| leads_closed.declared_product_catalog_size | Physical name retained; no saved recovered alias | REAL | schema / leads_closed |
| leads_closed.declared_monthly_revenue | Physical name retained; no saved recovered alias | REAL | schema / leads_closed |

## leads_qualified

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| leads_qualified.mql_id | Physical name retained; no saved recovered alias | TEXT | schema / leads_qualified |
| leads_qualified.first_contact_date | Physical name retained; no saved recovered alias | TEXT | schema / leads_qualified |
| leads_qualified.landing_page_id | Physical name retained; no saved recovered alias | TEXT | schema / leads_qualified |
| leads_qualified.origin | Physical name retained; no saved recovered alias | TEXT | schema / leads_qualified |

## order_items

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: oi

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
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
SQL table aliases: p

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| order_payments.order_id | Physical name retained; no saved recovered alias | TEXT | schema / order_payments |
| order_payments.payment_sequential | Physical name retained; no saved recovered alias | INTEGER | schema / order_payments |
| order_payments.payment_type | Physical name retained; no saved recovered alias | TEXT | schema / order_payments |
| order_payments.payment_installments | Physical name retained; no saved recovered alias | INTEGER | schema / order_payments |
| order_payments.payment_value | Physical name retained; no saved recovered alias | REAL | schema / order_payments |

## order_reviews

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
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
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| product_category_name_translation.product_category_name | Physical name retained; no saved recovered alias | TEXT | schema / product_category_name_translation |
| product_category_name_translation.product_category_name_english | Physical name retained; no saved recovered alias | TEXT | schema / product_category_name_translation |

## products

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: p

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
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
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| sellers.seller_id | Physical name retained; no saved recovered alias | TEXT | schema / sellers |
| sellers.seller_zip_code_prefix | Physical name retained; no saved recovered alias | INTEGER | schema / sellers |
| sellers.seller_city | Physical name retained; no saved recovered alias | TEXT | schema / sellers |
| sellers.seller_state | Physical name retained; no saved recovered alias | TEXT | schema / sellers |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

