# BIRD-Dev / california_schools — Schema 与业务口径解释

该数据库的存档目录包含 3 张表、89 个物理列、2 条关系，以及 3 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## frpm

This table stores Free and Reduced Price Meal (FRPM) eligibility and enrollment data for California schools, broken down by academic year, grade levels, and age groups.

恢复表名: frpm / Free and Reduced Price Meal data / FRPM eligibility table / California school meal program data / School meal program participation / Student meal eligibility records
SQL表别名: f, f2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| frpm.XCL_001 | cdscode / CDS code / California Department of Education school code / school identifier / school ID / unique school code | text | schema / frpm |
| frpm.XCL_002 | academic year / school year / year / school term | text | schema / frpm |
| frpm.XCL_003 | county code / county ID / county number / county identifier | text | schema / frpm |
| frpm.XCL_004 | district code / district ID / district number / school district code | integer | schema / frpm |
| frpm.XCL_005 | school code / school number / school ID / school identifier | text | schema / frpm |
| frpm.XCL_006 | county name / county / California county | text | schema / frpm |
| frpm.XCL_007 | district name / school district / district | text | schema / frpm |
| frpm.XCL_008 | school name / school / institution name | text | schema / frpm |
| frpm.XCL_009 | district type / district classification / type of district / district category | text | schema / frpm |
| frpm.XCL_010 | school type / school classification / type of school / school category | text | schema / frpm |
| frpm.XCL_011 | educational option type / educational option / school program type / option type | text | schema / frpm |
| frpm.XCL_012 | nslp provision status / NSLP status / National School Lunch Program provision / meal provision status | text | schema / frpm |
| frpm.XCL_013 | charter school y n / charter school indicator / is charter school / charter status | integer | schema / frpm |
| frpm.XCL_014 | charter school number / charter number / charter ID / charter school identifier | text | schema / frpm |
| frpm.XCL_015 | charter funding type / charter funding source / funding type / charter funding model | text | schema / frpm |
| frpm.XCL_016 | irc / IRC status / Independent Reading Counts / IRC indicator | integer | schema / frpm |
| frpm.XCL_017 | low grade / lowest grade / minimum grade / starting grade | text | schema / frpm |
| frpm.XCL_018 | high grade / highest grade / maximum grade / ending grade | text | schema / frpm |
| frpm.XCL_019 | enrollment k 12 / K-12 enrollment / total enrollment / student count K-12 | real | schema / frpm |
| frpm.XCL_020 | free meal count k 12 / free meal count K-12 / number of free meals K-12 / free lunch count | real | schema / frpm |
| frpm.XCL_021 | percent eligible free k 12 / free meal percentage K-12 / percent free K-12 / free eligibility rate K-12 | real | schema / frpm |
| frpm.XCL_022 | frpm count k 12 / FRPM count K-12 / free and reduced meal count K-12 / number of FRPM students K-12 | real | schema / frpm |
| frpm.XCL_023 | percent eligible frpm k 12 / FRPM percentage K-12 / percent FRPM K-12 / FRPM eligibility rate K-12 | real | schema / frpm |
| frpm.XCL_024 | enrollment ages 5 17 / enrollment ages 5-17 / student count ages 5-17 / total enrollment 5-17 | real | schema / frpm |
| frpm.XCL_025 | free meal count ages 5 17 / free meal count ages 5-17 / number of free meals ages 5-17 / free lunch count ages 5-17 | real | schema / frpm |
| frpm.XCL_026 | percent eligible free ages 5 17 / free meal percentage ages 5-17 / percent free ages 5-17 / free eligibility rate ages 5-17 | real | schema / frpm |
| frpm.XCL_027 | frpm count ages 5 17 / FRPM count ages 5-17 / free and reduced meal count ages 5-17 / number of FRPM students ages 5-17 | real | schema / frpm |
| frpm.XCL_028 | percent eligible frpm ages 5 17 / FRPM percentage ages 5-17 / percent FRPM ages 5-17 / FRPM eligibility rate ages 5-17 | real | schema / frpm |
| frpm.XCL_029 | 2013 14 calpads fall 1 certification status / CALPADS certification status / 2013-14 certification / Fall 1 certification status | integer | schema / frpm |

## satscores

This table stores SAT test results for California schools, including enrollment, test takers, and average scores in reading, math, and writing.

恢复表名: satscores / sat_scores / sat_results / test_scores
SQL表别名: s, sat, ss, t

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| satscores.XCL_030 | cds / cds_code / school_code / county_district_school_code / cds_id | text | schema / satscores |
| satscores.XCL_031 | rtype / record_type / report_type / type | text | schema / satscores |
| satscores.XCL_032 | sname / school_name / school / name | text | schema / satscores |
| satscores.XCL_033 | dname / district_name / district / school_district | text | schema / satscores |
| satscores.XCL_034 | cname / county_name / county | text | schema / satscores |
| satscores.XCL_035 | enroll12 / enrollment_12th_grade / grade_12_enrollment / senior_enrollment / enrollment | integer | schema / satscores |
| satscores.XCL_036 | num tst takr / number tst takr / test_takers / number_of_test_takers / sat_takers / num_test_takers | integer | schema / satscores |
| satscores.XCL_037 | avg scr read / average scr read / average_reading_score / reading_average / avg_read / sat_reading_score | integer | schema / satscores |
| satscores.XCL_038 | avg scr math / average scr math / average_math_score / math_average / avg_math / sat_math_score | integer | schema / satscores |
| satscores.XCL_039 | avg scr write / average scr write / average_writing_score / writing_average / avg_write / sat_writing_score | integer | schema / satscores |
| satscores.XCL_040 | num ge1500 / number ge1500 / students_above_1500 / count_ge_1500 / num_scoring_1500_or_higher / high_scorers | integer | schema / satscores |

