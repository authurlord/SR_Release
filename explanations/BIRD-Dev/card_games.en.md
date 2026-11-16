# BIRD-Dev / card_games — Schema and business semantics

The saved catalogue for this database contains 6 tables, 115 physical columns, 4 relationships and 6 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## cards

This table stores detailed information about individual Magic: The Gathering cards, including identifiers, attributes, game mechanics, and metadata.

Recovered table names: cards / card / mtg cards / magic cards / magic the gathering cards
SQL table aliases: T1, T2, c, c2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| cards.XCL_001 | id / identifier / card id / card identifier / internal id / primary key | integer | schema / cards |
| cards.XCL_002 | artist / illustrator / card artist / art creator | text | schema / cards |
| cards.XCL_003 | ascii name / english name / name ascii / card name | text | schema / cards |
| cards.XCL_004 | availability / available formats / platforms / where to play | text | schema / cards |
| cards.XCL_005 | border color / border / card border | text | schema / cards |
| cards.XCL_006 | card kingdom foil id / card kingdom foil identifier / ck foil id / foil id | text | schema / cards |
| cards.XCL_007 | card kingdom id / card kingdom identifier / ck id | text | schema / cards |
| cards.XCL_008 | color identity / color id / color pie / mana colors | text | schema / cards |
| cards.XCL_009 | color indicator / mana indicator | text | schema / cards |
| cards.XCL_010 | colors / card colors / mana colors / color | text | schema / cards |
| cards.XCL_011 | converted mana cost / cmc / mana value / total mana cost | real | schema / cards |
| cards.XCL_012 | duel deck / duel deck indicator / duel deck version | text | schema / cards |
| cards.XCL_013 | edhrec rank / commander rank / edh popularity / edhrec rating | integer | schema / cards |
| cards.XCL_014 | face converted mana cost / face cmc / front face cmc | real | schema / cards |
| cards.XCL_015 | face name / front face name / card face name | text | schema / cards |
| cards.XCL_016 | flavor name / alternate name / godzilla name / special name | text | schema / cards |
| cards.XCL_017 | flavor text / flavor / card flavor / story text | text | schema / cards |
| cards.XCL_018 | frame effects / card frame effects / special frame / frame style | text | schema / cards |
| cards.XCL_019 | frame version / card frame version / frame year | text | schema / cards |
| cards.XCL_020 | hand / hand modifier / hand size / hand bonus | text | schema / cards |
| cards.XCL_021 | has alternative deck limit / alternative deck limit / deck limit flag | integer | schema / cards |
| cards.XCL_022 | has content warning / content warning / content warning flag | integer | schema / cards |
| cards.XCL_023 | has foil / foil available / foil version / foil flag | integer | schema / cards |
| cards.XCL_024 | has non foil / has non-foil / non-foil available / non-foil version / non-foil flag | integer | schema / cards |
| cards.XCL_025 | is alternative / alternative version / alternate art / alternate card | integer | schema / cards |
| cards.XCL_026 | is full art / full art / full art card | integer | schema / cards |
| cards.XCL_027 | is online only / online only / digital only / mtgo only | integer | schema / cards |
| cards.XCL_028 | is oversized / oversized / oversized card | integer | schema / cards |
| cards.XCL_029 | is promo / promo / promotional card | integer | schema / cards |
| cards.XCL_030 | is reprint / reprint / reprinted card | integer | schema / cards |
| cards.XCL_031 | is reserved / reserved list / reserved card | integer | schema / cards |
| cards.XCL_032 | is starter / starter card / starter deck | integer | schema / cards |
| cards.XCL_033 | is story spotlight / story spotlight / story card | integer | schema / cards |
| cards.XCL_034 | is textless / textless / textless card | integer | schema / cards |
| cards.XCL_035 | is timeshifted / timeshifted / timeshifted card | integer | schema / cards |
| cards.XCL_036 | keywords / abilities / card keywords / keyword abilities | text | schema / cards |
| cards.XCL_037 | layout / card layout / card type layout | text | schema / cards |
| cards.XCL_038 | leadership skills / commander skills / brawl/commander/oathbreaker | text | schema / cards |
| cards.XCL_039 | life / life modifier / life bonus / life total | text | schema / cards |
| cards.XCL_040 | loyalty / planeswalker loyalty / loyalty counters | text | schema / cards |
| cards.XCL_041 | mana cost / mana cost string / casting cost | text | schema / cards |
| cards.XCL_042 | mcm id / mcm identifier / cardmarket id / mkm id | text | schema / cards |
| cards.XCL_043 | mcm meta id / mcm meta identifier / cardmarket meta id / mkm meta id | text | schema / cards |
| cards.XCL_044 | mtg arena id / mtg arena identifier / arena id / mtga id | text | schema / cards |
| cards.XCL_045 | mtgjson v4 id / mtgjson v4 identifier / mtgjson id / json id | text | schema / cards |
| cards.XCL_046 | mtgo foil id / mtgo foil identifier | text | schema / cards |
| cards.XCL_047 | mtgo id / mtgo identifier | text | schema / cards |
| cards.XCL_048 | multiverse id / multiverse identifier | text | schema / cards |
| cards.XCL_049 | name | text | schema / cards |
| cards.XCL_050 | number | text | schema / cards |
| cards.XCL_051 | original release date | text | schema / cards |
| cards.XCL_052 | original text | text | schema / cards |
| cards.XCL_053 | original type | text | schema / cards |
| cards.XCL_054 | other face ids | text | schema / cards |
| cards.XCL_055 | power | text | schema / cards |
| cards.XCL_056 | printings | text | schema / cards |
| cards.XCL_057 | promo types | text | schema / cards |
| cards.XCL_058 | purchase urls | text | schema / cards |
| cards.XCL_059 | rarity | text | schema / cards |
| cards.XCL_060 | scryfall id / scryfall identifier | text | schema / cards |
| cards.XCL_061 | scryfall illustration id / scryfall illustration identifier | text | schema / cards |
| cards.XCL_062 | scryfall oracle id / scryfall oracle identifier | text | schema / cards |
| cards.XCL_063 | set code | text | schema / cards |
| cards.XCL_064 | side | text | schema / cards |
| cards.XCL_065 | subtypes | text | schema / cards |
| cards.XCL_066 | supertypes | text | schema / cards |
| cards.XCL_067 | tcgplayer product id / tcgplayer product identifier | text | schema / cards |
| cards.XCL_068 | text | text | schema / cards |
| cards.XCL_069 | toughness | text | schema / cards |
| cards.XCL_070 | type | text | schema / cards |
| cards.XCL_071 | types | text | schema / cards |
| cards.XCL_072 | uuid | text | schema / cards |
| cards.XCL_073 | variations | text | schema / cards |
| cards.XCL_074 | watermark | text | schema / cards |

