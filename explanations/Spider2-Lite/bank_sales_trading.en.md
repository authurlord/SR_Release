# Spider2-Lite / bank_sales_trading — Schema and business semantics

The saved catalogue for this database contains 19 tables, 106 physical columns, 0 relationships and 19 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## bitcoin_members

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: m

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| bitcoin_members.member_id | Physical name retained; no saved recovered alias | TEXT | schema / bitcoin_members |
| bitcoin_members.first_name | Physical name retained; no saved recovered alias | TEXT | schema / bitcoin_members |
| bitcoin_members.region | Physical name retained; no saved recovered alias | TEXT | schema / bitcoin_members |

## bitcoin_prices

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: p

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| bitcoin_prices.ticker | Physical name retained; no saved recovered alias | TEXT | schema / bitcoin_prices |
| bitcoin_prices.market_date | Physical name retained; no saved recovered alias | TEXT | schema / bitcoin_prices |
| bitcoin_prices.price | Physical name retained; no saved recovered alias | REAL | schema / bitcoin_prices |
| bitcoin_prices.open | Physical name retained; no saved recovered alias | REAL | schema / bitcoin_prices |
| bitcoin_prices.high | Physical name retained; no saved recovered alias | REAL | schema / bitcoin_prices |
| bitcoin_prices.low | Physical name retained; no saved recovered alias | REAL | schema / bitcoin_prices |
| bitcoin_prices.volume | Physical name retained; no saved recovered alias | TEXT | schema / bitcoin_prices |
| bitcoin_prices.change | Physical name retained; no saved recovered alias | TEXT | schema / bitcoin_prices |

## bitcoin_transactions

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: t

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| bitcoin_transactions.txn_id | Physical name retained; no saved recovered alias | INTEGER | schema / bitcoin_transactions |
| bitcoin_transactions.member_id | Physical name retained; no saved recovered alias | TEXT | schema / bitcoin_transactions |
| bitcoin_transactions.ticker | Physical name retained; no saved recovered alias | TEXT | schema / bitcoin_transactions |
| bitcoin_transactions.txn_date | Physical name retained; no saved recovered alias | TEXT | schema / bitcoin_transactions |
| bitcoin_transactions.txn_type | Physical name retained; no saved recovered alias | TEXT | schema / bitcoin_transactions |
| bitcoin_transactions.quantity | Physical name retained; no saved recovered alias | REAL | schema / bitcoin_transactions |
| bitcoin_transactions.percentage_fee | Physical name retained; no saved recovered alias | REAL | schema / bitcoin_transactions |
| bitcoin_transactions.txn_time | Physical name retained; no saved recovered alias | TEXT | schema / bitcoin_transactions |

## cleaned_weekly_sales

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| cleaned_weekly_sales.week_date_formatted | Physical name retained; no saved recovered alias | TEXT | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.week_date | Physical name retained; no saved recovered alias | TEXT | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.region | Physical name retained; no saved recovered alias | TEXT | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.platform | Physical name retained; no saved recovered alias | TEXT | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.segment | Physical name retained; no saved recovered alias | TEXT | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.customer_type | Physical name retained; no saved recovered alias | TEXT | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.transactions | Physical name retained; no saved recovered alias | INTEGER | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.sales | Physical name retained; no saved recovered alias | INTEGER | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.week_number | Physical name retained; no saved recovered alias | INTEGER | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.month_number | Physical name retained; no saved recovered alias | INTEGER | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.calendar_year | Physical name retained; no saved recovered alias | INTEGER | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.age_band | Physical name retained; no saved recovered alias | TEXT | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.demographic | Physical name retained; no saved recovered alias | TEXT | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.avg_transaction | Physical name retained; no saved recovered alias | REAL | schema / cleaned_weekly_sales |

## customer_nodes

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| customer_nodes.customer_id | Physical name retained; no saved recovered alias | INTEGER | schema / customer_nodes |
| customer_nodes.region_id | Physical name retained; no saved recovered alias | INTEGER | schema / customer_nodes |
| customer_nodes.node_id | Physical name retained; no saved recovered alias | INTEGER | schema / customer_nodes |
| customer_nodes.start_date | Physical name retained; no saved recovered alias | TEXT | schema / customer_nodes |
| customer_nodes.end_date | Physical name retained; no saved recovered alias | TEXT | schema / customer_nodes |