## schools

This table stores comprehensive information about schools in California, including identifiers, location, contact details, operational status, educational programs, and administrative contacts.

恢复表名: schools / school / california schools / ca schools / educational institutions
SQL表别名: c, s, s2, sc

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| schools.XCL_041 | cdscode / CDS code / California Department of Education code / school ID / school identifier | text | schema / schools |
| schools.XCL_042 | ncesdist / NCES district code / National Center for Education Statistics district ID / district identifier | text | schema / schools |
| schools.XCL_043 | ncesschool / NCES school code / National Center for Education Statistics school ID / school identifier | text | schema / schools |
| schools.XCL_044 | status type / status / school status / operational status / StatusType | text | schema / schools |
| schools.XCL_045 | county / county name | text | schema / schools |
| schools.XCL_046 | district / school district / district name | text | schema / schools |
| schools.XCL_047 | school / school name / institution name | text | schema / schools |
| schools.XCL_048 | street / street address / address / physical address | text | schema / schools |
| schools.XCL_049 | street abr / abbreviated street / street abbreviation / short street / StreetAbr | text | schema / schools |
| schools.XCL_050 | city / city name | text | schema / schools |
| schools.XCL_051 | zip / zip code / postal code | text | schema / schools |
| schools.XCL_052 | state / state abbreviation | text | schema / schools |
| schools.XCL_053 | mail street / mailing street / mailing address / MailStreet | text | schema / schools |
| schools.XCL_054 | mail str abr / mailing street abbreviation / abbreviated mailing street / MailStrAbr | text | schema / schools |
| schools.XCL_055 | mail city / mailing city / MailCity | text | schema / schools |
| schools.XCL_056 | mail zip / mailing zip / mailing ZIP code / MailZip | text | schema / schools |
| schools.XCL_057 | mail state / mailing state / MailState | text | schema / schools |
| schools.XCL_058 | phone / phone number / telephone / contact number | text | schema / schools |
| schools.XCL_059 | ext / extension / phone extension | text | schema / schools |
| schools.XCL_060 | website / web address / URL / school website | text | schema / schools |
| schools.XCL_061 | open date / opening date / date opened / OpenDate | date | schema / schools |
| schools.XCL_062 | closed date / closing date / date closed / ClosedDate | date | schema / schools |
| schools.XCL_063 | charter / charter school flag / is charter / charter indicator | integer | schema / schools |
| schools.XCL_064 | charter num / charter number / charter ID / CharterNum | text | schema / schools |
| schools.XCL_065 | funding type / funding source / FundingType | text | schema / schools |
| schools.XCL_066 | doc / document / district of control code / DOC code | text | schema / schools |
| schools.XCL_067 | doctype / district of control type / DOC type | text | schema / schools |
| schools.XCL_068 | soc / school of control code / SOC code | text | schema / schools |
| schools.XCL_069 | soctype / school of control type / SOC type | text | schema / schools |
| schools.XCL_070 | ed ops code / educational operations code / EdOps code / EdOpsCode | text | schema / schools |
| schools.XCL_071 | ed ops name / educational operations name / EdOps name / EdOpsName | text | schema / schools |
| schools.XCL_072 | eilcode / educational level code / EIL code | text | schema / schools |
| schools.XCL_073 | eilname / educational level name / EIL name | text | schema / schools |
| schools.XCL_074 | gsoffered / grades offered / grade span offered | text | schema / schools |
| schools.XCL_075 | gsserved / grades served / grade span served | text | schema / schools |
| schools.XCL_076 | virtual / virtual school flag / is virtual / virtual indicator | text | schema / schools |
| schools.XCL_077 | magnet / magnet school flag / is magnet / magnet indicator | integer | schema / schools |
| schools.XCL_078 | latitude / lat | real | schema / schools |
| schools.XCL_079 | longitude / lon / lng | real | schema / schools |
| schools.XCL_080 | adm fname1 / administrator first name 1 / admin first name / principal first name / AdmFName1 | text | schema / schools |
| schools.XCL_081 | adm lname1 / administrator last name 1 / admin last name / principal last name / AdmLName1 | text | schema / schools |
| schools.XCL_082 | adm email1 / administrator email 1 / admin email / principal email / AdmEmail1 | text | schema / schools |
| schools.XCL_083 | adm fname2 / administrator first name 2 / admin first name 2 / secondary admin first name / AdmFName2 | text | schema / schools |
| schools.XCL_084 | adm lname2 / administrator last name 2 / admin last name 2 / secondary admin last name / AdmLName2 | text | schema / schools |
| schools.XCL_085 | adm email2 / administrator email 2 / admin email 2 / secondary admin email / AdmEmail2 | text | schema / schools |
| schools.XCL_086 | adm fname3 / administrator first name 3 / admin first name 3 / tertiary admin first name / AdmFName3 | text | schema / schools |
| schools.XCL_087 | adm lname3 / administrator last name 3 / admin last name 3 / tertiary admin last name / AdmLName3 | text | schema / schools |
| schools.XCL_088 | adm email3 | text | schema / schools |
| schools.XCL_089 | last update | date | schema / schools |

## 表关系与连接依据

- frpm.XCL_001 ↔ schools.XCL_041; declared_or_materialized_relationship
- satscores.XCL_030 ↔ schools.XCL_041; declared_or_materialized_relationship

## 业务口径、总体与粒度


## 增量维护事件

