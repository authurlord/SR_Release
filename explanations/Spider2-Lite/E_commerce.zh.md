# Spider2-Lite / E_commerce — Schema 与业务口径解释

该数据库的存档目录包含 11 张表、70 个物理列、0 条关系，以及 11 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## customers

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: c

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| customers.customer_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.customer_unique_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.customer_zip_code_prefix | 保留物理名称；存档没有恢复别名 | INTEGER | schema / customers |
| customers.customer_city | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.customer_state | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |

## geolocation

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| geolocation.geolocation_zip_code_prefix | 保留物理名称；存档没有恢复别名 | INTEGER | schema / geolocation |
| geolocation.geolocation_lat | 保留物理名称；存档没有恢复别名 | REAL | schema / geolocation |
| geolocation.geolocation_lng | 保留物理名称；存档没有恢复别名 | REAL | schema / geolocation |
| geolocation.geolocation_city | 保留物理名称；存档没有恢复别名 | TEXT | schema / geolocation |
| geolocation.geolocation_state | 保留物理名称；存档没有恢复别名 | TEXT | schema / geolocation |

## leads_closed

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| leads_closed.mql_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / leads_closed |
| leads_closed.seller_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / leads_closed |
| leads_closed.sdr_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / leads_closed |
| leads_closed.sr_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / leads_closed |
| leads_closed.won_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / leads_closed |
| leads_closed.business_segment | 保留物理名称；存档没有恢复别名 | TEXT | schema / leads_closed |
| leads_closed.lead_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / leads_closed |
| leads_closed.lead_behaviour_profile | 保留物理名称；存档没有恢复别名 | TEXT | schema / leads_closed |
| leads_closed.has_company | 保留物理名称；存档没有恢复别名 | INTEGER | schema / leads_closed |
| leads_closed.has_gtin | 保留物理名称；存档没有恢复别名 | INTEGER | schema / leads_closed |
| leads_closed.average_stock | 保留物理名称；存档没有恢复别名 | TEXT | schema / leads_closed |
| leads_closed.business_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / leads_closed |
| leads_closed.declared_product_catalog_size | 保留物理名称；存档没有恢复别名 | REAL | schema / leads_closed |
| leads_closed.declared_monthly_revenue | 保留物理名称；存档没有恢复别名 | REAL | schema / leads_closed |

## leads_qualified

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| leads_qualified.mql_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / leads_qualified |
| leads_qualified.first_contact_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / leads_qualified |
| leads_qualified.landing_page_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / leads_qualified |
| leads_qualified.origin | 保留物理名称；存档没有恢复别名 | TEXT | schema / leads_qualified |

## order_items

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: oi

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| order_items.order_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / order_items |
| order_items.order_item_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / order_items |
| order_items.product_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / order_items |
| order_items.seller_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / order_items |
| order_items.shipping_limit_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / order_items |
| order_items.price | 保留物理名称；存档没有恢复别名 | REAL | schema / order_items |
| order_items.freight_value | 保留物理名称；存档没有恢复别名 | REAL | schema / order_items |

## order_payments

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: p

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| order_payments.order_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / order_payments |
| order_payments.payment_sequential | 保留物理名称；存档没有恢复别名 | INTEGER | schema / order_payments |
| order_payments.payment_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / order_payments |
| order_payments.payment_installments | 保留物理名称；存档没有恢复别名 | INTEGER | schema / order_payments |
| order_payments.payment_value | 保留物理名称；存档没有恢复别名 | REAL | schema / order_payments |

## order_reviews

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| order_reviews.review_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / order_reviews |
| order_reviews.order_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / order_reviews |
| order_reviews.review_score | 保留物理名称；存档没有恢复别名 | INTEGER | schema / order_reviews |
| order_reviews.review_comment_title | 保留物理名称；存档没有恢复别名 | TEXT | schema / order_reviews |
| order_reviews.review_comment_message | 保留物理名称；存档没有恢复别名 | TEXT | schema / order_reviews |
| order_reviews.review_creation_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / order_reviews |
| order_reviews.review_answer_timestamp | 保留物理名称；存档没有恢复别名 | TEXT | schema / order_reviews |

## orders

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: o

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| orders.order_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / orders |
| orders.customer_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / orders |
| orders.order_status | 保留物理名称；存档没有恢复别名 | TEXT | schema / orders |
| orders.order_purchase_timestamp | 保留物理名称；存档没有恢复别名 | TEXT | schema / orders |
| orders.order_approved_at | 保留物理名称；存档没有恢复别名 | TEXT | schema / orders |
| orders.order_delivered_carrier_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / orders |
| orders.order_delivered_customer_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / orders |
| orders.order_estimated_delivery_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / orders |

## product_category_name_translation

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| product_category_name_translation.product_category_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / product_category_name_translation |
| product_category_name_translation.product_category_name_english | 保留物理名称；存档没有恢复别名 | TEXT | schema / product_category_name_translation |

## products

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: p

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| products.product_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / products |
| products.product_category_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / products |
| products.product_name_lenght | 保留物理名称；存档没有恢复别名 | REAL | schema / products |
| products.product_description_lenght | 保留物理名称；存档没有恢复别名 | REAL | schema / products |
| products.product_photos_qty | 保留物理名称；存档没有恢复别名 | REAL | schema / products |
| products.product_weight_g | 保留物理名称；存档没有恢复别名 | REAL | schema / products |
| products.product_length_cm | 保留物理名称；存档没有恢复别名 | REAL | schema / products |
| products.product_height_cm | 保留物理名称；存档没有恢复别名 | REAL | schema / products |
| products.product_width_cm | 保留物理名称；存档没有恢复别名 | REAL | schema / products |

## sellers

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| sellers.seller_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / sellers |
| sellers.seller_zip_code_prefix | 保留物理名称；存档没有恢复别名 | INTEGER | schema / sellers |
| sellers.seller_city | 保留物理名称；存档没有恢复别名 | TEXT | schema / sellers |
| sellers.seller_state | 保留物理名称；存档没有恢复别名 | TEXT | schema / sellers |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

