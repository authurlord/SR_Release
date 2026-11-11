# Spider2-Lite / city_legislation — Schema 与业务口径解释

该数据库的存档目录包含 15 张表、133 个物理列、0 条关系，以及 15 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## alien_data

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| alien_data.id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / alien_data |
| alien_data.first_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / alien_data |
| alien_data.last_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / alien_data |
| alien_data.email | 保留物理名称；存档没有恢复别名 | TEXT | schema / alien_data |
| alien_data.gender | 保留物理名称；存档没有恢复别名 | TEXT | schema / alien_data |
| alien_data.type | 保留物理名称；存档没有恢复别名 | TEXT | schema / alien_data |
| alien_data.birth_year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / alien_data |
| alien_data.age | 保留物理名称；存档没有恢复别名 | INTEGER | schema / alien_data |
| alien_data.favorite_food | 保留物理名称；存档没有恢复别名 | TEXT | schema / alien_data |
| alien_data.feeding_frequency | 保留物理名称；存档没有恢复别名 | TEXT | schema / alien_data |
| alien_data.aggressive | 保留物理名称；存档没有恢复别名 | INTEGER | schema / alien_data |
| alien_data.occupation | 保留物理名称；存档没有恢复别名 | TEXT | schema / alien_data |
| alien_data.current_location | 保留物理名称；存档没有恢复别名 | TEXT | schema / alien_data |
| alien_data.state | 保留物理名称；存档没有恢复别名 | TEXT | schema / alien_data |
| alien_data.us_region | 保留物理名称；存档没有恢复别名 | TEXT | schema / alien_data |
| alien_data.country | 保留物理名称；存档没有恢复别名 | TEXT | schema / alien_data |

## aliens

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| aliens.id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / aliens |
| aliens.first_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / aliens |
| aliens.last_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / aliens |
| aliens.email | 保留物理名称；存档没有恢复别名 | TEXT | schema / aliens |
| aliens.gender | 保留物理名称；存档没有恢复别名 | TEXT | schema / aliens |
| aliens.type | 保留物理名称；存档没有恢复别名 | TEXT | schema / aliens |
| aliens.birth_year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / aliens |

## aliens_details

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| aliens_details.detail_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / aliens_details |
| aliens_details.favorite_food | 保留物理名称；存档没有恢复别名 | TEXT | schema / aliens_details |
| aliens_details.feeding_frequency | 保留物理名称；存档没有恢复别名 | TEXT | schema / aliens_details |
| aliens_details.aggressive | 保留物理名称；存档没有恢复别名 | INTEGER | schema / aliens_details |

## aliens_location

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| aliens_location.loc_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / aliens_location |
| aliens_location.current_location | 保留物理名称；存档没有恢复别名 | TEXT | schema / aliens_location |
| aliens_location.state | 保留物理名称；存档没有恢复别名 | TEXT | schema / aliens_location |
| aliens_location.country | 保留物理名称；存档没有恢复别名 | TEXT | schema / aliens_location |
| aliens_location.occupation | 保留物理名称；存档没有恢复别名 | TEXT | schema / aliens_location |

## cities

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: c

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cities.city_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / cities |
| cities.city_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / cities |
| cities.latitude | 保留物理名称；存档没有恢复别名 | REAL | schema / cities |
| cities.longitude | 保留物理名称；存档没有恢复别名 | REAL | schema / cities |
| cities.country_code_2 | 保留物理名称；存档没有恢复别名 | TEXT | schema / cities |
| cities.capital | 保留物理名称；存档没有恢复别名 | INTEGER | schema / cities |
| cities.population | 保留物理名称；存档没有恢复别名 | REAL | schema / cities |
| cities.insert_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / cities |

## cities_countries

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: cc

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cities_countries.country_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / cities_countries |
| cities_countries.country_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / cities_countries |
| cities_countries.country_code_2 | 保留物理名称；存档没有恢复别名 | TEXT | schema / cities_countries |
| cities_countries.country_code_3 | 保留物理名称；存档没有恢复别名 | TEXT | schema / cities_countries |
| cities_countries.region | 保留物理名称；存档没有恢复别名 | TEXT | schema / cities_countries |
| cities_countries.sub_region | 保留物理名称；存档没有恢复别名 | TEXT | schema / cities_countries |
| cities_countries.intermediate_region | 保留物理名称；存档没有恢复别名 | TEXT | schema / cities_countries |
| cities_countries.created_on | 保留物理名称；存档没有恢复别名 | TEXT | schema / cities_countries |

## cities_currencies

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cities_currencies.currency_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / cities_currencies |
| cities_currencies.country_code_2 | 保留物理名称；存档没有恢复别名 | TEXT | schema / cities_currencies |
| cities_currencies.currency_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / cities_currencies |
| cities_currencies.currency_code | 保留物理名称；存档没有恢复别名 | TEXT | schema / cities_currencies |

## cities_languages

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cities_languages.language_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / cities_languages |
| cities_languages.language | 保留物理名称；存档没有恢复别名 | TEXT | schema / cities_languages |
| cities_languages.country_code_2 | 保留物理名称；存档没有恢复别名 | TEXT | schema / cities_languages |

## job_company

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| job_company.company_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / job_company |
| job_company.name | 保留物理名称；存档没有恢复别名 | TEXT | schema / job_company |
| job_company.link | 保留物理名称；存档没有恢复别名 | TEXT | schema / job_company |
| job_company.link_google | 保留物理名称；存档没有恢复别名 | TEXT | schema / job_company |
| job_company.thumbnail | 保留物理名称；存档没有恢复别名 | TEXT | schema / job_company |

