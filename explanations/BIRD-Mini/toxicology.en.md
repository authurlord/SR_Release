# BIRD-Mini / toxicology — Schema and business semantics

The saved catalogue for this database contains 4 tables, 11 physical columns, 5 relationships and 4 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## atom

Stores individual atoms that make up molecules in a toxicology database, with each atom identified by a unique ID and linked to its parent molecule.

Recovered table names: atom / atoms / atom records / chemical atoms
SQL table aliases: a, a1, a2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| atom.XCL_001 | atom id / atom identifier / atom key / atom number / atom code | text | schema / atom |
| atom.XCL_002 | molecule id / molecule identifier / parent molecule / molecule key / molecule number / molecule code | text | schema / atom |
| atom.XCL_003 | element / element symbol / chemical element / atom element / element type / element name | text | schema / atom |

## bond

Stores information about chemical bonds between atoms in molecules.

Recovered table names: bond / bonds / chemical bonds / molecular bonds
SQL table aliases: b

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| bond.XCL_004 | bond id / bond identifier / bond key / bond code | text | schema / bond |
| bond.XCL_005 | molecule id / molecule identifier / molecule key / molecule code / parent molecule | text | schema / bond |
| bond.XCL_006 | bond type / bond kind / bond category / bond order | text | schema / bond |

## connected

Links atoms to bonds and atoms to other atoms in a molecular structure, representing connectivity.

Recovered table names: connected / connections / atom_bond_links / bond_atom_associations
SQL table aliases: c, c1, c2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| connected.XCL_007 | atom id / atom identifier / first atom / atom A / source atom | text | schema / connected |
| connected.XCL_008 | atom id2 / second atom identifier / atom B / target atom / other atom / atom ID 2 | text | schema / connected |
| connected.XCL_009 | bond id / bond identifier / chemical bond / link id / connection id | text | schema / connected |

## molecule

Stores identifiers and labels for chemical molecules in a toxicology database.

Recovered table names: molecule / molecules / chemical entity / compound
SQL table aliases: m

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| molecule.XCL_010 | molecule id / molecule identifier / compound ID / chemical ID / molecule code / molecule number | text | schema / molecule |
| molecule.XCL_011 | label / marker / sign / indicator / classification | text | schema / molecule |

## Relationships and join evidence

- atom.XCL_001 ↔ connected.XCL_007; declared_or_materialized_relationship
- atom.XCL_001 ↔ connected.XCL_008; declared_or_materialized_relationship
- atom.XCL_002 ↔ molecule.XCL_010; declared_or_materialized_relationship
- bond.XCL_004 ↔ connected.XCL_009; declared_or_materialized_relationship
- bond.XCL_005 ↔ molecule.XCL_010; declared_or_materialized_relationship

## Business definitions, population and grain


## Incremental maintenance events

