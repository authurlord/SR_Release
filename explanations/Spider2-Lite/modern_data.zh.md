# Spider2-Lite / modern_data — Schema 与业务口径解释

该数据库的存档目录包含 17 张表、77 个物理列、0 条关系，以及 17 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## companies_dates

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: cd

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| companies_dates.company_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / companies_dates |
| companies_dates.date_joined | 保留物理名称；存档没有恢复别名 | TEXT | schema / companies_dates |
| companies_dates.year_founded | 保留物理名称；存档没有恢复别名 | INTEGER | schema / companies_dates |

## companies_funding

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: cf

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| companies_funding.company_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / companies_funding |
| companies_funding.valuation | 保留物理名称；存档没有恢复别名 | INTEGER | schema / companies_funding |
| companies_funding.funding | 保留物理名称；存档没有恢复别名 | INTEGER | schema / companies_funding |
| companies_funding.select_investors | 保留物理名称；存档没有恢复别名 | TEXT | schema / companies_funding |

## companies_industries

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: ci

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| companies_industries.company_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / companies_industries |
| companies_industries.industry | 保留物理名称；存档没有恢复别名 | TEXT | schema / companies_industries |

## income_trees

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: i

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| income_trees.zipcode | 保留物理名称；存档没有恢复别名 | INTEGER | schema / income_trees |
| income_trees.Estimate_Total | 保留物理名称；存档没有恢复别名 | INTEGER | schema / income_trees |
| income_trees.Margin_of_Error_Total | 保留物理名称；存档没有恢复别名 | INTEGER | schema / income_trees |
| income_trees.Estimate_Median_income | 保留物理名称；存档没有恢复别名 | INTEGER | schema / income_trees |
| income_trees.Margin_of_Error_Median_income | 保留物理名称；存档没有恢复别名 | INTEGER | schema / income_trees |
| income_trees.Estimate_Mean_income | 保留物理名称；存档没有恢复别名 | INTEGER | schema / income_trees |
| income_trees.Margin_of_Error_Mean_income | 保留物理名称；存档没有恢复别名 | INTEGER | schema / income_trees |

## pizza_clean_customer_orders

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: co

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| pizza_clean_customer_orders.order_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_clean_customer_orders |
| pizza_clean_customer_orders.customer_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_clean_customer_orders |
| pizza_clean_customer_orders.pizza_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_clean_customer_orders |
| pizza_clean_customer_orders.exclusions | 保留物理名称；存档没有恢复别名 | TEXT | schema / pizza_clean_customer_orders |
| pizza_clean_customer_orders.extras | 保留物理名称；存档没有恢复别名 | TEXT | schema / pizza_clean_customer_orders |
| pizza_clean_customer_orders.order_time | 保留物理名称；存档没有恢复别名 | TEXT | schema / pizza_clean_customer_orders |

## pizza_clean_runner_orders

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: ro

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| pizza_clean_runner_orders.order_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_clean_runner_orders |
| pizza_clean_runner_orders.runner_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_clean_runner_orders |
| pizza_clean_runner_orders.pickup_time | 保留物理名称；存档没有恢复别名 | TEXT | schema / pizza_clean_runner_orders |
| pizza_clean_runner_orders.distance | 保留物理名称；存档没有恢复别名 | REAL | schema / pizza_clean_runner_orders |
| pizza_clean_runner_orders.duration | 保留物理名称；存档没有恢复别名 | REAL | schema / pizza_clean_runner_orders |
| pizza_clean_runner_orders.cancellation | 保留物理名称；存档没有恢复别名 | TEXT | schema / pizza_clean_runner_orders |

## pizza_customer_orders

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: co

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| pizza_customer_orders.order_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_customer_orders |
| pizza_customer_orders.customer_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_customer_orders |
| pizza_customer_orders.pizza_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_customer_orders |
| pizza_customer_orders.exclusions | 保留物理名称；存档没有恢复别名 | TEXT | schema / pizza_customer_orders |
| pizza_customer_orders.extras | 保留物理名称；存档没有恢复别名 | TEXT | schema / pizza_customer_orders |
| pizza_customer_orders.order_time | 保留物理名称；存档没有恢复别名 | TEXT | schema / pizza_customer_orders |

