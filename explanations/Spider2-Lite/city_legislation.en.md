# Spider2-Lite / city_legislation — Schema and business semantics

The saved catalogue for this database contains 15 tables, 133 physical columns, 0 relationships and 15 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## alien_data

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| alien_data.id | Physical name retained; no saved recovered alias | INTEGER | schema / alien_data |
| alien_data.first_name | Physical name retained; no saved recovered alias | TEXT | schema / alien_data |
| alien_data.last_name | Physical name retained; no saved recovered alias | TEXT | schema / alien_data |
| alien_data.email | Physical name retained; no saved recovered alias | TEXT | schema / alien_data |
| alien_data.gender | Physical name retained; no saved recovered alias | TEXT | schema / alien_data |
| alien_data.type | Physical name retained; no saved recovered alias | TEXT | schema / alien_data |
| alien_data.birth_year | Physical name retained; no saved recovered alias | INTEGER | schema / alien_data |
| alien_data.age | Physical name retained; no saved recovered alias | INTEGER | schema / alien_data |
| alien_data.favorite_food | Physical name retained; no saved recovered alias | TEXT | schema / alien_data |
| alien_data.feeding_frequency | Physical name retained; no saved recovered alias | TEXT | schema / alien_data |
| alien_data.aggressive | Physical name retained; no saved recovered alias | INTEGER | schema / alien_data |
| alien_data.occupation | Physical name retained; no saved recovered alias | TEXT | schema / alien_data |
| alien_data.current_location | Physical name retained; no saved recovered alias | TEXT | schema / alien_data |
| alien_data.state | Physical name retained; no saved recovered alias | TEXT | schema / alien_data |
| alien_data.us_region | Physical name retained; no saved recovered alias | TEXT | schema / alien_data |
| alien_data.country | Physical name retained; no saved recovered alias | TEXT | schema / alien_data |

## aliens

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| aliens.id | Physical name retained; no saved recovered alias | INTEGER | schema / aliens |
| aliens.first_name | Physical name retained; no saved recovered alias | TEXT | schema / aliens |
| aliens.last_name | Physical name retained; no saved recovered alias | TEXT | schema / aliens |
| aliens.email | Physical name retained; no saved recovered alias | TEXT | schema / aliens |
| aliens.gender | Physical name retained; no saved recovered alias | TEXT | schema / aliens |
| aliens.type | Physical name retained; no saved recovered alias | TEXT | schema / aliens |
| aliens.birth_year | Physical name retained; no saved recovered alias | INTEGER | schema / aliens |

## aliens_details

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| aliens_details.detail_id | Physical name retained; no saved recovered alias | INTEGER | schema / aliens_details |
| aliens_details.favorite_food | Physical name retained; no saved recovered alias | TEXT | schema / aliens_details |
| aliens_details.feeding_frequency | Physical name retained; no saved recovered alias | TEXT | schema / aliens_details |
| aliens_details.aggressive | Physical name retained; no saved recovered alias | INTEGER | schema / aliens_details |

## aliens_location

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| aliens_location.loc_id | Physical name retained; no saved recovered alias | INTEGER | schema / aliens_location |
| aliens_location.current_location | Physical name retained; no saved recovered alias | TEXT | schema / aliens_location |
| aliens_location.state | Physical name retained; no saved recovered alias | TEXT | schema / aliens_location |
| aliens_location.country | Physical name retained; no saved recovered alias | TEXT | schema / aliens_location |
| aliens_location.occupation | Physical name retained; no saved recovered alias | TEXT | schema / aliens_location |

## cities

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: c

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| cities.city_id | Physical name retained; no saved recovered alias | INTEGER | schema / cities |
| cities.city_name | Physical name retained; no saved recovered alias | TEXT | schema / cities |
| cities.latitude | Physical name retained; no saved recovered alias | REAL | schema / cities |
| cities.longitude | Physical name retained; no saved recovered alias | REAL | schema / cities |
| cities.country_code_2 | Physical name retained; no saved recovered alias | TEXT | schema / cities |
| cities.capital | Physical name retained; no saved recovered alias | INTEGER | schema / cities |
| cities.population | Physical name retained; no saved recovered alias | REAL | schema / cities |
| cities.insert_date | Physical name retained; no saved recovered alias | TEXT | schema / cities |

## cities_countries

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: cc

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| cities_countries.country_id | Physical name retained; no saved recovered alias | INTEGER | schema / cities_countries |
| cities_countries.country_name | Physical name retained; no saved recovered alias | TEXT | schema / cities_countries |
| cities_countries.country_code_2 | Physical name retained; no saved recovered alias | TEXT | schema / cities_countries |
| cities_countries.country_code_3 | Physical name retained; no saved recovered alias | TEXT | schema / cities_countries |
| cities_countries.region | Physical name retained; no saved recovered alias | TEXT | schema / cities_countries |
| cities_countries.sub_region | Physical name retained; no saved recovered alias | TEXT | schema / cities_countries |
| cities_countries.intermediate_region | Physical name retained; no saved recovered alias | TEXT | schema / cities_countries |
| cities_countries.created_on | Physical name retained; no saved recovered alias | TEXT | schema / cities_countries |