## foreign_data

Stores translated or foreign-language versions of card text, names, and types for a card game, linked to the main cards table via uuid.

Recovered table names: foreign data / foreign_data / foreign card data / translated card info / card translations
SQL table aliases: f, fd

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| foreign_data.XCL_075 | id / identifier / row id / primary key / record number | integer | schema / foreign_data |
| foreign_data.XCL_076 | flavor text / flavor_text / flavor / quote / story text | text | schema / foreign_data |
| foreign_data.XCL_077 | language / lang / locale / translation language | text | schema / foreign_data |
| foreign_data.XCL_078 | multiverseid / multiverse id / multiverse_id / gatherer id | integer | schema / foreign_data |
| foreign_data.XCL_079 | name / card name / translated name / foreign name | text | schema / foreign_data |
| foreign_data.XCL_080 | text / card text / rules text / ability text / oracle text | text | schema / foreign_data |
| foreign_data.XCL_081 | type / card type / type line / creature type / subtype | text | schema / foreign_data |
| foreign_data.XCL_082 | uuid / universally unique identifier / card uuid / foreign key | text | schema / foreign_data |

## legalities

Stores the legal status of cards in various game formats (e.g., Commander, Modern).

Recovered table names: legalities / legality / legal statuses / format legality / card legality
SQL table aliases: l

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| legalities.XCL_083 | id / identifier / legality id / record id / legal status id | integer | schema / legalities |
| legalities.XCL_084 | format / game format / format name / play format / format type / formats | text | schema / legalities |
| legalities.XCL_085 | status / legality status / legal status / is legal / status value / statuses | text | schema / legalities |
| legalities.XCL_086 | uuid / card uuid / card identifier / universal unique id / card reference | text | schema / legalities |