## pizza_get_exclusions

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| pizza_get_exclusions.row_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_get_exclusions |
| pizza_get_exclusions.order_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_get_exclusions |
| pizza_get_exclusions.exclusions | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_get_exclusions |
| pizza_get_exclusions.total_exclusions | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_get_exclusions |

## pizza_get_extras

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| pizza_get_extras.row_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_get_extras |
| pizza_get_extras.order_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_get_extras |
| pizza_get_extras.extras | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_get_extras |
| pizza_get_extras.extras_count | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_get_extras |

## pizza_names

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: pn

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| pizza_names.pizza_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_names |
| pizza_names.pizza_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / pizza_names |

## pizza_recipes

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: r

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| pizza_recipes.pizza_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_recipes |
| pizza_recipes.toppings | 保留物理名称；存档没有恢复别名 | TEXT | schema / pizza_recipes |

## pizza_runner_orders

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| pizza_runner_orders.order_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_runner_orders |
| pizza_runner_orders.runner_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_runner_orders |
| pizza_runner_orders.pickup_time | 保留物理名称；存档没有恢复别名 | TEXT | schema / pizza_runner_orders |
| pizza_runner_orders.distance | 保留物理名称；存档没有恢复别名 | TEXT | schema / pizza_runner_orders |
| pizza_runner_orders.duration | 保留物理名称；存档没有恢复别名 | TEXT | schema / pizza_runner_orders |
| pizza_runner_orders.cancellation | 保留物理名称；存档没有恢复别名 | TEXT | schema / pizza_runner_orders |

## pizza_runners

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| pizza_runners.runner_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_runners |
| pizza_runners.registration_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / pizza_runners |

## pizza_toppings

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: pt, tp

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| pizza_toppings.topping_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / pizza_toppings |
| pizza_toppings.topping_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / pizza_toppings |

## statistics

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| statistics.date | 保留物理名称；存档没有恢复别名 | TEXT | schema / statistics |
| statistics.state | 保留物理名称；存档没有恢复别名 | TEXT | schema / statistics |
| statistics.total_cases | 保留物理名称；存档没有恢复别名 | INTEGER | schema / statistics |
| statistics.total_deaths | 保留物理名称；存档没有恢复别名 | INTEGER | schema / statistics |

## trees

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: t

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| trees.idx | 保留物理名称；存档没有恢复别名 | INTEGER | schema / trees |
| trees.tree_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / trees |
| trees.tree_dbh | 保留物理名称；存档没有恢复别名 | INTEGER | schema / trees |
| trees.stump_diam | 保留物理名称；存档没有恢复别名 | INTEGER | schema / trees |
| trees.status | 保留物理名称；存档没有恢复别名 | TEXT | schema / trees |
| trees.health | 保留物理名称；存档没有恢复别名 | TEXT | schema / trees |
| trees.spc_latin | 保留物理名称；存档没有恢复别名 | TEXT | schema / trees |
| trees.spc_common | 保留物理名称；存档没有恢复别名 | TEXT | schema / trees |
| trees.address | 保留物理名称；存档没有恢复别名 | TEXT | schema / trees |
| trees.zipcode | 保留物理名称；存档没有恢复别名 | INTEGER | schema / trees |
| trees.borocode | 保留物理名称；存档没有恢复别名 | INTEGER | schema / trees |
| trees.boroname | 保留物理名称；存档没有恢复别名 | TEXT | schema / trees |
| trees.nta_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / trees |
| trees.state | 保留物理名称；存档没有恢复别名 | TEXT | schema / trees |
| trees.latitude | 保留物理名称；存档没有恢复别名 | REAL | schema / trees |
| trees.longitude | 保留物理名称；存档没有恢复别名 | REAL | schema / trees |

## word_list

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| word_list.words | 保留物理名称；存档没有恢复别名 | TEXT | schema / word_list |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

