# Spider2-Lite / WWE — Schema 与业务口径解释

该数据库的存档目录包含 9 张表、33 个物理列、0 条关系，以及 9 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## Belts

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Belts.id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Belts |
| Belts.name | 保留物理名称；存档没有恢复别名 | TEXT | schema / Belts |

## Cards

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: c

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Cards.id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Cards |
| Cards.table_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Cards |
| Cards.location_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Cards |
| Cards.promotion_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Cards |
| Cards.event_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / Cards |
| Cards.event_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Cards |
| Cards.url | 保留物理名称；存档没有恢复别名 | TEXT | schema / Cards |
| Cards.info_html | 保留物理名称；存档没有恢复别名 | TEXT | schema / Cards |
| Cards.match_html | 保留物理名称；存档没有恢复别名 | TEXT | schema / Cards |

## Events

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Events.id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Events |
| Events.name | 保留物理名称；存档没有恢复别名 | TEXT | schema / Events |

## Locations

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Locations.id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Locations |
| Locations.name | 保留物理名称；存档没有恢复别名 | TEXT | schema / Locations |

## Match_Types

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Match_Types.id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Match_Types |
| Match_Types.name | 保留物理名称；存档没有恢复别名 | TEXT | schema / Match_Types |

## Matches

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: m

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Matches.id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Matches |
| Matches.card_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Matches |
| Matches.winner_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / Matches |
| Matches.win_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / Matches |
| Matches.loser_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / Matches |
| Matches.match_type_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / Matches |
| Matches.duration | 保留物理名称；存档没有恢复别名 | TEXT | schema / Matches |
| Matches.title_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / Matches |
| Matches.title_change | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Matches |

## Promotions

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: p

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Promotions.id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Promotions |
| Promotions.name | 保留物理名称；存档没有恢复别名 | TEXT | schema / Promotions |

## Tables

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Tables.id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Tables |
| Tables.html | 保留物理名称；存档没有恢复别名 | TEXT | schema / Tables |
| Tables.url | 保留物理名称；存档没有恢复别名 | TEXT | schema / Tables |

## Wrestlers

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: w1, w2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Wrestlers.id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Wrestlers |
| Wrestlers.name | 保留物理名称；存档没有恢复别名 | unknown | schema / Wrestlers |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

