# BEAVER / dw — Schema 与业务口径解释

该数据库的存档目录包含 97 张表、1530 个物理列、1965 条关系，以及 1098 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## ACADEMIC_TERMS

Stores metadata for academic terms (semesters) including codes, descriptions, dates, academic years, and status flags.

恢复表名: academic terms / term / terms / academic term / semester / semesters / term calendar / academic calendar
SQL表别名: a, at, at2, t, t0, t1, t2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ACADEMIC_TERMS.ACADEMIC_TERMS_KEY | academic terms key / term key / key / id / primary key | varchar(127) | dw_3966, dw_4397, dw_4400 |
| ACADEMIC_TERMS.TERM_CODE | term code / term / semester code / term id / code / term identifier | varchar(127) | dw_3966, dw_1305, dw_4325, dw_4410, dw_4804, dw_1049, dw_2181, dw_4397 |
| ACADEMIC_TERMS.TERM_DESCRIPTION | term description / term name / semester name / description / term label | varchar(127) | dw_3966, dw_1305, dw_4325, dw_4410, dw_2181, dw_4397, dw_4400, dw_1722 |
| ACADEMIC_TERMS.TERM_SELECTOR | term selector / display term / term label / combined term info | varchar(127) | schema / ACADEMIC_TERMS |
| ACADEMIC_TERMS.TERM_START_DATE | term start date / start date / semester start / begin date / first day | varchar(255) | dw_1305, dw_4325, dw_1722, dw_1752, dw_1776 |
| ACADEMIC_TERMS.TERM_END_DATE | term end date / end date / semester end / finish date / last day | varchar(255) | dw_1305, dw_1752, dw_1776 |
| ACADEMIC_TERMS.ACADEMIC_YEAR | academic year / year / school year / year number / ay | varchar(127) | dw_3966, dw_1305, dw_4325, dw_4410, dw_4804, dw_4397, dw_4400, dw_1722 |
| ACADEMIC_TERMS.ACADEMIC_YEAR_DESC | academic year desc / academic year description / year description / school year name / year label | varchar(127) | dw_1305, dw_4410, dw_4804, dw_1722, dw_1752 |
| ACADEMIC_TERMS.IS_CURRENT_TERM | is current term / current term flag / active term / current status | varchar(127) | dw_1049 |
| ACADEMIC_TERMS.IS_REGULAR_TERM | is regular term / regular term flag / standard term / regular status | varchar(127) | dw_3966, dw_4410, dw_4804, dw_1049, dw_4397, dw_4400, dw_1722, dw_1776 |
| ACADEMIC_TERMS.TERM_STATUS_INDICATOR | term status indicator / status code / term status code / indicator | varchar(127) | dw_4410 |
| ACADEMIC_TERMS.TERM_STATUS | term status / status / term state / status description | varchar(127) | dw_3966, dw_4325, dw_4397, dw_4400 |
| ACADEMIC_TERMS.FINANCIAL_AID_YEAR | financial aid year / fa year / aid year / financial year | varchar(127) | dw_3966, dw_4804, dw_4397, dw_4400 |
| ACADEMIC_TERMS.DEGREE_YEAR | degree year / graduation year / completion year / degree completion year | varchar(127) | dw_4804 |
| ACADEMIC_TERMS.LAST_DAY_OF_FINAL_EXAM | last day of final exam / final exam end / exam end date / last exam day | varchar(255) | dw_4325 |
| ACADEMIC_TERMS.PRE_REGISTRATION_START_DAY | pre registration start day / pre-reg start / early registration start / pre-registration date | varchar(255) | schema / ACADEMIC_TERMS |
| ACADEMIC_TERMS.REGISTRATION_DAY | registration day / registration date / reg date / enrollment start | varchar(255) | schema / ACADEMIC_TERMS |
| ACADEMIC_TERMS.FIRST_DAY_OF_CLASSES | first day of classes / classes start / start of classes / first class day | varchar(255) | dw_2181 |
| ACADEMIC_TERMS.LAST_DAY_OF_CLASSES | last day of classes / classes end / end of classes / last class day | varchar(255) | schema / ACADEMIC_TERMS |
| ACADEMIC_TERMS.ADD_DATE | add date / add deadline / last day to add / add drop start | varchar(255) | schema / ACADEMIC_TERMS |
| ACADEMIC_TERMS.DROP_DATE | drop date / drop deadline / last day to drop / add drop end | varchar(255) | schema / ACADEMIC_TERMS |
| ACADEMIC_TERMS.GRADUATE_AWARD_START_DATE | graduate award start date / grad award start / graduate stipend start / award start | varchar(255) | schema / ACADEMIC_TERMS |
| ACADEMIC_TERMS.GRADUATE_AWARD_END_DATE | graduate award end date / grad award end / graduate stipend end / award end | varchar(255) | schema / ACADEMIC_TERMS |
| ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE | warehouse load date / load date / etl date / data load date | varchar(255) | schema / ACADEMIC_TERMS |

## ACADEMIC_TERMS_ALL

Reference table containing metadata for all academic terms, including term codes, descriptions, start/end dates, academic years, and status indicators, used to join with course and enrollment data.

恢复表名: academic terms all / academic terms / term master / academic calendar / term reference / semester info / academic year terms
SQL表别名: a, at, ata, ata2, t, t0, t1, t2, t3, ta

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ACADEMIC_TERMS_ALL.ACADEMIC_TERMS_KEY | academic terms key / term key / term id / primary key / unique term identifier | varchar(127) | dw_5037, dw_4474, dw_3872, dw_3952, dw_4266, dw_4337 |
| ACADEMIC_TERMS_ALL.TERM_CODE | term code / semester code / term identifier / academic term code / term abbreviation | varchar(127) | dw_4024, dw_5037, dw_1339, dw_4474, dw_1811, dw_3162, dw_3872, dw_3952 |
| ACADEMIC_TERMS_ALL.TERM_DESCRIPTION | term description / semester name / term name / academic term description / full term name | varchar(127) | dw_4024, dw_5037, dw_1339, dw_1811, dw_3162, dw_3872, dw_3952, dw_4058 |
| ACADEMIC_TERMS_ALL.TERM_SELECTOR | term selector / term display value / term label / combined term code and description | varchar(127) | schema / ACADEMIC_TERMS_ALL |
| ACADEMIC_TERMS_ALL.TERM_START_DATE | term start date / semester start date / start date / term beginning date | varchar(255) | dw_4024, dw_1339, dw_4474, dw_1811, dw_3162, dw_4058, dw_4276 |
| ACADEMIC_TERMS_ALL.TERM_END_DATE | term end date / semester end date / end date / term completion date | varchar(255) | dw_4024, dw_4474, dw_3162, dw_4058, dw_4276 |
| ACADEMIC_TERMS_ALL.ACADEMIC_YEAR | academic year / year / school year / term year | varchar(127) | dw_4024, dw_1339, dw_4474, dw_1811, dw_3162, dw_3872, dw_3952, dw_4058 |
| ACADEMIC_TERMS_ALL.ACADEMIC_YEAR_DESC | academic year desc / academic year description / year description / full academic year name / school year description | varchar(127) | dw_4024, dw_5037, dw_1339, dw_4474, dw_1811, dw_3872, dw_3952, dw_4058 |
| ACADEMIC_TERMS_ALL.IS_CURRENT_TERM | is current term / current term flag / active term indicator / current semester flag | varchar(127) | dw_1339, dw_1811 |
| ACADEMIC_TERMS_ALL.TERM_STATUS_INDICATOR | term status indicator / term status / status indicator / term state / past current future indicator | varchar(127) | dw_4024, dw_4474, dw_3162, dw_4276 |
| ACADEMIC_TERMS_ALL.FINANCIAL_AID_YEAR | financial aid year / aid year / fiscal year for aid / financial year | varchar(127) | dw_5037, dw_3872, dw_3952, dw_4266, dw_4337 |
| ACADEMIC_TERMS_ALL.DEGREE_YEAR | degree year / graduation year / class year / academic degree year | varchar(127) | schema / ACADEMIC_TERMS_ALL |
| ACADEMIC_TERMS_ALL.LAST_DAY_OF_FINAL_EXAM | last day of final exam / final exam end date / exam end date / last exam day | varchar(255) | dw_5037 |
| ACADEMIC_TERMS_ALL.PRE_REGISTRATION_START_DAY | pre registration start day / pre-registration start day / pre-reg start date / early registration start / pre-registration date | varchar(255) | schema / ACADEMIC_TERMS_ALL |
| ACADEMIC_TERMS_ALL.REGISTRATION_DAY | registration day / registration date / enrollment start date / reg date | varchar(255) | schema / ACADEMIC_TERMS_ALL |
| ACADEMIC_TERMS_ALL.FIRST_DAY_OF_CLASSES | first day of classes / classes start date / semester start / instruction start date | varchar(255) | schema / ACADEMIC_TERMS_ALL |
| ACADEMIC_TERMS_ALL.LAST_DAY_OF_CLASSES | last day of classes / classes end date / semester end / instruction end date | varchar(255) | schema / ACADEMIC_TERMS_ALL |
| ACADEMIC_TERMS_ALL.GRADUATE_AWARD_START_DATE | graduate award start date / grad award start / graduate term start / grad start date | varchar(255) | schema / ACADEMIC_TERMS_ALL |
| ACADEMIC_TERMS_ALL.GRADUATE_AWARD_END_DATE | graduate award end date / grad award end / graduate term end / grad end date | varchar(255) | schema / ACADEMIC_TERMS_ALL |
| ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE | warehouse load date / load date / etl date / data load timestamp | varchar(255) | schema / ACADEMIC_TERMS_ALL |

## ACADEMIC_TERM_PARAMETER

Stores parameterized definitions and status indicators for academic terms, mapping specific term codes to SIS parameters (current, previous, upcoming) and providing key dates and descriptions for term-based reporting.

恢复表名: academic term parameter / Term Parameter / Academic Term Parameters / Term Parameters / SIS Term Parameter / Academic Term Status / Term Status Parameter
SQL表别名: atp, p, t1, t2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ACADEMIC_TERM_PARAMETER.TERM_PARAMETER | term parameter / SIS Parameter / Parameter Name / Term Type Parameter / SIS Term Type / Parameter Code | varchar(127) | dw_3417, dw_3729, dw_3472, dw_3630, dw_3694, dw_4414, dw_4474, dw_4667 |
| ACADEMIC_TERM_PARAMETER.TERM_INDICATOR | term indicator / Status Indicator / Term Status / Indicator Code / Term Flag / Status Code | varchar(127) | dw_3417, dw_3472, dw_3630, dw_3694, dw_4789, dw_4833, dw_5062 |
| ACADEMIC_TERM_PARAMETER.TERM_CODE | term code / Academic Term Code / Term ID / SIS Term Code / Term Identifier / Term Key | varchar(127) | dw_3417, dw_3729, dw_3472, dw_3630, dw_3694, dw_4414, dw_4474, dw_4667 |
| ACADEMIC_TERM_PARAMETER.TERM_DESCRIPTION | term description / Term Name / Academic Term Name / Term Label / Full Term Name / Term Title | varchar(127) | dw_3729, dw_4414, dw_4474, dw_4667 |
| ACADEMIC_TERM_PARAMETER.TERM_START_DATE | term start date / Start Date / Term Beginning Date / Academic Term Start / First Day of Term / Term Open Date | varchar(255) | dw_3417, dw_3472, dw_3630, dw_3694, dw_4789, dw_4833, dw_5062 |
| ACADEMIC_TERM_PARAMETER.TERM_END_DATE | term end date / End Date / Term Closing Date / Academic Term End / Last Day of Term / Term Close Date | varchar(255) | schema / ACADEMIC_TERM_PARAMETER |
| ACADEMIC_TERM_PARAMETER.TERM_LAST_DAY_BEFORE_NEXT_TERM | term last day before next term / Last Day Before Next Term / Term Gap End Date / Pre-Next-Term Date / Inter-Term End Date / Last Day Before Next Academic Term / Term Transition Date | varchar(255) | schema / ACADEMIC_TERM_PARAMETER |
| ACADEMIC_TERM_PARAMETER.IS_CURRENT_TERM | is current term / Current Term Flag / Current Term Indicator / Active Term Flag / Is Active Term / Current Term Status | varchar(127) | dw_3729, dw_4414, dw_4474, dw_4667, dw_1202 |

## BUILDINGS

Stores master data for physical buildings including identifiers, names, addresses, and square footage metrics.

恢复表名: buildings / building / building_master / property_buildings / real_estate_buildings / facility_buildings
SQL表别名: b

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| BUILDINGS.BUILDING_KEY | building key / building_key / building_id / building_code / bldg_key / building_identifier | varchar(127) | schema / BUILDINGS |
| BUILDINGS.BUILDING_NUMBER | building number / building_number / bldg_number / building_no / building_id / building_code | varchar(127) | schema / BUILDINGS |
| BUILDINGS.BUILDING_NAME | building name / building_name / bldg_name / building_title / property_name / facility_name | varchar(127) | schema / BUILDINGS |
| BUILDINGS.BUILDING_STREET_ADDRESS | building street address / street_address / building_address / physical_address / bldg_street_addr / location_address | varchar(127) | schema / BUILDINGS |
| BUILDINGS.BUILDING_MAILING_ADDRESS | building mailing address / mailing_address / postal_address / building_mailing_addr / bldg_mailing_addr / correspondence_address | varchar(127) | schema / BUILDINGS |
| BUILDINGS.BLDG_GROSS_SQUARE_FOOTAGE | bldg gross square footage / gross_square_footage / total_square_feet / bldg_gross_sqft / gross_area / total_building_area | int | schema / BUILDINGS |
| BUILDINGS.BLDG_ASSIGNABLE_SQUARE_FOOTAGE | bldg assignable square footage / assignable_square_footage / net_square_feet / bldg_assignable_sqft / rentable_area / usable_area | int | schema / BUILDINGS |
| BUILDINGS.BUILDING_COUNTER | building counter / building_counter / row_number / sequence_number / bldg_counter / record_index | int | schema / BUILDINGS |
| BUILDINGS.WAREHOUSE_LOAD_DATE | warehouse load date / load_date / warehouse_load_date / data_load_date / etl_date / last_updated | varchar(255) | schema / BUILDINGS |

## CIP

Reference table for the Classification of Instructional Programs (CIP) codes, providing hierarchical program codes, titles, and categories for academic programs.

恢复表名: cip / Classification of Instructional Programs / CIP Codes / Program Classification / Academic Program Codes / CIP Reference / Program Taxonomy
SQL表别名: c, cip, t0

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| CIP.PROGRAM_CODE | program code / CIP Code / CIP Program Code / Instructional Program Code / 6-Digit CIP Code / Program Identifier | varchar(127) | dw_1997, dw_367, dw_220, dw_2268, dw_2704, dw_3017, dw_3755, dw_3790 |
| CIP.PROGRAM_TITLE | program title / Program Name / CIP Program Title / Instructional Program Title / Academic Program Name / Program Description / Specific Program Title | varchar(127) | dw_1997, dw_367, dw_220, dw_2268, dw_2704, dw_3017, dw_3755, dw_3790 |
| CIP.CATEGORY_CODE | category code / CIP Category Code / Program Category Code / Broad Category Code / CIP Group Code / Category Identifier / Top-Level CIP Code | varchar(127) | dw_1997, dw_220, dw_2268, dw_2704, dw_3017, dw_3755, dw_3790, dw_3806 |
| CIP.CATEGORY_TITLE | category title / CIP Category Title / Program Category Name / Broad Category Name / CIP Group Title / Category Description / Top-Level Category Title | varchar(127) | dw_1997, dw_367, dw_220, dw_2268, dw_2704, dw_3017, dw_3755, dw_3790 |
| CIP.FOUR_DIGIT_CODE | four digit code / 4-Digit CIP Code / CIP Family Code / Program Family Code / Intermediate CIP Code / 4-Digit Program Code / CIP Subcategory Code | varchar(127) | dw_1997, dw_220, dw_2268, dw_2704, dw_3017, dw_3755, dw_3790, dw_3806 |
| CIP.FOUR_DIGIT_TITLE | four digit title / 4-Digit CIP Title / CIP Family Title / Program Family Name / Intermediate CIP Title / 4-Digit Program Title / CIP Subcategory Title | varchar(127) | dw_1997, dw_220, dw_2268, dw_2704, dw_3017, dw_3755, dw_3790, dw_3806 |
| CIP.NOTE | note / CIP Note / Program Note / Change Note / Version Note / CIP Revision Note / Program Status Note | varchar(127) | schema / CIP |
| CIP.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date / Warehouse Date / Record Load Date / Data Refresh Date | varchar(255) | dw_1997, dw_220, dw_2268, dw_2704, dw_3017, dw_3755, dw_3790, dw_3806 |
| CIP.VERSION | version / CIP Version / Taxonomy Version / Year Version / CIP Year / Program Version / Classification Version | varchar(127) | dw_367 |

## CIP_WITH_VERSION

Stores versioned CIP (Classification of Instructional Programs) codes, titles, and hierarchical categories for educational programs.

恢复表名: cip with version / CIP versioned / CIP code version / CIP program version / CIP classification version / CIP with year
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| CIP_WITH_VERSION.CIP_WITH_VERSION_KEY | cip with version key / CIP version key / CIP key / CIP code key / CIP identifier / CIP ID | varchar(127) | schema / CIP_WITH_VERSION |
| CIP_WITH_VERSION.VERSION | version / CIP version / version year / CIP year / classification version / CIP edition | varchar(127) | schema / CIP_WITH_VERSION |
| CIP_WITH_VERSION.PROGRAM_CODE | program code / CIP code / CIP program code / instructional program code / CIP 6-digit code / program identifier | varchar(127) | schema / CIP_WITH_VERSION |
| CIP_WITH_VERSION.PROGRAM_TITLE | program title / CIP title / CIP program title / instructional program title / program name / CIP description | varchar(127) | schema / CIP_WITH_VERSION |
| CIP_WITH_VERSION.CATEGORY_CODE | category code / CIP category code / CIP 2-digit code / broad category code / CIP category / category identifier | varchar(127) | schema / CIP_WITH_VERSION |
| CIP_WITH_VERSION.CATEGORY_TITLE | category title / CIP category title / CIP broad category title / category name / broad category name / CIP category description | varchar(127) | schema / CIP_WITH_VERSION |
| CIP_WITH_VERSION.FOUR_DIGIT_CODE | four digit code / CIP 4-digit code / CIP family code / family code / CIP 4-digit identifier / program family code | varchar(127) | schema / CIP_WITH_VERSION |
| CIP_WITH_VERSION.FOUR_DIGIT_TITLE | four digit title / CIP 4-digit title / CIP family title / family title / CIP 4-digit description / program family title | varchar(127) | schema / CIP_WITH_VERSION |
| CIP_WITH_VERSION.WAREHOUSE_LOAD_DATE | warehouse load date / load date / ETL date / data load date / insert date / load timestamp | varchar(255) | schema / CIP_WITH_VERSION |

## CIS_COURSE_CATALOG

Stores detailed metadata for academic subjects/courses in the course catalog, including department, units, grading rules, offering terms, and attributes for a specific academic year.

恢复表名: cis course catalog / course catalog / catalog / course catalog table / subject catalog / course catalog data / catalog subjects
SQL表别名: c, ccat, ccc, t1

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| CIS_COURSE_CATALOG.IS_OFFERED_FALL_TERM | is offered fall term / offered fall / fall term offered / is fall / fall availability / offered in fall | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.IS_OFFERED_IAP | is offered iap / offered iap / independent activities period / is iap / iap availability / offered in iap | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.IS_OFFERED_SPRING_TERM | is offered spring term / offered spring / spring term offered / is spring / spring availability / offered in spring | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.IS_OFFERED_SUMMER_TERM | is offered summer term / offered summer / summer term offered / is summer / summer availability / offered in summer | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.FALL_INSTRUCTORS | fall instructors / fall instructor / fall faculty / instructor fall / fall teacher / fall professor | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.SPRING_INSTRUCTORS | spring instructors / spring instructor / spring faculty / instructor spring / spring teacher / spring professor | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.STATUS_CHANGE | status change / catalog status change / subject status change / change in status / status update | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.LAST_ACTIVITY_DATE | last activity date / last updated / last modified date / activity date / last change date | varchar(255) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE | warehouse load date / etl load date / data load date / load date / warehouse date | varchar(255) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.MASTER_SUBJECT_ID | master subject id / master subject identifier / master id / primary subject id / master course id / subject master key | varchar(127) | dw_5279 |
| CIS_COURSE_CATALOG.HASS_ATTRIBUTE | hass attribute / hass code / hass requirement / hass category / hass flag | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.HASS_ATTRIBUTE_DESC | hass attribute desc / hass attribute description / hass description / hass text / hass requirement description / hass category name | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.TERM_DURATION | term duration / duration / term length / course duration / time span | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.GLOBAL_REGIONS | global regions / regions / world regions / geographic regions / region list | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.GLOBAL_COUNTRIES | global countries / countries / world countries / geographic countries / country list | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.ON_LINE_PAGE_NUMBER | on line page number / online page number / page number / catalog page / web page number / online catalog page | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.ACADEMIC_YEAR | academic year / year / catalog year / school year / fiscal year | varchar(127) | dw_1302, dw_5279, dw_1306, dw_1027, dw_1266, dw_1717, dw_2411 |
| CIS_COURSE_CATALOG.SUBJECT_ID | subject id / subject identifier / course id / subject number / course number / subject key | varchar(127) | dw_1302, dw_1306, dw_1027, dw_1266, dw_2411 |
| CIS_COURSE_CATALOG.SUBJECT_CODE | subject code / course code / department code / dept code / subject prefix | varchar(127) | dw_1302, dw_1733, dw_1306, dw_1717 |
| CIS_COURSE_CATALOG.SUBJECT_NUMBER | subject number / course number / subject seq / course seq / subject suffix | varchar(127) | dw_1302, dw_1306 |
| CIS_COURSE_CATALOG.SOURCE_SUBJECT_ID | source subject id / source subject identifier / original subject id / source id / origin subject id / source course id | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.PRINT_SUBJECT_ID | print subject id / print subject identifier / printed subject id / print id / bulletin subject id / print course id | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.IS_PRINTED_IN_BULLETIN | is printed in bulletin / printed in bulletin / in bulletin / bulletin flag / print flag / catalog printed | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.DEPARTMENT_CODE | department code / dept code / department id / dept id / department number | varchar(127) | dw_1302, dw_2272, dw_4868, dw_1733, dw_3163, dw_1306, dw_1027, dw_1266 |
| CIS_COURSE_CATALOG.DEPARTMENT_NAME | department name / dept name / department / academic department / school department | varchar(127) | dw_50, dw_1027, dw_1266, dw_1717, dw_2411 |
| CIS_COURSE_CATALOG.EFFECTIVE_TERM_CODE | effective term code / term code / effective term / start term / term identifier | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.SUBJECT_SHORT_TITLE | subject short title / short title / subject short name / course short title / abbreviated title / short course name | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.SUBJECT_TITLE | subject title / course title / course name / subject name / full title | varchar(127) | dw_4868 |
| CIS_COURSE_CATALOG.IS_VARIABLE_UNITS | is variable units / variable units / is variable / variable credit / flexible units / unit variability | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.LECTURE_UNITS | lecture units / lecture credits / lecture hours / class units / lecture workload | int | dw_2272 |
| CIS_COURSE_CATALOG.LAB_UNITS | lab units | int | dw_2272 |
| CIS_COURSE_CATALOG.PREPARATION_UNITS | preparation units | int | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.TOTAL_UNITS | total units | int | dw_1302, dw_2272, dw_1733, dw_3163, dw_1306, dw_1027, dw_1266, dw_1717 |
| CIS_COURSE_CATALOG.DESIGN_UNITS | design units | int | dw_3163 |
| CIS_COURSE_CATALOG.GRADE_TYPE | grade type | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.GRADE_TYPE_DESC | grade type desc / grade type description | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.GRADE_RULE | grade rule | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.GRADE_RULE_DESC | grade rule desc / grade rule description | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.HGN_CODE | hgn code | varchar(127) | dw_50 |
| CIS_COURSE_CATALOG.HGN_DESC | hgn desc / hgn description | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.HGN_EXCEPT | hgn except | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.GIR_ATTRIBUTE | gir attribute | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.GIR_ATTRIBUTE_DESC | gir attribute desc / gir attribute description | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.COMM_REQ_ATTRIBUTE | comm req attribute | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.COMM_REQ_ATTRIBUTE_DESC | comm req attribute desc / comm req attribute description | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.TUITION_ATTRIBUTE | tuition attribute | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.TUITION_ATTRIBUTE_DESC | tuition attribute desc / tuition attribute description | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.WRITE_REQ_ATTRIBUTE | write req attribute | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.WRITE_REQ_ATTRIBUTE_DESC | write req attribute desc / write req attribute description | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.SUPERVISOR_ATTRIBUTE | supervisor attribute | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.SUPERVISOR_ATTRIBUTE_DESC | supervisor attribute desc / supervisor attribute description | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.PREREQUISITES | prerequisites | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.SUBJECT_DESCRIPTION | subject description | varchar(127) | dw_4868 |
| CIS_COURSE_CATALOG.JOINT_SUBJECTS | joint subjects | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.SCHOOL_WIDE_ELECTIVES | school wide electives | varchar(127) | dw_50 |
| CIS_COURSE_CATALOG.MEETS_WITH_SUBJECTS | meets with subjects | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.EQUIVALENT_SUBJECTS | equivalent subjects | varchar(127) | schema / CIS_COURSE_CATALOG |
| CIS_COURSE_CATALOG.IS_OFFERED_THIS_YEAR | is offered this year | varchar(127) | dw_1733 |

## CIS_HASS_ATTRIBUTE

Reference table defining HASS (Humanities, Arts, and Social Sciences) attribute codes, their descriptions for forms and bulletins, and associated metadata such as icons and group classifications.

恢复表名: cis hass attribute / HASS Attribute Lookup / Humanities, Arts, and Social Sciences Attribute Reference / HASS Attribute Master / HASS Category Definition / HASS Attribute Code Table
SQL表别名: a, h, t1

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| CIS_HASS_ATTRIBUTE.HASS_ATTRIBUTE | hass attribute / HASS Attribute Code / HASS Code / Attribute ID / HASS Type / HASS Category Code | varchar(127) | dw_538, dw_1589, dw_1713, dw_2700, dw_3018, dw_310, dw_3102, dw_3168 |
| CIS_HASS_ATTRIBUTE.DESCRIPTION_ON_FORM | description on form / Form Description / HASS Description on Form / Attribute Form Label / HASS Form Text / Description for Forms / HASS Elective Label | varchar(127) | dw_538, dw_1589, dw_1713, dw_2700, dw_3018, dw_310, dw_3102, dw_3168 |
| CIS_HASS_ATTRIBUTE.DESCRIPTION_IN_BULLETIN | description in bulletin / Bulletin Description / HASS Description in Bulletin / Attribute Bulletin Label / HASS Bulletin Text / Description for Bulletins / Catalog Description | varchar(127) | dw_538 |
| CIS_HASS_ATTRIBUTE.CIS_ATTRIBUTE_GROUP | cis attribute group / Attribute Group / CIS Group / HASS Group / Attribute Category Group / Group Code / HASS Attribute Group | varchar(127) | schema / CIS_HASS_ATTRIBUTE |
| CIS_HASS_ATTRIBUTE.CIS_ATTRIBUTE_GROUP_NOTE | cis attribute group note / Group Note / Attribute Group Note / CIS Note / HASS Group Note / Group Description / Attribute Group Comment | varchar(127) | schema / CIS_HASS_ATTRIBUTE |
| CIS_HASS_ATTRIBUTE.ICON_GIF_NAME | icon gif name / Icon Name / GIF Name / HASS Icon / Attribute Icon / Icon File / Graphic Name | varchar(127) | schema / CIS_HASS_ATTRIBUTE |
| CIS_HASS_ATTRIBUTE.ICON_HEIGHT | icon height / Height / GIF Height / Attribute Icon Height / Image Height / Pixel Height | varchar(127) | schema / CIS_HASS_ATTRIBUTE |
| CIS_HASS_ATTRIBUTE.ICON_WIDTH | icon width / Width / GIF Width / Attribute Icon Width / Image Width / Pixel Width | varchar(127) | schema / CIS_HASS_ATTRIBUTE |
| CIS_HASS_ATTRIBUTE.LAST_ACTIVITY_DATE | last activity date / Activity Date / Last Modified Date / HASS Activity Date / Attribute Activity Date / Last Action Date | varchar(255) | schema / CIS_HASS_ATTRIBUTE |
| CIS_HASS_ATTRIBUTE.LAST_UPDATE_USER | last update user / Updated By / Last Modified By / HASS Update User / Attribute Update User / Last Editor | varchar(127) | schema / CIS_HASS_ATTRIBUTE |
| CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / ETL Date / Data Load Date / HASS Load Date / Attribute Load Date | varchar(255) | schema / CIS_HASS_ATTRIBUTE |

## COURSE_CATALOG_SUBJECT_OFFERED

Stores detailed information about subjects (courses) offered in the academic catalog, including term, department, units, grading, prerequisites, and section details.

恢复表名: course catalog subject offered / course catalog / subject offered / course offering / catalog subject / subject catalog
SQL表别名: CCSO, c, c2, cco, cco2, ccs, ccs2, ccso, ccso2, co, cso, f, s, s2, t0, t1, t2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| COURSE_CATALOG_SUBJECT_OFFERED.ACADEMIC_YEAR | academic year / year / catalog year / school year | varchar(127) | dw_2498, dw_1771, dw_2526, dw_1471, dw_2090, dw_2158, dw_4459, dw_1601 |
| COURSE_CATALOG_SUBJECT_OFFERED.TERM_CODE | term code / term / semester code / academic term / term identifier | varchar(127) | dw_1771, dw_4730, dw_4459 |
| COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_ID | subject id / subject identifier / course id / course number / subject code full | varchar(127) | dw_2498, dw_2526, dw_4730, dw_2158, dw_4459, dw_1601, dw_2015, dw_2376 |
| COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_CODE | subject code / department code / course department / department number / course prefix | varchar(127) | dw_2498, dw_1771, dw_1471, dw_2090, dw_4459, dw_3178 |
| COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_NUMBER | subject number / course number / subject suffix / course sequence number | varchar(127) | dw_2498, dw_1771, dw_2090, dw_3178 |
| COURSE_CATALOG_SUBJECT_OFFERED.SOURCE_SUBJECT_ID | source subject id / source subject identifier / original subject id / source course id | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.PRINT_SUBJECT_ID | print subject id / print subject identifier / catalog subject id / display subject id | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.IS_PRINTED_IN_BULLETIN | is printed in bulletin / printed in bulletin / in catalog / bulletin flag / catalog visibility | varchar(127) | dw_1601 |
| COURSE_CATALOG_SUBJECT_OFFERED.DEPARTMENT_CODE | department code / dept code / department identifier / course department code | varchar(127) | dw_2498, dw_2526, dw_1471, dw_2158, dw_1601, dw_2376, dw_3178 |
| COURSE_CATALOG_SUBJECT_OFFERED.DEPARTMENT_NAME | department name / dept name / department / offering department / course department name | varchar(127) | dw_2498, dw_1771, dw_2526, dw_4730, dw_1471, dw_2090, dw_4459, dw_2015 |
| COURSE_CATALOG_SUBJECT_OFFERED.EFFECTIVE_TERM_CODE | effective term code / effective term / catalog effective term / term of record | varchar(127) | dw_1771, dw_2090, dw_4459, dw_2015 |
| COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_SHORT_TITLE | subject short title / short title / subject short name / course short title / abbreviated title | varchar(127) | dw_2498, dw_2090 |
| COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_TITLE | subject title / course title / subject name / course name / full title | varchar(127) | dw_2498, dw_1771, dw_2526, dw_1471, dw_2090, dw_2158, dw_4459, dw_1601 |
| COURSE_CATALOG_SUBJECT_OFFERED.IS_VARIABLE_UNITS | is variable units / variable units / variable credit / flexible units / variable unit flag | varchar(127) | dw_1771, dw_2015 |
| COURSE_CATALOG_SUBJECT_OFFERED.LECTURE_UNITS | lecture units / lecture credits / lecture hours / class units | int | dw_2498, dw_2526, dw_2158, dw_1601, dw_2376 |
| COURSE_CATALOG_SUBJECT_OFFERED.LAB_UNITS | lab units / laboratory units / lab credits / practical units | int | dw_2498 |
| COURSE_CATALOG_SUBJECT_OFFERED.PREPARATION_UNITS | preparation units / prep units / study units / out-of-class units | int | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.TOTAL_UNITS | total units / total credits / credit hours / unit count / total workload | int | dw_2498, dw_1771, dw_2526, dw_1471, dw_2090, dw_2158, dw_1601, dw_2015 |
| COURSE_CATALOG_SUBJECT_OFFERED.DESIGN_UNITS | design units / design credits / studio units | int | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.GRADE_TYPE | grade type / grading type / grade scheme / grading method | varchar(127) | dw_2498, dw_1471, dw_2158 |
| COURSE_CATALOG_SUBJECT_OFFERED.GRADE_TYPE_DESC | grade type desc / grade type description / grading description / grade scheme name | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.GRADE_RULE | grade rule / repeat rule / credit rule / grading rule code | varchar(127) | dw_2498 |
| COURSE_CATALOG_SUBJECT_OFFERED.GRADE_RULE_DESC | grade rule desc / grade rule description / repeat rule description / credit rule text | varchar(127) | dw_4459 |
| COURSE_CATALOG_SUBJECT_OFFERED.HGN_CODE | hgn code / level code / grade level code / student level code | varchar(127) | dw_2376 |
| COURSE_CATALOG_SUBJECT_OFFERED.HGN_DESC | hgn desc / hgn description / level description / grade level / student level | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.HGN_EXCEPT | hgn except / hgn exception / level exception / grade level exception | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.GIR_ATTRIBUTE | gir attribute / gir code / general requirement attribute / elective attribute | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.GIR_ATTRIBUTE_DESC | gir attribute desc / gir attribute description / gir description / general requirement description | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.COMM_REQ_ATTRIBUTE | comm req attribute / communication requirement / cim attribute / communication intensive | varchar(127) | dw_1471 |
| COURSE_CATALOG_SUBJECT_OFFERED.COMM_REQ_ATTRIBUTE_DESC | comm req attribute desc / comm req attribute description / comm req description / communication requirement description / cim description | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.TUITION_ATTRIBUTE | tuition attribute / tuition code / fee attribute | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.TUITION_ATTRIBUTE_DESC | tuition attribute desc / tuition attribute description / tuition description / fee description | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.WRITE_REQ_ATTRIBUTE | write req attribute / writing requirement / writing attribute | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.WRITE_REQ_ATTRIBUTE_DESC | write req attribute desc / write req attribute description / write req description / writing requirement description / writing attribute description | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.SUPERVISOR_ATTRIBUTE | supervisor attribute / thesis attribute / supervision code | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.SUPERVISOR_ATTRIBUTE_DESC | supervisor attribute desc / supervisor attribute description / thesis description / supervision description | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.PREREQUISITES | prerequisites | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_DESCRIPTION | subject description | varchar(127) | dw_2090 |
| COURSE_CATALOG_SUBJECT_OFFERED.JOINT_SUBJECTS | joint subjects | varchar(127) | dw_2158 |
| COURSE_CATALOG_SUBJECT_OFFERED.SCHOOL_WIDE_ELECTIVES | school wide electives | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.MEETS_WITH_SUBJECTS | meets with subjects | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.EQUIVALENT_SUBJECTS | equivalent subjects | varchar(127) | dw_4730 |
| COURSE_CATALOG_SUBJECT_OFFERED.IS_OFFERED_THIS_YEAR | is offered this year | varchar(127) | dw_2498, dw_2526, dw_1471, dw_2158 |
| COURSE_CATALOG_SUBJECT_OFFERED.IS_OFFERED_FALL_TERM | is offered fall term | varchar(127) | dw_1771, dw_4459, dw_2015 |
| COURSE_CATALOG_SUBJECT_OFFERED.IS_OFFERED_IAP | is offered iap | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.IS_OFFERED_SPRING_TERM | is offered spring term | varchar(127) | dw_2015 |
| COURSE_CATALOG_SUBJECT_OFFERED.IS_OFFERED_SUMMER_TERM | is offered summer term | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.FALL_INSTRUCTORS | fall instructors | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.SPRING_INSTRUCTORS | spring instructors | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.STATUS_CHANGE | status change | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.LAST_ACTIVITY_DATE | last activity date | varchar(255) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE | warehouse load date | varchar(255) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.MASTER_SUBJECT_ID | master subject id / master subject identifier | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.HASS_ATTRIBUTE | hass attribute | varchar(127) | dw_3178 |
| COURSE_CATALOG_SUBJECT_OFFERED.HASS_ATTRIBUTE_DESC | hass attribute desc / hass attribute description | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.TERM_DURATION | term duration | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.GLOBAL_REGIONS | global regions | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.GLOBAL_COUNTRIES | global countries | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.ON_LINE_PAGE_NUMBER | on line page number | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.SECTION_ID | section id / section identifier | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.IS_MASTER_SECTION | is master section | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.IS_LECTURE_SECTION | is lecture section | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.IS_LAB_SECTION | is lab section | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.IS_RECITATION_SECTION | is recitation section | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.IS_DESIGN_SECTION | is design section | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |
| COURSE_CATALOG_SUBJECT_OFFERED.RESPONSIBLE_FACULTY_NAME | responsible faculty name | varchar(127) | dw_2526, dw_1601 |
| COURSE_CATALOG_SUBJECT_OFFERED.RESPONSIBLE_FACULTY_MIT_ID | responsible faculty mit id / responsible faculty mit identifier | varchar(127) | dw_2526 |
| COURSE_CATALOG_SUBJECT_OFFERED.MEET_TIME | meet time | varchar(127) | dw_4730 |
| COURSE_CATALOG_SUBJECT_OFFERED.MEET_PLACE | meet place | varchar(127) | schema / COURSE_CATALOG_SUBJECT_OFFERED |

## DRUPAL_COURSE_CATALOG

Stores detailed metadata for academic course subjects, including department, units, grading policies, prerequisites, instructors, and section-level scheduling information for specific academic terms.

恢复表名: drupal course catalog / Course Catalog / Course Offerings / Academic Catalog / Subject Catalog / Course Information / Class Catalog
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| DRUPAL_COURSE_CATALOG.ACADEMIC_YEAR | academic year / Year / Catalog Year / Fiscal Year | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.SUBJECT_ID | subject id / subject identifier / Course ID / Subject Number / Course Code | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.SUBJECT_CODE | subject code / Department Code / Course Prefix / Subject Prefix | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.SUBJECT_NUMBER | subject number / Course Number / Subject Suffix / Course Suffix | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.SOURCE_SUBJECT_ID | source subject id / source subject identifier / Original Subject ID / Source Course ID | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.PRINT_SUBJECT_ID | print subject id / print subject identifier / Bulletin Subject ID / Printed Course ID | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.IS_PRINTED_IN_BULLETIN | is printed in bulletin / Printed in Bulletin / In Bulletin / Bulletin Flag / Printed Flag | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.DEPARTMENT_CODE | department code / Dept Code / Department ID / Dept ID | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.DEPARTMENT_NAME | department name / Dept Name / Department / Academic Department | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.EFFECTIVE_TERM_CODE | effective term code / Effective Term / Term Code / Academic Term / Offering Term | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.SUBJECT_SHORT_TITLE | subject short title / Short Title / Course Short Name / Abbreviated Title | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.SUBJECT_TITLE | subject title / Course Title / Full Title / Course Name | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.IS_VARIABLE_UNITS | is variable units / Variable Units / Variable Credit / Unit Variability / Variable Unit Flag | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.LECTURE_UNITS | lecture units / Lecture Credits / Lecture Hours / Lecture Credit | int | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.LAB_UNITS | lab units / Laboratory Credits / Lab Hours / Laboratory Units | int | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.PREPARATION_UNITS | preparation units / Prep Credits / Preparation Hours / Study Units | int | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.TOTAL_UNITS | total units / Total Credits / Credit Hours / Total Credit | int | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.DESIGN_UNITS | design units / Design Credits / Design Hours / Design Credit | int | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.GRADE_TYPE | grade type / Grading Type / Grade Code / Grading Code | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.GRADE_TYPE_DESC | grade type desc / grade type description / Grading Description / Grade Type Text / Grading System | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.GRADE_RULE | grade rule / Grading Rule / Repeat Rule / Credit Rule | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.GRADE_RULE_DESC | grade rule desc / grade rule description / Grading Rule Description / Repeat Rule Text / Credit Rule Text | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.HGN_CODE | hgn code / Level Code / Grade Level Code / Student Level Code | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.HGN_DESC | hgn desc / hgn description / Level Description / Grade Level Description / Student Level | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.HGN_EXCEPT | hgn except / HGN Exception / Level Exception / Grade Level Exception / Level Exclusion | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.GIR_ATTRIBUTE | gir attribute / General Education Attribute / GIR Code / Gen Ed Attribute | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.GIR_ATTRIBUTE_DESC | gir attribute desc / gir attribute description / General Education Description / GIR Text / Gen Ed Description | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.COMM_REQ_ATTRIBUTE | comm req attribute / Communication Requirement Attribute / Communication Code / Comm Requirement | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.COMM_REQ_ATTRIBUTE_DESC | comm req attribute desc / comm req attribute description / Communication Requirement Description / Comm Req Description / Communication Text / Comm Requirement Text | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.TUITION_ATTRIBUTE | tuition attribute / Tuition Code / Fee Attribute / Tuition Flag | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.TUITION_ATTRIBUTE_DESC | tuition attribute desc / tuition attribute description / Tuition Description / Fee Description / Tuition Text | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.WRITE_REQ_ATTRIBUTE | write req attribute / Writing Requirement Attribute / Writing Code / Writing Requirement | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.WRITE_REQ_ATTRIBUTE_DESC | write req attribute desc / write req attribute description / Writing Requirement Description / Write Req Description / Writing Text / Writing Requirement Text | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.SUPERVISOR_ATTRIBUTE | supervisor attribute / Supervision Attribute / Supervisor Code / Supervision Flag | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.SUPERVISOR_ATTRIBUTE_DESC | supervisor attribute desc / supervisor attribute description / Supervision Description | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.PREREQUISITES | prerequisites | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.SUBJECT_DESCRIPTION | subject description | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.JOINT_SUBJECTS | joint subjects | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.SCHOOL_WIDE_ELECTIVES | school wide electives | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.MEETS_WITH_SUBJECTS | meets with subjects | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.EQUIVALENT_SUBJECTS | equivalent subjects | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.IS_OFFERED_THIS_YEAR | is offered this year | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.IS_OFFERED_FALL_TERM | is offered fall term | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.IS_OFFERED_IAP | is offered iap | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.IS_OFFERED_SPRING_TERM | is offered spring term | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.IS_OFFERED_SUMMER_TERM | is offered summer term | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.FALL_INSTRUCTORS | fall instructors | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.SPRING_INSTRUCTORS | spring instructors | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.STATUS_CHANGE | status change | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.LAST_ACTIVITY_DATE | last activity date | varchar(255) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE | warehouse load date | varchar(255) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.MASTER_SUBJECT_ID | master subject id / master subject identifier | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.HASS_ATTRIBUTE | hass attribute | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.HASS_ATTRIBUTE_DESC | hass attribute desc / hass attribute description | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.TERM_DURATION | term duration | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.GLOBAL_REGIONS | global regions | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.GLOBAL_COUNTRIES | global countries | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.ON_LINE_PAGE_NUMBER | on line page number | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.SO_SUBJECT_ID | so subject id / so subject identifier | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.SO_TERM_CODE | so term code | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.SO_TERM_DESCRIPTION | so term description | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.SO_CLUSTER_TYPE | so cluster type | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.SECTION_ID | section id / section identifier | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.IS_MASTER_SECTION | is master section | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.IS_LECTURE_SECTION | is lecture section | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.IS_LAB_SECTION | is lab section | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.IS_RECITATION_SECTION | is recitation section | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.IS_DESIGN_SECTION | is design section | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.RESPONSIBLE_FACULTY_NAME | responsible faculty name | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.RESPONSIBLE_FACULTY_MIT_ID | responsible faculty mit id / responsible faculty mit identifier | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.MEET_TIME | meet time | varchar(127) | schema / DRUPAL_COURSE_CATALOG |
| DRUPAL_COURSE_CATALOG.MEET_PLACE | meet place | varchar(127) | schema / DRUPAL_COURSE_CATALOG |

## DRUPAL_EMPLOYEE_DIRECTORY

Stores contact information, job titles, organizational affiliations, and employment classification for MIT employees and staff.

恢复表名: drupal employee directory / Employee Directory / Staff Directory / MIT Employee List / Personnel Directory / Workforce Roster / Employee Master
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| DRUPAL_EMPLOYEE_DIRECTORY.MIT_ID | mit id / mit identifier / Employee ID / Staff ID / Person ID / Unique Identifier / Employee Number | varchar(127) | schema / DRUPAL_EMPLOYEE_DIRECTORY |
| DRUPAL_EMPLOYEE_DIRECTORY.LAST_NAME | last name / Surname / Family Name / Employee Last Name / Staff Surname | varchar(127) | schema / DRUPAL_EMPLOYEE_DIRECTORY |
| DRUPAL_EMPLOYEE_DIRECTORY.FIRST_NAME | first name / Given Name / Employee First Name / Staff First Name / Christian Name | varchar(127) | schema / DRUPAL_EMPLOYEE_DIRECTORY |
| DRUPAL_EMPLOYEE_DIRECTORY.MIDDLE_NAME | middle name / Middle Initial / Employee Middle Name / Staff Middle Name / Second Name | varchar(127) | schema / DRUPAL_EMPLOYEE_DIRECTORY |
| DRUPAL_EMPLOYEE_DIRECTORY.FULL_NAME | full name / Employee Name / Staff Name / Display Name / Complete Name | varchar(127) | schema / DRUPAL_EMPLOYEE_DIRECTORY |
| DRUPAL_EMPLOYEE_DIRECTORY.EMPLOYEE_GROUP | employee group / Employment Group / Staff Group / Exempt Status / Pay Group | varchar(127) | schema / DRUPAL_EMPLOYEE_DIRECTORY |
| DRUPAL_EMPLOYEE_DIRECTORY.EMPLOYEE_TYPE | employee type / Job Category / Staff Type / Position Category / Role Type | varchar(127) | schema / DRUPAL_EMPLOYEE_DIRECTORY |
| DRUPAL_EMPLOYEE_DIRECTORY.HAS_ADDL_APPOINTMENT | has addl appointment / Has Additional Appointment / Additional Appointment Flag / Extra Appointment / Secondary Appointment | varchar(127) | schema / DRUPAL_EMPLOYEE_DIRECTORY |
| DRUPAL_EMPLOYEE_DIRECTORY.HAS_DUAL_APPOINTMENT | has dual appointment / Dual Appointment Flag / Split Appointment / Concurrent Appointment | varchar(127) | schema / DRUPAL_EMPLOYEE_DIRECTORY |
| DRUPAL_EMPLOYEE_DIRECTORY.OFFICE_LOCATION | office location / Office Number / Room Number / Work Location / Physical Office | varchar(127) | schema / DRUPAL_EMPLOYEE_DIRECTORY |
| DRUPAL_EMPLOYEE_DIRECTORY.OFFICE_PHONE | office phone / Work Phone / Phone Number / Contact Number / Direct Line | varchar(127) | schema / DRUPAL_EMPLOYEE_DIRECTORY |
| DRUPAL_EMPLOYEE_DIRECTORY.HR_ORG_UNIT_ID | hr org unit id / hr org unit identifier / Department ID / Organization ID / Unit ID / Department Code | varchar(127) | schema / DRUPAL_EMPLOYEE_DIRECTORY |
| DRUPAL_EMPLOYEE_DIRECTORY.HR_ORG_UNIT_TITLE | hr org unit title / Department Name / Organization Name / Unit Name / Department Title | varchar(127) | schema / DRUPAL_EMPLOYEE_DIRECTORY |
| DRUPAL_EMPLOYEE_DIRECTORY.DIRECTORY_TITLE | directory title / Public Title / Display Title / Job Title / Role Title | varchar(127) | schema / DRUPAL_EMPLOYEE_DIRECTORY |
| DRUPAL_EMPLOYEE_DIRECTORY.PRIMARY_TITLE | primary title / Main Job Title / Official Title / Primary Role / Main Position | varchar(127) | schema / DRUPAL_EMPLOYEE_DIRECTORY |
| DRUPAL_EMPLOYEE_DIRECTORY.EMAIL_ADDRESS | email address / Email / Work Email / Contact Email / Electronic Mail | varchar(127) | schema / DRUPAL_EMPLOYEE_DIRECTORY |
| DRUPAL_EMPLOYEE_DIRECTORY.PERSONAL_URL | personal url / Website / Personal Website / Profile URL / Online Profile | varchar(127) | schema / DRUPAL_EMPLOYEE_DIRECTORY |
| DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / ETL Date / Data Load Date / Refresh Date | varchar(255) | schema / DRUPAL_EMPLOYEE_DIRECTORY |

## EMPLOYEE_DIRECTORY

Stores contact information, names, office locations, and departmental affiliations for employees and faculty members, serving as the primary reference for individual identity and organizational placement.

恢复表名: employee directory / employee_directory / employee / faculty_directory / staff_directory / person_directory / employee_info / directory
SQL表别名: e, ed, ed2, t1

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| EMPLOYEE_DIRECTORY.MIT_ID | mit id / mit identifier / mit_id / employee_id / staff_id / person_id / faculty_id / unique_employee_identifier | varchar(127) | dw_1342, dw_1942, dw_5187, dw_1428, dw_2370, dw_2377, dw_2511, dw_636 |
| EMPLOYEE_DIRECTORY.LAST_NAME | last name / last_name / surname / family_name / employee_last_name / faculty_last_name | varchar(127) | dw_1942, dw_2370, dw_2377, dw_2511, dw_1270 |
| EMPLOYEE_DIRECTORY.FIRST_NAME | first name / first_name / given_name / employee_first_name / faculty_first_name | varchar(127) | schema / EMPLOYEE_DIRECTORY |
| EMPLOYEE_DIRECTORY.MIDDLE_NAME | middle name / middle_name / middle_initial / employee_middle_name / faculty_middle_name | varchar(127) | schema / EMPLOYEE_DIRECTORY |
| EMPLOYEE_DIRECTORY.FULL_NAME | full name / full_name / employee_name / faculty_name / person_name / display_name | varchar(127) | dw_1342, dw_2644, dw_1942, dw_1428, dw_2370, dw_2377, dw_2511, dw_636 |
| EMPLOYEE_DIRECTORY.DIRECTORY_FULL_NAME | directory full name / directory_full_name / directory_name / official_directory_name | varchar(127) | schema / EMPLOYEE_DIRECTORY |
| EMPLOYEE_DIRECTORY.OFFICE_LOCATION | office location / office_location / office_room / room_number / building_room / office_address / work_location | varchar(127) | dw_1342, dw_2644, dw_1428, dw_636, dw_3299, dw_3419 |
| EMPLOYEE_DIRECTORY.OFFICE_PHONE | office phone / office_phone / phone_number / work_phone / contact_number / telephone | varchar(127) | dw_1342, dw_1942, dw_1428, dw_2370, dw_2377, dw_2511, dw_636, dw_1270 |
| EMPLOYEE_DIRECTORY.DIRECTORY_TITLE | directory title / directory_title / job_title / position_title / role_title | varchar(127) | schema / EMPLOYEE_DIRECTORY |
| EMPLOYEE_DIRECTORY.PRIMARY_TITLE | primary title / primary_title / main_job_title / primary_position | varchar(127) | schema / EMPLOYEE_DIRECTORY |
| EMPLOYEE_DIRECTORY.DEPARTMENT_NUMBER | department number / department_number / dept_code / department_code / org_unit_code / course_number | varchar(127) | dw_2644, dw_3299, dw_3419 |
| EMPLOYEE_DIRECTORY.DEPARTMENT_NAME | department name / department_name / dept_name / department / org_unit_name / affiliation | varchar(127) | dw_2644, dw_5187, dw_3299, dw_3419 |
| EMPLOYEE_DIRECTORY.KRB_NAME | krb name / krb_name / kerberos_name / username / login_id / network_id / moira_list_member | varchar(127) | dw_5187 |
| EMPLOYEE_DIRECTORY.KRB_NAME_UPPERCASE | krb name uppercase / krb_name_uppercase / kerberos_name_upper / username_upper / login_id_upper | varchar(127) | schema / EMPLOYEE_DIRECTORY |
| EMPLOYEE_DIRECTORY.EMAIL_ADDRESS | email address / email_address / email / email_addr / contact_email / work_email | varchar(127) | dw_1342, dw_1942, dw_1428, dw_2370, dw_2377, dw_2511, dw_636 |
| EMPLOYEE_DIRECTORY.PERSONAL_URL | personal url / personal_url / website / personal_website / homepage / profile_url | varchar(127) | schema / EMPLOYEE_DIRECTORY |
| EMPLOYEE_DIRECTORY.NAME_KNOWN_BY | name known by / name_known_by / preferred_name / nickname / common_name | varchar(127) | schema / EMPLOYEE_DIRECTORY |
| EMPLOYEE_DIRECTORY.EMAIL_ADDRESS_UPPERCASE | email address uppercase / email_address_uppercase / email_upper / email_addr_upper | varchar(127) | schema / EMPLOYEE_DIRECTORY |
| EMPLOYEE_DIRECTORY.FULL_NAME_UPPERCASE | full name uppercase / full_name_uppercase / name_upper / employee_name_upper | varchar(127) | schema / EMPLOYEE_DIRECTORY |
| EMPLOYEE_DIRECTORY.PREFERRED_FIRST_NAME_UPPER | preferred first name upper / preferred_first_name_upper / first_name_upper / given_name_upper | varchar(127) | schema / EMPLOYEE_DIRECTORY |
| EMPLOYEE_DIRECTORY.PREFERRED_LAST_NAME_UPPER | preferred last name upper / preferred_last_name_upper / last_name_upper / surname_upper | varchar(127) | schema / EMPLOYEE_DIRECTORY |
| EMPLOYEE_DIRECTORY.PREFERRED_FIRST_NAME | preferred first name / preferred_first_name / first_name_pref / given_name_pref | varchar(127) | schema / EMPLOYEE_DIRECTORY |
| EMPLOYEE_DIRECTORY.PREFERRED_MIDDLE_NAME | preferred middle name / preferred_middle_name / middle_name_pref / middle_initial_pref | varchar(127) | schema / EMPLOYEE_DIRECTORY |
| EMPLOYEE_DIRECTORY.PREFERRED_LAST_NAME | preferred last name / preferred_last_name / last_name_pref / surname_pref | varchar(127) | schema / EMPLOYEE_DIRECTORY |

## ESTIMATED_SURCHARGES_ESTONLY

Stores estimated surcharge amounts, budgets, and commitments by cost collector, GL account, and time period for financial planning and analysis.

恢复表名: estimated surcharges estonly / estimated surcharges / surcharge estimates / est only surcharges / estimated surcharge budget / surcharge forecast
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ESTIMATED_SURCHARGES_ESTONLY.COST_COLLECTOR_KEY | cost collector key / cost collector id / cost center key / cost collector identifier | varchar(127) | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.COST_COLLECTOR_FP_KEY | cost collector fp key / cost collector functional period key / cost collector fp id / cost collector functional period identifier | varchar(127) | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.COST_COLLECTOR_FY_KEY | cost collector fy key / cost collector fiscal year key / cost collector fy id / cost collector fiscal year identifier | varchar(127) | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.GL_ACCOUNT_KEY | gl account key / general ledger account key / gl account id / account key / gl account identifier | varchar(127) | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.TIME_MONTH_KEY | time month key / month key / time period key / month identifier / calendar month key | varchar(127) | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.AMOUNT | amount / surcharge amount / estimated amount / value / total amount | int | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.CUMULATIVE_AMOUNT | cumulative amount / running total / cumulative surcharge / total to date / accumulated amount | int | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.FYTD_AMOUNT | fytd amount / fiscal year to date amount / ytd amount / year to date surcharge / fytd surcharge | int | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.INSTITUTE_BUDGET | institute budget / institutional budget / org budget / institute allocated budget / budget institute | int | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.TOTAL_INSTITUTE_BUDGET | total institute budget / total institutional budget / sum institute budget / aggregate institute budget / total org budget | int | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.FYTD_INSTITUTE_BUDGET | fytd institute budget / fiscal year to date institute budget / ytd institute budget / year to date institutional budget / fytd org budget | int | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.DEPARTMENT_BUDGET | department budget / dept budget / departmental budget / dept allocated budget / budget department | int | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.TOTAL_DEPARTMENT_BUDGET | total department budget / total dept budget / sum department budget / aggregate department budget / total deptal budget | int | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.FYTD_DEPARTMENT_BUDGET | fytd department budget / fiscal year to date department budget / ytd department budget / year to date dept budget / fytd deptal budget | int | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.ANNUAL_FORECAST_BUDGET | annual forecast budget / yearly forecast budget / annual projected budget / forecast annual budget / annual estimate budget | int | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.COMMITMENT_AMOUNT | commitment amount / committed amount / commitment value / total commitment / committed surcharge | int | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.NON_BL_ORDER_COMMITMENT_AMOUNT | non bl order commitment amount / non blank order commitment / non-bl order commitment / order commitment amount / non blank order committed amount | int | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.COMMITMENT_AMOUNT_FY | commitment amount fy / fiscal year commitment amount / fy commitment / yearly commitment amount / fy committed amount | int | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.NON_BL_ORDER_COMMIT_AMOUNT_FY | non bl order commit amount fy / non blank order commitment fy / fy non bl order commitment / yearly non blank order commitment / fy order commitment | int | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.RECORD_TYPE | record type / type / record category / data type / entry type | varchar(31) | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.RECORD_COUNTER | record counter / counter / record number / sequence number / row counter | int | schema / ESTIMATED_SURCHARGES_ESTONLY |
| ESTIMATED_SURCHARGES_ESTONLY.WAREHOUSE_LOAD_DATE | warehouse load date / load date / etl date / data load date / insert date / warehouse date | varchar(255) | schema / ESTIMATED_SURCHARGES_ESTONLY |

## FAC_BUILDING

Stores detailed metadata, physical characteristics, location, and ownership information for campus buildings and structures.

恢复表名: fac building / building / buildings / facility building / campus building / structure / physical structure
SQL表别名: b

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FAC_BUILDING.DATE_ACQUIRED | date acquired / acquisition date / purchase date / buy date | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.DATE_OCCUPIED | date occupied / occupancy date / move-in date / start of occupancy | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.WAREHOUSE_LOAD_DATE | warehouse load date / load date / data load date / warehouse date / etl date | varchar(255) | schema / FAC_BUILDING |
| FAC_BUILDING.NUM_OF_ROOMS | num of rooms / number of rooms / room count / rooms / room total | int | schema / FAC_BUILDING |
| FAC_BUILDING.FAC_BUILDING_KEY | fac building key / building key / facility building key / building id / unique building identifier | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.BUILDING_NUMBER | building number / building no / structure number / bldg num | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.PARENT_BUILDING_NUMBER | parent building number / parent building no / parent structure number / complex number / parent bldg id | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.PARENT_BUILDING_NAME | parent building name / complex name / parent structure name / group name | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.PARENT_BUILDING_NAME_LONG | parent building name long / parent building full name / complex full name / parent structure long name | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.BUILDING_NAME_LONG | building name long / building full name / long building name / formal building name / complete building name | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.EXT_GROSS_AREA | ext gross area / gross area / external gross area / total area / building size / square footage | float | schema / FAC_BUILDING |
| FAC_BUILDING.ASSIGNABLE_AREA | assignable area / usable area / net assignable area / rentable area | float | schema / FAC_BUILDING |
| FAC_BUILDING.NON_ASSIGNABLE_AREA | non assignable area / non-assignable area / unusable area / common area / non-rentable area | float | schema / FAC_BUILDING |
| FAC_BUILDING.SITE | site / site code / location code / campus site / institution site | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.CAMPUS_SECTOR | campus sector / sector / campus area / zone / campus region | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.ACCESS_LEVEL_CODE | access level code / access code / security level code / access level / entry level code | int | schema / FAC_BUILDING |
| FAC_BUILDING.ACCESS_LEVEL_NAME | access level name / access level / security level name / entry level / access description | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.BUILDING_TYPE | building type / type / building category / structure type / functional type | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.OWNERSHIP_TYPE | ownership type / ownership / property status / lease status / owned or leased | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.BUILDING_USE | building use / use code / building function code / purpose code / usage code | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.OCCUPANCY_CLASS | occupancy class / occupancy code / fire code class / occupancy type / safety class | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.BUILDING_HEIGHT | building height / height / structure height / vertical dimension | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.COST_CENTER_CODE | cost center code / cost center / cc code / budget code / financial center code | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.COST_COLLECTOR_KEY | cost collector key / cost collector / cc key / cost account key / financial collector id | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.LATITUDE_WGS | latitude wgs / latitude / lat / wgs latitude / geographic latitude | float | schema / FAC_BUILDING |
| FAC_BUILDING.LONGITUDE_WGS | longitude wgs / longitude / lon / wgs longitude / geographic longitude | float | schema / FAC_BUILDING |
| FAC_BUILDING.EASTING_X_SPCS | easting x spcs / easting / x coordinate / spcs easting / state plane x | float | schema / FAC_BUILDING |
| FAC_BUILDING.NORTHING_Y_SPCS | northing y spcs / northing / y coordinate / spcs northing / state plane y | float | schema / FAC_BUILDING |
| FAC_BUILDING.BUILDING_SORT | building sort / sort key / building sort order / display order / sequence number | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.BUILDING_NAMED_FOR | building named for / namesake / named after / honoree / dedication name | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.BUILDING_NAME | building name / name / short name / structure name | varchar(127) | schema / FAC_BUILDING |
| FAC_BUILDING.DATE_BUILT | date built / construction date / date constructed / built date / completion date | varchar(127) | schema / FAC_BUILDING |

## FAC_BUILDING_ADDRESS

Stores detailed street address information for facilities and buildings, including multiple address types such as street, mail, and emergency (E911) addresses.

恢复表名: fac building address / Building Address / Facility Address / Building Location / Address Details / Facility Location
SQL表别名: a

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / Warehouse Date / ETL Date / Last Updated | varchar(255) | schema / FAC_BUILDING_ADDRESS |
| FAC_BUILDING_ADDRESS.BUILDING_ADDRESS_KEY | building address key / Address Key / Building Address ID / Address Identifier / Unique Address ID / Address Code | varchar(127) | schema / FAC_BUILDING_ADDRESS |
| FAC_BUILDING_ADDRESS.BUILDING_KEY | building key / Building ID / Building Identifier / Facility ID / Building Code / Structure ID | varchar(127) | schema / FAC_BUILDING_ADDRESS |
| FAC_BUILDING_ADDRESS.ADDRESS_PURPOSE | address purpose / Address Type / Address Category / Purpose of Address / Address Kind / Address Classification | varchar(127) | schema / FAC_BUILDING_ADDRESS |
| FAC_BUILDING_ADDRESS.ADDRESS_CITY_ID | address city id / address city identifier / City ID / City Identifier / Municipality ID / City Code / Location ID | varchar(127) | schema / FAC_BUILDING_ADDRESS |
| FAC_BUILDING_ADDRESS.IS_E911_ADDRESS | is e911 address / E911 Flag / Emergency Address Indicator / Is Emergency Address / E911 Status / Emergency Address | varchar(127) | schema / FAC_BUILDING_ADDRESS |
| FAC_BUILDING_ADDRESS.STREET_NUMBER | street number / House Number / Building Number / Street No / Address Number / Property Number | varchar(127) | schema / FAC_BUILDING_ADDRESS |
| FAC_BUILDING_ADDRESS.STREET_NUMBER_SUFFIX | street number suffix / Number Suffix / Unit Suffix / Street Number Extension / Address Suffix / Unit Identifier | varchar(127) | schema / FAC_BUILDING_ADDRESS |
| FAC_BUILDING_ADDRESS.PRE_DIRECTIONAL | pre directional / Pre-Directional / Front Direction / North/South/East/West Prefix / Directional Prefix / Pre-Direction | varchar(127) | schema / FAC_BUILDING_ADDRESS |
| FAC_BUILDING_ADDRESS.STREET_NAME | street name / Street / Road Name / Avenue Name / Street Title / Road | varchar(127) | schema / FAC_BUILDING_ADDRESS |
| FAC_BUILDING_ADDRESS.STREET_SUFFIX | street suffix / Street Type / Road Suffix / Street Ending / Avenue Suffix / Street Abbreviation | varchar(127) | schema / FAC_BUILDING_ADDRESS |
| FAC_BUILDING_ADDRESS.POST_DIRECTIONAL | post directional / Post-Directional / Back Direction / Directional Suffix / Post-Direction / Directional Ending | varchar(127) | schema / FAC_BUILDING_ADDRESS |
| FAC_BUILDING_ADDRESS.CITY | city / City Name / Municipality / Town / Location City | varchar(127) | schema / FAC_BUILDING_ADDRESS |
| FAC_BUILDING_ADDRESS.STATE | state / State Code / Province / Region / State Abbreviation | varchar(127) | schema / FAC_BUILDING_ADDRESS |
| FAC_BUILDING_ADDRESS.POSTAL_CODE | postal code / Zip Code / ZIP / Postcode | varchar(127) | schema / FAC_BUILDING_ADDRESS |

## FAC_FLOOR

Stores detailed information about individual floors within buildings, including area measurements, identifiers, and access levels.

恢复表名: fac floor / Facility Floor / Building Floor / Floor Details / Floor Area / Floor Inventory
SQL表别名: f

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FAC_FLOOR.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date / Refresh Date | varchar(255) | schema / FAC_FLOOR |
| FAC_FLOOR.BUILDING_KEY | building key / Building ID / Building Code / Building Identifier / Structure Key / Building Ref | varchar(127) | schema / FAC_FLOOR |
| FAC_FLOOR.FLOOR | floor / Floor Number / Level Number / Floor Level / Storey / Floor ID | varchar(127) | schema / FAC_FLOOR |
| FAC_FLOOR.FLOOR_KEY | floor key / Floor Identifier / Unique Floor ID / Floor Code / Composite Floor Key / Floor Ref | varchar(127) | schema / FAC_FLOOR |
| FAC_FLOOR.EXT_GROSS_AREA | ext gross area / Gross Area / External Gross Area / Total Floor Area / Gross Square Feet / Total Area | float | schema / FAC_FLOOR |
| FAC_FLOOR.ASSIGNABLE_AREA | assignable area / Net Area / Usable Area / Assignable Square Feet / Leasable Area / Net Square Feet | float | schema / FAC_FLOOR |
| FAC_FLOOR.NON_ASSIGNABLE_AREA | non assignable area / Common Area / Non-Usable Area / Overhead Area / Shared Area / Non-Assignable Space | float | schema / FAC_FLOOR |
| FAC_FLOOR.FLOOR_SORT_SEQUENCE | floor sort sequence / Sort Order / Display Sequence / Floor Order / Sorting Key / Sequence Number | varchar(127) | schema / FAC_FLOOR |
| FAC_FLOOR.LEVEL_ID | level id / level identifier / Floor Level ID / Level Code / Storey ID / Level Number | varchar(127) | schema / FAC_FLOOR |
| FAC_FLOOR.BUILDING_WINGS_ID | building wings id / building wings identifier / Wing ID / Building Wing Identifier / Wing Code / Section ID / Wing Ref | varchar(127) | schema / FAC_FLOOR |
| FAC_FLOOR.ACCESS_LEVEL | access level / Security Level / Access Restriction / Clearance Level / Access Code / Security Clearance | varchar(127) | schema / FAC_FLOOR |

## FAC_MAJOR_USE

Reference table defining major facility usage categories, their codes, descriptions, and assignability status for building spaces.

恢复表名: fac major use / Facility Major Use / Major Use Codes / Building Use Types / Space Usage Categories / Facility Usage Reference
SQL表别名: m

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FAC_MAJOR_USE.MAJOR_USE_KEY | major use key / Use Code / Usage ID / Major Use ID / Facility Use Code | varchar(127) | schema / FAC_MAJOR_USE |
| FAC_MAJOR_USE.MAJOR_USE | major use / Use Type / Usage Category / Short Use Name / Facility Use | varchar(127) | schema / FAC_MAJOR_USE |
| FAC_MAJOR_USE.DESCRIPTION | description / Use Description / Full Use Name / Usage Description / Facility Use Description | varchar(127) | schema / FAC_MAJOR_USE |
| FAC_MAJOR_USE.ASSIGNABLE | assignable / Is Assignable / Assignment Flag / Can Assign / Assignable Status | varchar(127) | schema / FAC_MAJOR_USE |
| FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / ETL Date / Data Load Date / Last Updated | varchar(255) | schema / FAC_MAJOR_USE |

## FAC_ORGANIZATION

Master table containing the hierarchy, codes, and descriptive attributes for MIT faculty organizations, departments, and administrative units.

恢复表名: fac organization / Organization / Department / Faculty Organization / Org / Department Master / Organizational Unit
SQL表别名: o

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FAC_ORGANIZATION.ORGANIZATION_KEY | organization key / Org Key / Internal Organization ID / Organization Identifier | varchar(127) | schema / FAC_ORGANIZATION |
| FAC_ORGANIZATION.ORGANIZATION_ID | organization id / organization identifier / Org ID / Organization Number / Department ID | varchar(127) | schema / FAC_ORGANIZATION |
| FAC_ORGANIZATION.ORGANIZATION | organization / Organization Code / Org Code / Short Organization Name / Department Code | varchar(127) | schema / FAC_ORGANIZATION |
| FAC_ORGANIZATION.ORGANIZATION_NAME | organization name / Org Name / Department Name / Full Organization Name | varchar(127) | schema / FAC_ORGANIZATION |
| FAC_ORGANIZATION.ORG_PARENT_KEY | org parent key / Parent Organization Key / Parent Org Key / Superior Org Key / Reporting Org Key | varchar(127) | schema / FAC_ORGANIZATION |
| FAC_ORGANIZATION.ORG_PARENT | org parent / Parent Organization Code / Parent Org Code / Superior Org Code / Reporting Org Code | varchar(127) | schema / FAC_ORGANIZATION |
| FAC_ORGANIZATION.MAJOR_ORG_KEY | major org key / Major Organization Key / Top Level Org Key / Executive Org Key | varchar(127) | schema / FAC_ORGANIZATION |
| FAC_ORGANIZATION.MAJOR_ORG | major org / Major Organization Code / Major Org Code / Top Level Org Code / Executive Org Code | varchar(127) | schema / FAC_ORGANIZATION |
| FAC_ORGANIZATION.ORGANIZATION_LEVEL | organization level / Org Level / Hierarchy Level / Depth Level | varchar(127) | schema / FAC_ORGANIZATION |
| FAC_ORGANIZATION.ORGANIZATION_NUMBER | organization number / Org Number / Department Number / HR Department Code | varchar(127) | schema / FAC_ORGANIZATION |
| FAC_ORGANIZATION.ORGANIZATION_SORT | organization sort / Organization Sort Code / Org Sort / Sort Order / Display Order | varchar(127) | schema / FAC_ORGANIZATION |
| FAC_ORGANIZATION.ASSIGNABLE | assignable / Assignable Flag / Is Assignable / Can Assign / Assignment Allowed | varchar(127) | schema / FAC_ORGANIZATION |
| FAC_ORGANIZATION.COURSE | course / Course Number / Course Code / Department Course Prefix / Academic Course | varchar(127) | schema / FAC_ORGANIZATION |
| FAC_ORGANIZATION.DESCRIPTION | description / Organization Description / Long Description / Detailed Name | varchar(127) | schema / FAC_ORGANIZATION |
| FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / ETL Date / Data Load Date | varchar(255) | schema / FAC_ORGANIZATION |
| FAC_ORGANIZATION.D_CODE | d code / Department Code / HR D Code / Legacy Department Code | varchar(127) | schema / FAC_ORGANIZATION |
| FAC_ORGANIZATION.HR_DEPARTMENT_CODE_OLD | hr department code old / Old HR Department Code / Legacy HR Dept Code / Previous Department Code / Historical HR Code | varchar(127) | schema / FAC_ORGANIZATION |
| FAC_ORGANIZATION.HR_ORG_UNIT_ID | hr org unit id / hr org unit identifier / HR Organization Unit ID / HR Unit Identifier / PeopleSoft Org ID | varchar(127) | schema / FAC_ORGANIZATION |
| FAC_ORGANIZATION.HR_DEPARTMENT_NAME | hr department name / HR Dept Name / Official Department Name / HR Org Name | varchar(127) | schema / FAC_ORGANIZATION |

## FAC_ROOMS

Stores detailed information about individual rooms and spaces within facility buildings, including location, usage, organization, and physical dimensions.

恢复表名: fac rooms / Facility Rooms / Building Rooms / Room Inventory / Space Details / Facility Space / Room Master
SQL表别名: r

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FAC_ROOMS.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date / Warehouse Date / Last Updated / Refresh Date | varchar(255) | schema / FAC_ROOMS |
| FAC_ROOMS.FAC_ROOM_KEY | fac room key / Room Key / Facility Room ID / Room Identifier / Unique Room Code / Room Surrogate Key | varchar(127) | schema / FAC_ROOMS |
| FAC_ROOMS.BUILDING_KEY | building key / Building ID / Building Identifier / Structure Key / Building Code / Building Surrogate Key / Bldg Key | varchar(127) | schema / FAC_ROOMS |
| FAC_ROOMS.FLOOR | floor / Floor Number / Level / Storey / Floor Level / Building Floor / Floor Num | varchar(127) | schema / FAC_ROOMS |
| FAC_ROOMS.FLOOR_KEY | floor key / Floor ID / Floor Identifier / Level Key / Floor Surrogate Key / Floor Code / Bldg Floor Key | varchar(127) | schema / FAC_ROOMS |
| FAC_ROOMS.ROOM | room / Room Number / Room ID / Room Code / Room Label / Space Number / Room Num | varchar(127) | schema / FAC_ROOMS |
| FAC_ROOMS.SPACE_ID | space id / space identifier / Unique Space ID / Room Space Key / Global Room ID / Space Code / Full Room ID | varchar(127) | schema / FAC_ROOMS |
| FAC_ROOMS.MAJOR_USE_KEY | major use key / Major Use ID / Primary Use Code / Main Usage Key / Major Function ID / Use Category Key / Primary Use Key | varchar(127) | schema / FAC_ROOMS |
| FAC_ROOMS.MAJOR_USE_DESC | major use desc / major use description / Primary Use / Main Usage / Room Function / Use Category / Primary Function | varchar(127) | schema / FAC_ROOMS |
| FAC_ROOMS.USE_KEY | use key / Use ID / Usage Code / Function Key / Room Use Identifier / Specific Use Key / Use Surrogate Key | varchar(127) | schema / FAC_ROOMS |
| FAC_ROOMS.USE_DESC | use desc / use description / Usage Detail / Function Description / Specific Use / Room Function Detail / Use Text | varchar(127) | schema / FAC_ROOMS |
| FAC_ROOMS.MINOR_USE_KEY | minor use key / Minor Use ID / Secondary Use Code / Sub Use Key / Minor Function ID / Secondary Usage Key / Sub Use Identifier | varchar(127) | schema / FAC_ROOMS |
| FAC_ROOMS.MINOR_USE_DESC | minor use desc / minor use description / Secondary Use / Sub Usage / Minor Function / Secondary Function / Sub Use Text | varchar(127) | schema / FAC_ROOMS |
| FAC_ROOMS.ORGANIZATION_KEY | organization key / Organization ID / Org Key / Department Key / Owner Organization ID / Primary Org Identifier / Org Surrogate Key | varchar(127) | schema / FAC_ROOMS |
| FAC_ROOMS.ORGANIZATION_NAME | organization name / Department Name / Owner Name / Org Name / Primary Organization / Dept Name | varchar(127) | schema / FAC_ROOMS |
| FAC_ROOMS.MINOR_ORGANIZATION_KEY | minor organization key / Minor Org ID / Secondary Organization Key / Sub Org Identifier / Secondary Dept Key / Minor Department ID / Sub Org Key | varchar(127) | schema / FAC_ROOMS |
| FAC_ROOMS.MINOR_ORGANIZATION | minor organization / Minor Organization Name / Secondary Department / Sub Org Name / Secondary Org / Minor Dept Name / Sub Department | varchar(127) | schema / FAC_ROOMS |
| FAC_ROOMS.AREA | area / Square Footage / Room Size / Space Area / Area in Sq Ft / Room Dimensions / Size | float | schema / FAC_ROOMS |
| FAC_ROOMS.ROOM_FULL_NAME | room full name / Full Room Name / Room Title / Complete Room Identifier / Room Label Full / Descriptive Room Name / Room Full ID | varchar(127) | schema / FAC_ROOMS |
| FAC_ROOMS.DEPT_CODE | dept code / department code / Dept ID / Org Code / Department Identifier / Dept Number | varchar(127) | schema / FAC_ROOMS |
| FAC_ROOMS.ACCESS_LEVEL | access level / Security Level / Access Restriction / Clearance Level / Access Type / Security Clearance / Access Control | varchar(127) | schema / FAC_ROOMS |
| FAC_ROOMS.LATITUDE_WGS | latitude wgs / Latitude / Lat / WGS Latitude / Geographic Latitude / Lat WGS84 / Latitude Coordinate | float | schema / FAC_ROOMS |
| FAC_ROOMS.LONGITUDE_WGS | longitude wgs / Longitude / Lon / WGS Longitude / Geographic Longitude / Lon WGS84 / Longitude Coordinate | float | schema / FAC_ROOMS |
| FAC_ROOMS.NORTHING_SPCS | northing spcs / Northing / Y Coordinate / SPCS Northing / State Plane Northing / North Coordinate / Y SPCS | float | schema / FAC_ROOMS |
| FAC_ROOMS.EASTING_SPCS | easting spcs / Easting / X Coordinate / SPCS Easting / State Plane Easting / East Coordinate / X SPCS | float | schema / FAC_ROOMS |

## FCLT_BUILDING

Stores current-state attributes for physical buildings on campus, including identifiers, names, locations, areas, types, and ownership details.

恢复表名: fclt building / building / buildings / facility building / campus building / building fact / building dimension
SQL表别名: b, f, fb, t0, t1, t2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FCLT_BUILDING.FCLT_BUILDING_KEY | fclt building key / building key / building id / building identifier / facility key / building primary key | varchar(127) | dw_1566, dw_144, dw_1458, dw_2659, dw_1357, dw_4693, dw_1848, dw_17 |
| FCLT_BUILDING.BUILDING_NUMBER | building number / building id number / facility number / building code / building label | varchar(127) | dw_2659 |
| FCLT_BUILDING.PARENT_BUILDING_NUMBER | parent building number / parent facility number / complex number / parent building id | varchar(127) | schema / FCLT_BUILDING |
| FCLT_BUILDING.PARENT_BUILDING_NAME | parent building name / parent facility name / complex name / parent building label | varchar(127) | schema / FCLT_BUILDING |
| FCLT_BUILDING.PARENT_BUILDING_NAME_LONG | parent building name long / parent building long name / parent facility full name / complex full name | varchar(127) | schema / FCLT_BUILDING |
| FCLT_BUILDING.BUILDING_NAME_LONG | building name long / building long name / full building name / building full name | varchar(127) | dw_144, dw_1357, dw_4693 |
| FCLT_BUILDING.EXT_GROSS_AREA | ext gross area / external gross area / gross area / total building area / building size | float | dw_1566, dw_1848 |
| FCLT_BUILDING.ASSIGNABLE_AREA | assignable area / usable area / net assignable area / assignable square footage | float | dw_1458, dw_1791, dw_1888 |
| FCLT_BUILDING.NON_ASSIGNABLE_AREA | non assignable area / non-assignable area / unassignable area / common area / non-assignable square footage | float | schema / FCLT_BUILDING |
| FCLT_BUILDING.SITE | site / campus site / location site / institution site | varchar(127) | dw_1566, dw_1458, dw_2935, dw_1848, dw_17, dw_1791, dw_1888 |
| FCLT_BUILDING.CAMPUS_SECTOR | campus sector / sector / campus area / building sector / campus zone | varchar(127) | dw_1566, dw_144, dw_1848 |
| FCLT_BUILDING.ACCESS_LEVEL_CODE | access level code / security level code / access code / building access level | int | dw_144, dw_1357, dw_17 |
| FCLT_BUILDING.ACCESS_LEVEL_NAME | access level name / security level name / access description | varchar(127) | dw_1357 |
| FCLT_BUILDING.BUILDING_TYPE | building type / facility type / building category / type of building | varchar(127) | dw_1566, dw_144, dw_1458, dw_2698, dw_1357, dw_2935, dw_1848, dw_17 |
| FCLT_BUILDING.OWNERSHIP_TYPE | ownership type / owned or leased / property status / building ownership | varchar(127) | dw_1566, dw_1848 |
| FCLT_BUILDING.BUILDING_USE | building use / primary use / use code / building function | varchar(127) | dw_2659 |
| FCLT_BUILDING.OCCUPANCY_CLASS | occupancy class / fire occupancy class / occupancy code / safety class | varchar(127) | schema / FCLT_BUILDING |
| FCLT_BUILDING.BUILDING_HEIGHT | building height / height / structure height / building elevation | varchar(127) | dw_2698 |
| FCLT_BUILDING.COST_CENTER_CODE | cost center code / cost center / financial cost center / cc code | varchar(127) | dw_2698 |
| FCLT_BUILDING.COST_COLLECTOR_KEY | cost collector key / cost collector / financial collector key / cc key | varchar(127) | dw_2935 |
| FCLT_BUILDING.LATITUDE_WGS | latitude wgs / latitude / wgs latitude / lat / geographic latitude | float | schema / FCLT_BUILDING |
| FCLT_BUILDING.LONGITUDE_WGS | longitude wgs / longitude / wgs longitude / lon / geographic longitude | float | schema / FCLT_BUILDING |
| FCLT_BUILDING.EASTING_X_SPCS | easting x spcs / easting / x coordinate / spcs easting / state plane easting | float | schema / FCLT_BUILDING |
| FCLT_BUILDING.NORTHING_Y_SPCS | northing y spcs / northing / y coordinate / spcs northing / state plane northing | float | schema / FCLT_BUILDING |
| FCLT_BUILDING.BUILDING_SORT | building sort / sort key / building order / display sort | varchar(127) | dw_4693 |
| FCLT_BUILDING.BUILDING_NAMED_FOR | building named for / named for / namesake / building namesake / honoree | varchar(127) | schema / FCLT_BUILDING |
| FCLT_BUILDING.BUILDING_NAME | building name / short building name / facility name / building label | varchar(127) | dw_1566, dw_1458, dw_2659, dw_2698, dw_2935, dw_1848, dw_17, dw_1791 |
| FCLT_BUILDING.DATE_BUILT | date built / construction date / year built / built date | varchar(127) | dw_1458, dw_1791 |
| FCLT_BUILDING.DATE_ACQUIRED | date acquired / acquisition date / purchase date / acquired date | varchar(127) | schema / FCLT_BUILDING |
| FCLT_BUILDING.DATE_OCCUPIED | date occupied / occupancy date / move-in date / first occupied date | varchar(127) | schema / FCLT_BUILDING |
| FCLT_BUILDING.WAREHOUSE_LOAD_DATE | warehouse load date / load date / etl date / data load date | varchar(255) | schema / FCLT_BUILDING |
| FCLT_BUILDING.NUM_OF_ROOMS | num of rooms / number of rooms / room count / total rooms / rooms in building | int | dw_144, dw_2659, dw_2698, dw_2935, dw_4693, dw_17, dw_1888 |

## FCLT_BUILDING_ADDRESS

Stores detailed street address components and location identifiers for campus buildings, supporting joins to building, room, and floor facts for geographic and administrative reporting.

恢复表名: fclt building address / Building Address / Building Address Fact / Address Fact / Building Location / Campus Address
SQL表别名: a, ba, fba, t0

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FCLT_BUILDING_ADDRESS.POSTAL_CODE | postal code / Zip Code / Zip / Post Code | varchar(127) | dw_295, dw_516, dw_5315, dw_5561, dw_126, dw_374, dw_5369, dw_1451 |
| FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / ETL Date / Data Load Date | varchar(255) | schema / FCLT_BUILDING_ADDRESS |
| FCLT_BUILDING_ADDRESS.FCLT_BUILDING_ADDRESS_KEY | fclt building address key / Address Key / Building Address Key / Address ID / Address Identifier | varchar(127) | schema / FCLT_BUILDING_ADDRESS |
| FCLT_BUILDING_ADDRESS.FCLT_BUILDING_KEY | fclt building key / Building Key / Building ID / Building Identifier / Building Number Key | varchar(127) | dw_295, dw_5455, dw_516, dw_5315, dw_5561, dw_126, dw_374, dw_5369 |
| FCLT_BUILDING_ADDRESS.BUILDING_NUMBER | building number / Building ID / Building Code / Building Designation | varchar(127) | dw_295, dw_565, dw_516, dw_5315, dw_5561, dw_126, dw_374, dw_5369 |
| FCLT_BUILDING_ADDRESS.ADDRESS_PURPOSE | address purpose / Address Type / Address Category / Address Usage | varchar(127) | dw_295, dw_516, dw_5315, dw_5561, dw_126, dw_374, dw_5369 |
| FCLT_BUILDING_ADDRESS.ADDRESS_CITY_ID | address city id / address city identifier / City ID / City Identifier / City Code | varchar(127) | schema / FCLT_BUILDING_ADDRESS |
| FCLT_BUILDING_ADDRESS.IS_E911_ADDRESS | is e911 address / Is E911 / E911 Flag / Emergency Address Flag / Is Emergency Address | varchar(127) | schema / FCLT_BUILDING_ADDRESS |
| FCLT_BUILDING_ADDRESS.STREET_NUMBER | street number / House Number / Building Street Number / Address Number | varchar(127) | dw_5455 |
| FCLT_BUILDING_ADDRESS.STREET_NUMBER_SUFFIX | street number suffix / Number Suffix / Address Number Suffix / Unit Suffix | varchar(127) | schema / FCLT_BUILDING_ADDRESS |
| FCLT_BUILDING_ADDRESS.PRE_DIRECTIONAL | pre directional / Pre-Directional / Prefix Direction / Street Prefix Direction | varchar(127) | schema / FCLT_BUILDING_ADDRESS |
| FCLT_BUILDING_ADDRESS.STREET_NAME | street name / Road Name / Avenue Name / Street | varchar(127) | dw_565 |
| FCLT_BUILDING_ADDRESS.STREET_SUFFIX | street suffix / Road Suffix / Street Type / Avenue Type | varchar(127) | schema / FCLT_BUILDING_ADDRESS |
| FCLT_BUILDING_ADDRESS.POST_DIRECTIONAL | post directional / Post-Directional / Suffix Direction / Street Suffix Direction | varchar(127) | schema / FCLT_BUILDING_ADDRESS |
| FCLT_BUILDING_ADDRESS.CITY | city / Town / Municipality / City Name | varchar(127) | dw_295, dw_565, dw_516, dw_5315, dw_5561, dw_126, dw_374, dw_5369 |
| FCLT_BUILDING_ADDRESS.STATE | state / Province / Region / State Code | varchar(127) | dw_295, dw_516, dw_5315, dw_5561, dw_1888, dw_203 |

## FCLT_BUILDING_ADDRESS_HIST

Stores historical records of building addresses, including street, mail, and E911 address details, linked to specific buildings and fiscal periods.

恢复表名: fclt building address hist / Building Address History / Historical Building Addresses / Building Address Fact / Address History / Building Location History
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FCLT_BUILDING_ADDRESS_HIST.FCLT_BUILDING_ADDRESS_KEY | fclt building address key / Building Address Key / Address Key / Building Address ID / Address Identifier | varchar(127) | schema / FCLT_BUILDING_ADDRESS_HIST |
| FCLT_BUILDING_ADDRESS_HIST.FCLT_BUILDING_KEY | fclt building key / Building Key / Building ID / Building Number / Building Identifier | varchar(127) | schema / FCLT_BUILDING_ADDRESS_HIST |
| FCLT_BUILDING_ADDRESS_HIST.FISCAL_PERIOD | fiscal period / Period / Fiscal Month / Reporting Period | varchar(127) | schema / FCLT_BUILDING_ADDRESS_HIST |
| FCLT_BUILDING_ADDRESS_HIST.FCLT_BUILDING_ADDRESS_HIST_KEY | fclt building address hist key / Building Address History Key / History Key / Record Key / Unique History ID | varchar(127) | schema / FCLT_BUILDING_ADDRESS_HIST |
| FCLT_BUILDING_ADDRESS_HIST.BUILDING_NUMBER | building number / Building ID / Building Code / Structure Number | varchar(127) | schema / FCLT_BUILDING_ADDRESS_HIST |
| FCLT_BUILDING_ADDRESS_HIST.ADDRESS_PURPOSE | address purpose / Address Type / Address Category / Purpose of Address | varchar(127) | schema / FCLT_BUILDING_ADDRESS_HIST |
| FCLT_BUILDING_ADDRESS_HIST.ADDRESS_CITY_ID | address city id / address city identifier / City ID / City Code / Municipality ID | varchar(127) | schema / FCLT_BUILDING_ADDRESS_HIST |
| FCLT_BUILDING_ADDRESS_HIST.IS_E911_ADDRESS | is e911 address / Is E911 / E911 Flag / Emergency Address Indicator / E911 Status | varchar(127) | schema / FCLT_BUILDING_ADDRESS_HIST |
| FCLT_BUILDING_ADDRESS_HIST.STREET_NUMBER | street number / House Number / Building Street Number / Address Number | varchar(127) | schema / FCLT_BUILDING_ADDRESS_HIST |
| FCLT_BUILDING_ADDRESS_HIST.STREET_NUMBER_SUFFIX | street number suffix / Number Suffix / Unit Suffix / Address Suffix | varchar(127) | schema / FCLT_BUILDING_ADDRESS_HIST |
| FCLT_BUILDING_ADDRESS_HIST.PRE_DIRECTIONAL | pre directional / Pre-Directional / Prefix Direction / Street Prefix / Directional Prefix | varchar(127) | schema / FCLT_BUILDING_ADDRESS_HIST |
| FCLT_BUILDING_ADDRESS_HIST.STREET_NAME | street name / Road Name / Avenue Name / Street | varchar(127) | schema / FCLT_BUILDING_ADDRESS_HIST |
| FCLT_BUILDING_ADDRESS_HIST.STREET_SUFFIX | street suffix / Road Suffix / Street Type / Avenue Suffix | varchar(127) | schema / FCLT_BUILDING_ADDRESS_HIST |
| FCLT_BUILDING_ADDRESS_HIST.POST_DIRECTIONAL | post directional / Post-Directional / Suffix Direction / Directional Suffix / Rear Indicator | varchar(127) | schema / FCLT_BUILDING_ADDRESS_HIST |
| FCLT_BUILDING_ADDRESS_HIST.CITY | city / Municipality / Town / City Name | varchar(127) | schema / FCLT_BUILDING_ADDRESS_HIST |
| FCLT_BUILDING_ADDRESS_HIST.STATE | state / State Code / Province / Region | varchar(127) | schema / FCLT_BUILDING_ADDRESS_HIST |
| FCLT_BUILDING_ADDRESS_HIST.POSTAL_CODE | postal code / Zip Code / Postcode / ZIP | varchar(127) | schema / FCLT_BUILDING_ADDRESS_HIST |
| FCLT_BUILDING_ADDRESS_HIST.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / ETL Date / Data Load Date | varchar(255) | schema / FCLT_BUILDING_ADDRESS_HIST |

## FCLT_BUILDING_HIST

Stores historical snapshots of building attributes, including area metrics, access levels, and location data, keyed by building and fiscal period.

恢复表名: fclt building hist / Building History / Historical Building Facts / Building Historical Records / FCLT Building History / Building Area History / Historical Building Data
SQL表别名: b, fbh, fbh1, fbh2, h, t1

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FCLT_BUILDING_HIST.FCLT_BUILDING_HIST_KEY | fclt building hist key / Building History Key / History ID / Record ID / Historical Record Key | varchar(127) | dw_330 |
| FCLT_BUILDING_HIST.FISCAL_PERIOD | fiscal period / Period / Fiscal Year Month / Reporting Period / Time Period | varchar(127) | dw_330, dw_3075, dw_126 |
| FCLT_BUILDING_HIST.FCLT_BUILDING_KEY | fclt building key / Building Key / Building ID / Building Identifier / Fact Building Key | varchar(127) | dw_1190, dw_330, dw_488, dw_505, dw_2005, dw_780, dw_126, dw_1488 |
| FCLT_BUILDING_HIST.BUILDING_NUMBER | building number / Building Code / Building ID / Building Designation | varchar(127) | dw_1190, dw_2005, dw_780 |
| FCLT_BUILDING_HIST.PARENT_BUILDING_NUMBER | parent building number / Parent Building Code / Main Building Number | varchar(127) | schema / FCLT_BUILDING_HIST |
| FCLT_BUILDING_HIST.PARENT_BUILDING_NAME | parent building name / Main Building Name / Parent Structure Name | varchar(127) | schema / FCLT_BUILDING_HIST |
| FCLT_BUILDING_HIST.PARENT_BUILDING_NAME_LONG | parent building name long / Parent Building Long Name / Full Parent Building Name / Parent Building Official Name | varchar(127) | schema / FCLT_BUILDING_HIST |
| FCLT_BUILDING_HIST.BUILDING_NAME_LONG | building name long / Building Long Name / Full Building Name / Building Official Name / Complete Building Name | varchar(127) | dw_488, dw_1488 |
| FCLT_BUILDING_HIST.EXT_GROSS_AREA | ext gross area / External Gross Area / Gross Area / Total Building Area / External Area | float | schema / FCLT_BUILDING_HIST |
| FCLT_BUILDING_HIST.ASSIGNABLE_AREA | assignable area / Usable Area / Net Area / Leasable Area | float | dw_1190, dw_1357, dw_330, dw_3075, dw_505, dw_2005, dw_780, dw_5283 |
| FCLT_BUILDING_HIST.NON_ASSIGNABLE_AREA | non assignable area / Non-Assignable Area / Common Area / Unusable Area / Circulation Area | float | dw_505 |
| FCLT_BUILDING_HIST.SITE | site / Campus / Location / Site Code | varchar(127) | dw_1357, dw_488, dw_5283, dw_1488 |
| FCLT_BUILDING_HIST.CAMPUS_SECTOR | campus sector / Sector / Campus Region / Building Sector | varchar(127) | dw_1357, dw_160 |
| FCLT_BUILDING_HIST.ACCESS_LEVEL_CODE | access level code / Security Level Code / Access Code | int | dw_1357, dw_330, dw_5283, dw_160 |
| FCLT_BUILDING_HIST.ACCESS_LEVEL_NAME | access level name / Security Level Name / Access Description | varchar(127) | schema / FCLT_BUILDING_HIST |
| FCLT_BUILDING_HIST.BUILDING_TYPE | building type / Type / Building Category / Structure Type | varchar(127) | dw_1190, dw_1357, dw_488, dw_2005, dw_780, dw_5283, dw_1488, dw_160 |
| FCLT_BUILDING_HIST.OWNERSHIP_TYPE | ownership type / Ownership / Property Status / Lease Status | varchar(127) | schema / FCLT_BUILDING_HIST |
| FCLT_BUILDING_HIST.BUILDING_USE | building use / Use Code / Function Code / Building Function | varchar(127) | dw_488 |
| FCLT_BUILDING_HIST.OCCUPANCY_CLASS | occupancy class / Fire Code Class / Occupancy Type / Safety Class | varchar(127) | schema / FCLT_BUILDING_HIST |
| FCLT_BUILDING_HIST.BUILDING_HEIGHT | building height / Height / Structure Height | varchar(127) | schema / FCLT_BUILDING_HIST |
| FCLT_BUILDING_HIST.COST_CENTER_CODE | cost center code / Cost Center / Accounting Code / Financial Code | varchar(127) | dw_1190, dw_2005, dw_780 |
| FCLT_BUILDING_HIST.COST_COLLECTOR_KEY | cost collector key / Cost Collector / Financial Collector Key | varchar(127) | dw_3075 |
| FCLT_BUILDING_HIST.LATITUDE_WGS | latitude wgs / Latitude / WGS Latitude / Geo Latitude / Lat | float | schema / FCLT_BUILDING_HIST |
| FCLT_BUILDING_HIST.LONGITUDE_WGS | longitude wgs / Longitude / WGS Longitude / Geo Longitude / Lon | float | schema / FCLT_BUILDING_HIST |
| FCLT_BUILDING_HIST.EASTING_X_SPCS | easting x spcs / Easting / X Coordinate / SPCS Easting / State Plane Easting | float | schema / FCLT_BUILDING_HIST |
| FCLT_BUILDING_HIST.NORTHING_Y_SPCS | northing y spcs / Northing / Y Coordinate / SPCS Northing / State Plane Northing | float | schema / FCLT_BUILDING_HIST |
| FCLT_BUILDING_HIST.BUILDING_SORT | building sort / Sort Key / Building Order / Display Order | varchar(127) | schema / FCLT_BUILDING_HIST |
| FCLT_BUILDING_HIST.BUILDING_NAMED_FOR | building named for / Named For / Dedicated To / Honoree / Building Namesake | varchar(127) | schema / FCLT_BUILDING_HIST |
| FCLT_BUILDING_HIST.BUILDING_NAME | building name / Name / Short Name / Building Title | varchar(127) | dw_1190, dw_2005, dw_780 |
| FCLT_BUILDING_HIST.DATE_BUILT | date built / Construction Date / Built Date / Completion Date | varchar(127) | schema / FCLT_BUILDING_HIST |
| FCLT_BUILDING_HIST.DATE_ACQUIRED | date acquired / Acquisition Date / Purchase Date / Ownership Start Date | varchar(127) | schema / FCLT_BUILDING_HIST |
| FCLT_BUILDING_HIST.DATE_OCCUPIED | date occupied / Occupancy Start Date / Move-in Date / First Occupied Date | varchar(127) | schema / FCLT_BUILDING_HIST |
| FCLT_BUILDING_HIST.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / ETL Date / Data Load Date | varchar(255) | schema / FCLT_BUILDING_HIST |
| FCLT_BUILDING_HIST.NUM_OF_ROOMS | num of rooms / number of rooms / Room Count / Total Rooms / Rooms | int | dw_1357, dw_5283, dw_126, dw_160 |

## FCLT_BUILDING_HIST_1

Historical snapshot of campus building attributes, including physical dimensions, location, ownership, usage, and financial cost centers for specific fiscal periods.

恢复表名: fclt building hist 1 / Building History Fact / Building Historical Data / Campus Building Inventory / Facility History / Building Snapshot / Real Estate History
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FCLT_BUILDING_HIST_1.FCLT_BUILDING_HIST_KEY | fclt building hist key / Building History Key / Fact Building History ID / Record ID / Unique Building Period ID | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.FISCAL_PERIOD | fiscal period / Reporting Period / Fiscal Month / Period Code / Accounting Period | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.FCLT_BUILDING_KEY | fclt building key / Building Key / Building ID / Facility Key / Building Identifier | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.BUILDING_NUMBER | building number / Building Code / Building ID / Facility Number / Building Designation | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.PARENT_BUILDING_NUMBER | parent building number / Main Building Number / Complex Building Number / Parent Facility Code | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.PARENT_BUILDING_NAME | parent building name / Main Building Name / Complex Name / Parent Facility Name | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.PARENT_BUILDING_NAME_LONG | parent building name long / Parent Building Full Name / Main Building Long Name / Complex Full Name / Parent Facility Full Name | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.BUILDING_NAME_LONG | building name long / Building Full Name / Building Long Name / Facility Full Name / Building Description | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.EXT_GROSS_AREA | ext gross area / External Gross Area / Gross Floor Area / Total Building Area / External Area / Gross Square Feet | float | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.ASSIGNABLE_AREA | assignable area / Net Usable Area / Leasable Area / Occupiable Area / Net Square Feet | float | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.NON_ASSIGNABLE_AREA | non assignable area / Non-Assignable Area / Common Area / Non-Usable Area / Circulation Area / Overhead Area | float | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.SITE | site / Campus Site / Location Code / Campus Code / Site Identifier | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.CAMPUS_SECTOR | campus sector / Campus Zone / Building Sector / Campus Region / Area of Campus | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.ACCESS_LEVEL_CODE | access level code / Security Level Code / Access Code / Entry Level Code | int | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.ACCESS_LEVEL_NAME | access level name / Security Level Name / Access Description / Entry Level Name | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.BUILDING_TYPE | building type / Facility Type / Building Category / Structure Type | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.OWNERSHIP_TYPE | ownership type / Property Ownership / Lease Status / Asset Ownership | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.BUILDING_USE | building use / Facility Use / Primary Use / Building Function / Usage Code | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.OCCUPANCY_CLASS | occupancy class / Fire Code Class / Occupancy Type / Safety Class / Building Occupancy | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.BUILDING_HEIGHT | building height / Structure Height / Height in Feet / Vertical Dimension | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.COST_CENTER_CODE | cost center code / Cost Center ID / Financial Cost Center / Accounting Cost Center | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.COST_COLLECTOR_KEY | cost collector key / Cost Collector ID / Financial Collector Code / Cost Allocation Key | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.LATITUDE_WGS | latitude wgs / Latitude / WGS Latitude / Geo Latitude / Latitude Coordinate | float | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.LONGITUDE_WGS | longitude wgs / Longitude / WGS Longitude / Geo Longitude / Longitude Coordinate | float | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.EASTING_X_SPCS | easting x spcs / Easting / X Coordinate / SPCS Easting / Projected X / Map Easting | float | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.NORTHING_Y_SPCS | northing y spcs / Northing / Y Coordinate / SPCS Northing / Projected Y / Map Northing | float | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.BUILDING_SORT | building sort / Sort Order / Building Sequence / Display Order | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.BUILDING_NAMED_FOR | building named for / Named For / Dedicated To / Honoree / Building Namesake / Person Named | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.BUILDING_NAME | building name / Short Name / Facility Name / Building Label | varchar(127) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.DATE_BUILT | date built / Construction Date / Built Date / Completion Date | varchar(255) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.DATE_ACQUIRED | date acquired / Purchase Date / Acquisition Date / Lease Start Date | varchar(255) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.DATE_OCCUPIED | date occupied / Occupancy Start Date / Move-in Date / First Occupied Date | varchar(255) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.WAREHOUSE_LOAD_DATE | warehouse load date | varchar(255) | schema / FCLT_BUILDING_HIST_1 |
| FCLT_BUILDING_HIST_1.NUM_OF_ROOMS | num of rooms / number of rooms | int | schema / FCLT_BUILDING_HIST_1 |

## FCLT_FLOOR

Stores dimensional information for individual floors within buildings, including floor numbers, area metrics, access levels, and sorting sequences.

恢复表名: fclt floor / floor / floors / building_floor / building_floors / floor_dimension / floor_fact
SQL表别名: f, ff, t1

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FCLT_FLOOR.FCLT_FLOOR_KEY | fclt floor key / floor_key / floor_id / floor_identifier / unique_floor_id | varchar(127) | dw_76, dw_1488, dw_1109, dw_2274, dw_238, dw_2450 |
| FCLT_FLOOR.FCLT_BUILDING_KEY | fclt building key / building_key / building_id / building_identifier / parent_building_key | varchar(127) | dw_76, dw_385, dw_1488, dw_5155, dw_1109, dw_118, dw_1451, dw_1555 |
| FCLT_FLOOR.FLOOR | floor / floor_number / floor_num / level_number / floor_level | varchar(127) | dw_76, dw_385, dw_1488, dw_5155, dw_118, dw_1451, dw_1555, dw_293 |
| FCLT_FLOOR.EXT_GROSS_AREA | ext gross area / external_gross_area / gross_area / total_floor_area / ext_gross_sqft | float | schema / FCLT_FLOOR |
| FCLT_FLOOR.ASSIGNABLE_AREA | assignable area / assignable_area / net_assignable_area / usable_area / assignable_sqft | float | dw_76, dw_1488, dw_1109, dw_2274, dw_238, dw_2450, dw_293 |
| FCLT_FLOOR.NON_ASSIGNABLE_AREA | non assignable area / non_assignable_area / common_area / non_usable_area / non_assignable_sqft | float | dw_76 |
| FCLT_FLOOR.FLOOR_SORT_SEQUENCE | floor sort sequence / floor_sort / sort_order / floor_sequence / display_order | varchar(127) | dw_385, dw_5155 |
| FCLT_FLOOR.LEVEL_ID | level id / level identifier / level_id / floor_level_id / level_identifier / level_code | varchar(127) | schema / FCLT_FLOOR |
| FCLT_FLOOR.BUILDING_WINGS_ID | building wings id / building wings identifier / building_wing_id / wing_id / wing_identifier / building_wing | varchar(127) | schema / FCLT_FLOOR |
| FCLT_FLOOR.ACCESS_LEVEL | access level / access_level / security_level / floor_access / access_code | varchar(127) | dw_385, dw_5155, dw_118, dw_1451, dw_1555 |
| FCLT_FLOOR.WAREHOUSE_LOAD_DATE | warehouse load date / load_date / warehouse_date / etl_date / data_load_date | varchar(255) | schema / FCLT_FLOOR |

## FCLT_FLOOR_HIST

Stores historical records of building floor attributes, including area measurements, identifiers, and metadata for specific fiscal periods.

恢复表名: fclt floor hist / Floor History / Floor Historical Data / Building Floor History / Floor Area History / Historical Floor Metrics
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FCLT_FLOOR_HIST.FCLT_FLOOR_HIST_KEY | fclt floor hist key / Floor History Key / History ID / Record Key / Unique Identifier | varchar(127) | schema / FCLT_FLOOR_HIST |
| FCLT_FLOOR_HIST.FISCAL_PERIOD | fiscal period / Period / Fiscal Month / Reporting Period | varchar(127) | schema / FCLT_FLOOR_HIST |
| FCLT_FLOOR_HIST.FCLT_FLOOR_KEY | fclt floor key / Floor Key / Floor ID / Building Floor Identifier | varchar(127) | schema / FCLT_FLOOR_HIST |
| FCLT_FLOOR_HIST.FCLT_BUILDING_KEY | fclt building key / Building Key / Building ID / Building Identifier | varchar(127) | schema / FCLT_FLOOR_HIST |
| FCLT_FLOOR_HIST.FLOOR | floor / Floor Number / Floor Level / Floor Name / Level | varchar(127) | schema / FCLT_FLOOR_HIST |
| FCLT_FLOOR_HIST.EXT_GROSS_AREA | ext gross area / External Gross Area / Gross Area / Total Area / External Area | float | schema / FCLT_FLOOR_HIST |
| FCLT_FLOOR_HIST.ASSIGNABLE_AREA | assignable area / Leasable Area / Usable Area / Net Area | float | schema / FCLT_FLOOR_HIST |
| FCLT_FLOOR_HIST.NON_ASSIGNABLE_AREA | non assignable area / Non-Assignable Area / Common Area / Non-Leasable Area / Overhead Area | float | schema / FCLT_FLOOR_HIST |
| FCLT_FLOOR_HIST.FLOOR_SORT_SEQUENCE | floor sort sequence / Floor Sort Order / Sort Sequence / Floor Order / Display Order | varchar(127) | schema / FCLT_FLOOR_HIST |
| FCLT_FLOOR_HIST.LEVEL_ID | level id / level identifier / Floor Level ID | varchar(127) | schema / FCLT_FLOOR_HIST |
| FCLT_FLOOR_HIST.BUILDING_WINGS_ID | building wings id / building wings identifier / Building Wing ID / Wing Identifier / Wing ID | varchar(127) | schema / FCLT_FLOOR_HIST |
| FCLT_FLOOR_HIST.ACCESS_LEVEL | access level / Security Level / Access Control Level | varchar(127) | schema / FCLT_FLOOR_HIST |
| FCLT_FLOOR_HIST.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date | varchar(255) | schema / FCLT_FLOOR_HIST |

## FCLT_MAJOR_USE

Dimension table defining the primary functional use or category of rooms and spaces within a facility, including codes, descriptions, and assignability flags.

恢复表名: fclt major use / Major Use / Major Use Dimension / Room Use Type / Space Usage Category / Facility Use Code / Building Use Type
SQL表别名: mu, t0

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FCLT_MAJOR_USE.FCLT_MAJOR_USE_KEY | fclt major use key / Major Use Key / Major Use ID / Use Code / Space Use Key / Room Use ID | varchar(127) | dw_2962, dw_3219, dw_3272, dw_3379, dw_3579, dw_4034, dw_4142, dw_4590 |
| FCLT_MAJOR_USE.MAJOR_USE | major use / Use Code / Room Use / Space Use / Usage Type / Function Code | varchar(127) | dw_2962, dw_3219, dw_3272, dw_3379, dw_3579, dw_4034, dw_4142, dw_4590 |
| FCLT_MAJOR_USE.DESCRIPTION | description / Major Use Description / Use Description / Room Use Description / Space Description / Usage Label | varchar(127) | dw_2962, dw_3219, dw_3272, dw_3379, dw_3579, dw_4034, dw_4142, dw_4590 |
| FCLT_MAJOR_USE.ASSIGNABLE | assignable / Is Assignable / Assignability / Can Assign / Assignment Flag | varchar(127) | dw_2962, dw_3219, dw_3272, dw_3379, dw_3579, dw_4034, dw_4142, dw_4590 |
| FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / ETL Date / Data Load Date / Refresh Date | varchar(255) | schema / FCLT_MAJOR_USE |

## FCLT_MAJOR_USE_HIST

Stores historical records of major facility usage categories, including descriptions, assignability status, and fiscal period associations for space management.

恢复表名: fclt major use hist / Major Use History / Facility Major Use History / Space Major Use History / Major Use Historical Data / Facility Usage History
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FCLT_MAJOR_USE_HIST.FCLT_MAJOR_USE_HIST_KEY | fclt major use hist key / Major Use History Key / History Key / Record ID / Unique Identifier / Surrogate Key | varchar(127) | schema / FCLT_MAJOR_USE_HIST |
| FCLT_MAJOR_USE_HIST.FISCAL_PERIOD | fiscal period / Period / Fiscal Year Month / Reporting Period / Time Period | varchar(127) | schema / FCLT_MAJOR_USE_HIST |
| FCLT_MAJOR_USE_HIST.FCLT_MAJOR_USE_KEY | fclt major use key / Major Use Key / Use Key / Category ID / Major Use ID / Foreign Key | varchar(127) | schema / FCLT_MAJOR_USE_HIST |
| FCLT_MAJOR_USE_HIST.MAJOR_USE | major use / Use Code / Usage Type / Space Type / Category Code | varchar(127) | schema / FCLT_MAJOR_USE_HIST |
| FCLT_MAJOR_USE_HIST.DESCRIPTION | description / Use Description / Category Name / Full Name / Label | varchar(127) | schema / FCLT_MAJOR_USE_HIST |
| FCLT_MAJOR_USE_HIST.ASSIGNABLE | assignable / Is Assignable / Assignment Flag / Can Assign / Assignable Status | varchar(127) | schema / FCLT_MAJOR_USE_HIST |
| FCLT_MAJOR_USE_HIST.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / ETL Date / Data Load Date / Ingestion Date | varchar(255) | schema / FCLT_MAJOR_USE_HIST |

## FCLT_ORGANIZATION

Dimension table containing the hierarchy, identifiers, and attributes of academic departments, programs, and administrative units within the Faculty of Arts and Sciences, including links to HR and Space systems.

恢复表名: fclt organization / Organization / Department / Faculty Organization / Academic Unit / Org / Department Hierarchy
SQL表别名: f, fo, fo2, o, parent_org, t0, t1, t2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FCLT_ORGANIZATION.FCLT_ORGANIZATION_KEY | fclt organization key / Organization Key / Org Key / Primary Key / ID / Unique Identifier | varchar(127) | dw_1864, dw_2321, dw_3252, dw_4055, dw_4352, dw_2559, dw_3542, dw_4402 |
| FCLT_ORGANIZATION.ORGANIZATION_ID | organization id / organization identifier / Org ID / Department ID / Unit ID / Business Key | varchar(127) | dw_1864, dw_2321, dw_3895, dw_4099, dw_702, dw_770 |
| FCLT_ORGANIZATION.ORGANIZATION | organization / Organization Code / Org Code / Department Code / Acronym / Short Name | varchar(127) | dw_1864, dw_3895 |
| FCLT_ORGANIZATION.ORGANIZATION_NAME | organization name / Department Name / Unit Name / Academic Unit / Program Name | varchar(127) | dw_1864, dw_2321, dw_3252, dw_4055, dw_4352, dw_3542, dw_3895, dw_4099 |
| FCLT_ORGANIZATION.FCLT_ORG_PARENT_KEY | fclt org parent key / Parent Organization Key / Parent Key / Superior Org Key / Hierarchy Parent | varchar(127) | dw_4352 |
| FCLT_ORGANIZATION.ORG_PARENT | org parent / Parent Organization / Parent Code / Superior Department / Reporting Unit | varchar(127) | dw_3252, dw_3542, dw_4099 |
| FCLT_ORGANIZATION.FCLT_MAJOR_ORG_KEY | fclt major org key / Major Organization Key / Major Org Key / Top Level Org Key / Division Key | varchar(127) | dw_2321, dw_4099, dw_702 |
| FCLT_ORGANIZATION.MAJOR_ORG | major org / Major Organization / Top Level Org / Division / School | varchar(127) | dw_4055, dw_4402 |
| FCLT_ORGANIZATION.ORGANIZATION_LEVEL | organization level / Org Level / Hierarchy Level / Depth / Tier | varchar(127) | dw_1864, dw_3252, dw_4055, dw_4352, dw_3542, dw_3895, dw_4099, dw_4402 |
| FCLT_ORGANIZATION.ORGANIZATION_NUMBER | organization number / Org Number / Department Number / Cost Center / Budget Code | varchar(127) | dw_1864, dw_2321, dw_4055, dw_2559, dw_3895, dw_4099, dw_4402, dw_702 |
| FCLT_ORGANIZATION.ORGANIZATION_SORT | organization sort / Sort Order / Display Order / Sequence | varchar(127) | dw_2321 |
| FCLT_ORGANIZATION.ASSIGNABLE | assignable / Is Assignable / Active / Valid / Flag | varchar(127) | dw_1864, dw_2321, dw_3252, dw_4055, dw_4352, dw_2559, dw_3542, dw_3895 |
| FCLT_ORGANIZATION.COURSE | course / Course Number / Department Number / Academic Code / Subject | varchar(127) | schema / FCLT_ORGANIZATION |
| FCLT_ORGANIZATION.DESCRIPTION | description / Long Name / Full Name / Department Description / Details | varchar(127) | dw_1864, dw_3252, dw_4352, dw_3542, dw_770 |
| FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Warehouse Date / ETL Date / Update Date / Timestamp | varchar(255) | dw_2559 |
| FCLT_ORGANIZATION.DLC_KEY | dlc key / Department Key / Dept Key / Academic Dept ID / SIS Department Key | varchar(127) | dw_1864, dw_2321, dw_3252, dw_4055, dw_4352, dw_2559, dw_3542, dw_3895 |
| FCLT_ORGANIZATION.DLC_NAME | dlc name / Department Name / Academic Department / Dept Name / Program Title | varchar(127) | dw_4055, dw_4352, dw_2559, dw_3895, dw_4402 |
| FCLT_ORGANIZATION.HR_DEPARTMENT_CODE_OLD | hr department code old / HR Department Code / Old HR Code / Legacy HR Code / HR Dept ID / Personnel Code | varchar(127) | dw_1864 |
| FCLT_ORGANIZATION.HR_ORG_UNIT_ID | hr org unit id / hr org unit identifier / HR Unit ID / Personnel Unit ID / HR Identifier / Workday ID | varchar(127) | dw_3252, dw_3542 |
| FCLT_ORGANIZATION.HR_DEPARTMENT_NAME | hr department name / HR Unit Name / Personnel Department / HR Name / Official HR Name | varchar(127) | dw_2321, dw_4099, dw_702 |

## FCLT_ORGANIZATION_HIST

Historical snapshot of the university's organizational structure, mapping academic units, departments, and administrative offices to their parent hierarchies, major organizations, and HR department codes for a specific fiscal period.

恢复表名: fclt organization hist / Organization History / Org History / Department History / Academic Unit History / Organizational Structure History / FCLT Organization
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FCLT_ORGANIZATION_HIST.FCLT_ORGANIZATION_HIST_KEY | fclt organization hist key / Organization History Key / Org Hist Key / Record ID / Unique Identifier | varchar(127) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.FISCAL_PERIOD | fiscal period / Period / Fiscal Year Month / Reporting Period | varchar(127) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.FCLT_ORGANIZATION_KEY | fclt organization key / Organization Key / Org Key / Department Key / Unit Key | varchar(127) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.ORGANIZATION_ID | organization id / organization identifier / Org ID / Department ID / Unit ID | varchar(127) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.ORGANIZATION | organization / Organization Code / Org Code / Department Code / Unit Code / Acronym | varchar(127) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.ORGANIZATION_NAME | organization name / Org Name / Department Name / Unit Name / Short Name | varchar(127) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.FCLT_ORG_PARENT_KEY | fclt org parent key / Parent Organization Key / Parent Org Key / Parent Department Key / Superior Unit Key | varchar(127) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.ORG_PARENT | org parent / Parent Organization / Parent Org / Parent Department / Superior Unit / Reporting To | varchar(127) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.FCLT_MAJOR_ORG_KEY | fclt major org key / Major Organization Key / Major Org Key / Top Level Org Key / Division Key | varchar(127) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.MAJOR_ORG | major org / Major Organization / Division / Top Level Org / School | varchar(127) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.ORGANIZATION_LEVEL | organization level / Org Level / Hierarchy Level / Depth / Tier | varchar(127) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.ORGANIZATION_NUMBER | organization number / Org Number / Department Number / Cost Center Number | varchar(127) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.ORGANIZATION_SORT | organization sort / Sort Order / Sort Key / Sequence Number | varchar(127) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.ASSIGNABLE | assignable / Is Assignable / Can Assign / Assignment Flag | varchar(127) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.COURSE | course / Course Code / Academic Course / Subject | varchar(127) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.DESCRIPTION | description / Org Description / Details / Notes | varchar(127) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / ETL Date / Data Load Date | varchar(255) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.DLC_KEY | dlc key / Department Level Code Key / DLC ID | varchar(127) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.DLC_NAME | dlc name / Department Level Code Name / Formal Department Name | varchar(127) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.HR_DEPARTMENT_CODE_OLD | hr department code old / Old HR Dept Code / Legacy HR Code / Previous HR Department | varchar(127) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.HR_ORG_UNIT_ID | hr org unit id / hr org unit identifier / HR Organization Unit ID / HR Unit ID / PeopleSoft Org ID | varchar(127) | schema / FCLT_ORGANIZATION_HIST |
| FCLT_ORGANIZATION_HIST.HR_DEPARTMENT_NAME | hr department name / HR Dept Name / PeopleSoft Department Name / Official HR Name | varchar(127) | schema / FCLT_ORGANIZATION_HIST |

## FCLT_ORG_DLC_KEY

A bridge table that maps FCLT organization keys to Department Location Codes (DLC keys), enabling the association of physical organizations (like buildings or rooms) with academic or administrative departments.

恢复表名: fclt org dlc key / Organization DLC Key Mapping / Org DLC Bridge / Department Location Code Key / Organization Department Link / FCLT Org DLC / Org DLC Join Table
SQL表别名: d, dlc, f, fdlk, fodk, t0, t1

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FCLT_ORG_DLC_KEY.FCLT_ORGANIZATION_KEY | fclt organization key / Organization Key / Org Key / FCLT Organization ID / Organization Identifier / Org ID / Physical Organization Key | varchar(127) | dw_1166, dw_1702, dw_1833, dw_1873, dw_1890, dw_1896, dw_1966, dw_2321 |
| FCLT_ORG_DLC_KEY.DLC_KEY | dlc key / Department Location Code / DLC / Department Code / Academic Department Key / Department Identifier / DLC ID | varchar(127) | dw_1166, dw_1702, dw_1833, dw_1873, dw_1890, dw_1896, dw_1966, dw_2321 |

## FCLT_ROOMS

Stores detailed information about individual rooms within buildings, including location identifiers, physical dimensions, usage classifications, organizational assignments, and access control levels.

恢复表名: fclt rooms / rooms / room / facility rooms / building rooms / space inventory / room directory
SQL表别名: f, fr, r, t0, t1, t2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FCLT_ROOMS.FCLT_ROOM_KEY | fclt room key / room key / room id / room identifier / unique room code | varchar(127) | dw_3219, dw_3332, dw_1488, dw_4775, dw_5052, dw_5315, dw_1451, dw_4041 |
| FCLT_ROOMS.BUILDING_ROOM | building room / room location / room address / building-room combo / location code | varchar(127) | dw_3219, dw_3332, dw_4775, dw_5052, dw_5315, dw_1451, dw_4041, dw_4299 |
| FCLT_ROOMS.FCLT_BUILDING_KEY | fclt building key / building key / building id / building code / building identifier | varchar(127) | dw_3332, dw_1488, dw_4693, dw_5315, dw_1451, dw_4299, dw_4905 |
| FCLT_ROOMS.FLOOR | floor / floor number / level / storey | varchar(127) | dw_3219, dw_1488, dw_4775, dw_5052, dw_5315, dw_1451, dw_4041, dw_4905 |
| FCLT_ROOMS.FCLT_FLOOR_KEY | fclt floor key / floor key / floor id / building floor key | varchar(127) | dw_1488 |
| FCLT_ROOMS.ROOM | room / room number / room name / room id / room label | varchar(127) | dw_3219, dw_4775, dw_5052, dw_5315 |
| FCLT_ROOMS.SPACE_ID | space id / space identifier / full space code / unique space key | varchar(127) | dw_3219, dw_4775, dw_5052 |
| FCLT_ROOMS.FCLT_MAJOR_USE_KEY | fclt major use key / major use key / primary use id / main usage code | varchar(127) | dw_3219, dw_4775, dw_5052, dw_4905 |
| FCLT_ROOMS.MAJOR_USE_DESC | major use desc / major use description / major use / primary use / main usage / room type / usage description | varchar(127) | dw_3219, dw_3332, dw_4775, dw_5052, dw_5315, dw_1451, dw_4041, dw_4299 |
| FCLT_ROOMS.FCLT_USE_KEY | fclt use key / use key / usage id / specific use code | varchar(127) | schema / FCLT_ROOMS |
| FCLT_ROOMS.USE_DESC | use desc / use description / specific use / detailed usage | varchar(127) | schema / FCLT_ROOMS |
| FCLT_ROOMS.FCLT_MINOR_USE_KEY | fclt minor use key / minor use key / secondary use id / sub-usage code | varchar(127) | schema / FCLT_ROOMS |
| FCLT_ROOMS.MINOR_USE_DESC | minor use desc / minor use description / minor use / secondary use / sub-usage description | varchar(127) | schema / FCLT_ROOMS |
| FCLT_ROOMS.FCLT_ORGANIZATION_KEY | fclt organization key / organization key / org id / department id / owner id | varchar(127) | dw_3219, dw_3332, dw_4693, dw_4775, dw_5052, dw_4041, dw_4299, dw_3019 |
| FCLT_ROOMS.ORGANIZATION_NAME | organization name / department name / org name / occupant / owner | varchar(127) | dw_3332, dw_5315, dw_1451, dw_4041, dw_4299, dw_4905, dw_3019 |
| FCLT_ROOMS.FCLT_MINOR_ORGANIZATION_KEY | fclt minor organization key / minor organization key / secondary org id / sub-department id | varchar(127) | schema / FCLT_ROOMS |
| FCLT_ROOMS.MINOR_ORGANIZATION | minor organization / secondary department / sub-org name | varchar(127) | schema / FCLT_ROOMS |
| FCLT_ROOMS.AREA | area / square footage / size / room area / sq ft | float | dw_3219, dw_3332, dw_1488, dw_4693, dw_4775, dw_5052, dw_5315, dw_1451 |
| FCLT_ROOMS.ROOM_FULL_NAME | room full name / full room name / room title / complete room identifier | varchar(127) | dw_4693 |
| FCLT_ROOMS.DEPT_CODE | dept code / department code / department identifier | varchar(127) | dw_3332, dw_4693, dw_4041, dw_3019 |
| FCLT_ROOMS.ACCESS_LEVEL | access level / security level / access control / entry level | varchar(127) | dw_3219, dw_1488, dw_4775, dw_5052, dw_5315, dw_1451, dw_4299, dw_4905 |
| FCLT_ROOMS.LATITUDE_WGS | latitude wgs / latitude / lat / wgs latitude / geographic latitude | float | schema / FCLT_ROOMS |
| FCLT_ROOMS.LONGITUDE_WGS | longitude wgs / longitude / lon / wgs longitude / geographic longitude | float | schema / FCLT_ROOMS |
| FCLT_ROOMS.NORTHING_SPCS | northing spcs / northing / spcs northing / y coordinate / state plane northing | float | schema / FCLT_ROOMS |
| FCLT_ROOMS.EASTING_SPCS | easting spcs / easting / spcs easting / x coordinate / state plane easting | float | schema / FCLT_ROOMS |
| FCLT_ROOMS.WAREHOUSE_LOAD_DATE | warehouse load date / load date / warehouse date / etl date / data load timestamp | varchar(255) | schema / FCLT_ROOMS |

## FCLT_ROOMS_HIST

Stores historical snapshots of facility room attributes, including location, usage, organization, and area, for a specific fiscal period.

恢复表名: fclt rooms hist / Room History Fact Table / Historical Room Data / Facility Room History / Room Usage History
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FCLT_ROOMS_HIST.FCLT_ROOM_HIST_KEY | fclt room hist key / Room History Key / Historical Room ID / Room Hist Key / Unique Room History Identifier | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.FISCAL_PERIOD | fiscal period / Period / Fiscal Year Month / Reporting Period | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.FCLT_ROOM_KEY | fclt room key / Room Key / Room ID / Facility Room Key / Building Room Key | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.BUILDING_ROOM | building room / Room Number / Building and Room / Physical Room ID | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.FCLT_BUILDING_KEY | fclt building key / Building Key / Building ID / Facility Building Key | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.FLOOR | floor / Floor Number / Level | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.FCLT_FLOOR_KEY | fclt floor key / Floor Key / Floor ID / Building Floor Key | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.ROOM | room / Room Number / Room ID | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.SPACE_ID | space id / space identifier / Full Space Key | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.FCLT_MAJOR_USE_KEY | fclt major use key / Major Use Key / Primary Use ID / Main Usage Key | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.MAJOR_USE_DESC | major use desc / major use description / Primary Use / Main Usage Description / Room Type | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.FCLT_USE_KEY | fclt use key / Use Key / Usage ID / Specific Use Key | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.USE_DESC | use desc / use description / Usage Description / Specific Use | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.FCLT_MINOR_USE_KEY | fclt minor use key / Minor Use Key / Secondary Use ID / Sub Use Key | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.MINOR_USE_DESC | minor use desc / minor use description / Secondary Use / Sub Usage Description | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.FCLT_ORGANIZATION_KEY | fclt organization key / Organization Key / Department Key / Primary Org ID | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.ORGANIZATION_NAME | organization name / Department Name / Primary Department / Occupant | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.FCLT_MINOR_ORGANIZATION_KEY | fclt minor organization key / Minor Organization Key / Secondary Dept Key / Sub Org ID | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.MINOR_ORGANIZATION | minor organization / Secondary Department / Sub Department | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.AREA | area / Square Feet / Room Size / Square Footage | float | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.ROOM_FULL_NAME | room full name / Room Name / Formal Room Name | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.DEPT_CODE | dept code / department code / Organization Code | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.ACCESS_LEVEL | access level / Security Level / Access Restriction | varchar(127) | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.LATITUDE_WGS | latitude wgs / Latitude / WGS Latitude / Geo Latitude | float | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.LONGITUDE_WGS | longitude wgs / Longitude / WGS Longitude / Geo Longitude | float | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.NORTHING_SPCS | northing spcs / Northing / SPCS Northing / State Plane Northing | float | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.EASTING_SPCS | easting spcs / Easting / SPCS Easting / State Plane Easting | float | schema / FCLT_ROOMS_HIST |
| FCLT_ROOMS_HIST.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date | varchar(255) | schema / FCLT_ROOMS_HIST |

## FRC_FISCAL_PERIODS

Reference table mapping fiscal period keys to calendar descriptions and standard fiscal period codes.

恢复表名: frc fiscal periods / fiscal periods / fiscal calendar / period mapping / fiscal period reference / time periods / accounting periods
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FRC_FISCAL_PERIODS.TIME_MONTH_KEY | time month key / month key / fiscal month key / period key / time period identifier | varchar(127) | schema / FRC_FISCAL_PERIODS |
| FRC_FISCAL_PERIODS.CALENDAR_PERIOD_DESCRIPTION | calendar period description / period description / fiscal period name / calendar month name / period label | varchar(127) | schema / FRC_FISCAL_PERIODS |
| FRC_FISCAL_PERIODS.FISCAL_PERIOD | fiscal period / period code / fiscal period code / accounting period / period identifier | varchar(127) | schema / FRC_FISCAL_PERIODS |

## FUND_CENTER_HIERARCHY

Stores the multi-level hierarchical structure of fund centers, including IDs and names for each level from 1 to 10, used for roll-ups and organizational reporting.

恢复表名: fund center hierarchy / fund center tree / fc hierarchy / fund center structure / cost center hierarchy / organizational fund center
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| FUND_CENTER_HIERARCHY.FUND_CENTER_KEY | fund center key / fc key / fund center identifier / fc id key | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_ID | fund center id / fund center identifier / fc id / fund center code / fc code / leaf fund center id | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_NAME | fund center name / fc name / fund center description / fc label | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_ID_LEVEL1 | fund center id level1 / fund center identifier level1 / level 1 fund center id / fc id level 1 / top level fc id / root fund center id / level 1 fc code | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_NAME_LEVEL1 | fund center name level1 / level 1 fund center name / fc name level 1 / top level fc name / root fund center name | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_ID_LEVEL2 | fund center id level2 / fund center identifier level2 / level 2 fund center id / fc id level 2 / second level fc id / level 2 fc code | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_NAME_LEVEL2 | fund center name level2 / level 2 fund center name / fc name level 2 / second level fc name | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_ID_LEVEL3 | fund center id level3 / fund center identifier level3 / level 3 fund center id / fc id level 3 / third level fc id / level 3 fc code | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_NAME_LEVEL3 | fund center name level3 / level 3 fund center name / fc name level 3 / third level fc name | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_ID_LEVEL4 | fund center id level4 / fund center identifier level4 / level 4 fund center id / fc id level 4 / fourth level fc id / level 4 fc code | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_NAME_LEVEL4 | fund center name level4 / level 4 fund center name / fc name level 4 / fourth level fc name | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_ID_LEVEL5 | fund center id level5 / fund center identifier level5 / level 5 fund center id / fc id level 5 / fifth level fc id / level 5 fc code | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_NAME_LEVEL5 | fund center name level5 / level 5 fund center name / fc name level 5 / fifth level fc name | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_ID_LEVEL6 | fund center id level6 / fund center identifier level6 / level 6 fund center id / fc id level 6 / sixth level fc id / level 6 fc code | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_NAME_LEVEL6 | fund center name level6 / level 6 fund center name / fc name level 6 / sixth level fc name | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_ID_LEVEL7 | fund center id level7 / fund center identifier level7 / level 7 fund center id / fc id level 7 / seventh level fc id / level 7 fc code | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_NAME_LEVEL7 | fund center name level7 / level 7 fund center name / fc name level 7 / seventh level fc name | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_ID_LEVEL8 | fund center id level8 / fund center identifier level8 / level 8 fund center id / fc id level 8 / eighth level fc id / level 8 fc code | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_NAME_LEVEL8 | fund center name level8 / level 8 fund center name / fc name level 8 / eighth level fc name | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_ID_LEVEL9 | fund center id level9 / fund center identifier level9 / level 9 fund center id / fc id level 9 / ninth level fc id / level 9 fc code | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_NAME_LEVEL9 | fund center name level9 / level 9 fund center name / fc name level 9 / ninth level fc name | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_ID_LEVEL10 | fund center id level10 / fund center identifier level10 / level 10 fund center id / fc id level 10 / tenth level fc id / level 10 fc code | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.FUND_CENTER_NAME_LEVEL10 | fund center name level10 / level 10 fund center name / fc name level 10 / tenth level fc name | varchar(127) | schema / FUND_CENTER_HIERARCHY |
| FUND_CENTER_HIERARCHY.WAREHOUSE_LOAD_DATE | warehouse load date / load date / etl date / data load date / refresh date | varchar(255) | schema / FUND_CENTER_HIERARCHY |

## HR_FACULTY_ROSTER

Stores detailed personnel and appointment information for faculty members, including names, degrees, job titles, and organizational affiliations.

恢复表名: hr faculty roster / Faculty Roster / HR Faculty / Faculty Directory / Academic Staff List / Faculty Personnel
SQL表别名: hfr

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| HR_FACULTY_ROSTER.MIT_ID | mit id / mit identifier / Employee ID / Staff ID / Person ID / Faculty ID / Unique Identifier | varchar(127) | schema / HR_FACULTY_ROSTER |
| HR_FACULTY_ROSTER.LAST_NAME | last name / Surname / Family Name | varchar(127) | schema / HR_FACULTY_ROSTER |
| HR_FACULTY_ROSTER.FIRST_NAME | first name / Given Name / Forename | varchar(127) | schema / HR_FACULTY_ROSTER |
| HR_FACULTY_ROSTER.MIDDLE_NAME | middle name / Middle Initial | varchar(127) | schema / HR_FACULTY_ROSTER |
| HR_FACULTY_ROSTER.TERMINAL_DEGREE | terminal degree / Highest Degree / Academic Degree / Final Degree / Degree Type | varchar(127) | schema / HR_FACULTY_ROSTER |
| HR_FACULTY_ROSTER.APPOINTMENT_TYPE | appointment type / Employment Type / Appointment Category / Job Appointment / Appointment Status | varchar(127) | schema / HR_FACULTY_ROSTER |
| HR_FACULTY_ROSTER.JOB_TITLE | job title / Academic Rank / Faculty Rank / Position Rank / Title | varchar(127) | schema / HR_FACULTY_ROSTER |
| HR_FACULTY_ROSTER.HR_ORG_UNIT_TITLE | hr org unit title / HR Org Unit / Department / Academic Department / School / Organizational Unit / Department Name | varchar(127) | schema / HR_FACULTY_ROSTER |
| HR_FACULTY_ROSTER.POSITION_TITLE | position title / Role Title / Job Position / Position Name | varchar(127) | schema / HR_FACULTY_ROSTER |
| HR_FACULTY_ROSTER.ADMIN_ORG_UNIT_TITLE | admin org unit title / Admin Org Unit / Administrative Department / Admin Unit / Administrative Organization | varchar(127) | schema / HR_FACULTY_ROSTER |
| HR_FACULTY_ROSTER.ADMIN_POSITION_TITLE | admin position title / Administrative Position / Admin Role | varchar(127) | schema / HR_FACULTY_ROSTER |
| HR_FACULTY_ROSTER.ADMIN_JOB_TITLE | admin job title / Administrative Job Title / Admin Rank | varchar(127) | schema / HR_FACULTY_ROSTER |
| HR_FACULTY_ROSTER.DIRECTORY_ORG_UNIT_TITLE | directory org unit title / Directory Org Unit / Directory Department / Public Department / Directory Unit | varchar(127) | schema / HR_FACULTY_ROSTER |
| HR_FACULTY_ROSTER.ENDOWED_CHAIR | endowed chair / Chair Title / Named Chair / Endowed Position | varchar(127) | schema / HR_FACULTY_ROSTER |
| HR_FACULTY_ROSTER.EMERITUS_STATUS | emeritus status / Retirement Status / Emeritus Flag / Retired Status | varchar(31) | schema / HR_FACULTY_ROSTER |
| HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date / Update Date / Warehouse Date | varchar(255) | schema / HR_FACULTY_ROSTER |

## HR_ORG_UNIT

Reference table containing the hierarchical structure of MIT departments and organizations, including department codes, names, hierarchy levels, and DLC keys for joining with fact tables.

恢复表名: hr org unit / HR Organization Unit / Department Hierarchy / Org Unit Reference / Department Master / Department Structure
SQL表别名: h, h2, hou, hou2, t1, t2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| HR_ORG_UNIT.HR_ORG_UNIT_KEY | hr org unit key / Org Unit Key / Organization Unit Key / Org Key / Unit Key | varchar(127) | dw_2952, dw_4353, dw_4056, dw_4451, dw_4548 |
| HR_ORG_UNIT.HR_ORG_UNIT_ID | hr org unit id / hr org unit identifier / Org Unit ID / Organization Unit ID / Org ID / Unit ID | varchar(127) | dw_4353, dw_4099, dw_4056, dw_4451, dw_4484, dw_512, dw_2624, dw_2879 |
| HR_ORG_UNIT.HR_ORG_UNIT_TITLE | hr org unit title / Org Unit Title / Organization Unit Title / Unit Title / Org Title | varchar(127) | dw_3452, dw_4353, dw_4099, dw_4056, dw_4451, dw_4648, dw_512, dw_2624 |
| HR_ORG_UNIT.HR_ORG_UNIT_LEVEL | hr org unit level / Org Unit Level / Organization Unit Level / Unit Level / Org Level | varchar(127) | dw_3452, dw_4353, dw_4099, dw_4056, dw_4451, dw_4484, dw_4548, dw_4648 |
| HR_ORG_UNIT.HR_DEPARTMENT_ID | hr department id / hr department identifier / Department ID / Dept ID / Department Number / Dept Number | varchar(127) | dw_2952, dw_4548 |
| HR_ORG_UNIT.HR_DEPARTMENT_CODE | hr department code / Department Code / Dept Code / Department Number / Dept Number | varchar(127) | dw_3452, dw_4353, dw_4099, dw_4056, dw_4451, dw_4484, dw_4648, dw_512 |
| HR_ORG_UNIT.HR_DEPARTMENT_CODE_OLD | hr department code old / Old Department Code / Legacy Department Code / Previous Dept Code / Old Dept Code / Legacy Dept Code | varchar(127) | dw_2952, dw_4548, dw_4648 |
| HR_ORG_UNIT.HR_DEPARTMENT_NAME | hr department name / Department Name / Dept Name / Department / Dept | varchar(127) | dw_3452, dw_2952, dw_4353, dw_4099, dw_4056, dw_4451, dw_4484, dw_4548 |
| HR_ORG_UNIT.HR_DEPARTMENT_NAME_LONG | hr department name long / Long Department Name / Full Department Name / Dept Long Name / Department Full Name / Long Dept Name | varchar(127) | dw_3452, dw_4099, dw_4484, dw_512 |
| HR_ORG_UNIT.HR_DEPARTMENT_NAME_ALPHA | hr department name alpha / Alpha Department Name / Alphabetical Dept Name / Dept Name Alpha / Sorted Dept Name / Alpha Dept Name | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.ORG_HIER_SCHOOL_AREA_NAME | org hier school area name / School Area Name / Org Hierarchy School Area / School Area / Area Name | varchar(127) | dw_4353, dw_512 |
| HR_ORG_UNIT.ORG_HIER_TOP_LEVEL_NAME | org hier top level name / Top Level Name / Org Hierarchy Top Level / Top Level Area / Top Level / Top Area | varchar(127) | dw_3452, dw_4548 |
| HR_ORG_UNIT.ORG_HIER_ROOT_NAME | org hier root name / Root Name / Org Hierarchy Root / Root Level / Root Area / Root | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL1_ID | hr org level1 id / hr org level1 identifier / Level 1 ID / Org Level 1 ID / Root ID / Level 1 Org ID / L1 ID | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL1_SORT | hr org level1 sort / Level 1 Sort / Org Level 1 Sort / Root Sort / Level 1 Order / L1 Sort | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL1_NAME | hr org level1 name / Level 1 Name / Org Level 1 Name / Root Name / Level 1 Org Name / L1 Name | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL2_ID | hr org level2 id / hr org level2 identifier / Level 2 ID / Org Level 2 ID / Top Level ID / Level 2 Org ID / L2 ID | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL2_SORT | hr org level2 sort / Level 2 Sort / Org Level 2 Sort / Top Level Sort / Level 2 Order / L2 Sort | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL2_NAME | hr org level2 name / Level 2 Name / Org Level 2 Name / Top Level Name / Level 2 Org Name / L2 Name | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL3_ID | hr org level3 id / hr org level3 identifier / Level 3 ID / Org Level 3 ID / School Area ID / Level 3 Org ID / L3 ID | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL3_SORT | hr org level3 sort / Level 3 Sort / Org Level 3 Sort / School Area Sort / Level 3 Order / L3 Sort | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL3_NAME | hr org level3 name / Level 3 Name / Org Level 3 Name / School Area Name / Level 3 Org Name / L3 Name | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL4_ID | hr org level4 id / hr org level4 identifier / Level 4 ID / Org Level 4 ID / Department ID / Level 4 Org ID / L4 ID | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL4_SORT | hr org level4 sort / Level 4 Sort / Org Level 4 Sort / Department Sort / Level 4 Order / L4 Sort | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL4_NAME | hr org level4 name / Level 4 Name / Org Level 4 Name / Department Name / Level 4 Org Name / L4 Name | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL5_ID | hr org level5 id / hr org level5 identifier / Level 5 ID / Org Level 5 ID / Sub Department ID / Level 5 Org ID / L5 ID | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL5_SORT | hr org level5 sort / Level 5 Sort / Org Level 5 Sort / Sub Department Sort / Level 5 Order / L5 Sort | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL5_NAME | hr org level5 name / Level 5 Name / Org Level 5 Name / Sub Department Name / Level 5 Org Name / L5 Name | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL6_ID | hr org level6 id / hr org level6 identifier | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL6_SORT | hr org level6 sort | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL6_NAME | hr org level6 name | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL7_ID | hr org level7 id / hr org level7 identifier | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL7_SORT | hr org level7 sort | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.HR_ORG_LEVEL7_NAME | hr org level7 name | varchar(127) | schema / HR_ORG_UNIT |
| HR_ORG_UNIT.DLC_KEY | dlc key | varchar(127) | dw_3452, dw_4353, dw_4099, dw_4056, dw_4451, dw_4484, dw_4548, dw_4648 |
| HR_ORG_UNIT.DLC_NAME | dlc name | varchar(127) | dw_3452, dw_4099, dw_2624 |
| HR_ORG_UNIT.WAREHOUSE_LOAD_DATE | warehouse load date | varchar(255) | dw_2952, dw_4484, dw_4648 |

## HR_ORG_UNIT_NEW

Stores the hierarchical structure of HR organizational units, including department codes, names, levels, and parent-child relationships within the MIT organizational chart.

恢复表名: hr org unit new / HR Organization Unit / Department Hierarchy / Org Unit / Department Structure / HR Org Unit / Organizational Unit
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| HR_ORG_UNIT_NEW.HR_ORG_UNIT_KEY | hr org unit key / Org Unit Key / Organization Unit Key / HR Org Key / Unit Key | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_ORG_UNIT_ID | hr org unit id / hr org unit identifier / Org Unit ID / Organization Unit ID / HR Org ID / Unit ID | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_ORG_UNIT_TITLE | hr org unit title / Org Unit Title / Organization Unit Title / Department Title / Unit Name | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_ORG_UNIT_LEVEL | hr org unit level / Org Unit Level / Organization Unit Level / Department Level / Unit Level | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_DEPARTMENT_CODE | hr department code / Department Code / Dept Code / Department Number | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_DEPARTMENT_ABBR | hr department abbr / Department Abbreviation / Dept Abbr / Department Short Code | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_DEPARTMENT_CODE_OLD | hr department code old / Old Department Code / Previous Department Code / Legacy Dept Code / Historical Department Code | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_DEPARTMENT_NAME | hr department name / Department Name / Dept Name / Department Title | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_DEPARTMENT_NAME_LONG | hr department name long / Long Department Name / Full Department Name / HR Dept Long Name / Department Full Name | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_DEPARTMENT_NAME_ALPHA | hr department name alpha / Alpha Department Name / Alphabetical Department Name / HR Dept Alpha Name / Department Name Alpha | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.ORG_HIER_SCHOOL_AREA_NAME | org hier school area name / School Area Name / Org Hierarchy School Area / Area Name / School Area | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.ORG_HIER_TOP_LEVEL_NAME | org hier top level name / Top Level Name / Org Hierarchy Top Level / Top Level Area / Highest Level Name | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.ORG_HIER_ROOT_NAME | org hier root name / Root Name / Org Hierarchy Root / Root Level Name / Top Root Name | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_ORG_LEVEL1_ID | hr org level1 id / hr org level1 identifier / Level 1 ID / Org Level 1 ID / First Level ID / Top Level ID | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_ORG_LEVEL1_SORT | hr org level1 sort / Level 1 Sort / Org Level 1 Sort Order / First Level Sort / Top Level Sort | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_ORG_LEVEL1_NAME | hr org level1 name / Level 1 Name / Org Level 1 Name / First Level Name / Top Level Name | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_ORG_LEVEL2_ID | hr org level2 id / hr org level2 identifier / Level 2 ID / Org Level 2 ID / Second Level ID / Upper Level ID | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_ORG_LEVEL2_SORT | hr org level2 sort / Level 2 Sort / Org Level 2 Sort Order / Second Level Sort / Upper Level Sort | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_ORG_LEVEL2_NAME | hr org level2 name / Level 2 Name / Org Level 2 Name / Second Level Name / Upper Level Name | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_ORG_LEVEL3_ID | hr org level3 id / hr org level3 identifier / Level 3 ID / Org Level 3 ID / Third Level ID / Middle Level ID | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_ORG_LEVEL3_SORT | hr org level3 sort / Level 3 Sort / Org Level 3 Sort Order / Third Level Sort / Middle Level Sort | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_ORG_LEVEL3_NAME | hr org level3 name / Level 3 Name / Org Level 3 Name / Third Level Name / Middle Level Name | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_ORG_LEVEL4_ID | hr org level4 id / hr org level4 identifier / Level 4 ID / Org Level 4 ID / Fourth Level ID / Lower Level ID | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_ORG_LEVEL4_SORT | hr org level4 sort / Level 4 Sort / Org Level 4 Sort Order / Fourth Level Sort / Lower Level Sort | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_ORG_LEVEL4_NAME | hr org level4 name / Level 4 Name / Org Level 4 Name / Fourth Level Name / Lower Level Name | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_ORG_LEVEL5_ID | hr org level5 id / hr org level5 identifier / Level 5 ID / Org Level 5 ID / Fifth Level ID / Bottom Level ID | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_ORG_LEVEL5_SORT | hr org level5 sort / Level 5 Sort / Org Level 5 Sort Order / Fifth Level Sort / Bottom Level Sort | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.HR_ORG_LEVEL5_NAME | hr org level5 name / Level 5 Name / Org Level 5 Name / Fifth Level Name / Bottom Level Name | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.DLC_KEY | dlc key / Data Load Control Key / Load Key / DLC Identifier | varchar(127) | schema / HR_ORG_UNIT_NEW |
| HR_ORG_UNIT_NEW.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date | varchar(255) | schema / HR_ORG_UNIT_NEW |

## IAP_SUBJECT_CATEGORY

Lookup table defining the subject categories for IAP (Independent Activities Program) activities, linking category identifiers to their names and descriptions.

恢复表名: iap subject category / IAP Category / Subject Category / IAP Subject Categories / Category Lookup / IAP Category Lookup
SQL表别名: c, isc

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| IAP_SUBJECT_CATEGORY.IAP_SUBJECT_CATEGORY_KEY | iap subject category key / Subject Category Key / Category Key / IAP Category ID / Subject Category ID / Category Identifier / IAP Subject Category Identifier | varchar(127) | dw_2844, dw_2905, dw_2635, dw_2713, dw_2766, dw_2826, dw_2872, dw_2921 |
| IAP_SUBJECT_CATEGORY.IAP_CATEGORY_NAME | iap category name / Category Name / Subject Category Name / IAP Category / Subject Category / Category Title / IAP Subject Category Name | varchar(127) | dw_2844, dw_2905, dw_2635, dw_2713, dw_2766, dw_2826, dw_2872, dw_2921 |
| IAP_SUBJECT_CATEGORY.IAP_CATEGORY_DESC | iap category desc / iap category description / Category Description / Subject Category Description / Category Details / Subject Category Details / IAP Subject Category Description | varchar(127) | dw_2844, dw_2905 |
| IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date / Refresh Date / Last Updated Date | varchar(255) | schema / IAP_SUBJECT_CATEGORY |

## IAP_SUBJECT_DETAIL

Stores detailed information about Independent Activities Period (IAP) subject offerings, including activity titles, descriptions, enrollment limits, fees, prerequisites, and associations with academic terms, categories, sponsors, and sessions.

恢复表名: iap subject detail / IAP Activities / Independent Activities Period Subjects / IAP Courses / IAP Events / IAP Subject Offerings
SQL表别名: d, i, iad, isd, t0, t1

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| IAP_SUBJECT_DETAIL.IAP_SUBJECT_CATEGORY_KEY | iap subject category key / Subject Category Key / IAP Category Key / Category ID / Subject Category ID / IAP Category ID | varchar(127) | dw_4245, dw_5095, dw_4229, dw_4313, dw_4075, dw_2985 |
| IAP_SUBJECT_DETAIL.IAP_SUBJECT_SPONSOR_KEY | iap subject sponsor key / Subject Sponsor Key / IAP Sponsor Key / Sponsor ID / Sponsor Key / IAP Sponsor ID | varchar(127) | dw_4245, dw_4313, dw_2985, dw_3518 |
| IAP_SUBJECT_DETAIL.IAP_SUBJECT_SESSION_KEY | iap subject session key / Subject Session Key / IAP Session Key / Session ID / IAP Session ID / Subject Session ID | varchar(127) | dw_5095, dw_4075, dw_3486, dw_3518 |
| IAP_SUBJECT_DETAIL.IAP_SUBJECT_PERSON_KEY | iap subject person key / Subject Person Key / IAP Person Key / Person ID / IAP Person ID / Subject Person ID | varchar(127) | dw_2742 |
| IAP_SUBJECT_DETAIL.ACTIVITY_TITLE | activity title / IAP Title / Subject Title / Course Title / Event Title / IAP Activity Name | varchar(127) | dw_4245, dw_3047, dw_4229, dw_2790, dw_2858, dw_4313, dw_4075, dw_2985 |
| IAP_SUBJECT_DETAIL.ACTIVITY_DESCRIPTION | activity description / IAP Description / Subject Description / Course Description / Event Description | varchar(127) | dw_4229 |
| IAP_SUBJECT_DETAIL.TERM_CODE | term code / Academic Term Code / Term ID / IAP Term Code / Academic Period Code | varchar(127) | dw_4245, dw_5095, dw_3047, dw_4229, dw_2790, dw_2858, dw_2742, dw_4313 |
| IAP_SUBJECT_DETAIL.ENROLLMENT_TYPE | enrollment type / Sign-up Type / Registration Type / IAP Enrollment Type / Enrollment Method | varchar(127) | dw_4245, dw_3047, dw_4229, dw_2790, dw_2858, dw_4313, dw_4075, dw_2985 |
| IAP_SUBJECT_DETAIL.MAX_ENROLLMENT | max enrollment / maximum enrollment / Capacity / Enrollment Limit / Max Capacity / IAP Capacity | int | dw_4245, dw_5095, dw_3047, dw_4229, dw_2790, dw_2858, dw_2742, dw_4313 |
| IAP_SUBJECT_DETAIL.ATTENDANCE | attendance / Attendance Policy / Attendance Requirement / Attendance Rule / IAP Attendance / Session Attendance | varchar(127) | schema / IAP_SUBJECT_DETAIL |
| IAP_SUBJECT_DETAIL.PREREQUISITES | prerequisites / Prereqs / Required Background / IAP Prerequisites / Pre-requirements | varchar(127) | dw_2858 |
| IAP_SUBJECT_DETAIL.FEE | fee / Cost / Price / IAP Fee / Activity Cost / Tuition | int | dw_4245, dw_4313, dw_2985, dw_3518 |
| IAP_SUBJECT_DETAIL.FEE_REASON | fee reason / Cost Reason / Fee Justification / IAP Fee Reason / Reason for Fee | varchar(127) | schema / IAP_SUBJECT_DETAIL |
| IAP_SUBJECT_DETAIL.PREREG_DEADLINE | prereg deadline / Pre-registration Deadline / Sign-up Deadline / Registration Deadline / IAP Prereg Deadline | varchar(255) | dw_5095 |
| IAP_SUBJECT_DETAIL.CREATE_DATE | create date / Creation Date / Record Created / IAP Create Date / Entry Date | varchar(255) | dw_2790 |
| IAP_SUBJECT_DETAIL.LAST_ACTIVITY_DATE | last activity date / Last Updated / Last Modified / IAP Last Activity / Activity Date | varchar(255) | schema / IAP_SUBJECT_DETAIL |
| IAP_SUBJECT_DETAIL.IS_MULTIPLE_SESSION | is multiple session / Multiple Sessions / Multi-session Flag / IAP Multi-session / Session Count Flag | varchar(127) | dw_3047 |
| IAP_SUBJECT_DETAIL.IS_CANCELLED | is cancelled / Cancelled Flag / Cancellation Status / IAP Cancelled / Active Status | varchar(127) | dw_4245, dw_3047, dw_2742, dw_4313, dw_4075, dw_3486 |
| IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE | warehouse load date / ETL Date / Data Load Date / IAP Load Date / System Load Date | varchar(255) | schema / IAP_SUBJECT_DETAIL |

## IAP_SUBJECT_PERSON

Stores information about individuals (leaders, staff, students) associated with Independent Activities Period (IAP) subjects, including their roles, affiliations, and contact details.

恢复表名: iap subject person / IAP Person / IAP Activity Person / IAP Leader / IAP Staff / Independent Activities Period Person
SQL表别名: p

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| IAP_SUBJECT_PERSON.IAP_SUBJECT_PERSON_KEY | iap subject person key / Person Key / IAP Person ID / Subject Person Key / Person Identifier / IAP Subject Person ID | varchar(127) | dw_2737, dw_2742, dw_2791, dw_2823, dw_3796, dw_3998, dw_4677 |
| IAP_SUBJECT_PERSON.PERSON_ROLE | person role / Role / Activity Role / Leader Type / Staff Role / Position in Activity | varchar(127) | dw_2737, dw_2742, dw_2791, dw_2823, dw_3796, dw_3998, dw_4677 |
| IAP_SUBJECT_PERSON.PERSON_MIT_AFFILIATION | person mit affiliation / MIT Affiliation / Affiliation / MIT Status / Academic Affiliation / Person Affiliation / MIT Relationship | varchar(127) | schema / IAP_SUBJECT_PERSON |
| IAP_SUBJECT_PERSON.PERSON_NAME | person name / Name / Full Name / Leader Name / Staff Name / Individual Name | varchar(127) | schema / IAP_SUBJECT_PERSON |
| IAP_SUBJECT_PERSON.PERSON_LOCATION | person location / Location / Address / Physical Location / Site | varchar(127) | schema / IAP_SUBJECT_PERSON |
| IAP_SUBJECT_PERSON.PERSON_EMAIL | person email / Email / Email Address / Contact Email / E-mail | varchar(127) | schema / IAP_SUBJECT_PERSON |
| IAP_SUBJECT_PERSON.PERSON_ORGANIZATION | person organization / Organization / Department / Affiliated Organization / Institution | varchar(127) | schema / IAP_SUBJECT_PERSON |
| IAP_SUBJECT_PERSON.PERSON_TITLE | person title / Title / Job Title / Professional Title / Position Title | varchar(127) | schema / IAP_SUBJECT_PERSON |
| IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / ETL Date / Data Load Date / Last Updated | varchar(255) | schema / IAP_SUBJECT_PERSON |

## IAP_SUBJECT_SESSION

Stores detailed scheduling information for individual sessions of IAP (Independent Activities Period) subjects, including titles, descriptions, locations, dates, and times.

恢复表名: iap subject session / IAP Session / Independent Activities Period Session / Session Details / IAP Schedule
SQL表别名: iss, s

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| IAP_SUBJECT_SESSION.IAP_SUBJECT_SESSION_KEY | iap subject session key / Session Key / Session ID / IAP Session Identifier / Subject Session Key | varchar(127) | dw_3486, dw_4682, dw_4880 |
| IAP_SUBJECT_SESSION.SESSION_SEQUENCE | session sequence / Session Number / Session Order / Sequence Number / Session Index | int | schema / IAP_SUBJECT_SESSION |
| IAP_SUBJECT_SESSION.SESSION_TITLE | session title / Session Name / Session Heading / Module Title / Session Label | varchar(127) | dw_3486, dw_4682, dw_4880 |
| IAP_SUBJECT_SESSION.SESSION_DESCRIPTION | session description / Session Details / Session Summary / Module Description / Session Content | varchar(127) | schema / IAP_SUBJECT_SESSION |
| IAP_SUBJECT_SESSION.SESSION_LOCATION | session location / Session Venue / Meeting Place / Location / Session Site | varchar(127) | dw_3486, dw_4682, dw_4880 |
| IAP_SUBJECT_SESSION.SESSION_DATE | session date / Session Day / Date of Session / Meeting Date / Session Calendar Date | varchar(255) | dw_3486, dw_4682, dw_4880 |
| IAP_SUBJECT_SESSION.SESSION_START_TIME | session start time / Start Time / Session Begin Time / Meeting Start / Session Opening Time | varchar(127) | dw_3486, dw_4682, dw_4880 |
| IAP_SUBJECT_SESSION.SESSION_END_TIME | session end time / End Time / Session Finish Time / Meeting End / Session Closing Time | varchar(127) | dw_3486, dw_4682, dw_4880 |
| IAP_SUBJECT_SESSION.HAS_SESSION_INFO | has session info / Has Info Flag / Session Info Available / Info Present / Detail Flag | varchar(127) | schema / IAP_SUBJECT_SESSION |
| IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / ETL Date / Data Load Timestamp / Warehouse Update Date | varchar(255) | schema / IAP_SUBJECT_SESSION |

## IAP_SUBJECT_SPONSOR

Reference table containing details about sponsors (departments, centers, student groups) for Independent Activities Period (IAP) subjects.

恢复表名: iap subject sponsor / IAP Sponsor / Independent Activities Period Sponsor / Sponsor Reference / IAP Sponsor Reference
SQL表别名: iss, s, sp

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| IAP_SUBJECT_SPONSOR.IAP_SUBJECT_SPONSOR_KEY | iap subject sponsor key / Sponsor Key / IAP Sponsor Key / Sponsor ID / Subject Sponsor Key / Sponsor Identifier | varchar(127) | dw_2642, dw_2671, dw_2814, dw_3180, dw_3934, dw_4014, dw_4091, dw_4345 |
| IAP_SUBJECT_SPONSOR.SPONSOR_NAME | sponsor name / Department Name / Sponsoring Department / Sponsoring Group / Sponsoring Center / Sponsor Title | varchar(127) | dw_2642, dw_2671, dw_2814, dw_3180, dw_3934, dw_4014, dw_4091, dw_4345 |
| IAP_SUBJECT_SPONSOR.SPONSOR_TYPE | sponsor type / Sponsor Category / Sponsor Class / Type of Sponsor / Sponsor Group Type | varchar(127) | dw_2642, dw_2671, dw_2814, dw_3180, dw_3934, dw_4014, dw_4091, dw_4345 |
| IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / ETL Date / Data Load Date / Last Updated | varchar(255) | schema / IAP_SUBJECT_SPONSOR |

## IR_INSTITUTION

Stores detailed information about educational institutions, including names, addresses, locations, and Carnegie classification categories.

恢复表名: ir institution / Institution / Institutions / College / Colleges / University / Universities / School
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| IR_INSTITUTION.INSTITUTION_ID | institution id / institution identifier / School ID / College ID / University ID / Institution Number | varchar(127) | schema / IR_INSTITUTION |
| IR_INSTITUTION.INSTITUTION_NAME | institution name / School Name / College Name / University Name / Official Name / Primary Name | varchar(127) | schema / IR_INSTITUTION |
| IR_INSTITUTION.ALTERNATE_INSTITUTION_NAME | alternate institution name / Alternate Name / Alternative Name / Common Name / Short Name / Branch Name / Secondary Name | varchar(127) | schema / IR_INSTITUTION |
| IR_INSTITUTION.STREET_ADDRESS | street address / Address / Mailing Address / Physical Address / Location Address | varchar(127) | schema / IR_INSTITUTION |
| IR_INSTITUTION.CITY | city / Town / Municipality / Location City | varchar(127) | schema / IR_INSTITUTION |
| IR_INSTITUTION.ZIP | zip / Zip Code / Postal Code / Postcode | varchar(127) | schema / IR_INSTITUTION |
| IR_INSTITUTION.STATE | state / State Code / Province / Region / State Abbreviation | varchar(127) | schema / IR_INSTITUTION |
| IR_INSTITUTION.COUNTRY_CODE | country code / ISO Country Code / Nation Code | varchar(127) | schema / IR_INSTITUTION |
| IR_INSTITUTION.COUNTRY | country / Nation / Country Name | varchar(127) | schema / IR_INSTITUTION |
| IR_INSTITUTION.INSTITUTION_CATEGORY_VALUE | institution category value / Category Value / Institution Type Code / Carnegie Code / Classification Code / Category ID | int | schema / IR_INSTITUTION |
| IR_INSTITUTION.INSTITUTION_CATEGORY_LABEL | institution category label / Category Label / Institution Type / Carnegie Classification / Classification Label / Institution Category / Type of Institution | varchar(127) | schema / IR_INSTITUTION |
| IR_INSTITUTION.INSTITUTION_SORT_ORDER | institution sort order / Sort Order / Sort Key / Display Order / Sequence Number | varchar(127) | schema / IR_INSTITUTION |
| IR_INSTITUTION.RECORD_CREATED_DATE | record created date / Created Date / Record Creation Date / Insert Date / Date Added / Creation Timestamp | varchar(255) | schema / IR_INSTITUTION |

## LIBRARY_COURSE_INSTRUCTOR

Maps specific library reserve course offerings to their instructors, departments, and physical locations (units/buildings) for a given date range, serving as a bridge between library material details and academic course metadata.

恢复表名: library course instructor / Course Instructor Mapping / Library Reserve Course Details / Instructor Course Assignment / Library Course Offerings
SQL表别名: ci, i, lci, t0

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| LIBRARY_COURSE_INSTRUCTOR.LIBRARY_COURSE_INSTRUCTOR_KEY | library course instructor key / Course Instructor Key / Library Course ID / Reserve Course Key / Primary Key / Identifier | varchar(127) | dw_2850, dw_3382, dw_3401, dw_3442, dw_3554, dw_3675, dw_3696, dw_3757 |
| LIBRARY_COURSE_INSTRUCTOR.COURSE_NAME | course name / Course Title / Subject Name / Class Name / Course Description / Offering Name | varchar(127) | dw_2590 |
| LIBRARY_COURSE_INSTRUCTOR.INSTRUCTOR_NAME | instructor name / Professor Name / Teacher Name / Faculty Name / Instructor / Staff Name | varchar(127) | dw_2590 |
| LIBRARY_COURSE_INSTRUCTOR.DEPARTMENT | department / Department Name / Academic Department / School / Division / Dept | varchar(127) | dw_2590, dw_2850, dw_3382, dw_3401, dw_3442, dw_3554, dw_3675, dw_3696 |
| LIBRARY_COURSE_INSTRUCTOR.DATE_FROM | date from / Start Date / Course Start / Effective From / Begin Date / First Day | varchar(255) | schema / LIBRARY_COURSE_INSTRUCTOR |
| LIBRARY_COURSE_INSTRUCTOR.DATE_TO | date to / End Date / Course End / Effective To / Finish Date / Last Day | varchar(255) | schema / LIBRARY_COURSE_INSTRUCTOR |
| LIBRARY_COURSE_INSTRUCTOR.UNIT_CODE | unit code / Building Code / Location Code / Unit Abbreviation / Short Unit Name / Code | varchar(127) | schema / LIBRARY_COURSE_INSTRUCTOR |
| LIBRARY_COURSE_INSTRUCTOR.UNIT | unit / Building Name / Location / Unit Name / Physical Location / Room Building | varchar(127) | dw_2590 |
| LIBRARY_COURSE_INSTRUCTOR.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / ETL Date / Data Load Timestamp / Insert Date / System Update Date | varchar(255) | schema / LIBRARY_COURSE_INSTRUCTOR |

## LIBRARY_MATERIAL_STATUS

Lookup table defining the status of library materials, such as whether they are required course materials, reserve only, or non-required, used to categorize reserve catalog items.

恢复表名: library material status / Library Material Status Lookup / Library Material Status Reference / Material Status / Library Status
SQL表别名: lms, m, s

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| LIBRARY_MATERIAL_STATUS.LIBRARY_MATERIAL_STATUS_KEY | library material status key / Status Key / Material Status ID / Library Status Key / Status Identifier | varchar(127) | dw_2705, dw_2748, dw_3234, dw_3505, dw_3587, dw_3637, dw_4251 |
| LIBRARY_MATERIAL_STATUS.LIBRARY_MATERIAL_STATUS_CODE | library material status code / Status Code / Material Status Code / Library Status Code / Status Abbreviation | varchar(127) | schema / LIBRARY_MATERIAL_STATUS |
| LIBRARY_MATERIAL_STATUS.LIBRARY_MATERIAL_STATUS | library material status / Material Status / Status Description / Library Status / Material Status Name / Status Label | varchar(127) | dw_2705, dw_2748, dw_3234, dw_3505, dw_3587, dw_3637, dw_4251 |
| LIBRARY_MATERIAL_STATUS.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date / Refresh Date | varchar(255) | schema / LIBRARY_MATERIAL_STATUS |

## LIBRARY_RESERVE_CATALOG

Stores bibliographic metadata and system identifiers for items in the library reserve catalog, linking to material details via the catalog key.

恢复表名: library reserve catalog / reserve catalog / library catalog / reserve materials catalog / catalog items / library holdings
SQL表别名: c, lrc, rc

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| LIBRARY_RESERVE_CATALOG.LIBRARY_RESERVE_CATALOG_KEY | library reserve catalog key / catalog key / reserve catalog key / item key / catalog id / primary key | varchar(127) | dw_4583, dw_2720, dw_2760, dw_3857, dw_3980 |
| LIBRARY_RESERVE_CATALOG.CATALOG_TITLE | catalog title / title / book title / item title / work title / name | varchar(127) | dw_4583 |
| LIBRARY_RESERVE_CATALOG.CATALOG_AUTHOR_NAME | catalog author name / author / author name / catalog author / creator / writer / artist | varchar(127) | dw_4583 |
| LIBRARY_RESERVE_CATALOG.CATALOG_YEAR | catalog year / year / publication year / publish year / release year / date published | varchar(127) | dw_4583, dw_2720, dw_2760, dw_3857, dw_3980 |
| LIBRARY_RESERVE_CATALOG.CATALOG_PUBLISHER | catalog publisher / publisher / publishing house / imprint / producer | varchar(127) | schema / LIBRARY_RESERVE_CATALOG |
| LIBRARY_RESERVE_CATALOG.CATALOG_CALL_NUMBER | catalog call number / call number / shelf number / location code / classification number | varchar(127) | schema / LIBRARY_RESERVE_CATALOG |
| LIBRARY_RESERVE_CATALOG.CATALOG_ISBN | catalog isbn / isbn / international standard book number / book id / isbn number | varchar(127) | schema / LIBRARY_RESERVE_CATALOG |
| LIBRARY_RESERVE_CATALOG.CATALOG_SYSTEM_NUMBER | catalog system number / system number / accession number / control number / internal id | varchar(127) | schema / LIBRARY_RESERVE_CATALOG |
| LIBRARY_RESERVE_CATALOG.CATALOG_RECORD_CREATE_DATE | catalog record create date / create date / record create date / creation date / date created / insert date | varchar(255) | schema / LIBRARY_RESERVE_CATALOG |
| LIBRARY_RESERVE_CATALOG.CATALOG_RECORD_UPDATE_DATE | catalog record update date / update date / record update date / last modified date / date updated / modification date | varchar(255) | schema / LIBRARY_RESERVE_CATALOG |
| LIBRARY_RESERVE_CATALOG.RECORD_COUNTER | record counter / counter / record count / item count / quantity / number of records | int | dw_4583, dw_2720, dw_2760, dw_3857, dw_3980 |
| LIBRARY_RESERVE_CATALOG.WAREHOUSE_LOAD_DATE | warehouse load date / load date / etl date / data load date / ingestion date | varchar(255) | schema / LIBRARY_RESERVE_CATALOG |

## LIBRARY_RESERVE_MATRL_DETAIL

Stores detailed records of library reserve materials associated with specific course offerings, instructors, and academic terms, including material status and catalog references.

恢复表名: library reserve matrl detail / library reserve material detail / library reserve materials / reserve material details / library reserve catalog details / course reserve materials
SQL表别名: d, l, lrd, lrm, lrmd, md, t0, t2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| LIBRARY_RESERVE_MATRL_DETAIL.LIBRARY_COURSE_INSTRUCTOR_KEY | library course instructor key / course instructor key / instructor key / library course instructor / faculty key / instructor identifier | varchar(127) | dw_2769, dw_4347, dw_2730, dw_2733, dw_2997, dw_3101, dw_3211, dw_3240 |
| LIBRARY_RESERVE_MATRL_DETAIL.LIBRARY_RESERVE_CATALOG_KEY | library reserve catalog key / reserve catalog key / catalog key / library reserve catalog / material catalog id / reserve item key | varchar(127) | dw_2769, dw_4347, dw_2730, dw_2733, dw_2997, dw_3101, dw_3211, dw_3240 |
| LIBRARY_RESERVE_MATRL_DETAIL.LIBRARY_SUBJECT_OFFERED_KEY | library subject offered key / subject offered key / library subject offered / course offering key / subject key / offering identifier | varchar(127) | dw_2769, dw_4347 |
| LIBRARY_RESERVE_MATRL_DETAIL.LIBRARY_MATERIAL_STATUS_KEY | library material status key / material status key / library material status / status key / reserve status / material availability status | varchar(127) | dw_2769, dw_2895, dw_4347, dw_2730, dw_2733, dw_2997, dw_3101, dw_3211 |
| LIBRARY_RESERVE_MATRL_DETAIL.TERM_CODE | term code / academic term / semester code / term identifier / academic period | varchar(127) | dw_2769, dw_4347, dw_2730, dw_2733, dw_2997, dw_3101, dw_3211, dw_3240 |
| LIBRARY_RESERVE_MATRL_DETAIL.SUBJECT_ID | subject id / subject identifier / course id / course number / subject code | varchar(127) | dw_2769, dw_2895, dw_4347, dw_2730, dw_2733, dw_2997, dw_3101, dw_3211 |
| LIBRARY_RESERVE_MATRL_DETAIL.WAREHOUSE_LOAD_DATE | warehouse load date / load date / data load date / etl date / record update date | varchar(255) | dw_2895 |

## LIBRARY_SUBJECT_OFFERED

Stores detailed information about subjects (courses) offered in the library system, including term, department, faculty, enrollment counts, and subject identifiers for each offering.

恢复表名: library subject offered / Library Course Offerings / Library Subject Catalog / Library Reserve Subject Details / Library Course Enrollment
SQL表别名: l, l2, lso, lso2, s, so, t0, t1, t2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| LIBRARY_SUBJECT_OFFERED.LIBRARY_SUBJECT_OFFERED_KEY | library subject offered key / Library Subject Key / Subject Offered Key / Library Course Key / Unique Subject ID / Library Offering ID | varchar(127) | dw_4449 |
| LIBRARY_SUBJECT_OFFERED.TERM_CODE | term code / Academic Term / Semester Code / Term Identifier / Academic Period | varchar(127) | dw_4449, dw_1519, dw_4716, dw_2346, dw_2960, dw_3238, dw_3463, dw_3602 |
| LIBRARY_SUBJECT_OFFERED.MASTER_COURSE_NUMBER | master course number / Course Number / Department Number / Course ID / Master Course ID | varchar(127) | schema / LIBRARY_SUBJECT_OFFERED |
| LIBRARY_SUBJECT_OFFERED.MASTER_COURSE_NUMBER_SORT | master course number sort / Master Course Sort / Sorted Master Course Number / Course Number Sort Key / Master Course Sort Key | varchar(127) | schema / LIBRARY_SUBJECT_OFFERED |
| LIBRARY_SUBJECT_OFFERED.MASTER_COURSE_NUMBER_DESC | master course number desc / master course number description / Master Course Description / Course Name / Department Name / Master Course Title / Course Description | varchar(127) | schema / LIBRARY_SUBJECT_OFFERED |
| LIBRARY_SUBJECT_OFFERED.MASTER_SUBJECT_ID | master subject id / master subject identifier / Subject ID / Course Subject ID / Subject Code | varchar(127) | dw_1519 |
| LIBRARY_SUBJECT_OFFERED.MASTER_SUBJECT_ID_SORT | master subject id sort / master subject identifier sort / Master Subject Sort / Sorted Master Subject ID / Subject ID Sort Key / Master Subject Sort Key | varchar(127) | dw_1288 |
| LIBRARY_SUBJECT_OFFERED.COURSE_NUMBER | course number / Course ID / Department Number / Course Code / Course Identifier | varchar(127) | dw_4449, dw_1519, dw_4716, dw_2346, dw_3463, dw_3688, dw_3743, dw_3875 |
| LIBRARY_SUBJECT_OFFERED.COURSE_NUMBER_SORT | course number sort / Course Sort / Sorted Course Number / Course Number Sort Key / Course Sort Key | varchar(127) | schema / LIBRARY_SUBJECT_OFFERED |
| LIBRARY_SUBJECT_OFFERED.COURSE_NUMBER_DESC | course number desc / course number description / Course Description / Course Name / Department Name / Course Title / Course Description Text | varchar(127) | dw_4716 |
| LIBRARY_SUBJECT_OFFERED.SUBJECT_ID | subject id / subject identifier / Course Subject ID / Subject Code / Unique Subject ID | varchar(127) | dw_4449, dw_4716, dw_2960, dw_3238, dw_3463, dw_3602, dw_3688, dw_3743 |
| LIBRARY_SUBJECT_OFFERED.SUBJECT_ID_SORT | subject id sort / subject identifier sort / Subject Sort / Sorted Subject ID / Subject ID Sort Key / Subject Sort Key | varchar(127) | schema / LIBRARY_SUBJECT_OFFERED |
| LIBRARY_SUBJECT_OFFERED.SUBJECT_TITLE | subject title / Course Title / Subject Name / Course Name / Subject Description | varchar(127) | dw_4449, dw_1519, dw_2346, dw_2960, dw_3238, dw_3463, dw_3602, dw_3688 |
| LIBRARY_SUBJECT_OFFERED.OFFER_DEPT_CODE | offer dept code / offer department code / Offering Department Code / Department Code / Dept Code / Offering Dept ID / Department Identifier | varchar(127) | dw_1288, dw_2346, dw_2960, dw_3238 |
| LIBRARY_SUBJECT_OFFERED.OFFER_DEPT_NAME | offer dept name / offer department name / Offering Department Name / Department Name / Dept Name / Offering Dept / Department | varchar(127) | dw_4449, dw_1288, dw_4716, dw_2346, dw_2960, dw_3238, dw_3463, dw_3602 |
| LIBRARY_SUBJECT_OFFERED.OFFER_SCHOOL_NAME | offer school name / Offering School Name / School Name / School / Offering School / Academic School | varchar(127) | dw_4449, dw_3602 |
| LIBRARY_SUBJECT_OFFERED.RESPONSIBLE_FACULTY_NAME | responsible faculty name / Faculty Name / Instructor Name / Professor Name / Responsible Instructor | varchar(127) | dw_4449, dw_1519, dw_1288, dw_2346, dw_2960, dw_3238, dw_3463, dw_3602 |
| LIBRARY_SUBJECT_OFFERED.RESPONSIBLE_FACULTY_MIT_ID | responsible faculty mit id / responsible faculty mit identifier / Faculty MIT ID / Instructor MIT ID / Professor ID / Faculty Identifier | varchar(127) | dw_1519 |
| LIBRARY_SUBJECT_OFFERED.NUM_ENROLLED_STUDENTS | num enrolled students / number enrolled students / Number of Enrolled Students / Enrollment Count / Enrolled Students / Student Count / Enrollment Number | int | dw_4449, dw_1519, dw_1288, dw_4716, dw_2346, dw_2960, dw_3238, dw_3463 |
| LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date / Last Updated Date | varchar(255) | schema / LIBRARY_SUBJECT_OFFERED |

## MASTER_DEPT_DCODE_PARENT

Maps each department to its parent department in the organizational hierarchy, providing department IDs, codes, and names for both the child and parent entities.

恢复表名: master dept dcode parent / master department dcode parent / Department Hierarchy / Department Parent Mapping / Dept Code Parent / Organizational Structure / Department Tree / Dept Hierarchy
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| MASTER_DEPT_DCODE_PARENT.DEPT_ID | dept id / department identifier / Department ID / Child Department ID / Dept Number | int | schema / MASTER_DEPT_DCODE_PARENT |
| MASTER_DEPT_DCODE_PARENT.D_CODE | d code / Department Code / Dept Code / Child Department Code / Department Abbreviation | varchar(127) | schema / MASTER_DEPT_DCODE_PARENT |
| MASTER_DEPT_DCODE_PARENT.D_NAME | d name / Department Name / Dept Name / Child Department Name / Department Title / Full Department Name | varchar(127) | schema / MASTER_DEPT_DCODE_PARENT |
| MASTER_DEPT_DCODE_PARENT.PARENT_ID | parent id / parent identifier / Parent Department ID / Superior Department ID / Reporting Department ID / Parent Dept ID | int | schema / MASTER_DEPT_DCODE_PARENT |
| MASTER_DEPT_DCODE_PARENT.PARENT_D_CODE | parent d code / Parent Department Code / Parent Code / Superior Department Code / Reporting Department Code | varchar(127) | schema / MASTER_DEPT_DCODE_PARENT |
| MASTER_DEPT_DCODE_PARENT.PARENT_D_NAME | parent d name / Parent Department Name / Parent Name / Superior Department Name / Reporting Department Name / Parent Dept Name | varchar(127) | schema / MASTER_DEPT_DCODE_PARENT |
| MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date / Last Updated | varchar(255) | schema / MASTER_DEPT_DCODE_PARENT |

## MASTER_DEPT_HIERARCHY

Defines the multi-level organizational hierarchy for departments, mapping department codes (DLC) to their respective levels (1-5) and names, used to filter and categorize departments by area (e.g., Provost Area, Finance Area).

恢复表名: master dept hierarchy / master department hierarchy / Department Hierarchy / Dept Hierarchy / Department Structure / Org Hierarchy / Departmental Hierarchy
SQL表别名: m, m2, mdh, t0

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| MASTER_DEPT_HIERARCHY.HIERARCHY_TYPE | hierarchy type / Type of Hierarchy / Hierarchy Category / Standard Hierarchy Flag | varchar(127) | dw_4373, dw_3235, dw_3653, dw_4638 |
| MASTER_DEPT_HIERARCHY.DLC_KEY | dlc key / Department Key / Department Code Key / Dept Key / Department Identifier | varchar(127) | dw_4373, dw_1465, dw_184, dw_2677, dw_3046, dw_3235, dw_3653, dw_3697 |
| MASTER_DEPT_HIERARCHY.DLC_CODE | dlc code / Department Code / Dept Code / Department Identifier Code | varchar(127) | dw_1465, dw_184, dw_3046, dw_4008, dw_4269 |
| MASTER_DEPT_HIERARCHY.DLC_NAME | dlc name / Department Name / Dept Name / Department Title | varchar(127) | dw_4373, dw_1465, dw_184, dw_2677, dw_3046, dw_3235, dw_3653, dw_3697 |
| MASTER_DEPT_HIERARCHY.MASTER_DEPT_HIER_LEVEL_1_CODE | master dept hier level 1 code / master department hier level 1 code / Level 1 Code / Hierarchy Level 1 Code / Top Level Code / Root Department Code | varchar(127) | schema / MASTER_DEPT_HIERARCHY |
| MASTER_DEPT_HIERARCHY.MASTER_DEPT_HIER_LEVEL_1_NAME | master dept hier level 1 name / master department hier level 1 name / Level 1 Name / Hierarchy Level 1 Name / Top Level Name / Root Department Name | varchar(127) | schema / MASTER_DEPT_HIERARCHY |
| MASTER_DEPT_HIERARCHY.MASTER_DEPT_HIER_LEVEL_2_CODE | master dept hier level 2 code / master department hier level 2 code / Level 2 Code / Hierarchy Level 2 Code / Second Level Code / Area Code | varchar(127) | schema / MASTER_DEPT_HIERARCHY |
| MASTER_DEPT_HIERARCHY.MASTER_DEPT_HIER_LEVEL_2_NAME | master dept hier level 2 name / master department hier level 2 name / Level 2 Name / Hierarchy Level 2 Name / Second Level Name / Area Name / Department Area | varchar(127) | dw_4373, dw_1465, dw_184, dw_2677, dw_3046, dw_3235, dw_3653, dw_3697 |
| MASTER_DEPT_HIERARCHY.MASTER_DEPT_HIER_LEVEL_3_CODE | master dept hier level 3 code / master department hier level 3 code / Level 3 Code / Hierarchy Level 3 Code / Third Level Code / School Code | varchar(127) | dw_4373, dw_2677, dw_3046, dw_3235, dw_3653, dw_3697, dw_4008, dw_4269 |
| MASTER_DEPT_HIERARCHY.MASTER_DEPT_HIER_LEVEL_3_NAME | master dept hier level 3 name / master department hier level 3 name / Level 3 Name / Hierarchy Level 3 Name / Third Level Name / School Name / Department Division | varchar(127) | dw_4373, dw_1465, dw_184, dw_2677, dw_3697, dw_4335 |
| MASTER_DEPT_HIERARCHY.MASTER_DEPT_HIER_LEVEL_4_CODE | master dept hier level 4 code / master department hier level 4 code / Level 4 Code / Hierarchy Level 4 Code / Fourth Level Code / Sub-Area Code | varchar(127) | schema / MASTER_DEPT_HIERARCHY |
| MASTER_DEPT_HIERARCHY.MASTER_DEPT_HIER_LEVEL_4_NAME | master dept hier level 4 name / master department hier level 4 name / Level 4 Name / Hierarchy Level 4 Name / Fourth Level Name / Sub-Area Name | varchar(127) | schema / MASTER_DEPT_HIERARCHY |
| MASTER_DEPT_HIERARCHY.MASTER_DEPT_HIER_LEVEL_5_CODE | master dept hier level 5 code / master department hier level 5 code / Level 5 Code / Hierarchy Level 5 Code / Fifth Level Code / Unit Code | varchar(127) | schema / MASTER_DEPT_HIERARCHY |
| MASTER_DEPT_HIERARCHY.MASTER_DEPT_HIER_LEVEL_5_NAME | master dept hier level 5 name / master department hier level 5 name / Level 5 Name / Hierarchy Level 5 Name / Fifth Level Name / Unit Name | varchar(127) | schema / MASTER_DEPT_HIERARCHY |

## MASTER_DEPT_HIERARCHY_LINKS

Stores the mapping and linkage between different departmental or organizational hierarchy types (such as Funds Centers, Student Systems Units, and Profit Centers) to support cross-hierarchy reporting and navigation.

恢复表名: master dept hierarchy links / master department hierarchy links / Department Hierarchy Links / Dept Hierarchy / Master Department Hierarchy / Org Hierarchy Links / Department Structure Links / Hierarchy Mapping
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| MASTER_DEPT_HIERARCHY_LINKS.HIERARCHY_TYPE | hierarchy type / Type of Hierarchy / Hierarchy Category / Standard Hierarchy | varchar(127) | schema / MASTER_DEPT_HIERARCHY_LINKS |
| MASTER_DEPT_HIERARCHY_LINKS.LINK_TYPE_CODE | link type code / Hierarchy Link Code / Link Code / Type Code / FC Code / SIS Code | varchar(127) | schema / MASTER_DEPT_HIERARCHY_LINKS |
| MASTER_DEPT_HIERARCHY_LINKS.LINK_TYPE | link type / Hierarchy Link Name / Link Description / Type Name / Funds Center Type / Student Systems Unit Type | varchar(127) | schema / MASTER_DEPT_HIERARCHY_LINKS |
| MASTER_DEPT_HIERARCHY_LINKS.DLC_KEY | dlc key / Department Link Key / Hierarchy Key / DLC Identifier / Department Code Key | varchar(127) | schema / MASTER_DEPT_HIERARCHY_LINKS |
| MASTER_DEPT_HIERARCHY_LINKS.DLC_CODE | dlc code / Department Link Code / Department Code / Org Code / Unit Code | varchar(127) | schema / MASTER_DEPT_HIERARCHY_LINKS |
| MASTER_DEPT_HIERARCHY_LINKS.LINKED_OBJECT_KEY | linked object key / Object Key / Linked Department Key / Target Key / Funds Center Key | varchar(127) | schema / MASTER_DEPT_HIERARCHY_LINKS |
| MASTER_DEPT_HIERARCHY_LINKS.LINKED_OBJECT_CODE | linked object code / Object Code / Linked Department Code / Target Code / Funds Center Code | varchar(127) | schema / MASTER_DEPT_HIERARCHY_LINKS |

## MIT_HOLIDAY_CLOSING_CALENDAR

Stores the official calendar of holidays and closure dates for MIT, including the specific date, description, and type of each holiday.

恢复表名: mit holiday closing calendar / MIT Holiday Calendar / MIT Closing Calendar / MIT Holidays / MIT Closure Dates / MIT Holiday Schedule / MIT Institutional Holidays
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| MIT_HOLIDAY_CLOSING_CALENDAR.HOLIDAY_CLOSING_DATE | holiday closing date / Holiday Date / Closing Date / Date of Holiday / Closure Date / MIT Holiday Date / Day of Closure | varchar(255) | schema / MIT_HOLIDAY_CLOSING_CALENDAR |
| MIT_HOLIDAY_CLOSING_CALENDAR.HOLIDAY_CLOSING_DESCRIPTION | holiday closing description / Holiday Name / Holiday Description / Closure Description / Name of Holiday / MIT Holiday Name / Holiday Title | varchar(127) | schema / MIT_HOLIDAY_CLOSING_CALENDAR |
| MIT_HOLIDAY_CLOSING_CALENDAR.HOLIDAY_CLOSING_TYPE | holiday closing type / Holiday Type / Closure Type / Type of Holiday / Category of Closure / MIT Holiday Category / Holiday Classification | varchar(127) | schema / MIT_HOLIDAY_CLOSING_CALENDAR |
| MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date / Warehouse Date / Last Updated Date / System Load Date | varchar(255) | schema / MIT_HOLIDAY_CLOSING_CALENDAR |

## MIT_STUDENT_DIRECTORY

A directory table containing contact information, departmental affiliation, and academic year details for MIT students, used for lookups and joins with department and person tables.

恢复表名: mit student directory / Student Directory / MIT Students / Student Roster / MIT Student List / Directory of MIT Students
SQL表别名: m, msd, s, t1, t2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| MIT_STUDENT_DIRECTORY.FIRST_NAME | first name / Student First Name / Given Name / First Name of Student / Student Given Name | varchar(127) | dw_1082, dw_1330, dw_1350, dw_1366, dw_1368, dw_1402, dw_1474, dw_1477 |
| MIT_STUDENT_DIRECTORY.MIDDLE_NAME | middle name / Student Middle Name / Middle Initial / Middle Name of Student | varchar(127) | schema / MIT_STUDENT_DIRECTORY |
| MIT_STUDENT_DIRECTORY.LAST_NAME | last name / Student Last Name / Surname / Family Name / Last Name of Student | varchar(127) | dw_1082, dw_1330, dw_1350, dw_1366, dw_1368, dw_1402, dw_1474, dw_1477 |
| MIT_STUDENT_DIRECTORY.FULL_NAME | full name / Student Full Name / Complete Name / Name / Student Name | varchar(127) | dw_1082, dw_4113, dw_2666, dw_1330, dw_1350, dw_1366, dw_1368, dw_1402 |
| MIT_STUDENT_DIRECTORY.OFFICE_LOCATION | office location / Office Room / Room Number / Student Office / Office Address | varchar(127) | dw_4113, dw_2666 |
| MIT_STUDENT_DIRECTORY.OFFICE_PHONE | office phone / Phone Number / Student Phone / Contact Number / Office Telephone | varchar(127) | dw_4113 |
| MIT_STUDENT_DIRECTORY.EMAIL_ADDRESS | email address / Email / Student Email / Electronic Mail / Contact Email | varchar(127) | dw_1082, dw_1330, dw_1350, dw_1366, dw_1368, dw_1402, dw_1474, dw_1477 |
| MIT_STUDENT_DIRECTORY.DEPARTMENT | department / Department Code / Dept Code / Department ID / Course Number / Student Department Code | varchar(127) | dw_1082, dw_4113, dw_1330, dw_1350, dw_1366, dw_1368, dw_1402, dw_1474 |
| MIT_STUDENT_DIRECTORY.DEPARTMENT_NAME | department name / Dept Name / Student Department / Academic Department / Department | varchar(127) | dw_1082, dw_4113, dw_2666, dw_1330, dw_1350, dw_1366, dw_1368, dw_1402 |
| MIT_STUDENT_DIRECTORY.STUDENT_YEAR | student year / Year / Academic Year / Class Year / Student Level | varchar(127) | dw_1082, dw_4113, dw_2666, dw_1330, dw_1350, dw_1366, dw_1368, dw_1402 |
| MIT_STUDENT_DIRECTORY.FULL_NAME_UPPERCASE | full name uppercase / Uppercase Name / Name Upper / Full Name Caps | varchar(127) | schema / MIT_STUDENT_DIRECTORY |
| MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date / Snapshot Date | varchar(255) | dw_2666 |

## MOIRA_LIST

Stores metadata and configuration flags for Moira mailing lists and groups, including their identifiers, names, descriptions, and status attributes such as activity, visibility, and type.

恢复表名: moira list / Moira Lists / Mailing List / Mailing Lists / List / Lists / Moira Mailing List / Moira Group
SQL表别名: l, l2, m, ml, t0

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| MOIRA_LIST.MOIRA_LIST_KEY | moira list key / List Key / List ID / List Identifier / Key / Moira Key | varchar(127) | dw_2956, dw_3053 |
| MOIRA_LIST.MOIRA_LIST_NAME | moira list name / List Name / Name / Mailing List Name / Group Name / List Title | varchar(127) | dw_2956, dw_3053 |
| MOIRA_LIST.MOIRA_LIST_DESCRIPTION | moira list description / List Description / Description / List Info / Mailing List Description | varchar(127) | schema / MOIRA_LIST |
| MOIRA_LIST.IS_ACTIVE | is active / Active / List Status / Active Status / Enabled / Moira Active | varchar(127) | dw_2956 |
| MOIRA_LIST.IS_MOIRA_MAILING_LIST | is moira mailing list / Mailing List Flag / Is Mailing List / Moira Mailing List / List Type Mailing / Mailing List Indicator | varchar(127) | dw_2956, dw_3053 |
| MOIRA_LIST.IS_MOIRA_GROUP | is moira group / Group Flag / Is Group / Moira Group / List Type Group / Group Indicator | varchar(127) | schema / MOIRA_LIST |
| MOIRA_LIST.IS_NFS_GROUP | is nfs group / NFS Group Flag / Is NFS / NFS Group / NFS Indicator / NFS Status | varchar(127) | schema / MOIRA_LIST |
| MOIRA_LIST.IS_PUBLIC | is public / Public / Public Flag / Visibility / Public Status / List Visibility | varchar(127) | dw_2956, dw_3053 |
| MOIRA_LIST.IS_HIDDEN | is hidden / Hidden / Hidden Flag / Hidden Status / List Hidden / Visibility Hidden | varchar(127) | schema / MOIRA_LIST |

## MOIRA_LIST_DETAIL

Stores detailed membership records for Moira mailing lists, linking specific members (identified by Kerberos name, full name, and MIT ID) to specific lists and their owners, including metadata on when the membership was last updated.

恢复表名: moira list detail / Moira List Members / Moira Mailing List Members / List Member Details / Moira Subscription Details
SQL表别名: d, d2, m, mld, mld2, t1

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| MOIRA_LIST_DETAIL.MOIRA_LIST_KEY | moira list key / List Key / Moira List Identifier / List ID / Mailing List Key | varchar(127) | dw_2901, dw_3053, dw_2956 |
| MOIRA_LIST_DETAIL.MOIRA_LIST_OWNER_KEY | moira list owner key / List Owner Key / Owner Identifier / List Owner ID / Moira Owner Key | varchar(127) | dw_2901 |
| MOIRA_LIST_DETAIL.MOIRA_LIST_MEMBER | moira list member / Member Kerberos Name / Member Username / Kerberos Name / Member ID / User Name | varchar(127) | dw_3053, dw_1270, dw_1942, dw_2370, dw_2377, dw_2511, dw_5187, dw_5709 |
| MOIRA_LIST_DETAIL.MOIRA_LIST_MEMBER_FULL_NAME | moira list member full name / Member Full Name / Moira List Member Name / Full Name / Member Name / Subscriber Name | varchar(127) | dw_2901, dw_2956 |
| MOIRA_LIST_DETAIL.MOIRA_LIST_MEMBER_MIT_ID | moira list member mit id / moira list member mit identifier / Member MIT ID / MIT ID / Employee ID / Member Employee ID / Staff ID | varchar(127) | dw_2901, dw_2956, dw_1270, dw_1942, dw_2370, dw_2377, dw_2511, dw_5709 |
| MOIRA_LIST_DETAIL.LAST_UPDATE_DATE | last update date / Update Date / Last Modified Date / Membership Update Date / Date Updated | varchar(255) | dw_2901, dw_3053, dw_2956, dw_5187 |
| MOIRA_LIST_DETAIL.COUNTER | counter / Row Counter / Sequence Number / Record Counter | int | schema / MOIRA_LIST_DETAIL |
| MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / ETL Date / Data Load Date / Ingestion Date | varchar(255) | schema / MOIRA_LIST_DETAIL |

## MOIRA_LIST_OWNER

Stores ownership information for Moira lists, linking list identifiers to their owners and owner types.

恢复表名: moira list owner / Moira List Ownership / List Owner Details / Moira List Owner Reference
SQL表别名: mlo, o

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| MOIRA_LIST_OWNER.MOIRA_LIST_OWNER_KEY | moira list owner key / List Owner Key / Owner Key / List Owner ID / Moira List Owner Identifier | varchar(127) | dw_2901 |
| MOIRA_LIST_OWNER.OWNER | owner / List Owner / Moira List Owner / Owner Name / Owner ID | varchar(127) | dw_2901 |
| MOIRA_LIST_OWNER.OWNER_TYPE | owner type / List Owner Type / Moira List Owner Type / Owner Category / Owner Class | varchar(127) | dw_2901 |
| MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date / Last Loaded Date | varchar(255) | schema / MOIRA_LIST_OWNER |

## OPA_PERSON_CURRENT

Stores current demographic, employment, and organizational details for active personnel, including faculty and staff, within the OPA (Office of Personnel Administration) or HR system.

恢复表名: opa person current / Current Personnel / Active Employees / Staff Directory / Faculty and Staff / Current HR Records / OPA Person
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| OPA_PERSON_CURRENT.MIT_ID | mit id / mit identifier / Employee ID / Staff ID / Person ID / Unique Identifier | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.FULL_NAME | full name / Employee Name / Staff Name / Person Name / Complete Name | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.FORM_OF_ADDRESS_SHORT | form of address short / Title / Honorific / Prefix / Form of Address / Mr/Ms/Dr | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.FIRST_NAME | first name / Given Name / Forename / Employee First Name | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.MIDDLE_NAME | middle name / Middle Initial / Employee Middle Name | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.LAST_NAME | last name / Surname / Family Name / Employee Last Name | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.KRB_NAME_UPPERCASE | krb name uppercase / Kerberos Name / KRB Name / Username / Login ID / Uppercase Kerberos | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.EMAIL_ADDRESS | email address / Email / Work Email / Contact Email / Staff Email | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.JOB_ID | job id / job identifier / Position ID / Role ID / Job Code | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.JOB_TITLE | job title / Position Title / Role / Job Description / Employee Title | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.ADMIN_EMPLOYEE_TYPE | admin employee type / Employee Type / Staff Type / Employment Type / Personnel Type / Admin Type | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.HR_DEPARTMENT_CODE_OLD | hr department code old / Old Department Code / Legacy Dept Code / HR Dept Code / Department Code | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.HR_DEPARTMENT_NAME | hr department name / Department Name / HR Department / Dept Name / Organizational Unit Name | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.HR_ORG_UNIT_ID | hr org unit id / hr org unit identifier / Org Unit ID / Organization ID / HR Org ID / Unit ID | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.ADMIN_ORG_UNIT_TITLE | admin org unit title / Org Unit Title / Organization Title / Unit Name / Admin Org Title | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.ADMIN_POSITION_TITLE | admin position title / Position Title / Admin Position / Role Title / Job Position | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.PAYROLL_RANK | payroll rank / Salary Rank / Grade / Pay Grade / Rank | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.IS_FACULTY | is faculty / Faculty Flag / Faculty Status / Teaching Staff | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.EMPLOYMENT_PERCENT | employment percent / FTE / Full Time Equivalent / Work Percentage / Employment Rate | int | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.IS_CONSULT_PRIV | is consult priv / Consulting Privilege / Consultant Flag / Privileged Consultant / Consulting Status | varchar(31) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.IS_PAID_APPT | is paid appt / Paid Appointment / Paid Status / Salary Appointment / Paid Flag | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.IS_SUMMER_SESSION_APPT | is summer session appt / Summer Session Appointment / Summer Appointment / Summer Flag / Summer Session Status | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.SUMMER_SESSION_MONTHS | summer session months / Summer Months / Summer Duration / Months in Summer / Summer Session Length | int | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.IS_SABBATICAL | is sabbatical / On Sabbatical / Sabbatical Flag / Sabbatical Status / Leave Status | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.SABBATICAL_BEGIN_DATE | sabbatical begin date / Sabbatical Start Date / Sabbatical Begin / Leave Start Date / Sabbatical Start | varchar(255) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.SABBATICAL_END_DATE | sabbatical end date / Sabbatical Finish / Leave End Date / Sabbatical End | varchar(255) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.IS_OPA_REQUIRED | is opa required / OPA Required / OPA Flag / Personnel Action Required / OPA Status | varchar(31) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.IS_6MO_APPT | is 6 mo appt / 6 Month Appointment / Six Month Appointment / 6-Month Flag / Short Term Appointment | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.PERSONNEL_SUBAREA | personnel subarea / Subarea / HR Subarea / Personnel Category | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.PERSONNEL_SUBAREA_CODE | personnel subarea code / Subarea Code / Personnel Code / HR Subarea Code / Category Code | varchar(127) | schema / OPA_PERSON_CURRENT |
| OPA_PERSON_CURRENT.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date / Last Updated / Warehouse Date | varchar(255) | schema / OPA_PERSON_CURRENT |

## PERSON_AUTH_AREA

Stores the specific authorization levels and access rights assigned to individual users or employees across different functional areas such as finance, HR, and payroll.

恢复表名: person auth area / person authorization area / user access rights / employee permissions / security roles / access control / user privileges
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| PERSON_AUTH_AREA.USER_NAME | user name / username / user id / employee name / login name / account name / person name | varchar(127) | schema / PERSON_AUTH_AREA |
| PERSON_AUTH_AREA.HAS_FINANCIAL_AUTH | has financial auth / financial access / finance permission / financial authorization / finance rights / financial clearance | varchar(127) | schema / PERSON_AUTH_AREA |
| PERSON_AUTH_AREA.HAS_HR_FULL_AUTH | has hr full auth / full HR access / HR full permission / complete HR authorization / full HR rights / HR admin access | varchar(127) | schema / PERSON_AUTH_AREA |
| PERSON_AUTH_AREA.HAS_HR_LIMITED_AUTH | has hr limited auth / limited HR access / HR limited permission / partial HR authorization / restricted HR rights / limited HR clearance | varchar(127) | schema / PERSON_AUTH_AREA |
| PERSON_AUTH_AREA.HAS_PAYROLL_AUTH | has payroll auth / payroll access / payroll permission / payroll authorization / payroll rights / payroll clearance | varchar(127) | schema / PERSON_AUTH_AREA |
| PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE | warehouse load date / load date / data load date / etl date / refresh date / update date / warehouse date | varchar(255) | schema / PERSON_AUTH_AREA |

## PROFIT_CENTER_GROUP

Stores the hierarchical structure and grouping of profit centers, including multi-level categories and sorting order for organizational reporting.

恢复表名: profit center group / pc group / profit center hierarchy / pc hierarchy / profit center structure / pc structure
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| PROFIT_CENTER_GROUP.PROFIT_CENTER_KEY | profit center key / pc key / profit center identifier / pc id key | varchar(127) | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.PROFIT_CENTER_ID | profit center id / profit center identifier / pc id / profit center number / pc code | varchar(127) | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.PROFIT_CENTER_NAME | profit center name / pc name / profit center label / pc description | varchar(127) | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.PC_LEVEL1_SORT | pc level1 sort / level 1 sort / pc level 1 order / first level sort / top level sort | int | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.PC_LEVEL1_CATEGORY | pc level1 category / level 1 category / pc level 1 group / first level category / top level category | varchar(127) | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.PC_LEVEL2_SORT | pc level2 sort / level 2 sort / pc level 2 order / second level sort / level 2 sequence | int | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.PC_LEVEL2_CATEGORY | pc level2 category / level 2 category / pc level 2 group / second level category / level 2 subcategory | varchar(127) | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.PC_LEVEL3_SORT | pc level3 sort / level 3 sort / pc level 3 order / third level sort / level 3 sequence | int | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.PC_LEVEL3_CATEGORY | pc level3 category / level 3 category / pc level 3 group / third level category / level 3 subcategory | varchar(127) | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.PC_LEVEL4_SORT | pc level4 sort / level 4 sort / pc level 4 order / fourth level sort / level 4 sequence | int | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.PC_LEVEL4_CATEGORY | pc level4 category / level 4 category / pc level 4 group / fourth level category / level 4 subcategory | varchar(127) | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.PC_LEVEL5_SORT | pc level5 sort / level 5 sort / pc level 5 order / fifth level sort / level 5 sequence | int | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.PC_LEVEL5_CATEGORY | pc level5 category / level 5 category / pc level 5 group / fifth level category / level 5 subcategory | varchar(127) | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.PC_LEVEL6_SORT | pc level6 sort / level 6 sort / pc level 6 order / sixth level sort / level 6 sequence | int | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.PC_LEVEL6_CATEGORY | pc level6 category / level 6 category / pc level 6 group / sixth level category / level 6 subcategory | varchar(127) | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.PC_LEVEL7_SORT | pc level7 sort / level 7 sort / pc level 7 order / seventh level sort / level 7 sequence | int | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.PC_LEVEL7_CATEGORY | pc level7 category / level 7 category / pc level 7 group / seventh level category / level 7 subcategory | varchar(127) | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.PC_LEVEL8_SORT | pc level8 sort / level 8 sort / pc level 8 order / eighth level sort / level 8 sequence | int | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.PC_LEVEL8_CATEGORY | pc level8 category / level 8 category / pc level 8 group / eighth level category / level 8 subcategory | varchar(127) | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.DLC_KEY | dlc key / data load control key / dlc id / load control key | varchar(127) | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.DLC_NAME | dlc name / data load control name / dlc label / load control name | varchar(127) | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.WAREHOUSE_LOAD_DATE | warehouse load date / load date / data load date / etl date | varchar(255) | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.PROFIT_CENTER_GROUP_CODE | profit center group code / pc group code / group code / pcg code | varchar(127) | schema / PROFIT_CENTER_GROUP |
| PROFIT_CENTER_GROUP.PROFIT_CENTER_GROUP_NAME | profit center group name / pc group name / group name / pcg name | varchar(127) | schema / PROFIT_CENTER_GROUP |

## ROLES_FIN_PA

Maps user accounts to specific financial roles or domains (e.g., Bates, LNS, Anthro, CIS, CMS) for access control or reporting segmentation.

恢复表名: roles fin pa / Financial Roles / PA Roles / User Roles / Role Assignments / Financial Access Roles
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ROLES_FIN_PA.USERNAME | username / User / User ID / Login / Account / Employee ID / Staff Name | varchar(127) | schema / ROLES_FIN_PA |
| ROLES_FIN_PA.DLC_KEY | dlc key / Role / Role Key / Domain / Department / Financial Area / Access Code / Role Code | varchar(127) | schema / ROLES_FIN_PA |

## SE_PERSON

Stores demographic and employment details for individuals (students and staff) at MIT, including names, IDs, roles, and organizational affiliations.

恢复表名: se person / person / employee / student / individual / staff / MIT person
SQL表别名: s, sp, t1

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SE_PERSON.MIT_ID | mit id / mit identifier / student ID / employee ID / person ID / unique identifier / ID number | varchar(127) | dw_2759, dw_463, dw_4232, dw_4477, dw_1054, dw_1333, dw_135, dw_1561 |
| SE_PERSON.KRB_NAME | krb name / Kerberos name / username / login name / network ID / account name | varchar(127) | schema / SE_PERSON |
| SE_PERSON.FULL_NAME | full name / name / person name / student name / employee name / instructor name | varchar(127) | dw_2759, dw_463, dw_2666, dw_4232, dw_4477, dw_1054, dw_1333, dw_135 |
| SE_PERSON.PAYROLL_RANK | payroll rank / job title / position rank / employment rank / role / staff type | varchar(127) | schema / SE_PERSON |
| SE_PERSON.POSITION_TITLE | position title / job title / role title / professional title / position / job description | varchar(127) | schema / SE_PERSON |
| SE_PERSON.IS_ACTIVE | is active / active status / employment status / active flag / current status / active indicator | varchar(31) | dw_2666 |
| SE_PERSON.OFFICE_LOCATION | office location / office / room number / work location / office room / physical location | varchar(127) | dw_2759, dw_4232, dw_4477 |
| SE_PERSON.ORGANIZATION | organization / department / school / unit / academic department / affiliation | varchar(127) | dw_463 |
| SE_PERSON.FIRST_NAME | first name / given name / forename / name first / student first name / employee first name | varchar(127) | schema / SE_PERSON |
| SE_PERSON.LAST_NAME | last name / surname / family name / name last / student last name / employee last name | varchar(127) | schema / SE_PERSON |
| SE_PERSON.MIDDLE_NAME | middle name / middle initial / second name / name middle / student middle name / employee middle name | varchar(127) | schema / SE_PERSON |
| SE_PERSON.EMPLOYEE_TYPE | employee type / person type / staff type / role type / employment category / student type | varchar(127) | dw_2759, dw_4232, dw_4477, dw_1054, dw_1333, dw_135, dw_1561, dw_1655 |

## SIS_ADMIN_DEPARTMENT

Stores administrative department metadata, including codes, names, contact information, and financial clearing cost collectors, linked to academic departments.

恢复表名: sis admin department / Administrative Department / Admin Department / Department Administration / SIS Department Admin
SQL表别名: a, ad, sad, t0, t2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / ETL Date / Data Load Date / Refresh Date | varchar(255) | schema / SIS_ADMIN_DEPARTMENT |
| SIS_ADMIN_DEPARTMENT.SIS_ADMIN_DEPARTMENT_CODE | sis admin department code / Admin Department Code / SIS Admin Code / Department Code / Admin Dept Code / Administrative Department Identifier | varchar(127) | dw_112, dw_1305, dw_2224, dw_1298, dw_1332, dw_1390, dw_1464, dw_1515 |
| SIS_ADMIN_DEPARTMENT.SIS_ADMIN_DEPARTMENT_NAME | sis admin department name / Admin Department Name / SIS Admin Name / Administrative Department Name / Department Name / Admin Dept Name | varchar(127) | dw_112, dw_1305, dw_1298, dw_1332, dw_1390, dw_1515, dw_1516, dw_1525 |
| SIS_ADMIN_DEPARTMENT.DEPARTMENT_PHONE_AREA_CODE | department phone area code / Phone Area Code / Department Area Code / Area Code / Admin Dept Area Code | varchar(127) | schema / SIS_ADMIN_DEPARTMENT |
| SIS_ADMIN_DEPARTMENT.DEPARTMENT_PHONE_NUMBER | department phone number / Department Phone / Phone Number / Admin Dept Phone / Contact Number / Department Contact | varchar(127) | dw_1305, dw_1332, dw_1390, dw_1464, dw_1525, dw_1624, dw_1717 |
| SIS_ADMIN_DEPARTMENT.CLEARING_COST_COLLECTOR | clearing cost collector / Cost Collector / Clearing Cost Code / Financial Collector ID / Budget Collector | varchar(127) | dw_112, dw_2224, dw_1298, dw_1464, dw_1515, dw_1516 |
| SIS_ADMIN_DEPARTMENT.LAST_ACTIVITY_DATE | last activity date / Last Updated / Last Modified Date / Activity Date / Last Change Date | varchar(255) | dw_2224 |

## SIS_COURSE_DESCRIPTION

Stores descriptive metadata, departmental affiliation, and validity periods for academic courses (subjects) within the SIS system, linking course numbers to their names, levels, and degree-granting status.

恢复表名: sis course description / course description / course catalog description / department course info / academic course metadata
SQL表别名: SCD, c, c2, cd, d, s, sc, scd, scd2, t0, t1

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SIS_COURSE_DESCRIPTION.SIS_COURSE_DESCRIPTION_KEY | sis course description key / course description key / primary key / record id / unique course identifier | varchar(127) | dw_263, dw_1666 |
| SIS_COURSE_DESCRIPTION.COURSE | course / course number / subject code / course id / department course number / subject number | varchar(127) | dw_2365, dw_1766, dw_263, dw_4835, dw_1091, dw_1152, dw_1276, dw_1626 |
| SIS_COURSE_DESCRIPTION.COURSE_DESCRIPTION | course description / course name / short description / subject title / course title | varchar(127) | dw_2365, dw_4835, dw_1091, dw_1152, dw_1276, dw_1626, dw_1666 |
| SIS_COURSE_DESCRIPTION.COURSE_DESCRIPTION_LONG | course description long / long course description / full course name / detailed course title / extended description | varchar(127) | dw_1595 |
| SIS_COURSE_DESCRIPTION.DEPARTMENT | department / department code / dept code / department number / academic department id | varchar(127) | dw_2365, dw_1766, dw_263, dw_1595, dw_1091, dw_1276, dw_1626, dw_1666 |
| SIS_COURSE_DESCRIPTION.DEPARTMENT_NAME | department name / department / dept name / academic department / department title | varchar(127) | dw_2365, dw_1766, dw_1595, dw_4835, dw_1091, dw_1152, dw_1276, dw_1626 |
| SIS_COURSE_DESCRIPTION.DEPT_NAME_IN_COMMENCEMENT_BK | dept name in commencement bk / department name in commencement bk / commencement department name / formal department name / graduation department name | varchar(127) | schema / SIS_COURSE_DESCRIPTION |
| SIS_COURSE_DESCRIPTION.SCHOOL_NAME | school name / school / college name / academic school / school of | varchar(127) | dw_2365, dw_1766, dw_1595, dw_4835, dw_1091, dw_1152, dw_1276, dw_1666 |
| SIS_COURSE_DESCRIPTION.SCHOOL_NAME_IN_COMMENCEMENT_BK | school name in commencement bk / commencement school name / formal school name / graduation school name | varchar(127) | schema / SIS_COURSE_DESCRIPTION |
| SIS_COURSE_DESCRIPTION.FROM_TERM | from term / start term / effective from term / beginning term code / valid from term | varchar(127) | dw_2365 |
| SIS_COURSE_DESCRIPTION.FROM_TERM_DESCRIPTION | from term description / start term description / effective from term name / beginning term label | varchar(127) | dw_2365 |
| SIS_COURSE_DESCRIPTION.THRU_TERM | thru term / end term / effective thru term / ending term code / valid thru term | varchar(127) | schema / SIS_COURSE_DESCRIPTION |
| SIS_COURSE_DESCRIPTION.THRU_TERM_DESCRIPTION | thru term description / end term description / effective thru term name / ending term label | varchar(127) | schema / SIS_COURSE_DESCRIPTION |
| SIS_COURSE_DESCRIPTION.COURSE_OPTION | course option / course variant / subject option / course suffix / option code | varchar(127) | dw_1766, dw_1815, dw_1872 |
| SIS_COURSE_DESCRIPTION.COURSE_LEVEL | course level / level / undergraduate graduate / course tier / academic level | varchar(127) | dw_1766, dw_1595, dw_1091, dw_1152, dw_1276, dw_1626, dw_1666, dw_1815 |
| SIS_COURSE_DESCRIPTION.CIP_PROGRAM_CODE | cip program code / cip code / program code / classification code / cip program | varchar(127) | dw_2365, dw_1152, dw_1626, dw_1666 |
| SIS_COURSE_DESCRIPTION.IS_DEGREE_GRANTING | is degree granting / degree granting / counts toward degree / degree eligible / credit bearing | varchar(31) | dw_1766, dw_1595, dw_4835, dw_1091, dw_1152, dw_1276, dw_1626, dw_1815 |
| SIS_COURSE_DESCRIPTION.DEFAULT_ULTIMATE_DEGREE | default ultimate degree / default degree / ultimate degree / target degree / degree type | varchar(127) | schema / SIS_COURSE_DESCRIPTION |
| SIS_COURSE_DESCRIPTION.GRADAUTE_LEVEL | gradaute level / graduate level typo / grad level / post-baccalaureate level | varchar(127) | schema / SIS_COURSE_DESCRIPTION |
| SIS_COURSE_DESCRIPTION.GRADUATE_LEVEL | graduate level / grad level / post-baccalaureate level / masters doctoral | varchar(127) | dw_263 |
| SIS_COURSE_DESCRIPTION.LAST_ACTIVITY_DATE | last activity date / last updated / last modified / update date / activity date | varchar(255) | dw_4835 |
| SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE | warehouse load date / load date / etl date / data load timestamp / warehouse date | varchar(255) | schema / SIS_COURSE_DESCRIPTION |

## SIS_DEPARTMENT

Reference table containing metadata for academic departments, including codes, names, school affiliations, budget codes, and degree-granting status.

恢复表名: sis department / department / academic_department / sis_department / department_reference / dept / department_master
SQL表别名: d, d2, s, sd, sd2, t0, t1

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SIS_DEPARTMENT.DEPARTMENT_CODE | department code / dept code / department identifier / course number / dept id / department key | varchar(127) | dw_1350, dw_1618, dw_1033, dw_1833, dw_1437, dw_1623, dw_1631, dw_1785 |
| SIS_DEPARTMENT.DEPARTMENT_NAME | department name / dept name / department short name / academic unit name / department label | varchar(127) | dw_1350, dw_1618, dw_1033, dw_1833, dw_1437, dw_1623, dw_1631, dw_1785 |
| SIS_DEPARTMENT.DEPARTMENT_FULL_NAME | department full name / full department name / dept full name / department title / complete department name | varchar(127) | dw_1350, dw_1618, dw_1033, dw_1437, dw_1623, dw_1631, dw_1785, dw_634 |
| SIS_DEPARTMENT.SCHOOL_CODE | school code / college code / school identifier / academic school code / school id | varchar(127) | dw_1618, dw_1033, dw_1437, dw_1623, dw_1631, dw_1785, dw_634, dw_1061 |
| SIS_DEPARTMENT.SCHOOL_NAME | school name / college name / academic school / school title / college label | varchar(127) | dw_1350, dw_1618, dw_1833, dw_1437, dw_1623, dw_1631, dw_1785, dw_634 |
| SIS_DEPARTMENT.DEPT_BUDGET_CODE | dept budget code / department budget code / budget code / dept budget / financial code / department financial identifier | varchar(127) | dw_1350, dw_1437, dw_1631 |
| SIS_DEPARTMENT.IS_DEGREE_GRANTING | is degree granting / degree granting flag / degree status / grants degrees / degree granting indicator | varchar(127) | dw_1350, dw_1618, dw_1033, dw_1437, dw_1623, dw_1631, dw_1785, dw_634 |
| SIS_DEPARTMENT.DEPT_NAME_IN_COMMENCEMENT_BK | dept name in commencement bk / department name in commencement bk / commencement department name / department name in commencement / commencement book dept name / formal commencement name / graduation department name | varchar(127) | dw_1033, dw_1061, dw_1205 |
| SIS_DEPARTMENT.SCHOOL_NAME_IN_COMMENCEMENT_BK | school name in commencement bk / commencement school name / school name in commencement / commencement book school name / formal commencement school name / graduation school name | varchar(127) | dw_1618, dw_1623, dw_1785, dw_634 |
| SIS_DEPARTMENT.DEPARTMENT_NAME_HISTORY | department name history / dept history / name change history / department previous names / historical department name | varchar(127) | schema / SIS_DEPARTMENT |
| SIS_DEPARTMENT.DEPARTMENT_LAST_ACTIVITY_DATE | department last activity date / last activity date / department last active / last activity / department activity date / last updated activity | varchar(255) | dw_1350 |
| SIS_DEPARTMENT.DLC_KEY | dlc key / department location code / dlc identifier / facility key / organization key | varchar(127) | dw_1833 |
| SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE | warehouse load date / load date / data load date / etl date / last load date | varchar(255) | schema / SIS_DEPARTMENT |

## SIS_LOOKUP

Stores reference codes and descriptions for various SIS categories such as load levels, registration types, and enrollment statuses.

恢复表名: sis lookup / Student Information System Lookup / Lookup Table / Code Table / Reference Data / SIS Reference
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SIS_LOOKUP.LOOKUP_TYPE | lookup type / Category / Code Type / Reference Category / Group / Type | varchar(127) | schema / SIS_LOOKUP |
| SIS_LOOKUP.CODE | code / Value / Short Code / Identifier / Key / Abbreviation | varchar(127) | schema / SIS_LOOKUP |
| SIS_LOOKUP.DESCRIPTION | description / Label / Name / Text / Full Name / Meaning | varchar(127) | schema / SIS_LOOKUP |
| SIS_LOOKUP.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / ETL Date / Update Date / Refresh Date / Data Load Timestamp | varchar(255) | schema / SIS_LOOKUP |

## SIS_SUBJECT_CODE

Reference table mapping academic subject codes to their descriptions, associated departments, and schools within the MIT SIS system.

恢复表名: sis subject code / Subject Code Reference / Course Subject Mapping / Department Subject Lookup / Academic Subject Directory / SIS Subject Codes
SQL表别名: s, sc, ssc, ssc2, t0, t1, t2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SIS_SUBJECT_CODE.COURSE_NUMBER | course number / Course ID / Subject Number / Course Code / Academic Course Identifier | varchar(127) | dw_4176, dw_1731, dw_1830, dw_5011, dw_649, dw_1146, dw_1538, dw_1597 |
| SIS_SUBJECT_CODE.SUBJECT_CODE | subject code / Subject ID / Course Subject Code / Academic Subject Code / Subject Abbreviation | varchar(127) | dw_4176, dw_1731, dw_1830, dw_2290, dw_5011, dw_649, dw_1146, dw_1538 |
| SIS_SUBJECT_CODE.SUBJECT_CODE_DESC | subject code desc / subject code description / Subject Description / Subject Name / Subject Title / Course Subject Description / Academic Subject Name | varchar(127) | dw_4176, dw_1731, dw_1830, dw_2290, dw_5011, dw_649, dw_1146, dw_1538 |
| SIS_SUBJECT_CODE.DEPARTMENT_CODE | department code / Dept Code / Department ID / Academic Department Code / Department Identifier | varchar(127) | dw_4176, dw_1731, dw_1830, dw_2290, dw_5011, dw_649, dw_1597, dw_1747 |
| SIS_SUBJECT_CODE.DEPARTMENT_NAME | department name / Dept Name / Academic Department / Department Title / Department Description | varchar(127) | dw_4176, dw_1731, dw_1830, dw_2290, dw_5011, dw_649, dw_1146, dw_1538 |
| SIS_SUBJECT_CODE.SCHOOL_CODE | school code / School ID / College Code / Academic School Code / School Identifier | varchar(127) | dw_4176, dw_2290 |
| SIS_SUBJECT_CODE.SCHOOL_NAME | school name / College Name / Academic School / School Title / School Description | varchar(127) | dw_4176, dw_1731, dw_1830, dw_2290, dw_5011, dw_649, dw_1146, dw_1538 |
| SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date / Warehouse Update Date / Record Load Timestamp | varchar(255) | schema / SIS_SUBJECT_CODE |

## SIS_TERM_ADDRESS_CATEGORY

Defines the categories of student living arrangements (e.g., fraternities, dormitories, off-campus) associated with term addresses, including their codes, descriptions, and validity periods.

恢复表名: sis term address category / Term Address Category / Housing Category / Living Group Category / Fraternity Dorm Category / Student Housing Type / Residence Category
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SIS_TERM_ADDRESS_CATEGORY.TERM_ADDRESS_CATEGORY_CODE | term address category code / Category Code / Address Category Code / Housing Code / Living Group Code / Term Address Code | varchar(127) | schema / SIS_TERM_ADDRESS_CATEGORY |
| SIS_TERM_ADDRESS_CATEGORY.TERM_ADDRESS_CATEGORY | term address category / Category Name / Address Category Name / Housing Name / Living Group Name / Fraternity Name / Dorm Name | varchar(127) | schema / SIS_TERM_ADDRESS_CATEGORY |
| SIS_TERM_ADDRESS_CATEGORY.LIVING_GROUP_TYPE | living group type / Living Group Type Code / Housing Type Code / Residence Type Code / Group Type / Category Type Code | varchar(127) | schema / SIS_TERM_ADDRESS_CATEGORY |
| SIS_TERM_ADDRESS_CATEGORY.LIVING_GROUP_TYPE_DESC | living group type desc / living group type description / Housing Type Description / Residence Type / Group Type Name / Category Type Description | varchar(127) | schema / SIS_TERM_ADDRESS_CATEGORY |
| SIS_TERM_ADDRESS_CATEGORY.VALID_FROM_DATE | valid from date / Start Date / Effective Date / Valid From / Category Start Date / Housing Start Date | varchar(255) | schema / SIS_TERM_ADDRESS_CATEGORY |
| SIS_TERM_ADDRESS_CATEGORY.VALID_THRU_DATE | valid thru date / End Date / Expiration Date / Valid Through / Category End Date / Housing End Date | varchar(255) | schema / SIS_TERM_ADDRESS_CATEGORY |
| SIS_TERM_ADDRESS_CATEGORY.LAST_ACTIVITY_DATE | last activity date / Last Updated Date / Last Modified Date / Activity Date / Last Change Date / Record Update Date | varchar(255) | schema / SIS_TERM_ADDRESS_CATEGORY |
| SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / ETL Date / Data Load Date / Warehouse Date / Ingestion Date | varchar(255) | schema / SIS_TERM_ADDRESS_CATEGORY |

## SPACE_DETAIL

Stores detailed information about individual rooms or spaces within buildings, including room identifiers, square footage, usage types, and associated building and floor keys.

恢复表名: space detail / room detail / building room details / space unit details / room square footage table / floor room details
SQL表别名: d, d2, sd, sd2, t0

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SPACE_DETAIL.BUILDING_KEY | building key / building id / building identifier / building number / building code | varchar(127) | dw_2780, dw_1003, dw_2094, dw_2212, dw_2528, dw_810, dw_817, dw_389 |
| SPACE_DETAIL.FLOOR_KEY | floor key / floor id / floor identifier / floor number / floor code | varchar(127) | dw_2616, dw_1003, dw_2094, dw_2212, dw_2528, dw_3113, dw_810, dw_817 |
| SPACE_DETAIL.SPACE_UNIT_KEY | space unit key / space unit id / space unit identifier / unit key / unit code | varchar(127) | dw_2592 |
| SPACE_DETAIL.SPACE_USAGE_KEY | space usage key / space usage id / usage key / usage identifier / room usage code | int | dw_2780, dw_2616, dw_3113, dw_389, dw_391 |
| SPACE_DETAIL.BUILDING_ROOM | building room / room code / room identifier / full room id / building room code | varchar(127) | dw_2780, dw_2616, dw_2592, dw_3113 |
| SPACE_DETAIL.BUILDING_ROOM_NAME | building room name / room name / room label / display room id / room title | varchar(127) | dw_2616, dw_1003, dw_2094, dw_2212, dw_2528, dw_3113, dw_810, dw_817 |
| SPACE_DETAIL.ROOM_NUMBER | room number / room id / room suffix / local room number / room code suffix | varchar(127) | dw_2780, dw_2592, dw_1003, dw_2094, dw_2212, dw_2528, dw_810, dw_817 |
| SPACE_DETAIL.ROOM_SQUARE_FOOTAGE | room square footage / square footage / room size / area / sq ft / room area | int | dw_2780, dw_2616, dw_2592, dw_1003, dw_2094, dw_2212, dw_2528, dw_3113 |
| SPACE_DETAIL.ROOM_COUNTER | room counter / room count / counter value / room index / sequence number | int | dw_2616, dw_3113, dw_389, dw_391 |
| SPACE_DETAIL.BUILDING_COMPONENT | building component / component id / component code / building part / section id | varchar(127) | dw_2780, dw_391 |
| SPACE_DETAIL.WAREHOUSE_LOAD_DATE | warehouse load date / load date / etl date / data load date / refresh date | varchar(255) | dw_2780, dw_1003, dw_2094, dw_2212, dw_2528, dw_810, dw_817 |

## SPACE_FLOOR

Dimension table containing metadata for building floors, including floor identifiers, display names, and warehouse load dates, used to join with space details for floor-level analysis.

恢复表名: space floor / floor / floors / building floor / floor dimension / floor reference
SQL表别名: f, sf

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SPACE_FLOOR.FLOOR_KEY | floor key / floor id / floor identifier / floor code / floor number / floor level | varchar(127) | dw_2528, dw_1003, dw_2094, dw_2212, dw_2948, dw_3096, dw_397, dw_5145 |
| SPACE_FLOOR.FLOOR | floor / floor number / floor level / floor code / floor index / floor value / floor sequence | varchar(127) | schema / SPACE_FLOOR |
| SPACE_FLOOR.FLOOR_NAME | floor name / floor label / floor title / floor display name / floor description / floor text | varchar(127) | dw_2528, dw_1003, dw_2094, dw_2212, dw_2948, dw_3096, dw_397, dw_5145 |
| SPACE_FLOOR.WAREHOUSE_LOAD_DATE | warehouse load date / load date / data load date / etl date / refresh date / update date | varchar(255) | dw_2528 |

## SPACE_SUPERVISOR_USAGE

Stores metrics regarding space usage, research volume, and supervisee counts for departments, linked to space units via department names.

恢复表名: space supervisor usage / supervisor space usage / department space metrics / research space allocation / supervisee space data
SQL表别名: SSU, s, ssu, suu, t0, t2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SPACE_SUPERVISOR_USAGE.MIT_ID | mit id / mit identifier / employee ID / person ID / supervisor ID | varchar(127) | dw_2896 |
| SPACE_SUPERVISOR_USAGE.DEPT_COUNT | dept count / department count / number of departments / department quantity | int | dw_2709, dw_3891, dw_4081, dw_4319, dw_4452, dw_4612 |
| SPACE_SUPERVISOR_USAGE.DEPT_NAMES | dept names / department names / department name / DLC key / department code / space unit key | varchar(127) | dw_2896, dw_2709, dw_2669, dw_3891, dw_4081, dw_4319, dw_4393, dw_4452 |
| SPACE_SUPERVISOR_USAGE.NUM_OF_SUPERVISEES | num of supervisees / number of supervisees / supervisee count / supervisees / staff count / team size | int | dw_2896, dw_2709, dw_2669, dw_3891, dw_4081, dw_4319, dw_4393, dw_4452 |
| SPACE_SUPERVISOR_USAGE.SQFT | sqft / square footage / square feet / space size / area | float | dw_2896, dw_2669, dw_4393, dw_4612, dw_4933, dw_311, dw_3115 |
| SPACE_SUPERVISOR_USAGE.RESEARCH_VOLUME | research volume / research amount / research output / res vol / research metric | float | dw_2896, dw_2709, dw_2669, dw_3891, dw_4081, dw_4319, dw_4393, dw_4452 |
| SPACE_SUPERVISOR_USAGE.SQFT_PER_SUPERVISEE | sqft per supervisee / square feet per supervisee / space per person / space efficiency per staff | float | schema / SPACE_SUPERVISOR_USAGE |
| SPACE_SUPERVISOR_USAGE.SQFT_PER_RES_VOL | sqft per res vol / square feet per research volume / space per research / space efficiency per research | float | schema / SPACE_SUPERVISOR_USAGE |
| SPACE_SUPERVISOR_USAGE.RES_VOL_PER_SQFT | res vol per sqft / research volume per square foot / research density / research output per space | float | schema / SPACE_SUPERVISOR_USAGE |

## SPACE_UNIT

Dimension table mapping space units (departments, programs, divisions) to their organizational hierarchy, DLC keys, and warehouse load metadata.

恢复表名: space unit / space units / department space / academic unit / organizational space / space unit dimension
SQL表别名: s, su, su2, t0, t1, t2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SPACE_UNIT.FCLT_ORGANIZATION_KEY | fclt organization key / facility organization key / org key / organization key / facility org id / parent org key | varchar(127) | dw_3366, dw_5020, dw_2812, dw_3158, dw_3931, dw_4173, dw_4252 |
| SPACE_UNIT.SPACE_UNIT_KEY | space unit key / space unit id / su key / unique space identifier / space unit primary key | varchar(127) | dw_3366, dw_5020, dw_2812, dw_3158, dw_3346, dw_3431, dw_3691, dw_3739 |
| SPACE_UNIT.SPACE_UNIT_CODE | space unit code / su code / department code / space code / unit code | varchar(127) | dw_3366, dw_5020, dw_2812, dw_3158, dw_3346, dw_3431, dw_3691, dw_3739 |
| SPACE_UNIT.SPACE_UNIT | space unit / space unit name / department name / unit name / program name / division name | varchar(127) | dw_3366, dw_5020, dw_2812, dw_3158, dw_3346, dw_3431, dw_3691, dw_3739 |
| SPACE_UNIT.DLC_KEY | dlc key / department location code key / org dlc key / department key / location code | varchar(127) | dw_3366, dw_5020, dw_2812, dw_3158, dw_3346, dw_3431, dw_3691, dw_3739 |
| SPACE_UNIT.WAREHOUSE_LOAD_DATE | warehouse load date / load date / etl date / data load date / refresh date | varchar(255) | dw_3366, dw_5020, dw_3346, dw_3431, dw_3691, dw_3739, dw_3916 |

## SPACE_UNIT2

Reference table mapping space unit codes and keys to department names and division keys.

恢复表名: space unit2 / space unit / department / organizational unit / space unit reference / department reference / org unit
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SPACE_UNIT2.SPACE_UNIT_KEY | space unit key / department key / org unit key / space unit id / department id | varchar(127) | schema / SPACE_UNIT2 |
| SPACE_UNIT2.SPACE_UNIT_CODE | space unit code / department code / org unit code / space unit number / department number | varchar(127) | schema / SPACE_UNIT2 |
| SPACE_UNIT2.SPACE_UNIT | space unit / space unit name / department name / org unit name / department description / space unit description | varchar(127) | schema / SPACE_UNIT2 |
| SPACE_UNIT2.DLC_KEY | dlc key / division key / division code / department level code / division identifier | varchar(127) | schema / SPACE_UNIT2 |
| SPACE_UNIT2.WAREHOUSE_LOAD_DATE | warehouse load date / load date / etl date / data load date / refresh date | varchar(255) | schema / SPACE_UNIT2 |

## SPACE_USAGE

Dimension table defining the functional usage or category of physical spaces (rooms) within buildings, such as research centers, labs, or storage.

恢复表名: space usage / space usage dimension / room usage type / space category / usage type
SQL表别名: su, suu, t1, u

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SPACE_USAGE.SPACE_USAGE_KEY | space usage key / usage id / space usage identifier / usage code key | int | dw_2780, dw_2616, dw_2851, dw_3052, dw_3113, dw_389, dw_391, dw_455 |
| SPACE_USAGE.SPACE_USAGE | space usage / usage type / room usage / space category / functional use / room type | varchar(127) | dw_2780, dw_2616, dw_2851, dw_3052, dw_3113, dw_389, dw_391, dw_455 |
| SPACE_USAGE.WAREHOUSE_LOAD_DATE | warehouse load date / load date / etl date / data load timestamp / refresh date | varchar(255) | dw_2780 |

## STUDENT_DEGREE_PROGRAM

Defines academic degree programs, including degree types, associated departments, schools, course numbers, and validity periods for student degree tracking.

恢复表名: student degree program / degree program / student degree / degree catalog / academic program / degree definition
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| STUDENT_DEGREE_PROGRAM.DEGREE_CODE | degree code / degree identifier / program code / degree id | varchar(127) | schema / STUDENT_DEGREE_PROGRAM |
| STUDENT_DEGREE_PROGRAM.DEGREE_DESC | degree desc / degree description / degree name / full degree name / program name | varchar(127) | schema / STUDENT_DEGREE_PROGRAM |
| STUDENT_DEGREE_PROGRAM.DEGREE_DESC_SHORT | degree desc short / degree description short / short degree description / abbreviated degree name / degree short name | varchar(127) | schema / STUDENT_DEGREE_PROGRAM |
| STUDENT_DEGREE_PROGRAM.DEGREE_TYPE | degree type / program type / degree category / academic level | varchar(127) | schema / STUDENT_DEGREE_PROGRAM |
| STUDENT_DEGREE_PROGRAM.DEGREE_TYPE_DESC | degree type desc / degree type description / program type name / degree category name | varchar(127) | schema / STUDENT_DEGREE_PROGRAM |
| STUDENT_DEGREE_PROGRAM.DEGREE_WEIGHT | degree weight / program weight / degree priority / sort order | int | schema / STUDENT_DEGREE_PROGRAM |
| STUDENT_DEGREE_PROGRAM.FROM_TERM | from term / start term / effective start term / program start term | varchar(127) | schema / STUDENT_DEGREE_PROGRAM |
| STUDENT_DEGREE_PROGRAM.THRU_TERM | thru term / end term / effective end term / program end term | varchar(127) | schema / STUDENT_DEGREE_PROGRAM |
| STUDENT_DEGREE_PROGRAM.DEPARTMENT | department / department code / dept code / department id / academic department | varchar(127) | schema / STUDENT_DEGREE_PROGRAM |
| STUDENT_DEGREE_PROGRAM.DEPT_NAME_IN_COMMENCEMENT_BK | dept name in commencement bk / department name in commencement bk / department name / commencement department name / dept name / academic department name | varchar(127) | schema / STUDENT_DEGREE_PROGRAM |
| STUDENT_DEGREE_PROGRAM.SCHOOL_NAME_IN_COMMENCEMENT_BK | school name in commencement bk / school name / commencement school name / academic school / college name | varchar(127) | schema / STUDENT_DEGREE_PROGRAM |
| STUDENT_DEGREE_PROGRAM.COURSE | course / course number / course code / academic course / program course | varchar(127) | schema / STUDENT_DEGREE_PROGRAM |
| STUDENT_DEGREE_PROGRAM.COURSE_LEVEL | course level / academic level / program level / degree level | varchar(127) | schema / STUDENT_DEGREE_PROGRAM |
| STUDENT_DEGREE_PROGRAM.IS_DOUBLE_MAJOR | is double major / double major flag / joint major / dual degree | varchar(127) | schema / STUDENT_DEGREE_PROGRAM |
| STUDENT_DEGREE_PROGRAM.COMMENCEMENT_BK_COURSE_ROMAN | commencement bk course roman / roman numeral course / commencement course roman / course roman numeral / traditional course number | varchar(127) | schema / STUDENT_DEGREE_PROGRAM |
| STUDENT_DEGREE_PROGRAM.COMMENCEMENT_BK_SEE_ALSO | commencement bk see also / see also / commencement reference / related degree reference / cross reference | varchar(127) | schema / STUDENT_DEGREE_PROGRAM |
| STUDENT_DEGREE_PROGRAM.DEGREE_LAST_ACTIVITY_DATE | degree last activity date / degree last activity / program last updated / degree activity date / last degree change | varchar(255) | schema / STUDENT_DEGREE_PROGRAM |
| STUDENT_DEGREE_PROGRAM.COURSE_LAST_ACTIVITY_DATE | course last activity date / course last activity / course last updated / course activity date / last course change | varchar(255) | schema / STUDENT_DEGREE_PROGRAM |
| STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE | warehouse load date / load date / data load date / etl date | varchar(255) | schema / STUDENT_DEGREE_PROGRAM |

## STUDENT_DEPARTMENT

Reference table mapping academic department codes to their names, full names, and parent school information.

恢复表名: student department / Department Reference / Academic Department Lookup / Department Master / Dept Lookup
SQL表别名: sd, t1

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| STUDENT_DEPARTMENT.DEPARTMENT_CODE | department code / Dept Code / Department ID / Dept ID / Offering Department Code / Department Abbreviation | varchar(127) | dw_4640, dw_1689, dw_1978, dw_2293, dw_3355, dw_3836, dw_5004, dw_783 |
| STUDENT_DEPARTMENT.DEPARTMENT_NAME | department name / Dept Name / Department Short Name / Academic Department / Offering Department Name / Department | varchar(127) | dw_4640, dw_1689, dw_1978, dw_2293, dw_3355, dw_3836, dw_5004, dw_783 |
| STUDENT_DEPARTMENT.DEPARTMENT_FULL_NAME | department full name / Full Department Name / Dept Full Name / Complete Department Name / Department Title | varchar(127) | dw_4640, dw_1689, dw_1978, dw_2293, dw_3355, dw_3836, dw_5004, dw_783 |
| STUDENT_DEPARTMENT.SCHOOL_CODE | school code / College Code / School ID / College ID / Parent School Code / Institution Code | varchar(127) | dw_4640 |
| STUDENT_DEPARTMENT.SCHOOL_NAME | school name / College Name / Parent School / Academic School / Institution Name / School | varchar(127) | dw_4640, dw_1689, dw_1978, dw_2293, dw_3355, dw_3836, dw_5004, dw_783 |

## STUDENT_ETHNIC_SUBGROUP

Reference table defining the hierarchical relationship between broad ethnic groups and their specific subgroups, including associated codes and names for student demographic reporting.

恢复表名: student ethnic subgroup / Ethnic Subgroup Reference / Student Ethnicity Subgroup / Ethnic Subgroup Lookup / Student Ethnic Subgroup Reference
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| STUDENT_ETHNIC_SUBGROUP.STUDENT_ETHNIC_SUBGROUP_KEY | student ethnic subgroup key / Ethnic Subgroup Key / Subgroup Key / Composite Key / Ethnic Subgroup ID | varchar(127) | schema / STUDENT_ETHNIC_SUBGROUP |
| STUDENT_ETHNIC_SUBGROUP.ETHNIC_GROUP_NAME | ethnic group name / Major Ethnic Group / Broad Ethnic Category / Parent Ethnic Group / Ethnicity Name | varchar(127) | schema / STUDENT_ETHNIC_SUBGROUP |
| STUDENT_ETHNIC_SUBGROUP.ETHNIC_SUBGROUP_NAME | ethnic subgroup name / Specific Ethnic Subgroup / Subgroup Name / Detailed Ethnicity / Ethnic Subcategory | varchar(127) | schema / STUDENT_ETHNIC_SUBGROUP |
| STUDENT_ETHNIC_SUBGROUP.ETHNIC_CODE | ethnic code / Ethnic Group Code / Major Ethnic Code / Parent Ethnic Code / Ethnicity Code / Broad Ethnic Code | varchar(127) | schema / STUDENT_ETHNIC_SUBGROUP |
| STUDENT_ETHNIC_SUBGROUP.ETHNIC_SUBGROUP_CODE | ethnic subgroup code / Subgroup Code / Specific Ethnic Code / Ethnic Subcategory Code / Detailed Ethnic Code | varchar(127) | schema / STUDENT_ETHNIC_SUBGROUP |
| STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date / Last Updated Date | varchar(255) | schema / STUDENT_ETHNIC_SUBGROUP |

## SUBJECT_ATTRIBUTE

Stores metadata and descriptive attributes for academic subjects or courses, including codes, short and full descriptions, report identifiers, and audit timestamps.

恢复表名: subject attribute / subject_attribute / subject_attributes / course_attributes / subject_codes / course_catalog / academic_subjects
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SUBJECT_ATTRIBUTE.SUBJECT_ATTRIBUTE_CODE | subject attribute code / subject_code / course_code / subject_id / course_id / subject_attribute_code / academic_code | varchar(127) | schema / SUBJECT_ATTRIBUTE |
| SUBJECT_ATTRIBUTE.SUBJECT_ATTRIBUTE_TYPE | subject attribute type / subject_type / course_type / attribute_type / subject_category / type_code / subject_attribute_type | varchar(127) | schema / SUBJECT_ATTRIBUTE |
| SUBJECT_ATTRIBUTE.SUBJECT_ATTRIBUTE_SHORT_DESC | subject attribute short desc / subject attribute short description / short_description / subject_short_desc / course_short_name / abbreviated_name / subject_attribute_short_desc / short_title | varchar(127) | schema / SUBJECT_ATTRIBUTE |
| SUBJECT_ATTRIBUTE.SUBJECT_ATTRIBUTE_DESC | subject attribute desc / subject attribute description / description / subject_desc / course_name / full_description / subject_attribute_desc / subject_title | varchar(127) | schema / SUBJECT_ATTRIBUTE |
| SUBJECT_ATTRIBUTE.SUBJECT_ATTRIBUTE_REPORT_DESC | subject attribute report desc / subject attribute report description / report_description / report_code / subject_report_desc / reporting_name / subject_attribute_report_desc / report_id | varchar(127) | schema / SUBJECT_ATTRIBUTE |
| SUBJECT_ATTRIBUTE.LAST_ACTIVITY_DATE | last activity date / last_activity / last_updated / activity_date / last_change_date / last_activity_date / modification_date | varchar(255) | schema / SUBJECT_ATTRIBUTE |
| SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE | warehouse load date / load_date / warehouse_date / etl_date / data_load_date / warehouse_load_date / ingestion_date | varchar(255) | schema / SUBJECT_ATTRIBUTE |

## SUBJECT_ENROLLABLE

Stores details about subjects (courses) that are available for enrollment, including their identifiers, titles, offering departments, and associated academic clusters for a specific term.

恢复表名: subject enrollable / enrollable subjects / course enrollment catalog / subject availability / enrollable courses / course offering details / subject enrollment data
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SUBJECT_ENROLLABLE.TERM_CODE | term code / term / academic term / semester / session / academic period | varchar(127) | schema / SUBJECT_ENROLLABLE |
| SUBJECT_ENROLLABLE.SUBJECT_ID | subject id / subject identifier / course id / course code / subject code / class id / course identifier | varchar(127) | schema / SUBJECT_ENROLLABLE |
| SUBJECT_ENROLLABLE.SUBJECT_TITLE | subject title / course title / course name / subject name / class title / course description | varchar(127) | schema / SUBJECT_ENROLLABLE |
| SUBJECT_ENROLLABLE.SUBJECT_TITLE_LONG | subject title long / long subject title / full course title / extended course name / detailed subject title / long course description | varchar(127) | schema / SUBJECT_ENROLLABLE |
| SUBJECT_ENROLLABLE.MASTER_SUBJECT_ID | master subject id / master subject identifier / parent course id / primary subject id / main course identifier / root subject id | varchar(127) | schema / SUBJECT_ENROLLABLE |
| SUBJECT_ENROLLABLE.ULT_MASTER_SUBJECT_ID | ult master subject id / ult master subject identifier / ultimate master subject id / root master course id / top-level subject id / final master identifier / ultimate parent course | varchar(127) | schema / SUBJECT_ENROLLABLE |
| SUBJECT_ENROLLABLE.CLUSTER_LIST | cluster list / subject clusters / course clusters / academic clusters / grouped subjects / cluster ids | varchar(127) | schema / SUBJECT_ENROLLABLE |
| SUBJECT_ENROLLABLE.OFFER_DEPT_CODE | offer dept code / offer department code / offering department code / department code / dept code / offering dept / department identifier / academic department | varchar(127) | schema / SUBJECT_ENROLLABLE |
| SUBJECT_ENROLLABLE.OFFER_SCHOOL_CODE | offer school code / offering school code / school code / college code / offering school / academic school identifier / faculty code | varchar(127) | schema / SUBJECT_ENROLLABLE |
| SUBJECT_ENROLLABLE.SUBJECT_GROUP_ID | subject group id / subject group identifier / course group id / group identifier / subject group / course grouping id / enrollment group id | varchar(127) | schema / SUBJECT_ENROLLABLE |
| SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE | warehouse load date / load date / data load date / etl date / record load date / data refresh date | varchar(255) | schema / SUBJECT_ENROLLABLE |

## SUBJECT_GROUPING

Stores the mapping of academic subjects or courses to specific departments, schools, and terms, including cross-enrollment programs and non-institute affiliations.

恢复表名: subject grouping / subject groupings / course grouping / department grouping / academic grouping / subject hierarchy
SQL表别名: g

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SUBJECT_GROUPING.SUBJECT_GROUPING_KEY | subject grouping key / grouping id / subject group id / unique grouping identifier / primary key for grouping | varchar(127) | schema / SUBJECT_GROUPING |
| SUBJECT_GROUPING.TERM_CODE | term code / academic term / semester code / term / session code / academic period | varchar(127) | schema / SUBJECT_GROUPING |
| SUBJECT_GROUPING.DEPARTMENT_CODE | department code / dept code / department abbreviation / academic unit code / department id | varchar(127) | schema / SUBJECT_GROUPING |
| SUBJECT_GROUPING.DEPARTMENT_NAME | department name / dept name / academic unit name / department short name / program name | varchar(127) | schema / SUBJECT_GROUPING |
| SUBJECT_GROUPING.DEPARTMENT_FULL_NAME | department full name / full department name / complete department name / department title / academic unit full name | varchar(127) | schema / SUBJECT_GROUPING |
| SUBJECT_GROUPING.SCHOOL_NAME | school name / institution name / campus name / school / affiliation | varchar(127) | schema / SUBJECT_GROUPING |
| SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE | warehouse load date / load date / etl date / data load date / refresh date / last updated | varchar(255) | schema / SUBJECT_GROUPING |

## SUBJECT_IAP_SCHEDULE

Stores the scheduling details for Intensive Assessment Period (IAP) sessions, including dates, times, locations, and virtual meeting links for specific subjects.

恢复表名: subject iap schedule / IAP Schedule / Intensive Assessment Period Schedule / Subject IAP Timetable / IAP Class Schedule / Assessment Period Schedule
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SUBJECT_IAP_SCHEDULE.TERM_CODE | term code / Term / Academic Term / Session Code / Academic Year | varchar(127) | schema / SUBJECT_IAP_SCHEDULE |
| SUBJECT_IAP_SCHEDULE.SUBJECT_ID | subject id / subject identifier / Subject / Course ID / Course Code / Module ID | varchar(127) | schema / SUBJECT_IAP_SCHEDULE |
| SUBJECT_IAP_SCHEDULE.SESSION_NUMBER | session number / Session / IAP Session / Assessment Session / Meeting Number | int | schema / SUBJECT_IAP_SCHEDULE |
| SUBJECT_IAP_SCHEDULE.MEET_PLACE | meet place / Location / Meeting Place / Venue / Classroom / Online Platform / Zoom | varchar(127) | schema / SUBJECT_IAP_SCHEDULE |
| SUBJECT_IAP_SCHEDULE.MEET_START_TIME | meet start time / Start Time / Begin Time / IAP Start / Session Start / Meeting Start | varchar(127) | schema / SUBJECT_IAP_SCHEDULE |
| SUBJECT_IAP_SCHEDULE.MEET_END_TIME | meet end time / End Time / Finish Time / IAP End / Session End / Meeting End | varchar(127) | schema / SUBJECT_IAP_SCHEDULE |
| SUBJECT_IAP_SCHEDULE.IAP_DAY | iap day / Day / Day of Week / Assessment Day / Meeting Day | varchar(127) | schema / SUBJECT_IAP_SCHEDULE |
| SUBJECT_IAP_SCHEDULE.IAP_DATE | iap date / Date / Assessment Date / Session Date / Meeting Date | varchar(255) | schema / SUBJECT_IAP_SCHEDULE |
| SUBJECT_IAP_SCHEDULE.REMARKS | remarks / Notes / Comments / Zoom Link / Meeting URL / Additional Info | varchar(127) | schema / SUBJECT_IAP_SCHEDULE |
| SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / ETL Date / Data Load Date / Warehouse Date / Last Updated | varchar(255) | schema / SUBJECT_IAP_SCHEDULE |

## SUBJECT_OFFERED

Stores detailed records of academic subjects (courses) offered in specific terms, including section details, enrollment counts, departmental information, and cluster classifications.

恢复表名: subject offered / subject_offered / offered_subjects / course_offerings / subject_offerings / academic_subjects_offered / term_subjects
SQL表别名: o, s, so, t0, t1

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SUBJECT_OFFERED.SUBJECT_KEY | subject key / subject_key / subject identifier / course key / offering key / unique subject id | varchar(127) | dw_3277, dw_3873, dw_4130 |
| SUBJECT_OFFERED.SUBJECT_OFFERED_SUMMARY_KEY | subject offered summary key / subject_offered_summary_key / summary key / offered summary id / subject summary link | varchar(127) | dw_3873 |
| SUBJECT_OFFERED.MASTER_SUBJECT_KEY | master subject key / master_subject_key / master key / parent subject key / master course id | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.COMPOSITE_SUBJECT_KEY | composite subject key / composite_subject_key / composite key / combined subject id / subject composite identifier | varchar(127) | dw_3530 |
| SUBJECT_OFFERED.TERM_CODE | term code / term_code / term / academic term / semester code / term identifier | varchar(127) | dw_3277, dw_4197, dw_3873, dw_4130, dw_3530, dw_3941, dw_3644, dw_5279 |
| SUBJECT_OFFERED.MASTER_COURSE_NUMBER | master course number / master_course_number / master course code / parent course number / master subject code | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.MASTER_COURSE_NUMBER_SORT | master course number sort / master_course_number_sort / master course sort / sorted master course number | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.MASTER_COURSE_NUMBER_DESC | master course number desc / master course number description / master_course_number_desc / master course description / master course name / master department name | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.MASTER_SUBJECT_ID | master subject id / master subject identifier / master_subject_id / master id / parent subject id / master course id | varchar(127) | dw_5279 |
| SUBJECT_OFFERED.MASTER_SUBJECT_ID_SORT | master subject id sort / master subject identifier sort / master_subject_id_sort / master id sort / sorted master subject id | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.COURSE_NUMBER | course number / course_number / course code / subject code / department code / course prefix | varchar(127) | dw_3644 |
| SUBJECT_OFFERED.COURSE_NUMBER_SORT | course number sort / course_number_sort / course sort / sorted course number | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.COURSE_NUMBER_DESC | course number desc / course number description / course_number_desc / course description / course name / department name | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.SUBJECT_ID | subject id / subject identifier / subject_id / course id / subject code / unique subject | varchar(127) | dw_3277, dw_3873, dw_3530, dw_2122 |
| SUBJECT_OFFERED.SUBJECT_ID_SORT | subject id sort / subject identifier sort / subject_id_sort / subject sort / sorted subject id | varchar(127) | dw_4197, dw_3644 |
| SUBJECT_OFFERED.SUBJECT_TITLE | subject title / subject_title / subject name / course title / course name / subject description | varchar(127) | dw_3277, dw_4197, dw_3873, dw_4130, dw_3530, dw_3941, dw_2122 |
| SUBJECT_OFFERED.SECTION_ID | section id / section identifier / section_id / section number / section code / class section | varchar(127) | dw_4130 |
| SUBJECT_OFFERED.IS_MASTER_SECTION | is master section / is_master_section / master section flag / is master / primary section | varchar(127) | dw_3277 |
| SUBJECT_OFFERED.IS_LECTURE_SECTION | is lecture section / is_lecture_section / lecture flag / is lecture / lecture section | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.IS_LAB_SECTION | is lab section / is_lab_section / lab flag / is lab / lab section | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.IS_RECITATION_SECTION | is recitation section / is_recitation_section / recitation flag / is recitation / recitation section | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.IS_DESIGN_SECTION | is design section / is_design_section / design flag / is design / design section | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.OFFER_DEPT_CODE | offer dept code / offer department code / offer_dept_code / department code / offering department code / dept code | varchar(127) | dw_4197, dw_3941 |
| SUBJECT_OFFERED.OFFER_DEPT_NAME | offer dept name / offer department name / offer_dept_name / department name / offering department / dept name | varchar(127) | dw_3277, dw_4197, dw_3873, dw_4130, dw_3530, dw_3941, dw_5279, dw_5377 |
| SUBJECT_OFFERED.OFFER_SCHOOL_NAME | offer school name / offer_school_name / school name / offering school / school | varchar(127) | dw_3277, dw_4197 |
| SUBJECT_OFFERED.RESPONSIBLE_FACULTY_NAME | responsible faculty name / responsible_faculty_name / faculty name / instructor name / professor name / teacher name | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.RESPONSIBLE_FACULTY_MIT_ID | responsible faculty mit id / responsible faculty mit identifier / responsible_faculty_mit_id / faculty id / instructor id / professor id / mit id | varchar(127) | dw_5387 |
| SUBJECT_OFFERED.MEET_TIME | meet time / meet_time / meeting time / class time / schedule time | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.MEET_PLACE | meet place / meet_place / meeting place / class location / room / location | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.CLUSTER_TYPE | cluster type / cluster_type / cluster code / elective cluster / type code | varchar(127) | dw_4130 |
| SUBJECT_OFFERED.CLUSTER_TYPE_DESC | cluster type desc / cluster type description / cluster_type_desc / cluster description / cluster name / elective type | varchar(127) | dw_4197 |
| SUBJECT_OFFERED.CLUSTER_LIST | cluster list / cluster_list / cluster members / subject list / related subjects | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.HGN_CODE | hgn code / hgn_code / hgn / graduate credit code / credit type | varchar(127) | dw_2122 |
| SUBJECT_OFFERED.HGN_CODE_DESC | hgn code desc / hgn code description / hgn_code_desc / hgn description / credit description / graduate credit status | varchar(127) | dw_5545 |
| SUBJECT_OFFERED.FORM_TYPE | form type / form_type / form code / subject form | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.FORM_TYPE_DESC | form type desc / form type description | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.SUBJECT_ENROLLMENT_NUMBER | subject enrollment number | int | dw_3873 |
| SUBJECT_OFFERED.SECTION_ENROLLMENT_NUMBER | section enrollment number | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.CLUSTER_ENROLLMENT_NUMBER | cluster enrollment number | int | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.EVALUATE_THIS_SUBJECT | evaluate this subject | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.IS_OSE_SUBJECT | is ose subject | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.IS_CREATED_BY_DATA_WAREHOUSE | is created by data warehouse | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.SUBJECT_GROUPING_KEY | subject grouping key | varchar(127) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE | warehouse load date | varchar(255) | schema / SUBJECT_OFFERED |
| SUBJECT_OFFERED.NUM_ENROLLED_STUDENTS | num enrolled students / number enrolled students | int | dw_3277, dw_4197, dw_3873, dw_3530, dw_3941, dw_2122 |
| SUBJECT_OFFERED.SUBJECT_SUMMARY_KEY | subject summary key | varchar(127) | dw_5377 |
| SUBJECT_OFFERED.IS_REPEATABLE_SUBJECT | is repeatable subject | varchar(127) | dw_3941 |

## SUBJECT_OFFERED_SUMMARY

A summary table containing detailed information about subjects (courses) offered in specific academic terms, including enrollment numbers, unit breakdowns, offering department details, and cluster classifications.

恢复表名: subject offered summary / Course Offer Summary / Subject Summary / Offered Subject Details / Course Enrollment Summary / Subject Offering Statistics
SQL表别名: s, sos, sos2, sso, t0, t1, t2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SUBJECT_OFFERED_SUMMARY.SUBJECT_OFFERED_SUMMARY_KEY | subject offered summary key / Summary Key / Record ID / Primary Identifier / Subject Term Key | varchar(127) | dw_1314, dw_2661 |
| SUBJECT_OFFERED_SUMMARY.COMPOSITE_SUBJECT_KEY | composite subject key / Subject Key / Course Key / Subject Identifier / Composite ID | varchar(127) | dw_4636 |
| SUBJECT_OFFERED_SUMMARY.TERM_CODE | term code / Academic Term / Term / Semester / Session / Term Identifier | varchar(127) | dw_1217, dw_1440, dw_1312, dw_2591, dw_2639, dw_4636, dw_2661, dw_3400 |
| SUBJECT_OFFERED_SUMMARY.COURSE_NUMBER | course number / Subject Code / Course Prefix / Department Code / Course ID Prefix | varchar(127) | dw_1217, dw_1314, dw_2591, dw_2639, dw_1360, dw_2661, dw_3400 |
| SUBJECT_OFFERED_SUMMARY.SUBJECT_ID | subject id / subject identifier / Course ID / Course Identifier / Subject Code | varchar(127) | dw_1217, dw_1440, dw_1312, dw_2591, dw_4877, dw_1360, dw_3400 |
| SUBJECT_OFFERED_SUMMARY.SUBJECT_ID_SORT | subject id sort / subject identifier sort / Sorted Subject ID / Subject Sort Key / Course Sort ID | varchar(127) | dw_1440, dw_4877 |
| SUBJECT_OFFERED_SUMMARY.SUBJECT_TITLE | subject title / Course Title / Course Name / Subject Name / Course Description Title | varchar(127) | dw_1217, dw_1312, dw_2639, dw_4636, dw_4877, dw_2661, dw_3400 |
| SUBJECT_OFFERED_SUMMARY.MASTER_SUBJECT_ID | master subject id / master subject identifier / Parent Subject ID / Base Subject ID / Root Subject ID | varchar(127) | schema / SUBJECT_OFFERED_SUMMARY |
| SUBJECT_OFFERED_SUMMARY.MASTER_SUBJECT_ID_SORT | master subject id sort / master subject identifier sort / Sorted Master Subject ID / Master Sort Key | varchar(127) | schema / SUBJECT_OFFERED_SUMMARY |
| SUBJECT_OFFERED_SUMMARY.CLUSTER_TYPE | cluster type / Cluster Code / Group Type / Category Type | varchar(127) | dw_4877 |
| SUBJECT_OFFERED_SUMMARY.CLUSTER_TYPE_DESC | cluster type desc / cluster type description / Cluster Name / Group Description / Category Description | varchar(127) | dw_1440, dw_2591 |
| SUBJECT_OFFERED_SUMMARY.CLUSTER_LIST | cluster list / Subject List / Group Members / Cluster Subjects | varchar(127) | schema / SUBJECT_OFFERED_SUMMARY |
| SUBJECT_OFFERED_SUMMARY.HGN_CODE | hgn code / Graduate Code / Credit Type Code / Level Code | varchar(127) | dw_5387, dw_1360 |
| SUBJECT_OFFERED_SUMMARY.HGN_CODE_DESC | hgn code desc / hgn code description / Graduate Credit Description / Credit Type Description / Level Description | varchar(127) | dw_2591 |
| SUBJECT_OFFERED_SUMMARY.OFFER_DEPT_CODE | offer dept code / offer department code / Offering Department Code / Department Code / Dept Code / Offering Dept / Department Identifier | varchar(127) | dw_1440, dw_1314, dw_5387, dw_1312, dw_1360, dw_2661 |
| SUBJECT_OFFERED_SUMMARY.OFFER_DEPT_NAME | offer dept name / offer department name / Offering Department Name / Department Name / Dept Name / Offering Dept Name / Department | varchar(127) | dw_1217, dw_3400 |
| SUBJECT_OFFERED_SUMMARY.OFFER_SCHOOL_NAME | offer school name / Offering School Name / School Name / School / Offering School | varchar(127) | dw_1217, dw_1314, dw_1360, dw_2661 |
| SUBJECT_OFFERED_SUMMARY.RESPONSIBLE_FACULTY_NAME | responsible faculty name / Faculty Name / Instructor Name / Professor Name / Teacher Name | varchar(127) | dw_1312 |
| SUBJECT_OFFERED_SUMMARY.RESPONSIBLE_FACULTY_MIT_ID | responsible faculty mit id / responsible faculty mit identifier / Faculty ID / Instructor ID / Professor ID / Faculty Identifier | varchar(127) | dw_5387 |
| SUBJECT_OFFERED_SUMMARY.TOTAL_UNITS | total units / Units / Credit Units / Total Credits / Unit Count | int | dw_1440, dw_1314, dw_1312, dw_2591, dw_2639, dw_4636, dw_4877, dw_1360 |
| SUBJECT_OFFERED_SUMMARY.LECTURE_UNITS | lecture units / Lecture Credits / Lecture Unit Count | int | dw_2639 |
| SUBJECT_OFFERED_SUMMARY.LAB_UNITS | lab units / Laboratory Units / Lab Credits / Laboratory Credits | int | schema / SUBJECT_OFFERED_SUMMARY |
| SUBJECT_OFFERED_SUMMARY.PREPARATION_UNITS | preparation units / Prep Units / Preparation Credits / Prep Credits | int | schema / SUBJECT_OFFERED_SUMMARY |
| SUBJECT_OFFERED_SUMMARY.SUBJECT_ENROLLMENT_NUMBER | subject enrollment number / Enrollment Number / Subject Enrollment / Enrollment Count | int | dw_1314 |
| SUBJECT_OFFERED_SUMMARY.CLUSTER_ENROLLMENT_NUMBER | cluster enrollment number / Cluster Enrollment / Group Enrollment / Cluster Student Count | int | schema / SUBJECT_OFFERED_SUMMARY |
| SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date / Update Date | varchar(255) | schema / SUBJECT_OFFERED_SUMMARY |
| SUBJECT_OFFERED_SUMMARY.NUM_ENROLLED_STUDENTS | num enrolled students / number enrolled students / Number of Enrolled Students / Enrolled Students / Student Count / Enrollment Count / Num Students | int | dw_1217, dw_1440, dw_1312, dw_4636, dw_1360, dw_2661, dw_3400 |
| SUBJECT_OFFERED_SUMMARY.SUBJECT_GROUPING_KEY | subject grouping key / Grouping Key / Subject Group ID / Group Key | varchar(127) | schema / SUBJECT_OFFERED_SUMMARY |
| SUBJECT_OFFERED_SUMMARY.SUBJECT_SUMMARY_KEY | subject summary key / Summary Key / Subject Key / Course Summary ID | varchar(127) | schema / SUBJECT_OFFERED_SUMMARY |

## SUBJECT_SELECTOR

Maps academic subjects to clusters, departments, and schools, providing hierarchical subject identifiers and organizational context for reporting and selection.

恢复表名: subject selector / subject_selector / subject selection / subject cluster mapping / academic subject hierarchy / subject department mapping / course subject selector
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SUBJECT_SELECTOR.SUBJECT_SUMMARY_KEY | subject summary key / summary key / subject key / subject identifier key | varchar(127) | schema / SUBJECT_SELECTOR |
| SUBJECT_SELECTOR.TERM_CODE | term code / academic term / semester code / term identifier / session code | varchar(127) | schema / SUBJECT_SELECTOR |
| SUBJECT_SELECTOR.SUBJECT_ID | subject id / subject identifier / course id / subject code / academic subject id | varchar(127) | schema / SUBJECT_SELECTOR |
| SUBJECT_SELECTOR.SUBJECT_ID_SORT | subject id sort / subject identifier sort / sort key / subject sort order / ordering key | varchar(127) | schema / SUBJECT_SELECTOR |
| SUBJECT_SELECTOR.SUBJECT_OR_CLUSTER | subject or cluster / entity type / record type / subject cluster flag | varchar(127) | schema / SUBJECT_SELECTOR |
| SUBJECT_SELECTOR.MASTER_SUBJECT_ID | master subject id / master subject identifier / parent subject id / primary subject id / top-level subject id | varchar(127) | schema / SUBJECT_SELECTOR |
| SUBJECT_SELECTOR.ULT_MASTER_SUBJECT_ID | ult master subject id / ult master subject identifier / ultimate master subject id / root subject id / top-level master subject / final master subject id | varchar(127) | schema / SUBJECT_SELECTOR |
| SUBJECT_SELECTOR.CLUSTER_TYPE | cluster type / group type / subject cluster category / cluster code | varchar(127) | schema / SUBJECT_SELECTOR |
| SUBJECT_SELECTOR.CLUSTER_TYPE_DESC | cluster type desc / cluster type description / cluster description / group type name / cluster label | varchar(127) | schema / SUBJECT_SELECTOR |
| SUBJECT_SELECTOR.CLUSTER_LIST | cluster list / subject list / members of cluster / cluster contents | varchar(127) | schema / SUBJECT_SELECTOR |
| SUBJECT_SELECTOR.DEPARTMENT_CODE | department code / dept code / department identifier / academic department code | varchar(127) | schema / SUBJECT_SELECTOR |
| SUBJECT_SELECTOR.DEPARTMENT_NAME | department name / dept name / academic department / department title | varchar(127) | schema / SUBJECT_SELECTOR |
| SUBJECT_SELECTOR.SCHOOL_CODE | school code / campus code / institution code / school identifier | varchar(127) | schema / SUBJECT_SELECTOR |
| SUBJECT_SELECTOR.SCHOOL_NAME | school name / campus name / institution name / school title | varchar(127) | schema / SUBJECT_SELECTOR |
| SUBJECT_SELECTOR.SUBJECT_GROUP_ID | subject group id / subject group identifier / group id / subject category id / academic group identifier | varchar(127) | schema / SUBJECT_SELECTOR |
| SUBJECT_SELECTOR.WAREHOUSE_LOAD_DATE | warehouse load date / load date / etl date / data load timestamp / refresh date | varchar(255) | schema / SUBJECT_SELECTOR |

## SUBJECT_SUMMARY

Stores summary-level academic subject information including subject identifiers, titles, department and school affiliations, unit breakdowns (lecture, lab, prep), enrollment counts at various time points, and cluster relationships for a specific academic term.

恢复表名: subject summary / subject catalog / course summary / subject master / academic subject details / subject enrollment summary
SQL表别名: s, ss, t1, t2, t3

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SUBJECT_SUMMARY.SUBJECT_SUMMARY_KEY | subject summary key / summary key / subject key / unique subject identifier / subject record id | varchar(127) | dw_5377 |
| SUBJECT_SUMMARY.TERM_CODE | term code / academic term / semester code / term identifier / session code | varchar(127) | dw_4308, dw_3482, dw_1389, dw_3944, dw_4143, dw_4350, dw_1395, dw_1468 |
| SUBJECT_SUMMARY.SUBJECT_ID | subject id / subject identifier / subject code / course id / course number | varchar(127) | dw_4308, dw_3482, dw_1389, dw_3944, dw_4143, dw_3078, dw_4350, dw_1395 |
| SUBJECT_SUMMARY.SUBJECT_ID_SORT | subject id sort / subject identifier sort / sorted subject id / subject id for sorting / normalized subject id | varchar(127) | dw_3482 |
| SUBJECT_SUMMARY.SUBJECT_TITLE | subject title / course title / subject name / course name / subject description | varchar(127) | dw_4308, dw_3482, dw_1389, dw_3944, dw_4143, dw_3078, dw_4350, dw_1395 |
| SUBJECT_SUMMARY.SUBJECT_OR_CLUSTER | subject or cluster / subject cluster id / cluster subject id / subject group id | varchar(127) | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.MASTER_SUBJECT_ID | master subject id / master subject identifier / parent subject id / primary subject id / root subject id | varchar(127) | dw_5421 |
| SUBJECT_SUMMARY.MASTER_SUBJECT_ID_SORT | master subject id sort / master subject identifier sort / sorted master subject id / normalized master subject id | varchar(127) | dw_5364 |
| SUBJECT_SUMMARY.ULT_MASTER_SUBJECT_ID | ult master subject id / ult master subject identifier / ultimate master subject id / top level subject id / root master subject id / final master subject id | varchar(127) | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.CLUSTER_TYPE | cluster type / subject cluster type / grouping type / cluster category | varchar(127) | dw_3482 |
| SUBJECT_SUMMARY.CLUSTER_TYPE_DESC | cluster type desc / cluster type description / cluster type name / grouping type description / cluster category name | varchar(127) | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.CLUSTER_LIST | cluster list / subject cluster list / list of subjects in cluster / cluster members | varchar(127) | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.DEPARTMENT_CODE | department code / dept code / department identifier / offering department code | varchar(127) | dw_4308, dw_4350, dw_1395 |
| SUBJECT_SUMMARY.DEPARTMENT_NAME | department name / dept name / offering department / academic department | varchar(127) | dw_4308, dw_3482, dw_1389, dw_3944, dw_4143, dw_3078, dw_4350, dw_1395 |
| SUBJECT_SUMMARY.SCHOOL_CODE | school code / college code / school identifier / academic school code | varchar(127) | dw_4308, dw_4350 |
| SUBJECT_SUMMARY.SCHOOL_NAME | school name / college name / academic school / school of study | varchar(127) | dw_4308, dw_1389, dw_3944, dw_4143, dw_4350, dw_1395, dw_1468 |
| SUBJECT_SUMMARY.TOTAL_UNITS | total units / credit units / total credit hours / subject units | int | dw_4308, dw_3482, dw_1389, dw_3944, dw_4143, dw_5377, dw_4350, dw_1395 |
| SUBJECT_SUMMARY.LECTURE_UNITS | lecture units / lecture credits / class units / lecture hours | int | dw_3944 |
| SUBJECT_SUMMARY.LAB_UNITS | lab units / laboratory units / lab credits / practical units | int | dw_3078 |
| SUBJECT_SUMMARY.PREP_UNITS | prep units / preparation units / study units / independent work units | int | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.DESIGN_UNITS | design units / studio units / project units / creative work units | int | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.SUBJECT_ENROLLMENT_NUMBER | subject enrollment number / subject enrollment / enrolled students / subject headcount / number of students enrolled | int | dw_1389, dw_1468 |
| SUBJECT_SUMMARY.CLUSTER_ENROLLMENT_NUMBER | cluster enrollment number / cluster enrollment / cluster headcount / enrolled in cluster / total cluster students | int | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.SUBJECT_GROUP_ID | subject group id / subject group identifier / group identifier / subject category id / subject family id | varchar(127) | dw_4143 |
| SUBJECT_SUMMARY.SUBJECT_ENROLLMENT_FIRST_WEEK | subject enrollment first week / first week enrollment / week 1 enrollment / initial enrollment / enrollment at start | int | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.CLUSTER_ENROLLMENT_FIRST_WEEK | cluster enrollment first week / cluster first week enrollment / cluster week 1 enrollment / initial cluster enrollment | int | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.SUBJECT_ENROLLMENT_FIFTH_WEEK | subject enrollment fifth week / fifth week enrollment / week 5 enrollment / mid-term enrollment / enrollment at week 5 | int | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.CLUSTER_ENROLLMENT_FIFTH_WEEK | cluster enrollment fifth week / cluster fifth week enrollment / cluster week 5 enrollment / mid-term cluster enrollment | int | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.SUBJECT_ENROLLMENT_CREDIT | subject enrollment credit / credit enrollment / enrolled for credit / credit-seeking students / enrollment for credit | int | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.SUBJECT_ENROLLMENT_LISTEN | subject enrollment listen / listen enrollment / audit enrollment / non-credit enrollment / listening students | int | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.CLUSTER_ENROLLMENT_CREDIT | cluster enrollment credit / cluster credit enrollment / cluster enrolled for credit / cluster credit-seeking students | int | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.CLUSTER_ENROLLMENT_LISTEN | cluster enrollment listen | int | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.SUBJECT_ENROLLMENT_1ST_CREDIT | subject enrollment 1 st credit | int | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.SUBJECT_ENROLLMENT_1ST_LISTEN | subject enrollment 1 st listen | int | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.CLUSTER_ENROLLMENT_1ST_CREDIT | cluster enrollment 1 st credit | int | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.CLUSTER_ENROLLMENT_1ST_LISTEN | cluster enrollment 1 st listen | int | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.SUBJECT_ENROLLMENT_5TH_CREDIT | subject enrollment 5 th credit | int | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.SUBJECT_ENROLLMENT_5TH_LISTEN | subject enrollment 5 th listen | int | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.CLUSTER_ENROLLMENT_5TH_CREDIT | cluster enrollment 5 th credit | int | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.CLUSTER_ENROLLMENT_5TH_LISTEN | cluster enrollment 5 th listen | int | schema / SUBJECT_SUMMARY |
| SUBJECT_SUMMARY.WAREHOUSE_LOAD_DATE | warehouse load date | varchar(255) | schema / SUBJECT_SUMMARY |

## TIME_DAY

A daily grain time dimension table that maps calendar dates to fiscal periods, academic terms, and financial aid years, serving as a lookup for date-based reporting and joining with fact tables.

恢复表名: time day / Daily Time Dimension / Calendar Day / Date Dimension / Time Dimension / Day Table
SQL表别名: t, t0, t1, t2, td

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| TIME_DAY.FISCAL_PERIOD | fiscal period / Fiscal Month / Fiscal Period Code / Fiscal Period ID / Fiscal Period Key | varchar(127) | dw_3131 |
| TIME_DAY.FISCAL_YEAR | fiscal year / Fiscal Year Code / Fiscal Year ID / Fiscal Year Key | varchar(127) | dw_2603 |
| TIME_DAY.FISCAL_PERIOD_DESCRIPTION | fiscal period description / Fiscal Period Name / Fiscal Period Label / Fiscal Period Text | varchar(127) | schema / TIME_DAY |
| TIME_DAY.CALENDAR_PERIOD | calendar period / Calendar Month / Calendar Period Code / Calendar Period ID / Calendar Period Key | varchar(127) | schema / TIME_DAY |
| TIME_DAY.CALENDAR_PERIOD_DESCRIPTION | calendar period description / Calendar Month Name / Calendar Period Label / Calendar Period Text | varchar(127) | schema / TIME_DAY |
| TIME_DAY.CALENDAR_YEAR | calendar year / Year / Calendar Year Code / Calendar Year ID / Calendar Year Key | varchar(127) | dw_3056, dw_3131, dw_3307, dw_3312, dw_3414, dw_3686 |
| TIME_DAY.START_DATE | start date / Period Start Date / Fiscal Period Start Date / Term Start Date / Beginning Date | varchar(255) | dw_2574, dw_2971 |
| TIME_DAY.END_DATE | end date / Period End Date / Fiscal Period End Date / Term End Date / Ending Date | varchar(255) | dw_2574, dw_2971 |
| TIME_DAY.CALENDAR_DATE | calendar date / Date / Day / Specific Date / Date Key | varchar(255) | dw_3056, dw_2603, dw_2837, dw_3150, dw_3307, dw_3312, dw_3414, dw_3686 |
| TIME_DAY.DAY_OF_WEEK | day of week / Weekday / Day Name / Day of the Week | varchar(127) | dw_3056, dw_2837, dw_3150, dw_3307, dw_3312, dw_3414, dw_3686 |
| TIME_DAY.FINANCIAL_AID_YEAR | financial aid year / Aid Year / Financial Aid Year Code / Aid Year ID / Aid Year Key | varchar(127) | schema / TIME_DAY |
| TIME_DAY.FINANCIAL_AID_YEAR_DESC | financial aid year desc / financial aid year description / Aid Year Description / Aid Year Name / Aid Year Label | varchar(127) | schema / TIME_DAY |
| TIME_DAY.ACADEMIC_YEAR | academic year / Academic Year Code / Academic Year ID / Academic Year Key | varchar(127) | dw_3131, dw_4558 |
| TIME_DAY.ACADEMIC_TERM_CODE | academic term code / Term Code / Academic Term ID / Academic Term Key / Term Key | varchar(127) | dw_2574, dw_2603, dw_4558, dw_2837, dw_2971, dw_3150 |
| TIME_DAY.ACADEMIC_TERM_DESCRIPTION | academic term description / Term Description / Academic Term Name / Term Name / Academic Term Label | varchar(127) | dw_4558 |

## TIME_MONTH

A dimension table that maps fiscal periods to calendar months, quarters, years, and academic terms, providing start/end dates and descriptive labels for time-based analysis.

恢复表名: time month / Monthly Time Dimension / Fiscal Month / Calendar Month / Month Calendar / Time Month Dimension
SQL表别名: t1, tm

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| TIME_MONTH.IS_CLOSING_PERIOD | is closing period / Closing Period Flag / Is Closing / Period Closing Status / Closing Indicator | varchar(127) | schema / TIME_MONTH |
| TIME_MONTH.FISCAL_PERIOD_SELECTOR | fiscal period selector / Fiscal Period Label / Fiscal Month Selector / Fiscal Period Display / Fiscal Month Description | varchar(127) | schema / TIME_MONTH |
| TIME_MONTH.IS_CURRENT_FISCAL_YEAR | is current fiscal year / Current Fiscal Year Flag / Is Current FY / Current Year Indicator / Fiscal Year Status | varchar(127) | schema / TIME_MONTH |
| TIME_MONTH.TIME_MONTH_KEY | time month key / Month Key / Time Month ID / Month Identifier / Fiscal Month Key | varchar(127) | schema / TIME_MONTH |
| TIME_MONTH.FISCAL_PERIOD | fiscal period / Fiscal Month / Fiscal Period Code / Fiscal Month Code / Fiscal Period ID | varchar(127) | dw_2614, dw_2735, dw_3131, dw_3099 |
| TIME_MONTH.FISCAL_PERIOD_DESCRIPTION | fiscal period description / Fiscal Period Name / Fiscal Month Description / Fiscal Period Label / Fiscal Month Name | varchar(127) | dw_3131 |
| TIME_MONTH.FISCAL_YEAR | fiscal year / FY / Fiscal Year Code / Fiscal Year Number | varchar(127) | dw_2614, dw_2735, dw_3099, dw_3086 |
| TIME_MONTH.FISCAL_YEAR_QUARTER | fiscal year quarter / Fiscal Quarter Description / Fiscal Quarter Name / Fiscal Year Quarter Label / Fiscal Quarter Display | varchar(127) | schema / TIME_MONTH |
| TIME_MONTH.FY_QUARTER_CODE | fy quarter code / Fiscal Quarter Code / FY Quarter / Fiscal Quarter ID / Quarter Code | varchar(127) | schema / TIME_MONTH |
| TIME_MONTH.CALENDAR_PERIOD | calendar period / Calendar Month Code / Calendar Period Code / Calendar Month ID / Month Code | varchar(127) | schema / TIME_MONTH |
| TIME_MONTH.CALENDAR_PERIOD_DESCRIPTION | calendar period description / Calendar Month Description / Calendar Period Name / Calendar Month Label / Month Description | varchar(127) | dw_2614 |
| TIME_MONTH.CALENDAR_YEAR | calendar year / Year / Calendar Year Code / Year Number | varchar(127) | dw_2735, dw_3099 |
| TIME_MONTH.START_DATE | start date / Month Start Date / Period Start Date / First Day of Month | varchar(255) | schema / TIME_MONTH |
| TIME_MONTH.END_DATE | end date / Month End Date / Period End Date / Last Day of Month | varchar(255) | schema / TIME_MONTH |
| TIME_MONTH.CALENDAR_MONTH | calendar month / Month Number / Calendar Month Number / Month / Month Index | varchar(127) | dw_2614, dw_2735, dw_3099, dw_3086 |
| TIME_MONTH.CALENDAR_MONTH_NAME | calendar month name / Month Name / Month Label / Month Title | varchar(127) | dw_2614 |
| TIME_MONTH.IS_CURRENT_FISCAL_PERIOD | is current fiscal period / Current Fiscal Period Flag / Is Current Period / Current Month Indicator / Fiscal Period Status | varchar(127) | schema / TIME_MONTH |
| TIME_MONTH.IS_PREVIOUS_FISCAL_PERIOD | is previous fiscal period / Previous Fiscal Period Flag / Is Previous Period / Prior Month Indicator / Previous Month Status | varchar(127) | schema / TIME_MONTH |
| TIME_MONTH.ACADEMIC_YEAR | academic year / Academic Year Code / School Year / Academic Year Number | varchar(127) | schema / TIME_MONTH |
| TIME_MONTH.ACADEMIC_TERM | academic term / Academic Term Code / Term Code / Academic Term ID / School Term Code | varchar(127) | schema / TIME_MONTH |
| TIME_MONTH.ACADEMIC_TERM_DESCRIPTION | academic term description / Academic Term Name / Term Description / Academic Term Label / School Term Name | varchar(127) | schema / TIME_MONTH |
| TIME_MONTH.FINANCIAL_AID_YEAR | financial aid year / Aid Year / Financial Aid Year Code / Aid Year Number | varchar(127) | schema / TIME_MONTH |
| TIME_MONTH.FINANCIAL_AID_YEAR_DESC | financial aid year desc / financial aid year description / Aid Year Description / Financial Aid Year Label / Aid Year Name | varchar(127) | schema / TIME_MONTH |

## TIME_QUARTER

Dimension table providing fiscal and calendar quarter definitions, including start/end dates, certification schedules, and status flags for time-based reporting.

恢复表名: time quarter / fiscal quarter dimension / quarter calendar / fiscal period quarter / quarter reference table
SQL表别名: t0, tq

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| TIME_QUARTER.FISCAL_YEAR | fiscal year / fy year / fiscal year number / accounting year | varchar(127) | dw_2614, dw_3086 |
| TIME_QUARTER.FY_QUARTER_CODE | fy quarter code / fiscal quarter code / fy quarter / fiscal period code / quarter identifier | varchar(127) | dw_2614, dw_3086 |
| TIME_QUARTER.FY_QUARTER_NAME | fy quarter name / fiscal quarter name / fy quarter description / quarter label / fiscal period name | varchar(127) | schema / TIME_QUARTER |
| TIME_QUARTER.CY_QUARTER_CODE | cy quarter code / calendar quarter code / cy quarter / calendar period code / civil quarter code | varchar(127) | schema / TIME_QUARTER |
| TIME_QUARTER.CY_QUARTER_NAME | cy quarter name / calendar quarter name / cy quarter description / calendar period name / civil quarter label | varchar(127) | schema / TIME_QUARTER |
| TIME_QUARTER.CALENDAR_YEAR | calendar year / cy year / civil year / year | varchar(127) | dw_2614 |
| TIME_QUARTER.QUARTER_START_DATE | quarter start date / quarter start / fiscal quarter start date / period start date / quarter beginning | varchar(255) | dw_2614 |
| TIME_QUARTER.QUARTER_END_DATE | quarter end date / quarter end / fiscal quarter end date / period end date / quarter closing date | varchar(255) | schema / TIME_QUARTER |
| TIME_QUARTER.QUARTER_START_FP | quarter start fp / quarter start fiscal period / start fp / fiscal period start / quarter start month code | varchar(127) | schema / TIME_QUARTER |
| TIME_QUARTER.QUARTER_END_FP | quarter end fp / quarter end fiscal period / end fp / fiscal period end / quarter end month code | varchar(127) | schema / TIME_QUARTER |
| TIME_QUARTER.QUARTER_CERT_OPEN | quarter cert open / certification open date / cert open / quarter cert start / certification period start | varchar(255) | schema / TIME_QUARTER |
| TIME_QUARTER.QUARTER_CERT_EXPECTED | quarter cert expected / certification expected date / cert expected / expected cert date / certification target date | varchar(255) | schema / TIME_QUARTER |
| TIME_QUARTER.QUARTER_CERT_DUE | quarter cert due / certification due date / cert due / cert deadline / certification deadline | varchar(255) | schema / TIME_QUARTER |
| TIME_QUARTER.IS_CURRENT_QUARTER | is current quarter / current quarter flag / is current / current quarter indicator / active quarter | varchar(127) | schema / TIME_QUARTER |
| TIME_QUARTER.IS_NEXT_QUARTER | is next quarter / next quarter flag / is next / next quarter indicator / upcoming quarter | varchar(127) | schema / TIME_QUARTER |
| TIME_QUARTER.IS_PREVIOUS_QUARTER | is previous quarter / previous quarter flag / is previous / last quarter indicator / prior quarter | varchar(127) | schema / TIME_QUARTER |
| TIME_QUARTER.IS_PAST_QUARTER | is past quarter / past quarter flag / is past / historical quarter indicator / closed quarter | varchar(127) | schema / TIME_QUARTER |
| TIME_QUARTER.IS_FUTURE_QUARTER | is future quarter / future quarter flag / is future / upcoming quarter indicator / planned quarter | varchar(127) | schema / TIME_QUARTER |
| TIME_QUARTER.PAYROLL_EDACCA_CERT_SCHED_KEY | payroll edacca cert sched key / payroll cert schedule key / edacca cert key / payroll certification period / cert schedule identifier | varchar(127) | schema / TIME_QUARTER |
| TIME_QUARTER.WAREHOUSE_LOAD_DATE | warehouse load date / load date / etl date / data load timestamp / warehouse update date | varchar(255) | schema / TIME_QUARTER |

## TIP_DETAIL

Stores detailed records of course materials (textbooks, reserves) associated with specific subject offerings, including material status, ISBN, and warehouse load metadata.

恢复表名: tip detail / Textbook Information Program Detail / Course Material Detail / Library Reserve Material Detail / TIP Material Detail / Course Textbook Detail
SQL表别名: d, t, t0, t1, t2, td

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| TIP_DETAIL.TIP_SUBJECT_OFFERED_KEY | tip subject offered key / Subject Offered Key / Course Offering Key / Subject Offered ID / Offering Key | varchar(127) | dw_3243, dw_3466, dw_3562, dw_3612, dw_3619, dw_3627, dw_3668, dw_3764 |
| TIP_DETAIL.TIP_MATERIAL_KEY | tip material key / Material Key / Course Material Key / Textbook Key / Material ID | varchar(127) | dw_3243, dw_3466, dw_3562, dw_3612, dw_3619, dw_3627, dw_3668, dw_3764 |
| TIP_DETAIL.TIP_MATERIAL_STATUS_KEY | tip material status key / Material Status Key / Course Material Status / Textbook Status Key / Material Status Code | varchar(127) | dw_3243, dw_2895, dw_3466, dw_3562, dw_3612, dw_3619, dw_3627, dw_3668 |
| TIP_DETAIL.TERM_CODE | term code / Academic Term Code / Term / Semester Code / Academic Year Term | varchar(127) | dw_3243, dw_3466, dw_3562, dw_3612, dw_3619, dw_3627, dw_3668, dw_3764 |
| TIP_DETAIL.SUBJECT_ID | subject id / subject identifier / Course ID / Course Number / Subject Code | varchar(127) | dw_3243, dw_2895, dw_3466, dw_3562, dw_3612, dw_3619, dw_3627, dw_3668 |
| TIP_DETAIL.ISBN | isbn / International Standard Book Number / Book ISBN / Textbook ISBN / Material ISBN | varchar(127) | dw_3243, dw_3562, dw_3627, dw_3668, dw_3937, dw_4363 |
| TIP_DETAIL.RECORD_COUNT | record count / Number of Records / Material Count / Row Count / Count | int | dw_2895, dw_3466, dw_3612, dw_3619, dw_3764, dw_4363, dw_4364 |
| TIP_DETAIL.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date / Last Updated Date | varchar(255) | dw_2895 |

## TIP_MATERIAL

Stores master data for course materials (textbooks/ebooks) including bibliographic details, pricing, and source information, linked to course offerings via TIP_DETAIL.

恢复表名: tip material / Textbook Information Project Material / Course Materials / Textbook Catalog / Material Master / Book Inventory / Course Textbooks
SQL表别名: m, tm

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| TIP_MATERIAL.TIP_MATERIAL_KEY | tip material key / Material Key / Material ID / Textbook Key / Book ID / Material Identifier | varchar(127) | dw_3191, dw_2904, dw_2989, dw_2913, dw_3120, dw_3426, dw_3973, dw_4005 |
| TIP_MATERIAL.ISBN | isbn / International Standard Book Number / Book ISBN / Material ISBN / ISBN Number | varchar(127) | schema / TIP_MATERIAL |
| TIP_MATERIAL.TITLE | title / Material Title / Book Title / Textbook Title / Course Material Name | varchar(127) | schema / TIP_MATERIAL |
| TIP_MATERIAL.AUTHOR | author / Material Author / Book Author / Textbook Author / Author Name | varchar(127) | dw_2904, dw_3120, dw_3973, dw_4005, dw_4045, dw_4129, dw_4379 |
| TIP_MATERIAL.EDITION | edition / Material Edition / Book Edition / Textbook Edition / Edition Number | varchar(127) | schema / TIP_MATERIAL |
| TIP_MATERIAL.PUBLISHER | publisher / Material Publisher / Book Publisher / Textbook Publisher / Publisher Name | varchar(127) | dw_2989, dw_3426 |
| TIP_MATERIAL.YEAR | year / Publication Year / Material Year / Book Year / Year Published | varchar(127) | dw_3191, dw_2913 |
| TIP_MATERIAL.NEW_SHELF_PRICE | new shelf price / New Price / New Book Price / List Price | int | dw_3191, dw_2904, dw_2989, dw_2913, dw_3120, dw_3426, dw_3973, dw_4005 |
| TIP_MATERIAL.USED_SHELF_PRICE | used shelf price / Used Price / Used Book Price / Second-hand Price | int | dw_3191, dw_2989, dw_3426, dw_3188 |
| TIP_MATERIAL.RENTAL_NEW_PRICE | rental new price / New Rental Price / Rental Price New / New Rent Cost | int | schema / TIP_MATERIAL |
| TIP_MATERIAL.RENTAL_USED_PRICE | rental used price / Used Rental Price / Rental Price Used / Used Rent Cost | int | schema / TIP_MATERIAL |
| TIP_MATERIAL.MATERIAL_INFO_SOURCE | material info source / Info Source / Material Source / Data Source / Source Type | varchar(127) | dw_3191, dw_2904, dw_2913, dw_3120, dw_3973, dw_4005, dw_4045, dw_4129 |

## TIP_MATERIAL_STATUS

Lookup table defining the status codes and descriptions for course materials (e.g., required, optional, recommended) used in the TIP (Textbook Information Program) system.

恢复表名: tip material status / Material Status Lookup / Course Material Status / Textbook Status / Required Material Status
SQL表别名: tms, tms2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| TIP_MATERIAL_STATUS.TIP_MATERIAL_STATUS_KEY | tip material status key / Material Status Key / Status ID / Material Status Identifier / TIP Status Key | varchar(127) | dw_1880, dw_1884, dw_319, dw_3234, dw_3505, dw_3587, dw_3637, dw_5506 |
| TIP_MATERIAL_STATUS.TIP_MATERIAL_STATUS_CODE | tip material status code / Material Status Code / Status Code / Short Status Code / TIP Status Code | varchar(127) | schema / TIP_MATERIAL_STATUS |
| TIP_MATERIAL_STATUS.TIP_MATERIAL_STATUS | tip material status / Material Status Description / Status Description / Material Status Name / Textbook Status / Required Material Status | varchar(127) | dw_1880, dw_1884, dw_319, dw_3234, dw_3505, dw_3587, dw_3637, dw_5506 |
| TIP_MATERIAL_STATUS.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date | varchar(255) | schema / TIP_MATERIAL_STATUS |

## TIP_SUBJECT_OFFERED

Stores detailed information about academic subjects (courses) offered in specific terms, including enrollment counts, responsible faculty, offering departments, and flags indicating whether course materials are associated with the subject in the TIP system.

恢复表名: tip subject offered / TIP Course Offerings / Textbook Information Project Subject Offered / Course Offerings with Materials / TIP Enrollment Data
SQL表别名: s, so, t, t0, t1, t2, tso

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| TIP_SUBJECT_OFFERED.TIP_SUBJECT_OFFERED_KEY | tip subject offered key / TIP Subject Key / Subject Offered Key / TIP Course Key / Primary Key / Record ID | varchar(127) | dw_2293, dw_1958, dw_3668, dw_783, dw_1040, dw_1066, dw_1119 |
| TIP_SUBJECT_OFFERED.TERM_CODE | term code / Term / Academic Term / Semester / Offering Term / Academic Period | varchar(127) | dw_2293, dw_1954, dw_1958, dw_2246, dw_2270, dw_5364, dw_783, dw_1040 |
| TIP_SUBJECT_OFFERED.IS_NO_COURSE_MATERIAL | is no course material / is number course material / No Course Material Flag / Has Materials / Course Material Indicator / Material Status / Textbook Required | varchar(127) | dw_2293, dw_1954, dw_783, dw_1040, dw_1066, dw_1119 |
| TIP_SUBJECT_OFFERED.MASTER_COURSE_NUMBER | master course number / Department Code / Course Number / Department ID / Subject Number | varchar(127) | dw_1954 |
| TIP_SUBJECT_OFFERED.MASTER_COURSE_NUMBER_SORT | master course number sort / Master Course Sort / Sorted Department Code / Course Number Sort Key | varchar(127) | schema / TIP_SUBJECT_OFFERED |
| TIP_SUBJECT_OFFERED.MASTER_COURSE_NUMBER_DESC | master course number desc / master course number description / Master Course Description / Department Name / Course Name / Department Description | varchar(127) | schema / TIP_SUBJECT_OFFERED |
| TIP_SUBJECT_OFFERED.MASTER_SUBJECT_ID | master subject id / master subject identifier / Master Course ID / Department Course Code / Full Course Identifier | varchar(127) | dw_2246 |
| TIP_SUBJECT_OFFERED.MASTER_SUBJECT_ID_SORT | master subject id sort / master subject identifier sort / Master Subject Sort / Sorted Master Subject ID / Master Course Sort Key | varchar(127) | dw_5364 |
| TIP_SUBJECT_OFFERED.COURSE_NUMBER | course number / Department Code / Course ID / Subject Number | varchar(127) | dw_2270 |
| TIP_SUBJECT_OFFERED.COURSE_NUMBER_SORT | course number sort / Course Sort / Sorted Course Number / Course Number Sort Key | varchar(127) | schema / TIP_SUBJECT_OFFERED |
| TIP_SUBJECT_OFFERED.COURSE_NUMBER_DESC | course number desc / course number description / Course Description / Department Name / Course Name / Department Description | varchar(127) | dw_3668 |
| TIP_SUBJECT_OFFERED.SUBJECT_ID | subject id / subject identifier / Course ID / Subject Code / Course Identifier | varchar(127) | dw_2293, dw_1958, dw_2246, dw_2270, dw_783 |
| TIP_SUBJECT_OFFERED.SUBJECT_ID_SORT | subject id sort / subject identifier sort / Subject Sort / Sorted Subject ID / Subject ID Sort Key | varchar(127) | dw_2771 |
| TIP_SUBJECT_OFFERED.SUBJECT_TITLE | subject title / Course Title / Course Name / Subject Name / Course Description | varchar(127) | dw_2293, dw_1954, dw_2270, dw_3668, dw_783, dw_1040, dw_1066, dw_1119 |
| TIP_SUBJECT_OFFERED.OFFER_DEPT_CODE | offer dept code / offer department code / Offering Department Code / Department Code / Department ID | varchar(127) | dw_2293, dw_1954, dw_2246, dw_2270, dw_3668, dw_783, dw_1040, dw_1066 |
| TIP_SUBJECT_OFFERED.OFFER_DEPT_NAME | offer dept name / offer department name / Offering Department Name / Department Name / Department | varchar(127) | dw_2293, dw_1954, dw_1958, dw_2246, dw_3668, dw_5364, dw_783, dw_1040 |
| TIP_SUBJECT_OFFERED.OFFER_SCHOOL_NAME | offer school name / Offering School Name / School Name / School / Academic School | varchar(127) | dw_2293, dw_1954, dw_783 |
| TIP_SUBJECT_OFFERED.RESPONSIBLE_FACULTY_NAME | responsible faculty name / Responsible Faculty / Faculty Name / Instructor Name / Professor Name / Course Instructor | varchar(127) | dw_2293, dw_1958, dw_783, dw_1040, dw_1066, dw_1119 |
| TIP_SUBJECT_OFFERED.RESPONSIBLE_FACULTY_MIT_ID | responsible faculty mit id / responsible faculty mit identifier / Faculty MIT ID / Instructor ID / Professor ID / Responsible Faculty ID | varchar(127) | dw_1958 |
| TIP_SUBJECT_OFFERED.NUM_ENROLLED_STUDENTS | num enrolled students / number enrolled students / Enrolled Students / Enrollment Count / Number of Students / Student Count / Enrollment | int | dw_2293, dw_1954, dw_2246, dw_2270, dw_3668, dw_5364, dw_2771, dw_783 |
| TIP_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / Warehouse Date / ETL Date | varchar(255) | schema / TIP_SUBJECT_OFFERED |

## TOP_LEVEL_DOMAIN

Reference table defining standard top-level domain (TLD) codes and their corresponding organizational or functional descriptions.

恢复表名: top level domain / TLD / Domain Types / Internet Domain Categories / Top Level Domain Reference / Domain Suffixes
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| TOP_LEVEL_DOMAIN.TOP_LEVEL_DOMAIN_KEY | top level domain key / TLD Key / Domain Code / TLD Identifier / Domain Suffix / TLD Code | varchar(127) | schema / TOP_LEVEL_DOMAIN |
| TOP_LEVEL_DOMAIN.TOP_LEVEL_DOMAIN | top level domain / TLD / Domain Name / Domain Type / TLD Value | varchar(127) | schema / TOP_LEVEL_DOMAIN |
| TOP_LEVEL_DOMAIN.TOP_LEVEL_DOMAIN_DESCRIPTION | top level domain description / TLD Description / Domain Description / Domain Meaning / TLD Label / Domain Category Name | varchar(127) | schema / TOP_LEVEL_DOMAIN |
| TOP_LEVEL_DOMAIN.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date / Warehouse Date / Last Updated | varchar(255) | schema / TOP_LEVEL_DOMAIN |

## WAREHOUSE_USERS

Stores demographic, contact, and organizational details for users and employees within the MIT warehouse system.

恢复表名: warehouse users / user directory / employee list / staff roster / MIT users / personnel table
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| WAREHOUSE_USERS.MIT_ID | mit id / mit identifier / employee ID / user ID / staff ID / person ID / unique identifier | varchar(127) | schema / WAREHOUSE_USERS |
| WAREHOUSE_USERS.KRB_NAME | krb name / Kerberos name / login name / username / user account / netid / login ID | varchar(127) | schema / WAREHOUSE_USERS |
| WAREHOUSE_USERS.KRB_NAME_UPPERCASE | krb name uppercase / uppercase login / Kerberos name upper / username upper / login name uppercase / netid upper | varchar(127) | schema / WAREHOUSE_USERS |
| WAREHOUSE_USERS.LAST_NAME | last name / surname / family name / last name of user / employee last name | varchar(127) | schema / WAREHOUSE_USERS |
| WAREHOUSE_USERS.FIRST_NAME | first name / given name / forename / user first name / employee first name | varchar(127) | schema / WAREHOUSE_USERS |
| WAREHOUSE_USERS.MIDDLE_NAME | middle name / middle initial / second name / user middle name / employee middle name | varchar(127) | schema / WAREHOUSE_USERS |
| WAREHOUSE_USERS.EMAIL_ADDRESS | email address / email / e-mail / user email / contact email / mail address | varchar(127) | schema / WAREHOUSE_USERS |
| WAREHOUSE_USERS.OFFICE_LOCATION | office location / office number / room number / work location / office code / physical location | varchar(127) | schema / WAREHOUSE_USERS |
| WAREHOUSE_USERS.OFFICE_PHONE | office phone / phone number / work phone / contact number / telephone / office contact | varchar(127) | schema / WAREHOUSE_USERS |
| WAREHOUSE_USERS.UNIT_ID | unit id / unit identifier / department ID / organization ID / unit code / dept ID / organizational unit ID | varchar(127) | schema / WAREHOUSE_USERS |
| WAREHOUSE_USERS.UNIT_NAME | unit name / department name / organization name / dept name / affiliation / department | varchar(127) | schema / WAREHOUSE_USERS |
| WAREHOUSE_USERS.TITLE | title / job title / position / role / professional title / user title / employee title | varchar(127) | schema / WAREHOUSE_USERS |
| WAREHOUSE_USERS.YEAR | year / academic year / fiscal year / year of record / user year | varchar(127) | schema / WAREHOUSE_USERS |
| WAREHOUSE_USERS.TYPE | type / user type / employee type / account type / personnel type / user category / staff type | varchar(127) | schema / WAREHOUSE_USERS |
| WAREHOUSE_USERS.APPOINTMENT_TYPE | appointment type / employment type / appointment status / job appointment / user appointment / staff appointment | varchar(127) | schema / WAREHOUSE_USERS |

## ZIP_CANADA

Reference table containing Canadian postal codes and their associated geographic locations, including city, province, and administrative details.

恢复表名: zip canada / Canadian Postal Codes / Canada ZIP Codes / Canadian Address Lookup / Postal Code Reference / Canada Location Data
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ZIP_CANADA.POSTAL_CODE | postal code / ZIP Code / Canada Postal Code / Postal Code Number / Address Code | varchar(127) | schema / ZIP_CANADA |
| ZIP_CANADA.CITY_NAME | city name / City / Town / Village / Community / Location Name / Municipality | varchar(127) | schema / ZIP_CANADA |
| ZIP_CANADA.CITY_TYPE | city type / Location Type / Settlement Type / Administrative Type / Community Classification | varchar(127) | schema / ZIP_CANADA |
| ZIP_CANADA.PROVINCE_ABBR | province abbr / Province Abbreviation / Province Code / State Abbreviation / Region Code / Prov Abbr | varchar(127) | schema / ZIP_CANADA |
| ZIP_CANADA.PROVINCE_NAME | province name / Province / State / Region / Territory | varchar(127) | schema / ZIP_CANADA |
| ZIP_CANADA.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date / Last Updated / Refresh Date / Warehouse Date | varchar(255) | schema / ZIP_CANADA |

## ZIP_USA

Reference table containing US ZIP code details including city, county, state, and postal type information.

恢复表名: zip usa / US ZIP Codes / ZIP Code Reference / Postal Codes / US Postal Address Data / ZIP Lookup / US Geographic ZIP Data
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ZIP_USA.STATE_NAME | state name / State / US State / Province / Territory | varchar(127) | schema / ZIP_USA |
| ZIP_USA.WAREHOUSE_LOAD_DATE | warehouse load date / Load Date / Data Load Date / ETL Date / Last Updated / Refresh Date | varchar(255) | schema / ZIP_USA |
| ZIP_USA.ZIP_CODE | zip code / ZIP / Postal Code / USPS Code / Postal Zone | varchar(127) | schema / ZIP_USA |
| ZIP_USA.ZIP_TYPE | zip type / Postal Type / ZIP Category / Code Type / Delivery Type | varchar(127) | schema / ZIP_USA |
| ZIP_USA.CITY_NAME | city name / City / Town / Municipality / Locality / Place Name | varchar(127) | schema / ZIP_USA |
| ZIP_USA.CITY_TYPE | city type / City Classification / Locality Type / Place Type / Urban/Rural Type | varchar(127) | schema / ZIP_USA |
| ZIP_USA.COUNTY_NAME | county name / County / Parish / Borough / Municipality / Regional County | varchar(127) | schema / ZIP_USA |
| ZIP_USA.STATE_ABBR | state abbr / State Code / State Abbreviation / 2-Letter State / USPS State Code | varchar(127) | schema / ZIP_USA |

## ZPM_ROOMS_LOAD

Stores detailed information about building rooms, including their location, usage, access levels, and associated organizational units.

恢复表名: zpm rooms load / Rooms Load / ZPM Rooms / Room Access Data / Building Room Details / Space Usage Load
SQL表别名: t0, t1, zr

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ZPM_ROOMS_LOAD.BUILDING_ROOM | building room / Room ID / Room Number / Room Identifier / Building Room Code | varchar(127) | dw_2741, dw_3190, dw_3315, dw_3359, dw_3521, dw_3626, dw_3659, dw_3698 |
| ZPM_ROOMS_LOAD.BUILDING_COMPONENT | building component / Building Number / Building ID / Component ID / Building Part | varchar(127) | dw_2741, dw_3190, dw_3315, dw_3359, dw_3521, dw_3626, dw_3659, dw_3698 |
| ZPM_ROOMS_LOAD.FLOOR | floor / Floor Number / Level / Storey / Floor Level | varchar(127) | dw_2741, dw_3190, dw_3315, dw_3359, dw_3521, dw_3626, dw_3659, dw_3698 |
| ZPM_ROOMS_LOAD.SPACE_USAGE | space usage / Room Usage / Usage Type / Room Type / Function / Purpose | varchar(127) | dw_2741, dw_3190, dw_3315, dw_3359, dw_3521, dw_3626, dw_3659, dw_3698 |
| ZPM_ROOMS_LOAD.SPACE_UNIT_CODE | space unit code / Space Code / Unit Code / Space Identifier / Space Unit ID | varchar(127) | dw_2741, dw_3190, dw_3315, dw_3359, dw_3521, dw_3626, dw_3659, dw_3698 |
| ZPM_ROOMS_LOAD.HR_ORG_UNIT_ID | hr org unit id / hr org unit identifier / Organization Unit ID / Org Unit ID / HR Organization ID / Department ID / Organization ID | varchar(127) | dw_2741, dw_3190, dw_3315, dw_3359, dw_3521, dw_3626, dw_3659, dw_3698 |
| ZPM_ROOMS_LOAD.ACCESS_LEVEL | access level / Security Level / Access Restriction / Clearance Level / Access Code | varchar(127) | dw_2741, dw_3190, dw_3315, dw_3359, dw_3521, dw_3626, dw_3659, dw_3698 |

## 表关系与连接依据

- ACADEMIC_TERMS.ACADEMIC_TERMS_KEY ↔ ACADEMIC_TERMS_ALL.ACADEMIC_TERMS_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS.ACADEMIC_YEAR ↔ TIME_MONTH.ACADEMIC_YEAR; profile_name_value_compatibility
- ACADEMIC_TERMS.FINANCIAL_AID_YEAR ↔ TIME_MONTH.FINANCIAL_AID_YEAR; profile_name_value_compatibility
- ACADEMIC_TERMS.IS_CURRENT_TERM ↔ ACADEMIC_TERMS_ALL.IS_CURRENT_TERM; profile_name_value_compatibility
- ACADEMIC_TERMS.IS_CURRENT_TERM ↔ ACADEMIC_TERM_PARAMETER.IS_CURRENT_TERM; profile_name_value_compatibility
- ACADEMIC_TERMS.TERM_CODE ↔ ACADEMIC_TERMS_ALL.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS.TERM_CODE ↔ ACADEMIC_TERM_PARAMETER.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS.TERM_CODE ↔ COURSE_CATALOG_SUBJECT_OFFERED.EFFECTIVE_TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS.TERM_CODE ↔ COURSE_CATALOG_SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS.TERM_CODE ↔ IAP_SUBJECT_DETAIL.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS.TERM_CODE ↔ LIBRARY_RESERVE_MATRL_DETAIL.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS.TERM_CODE ↔ LIBRARY_SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS.TERM_CODE ↔ SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS.TERM_CODE ↔ SUBJECT_OFFERED_SUMMARY.TERM_CODE; declared_or_materialized_relationship
- ACADEMIC_TERMS.TERM_CODE ↔ SUBJECT_SUMMARY.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS.TERM_CODE ↔ TIP_DETAIL.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS.TERM_CODE ↔ TIP_SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS.TERM_START_DATE ↔ TIME_DAY.CALENDAR_DATE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS.TERM_STATUS_INDICATOR ↔ ACADEMIC_TERMS_ALL.TERM_STATUS_INDICATOR; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ BUILDINGS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ FAC_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ FAC_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ FAC_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ FCLT_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.IS_CURRENT_TERM ↔ ACADEMIC_TERM_PARAMETER.IS_CURRENT_TERM; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.TERM_CODE ↔ ACADEMIC_TERM_PARAMETER.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS_ALL.TERM_CODE ↔ COURSE_CATALOG_SUBJECT_OFFERED.EFFECTIVE_TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS_ALL.TERM_CODE ↔ COURSE_CATALOG_SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS_ALL.TERM_CODE ↔ IAP_SUBJECT_DETAIL.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS_ALL.TERM_CODE ↔ LIBRARY_RESERVE_MATRL_DETAIL.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS_ALL.TERM_CODE ↔ LIBRARY_SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS_ALL.TERM_CODE ↔ SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS_ALL.TERM_CODE ↔ SUBJECT_SUMMARY.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS_ALL.TERM_CODE ↔ TIP_DETAIL.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS_ALL.TERM_CODE ↔ TIP_SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ BUILDINGS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ FAC_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ FAC_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ FAC_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ FCLT_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERMS_ALL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ACADEMIC_TERM_PARAMETER.TERM_CODE ↔ COURSE_CATALOG_SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship
- ACADEMIC_TERM_PARAMETER.TERM_CODE ↔ LIBRARY_SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship
- ACADEMIC_TERM_PARAMETER.TERM_CODE ↔ SUBJECT_OFFERED_SUMMARY.TERM_CODE; declared_or_materialized_relationship
- ACADEMIC_TERM_PARAMETER.TERM_CODE ↔ TIP_DETAIL.TERM_CODE; declared_or_materialized_relationship
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ FAC_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ FAC_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ FAC_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ FCLT_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- BUILDINGS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIP.PROGRAM_CODE ↔ SIS_COURSE_DESCRIPTION.CIP_PROGRAM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- CIS_COURSE_CATALOG.DEPARTMENT_CODE ↔ COURSE_CATALOG_SUBJECT_OFFERED.DEPARTMENT_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- CIS_COURSE_CATALOG.DEPARTMENT_CODE ↔ MIT_STUDENT_DIRECTORY.DEPARTMENT; declared_or_materialized_relationship
- CIS_COURSE_CATALOG.DEPARTMENT_CODE ↔ SIS_COURSE_DESCRIPTION.DEPARTMENT; declared_or_materialized_relationship, target_disjoint_historical_join
- CIS_COURSE_CATALOG.DEPARTMENT_CODE ↔ SIS_DEPARTMENT.DEPARTMENT_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- CIS_COURSE_CATALOG.DEPARTMENT_CODE ↔ SIS_SUBJECT_CODE.DEPARTMENT_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- CIS_COURSE_CATALOG.DESIGN_UNITS ↔ COURSE_CATALOG_SUBJECT_OFFERED.DESIGN_UNITS; profile_name_value_compatibility
- CIS_COURSE_CATALOG.DESIGN_UNITS ↔ DRUPAL_COURSE_CATALOG.DESIGN_UNITS; profile_name_value_compatibility
- CIS_COURSE_CATALOG.DESIGN_UNITS ↔ SUBJECT_SUMMARY.DESIGN_UNITS; profile_name_value_compatibility
- CIS_COURSE_CATALOG.GRADE_RULE ↔ COURSE_CATALOG_SUBJECT_OFFERED.GRADE_RULE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.GRADE_RULE ↔ DRUPAL_COURSE_CATALOG.GRADE_RULE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.GRADE_RULE_DESC ↔ COURSE_CATALOG_SUBJECT_OFFERED.GRADE_RULE_DESC; profile_name_value_compatibility
- CIS_COURSE_CATALOG.GRADE_RULE_DESC ↔ DRUPAL_COURSE_CATALOG.GRADE_RULE_DESC; profile_name_value_compatibility
- CIS_COURSE_CATALOG.GRADE_TYPE ↔ COURSE_CATALOG_SUBJECT_OFFERED.GRADE_TYPE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.GRADE_TYPE ↔ DRUPAL_COURSE_CATALOG.GRADE_TYPE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.GRADE_TYPE_DESC ↔ COURSE_CATALOG_SUBJECT_OFFERED.GRADE_TYPE_DESC; profile_name_value_compatibility
- CIS_COURSE_CATALOG.GRADE_TYPE_DESC ↔ DRUPAL_COURSE_CATALOG.GRADE_TYPE_DESC; profile_name_value_compatibility
- CIS_COURSE_CATALOG.HGN_CODE ↔ COURSE_CATALOG_SUBJECT_OFFERED.HGN_CODE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.HGN_CODE ↔ DRUPAL_COURSE_CATALOG.HGN_CODE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.HGN_CODE ↔ SUBJECT_OFFERED_SUMMARY.HGN_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- CIS_COURSE_CATALOG.HGN_DESC ↔ COURSE_CATALOG_SUBJECT_OFFERED.HGN_DESC; profile_name_value_compatibility
- CIS_COURSE_CATALOG.HGN_DESC ↔ DRUPAL_COURSE_CATALOG.HGN_DESC; profile_name_value_compatibility
- CIS_COURSE_CATALOG.IS_OFFERED_FALL_TERM ↔ COURSE_CATALOG_SUBJECT_OFFERED.IS_OFFERED_FALL_TERM; profile_name_value_compatibility
- CIS_COURSE_CATALOG.IS_OFFERED_FALL_TERM ↔ DRUPAL_COURSE_CATALOG.IS_OFFERED_FALL_TERM; profile_name_value_compatibility
- CIS_COURSE_CATALOG.IS_OFFERED_IAP ↔ COURSE_CATALOG_SUBJECT_OFFERED.IS_OFFERED_IAP; profile_name_value_compatibility
- CIS_COURSE_CATALOG.IS_OFFERED_IAP ↔ DRUPAL_COURSE_CATALOG.IS_OFFERED_IAP; profile_name_value_compatibility
- CIS_COURSE_CATALOG.IS_OFFERED_SPRING_TERM ↔ COURSE_CATALOG_SUBJECT_OFFERED.IS_OFFERED_SPRING_TERM; profile_name_value_compatibility
- CIS_COURSE_CATALOG.IS_OFFERED_SPRING_TERM ↔ DRUPAL_COURSE_CATALOG.IS_OFFERED_SPRING_TERM; profile_name_value_compatibility
- CIS_COURSE_CATALOG.IS_OFFERED_SUMMER_TERM ↔ COURSE_CATALOG_SUBJECT_OFFERED.IS_OFFERED_SUMMER_TERM; profile_name_value_compatibility
- CIS_COURSE_CATALOG.IS_OFFERED_SUMMER_TERM ↔ DRUPAL_COURSE_CATALOG.IS_OFFERED_SUMMER_TERM; profile_name_value_compatibility
- CIS_COURSE_CATALOG.IS_OFFERED_THIS_YEAR ↔ COURSE_CATALOG_SUBJECT_OFFERED.IS_OFFERED_THIS_YEAR; profile_name_value_compatibility
- CIS_COURSE_CATALOG.IS_OFFERED_THIS_YEAR ↔ DRUPAL_COURSE_CATALOG.IS_OFFERED_THIS_YEAR; profile_name_value_compatibility
- CIS_COURSE_CATALOG.IS_PRINTED_IN_BULLETIN ↔ COURSE_CATALOG_SUBJECT_OFFERED.IS_PRINTED_IN_BULLETIN; profile_name_value_compatibility
- CIS_COURSE_CATALOG.IS_PRINTED_IN_BULLETIN ↔ DRUPAL_COURSE_CATALOG.IS_PRINTED_IN_BULLETIN; profile_name_value_compatibility
- CIS_COURSE_CATALOG.IS_VARIABLE_UNITS ↔ COURSE_CATALOG_SUBJECT_OFFERED.IS_VARIABLE_UNITS; profile_name_value_compatibility
- CIS_COURSE_CATALOG.IS_VARIABLE_UNITS ↔ DRUPAL_COURSE_CATALOG.IS_VARIABLE_UNITS; profile_name_value_compatibility
- CIS_COURSE_CATALOG.LAB_UNITS ↔ COURSE_CATALOG_SUBJECT_OFFERED.LAB_UNITS; profile_name_value_compatibility
- CIS_COURSE_CATALOG.LAB_UNITS ↔ SUBJECT_SUMMARY.LAB_UNITS; profile_name_value_compatibility
- CIS_COURSE_CATALOG.LECTURE_UNITS ↔ COURSE_CATALOG_SUBJECT_OFFERED.LECTURE_UNITS; profile_name_value_compatibility
- CIS_COURSE_CATALOG.LECTURE_UNITS ↔ SUBJECT_OFFERED_SUMMARY.LECTURE_UNITS; profile_name_value_compatibility
- CIS_COURSE_CATALOG.LECTURE_UNITS ↔ SUBJECT_SUMMARY.LECTURE_UNITS; profile_name_value_compatibility
- CIS_COURSE_CATALOG.MASTER_SUBJECT_ID ↔ SUBJECT_OFFERED.MASTER_SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- CIS_COURSE_CATALOG.PREPARATION_UNITS ↔ COURSE_CATALOG_SUBJECT_OFFERED.PREPARATION_UNITS; profile_name_value_compatibility
- CIS_COURSE_CATALOG.PREPARATION_UNITS ↔ SUBJECT_OFFERED_SUMMARY.PREPARATION_UNITS; profile_name_value_compatibility
- CIS_COURSE_CATALOG.SUBJECT_CODE ↔ COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_CODE; declared_or_materialized_relationship
- CIS_COURSE_CATALOG.SUBJECT_CODE ↔ SIS_COURSE_DESCRIPTION.COURSE; declared_or_materialized_relationship
- CIS_COURSE_CATALOG.SUBJECT_CODE ↔ SIS_SUBJECT_CODE.SUBJECT_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- CIS_COURSE_CATALOG.SUBJECT_ID ↔ COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- CIS_COURSE_CATALOG.SUBJECT_ID ↔ SUBJECT_OFFERED_SUMMARY.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- CIS_COURSE_CATALOG.SUBJECT_ID ↔ TIP_SUBJECT_OFFERED.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- CIS_COURSE_CATALOG.SUBJECT_TITLE ↔ COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_TITLE; declared_or_materialized_relationship, target_disjoint_historical_join
- CIS_COURSE_CATALOG.TOTAL_UNITS ↔ COURSE_CATALOG_SUBJECT_OFFERED.TOTAL_UNITS; profile_name_value_compatibility
- CIS_COURSE_CATALOG.TOTAL_UNITS ↔ DRUPAL_COURSE_CATALOG.TOTAL_UNITS; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FAC_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FAC_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FAC_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FCLT_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.HASS_ATTRIBUTE ↔ COURSE_CATALOG_SUBJECT_OFFERED.HASS_ATTRIBUTE; declared_or_materialized_relationship, target_disjoint_historical_join
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ FAC_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ FAC_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ FAC_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ FCLT_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- CIS_HASS_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.DEPARTMENT_CODE ↔ MIT_STUDENT_DIRECTORY.DEPARTMENT; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.DEPARTMENT_CODE ↔ SIS_COURSE_DESCRIPTION.DEPARTMENT; declared_or_materialized_relationship, target_disjoint_historical_join
- COURSE_CATALOG_SUBJECT_OFFERED.DEPARTMENT_CODE ↔ SIS_DEPARTMENT.DEPARTMENT_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- COURSE_CATALOG_SUBJECT_OFFERED.DEPARTMENT_CODE ↔ TIP_SUBJECT_OFFERED.OFFER_DEPT_CODE; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.DEPARTMENT_NAME ↔ FCLT_ORGANIZATION.DLC_NAME; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.DEPARTMENT_NAME ↔ FCLT_ORGANIZATION.HR_DEPARTMENT_NAME; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.DEPARTMENT_NAME ↔ LIBRARY_COURSE_INSTRUCTOR.DEPARTMENT; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.DEPARTMENT_NAME ↔ LIBRARY_SUBJECT_OFFERED.OFFER_DEPT_NAME; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.DEPARTMENT_NAME ↔ SIS_COURSE_DESCRIPTION.DEPARTMENT_NAME; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.DEPARTMENT_NAME ↔ SIS_DEPARTMENT.DEPARTMENT_NAME; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.DEPARTMENT_NAME ↔ SIS_SUBJECT_CODE.DEPARTMENT_NAME; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.DEPARTMENT_NAME ↔ SUBJECT_OFFERED_SUMMARY.OFFER_DEPT_NAME; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.DEPARTMENT_NAME ↔ SUBJECT_SUMMARY.DEPARTMENT_NAME; declared_or_materialized_relationship, target_disjoint_historical_join
- COURSE_CATALOG_SUBJECT_OFFERED.DEPARTMENT_NAME ↔ TIP_SUBJECT_OFFERED.OFFER_DEPT_NAME; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.DESIGN_UNITS ↔ SUBJECT_SUMMARY.DESIGN_UNITS; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.EFFECTIVE_TERM_CODE ↔ LIBRARY_SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.GIR_ATTRIBUTE ↔ DRUPAL_COURSE_CATALOG.GIR_ATTRIBUTE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.GIR_ATTRIBUTE_DESC ↔ DRUPAL_COURSE_CATALOG.GIR_ATTRIBUTE_DESC; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.GRADE_RULE ↔ DRUPAL_COURSE_CATALOG.GRADE_RULE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.GRADE_RULE_DESC ↔ DRUPAL_COURSE_CATALOG.GRADE_RULE_DESC; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.GRADE_TYPE ↔ DRUPAL_COURSE_CATALOG.GRADE_TYPE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.GRADE_TYPE_DESC ↔ DRUPAL_COURSE_CATALOG.GRADE_TYPE_DESC; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.HGN_CODE ↔ DRUPAL_COURSE_CATALOG.HGN_CODE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.HGN_CODE ↔ SUBJECT_OFFERED.HGN_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- COURSE_CATALOG_SUBJECT_OFFERED.HGN_CODE ↔ SUBJECT_OFFERED_SUMMARY.HGN_CODE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.HGN_DESC ↔ DRUPAL_COURSE_CATALOG.HGN_DESC; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.IS_DESIGN_SECTION ↔ SUBJECT_OFFERED.IS_DESIGN_SECTION; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.IS_LAB_SECTION ↔ SUBJECT_OFFERED.IS_LAB_SECTION; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.IS_LECTURE_SECTION ↔ SUBJECT_OFFERED.IS_LECTURE_SECTION; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.IS_MASTER_SECTION ↔ SUBJECT_OFFERED.IS_MASTER_SECTION; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.IS_OFFERED_FALL_TERM ↔ DRUPAL_COURSE_CATALOG.IS_OFFERED_FALL_TERM; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.IS_OFFERED_IAP ↔ DRUPAL_COURSE_CATALOG.IS_OFFERED_IAP; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.IS_OFFERED_SPRING_TERM ↔ DRUPAL_COURSE_CATALOG.IS_OFFERED_SPRING_TERM; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.IS_OFFERED_SUMMER_TERM ↔ DRUPAL_COURSE_CATALOG.IS_OFFERED_SUMMER_TERM; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.IS_OFFERED_THIS_YEAR ↔ DRUPAL_COURSE_CATALOG.IS_OFFERED_THIS_YEAR; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.IS_PRINTED_IN_BULLETIN ↔ DRUPAL_COURSE_CATALOG.IS_PRINTED_IN_BULLETIN; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.IS_RECITATION_SECTION ↔ SUBJECT_OFFERED.IS_RECITATION_SECTION; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.IS_VARIABLE_UNITS ↔ DRUPAL_COURSE_CATALOG.IS_VARIABLE_UNITS; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.LAB_UNITS ↔ SUBJECT_SUMMARY.LAB_UNITS; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.LECTURE_UNITS ↔ DRUPAL_COURSE_CATALOG.LECTURE_UNITS; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.LECTURE_UNITS ↔ SUBJECT_OFFERED_SUMMARY.LECTURE_UNITS; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.LECTURE_UNITS ↔ SUBJECT_SUMMARY.LECTURE_UNITS; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.MEET_PLACE ↔ FCLT_ROOMS.FCLT_ROOM_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- COURSE_CATALOG_SUBJECT_OFFERED.PREPARATION_UNITS ↔ SUBJECT_OFFERED_SUMMARY.PREPARATION_UNITS; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.RESPONSIBLE_FACULTY_MIT_ID ↔ EMPLOYEE_DIRECTORY.MIT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- COURSE_CATALOG_SUBJECT_OFFERED.RESPONSIBLE_FACULTY_MIT_ID ↔ SUBJECT_OFFERED.RESPONSIBLE_FACULTY_MIT_ID; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_CODE ↔ SIS_COURSE_DESCRIPTION.COURSE; declared_or_materialized_relationship, target_disjoint_historical_join
- COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_CODE ↔ SIS_SUBJECT_CODE.SUBJECT_CODE; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_CODE ↔ SUBJECT_OFFERED_SUMMARY.COURSE_NUMBER; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_CODE ↔ SUBJECT_SUMMARY.DEPARTMENT_CODE; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_ID ↔ LIBRARY_RESERVE_MATRL_DETAIL.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_ID ↔ LIBRARY_SUBJECT_OFFERED.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_ID ↔ SUBJECT_OFFERED.SUBJECT_ID; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_ID ↔ SUBJECT_OFFERED_SUMMARY.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_ID ↔ SUBJECT_SUMMARY.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_ID ↔ TIP_DETAIL.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_ID ↔ TIP_SUBJECT_OFFERED.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_NUMBER ↔ LIBRARY_SUBJECT_OFFERED.SUBJECT_ID; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.SUBJECT_TITLE ↔ TIP_SUBJECT_OFFERED.SUBJECT_TITLE; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.TERM_CODE ↔ IAP_SUBJECT_DETAIL.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- COURSE_CATALOG_SUBJECT_OFFERED.TERM_CODE ↔ LIBRARY_RESERVE_MATRL_DETAIL.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- COURSE_CATALOG_SUBJECT_OFFERED.TERM_CODE ↔ LIBRARY_SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.TERM_CODE ↔ SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.TERM_CODE ↔ SUBJECT_OFFERED_SUMMARY.TERM_CODE; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.TERM_CODE ↔ SUBJECT_SUMMARY.TERM_CODE; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.TERM_CODE ↔ TIP_DETAIL.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- COURSE_CATALOG_SUBJECT_OFFERED.TERM_CODE ↔ TIP_SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship
- COURSE_CATALOG_SUBJECT_OFFERED.TERM_DURATION ↔ DRUPAL_COURSE_CATALOG.TERM_DURATION; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.TOTAL_UNITS ↔ DRUPAL_COURSE_CATALOG.TOTAL_UNITS; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ FAC_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ FAC_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ FAC_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ FCLT_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- COURSE_CATALOG_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.DESIGN_UNITS ↔ SUBJECT_SUMMARY.DESIGN_UNITS; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.MASTER_SUBJECT_ID ↔ LIBRARY_SUBJECT_OFFERED.MASTER_SUBJECT_ID; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.SUBJECT_ID ↔ LIBRARY_SUBJECT_OFFERED.SUBJECT_ID; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.TOTAL_UNITS ↔ SUBJECT_SUMMARY.TOTAL_UNITS; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FAC_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FAC_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FAC_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FCLT_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_COURSE_CATALOG.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ FAC_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ FAC_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ FAC_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ FCLT_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- DRUPAL_EMPLOYEE_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- EMPLOYEE_DIRECTORY.DEPARTMENT_NAME ↔ HR_ORG_UNIT.HR_DEPARTMENT_NAME; declared_or_materialized_relationship
- EMPLOYEE_DIRECTORY.KRB_NAME ↔ MOIRA_LIST_DETAIL.MOIRA_LIST_MEMBER; declared_or_materialized_relationship, target_disjoint_historical_join
- EMPLOYEE_DIRECTORY.MIT_ID ↔ MOIRA_LIST_DETAIL.MOIRA_LIST_MEMBER_MIT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- EMPLOYEE_DIRECTORY.MIT_ID ↔ TIP_SUBJECT_OFFERED.RESPONSIBLE_FACULTY_MIT_ID; declared_or_materialized_relationship
- EMPLOYEE_DIRECTORY.OFFICE_LOCATION ↔ FCLT_ROOMS.BUILDING_ROOM; declared_or_materialized_relationship, target_disjoint_historical_join
- FAC_BUILDING.ACCESS_LEVEL_CODE ↔ FCLT_BUILDING.ACCESS_LEVEL_CODE; profile_name_value_compatibility
- FAC_BUILDING.ACCESS_LEVEL_CODE ↔ FCLT_BUILDING_HIST.ACCESS_LEVEL_CODE; profile_name_value_compatibility
- FAC_BUILDING.ACCESS_LEVEL_CODE ↔ FCLT_BUILDING_HIST_1.ACCESS_LEVEL_CODE; profile_name_value_compatibility
- FAC_BUILDING.ACCESS_LEVEL_NAME ↔ FCLT_BUILDING.ACCESS_LEVEL_NAME; profile_name_value_compatibility
- FAC_BUILDING.ACCESS_LEVEL_NAME ↔ FCLT_BUILDING_HIST.ACCESS_LEVEL_NAME; profile_name_value_compatibility
- FAC_BUILDING.ACCESS_LEVEL_NAME ↔ FCLT_BUILDING_HIST_1.ACCESS_LEVEL_NAME; profile_name_value_compatibility
- FAC_BUILDING.ASSIGNABLE_AREA ↔ FCLT_BUILDING.ASSIGNABLE_AREA; profile_name_value_compatibility
- FAC_BUILDING.BUILDING_HEIGHT ↔ FCLT_BUILDING.BUILDING_HEIGHT; profile_name_value_compatibility
- FAC_BUILDING.BUILDING_NAME ↔ FCLT_BUILDING.BUILDING_NAME; profile_name_value_compatibility
- FAC_BUILDING.BUILDING_NAMED_FOR ↔ FCLT_BUILDING.BUILDING_NAMED_FOR; profile_name_value_compatibility
- FAC_BUILDING.BUILDING_NAME_LONG ↔ FCLT_BUILDING.BUILDING_NAME_LONG; profile_name_value_compatibility
- FAC_BUILDING.BUILDING_NUMBER ↔ FCLT_BUILDING.BUILDING_NUMBER; profile_name_value_compatibility
- FAC_BUILDING.BUILDING_SORT ↔ FCLT_BUILDING.BUILDING_SORT; profile_name_value_compatibility
- FAC_BUILDING.BUILDING_TYPE ↔ FCLT_BUILDING.BUILDING_TYPE; profile_name_value_compatibility
- FAC_BUILDING.BUILDING_TYPE ↔ FCLT_BUILDING_HIST.BUILDING_TYPE; profile_name_value_compatibility
- FAC_BUILDING.BUILDING_TYPE ↔ FCLT_BUILDING_HIST_1.BUILDING_TYPE; profile_name_value_compatibility
- FAC_BUILDING.BUILDING_USE ↔ FCLT_BUILDING.BUILDING_USE; profile_name_value_compatibility
- FAC_BUILDING.BUILDING_USE ↔ FCLT_BUILDING_HIST.BUILDING_USE; profile_name_value_compatibility
- FAC_BUILDING.BUILDING_USE ↔ FCLT_BUILDING_HIST_1.BUILDING_USE; profile_name_value_compatibility
- FAC_BUILDING.CAMPUS_SECTOR ↔ FCLT_BUILDING.CAMPUS_SECTOR; profile_name_value_compatibility
- FAC_BUILDING.CAMPUS_SECTOR ↔ FCLT_BUILDING_HIST.CAMPUS_SECTOR; profile_name_value_compatibility
- FAC_BUILDING.CAMPUS_SECTOR ↔ FCLT_BUILDING_HIST_1.CAMPUS_SECTOR; profile_name_value_compatibility
- FAC_BUILDING.COST_CENTER_CODE ↔ FCLT_BUILDING.COST_CENTER_CODE; profile_name_value_compatibility
- FAC_BUILDING.COST_COLLECTOR_KEY ↔ FCLT_BUILDING.COST_COLLECTOR_KEY; profile_name_value_compatibility
- FAC_BUILDING.DATE_ACQUIRED ↔ FCLT_BUILDING.DATE_ACQUIRED; profile_name_value_compatibility
- FAC_BUILDING.DATE_BUILT ↔ FCLT_BUILDING.DATE_BUILT; profile_name_value_compatibility
- FAC_BUILDING.DATE_OCCUPIED ↔ FCLT_BUILDING.DATE_OCCUPIED; profile_name_value_compatibility
- FAC_BUILDING.EASTING_X_SPCS ↔ FCLT_BUILDING.EASTING_X_SPCS; profile_name_value_compatibility
- FAC_BUILDING.EXT_GROSS_AREA ↔ FCLT_BUILDING.EXT_GROSS_AREA; profile_name_value_compatibility
- FAC_BUILDING.LATITUDE_WGS ↔ FCLT_BUILDING.LATITUDE_WGS; profile_name_value_compatibility
- FAC_BUILDING.LONGITUDE_WGS ↔ FCLT_BUILDING.LONGITUDE_WGS; profile_name_value_compatibility
- FAC_BUILDING.NON_ASSIGNABLE_AREA ↔ FCLT_BUILDING.NON_ASSIGNABLE_AREA; profile_name_value_compatibility
- FAC_BUILDING.NORTHING_Y_SPCS ↔ FCLT_BUILDING.NORTHING_Y_SPCS; profile_name_value_compatibility
- FAC_BUILDING.NUM_OF_ROOMS ↔ FCLT_BUILDING.NUM_OF_ROOMS; profile_name_value_compatibility
- FAC_BUILDING.OCCUPANCY_CLASS ↔ FCLT_BUILDING.OCCUPANCY_CLASS; profile_name_value_compatibility
- FAC_BUILDING.OCCUPANCY_CLASS ↔ FCLT_BUILDING_HIST.OCCUPANCY_CLASS; profile_name_value_compatibility
- FAC_BUILDING.OCCUPANCY_CLASS ↔ FCLT_BUILDING_HIST_1.OCCUPANCY_CLASS; profile_name_value_compatibility
- FAC_BUILDING.OWNERSHIP_TYPE ↔ FCLT_BUILDING.OWNERSHIP_TYPE; profile_name_value_compatibility
- FAC_BUILDING.OWNERSHIP_TYPE ↔ FCLT_BUILDING_HIST.OWNERSHIP_TYPE; profile_name_value_compatibility
- FAC_BUILDING.OWNERSHIP_TYPE ↔ FCLT_BUILDING_HIST_1.OWNERSHIP_TYPE; profile_name_value_compatibility
- FAC_BUILDING.PARENT_BUILDING_NAME ↔ FCLT_BUILDING.PARENT_BUILDING_NAME; profile_name_value_compatibility
- FAC_BUILDING.PARENT_BUILDING_NAME_LONG ↔ FCLT_BUILDING.PARENT_BUILDING_NAME_LONG; profile_name_value_compatibility
- FAC_BUILDING.PARENT_BUILDING_NUMBER ↔ FCLT_BUILDING.PARENT_BUILDING_NUMBER; profile_name_value_compatibility
- FAC_BUILDING.SITE ↔ FCLT_BUILDING.SITE; profile_name_value_compatibility
- FAC_BUILDING.SITE ↔ FCLT_BUILDING_HIST.SITE; profile_name_value_compatibility
- FAC_BUILDING.SITE ↔ FCLT_BUILDING_HIST_1.SITE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ FAC_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ FAC_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ FCLT_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.ADDRESS_CITY_ID ↔ FCLT_BUILDING_ADDRESS.ADDRESS_CITY_ID; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.ADDRESS_PURPOSE ↔ FCLT_BUILDING_ADDRESS.ADDRESS_PURPOSE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.ADDRESS_PURPOSE ↔ FCLT_BUILDING_ADDRESS_HIST.ADDRESS_PURPOSE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.CITY ↔ FCLT_BUILDING_ADDRESS.CITY; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.CITY ↔ FCLT_BUILDING_ADDRESS_HIST.CITY; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.POSTAL_CODE ↔ FCLT_BUILDING_ADDRESS.POSTAL_CODE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.POSTAL_CODE ↔ FCLT_BUILDING_ADDRESS_HIST.POSTAL_CODE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.STATE ↔ FCLT_BUILDING_ADDRESS.STATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.STATE ↔ FCLT_BUILDING_ADDRESS_HIST.STATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.STREET_NAME ↔ FCLT_BUILDING_ADDRESS.STREET_NAME; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.STREET_NUMBER ↔ FCLT_BUILDING_ADDRESS.STREET_NUMBER; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.STREET_SUFFIX ↔ FCLT_BUILDING_ADDRESS.STREET_SUFFIX; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.STREET_SUFFIX ↔ FCLT_BUILDING_ADDRESS_HIST.STREET_SUFFIX; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ FAC_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ FAC_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ FCLT_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.ACCESS_LEVEL ↔ FCLT_FLOOR.ACCESS_LEVEL; profile_name_value_compatibility
- FAC_FLOOR.ACCESS_LEVEL ↔ FCLT_ROOMS.ACCESS_LEVEL; profile_name_value_compatibility
- FAC_FLOOR.ACCESS_LEVEL ↔ FCLT_ROOMS_HIST.ACCESS_LEVEL; profile_name_value_compatibility
- FAC_FLOOR.ACCESS_LEVEL ↔ ZPM_ROOMS_LOAD.ACCESS_LEVEL; profile_name_value_compatibility
- FAC_FLOOR.ASSIGNABLE_AREA ↔ FCLT_FLOOR.ASSIGNABLE_AREA; profile_name_value_compatibility
- FAC_FLOOR.EXT_GROSS_AREA ↔ FCLT_FLOOR.EXT_GROSS_AREA; profile_name_value_compatibility
- FAC_FLOOR.FLOOR ↔ FAC_ROOMS.FLOOR; profile_name_value_compatibility
- FAC_FLOOR.FLOOR ↔ FCLT_FLOOR.FLOOR; profile_name_value_compatibility
- FAC_FLOOR.FLOOR ↔ FCLT_ROOMS.FLOOR; profile_name_value_compatibility
- FAC_FLOOR.FLOOR ↔ FCLT_ROOMS_HIST.FLOOR; profile_name_value_compatibility
- FAC_FLOOR.FLOOR_SORT_SEQUENCE ↔ FCLT_FLOOR.FLOOR_SORT_SEQUENCE; profile_name_value_compatibility
- FAC_FLOOR.FLOOR_SORT_SEQUENCE ↔ FCLT_FLOOR_HIST.FLOOR_SORT_SEQUENCE; profile_name_value_compatibility
- FAC_FLOOR.LEVEL_ID ↔ FCLT_FLOOR.LEVEL_ID; profile_name_value_compatibility
- FAC_FLOOR.LEVEL_ID ↔ FCLT_FLOOR_HIST.LEVEL_ID; profile_name_value_compatibility
- FAC_FLOOR.NON_ASSIGNABLE_AREA ↔ FCLT_FLOOR.NON_ASSIGNABLE_AREA; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ FAC_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ FCLT_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_FLOOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.ASSIGNABLE ↔ FAC_ORGANIZATION.ASSIGNABLE; profile_name_value_compatibility
- FAC_MAJOR_USE.ASSIGNABLE ↔ FCLT_MAJOR_USE.ASSIGNABLE; profile_name_value_compatibility
- FAC_MAJOR_USE.ASSIGNABLE ↔ FCLT_MAJOR_USE_HIST.ASSIGNABLE; profile_name_value_compatibility
- FAC_MAJOR_USE.ASSIGNABLE ↔ FCLT_ORGANIZATION.ASSIGNABLE; profile_name_value_compatibility
- FAC_MAJOR_USE.ASSIGNABLE ↔ FCLT_ORGANIZATION_HIST.ASSIGNABLE; profile_name_value_compatibility
- FAC_MAJOR_USE.DESCRIPTION ↔ FCLT_MAJOR_USE.DESCRIPTION; profile_name_value_compatibility
- FAC_MAJOR_USE.DESCRIPTION ↔ FCLT_MAJOR_USE_HIST.DESCRIPTION; profile_name_value_compatibility
- FAC_MAJOR_USE.MAJOR_USE ↔ FCLT_MAJOR_USE.MAJOR_USE; profile_name_value_compatibility
- FAC_MAJOR_USE.MAJOR_USE ↔ FCLT_MAJOR_USE_HIST.MAJOR_USE; profile_name_value_compatibility
- FAC_MAJOR_USE.MAJOR_USE_KEY ↔ FAC_ROOMS.MAJOR_USE_KEY; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ FAC_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ FCLT_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.ASSIGNABLE ↔ FCLT_MAJOR_USE.ASSIGNABLE; profile_name_value_compatibility
- FAC_ORGANIZATION.ASSIGNABLE ↔ FCLT_MAJOR_USE_HIST.ASSIGNABLE; profile_name_value_compatibility
- FAC_ORGANIZATION.ASSIGNABLE ↔ FCLT_ORGANIZATION.ASSIGNABLE; profile_name_value_compatibility
- FAC_ORGANIZATION.ASSIGNABLE ↔ FCLT_ORGANIZATION_HIST.ASSIGNABLE; profile_name_value_compatibility
- FAC_ORGANIZATION.MAJOR_ORG ↔ FCLT_ORGANIZATION.MAJOR_ORG; profile_name_value_compatibility
- FAC_ORGANIZATION.MAJOR_ORG ↔ FCLT_ORGANIZATION_HIST.MAJOR_ORG; profile_name_value_compatibility
- FAC_ORGANIZATION.ORGANIZATION_LEVEL ↔ FCLT_ORGANIZATION.ORGANIZATION_LEVEL; profile_name_value_compatibility
- FAC_ORGANIZATION.ORGANIZATION_LEVEL ↔ FCLT_ORGANIZATION_HIST.ORGANIZATION_LEVEL; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ FAC_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ FCLT_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.ACCESS_LEVEL ↔ FCLT_ROOMS.ACCESS_LEVEL; profile_name_value_compatibility
- FAC_ROOMS.ACCESS_LEVEL ↔ ZPM_ROOMS_LOAD.ACCESS_LEVEL; profile_name_value_compatibility
- FAC_ROOMS.BUILDING_KEY ↔ SPACE_DETAIL.BUILDING_KEY; profile_name_value_compatibility
- FAC_ROOMS.FLOOR ↔ FCLT_FLOOR.FLOOR; profile_name_value_compatibility
- FAC_ROOMS.FLOOR ↔ FCLT_ROOMS.FLOOR; profile_name_value_compatibility
- FAC_ROOMS.FLOOR ↔ FCLT_ROOMS_HIST.FLOOR; profile_name_value_compatibility
- FAC_ROOMS.FLOOR ↔ SPACE_FLOOR.FLOOR; profile_name_value_compatibility
- FAC_ROOMS.MAJOR_USE_DESC ↔ FCLT_ROOMS.MAJOR_USE_DESC; profile_name_value_compatibility
- FAC_ROOMS.ORGANIZATION_NAME ↔ FCLT_ROOMS.ORGANIZATION_NAME; profile_name_value_compatibility
- FAC_ROOMS.ORGANIZATION_NAME ↔ FCLT_ROOMS_HIST.ORGANIZATION_NAME; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ FCLT_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FAC_ROOMS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.ACCESS_LEVEL_CODE ↔ FCLT_BUILDING_HIST.ACCESS_LEVEL_CODE; declared_or_materialized_relationship, profile_name_value_compatibility, target_disjoint_historical_join
- FCLT_BUILDING.ACCESS_LEVEL_CODE ↔ FCLT_BUILDING_HIST_1.ACCESS_LEVEL_CODE; profile_name_value_compatibility
- FCLT_BUILDING.ACCESS_LEVEL_NAME ↔ FCLT_BUILDING_HIST.ACCESS_LEVEL_NAME; profile_name_value_compatibility
- FCLT_BUILDING.ACCESS_LEVEL_NAME ↔ FCLT_BUILDING_HIST_1.ACCESS_LEVEL_NAME; profile_name_value_compatibility
- FCLT_BUILDING.BUILDING_TYPE ↔ FCLT_BUILDING_HIST.BUILDING_TYPE; profile_name_value_compatibility
- FCLT_BUILDING.BUILDING_TYPE ↔ FCLT_BUILDING_HIST_1.BUILDING_TYPE; profile_name_value_compatibility
- FCLT_BUILDING.BUILDING_USE ↔ FCLT_BUILDING_HIST.BUILDING_USE; profile_name_value_compatibility
- FCLT_BUILDING.BUILDING_USE ↔ FCLT_BUILDING_HIST_1.BUILDING_USE; profile_name_value_compatibility
- FCLT_BUILDING.CAMPUS_SECTOR ↔ FCLT_BUILDING_HIST.CAMPUS_SECTOR; profile_name_value_compatibility
- FCLT_BUILDING.CAMPUS_SECTOR ↔ FCLT_BUILDING_HIST_1.CAMPUS_SECTOR; profile_name_value_compatibility
- FCLT_BUILDING.COST_CENTER_CODE ↔ FCLT_BUILDING_HIST.COST_CENTER_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_BUILDING.COST_COLLECTOR_KEY ↔ FCLT_BUILDING_HIST.COST_COLLECTOR_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_BUILDING.FCLT_BUILDING_KEY ↔ FCLT_BUILDING_ADDRESS.FCLT_BUILDING_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_BUILDING.FCLT_BUILDING_KEY ↔ FCLT_BUILDING_HIST.FCLT_BUILDING_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_BUILDING.FCLT_BUILDING_KEY ↔ FCLT_FLOOR.FCLT_BUILDING_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_BUILDING.FCLT_BUILDING_KEY ↔ FCLT_ROOMS.FCLT_BUILDING_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_BUILDING.OCCUPANCY_CLASS ↔ FCLT_BUILDING_HIST.OCCUPANCY_CLASS; profile_name_value_compatibility
- FCLT_BUILDING.OCCUPANCY_CLASS ↔ FCLT_BUILDING_HIST_1.OCCUPANCY_CLASS; profile_name_value_compatibility
- FCLT_BUILDING.OWNERSHIP_TYPE ↔ FCLT_BUILDING_HIST.OWNERSHIP_TYPE; profile_name_value_compatibility
- FCLT_BUILDING.OWNERSHIP_TYPE ↔ FCLT_BUILDING_HIST_1.OWNERSHIP_TYPE; profile_name_value_compatibility
- FCLT_BUILDING.SITE ↔ FCLT_BUILDING_HIST.SITE; profile_name_value_compatibility
- FCLT_BUILDING.SITE ↔ FCLT_BUILDING_HIST_1.SITE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ FCLT_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.ADDRESS_PURPOSE ↔ FCLT_BUILDING_ADDRESS_HIST.ADDRESS_PURPOSE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.BUILDING_NUMBER ↔ FCLT_ROOMS.FCLT_BUILDING_KEY; declared_or_materialized_relationship
- FCLT_BUILDING_ADDRESS.CITY ↔ FCLT_BUILDING_ADDRESS_HIST.CITY; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.FCLT_BUILDING_KEY ↔ FCLT_FLOOR.FCLT_BUILDING_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_BUILDING_ADDRESS.FCLT_BUILDING_KEY ↔ FCLT_ROOMS.FCLT_BUILDING_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_BUILDING_ADDRESS.POSTAL_CODE ↔ FCLT_BUILDING_ADDRESS_HIST.POSTAL_CODE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.STATE ↔ FCLT_BUILDING_ADDRESS_HIST.STATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.STREET_SUFFIX ↔ FCLT_BUILDING_ADDRESS_HIST.STREET_SUFFIX; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ FCLT_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS_HIST.FCLT_BUILDING_KEY ↔ FCLT_FLOOR_HIST.FCLT_BUILDING_KEY; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS_HIST.FISCAL_PERIOD ↔ FCLT_BUILDING_HIST.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS_HIST.FISCAL_PERIOD ↔ FCLT_BUILDING_HIST_1.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS_HIST.FISCAL_PERIOD ↔ FCLT_FLOOR_HIST.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS_HIST.FISCAL_PERIOD ↔ FCLT_MAJOR_USE_HIST.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS_HIST.FISCAL_PERIOD ↔ FCLT_ORGANIZATION_HIST.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS_HIST.FISCAL_PERIOD ↔ FCLT_ROOMS_HIST.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS_HIST.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING_HIST.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS_HIST.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING_HIST_1.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS_HIST.WAREHOUSE_LOAD_DATE ↔ FCLT_FLOOR_HIST.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS_HIST.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE_HIST.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS_HIST.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION_HIST.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_ADDRESS_HIST.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS_HIST.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_HIST.ACCESS_LEVEL_CODE ↔ FCLT_BUILDING_HIST_1.ACCESS_LEVEL_CODE; profile_name_value_compatibility
- FCLT_BUILDING_HIST.ACCESS_LEVEL_NAME ↔ FCLT_BUILDING_HIST_1.ACCESS_LEVEL_NAME; profile_name_value_compatibility
- FCLT_BUILDING_HIST.ASSIGNABLE_AREA ↔ FCLT_BUILDING_HIST_1.ASSIGNABLE_AREA; profile_name_value_compatibility
- FCLT_BUILDING_HIST.BUILDING_HEIGHT ↔ FCLT_BUILDING_HIST_1.BUILDING_HEIGHT; profile_name_value_compatibility
- FCLT_BUILDING_HIST.BUILDING_NAME ↔ FCLT_BUILDING_HIST_1.BUILDING_NAME; profile_name_value_compatibility
- FCLT_BUILDING_HIST.BUILDING_NAMED_FOR ↔ FCLT_BUILDING_HIST_1.BUILDING_NAMED_FOR; profile_name_value_compatibility
- FCLT_BUILDING_HIST.BUILDING_NAME_LONG ↔ FCLT_BUILDING_HIST_1.BUILDING_NAME_LONG; profile_name_value_compatibility
- FCLT_BUILDING_HIST.BUILDING_NUMBER ↔ FCLT_BUILDING_HIST_1.BUILDING_NUMBER; profile_name_value_compatibility
- FCLT_BUILDING_HIST.BUILDING_SORT ↔ FCLT_BUILDING_HIST_1.BUILDING_SORT; profile_name_value_compatibility
- FCLT_BUILDING_HIST.BUILDING_TYPE ↔ FCLT_BUILDING_HIST_1.BUILDING_TYPE; profile_name_value_compatibility
- FCLT_BUILDING_HIST.BUILDING_USE ↔ FCLT_BUILDING_HIST_1.BUILDING_USE; profile_name_value_compatibility
- FCLT_BUILDING_HIST.CAMPUS_SECTOR ↔ FCLT_BUILDING_HIST_1.CAMPUS_SECTOR; profile_name_value_compatibility
- FCLT_BUILDING_HIST.COST_CENTER_CODE ↔ FCLT_BUILDING_HIST_1.COST_CENTER_CODE; profile_name_value_compatibility
- FCLT_BUILDING_HIST.COST_COLLECTOR_KEY ↔ FCLT_BUILDING_HIST_1.COST_COLLECTOR_KEY; profile_name_value_compatibility
- FCLT_BUILDING_HIST.EASTING_X_SPCS ↔ FCLT_BUILDING_HIST_1.EASTING_X_SPCS; profile_name_value_compatibility
- FCLT_BUILDING_HIST.EXT_GROSS_AREA ↔ FCLT_BUILDING_HIST_1.EXT_GROSS_AREA; profile_name_value_compatibility
- FCLT_BUILDING_HIST.FCLT_BUILDING_HIST_KEY ↔ FCLT_BUILDING_HIST_1.FCLT_BUILDING_HIST_KEY; profile_name_value_compatibility
- FCLT_BUILDING_HIST.FCLT_BUILDING_KEY ↔ FCLT_BUILDING_HIST_1.FCLT_BUILDING_KEY; profile_name_value_compatibility
- FCLT_BUILDING_HIST.FCLT_BUILDING_KEY ↔ FCLT_ROOMS.FCLT_BUILDING_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_BUILDING_HIST.FISCAL_PERIOD ↔ FCLT_BUILDING_HIST_1.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_BUILDING_HIST.FISCAL_PERIOD ↔ FCLT_FLOOR_HIST.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_BUILDING_HIST.FISCAL_PERIOD ↔ FCLT_MAJOR_USE_HIST.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_BUILDING_HIST.FISCAL_PERIOD ↔ FCLT_ORGANIZATION_HIST.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_BUILDING_HIST.FISCAL_PERIOD ↔ FCLT_ROOMS_HIST.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_BUILDING_HIST.LATITUDE_WGS ↔ FCLT_BUILDING_HIST_1.LATITUDE_WGS; profile_name_value_compatibility
- FCLT_BUILDING_HIST.LONGITUDE_WGS ↔ FCLT_BUILDING_HIST_1.LONGITUDE_WGS; profile_name_value_compatibility
- FCLT_BUILDING_HIST.NON_ASSIGNABLE_AREA ↔ FCLT_BUILDING_HIST_1.NON_ASSIGNABLE_AREA; profile_name_value_compatibility
- FCLT_BUILDING_HIST.NORTHING_Y_SPCS ↔ FCLT_BUILDING_HIST_1.NORTHING_Y_SPCS; profile_name_value_compatibility
- FCLT_BUILDING_HIST.NUM_OF_ROOMS ↔ FCLT_BUILDING_HIST_1.NUM_OF_ROOMS; profile_name_value_compatibility
- FCLT_BUILDING_HIST.OCCUPANCY_CLASS ↔ FCLT_BUILDING_HIST_1.OCCUPANCY_CLASS; profile_name_value_compatibility
- FCLT_BUILDING_HIST.OWNERSHIP_TYPE ↔ FCLT_BUILDING_HIST_1.OWNERSHIP_TYPE; profile_name_value_compatibility
- FCLT_BUILDING_HIST.PARENT_BUILDING_NAME ↔ FCLT_BUILDING_HIST_1.PARENT_BUILDING_NAME; profile_name_value_compatibility
- FCLT_BUILDING_HIST.PARENT_BUILDING_NAME_LONG ↔ FCLT_BUILDING_HIST_1.PARENT_BUILDING_NAME_LONG; profile_name_value_compatibility
- FCLT_BUILDING_HIST.PARENT_BUILDING_NUMBER ↔ FCLT_BUILDING_HIST_1.PARENT_BUILDING_NUMBER; profile_name_value_compatibility
- FCLT_BUILDING_HIST.SITE ↔ FCLT_BUILDING_HIST_1.SITE; profile_name_value_compatibility
- FCLT_BUILDING_HIST.WAREHOUSE_LOAD_DATE ↔ FCLT_BUILDING_HIST_1.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_HIST.WAREHOUSE_LOAD_DATE ↔ FCLT_FLOOR_HIST.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_HIST.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE_HIST.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_HIST.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION_HIST.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_HIST.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS_HIST.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_HIST_1.FISCAL_PERIOD ↔ FCLT_FLOOR_HIST.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_BUILDING_HIST_1.FISCAL_PERIOD ↔ FCLT_MAJOR_USE_HIST.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_BUILDING_HIST_1.FISCAL_PERIOD ↔ FCLT_ORGANIZATION_HIST.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_BUILDING_HIST_1.FISCAL_PERIOD ↔ FCLT_ROOMS_HIST.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_BUILDING_HIST_1.WAREHOUSE_LOAD_DATE ↔ FCLT_FLOOR_HIST.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_HIST_1.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE_HIST.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_HIST_1.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION_HIST.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_BUILDING_HIST_1.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS_HIST.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.ACCESS_LEVEL ↔ FCLT_ROOMS.ACCESS_LEVEL; profile_name_value_compatibility
- FCLT_FLOOR.ACCESS_LEVEL ↔ FCLT_ROOMS_HIST.ACCESS_LEVEL; profile_name_value_compatibility
- FCLT_FLOOR.ACCESS_LEVEL ↔ ZPM_ROOMS_LOAD.ACCESS_LEVEL; profile_name_value_compatibility
- FCLT_FLOOR.FCLT_BUILDING_KEY ↔ FCLT_ROOMS.FCLT_BUILDING_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_FLOOR.FCLT_FLOOR_KEY ↔ FCLT_ROOMS.FCLT_FLOOR_KEY; declared_or_materialized_relationship
- FCLT_FLOOR.FLOOR ↔ FCLT_ROOMS.FLOOR; declared_or_materialized_relationship, profile_name_value_compatibility, target_disjoint_historical_join
- FCLT_FLOOR.FLOOR ↔ FCLT_ROOMS_HIST.FLOOR; profile_name_value_compatibility
- FCLT_FLOOR.FLOOR_SORT_SEQUENCE ↔ FCLT_FLOOR_HIST.FLOOR_SORT_SEQUENCE; profile_name_value_compatibility
- FCLT_FLOOR.LEVEL_ID ↔ FCLT_FLOOR_HIST.LEVEL_ID; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR_HIST.ACCESS_LEVEL ↔ FCLT_ROOMS.ACCESS_LEVEL; profile_name_value_compatibility
- FCLT_FLOOR_HIST.ACCESS_LEVEL ↔ ZPM_ROOMS_LOAD.ACCESS_LEVEL; profile_name_value_compatibility
- FCLT_FLOOR_HIST.FISCAL_PERIOD ↔ FCLT_MAJOR_USE_HIST.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_FLOOR_HIST.FISCAL_PERIOD ↔ FCLT_ORGANIZATION_HIST.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_FLOOR_HIST.FISCAL_PERIOD ↔ FCLT_ROOMS_HIST.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_FLOOR_HIST.WAREHOUSE_LOAD_DATE ↔ FCLT_MAJOR_USE_HIST.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR_HIST.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION_HIST.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_FLOOR_HIST.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS_HIST.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.ASSIGNABLE ↔ FCLT_MAJOR_USE_HIST.ASSIGNABLE; profile_name_value_compatibility
- FCLT_MAJOR_USE.ASSIGNABLE ↔ FCLT_ORGANIZATION.ASSIGNABLE; profile_name_value_compatibility
- FCLT_MAJOR_USE.ASSIGNABLE ↔ FCLT_ORGANIZATION_HIST.ASSIGNABLE; profile_name_value_compatibility
- FCLT_MAJOR_USE.DESCRIPTION ↔ FCLT_MAJOR_USE_HIST.DESCRIPTION; profile_name_value_compatibility
- FCLT_MAJOR_USE.FCLT_MAJOR_USE_KEY ↔ FCLT_MAJOR_USE_HIST.FCLT_MAJOR_USE_KEY; profile_name_value_compatibility
- FCLT_MAJOR_USE.FCLT_MAJOR_USE_KEY ↔ FCLT_ROOMS.FCLT_MAJOR_USE_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_MAJOR_USE.MAJOR_USE ↔ FCLT_MAJOR_USE_HIST.MAJOR_USE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE_HIST.ASSIGNABLE ↔ FCLT_ORGANIZATION.ASSIGNABLE; profile_name_value_compatibility
- FCLT_MAJOR_USE_HIST.ASSIGNABLE ↔ FCLT_ORGANIZATION_HIST.ASSIGNABLE; profile_name_value_compatibility
- FCLT_MAJOR_USE_HIST.FISCAL_PERIOD ↔ FCLT_ORGANIZATION_HIST.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_MAJOR_USE_HIST.FISCAL_PERIOD ↔ FCLT_ROOMS_HIST.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_MAJOR_USE_HIST.WAREHOUSE_LOAD_DATE ↔ FCLT_ORGANIZATION_HIST.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_MAJOR_USE_HIST.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS_HIST.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.ASSIGNABLE ↔ FCLT_ORGANIZATION_HIST.ASSIGNABLE; profile_name_value_compatibility
- FCLT_ORGANIZATION.COURSE ↔ FCLT_ORGANIZATION_HIST.COURSE; profile_name_value_compatibility
- FCLT_ORGANIZATION.DLC_KEY ↔ FCLT_ORGANIZATION_HIST.DLC_KEY; profile_name_value_compatibility
- FCLT_ORGANIZATION.DLC_KEY ↔ FCLT_ORG_DLC_KEY.DLC_KEY; declared_or_materialized_relationship, profile_name_value_compatibility, target_disjoint_historical_join
- FCLT_ORGANIZATION.DLC_KEY ↔ HR_ORG_UNIT.DLC_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_ORGANIZATION.DLC_KEY ↔ MASTER_DEPT_HIERARCHY.DLC_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_ORGANIZATION.DLC_KEY ↔ SIS_DEPARTMENT.DLC_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_ORGANIZATION.DLC_KEY ↔ SPACE_UNIT.DLC_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_ORGANIZATION.DLC_NAME ↔ FCLT_ORGANIZATION_HIST.DLC_NAME; profile_name_value_compatibility
- FCLT_ORGANIZATION.FCLT_MAJOR_ORG_KEY ↔ FCLT_ORGANIZATION_HIST.FCLT_MAJOR_ORG_KEY; profile_name_value_compatibility
- FCLT_ORGANIZATION.FCLT_ORGANIZATION_KEY ↔ FCLT_ORGANIZATION_HIST.FCLT_ORGANIZATION_KEY; profile_name_value_compatibility
- FCLT_ORGANIZATION.FCLT_ORGANIZATION_KEY ↔ FCLT_ORG_DLC_KEY.FCLT_ORGANIZATION_KEY; declared_or_materialized_relationship, profile_name_value_compatibility, target_disjoint_historical_join
- FCLT_ORGANIZATION.FCLT_ORGANIZATION_KEY ↔ FCLT_ROOMS.FCLT_ORGANIZATION_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_ORGANIZATION.FCLT_ORGANIZATION_KEY ↔ SPACE_UNIT.FCLT_ORGANIZATION_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_ORGANIZATION.FCLT_ORG_PARENT_KEY ↔ FCLT_ORGANIZATION_HIST.FCLT_ORG_PARENT_KEY; profile_name_value_compatibility
- FCLT_ORGANIZATION.HR_DEPARTMENT_CODE_OLD ↔ FCLT_ORGANIZATION_HIST.HR_DEPARTMENT_CODE_OLD; profile_name_value_compatibility
- FCLT_ORGANIZATION.HR_DEPARTMENT_CODE_OLD ↔ HR_ORG_UNIT.HR_DEPARTMENT_CODE_OLD; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_ORGANIZATION.HR_DEPARTMENT_NAME ↔ FCLT_ORGANIZATION_HIST.HR_DEPARTMENT_NAME; profile_name_value_compatibility
- FCLT_ORGANIZATION.HR_ORG_UNIT_ID ↔ FCLT_ORGANIZATION_HIST.HR_ORG_UNIT_ID; profile_name_value_compatibility
- FCLT_ORGANIZATION.HR_ORG_UNIT_ID ↔ HR_ORG_UNIT.HR_ORG_UNIT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_ORGANIZATION.HR_ORG_UNIT_ID ↔ ZPM_ROOMS_LOAD.HR_ORG_UNIT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_ORGANIZATION.MAJOR_ORG ↔ FCLT_ORGANIZATION_HIST.MAJOR_ORG; profile_name_value_compatibility
- FCLT_ORGANIZATION.ORGANIZATION ↔ FCLT_ORGANIZATION_HIST.ORGANIZATION; profile_name_value_compatibility
- FCLT_ORGANIZATION.ORGANIZATION_ID ↔ FCLT_ORGANIZATION_HIST.ORGANIZATION_ID; profile_name_value_compatibility
- FCLT_ORGANIZATION.ORGANIZATION_LEVEL ↔ FCLT_ORGANIZATION_HIST.ORGANIZATION_LEVEL; profile_name_value_compatibility
- FCLT_ORGANIZATION.ORGANIZATION_NAME ↔ FCLT_ORGANIZATION_HIST.ORGANIZATION_NAME; profile_name_value_compatibility
- FCLT_ORGANIZATION.ORGANIZATION_NUMBER ↔ FCLT_ORGANIZATION_HIST.ORGANIZATION_NUMBER; profile_name_value_compatibility
- FCLT_ORGANIZATION.ORGANIZATION_SORT ↔ FCLT_ORGANIZATION_HIST.ORGANIZATION_SORT; profile_name_value_compatibility
- FCLT_ORGANIZATION.ORG_PARENT ↔ FCLT_ORGANIZATION_HIST.ORG_PARENT; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORGANIZATION_HIST.DLC_KEY ↔ FCLT_ORG_DLC_KEY.DLC_KEY; profile_name_value_compatibility
- FCLT_ORGANIZATION_HIST.FCLT_ORGANIZATION_KEY ↔ FCLT_ORG_DLC_KEY.FCLT_ORGANIZATION_KEY; profile_name_value_compatibility
- FCLT_ORGANIZATION_HIST.FISCAL_PERIOD ↔ FCLT_ROOMS_HIST.FISCAL_PERIOD; profile_name_value_compatibility
- FCLT_ORGANIZATION_HIST.WAREHOUSE_LOAD_DATE ↔ FCLT_ROOMS_HIST.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ORG_DLC_KEY.DLC_KEY ↔ HR_ORG_UNIT.DLC_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_ORG_DLC_KEY.DLC_KEY ↔ MASTER_DEPT_HIERARCHY.DLC_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_ORG_DLC_KEY.DLC_KEY ↔ SIS_DEPARTMENT.DLC_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_ORG_DLC_KEY.FCLT_ORGANIZATION_KEY ↔ FCLT_ROOMS.FCLT_ORGANIZATION_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- FCLT_ROOMS.ACCESS_LEVEL ↔ FCLT_ROOMS_HIST.ACCESS_LEVEL; profile_name_value_compatibility
- FCLT_ROOMS.ACCESS_LEVEL ↔ ZPM_ROOMS_LOAD.ACCESS_LEVEL; profile_name_value_compatibility
- FCLT_ROOMS.BUILDING_ROOM ↔ ZPM_ROOMS_LOAD.BUILDING_ROOM; declared_or_materialized_relationship
- FCLT_ROOMS.FCLT_MAJOR_USE_KEY ↔ FCLT_ROOMS_HIST.FCLT_MAJOR_USE_KEY; profile_name_value_compatibility
- FCLT_ROOMS.FLOOR ↔ FCLT_ROOMS_HIST.FLOOR; profile_name_value_compatibility
- FCLT_ROOMS.FLOOR ↔ ZPM_ROOMS_LOAD.FLOOR; profile_name_value_compatibility
- FCLT_ROOMS.MAJOR_USE_DESC ↔ FCLT_ROOMS_HIST.MAJOR_USE_DESC; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- FCLT_ROOMS_HIST.ACCESS_LEVEL ↔ ZPM_ROOMS_LOAD.ACCESS_LEVEL; profile_name_value_compatibility
- FCLT_ROOMS_HIST.FLOOR ↔ SPACE_FLOOR.FLOOR; profile_name_value_compatibility
- HR_FACULTY_ROSTER.APPOINTMENT_TYPE ↔ WAREHOUSE_USERS.APPOINTMENT_TYPE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_FACULTY_ROSTER.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- HR_ORG_UNIT.DLC_KEY ↔ MASTER_DEPT_HIERARCHY.DLC_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- HR_ORG_UNIT.HR_ORG_LEVEL1_ID ↔ HR_ORG_UNIT_NEW.HR_ORG_LEVEL1_ID; profile_name_value_compatibility
- HR_ORG_UNIT.HR_ORG_LEVEL1_NAME ↔ HR_ORG_UNIT_NEW.HR_ORG_LEVEL1_NAME; profile_name_value_compatibility
- HR_ORG_UNIT.HR_ORG_LEVEL1_SORT ↔ HR_ORG_UNIT_NEW.HR_ORG_LEVEL1_SORT; profile_name_value_compatibility
- HR_ORG_UNIT.HR_ORG_LEVEL2_ID ↔ HR_ORG_UNIT_NEW.HR_ORG_LEVEL2_ID; profile_name_value_compatibility
- HR_ORG_UNIT.HR_ORG_LEVEL2_NAME ↔ HR_ORG_UNIT_NEW.HR_ORG_LEVEL2_NAME; profile_name_value_compatibility
- HR_ORG_UNIT.HR_ORG_LEVEL2_SORT ↔ HR_ORG_UNIT_NEW.HR_ORG_LEVEL2_SORT; profile_name_value_compatibility
- HR_ORG_UNIT.HR_ORG_UNIT_LEVEL ↔ HR_ORG_UNIT_NEW.HR_ORG_UNIT_LEVEL; profile_name_value_compatibility
- HR_ORG_UNIT.ORG_HIER_ROOT_NAME ↔ HR_ORG_UNIT_NEW.ORG_HIER_ROOT_NAME; profile_name_value_compatibility
- HR_ORG_UNIT.ORG_HIER_TOP_LEVEL_NAME ↔ HR_ORG_UNIT_NEW.ORG_HIER_TOP_LEVEL_NAME; profile_name_value_compatibility
- HR_ORG_UNIT.WAREHOUSE_LOAD_DATE ↔ HR_ORG_UNIT_NEW.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.IAP_CATEGORY_NAME ↔ LIBRARY_SUBJECT_OFFERED.OFFER_DEPT_NAME; declared_or_materialized_relationship
- IAP_SUBJECT_CATEGORY.IAP_SUBJECT_CATEGORY_KEY ↔ IAP_SUBJECT_DETAIL.IAP_SUBJECT_CATEGORY_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.IAP_SUBJECT_PERSON_KEY ↔ IAP_SUBJECT_PERSON.IAP_SUBJECT_PERSON_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- IAP_SUBJECT_DETAIL.IAP_SUBJECT_SESSION_KEY ↔ IAP_SUBJECT_SESSION.IAP_SUBJECT_SESSION_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- IAP_SUBJECT_DETAIL.IAP_SUBJECT_SPONSOR_KEY ↔ IAP_SUBJECT_SPONSOR.IAP_SUBJECT_SPONSOR_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- IAP_SUBJECT_DETAIL.TERM_CODE ↔ SUBJECT_IAP_SCHEDULE.TERM_CODE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.TERM_CODE ↔ TIME_DAY.ACADEMIC_TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- IAP_SUBJECT_DETAIL.TERM_CODE ↔ TIP_DETAIL.TERM_CODE; declared_or_materialized_relationship
- IAP_SUBJECT_DETAIL.TERM_CODE ↔ TIP_SUBJECT_OFFERED.TERM_CODE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_DETAIL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_PERSON.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SESSION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- IAP_SUBJECT_SPONSOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_COURSE_INSTRUCTOR.DEPARTMENT ↔ LIBRARY_SUBJECT_OFFERED.OFFER_DEPT_NAME; declared_or_materialized_relationship
- LIBRARY_COURSE_INSTRUCTOR.DEPARTMENT ↔ SUBJECT_SUMMARY.DEPARTMENT_NAME; declared_or_materialized_relationship
- LIBRARY_COURSE_INSTRUCTOR.DEPARTMENT ↔ TIP_SUBJECT_OFFERED.OFFER_DEPT_NAME; declared_or_materialized_relationship
- LIBRARY_COURSE_INSTRUCTOR.INSTRUCTOR_NAME ↔ SE_PERSON.FULL_NAME; declared_or_materialized_relationship, target_disjoint_historical_join
- LIBRARY_COURSE_INSTRUCTOR.LIBRARY_COURSE_INSTRUCTOR_KEY ↔ LIBRARY_RESERVE_MATRL_DETAIL.LIBRARY_COURSE_INSTRUCTOR_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- LIBRARY_MATERIAL_STATUS.LIBRARY_MATERIAL_STATUS ↔ TIP_MATERIAL_STATUS.TIP_MATERIAL_STATUS; declared_or_materialized_relationship, target_disjoint_historical_join
- LIBRARY_MATERIAL_STATUS.LIBRARY_MATERIAL_STATUS_KEY ↔ LIBRARY_RESERVE_MATRL_DETAIL.LIBRARY_MATERIAL_STATUS_KEY; declared_or_materialized_relationship, profile_name_value_compatibility, target_disjoint_historical_join
- LIBRARY_RESERVE_CATALOG.LIBRARY_RESERVE_CATALOG_KEY ↔ LIBRARY_RESERVE_MATRL_DETAIL.LIBRARY_RESERVE_CATALOG_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- LIBRARY_RESERVE_MATRL_DETAIL.LIBRARY_MATERIAL_STATUS_KEY ↔ TIP_DETAIL.TIP_MATERIAL_STATUS_KEY; declared_or_materialized_relationship
- LIBRARY_RESERVE_MATRL_DETAIL.LIBRARY_SUBJECT_OFFERED_KEY ↔ LIBRARY_SUBJECT_OFFERED.LIBRARY_SUBJECT_OFFERED_KEY; declared_or_materialized_relationship
- LIBRARY_RESERVE_MATRL_DETAIL.SUBJECT_ID ↔ LIBRARY_SUBJECT_OFFERED.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- LIBRARY_RESERVE_MATRL_DETAIL.SUBJECT_ID ↔ SUBJECT_SUMMARY.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- LIBRARY_RESERVE_MATRL_DETAIL.SUBJECT_ID ↔ TIP_DETAIL.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- LIBRARY_RESERVE_MATRL_DETAIL.SUBJECT_ID ↔ TIP_SUBJECT_OFFERED.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- LIBRARY_RESERVE_MATRL_DETAIL.TERM_CODE ↔ LIBRARY_SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship, profile_name_value_compatibility, target_disjoint_historical_join
- LIBRARY_RESERVE_MATRL_DETAIL.TERM_CODE ↔ SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship
- LIBRARY_RESERVE_MATRL_DETAIL.TERM_CODE ↔ SUBJECT_SUMMARY.TERM_CODE; declared_or_materialized_relationship
- LIBRARY_RESERVE_MATRL_DETAIL.TERM_CODE ↔ TIP_DETAIL.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- LIBRARY_RESERVE_MATRL_DETAIL.TERM_CODE ↔ TIP_SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship
- LIBRARY_SUBJECT_OFFERED.COURSE_NUMBER ↔ SIS_SUBJECT_CODE.COURSE_NUMBER; declared_or_materialized_relationship, target_disjoint_historical_join
- LIBRARY_SUBJECT_OFFERED.COURSE_NUMBER ↔ SUBJECT_OFFERED_SUMMARY.COURSE_NUMBER; declared_or_materialized_relationship
- LIBRARY_SUBJECT_OFFERED.MASTER_SUBJECT_ID ↔ TIP_SUBJECT_OFFERED.MASTER_SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- LIBRARY_SUBJECT_OFFERED.MASTER_SUBJECT_ID_SORT ↔ SUBJECT_OFFERED.MASTER_SUBJECT_ID_SORT; declared_or_materialized_relationship
- LIBRARY_SUBJECT_OFFERED.MASTER_SUBJECT_ID_SORT ↔ TIP_SUBJECT_OFFERED.MASTER_SUBJECT_ID_SORT; declared_or_materialized_relationship, target_disjoint_historical_join
- LIBRARY_SUBJECT_OFFERED.OFFER_DEPT_CODE ↔ SIS_DEPARTMENT.DEPARTMENT_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- LIBRARY_SUBJECT_OFFERED.OFFER_DEPT_CODE ↔ TIP_SUBJECT_OFFERED.OFFER_DEPT_CODE; declared_or_materialized_relationship
- LIBRARY_SUBJECT_OFFERED.OFFER_DEPT_NAME ↔ SIS_DEPARTMENT.DEPARTMENT_NAME; declared_or_materialized_relationship
- LIBRARY_SUBJECT_OFFERED.OFFER_DEPT_NAME ↔ SUBJECT_SUMMARY.DEPARTMENT_NAME; declared_or_materialized_relationship
- LIBRARY_SUBJECT_OFFERED.OFFER_SCHOOL_NAME ↔ TIP_SUBJECT_OFFERED.OFFER_SCHOOL_NAME; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.RESPONSIBLE_FACULTY_MIT_ID ↔ SUBJECT_OFFERED.RESPONSIBLE_FACULTY_MIT_ID; declared_or_materialized_relationship
- LIBRARY_SUBJECT_OFFERED.SUBJECT_ID ↔ SUBJECT_OFFERED_SUMMARY.SUBJECT_ID; declared_or_materialized_relationship
- LIBRARY_SUBJECT_OFFERED.SUBJECT_ID ↔ SUBJECT_SUMMARY.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- LIBRARY_SUBJECT_OFFERED.SUBJECT_ID ↔ TIP_DETAIL.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- LIBRARY_SUBJECT_OFFERED.SUBJECT_ID ↔ TIP_SUBJECT_OFFERED.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- LIBRARY_SUBJECT_OFFERED.SUBJECT_TITLE ↔ SUBJECT_SUMMARY.SUBJECT_TITLE; declared_or_materialized_relationship
- LIBRARY_SUBJECT_OFFERED.TERM_CODE ↔ SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- LIBRARY_SUBJECT_OFFERED.TERM_CODE ↔ SUBJECT_SUMMARY.TERM_CODE; declared_or_materialized_relationship
- LIBRARY_SUBJECT_OFFERED.TERM_CODE ↔ TIP_DETAIL.TERM_CODE; declared_or_materialized_relationship
- LIBRARY_SUBJECT_OFFERED.TERM_CODE ↔ TIP_SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- LIBRARY_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_DCODE_PARENT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MASTER_DEPT_HIERARCHY.HIERARCHY_TYPE ↔ MASTER_DEPT_HIERARCHY_LINKS.HIERARCHY_TYPE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_HOLIDAY_CLOSING_CALENDAR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.DEPARTMENT ↔ SIS_ADMIN_DEPARTMENT.SIS_ADMIN_DEPARTMENT_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- MIT_STUDENT_DIRECTORY.DEPARTMENT ↔ SIS_COURSE_DESCRIPTION.DEPARTMENT; declared_or_materialized_relationship
- MIT_STUDENT_DIRECTORY.DEPARTMENT ↔ SIS_DEPARTMENT.DEPARTMENT_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- MIT_STUDENT_DIRECTORY.DEPARTMENT ↔ SIS_SUBJECT_CODE.DEPARTMENT_CODE; declared_or_materialized_relationship
- MIT_STUDENT_DIRECTORY.DEPARTMENT ↔ SUBJECT_OFFERED_SUMMARY.OFFER_DEPT_CODE; declared_or_materialized_relationship
- MIT_STUDENT_DIRECTORY.DEPARTMENT ↔ TIP_SUBJECT_OFFERED.OFFER_DEPT_CODE; declared_or_materialized_relationship
- MIT_STUDENT_DIRECTORY.DEPARTMENT_NAME ↔ SIS_ADMIN_DEPARTMENT.SIS_ADMIN_DEPARTMENT_NAME; declared_or_materialized_relationship
- MIT_STUDENT_DIRECTORY.DEPARTMENT_NAME ↔ SIS_DEPARTMENT.DEPARTMENT_NAME; declared_or_materialized_relationship
- MIT_STUDENT_DIRECTORY.FULL_NAME ↔ SE_PERSON.FULL_NAME; declared_or_materialized_relationship, target_disjoint_historical_join
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MIT_STUDENT_DIRECTORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST.IS_ACTIVE ↔ SE_PERSON.IS_ACTIVE; profile_name_value_compatibility
- MOIRA_LIST.MOIRA_LIST_KEY ↔ MOIRA_LIST_DETAIL.MOIRA_LIST_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- MOIRA_LIST_DETAIL.MOIRA_LIST_OWNER_KEY ↔ MOIRA_LIST_OWNER.MOIRA_LIST_OWNER_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_DETAIL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE ↔ PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- MOIRA_LIST_OWNER.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE ↔ SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- PERSON_AUTH_AREA.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_ADMIN_DEPARTMENT.SIS_ADMIN_DEPARTMENT_CODE ↔ SIS_COURSE_DESCRIPTION.DEPARTMENT; declared_or_materialized_relationship
- SIS_ADMIN_DEPARTMENT.SIS_ADMIN_DEPARTMENT_CODE ↔ SIS_DEPARTMENT.DEPARTMENT_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- SIS_ADMIN_DEPARTMENT.SIS_ADMIN_DEPARTMENT_CODE ↔ TIP_SUBJECT_OFFERED.OFFER_DEPT_CODE; declared_or_materialized_relationship
- SIS_ADMIN_DEPARTMENT.SIS_ADMIN_DEPARTMENT_NAME ↔ SIS_DEPARTMENT.DEPARTMENT_NAME; declared_or_materialized_relationship
- SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_ADMIN_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.COURSE ↔ SIS_SUBJECT_CODE.COURSE_NUMBER; declared_or_materialized_relationship, target_disjoint_historical_join
- SIS_COURSE_DESCRIPTION.COURSE ↔ SIS_SUBJECT_CODE.SUBJECT_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- SIS_COURSE_DESCRIPTION.COURSE ↔ SUBJECT_OFFERED_SUMMARY.COURSE_NUMBER; declared_or_materialized_relationship, target_disjoint_historical_join
- SIS_COURSE_DESCRIPTION.COURSE ↔ TIP_SUBJECT_OFFERED.COURSE_NUMBER; declared_or_materialized_relationship, target_disjoint_historical_join
- SIS_COURSE_DESCRIPTION.COURSE_LEVEL ↔ STUDENT_DEGREE_PROGRAM.COURSE_LEVEL; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.DEPARTMENT ↔ SIS_DEPARTMENT.DEPARTMENT_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- SIS_COURSE_DESCRIPTION.DEPARTMENT ↔ SIS_SUBJECT_CODE.DEPARTMENT_CODE; declared_or_materialized_relationship
- SIS_COURSE_DESCRIPTION.DEPARTMENT ↔ STUDENT_DEPARTMENT.DEPARTMENT_CODE; declared_or_materialized_relationship
- SIS_COURSE_DESCRIPTION.DEPARTMENT ↔ TIP_SUBJECT_OFFERED.OFFER_DEPT_CODE; declared_or_materialized_relationship
- SIS_COURSE_DESCRIPTION.DEPARTMENT_NAME ↔ SIS_DEPARTMENT.DEPARTMENT_NAME; declared_or_materialized_relationship
- SIS_COURSE_DESCRIPTION.DEPARTMENT_NAME ↔ SIS_SUBJECT_CODE.DEPARTMENT_NAME; declared_or_materialized_relationship, target_disjoint_historical_join
- SIS_COURSE_DESCRIPTION.FROM_TERM ↔ STUDENT_DEGREE_PROGRAM.FROM_TERM; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.IS_DEGREE_GRANTING ↔ SIS_DEPARTMENT.IS_DEGREE_GRANTING; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.SCHOOL_NAME ↔ SIS_SUBJECT_CODE.SCHOOL_NAME; declared_or_materialized_relationship, target_disjoint_historical_join
- SIS_COURSE_DESCRIPTION.THRU_TERM ↔ STUDENT_DEGREE_PROGRAM.THRU_TERM; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE ↔ SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_COURSE_DESCRIPTION.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_DEPARTMENT.DEPARTMENT_CODE ↔ SIS_SUBJECT_CODE.DEPARTMENT_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- SIS_DEPARTMENT.DEPARTMENT_CODE ↔ SUBJECT_OFFERED_SUMMARY.OFFER_DEPT_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- SIS_DEPARTMENT.DEPARTMENT_CODE ↔ SUBJECT_SUMMARY.DEPARTMENT_CODE; declared_or_materialized_relationship
- SIS_DEPARTMENT.DEPARTMENT_CODE ↔ TIP_SUBJECT_OFFERED.COURSE_NUMBER; declared_or_materialized_relationship
- SIS_DEPARTMENT.DEPARTMENT_CODE ↔ TIP_SUBJECT_OFFERED.OFFER_DEPT_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- SIS_DEPARTMENT.DEPARTMENT_NAME ↔ SIS_SUBJECT_CODE.DEPARTMENT_NAME; declared_or_materialized_relationship
- SIS_DEPARTMENT.DEPARTMENT_NAME ↔ SUBJECT_OFFERED.OFFER_DEPT_NAME; declared_or_materialized_relationship
- SIS_DEPARTMENT.DEPARTMENT_NAME ↔ SUBJECT_OFFERED_SUMMARY.OFFER_DEPT_NAME; declared_or_materialized_relationship
- SIS_DEPARTMENT.DEPARTMENT_NAME ↔ SUBJECT_SUMMARY.DEPARTMENT_NAME; declared_or_materialized_relationship
- SIS_DEPARTMENT.DEPARTMENT_NAME ↔ TIP_SUBJECT_OFFERED.OFFER_DEPT_NAME; declared_or_materialized_relationship
- SIS_DEPARTMENT.SCHOOL_CODE ↔ SIS_SUBJECT_CODE.SCHOOL_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- SIS_DEPARTMENT.SCHOOL_NAME_IN_COMMENCEMENT_BK ↔ STUDENT_DEGREE_PROGRAM.SCHOOL_NAME_IN_COMMENCEMENT_BK; profile_name_value_compatibility
- SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SIS_LOOKUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_DEPARTMENT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_LOOKUP.WAREHOUSE_LOAD_DATE ↔ SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_LOOKUP.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_LOOKUP.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_LOOKUP.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_LOOKUP.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_LOOKUP.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_LOOKUP.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_LOOKUP.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_LOOKUP.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_LOOKUP.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_LOOKUP.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_LOOKUP.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_LOOKUP.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_LOOKUP.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_LOOKUP.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_SUBJECT_CODE.COURSE_NUMBER ↔ SUBJECT_OFFERED_SUMMARY.COURSE_NUMBER; declared_or_materialized_relationship
- SIS_SUBJECT_CODE.COURSE_NUMBER ↔ TIP_SUBJECT_OFFERED.COURSE_NUMBER; declared_or_materialized_relationship
- SIS_SUBJECT_CODE.DEPARTMENT_CODE ↔ STUDENT_DEPARTMENT.DEPARTMENT_CODE; declared_or_materialized_relationship
- SIS_SUBJECT_CODE.DEPARTMENT_CODE ↔ SUBJECT_GROUPING.DEPARTMENT_CODE; profile_name_value_compatibility
- SIS_SUBJECT_CODE.DEPARTMENT_CODE ↔ SUBJECT_OFFERED_SUMMARY.OFFER_DEPT_CODE; declared_or_materialized_relationship
- SIS_SUBJECT_CODE.DEPARTMENT_CODE ↔ TIP_SUBJECT_OFFERED.OFFER_DEPT_CODE; declared_or_materialized_relationship
- SIS_SUBJECT_CODE.DEPARTMENT_NAME ↔ SUBJECT_GROUPING.DEPARTMENT_NAME; profile_name_value_compatibility
- SIS_SUBJECT_CODE.SCHOOL_CODE ↔ STUDENT_DEPARTMENT.SCHOOL_CODE; profile_name_value_compatibility
- SIS_SUBJECT_CODE.SCHOOL_NAME ↔ STUDENT_DEPARTMENT.SCHOOL_NAME; profile_name_value_compatibility
- SIS_SUBJECT_CODE.SCHOOL_NAME ↔ SUBJECT_GROUPING.SCHOOL_NAME; profile_name_value_compatibility
- SIS_SUBJECT_CODE.SUBJECT_CODE ↔ SUBJECT_OFFERED_SUMMARY.COURSE_NUMBER; declared_or_materialized_relationship
- SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE ↔ SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_SUBJECT_CODE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SPACE_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SIS_TERM_ADDRESS_CATEGORY.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_DETAIL.BUILDING_COMPONENT ↔ ZPM_ROOMS_LOAD.BUILDING_COMPONENT; profile_name_value_compatibility
- SPACE_DETAIL.FLOOR_KEY ↔ SPACE_FLOOR.FLOOR_KEY; declared_or_materialized_relationship, profile_name_value_compatibility, target_disjoint_historical_join
- SPACE_DETAIL.SPACE_UNIT_KEY ↔ SPACE_UNIT.SPACE_UNIT_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- SPACE_DETAIL.SPACE_USAGE_KEY ↔ SPACE_USAGE.SPACE_USAGE_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- SPACE_DETAIL.WAREHOUSE_LOAD_DATE ↔ SPACE_FLOOR.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_DETAIL.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_DETAIL.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_DETAIL.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_DETAIL.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_DETAIL.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_DETAIL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_DETAIL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_DETAIL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_DETAIL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_DETAIL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_DETAIL.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_FLOOR.FLOOR ↔ ZPM_ROOMS_LOAD.FLOOR; profile_name_value_compatibility
- SPACE_FLOOR.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_FLOOR.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_FLOOR.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_FLOOR.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_FLOOR.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_FLOOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_FLOOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_FLOOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_FLOOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_FLOOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_FLOOR.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_SUPERVISOR_USAGE.DEPT_NAMES ↔ SPACE_UNIT.DLC_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- SPACE_UNIT.SPACE_UNIT_CODE ↔ ZPM_ROOMS_LOAD.SPACE_UNIT_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- SPACE_UNIT.WAREHOUSE_LOAD_DATE ↔ SPACE_UNIT2.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_UNIT.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_UNIT.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_UNIT.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_UNIT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_UNIT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_UNIT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_UNIT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_UNIT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_UNIT.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_UNIT2.WAREHOUSE_LOAD_DATE ↔ SPACE_USAGE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_UNIT2.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_UNIT2.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_UNIT2.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_UNIT2.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_UNIT2.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_UNIT2.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_UNIT2.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_UNIT2.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_USAGE.WAREHOUSE_LOAD_DATE ↔ STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_USAGE.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_USAGE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_USAGE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_USAGE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_USAGE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_USAGE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SPACE_USAGE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE ↔ STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- STUDENT_DEGREE_PROGRAM.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- STUDENT_DEPARTMENT.DEPARTMENT_CODE ↔ SUBJECT_OFFERED_SUMMARY.OFFER_DEPT_CODE; declared_or_materialized_relationship
- STUDENT_DEPARTMENT.DEPARTMENT_CODE ↔ TIP_SUBJECT_OFFERED.OFFER_DEPT_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- STUDENT_DEPARTMENT.SCHOOL_CODE ↔ SUBJECT_SUMMARY.SCHOOL_CODE; profile_name_value_compatibility
- STUDENT_DEPARTMENT.SCHOOL_NAME ↔ SUBJECT_GROUPING.SCHOOL_NAME; profile_name_value_compatibility
- STUDENT_DEPARTMENT.SCHOOL_NAME ↔ SUBJECT_SUMMARY.SCHOOL_NAME; profile_name_value_compatibility
- STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- STUDENT_ETHNIC_SUBGROUP.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SUBJECT_ATTRIBUTE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SUBJECT_ENROLLABLE.CLUSTER_LIST ↔ SUBJECT_OFFERED.CLUSTER_LIST; profile_name_value_compatibility
- SUBJECT_ENROLLABLE.CLUSTER_LIST ↔ SUBJECT_OFFERED_SUMMARY.CLUSTER_LIST; profile_name_value_compatibility
- SUBJECT_ENROLLABLE.MASTER_SUBJECT_ID ↔ SUBJECT_OFFERED.MASTER_SUBJECT_ID; profile_name_value_compatibility
- SUBJECT_ENROLLABLE.MASTER_SUBJECT_ID ↔ SUBJECT_OFFERED_SUMMARY.MASTER_SUBJECT_ID; profile_name_value_compatibility
- SUBJECT_ENROLLABLE.OFFER_DEPT_CODE ↔ SUBJECT_OFFERED.OFFER_DEPT_CODE; profile_name_value_compatibility
- SUBJECT_ENROLLABLE.OFFER_DEPT_CODE ↔ SUBJECT_OFFERED_SUMMARY.OFFER_DEPT_CODE; profile_name_value_compatibility
- SUBJECT_ENROLLABLE.TERM_CODE ↔ SUBJECT_OFFERED_SUMMARY.TERM_CODE; profile_name_value_compatibility
- SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SUBJECT_ENROLLABLE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SUBJECT_GROUPING.SCHOOL_NAME ↔ SUBJECT_SUMMARY.SCHOOL_NAME; profile_name_value_compatibility
- SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE ↔ SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SUBJECT_GROUPING.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SUBJECT_IAP_SCHEDULE.TERM_CODE ↔ TIP_SUBJECT_OFFERED.TERM_CODE; profile_name_value_compatibility
- SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SUBJECT_IAP_SCHEDULE.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SUBJECT_OFFERED.CLUSTER_ENROLLMENT_NUMBER ↔ SUBJECT_OFFERED_SUMMARY.CLUSTER_ENROLLMENT_NUMBER; profile_name_value_compatibility
- SUBJECT_OFFERED.CLUSTER_TYPE ↔ SUBJECT_OFFERED_SUMMARY.CLUSTER_TYPE; profile_name_value_compatibility
- SUBJECT_OFFERED.CLUSTER_TYPE ↔ SUBJECT_SUMMARY.CLUSTER_TYPE; profile_name_value_compatibility
- SUBJECT_OFFERED.CLUSTER_TYPE_DESC ↔ SUBJECT_OFFERED_SUMMARY.CLUSTER_TYPE_DESC; profile_name_value_compatibility
- SUBJECT_OFFERED.CLUSTER_TYPE_DESC ↔ SUBJECT_SUMMARY.CLUSTER_TYPE_DESC; profile_name_value_compatibility
- SUBJECT_OFFERED.COMPOSITE_SUBJECT_KEY ↔ SUBJECT_OFFERED_SUMMARY.COMPOSITE_SUBJECT_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- SUBJECT_OFFERED.COURSE_NUMBER ↔ SUBJECT_OFFERED_SUMMARY.COURSE_NUMBER; profile_name_value_compatibility
- SUBJECT_OFFERED.HGN_CODE ↔ SUBJECT_OFFERED_SUMMARY.HGN_CODE; profile_name_value_compatibility
- SUBJECT_OFFERED.HGN_CODE_DESC ↔ SUBJECT_OFFERED_SUMMARY.HGN_CODE_DESC; profile_name_value_compatibility
- SUBJECT_OFFERED.MASTER_SUBJECT_ID ↔ SUBJECT_OFFERED_SUMMARY.MASTER_SUBJECT_ID; profile_name_value_compatibility
- SUBJECT_OFFERED.MASTER_SUBJECT_ID ↔ SUBJECT_SUMMARY.MASTER_SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- SUBJECT_OFFERED.MASTER_SUBJECT_ID ↔ TIP_SUBJECT_OFFERED.MASTER_SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- SUBJECT_OFFERED.MASTER_SUBJECT_ID_SORT ↔ SUBJECT_OFFERED_SUMMARY.MASTER_SUBJECT_ID_SORT; profile_name_value_compatibility
- SUBJECT_OFFERED.MASTER_SUBJECT_ID_SORT ↔ SUBJECT_SUMMARY.MASTER_SUBJECT_ID_SORT; declared_or_materialized_relationship, target_disjoint_historical_join
- SUBJECT_OFFERED.MASTER_SUBJECT_ID_SORT ↔ TIP_SUBJECT_OFFERED.MASTER_SUBJECT_ID_SORT; declared_or_materialized_relationship, target_disjoint_historical_join
- SUBJECT_OFFERED.NUM_ENROLLED_STUDENTS ↔ SUBJECT_OFFERED_SUMMARY.NUM_ENROLLED_STUDENTS; profile_name_value_compatibility
- SUBJECT_OFFERED.OFFER_DEPT_CODE ↔ SUBJECT_OFFERED_SUMMARY.OFFER_DEPT_CODE; declared_or_materialized_relationship, profile_name_value_compatibility
- SUBJECT_OFFERED.OFFER_DEPT_CODE ↔ TIP_SUBJECT_OFFERED.OFFER_DEPT_CODE; declared_or_materialized_relationship
- SUBJECT_OFFERED.OFFER_DEPT_NAME ↔ SUBJECT_OFFERED_SUMMARY.OFFER_DEPT_NAME; profile_name_value_compatibility
- SUBJECT_OFFERED.OFFER_DEPT_NAME ↔ TIP_SUBJECT_OFFERED.OFFER_DEPT_NAME; declared_or_materialized_relationship
- SUBJECT_OFFERED.OFFER_SCHOOL_NAME ↔ SUBJECT_OFFERED_SUMMARY.OFFER_SCHOOL_NAME; profile_name_value_compatibility
- SUBJECT_OFFERED.RESPONSIBLE_FACULTY_MIT_ID ↔ SUBJECT_OFFERED_SUMMARY.RESPONSIBLE_FACULTY_MIT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- SUBJECT_OFFERED.SUBJECT_ENROLLMENT_NUMBER ↔ SUBJECT_OFFERED_SUMMARY.SUBJECT_ENROLLMENT_NUMBER; profile_name_value_compatibility
- SUBJECT_OFFERED.SUBJECT_ID ↔ SUBJECT_OFFERED_SUMMARY.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- SUBJECT_OFFERED.SUBJECT_ID ↔ SUBJECT_SUMMARY.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- SUBJECT_OFFERED.SUBJECT_ID_SORT ↔ SUBJECT_OFFERED_SUMMARY.SUBJECT_ID_SORT; declared_or_materialized_relationship, target_disjoint_historical_join
- SUBJECT_OFFERED.SUBJECT_ID_SORT ↔ SUBJECT_SUMMARY.SUBJECT_ID_SORT; declared_or_materialized_relationship, target_disjoint_historical_join
- SUBJECT_OFFERED.SUBJECT_ID_SORT ↔ TIP_SUBJECT_OFFERED.SUBJECT_ID_SORT; declared_or_materialized_relationship, target_disjoint_historical_join
- SUBJECT_OFFERED.SUBJECT_OFFERED_SUMMARY_KEY ↔ SUBJECT_OFFERED_SUMMARY.SUBJECT_OFFERED_SUMMARY_KEY; declared_or_materialized_relationship
- SUBJECT_OFFERED.SUBJECT_SUMMARY_KEY ↔ SUBJECT_SUMMARY.SUBJECT_SUMMARY_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- SUBJECT_OFFERED.TERM_CODE ↔ SUBJECT_OFFERED_SUMMARY.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- SUBJECT_OFFERED.TERM_CODE ↔ SUBJECT_SUMMARY.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- SUBJECT_OFFERED.TERM_CODE ↔ TIP_DETAIL.TERM_CODE; declared_or_materialized_relationship
- SUBJECT_OFFERED.TERM_CODE ↔ TIP_SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE ↔ SUBJECT_OFFERED_SUMMARY.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SUBJECT_OFFERED_SUMMARY.CLUSTER_TYPE ↔ SUBJECT_SUMMARY.CLUSTER_TYPE; profile_name_value_compatibility
- SUBJECT_OFFERED_SUMMARY.CLUSTER_TYPE_DESC ↔ SUBJECT_SUMMARY.CLUSTER_TYPE_DESC; profile_name_value_compatibility
- SUBJECT_OFFERED_SUMMARY.LECTURE_UNITS ↔ SUBJECT_SUMMARY.LECTURE_UNITS; profile_name_value_compatibility
- SUBJECT_OFFERED_SUMMARY.OFFER_DEPT_CODE ↔ SUBJECT_SUMMARY.DEPARTMENT_CODE; declared_or_materialized_relationship
- SUBJECT_OFFERED_SUMMARY.OFFER_DEPT_NAME ↔ SUBJECT_SUMMARY.DEPARTMENT_NAME; declared_or_materialized_relationship
- SUBJECT_OFFERED_SUMMARY.SUBJECT_ID ↔ SUBJECT_SUMMARY.SUBJECT_ID; declared_or_materialized_relationship
- SUBJECT_OFFERED_SUMMARY.SUBJECT_ID ↔ TIP_DETAIL.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- SUBJECT_OFFERED_SUMMARY.SUBJECT_ID ↔ TIP_SUBJECT_OFFERED.SUBJECT_ID; declared_or_materialized_relationship
- SUBJECT_OFFERED_SUMMARY.TERM_CODE ↔ TIP_DETAIL.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- SUBJECT_OFFERED_SUMMARY.TERM_CODE ↔ TIP_SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship
- SUBJECT_SUMMARY.DEPARTMENT_NAME ↔ TIP_SUBJECT_OFFERED.OFFER_DEPT_NAME; declared_or_materialized_relationship
- SUBJECT_SUMMARY.SUBJECT_ID ↔ TIP_DETAIL.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- SUBJECT_SUMMARY.SUBJECT_ID ↔ TIP_SUBJECT_OFFERED.SUBJECT_ID; declared_or_materialized_relationship
- SUBJECT_SUMMARY.SUBJECT_TITLE ↔ TIP_SUBJECT_OFFERED.SUBJECT_TITLE; declared_or_materialized_relationship
- SUBJECT_SUMMARY.TERM_CODE ↔ TIP_DETAIL.TERM_CODE; declared_or_materialized_relationship
- SUBJECT_SUMMARY.TERM_CODE ↔ TIP_SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship
- SUBJECT_SUMMARY.WAREHOUSE_LOAD_DATE ↔ TIME_QUARTER.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SUBJECT_SUMMARY.WAREHOUSE_LOAD_DATE ↔ TIP_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SUBJECT_SUMMARY.WAREHOUSE_LOAD_DATE ↔ TIP_MATERIAL_STATUS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- SUBJECT_SUMMARY.WAREHOUSE_LOAD_DATE ↔ TIP_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- TIME_DAY.FISCAL_PERIOD ↔ TIME_MONTH.FISCAL_PERIOD; declared_or_materialized_relationship, target_disjoint_historical_join
- TIME_MONTH.FISCAL_YEAR ↔ TIME_QUARTER.FISCAL_YEAR; declared_or_materialized_relationship, target_disjoint_historical_join
- TIME_QUARTER.WAREHOUSE_LOAD_DATE ↔ TIP_DETAIL.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- TIME_QUARTER.WAREHOUSE_LOAD_DATE ↔ TIP_MATERIAL_STATUS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- TIME_QUARTER.WAREHOUSE_LOAD_DATE ↔ TIP_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- TIP_DETAIL.SUBJECT_ID ↔ TIP_SUBJECT_OFFERED.SUBJECT_ID; declared_or_materialized_relationship, target_disjoint_historical_join
- TIP_DETAIL.TERM_CODE ↔ TIP_SUBJECT_OFFERED.TERM_CODE; declared_or_materialized_relationship, target_disjoint_historical_join
- TIP_DETAIL.TIP_MATERIAL_KEY ↔ TIP_MATERIAL.TIP_MATERIAL_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- TIP_DETAIL.TIP_MATERIAL_STATUS_KEY ↔ TIP_MATERIAL_STATUS.TIP_MATERIAL_STATUS_KEY; declared_or_materialized_relationship, profile_name_value_compatibility, target_disjoint_historical_join
- TIP_DETAIL.TIP_SUBJECT_OFFERED_KEY ↔ TIP_SUBJECT_OFFERED.TIP_SUBJECT_OFFERED_KEY; declared_or_materialized_relationship, target_disjoint_historical_join
- TIP_DETAIL.WAREHOUSE_LOAD_DATE ↔ TIP_MATERIAL_STATUS.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- TIP_DETAIL.WAREHOUSE_LOAD_DATE ↔ TIP_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- TIP_MATERIAL_STATUS.WAREHOUSE_LOAD_DATE ↔ TIP_SUBJECT_OFFERED.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility
- ZIP_CANADA.WAREHOUSE_LOAD_DATE ↔ ZIP_USA.WAREHOUSE_LOAD_DATE; profile_name_value_compatibility

## 业务口径、总体与粒度

### number of regular academic terms

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"number of regular academic terms\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.e3a67becc98c3d4af583\", \"physical_identifier\": \"ACADEMIC_TERMS.ACADEMIC_TERMS_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e3a67becc98c3d4af583"
  ]
}
```

### variance

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ec2847a810954dd64926"
  ]
}
```

### variance

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.80ab96774a86f61b4cfb"
  ]
}
```

### degree year

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"degree year\", \"year category\", \"minimum degree year\", \"academic year category\", \"degree year greater than 1900\", \"geometric mean of degree year\", \"degree year is greater than 1900\", \"geometric mean of the degree year\", \"academic year as 'RECENT', 'OLD', or 'AVERAGE'\", \"geometric mean of the degree year for that academic year (considering only degree years greater than 1900)\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.ac5dd165b5081f813658\", \"physical_identifier\": \"ACADEMIC_TERMS.DEGREE_YEAR\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ac5dd165b5081f813658"
  ]
}
```

### financial aid year

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"financial aid year\", \"geometric mean of financial aid year\", \"running sum of academic years within the financial aid year group\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.662b9cb6930f4b03d60d\", \"physical_identifier\": \"ACADEMIC_TERMS.FINANCIAL_AID_YEAR\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.662b9cb6930f4b03d60d"
  ]
}
```

### first day of classes

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"courses with materials\" is predicated by \"TIP_SUBJECT_OFFERED.IS_NO_COURSE_MATERIAL = 'N'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.75191383f6f4420daaa6"
  ]
}
```

### current term

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"degree-granting\" is predicated by \"TABLE.IS_DEGREE_GRANTING = 'Y'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.1782afd9bc3f38cbedc8"
  ]
}
```

### regular term

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e0702ee17dbbc55973de"
  ]
}
```

### last day of final exam

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"last day of final exam\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.3a8d15ee1bbb775829e6\", \"physical_identifier\": \"ACADEMIC_TERMS.LAST_DAY_OF_FINAL_EXAM\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.3a8d15ee1bbb775829e6"
  ]
}
```

### IAP

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d6161653c3243afd3a5b"
  ]
}
```

### term

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c62b40101599e9fa98a1"
  ]
}
```

### end date

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8797b8adcebcd59f9570"
  ]
}
```

### since 2010

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.88e1500d70dddf41d79b"
  ]
}
```

### Previous

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.aabeca9d660d220aa13b"
  ]
}
```

### term status indicator

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"term status indicator\", \"term status indicator of 'P'\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.01412d54117365ba11b8\", \"physical_identifier\": \"ACADEMIC_TERMS.TERM_STATUS_INDICATOR\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.01412d54117365ba11b8"
  ]
}
```

### academic term

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"academic term\", \"academic terms key\", \"ACADEMIC_TERMS_ALL\", \"total regular terms\", \"ACADEMIC_TERMS_ALL table\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.0fa5b9f4173f3186ca25\", \"physical_identifier\": \"ACADEMIC_TERMS_ALL.ACADEMIC_TERMS_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0fa5b9f4173f3186ca25"
  ]
}
```

### 2000

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.30f2d4e5853f0f6ed7ab"
  ]
}
```

### academic year

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5d6750ad6eb6ccac78a1"
  ]
}
```

### academic year

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"academic year\", \"financial aid year\", \"average record count\", \"financial aid year group\", \"previous term's running sum\", \"running sum of academic years\", \"average record count in a window\", \"previous term's financial aid year\", \"maximum windowed average record count\", \"total number of such terms per financial aid year\", \"grand total average record count for tip detail records\", \"running sum of academic years within the financial aid year group\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.da48a8ff9fb3db45fcfb\", \"physical_identifier\": \"ACADEMIC_TERMS_ALL.FINANCIAL_AID_YEAR\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.da48a8ff9fb3db45fcfb"
  ]
}
```

### current term

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f3bdea0ce3fa4cbb6bd9"
  ]
}
```

### last day of final exam

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"courses with materials\" is predicated by \"TIP_SUBJECT_OFFERED.IS_NO_COURSE_MATERIAL = 'N'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.49b918657536f2852ebc"
  ]
}
```

### term

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8db0040be81811ba0efb"
  ]
}
```

### summer term

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.60a98d36ad604a9615a4"
  ]
}
```

### academic term

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"academic term\", \"term end date\", \"maximum term end date\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.3ec342e438fdd35e0676\", \"physical_identifier\": \"ACADEMIC_TERMS_ALL.TERM_END_DATE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.3ec342e438fdd35e0676"
  ]
}
```

### academic term

```json
{
  "kind": "metric",
  "formula": "\"biology and chemistry department\" is predicated by \"TABLE.OFFER_DEPT_NAME IN ('Chemistry', 'Biology')\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.37e961ebbb374bd6be68"
  ]
}
```

### term status 'P'

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.262853201cd190c551fd"
  ]
}
```

### units range

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ffa00a9f2ba69b3e265c"
  ]
}
```

### terms

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.162bf1bb9038a55bea1f"
  ]
}
```

### academic term

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2a707c2c95937b0b631c"
  ]
}
```

### academic terms

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"academic terms\", \"term indicator\", \"term indicator 'C'\", \"term indicator is 'C'\", \"term status indicator\", \"term status indicator 'P'\", \"windowed average academic year\", \"average academic year in a window\", \"window of 2 preceding and 2 following rows grouped by the term indicator\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.7293779beed23b59ef98\", \"physical_identifier\": \"ACADEMIC_TERM_PARAMETER.TERM_INDICATOR\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.7293779beed23b59ef98"
  ]
}
```

### CurrentTerm

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.fcbb4157c1f5e12123d5"
  ]
}
```

### academic terms

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"academic terms\", \"term start date\", \"windowed average academic year\", \"average academic year in a window\", \"window of 2 preceding and 2 following rows grouped by the term indicator\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.bb6f9bd16d0f89c9df00\", \"physical_identifier\": \"ACADEMIC_TERM_PARAMETER.TERM_START_DATE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.bb6f9bd16d0f89c9df00"
  ]
}
```

### category code

```json
{
  "kind": "metric",
  "formula": "\"degree-granting\" is predicated by \"TABLE.IS_DEGREE_GRANTING = 'Y'\" | \"Course 6\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4515a67acf4252666722"
  ]
}
```

### category title

```json
{
  "kind": "metric",
  "formula": "\"degree-granting\" is predicated by \"TABLE.IS_DEGREE_GRANTING = 'Y'\" | \"Course 6\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0930536fc005503412b0"
  ]
}
```

### four digit code

```json
{
  "kind": "metric",
  "formula": "\"degree-granting\" is predicated by \"TABLE.IS_DEGREE_GRANTING = 'Y'\" | \"Course 6\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.3b0d36a64bdda4a1647c"
  ]
}
```

### four digit title

```json
{
  "kind": "metric",
  "formula": "\"degree-granting\" is predicated by \"TABLE.IS_DEGREE_GRANTING = 'Y'\" | \"Course 6\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.3c580b9984c77dee7d65"
  ]
}
```

### program code

```json
{
  "kind": "metric",
  "formula": "\"degree-granting\" is predicated by \"TABLE.IS_DEGREE_GRANTING = 'Y'\" | \"Course 6\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.14934e3bf61f47e1545c"
  ]
}
```

### program

```json
{
  "kind": "metric",
  "formula": "\"degree-granting\" is predicated by \"TABLE.IS_DEGREE_GRANTING = 'Y'\" | \"Course 6\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.7d39a62a315a14f13caf"
  ]
}
```

### program's CIP version

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Course 17\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.3fd872543be14ac81a5b"
  ]
}
```

### after '01-JAN-20'

```json
{
  "kind": "metric",
  "formula": "\"degree-granting\" is predicated by \"TABLE.IS_DEGREE_GRANTING = 'Y'\" | \"Course 6\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d7c05d85fce2c0541ffe"
  ]
}
```

### academic year

```json
{
  "kind": "metric",
  "formula": "\"Computer Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\" | \"except Cambridge-MIT Institute\" is predicated by \"TABLE.ORGANIZATION_NAME NOT IN ('CAMBRIDGE-MIT INST')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.be0e5833676d48edb29a"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"biology department\" is predicated by \"LOWER(TABLE.DLC_NAME) = LOWER('Biology')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.58d6fcd2d26b3b2c4aa6"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Mathematics\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.97b5c897ad1a30d8844f"
  ]
}
```

### design units

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"design units\", \"courses with design units 3 or more\", \"number of courses with design units at least 3\", \"number of courses where the design units are at least 3\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.13839f70e81ef74d83c9\", \"physical_identifier\": \"CIS_COURSE_CATALOG.DESIGN_UNITS\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.13839f70e81ef74d83c9"
  ]
}
```

### offered this year

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.81c323273f247cabec8f"
  ]
}
```

### maximum number of lab units

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_CODE = '18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e19d6c4d7334d5046984"
  ]
}
```

### average number of lecture units

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_CODE = '18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.92d1787a8cfe461f0368"
  ]
}
```

### course catalog

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4ddf38a3b3680bdc0915"
  ]
}
```

### undergraduate

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Mathematics\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0c9d2e82a235ab4c71fa"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Political Science\" is predicated by \"TABLE.DEPARTMENT_CODE = '17'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a58853cafe75d8e9fc55"
  ]
}
```

### CIS course catalog

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Mathematics\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a3bbac9f2a7b81279db2"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Course 17\" is predicated by \"TABLE.DEPARTMENT_CODE = '17'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.93455faf9fa1077850fd"
  ]
}
```

### courses

```json
{
  "kind": "metric",
  "formula": "\"Mechanical Engineering\" is predicated by \"UPPER(TABLE.SIS_ADMIN_DEPARTMENT_NAME) = 'MECHANICAL ENGINEERING'\" | \"Course 2\" is predicated by \"UPPER(TABLE.SIS_ADMIN_DEPARTMENT_NAME) = 'MECHANICAL ENGINEERING'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.9c4d0100a4dc7227e275"
  ]
}
```

### courses

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.62ff6bbbb1893f105c60"
  ]
}
```

### range

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Political Science\" is predicated by \"TABLE.DEPARTMENT_CODE = '17'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d2a08b4c73936bc2e680"
  ]
}
```

### description in the bulletin

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8a082c172000e83d4a94"
  ]
}
```

### description

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Political Science\" is predicated by \"TABLE.DEPARTMENT = '17'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e2981a346a693f4b41d8"
  ]
}
```

### 2022

```json
{
  "kind": "metric",
  "formula": "\"degree-granting\" is predicated by \"TABLE.IS_DEGREE_GRANTING = 'Y'\" | \"Biology\" is predicated by \"TABLE.DEPARTMENT_CODE = '7'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.32ed9d51f41e54f7d1e2"
  ]
}
```

### CI subject percentage

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.56a0a318a13421252b79"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_CODE = '18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ddd34f523a5ab1382d14"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.386ad834e5a93df3fe23"
  ]
}
```

### average number of design units

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"average number of design units\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.b6053ef2d00b98aec040\", \"physical_identifier\": \"COURSE_CATALOG_SUBJECT_OFFERED.DESIGN_UNITS\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b6053ef2d00b98aec040"
  ]
}
```

### term code

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.6839e31e5a9faf29caa7"
  ]
}
```

### equivalent subjects

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.7fa332698cfc3d5d5105"
  ]
}
```

### grade rule

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.79d4a70e0b7630d5450b"
  ]
}
```

### non-repeatable-for-credit

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"non-repeatable-for-credit\", \"not repeatable for credit\", \"non-repeatable-for-credit subjects\", \"subjects not repeatable for credit\", \"number of non-repeatable-for-credit subjects\", \"number of non-repeatable-for-credit subjects offered in the fall term\", \"top 10 by number of non-repeatable-for-credit subjects offered in the fall term\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.f656a461469994fbadeb\", \"physical_identifier\": \"COURSE_CATALOG_SUBJECT_OFFERED.GRADE_RULE_DESC\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f656a461469994fbadeb"
  ]
}
```

### grade type

```json
{
  "kind": "metric",
  "formula": "\"degree-granting\" is predicated by \"TABLE.IS_DEGREE_GRANTING = 'Y'\" | \"Biology\" is predicated by \"TABLE.DEPARTMENT_CODE = '7'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a3be825e4c14805d1493"
  ]
}
```

### grade type description

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"grade type description\", \"subject's grade type description\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.4c41068ca8f4cd53ac07\", \"physical_identifier\": \"COURSE_CATALOG_SUBJECT_OFFERED.GRADE_TYPE_DESC\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4c41068ca8f4cd53ac07"
  ]
}
```

### HE

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Course 17\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b0755576a4fe6d1a0def"
  ]
}
```

### grand total

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"grand total\", \"HASS attribute description\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.6d90af953ba69b062669\", \"physical_identifier\": \"COURSE_CATALOG_SUBJECT_OFFERED.HASS_ATTRIBUTE_DESC\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.6d90af953ba69b062669"
  ]
}
```

### HGN code

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Course 17\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.7f67d23fdca3b2f45095"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.82e48311c1dd95683de9"
  ]
}
```

### variance

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.fa4c2c765ad3052c1b89"
  ]
}
```

### spring term

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.92619c6c66e55f00e2bc"
  ]
}
```

### summer term

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5f5fddfd6ddb56739e03"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2f3c1f12edd936a6ac8c"
  ]
}
```

### printed in the bulletin

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_CODE = '18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a1b2f5836cb0e7092df7"
  ]
}
```

### variance

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a52fa5501fdf8de9c1e5"
  ]
}
```

### joint subject

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Physics\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Physics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d6688d7ed6cb6ac595a3"
  ]
}
```

### lab units

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.1a6380c060beb1f43d70"
  ]
}
```

### average

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.278e6b22d02f1e488684"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"Computer Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_NAME = 'Ray and Maria Stata Center'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ebc1d7dc5bf6b059d26f"
  ]
}
```

### faculty

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.bcf013a7b07242757bb5"
  ]
}
```

### instructor

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.9afbd6914d2f62f8fa8b"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT = '18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.93cbfe147f6df747e400"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c18e6303031cf6db0b10"
  ]
}
```

### range

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.581c33297df2e13a62d1"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.89a545923cbd7131fddb"
  ]
}
```

### short title

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.967c0326940016d8471e"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.83b1c42b2130dd8b772e"
  ]
}
```

### term

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.1604de637bea30547625"
  ]
}
```

### full term subjects

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.dbd1ab7439d2beafef4a"
  ]
}
```

### units

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a07e3a33a120b72af4cf"
  ]
}
```

### department

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.1f871fd414467bfa077b"
  ]
}
```

### department number

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"department number\", \"average area window\", \"deviation of the room's area from the average area for its department\", \"average area of rooms in a window of 2 preceding and 2 following rows grouped by department number and ordered by floor\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.99ef6a4215d581863d2b\", \"physical_identifier\": \"EMPLOYEE_DIRECTORY.DEPARTMENT_NUMBER\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.99ef6a4215d581863d2b"
  ]
}
```

### email address

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Course 17\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.eea164b191ace8396fbf"
  ]
}
```

### full name

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.3bf9b3dbfb2d96eed547"
  ]
}
```

### average office phone number

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_CODE = '18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.75cd256982ac4dabd609"
  ]
}
```

### MIT ID

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e5a1965eb91c382d0eaf"
  ]
}
```

### office location

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Course 17\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0c9cbab5c1228e42f459"
  ]
}
```

### office phone number

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Course 17\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.1648dbb1f490d0dd68b4"
  ]
}
```

### access level

```json
{
  "kind": "metric",
  "formula": "\"academic building\" is predicated by \"TABLE.BUILDING_TYPE = 'ACADEMIC'\" | \"used as a residence\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.7a4de1afd5c4c5e26010"
  ]
}
```

### access level name

```json
{
  "kind": "metric",
  "formula": "\"academic building\" is predicated by \"TABLE.BUILDING_TYPE = 'ACADEMIC'\" | \"residential\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ec59e0c52efa3abe1230"
  ]
}
```

### assignable area

```json
{
  "kind": "metric",
  "formula": "\"academic building\" is predicated by \"TABLE.BUILDING_TYPE = 'ACADEMIC'\" | \"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.281c93b5e5c6729ee5cd"
  ]
}
```

### building height

```json
{
  "kind": "metric",
  "formula": "\"residential\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\" | \"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.be5160706a45b9c144f3"
  ]
}
```

### building

```json
{
  "kind": "metric",
  "formula": "\"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_NAME = 'Ray and Maria Stata Center'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.6124be9f4bc75cd0b05c"
  ]
}
```

### building

```json
{
  "kind": "metric",
  "formula": "\"academic building\" is predicated by \"TABLE.BUILDING_TYPE = 'ACADEMIC'\" | \"Fairchild Building\" is predicated by \"TABLE.BUILDING_KEY = 36\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.512dcb54580de6fd4abc"
  ]
}
```

### buildings

```json
{
  "kind": "metric",
  "formula": "\"used as a residence\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\" | No relevant external evidence for 'residential' or 'used as a residence' in the provided list, so none added.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.de17dcd380bdfb50c138"
  ]
}
```

### ACADEMIC

```json
{
  "kind": "metric",
  "formula": "\"residential\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\" | \"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2ab1f92b7dae79c63653"
  ]
}
```

### building use

```json
{
  "kind": "metric",
  "formula": "\"used as a residence\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\" | \"Ashdown\" is predicated by \"TABLE.BUILDING_NAME = 'ASHDOWN HOUSE'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.7bd64c2f6af284285e1b"
  ]
}
```

### campus sector

```json
{
  "kind": "metric",
  "formula": "\"academic building\" is predicated by \"TABLE.BUILDING_TYPE = 'ACADEMIC'\" | \"used as a residence\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.90be693ace59a4ca125f"
  ]
}
```

### current and historical building data

```json
{
  "kind": "metric",
  "formula": "\"used as a residence\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\" | \"residential\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.7c1e201f7a2ca7a4fb3d"
  ]
}
```

### year built

```json
{
  "kind": "metric",
  "formula": "\"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\" | \"academic building\" is predicated by \"TABLE.BUILDING_TYPE = 'ACADEMIC'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.bc6a3dd8aa8859cbbadf"
  ]
}
```

### gross area

```json
{
  "kind": "metric",
  "formula": "\"used as a residence\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\" | \"Ashdown\" is predicated by \"TABLE.BUILDING_NAME = 'ASHDOWN HOUSE'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c7f2519b85ac0959479b"
  ]
}
```

### building

```json
{
  "kind": "metric",
  "formula": "\"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_NAME = 'Ray and Maria Stata Center'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.1fe1db5c6fa40e57394e"
  ]
}
```

### LOW_CAPACITY

```json
{
  "kind": "metric",
  "formula": "\"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_NAME = 'Ray and Maria Stata Center'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.60662c37d8ebce8da334"
  ]
}
```

### owned

```json
{
  "kind": "metric",
  "formula": "\"residential\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\" | \"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2c3f579152541ab33f36"
  ]
}
```

### MIT

```json
{
  "kind": "metric",
  "formula": "\"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_NAME = 'Ray and Maria Stata Center'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.300841a5a22f3a9875ec"
  ]
}
```

### address purpose

```json
{
  "kind": "metric",
  "formula": "\"used as a residence\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\" | \"Ashdown\" is predicated by \"TABLE.BUILDING_NAME = 'ASHDOWN HOUSE'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.027c3220c8795c64a484"
  ]
}
```

### building

```json
{
  "kind": "metric",
  "formula": "\"department of facilities\" is predicated by \"TABLE.ORGANIZATION_NAME = 'DP OF FACILITIES'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8ba5d69ad0566e306e42"
  ]
}
```

### city

```json
{
  "kind": "metric",
  "formula": "\"used as a residence\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_NAME = 'Ray and Maria Stata Center'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.30562e19914f41bf5946"
  ]
}
```

### postal code

```json
{
  "kind": "metric",
  "formula": "\"department of facilities\" is predicated by \"TABLE.ORGANIZATION_NAME = 'DP OF FACILITIES'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f85f6bc1556792fe8ccc"
  ]
}
```

### MA

```json
{
  "kind": "metric",
  "formula": "\"academic building\" is predicated by \"TABLE.BUILDING_TYPE = 'ACADEMIC'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.626d62ad454512dae4b6"
  ]
}
```

### street name

```json
{
  "kind": "metric",
  "formula": "\"academic building\" is predicated by \"TABLE.BUILDING_TYPE = 'ACADEMIC'\" | \"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.36dfca299e58e5495f82"
  ]
}
```

### street number

```json
{
  "kind": "metric",
  "formula": "\"residential\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\" | \"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4ef46a1ad56f05d37c2d"
  ]
}
```

### access level code

```json
{
  "kind": "metric",
  "formula": "\"academic building\" is predicated by \"TABLE.BUILDING_TYPE = 'ACADEMIC'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.96fe52264bf1954dc60d"
  ]
}
```

### assignable area

```json
{
  "kind": "metric",
  "formula": "\"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_NAME = 'Ray and Maria Stata Center'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d65fbcb84d5b7192db12"
  ]
}
```

### building name

```json
{
  "kind": "metric",
  "formula": "\"academic building\" is predicated by \"TABLE.BUILDING_TYPE = 'ACADEMIC'\" | \"Ashdown\" is predicated by \"TABLE.BUILDING_NAME = 'ASHDOWN HOUSE'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.572e031e99a60a1681e7"
  ]
}
```

### buildings

```json
{
  "kind": "metric",
  "formula": "\"academic building\" is predicated by \"TABLE.BUILDING_TYPE = 'ACADEMIC'\" | \"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a28282fea46d816f901c"
  ]
}
```

### Stata building

```json
{
  "kind": "metric",
  "formula": "\"residential\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\" | \"owned\" is predicated by \"TABLE.OWNERSHIP_TYPE = 'OWNED'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8bdc37666f09e4b8641b"
  ]
}
```

### academic

```json
{
  "kind": "metric",
  "formula": "\"academic building\" is predicated by \"TABLE.BUILDING_TYPE = 'ACADEMIC'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_NAME = 'Ray and Maria Stata Center'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b8d3c30e61df854b8ed6"
  ]
}
```

### building use type

```json
{
  "kind": "metric",
  "formula": "\"residential\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\" | \"owned\" is predicated by \"TABLE.OWNERSHIP_TYPE = 'OWNED'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.7bd0a5b40c748716277f"
  ]
}
```

### campus sector

```json
{
  "kind": "metric",
  "formula": "\"academic building\" is predicated by \"TABLE.BUILDING_TYPE = 'ACADEMIC'\" | \"residential\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8e584947395c523cc9ca"
  ]
}
```

### historical records

```json
{
  "kind": "metric",
  "formula": "\"Brown\" is predicated by \"TABLE.BUILDING_NAME = 'BROWN BUILDING'\" | \"academic building\" is predicated by \"TABLE.BUILDING_TYPE = 'ACADEMIC'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c5dc32692ec0e4456098"
  ]
}
```

### number of historical records

```json
{
  "kind": "metric",
  "formula": "\"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_NAME = 'Ray and Maria Stata Center'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.1e177c04fea1b33cd085"
  ]
}
```

### rooms

```json
{
  "kind": "metric",
  "formula": "\"residential\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\" | \"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.03832b0fda6091b744d5"
  ]
}
```

### fiscal period

```json
{
  "kind": "metric",
  "formula": "\"used as a residence\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\" | \"Ashdown\" is predicated by \"TABLE.BUILDING_NAME = 'ASHDOWN HOUSE'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8ed3da5ed195495956a8"
  ]
}
```

### historical records

```json
{
  "kind": "metric",
  "formula": "\"academic building\" is predicated by \"TABLE.BUILDING_TYPE = 'ACADEMIC'\" | \"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.cd7e6d78b1db4217655c"
  ]
}
```

### LOW_CAPACITY

```json
{
  "kind": "metric",
  "formula": "\"residential\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\" | \"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.bed34863cd924d0fce7b"
  ]
}
```

### owned

```json
{
  "kind": "metric",
  "formula": "\"residential\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\" | \"owned\" is predicated by \"TABLE.OWNERSHIP_TYPE = 'OWNED'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8731439514c473804e56"
  ]
}
```

### MIT

```json
{
  "kind": "metric",
  "formula": "\"residential\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\" | \"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.959dd00115975cac54d4"
  ]
}
```

### access level of 2

```json
{
  "kind": "metric",
  "formula": "\"academic building\" is predicated by \"TABLE.BUILDING_TYPE = 'ACADEMIC'\" | \"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ca51b1d47d4836aebe2e"
  ]
}
```

### assignable area

```json
{
  "kind": "metric",
  "formula": "\"academic building\" is predicated by \"TABLE.BUILDING_TYPE = 'ACADEMIC'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_NAME = 'Ray and Maria Stata Center'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5a8e811e35e54198acb4"
  ]
}
```

### building

```json
{
  "kind": "metric",
  "formula": "\"academic building\" is predicated by \"TABLE.BUILDING_TYPE = 'ACADEMIC'\" | \"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.65e652515fb36f32aad5"
  ]
}
```

### floors

```json
{
  "kind": "metric",
  "formula": "\"used as a residence\" is predicated by \"TABLE.BUILDING_TYPE = 'RESIDENT'\" | No relevant external evidence for 'residential' or 'used as a residence' in the provided list, so none added.",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e480dc148a2c8943aa59"
  ]
}
```

### floor

```json
{
  "kind": "metric",
  "formula": "\"academic building\" is predicated by \"TABLE.BUILDING_TYPE = 'ACADEMIC'\" | \"buildings at MIT\" is predicated by \"TABLE.SITE = 'MIT'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a9e8109e4ee4171c7519"
  ]
}
```

### floor's sort sequence

```json
{
  "kind": "metric",
  "formula": "\"exclude usage types that include 'STORAGE'\" is predicated by \"TABLE.SPACE_USAGE NOT LIKE '%STORAGE%'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.df04a9df4f3f23c723a3"
  ]
}
```

### total non-assignable area

```json
{
  "kind": "metric",
  "formula": "\"academic building\" is predicated by \"TABLE.BUILDING_TYPE = 'ACADEMIC'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_NAME = 'Ray and Maria Stata Center'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.08c24315fd6acc89babb"
  ]
}
```

### assignable major use

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"assignable major use\", \"minimum area value over each major use group for rooms with area greater than 200 and assignable major use\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.6ab856b86c49df3fe090\", \"physical_identifier\": \"FCLT_MAJOR_USE.ASSIGNABLE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.6ab856b86c49df3fe090"
  ]
}
```

### total rooms

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"total rooms\", \"major use description\", \"major use description (again)\", \"access level window row number\", \"average area for each major use description\", \"major use description (from major use table)\", \"average area for each major use description (rooms with access level 1)\", \"average area for each major use description (for rooms with access level 1)\", \"rooms whose area is greater than the average area for their major use description\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.a06556134afe262f5076\", \"physical_identifier\": \"FCLT_MAJOR_USE.DESCRIPTION\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a06556134afe262f5076"
  ]
}
```

### minimum area per major use

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"minimum area per major use\", \"minimum area value over each major use group\", \"minimum area value over each major use group ordered by major use\", \"deviation of the room's area from the average area for its major use\", \"minimum area value over each major use group for rooms with area greater than 200 and assignable major use\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.50f9925f792180d1745d\", \"physical_identifier\": \"FCLT_MAJOR_USE.FCLT_MAJOR_USE_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.50f9925f792180d1745d"
  ]
}
```

### major use

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"major use\", \"major use name\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.b580c05cddde47194609\", \"physical_identifier\": \"FCLT_MAJOR_USE.MAJOR_USE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b580c05cddde47194609"
  ]
}
```

### assignable

```json
{
  "kind": "metric",
  "formula": "\"admissions\" is predicated by \"TABLE.ORGANIZATION_NAME = 'ADMISSIONS'\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d8d2a0340d6373469281"
  ]
}
```

### description

```json
{
  "kind": "metric",
  "formula": "\"admissions\" is predicated by \"TABLE.ORGANIZATION_NAME = 'ADMISSIONS'\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.1a0bac948e4ab3a752fb"
  ]
}
```

### DLC

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"admissions\" is predicated by \"TABLE.ORGANIZATION_NAME = 'ADMISSIONS'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.30eeac401ab5ee0705c7"
  ]
}
```

### DLC

```json
{
  "kind": "metric",
  "formula": "\"history department\" is predicated by \"LOWER(TABLE.DLC_NAME) = LOWER('History')\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.3dad0adec5f67433e83c"
  ]
}
```

### major organization key

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"admissions\" is predicated by \"TABLE.ORGANIZATION_NAME = 'ADMISSIONS'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.fd5f8605ba48e21b50bc"
  ]
}
```

### rank

```json
{
  "kind": "metric",
  "formula": "\"history department\" is predicated by \"LOWER(TABLE.DLC_NAME) = LOWER('History')\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.74c35bfca671d51518a0"
  ]
}
```

### parent organization name

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"parent organization name\", \"parent organization description\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.62e452cf8368e300d2b4\", \"physical_identifier\": \"FCLT_ORGANIZATION.FCLT_ORG_PARENT_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.62e452cf8368e300d2b4"
  ]
}
```

### department code

```json
{
  "kind": "metric",
  "formula": "\"biology department\" is predicated by \"LOWER(TABLE.DLC_NAME) = LOWER('Biology')\" | \"Departments, Laboratories, and Centers\" are abbreviated by \"DLCs\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5fdb0e9714bd00145e6d"
  ]
}
```

### department

```json
{
  "kind": "metric",
  "formula": "\"biology department\" is predicated by \"LOWER(TABLE.DLC_NAME) = LOWER('Biology')\" | \"Departments, Laboratories, and Centers\" are abbreviated by \"DLCs\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a18afbf5ca2765cb094b"
  ]
}
```

### HR org units

```json
{
  "kind": "metric",
  "formula": "\"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\" | \"admissions\" is predicated by \"TABLE.ORGANIZATION_NAME = 'ADMISSIONS'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0866d4859824235eb5ec"
  ]
}
```

### name

```json
{
  "kind": "metric",
  "formula": "\"admissions\" is predicated by \"TABLE.ORGANIZATION_NAME = 'ADMISSIONS'\" | \"Departments, Laboratories, and Centers\" are abbreviated by \"DLCs\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.02a09e433e6dff039bb6"
  ]
}
```

### organization

```json
{
  "kind": "metric",
  "formula": "\"except Cambridge-MIT Institute\" is predicated by \"TABLE.ORGANIZATION_NAME NOT IN ('CAMBRIDGE-MIT INST')\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0e3aad987eab998b1177"
  ]
}
```

### organization

```json
{
  "kind": "metric",
  "formula": "\"admissions\" is predicated by \"TABLE.ORGANIZATION_NAME = 'ADMISSIONS'\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.651c06997e825886d2be"
  ]
}
```

### average

```json
{
  "kind": "metric",
  "formula": "\"biology department\" is predicated by \"LOWER(TABLE.DLC_NAME) = LOWER('Biology')\" | \"Departments, Laboratories, and Centers\" are abbreviated by \"DLCs\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e8a0354614cca1db1c62"
  ]
}
```

### ADMISSIONS

```json
{
  "kind": "metric",
  "formula": "\"admissions\" is predicated by \"TABLE.ORGANIZATION_NAME = 'ADMISSIONS'\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e8a9bf1aa590678cb294"
  ]
}
```

### average

```json
{
  "kind": "metric",
  "formula": "\"history department\" is predicated by \"LOWER(TABLE.DLC_NAME) = LOWER('History')\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.478698bf7a4fa48891f1"
  ]
}
```

### organization sort

```json
{
  "kind": "metric",
  "formula": "\"biology department\" is predicated by \"LOWER(TABLE.DLC_NAME) = LOWER('Biology')\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.6b8ea14dee85cc309d69"
  ]
}
```

### CHNCLR

```json
{
  "kind": "metric",
  "formula": "\"except Cambridge-MIT Institute\" is predicated by \"TABLE.ORGANIZATION_NAME NOT IN ('CAMBRIDGE-MIT INST')\" | \"Cambridge-MIT Institute\" is abbreviated as \"CAMBRIDGE-MIT INST\" in organization names",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.7169a5ba2e71d03af5df"
  ]
}
```

### earliest warehouse load date

```json
{
  "kind": "metric",
  "formula": "\"biology department\" is predicated by \"LOWER(TABLE.DLC_NAME) = LOWER('Biology')\" | \"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.3e06926505ece322ebf2"
  ]
}
```

### DLC

```json
{
  "kind": "metric",
  "formula": "\"history department\" is predicated by \"LOWER(TABLE.DLC_NAME) = LOWER('History')\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.3a3092e101b1bfa49c9b"
  ]
}
```

### organization

```json
{
  "kind": "metric",
  "formula": "\"admissions\" is predicated by \"TABLE.ORGANIZATION_NAME = 'ADMISSIONS'\" | \"Departments, Laboratories, and Centers\" are abbreviated by \"DLCs\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8209209c7ebcc5c5c46a"
  ]
}
```

### access level

```json
{
  "kind": "metric",
  "formula": "\"department of facilities\" is predicated by \"TABLE.ORGANIZATION_NAME = 'DP OF FACILITIES'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.388788aa3b18b455e5b7"
  ]
}
```

### area

```json
{
  "kind": "metric",
  "formula": "\"department of facilities\" is predicated by \"TABLE.ORGANIZATION_NAME = 'DP OF FACILITIES'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b6ad24166a17edee00bb"
  ]
}
```

### room

```json
{
  "kind": "metric",
  "formula": "\"Computer Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_NAME = 'Ray and Maria Stata Center'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.3fbff4a48989bc86bcfd"
  ]
}
```

### department code

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"department code\", \"average area in a window\", \"non-null department code\", \"department code of the room\", \"average area of rooms in their department\", \"rooms assigned to organization and department code\", \"rooms assigned to that organization and department code\", \"average area in a window of 2 preceding and 2 following rows grouped by department code and ordered by area\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.80550bf14468af96ff3b\", \"physical_identifier\": \"FCLT_ROOMS.DEPT_CODE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.80550bf14468af96ff3b"
  ]
}
```

### rooms

```json
{
  "kind": "metric",
  "formula": "\"department of facilities\" is predicated by \"TABLE.ORGANIZATION_NAME = 'DP OF FACILITIES'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ac2553ec4010342915fa"
  ]
}
```

### rooms

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"rooms\", \"floor key\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.3a48b610b9a7aa1e31b4\", \"physical_identifier\": \"FCLT_ROOMS.FCLT_FLOOR_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.3a48b610b9a7aa1e31b4"
  ]
}
```

### minimum area per major use

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"minimum area per major use\", \"minimum area value over each major use group\", \"minimum area value over each major use group for rooms with area greater than 200 and assignable major use\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.f65a282c044a9a81ae9d\", \"physical_identifier\": \"FCLT_ROOMS.FCLT_MAJOR_USE_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f65a282c044a9a81ae9d"
  ]
}
```

### rooms

```json
{
  "kind": "metric",
  "formula": "\"admissions\" is predicated by \"TABLE.ORGANIZATION_NAME = 'ADMISSIONS'\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0c4277e5eaffe4d965cc"
  ]
}
```

### room

```json
{
  "kind": "metric",
  "formula": "\"department of facilities\" is predicated by \"TABLE.ORGANIZATION_NAME = 'DP OF FACILITIES'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b6628a2f1d5f632d0384"
  ]
}
```

### room

```json
{
  "kind": "metric",
  "formula": "\"exclude usage types that include 'STORAGE'\" is predicated by \"TABLE.SPACE_USAGE NOT LIKE '%STORAGE%'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.88ccb8d0456c7ccd43d0"
  ]
}
```

### major use

```json
{
  "kind": "metric",
  "formula": "\"exclude usage types that include 'STORAGE'\" is predicated by \"TABLE.SPACE_USAGE NOT LIKE '%STORAGE%'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4bcfbf193a7801432bb2"
  ]
}
```

### organization

```json
{
  "kind": "metric",
  "formula": "\"department of facilities\" is predicated by \"TABLE.ORGANIZATION_NAME = 'DP OF FACILITIES'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.7303b199f2428ee309ea"
  ]
}
```

### room

```json
{
  "kind": "metric",
  "formula": "\"department of facilities\" is predicated by \"TABLE.ORGANIZATION_NAME = 'DP OF FACILITIES'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f087f52bc0225bf7227d"
  ]
}
```

### room's full name

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"room's full name\", \"total number of rooms in that building assigned to the organization with area greater than 300\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.be2cf7ce73b495b1feaf\", \"physical_identifier\": \"FCLT_ROOMS.ROOM_FULL_NAME\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.be2cf7ce73b495b1feaf"
  ]
}
```

### room

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"room\", \"rooms\", \"space ID\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.6df0b61cda626fcf79d1\", \"physical_identifier\": \"FCLT_ROOMS.SPACE_ID\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.6df0b61cda626fcf79d1"
  ]
}
```

### range

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"range\", \"DLC key\", \"DLC_KEY\", \"variance\", \"departments\", \"HR org units\", \"non-null DLC key\", \"standard deviation\", \"count of HR org units\", \"HR organization unit table\", \"HR org units linked to that space unit\", \"range of the number of HR organization units\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.010255fbc64c63d88b68\", \"physical_identifier\": \"HR_ORG_UNIT.DLC_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.010255fbc64c63d88b68"
  ]
}
```

### DLC name

```json
{
  "kind": "metric",
  "formula": "\"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\" | \"biology department\" is predicated by \"LOWER(TABLE.DLC_NAME) = LOWER('Biology')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d9bfa6e5ae5840808581"
  ]
}
```

### Course 17

```json
{
  "kind": "metric",
  "formula": "\"except Cambridge-MIT Institute\" is predicated by \"TABLE.ORGANIZATION_NAME NOT IN ('CAMBRIDGE-MIT INST')\" | \"Course 17\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.25a651790061bea4bb37"
  ]
}
```

### HR org units

```json
{
  "kind": "metric",
  "formula": "\"admissions\" is predicated by \"TABLE.ORGANIZATION_NAME = 'ADMISSIONS'\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.74f5160903c48af557d3"
  ]
}
```

### HR org units

```json
{
  "kind": "metric",
  "formula": "\"except Cambridge-MIT Institute\" is predicated by \"TABLE.ORGANIZATION_NAME NOT IN ('CAMBRIDGE-MIT INST')\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ef0f84f58bbeefe8e7ce"
  ]
}
```

### AVERAGE

```json
{
  "kind": "metric",
  "formula": "\"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\" | \"except Cambridge-MIT Institute\" is predicated by \"TABLE.ORGANIZATION_NAME NOT IN ('CAMBRIDGE-MIT INST')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8583a0e313255bdad6f2"
  ]
}
```

### dense rank

```json
{
  "kind": "metric",
  "formula": "\"except Cambridge-MIT Institute\" is predicated by \"TABLE.ORGANIZATION_NAME NOT IN ('CAMBRIDGE-MIT INST')\" | \"Course 17\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0f3293c483ed12b59791"
  ]
}
```

### average

```json
{
  "kind": "metric",
  "formula": "\"admissions\" is predicated by \"TABLE.ORGANIZATION_NAME = 'ADMISSIONS'\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8512b9d36b56213324f0"
  ]
}
```

### HR org units

```json
{
  "kind": "metric",
  "formula": "\"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\" | \"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.6f5657a0d01e7230febb"
  ]
}
```

### department level

```json
{
  "kind": "metric",
  "formula": "\"except Cambridge-MIT Institute\" is predicated by \"TABLE.ORGANIZATION_NAME NOT IN ('CAMBRIDGE-MIT INST')\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.514c809bb399dd48400c"
  ]
}
```

### HR org unit title

```json
{
  "kind": "metric",
  "formula": "\"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\" | \"except Cambridge-MIT Institute\" is predicated by \"TABLE.ORGANIZATION_NAME NOT IN ('CAMBRIDGE-MIT INST')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c641897ed00f6dc4a72d"
  ]
}
```

### school area

```json
{
  "kind": "metric",
  "formula": "\"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\" | \"Course 17\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b51919e571a694940128"
  ]
}
```

### Provost Area

```json
{
  "kind": "metric",
  "formula": "\"except Cambridge-MIT Institute\" is predicated by \"TABLE.ORGANIZATION_NAME NOT IN ('CAMBRIDGE-MIT INST')\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.9d9c8be9fd18e8c185ea"
  ]
}
```

### HR org units

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"HR org units\", \"latest warehouse load date\", \"most recent warehouse load date\", \"warehouse load date '03-DEC-24'\", \"warehouse load date (HR org unit)\", \"warehouse load date of '03-DEC-24'\", \"latest warehouse load date from HR_ORG_UNIT\", \"HR org unit warehouse load date of '03-DEC-24'\", \"HR org units warehouse load date of '03-DEC-24'\", \"HR org units with a warehouse load date of '03-DEC-24'\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.605457924d087e0a5430\", \"physical_identifier\": \"HR_ORG_UNIT.WAREHOUSE_LOAD_DATE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.605457924d087e0a5430"
  ]
}
```

### category description

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"category description\", \"description of the subject category\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.74d13e3d31046a5ce4a1\", \"physical_identifier\": \"IAP_SUBJECT_CATEGORY.IAP_CATEGORY_DESC\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.74d13e3d31046a5ce4a1"
  ]
}
```

### category

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"category\", \"dense rank\", \"Mathematics\", \"IAP category\", \"category name\", \"grand total row\", \"subject category\", \"total activities\", \"activity category\", \"Mathematics category\", \"subject category name\", \"activity's category name\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.5438f2b23fe247478aa4\", \"physical_identifier\": \"IAP_SUBJECT_CATEGORY.IAP_CATEGORY_NAME\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5438f2b23fe247478aa4"
  ]
}
```

### subject category

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"subject category\", \"subject category key\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.f8b9ee7264d311c0c1c5\", \"physical_identifier\": \"IAP_SUBJECT_CATEGORY.IAP_SUBJECT_CATEGORY_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f8b9ee7264d311c0c1c5"
  ]
}
```

### IAP subjects

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"IAP subjects\", \"activity description\", \"length of the activity description\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.d6a366f067fb7210734c\", \"physical_identifier\": \"IAP_SUBJECT_DETAIL.ACTIVITY_DESCRIPTION\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d6a366f067fb7210734c"
  ]
}
```

### title

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c0b73d979bc7486ccab3"
  ]
}
```

### create date

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"create date\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.027ddf4730da52386a19\", \"physical_identifier\": \"IAP_SUBJECT_DETAIL.CREATE_DATE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.027ddf4730da52386a19"
  ]
}
```

### IAP subjects

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.666f01522a0163fca8b0"
  ]
}
```

### fee

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"fee\", \"average fee\", \"minimum fee\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.b0b9c0b77ec2b9ce327b\", \"physical_identifier\": \"IAP_SUBJECT_DETAIL.FEE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b0b9c0b77ec2b9ce327b"
  ]
}
```

### activities

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"activities\", \"IAP subjects\", \"subject category\", \"subject categories\", \"IAP subject category\", \"subject category key\", \"IAP subject activities\", \"mathematics activity ratio\", \"total number of activities\", \"number of activities in that category\", \"number of activities in the \\\"Mathematics\\\" category\", \"average maximum enrollment for activities in the same category\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.10452ade9efcd714b116\", \"physical_identifier\": \"IAP_SUBJECT_DETAIL.IAP_SUBJECT_CATEGORY_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.10452ade9efcd714b116"
  ]
}
```

### activities led

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"activities led\", \"activities they lead\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.f544dfab7b64225638c1\", \"physical_identifier\": \"IAP_SUBJECT_DETAIL.IAP_SUBJECT_PERSON_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f544dfab7b64225638c1"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"subjects\", \"subject count\", \"IAP activities\", \"unique subjects\", \"number of activities\", \"IAP activity session key\", \"number of unique subjects\", \"number of unique activities\", \"normalized subjects per year\", \"number of activities in that category\", \"unique subjects in the subject category\", \"total number of such activities for the department\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.37f1de23f35167792a8d\", \"physical_identifier\": \"IAP_SUBJECT_DETAIL.IAP_SUBJECT_SESSION_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.37f1de23f35167792a8d"
  ]
}
```

### sponsor

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"sponsor\", \"activities\", \"sponsor key\", \"IAP activities\", \"IAP subject sponsor key\", \"total number of activities for each sponsor\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.23d499b098d1eb6f476a\", \"physical_identifier\": \"IAP_SUBJECT_DETAIL.IAP_SUBJECT_SPONSOR_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.23d499b098d1eb6f476a"
  ]
}
```

### cancelled

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2a49ddc067b4034fb501"
  ]
}
```

### multiple sessions

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"multiple sessions\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.6aceb91d616583341722\", \"physical_identifier\": \"IAP_SUBJECT_DETAIL.IS_MULTIPLE_SESSION\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.6aceb91d616583341722"
  ]
}
```

### 12

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.32b948de4eeab74c7d3b"
  ]
}
```

### earliest preregistration deadline

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"earliest preregistration deadline\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.4e1125a7f20ea71cfac3\", \"physical_identifier\": \"IAP_SUBJECT_DETAIL.PREREG_DEADLINE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4e1125a7f20ea71cfac3"
  ]
}
```

### prerequisites

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"prerequisites\", \"IAP subject activity\", \"IAP subject activities\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.dfa9b4ff7b891637e4f6\", \"physical_identifier\": \"IAP_SUBJECT_DETAIL.PREREQUISITES\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.dfa9b4ff7b891637e4f6"
  ]
}
```

### IAP

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.faf02e0c2807a4a24888"
  ]
}
```

### activities

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"activities\", \"activities led\", \"activities they lead\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.987773561ba23ec2c6fc\", \"physical_identifier\": \"IAP_SUBJECT_PERSON.IAP_SUBJECT_PERSON_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.987773561ba23ec2c6fc"
  ]
}
```

### person role

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"person role\", \"person role name\", \"total number of such activities for each role\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.7886786fa1e8bdd9c9f2\", \"physical_identifier\": \"IAP_SUBJECT_PERSON.PERSON_ROLE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.7886786fa1e8bdd9c9f2"
  ]
}
```

### session date

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"session date\", \"session dates\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.653de645e6496915fa43\", \"physical_identifier\": \"IAP_SUBJECT_SESSION.SESSION_DATE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.653de645e6496915fa43"
  ]
}
```

### session end time

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"session end time\", \"session end times\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.8371ebb3261ccb2212f0\", \"physical_identifier\": \"IAP_SUBJECT_SESSION.SESSION_END_TIME\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8371ebb3261ccb2212f0"
  ]
}
```

### session location

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"session location\", \"session locations\", \"session location ordering\", \"ordered by session location\", \"minimum session start time per session location\", \"minimum session start time over each session location group\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.c29cbb8b3861b5dadbd6\", \"physical_identifier\": \"IAP_SUBJECT_SESSION.SESSION_LOCATION\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c29cbb8b3861b5dadbd6"
  ]
}
```

### session start time

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"session start time\", \"session start times\", \"minimum session start time per session location\", \"minimum session start time over each session location group\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.e7deadfea905e7f7b30f\", \"physical_identifier\": \"IAP_SUBJECT_SESSION.SESSION_START_TIME\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e7deadfea905e7f7b30f"
  ]
}
```

### session title

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"session title\", \"session titles\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.ffe54046dc945ccf164c\", \"physical_identifier\": \"IAP_SUBJECT_SESSION.SESSION_TITLE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ffe54046dc945ccf164c"
  ]
}
```

### IAP activities

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"IAP activities\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.c469d6dae83a24c202f4\", \"physical_identifier\": \"IAP_SUBJECT_SPONSOR.IAP_SUBJECT_SPONSOR_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c469d6dae83a24c202f4"
  ]
}
```

### sponsor

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"sponsor\", \"sponsor name\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.9fd54f3d710fb9d5ef1a\", \"physical_identifier\": \"IAP_SUBJECT_SPONSOR.SPONSOR_NAME\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.9fd54f3d710fb9d5ef1a"
  ]
}
```

### sponsor

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"sponsor\", \"sponsor type\", \"sponsor type name\", \"number of unique sponsor types\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.8c94a2d251471034d005\", \"physical_identifier\": \"IAP_SUBJECT_SPONSOR.SPONSOR_TYPE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8c94a2d251471034d005"
  ]
}
```

### courses

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"courses\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.5c17568b51719b36f65b\", \"physical_identifier\": \"LIBRARY_COURSE_INSTRUCTOR.COURSE_NAME\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5c17568b51719b36f65b"
  ]
}
```

### department

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"department\", \"departments\", \"department name\", \"18 - Mathematics\", \"department's name\", \"Mathematics department\", \"name of the department\", \"courses in that department\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.cf31d0d8dc596bf40ee9\", \"physical_identifier\": \"LIBRARY_COURSE_INSTRUCTOR.DEPARTMENT\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.cf31d0d8dc596bf40ee9"
  ]
}
```

### Hayden unit

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"Hayden unit\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.f46ab31c6f8e4d4c7d18\", \"physical_identifier\": \"LIBRARY_COURSE_INSTRUCTOR.UNIT\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f46ab31c6f8e4d4c7d18"
  ]
}
```

### library material status

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"library material status\", \"library material statuses\", \"associated library material status\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.b0aabbfad3ec3c3e600c\", \"physical_identifier\": \"LIBRARY_MATERIAL_STATUS.LIBRARY_MATERIAL_STATUS\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b0aabbfad3ec3c3e600c"
  ]
}
```

### catalog author name

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"catalog author name\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.8d5765c4ad543bb40499\", \"physical_identifier\": \"LIBRARY_RESERVE_CATALOG.CATALOG_AUTHOR_NAME\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8d5765c4ad543bb40499"
  ]
}
```

### catalog title

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"catalog title\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.d28fd0457bccdb9a8c90\", \"physical_identifier\": \"LIBRARY_RESERVE_CATALOG.CATALOG_TITLE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d28fd0457bccdb9a8c90"
  ]
}
```

### catalog year

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"catalog year\", \"catalog year after 2000\", \"catalog year greater than 2000\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.d67924e04f76fb17dfe9\", \"physical_identifier\": \"LIBRARY_RESERVE_CATALOG.CATALOG_YEAR\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d67924e04f76fb17dfe9"
  ]
}
```

### reserve catalog items

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"reserve catalog items\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.48239d5af82284a30664\", \"physical_identifier\": \"LIBRARY_RESERVE_CATALOG.LIBRARY_RESERVE_CATALOG_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.48239d5af82284a30664"
  ]
}
```

### average record counter

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"average record counter\", \"minimum record counter\", \"record counter variance\", \"average of the record counter\", \"variance of the record counter\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.665f32047628f0d513de\", \"physical_identifier\": \"LIBRARY_RESERVE_CATALOG.RECORD_COUNTER\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.665f32047628f0d513de"
  ]
}
```

### instructor key

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"instructor key\", \"unique instructors\", \"course instructor key\", \"library course instructor\", \"number of unique instructors\", \"library course instructor key\", \"library reserve material detail\", \"library reserve material details\", \"ordered by course instructor key\", \"instructors who have assigned reserve materials\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.4711deb04ad8b5bad455\", \"physical_identifier\": \"LIBRARY_RESERVE_MATRL_DETAIL.LIBRARY_COURSE_INSTRUCTOR_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4711deb04ad8b5bad455"
  ]
}
```

### U

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5775c9a6713c94170542"
  ]
}
```

### AVERAGE

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.89e3b42cfea658851a09"
  ]
}
```

### reserved material

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"reserved material\", \"subject offered key\", \"unique subjects offered\", \"library subject offered key\", \"reserve subject offered key\", \"reserved materials per subject\", \"library reserve material detail\", \"library reserve material details\", \"number of reserved materials per subject\", \"number of library reserve material details\", \"range of the number of reserved materials per subject\", \"number of library reserve material details per subject\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.776aa0545569c91a65a8\", \"physical_identifier\": \"LIBRARY_RESERVE_MATRL_DETAIL.LIBRARY_SUBJECT_OFFERED_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.776aa0545569c91a65a8"
  ]
}
```

### subject

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.cdeb09845a7e47cf2c09"
  ]
}
```

### term

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c27e2c70682b695aee7c"
  ]
}
```

### warehouse load date

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"warehouse load date\", \"most recent warehouse load date from library reserve\", \"most recent warehouse load date from the library reserve table\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.ee02d4ba9136633be46e\", \"physical_identifier\": \"LIBRARY_RESERVE_MATRL_DETAIL.WAREHOUSE_LOAD_DATE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ee02d4ba9136633be46e"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"degree-granting courses\" is predicated by \"TABLE.IS_DEGREE_GRANTING = 'Y'\" | \"Chemistry\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.710b63c60b33c7401ba6"
  ]
}
```

### subject

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"subject\", \"course number description\", \"course number descriptions\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.23b8dfa8e85ce5688e2a\", \"physical_identifier\": \"LIBRARY_SUBJECT_OFFERED.COURSE_NUMBER_DESC\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.23b8dfa8e85ce5688e2a"
  ]
}
```

### courses

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.9d70fd5691c127f6830d"
  ]
}
```

### library subjects

```json
{
  "kind": "metric",
  "formula": "\"biology and chemistry department\" is predicated by \"TABLE.OFFER_DEPT_NAME IN ('Chemistry', 'Biology')\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f4310467d2dac429208c"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.83de996f5740279a4f95"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.990db77f8064f341b481"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.7c1bf9e2317ada8bd141"
  ]
}
```

### Chemistry

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b6d80ad5cceeb2ce495b"
  ]
}
```

### school

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.14ae2d375144ce0de271"
  ]
}
```

### responsible faculty MIT ID

```json
{
  "kind": "metric",
  "formula": "\"biology and chemistry department\" is predicated by \"TABLE.OFFER_DEPT_NAME IN ('Chemistry', 'Biology')\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.63b4e12de44934121f94"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f42cefe288fafc8a6e5b"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b67cfa65ab831c9fd116"
  ]
}
```

### title

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d3f1805a908be0ea44f4"
  ]
}
```

### IAP

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8e335412aea0460740ce"
  ]
}
```

### department

```json
{
  "kind": "metric",
  "formula": "\"biology department\" is predicated by \"LOWER(TABLE.DLC_NAME) = LOWER('Biology')\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.63a0a415074febadabd2"
  ]
}
```

### DLC key

```json
{
  "kind": "metric",
  "formula": "\"except organizations '101' and '103'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('101', '103')\" | \"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.9cd259836a00d9638c60"
  ]
}
```

### Biology

```json
{
  "kind": "metric",
  "formula": "\"biology department\" is predicated by \"LOWER(TABLE.DLC_NAME) = LOWER('Biology')\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.6b15d2040d5614478274"
  ]
}
```

### hierarchy type

```json
{
  "kind": "metric",
  "formula": "\"except Cambridge-MIT Institute\" is predicated by \"TABLE.ORGANIZATION_NAME NOT IN ('CAMBRIDGE-MIT INST')\" | \"Course 17\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.fb74307949b4df2ae0a3"
  ]
}
```

### departments

```json
{
  "kind": "metric",
  "formula": "\"admissions\" is predicated by \"TABLE.ORGANIZATION_NAME = 'ADMISSIONS'\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c7ad6bff0266464548d8"
  ]
}
```

### department hierarchy level 3 code

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"department hierarchy level 3 code\", \"maximum department hierarchy level 3 code\", \"minimum department hierarchy level 3 code\", \"maximum department hierarchy level 3 codes\", \"minimum department hierarchy level 3 codes\", \"unique DLC codes at the third hierarchy level\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.f38055247c5c89219245\", \"physical_identifier\": \"MASTER_DEPT_HIERARCHY.MASTER_DEPT_HIER_LEVEL_3_CODE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f38055247c5c89219245"
  ]
}
```

### department

```json
{
  "kind": "metric",
  "formula": "\"except Cambridge-MIT Institute\" is predicated by \"TABLE.ORGANIZATION_NAME NOT IN ('CAMBRIDGE-MIT INST')\" | \"Departments, Laboratories, and Centers\" are abbreviated by \"DLCs\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.86e799dc342160a103af"
  ]
}
```

### '6'

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Political Science\" is predicated by \"TABLE.DEPARTMENT_CODE = '17'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8f2e51ab4a983f120feb"
  ]
}
```

### student

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.531eccaf2dded11867ec"
  ]
}
```

### student

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Political Science\" is predicated by \"TABLE.DEPARTMENT_CODE = '17'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c59956ff44059e7b6dcd"
  ]
}
```

### AVERAGE

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Zoe\" is predicated by \"TABLE.FIRST_NAME = 'Zoe'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b9c4098ffc6b82bf2ff2"
  ]
}
```

### AVERAGE

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.21549b9ac0ab548178bb"
  ]
}
```

### student

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Computer Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.35bfe2a5af0c971ad21c"
  ]
}
```

### office location

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_CODE = '18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0dd0d5450be79985b1f7"
  ]
}
```

### students

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4c85e02e2ffc9775a4f9"
  ]
}
```

### G

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.13ef8b65bdd3fb0edf40"
  ]
}
```

### warehouse load date

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_CODE = '18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.cc8d48df4b61dc0319b9"
  ]
}
```

### active Moira lists

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"active Moira lists\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.6b6978e82125065d2b42\", \"physical_identifier\": \"MOIRA_LIST.IS_ACTIVE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.6b6978e82125065d2b42"
  ]
}
```

### Moira mailing list

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"Moira mailing list\", \"Moira mailing lists\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.a0c8cb2c90865a8ae774\", \"physical_identifier\": \"MOIRA_LIST.IS_MOIRA_MAILING_LIST\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a0c8cb2c90865a8ae774"
  ]
}
```

### public

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"public\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.05abe4e3f43a976e326d\", \"physical_identifier\": \"MOIRA_LIST.IS_PUBLIC\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.05abe4e3f43a976e326d"
  ]
}
```

### list key

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"list key\", \"sort by list key\", \"subtotals for each list key\", \"grand total across all lists\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.9a9f03e39141fcfe7659\", \"physical_identifier\": \"MOIRA_LIST.MOIRA_LIST_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.9a9f03e39141fcfe7659"
  ]
}
```

### list name

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"list name\", \"Moira list name\", \"sort by list name\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.3b95cc51f9749c45e3f8\", \"physical_identifier\": \"MOIRA_LIST.MOIRA_LIST_NAME\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.3b95cc51f9749c45e3f8"
  ]
}
```

### last update date

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Course 17\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.141455dbbda21b76c3e5"
  ]
}
```

### Moira list key

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"Moira list key\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.35f9622174334e7bcba8\", \"physical_identifier\": \"MOIRA_LIST_DETAIL.MOIRA_LIST_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.35f9622174334e7bcba8"
  ]
}
```

### members

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_CODE = '18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.755bf7de9feae1c128e2"
  ]
}
```

### Moira list member

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"Moira list member\", \"member's full name\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.a51e2c3a543544fe694a\", \"physical_identifier\": \"MOIRA_LIST_DETAIL.MOIRA_LIST_MEMBER_FULL_NAME\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a51e2c3a543544fe694a"
  ]
}
```

### Moira list

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.47687bc819fd4d709166"
  ]
}
```

### list owner

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"list owner\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.e0b59d862f2392ec2490\", \"physical_identifier\": \"MOIRA_LIST_OWNER.OWNER\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e0b59d862f2392ec2490"
  ]
}
```

### owner's type

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"owner's type\", \"average MIT ID for their owner type\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.18a2311231af5a5618ae\", \"physical_identifier\": \"MOIRA_LIST_OWNER.OWNER_TYPE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.18a2311231af5a5618ae"
  ]
}
```

### Student

```json
{
  "kind": "metric",
  "formula": "\"student\" is predicated by \"TABLE.EMPLOYEE_TYPE = 'Student'\" | \"Course 6\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.76b192429ac0e6bb0bd5"
  ]
}
```

### student

```json
{
  "kind": "metric",
  "formula": "\"student\" is predicated by \"TABLE.EMPLOYEE_TYPE = 'Student'\" | \"Course 6\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.1841d9535e1ad436132b"
  ]
}
```

### active graduate student

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"active graduate student\", \"active graduate students\", \"total number of active graduate students\", \"highest number of active graduate students\", \"total number of active graduate students with an office location assigned\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.0f706cd0fd0e5fe2ac52\", \"physical_identifier\": \"SE_PERSON.IS_ACTIVE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0f706cd0fd0e5fe2ac52"
  ]
}
```

### MIT ID

```json
{
  "kind": "metric",
  "formula": "\"student\" is predicated by \"TABLE.EMPLOYEE_TYPE = 'Student'\" | \"Course 6\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.03b46c0055ef67072627"
  ]
}
```

### office locations

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"office locations\", \"unique office locations\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.144ec82fb204fd6d928a\", \"physical_identifier\": \"SE_PERSON.OFFICE_LOCATION\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.144ec82fb204fd6d928a"
  ]
}
```

### Electrical Engineering and Computer Science department

```json
{
  "kind": "metric",
  "formula": "\"Electrical Engineering and Computer Science department\" is predicated by \"TABLE.ORGANIZATION = 'Electrical Engineering-Computer Science'\" | \"Electrical Engineering and Computer Science\" is predicated by \"TABLE.DEPARTMENT = '6'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.70160b0f5bab21c1791d"
  ]
}
```

### range

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4af4407312f94818d747"
  ]
}
```

### phone number

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.72af9efafe9e65ee79a7"
  ]
}
```

### most recent activity date

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.9e1135ba57ad176b636a"
  ]
}
```

### Course 2

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Mathematics\" is predicated by \"TABLE.DEPARTMENT_CODE = '18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.67e36f6304084661a136"
  ]
}
```

### Course 2

```json
{
  "kind": "metric",
  "formula": "\"Mechanical Engineering\" is predicated by \"UPPER(TABLE.SIS_ADMIN_DEPARTMENT_NAME) = 'MECHANICAL ENGINEERING'\" | \"Course 2\" is predicated by \"UPPER(TABLE.SIS_ADMIN_DEPARTMENT_NAME) = 'MECHANICAL ENGINEERING'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.bc4d75c22f94063af5c5"
  ]
}
```

### courses

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5bcd37512ae6e07d724e"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"courses with materials\" is predicated by \"TIP_SUBJECT_OFFERED.IS_NO_COURSE_MATERIAL = 'N'\" | \"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f769b2cdec5f9c4247b0"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.51575ed139a085eb05ea"
  ]
}
```

### course description

```json
{
  "kind": "metric",
  "formula": "\"degree-granting\" is predicated by \"TABLE.IS_DEGREE_GRANTING = 'Y'\" | \"Course 6\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.814599d487285b15f533"
  ]
}
```

### courses

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.984b23d28ca7882b129c"
  ]
}
```

### course option

```json
{
  "kind": "metric",
  "formula": "\"Computer Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\" | \"Course 6\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2bb18ccf1ffeffa3f001"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT = '18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.280edbdeec7889ba18be"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT = '18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d81ffc8c2ac2687a1e30"
  ]
}
```

### term code

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Mathematics\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f821cb690eded14c9b5a"
  ]
}
```

### term description

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Mathematics\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.fd929e268109e6ce9ad3"
  ]
}
```

### graduate level

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2be74949056f3f50ba41"
  ]
}
```

### courses

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT = '18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5fb1374cfe56d8fdf29c"
  ]
}
```

### last activity date

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"last activity date\", \"most recently added\", \"most recently added course\", \"most recently updated course\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.456532b7f4c77d52be6d\", \"physical_identifier\": \"SIS_COURSE_DESCRIPTION.LAST_ACTIVITY_DATE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.456532b7f4c77d52be6d"
  ]
}
```

### school

```json
{
  "kind": "metric",
  "formula": "\"degree-granting\" is predicated by \"TABLE.IS_DEGREE_GRANTING = 'Y'\" | \"Course 6\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.86347fa8085cac8b0acb"
  ]
}
```

### course key

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Political Science\" is predicated by \"TABLE.DEPARTMENT_CODE = '17'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5287877c2c5be84b67e7"
  ]
}
```

### 18

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Political Science\" is predicated by \"TABLE.DEPARTMENT = '17'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.cf28c63c883c49a4a833"
  ]
}
```

### full name

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5118bbc08f95bfb05b56"
  ]
}
```

### department last activity date

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5758d27b44439d6068ab"
  ]
}
```

### AVERAGE

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.534d8e82adf5747b24ab"
  ]
}
```

### range

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Political Science\" is predicated by \"TABLE.DEPARTMENT = '17'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f8d49ede8b43687c5cee"
  ]
}
```

### department

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.28ac64344af0374b130d"
  ]
}
```

### DLC key

```json
{
  "kind": "metric",
  "formula": "\"Mechanical Engineering\" is predicated by \"UPPER(TABLE.SIS_ADMIN_DEPARTMENT_NAME) = 'MECHANICAL ENGINEERING'\" | \"admissions\" is predicated by \"TABLE.ORGANIZATION_NAME = 'ADMISSIONS'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.cc504bca522316127859"
  ]
}
```

### department

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Course 17\" is predicated by \"TABLE.DEPARTMENT_CODE = '17'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.dcab21a51f4a713c12ff"
  ]
}
```

### school

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.317f4c1c4825bfd068f6"
  ]
}
```

### name

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Political Science\" is predicated by \"TABLE.DEPARTMENT = '17'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.222b6dec9dfa7c8a48b7"
  ]
}
```

### school

```json
{
  "kind": "metric",
  "formula": "\"degree-granting\" is predicated by \"TABLE.IS_DEGREE_GRANTING = 'Y'\" | \"Mathematics\" is predicated by \"TABLE.DEPARTMENT_CODE = '18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0506cc902d9fecd551df"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a78381cbf0592527f416"
  ]
}
```

### school

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Political Science\" is predicated by \"TABLE.DEPARTMENT_CODE = '17'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d09ccfc8d6a0d9125742"
  ]
}
```

### Biology

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.72f236ae8fae4fdcb646"
  ]
}
```

### school

```json
{
  "kind": "metric",
  "formula": "\"biology and chemistry department\" is predicated by \"TABLE.OFFER_DEPT_NAME IN ('Chemistry', 'Biology')\" | \"Chemistry\" is predicated by \"TABLE.DEPARTMENT = '5'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e5555a44925957a33d61"
  ]
}
```

### school

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b17bdf25a3bcfca2ed5f"
  ]
}
```

### subject

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Political Science\" is predicated by \"TABLE.DEPARTMENT = '17'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.33f0ddc82237a15a9086"
  ]
}
```

### subject

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e470ff80b1a403f39436"
  ]
}
```

### building component

```json
{
  "kind": "metric",
  "formula": "\"Stata building\" is predicated by \"TABLE.BUILDING_NAME = 'Ray and Maria Stata Center'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2403050e2fc2dcb31442"
  ]
}
```

### building 32

```json
{
  "kind": "metric",
  "formula": "\"exclude usage types that include 'STORAGE'\" is predicated by \"TABLE.SPACE_USAGE NOT LIKE '%STORAGE%'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.279979e9716b2368b5e0"
  ]
}
```

### rooms

```json
{
  "kind": "metric",
  "formula": "\"exclude usage types that include 'STORAGE'\" is predicated by \"TABLE.SPACE_USAGE NOT LIKE '%STORAGE%'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2de187e481eee9bb7475"
  ]
}
```

### room name

```json
{
  "kind": "metric",
  "formula": "\"Stata building\" is predicated by \"TABLE.BUILDING_NAME = 'Ray and Maria Stata Center'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.bf4710a950097db3b645"
  ]
}
```

### floor

```json
{
  "kind": "metric",
  "formula": "\"Stata building\" is predicated by \"TABLE.BUILDING_NAME = 'Ray and Maria Stata Center'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2dafb11ca1c4c2b52987"
  ]
}
```

### space unit

```json
{
  "kind": "metric",
  "formula": "\"building 32\" is predicated by \"TABLE.BUILDING_KEY = 32\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f41e988f692c629d1122"
  ]
}
```

### room

```json
{
  "kind": "metric",
  "formula": "\"Stata building\" is predicated by \"TABLE.BUILDING_NAME = 'Ray and Maria Stata Center'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e96c860644c83e93d1da"
  ]
}
```

### rooms

```json
{
  "kind": "metric",
  "formula": "\"exclude usage types that include 'STORAGE'\" is predicated by \"TABLE.SPACE_USAGE NOT LIKE '%STORAGE%'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4a22cc77afa727039697"
  ]
}
```

### space unit

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"space unit\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.d8cf06f204e97e3282ff\", \"physical_identifier\": \"SPACE_DETAIL.SPACE_USAGE_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d8cf06f204e97e3282ff"
  ]
}
```

### warehouse load date

```json
{
  "kind": "metric",
  "formula": "\"Stata building\" is predicated by \"TABLE.BUILDING_NAME = 'Ray and Maria Stata Center'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ab2616a18dd8e8b03468"
  ]
}
```

### floor

```json
{
  "kind": "metric",
  "formula": "\"Stata building\" is predicated by \"TABLE.BUILDING_NAME = 'Ray and Maria Stata Center'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.290a16901fbf7da3bff3"
  ]
}
```

### floor warehouse load date

```json
{
  "kind": "metric",
  "formula": "\"Stata building\" is predicated by \"TABLE.BUILDING_NAME = 'Ray and Maria Stata Center'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2364c73ed2ed82aac3b5"
  ]
}
```

### department count

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"department count\", \"supervision category\", \"average department count within each department count group\", \"average department count within each department count group ordered by number of supervisees\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.5c643d43b70b7cf79d6d\", \"physical_identifier\": \"SPACE_SUPERVISOR_USAGE.DEPT_COUNT\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5c643d43b70b7cf79d6d"
  ]
}
```

### department

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"department\", \"departments\", \"department names\", \"associated with that department\", \"space units associated with that department\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.76447429437b377ddff2\", \"physical_identifier\": \"SPACE_SUPERVISOR_USAGE.DEPT_NAMES\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.76447429437b377ddff2"
  ]
}
```

### MIT ID

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"MIT ID\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.0fad90b6e9a369ae6056\", \"physical_identifier\": \"SPACE_SUPERVISOR_USAGE.MIT_ID\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0fad90b6e9a369ae6056"
  ]
}
```

### range

```json
{
  "kind": "metric",
  "formula": "\"admissions\" is predicated by \"TABLE.ORGANIZATION_NAME = 'ADMISSIONS'\" | \"except Cambridge-MIT Institute\" is predicated by \"TABLE.ORGANIZATION_NAME NOT IN ('CAMBRIDGE-MIT INST')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.811b639776fe3f000b46"
  ]
}
```

### research volume

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"research volume\", \"total research volume\", \"average research volume\", \"highest research volume\", \"highest research volume ever recorded\", \"highest research volume ever recorded for each department count group\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.2d448296d8e1def71c32\", \"physical_identifier\": \"SPACE_SUPERVISOR_USAGE.RESEARCH_VOLUME\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2d448296d8e1def71c32"
  ]
}
```

### square footage

```json
{
  "kind": "metric",
  "formula": "\"admissions\" is predicated by \"TABLE.ORGANIZATION_NAME = 'ADMISSIONS'\" | \"except Cambridge-MIT Institute\" is predicated by \"TABLE.ORGANIZATION_NAME NOT IN ('CAMBRIDGE-MIT INST')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.36e2817ab4e39cd9090b"
  ]
}
```

### DLC

```json
{
  "kind": "metric",
  "formula": "\"admissions\" is predicated by \"TABLE.ORGANIZATION_NAME = 'ADMISSIONS'\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.7f6197d2f3243198183f"
  ]
}
```

### space unit

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"space unit\", \"space units\", \"organization key\", \"associated space unit\", \"facility organization\", \"minimum space unit code\", \"facility organization key\", \"space unit codes assigned to it\", \"minimum space unit code in a window\", \"total count of associated organizations\", \"space units associated with that department\", \"space unit code assigned to the organization\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.58a13fb4595f56cc0835\", \"physical_identifier\": \"SPACE_UNIT.FCLT_ORGANIZATION_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.58a13fb4595f56cc0835"
  ]
}
```

### name

```json
{
  "kind": "metric",
  "formula": "\"admissions\" is predicated by \"TABLE.ORGANIZATION_NAME = 'ADMISSIONS'\" | \"exclude organizations '138' and '250'\" is predicated by \"TABLE.ORGANIZATION_ID NOT IN ('138', '250')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a5d90a5a7e4d8e4e4849"
  ]
}
```

### range

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"range\", \"average\", \"variance\", \"code range\", \"space unit\", \"code 402100\", \"space units\", \"total rooms\", \"code variance\", \"geometric mean\", \"range category\", \"number of rooms\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.758d71c7422838ca1ece\", \"physical_identifier\": \"SPACE_UNIT.SPACE_UNIT_CODE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.758d71c7422838ca1ece"
  ]
}
```

### rank

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"rank\", \"space unit\", \"space units\", \"window column\", \"count of rooms\", \"space unit key\", \"holder category\", \"number of rooms\", \"overall average\", \"space unit's key\", \"unique space units\", \"count of space units\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.db519ea502934b5fd36d\", \"physical_identifier\": \"SPACE_UNIT.SPACE_UNIT_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.db519ea502934b5fd36d"
  ]
}
```

### space units

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"space units\", \"warehouse load date\", \"space unit window sum\", \"sum of space unit keys\", \"warehouse load date group\", \"sum of space unit keys window\", \"most recent warehouse load date\", \"warehouse load date '19-DEC-24'\", \"warehouse load date (space unit)\", \"warehouse load date of '19-DEC-24'\", \"warehouse load date of the space unit\", \"sum of space unit keys within warehouse load date\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.58de4b8aacea625bd142\", \"physical_identifier\": \"SPACE_UNIT.WAREHOUSE_LOAD_DATE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.58de4b8aacea625bd142"
  ]
}
```

### space usage

```json
{
  "kind": "metric",
  "formula": "\"exclude usage types that include 'STORAGE'\" is predicated by \"TABLE.SPACE_USAGE NOT LIKE '%STORAGE%'\" | \"Stata building\" is predicated by \"TABLE.BUILDING_KEY = '32'",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d11672bc5b4d6f4332c5"
  ]
}
```

### warehouse load date from SPACE_USAGE

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"warehouse load date from SPACE_USAGE\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.115f9b1ef10f4bf97515\", \"physical_identifier\": \"SPACE_USAGE.WAREHOUSE_LOAD_DATE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.115f9b1ef10f4bf97515"
  ]
}
```

### Course 18

```json
{
  "kind": "metric",
  "formula": "\"biology and chemistry department\" is predicated by \"TABLE.OFFER_DEPT_NAME IN ('Chemistry', 'Biology')\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c2bf381784457ab815e7"
  ]
}
```

### department full name

```json
{
  "kind": "metric",
  "formula": "\"courses with materials\" is predicated by \"TIP_SUBJECT_OFFERED.IS_NO_COURSE_MATERIAL = 'N'\" | \"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.bdcd088231174f33b6ad"
  ]
}
```

### department

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.796958cf6647c834417d"
  ]
}
```

### department's school code

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"department's school code\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.f3ede4f6d30080fd6795\", \"physical_identifier\": \"STUDENT_DEPARTMENT.SCHOOL_CODE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f3ede4f6d30080fd6795"
  ]
}
```

### school

```json
{
  "kind": "metric",
  "formula": "\"biology and chemistry department\" is predicated by \"TABLE.OFFER_DEPT_NAME IN ('Chemistry', 'Biology')\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ddcf9ed0c9f18c842e88"
  ]
}
```

### subjects offered

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"subjects offered\", \"cluster type of 'S'\", \"subject cluster type\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.d957fedc19d7ac1e02bb\", \"physical_identifier\": \"SUBJECT_OFFERED.CLUSTER_TYPE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d957fedc19d7ac1e02bb"
  ]
}
```

### cluster type

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"cluster type\", \"cluster type description\", \"cluster type of 'SWE: School-Wide Electives'\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.f6eb23a766c7941536c6\", \"physical_identifier\": \"SUBJECT_OFFERED.CLUSTER_TYPE_DESC\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f6eb23a766c7941536c6"
  ]
}
```

### course number from the offered table

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"course number from the offered table\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.94e12e2de5eb65052152\", \"physical_identifier\": \"SUBJECT_OFFERED.COURSE_NUMBER\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.94e12e2de5eb65052152"
  ]
}
```

### HGN code

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Course 17\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.df60dd9b3f5a172f57d3"
  ]
}
```

### not for graduate credit

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.62064b1bb6e5779544bc"
  ]
}
```

### master sections

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"master sections\", \"is master section\", \"IS_MASTER_SECTION = 'Y'\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.22b0955b4028b4f784c1\", \"physical_identifier\": \"SUBJECT_OFFERED.IS_MASTER_SECTION\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.22b0955b4028b4f784c1"
  ]
}
```

### not repeatable

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"not repeatable\", \"subjects offered\", \"repeatable subjects\", \"non-repeatable subjects\", \"subjects that are not repeatable\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.e444fe1b8d28f06d7c6d\", \"physical_identifier\": \"SUBJECT_OFFERED.IS_REPEATABLE_SUBJECT\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e444fe1b8d28f06d7c6d"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c0ae981effa18c72f331"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5892f6eeaae7a7ece6d5"
  ]
}
```

### AVERAGE

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.6ecc4ed382ab5eee61c2"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f654c020a4418d5327a3"
  ]
}
```

### rank

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.6094abb144d5d75c79b2"
  ]
}
```

### offer school name

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"offer school name\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.0cf1951681d77996a5ff\", \"physical_identifier\": \"SUBJECT_OFFERED.OFFER_SCHOOL_NAME\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0cf1951681d77996a5ff"
  ]
}
```

### faculty

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.afb545fb96779475669d"
  ]
}
```

### section ID of 0

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"section ID of 0\", \"subjects offered\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.4d57388c46c4f18c9e35\", \"physical_identifier\": \"SUBJECT_OFFERED.SECTION_ID\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4d57388c46c4f18c9e35"
  ]
}
```

### AVERAGE

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"AVERAGE\", \"POPULAR\", \"UNPOPULAR\", \"enrollment\", \"subjects offered\", \"popularity category\", \"subject enrollment number\", \"department's average enrollment\", \"average subject enrollment number\", \"average enrollment for the department\", \"deviation of each subject's enrollment number from the average\", \"average subject enrollment number within each subject key group\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.ad58e53fcf84df4fa105\", \"physical_identifier\": \"SUBJECT_OFFERED.SUBJECT_ENROLLMENT_NUMBER\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ad58e53fcf84df4fa105"
  ]
}
```

### subject

```json
{
  "kind": "metric",
  "formula": "\"biology department\" is predicated by \"LOWER(TABLE.DLC_NAME) = LOWER('Biology')\" | \"biology course\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Biology'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a6d1cb8c806e803a4fa0"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b78081f07f367899b758"
  ]
}
```

### rank

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.257d24ea261a1f9b997b"
  ]
}
```

### subjects offered

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"subjects offered\", \"subject offered summary key\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.647b67002e48728cd88e\", \"physical_identifier\": \"SUBJECT_OFFERED.SUBJECT_OFFERED_SUMMARY_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.647b67002e48728cd88e"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"biology and chemistry department\" is predicated by \"TABLE.OFFER_DEPT_NAME IN ('Chemistry', 'Biology')\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2dbcfcfccd37de660a15"
  ]
}
```

### subject

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Course 17\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a7d36039e9319a4fd559"
  ]
}
```

### 2012

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.67bdcd9403e8c8b36937"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"subjects\", \"2012SU term\", \"cluster type\", \"cluster type 'S'\", \"cluster type of 'S'\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.2ec59fba656c0e8e7e9c\", \"physical_identifier\": \"SUBJECT_OFFERED_SUMMARY.CLUSTER_TYPE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2ec59fba656c0e8e7e9c"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b450261a69f8cd961a4c"
  ]
}
```

### courses

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5f52d2569ae6a8d361d6"
  ]
}
```

### HGN code

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.1aa079c6f483a8992c2e"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.281fa783eb70b170cf12"
  ]
}
```

### lecture units

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"lecture units\", \"units minus lecture\", \"average lecture units\", \"difference between the total units and lecture units\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.efd050411e5fa6d55246\", \"physical_identifier\": \"SUBJECT_OFFERED_SUMMARY.LECTURE_UNITS\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.efd050411e5fa6d55246"
  ]
}
```

### average

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Political Science\" is predicated by \"TABLE.DEPARTMENT_CODE = '17'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.3356292216fb12452df7"
  ]
}
```

### AVERAGE

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_CODE = '18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.6b33fb4229f9254ceed5"
  ]
}
```

### Biology

```json
{
  "kind": "metric",
  "formula": "\"biology and chemistry department\" is predicated by \"TABLE.OFFER_DEPT_NAME IN ('Chemistry', 'Biology')\" | \"Course 7\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Biology'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.eff23a813b960007375f"
  ]
}
```

### school

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Course 17\" is predicated by \"TABLE.DEPARTMENT_CODE = '17'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d3d6fb2aa8412608fb26"
  ]
}
```

### faculty

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b4524c6ac7ed9755b10c"
  ]
}
```

### responsible faculty name

```json
{
  "kind": "metric",
  "formula": "\"degree-granting\" is predicated by \"TABLE.IS_DEGREE_GRANTING = 'Y'\" | \"Chemistry\" is predicated by \"TABLE.DEPARTMENT_CODE = '5'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8670dea95560d658e413"
  ]
}
```

### students enrolled

```json
{
  "kind": "metric",
  "formula": "\"degree-granting\" is predicated by \"TABLE.IS_DEGREE_GRANTING = 'Y'\" | \"Biology\" is predicated by \"TABLE.DEPARTMENT_CODE = '7'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.dec4a24ebdec0a798f3e"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"biology and chemistry department\" is predicated by \"TABLE.OFFER_DEPT_NAME IN ('Chemistry', 'Biology')\" | \"Course 7\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Biology'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.90d9a25268f1641e8bfc"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c7da165887de116131f0"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Course 17\" is predicated by \"TABLE.DEPARTMENT_CODE = '17'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5ba66ffd5c591af615a1"
  ]
}
```

### subject

```json
{
  "kind": "metric",
  "formula": "\"degree-granting\" is predicated by \"TABLE.IS_DEGREE_GRANTING = 'Y'\" | \"Course 6\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b164aa72e0e46f636781"
  ]
}
```

### 2012

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Mathematics\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2062168b0462d5fad1ee"
  ]
}
```

### units

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a8e81ff9ad5ac4798b21"
  ]
}
```

### rank

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"rank\", \"cluster type\", \"cluster type of 'S'\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.e153ffa854a1e0ca4a86\", \"physical_identifier\": \"SUBJECT_SUMMARY.CLUSTER_TYPE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e153ffa854a1e0ca4a86"
  ]
}
```

### Course 18

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b5984845286a2f494037"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4d1a75da4271e0fcbb0b"
  ]
}
```

### total lab units

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"total lab units\", \"average lab units\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.9334aead06cec811c9c6\", \"physical_identifier\": \"SUBJECT_SUMMARY.LAB_UNITS\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.9334aead06cec811c9c6"
  ]
}
```

### highest number of lecture units for a single Mathematics subject

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c4c23ca875d78194ad25"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"biology and chemistry department\" is predicated by \"TABLE.OFFER_DEPT_NAME IN ('Chemistry', 'Biology')\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b76461c74b5814484f66"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.32e4cffb00e00c6242c2"
  ]
}
```

### school

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Course 17\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.451d36ee4ad66e15ad33"
  ]
}
```

### school

```json
{
  "kind": "metric",
  "formula": "\"Computer Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\" | \"Course 6\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Electrical Eng & Computer Sci'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.6db80974245754456013"
  ]
}
```

### AVERAGE

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.758468612d66e9489ab1"
  ]
}
```

### subject group

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"subject group\", \"subject group ID\", \"average total units within subject group\", \"average total units within each subject group\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.89e38c4653148eac74ed\", \"physical_identifier\": \"SUBJECT_SUMMARY.SUBJECT_GROUP_ID\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.89e38c4653148eac74ed"
  ]
}
```

### rank

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.eaf592d751dbe9d8bcf0"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.199ad56cbfabf4e31bce"
  ]
}
```

### subject

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.57a69a63dc5d1a44fac2"
  ]
}
```

### term

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Course 17\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e5de602d281e10c09ff2"
  ]
}
```

### 1

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.23ea93a50d24f0b28535"
  ]
}
```

### term

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"term\", \"term code\", \"academic term\", \"term \\\"2021JA\\\"\", \"academic terms\", \"academic term code\", \"academic term code '2020FA'\", \"latest end date of the corresponding academic term\", \"academic term in which the maximum enrollment occurred\", \"earliest start date of the corresponding academic term\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.8b3a691b0ac9a6cc67da\", \"physical_identifier\": \"TIME_DAY.ACADEMIC_TERM_CODE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8b3a691b0ac9a6cc67da"
  ]
}
```

### academic term description

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"academic term description\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.a8cd9d8dc7cfa03327ac\", \"physical_identifier\": \"TIME_DAY.ACADEMIC_TERM_DESCRIPTION\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a8cd9d8dc7cfa03327ac"
  ]
}
```

### academic year is not null

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"academic year is not null\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.53eb159705af7d83d9c8\", \"physical_identifier\": \"TIME_DAY.ACADEMIC_YEAR\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.53eb159705af7d83d9c8"
  ]
}
```

### calendar date

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"calendar date\", \"calendar dates\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.0faaecf637edf7509774\", \"physical_identifier\": \"TIME_DAY.CALENDAR_DATE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0faaecf637edf7509774"
  ]
}
```

### calendar year

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"calendar year\", \"average calendar year\", \"normalized subjects per year\", \"variance of the calendar year\", \"average calendar year within each calendar year group ordered by term start date\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.44e312f2b6856dbc8365\", \"physical_identifier\": \"TIME_DAY.CALENDAR_YEAR\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.44e312f2b6856dbc8365"
  ]
}
```

### subtotals

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"subtotals\", \"day of week\", \"grand total\", \"day of the week\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.915e9a4f9e8c2d0b64b2\", \"physical_identifier\": \"TIME_DAY.DAY_OF_WEEK\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.915e9a4f9e8c2d0b64b2"
  ]
}
```

### latest end date

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"latest end date\", \"latest end date of the corresponding academic term\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.e97ed0fcbd00bf31f385\", \"physical_identifier\": \"TIME_DAY.END_DATE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e97ed0fcbd00bf31f385"
  ]
}
```

### days

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"days\", \"corresponding day\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.11964030983fa5ae7115\", \"physical_identifier\": \"TIME_DAY.FISCAL_PERIOD\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.11964030983fa5ae7115"
  ]
}
```

### fiscal year of the calendar date

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"fiscal year of the calendar date\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.2c5ca75af0cc0f36e4b2\", \"physical_identifier\": \"TIME_DAY.FISCAL_YEAR\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2c5ca75af0cc0f36e4b2"
  ]
}
```

### earliest start date

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"earliest start date\", \"earliest start date of the corresponding academic term\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.8330c2197dbdc494f43f\", \"physical_identifier\": \"TIME_DAY.START_DATE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8330c2197dbdc494f43f"
  ]
}
```

### months

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"months\", \"calendar month\", \"calendar month numbers\", \"current calendar month\", \"minimum calendar month\", \"average calendar month number\", \"average calendar month (as a number)\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.ee02033ef27e22fd9627\", \"physical_identifier\": \"TIME_MONTH.CALENDAR_MONTH\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ee02033ef27e22fd9627"
  ]
}
```

### calendar month name

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"calendar month name\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.7534c7ec6e64b0e07310\", \"physical_identifier\": \"TIME_MONTH.CALENDAR_MONTH_NAME\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.7534c7ec6e64b0e07310"
  ]
}
```

### calendar period description

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"calendar period description\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.628a90964e1a1b14f5cb\", \"physical_identifier\": \"TIME_MONTH.CALENDAR_PERIOD_DESCRIPTION\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.628a90964e1a1b14f5cb"
  ]
}
```

### calendar year

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"calendar year\", \"sum of calendar years\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.d4753257c93d30a072b3\", \"physical_identifier\": \"TIME_MONTH.CALENDAR_YEAR\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d4753257c93d30a072b3"
  ]
}
```

### fiscal period

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"fiscal period\", \"corresponding day\", \"window of 2 preceding and 2 following rows grouped by the fiscal period\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.45a43cb855a7f5b09c3f\", \"physical_identifier\": \"TIME_MONTH.FISCAL_PERIOD\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.45a43cb855a7f5b09c3f"
  ]
}
```

### fiscal period description

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"fiscal period description\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.58617dd6f9f3f43221b9\", \"physical_identifier\": \"TIME_MONTH.FISCAL_PERIOD_DESCRIPTION\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.58617dd6f9f3f43221b9"
  ]
}
```

### fiscal year

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"fiscal year\", \"months in the fiscal year 2020\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.73678ed7ca6d85fbf851\", \"physical_identifier\": \"TIME_MONTH.FISCAL_YEAR\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.73678ed7ca6d85fbf851"
  ]
}
```

### year 2026

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"year 2026\", \"fiscal year\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.5e27f4bdc6c95bd48d5e\", \"physical_identifier\": \"TIME_QUARTER.FISCAL_YEAR\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5e27f4bdc6c95bd48d5e"
  ]
}
```

### fiscal quarter

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"fiscal quarter\", \"fiscal quarters\", \"fiscal quarter code\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.9a401adfd32e3549c43b\", \"physical_identifier\": \"TIME_QUARTER.FY_QUARTER_CODE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.9a401adfd32e3549c43b"
  ]
}
```

### quarter start date

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"quarter start date\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.a7638468d90f5877b7cf\", \"physical_identifier\": \"TIME_QUARTER.QUARTER_START_DATE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a7638468d90f5877b7cf"
  ]
}
```

### ISBN

```json
{
  "kind": "metric",
  "formula": "\"biology and chemistry department\" is predicated by \"TABLE.OFFER_DEPT_NAME IN ('Chemistry', 'Biology')\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c159b794e39922eb434f"
  ]
}
```

### tip detail

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e4e21dd4ac50cd319c14"
  ]
}
```

### subject

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ef4a046185dc8b51e869"
  ]
}
```

### term

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0f9554279ae6f7deeb4b"
  ]
}
```

### count

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"Course 18\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.9dbe80ed1846d8119a3f"
  ]
}
```

### NM status

```json
{
  "kind": "metric",
  "formula": "\"biology and chemistry department\" is predicated by \"TABLE.OFFER_DEPT_NAME IN ('Chemistry', 'Biology')\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5da24851c2278d96d769"
  ]
}
```

### row number

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"TABLE.TERM_CODE\" is formatted as \"YYYYTT\" where \"YYYY\" is the year and \"TT\" is the term. Terms can be \"FA\", \"JA\", \"SP\", and \"SU\" for fall, IAP, spring, and summer",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0a3e7913735b57b32977"
  ]
}
```

### most recent warehouse load date from tip detail

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"most recent warehouse load date from tip detail\", \"most recent warehouse load date from the tip detail table\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.fc3b05f58bb140340be8\", \"physical_identifier\": \"TIP_DETAIL.WAREHOUSE_LOAD_DATE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.fc3b05f58bb140340be8"
  ]
}
```

### author

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"author\", \"TIP_MATERIAL\", \"non-null author\", \"material has a non-null author\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.e65126703f83dd2a0bcc\", \"physical_identifier\": \"TIP_MATERIAL.AUTHOR\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e65126703f83dd2a0bcc"
  ]
}
```

### TIP_MATERIAL

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"TIP_MATERIAL\", \"material info source\", \"material information source\", \"material info source of 'ISBN'\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.dc94b30955ddeec0cd8e\", \"physical_identifier\": \"TIP_MATERIAL.MATERIAL_INFO_SOURCE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.dc94b30955ddeec0cd8e"
  ]
}
```

### CHEAP

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"CHEAP\", \"MODERATE\", \"EXPENSIVE\", \"TIP_MATERIAL\", \"price category\", \"new shelf price\", \"used price category\", \"total new shelf price\", \"average new shelf price\", \"new shelf price greater than 10\", \"total new shelf price from TIP_MATERIAL\", \"materials with a new shelf price greater than 10\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.d686530dc7cd196f5e8e\", \"physical_identifier\": \"TIP_MATERIAL.NEW_SHELF_PRICE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d686530dc7cd196f5e8e"
  ]
}
```

### publisher

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"publisher\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.8e8e73170989f9a619e5\", \"physical_identifier\": \"TIP_MATERIAL.PUBLISHER\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8e8e73170989f9a619e5"
  ]
}
```

### TIP_MATERIAL

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"TIP_MATERIAL\", \"materials assigned\", \"number of materials\", \"number of materials assigned\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.71950f264cd3c646169d\", \"physical_identifier\": \"TIP_MATERIAL.TIP_MATERIAL_KEY\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.71950f264cd3c646169d"
  ]
}
```

### used shelf price

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"used shelf price\", \"used price category\", \"average used shelf price\", \"minimum used shelf price\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.307430e84271e0044428\", \"physical_identifier\": \"TIP_MATERIAL.USED_SHELF_PRICE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.307430e84271e0044428"
  ]
}
```

### materials published after 2010

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"materials published after 2010\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.e8e542aa5702c524c816\", \"physical_identifier\": \"TIP_MATERIAL.YEAR\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e8e542aa5702c524c816"
  ]
}
```

### material status

```json
{
  "kind": "metric",
  "formula": "\"courses with materials\" is predicated by \"TIP_SUBJECT_OFFERED.IS_NO_COURSE_MATERIAL = 'N'\" | \"Course 7\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Biology'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b88f7ac09e5b46b53d55"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e45703b6a0cfc776b03c"
  ]
}
```

### course number description

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"course number description\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.8e80760c9b86c56e47c7\", \"physical_identifier\": \"TIP_SUBJECT_OFFERED.COURSE_NUMBER_DESC\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8e80760c9b86c56e47c7"
  ]
}
```

### has materials

```json
{
  "kind": "metric",
  "formula": "\"courses with materials\" is predicated by \"TIP_SUBJECT_OFFERED.IS_NO_COURSE_MATERIAL = 'N'\" | \"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.03aaaf4ee4ae01b508d8"
  ]
}
```

### total number of such courses

```json
{
  "kind": "metric",
  "formula": "\"courses with materials\" is predicated by \"TIP_SUBJECT_OFFERED.IS_NO_COURSE_MATERIAL = 'N'\" | \"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c76157c97fe0e290c062"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"biology and chemistry department\" is predicated by \"TABLE.OFFER_DEPT_NAME IN ('Chemistry', 'Biology')\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a23c48bbd81abdac1b81"
  ]
}
```

### subjects

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.1139eae77f27c58b270c"
  ]
}
```

### range

```json
{
  "kind": "metric",
  "formula": "\"biology and chemistry department\" is predicated by \"TABLE.OFFER_DEPT_NAME IN ('Chemistry', 'Biology')\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e445e0096e126708f90c"
  ]
}
```

### courses

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Political Science\" is predicated by \"TABLE.DEPARTMENT_CODE = '17'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e9ca8509c1f930260637"
  ]
}
```

### Biology

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.bcf136771efcbd83411b"
  ]
}
```

### school

```json
{
  "kind": "metric",
  "formula": "\"Political Science\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Political Science'\" | \"Political Science\" is predicated by \"TABLE.DEPARTMENT_CODE = '17'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.db547341ff270657cbdd"
  ]
}
```

### TIP subject

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.97c5dbe80eafbd04f4ff"
  ]
}
```

### TIP subject

```json
{
  "kind": "metric",
  "formula": "\"math\" is predicated by \"TABLE.DEPARTMENT_NAME = 'Mathematics'\" | \"courses with materials\" is predicated by \"TIP_SUBJECT_OFFERED.IS_NO_COURSE_MATERIAL = 'N'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.44b2af18a975e483a3a0"
  ]
}
```

### courses

```json
{
  "kind": "metric",
  "formula": "\"biology and chemistry department\" is predicated by \"TABLE.OFFER_DEPT_NAME IN ('Chemistry', 'Biology')\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.1852932e741995a1314d"
  ]
}
```

### TIP subject

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"TIP subject\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.bdfe496324c5c798bd7d\", \"physical_identifier\": \"TIP_SUBJECT_OFFERED.SUBJECT_ID_SORT\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.bdfe496324c5c798bd7d"
  ]
}
```

### courses

```json
{
  "kind": "metric",
  "formula": "\"biology and chemistry department\" is predicated by \"TABLE.OFFER_DEPT_NAME IN ('Chemistry', 'Biology')\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.022a90cee596eb0f9f7f"
  ]
}
```

### 2012

```json
{
  "kind": "metric",
  "formula": "\"Chemistry\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\" | \"Course 5\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Chemistry'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.3b7a2abe089ddf2bbbdd"
  ]
}
```

### course

```json
{
  "kind": "metric",
  "formula": "\"courses with materials\" is predicated by \"TIP_SUBJECT_OFFERED.IS_NO_COURSE_MATERIAL = 'N'\" | \"Course 7\" is predicated by \"TABLE.OFFER_DEPT_NAME = 'Biology'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b21f6a239c4e74b530ee"
  ]
}
```

### rooms

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"rooms\", \"AVERAGE\", \"average\", \"LOW_ACCESS\", \"HIGH_ACCESS\", \"access level\", \"access levels\", \"access level 1\", \"number of rooms\", \"access level of 1\", \"standard deviation\", \"room's access level\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.d8c6a202bf7aef142c2c\", \"physical_identifier\": \"ZPM_ROOMS_LOAD.ACCESS_LEVEL\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d8c6a202bf7aef142c2c"
  ]
}
```

### building component

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"building component\", \"minimum access level\", \"windowed minimum access level\", \"minimum access level in a window\", \"minimum access level in a window of 3 preceding and 1 following row ordered by the building component\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.614f5062292eb54dd74e\", \"physical_identifier\": \"ZPM_ROOMS_LOAD.BUILDING_COMPONENT\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.614f5062292eb54dd74e"
  ]
}
```

### room

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"room\", \"rooms\", \"room count\", \"building room\", \"building rooms\", \"rooms assigned\", \"number of rooms\", \"room on floor 2\", \"rooms on floor 2\", \"maximum row number\", \"number of rooms assigned\", \"total number of rooms assigned\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.05ee16624c04768f1521\", \"physical_identifier\": \"ZPM_ROOMS_LOAD.BUILDING_ROOM\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.05ee16624c04768f1521"
  ]
}
```

### floor

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"floor\", \"rooms\", \"AVERAGE\", \"floor 2\", \"LOW_ACCESS\", \"HIGH_ACCESS\", \"average floor\", \"highest floor\", \"room on floor 2\", \"rooms on floor 2\", \"floor 2 or higher\", \"rooms located on floor 2\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.b71bd1aaa8a83ae8d5b1\", \"physical_identifier\": \"ZPM_ROOMS_LOAD.FLOOR\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b71bd1aaa8a83ae8d5b1"
  ]
}
```

### rooms

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"rooms\", \"HR org unit id\", \"rooms assigned to it\", \"department assigned to rooms\", \"rooms assigned to department\", \"rooms assigned to that organization\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.e9cc9a656da294eedf49\", \"physical_identifier\": \"ZPM_ROOMS_LOAD.HR_ORG_UNIT_ID\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e9cc9a656da294eedf49"
  ]
}
```

### rooms

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"rooms\", \"space unit code\", \"number of rooms per space unit\", \"rooms assigned to the space unit\", \"rooms assigned to each space unit\", \"average access level for that space unit\", \"total number of rooms per space unit code\", \"total number of such rooms per space unit\", \"average floor within each space unit code group\", \"total number of rooms per space unit code with access level 1\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.2370b9a234c6b30fe2bf\", \"physical_identifier\": \"ZPM_ROOMS_LOAD.SPACE_UNIT_CODE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2370b9a234c6b30fe2bf"
  ]
}
```

### space usage

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"space usage\", \"space usages\", \"space usage type\", \"space usage types\", \"unique space usages\", \"count of rooms for that usage\", \"average floor within each space usage group\", \"highest floor among rooms with access level 1 for each space usage group\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.c8586a32150d31d92501\", \"physical_identifier\": \"ZPM_ROOMS_LOAD.SPACE_USAGE\", \"schema_context\": \"dw\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c8586a32150d31d92501"
  ]
}
```


## 增量维护事件

