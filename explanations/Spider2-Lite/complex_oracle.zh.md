# Spider2-Lite / complex_oracle — Schema 与业务口径解释

该数据库的存档目录包含 10 张表、140 个物理列、0 条关系，以及 10 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## channels

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: ch

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| channels.channel_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / channels |
| channels.channel_desc | 保留物理名称；存档没有恢复别名 | TEXT | schema / channels |
| channels.channel_class | 保留物理名称；存档没有恢复别名 | TEXT | schema / channels |
| channels.channel_class_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / channels |
| channels.channel_total | 保留物理名称；存档没有恢复别名 | TEXT | schema / channels |
| channels.channel_total_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / channels |

## costs

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: c

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| costs.prod_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / costs |
| costs.time_id | 保留物理名称；存档没有恢复别名 | DATE | schema / costs |
| costs.promo_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / costs |
| costs.channel_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / costs |
| costs.unit_cost | 保留物理名称；存档没有恢复别名 | REAL | schema / costs |
| costs.unit_price | 保留物理名称；存档没有恢复别名 | REAL | schema / costs |

## countries

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: co

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| countries.country_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / countries |
| countries.country_iso_code | 保留物理名称；存档没有恢复别名 | CHAR(2) | schema / countries |
| countries.country_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / countries |
| countries.country_subregion | 保留物理名称；存档没有恢复别名 | TEXT | schema / countries |
| countries.country_subregion_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / countries |
| countries.country_region | 保留物理名称；存档没有恢复别名 | TEXT | schema / countries |
| countries.country_region_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / countries |
| countries.country_total | 保留物理名称；存档没有恢复别名 | TEXT | schema / countries |
| countries.country_total_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / countries |

## currency

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: c

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| currency.country | 保留物理名称；存档没有恢复别名 | TEXT | schema / currency |
| currency.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / currency |
| currency.month | 保留物理名称；存档没有恢复别名 | INTEGER | schema / currency |
| currency.to_us | 保留物理名称；存档没有恢复别名 | REAL | schema / currency |

## customers

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: c, cu

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| customers.cust_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / customers |
| customers.cust_first_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.cust_last_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.cust_gender | 保留物理名称；存档没有恢复别名 | CHAR(1) | schema / customers |
| customers.cust_year_of_birth | 保留物理名称；存档没有恢复别名 | INTEGER | schema / customers |
| customers.cust_marital_status | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.cust_street_address | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.cust_postal_code | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.cust_city | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.cust_city_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / customers |
| customers.cust_state_province | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.cust_state_province_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / customers |
| customers.country_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / customers |
| customers.cust_main_phone_number | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.cust_income_level | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.cust_credit_limit | 保留物理名称；存档没有恢复别名 | REAL | schema / customers |
| customers.cust_email | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.cust_total | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.cust_total_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / customers |
| customers.cust_src_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / customers |
| customers.cust_eff_from | 保留物理名称；存档没有恢复别名 | DATE | schema / customers |
| customers.cust_eff_to | 保留物理名称；存档没有恢复别名 | DATE | schema / customers |
| customers.cust_valid | 保留物理名称；存档没有恢复别名 | CHAR(1) | schema / customers |

## products

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| products.prod_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / products |
| products.prod_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / products |
| products.prod_desc | 保留物理名称；存档没有恢复别名 | TEXT | schema / products |
| products.prod_subcategory | 保留物理名称；存档没有恢复别名 | TEXT | schema / products |
| products.prod_subcategory_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / products |
| products.prod_subcategory_desc | 保留物理名称；存档没有恢复别名 | TEXT | schema / products |
| products.prod_category | 保留物理名称；存档没有恢复别名 | TEXT | schema / products |
| products.prod_category_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / products |
| products.prod_category_desc | 保留物理名称；存档没有恢复别名 | TEXT | schema / products |
| products.prod_weight_class | 保留物理名称；存档没有恢复别名 | INTEGER | schema / products |
| products.prod_unit_of_measure | 保留物理名称；存档没有恢复别名 | TEXT | schema / products |
| products.prod_pack_size | 保留物理名称；存档没有恢复别名 | TEXT | schema / products |
| products.supplier_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / products |
| products.prod_status | 保留物理名称；存档没有恢复别名 | TEXT | schema / products |
| products.prod_list_price | 保留物理名称；存档没有恢复别名 | REAL | schema / products |
| products.prod_min_price | 保留物理名称；存档没有恢复别名 | REAL | schema / products |
| products.prod_total | 保留物理名称；存档没有恢复别名 | TEXT | schema / products |
| products.prod_total_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / products |
| products.prod_src_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / products |
| products.prod_eff_from | 保留物理名称；存档没有恢复别名 | DATE | schema / products |
| products.prod_eff_to | 保留物理名称；存档没有恢复别名 | DATE | schema / products |
| products.prod_valid | 保留物理名称；存档没有恢复别名 | CHAR(1) | schema / products |

