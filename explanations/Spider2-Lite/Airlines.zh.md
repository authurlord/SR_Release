# Spider2-Lite / Airlines — Schema 与业务口径解释

该数据库的存档目录包含 8 张表、35 个物理列、0 条关系，以及 8 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## aircrafts_data

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| aircrafts_data.aircraft_code | 保留物理名称；存档没有恢复别名 | character(3) | schema / aircrafts_data |
| aircrafts_data.model | 保留物理名称；存档没有恢复别名 | jsonb | schema / aircrafts_data |
| aircrafts_data.range | 保留物理名称；存档没有恢复别名 | INTEGER | schema / aircrafts_data |

## airports_data

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| airports_data.airport_code | 保留物理名称；存档没有恢复别名 | character(3) | schema / airports_data |
| airports_data.airport_name | 保留物理名称；存档没有恢复别名 | jsonb | schema / airports_data |
| airports_data.city | 保留物理名称；存档没有恢复别名 | jsonb | schema / airports_data |
| airports_data.coordinates | 保留物理名称；存档没有恢复别名 | point | schema / airports_data |
| airports_data.timezone | 保留物理名称；存档没有恢复别名 | TEXT | schema / airports_data |

## boarding_passes

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| boarding_passes.ticket_no | 保留物理名称；存档没有恢复别名 | character(13) | schema / boarding_passes |
| boarding_passes.flight_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / boarding_passes |
| boarding_passes.boarding_no | 保留物理名称；存档没有恢复别名 | INTEGER | schema / boarding_passes |
| boarding_passes.seat_no | 保留物理名称；存档没有恢复别名 | character varying(4) | schema / boarding_passes |

## bookings

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| bookings.book_ref | 保留物理名称；存档没有恢复别名 | character(6) | schema / bookings |
| bookings.book_date | 保留物理名称；存档没有恢复别名 | timestamp with time zone | schema / bookings |
| bookings.total_amount | 保留物理名称；存档没有恢复别名 | numeric(10,2) | schema / bookings |

## flights

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: f

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| flights.flight_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / flights |
| flights.flight_no | 保留物理名称；存档没有恢复别名 | character(6) | schema / flights |
| flights.scheduled_departure | 保留物理名称；存档没有恢复别名 | timestamp with time zone | schema / flights |
| flights.scheduled_arrival | 保留物理名称；存档没有恢复别名 | timestamp with time zone | schema / flights |
| flights.departure_airport | 保留物理名称；存档没有恢复别名 | character(3) | schema / flights |
| flights.arrival_airport | 保留物理名称；存档没有恢复别名 | character(3) | schema / flights |
| flights.status | 保留物理名称；存档没有恢复别名 | character varying(20) | schema / flights |
| flights.aircraft_code | 保留物理名称；存档没有恢复别名 | character(3) | schema / flights |
| flights.actual_departure | 保留物理名称；存档没有恢复别名 | timestamp with time zone | schema / flights |
| flights.actual_arrival | 保留物理名称；存档没有恢复别名 | timestamp with time zone | schema / flights |

## seats

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| seats.aircraft_code | 保留物理名称；存档没有恢复别名 | character(3) | schema / seats |
| seats.seat_no | 保留物理名称；存档没有恢复别名 | character varying(4) | schema / seats |
| seats.fare_conditions | 保留物理名称；存档没有恢复别名 | character varying(10) | schema / seats |

## ticket_flights

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ticket_flights.ticket_no | 保留物理名称；存档没有恢复别名 | character(13) | schema / ticket_flights |
| ticket_flights.flight_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / ticket_flights |
| ticket_flights.fare_conditions | 保留物理名称；存档没有恢复别名 | character varying(10) | schema / ticket_flights |
| ticket_flights.amount | 保留物理名称；存档没有恢复别名 | numeric(10,2) | schema / ticket_flights |

## tickets

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| tickets.ticket_no | 保留物理名称；存档没有恢复别名 | character(13) | schema / tickets |
| tickets.book_ref | 保留物理名称；存档没有恢复别名 | character(6) | schema / tickets |
| tickets.passenger_id | 保留物理名称；存档没有恢复别名 | character varying(20) | schema / tickets |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

