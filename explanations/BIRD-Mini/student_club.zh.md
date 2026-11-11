# BIRD-Mini / student_club — Schema 与业务口径解释

该数据库的存档目录包含 8 张表、48 个物理列、8 条关系，以及 8 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## event

Stores information about student club events, including their names, dates, types, locations, statuses, and notes.

恢复表名: event / events / club events / student club events / activities
SQL表别名: e, ev

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| event.XCL_010 | event id / event identifier / event key / event code | text | schema / event |
| event.XCL_011 | event name / event title / event description / event label | text | schema / event |
| event.XCL_012 | event date / event datetime / event timestamp / event time / event start time | text | schema / event |
| event.XCL_013 | type / event type / event category / event kind / event classification | text | schema / event |
| event.XCL_014 | notes / event notes / event description / event details / event comments / event remarks | text | schema / event |
| event.XCL_015 | location / event location / event venue / event place / event address / event site | text | schema / event |
| event.XCL_016 | status / event status / event state / event condition / event phase | text | schema / event |

## major

Stores information about academic majors offered at the university, including their names, departments, and colleges.

恢复表名: major / majors / fields of study / academic programs / degree programs
SQL表别名: m, ma

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| major.XCL_030 | major id / major identifier / major code / major key | text | schema / major |
| major.XCL_031 | major name / major title / field of study / program name / degree name | text | schema / major |
| major.XCL_032 | department / department name / academic department / department offering | text | schema / major |
| major.XCL_033 | college / college name / academic college / school / faculty | text | schema / major |

## zip_code

Stores geographic location information for US postal codes, including city, county, state, and type of zip code.

恢复表名: zip code / zip codes / postal codes / zips / postal code table
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| zip_code.XCL_043 | zip code / postal code / zip / postal code number / 5-digit zip | integer | schema / zip_code |
| zip_code.XCL_044 | type / zip code type / delivery type / classification / kind | text | schema / zip_code |
| zip_code.XCL_045 | city / city name / town / municipality / place | text | schema / zip_code |
| zip_code.XCL_046 | county / county name / parish / borough / municipio | text | schema / zip_code |
| zip_code.XCL_047 | state / state name / full state name / province / region | text | schema / zip_code |
| zip_code.XCL_048 | short state / state abbreviation / state code / two-letter state / USPS state code | text | schema / zip_code |

## attendance

Records which members attended which events, linking members to events.

恢复表名: attendance / attendance records / event attendance / member attendance / attendance log
SQL表别名: a

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| attendance.XCL_001 | link to event / event / event ID / event link / event reference / event identifier | text | schema / attendance |
| attendance.XCL_002 | link to member / member / member ID / member link / member reference / member identifier / attendee | text | schema / attendance |

## budget

Tracks budget allocations, spending, and remaining funds for club events and categories.

恢复表名: budget / budgets / budget items / budget records
SQL表别名: b

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| budget.XCL_003 | budget id / budget identifier / budget record ID / budget key | text | schema / budget |
| budget.XCL_004 | category / budget category / expense category / spending category / budget type | text | schema / budget |
| budget.XCL_005 | spent / amount spent / expenditure / money spent / spending amount | real | schema / budget |
| budget.XCL_006 | remaining / remaining amount / budget left / unspent amount / balance | real | schema / budget |
| budget.XCL_007 | amount / budget amount / allocated amount / total budget / budgeted amount | integer | schema / budget |
| budget.XCL_008 | event status / status / budget status / planning status | text | schema / budget |
| budget.XCL_009 | link to event / event link / related event / event reference / event ID | text | schema / budget |

## expense

Records each expense incurred by the student club, including description, date, cost, approval status, and links to the member who submitted it and the budget it belongs to.

恢复表名: expense / expenses / spending / costs / outlays / expenditures
SQL表别名: e

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| expense.XCL_017 | expense id / expense identifier / expense record ID / expense key | text | schema / expense |
| expense.XCL_018 | expense description / description / item / expense item / purchase description / what was bought / expense detail | text | schema / expense |
| expense.XCL_019 | expense date / date / transaction date / purchase date / spending date | text | schema / expense |
| expense.XCL_020 | cost / amount / expense amount / price / spending amount / cost amount / dollar amount | real | schema / expense |
| expense.XCL_021 | approved / approval status / is approved / approved flag / approval / approved? | text | schema / expense |
| expense.XCL_022 | link to member / member ID / member link / submitted by / member reference / member foreign key | text | schema / expense |
| expense.XCL_023 | link to budget / budget ID / budget link / budget reference / budget foreign key / associated budget | text | schema / expense |

## income

Records all monetary inflows to the student club, including dues, fundraising, school appropriations, and sponsorships.

恢复表名: income / incomes / revenue / funds received / money collected
SQL表别名: i

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| income.XCL_024 | income id / income identifier / record ID / transaction ID / income key | text | schema / income |
| income.XCL_025 | date received / received date / payment date / transaction date / date of receipt | text | schema / income |
| income.XCL_026 | amount / income amount / dollar amount / value / sum / total | integer | schema / income |
| income.XCL_027 | source / income source / revenue source / funding source / category / type | text | schema / income |
| income.XCL_028 | notes / description / comments / remarks / details | text | schema / income |
| income.XCL_029 | link to member / member ID / associated member / payer / member link | text | schema / income |

## member

Stores information about each member of the student club, including personal details, contact info, position, and links to major and zip code.

恢复表名: member / members / club_members / student_members
SQL表别名: m, mem

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| member.XCL_034 | member id / member identifier / member record ID / member key | text | schema / member |
| member.XCL_035 | first name / given name / forename | text | schema / member |
| member.XCL_036 | last name / surname / family name | text | schema / member |
| member.XCL_037 | email / email address / e-mail | text | schema / member |
| member.XCL_038 | position / role / office / title / member position | text | schema / member |
| member.XCL_039 | t shirt size / t-shirt size / shirt size / tee size / size | text | schema / member |
| member.XCL_040 | phone / phone number / telephone / contact number / mobile | text | schema / member |
| member.XCL_041 | zip / zip code / postal code | integer | schema / member |
| member.XCL_042 | link to major / major link / major ID / major reference / major foreign key | text | schema / member |

## 表关系与连接依据

- attendance.XCL_001 ↔ event.XCL_010; declared_or_materialized_relationship
- attendance.XCL_002 ↔ member.XCL_034; declared_or_materialized_relationship
- budget.XCL_003 ↔ expense.XCL_023; declared_or_materialized_relationship
- budget.XCL_009 ↔ event.XCL_010; declared_or_materialized_relationship
- expense.XCL_022 ↔ member.XCL_034; declared_or_materialized_relationship
- income.XCL_029 ↔ member.XCL_034; declared_or_materialized_relationship
- major.XCL_030 ↔ member.XCL_042; declared_or_materialized_relationship
- member.XCL_041 ↔ zip_code.XCL_043; declared_or_materialized_relationship

## 业务口径、总体与粒度


## 增量维护事件

