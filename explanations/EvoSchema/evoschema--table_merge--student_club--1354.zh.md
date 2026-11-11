# EvoSchema / evoschema::table_merge::student_club::1354 — Schema 与业务口径解释

该数据库的存档目录包含 7 张表、48 个物理列、0 条关系，以及 7 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## attendance

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| attendance.link_to_event | 保留物理名称；存档没有恢复别名 | TEXT | schema / attendance |
| attendance.link_to_member | 保留物理名称；存档没有恢复别名 | TEXT | schema / attendance |

## budget

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| budget.budget_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / budget |
| budget.category | 保留物理名称；存档没有恢复别名 | TEXT | schema / budget |
| budget.spent | 保留物理名称；存档没有恢复别名 | REAL | schema / budget |
| budget.remaining | 保留物理名称；存档没有恢复别名 | REAL | schema / budget |
| budget.amount | 保留物理名称；存档没有恢复别名 | INTEGER | schema / budget |
| budget.event_status | 保留物理名称；存档没有恢复别名 | TEXT | schema / budget |
| budget.link_to_event | 保留物理名称；存档没有恢复别名 | TEXT | schema / budget |

## event

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| event.event_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / event |
| event.event_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / event |
| event.event_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / event |
| event.type | 保留物理名称；存档没有恢复别名 | TEXT | schema / event |
| event.notes | 保留物理名称；存档没有恢复别名 | TEXT | schema / event |
| event.location | 保留物理名称；存档没有恢复别名 | TEXT | schema / event |
| event.status | 保留物理名称；存档没有恢复别名 | TEXT | schema / event |

## expense

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| expense.expense_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / expense |
| expense.expense_description | 保留物理名称；存档没有恢复别名 | TEXT | schema / expense |
| expense.expense_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / expense |
| expense.cost | 保留物理名称；存档没有恢复别名 | REAL | schema / expense |
| expense.approved | 保留物理名称；存档没有恢复别名 | TEXT | schema / expense |
| expense.link_to_member | 保留物理名称；存档没有恢复别名 | TEXT | schema / expense |
| expense.link_to_budget | 保留物理名称；存档没有恢复别名 | TEXT | schema / expense |

## income

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| income.income_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / income |
| income.date_received | 保留物理名称；存档没有恢复别名 | TEXT | schema / income |
| income.amount | 保留物理名称；存档没有恢复别名 | INTEGER | schema / income |
| income.source | 保留物理名称；存档没有恢复别名 | TEXT | schema / income |
| income.notes | 保留物理名称；存档没有恢复别名 | TEXT | schema / income |
| income.link_to_member | 保留物理名称；存档没有恢复别名 | TEXT | schema / income |

## member_major

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| member_major.member_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / member_major |
| member_major.first_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / member_major |
| member_major.last_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / member_major |
| member_major.email | 保留物理名称；存档没有恢复别名 | TEXT | schema / member_major |
| member_major.position | 保留物理名称；存档没有恢复别名 | TEXT | schema / member_major |
| member_major.t_shirt_size | 保留物理名称；存档没有恢复别名 | TEXT | schema / member_major |
| member_major.phone | 保留物理名称；存档没有恢复别名 | TEXT | schema / member_major |
| member_major.zip | 保留物理名称；存档没有恢复别名 | INTEGER | schema / member_major |
| member_major.link_to_major | 保留物理名称；存档没有恢复别名 | TEXT | schema / member_major |
| member_major.major_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / member_major |
| member_major.major_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / member_major |
| member_major.department | 保留物理名称；存档没有恢复别名 | TEXT | schema / member_major |
| member_major.college | 保留物理名称；存档没有恢复别名 | TEXT | schema / member_major |

## zip_code

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| zip_code.zip_code | 保留物理名称；存档没有恢复别名 | INTEGER | schema / zip_code |
| zip_code.type | 保留物理名称；存档没有恢复别名 | TEXT | schema / zip_code |
| zip_code.city | 保留物理名称；存档没有恢复别名 | TEXT | schema / zip_code |
| zip_code.county | 保留物理名称；存档没有恢复别名 | TEXT | schema / zip_code |
| zip_code.state | 保留物理名称；存档没有恢复别名 | TEXT | schema / zip_code |
| zip_code.short_state | 保留物理名称；存档没有恢复别名 | TEXT | schema / zip_code |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

