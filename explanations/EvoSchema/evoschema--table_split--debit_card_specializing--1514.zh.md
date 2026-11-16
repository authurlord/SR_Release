# EvoSchema / evoschema::table_split::debit_card_specializing::1514 — Schema 与业务口径解释

该数据库的存档目录包含 7 张表、23 个物理列、0 条关系，以及 7 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## customers

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| customers.CustomerID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / customers |
| customers.Segment | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.Currency | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |

## GasStationDetails

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| GasStationDetails.GasStationID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / GasStationDetails |
| GasStationDetails.ChainID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / GasStationDetails |

## GasStationLocation

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| GasStationLocation.GasStationID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / GasStationLocation |
| GasStationLocation.Country | 保留物理名称；存档没有恢复别名 | TEXT | schema / GasStationLocation |

## GasStationSegment

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| GasStationSegment.GasStationID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / GasStationSegment |
| GasStationSegment.Segment | 保留物理名称；存档没有恢复别名 | TEXT | schema / GasStationSegment |

## products

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| products.ProductID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / products |
| products.Description | 保留物理名称；存档没有恢复别名 | TEXT | schema / products |

## transactions_1k

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| transactions_1k.TransactionID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / transactions_1k |
| transactions_1k.Date | 保留物理名称；存档没有恢复别名 | DATE | schema / transactions_1k |
| transactions_1k.Time | 保留物理名称；存档没有恢复别名 | TEXT | schema / transactions_1k |
| transactions_1k.CustomerID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / transactions_1k |
| transactions_1k.CardID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / transactions_1k |
| transactions_1k.GasStationID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / transactions_1k |
| transactions_1k.ProductID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / transactions_1k |
| transactions_1k.Amount | 保留物理名称；存档没有恢复别名 | INTEGER | schema / transactions_1k |
| transactions_1k.Price | 保留物理名称；存档没有恢复别名 | REAL | schema / transactions_1k |

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

