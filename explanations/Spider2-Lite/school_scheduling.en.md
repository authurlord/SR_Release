# Spider2-Lite / school_scheduling — Schema and business semantics

The saved catalogue for this database contains 15 tables, 75 physical columns, 0 relationships and 15 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## Buildings

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Buildings.BuildingCode | Physical name retained; no saved recovered alias | TEXT | schema / Buildings |
| Buildings.BuildingName | Physical name retained; no saved recovered alias | TEXT | schema / Buildings |
| Buildings.NumberOfFloors | Physical name retained; no saved recovered alias | INTEGER | schema / Buildings |
| Buildings.ElevatorAccess | Physical name retained; no saved recovered alias | BOOLEAN | schema / Buildings |
| Buildings.SiteParkingAvailable | Physical name retained; no saved recovered alias | BOOLEAN | schema / Buildings |

## Categories

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Categories.CategoryID | Physical name retained; no saved recovered alias | TEXT | schema / Categories |
| Categories.CategoryDescription | Physical name retained; no saved recovered alias | TEXT | schema / Categories |
| Categories.DepartmentID | Physical name retained; no saved recovered alias | INTEGER | schema / Categories |

## Class_Rooms

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Class_Rooms.ClassRoomID | Physical name retained; no saved recovered alias | INTEGER | schema / Class_Rooms |
| Class_Rooms.BuildingCode | Physical name retained; no saved recovered alias | TEXT | schema / Class_Rooms |
| Class_Rooms.PhoneAvailable | Physical name retained; no saved recovered alias | BOOLEAN | schema / Class_Rooms |

## Classes

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: c

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Classes.ClassID | Physical name retained; no saved recovered alias | INTEGER | schema / Classes |
| Classes.SubjectID | Physical name retained; no saved recovered alias | INTEGER | schema / Classes |
| Classes.ClassRoomID | Physical name retained; no saved recovered alias | INTEGER | schema / Classes |
| Classes.Credits | Physical name retained; no saved recovered alias | INTEGER | schema / Classes |
| Classes.StartDate | Physical name retained; no saved recovered alias | DATE | schema / Classes |
| Classes.StartTime | Physical name retained; no saved recovered alias | TIME | schema / Classes |
| Classes.Duration | Physical name retained; no saved recovered alias | INTEGER | schema / Classes |
| Classes.MondaySchedule | Physical name retained; no saved recovered alias | BOOLEAN | schema / Classes |
| Classes.TuesdaySchedule | Physical name retained; no saved recovered alias | BOOLEAN | schema / Classes |
| Classes.WednesdaySchedule | Physical name retained; no saved recovered alias | BOOLEAN | schema / Classes |
| Classes.ThursdaySchedule | Physical name retained; no saved recovered alias | BOOLEAN | schema / Classes |
| Classes.FridaySchedule | Physical name retained; no saved recovered alias | BOOLEAN | schema / Classes |
| Classes.SaturdaySchedule | Physical name retained; no saved recovered alias | BOOLEAN | schema / Classes |

## Departments

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Departments.DepartmentID | Physical name retained; no saved recovered alias | INTEGER | schema / Departments |
| Departments.DeptName | Physical name retained; no saved recovered alias | TEXT | schema / Departments |
| Departments.DeptChair | Physical name retained; no saved recovered alias | INTEGER | schema / Departments |

## Faculty

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Faculty.StaffID | Physical name retained; no saved recovered alias | INTEGER | schema / Faculty |
| Faculty.Title | Physical name retained; no saved recovered alias | TEXT | schema / Faculty |
| Faculty.Status | Physical name retained; no saved recovered alias | TEXT | schema / Faculty |
| Faculty.Tenured | Physical name retained; no saved recovered alias | BOOLEAN | schema / Faculty |

## Faculty_Categories

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Faculty_Categories.StaffID | Physical name retained; no saved recovered alias | INTEGER | schema / Faculty_Categories |
| Faculty_Categories.CategoryID | Physical name retained; no saved recovered alias | TEXT | schema / Faculty_Categories |

## Faculty_Classes

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Faculty_Classes.ClassID | Physical name retained; no saved recovered alias | INTEGER | schema / Faculty_Classes |
| Faculty_Classes.StaffID | Physical name retained; no saved recovered alias | INTEGER | schema / Faculty_Classes |

