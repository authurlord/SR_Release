# Spider2-Lite / education_business — Schema and business semantics

The saved catalogue for this database contains 18 tables, 98 physical columns, 0 relationships and 18 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## SalaryDataset

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| SalaryDataset.index | Physical name retained; no saved recovered alias | INTEGER | schema / SalaryDataset |
| SalaryDataset.CompanyName | Physical name retained; no saved recovered alias | TEXT | schema / SalaryDataset |
| SalaryDataset.JobTitle | Physical name retained; no saved recovered alias | TEXT | schema / SalaryDataset |
| SalaryDataset.SalariesReported | Physical name retained; no saved recovered alias | REAL | schema / SalaryDataset |
| SalaryDataset.Location | Physical name retained; no saved recovered alias | TEXT | schema / SalaryDataset |
| SalaryDataset.Salary | Physical name retained; no saved recovered alias | TEXT | schema / SalaryDataset |

## StaffHours

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| StaffHours.StaffMember | Physical name retained; no saved recovered alias | TEXT | schema / StaffHours |
| StaffHours.EventDate | Physical name retained; no saved recovered alias | TEXT | schema / StaffHours |
| StaffHours.EventTime | Physical name retained; no saved recovered alias | TEXT | schema / StaffHours |
| StaffHours.EventType | Physical name retained; no saved recovered alias | TEXT | schema / StaffHours |

## hardware_dim_customer

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| hardware_dim_customer.customer_code | Physical name retained; no saved recovered alias | INTEGER | schema / hardware_dim_customer |
| hardware_dim_customer.customer | Physical name retained; no saved recovered alias | TEXT | schema / hardware_dim_customer |
| hardware_dim_customer.platform | Physical name retained; no saved recovered alias | TEXT | schema / hardware_dim_customer |
| hardware_dim_customer.channel | Physical name retained; no saved recovered alias | TEXT | schema / hardware_dim_customer |
| hardware_dim_customer.market | Physical name retained; no saved recovered alias | TEXT | schema / hardware_dim_customer |
| hardware_dim_customer.sub_zone | Physical name retained; no saved recovered alias | TEXT | schema / hardware_dim_customer |
| hardware_dim_customer.region | Physical name retained; no saved recovered alias | TEXT | schema / hardware_dim_customer |

## hardware_dim_product

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: p

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| hardware_dim_product.product_code | Physical name retained; no saved recovered alias | TEXT | schema / hardware_dim_product |
| hardware_dim_product.division | Physical name retained; no saved recovered alias | TEXT | schema / hardware_dim_product |
| hardware_dim_product.segment | Physical name retained; no saved recovered alias | TEXT | schema / hardware_dim_product |
| hardware_dim_product.category | Physical name retained; no saved recovered alias | TEXT | schema / hardware_dim_product |
| hardware_dim_product.product | Physical name retained; no saved recovered alias | TEXT | schema / hardware_dim_product |
| hardware_dim_product.variant | Physical name retained; no saved recovered alias | TEXT | schema / hardware_dim_product |

## hardware_fact_gross_price

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| hardware_fact_gross_price.product_code | Physical name retained; no saved recovered alias | TEXT | schema / hardware_fact_gross_price |
| hardware_fact_gross_price.fiscal_year | Physical name retained; no saved recovered alias | INTEGER | schema / hardware_fact_gross_price |
| hardware_fact_gross_price.gross_price | Physical name retained; no saved recovered alias | REAL | schema / hardware_fact_gross_price |

## hardware_fact_manufacturing_cost

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| hardware_fact_manufacturing_cost.product_code | Physical name retained; no saved recovered alias | TEXT | schema / hardware_fact_manufacturing_cost |
| hardware_fact_manufacturing_cost.cost_year | Physical name retained; no saved recovered alias | INTEGER | schema / hardware_fact_manufacturing_cost |
| hardware_fact_manufacturing_cost.manufacturing_cost | Physical name retained; no saved recovered alias | REAL | schema / hardware_fact_manufacturing_cost |

