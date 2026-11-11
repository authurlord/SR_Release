# Spider2-Lite / education_business — Schema 与业务口径解释

该数据库的存档目录包含 18 张表、98 个物理列、0 条关系，以及 18 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## SalaryDataset

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| SalaryDataset.index | 保留物理名称；存档没有恢复别名 | INTEGER | schema / SalaryDataset |
| SalaryDataset.CompanyName | 保留物理名称；存档没有恢复别名 | TEXT | schema / SalaryDataset |
| SalaryDataset.JobTitle | 保留物理名称；存档没有恢复别名 | TEXT | schema / SalaryDataset |
| SalaryDataset.SalariesReported | 保留物理名称；存档没有恢复别名 | REAL | schema / SalaryDataset |
| SalaryDataset.Location | 保留物理名称；存档没有恢复别名 | TEXT | schema / SalaryDataset |
| SalaryDataset.Salary | 保留物理名称；存档没有恢复别名 | TEXT | schema / SalaryDataset |

## StaffHours

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| StaffHours.StaffMember | 保留物理名称；存档没有恢复别名 | TEXT | schema / StaffHours |
| StaffHours.EventDate | 保留物理名称；存档没有恢复别名 | TEXT | schema / StaffHours |
| StaffHours.EventTime | 保留物理名称；存档没有恢复别名 | TEXT | schema / StaffHours |
| StaffHours.EventType | 保留物理名称；存档没有恢复别名 | TEXT | schema / StaffHours |

## hardware_dim_customer

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| hardware_dim_customer.customer_code | 保留物理名称；存档没有恢复别名 | INTEGER | schema / hardware_dim_customer |
| hardware_dim_customer.customer | 保留物理名称；存档没有恢复别名 | TEXT | schema / hardware_dim_customer |
| hardware_dim_customer.platform | 保留物理名称；存档没有恢复别名 | TEXT | schema / hardware_dim_customer |
| hardware_dim_customer.channel | 保留物理名称；存档没有恢复别名 | TEXT | schema / hardware_dim_customer |
| hardware_dim_customer.market | 保留物理名称；存档没有恢复别名 | TEXT | schema / hardware_dim_customer |
| hardware_dim_customer.sub_zone | 保留物理名称；存档没有恢复别名 | TEXT | schema / hardware_dim_customer |
| hardware_dim_customer.region | 保留物理名称；存档没有恢复别名 | TEXT | schema / hardware_dim_customer |

## hardware_dim_product

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: p

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| hardware_dim_product.product_code | 保留物理名称；存档没有恢复别名 | TEXT | schema / hardware_dim_product |
| hardware_dim_product.division | 保留物理名称；存档没有恢复别名 | TEXT | schema / hardware_dim_product |
| hardware_dim_product.segment | 保留物理名称；存档没有恢复别名 | TEXT | schema / hardware_dim_product |
| hardware_dim_product.category | 保留物理名称；存档没有恢复别名 | TEXT | schema / hardware_dim_product |
| hardware_dim_product.product | 保留物理名称；存档没有恢复别名 | TEXT | schema / hardware_dim_product |
| hardware_dim_product.variant | 保留物理名称；存档没有恢复别名 | TEXT | schema / hardware_dim_product |

## hardware_fact_gross_price

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| hardware_fact_gross_price.product_code | 保留物理名称；存档没有恢复别名 | TEXT | schema / hardware_fact_gross_price |
| hardware_fact_gross_price.fiscal_year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / hardware_fact_gross_price |
| hardware_fact_gross_price.gross_price | 保留物理名称；存档没有恢复别名 | REAL | schema / hardware_fact_gross_price |

## hardware_fact_manufacturing_cost

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| hardware_fact_manufacturing_cost.product_code | 保留物理名称；存档没有恢复别名 | TEXT | schema / hardware_fact_manufacturing_cost |
| hardware_fact_manufacturing_cost.cost_year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / hardware_fact_manufacturing_cost |
| hardware_fact_manufacturing_cost.manufacturing_cost | 保留物理名称；存档没有恢复别名 | REAL | schema / hardware_fact_manufacturing_cost |

## hardware_fact_pre_invoice_deductions

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| hardware_fact_pre_invoice_deductions.customer_code | 保留物理名称；存档没有恢复别名 | INTEGER | schema / hardware_fact_pre_invoice_deductions |
| hardware_fact_pre_invoice_deductions.fiscal_year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / hardware_fact_pre_invoice_deductions |
| hardware_fact_pre_invoice_deductions.pre_invoice_discount_pct | 保留物理名称；存档没有恢复别名 | REAL | schema / hardware_fact_pre_invoice_deductions |

## hardware_fact_sales_monthly

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: s

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| hardware_fact_sales_monthly.date | 保留物理名称；存档没有恢复别名 | TEXT | schema / hardware_fact_sales_monthly |
| hardware_fact_sales_monthly.product_code | 保留物理名称；存档没有恢复别名 | TEXT | schema / hardware_fact_sales_monthly |
| hardware_fact_sales_monthly.customer_code | 保留物理名称；存档没有恢复别名 | INTEGER | schema / hardware_fact_sales_monthly |
| hardware_fact_sales_monthly.sold_quantity | 保留物理名称；存档没有恢复别名 | INTEGER | schema / hardware_fact_sales_monthly |
| hardware_fact_sales_monthly.fiscal_year | 保留物理名称；存档没有恢复别名 | INTEGER | schema / hardware_fact_sales_monthly |

