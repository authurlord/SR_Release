# Spider2-Lite / music — Schema and business semantics

The saved catalogue for this database contains 11 tables, 64 physical columns, 0 relationships and 11 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## Album

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Album.AlbumId | Physical name retained; no saved recovered alias | INTEGER | schema / Album |
| Album.Title | Physical name retained; no saved recovered alias | NVARCHAR(160) | schema / Album |
| Album.ArtistId | Physical name retained; no saved recovered alias | INTEGER | schema / Album |

## Artist

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Artist.ArtistId | Physical name retained; no saved recovered alias | INTEGER | schema / Artist |
| Artist.Name | Physical name retained; no saved recovered alias | NVARCHAR(120) | schema / Artist |

## Customer

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Customer.CustomerId | Physical name retained; no saved recovered alias | INTEGER | schema / Customer |
| Customer.FirstName | Physical name retained; no saved recovered alias | NVARCHAR(40) | schema / Customer |
| Customer.LastName | Physical name retained; no saved recovered alias | NVARCHAR(20) | schema / Customer |
| Customer.Company | Physical name retained; no saved recovered alias | NVARCHAR(80) | schema / Customer |
| Customer.Address | Physical name retained; no saved recovered alias | NVARCHAR(70) | schema / Customer |
| Customer.City | Physical name retained; no saved recovered alias | NVARCHAR(40) | schema / Customer |
| Customer.State | Physical name retained; no saved recovered alias | NVARCHAR(40) | schema / Customer |
| Customer.Country | Physical name retained; no saved recovered alias | NVARCHAR(40) | schema / Customer |
| Customer.PostalCode | Physical name retained; no saved recovered alias | NVARCHAR(10) | schema / Customer |
| Customer.Phone | Physical name retained; no saved recovered alias | NVARCHAR(24) | schema / Customer |
| Customer.Fax | Physical name retained; no saved recovered alias | NVARCHAR(24) | schema / Customer |
| Customer.Email | Physical name retained; no saved recovered alias | NVARCHAR(60) | schema / Customer |
| Customer.SupportRepId | Physical name retained; no saved recovered alias | INTEGER | schema / Customer |

## Employee

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Employee.EmployeeId | Physical name retained; no saved recovered alias | INTEGER | schema / Employee |
| Employee.LastName | Physical name retained; no saved recovered alias | NVARCHAR(20) | schema / Employee |
| Employee.FirstName | Physical name retained; no saved recovered alias | NVARCHAR(20) | schema / Employee |
| Employee.Title | Physical name retained; no saved recovered alias | NVARCHAR(30) | schema / Employee |
| Employee.ReportsTo | Physical name retained; no saved recovered alias | INTEGER | schema / Employee |
| Employee.BirthDate | Physical name retained; no saved recovered alias | DATETIME | schema / Employee |
| Employee.HireDate | Physical name retained; no saved recovered alias | DATETIME | schema / Employee |
| Employee.Address | Physical name retained; no saved recovered alias | NVARCHAR(70) | schema / Employee |
| Employee.City | Physical name retained; no saved recovered alias | NVARCHAR(40) | schema / Employee |
| Employee.State | Physical name retained; no saved recovered alias | NVARCHAR(40) | schema / Employee |
| Employee.Country | Physical name retained; no saved recovered alias | NVARCHAR(40) | schema / Employee |
| Employee.PostalCode | Physical name retained; no saved recovered alias | NVARCHAR(10) | schema / Employee |
| Employee.Phone | Physical name retained; no saved recovered alias | NVARCHAR(24) | schema / Employee |
| Employee.Fax | Physical name retained; no saved recovered alias | NVARCHAR(24) | schema / Employee |
| Employee.Email | Physical name retained; no saved recovered alias | NVARCHAR(60) | schema / Employee |

## Genre

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Genre.GenreId | Physical name retained; no saved recovered alias | INTEGER | schema / Genre |
| Genre.Name | Physical name retained; no saved recovered alias | NVARCHAR(120) | schema / Genre |

## Invoice

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Invoice.InvoiceId | Physical name retained; no saved recovered alias | INTEGER | schema / Invoice |
| Invoice.CustomerId | Physical name retained; no saved recovered alias | INTEGER | schema / Invoice |
| Invoice.InvoiceDate | Physical name retained; no saved recovered alias | DATETIME | schema / Invoice |
| Invoice.BillingAddress | Physical name retained; no saved recovered alias | NVARCHAR(70) | schema / Invoice |
| Invoice.BillingCity | Physical name retained; no saved recovered alias | NVARCHAR(40) | schema / Invoice |
| Invoice.BillingState | Physical name retained; no saved recovered alias | NVARCHAR(40) | schema / Invoice |
| Invoice.BillingCountry | Physical name retained; no saved recovered alias | NVARCHAR(40) | schema / Invoice |
| Invoice.BillingPostalCode | Physical name retained; no saved recovered alias | NVARCHAR(10) | schema / Invoice |
| Invoice.Total | Physical name retained; no saved recovered alias | NUMERIC(10,2) | schema / Invoice |

## InvoiceLine

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: il

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| InvoiceLine.InvoiceLineId | Physical name retained; no saved recovered alias | INTEGER | schema / InvoiceLine |
| InvoiceLine.InvoiceId | Physical name retained; no saved recovered alias | INTEGER | schema / InvoiceLine |
| InvoiceLine.TrackId | Physical name retained; no saved recovered alias | INTEGER | schema / InvoiceLine |
| InvoiceLine.UnitPrice | Physical name retained; no saved recovered alias | NUMERIC(10,2) | schema / InvoiceLine |
| InvoiceLine.Quantity | Physical name retained; no saved recovered alias | INTEGER | schema / InvoiceLine |

## MediaType

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| MediaType.MediaTypeId | Physical name retained; no saved recovered alias | INTEGER | schema / MediaType |
| MediaType.Name | Physical name retained; no saved recovered alias | NVARCHAR(120) | schema / MediaType |

## Playlist

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Playlist.PlaylistId | Physical name retained; no saved recovered alias | INTEGER | schema / Playlist |
| Playlist.Name | Physical name retained; no saved recovered alias | NVARCHAR(120) | schema / Playlist |

## PlaylistTrack

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| PlaylistTrack.PlaylistId | Physical name retained; no saved recovered alias | INTEGER | schema / PlaylistTrack |
| PlaylistTrack.TrackId | Physical name retained; no saved recovered alias | INTEGER | schema / PlaylistTrack |

## Track

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: t

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Track.TrackId | Physical name retained; no saved recovered alias | INTEGER | schema / Track |
| Track.Name | Physical name retained; no saved recovered alias | NVARCHAR(200) | schema / Track |
| Track.AlbumId | Physical name retained; no saved recovered alias | INTEGER | schema / Track |
| Track.MediaTypeId | Physical name retained; no saved recovered alias | INTEGER | schema / Track |
| Track.GenreId | Physical name retained; no saved recovered alias | INTEGER | schema / Track |
| Track.Composer | Physical name retained; no saved recovered alias | NVARCHAR(220) | schema / Track |
| Track.Milliseconds | Physical name retained; no saved recovered alias | INTEGER | schema / Track |
| Track.Bytes | Physical name retained; no saved recovered alias | INTEGER | schema / Track |
| Track.UnitPrice | Physical name retained; no saved recovered alias | NUMERIC(10,2) | schema / Track |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

