# Spider2-Lite / California_Traffic_Collision — Schema 与业务口径解释

该数据库的存档目录包含 4 张表、120 个物理列、0 条关系，以及 4 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## case_ids

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: c, ci

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| case_ids.case_id | 保留物理名称；存档没有恢复别名 | REAL | schema / case_ids |
| case_ids.db_year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / case_ids |

## collisions

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: c, col

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| collisions.case_id | 保留物理名称；存档没有恢复别名 | REAL | schema / collisions |
| collisions.jurisdiction | 保留物理名称；存档没有恢复别名 | REAL | schema / collisions |
| collisions.officer_id | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.reporting_district | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.chp_shift | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.population | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.county_city_location | 保留物理名称；存档没有恢复别名 | INTEGER | schema / collisions |
| collisions.county_location | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.special_condition | 保留物理名称；存档没有恢复别名 | REAL | schema / collisions |
| collisions.beat_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.chp_beat_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.city_division_lapd | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.chp_beat_class | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.beat_number | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.primary_road | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.secondary_road | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.distance | 保留物理名称；存档没有恢复别名 | REAL | schema / collisions |
| collisions.direction | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.intersection | 保留物理名称；存档没有恢复别名 | REAL | schema / collisions |
| collisions.weather_1 | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.weather_2 | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.state_highway_indicator | 保留物理名称；存档没有恢复别名 | REAL | schema / collisions |
| collisions.caltrans_county | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.caltrans_district | 保留物理名称；存档没有恢复别名 | REAL | schema / collisions |
| collisions.state_route | 保留物理名称；存档没有恢复别名 | REAL | schema / collisions |
| collisions.route_suffix | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.postmile_prefix | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.postmile | 保留物理名称；存档没有恢复别名 | REAL | schema / collisions |
| collisions.location_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.ramp_intersection | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.side_of_highway | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.tow_away | 保留物理名称；存档没有恢复别名 | REAL | schema / collisions |
| collisions.collision_severity | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.killed_victims | 保留物理名称；存档没有恢复别名 | REAL | schema / collisions |
| collisions.injured_victims | 保留物理名称；存档没有恢复别名 | REAL | schema / collisions |
| collisions.party_count | 保留物理名称；存档没有恢复别名 | REAL | schema / collisions |
| collisions.primary_collision_factor | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.pcf_violation_code | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.pcf_violation_category | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.pcf_violation | 保留物理名称；存档没有恢复别名 | REAL | schema / collisions |
| collisions.pcf_violation_subsection | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.hit_and_run | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.type_of_collision | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.motor_vehicle_involved_with | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.pedestrian_action | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.road_surface | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.road_condition_1 | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.road_condition_2 | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.lighting | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.control_device | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.chp_road_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.pedestrian_collision | 保留物理名称；存档没有恢复别名 | INTEGER | schema / collisions |
| collisions.bicycle_collision | 保留物理名称；存档没有恢复别名 | INTEGER | schema / collisions |
| collisions.motorcycle_collision | 保留物理名称；存档没有恢复别名 | INTEGER | schema / collisions |
| collisions.truck_collision | 保留物理名称；存档没有恢复别名 | INTEGER | schema / collisions |
| collisions.not_private_property | 保留物理名称；存档没有恢复别名 | REAL | schema / collisions |
| collisions.alcohol_involved | 保留物理名称；存档没有恢复别名 | REAL | schema / collisions |
| collisions.statewide_vehicle_type_at_fault | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.chp_vehicle_type_at_fault | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.severe_injury_count | 保留物理名称；存档没有恢复别名 | INTEGER | schema / collisions |
| collisions.other_visible_injury_count | 保留物理名称；存档没有恢复别名 | INTEGER | schema / collisions |
| collisions.complaint_of_pain_injury_count | 保留物理名称；存档没有恢复别名 | INTEGER | schema / collisions |
| collisions.pedestrian_killed_count | 保留物理名称；存档没有恢复别名 | INTEGER | schema / collisions |
| collisions.pedestrian_injured_count | 保留物理名称；存档没有恢复别名 | INTEGER | schema / collisions |
| collisions.bicyclist_killed_count | 保留物理名称；存档没有恢复别名 | INTEGER | schema / collisions |
| collisions.bicyclist_injured_count | 保留物理名称；存档没有恢复别名 | INTEGER | schema / collisions |
| collisions.motorcyclist_killed_count | 保留物理名称；存档没有恢复别名 | INTEGER | schema / collisions |
| collisions.motorcyclist_injured_count | 保留物理名称；存档没有恢复别名 | REAL | schema / collisions |
| collisions.primary_ramp | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.secondary_ramp | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.latitude | 保留物理名称；存档没有恢复别名 | REAL | schema / collisions |
| collisions.longitude | 保留物理名称；存档没有恢复别名 | REAL | schema / collisions |
| collisions.collision_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.collision_time | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |
| collisions.process_date | 保留物理名称；存档没有恢复别名 | TEXT | schema / collisions |

