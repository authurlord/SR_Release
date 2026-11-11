# Spider2-Lite / northwind — Schema 与业务口径解释

该数据库的存档目录包含 15 张表、95 个物理列、0 条关系，以及 15 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## categories

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| categories.categoryid | 保留物理名称；存档没有恢复别名 | INTEGER | schema / categories |
| categories.categoryname | 保留物理名称；存档没有恢复别名 | TEXT | schema / categories |
| categories.description | 保留物理名称；存档没有恢复别名 | TEXT | schema / categories |
| categories.picture | 保留物理名称；存档没有恢复别名 | BLOB | schema / categories |

## customercustomerdemo

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| customercustomerdemo.customerid | 保留物理名称；存档没有恢复别名 | TEXT | schema / customercustomerdemo |
| customercustomerdemo.customertypeid | 保留物理名称；存档没有恢复别名 | TEXT | schema / customercustomerdemo |

## customerdemographics

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| customerdemographics.customertypeid | 保留物理名称；存档没有恢复别名 | TEXT | schema / customerdemographics |
| customerdemographics.customerdesc | 保留物理名称；存档没有恢复别名 | TEXT | schema / customerdemographics |

## customergroupthreshold

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: g

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| customergroupthreshold.groupname | 保留物理名称；存档没有恢复别名 | TEXT | schema / customergroupthreshold |
| customergroupthreshold.rangebottom | 保留物理名称；存档没有恢复别名 | DECIMAL | schema / customergroupthreshold |
| customergroupthreshold.rangetop | 保留物理名称；存档没有恢复别名 | DECIMAL | schema / customergroupthreshold |

## customers

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| customers.customerid | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.companyname | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.contactname | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.contacttitle | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.address | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.city | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.region | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.postalcode | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.country | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.phone | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |
| customers.fax | 保留物理名称；存档没有恢复别名 | TEXT | schema / customers |

## employees

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| employees.employeeid | 保留物理名称；存档没有恢复别名 | INTEGER | schema / employees |
| employees.lastname | 保留物理名称；存档没有恢复别名 | TEXT | schema / employees |
| employees.firstname | 保留物理名称；存档没有恢复别名 | TEXT | schema / employees |
| employees.title | 保留物理名称；存档没有恢复别名 | TEXT | schema / employees |
| employees.titleofcourtesy | 保留物理名称；存档没有恢复别名 | TEXT | schema / employees |
| employees.birthdate | 保留物理名称；存档没有恢复别名 | DATE | schema / employees |
| employees.hiredate | 保留物理名称；存档没有恢复别名 | DATE | schema / employees |
| employees.address | 保留物理名称；存档没有恢复别名 | TEXT | schema / employees |
| employees.city | 保留物理名称；存档没有恢复别名 | TEXT | schema / employees |
| employees.region | 保留物理名称；存档没有恢复别名 | TEXT | schema / employees |
| employees.postalcode | 保留物理名称；存档没有恢复别名 | TEXT | schema / employees |
| employees.country | 保留物理名称；存档没有恢复别名 | TEXT | schema / employees |
| employees.homephone | 保留物理名称；存档没有恢复别名 | TEXT | schema / employees |
| employees.extension | 保留物理名称；存档没有恢复别名 | TEXT | schema / employees |
| employees.photo | 保留物理名称；存档没有恢复别名 | BLOB | schema / employees |
| employees.notes | 保留物理名称；存档没有恢复别名 | TEXT | schema / employees |
| employees.reportsto | 保留物理名称；存档没有恢复别名 | INTEGER | schema / employees |
| employees.photopath | 保留物理名称；存档没有恢复别名 | TEXT | schema / employees |

## employeeterritories

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| employeeterritories.employeeid | 保留物理名称；存档没有恢复别名 | INTEGER | schema / employeeterritories |
| employeeterritories.territoryid | 保留物理名称；存档没有恢复别名 | TEXT | schema / employeeterritories |

## order_details

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: od

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| order_details.orderid | 保留物理名称；存档没有恢复别名 | INTEGER | schema / order_details |
| order_details.productid | 保留物理名称；存档没有恢复别名 | INTEGER | schema / order_details |
| order_details.unitprice | 保留物理名称；存档没有恢复别名 | REAL | schema / order_details |
| order_details.quantity | 保留物理名称；存档没有恢复别名 | INTEGER | schema / order_details |
| order_details.discount | 保留物理名称；存档没有恢复别名 | REAL | schema / order_details |

