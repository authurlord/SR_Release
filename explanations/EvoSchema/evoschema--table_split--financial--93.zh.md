# EvoSchema / evoschema::table_split::financial::93 — Schema 与业务口径解释

该数据库的存档目录包含 10 张表、57 个物理列、0 条关系，以及 10 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## account

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: a

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| account.account_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / account |
| account.district_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / account |
| account.frequency | 保留物理名称；存档没有恢复别名 | TEXT | schema / account |
| account.date | 保留物理名称；存档没有恢复别名 | DATE | schema / account |

## card

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| card.card_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / card |
| card.disp_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / card |
| card.type | 保留物理名称；存档没有恢复别名 | TEXT | schema / card |
| card.issued | 保留物理名称；存档没有恢复别名 | DATE | schema / card |

## client

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: c

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| client.client_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / client |
| client.gender | 保留物理名称；存档没有恢复别名 | TEXT | schema / client |
| client.birth_date | 保留物理名称；存档没有恢复别名 | DATE | schema / client |
| client.district_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / client |

## disp

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: dp

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| disp.disp_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / disp |
| disp.client_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / disp |
| disp.account_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / disp |
| disp.type | 保留物理名称；存档没有恢复别名 | TEXT | schema / disp |

## district_info

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: d

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| district_info.district_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / district_info |
| district_info.A2 | 保留物理名称；存档没有恢复别名 | TEXT | schema / district_info |
| district_info.A3 | 保留物理名称；存档没有恢复别名 | TEXT | schema / district_info |

## district_numeric

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| district_numeric.district_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / district_numeric |
| district_numeric.A8 | 保留物理名称；存档没有恢复别名 | INTEGER | schema / district_numeric |
| district_numeric.A9 | 保留物理名称；存档没有恢复别名 | INTEGER | schema / district_numeric |
| district_numeric.A11 | 保留物理名称；存档没有恢复别名 | INTEGER | schema / district_numeric |
| district_numeric.A14 | 保留物理名称；存档没有恢复别名 | INTEGER | schema / district_numeric |
| district_numeric.A15 | 保留物理名称；存档没有恢复别名 | INTEGER | schema / district_numeric |
| district_numeric.A16 | 保留物理名称；存档没有恢复别名 | INTEGER | schema / district_numeric |

## district_real

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| district_real.district_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / district_real |
| district_real.A4 | 保留物理名称；存档没有恢复别名 | TEXT | schema / district_real |
| district_real.A5 | 保留物理名称；存档没有恢复别名 | TEXT | schema / district_real |
| district_real.A6 | 保留物理名称；存档没有恢复别名 | TEXT | schema / district_real |
| district_real.A7 | 保留物理名称；存档没有恢复别名 | TEXT | schema / district_real |
| district_real.A10 | 保留物理名称；存档没有恢复别名 | REAL | schema / district_real |
| district_real.A12 | 保留物理名称；存档没有恢复别名 | REAL | schema / district_real |
| district_real.A13 | 保留物理名称；存档没有恢复别名 | REAL | schema / district_real |

## loan

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| loan.loan_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / loan |
| loan.account_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / loan |
| loan.date | 保留物理名称；存档没有恢复别名 | DATE | schema / loan |
| loan.amount | 保留物理名称；存档没有恢复别名 | INTEGER | schema / loan |
| loan.duration | 保留物理名称；存档没有恢复别名 | INTEGER | schema / loan |
| loan.payments | 保留物理名称；存档没有恢复别名 | REAL | schema / loan |
| loan.status | 保留物理名称；存档没有恢复别名 | TEXT | schema / loan |

## order

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| order.order_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / order |
| order.account_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / order |
| order.bank_to | 保留物理名称；存档没有恢复别名 | TEXT | schema / order |
| order.account_to | 保留物理名称；存档没有恢复别名 | INTEGER | schema / order |
| order.amount | 保留物理名称；存档没有恢复别名 | REAL | schema / order |
| order.k_symbol | 保留物理名称；存档没有恢复别名 | TEXT | schema / order |

## trans

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: t

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| trans.trans_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / trans |
| trans.account_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / trans |
| trans.date | 保留物理名称；存档没有恢复别名 | DATE | schema / trans |
| trans.type | 保留物理名称；存档没有恢复别名 | TEXT | schema / trans |
| trans.operation | 保留物理名称；存档没有恢复别名 | TEXT | schema / trans |
| trans.amount | 保留物理名称；存档没有恢复别名 | INTEGER | schema / trans |
| trans.balance | 保留物理名称；存档没有恢复别名 | INTEGER | schema / trans |
| trans.k_symbol | 保留物理名称；存档没有恢复别名 | TEXT | schema / trans |
| trans.bank | 保留物理名称；存档没有恢复别名 | TEXT | schema / trans |
| trans.account | 保留物理名称；存档没有恢复别名 | INTEGER | schema / trans |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

