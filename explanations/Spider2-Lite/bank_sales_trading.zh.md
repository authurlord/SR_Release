# Spider2-Lite / bank_sales_trading — Schema 与业务口径解释

该数据库的存档目录包含 19 张表、106 个物理列、0 条关系，以及 19 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## bitcoin_members

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: m

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| bitcoin_members.member_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / bitcoin_members |
| bitcoin_members.first_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / bitcoin_members |
| bitcoin_members.region | 保留物理名称；存档没有恢复别名 | TEXT | schema / bitcoin_members |

## bitcoin_prices

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: p

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| bitcoin_prices.ticker | 保留物理名称；存档没有恢复别名 | TEXT | schema / bitcoin_prices |
| bitcoin_prices.market_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / bitcoin_prices |
| bitcoin_prices.price | 保留物理名称；存档没有恢复别名 | REAL | schema / bitcoin_prices |
| bitcoin_prices.open | 保留物理名称；存档没有恢复别名 | REAL | schema / bitcoin_prices |
| bitcoin_prices.high | 保留物理名称；存档没有恢复别名 | REAL | schema / bitcoin_prices |
| bitcoin_prices.low | 保留物理名称；存档没有恢复别名 | REAL | schema / bitcoin_prices |
| bitcoin_prices.volume | 保留物理名称；存档没有恢复别名 | TEXT | schema / bitcoin_prices |
| bitcoin_prices.change | 保留物理名称；存档没有恢复别名 | TEXT | schema / bitcoin_prices |

## bitcoin_transactions

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: t

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| bitcoin_transactions.txn_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / bitcoin_transactions |
| bitcoin_transactions.member_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / bitcoin_transactions |
| bitcoin_transactions.ticker | 保留物理名称；存档没有恢复别名 | TEXT | schema / bitcoin_transactions |
| bitcoin_transactions.txn_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / bitcoin_transactions |
| bitcoin_transactions.txn_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / bitcoin_transactions |
| bitcoin_transactions.quantity | 保留物理名称；存档没有恢复别名 | REAL | schema / bitcoin_transactions |
| bitcoin_transactions.percentage_fee | 保留物理名称；存档没有恢复别名 | REAL | schema / bitcoin_transactions |
| bitcoin_transactions.txn_time | 保留物理名称；存档没有恢复别名 | TEXT | schema / bitcoin_transactions |

## cleaned_weekly_sales

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cleaned_weekly_sales.week_date_formatted | 保留物理名称；存档没有恢复别名 | TEXT | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.week_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.region | 保留物理名称；存档没有恢复别名 | TEXT | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.platform | 保留物理名称；存档没有恢复别名 | TEXT | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.segment | 保留物理名称；存档没有恢复别名 | TEXT | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.customer_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.transactions | 保留物理名称；存档没有恢复别名 | INTEGER | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.sales | 保留物理名称；存档没有恢复别名 | INTEGER | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.week_number | 保留物理名称；存档没有恢复别名 | INTEGER | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.month_number | 保留物理名称；存档没有恢复别名 | INTEGER | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.calendar_year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.age_band | 保留物理名称；存档没有恢复别名 | TEXT | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.demographic | 保留物理名称；存档没有恢复别名 | TEXT | schema / cleaned_weekly_sales |
| cleaned_weekly_sales.avg_transaction | 保留物理名称；存档没有恢复别名 | REAL | schema / cleaned_weekly_sales |

## customer_nodes

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| customer_nodes.customer_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / customer_nodes |
| customer_nodes.region_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / customer_nodes |
| customer_nodes.node_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / customer_nodes |
| customer_nodes.start_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / customer_nodes |
| customer_nodes.end_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / customer_nodes |

## customer_regions

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| customer_regions.region_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / customer_regions |
| customer_regions.region_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / customer_regions |

## customer_transactions

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: t

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| customer_transactions.customer_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / customer_transactions |
| customer_transactions.txn_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / customer_transactions |
| customer_transactions.txn_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / customer_transactions |
| customer_transactions.txn_amount | 保留物理名称；存档没有恢复别名 | INTEGER | schema / customer_transactions |

## interest_map

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: i, im, im1, im2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| interest_map.id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / interest_map |
| interest_map.interest_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / interest_map |
| interest_map.interest_summary | 保留物理名称；存档没有恢复别名 | TEXT | schema / interest_map |
| interest_map.created_at | 保留物理名称；存档没有恢复别名 | TEXT | schema / interest_map |
| interest_map.last_modified | 保留物理名称；存档没有恢复别名 | TEXT | schema / interest_map |

## interest_metrics

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: m

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| interest_metrics._month | 保留物理名称；存档没有恢复别名 | REAL | schema / interest_metrics |
| interest_metrics._year | 保留物理名称；存档没有恢复别名 | REAL | schema / interest_metrics |
| interest_metrics.month_year | 保留物理名称；存档没有恢复别名 | TEXT | schema / interest_metrics |
| interest_metrics.interest_id | 保留物理名称；存档没有恢复别名 | REAL | schema / interest_metrics |
| interest_metrics.composition | 保留物理名称；存档没有恢复别名 | REAL | schema / interest_metrics |
| interest_metrics.index_value | 保留物理名称；存档没有恢复别名 | REAL | schema / interest_metrics |
| interest_metrics.ranking | 保留物理名称；存档没有恢复别名 | INTEGER | schema / interest_metrics |
| interest_metrics.percentile_ranking | 保留物理名称；存档没有恢复别名 | REAL | schema / interest_metrics |