## cities_currencies

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| cities_currencies.currency_id | Physical name retained; no saved recovered alias | INTEGER | schema / cities_currencies |
| cities_currencies.country_code_2 | Physical name retained; no saved recovered alias | TEXT | schema / cities_currencies |
| cities_currencies.currency_name | Physical name retained; no saved recovered alias | TEXT | schema / cities_currencies |
| cities_currencies.currency_code | Physical name retained; no saved recovered alias | TEXT | schema / cities_currencies |

## cities_languages

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| cities_languages.language_id | Physical name retained; no saved recovered alias | INTEGER | schema / cities_languages |
| cities_languages.language | Physical name retained; no saved recovered alias | TEXT | schema / cities_languages |
| cities_languages.country_code_2 | Physical name retained; no saved recovered alias | TEXT | schema / cities_languages |

## job_company

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| job_company.company_id | Physical name retained; no saved recovered alias | INTEGER | schema / job_company |
| job_company.name | Physical name retained; no saved recovered alias | TEXT | schema / job_company |
| job_company.link | Physical name retained; no saved recovered alias | TEXT | schema / job_company |
| job_company.link_google | Physical name retained; no saved recovered alias | TEXT | schema / job_company |
| job_company.thumbnail | Physical name retained; no saved recovered alias | TEXT | schema / job_company |

## job_postings_fact

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| job_postings_fact.job_id | Physical name retained; no saved recovered alias | INTEGER | schema / job_postings_fact |
| job_postings_fact.company_id | Physical name retained; no saved recovered alias | INTEGER | schema / job_postings_fact |
| job_postings_fact.job_title_short | Physical name retained; no saved recovered alias | TEXT | schema / job_postings_fact |
| job_postings_fact.job_title | Physical name retained; no saved recovered alias | TEXT | schema / job_postings_fact |
| job_postings_fact.job_location | Physical name retained; no saved recovered alias | TEXT | schema / job_postings_fact |
| job_postings_fact.job_via | Physical name retained; no saved recovered alias | TEXT | schema / job_postings_fact |
| job_postings_fact.job_schedule_type | Physical name retained; no saved recovered alias | TEXT | schema / job_postings_fact |
| job_postings_fact.job_work_from_home | Physical name retained; no saved recovered alias | INTEGER | schema / job_postings_fact |
| job_postings_fact.search_location | Physical name retained; no saved recovered alias | TEXT | schema / job_postings_fact |
| job_postings_fact.job_posted_date | Physical name retained; no saved recovered alias | TEXT | schema / job_postings_fact |
| job_postings_fact.job_no_degree_mention | Physical name retained; no saved recovered alias | INTEGER | schema / job_postings_fact |
| job_postings_fact.job_health_insurance | Physical name retained; no saved recovered alias | INTEGER | schema / job_postings_fact |
| job_postings_fact.job_country | Physical name retained; no saved recovered alias | TEXT | schema / job_postings_fact |
| job_postings_fact.salary_rate | Physical name retained; no saved recovered alias | TEXT | schema / job_postings_fact |
| job_postings_fact.salary_year_avg | Physical name retained; no saved recovered alias | REAL | schema / job_postings_fact |
| job_postings_fact.salary_hour_avg | Physical name retained; no saved recovered alias | REAL | schema / job_postings_fact |

## legislation_date_dim

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: d

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| legislation_date_dim.date | Physical name retained; no saved recovered alias | TEXT | schema / legislation_date_dim |
| legislation_date_dim.month_name | Physical name retained; no saved recovered alias | TEXT | schema / legislation_date_dim |
| legislation_date_dim.day_of_month | Physical name retained; no saved recovered alias | INTEGER | schema / legislation_date_dim |