## university_course

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| university_course.CourseNo | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_course |
| university_course.CrsDesc | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_course |
| university_course.CrsUnits | 保留物理名称；存档没有恢复别名 | INTEGER | schema / university_course |

## university_enrollment

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| university_enrollment.OfferNo | 保留物理名称；存档没有恢复别名 | INTEGER | schema / university_enrollment |
| university_enrollment.StdNo | 保留物理名称；存档没有恢复别名 | INTEGER | schema / university_enrollment |
| university_enrollment.EnrGrade | 保留物理名称；存档没有恢复别名 | REAL | schema / university_enrollment |

## university_faculty

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: f

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| university_faculty.FacNo | 保留物理名称；存档没有恢复别名 | INTEGER | schema / university_faculty |
| university_faculty.FacFirstName | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_faculty |
| university_faculty.FacLastName | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_faculty |
| university_faculty.FacCity | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_faculty |
| university_faculty.FacState | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_faculty |
| university_faculty.FacDept | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_faculty |
| university_faculty.FacRank | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_faculty |
| university_faculty.FacSalary | 保留物理名称；存档没有恢复别名 | INTEGER | schema / university_faculty |
| university_faculty.FacSupervisor | 保留物理名称；存档没有恢复别名 | REAL | schema / university_faculty |
| university_faculty.FacHireDate | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_faculty |
| university_faculty.FacZipCode | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_faculty |

## university_offering

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| university_offering.OfferNo | 保留物理名称；存档没有恢复别名 | INTEGER | schema / university_offering |
| university_offering.CourseNo | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_offering |
| university_offering.OffTerm | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_offering |
| university_offering.OffYear | 保留物理名称；存档没有恢复别名 | INTEGER | schema / university_offering |
| university_offering.OffLocation | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_offering |
| university_offering.OffTime | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_offering |
| university_offering.FacNo | 保留物理名称；存档没有恢复别名 | REAL | schema / university_offering |
| university_offering.OffDays | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_offering |

## university_student

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| university_student.StdNo | 保留物理名称；存档没有恢复别名 | INTEGER | schema / university_student |
| university_student.StdFirstName | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_student |
| university_student.StdLastName | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_student |
| university_student.StdCity | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_student |
| university_student.StdState | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_student |
| university_student.StdZip | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_student |
| university_student.StdMajor | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_student |
| university_student.StdClass | 保留物理名称；存档没有恢复别名 | TEXT | schema / university_student |
| university_student.StdGPA | 保留物理名称；存档没有恢复别名 | REAL | schema / university_student |

## web_accounts

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: a

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| web_accounts.id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / web_accounts |
| web_accounts.name | 保留物理名称；存档没有恢复别名 | TEXT | schema / web_accounts |
| web_accounts.website | 保留物理名称；存档没有恢复别名 | TEXT | schema / web_accounts |
| web_accounts.lat | 保留物理名称；存档没有恢复别名 | REAL | schema / web_accounts |
| web_accounts.long | 保留物理名称；存档没有恢复别名 | REAL | schema / web_accounts |
| web_accounts.primary_poc | 保留物理名称；存档没有恢复别名 | TEXT | schema / web_accounts |
| web_accounts.sales_rep_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / web_accounts |

## web_events

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| web_events.id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / web_events |
| web_events.account_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / web_events |
| web_events.occurred_at | 保留物理名称；存档没有恢复别名 | TEXT | schema / web_events |
| web_events.channel | 保留物理名称；存档没有恢复别名 | TEXT | schema / web_events |

## web_orders

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: o

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| web_orders.id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / web_orders |
| web_orders.account_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / web_orders |
| web_orders.occurred_at | 保留物理名称；存档没有恢复别名 | TEXT | schema / web_orders |
| web_orders.standard_qty | 保留物理名称；存档没有恢复别名 | INTEGER | schema / web_orders |
| web_orders.gloss_qty | 保留物理名称；存档没有恢复别名 | INTEGER | schema / web_orders |
| web_orders.poster_qty | 保留物理名称；存档没有恢复别名 | INTEGER | schema / web_orders |
| web_orders.total | 保留物理名称；存档没有恢复别名 | INTEGER | schema / web_orders |
| web_orders.standard_amt_usd | 保留物理名称；存档没有恢复别名 | REAL | schema / web_orders |
| web_orders.gloss_amt_usd | 保留物理名称；存档没有恢复别名 | REAL | schema / web_orders |
| web_orders.poster_amt_usd | 保留物理名称；存档没有恢复别名 | REAL | schema / web_orders |
| web_orders.total_amt_usd | 保留物理名称；存档没有恢复别名 | REAL | schema / web_orders |

## web_region

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: rg

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| web_region.id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / web_region |
| web_region.name | 保留物理名称；存档没有恢复别名 | TEXT | schema / web_region |

## web_sales_reps

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: sr

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| web_sales_reps.id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / web_sales_reps |
| web_sales_reps.name | 保留物理名称；存档没有恢复别名 | TEXT | schema / web_sales_reps |
| web_sales_reps.region_id | 保留物理名称；存档没有恢复别名 | INTEGER | schema / web_sales_reps |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