## customer_regions

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| customer_regions.region_id | Physical name retained; no saved recovered alias | INTEGER | schema / customer_regions |
| customer_regions.region_name | Physical name retained; no saved recovered alias | TEXT | schema / customer_regions |

## customer_transactions

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: t

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| customer_transactions.customer_id | Physical name retained; no saved recovered alias | INTEGER | schema / customer_transactions |
| customer_transactions.txn_date | Physical name retained; no saved recovered alias | TEXT | schema / customer_transactions |
| customer_transactions.txn_type | Physical name retained; no saved recovered alias | TEXT | schema / customer_transactions |
| customer_transactions.txn_amount | Physical name retained; no saved recovered alias | INTEGER | schema / customer_transactions |

## interest_map

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: i, im, im1, im2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| interest_map.id | Physical name retained; no saved recovered alias | INTEGER | schema / interest_map |
| interest_map.interest_name | Physical name retained; no saved recovered alias | TEXT | schema / interest_map |
| interest_map.interest_summary | Physical name retained; no saved recovered alias | TEXT | schema / interest_map |
| interest_map.created_at | Physical name retained; no saved recovered alias | TEXT | schema / interest_map |
| interest_map.last_modified | Physical name retained; no saved recovered alias | TEXT | schema / interest_map |

## interest_metrics

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: m

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| interest_metrics._month | Physical name retained; no saved recovered alias | REAL | schema / interest_metrics |
| interest_metrics._year | Physical name retained; no saved recovered alias | REAL | schema / interest_metrics |
| interest_metrics.month_year | Physical name retained; no saved recovered alias | TEXT | schema / interest_metrics |
| interest_metrics.interest_id | Physical name retained; no saved recovered alias | REAL | schema / interest_metrics |
| interest_metrics.composition | Physical name retained; no saved recovered alias | REAL | schema / interest_metrics |
| interest_metrics.index_value | Physical name retained; no saved recovered alias | REAL | schema / interest_metrics |
| interest_metrics.ranking | Physical name retained; no saved recovered alias | INTEGER | schema / interest_metrics |
| interest_metrics.percentile_ranking | Physical name retained; no saved recovered alias | REAL | schema / interest_metrics |

## shopping_cart_campaign_identifier

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| shopping_cart_campaign_identifier.campaign_id | Physical name retained; no saved recovered alias | INTEGER | schema / shopping_cart_campaign_identifier |
| shopping_cart_campaign_identifier.products | Physical name retained; no saved recovered alias | TEXT | schema / shopping_cart_campaign_identifier |
| shopping_cart_campaign_identifier.campaign_name | Physical name retained; no saved recovered alias | TEXT | schema / shopping_cart_campaign_identifier |
| shopping_cart_campaign_identifier.start_date | Physical name retained; no saved recovered alias | TEXT | schema / shopping_cart_campaign_identifier |
| shopping_cart_campaign_identifier.end_date | Physical name retained; no saved recovered alias | TEXT | schema / shopping_cart_campaign_identifier |

## shopping_cart_event_identifier

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| shopping_cart_event_identifier.event_type | Physical name retained; no saved recovered alias | INTEGER | schema / shopping_cart_event_identifier |
| shopping_cart_event_identifier.event_name | Physical name retained; no saved recovered alias | TEXT | schema / shopping_cart_event_identifier |

## shopping_cart_events

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: e

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| shopping_cart_events.visit_id | Physical name retained; no saved recovered alias | TEXT | schema / shopping_cart_events |
| shopping_cart_events.cookie_id | Physical name retained; no saved recovered alias | TEXT | schema / shopping_cart_events |
| shopping_cart_events.page_id | Physical name retained; no saved recovered alias | INTEGER | schema / shopping_cart_events |
| shopping_cart_events.event_type | Physical name retained; no saved recovered alias | INTEGER | schema / shopping_cart_events |
| shopping_cart_events.sequence_number | Physical name retained; no saved recovered alias | INTEGER | schema / shopping_cart_events |
| shopping_cart_events.event_time | Physical name retained; no saved recovered alias | TEXT | schema / shopping_cart_events |

