# Spider2-Lite / Db-IMDB — Schema 与业务口径解释

该数据库的存档目录包含 13 张表、50 个物理列、0 条关系，以及 13 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## Country

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Country.index | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Country |
| Country.Name | 保留物理名称；存档没有恢复别名 | TEXT | schema / Country |
| Country.CID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Country |

## Genre

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Genre.index | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Genre |
| Genre.Name | 保留物理名称；存档没有恢复别名 | TEXT | schema / Genre |
| Genre.GID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Genre |

## Language

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Language.index | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Language |
| Language.Name | 保留物理名称；存档没有恢复别名 | TEXT | schema / Language |
| Language.LAID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Language |

## Location

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Location.index | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Location |
| Location.Name | 保留物理名称；存档没有恢复别名 | TEXT | schema / Location |
| Location.LID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Location |

## M_Cast

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: c

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| M_Cast.index | 保留物理名称；存档没有恢复别名 | INTEGER | schema / M_Cast |
| M_Cast.MID | 保留物理名称；存档没有恢复别名 | TEXT | schema / M_Cast |
| M_Cast.PID | 保留物理名称；存档没有恢复别名 | TEXT | schema / M_Cast |
| M_Cast.ID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / M_Cast |

## M_Country

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| M_Country.index | 保留物理名称；存档没有恢复别名 | INTEGER | schema / M_Country |
| M_Country.MID | 保留物理名称；存档没有恢复别名 | TEXT | schema / M_Country |
| M_Country.CID | 保留物理名称；存档没有恢复别名 | REAL | schema / M_Country |
| M_Country.ID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / M_Country |

## M_Director

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: d

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| M_Director.index | 保留物理名称；存档没有恢复别名 | INTEGER | schema / M_Director |
| M_Director.MID | 保留物理名称；存档没有恢复别名 | TEXT | schema / M_Director |
| M_Director.PID | 保留物理名称；存档没有恢复别名 | TEXT | schema / M_Director |
| M_Director.ID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / M_Director |

## M_Genre

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| M_Genre.index | 保留物理名称；存档没有恢复别名 | INTEGER | schema / M_Genre |
| M_Genre.MID | 保留物理名称；存档没有恢复别名 | TEXT | schema / M_Genre |
| M_Genre.GID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / M_Genre |
| M_Genre.ID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / M_Genre |

## M_Language

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| M_Language.index | 保留物理名称；存档没有恢复别名 | INTEGER | schema / M_Language |
| M_Language.MID | 保留物理名称；存档没有恢复别名 | TEXT | schema / M_Language |
| M_Language.LAID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / M_Language |
| M_Language.ID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / M_Language |

## M_Location

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| M_Location.index | 保留物理名称；存档没有恢复别名 | INTEGER | schema / M_Location |
| M_Location.MID | 保留物理名称；存档没有恢复别名 | TEXT | schema / M_Location |
| M_Location.LID | 保留物理名称；存档没有恢复别名 | REAL | schema / M_Location |
| M_Location.ID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / M_Location |

## M_Producer

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| M_Producer.index | 保留物理名称；存档没有恢复别名 | INTEGER | schema / M_Producer |
| M_Producer.MID | 保留物理名称；存档没有恢复别名 | TEXT | schema / M_Producer |
| M_Producer.PID | 保留物理名称；存档没有恢复别名 | TEXT | schema / M_Producer |
| M_Producer.ID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / M_Producer |

## Movie

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: m

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Movie.index | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Movie |
| Movie.MID | 保留物理名称；存档没有恢复别名 | TEXT | schema / Movie |
| Movie.title | 保留物理名称；存档没有恢复别名 | TEXT | schema / Movie |
| Movie.year | 保留物理名称；存档没有恢复别名 | TEXT | schema / Movie |
| Movie.rating | 保留物理名称；存档没有恢复别名 | REAL | schema / Movie |
| Movie.num_votes | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Movie |

## Person

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: p

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Person.index | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Person |
| Person.PID | 保留物理名称；存档没有恢复别名 | TEXT | schema / Person |
| Person.Name | 保留物理名称；存档没有恢复别名 | TEXT | schema / Person |
| Person.Gender | 保留物理名称；存档没有恢复别名 | TEXT | schema / Person |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