## Faculty_Subjects

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Faculty_Subjects.StaffID | Physical name retained; no saved recovered alias | INTEGER | schema / Faculty_Subjects |
| Faculty_Subjects.SubjectID | Physical name retained; no saved recovered alias | INTEGER | schema / Faculty_Subjects |
| Faculty_Subjects.ProficiencyRating | Physical name retained; no saved recovered alias | REAL | schema / Faculty_Subjects |

## Majors

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Majors.MajorID | Physical name retained; no saved recovered alias | INTEGER | schema / Majors |
| Majors.Major | Physical name retained; no saved recovered alias | TEXT | schema / Majors |

## Staff

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Staff.StaffID | Physical name retained; no saved recovered alias | INTEGER | schema / Staff |
| Staff.StfFirstName | Physical name retained; no saved recovered alias | TEXT | schema / Staff |
| Staff.StfLastname | Physical name retained; no saved recovered alias | TEXT | schema / Staff |
| Staff.StfStreetAddress | Physical name retained; no saved recovered alias | TEXT | schema / Staff |
| Staff.StfCity | Physical name retained; no saved recovered alias | TEXT | schema / Staff |
| Staff.StfState | Physical name retained; no saved recovered alias | TEXT | schema / Staff |
| Staff.StfZipCode | Physical name retained; no saved recovered alias | TEXT | schema / Staff |
| Staff.StfAreaCode | Physical name retained; no saved recovered alias | TEXT | schema / Staff |
| Staff.StfPhoneNumber | Physical name retained; no saved recovered alias | TEXT | schema / Staff |
| Staff.Salary | Physical name retained; no saved recovered alias | REAL | schema / Staff |
| Staff.DateHired | Physical name retained; no saved recovered alias | DATE | schema / Staff |
| Staff.Position | Physical name retained; no saved recovered alias | TEXT | schema / Staff |

## Student_Class_Status

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Student_Class_Status.ClassStatus | Physical name retained; no saved recovered alias | INTEGER | schema / Student_Class_Status |
| Student_Class_Status.ClassStatusDescription | Physical name retained; no saved recovered alias | TEXT | schema / Student_Class_Status |

## Student_Schedules

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: ss

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Student_Schedules.StudentID | Physical name retained; no saved recovered alias | INTEGER | schema / Student_Schedules |
| Student_Schedules.ClassID | Physical name retained; no saved recovered alias | INTEGER | schema / Student_Schedules |
| Student_Schedules.ClassStatus | Physical name retained; no saved recovered alias | INTEGER | schema / Student_Schedules |
| Student_Schedules.Grade | Physical name retained; no saved recovered alias | REAL | schema / Student_Schedules |

## Students

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: st

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Students.StudentID | Physical name retained; no saved recovered alias | INTEGER | schema / Students |
| Students.StudFirstName | Physical name retained; no saved recovered alias | TEXT | schema / Students |
| Students.StudLastName | Physical name retained; no saved recovered alias | TEXT | schema / Students |
| Students.StudStreetAddress | Physical name retained; no saved recovered alias | TEXT | schema / Students |
| Students.StudCity | Physical name retained; no saved recovered alias | TEXT | schema / Students |
| Students.StudState | Physical name retained; no saved recovered alias | TEXT | schema / Students |
| Students.StudZipCode | Physical name retained; no saved recovered alias | TEXT | schema / Students |
| Students.StudAreaCode | Physical name retained; no saved recovered alias | TEXT | schema / Students |
| Students.StudPhoneNumber | Physical name retained; no saved recovered alias | TEXT | schema / Students |
| Students.StudGPA | Physical name retained; no saved recovered alias | REAL | schema / Students |
| Students.StudMajor | Physical name retained; no saved recovered alias | INTEGER | schema / Students |

## Subjects

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: s

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Subjects.SubjectID | Physical name retained; no saved recovered alias | INTEGER | schema / Subjects |
| Subjects.CategoryID | Physical name retained; no saved recovered alias | TEXT | schema / Subjects |
| Subjects.SubjectCode | Physical name retained; no saved recovered alias | TEXT | schema / Subjects |
| Subjects.SubjectName | Physical name retained; no saved recovered alias | TEXT | schema / Subjects |
| Subjects.SubjectPreReq | Physical name retained; no saved recovered alias | TEXT | schema / Subjects |
| Subjects.SubjectDescription | Physical name retained; no saved recovered alias | TEXT | schema / Subjects |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

