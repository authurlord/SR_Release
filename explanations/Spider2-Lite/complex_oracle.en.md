# Spider2-Lite / complex_oracle — Schema and business semantics

The saved catalogue for this database contains 10 tables, 140 physical columns, 0 relationships and 10 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## channels

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: ch

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| channels.channel_id | Physical name retained; no saved recovered alias | INTEGER | schema / channels |
| channels.channel_desc | Physical name retained; no saved recovered alias | TEXT | schema / channels |
| channels.channel_class | Physical name retained; no saved recovered alias | TEXT | schema / channels |
| channels.channel_class_id | Physical name retained; no saved recovered alias | INTEGER | schema / channels |
| channels.channel_total | Physical name retained; no saved recovered alias | TEXT | schema / channels |
| channels.channel_total_id | Physical name retained; no saved recovered alias | INTEGER | schema / channels |

## costs

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: c

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| costs.prod_id | Physical name retained; no saved recovered alias | INTEGER | schema / costs |
| costs.time_id | Physical name retained; no saved recovered alias | DATE | schema / costs |
| costs.promo_id | Physical name retained; no saved recovered alias | INTEGER | schema / costs |
| costs.channel_id | Physical name retained; no saved recovered alias | INTEGER | schema / costs |
| costs.unit_cost | Physical name retained; no saved recovered alias | REAL | schema / costs |
| costs.unit_price | Physical name retained; no saved recovered alias | REAL | schema / costs |

## countries

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: co

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| countries.country_id | Physical name retained; no saved recovered alias | INTEGER | schema / countries |
| countries.country_iso_code | Physical name retained; no saved recovered alias | CHAR(2) | schema / countries |
| countries.country_name | Physical name retained; no saved recovered alias | TEXT | schema / countries |
| countries.country_subregion | Physical name retained; no saved recovered alias | TEXT | schema / countries |
| countries.country_subregion_id | Physical name retained; no saved recovered alias | INTEGER | schema / countries |
| countries.country_region | Physical name retained; no saved recovered alias | TEXT | schema / countries |
| countries.country_region_id | Physical name retained; no saved recovered alias | INTEGER | schema / countries |
| countries.country_total | Physical name retained; no saved recovered alias | TEXT | schema / countries |
| countries.country_total_id | Physical name retained; no saved recovered alias | INTEGER | schema / countries |

## currency

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: c

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| currency.country | Physical name retained; no saved recovered alias | TEXT | schema / currency |
| currency.year | Physical name retained; no saved recovered alias | INTEGER | schema / currency |
| currency.month | Physical name retained; no saved recovered alias | INTEGER | schema / currency |
| currency.to_us | Physical name retained; no saved recovered alias | REAL | schema / currency |

## customers

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: c, cu

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| customers.cust_id | Physical name retained; no saved recovered alias | INTEGER | schema / customers |
| customers.cust_first_name | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.cust_last_name | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.cust_gender | Physical name retained; no saved recovered alias | CHAR(1) | schema / customers |
| customers.cust_year_of_birth | Physical name retained; no saved recovered alias | INTEGER | schema / customers |
| customers.cust_marital_status | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.cust_street_address | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.cust_postal_code | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.cust_city | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.cust_city_id | Physical name retained; no saved recovered alias | INTEGER | schema / customers |
| customers.cust_state_province | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.cust_state_province_id | Physical name retained; no saved recovered alias | INTEGER | schema / customers |
| customers.country_id | Physical name retained; no saved recovered alias | INTEGER | schema / customers |
| customers.cust_main_phone_number | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.cust_income_level | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.cust_credit_limit | Physical name retained; no saved recovered alias | REAL | schema / customers |
| customers.cust_email | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.cust_total | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.cust_total_id | Physical name retained; no saved recovered alias | INTEGER | schema / customers |
| customers.cust_src_id | Physical name retained; no saved recovered alias | INTEGER | schema / customers |
| customers.cust_eff_from | Physical name retained; no saved recovered alias | DATE | schema / customers |
| customers.cust_eff_to | Physical name retained; no saved recovered alias | DATE | schema / customers |
| customers.cust_valid | Physical name retained; no saved recovered alias | CHAR(1) | schema / customers |