## shopping_cart_campaign_identifier

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shopping_cart_campaign_identifier.campaign_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / shopping_cart_campaign_identifier |
| shopping_cart_campaign_identifier.products | 保留物理名称；存档没有恢复别名 | TEXT | schema / shopping_cart_campaign_identifier |
| shopping_cart_campaign_identifier.campaign_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / shopping_cart_campaign_identifier |
| shopping_cart_campaign_identifier.start_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / shopping_cart_campaign_identifier |
| shopping_cart_campaign_identifier.end_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / shopping_cart_campaign_identifier |

## shopping_cart_event_identifier

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shopping_cart_event_identifier.event_type | 保留物理名称；存档没有恢复别名 | INTEGER | schema / shopping_cart_event_identifier |
| shopping_cart_event_identifier.event_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / shopping_cart_event_identifier |

## shopping_cart_events

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: e

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shopping_cart_events.visit_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / shopping_cart_events |
| shopping_cart_events.cookie_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / shopping_cart_events |
| shopping_cart_events.page_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / shopping_cart_events |
| shopping_cart_events.event_type | 保留物理名称；存档没有恢复别名 | INTEGER | schema / shopping_cart_events |
| shopping_cart_events.sequence_number | 保留物理名称；存档没有恢复别名 | INTEGER | schema / shopping_cart_events |
| shopping_cart_events.event_time | 保留物理名称；存档没有恢复别名 | TEXT | schema / shopping_cart_events |

## shopping_cart_page_hierarchy

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: p

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shopping_cart_page_hierarchy.page_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / shopping_cart_page_hierarchy |
| shopping_cart_page_hierarchy.page_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / shopping_cart_page_hierarchy |
| shopping_cart_page_hierarchy.product_category | 保留物理名称；存档没有恢复别名 | TEXT | schema / shopping_cart_page_hierarchy |
| shopping_cart_page_hierarchy.product_id | 保留物理名称；存档没有恢复别名 | REAL | schema / shopping_cart_page_hierarchy |

## shopping_cart_users

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shopping_cart_users.user_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / shopping_cart_users |
| shopping_cart_users.cookie_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / shopping_cart_users |
| shopping_cart_users.start_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / shopping_cart_users |

## veg_cat

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: c

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| veg_cat.index | 保留物理名称；存档没有恢复别名 | INTEGER | schema / veg_cat |
| veg_cat.item_code | 保留物理名称；存档没有恢复别名 | INTEGER | schema / veg_cat |
| veg_cat.item_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / veg_cat |
| veg_cat.category_code | 保留物理名称；存档没有恢复别名 | INTEGER | schema / veg_cat |
| veg_cat.category_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / veg_cat |

## veg_loss_rate_df

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: l, v

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| veg_loss_rate_df.index | 保留物理名称；存档没有恢复别名 | INTEGER | schema / veg_loss_rate_df |
| veg_loss_rate_df.item_code | 保留物理名称；存档没有恢复别名 | INTEGER | schema / veg_loss_rate_df |
| veg_loss_rate_df.item_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / veg_loss_rate_df |
| veg_loss_rate_df.loss_rate_% | 保留物理名称；存档没有恢复别名 | REAL | schema / veg_loss_rate_df |

## veg_txn_df

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: t

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| veg_txn_df.index | 保留物理名称；存档没有恢复别名 | INTEGER | schema / veg_txn_df |
| veg_txn_df.txn_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / veg_txn_df |
| veg_txn_df.txn_time | 保留物理名称；存档没有恢复别名 | TEXT | schema / veg_txn_df |
| veg_txn_df.item_code | 保留物理名称；存档没有恢复别名 | INTEGER | schema / veg_txn_df |
| veg_txn_df.qty_sold(kg) | 保留物理名称；存档没有恢复别名 | REAL | schema / veg_txn_df |
| veg_txn_df.unit_selling_px_rmb/kg | 保留物理名称；存档没有恢复别名 | REAL | schema / veg_txn_df |
| veg_txn_df.sale/return | 保留物理名称；存档没有恢复别名 | TEXT | schema / veg_txn_df |
| veg_txn_df.discount(%) | 保留物理名称；存档没有恢复别名 | INTEGER | schema / veg_txn_df |
| veg_txn_df.day_of_week | 保留物理名称；存档没有恢复别名 | TEXT | schema / veg_txn_df |

## veg_whsle_df

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: w

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| veg_whsle_df.index | 保留物理名称；存档没有恢复别名 | INTEGER | schema / veg_whsle_df |
| veg_whsle_df.whsle_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / veg_whsle_df |
| veg_whsle_df.item_code | 保留物理名称；存档没有恢复别名 | INTEGER | schema / veg_whsle_df |
| veg_whsle_df.whsle_px_rmb-kg | 保留物理名称；存档没有恢复别名 | REAL | schema / veg_whsle_df |

## weekly_sales

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| weekly_sales.week_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / weekly_sales |
| weekly_sales.region | 保留物理名称；存档没有恢复别名 | TEXT | schema / weekly_sales |
| weekly_sales.platform | 保留物理名称；存档没有恢复别名 | TEXT | schema / weekly_sales |
| weekly_sales.segment | 保留物理名称；存档没有恢复别名 | TEXT | schema / weekly_sales |
| weekly_sales.customer_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / weekly_sales |
| weekly_sales.transactions | 保留物理名称；存档没有恢复别名 | INTEGER | schema / weekly_sales |
| weekly_sales.sales | 保留物理名称；存档没有恢复别名 | INTEGER | schema / weekly_sales |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

