# Spider2-Lite / EntertainmentAgency — Schema and business semantics

The saved catalogue for this database contains 13 tables, 76 physical columns, 0 relationships and 13 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## Agents

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Agents.AgentID | Physical name retained; no saved recovered alias | INT | schema / Agents |
| Agents.AgtFirstName | Physical name retained; no saved recovered alias | nvarchar (25) | schema / Agents |
| Agents.AgtLastName | Physical name retained; no saved recovered alias | nvarchar (25) | schema / Agents |
| Agents.AgtStreetAddress | Physical name retained; no saved recovered alias | nvarchar (50) | schema / Agents |
| Agents.AgtCity | Physical name retained; no saved recovered alias | nvarchar (30) | schema / Agents |
| Agents.AgtState | Physical name retained; no saved recovered alias | nvarchar (2) | schema / Agents |
| Agents.AgtZipCode | Physical name retained; no saved recovered alias | nvarchar (10) | schema / Agents |
| Agents.AgtPhoneNumber | Physical name retained; no saved recovered alias | nvarchar (15) | schema / Agents |
| Agents.DateHired | Physical name retained; no saved recovered alias | date | schema / Agents |
| Agents.Salary | Physical name retained; no saved recovered alias | decimal(15, 2) | schema / Agents |
| Agents.CommissionRate | Physical name retained; no saved recovered alias | float(24) | schema / Agents |

## Customers

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: c

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Customers.CustomerID | Physical name retained; no saved recovered alias | INT | schema / Customers |
| Customers.CustFirstName | Physical name retained; no saved recovered alias | nvarchar (25) | schema / Customers |
| Customers.CustLastName | Physical name retained; no saved recovered alias | nvarchar (25) | schema / Customers |
| Customers.CustStreetAddress | Physical name retained; no saved recovered alias | nvarchar (50) | schema / Customers |
| Customers.CustCity | Physical name retained; no saved recovered alias | nvarchar (30) | schema / Customers |
| Customers.CustState | Physical name retained; no saved recovered alias | nvarchar (2) | schema / Customers |
| Customers.CustZipCode | Physical name retained; no saved recovered alias | nvarchar (10) | schema / Customers |
| Customers.CustPhoneNumber | Physical name retained; no saved recovered alias | nvarchar (15) | schema / Customers |

## Engagements

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Engagements.EngagementNumber | Physical name retained; no saved recovered alias | INT | schema / Engagements |
| Engagements.StartDate | Physical name retained; no saved recovered alias | date | schema / Engagements |
| Engagements.EndDate | Physical name retained; no saved recovered alias | date | schema / Engagements |
| Engagements.StartTime | Physical name retained; no saved recovered alias | time | schema / Engagements |
| Engagements.StopTime | Physical name retained; no saved recovered alias | time | schema / Engagements |
| Engagements.ContractPrice | Physical name retained; no saved recovered alias | decimal(15, 2) | schema / Engagements |
| Engagements.CustomerID | Physical name retained; no saved recovered alias | INT | schema / Engagements |
| Engagements.AgentID | Physical name retained; no saved recovered alias | INT | schema / Engagements |
| Engagements.EntertainerID | Physical name retained; no saved recovered alias | INT | schema / Engagements |

## Entertainer_Members

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Entertainer_Members.EntertainerID | Physical name retained; no saved recovered alias | INT | schema / Entertainer_Members |
| Entertainer_Members.MemberID | Physical name retained; no saved recovered alias | INT | schema / Entertainer_Members |
| Entertainer_Members.Status | Physical name retained; no saved recovered alias | smallint | schema / Entertainer_Members |

## Entertainer_Styles

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Entertainer_Styles.EntertainerID | Physical name retained; no saved recovered alias | INT | schema / Entertainer_Styles |
| Entertainer_Styles.StyleID | Physical name retained; no saved recovered alias | smallint | schema / Entertainer_Styles |
| Entertainer_Styles.StyleStrength | Physical name retained; no saved recovered alias | smallint | schema / Entertainer_Styles |