## products

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| products.prod_id | Physical name retained; no saved recovered alias | INTEGER | schema / products |
| products.prod_name | Physical name retained; no saved recovered alias | TEXT | schema / products |
| products.prod_desc | Physical name retained; no saved recovered alias | TEXT | schema / products |
| products.prod_subcategory | Physical name retained; no saved recovered alias | TEXT | schema / products |
| products.prod_subcategory_id | Physical name retained; no saved recovered alias | INTEGER | schema / products |
| products.prod_subcategory_desc | Physical name retained; no saved recovered alias | TEXT | schema / products |
| products.prod_category | Physical name retained; no saved recovered alias | TEXT | schema / products |
| products.prod_category_id | Physical name retained; no saved recovered alias | INTEGER | schema / products |
| products.prod_category_desc | Physical name retained; no saved recovered alias | TEXT | schema / products |
| products.prod_weight_class | Physical name retained; no saved recovered alias | INTEGER | schema / products |
| products.prod_unit_of_measure | Physical name retained; no saved recovered alias | TEXT | schema / products |
| products.prod_pack_size | Physical name retained; no saved recovered alias | TEXT | schema / products |
| products.supplier_id | Physical name retained; no saved recovered alias | INTEGER | schema / products |
| products.prod_status | Physical name retained; no saved recovered alias | TEXT | schema / products |
| products.prod_list_price | Physical name retained; no saved recovered alias | REAL | schema / products |
| products.prod_min_price | Physical name retained; no saved recovered alias | REAL | schema / products |
| products.prod_total | Physical name retained; no saved recovered alias | TEXT | schema / products |
| products.prod_total_id | Physical name retained; no saved recovered alias | INTEGER | schema / products |
| products.prod_src_id | Physical name retained; no saved recovered alias | INTEGER | schema / products |
| products.prod_eff_from | Physical name retained; no saved recovered alias | DATE | schema / products |
| products.prod_eff_to | Physical name retained; no saved recovered alias | DATE | schema / products |
| products.prod_valid | Physical name retained; no saved recovered alias | CHAR(1) | schema / products |

## promotions

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: p

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| promotions.promo_id | Physical name retained; no saved recovered alias | INTEGER | schema / promotions |
| promotions.promo_name | Physical name retained; no saved recovered alias | TEXT | schema / promotions |
| promotions.promo_subcategory | Physical name retained; no saved recovered alias | TEXT | schema / promotions |
| promotions.promo_subcategory_id | Physical name retained; no saved recovered alias | INTEGER | schema / promotions |
| promotions.promo_category | Physical name retained; no saved recovered alias | TEXT | schema / promotions |
| promotions.promo_category_id | Physical name retained; no saved recovered alias | INTEGER | schema / promotions |
| promotions.promo_cost | Physical name retained; no saved recovered alias | REAL | schema / promotions |
| promotions.promo_begin_date | Physical name retained; no saved recovered alias | DATE | schema / promotions |
| promotions.promo_end_date | Physical name retained; no saved recovered alias | DATE | schema / promotions |
| promotions.promo_total | Physical name retained; no saved recovered alias | TEXT | schema / promotions |
| promotions.promo_total_id | Physical name retained; no saved recovered alias | INTEGER | schema / promotions |

## sales

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: s

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| sales.prod_id | Physical name retained; no saved recovered alias | INTEGER | schema / sales |
| sales.cust_id | Physical name retained; no saved recovered alias | INTEGER | schema / sales |
| sales.time_id | Physical name retained; no saved recovered alias | DATE | schema / sales |
| sales.channel_id | Physical name retained; no saved recovered alias | INTEGER | schema / sales |
| sales.promo_id | Physical name retained; no saved recovered alias | INTEGER | schema / sales |
| sales.quantity_sold | Physical name retained; no saved recovered alias | INTEGER | schema / sales |
| sales.amount_sold | Physical name retained; no saved recovered alias | REAL | schema / sales |