## hardware_fact_pre_invoice_deductions

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| hardware_fact_pre_invoice_deductions.customer_code | Physical name retained; no saved recovered alias | INTEGER | schema / hardware_fact_pre_invoice_deductions |
| hardware_fact_pre_invoice_deductions.fiscal_year | Physical name retained; no saved recovered alias | INTEGER | schema / hardware_fact_pre_invoice_deductions |
| hardware_fact_pre_invoice_deductions.pre_invoice_discount_pct | Physical name retained; no saved recovered alias | REAL | schema / hardware_fact_pre_invoice_deductions |

## hardware_fact_sales_monthly

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: s

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| hardware_fact_sales_monthly.date | Physical name retained; no saved recovered alias | TEXT | schema / hardware_fact_sales_monthly |
| hardware_fact_sales_monthly.product_code | Physical name retained; no saved recovered alias | TEXT | schema / hardware_fact_sales_monthly |
| hardware_fact_sales_monthly.customer_code | Physical name retained; no saved recovered alias | INTEGER | schema / hardware_fact_sales_monthly |
| hardware_fact_sales_monthly.sold_quantity | Physical name retained; no saved recovered alias | INTEGER | schema / hardware_fact_sales_monthly |
| hardware_fact_sales_monthly.fiscal_year | Physical name retained; no saved recovered alias | INTEGER | schema / hardware_fact_sales_monthly |

## university_course

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| university_course.CourseNo | Physical name retained; no saved recovered alias | TEXT | schema / university_course |
| university_course.CrsDesc | Physical name retained; no saved recovered alias | TEXT | schema / university_course |
| university_course.CrsUnits | Physical name retained; no saved recovered alias | INTEGER | schema / university_course |

## university_enrollment

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| university_enrollment.OfferNo | Physical name retained; no saved recovered alias | INTEGER | schema / university_enrollment |
| university_enrollment.StdNo | Physical name retained; no saved recovered alias | INTEGER | schema / university_enrollment |
| university_enrollment.EnrGrade | Physical name retained; no saved recovered alias | REAL | schema / university_enrollment |

## university_faculty

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: f

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| university_faculty.FacNo | Physical name retained; no saved recovered alias | INTEGER | schema / university_faculty |
| university_faculty.FacFirstName | Physical name retained; no saved recovered alias | TEXT | schema / university_faculty |
| university_faculty.FacLastName | Physical name retained; no saved recovered alias | TEXT | schema / university_faculty |
| university_faculty.FacCity | Physical name retained; no saved recovered alias | TEXT | schema / university_faculty |
| university_faculty.FacState | Physical name retained; no saved recovered alias | TEXT | schema / university_faculty |
| university_faculty.FacDept | Physical name retained; no saved recovered alias | TEXT | schema / university_faculty |
| university_faculty.FacRank | Physical name retained; no saved recovered alias | TEXT | schema / university_faculty |
| university_faculty.FacSalary | Physical name retained; no saved recovered alias | INTEGER | schema / university_faculty |
| university_faculty.FacSupervisor | Physical name retained; no saved recovered alias | REAL | schema / university_faculty |
| university_faculty.FacHireDate | Physical name retained; no saved recovered alias | TEXT | schema / university_faculty |
| university_faculty.FacZipCode | Physical name retained; no saved recovered alias | TEXT | schema / university_faculty |

## university_offering

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| university_offering.OfferNo | Physical name retained; no saved recovered alias | INTEGER | schema / university_offering |
| university_offering.CourseNo | Physical name retained; no saved recovered alias | TEXT | schema / university_offering |
| university_offering.OffTerm | Physical name retained; no saved recovered alias | TEXT | schema / university_offering |
| university_offering.OffYear | Physical name retained; no saved recovered alias | INTEGER | schema / university_offering |
| university_offering.OffLocation | Physical name retained; no saved recovered alias | TEXT | schema / university_offering |
| university_offering.OffTime | Physical name retained; no saved recovered alias | TEXT | schema / university_offering |
| university_offering.FacNo | Physical name retained; no saved recovered alias | REAL | schema / university_offering |
| university_offering.OffDays | Physical name retained; no saved recovered alias | TEXT | schema / university_offering |