## legislators

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: l

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| legislators.full_name | Physical name retained; no saved recovered alias | TEXT | schema / legislators |
| legislators.first_name | Physical name retained; no saved recovered alias | TEXT | schema / legislators |
| legislators.last_name | Physical name retained; no saved recovered alias | TEXT | schema / legislators |
| legislators.middle_name | Physical name retained; no saved recovered alias | TEXT | schema / legislators |
| legislators.nickname | Physical name retained; no saved recovered alias | TEXT | schema / legislators |
| legislators.suffix | Physical name retained; no saved recovered alias | TEXT | schema / legislators |
| legislators.other_names_end | Physical name retained; no saved recovered alias | TEXT | schema / legislators |
| legislators.other_names_middle | Physical name retained; no saved recovered alias | REAL | schema / legislators |
| legislators.other_names_last | Physical name retained; no saved recovered alias | TEXT | schema / legislators |
| legislators.birthday | Physical name retained; no saved recovered alias | TEXT | schema / legislators |
| legislators.gender | Physical name retained; no saved recovered alias | TEXT | schema / legislators |
| legislators.id_bioguide | Physical name retained; no saved recovered alias | TEXT | schema / legislators |
| legislators.id_bioguide_previous_0 | Physical name retained; no saved recovered alias | TEXT | schema / legislators |
| legislators.id_govtrack | Physical name retained; no saved recovered alias | INTEGER | schema / legislators |
| legislators.id_icpsr | Physical name retained; no saved recovered alias | REAL | schema / legislators |
| legislators.id_wikipedia | Physical name retained; no saved recovered alias | TEXT | schema / legislators |
| legislators.id_wikidata | Physical name retained; no saved recovered alias | TEXT | schema / legislators |
| legislators.id_google_entity_id | Physical name retained; no saved recovered alias | TEXT | schema / legislators |
| legislators.id_house_history | Physical name retained; no saved recovered alias | REAL | schema / legislators |
| legislators.id_house_history_alternate | Physical name retained; no saved recovered alias | REAL | schema / legislators |
| legislators.id_thomas | Physical name retained; no saved recovered alias | REAL | schema / legislators |
| legislators.id_cspan | Physical name retained; no saved recovered alias | REAL | schema / legislators |
| legislators.id_votesmart | Physical name retained; no saved recovered alias | REAL | schema / legislators |
| legislators.id_lis | Physical name retained; no saved recovered alias | TEXT | schema / legislators |
| legislators.id_ballotpedia | Physical name retained; no saved recovered alias | TEXT | schema / legislators |
| legislators.id_opensecrets | Physical name retained; no saved recovered alias | TEXT | schema / legislators |
| legislators.id_fec_0 | Physical name retained; no saved recovered alias | TEXT | schema / legislators |
| legislators.id_fec_1 | Physical name retained; no saved recovered alias | TEXT | schema / legislators |
| legislators.id_fec_2 | Physical name retained; no saved recovered alias | TEXT | schema / legislators |

## legislators_terms

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: t

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| legislators_terms.id_bioguide | Physical name retained; no saved recovered alias | TEXT | schema / legislators_terms |
| legislators_terms.term_number | Physical name retained; no saved recovered alias | INTEGER | schema / legislators_terms |
| legislators_terms.term_id | Physical name retained; no saved recovered alias | TEXT | schema / legislators_terms |
| legislators_terms.term_type | Physical name retained; no saved recovered alias | TEXT | schema / legislators_terms |
| legislators_terms.term_start | Physical name retained; no saved recovered alias | TEXT | schema / legislators_terms |
| legislators_terms.term_end | Physical name retained; no saved recovered alias | TEXT | schema / legislators_terms |
| legislators_terms.state | Physical name retained; no saved recovered alias | TEXT | schema / legislators_terms |
| legislators_terms.district | Physical name retained; no saved recovered alias | REAL | schema / legislators_terms |
| legislators_terms.class | Physical name retained; no saved recovered alias | REAL | schema / legislators_terms |
| legislators_terms.party | Physical name retained; no saved recovered alias | TEXT | schema / legislators_terms |
| legislators_terms.how | Physical name retained; no saved recovered alias | TEXT | schema / legislators_terms |
| legislators_terms.url | Physical name retained; no saved recovered alias | TEXT | schema / legislators_terms |
| legislators_terms.address | Physical name retained; no saved recovered alias | TEXT | schema / legislators_terms |
| legislators_terms.phone | Physical name retained; no saved recovered alias | TEXT | schema / legislators_terms |
| legislators_terms.fax | Physical name retained; no saved recovered alias | TEXT | schema / legislators_terms |
| legislators_terms.contact_form | Physical name retained; no saved recovered alias | TEXT | schema / legislators_terms |
| legislators_terms.office | Physical name retained; no saved recovered alias | TEXT | schema / legislators_terms |
| legislators_terms.state_rank | Physical name retained; no saved recovered alias | TEXT | schema / legislators_terms |
| legislators_terms.rss_url | Physical name retained; no saved recovered alias | TEXT | schema / legislators_terms |
| legislators_terms.caucus | Physical name retained; no saved recovered alias | TEXT | schema / legislators_terms |

## skills_dim

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: s

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| skills_dim.skill_id | Physical name retained; no saved recovered alias | INTEGER | schema / skills_dim |
| skills_dim.skills | Physical name retained; no saved recovered alias | TEXT | schema / skills_dim |
| skills_dim.type | Physical name retained; no saved recovered alias | TEXT | schema / skills_dim |

## skills_job_dim

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: sj

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| skills_job_dim.job_id | Physical name retained; no saved recovered alias | INTEGER | schema / skills_job_dim |
| skills_job_dim.skill_id | Physical name retained; no saved recovered alias | INTEGER | schema / skills_job_dim |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

