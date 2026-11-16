# Spider2-Lite / northwind — Schema and business semantics

The saved catalogue for this database contains 15 tables, 95 physical columns, 0 relationships and 15 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## categories

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| categories.categoryid | Physical name retained; no saved recovered alias | INTEGER | schema / categories |
| categories.categoryname | Physical name retained; no saved recovered alias | TEXT | schema / categories |
| categories.description | Physical name retained; no saved recovered alias | TEXT | schema / categories |
| categories.picture | Physical name retained; no saved recovered alias | BLOB | schema / categories |

## customercustomerdemo

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| customercustomerdemo.customerid | Physical name retained; no saved recovered alias | TEXT | schema / customercustomerdemo |
| customercustomerdemo.customertypeid | Physical name retained; no saved recovered alias | TEXT | schema / customercustomerdemo |

## customerdemographics

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| customerdemographics.customertypeid | Physical name retained; no saved recovered alias | TEXT | schema / customerdemographics |
| customerdemographics.customerdesc | Physical name retained; no saved recovered alias | TEXT | schema / customerdemographics |

## customergroupthreshold

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: g

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| customergroupthreshold.groupname | Physical name retained; no saved recovered alias | TEXT | schema / customergroupthreshold |
| customergroupthreshold.rangebottom | Physical name retained; no saved recovered alias | DECIMAL | schema / customergroupthreshold |
| customergroupthreshold.rangetop | Physical name retained; no saved recovered alias | DECIMAL | schema / customergroupthreshold |

## customers

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| customers.customerid | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.companyname | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.contactname | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.contacttitle | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.address | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.city | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.region | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.postalcode | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.country | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.phone | Physical name retained; no saved recovered alias | TEXT | schema / customers |
| customers.fax | Physical name retained; no saved recovered alias | TEXT | schema / customers |

## employees

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| employees.employeeid | Physical name retained; no saved recovered alias | INTEGER | schema / employees |
| employees.lastname | Physical name retained; no saved recovered alias | TEXT | schema / employees |
| employees.firstname | Physical name retained; no saved recovered alias | TEXT | schema / employees |
| employees.title | Physical name retained; no saved recovered alias | TEXT | schema / employees |
| employees.titleofcourtesy | Physical name retained; no saved recovered alias | TEXT | schema / employees |
| employees.birthdate | Physical name retained; no saved recovered alias | DATE | schema / employees |
| employees.hiredate | Physical name retained; no saved recovered alias | DATE | schema / employees |
| employees.address | Physical name retained; no saved recovered alias | TEXT | schema / employees |
| employees.city | Physical name retained; no saved recovered alias | TEXT | schema / employees |
| employees.region | Physical name retained; no saved recovered alias | TEXT | schema / employees |
| employees.postalcode | Physical name retained; no saved recovered alias | TEXT | schema / employees |
| employees.country | Physical name retained; no saved recovered alias | TEXT | schema / employees |
| employees.homephone | Physical name retained; no saved recovered alias | TEXT | schema / employees |
| employees.extension | Physical name retained; no saved recovered alias | TEXT | schema / employees |
| employees.photo | Physical name retained; no saved recovered alias | BLOB | schema / employees |
| employees.notes | Physical name retained; no saved recovered alias | TEXT | schema / employees |
| employees.reportsto | Physical name retained; no saved recovered alias | INTEGER | schema / employees |
| employees.photopath | Physical name retained; no saved recovered alias | TEXT | schema / employees |

## employeeterritories

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| employeeterritories.employeeid | Physical name retained; no saved recovered alias | INTEGER | schema / employeeterritories |
| employeeterritories.territoryid | Physical name retained; no saved recovered alias | TEXT | schema / employeeterritories |

## order_details

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: od

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| order_details.orderid | Physical name retained; no saved recovered alias | INTEGER | schema / order_details |
| order_details.productid | Physical name retained; no saved recovered alias | INTEGER | schema / order_details |
| order_details.unitprice | Physical name retained; no saved recovered alias | REAL | schema / order_details |
| order_details.quantity | Physical name retained; no saved recovered alias | INTEGER | schema / order_details |
| order_details.discount | Physical name retained; no saved recovered alias | REAL | schema / order_details |