## promotions

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: p

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| promotions.promo_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / promotions |
| promotions.promo_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / promotions |
| promotions.promo_subcategory | 保留物理名称；存档没有恢复别名 | TEXT | schema / promotions |
| promotions.promo_subcategory_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / promotions |
| promotions.promo_category | 保留物理名称；存档没有恢复别名 | TEXT | schema / promotions |
| promotions.promo_category_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / promotions |
| promotions.promo_cost | 保留物理名称；存档没有恢复别名 | REAL | schema / promotions |
| promotions.promo_begin_date | 保留物理名称；存档没有恢复别名 | DATE | schema / promotions |
| promotions.promo_end_date | 保留物理名称；存档没有恢复别名 | DATE | schema / promotions |
| promotions.promo_total | 保留物理名称；存档没有恢复别名 | TEXT | schema / promotions |
| promotions.promo_total_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / promotions |

## sales

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: s

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| sales.prod_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / sales |
| sales.cust_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / sales |
| sales.time_id | 保留物理名称；存档没有恢复别名 | DATE | schema / sales |
| sales.channel_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / sales |
| sales.promo_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / sales |
| sales.quantity_sold | 保留物理名称；存档没有恢复别名 | INTEGER | schema / sales |
| sales.amount_sold | 保留物理名称；存档没有恢复别名 | REAL | schema / sales |

## supplementary_demographics

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| supplementary_demographics.cust_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / supplementary_demographics |
| supplementary_demographics.education | 保留物理名称；存档没有恢复别名 | TEXT | schema / supplementary_demographics |
| supplementary_demographics.occupation | 保留物理名称；存档没有恢复别名 | TEXT | schema / supplementary_demographics |
| supplementary_demographics.household_size | 保留物理名称；存档没有恢复别名 | TEXT | schema / supplementary_demographics |
| supplementary_demographics.yrs_residence | 保留物理名称；存档没有恢复别名 | INTEGER | schema / supplementary_demographics |
| supplementary_demographics.affinity_card | 保留物理名称；存档没有恢复别名 | INTEGER | schema / supplementary_demographics |
| supplementary_demographics.cricket | 保留物理名称；存档没有恢复别名 | INTEGER | schema / supplementary_demographics |
| supplementary_demographics.baseball | 保留物理名称；存档没有恢复别名 | INTEGER | schema / supplementary_demographics |
| supplementary_demographics.tennis | 保留物理名称；存档没有恢复别名 | INTEGER | schema / supplementary_demographics |
| supplementary_demographics.soccer | 保留物理名称；存档没有恢复别名 | INTEGER | schema / supplementary_demographics |
| supplementary_demographics.golf | 保留物理名称；存档没有恢复别名 | INTEGER | schema / supplementary_demographics |
| supplementary_demographics.unknown | 保留物理名称；存档没有恢复别名 | INTEGER | schema / supplementary_demographics |
| supplementary_demographics.misc | 保留物理名称；存档没有恢复别名 | INTEGER | schema / supplementary_demographics |
| supplementary_demographics.comments | 保留物理名称；存档没有恢复别名 | TEXT | schema / supplementary_demographics |

## times

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: t

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| times.time_id | 保留物理名称；存档没有恢复别名 | DATE | schema / times |
| times.day_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / times |
| times.day_number_in_week | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.day_number_in_month | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.calendar_week_number | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.fiscal_week_number | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.week_ending_day | 保留物理名称；存档没有恢复别名 | DATE | schema / times |
| times.week_ending_day_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.calendar_month_number | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.fiscal_month_number | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.calendar_month_desc | 保留物理名称；存档没有恢复别名 | TEXT | schema / times |
| times.calendar_month_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.fiscal_month_desc | 保留物理名称；存档没有恢复别名 | TEXT | schema / times |
| times.fiscal_month_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.days_in_cal_month | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.days_in_fis_month | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.end_of_cal_month | 保留物理名称；存档没有恢复别名 | DATE | schema / times |
| times.end_of_fis_month | 保留物理名称；存档没有恢复别名 | DATE | schema / times |
| times.calendar_month_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / times |
| times.fiscal_month_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / times |
| times.calendar_quarter_desc | 保留物理名称；存档没有恢复别名 | CHAR(7) | schema / times |
| times.calendar_quarter_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.fiscal_quarter_desc | 保留物理名称；存档没有恢复别名 | CHAR(7) | schema / times |
| times.fiscal_quarter_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.days_in_cal_quarter | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.days_in_fis_quarter | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.end_of_cal_quarter | 保留物理名称；存档没有恢复别名 | DATE | schema / times |
| times.end_of_fis_quarter | 保留物理名称；存档没有恢复别名 | DATE | schema / times |
| times.calendar_quarter_number | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.fiscal_quarter_number | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.calendar_year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.calendar_year_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.fiscal_year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.fiscal_year_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.days_in_cal_year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.days_in_fis_year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / times |
| times.end_of_cal_year | 保留物理名称；存档没有恢复别名 | DATE | schema / times |
| times.end_of_fis_year | 保留物理名称；存档没有恢复别名 | DATE | schema / times |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