## job_postings_fact

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| job_postings_fact.job_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / job_postings_fact |
| job_postings_fact.company_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / job_postings_fact |
| job_postings_fact.job_title_short | 保留物理名称；存档没有恢复别名 | TEXT | schema / job_postings_fact |
| job_postings_fact.job_title | 保留物理名称；存档没有恢复别名 | TEXT | schema / job_postings_fact |
| job_postings_fact.job_location | 保留物理名称；存档没有恢复别名 | TEXT | schema / job_postings_fact |
| job_postings_fact.job_via | 保留物理名称；存档没有恢复别名 | TEXT | schema / job_postings_fact |
| job_postings_fact.job_schedule_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / job_postings_fact |
| job_postings_fact.job_work_from_home | 保留物理名称；存档没有恢复别名 | INTEGER | schema / job_postings_fact |
| job_postings_fact.search_location | 保留物理名称；存档没有恢复别名 | TEXT | schema / job_postings_fact |
| job_postings_fact.job_posted_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / job_postings_fact |
| job_postings_fact.job_no_degree_mention | 保留物理名称；存档没有恢复别名 | INTEGER | schema / job_postings_fact |
| job_postings_fact.job_health_insurance | 保留物理名称；存档没有恢复别名 | INTEGER | schema / job_postings_fact |
| job_postings_fact.job_country | 保留物理名称；存档没有恢复别名 | TEXT | schema / job_postings_fact |
| job_postings_fact.salary_rate | 保留物理名称；存档没有恢复别名 | TEXT | schema / job_postings_fact |
| job_postings_fact.salary_year_avg | 保留物理名称；存档没有恢复别名 | REAL | schema / job_postings_fact |
| job_postings_fact.salary_hour_avg | 保留物理名称；存档没有恢复别名 | REAL | schema / job_postings_fact |

## legislation_date_dim

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: d

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| legislation_date_dim.date | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislation_date_dim |
| legislation_date_dim.month_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislation_date_dim |
| legislation_date_dim.day_of_month | 保留物理名称；存档没有恢复别名 | INTEGER | schema / legislation_date_dim |

## legislators

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: l

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| legislators.full_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |
| legislators.first_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |
| legislators.last_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |
| legislators.middle_name | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |
| legislators.nickname | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |
| legislators.suffix | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |
| legislators.other_names_end | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |
| legislators.other_names_middle | 保留物理名称；存档没有恢复别名 | REAL | schema / legislators |
| legislators.other_names_last | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |
| legislators.birthday | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |
| legislators.gender | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |
| legislators.id_bioguide | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |
| legislators.id_bioguide_previous_0 | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |
| legislators.id_govtrack | 保留物理名称；存档没有恢复别名 | INTEGER | schema / legislators |
| legislators.id_icpsr | 保留物理名称；存档没有恢复别名 | REAL | schema / legislators |
| legislators.id_wikipedia | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |
| legislators.id_wikidata | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |
| legislators.id_google_entity_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |
| legislators.id_house_history | 保留物理名称；存档没有恢复别名 | REAL | schema / legislators |
| legislators.id_house_history_alternate | 保留物理名称；存档没有恢复别名 | REAL | schema / legislators |
| legislators.id_thomas | 保留物理名称；存档没有恢复别名 | REAL | schema / legislators |
| legislators.id_cspan | 保留物理名称；存档没有恢复别名 | REAL | schema / legislators |
| legislators.id_votesmart | 保留物理名称；存档没有恢复别名 | REAL | schema / legislators |
| legislators.id_lis | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |
| legislators.id_ballotpedia | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |
| legislators.id_opensecrets | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |
| legislators.id_fec_0 | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |
| legislators.id_fec_1 | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |
| legislators.id_fec_2 | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators |

## legislators_terms

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: t

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| legislators_terms.id_bioguide | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators_terms |
| legislators_terms.term_number | 保留物理名称；存档没有恢复别名 | INTEGER | schema / legislators_terms |
| legislators_terms.term_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators_terms |
| legislators_terms.term_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators_terms |
| legislators_terms.term_start | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators_terms |
| legislators_terms.term_end | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators_terms |
| legislators_terms.state | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators_terms |
| legislators_terms.district | 保留物理名称；存档没有恢复别名 | REAL | schema / legislators_terms |
| legislators_terms.class | 保留物理名称；存档没有恢复别名 | REAL | schema / legislators_terms |
| legislators_terms.party | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators_terms |
| legislators_terms.how | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators_terms |
| legislators_terms.url | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators_terms |
| legislators_terms.address | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators_terms |
| legislators_terms.phone | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators_terms |
| legislators_terms.fax | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators_terms |
| legislators_terms.contact_form | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators_terms |
| legislators_terms.office | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators_terms |
| legislators_terms.state_rank | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators_terms |
| legislators_terms.rss_url | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators_terms |
| legislators_terms.caucus | 保留物理名称；存档没有恢复别名 | TEXT | schema / legislators_terms |

## skills_dim

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: s

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| skills_dim.skill_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / skills_dim |
| skills_dim.skills | 保留物理名称；存档没有恢复别名 | TEXT | schema / skills_dim |
| skills_dim.type | 保留物理名称；存档没有恢复别名 | TEXT | schema / skills_dim |

## skills_job_dim

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: sj

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| skills_job_dim.job_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / skills_job_dim |
| skills_job_dim.skill_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / skills_job_dim |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

