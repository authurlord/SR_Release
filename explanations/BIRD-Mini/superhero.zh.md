# BIRD-Mini / superhero — Schema 与业务口径解释

该数据库的存档目录包含 10 张表、31 个物理列、11 条关系，以及 10 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## alignment

Stores the possible moral or ethical alignments for superheroes, villains, and other characters.

恢复表名: alignment / alignments / moral_alignments / character_alignments / alignment_types
SQL表别名: a

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| alignment.XCL_001 | id / identifier / alignment_id / alignment_key / id_number | integer | schema / alignment |
| alignment.XCL_002 | alignment / alignment_name / moral_alignment / ethical_alignment / alignment_label / alignment_value / character_alignment | text | schema / alignment |

## attribute

Defines the types of attributes (e.g., Intelligence, Strength) that superheroes can possess, used as a lookup table for hero_attribute assignments.

恢复表名: attribute / attributes / superhero attributes / hero attributes / attribute definitions
SQL表别名: a

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| attribute.XCL_003 | id / identifier / attribute id / attribute identifier / attribute number / attribute key | integer | schema / attribute |
| attribute.XCL_004 | attribute name / attribute type / attribute label / attribute title / attribute description / superhero attribute / hero attribute | text | schema / attribute |

## colour

Lookup table mapping numeric IDs to colour names for superhero attributes such as skin, hair, and eye colour.

恢复表名: colour / colors / colour table / color lookup
SQL表别名: c, c1, c2, c_skin, e, h

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| colour.XCL_005 | id / identifier / colour id / color id / colour identifier / color identifier / colour key / color key | integer | schema / colour |
| colour.XCL_006 | colour / colour name / color name / colour value / color value / colour description / color description / colour label | text | schema / colour |

## gender

Stores a lookup of gender/sex identifiers and their textual labels for superhero entities.

恢复表名: gender / genders / sex / sexes
SQL表别名: g

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| gender.XCL_007 | id / identifier / gender_id / gender_identifier / gender_code / sex_id / sex_code | integer | schema / gender |
| gender.XCL_008 | gender / gender_label / gender_name / sex / sex_label / sex_name / gender_description | text | schema / gender |

## publisher

Stores information about comic book publishers and media companies that produce superhero content.

恢复表名: publisher / publishers / publishing companies / comic publishers
SQL表别名: p

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| publisher.XCL_014 | id / identifier / publisher id / publisher identifier / publisher number / publisher key | integer | schema / publisher |
| publisher.XCL_015 | publisher name / publisher / company name / publishing house / label / studio | text | schema / publisher |

## race

Stores the distinct race or species categories that a superhero can belong to, used as a lookup table for the superhero table.

恢复表名: race / races / species / ethnicities / superhero races
SQL表别名: r

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| race.XCL_016 | id / identifier / race_id / race identifier / species id / race number / race key | integer | schema / race |
| race.XCL_017 | race / race name / species / species name / race type / race category / superhero race / superhero species | text | schema / race |

## superhero

Stores core biographical and physical attributes of superhero characters, including their names, physical characteristics, and identifiers linking to reference tables for gender, eye colour, hair colour, skin colour, race, publisher, and alignment.

恢复表名: superhero / superheroes / heroes / superheroes table / heroes table
SQL表别名: s, s2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| superhero.XCL_018 | id / identifier / hero id / superhero id / character id | integer | schema / superhero |
| superhero.XCL_019 | superhero name / hero name / character name / alias / superhero alias | text | schema / superhero |
| superhero.XCL_020 | full name / real name / civilian name / secret identity | text | schema / superhero |
| superhero.XCL_021 | gender id / gender identifier / gender / sex | integer | schema / superhero |
| superhero.XCL_022 | eye colour id / eye colour identifier / eye color / eye colour / eye color id | integer | schema / superhero |
| superhero.XCL_023 | hair colour id / hair colour identifier / hair color / hair colour / hair color id | integer | schema / superhero |
| superhero.XCL_024 | skin colour id / skin colour identifier / skin color / skin colour / skin color id | integer | schema / superhero |
| superhero.XCL_025 | race id / race identifier / race / species | integer | schema / superhero |
| superhero.XCL_026 | publisher id / publisher identifier / publisher / comic publisher | integer | schema / superhero |
| superhero.XCL_027 | alignment id / alignment identifier / alignment / moral alignment | integer | schema / superhero |
| superhero.XCL_028 | height cm / height / height in cm / centimeters / cm | integer | schema / superhero |
| superhero.XCL_029 | weight kg / weight / weight in kg / kilograms / kg | integer | schema / superhero |

## hero_attribute

Stores numeric attribute values (e.g., strength, speed, intelligence) for each superhero, linking heroes to their specific attributes.

恢复表名: hero attribute / hero attributes / superhero attributes / character attributes / hero stats / superhero stats
SQL表别名: ha

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| hero_attribute.XCL_009 | hero id / hero identifier / hero / superhero / character / superhero id | integer | schema / hero_attribute |
| hero_attribute.XCL_010 | attribute id / attribute identifier / attribute / stat / trait / stat id | integer | schema / hero_attribute |
| hero_attribute.XCL_011 | attribute value / value / score / rating / level / stat value / attribute score | integer | schema / hero_attribute |

## superpower

Stores a catalog of distinct superpowers or abilities that can be assigned to superheroes.

恢复表名: superpower / superpowers / powers / abilities / capabilities
SQL表别名: sp

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| superpower.XCL_030 | id / identifier / power_id / superpower_id / ability_id | integer | schema / superpower |
| superpower.XCL_031 | power name / power_name / ability_name / superpower_name / power / ability / superpower | text | schema / superpower |

## hero_power

Associates heroes with their superpowers, linking each hero to one or more powers.

恢复表名: hero power / hero_powers / hero_power_assignments / power_links
SQL表别名: hp

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| hero_power.XCL_012 | hero id / hero identifier / hero / hero_identifier / hero_reference / superhero_id | integer | schema / hero_power |
| hero_power.XCL_013 | power id / power identifier / power / power_identifier / power_reference / superpower_id | integer | schema / hero_power |

## 表关系与连接依据

- alignment.XCL_001 ↔ superhero.XCL_027; declared_or_materialized_relationship
- attribute.XCL_003 ↔ hero_attribute.XCL_010; declared_or_materialized_relationship
- colour.XCL_005 ↔ superhero.XCL_022; declared_or_materialized_relationship
- colour.XCL_005 ↔ superhero.XCL_023; declared_or_materialized_relationship
- colour.XCL_005 ↔ superhero.XCL_024; declared_or_materialized_relationship
- gender.XCL_007 ↔ superhero.XCL_021; declared_or_materialized_relationship
- hero_attribute.XCL_009 ↔ superhero.XCL_018; declared_or_materialized_relationship
- hero_power.XCL_012 ↔ superhero.XCL_018; declared_or_materialized_relationship
- hero_power.XCL_013 ↔ superpower.XCL_030; declared_or_materialized_relationship
- publisher.XCL_014 ↔ superhero.XCL_026; declared_or_materialized_relationship
- race.XCL_016 ↔ superhero.XCL_025; declared_or_materialized_relationship

## 业务口径、总体与粒度


## 增量维护事件

