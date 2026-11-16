# Spider2-Lite / modern_data — Schema and business semantics

The saved catalogue for this database contains 17 tables, 77 physical columns, 0 relationships and 17 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## companies_dates

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: cd

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| companies_dates.company_id | Physical name retained; no saved recovered alias | INTEGER | schema / companies_dates |
| companies_dates.date_joined | Physical name retained; no saved recovered alias | TEXT | schema / companies_dates |
| companies_dates.year_founded | Physical name retained; no saved recovered alias | INTEGER | schema / companies_dates |

## companies_funding

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: cf

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| companies_funding.company_id | Physical name retained; no saved recovered alias | INTEGER | schema / companies_funding |
| companies_funding.valuation | Physical name retained; no saved recovered alias | INTEGER | schema / companies_funding |
| companies_funding.funding | Physical name retained; no saved recovered alias | INTEGER | schema / companies_funding |
| companies_funding.select_investors | Physical name retained; no saved recovered alias | TEXT | schema / companies_funding |

## companies_industries

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: ci

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| companies_industries.company_id | Physical name retained; no saved recovered alias | INTEGER | schema / companies_industries |
| companies_industries.industry | Physical name retained; no saved recovered alias | TEXT | schema / companies_industries |

## income_trees

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: i

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| income_trees.zipcode | Physical name retained; no saved recovered alias | INTEGER | schema / income_trees |
| income_trees.Estimate_Total | Physical name retained; no saved recovered alias | INTEGER | schema / income_trees |
| income_trees.Margin_of_Error_Total | Physical name retained; no saved recovered alias | INTEGER | schema / income_trees |
| income_trees.Estimate_Median_income | Physical name retained; no saved recovered alias | INTEGER | schema / income_trees |
| income_trees.Margin_of_Error_Median_income | Physical name retained; no saved recovered alias | INTEGER | schema / income_trees |
| income_trees.Estimate_Mean_income | Physical name retained; no saved recovered alias | INTEGER | schema / income_trees |
| income_trees.Margin_of_Error_Mean_income | Physical name retained; no saved recovered alias | INTEGER | schema / income_trees |

## pizza_clean_customer_orders

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: co

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| pizza_clean_customer_orders.order_id | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_clean_customer_orders |
| pizza_clean_customer_orders.customer_id | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_clean_customer_orders |
| pizza_clean_customer_orders.pizza_id | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_clean_customer_orders |
| pizza_clean_customer_orders.exclusions | Physical name retained; no saved recovered alias | TEXT | schema / pizza_clean_customer_orders |
| pizza_clean_customer_orders.extras | Physical name retained; no saved recovered alias | TEXT | schema / pizza_clean_customer_orders |
| pizza_clean_customer_orders.order_time | Physical name retained; no saved recovered alias | TEXT | schema / pizza_clean_customer_orders |

## pizza_clean_runner_orders

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: ro

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| pizza_clean_runner_orders.order_id | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_clean_runner_orders |
| pizza_clean_runner_orders.runner_id | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_clean_runner_orders |
| pizza_clean_runner_orders.pickup_time | Physical name retained; no saved recovered alias | TEXT | schema / pizza_clean_runner_orders |
| pizza_clean_runner_orders.distance | Physical name retained; no saved recovered alias | REAL | schema / pizza_clean_runner_orders |
| pizza_clean_runner_orders.duration | Physical name retained; no saved recovered alias | REAL | schema / pizza_clean_runner_orders |
| pizza_clean_runner_orders.cancellation | Physical name retained; no saved recovered alias | TEXT | schema / pizza_clean_runner_orders |

## pizza_customer_orders

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: co

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| pizza_customer_orders.order_id | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_customer_orders |
| pizza_customer_orders.customer_id | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_customer_orders |
| pizza_customer_orders.pizza_id | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_customer_orders |
| pizza_customer_orders.exclusions | Physical name retained; no saved recovered alias | TEXT | schema / pizza_customer_orders |
| pizza_customer_orders.extras | Physical name retained; no saved recovered alias | TEXT | schema / pizza_customer_orders |
| pizza_customer_orders.order_time | Physical name retained; no saved recovered alias | TEXT | schema / pizza_customer_orders |

