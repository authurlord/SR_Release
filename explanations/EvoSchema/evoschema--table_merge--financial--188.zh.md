# EvoSchema / evoschema::table_merge::financial::188 — Schema 与业务口径解释

该数据库的存档目录包含 7 张表、54 个物理列、0 条关系，以及 7 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## account_loan

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| account_loan.account_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / account_loan |
| account_loan.district_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / account_loan |
| account_loan.frequency | 保留物理名称；存档没有恢复别名 | TEXT | schema / account_loan |
| account_loan.account_date | 保留物理名称；存档没有恢复别名 | DATE | schema / account_loan |
| account_loan.loan_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / account_loan |
| account_loan.loan_date | 保留物理名称；存档没有恢复别名 | DATE | schema / account_loan |
| account_loan.amount | 保留物理名称；存档没有恢复别名 | INTEGER | schema / account_loan |
| account_loan.duration | 保留物理名称；存档没有恢复别名 | INTEGER | schema / account_loan |
| account_loan.payments | 保留物理名称；存档没有恢复别名 | REAL | schema / account_loan |
| account_loan.status | 保留物理名称；存档没有恢复别名 | TEXT | schema / account_loan |

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
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| client.client_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / client |
| client.gender | 保留物理名称；存档没有恢复别名 | TEXT | schema / client |
| client.birth_date | 保留物理名称；存档没有恢复别名 | DATE | schema / client |
| client.district_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / client |

## disp

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| disp.disp_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / disp |
| disp.client_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / disp |
| disp.account_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / disp |
| disp.type | 保留物理名称；存档没有恢复别名 | TEXT | schema / disp |

## district

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| district.district_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / district |
| district.A2 | 保留物理名称；存档没有恢复别名 | TEXT | schema / district |
| district.A3 | 保留物理名称；存档没有恢复别名 | TEXT | schema / district |
| district.A4 | 保留物理名称；存档没有恢复别名 | TEXT | schema / district |
| district.A5 | 保留物理名称；存档没有恢复别名 | TEXT | schema / district |
| district.A6 | 保留物理名称；存档没有恢复别名 | TEXT | schema / district |
| district.A7 | 保留物理名称；存档没有恢复别名 | TEXT | schema / district |
| district.A8 | 保留物理名称；存档没有恢复别名 | INTEGER | schema / district |
| district.A9 | 保留物理名称；存档没有恢复别名 | INTEGER | schema / district |
| district.A10 | 保留物理名称；存档没有恢复别名 | REAL | schema / district |
| district.A11 | 保留物理名称；存档没有恢复别名 | INTEGER | schema / district |
| district.A12 | 保留物理名称；存档没有恢复别名 | REAL | schema / district |
| district.A13 | 保留物理名称；存档没有恢复别名 | REAL | schema / district |
| district.A14 | 保留物理名称；存档没有恢复别名 | INTEGER | schema / district |
| district.A15 | 保留物理名称；存档没有恢复别名 | INTEGER | schema / district |
| district.A16 | 保留物理名称；存档没有恢复别名 | INTEGER | schema / district |

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
SQL表别名: —

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

