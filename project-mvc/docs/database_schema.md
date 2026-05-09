\# Database Schema - Inventaris Layanan Lab Terpadu



\## Tabel Users

Digunakan untuk menyimpan data pengguna sistem.



Field:

\- id

\- username

\- email

\- password

\- role



\---



\## Tabel Inventaris

Digunakan untuk menyimpan data barang inventaris laboratorium.



Field:

\- id

\- nama\_barang

\- kategori

\- stok

\- kondisi

\- lokasi



\---



\## Tabel Peminjaman

Digunakan untuk mencatat proses peminjaman barang.



Field:

\- id

\- user\_id

\- inventaris\_id

\- tanggal\_pinjam

\- tanggal\_kembali

\- status

