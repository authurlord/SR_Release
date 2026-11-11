# Spider2-Lite / stacking — Schema and business semantics

The saved catalogue for this database contains 7 tables, 40 physical columns, 0 relationships and 7 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## eda

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| eda.name | Physical name retained; no saved recovered alias | TEXT | schema / eda |
| eda.version | Physical name retained; no saved recovered alias | INTEGER | schema / eda |
| eda.feature | Physical name retained; no saved recovered alias | TEXT | schema / eda |
| eda.type | Physical name retained; no saved recovered alias | TEXT | schema / eda |
| eda.range | Physical name retained; no saved recovered alias | BLOB | schema / eda |
| eda.drop_user | Physical name retained; no saved recovered alias | INTEGER | schema / eda |
| eda.drop_correlation | Physical name retained; no saved recovered alias | INTEGER | schema / eda |
| eda.target | Physical name retained; no saved recovered alias | INTEGER | schema / eda |

## feature_importance

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| feature_importance.name | Physical name retained; no saved recovered alias | TEXT | schema / feature_importance |
| feature_importance.version | Physical name retained; no saved recovered alias | INTEGER | schema / feature_importance |
| feature_importance.step | Physical name retained; no saved recovered alias | INTEGER | schema / feature_importance |
| feature_importance.feature | Physical name retained; no saved recovered alias | TEXT | schema / feature_importance |
| feature_importance.importance | Physical name retained; no saved recovered alias | NUMERIC | schema / feature_importance |

## model

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: m

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| model.name | Physical name retained; no saved recovered alias | TEXT | schema / model |
| model.version | Physical name retained; no saved recovered alias | INTEGER | schema / model |
| model.step | Physical name retained; no saved recovered alias | INTEGER | schema / model |
| model.L1_model | Physical name retained; no saved recovered alias | TEXT | schema / model |

## model_importance

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| model_importance.name | Physical name retained; no saved recovered alias | TEXT | schema / model_importance |
| model_importance.version | Physical name retained; no saved recovered alias | INTEGER | schema / model_importance |
| model_importance.step | Physical name retained; no saved recovered alias | INTEGER | schema / model_importance |
| model_importance.model | Physical name retained; no saved recovered alias | TEXT | schema / model_importance |
| model_importance.importance | Physical name retained; no saved recovered alias | NUMERIC | schema / model_importance |

## model_score

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| model_score.name | Physical name retained; no saved recovered alias | TEXT | schema / model_score |
| model_score.version | Physical name retained; no saved recovered alias | INTEGER | schema / model_score |
| model_score.step | Physical name retained; no saved recovered alias | INTEGER | schema / model_score |
| model_score.model | Physical name retained; no saved recovered alias | TEXT | schema / model_score |
| model_score.train_score | Physical name retained; no saved recovered alias | NUMERIC | schema / model_score |
| model_score.test_score | Physical name retained; no saved recovered alias | NUMERIC | schema / model_score |

## problem

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| problem.name | Physical name retained; no saved recovered alias | TEXT | schema / problem |
| problem.path | Physical name retained; no saved recovered alias | TEXT | schema / problem |
| problem.type | Physical name retained; no saved recovered alias | TEXT | schema / problem |
| problem.target | Physical name retained; no saved recovered alias | TEXT | schema / problem |

## solution

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| solution.name | Physical name retained; no saved recovered alias | TEXT | schema / solution |
| solution.version | Physical name retained; no saved recovered alias | INTEGER | schema / solution |
| solution.correlation | Physical name retained; no saved recovered alias | NUMERIC | schema / solution |
| solution.nb_model | Physical name retained; no saved recovered alias | INTEGER | schema / solution |
| solution.nb_feature | Physical name retained; no saved recovered alias | INTEGER | schema / solution |
| solution.score | Physical name retained; no saved recovered alias | NUMERIC | schema / solution |
| solution.test_size | Physical name retained; no saved recovered alias | NUMERIC | schema / solution |
| solution.resampling | Physical name retained; no saved recovered alias | INTEGER | schema / solution |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

