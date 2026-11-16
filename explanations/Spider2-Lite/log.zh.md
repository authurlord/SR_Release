# Spider2-Lite / log — Schema 与业务口径解释

该数据库的存档目录包含 19 张表、88 个物理列、0 条关系，以及 19 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## access_log

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| access_log.session | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / access_log |
| access_log.user_id | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / access_log |
| access_log.action | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / access_log |
| access_log.stamp | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / access_log |

## action_log

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| action_log.session | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / action_log |
| action_log.user_id | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / action_log |
| action_log.action | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / action_log |
| action_log.category | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / action_log |
| action_log.products | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / action_log |
| action_log.amount | 保留物理名称；存档没有恢复别名 | INTEGER | schema / action_log |
| action_log.stamp | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / action_log |

## action_log_with_ip

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| action_log_with_ip.session | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / action_log_with_ip |
| action_log_with_ip.user_id | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / action_log_with_ip |
| action_log_with_ip.action | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / action_log_with_ip |
| action_log_with_ip.ip | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / action_log_with_ip |
| action_log_with_ip.stamp | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / action_log_with_ip |

## action_log_with_noise

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| action_log_with_noise.stamp | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / action_log_with_noise |
| action_log_with_noise.session | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / action_log_with_noise |
| action_log_with_noise.action | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / action_log_with_noise |
| action_log_with_noise.products | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / action_log_with_noise |
| action_log_with_noise.url | 保留物理名称；存档没有恢复别名 | TEXT | schema / action_log_with_noise |
| action_log_with_noise.ip | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / action_log_with_noise |
| action_log_with_noise.user_agent | 保留物理名称；存档没有恢复别名 | TEXT | schema / action_log_with_noise |

## activity_log

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: a

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| activity_log.stamp | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / activity_log |
| activity_log.session | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / activity_log |
| activity_log.action | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / activity_log |
| activity_log.option | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / activity_log |
| activity_log.path | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / activity_log |
| activity_log.search_type | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / activity_log |

## app1_mst_users

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| app1_mst_users.user_id | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / app1_mst_users |
| app1_mst_users.name | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / app1_mst_users |
| app1_mst_users.email | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / app1_mst_users |

## app2_mst_users

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| app2_mst_users.user_id | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / app2_mst_users |
| app2_mst_users.name | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / app2_mst_users |
| app2_mst_users.phone | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / app2_mst_users |

## dup_action_log

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| dup_action_log.stamp | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / dup_action_log |
| dup_action_log.session | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / dup_action_log |
| dup_action_log.user_id | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / dup_action_log |
| dup_action_log.action | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / dup_action_log |
| dup_action_log.products | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / dup_action_log |

## form_error_log

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| form_error_log.stamp | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / form_error_log |
| form_error_log.session | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / form_error_log |
| form_error_log.form | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / form_error_log |
| form_error_log.field | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / form_error_log |
| form_error_log.error_type | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / form_error_log |
| form_error_log.value | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / form_error_log |

## form_log

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| form_log.stamp | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / form_log |
| form_log.session | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / form_log |
| form_log.action | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / form_log |
| form_log.path | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / form_log |
| form_log.status | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / form_log |

## invalid_action_log

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| invalid_action_log.stamp | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / invalid_action_log |
| invalid_action_log.session | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / invalid_action_log |
| invalid_action_log.user_id | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / invalid_action_log |
| invalid_action_log.action | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / invalid_action_log |
| invalid_action_log.category | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / invalid_action_log |
| invalid_action_log.products | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / invalid_action_log |
| invalid_action_log.amount | 保留物理名称；存档没有恢复别名 | INTEGER | schema / invalid_action_log |

## mst_categories

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| mst_categories.id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / mst_categories |
| mst_categories.name | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / mst_categories |
| mst_categories.stamp | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / mst_categories |

## mst_products_20161201

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| mst_products_20161201.product_id | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / mst_products_20161201 |
| mst_products_20161201.name | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / mst_products_20161201 |
| mst_products_20161201.price | 保留物理名称；存档没有恢复别名 | INTEGER | schema / mst_products_20161201 |
| mst_products_20161201.updated_at | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / mst_products_20161201 |

## mst_products_20170101

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| mst_products_20170101.product_id | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / mst_products_20170101 |
| mst_products_20170101.name | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / mst_products_20170101 |
| mst_products_20170101.price | 保留物理名称；存档没有恢复别名 | INTEGER | schema / mst_products_20170101 |
| mst_products_20170101.updated_at | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / mst_products_20170101 |

## mst_users

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| mst_users.user_id | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / mst_users |
| mst_users.sex | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / mst_users |
| mst_users.birth_date | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / mst_users |
| mst_users.register_date | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / mst_users |
| mst_users.register_device | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / mst_users |
| mst_users.withdraw_date | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / mst_users |

## mst_users_with_card_number

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| mst_users_with_card_number.user_id | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / mst_users_with_card_number |
| mst_users_with_card_number.card_number | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / mst_users_with_card_number |

## product_sales

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| product_sales.category_name | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / product_sales |
| product_sales.product_id | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / product_sales |
| product_sales.sales | 保留物理名称；存档没有恢复别名 | INTEGER | schema / product_sales |

## purchase_log

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| purchase_log.purchase_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / purchase_log |
| purchase_log.user_id | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / purchase_log |
| purchase_log.amount | 保留物理名称；存档没有恢复别名 | INTEGER | schema / purchase_log |
| purchase_log.stamp | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / purchase_log |

## read_log

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| read_log.stamp | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / read_log |
| read_log.session | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / read_log |
| read_log.action | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / read_log |
| read_log.url | 保留物理名称；存档没有恢复别名 | varchar(255) | schema / read_log |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

