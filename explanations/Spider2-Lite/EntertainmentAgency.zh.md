# Spider2-Lite / EntertainmentAgency — Schema 与业务口径解释

该数据库的存档目录包含 13 张表、76 个物理列、0 条关系，以及 13 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## Agents

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Agents.AgentID | 保留物理名称；存档没有恢复别名 | INT | schema / Agents |
| Agents.AgtFirstName | 保留物理名称；存档没有恢复别名 | nvarchar (25) | schema / Agents |
| Agents.AgtLastName | 保留物理名称；存档没有恢复别名 | nvarchar (25) | schema / Agents |
| Agents.AgtStreetAddress | 保留物理名称；存档没有恢复别名 | nvarchar (50) | schema / Agents |
| Agents.AgtCity | 保留物理名称；存档没有恢复别名 | nvarchar (30) | schema / Agents |
| Agents.AgtState | 保留物理名称；存档没有恢复别名 | nvarchar (2) | schema / Agents |
| Agents.AgtZipCode | 保留物理名称；存档没有恢复别名 | nvarchar (10) | schema / Agents |
| Agents.AgtPhoneNumber | 保留物理名称；存档没有恢复别名 | nvarchar (15) | schema / Agents |
| Agents.DateHired | 保留物理名称；存档没有恢复别名 | date | schema / Agents |
| Agents.Salary | 保留物理名称；存档没有恢复别名 | decimal(15, 2) | schema / Agents |
| Agents.CommissionRate | 保留物理名称；存档没有恢复别名 | float(24) | schema / Agents |

## Customers

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: c

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Customers.CustomerID | 保留物理名称；存档没有恢复别名 | INT | schema / Customers |
| Customers.CustFirstName | 保留物理名称；存档没有恢复别名 | nvarchar (25) | schema / Customers |
| Customers.CustLastName | 保留物理名称；存档没有恢复别名 | nvarchar (25) | schema / Customers |
| Customers.CustStreetAddress | 保留物理名称；存档没有恢复别名 | nvarchar (50) | schema / Customers |
| Customers.CustCity | 保留物理名称；存档没有恢复别名 | nvarchar (30) | schema / Customers |
| Customers.CustState | 保留物理名称；存档没有恢复别名 | nvarchar (2) | schema / Customers |
| Customers.CustZipCode | 保留物理名称；存档没有恢复别名 | nvarchar (10) | schema / Customers |
| Customers.CustPhoneNumber | 保留物理名称；存档没有恢复别名 | nvarchar (15) | schema / Customers |

## Engagements

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Engagements.EngagementNumber | 保留物理名称；存档没有恢复别名 | INT | schema / Engagements |
| Engagements.StartDate | 保留物理名称；存档没有恢复别名 | date | schema / Engagements |
| Engagements.EndDate | 保留物理名称；存档没有恢复别名 | date | schema / Engagements |
| Engagements.StartTime | 保留物理名称；存档没有恢复别名 | time | schema / Engagements |
| Engagements.StopTime | 保留物理名称；存档没有恢复别名 | time | schema / Engagements |
| Engagements.ContractPrice | 保留物理名称；存档没有恢复别名 | decimal(15, 2) | schema / Engagements |
| Engagements.CustomerID | 保留物理名称；存档没有恢复别名 | INT | schema / Engagements |
| Engagements.AgentID | 保留物理名称；存档没有恢复别名 | INT | schema / Engagements |
| Engagements.EntertainerID | 保留物理名称；存档没有恢复别名 | INT | schema / Engagements |

## Entertainer_Members

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Entertainer_Members.EntertainerID | 保留物理名称；存档没有恢复别名 | INT | schema / Entertainer_Members |
| Entertainer_Members.MemberID | 保留物理名称；存档没有恢复别名 | INT | schema / Entertainer_Members |
| Entertainer_Members.Status | 保留物理名称；存档没有恢复别名 | smallint | schema / Entertainer_Members |

## Entertainer_Styles

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Entertainer_Styles.EntertainerID | 保留物理名称；存档没有恢复别名 | INT | schema / Entertainer_Styles |
| Entertainer_Styles.StyleID | 保留物理名称；存档没有恢复别名 | smallint | schema / Entertainer_Styles |
| Entertainer_Styles.StyleStrength | 保留物理名称；存档没有恢复别名 | smallint | schema / Entertainer_Styles |