## sets

This table stores information about each card set or expansion in a card game, including its name, release date, size, and various identifiers.

Recovered table names: sets / card sets / card game sets / Magic: The Gathering sets / MTG sets / expansions / releases
SQL table aliases: T2, s, s2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| sets.XCL_095 | id / identifier / set ID / set identifier / internal ID / primary key | integer | schema / sets |
| sets.XCL_096 | base set size / number of cards in base set / base card count | integer | schema / sets |
| sets.XCL_097 | block / block name / story block / set block | text | schema / sets |
| sets.XCL_098 | booster / booster pack contents / booster configuration / pack contents | text | schema / sets |
| sets.XCL_099 | code / set code / abbreviation / short code | text | schema / sets |
| sets.XCL_100 | is foil only / foil only / only foil / foil exclusive | integer | schema / sets |
| sets.XCL_101 | is foreign only / foreign only / non-English only / foreign language exclusive | integer | schema / sets |
| sets.XCL_102 | is non foil only / non-foil only / only non-foil / non-foil exclusive | integer | schema / sets |
| sets.XCL_103 | is online only / online only / digital only / MTGO only | integer | schema / sets |
| sets.XCL_104 | is partial preview / partial preview / preview incomplete / partial spoiler | integer | schema / sets |
| sets.XCL_105 | keyrune code / symbol code / set symbol code | text | schema / sets |
| sets.XCL_106 | mcm id / mcm identifier / MagicCardMarket ID / cardmarket ID | integer | schema / sets |
| sets.XCL_107 | mcm id extras / mcm identifier extras / MCM extras ID / Cardmarket extras ID / extra MCM ID | integer | schema / sets |
| sets.XCL_108 | mcm name / Cardmarket name / MagicCardMarket name | text | schema / sets |
| sets.XCL_109 | mtgo code / Magic Online code / digital code | text | schema / sets |
| sets.XCL_110 | name / set name / full name / set title | text | schema / sets |
| sets.XCL_111 | parent code / parent set code / master set code | text | schema / sets |
| sets.XCL_112 | release date / release day / launch date | date | schema / sets |
| sets.XCL_113 | tcgplayer group id / tcgplayer group identifier / TCGplayer ID / group ID | integer | schema / sets |
| sets.XCL_114 | total set size / total card count / full set size | integer | schema / sets |
| sets.XCL_115 | type / set type / category / expansion type | text | schema / sets |

## set_translations

Stores localized translations of card set names in various languages.

Recovered table names: set translations / set_translations / set_translation / card_set_translations / set_name_translations / translated_sets
SQL table aliases: st, t

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| set_translations.XCL_091 | id / identifier / translation_id / set_translation_id / record_id | integer | schema / set_translations |
| set_translations.XCL_092 | language / lang / locale / language_code / language_name | text | schema / set_translations |
| set_translations.XCL_093 | set code / setCode / set_code / code / set_identifier / expansion_code | text | schema / set_translations |
| set_translations.XCL_094 | translation / translated_name / localized_name / set_name / name_in_language | text | schema / set_translations |

## rulings

Stores official rulings or clarifications for card games, each identified by a unique ID and UUID, with a date and explanatory text.

Recovered table names: rulings / ruling / card_rulings / game_rulings / official_rulings
SQL table aliases: r

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| rulings.XCL_087 | id / identifier / ruling_id / ruling_number / entry_id / record_id | integer | schema / rulings |
| rulings.XCL_088 | date / ruling_date / publication_date / effective_date / date_issued | date | schema / rulings |
| rulings.XCL_089 | text / ruling_text / explanation / clarification / ruling_description | text | schema / rulings |
| rulings.XCL_090 | uuid / ruling_uuid / card_uuid / ruling_identifier / unique_id | text | schema / rulings |

## Relationships and join evidence

- cards.XCL_072 ↔ foreign_data.XCL_082; declared_or_materialized_relationship
- cards.XCL_072 ↔ legalities.XCL_086; declared_or_materialized_relationship
- cards.XCL_072 ↔ rulings.XCL_090; declared_or_materialized_relationship
- set_translations.XCL_093 ↔ sets.XCL_099; declared_or_materialized_relationship

## Business definitions, population and grain


## Incremental maintenance events

