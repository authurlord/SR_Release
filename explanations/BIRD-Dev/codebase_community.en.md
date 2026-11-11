# BIRD-Dev / codebase_community — Schema and business semantics

The saved catalogue for this database contains 8 tables, 71 physical columns, 12 relationships and 8 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## badges

Stores badges awarded to users on the platform, including the badge type and award date.

Recovered table names: badges / badge / awarded badges / badge records
SQL table aliases: b, b1, b2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| badges.XCL_001 | id / identifier / badge id / badge identifier / badge record id / badge number | integer | schema / badges |
| badges.XCL_002 | user id / user identifier / recipient user id / badge recipient / user who received the badge | integer | schema / badges |
| badges.XCL_003 | name / badge name / badge title / badge type / badge class / award name | text | schema / badges |
| badges.XCL_004 | date / award date / badge date / date awarded / granted date / badge award timestamp | datetime | schema / badges |

## comments

Stores user-submitted comments or feedback on posts, including the comment text, author info, and creation timestamp.

Recovered table names: comments / comment / remarks / feedback / notes
SQL table aliases: c

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| comments.XCL_005 | id / identifier / comment ID / comment identifier / comment number | integer | schema / comments |
| comments.XCL_006 | post id / post identifier / parent post / related post | integer | schema / comments |
| comments.XCL_007 | score / comment score / rating / upvotes minus downvotes / net votes | integer | schema / comments |
| comments.XCL_008 | text / comment text / body / content / message | text | schema / comments |
| comments.XCL_009 | creation date / comment date / posted date / timestamp / created at | datetime | schema / comments |
| comments.XCL_010 | user id / user identifier / author ID / commenter ID | integer | schema / comments |
| comments.XCL_011 | user display name / display name / username / author name / commenter name | text | schema / comments |

## postHistory

Tracks all changes, edits, and revisions made to posts on the community platform, including who made the change, when, and what was changed.

Recovered table names: post history / post revisions / post edits / post change log / post audit trail
SQL table aliases: ph

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| postHistory.XCL_012 | id / identifier / history id / revision id / change id / entry id / record id | integer | schema / postHistory |
| postHistory.XCL_013 | post history type id / post history type identifier / history type id / revision type id / change type id / action type id / edit type id | integer | schema / postHistory |
| postHistory.XCL_014 | post id / post identifier / question id / answer id / target post id / affected post id | integer | schema / postHistory |
| postHistory.XCL_015 | revision guid / revision uuid / change guid / edit guid / version guid | text | schema / postHistory |
| postHistory.XCL_016 | creation date / change date / revision date / edit date / timestamp / date of change | datetime | schema / postHistory |
| postHistory.XCL_017 | user id / user identifier / author id / editor id / modifier id / change author id | integer | schema / postHistory |
| postHistory.XCL_018 | text / revision text / post body / content / revised text / new text / updated content | text | schema / postHistory |
| postHistory.XCL_019 | comment / edit comment / revision comment / change comment / edit summary / revision note | text | schema / postHistory |
| postHistory.XCL_020 | user display name / display name / user name / author name / editor name / modifier name | text | schema / postHistory |

## postLinks

Stores links between posts, such as duplicates or related content.

Recovered table names: post links / link table / post connections / related posts
SQL table aliases: pl

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| postLinks.XCL_021 | id / identifier / link id / link identifier / post link id / record id | integer | schema / postLinks |
| postLinks.XCL_022 | creation date / link creation date / date created / timestamp | datetime | schema / postLinks |
| postLinks.XCL_023 | post id / post identifier / source post id / original post | integer | schema / postLinks |
| postLinks.XCL_024 | related post id / related post identifier / target post id / linked post / destination post | integer | schema / postLinks |
| postLinks.XCL_025 | link type id / link type identifier / link type / relationship type / link category | integer | schema / postLinks |

## posts

Stores all questions and answers posted on the Stack Exchange community, including metadata such as scores, view counts, tags, and user associations.

Recovered table names: posts / questions / answers / postings / discussions
SQL table aliases: p, p1, p2, parent

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| posts.XCL_026 | id / identifier / post id / post identifier / question id / answer id | integer | schema / posts |
| posts.XCL_027 | post type id / post type identifier / post type / type of post / post category / question or answer | integer | schema / posts |
| posts.XCL_028 | accepted answer id / accepted answer identifier / accepted answer / best answer id / chosen answer | integer | schema / posts |
| posts.XCL_029 | creaion date / creation date / post date / date posted / created at / post creation time | datetime | schema / posts |
| posts.XCL_030 | score / post score / votes / rating / points | integer | schema / posts |
| posts.XCL_031 | view count / views / number of views / page views / visits | integer | schema / posts |
| posts.XCL_032 | body / post body / content / text / post content | text | schema / posts |
| posts.XCL_033 | owner user id / owner user identifier / author id / poster id / user id of owner / creator id | integer | schema / posts |
| posts.XCL_034 | las activity date / last activity date / last active / last update / most recent activity / last modified | datetime | schema / posts |
| posts.XCL_035 | title / post title / question title / subject / heading | text | schema / posts |
| posts.XCL_036 | tags / post tags / tag list / categories / labels | text | schema / posts |
| posts.XCL_037 | answer count / number of answers / answers / reply count | integer | schema / posts |
| posts.XCL_038 | comment count / number of comments / comments / remarks | integer | schema / posts |
| posts.XCL_039 | favorite count / number of favorites / favorites / bookmarks / stars | integer | schema / posts |
| posts.XCL_040 | last editor user id / last editor user identifier / last editor id / editor id / user who last edited | integer | schema / posts |
| posts.XCL_041 | last edit date / last edited / edit date / most recent edit / last modification | datetime | schema / posts |
| posts.XCL_042 | community owned date / community wiki date / wiki date / community ownership | datetime | schema / posts |
| posts.XCL_043 | parent id / parent identifier / parent post id / question id for answer / related question id | integer | schema / posts |
| posts.XCL_044 | closed date / closure date / date closed / when closed | datetime | schema / posts |
| posts.XCL_045 | owner display name / author name / poster name / display name / username | text | schema / posts |
| posts.XCL_046 | last editor display name / editor name / last editor name / display name of last editor | text | schema / posts |

