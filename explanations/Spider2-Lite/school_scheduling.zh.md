# Spider2-Lite / school_scheduling — Schema 与业务口径解释

该数据库的存档目录包含 15 张表、75 个物理列、0 条关系，以及 15 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## Buildings

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Buildings.BuildingCode | 保留物理名称；存档没有恢复别名 | TEXT | schema / Buildings |
| Buildings.BuildingName | 保留物理名称；存档没有恢复别名 | TEXT | schema / Buildings |
| Buildings.NumberOfFloors | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Buildings |
| Buildings.ElevatorAccess | 保留物理名称；存档没有恢复别名 | BOOLEAN | schema / Buildings |
| Buildings.SiteParkingAvailable | 保留物理名称；存档没有恢复别名 | BOOLEAN | schema / Buildings |

## Categories

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Categories.CategoryID | 保留物理名称；存档没有恢复别名 | TEXT | schema / Categories |
| Categories.CategoryDescription | 保留物理名称；存档没有恢复别名 | TEXT | schema / Categories |
| Categories.DepartmentID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Categories |

## Class_Rooms

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Class_Rooms.ClassRoomID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Class_Rooms |
| Class_Rooms.BuildingCode | 保留物理名称；存档没有恢复别名 | TEXT | schema / Class_Rooms |
| Class_Rooms.PhoneAvailable | 保留物理名称；存档没有恢复别名 | BOOLEAN | schema / Class_Rooms |

## Classes

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: c

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Classes.ClassID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Classes |
| Classes.SubjectID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Classes |
| Classes.ClassRoomID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Classes |
| Classes.Credits | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Classes |
| Classes.StartDate | 保留物理名称；存档没有恢复别名 | DATE | schema / Classes |
| Classes.StartTime | 保留物理名称；存档没有恢复别名 | TIME | schema / Classes |
| Classes.Duration | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Classes |
| Classes.MondaySchedule | 保留物理名称；存档没有恢复别名 | BOOLEAN | schema / Classes |
| Classes.TuesdaySchedule | 保留物理名称；存档没有恢复别名 | BOOLEAN | schema / Classes |
| Classes.WednesdaySchedule | 保留物理名称；存档没有恢复别名 | BOOLEAN | schema / Classes |
| Classes.ThursdaySchedule | 保留物理名称；存档没有恢复别名 | BOOLEAN | schema / Classes |
| Classes.FridaySchedule | 保留物理名称；存档没有恢复别名 | BOOLEAN | schema / Classes |
| Classes.SaturdaySchedule | 保留物理名称；存档没有恢复别名 | BOOLEAN | schema / Classes |

## Departments

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Departments.DepartmentID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Departments |
| Departments.DeptName | 保留物理名称；存档没有恢复别名 | TEXT | schema / Departments |
| Departments.DeptChair | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Departments |

## Faculty

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Faculty.StaffID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Faculty |
| Faculty.Title | 保留物理名称；存档没有恢复别名 | TEXT | schema / Faculty |
| Faculty.Status | 保留物理名称；存档没有恢复别名 | TEXT | schema / Faculty |
| Faculty.Tenured | 保留物理名称；存档没有恢复别名 | BOOLEAN | schema / Faculty |

## Faculty_Categories

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Faculty_Categories.StaffID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Faculty_Categories |
| Faculty_Categories.CategoryID | 保留物理名称；存档没有恢复别名 | TEXT | schema / Faculty_Categories |

## Faculty_Classes

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Faculty_Classes.ClassID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Faculty_Classes |
| Faculty_Classes.StaffID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Faculty_Classes |

## Faculty_Subjects

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Faculty_Subjects.StaffID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Faculty_Subjects |
| Faculty_Subjects.SubjectID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Faculty_Subjects |
| Faculty_Subjects.ProficiencyRating | 保留物理名称；存档没有恢复别名 | REAL | schema / Faculty_Subjects |

## Majors

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Majors.MajorID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Majors |
| Majors.Major | 保留物理名称；存档没有恢复别名 | TEXT | schema / Majors |

## Staff

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Staff.StaffID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Staff |
| Staff.StfFirstName | 保留物理名称；存档没有恢复别名 | TEXT | schema / Staff |
| Staff.StfLastname | 保留物理名称；存档没有恢复别名 | TEXT | schema / Staff |
| Staff.StfStreetAddress | 保留物理名称；存档没有恢复别名 | TEXT | schema / Staff |
| Staff.StfCity | 保留物理名称；存档没有恢复别名 | TEXT | schema / Staff |
| Staff.StfState | 保留物理名称；存档没有恢复别名 | TEXT | schema / Staff |
| Staff.StfZipCode | 保留物理名称；存档没有恢复别名 | TEXT | schema / Staff |
| Staff.StfAreaCode | 保留物理名称；存档没有恢复别名 | TEXT | schema / Staff |
| Staff.StfPhoneNumber | 保留物理名称；存档没有恢复别名 | TEXT | schema / Staff |
| Staff.Salary | 保留物理名称；存档没有恢复别名 | REAL | schema / Staff |
| Staff.DateHired | 保留物理名称；存档没有恢复别名 | DATE | schema / Staff |
| Staff.Position | 保留物理名称；存档没有恢复别名 | TEXT | schema / Staff |

## Student_Class_Status

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Student_Class_Status.ClassStatus | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Student_Class_Status |
| Student_Class_Status.ClassStatusDescription | 保留物理名称；存档没有恢复别名 | TEXT | schema / Student_Class_Status |

## Student_Schedules

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: ss

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Student_Schedules.StudentID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Student_Schedules |
| Student_Schedules.ClassID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Student_Schedules |
| Student_Schedules.ClassStatus | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Student_Schedules |
| Student_Schedules.Grade | 保留物理名称；存档没有恢复别名 | REAL | schema / Student_Schedules |

## Students

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: st

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Students.StudentID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Students |
| Students.StudFirstName | 保留物理名称；存档没有恢复别名 | TEXT | schema / Students |
| Students.StudLastName | 保留物理名称；存档没有恢复别名 | TEXT | schema / Students |
| Students.StudStreetAddress | 保留物理名称；存档没有恢复别名 | TEXT | schema / Students |
| Students.StudCity | 保留物理名称；存档没有恢复别名 | TEXT | schema / Students |
| Students.StudState | 保留物理名称；存档没有恢复别名 | TEXT | schema / Students |
| Students.StudZipCode | 保留物理名称；存档没有恢复别名 | TEXT | schema / Students |
| Students.StudAreaCode | 保留物理名称；存档没有恢复别名 | TEXT | schema / Students |
| Students.StudPhoneNumber | 保留物理名称；存档没有恢复别名 | TEXT | schema / Students |
| Students.StudGPA | 保留物理名称；存档没有恢复别名 | REAL | schema / Students |
| Students.StudMajor | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Students |

## Subjects

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: s

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Subjects.SubjectID | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Subjects |
| Subjects.CategoryID | 保留物理名称；存档没有恢复别名 | TEXT | schema / Subjects |
| Subjects.SubjectCode | 保留物理名称；存档没有恢复别名 | TEXT | schema / Subjects |
| Subjects.SubjectName | 保留物理名称；存档没有恢复别名 | TEXT | schema / Subjects |
| Subjects.SubjectPreReq | 保留物理名称；存档没有恢复别名 | TEXT | schema / Subjects |
| Subjects.SubjectDescription | 保留物理名称；存档没有恢复别名 | TEXT | schema / Subjects |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