## orders

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: o

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| orders.orderid | Physical name retained; no saved recovered alias | INTEGER | schema / orders |
| orders.customerid | Physical name retained; no saved recovered alias | TEXT | schema / orders |
| orders.employeeid | Physical name retained; no saved recovered alias | INTEGER | schema / orders |
| orders.orderdate | Physical name retained; no saved recovered alias | DATE | schema / orders |
| orders.requireddate | Physical name retained; no saved recovered alias | DATE | schema / orders |
| orders.shippeddate | Physical name retained; no saved recovered alias | DATE | schema / orders |
| orders.shipvia | Physical name retained; no saved recovered alias | INTEGER | schema / orders |
| orders.freight | Physical name retained; no saved recovered alias | REAL | schema / orders |
| orders.shipname | Physical name retained; no saved recovered alias | TEXT | schema / orders |
| orders.shipaddress | Physical name retained; no saved recovered alias | TEXT | schema / orders |
| orders.shipcity | Physical name retained; no saved recovered alias | TEXT | schema / orders |
| orders.shipregion | Physical name retained; no saved recovered alias | TEXT | schema / orders |
| orders.shippostalcode | Physical name retained; no saved recovered alias | TEXT | schema / orders |
| orders.shipcountry | Physical name retained; no saved recovered alias | TEXT | schema / orders |

## products

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| products.productid | Physical name retained; no saved recovered alias | INTEGER | schema / products |
| products.productname | Physical name retained; no saved recovered alias | TEXT | schema / products |
| products.supplierid | Physical name retained; no saved recovered alias | INTEGER | schema / products |
| products.categoryid | Physical name retained; no saved recovered alias | INTEGER | schema / products |
| products.quantityperunit | Physical name retained; no saved recovered alias | TEXT | schema / products |
| products.unitprice | Physical name retained; no saved recovered alias | REAL | schema / products |
| products.unitsinstock | Physical name retained; no saved recovered alias | INTEGER | schema / products |
| products.unitsonorder | Physical name retained; no saved recovered alias | INTEGER | schema / products |
| products.reorderlevel | Physical name retained; no saved recovered alias | INTEGER | schema / products |
| products.discontinued | Physical name retained; no saved recovered alias | INTEGER | schema / products |

## region

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| region.regionid | Physical name retained; no saved recovered alias | INTEGER | schema / region |
| region.regiondescription | Physical name retained; no saved recovered alias | TEXT | schema / region |

## shippers

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| shippers.shipperid | Physical name retained; no saved recovered alias | INTEGER | schema / shippers |
| shippers.companyname | Physical name retained; no saved recovered alias | TEXT | schema / shippers |
| shippers.phone | Physical name retained; no saved recovered alias | TEXT | schema / shippers |

## suppliers

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| suppliers.supplierid | Physical name retained; no saved recovered alias | INTEGER | schema / suppliers |
| suppliers.companyname | Physical name retained; no saved recovered alias | TEXT | schema / suppliers |
| suppliers.contactname | Physical name retained; no saved recovered alias | TEXT | schema / suppliers |
| suppliers.contacttitle | Physical name retained; no saved recovered alias | TEXT | schema / suppliers |
| suppliers.address | Physical name retained; no saved recovered alias | TEXT | schema / suppliers |
| suppliers.city | Physical name retained; no saved recovered alias | TEXT | schema / suppliers |
| suppliers.region | Physical name retained; no saved recovered alias | TEXT | schema / suppliers |
| suppliers.postalcode | Physical name retained; no saved recovered alias | TEXT | schema / suppliers |
| suppliers.country | Physical name retained; no saved recovered alias | TEXT | schema / suppliers |
| suppliers.phone | Physical name retained; no saved recovered alias | TEXT | schema / suppliers |
| suppliers.fax | Physical name retained; no saved recovered alias | TEXT | schema / suppliers |
| suppliers.homepage | Physical name retained; no saved recovered alias | TEXT | schema / suppliers |

## territories

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| territories.territoryid | Physical name retained; no saved recovered alias | TEXT | schema / territories |
| territories.territorydescription | Physical name retained; no saved recovered alias | TEXT | schema / territories |
| territories.regionid | Physical name retained; no saved recovered alias | INTEGER | schema / territories |

## usstates

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| usstates.stateid | Physical name retained; no saved recovered alias | INTEGER | schema / usstates |
| usstates.statename | Physical name retained; no saved recovered alias | TEXT | schema / usstates |
| usstates.stateabbr | Physical name retained; no saved recovered alias | TEXT | schema / usstates |
| usstates.stateregion | Physical name retained; no saved recovered alias | TEXT | schema / usstates |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

