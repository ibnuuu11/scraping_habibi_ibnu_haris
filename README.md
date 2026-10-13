# Web Scraping Python

**Nama:** Habibi Ibnu Haris

## Deskripsi
Proyek ini dibuat untuk mempelajari teknik web scraping menggunakan Python. Program mengambil informasi dari website menggunakan library `requests` dan `BeautifulSoup`, kemudian menyimpan data hasil scraping ke dalam file CSV.

## Teknologi yang Digunakan
- Python
- Requests
- BeautifulSoup4
- Pandas

## Fitur
- Mengakses halaman website.
- Mengambil judul halaman website.
- Mencari elemen HTML seperti `h1` dan `h2`.
- Membandingkan parser HTML.
- Menangani HTTP Error dan URL Error.
- Menyimpan hasil scraping ke file CSV.

## Cara Menjalankan
1. Pastikan Python sudah terinstal.
2. Instal library yang diperlukan:

   ```bash
   pip install requests beautifulsoup4 pandas lxml
   ```

3. Jalankan program:

   ```bash
   python scraping.py
   ```

4. Periksa file CSV yang dihasilkan di folder proyek.

## File Proyek
- `scraping.py` — kode program web scraping.
- `detik.csv` — data hasil scraping dalam format CSV.
- `README.md` — dokumentasi proyek.

## Penulis
Habibi Ibnu Haris
