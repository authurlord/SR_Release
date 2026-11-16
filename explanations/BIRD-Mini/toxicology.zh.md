# BIRD-Mini / toxicology — Schema 与业务口径解释

该数据库的存档目录包含 4 张表、11 个物理列、5 条关系，以及 4 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## atom

Stores individual atoms that make up molecules in a toxicology database, with each atom identified by a unique ID and linked to its parent molecule.

恢复表名: atom / atoms / atom records / chemical atoms
SQL表别名: a, a1, a2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| atom.XCL_001 | atom id / atom identifier / atom key / atom number / atom code | text | schema / atom |
| atom.XCL_002 | molecule id / molecule identifier / parent molecule / molecule key / molecule number / molecule code | text | schema / atom |
| atom.XCL_003 | element / element symbol / chemical element / atom element / element type / element name | text | schema / atom |

## bond

Stores information about chemical bonds between atoms in molecules.

恢复表名: bond / bonds / chemical bonds / molecular bonds
SQL表别名: b

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| bond.XCL_004 | bond id / bond identifier / bond key / bond code | text | schema / bond |
| bond.XCL_005 | molecule id / molecule identifier / molecule key / molecule code / parent molecule | text | schema / bond |
| bond.XCL_006 | bond type / bond kind / bond category / bond order | text | schema / bond |

## connected

Links atoms to bonds and atoms to other atoms in a molecular structure, representing connectivity.

恢复表名: connected / connections / atom_bond_links / bond_atom_associations
SQL表别名: c, c1, c2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| connected.XCL_007 | atom id / atom identifier / first atom / atom A / source atom | text | schema / connected |
| connected.XCL_008 | atom id2 / second atom identifier / atom B / target atom / other atom / atom ID 2 | text | schema / connected |
| connected.XCL_009 | bond id / bond identifier / chemical bond / link id / connection id | text | schema / connected |

## molecule

Stores identifiers and labels for chemical molecules in a toxicology database.

恢复表名: molecule / molecules / chemical entity / compound
SQL表别名: m

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| molecule.XCL_010 | molecule id / molecule identifier / compound ID / chemical ID / molecule code / molecule number | text | schema / molecule |
| molecule.XCL_011 | label / marker / sign / indicator / classification | text | schema / molecule |

## 表关系与连接依据

- atom.XCL_001 ↔ connected.XCL_007; declared_or_materialized_relationship
- atom.XCL_001 ↔ connected.XCL_008; declared_or_materialized_relationship
- atom.XCL_002 ↔ molecule.XCL_010; declared_or_materialized_relationship
- bond.XCL_004 ↔ connected.XCL_009; declared_or_materialized_relationship
- bond.XCL_005 ↔ molecule.XCL_010; declared_or_materialized_relationship

## 业务口径、总体与粒度


## 增量维护事件

