# EvoSchema / evoschema::table_split::debit_card_specializing::1502 — Schema 与业务口径解释

该数据库的存档目录包含 7 张表、23 个物理列、0 条关系，以及 7 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## customers

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: c

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| customers.CustomerID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / customers |
| customers.Segment | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.Currency | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |

## CustomerTransactions

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: ct

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| CustomerTransactions.TransactionID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / CustomerTransactions |
| CustomerTransactions.CustomerID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / CustomerTransactions |
| CustomerTransactions.CardID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / CustomerTransactions |

## gasstations

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: gs

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| gasstations.GasStationID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / gasstations |
| gasstations.ChainID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / gasstations |
| gasstations.Country | 保留物理名称；存档没有恢复别名 | TEXT | schema / gasstations |
| gasstations.Segment | 保留物理名称；存档没有恢复别名 | TEXT | schema / gasstations |

## GasStationTransactions

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: gst

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| GasStationTransactions.TransactionID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / GasStationTransactions |
| GasStationTransactions.GasStationID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / GasStationTransactions |
| GasStationTransactions.ProductID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / GasStationTransactions |

## products

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| products.ProductID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / products |
| products.Description | 保留物理名称；存档没有恢复别名 | TEXT | schema / products |

## TransactionDetails

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| TransactionDetails.TransactionID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / TransactionDetails |
| TransactionDetails.Date | 保留物理名称；存档没有恢复别名 | DATE | schema / TransactionDetails |
| TransactionDetails.Time | 保留物理名称；存档没有恢复别名 | TEXT | schema / TransactionDetails |
| TransactionDetails.Amount | 保留物理名称；存档没有恢复别名 | INTEGER | schema / TransactionDetails |
| TransactionDetails.Price | 保留物理名称；存档没有恢复别名 | REAL | schema / TransactionDetails |

## yearmonth

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| yearmonth.CustomerID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / yearmonth |
| yearmonth.Date | 保留物理名称；存档没有恢复别名 | TEXT | schema / yearmonth |
| yearmonth.Consumption | 保留物理名称；存档没有恢复别名 | REAL | schema / yearmonth |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