## orders

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: o

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| orders.orderid | 保留物理名称；存档没有恢复别名 | INTEGER | schema / orders |
| orders.customerid | 保留物理名称；存档没有恢复别名 | TEXT | schema / orders |
| orders.employeeid | 保留物理名称；存档没有恢复别名 | INTEGER | schema / orders |
| orders.orderdate | 保留物理名称；存档没有恢复别名 | DATE | schema / orders |
| orders.requireddate | 保留物理名称；存档没有恢复别名 | DATE | schema / orders |
| orders.shippeddate | 保留物理名称；存档没有恢复别名 | DATE | schema / orders |
| orders.shipvia | 保留物理名称；存档没有恢复别名 | INTEGER | schema / orders |
| orders.freight | 保留物理名称；存档没有恢复别名 | REAL | schema / orders |
| orders.shipname | 保留物理名称；存档没有恢复别名 | TEXT | schema / orders |
| orders.shipaddress | 保留物理名称；存档没有恢复别名 | TEXT | schema / orders |
| orders.shipcity | 保留物理名称；存档没有恢复别名 | TEXT | schema / orders |
| orders.shipregion | 保留物理名称；存档没有恢复别名 | TEXT | schema / orders |
| orders.shippostalcode | 保留物理名称；存档没有恢复别名 | TEXT | schema / orders |
| orders.shipcountry | 保留物理名称；存档没有恢复别名 | TEXT | schema / orders |

## products

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| products.productid | 保留物理名称；存档没有恢复别名 | INTEGER | schema / products |
| products.productname | 保留物理名称；存档没有恢复别名 | TEXT | schema / products |
| products.supplierid | 保留物理名称；存档没有恢复别名 | INTEGER | schema / products |
| products.categoryid | 保留物理名称；存档没有恢复别名 | INTEGER | schema / products |
| products.quantityperunit | 保留物理名称；存档没有恢复别名 | TEXT | schema / products |
| products.unitprice | 保留物理名称；存档没有恢复别名 | REAL | schema / products |
| products.unitsinstock | 保留物理名称；存档没有恢复别名 | INTEGER | schema / products |
| products.unitsonorder | 保留物理名称；存档没有恢复别名 | INTEGER | schema / products |
| products.reorderlevel | 保留物理名称；存档没有恢复别名 | INTEGER | schema / products |
| products.discontinued | 保留物理名称；存档没有恢复别名 | INTEGER | schema / products |

## region

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| region.regionid | 保留物理名称；存档没有恢复别名 | INTEGER | schema / region |
| region.regiondescription | 保留物理名称；存档没有恢复别名 | TEXT | schema / region |

## shippers

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shippers.shipperid | 保留物理名称；存档没有恢复别名 | INTEGER | schema / shippers |
| shippers.companyname | 保留物理名称；存档没有恢复别名 | TEXT | schema / shippers |
| shippers.phone | 保留物理名称；存档没有恢复别名 | TEXT | schema / shippers |

## suppliers

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| suppliers.supplierid | 保留物理名称；存档没有恢复别名 | INTEGER | schema / suppliers |
| suppliers.companyname | 保留物理名称；存档没有恢复别名 | TEXT | schema / suppliers |
| suppliers.contactname | 保留物理名称；存档没有恢复别名 | TEXT | schema / suppliers |
| suppliers.contacttitle | 保留物理名称；存档没有恢复别名 | TEXT | schema / suppliers |
| suppliers.address | 保留物理名称；存档没有恢复别名 | TEXT | schema / suppliers |
| suppliers.city | 保留物理名称；存档没有恢复别名 | TEXT | schema / suppliers |
| suppliers.region | 保留物理名称；存档没有恢复别名 | TEXT | schema / suppliers |
| suppliers.postalcode | 保留物理名称；存档没有恢复别名 | TEXT | schema / suppliers |
| suppliers.country | 保留物理名称；存档没有恢复别名 | TEXT | schema / suppliers |
| suppliers.phone | 保留物理名称；存档没有恢复别名 | TEXT | schema / suppliers |
| suppliers.fax | 保留物理名称；存档没有恢复别名 | TEXT | schema / suppliers |
| suppliers.homepage | 保留物理名称；存档没有恢复别名 | TEXT | schema / suppliers |

## territories

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| territories.territoryid | 保留物理名称；存档没有恢复别名 | TEXT | schema / territories |
| territories.territorydescription | 保留物理名称；存档没有恢复别名 | TEXT | schema / territories |
| territories.regionid | 保留物理名称；存档没有恢复别名 | INTEGER | schema / territories |

## usstates

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| usstates.stateid | 保留物理名称；存档没有恢复别名 | INTEGER | schema / usstates |
| usstates.statename | 保留物理名称；存档没有恢复别名 | TEXT | schema / usstates |
| usstates.stateabbr | 保留物理名称；存档没有恢复别名 | TEXT | schema / usstates |
| usstates.stateregion | 保留物理名称；存档没有恢复别名 | TEXT | schema / usstates |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

