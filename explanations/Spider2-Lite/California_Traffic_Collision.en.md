# Spider2-Lite / California_Traffic_Collision — Schema and business semantics

The saved catalogue for this database contains 4 tables, 120 physical columns, 0 relationships and 4 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## case_ids

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: c, ci

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| case_ids.case_id | Physical name retained; no saved recovered alias | REAL | schema / case_ids |
| case_ids.db_year | Physical name retained; no saved recovered alias | INTEGER | schema / case_ids |

## collisions

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: c, col

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| collisions.case_id | Physical name retained; no saved recovered alias | REAL | schema / collisions |
| collisions.jurisdiction | Physical name retained; no saved recovered alias | REAL | schema / collisions |
| collisions.officer_id | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.reporting_district | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.chp_shift | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.population | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.county_city_location | Physical name retained; no saved recovered alias | INTEGER | schema / collisions |
| collisions.county_location | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.special_condition | Physical name retained; no saved recovered alias | REAL | schema / collisions |
| collisions.beat_type | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.chp_beat_type | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.city_division_lapd | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.chp_beat_class | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.beat_number | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.primary_road | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.secondary_road | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.distance | Physical name retained; no saved recovered alias | REAL | schema / collisions |
| collisions.direction | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.intersection | Physical name retained; no saved recovered alias | REAL | schema / collisions |
| collisions.weather_1 | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.weather_2 | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.state_highway_indicator | Physical name retained; no saved recovered alias | REAL | schema / collisions |
| collisions.caltrans_county | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.caltrans_district | Physical name retained; no saved recovered alias | REAL | schema / collisions |
| collisions.state_route | Physical name retained; no saved recovered alias | REAL | schema / collisions |
| collisions.route_suffix | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.postmile_prefix | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.postmile | Physical name retained; no saved recovered alias | REAL | schema / collisions |
| collisions.location_type | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.ramp_intersection | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.side_of_highway | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.tow_away | Physical name retained; no saved recovered alias | REAL | schema / collisions |
| collisions.collision_severity | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.killed_victims | Physical name retained; no saved recovered alias | REAL | schema / collisions |
| collisions.injured_victims | Physical name retained; no saved recovered alias | REAL | schema / collisions |
| collisions.party_count | Physical name retained; no saved recovered alias | REAL | schema / collisions |
| collisions.primary_collision_factor | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.pcf_violation_code | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.pcf_violation_category | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.pcf_violation | Physical name retained; no saved recovered alias | REAL | schema / collisions |
| collisions.pcf_violation_subsection | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.hit_and_run | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.type_of_collision | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.motor_vehicle_involved_with | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.pedestrian_action | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.road_surface | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.road_condition_1 | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.road_condition_2 | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.lighting | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.control_device | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.chp_road_type | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.pedestrian_collision | Physical name retained; no saved recovered alias | INTEGER | schema / collisions |
| collisions.bicycle_collision | Physical name retained; no saved recovered alias | INTEGER | schema / collisions |
| collisions.motorcycle_collision | Physical name retained; no saved recovered alias | INTEGER | schema / collisions |
| collisions.truck_collision | Physical name retained; no saved recovered alias | INTEGER | schema / collisions |
| collisions.not_private_property | Physical name retained; no saved recovered alias | REAL | schema / collisions |
| collisions.alcohol_involved | Physical name retained; no saved recovered alias | REAL | schema / collisions |
| collisions.statewide_vehicle_type_at_fault | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.chp_vehicle_type_at_fault | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.severe_injury_count | Physical name retained; no saved recovered alias | INTEGER | schema / collisions |
| collisions.other_visible_injury_count | Physical name retained; no saved recovered alias | INTEGER | schema / collisions |
| collisions.complaint_of_pain_injury_count | Physical name retained; no saved recovered alias | INTEGER | schema / collisions |
| collisions.pedestrian_killed_count | Physical name retained; no saved recovered alias | INTEGER | schema / collisions |
| collisions.pedestrian_injured_count | Physical name retained; no saved recovered alias | INTEGER | schema / collisions |
| collisions.bicyclist_killed_count | Physical name retained; no saved recovered alias | INTEGER | schema / collisions |
| collisions.bicyclist_injured_count | Physical name retained; no saved recovered alias | INTEGER | schema / collisions |
| collisions.motorcyclist_killed_count | Physical name retained; no saved recovered alias | INTEGER | schema / collisions |
| collisions.motorcyclist_injured_count | Physical name retained; no saved recovered alias | REAL | schema / collisions |
| collisions.primary_ramp | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.secondary_ramp | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.latitude | Physical name retained; no saved recovered alias | REAL | schema / collisions |
| collisions.longitude | Physical name retained; no saved recovered alias | REAL | schema / collisions |
| collisions.collision_date | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.collision_time | Physical name retained; no saved recovered alias | TEXT | schema / collisions |
| collisions.process_date | Physical name retained; no saved recovered alias | TEXT | schema / collisions |

