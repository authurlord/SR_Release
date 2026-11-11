# EvoSchema / evoschema::table_split::toxicology::210 — Schema 与业务口径解释

该数据库的存档目录包含 5 张表、12 个物理列、0 条关系，以及 5 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## atom

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| atom.atom_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / atom |
| atom.molecule_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / atom |
| atom.element | 保留物理名称；存档没有恢复别名 | TEXT | schema / atom |

## BondDetails

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| BondDetails.bond_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / BondDetails |
| BondDetails.bond_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / BondDetails |

## connected

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: T1

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| connected.atom_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / connected |
| connected.atom_id2 | 保留物理名称；存档没有恢复别名 | TEXT | schema / connected |
| connected.bond_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / connected |

## molecule

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| molecule.molecule_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / molecule |
| molecule.label | 保留物理名称；存档没有恢复别名 | TEXT | schema / molecule |

## MoleculeDetails

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| MoleculeDetails.bond_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / MoleculeDetails |
| MoleculeDetails.molecule_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / MoleculeDetails |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

