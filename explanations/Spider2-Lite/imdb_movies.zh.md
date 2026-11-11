# Spider2-Lite / imdb_movies — Schema 与业务口径解释

该数据库的存档目录包含 7 张表、38 个物理列、0 条关系，以及 7 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## ERD

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ERD.table | 保留物理名称；存档没有恢复别名 | TEXT | schema / ERD |
| ERD.column | 保留物理名称；存档没有恢复别名 | TEXT | schema / ERD |
| ERD.Unnamed: 2 | 保留物理名称；存档没有恢复别名 | REAL | schema / ERD |
| ERD.Unnamed: 3 | 保留物理名称；存档没有恢复别名 | REAL | schema / ERD |
| ERD.Unnamed: 4 | 保留物理名称；存档没有恢复别名 | REAL | schema / ERD |
| ERD.Unnamed: 5 | 保留物理名称；存档没有恢复别名 | REAL | schema / ERD |
| ERD.Unnamed: 6 | 保留物理名称；存档没有恢复别名 | TEXT | schema / ERD |
| ERD.Unnamed: 7 | 保留物理名称；存档没有恢复别名 | REAL | schema / ERD |
| ERD.Unnamed: 8 | 保留物理名称；存档没有恢复别名 | REAL | schema / ERD |
| ERD.Unnamed: 9 | 保留物理名称；存档没有恢复别名 | TEXT | schema / ERD |
| ERD.Unnamed: 10 | 保留物理名称；存档没有恢复别名 | REAL | schema / ERD |
| ERD.Unnamed: 11 | 保留物理名称；存档没有恢复别名 | REAL | schema / ERD |
| ERD.Unnamed: 12 | 保留物理名称；存档没有恢复别名 | TEXT | schema / ERD |

## director_mapping

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: dm

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| director_mapping.movie_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / director_mapping |
| director_mapping.name_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / director_mapping |

## genre

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: g

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| genre.movie_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / genre |
| genre.genre | 保留物理名称；存档没有恢复别名 | TEXT | schema / genre |

## movies

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: m

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| movies.id | 保留物理名称；存档没有恢复别名 | TEXT | schema / movies |
| movies.title | 保留物理名称；存档没有恢复别名 | TEXT | schema / movies |
| movies.year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / movies |
| movies.date_published | 保留物理名称；存档没有恢复别名 | TIMESTAMP | schema / movies |
| movies.duration | 保留物理名称；存档没有恢复别名 | INTEGER | schema / movies |
| movies.country | 保留物理名称；存档没有恢复别名 | TEXT | schema / movies |
| movies.worlwide_gross_income | 保留物理名称；存档没有恢复别名 | TEXT | schema / movies |
| movies.languages | 保留物理名称；存档没有恢复别名 | TEXT | schema / movies |
| movies.production_company | 保留物理名称；存档没有恢复别名 | TEXT | schema / movies |

## names

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: n

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| names.id | 保留物理名称；存档没有恢复别名 | TEXT | schema / names |
| names.name | 保留物理名称；存档没有恢复别名 | TEXT | schema / names |
| names.height | 保留物理名称；存档没有恢复别名 | REAL | schema / names |
| names.date_of_birth | 保留物理名称；存档没有恢复别名 | TEXT | schema / names |
| names.known_for_movies | 保留物理名称；存档没有恢复别名 | TEXT | schema / names |

## ratings

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: r

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ratings.movie_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / ratings |
| ratings.avg_rating | 保留物理名称；存档没有恢复别名 | REAL | schema / ratings |
| ratings.total_votes | 保留物理名称；存档没有恢复别名 | INTEGER | schema / ratings |
| ratings.median_rating | 保留物理名称；存档没有恢复别名 | REAL | schema / ratings |

## role_mapping

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| role_mapping.movie_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / role_mapping |
| role_mapping.name_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / role_mapping |
| role_mapping.category | 保留物理名称；存档没有恢复别名 | TEXT | schema / role_mapping |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

