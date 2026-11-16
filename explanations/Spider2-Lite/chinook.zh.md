# Spider2-Lite / chinook — Schema 与业务口径解释

该数据库的存档目录包含 11 张表、64 个物理列、0 条关系，以及 11 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## albums

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: a, al

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| albums.AlbumId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / albums |
| albums.Title | 保留物理名称；存档没有恢复别名 | NVARCHAR(160) | schema / albums |
| albums.ArtistId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / albums |

## artists

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: a

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| artists.ArtistId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / artists |
| artists.Name | 保留物理名称；存档没有恢复别名 | NVARCHAR(120) | schema / artists |

## customers

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: c

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| customers.CustomerId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / customers |
| customers.FirstName | 保留物理名称；存档没有恢复别名 | NVARCHAR(40) | schema / customers |
| customers.LastName | 保留物理名称；存档没有恢复别名 | NVARCHAR(20) | schema / customers |
| customers.Company | 保留物理名称；存档没有恢复别名 | NVARCHAR(80) | schema / customers |
| customers.Address | 保留物理名称；存档没有恢复别名 | NVARCHAR(70) | schema / customers |
| customers.City | 保留物理名称；存档没有恢复别名 | NVARCHAR(40) | schema / customers |
| customers.State | 保留物理名称；存档没有恢复别名 | NVARCHAR(40) | schema / customers |
| customers.Country | 保留物理名称；存档没有恢复别名 | NVARCHAR(40) | schema / customers |
| customers.PostalCode | 保留物理名称；存档没有恢复别名 | NVARCHAR(10) | schema / customers |
| customers.Phone | 保留物理名称；存档没有恢复别名 | NVARCHAR(24) | schema / customers |
| customers.Fax | 保留物理名称；存档没有恢复别名 | NVARCHAR(24) | schema / customers |
| customers.Email | 保留物理名称；存档没有恢复别名 | NVARCHAR(60) | schema / customers |
| customers.SupportRepId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / customers |

## employees

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| employees.EmployeeId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / employees |
| employees.LastName | 保留物理名称；存档没有恢复别名 | NVARCHAR(20) | schema / employees |
| employees.FirstName | 保留物理名称；存档没有恢复别名 | NVARCHAR(20) | schema / employees |
| employees.Title | 保留物理名称；存档没有恢复别名 | NVARCHAR(30) | schema / employees |
| employees.ReportsTo | 保留物理名称；存档没有恢复别名 | INTEGER | schema / employees |
| employees.BirthDate | 保留物理名称；存档没有恢复别名 | DATETIME | schema / employees |
| employees.HireDate | 保留物理名称；存档没有恢复别名 | DATETIME | schema / employees |
| employees.Address | 保留物理名称；存档没有恢复别名 | NVARCHAR(70) | schema / employees |
| employees.City | 保留物理名称；存档没有恢复别名 | NVARCHAR(40) | schema / employees |
| employees.State | 保留物理名称；存档没有恢复别名 | NVARCHAR(40) | schema / employees |
| employees.Country | 保留物理名称；存档没有恢复别名 | NVARCHAR(40) | schema / employees |
| employees.PostalCode | 保留物理名称；存档没有恢复别名 | NVARCHAR(10) | schema / employees |
| employees.Phone | 保留物理名称；存档没有恢复别名 | NVARCHAR(24) | schema / employees |
| employees.Fax | 保留物理名称；存档没有恢复别名 | NVARCHAR(24) | schema / employees |
| employees.Email | 保留物理名称；存档没有恢复别名 | NVARCHAR(60) | schema / employees |

## genres

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| genres.GenreId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / genres |
| genres.Name | 保留物理名称；存档没有恢复别名 | NVARCHAR(120) | schema / genres |

## invoice_items

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: ii

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| invoice_items.InvoiceLineId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / invoice_items |
| invoice_items.InvoiceId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / invoice_items |
| invoice_items.TrackId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / invoice_items |
| invoice_items.UnitPrice | 保留物理名称；存档没有恢复别名 | NUMERIC(10,2) | schema / invoice_items |
| invoice_items.Quantity | 保留物理名称；存档没有恢复别名 | INTEGER | schema / invoice_items |

## invoices

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: i, inv

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| invoices.InvoiceId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / invoices |
| invoices.CustomerId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / invoices |
| invoices.InvoiceDate | 保留物理名称；存档没有恢复别名 | DATETIME | schema / invoices |
| invoices.BillingAddress | 保留物理名称；存档没有恢复别名 | NVARCHAR(70) | schema / invoices |
| invoices.BillingCity | 保留物理名称；存档没有恢复别名 | NVARCHAR(40) | schema / invoices |
| invoices.BillingState | 保留物理名称；存档没有恢复别名 | NVARCHAR(40) | schema / invoices |
| invoices.BillingCountry | 保留物理名称；存档没有恢复别名 | NVARCHAR(40) | schema / invoices |
| invoices.BillingPostalCode | 保留物理名称；存档没有恢复别名 | NVARCHAR(10) | schema / invoices |
| invoices.Total | 保留物理名称；存档没有恢复别名 | NUMERIC(10,2) | schema / invoices |

## media_types

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| media_types.MediaTypeId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / media_types |
| media_types.Name | 保留物理名称；存档没有恢复别名 | NVARCHAR(120) | schema / media_types |

## playlist_track

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| playlist_track.PlaylistId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / playlist_track |
| playlist_track.TrackId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / playlist_track |

## playlists

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| playlists.PlaylistId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / playlists |
| playlists.Name | 保留物理名称；存档没有恢复别名 | NVARCHAR(120) | schema / playlists |

## tracks

该表的存档未记录额外业务说明。

恢复表名: —
SQL表别名: t

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| tracks.TrackId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / tracks |
| tracks.Name | 保留物理名称；存档没有恢复别名 | NVARCHAR(200) | schema / tracks |
| tracks.AlbumId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / tracks |
| tracks.MediaTypeId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / tracks |
| tracks.GenreId | 保留物理名称；存档没有恢复别名 | INTEGER | schema / tracks |
| tracks.Composer | 保留物理名称；存档没有恢复别名 | NVARCHAR(220) | schema / tracks |
| tracks.Milliseconds | 保留物理名称；存档没有恢复别名 | INTEGER | schema / tracks |
| tracks.Bytes | 保留物理名称；存档没有恢复别名 | INTEGER | schema / tracks |
| tracks.UnitPrice | 保留物理名称；存档没有恢复别名 | NUMERIC(10,2) | schema / tracks |

## 表关系与连接依据


## 业务口径、总体与粒度


## 增量维护事件