## shopping_cart_page_hierarchy

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: p

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| shopping_cart_page_hierarchy.page_id | Physical name retained; no saved recovered alias | INTEGER | schema / shopping_cart_page_hierarchy |
| shopping_cart_page_hierarchy.page_name | Physical name retained; no saved recovered alias | TEXT | schema / shopping_cart_page_hierarchy |
| shopping_cart_page_hierarchy.product_category | Physical name retained; no saved recovered alias | TEXT | schema / shopping_cart_page_hierarchy |
| shopping_cart_page_hierarchy.product_id | Physical name retained; no saved recovered alias | REAL | schema / shopping_cart_page_hierarchy |

## shopping_cart_users

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| shopping_cart_users.user_id | Physical name retained; no saved recovered alias | INTEGER | schema / shopping_cart_users |
| shopping_cart_users.cookie_id | Physical name retained; no saved recovered alias | TEXT | schema / shopping_cart_users |
| shopping_cart_users.start_date | Physical name retained; no saved recovered alias | TEXT | schema / shopping_cart_users |

## veg_cat

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: c

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| veg_cat.index | Physical name retained; no saved recovered alias | INTEGER | schema / veg_cat |
| veg_cat.item_code | Physical name retained; no saved recovered alias | INTEGER | schema / veg_cat |
| veg_cat.item_name | Physical name retained; no saved recovered alias | TEXT | schema / veg_cat |
| veg_cat.category_code | Physical name retained; no saved recovered alias | INTEGER | schema / veg_cat |
| veg_cat.category_name | Physical name retained; no saved recovered alias | TEXT | schema / veg_cat |

## veg_loss_rate_df

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: l, v

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| veg_loss_rate_df.index | Physical name retained; no saved recovered alias | INTEGER | schema / veg_loss_rate_df |
| veg_loss_rate_df.item_code | Physical name retained; no saved recovered alias | INTEGER | schema / veg_loss_rate_df |
| veg_loss_rate_df.item_name | Physical name retained; no saved recovered alias | TEXT | schema / veg_loss_rate_df |
| veg_loss_rate_df.loss_rate_% | Physical name retained; no saved recovered alias | REAL | schema / veg_loss_rate_df |

## veg_txn_df

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: t

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| veg_txn_df.index | Physical name retained; no saved recovered alias | INTEGER | schema / veg_txn_df |
| veg_txn_df.txn_date | Physical name retained; no saved recovered alias | TEXT | schema / veg_txn_df |
| veg_txn_df.txn_time | Physical name retained; no saved recovered alias | TEXT | schema / veg_txn_df |
| veg_txn_df.item_code | Physical name retained; no saved recovered alias | INTEGER | schema / veg_txn_df |
| veg_txn_df.qty_sold(kg) | Physical name retained; no saved recovered alias | REAL | schema / veg_txn_df |
| veg_txn_df.unit_selling_px_rmb/kg | Physical name retained; no saved recovered alias | REAL | schema / veg_txn_df |
| veg_txn_df.sale/return | Physical name retained; no saved recovered alias | TEXT | schema / veg_txn_df |
| veg_txn_df.discount(%) | Physical name retained; no saved recovered alias | INTEGER | schema / veg_txn_df |
| veg_txn_df.day_of_week | Physical name retained; no saved recovered alias | TEXT | schema / veg_txn_df |

## veg_whsle_df

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: w

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| veg_whsle_df.index | Physical name retained; no saved recovered alias | INTEGER | schema / veg_whsle_df |
| veg_whsle_df.whsle_date | Physical name retained; no saved recovered alias | TEXT | schema / veg_whsle_df |
| veg_whsle_df.item_code | Physical name retained; no saved recovered alias | INTEGER | schema / veg_whsle_df |
| veg_whsle_df.whsle_px_rmb-kg | Physical name retained; no saved recovered alias | REAL | schema / veg_whsle_df |

## weekly_sales

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| weekly_sales.week_date | Physical name retained; no saved recovered alias | TEXT | schema / weekly_sales |
| weekly_sales.region | Physical name retained; no saved recovered alias | TEXT | schema / weekly_sales |
| weekly_sales.platform | Physical name retained; no saved recovered alias | TEXT | schema / weekly_sales |
| weekly_sales.segment | Physical name retained; no saved recovered alias | TEXT | schema / weekly_sales |
| weekly_sales.customer_type | Physical name retained; no saved recovered alias | TEXT | schema / weekly_sales |
| weekly_sales.transactions | Physical name retained; no saved recovered alias | INTEGER | schema / weekly_sales |
| weekly_sales.sales | Physical name retained; no saved recovered alias | INTEGER | schema / weekly_sales |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