## pizza_get_exclusions

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| pizza_get_exclusions.row_id | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_get_exclusions |
| pizza_get_exclusions.order_id | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_get_exclusions |
| pizza_get_exclusions.exclusions | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_get_exclusions |
| pizza_get_exclusions.total_exclusions | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_get_exclusions |

## pizza_get_extras

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| pizza_get_extras.row_id | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_get_extras |
| pizza_get_extras.order_id | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_get_extras |
| pizza_get_extras.extras | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_get_extras |
| pizza_get_extras.extras_count | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_get_extras |

## pizza_names

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: pn

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| pizza_names.pizza_id | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_names |
| pizza_names.pizza_name | Physical name retained; no saved recovered alias | TEXT | schema / pizza_names |

## pizza_recipes

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: r

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| pizza_recipes.pizza_id | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_recipes |
| pizza_recipes.toppings | Physical name retained; no saved recovered alias | TEXT | schema / pizza_recipes |

## pizza_runner_orders

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| pizza_runner_orders.order_id | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_runner_orders |
| pizza_runner_orders.runner_id | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_runner_orders |
| pizza_runner_orders.pickup_time | Physical name retained; no saved recovered alias | TEXT | schema / pizza_runner_orders |
| pizza_runner_orders.distance | Physical name retained; no saved recovered alias | TEXT | schema / pizza_runner_orders |
| pizza_runner_orders.duration | Physical name retained; no saved recovered alias | TEXT | schema / pizza_runner_orders |
| pizza_runner_orders.cancellation | Physical name retained; no saved recovered alias | TEXT | schema / pizza_runner_orders |

## pizza_runners

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| pizza_runners.runner_id | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_runners |
| pizza_runners.registration_date | Physical name retained; no saved recovered alias | TEXT | schema / pizza_runners |

## pizza_toppings

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: pt, tp

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| pizza_toppings.topping_id | Physical name retained; no saved recovered alias | INTEGER | schema / pizza_toppings |
| pizza_toppings.topping_name | Physical name retained; no saved recovered alias | TEXT | schema / pizza_toppings |

## statistics

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| statistics.date | Physical name retained; no saved recovered alias | TEXT | schema / statistics |
| statistics.state | Physical name retained; no saved recovered alias | TEXT | schema / statistics |
| statistics.total_cases | Physical name retained; no saved recovered alias | INTEGER | schema / statistics |
| statistics.total_deaths | Physical name retained; no saved recovered alias | INTEGER | schema / statistics |

## trees

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: t

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| trees.idx | Physical name retained; no saved recovered alias | INTEGER | schema / trees |
| trees.tree_id | Physical name retained; no saved recovered alias | INTEGER | schema / trees |
| trees.tree_dbh | Physical name retained; no saved recovered alias | INTEGER | schema / trees |
| trees.stump_diam | Physical name retained; no saved recovered alias | INTEGER | schema / trees |
| trees.status | Physical name retained; no saved recovered alias | TEXT | schema / trees |
| trees.health | Physical name retained; no saved recovered alias | TEXT | schema / trees |
| trees.spc_latin | Physical name retained; no saved recovered alias | TEXT | schema / trees |
| trees.spc_common | Physical name retained; no saved recovered alias | TEXT | schema / trees |
| trees.address | Physical name retained; no saved recovered alias | TEXT | schema / trees |
| trees.zipcode | Physical name retained; no saved recovered alias | INTEGER | schema / trees |
| trees.borocode | Physical name retained; no saved recovered alias | INTEGER | schema / trees |
| trees.boroname | Physical name retained; no saved recovered alias | TEXT | schema / trees |
| trees.nta_name | Physical name retained; no saved recovered alias | TEXT | schema / trees |
| trees.state | Physical name retained; no saved recovered alias | TEXT | schema / trees |
| trees.latitude | Physical name retained; no saved recovered alias | REAL | schema / trees |
| trees.longitude | Physical name retained; no saved recovered alias | REAL | schema / trees |

## word_list

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| word_list.words | Physical name retained; no saved recovered alias | TEXT | schema / word_list |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

