# Spider2-Lite / stacking — Schema 与业务口径解释

该数据库的存档目录包含 7 张表、40 个物理列、0 条关系，以及 7 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## eda

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| eda.name | 保留物理名称；存档没有恢复别名 | TEXT | schema / eda |
| eda.version | 保留物理名称；存档没有恢复别名 | INTEGER | schema / eda |
| eda.feature | 保留物理名称；存档没有恢复别名 | TEXT | schema / eda |
| eda.type | 保留物理名称；存档没有恢复别名 | TEXT | schema / eda |
| eda.range | 保留物理名称；存档没有恢复别名 | BLOB | schema / eda |
| eda.drop_user | 保留物理名称；存档没有恢复别名 | INTEGER | schema / eda |
| eda.drop_correlation | 保留物理名称；存档没有恢复别名 | INTEGER | schema / eda |
| eda.target | 保留物理名称；存档没有恢复别名 | INTEGER | schema / eda |

## feature_importance

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| feature_importance.name | 保留物理名称；存档没有恢复别名 | TEXT | schema / feature_importance |
| feature_importance.version | 保留物理名称；存档没有恢复别名 | INTEGER | schema / feature_importance |
| feature_importance.step | 保留物理名称；存档没有恢复别名 | INTEGER | schema / feature_importance |
| feature_importance.feature | 保留物理名称；存档没有恢复别名 | TEXT | schema / feature_importance |
| feature_importance.importance | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / feature_importance |

## model

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: m

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| model.name | 保留物理名称；存档没有恢复别名 | TEXT | schema / model |
| model.version | 保留物理名称；存档没有恢复别名 | INTEGER | schema / model |
| model.step | 保留物理名称；存档没有恢复别名 | INTEGER | schema / model |
| model.L1_model | 保留物理名称；存档没有恢复别名 | TEXT | schema / model |

## model_importance

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| model_importance.name | 保留物理名称；存档没有恢复别名 | TEXT | schema / model_importance |
| model_importance.version | 保留物理名称；存档没有恢复别名 | INTEGER | schema / model_importance |
| model_importance.step | 保留物理名称；存档没有恢复别名 | INTEGER | schema / model_importance |
| model_importance.model | 保留物理名称；存档没有恢复别名 | TEXT | schema / model_importance |
| model_importance.importance | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / model_importance |

## model_score

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| model_score.name | 保留物理名称；存档没有恢复别名 | TEXT | schema / model_score |
| model_score.version | 保留物理名称；存档没有恢复别名 | INTEGER | schema / model_score |
| model_score.step | 保留物理名称；存档没有恢复别名 | INTEGER | schema / model_score |
| model_score.model | 保留物理名称；存档没有恢复别名 | TEXT | schema / model_score |
| model_score.train_score | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / model_score |
| model_score.test_score | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / model_score |

## problem

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| problem.name | 保留物理名称；存档没有恢复别名 | TEXT | schema / problem |
| problem.path | 保留物理名称；存档没有恢复别名 | TEXT | schema / problem |
| problem.type | 保留物理名称；存档没有恢复别名 | TEXT | schema / problem |
| problem.target | 保留物理名称；存档没有恢复别名 | TEXT | schema / problem |

## solution

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| solution.name | 保留物理名称；存档没有恢复别名 | TEXT | schema / solution |
| solution.version | 保留物理名称；存档没有恢复别名 | INTEGER | schema / solution |
| solution.correlation | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / solution |
| solution.nb_model | 保留物理名称；存档没有恢复别名 | INTEGER | schema / solution |
| solution.nb_feature | 保留物理名称；存档没有恢复别名 | INTEGER | schema / solution |
| solution.score | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / solution |
| solution.test_size | 保留物理名称；存档没有恢复别名 | NUMERIC | schema / solution |
| solution.resampling | 保留物理名称；存档没有恢复别名 | INTEGER | schema / solution |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