## supplementary_demographics

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| supplementary_demographics.cust_id | Physical name retained; no saved recovered alias | INTEGER | schema / supplementary_demographics |
| supplementary_demographics.education | Physical name retained; no saved recovered alias | TEXT | schema / supplementary_demographics |
| supplementary_demographics.occupation | Physical name retained; no saved recovered alias | TEXT | schema / supplementary_demographics |
| supplementary_demographics.household_size | Physical name retained; no saved recovered alias | TEXT | schema / supplementary_demographics |
| supplementary_demographics.yrs_residence | Physical name retained; no saved recovered alias | INTEGER | schema / supplementary_demographics |
| supplementary_demographics.affinity_card | Physical name retained; no saved recovered alias | INTEGER | schema / supplementary_demographics |
| supplementary_demographics.cricket | Physical name retained; no saved recovered alias | INTEGER | schema / supplementary_demographics |
| supplementary_demographics.baseball | Physical name retained; no saved recovered alias | INTEGER | schema / supplementary_demographics |
| supplementary_demographics.tennis | Physical name retained; no saved recovered alias | INTEGER | schema / supplementary_demographics |
| supplementary_demographics.soccer | Physical name retained; no saved recovered alias | INTEGER | schema / supplementary_demographics |
| supplementary_demographics.golf | Physical name retained; no saved recovered alias | INTEGER | schema / supplementary_demographics |
| supplementary_demographics.unknown | Physical name retained; no saved recovered alias | INTEGER | schema / supplementary_demographics |
| supplementary_demographics.misc | Physical name retained; no saved recovered alias | INTEGER | schema / supplementary_demographics |
| supplementary_demographics.comments | Physical name retained; no saved recovered alias | TEXT | schema / supplementary_demographics |

## times

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: t

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| times.time_id | Physical name retained; no saved recovered alias | DATE | schema / times |
| times.day_name | Physical name retained; no saved recovered alias | TEXT | schema / times |
| times.day_number_in_week | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.day_number_in_month | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.calendar_week_number | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.fiscal_week_number | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.week_ending_day | Physical name retained; no saved recovered alias | DATE | schema / times |
| times.week_ending_day_id | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.calendar_month_number | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.fiscal_month_number | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.calendar_month_desc | Physical name retained; no saved recovered alias | TEXT | schema / times |
| times.calendar_month_id | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.fiscal_month_desc | Physical name retained; no saved recovered alias | TEXT | schema / times |
| times.fiscal_month_id | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.days_in_cal_month | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.days_in_fis_month | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.end_of_cal_month | Physical name retained; no saved recovered alias | DATE | schema / times |
| times.end_of_fis_month | Physical name retained; no saved recovered alias | DATE | schema / times |
| times.calendar_month_name | Physical name retained; no saved recovered alias | TEXT | schema / times |
| times.fiscal_month_name | Physical name retained; no saved recovered alias | TEXT | schema / times |
| times.calendar_quarter_desc | Physical name retained; no saved recovered alias | CHAR(7) | schema / times |
| times.calendar_quarter_id | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.fiscal_quarter_desc | Physical name retained; no saved recovered alias | CHAR(7) | schema / times |
| times.fiscal_quarter_id | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.days_in_cal_quarter | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.days_in_fis_quarter | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.end_of_cal_quarter | Physical name retained; no saved recovered alias | DATE | schema / times |
| times.end_of_fis_quarter | Physical name retained; no saved recovered alias | DATE | schema / times |
| times.calendar_quarter_number | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.fiscal_quarter_number | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.calendar_year | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.calendar_year_id | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.fiscal_year | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.fiscal_year_id | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.days_in_cal_year | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.days_in_fis_year | Physical name retained; no saved recovered alias | INTEGER | schema / times |
| times.end_of_cal_year | Physical name retained; no saved recovered alias | DATE | schema / times |
| times.end_of_fis_year | Physical name retained; no saved recovered alias | DATE | schema / times |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