## parties

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: p

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| parties.id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / parties |
| parties.case_id | 保留物理名称；存档没有恢复别名 | REAL | schema / parties |
| parties.party_number | 保留物理名称；存档没有恢复别名 | INTEGER | schema / parties |
| parties.party_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / parties |
| parties.at_fault | 保留物理名称；存档没有恢复别名 | INTEGER | schema / parties |
| parties.party_sex | 保留物理名称；存档没有恢复别名 | TEXT | schema / parties |
| parties.party_age | 保留物理名称；存档没有恢复别名 | REAL | schema / parties |
| parties.party_sobriety | 保留物理名称；存档没有恢复别名 | TEXT | schema / parties |
| parties.party_drug_physical | 保留物理名称；存档没有恢复别名 | TEXT | schema / parties |
| parties.direction_of_travel | 保留物理名称；存档没有恢复别名 | TEXT | schema / parties |
| parties.party_safety_equipment_1 | 保留物理名称；存档没有恢复别名 | TEXT | schema / parties |
| parties.party_safety_equipment_2 | 保留物理名称；存档没有恢复别名 | TEXT | schema / parties |
| parties.financial_responsibility | 保留物理名称；存档没有恢复别名 | TEXT | schema / parties |
| parties.hazardous_materials | 保留物理名称；存档没有恢复别名 | REAL | schema / parties |
| parties.cellphone_in_use | 保留物理名称；存档没有恢复别名 | REAL | schema / parties |
| parties.cellphone_use_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / parties |
| parties.school_bus_related | 保留物理名称；存档没有恢复别名 | REAL | schema / parties |
| parties.oaf_violation_code | 保留物理名称；存档没有恢复别名 | TEXT | schema / parties |
| parties.oaf_violation_category | 保留物理名称；存档没有恢复别名 | TEXT | schema / parties |
| parties.oaf_violation_section | 保留物理名称；存档没有恢复别名 | REAL | schema / parties |
| parties.oaf_violation_suffix | 保留物理名称；存档没有恢复别名 | TEXT | schema / parties |
| parties.other_associate_factor_1 | 保留物理名称；存档没有恢复别名 | TEXT | schema / parties |
| parties.other_associate_factor_2 | 保留物理名称；存档没有恢复别名 | TEXT | schema / parties |
| parties.party_number_killed | 保留物理名称；存档没有恢复别名 | INTEGER | schema / parties |
| parties.party_number_injured | 保留物理名称；存档没有恢复别名 | INTEGER | schema / parties |
| parties.movement_preceding_collision | 保留物理名称；存档没有恢复别名 | TEXT | schema / parties |
| parties.vehicle_year | 保留物理名称；存档没有恢复别名 | REAL | schema / parties |
| parties.vehicle_make | 保留物理名称；存档没有恢复别名 | TEXT | schema / parties |
| parties.statewide_vehicle_type | 保留物理名称；存档没有恢复别名 | TEXT | schema / parties |
| parties.chp_vehicle_type_towing | 保留物理名称；存档没有恢复别名 | TEXT | schema / parties |
| parties.chp_vehicle_type_towed | 保留物理名称；存档没有恢复别名 | TEXT | schema / parties |
| parties.party_race | 保留物理名称；存档没有恢复别名 | TEXT | schema / parties |

## victims

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| victims.id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / victims |
| victims.case_id | 保留物理名称；存档没有恢复别名 | REAL | schema / victims |
| victims.party_number | 保留物理名称；存档没有恢复别名 | INTEGER | schema / victims |
| victims.victim_role | 保留物理名称；存档没有恢复别名 | TEXT | schema / victims |
| victims.victim_sex | 保留物理名称；存档没有恢复别名 | TEXT | schema / victims |
| victims.victim_age | 保留物理名称；存档没有恢复别名 | REAL | schema / victims |
| victims.victim_degree_of_injury | 保留物理名称；存档没有恢复别名 | TEXT | schema / victims |
| victims.victim_seating_position | 保留物理名称；存档没有恢复别名 | TEXT | schema / victims |
| victims.victim_safety_equipment_1 | 保留物理名称；存档没有恢复别名 | TEXT | schema / victims |
| victims.victim_safety_equipment_2 | 保留物理名称；存档没有恢复别名 | TEXT | schema / victims |
| victims.victim_ejected | 保留物理名称；存档没有恢复别名 | TEXT | schema / victims |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