## Entertainers

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: e2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Entertainers.EntertainerID | 保留物理名称；存档没有恢复别名 | INT | schema / Entertainers |
| Entertainers.EntStageName | 保留物理名称；存档没有恢复别名 | nvarchar (50) | schema / Entertainers |
| Entertainers.EntSSN | 保留物理名称；存档没有恢复别名 | nvarchar (12) | schema / Entertainers |
| Entertainers.EntStreetAddress | 保留物理名称；存档没有恢复别名 | nvarchar (50) | schema / Entertainers |
| Entertainers.EntCity | 保留物理名称；存档没有恢复别名 | nvarchar (30) | schema / Entertainers |
| Entertainers.EntState | 保留物理名称；存档没有恢复别名 | nvarchar (2) | schema / Entertainers |
| Entertainers.EntZipCode | 保留物理名称；存档没有恢复别名 | nvarchar (10) | schema / Entertainers |
| Entertainers.EntPhoneNumber | 保留物理名称；存档没有恢复别名 | nvarchar (15) | schema / Entertainers |
| Entertainers.EntWebPage | 保留物理名称；存档没有恢复别名 | nvarchar (50) | schema / Entertainers |
| Entertainers.EntEMailAddress | 保留物理名称；存档没有恢复别名 | nvarchar (50) | schema / Entertainers |
| Entertainers.DateEntered | 保留物理名称；存档没有恢复别名 | date | schema / Entertainers |

## Members

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Members.MemberID | 保留物理名称；存档没有恢复别名 | INT | schema / Members |
| Members.MbrFirstName | 保留物理名称；存档没有恢复别名 | nvarchar (25) | schema / Members |
| Members.MbrLastName | 保留物理名称；存档没有恢复别名 | nvarchar (25) | schema / Members |
| Members.MbrPhoneNumber | 保留物理名称；存档没有恢复别名 | nvarchar (15) | schema / Members |
| Members.Gender | 保留物理名称；存档没有恢复别名 | nvarchar (2) | schema / Members |

## Musical_Preferences

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: mp

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Musical_Preferences.CustomerID | 保留物理名称；存档没有恢复别名 | INT | schema / Musical_Preferences |
| Musical_Preferences.StyleID | 保留物理名称；存档没有恢复别名 | smallint | schema / Musical_Preferences |
| Musical_Preferences.PreferenceSeq | 保留物理名称；存档没有恢复别名 | smallint | schema / Musical_Preferences |

## Musical_Styles

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: ms

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Musical_Styles.StyleID | 保留物理名称；存档没有恢复别名 | smallint | schema / Musical_Styles |
| Musical_Styles.StyleName | 保留物理名称；存档没有恢复别名 | nvarchar (75) | schema / Musical_Styles |

## ztblDays

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ztblDays.DateField | 保留物理名称；存档没有恢复别名 | date | schema / ztblDays |

## ztblMonths

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ztblMonths.MonthYear | 保留物理名称；存档没有恢复别名 | nvarchar (15) | schema / ztblMonths |
| ztblMonths.YearNumber | 保留物理名称；存档没有恢复别名 | smallint | schema / ztblMonths |
| ztblMonths.MonthNumber | 保留物理名称；存档没有恢复别名 | smallint | schema / ztblMonths |
| ztblMonths.MonthStart | 保留物理名称；存档没有恢复别名 | date | schema / ztblMonths |
| ztblMonths.MonthEnd | 保留物理名称；存档没有恢复别名 | date | schema / ztblMonths |
| ztblMonths.January | 保留物理名称；存档没有恢复别名 | smallint | schema / ztblMonths |
| ztblMonths.February | 保留物理名称；存档没有恢复别名 | smallint | schema / ztblMonths |
| ztblMonths.March | 保留物理名称；存档没有恢复别名 | smallint | schema / ztblMonths |
| ztblMonths.April | 保留物理名称；存档没有恢复别名 | smallint | schema / ztblMonths |
| ztblMonths.May | 保留物理名称；存档没有恢复别名 | smallint | schema / ztblMonths |
| ztblMonths.June | 保留物理名称；存档没有恢复别名 | smallint | schema / ztblMonths |
| ztblMonths.July | 保留物理名称；存档没有恢复别名 | smallint | schema / ztblMonths |
| ztblMonths.August | 保留物理名称；存档没有恢复别名 | smallint | schema / ztblMonths |
| ztblMonths.September | 保留物理名称；存档没有恢复别名 | smallint | schema / ztblMonths |
| ztblMonths.October | 保留物理名称；存档没有恢复别名 | smallint | schema / ztblMonths |
| ztblMonths.November | 保留物理名称；存档没有恢复别名 | smallint | schema / ztblMonths |
| ztblMonths.December | 保留物理名称；存档没有恢复别名 | smallint | schema / ztblMonths |

## ztblSkipLabels

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ztblSkipLabels.LabelCount | 保留物理名称；存档没有恢复别名 | INT | schema / ztblSkipLabels |

## ztblWeeks

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ztblWeeks.WeekStart | 保留物理名称；存档没有恢复别名 | date | schema / ztblWeeks |
| ztblWeeks.WeekEnd | 保留物理名称；存档没有恢复别名 | date | schema / ztblWeeks |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