## parties

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: p

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| parties.id | Physical name retained; no saved recovered alias | INTEGER | schema / parties |
| parties.case_id | Physical name retained; no saved recovered alias | REAL | schema / parties |
| parties.party_number | Physical name retained; no saved recovered alias | INTEGER | schema / parties |
| parties.party_type | Physical name retained; no saved recovered alias | TEXT | schema / parties |
| parties.at_fault | Physical name retained; no saved recovered alias | INTEGER | schema / parties |
| parties.party_sex | Physical name retained; no saved recovered alias | TEXT | schema / parties |
| parties.party_age | Physical name retained; no saved recovered alias | REAL | schema / parties |
| parties.party_sobriety | Physical name retained; no saved recovered alias | TEXT | schema / parties |
| parties.party_drug_physical | Physical name retained; no saved recovered alias | TEXT | schema / parties |
| parties.direction_of_travel | Physical name retained; no saved recovered alias | TEXT | schema / parties |
| parties.party_safety_equipment_1 | Physical name retained; no saved recovered alias | TEXT | schema / parties |
| parties.party_safety_equipment_2 | Physical name retained; no saved recovered alias | TEXT | schema / parties |
| parties.financial_responsibility | Physical name retained; no saved recovered alias | TEXT | schema / parties |
| parties.hazardous_materials | Physical name retained; no saved recovered alias | REAL | schema / parties |
| parties.cellphone_in_use | Physical name retained; no saved recovered alias | REAL | schema / parties |
| parties.cellphone_use_type | Physical name retained; no saved recovered alias | TEXT | schema / parties |
| parties.school_bus_related | Physical name retained; no saved recovered alias | REAL | schema / parties |
| parties.oaf_violation_code | Physical name retained; no saved recovered alias | TEXT | schema / parties |
| parties.oaf_violation_category | Physical name retained; no saved recovered alias | TEXT | schema / parties |
| parties.oaf_violation_section | Physical name retained; no saved recovered alias | REAL | schema / parties |
| parties.oaf_violation_suffix | Physical name retained; no saved recovered alias | TEXT | schema / parties |
| parties.other_associate_factor_1 | Physical name retained; no saved recovered alias | TEXT | schema / parties |
| parties.other_associate_factor_2 | Physical name retained; no saved recovered alias | TEXT | schema / parties |
| parties.party_number_killed | Physical name retained; no saved recovered alias | INTEGER | schema / parties |
| parties.party_number_injured | Physical name retained; no saved recovered alias | INTEGER | schema / parties |
| parties.movement_preceding_collision | Physical name retained; no saved recovered alias | TEXT | schema / parties |
| parties.vehicle_year | Physical name retained; no saved recovered alias | REAL | schema / parties |
| parties.vehicle_make | Physical name retained; no saved recovered alias | TEXT | schema / parties |
| parties.statewide_vehicle_type | Physical name retained; no saved recovered alias | TEXT | schema / parties |
| parties.chp_vehicle_type_towing | Physical name retained; no saved recovered alias | TEXT | schema / parties |
| parties.chp_vehicle_type_towed | Physical name retained; no saved recovered alias | TEXT | schema / parties |
| parties.party_race | Physical name retained; no saved recovered alias | TEXT | schema / parties |

## victims

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| victims.id | Physical name retained; no saved recovered alias | INTEGER | schema / victims |
| victims.case_id | Physical name retained; no saved recovered alias | REAL | schema / victims |
| victims.party_number | Physical name retained; no saved recovered alias | INTEGER | schema / victims |
| victims.victim_role | Physical name retained; no saved recovered alias | TEXT | schema / victims |
| victims.victim_sex | Physical name retained; no saved recovered alias | TEXT | schema / victims |
| victims.victim_age | Physical name retained; no saved recovered alias | REAL | schema / victims |
| victims.victim_degree_of_injury | Physical name retained; no saved recovered alias | TEXT | schema / victims |
| victims.victim_seating_position | Physical name retained; no saved recovered alias | TEXT | schema / victims |
| victims.victim_safety_equipment_1 | Physical name retained; no saved recovered alias | TEXT | schema / victims |
| victims.victim_safety_equipment_2 | Physical name retained; no saved recovered alias | TEXT | schema / victims |
| victims.victim_ejected | Physical name retained; no saved recovered alias | TEXT | schema / victims |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