## Entertainers

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: e2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Entertainers.EntertainerID | Physical name retained; no saved recovered alias | INT | schema / Entertainers |
| Entertainers.EntStageName | Physical name retained; no saved recovered alias | nvarchar (50) | schema / Entertainers |
| Entertainers.EntSSN | Physical name retained; no saved recovered alias | nvarchar (12) | schema / Entertainers |
| Entertainers.EntStreetAddress | Physical name retained; no saved recovered alias | nvarchar (50) | schema / Entertainers |
| Entertainers.EntCity | Physical name retained; no saved recovered alias | nvarchar (30) | schema / Entertainers |
| Entertainers.EntState | Physical name retained; no saved recovered alias | nvarchar (2) | schema / Entertainers |
| Entertainers.EntZipCode | Physical name retained; no saved recovered alias | nvarchar (10) | schema / Entertainers |
| Entertainers.EntPhoneNumber | Physical name retained; no saved recovered alias | nvarchar (15) | schema / Entertainers |
| Entertainers.EntWebPage | Physical name retained; no saved recovered alias | nvarchar (50) | schema / Entertainers |
| Entertainers.EntEMailAddress | Physical name retained; no saved recovered alias | nvarchar (50) | schema / Entertainers |
| Entertainers.DateEntered | Physical name retained; no saved recovered alias | date | schema / Entertainers |

## Members

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Members.MemberID | Physical name retained; no saved recovered alias | INT | schema / Members |
| Members.MbrFirstName | Physical name retained; no saved recovered alias | nvarchar (25) | schema / Members |
| Members.MbrLastName | Physical name retained; no saved recovered alias | nvarchar (25) | schema / Members |
| Members.MbrPhoneNumber | Physical name retained; no saved recovered alias | nvarchar (15) | schema / Members |
| Members.Gender | Physical name retained; no saved recovered alias | nvarchar (2) | schema / Members |

## Musical_Preferences

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: mp

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Musical_Preferences.CustomerID | Physical name retained; no saved recovered alias | INT | schema / Musical_Preferences |
| Musical_Preferences.StyleID | Physical name retained; no saved recovered alias | smallint | schema / Musical_Preferences |
| Musical_Preferences.PreferenceSeq | Physical name retained; no saved recovered alias | smallint | schema / Musical_Preferences |

## Musical_Styles

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: ms

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Musical_Styles.StyleID | Physical name retained; no saved recovered alias | smallint | schema / Musical_Styles |
| Musical_Styles.StyleName | Physical name retained; no saved recovered alias | nvarchar (75) | schema / Musical_Styles |

## ztblDays

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| ztblDays.DateField | Physical name retained; no saved recovered alias | date | schema / ztblDays |

## ztblMonths

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| ztblMonths.MonthYear | Physical name retained; no saved recovered alias | nvarchar (15) | schema / ztblMonths |
| ztblMonths.YearNumber | Physical name retained; no saved recovered alias | smallint | schema / ztblMonths |
| ztblMonths.MonthNumber | Physical name retained; no saved recovered alias | smallint | schema / ztblMonths |
| ztblMonths.MonthStart | Physical name retained; no saved recovered alias | date | schema / ztblMonths |
| ztblMonths.MonthEnd | Physical name retained; no saved recovered alias | date | schema / ztblMonths |
| ztblMonths.January | Physical name retained; no saved recovered alias | smallint | schema / ztblMonths |
| ztblMonths.February | Physical name retained; no saved recovered alias | smallint | schema / ztblMonths |
| ztblMonths.March | Physical name retained; no saved recovered alias | smallint | schema / ztblMonths |
| ztblMonths.April | Physical name retained; no saved recovered alias | smallint | schema / ztblMonths |
| ztblMonths.May | Physical name retained; no saved recovered alias | smallint | schema / ztblMonths |
| ztblMonths.June | Physical name retained; no saved recovered alias | smallint | schema / ztblMonths |
| ztblMonths.July | Physical name retained; no saved recovered alias | smallint | schema / ztblMonths |
| ztblMonths.August | Physical name retained; no saved recovered alias | smallint | schema / ztblMonths |
| ztblMonths.September | Physical name retained; no saved recovered alias | smallint | schema / ztblMonths |
| ztblMonths.October | Physical name retained; no saved recovered alias | smallint | schema / ztblMonths |
| ztblMonths.November | Physical name retained; no saved recovered alias | smallint | schema / ztblMonths |
| ztblMonths.December | Physical name retained; no saved recovered alias | smallint | schema / ztblMonths |

## ztblSkipLabels

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| ztblSkipLabels.LabelCount | Physical name retained; no saved recovered alias | INT | schema / ztblSkipLabels |

## ztblWeeks

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| ztblWeeks.WeekStart | Physical name retained; no saved recovered alias | date | schema / ztblWeeks |
| ztblWeeks.WeekEnd | Physical name retained; no saved recovered alias | date | schema / ztblWeeks |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