## tags

Stores metadata about tags used to categorize questions or posts in a community forum, including tag names, usage counts, and links to associated wiki and excerpt posts.

Recovered table names: tags / tag / topic labels / subject tags / keyword tags
SQL table aliases: t

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| tags.XCL_047 | id / identifier / tag id / tag identifier / tag number / tag key | integer | schema / tags |
| tags.XCL_048 | tag name / tag label / tag text / topic name / subject name | text | schema / tags |
| tags.XCL_049 | count / tag count / usage count / number of uses / frequency / occurrences | integer | schema / tags |
| tags.XCL_050 | excerpt post id / excerpt post identifier / excerpt id / tag excerpt post / description post id | integer | schema / tags |
| tags.XCL_051 | wiki post id / wiki post identifier / wiki id / tag wiki post / full description post id | integer | schema / tags |

## users

Stores registered user accounts and profiles for the Stack Exchange community platform.

Recovered table names: users / user / people / members / contributors
SQL table aliases: u

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| users.XCL_052 | id / identifier / user id / user identifier / user number / user key | integer | schema / users |
| users.XCL_053 | reputation / reputation points / reputation score / points / karma | integer | schema / users |
| users.XCL_054 | creation date / join date / registration date / signup date / account created | datetime | schema / users |
| users.XCL_055 | display name / username / screen name / handle / nickname | text | schema / users |
| users.XCL_056 | last access date / last login / last visit / last activity / last seen | datetime | schema / users |
| users.XCL_057 | website url / website / homepage / personal site / web address / URL | text | schema / users |
| users.XCL_058 | location / city / region / place / geographic location / hometown | text | schema / users |
| users.XCL_059 | about me / bio / biography / about / description / profile text | text | schema / users |
| users.XCL_060 | views / profile views / page views / visits / view count | integer | schema / users |
| users.XCL_061 | up votes / upvotes / positive votes / likes received | integer | schema / users |
| users.XCL_062 | down votes / downvotes / negative votes / dislikes received | integer | schema / users |
| users.XCL_063 | account id / account identifier / global account id / network account id / parent account | integer | schema / users |
| users.XCL_064 | age / user age / age in years / years old | integer | schema / users |
| users.XCL_065 | profile image url / avatar / profile picture / user image / photo / gravatar | text | schema / users |

## votes

Records votes cast by users on posts, including bounty awards and vote types.

Recovered table names: votes / vote / voting / poll / ballot / rating
SQL table aliases: v

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| votes.XCL_066 | id / identifier / vote id / vote identifier / record id / primary key | integer | schema / votes |
| votes.XCL_067 | post id / post identifier / question id / answer id / target post | integer | schema / votes |
| votes.XCL_068 | vote type id / vote type identifier / vote type / vote category / vote kind / vote class | integer | schema / votes |
| votes.XCL_069 | creation date / vote date / date voted / timestamp / vote time | date | schema / votes |
| votes.XCL_070 | user id / user identifier / voter id / voter identifier | integer | schema / votes |
| votes.XCL_071 | bounty amount / bounty / bounty points / reward amount / bonus | integer | schema / votes |

## Relationships and join evidence

- badges.XCL_002 ↔ users.XCL_052; declared_or_materialized_relationship
- comments.XCL_006 ↔ posts.XCL_026; declared_or_materialized_relationship
- comments.XCL_010 ↔ users.XCL_052; declared_or_materialized_relationship
- postHistory.XCL_014 ↔ posts.XCL_026; declared_or_materialized_relationship
- postHistory.XCL_017 ↔ users.XCL_052; declared_or_materialized_relationship
- postLinks.XCL_023 ↔ posts.XCL_026; declared_or_materialized_relationship
- postLinks.XCL_024 ↔ posts.XCL_026; declared_or_materialized_relationship
- posts.XCL_026 ↔ tags.XCL_050; declared_or_materialized_relationship
- posts.XCL_026 ↔ votes.XCL_067; declared_or_materialized_relationship
- posts.XCL_033 ↔ users.XCL_052; declared_or_materialized_relationship
- posts.XCL_040 ↔ users.XCL_052; declared_or_materialized_relationship
- users.XCL_052 ↔ votes.XCL_070; declared_or_materialized_relationship

## Business definitions, population and grain


## Incremental maintenance events

