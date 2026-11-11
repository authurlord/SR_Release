# Spider2-Lite / music — Schema 与业务口径解释

该数据库的存档目录包含 11 张表、64 个物理列、0 条关系，以及 11 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## Album

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Album.AlbumId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Album |
| Album.Title | 保留物理名称；存档没有恢复别名 | NVARCHAR(160) | schema / Album |
| Album.ArtistId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Album |

## Artist

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Artist.ArtistId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Artist |
| Artist.Name | 保留物理名称；存档没有恢复别名 | NVARCHAR(120) | schema / Artist |

## Customer

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Customer.CustomerId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Customer |
| Customer.FirstName | 保留物理名称；存档没有恢复别名 | NVARCHAR(40) | schema / Customer |
| Customer.LastName | 保留物理名称；存档没有恢复别名 | NVARCHAR(20) | schema / Customer |
| Customer.Company | 保留物理名称；存档没有恢复别名 | NVARCHAR(80) | schema / Customer |
| Customer.Address | 保留物理名称；存档没有恢复别名 | NVARCHAR(70) | schema / Customer |
| Customer.City | 保留物理名称；存档没有恢复别名 | NVARCHAR(40) | schema / Customer |
| Customer.State | 保留物理名称；存档没有恢复别名 | NVARCHAR(40) | schema / Customer |
| Customer.Country | 保留物理名称；存档没有恢复别名 | NVARCHAR(40) | schema / Customer |
| Customer.PostalCode | 保留物理名称；存档没有恢复别名 | NVARCHAR(10) | schema / Customer |
| Customer.Phone | 保留物理名称；存档没有恢复别名 | NVARCHAR(24) | schema / Customer |
| Customer.Fax | 保留物理名称；存档没有恢复别名 | NVARCHAR(24) | schema / Customer |
| Customer.Email | 保留物理名称；存档没有恢复别名 | NVARCHAR(60) | schema / Customer |
| Customer.SupportRepId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Customer |

## Employee

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Employee.EmployeeId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Employee |
| Employee.LastName | 保留物理名称；存档没有恢复别名 | NVARCHAR(20) | schema / Employee |
| Employee.FirstName | 保留物理名称；存档没有恢复别名 | NVARCHAR(20) | schema / Employee |
| Employee.Title | 保留物理名称；存档没有恢复别名 | NVARCHAR(30) | schema / Employee |
| Employee.ReportsTo | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Employee |
| Employee.BirthDate | 保留物理名称；存档没有恢复别名 | DATETIME | schema / Employee |
| Employee.HireDate | 保留物理名称；存档没有恢复别名 | DATETIME | schema / Employee |
| Employee.Address | 保留物理名称；存档没有恢复别名 | NVARCHAR(70) | schema / Employee |
| Employee.City | 保留物理名称；存档没有恢复别名 | NVARCHAR(40) | schema / Employee |
| Employee.State | 保留物理名称；存档没有恢复别名 | NVARCHAR(40) | schema / Employee |
| Employee.Country | 保留物理名称；存档没有恢复别名 | NVARCHAR(40) | schema / Employee |
| Employee.PostalCode | 保留物理名称；存档没有恢复别名 | NVARCHAR(10) | schema / Employee |
| Employee.Phone | 保留物理名称；存档没有恢复别名 | NVARCHAR(24) | schema / Employee |
| Employee.Fax | 保留物理名称；存档没有恢复别名 | NVARCHAR(24) | schema / Employee |
| Employee.Email | 保留物理名称；存档没有恢复别名 | NVARCHAR(60) | schema / Employee |

## Genre

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Genre.GenreId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Genre |
| Genre.Name | 保留物理名称；存档没有恢复别名 | NVARCHAR(120) | schema / Genre |

## Invoice

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Invoice.InvoiceId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Invoice |
| Invoice.CustomerId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Invoice |
| Invoice.InvoiceDate | 保留物理名称；存档没有恢复别名 | DATETIME | schema / Invoice |
| Invoice.BillingAddress | 保留物理名称；存档没有恢复别名 | NVARCHAR(70) | schema / Invoice |
| Invoice.BillingCity | 保留物理名称；存档没有恢复别名 | NVARCHAR(40) | schema / Invoice |
| Invoice.BillingState | 保留物理名称；存档没有恢复别名 | NVARCHAR(40) | schema / Invoice |
| Invoice.BillingCountry | 保留物理名称；存档没有恢复别名 | NVARCHAR(40) | schema / Invoice |
| Invoice.BillingPostalCode | 保留物理名称；存档没有恢复别名 | NVARCHAR(10) | schema / Invoice |
| Invoice.Total | 保留物理名称；存档没有恢复别名 | NUMERIC(10,2) | schema / Invoice |

## InvoiceLine

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: il

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| InvoiceLine.InvoiceLineId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / InvoiceLine |
| InvoiceLine.InvoiceId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / InvoiceLine |
| InvoiceLine.TrackId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / InvoiceLine |
| InvoiceLine.UnitPrice | 保留物理名称；存档没有恢复别名 | NUMERIC(10,2) | schema / InvoiceLine |
| InvoiceLine.Quantity | 保留物理名称；存档没有恢复别名 | INTEGER | schema / InvoiceLine |

## MediaType

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| MediaType.MediaTypeId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / MediaType |
| MediaType.Name | 保留物理名称；存档没有恢复别名 | NVARCHAR(120) | schema / MediaType |

## Playlist

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Playlist.PlaylistId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Playlist |
| Playlist.Name | 保留物理名称；存档没有恢复别名 | NVARCHAR(120) | schema / Playlist |

## PlaylistTrack

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| PlaylistTrack.PlaylistId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / PlaylistTrack |
| PlaylistTrack.TrackId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / PlaylistTrack |

## Track

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: t

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| Track.TrackId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Track |
| Track.Name | 保留物理名称；存档没有恢复别名 | NVARCHAR(200) | schema / Track |
| Track.AlbumId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Track |
| Track.MediaTypeId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Track |
| Track.GenreId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Track |
| Track.Composer | 保留物理名称；存档没有恢复别名 | NVARCHAR(220) | schema / Track |
| Track.Milliseconds | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Track |
| Track.Bytes | 保留物理名称；存档没有恢复别名 | INTEGER | schema / Track |
| Track.UnitPrice | 保留物理名称；存档没有恢复别名 | NUMERIC(10,2) | schema / Track |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