## university_student

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| university_student.StdNo | Physical name retained; no saved recovered alias | INTEGER | schema / university_student |
| university_student.StdFirstName | Physical name retained; no saved recovered alias | TEXT | schema / university_student |
| university_student.StdLastName | Physical name retained; no saved recovered alias | TEXT | schema / university_student |
| university_student.StdCity | Physical name retained; no saved recovered alias | TEXT | schema / university_student |
| university_student.StdState | Physical name retained; no saved recovered alias | TEXT | schema / university_student |
| university_student.StdZip | Physical name retained; no saved recovered alias | TEXT | schema / university_student |
| university_student.StdMajor | Physical name retained; no saved recovered alias | TEXT | schema / university_student |
| university_student.StdClass | Physical name retained; no saved recovered alias | TEXT | schema / university_student |
| university_student.StdGPA | Physical name retained; no saved recovered alias | REAL | schema / university_student |

## web_accounts

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: a

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| web_accounts.id | Physical name retained; no saved recovered alias | INTEGER | schema / web_accounts |
| web_accounts.name | Physical name retained; no saved recovered alias | TEXT | schema / web_accounts |
| web_accounts.website | Physical name retained; no saved recovered alias | TEXT | schema / web_accounts |
| web_accounts.lat | Physical name retained; no saved recovered alias | REAL | schema / web_accounts |
| web_accounts.long | Physical name retained; no saved recovered alias | REAL | schema / web_accounts |
| web_accounts.primary_poc | Physical name retained; no saved recovered alias | TEXT | schema / web_accounts |
| web_accounts.sales_rep_id | Physical name retained; no saved recovered alias | INTEGER | schema / web_accounts |

## web_events

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| web_events.id | Physical name retained; no saved recovered alias | INTEGER | schema / web_events |
| web_events.account_id | Physical name retained; no saved recovered alias | INTEGER | schema / web_events |
| web_events.occurred_at | Physical name retained; no saved recovered alias | TEXT | schema / web_events |
| web_events.channel | Physical name retained; no saved recovered alias | TEXT | schema / web_events |

## web_orders

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: o

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| web_orders.id | Physical name retained; no saved recovered alias | INTEGER | schema / web_orders |
| web_orders.account_id | Physical name retained; no saved recovered alias | INTEGER | schema / web_orders |
| web_orders.occurred_at | Physical name retained; no saved recovered alias | TEXT | schema / web_orders |
| web_orders.standard_qty | Physical name retained; no saved recovered alias | INTEGER | schema / web_orders |
| web_orders.gloss_qty | Physical name retained; no saved recovered alias | INTEGER | schema / web_orders |
| web_orders.poster_qty | Physical name retained; no saved recovered alias | INTEGER | schema / web_orders |
| web_orders.total | Physical name retained; no saved recovered alias | INTEGER | schema / web_orders |
| web_orders.standard_amt_usd | Physical name retained; no saved recovered alias | REAL | schema / web_orders |
| web_orders.gloss_amt_usd | Physical name retained; no saved recovered alias | REAL | schema / web_orders |
| web_orders.poster_amt_usd | Physical name retained; no saved recovered alias | REAL | schema / web_orders |
| web_orders.total_amt_usd | Physical name retained; no saved recovered alias | REAL | schema / web_orders |

## web_region

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: rg

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| web_region.id | Physical name retained; no saved recovered alias | INTEGER | schema / web_region |
| web_region.name | Physical name retained; no saved recovered alias | TEXT | schema / web_region |

## web_sales_reps

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: sr

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| web_sales_reps.id | Physical name retained; no saved recovered alias | INTEGER | schema / web_sales_reps |
| web_sales_reps.name | Physical name retained; no saved recovered alias | TEXT | schema / web_sales_reps |
| web_sales_reps.region_id | Physical name retained; no saved recovered alias | INTEGER | schema / web_sales_reps |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

