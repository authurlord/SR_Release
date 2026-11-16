# Spider2-Lite / chinook — Schema and business semantics

The saved catalogue for this database contains 11 tables, 64 physical columns, 0 relationships and 11 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## albums

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: a, al

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| albums.AlbumId | Physical name retained; no saved recovered alias | INTEGER | schema / albums |
| albums.Title | Physical name retained; no saved recovered alias | NVARCHAR(160) | schema / albums |
| albums.ArtistId | Physical name retained; no saved recovered alias | INTEGER | schema / albums |

## artists

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: a

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| artists.ArtistId | Physical name retained; no saved recovered alias | INTEGER | schema / artists |
| artists.Name | Physical name retained; no saved recovered alias | NVARCHAR(120) | schema / artists |

## customers

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: c

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| customers.CustomerId | Physical name retained; no saved recovered alias | INTEGER | schema / customers |
| customers.FirstName | Physical name retained; no saved recovered alias | NVARCHAR(40) | schema / customers |
| customers.LastName | Physical name retained; no saved recovered alias | NVARCHAR(20) | schema / customers |
| customers.Company | Physical name retained; no saved recovered alias | NVARCHAR(80) | schema / customers |
| customers.Address | Physical name retained; no saved recovered alias | NVARCHAR(70) | schema / customers |
| customers.City | Physical name retained; no saved recovered alias | NVARCHAR(40) | schema / customers |
| customers.State | Physical name retained; no saved recovered alias | NVARCHAR(40) | schema / customers |
| customers.Country | Physical name retained; no saved recovered alias | NVARCHAR(40) | schema / customers |
| customers.PostalCode | Physical name retained; no saved recovered alias | NVARCHAR(10) | schema / customers |
| customers.Phone | Physical name retained; no saved recovered alias | NVARCHAR(24) | schema / customers |
| customers.Fax | Physical name retained; no saved recovered alias | NVARCHAR(24) | schema / customers |
| customers.Email | Physical name retained; no saved recovered alias | NVARCHAR(60) | schema / customers |
| customers.SupportRepId | Physical name retained; no saved recovered alias | INTEGER | schema / customers |

## employees

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| employees.EmployeeId | Physical name retained; no saved recovered alias | INTEGER | schema / employees |
| employees.LastName | Physical name retained; no saved recovered alias | NVARCHAR(20) | schema / employees |
| employees.FirstName | Physical name retained; no saved recovered alias | NVARCHAR(20) | schema / employees |
| employees.Title | Physical name retained; no saved recovered alias | NVARCHAR(30) | schema / employees |
| employees.ReportsTo | Physical name retained; no saved recovered alias | INTEGER | schema / employees |
| employees.BirthDate | Physical name retained; no saved recovered alias | DATETIME | schema / employees |
| employees.HireDate | Physical name retained; no saved recovered alias | DATETIME | schema / employees |
| employees.Address | Physical name retained; no saved recovered alias | NVARCHAR(70) | schema / employees |
| employees.City | Physical name retained; no saved recovered alias | NVARCHAR(40) | schema / employees |
| employees.State | Physical name retained; no saved recovered alias | NVARCHAR(40) | schema / employees |
| employees.Country | Physical name retained; no saved recovered alias | NVARCHAR(40) | schema / employees |
| employees.PostalCode | Physical name retained; no saved recovered alias | NVARCHAR(10) | schema / employees |
| employees.Phone | Physical name retained; no saved recovered alias | NVARCHAR(24) | schema / employees |
| employees.Fax | Physical name retained; no saved recovered alias | NVARCHAR(24) | schema / employees |
| employees.Email | Physical name retained; no saved recovered alias | NVARCHAR(60) | schema / employees |

## genres

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| genres.GenreId | Physical name retained; no saved recovered alias | INTEGER | schema / genres |
| genres.Name | Physical name retained; no saved recovered alias | NVARCHAR(120) | schema / genres |

## invoice_items

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: ii

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| invoice_items.InvoiceLineId | Physical name retained; no saved recovered alias | INTEGER | schema / invoice_items |
| invoice_items.InvoiceId | Physical name retained; no saved recovered alias | INTEGER | schema / invoice_items |
| invoice_items.TrackId | Physical name retained; no saved recovered alias | INTEGER | schema / invoice_items |
| invoice_items.UnitPrice | Physical name retained; no saved recovered alias | NUMERIC(10,2) | schema / invoice_items |
| invoice_items.Quantity | Physical name retained; no saved recovered alias | INTEGER | schema / invoice_items |

## invoices

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: i, inv

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| invoices.InvoiceId | Physical name retained; no saved recovered alias | INTEGER | schema / invoices |
| invoices.CustomerId | Physical name retained; no saved recovered alias | INTEGER | schema / invoices |
| invoices.InvoiceDate | Physical name retained; no saved recovered alias | DATETIME | schema / invoices |
| invoices.BillingAddress | Physical name retained; no saved recovered alias | NVARCHAR(70) | schema / invoices |
| invoices.BillingCity | Physical name retained; no saved recovered alias | NVARCHAR(40) | schema / invoices |
| invoices.BillingState | Physical name retained; no saved recovered alias | NVARCHAR(40) | schema / invoices |
| invoices.BillingCountry | Physical name retained; no saved recovered alias | NVARCHAR(40) | schema / invoices |
| invoices.BillingPostalCode | Physical name retained; no saved recovered alias | NVARCHAR(10) | schema / invoices |
| invoices.Total | Physical name retained; no saved recovered alias | NUMERIC(10,2) | schema / invoices |

## media_types

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| media_types.MediaTypeId | Physical name retained; no saved recovered alias | INTEGER | schema / media_types |
| media_types.Name | Physical name retained; no saved recovered alias | NVARCHAR(120) | schema / media_types |

## playlist_track

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| playlist_track.PlaylistId | Physical name retained; no saved recovered alias | INTEGER | schema / playlist_track |
| playlist_track.TrackId | Physical name retained; no saved recovered alias | INTEGER | schema / playlist_track |

## playlists

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: —

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| playlists.PlaylistId | Physical name retained; no saved recovered alias | INTEGER | schema / playlists |
| playlists.Name | Physical name retained; no saved recovered alias | NVARCHAR(120) | schema / playlists |

## tracks

No additional table purpose is recorded in this archive.

Recovered table names: —
SQL table aliases: t

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| tracks.TrackId | Physical name retained; no saved recovered alias | INTEGER | schema / tracks |
| tracks.Name | Physical name retained; no saved recovered alias | NVARCHAR(200) | schema / tracks |
| tracks.AlbumId | Physical name retained; no saved recovered alias | INTEGER | schema / tracks |
| tracks.MediaTypeId | Physical name retained; no saved recovered alias | INTEGER | schema / tracks |
| tracks.GenreId | Physical name retained; no saved recovered alias | INTEGER | schema / tracks |
| tracks.Composer | Physical name retained; no saved recovered alias | NVARCHAR(220) | schema / tracks |
| tracks.Milliseconds | Physical name retained; no saved recovered alias | INTEGER | schema / tracks |
| tracks.Bytes | Physical name retained; no saved recovered alias | INTEGER | schema / tracks |
| tracks.UnitPrice | Physical name retained; no saved recovered alias | NUMERIC(10,2) | schema / tracks |

## Relationships and join evidence


## Business definitions, population and grain


## Incremental maintenance events

