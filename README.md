# Sistem Pemesanan Tiket Konser 🎟️

Program ini dibuat menggunakan **Python** untuk mensimulasikan sistem pemesanan tiket konser.

## 📌 Fitur:
- Memesan tiket dengan kategori **VIP**, **Reguler**, dan **Ekonomi**.
- Menampilkan total harga berdasarkan jumlah tiket.
- Mencatat waktu pemesanan menggunakan `datetime`.
- Menampilkan daftar pemesan setelah transaksi selesai.

## 🚀 Cara Menjalankan
1. Pastikan Python sudah terinstal (`python --version`).
2. Jalankan perintah berikut di terminal:
   ```sh
   python tiket_konser.py

## Library yang digunakanan
1. import random : Tidak digunakan secara eksplisit dalam kode saat ini, tetapi bisa digunakan untuk fitur tambahan seperti memilih pemenang undian.
2. import datetime : Digunakan untuk mencatat waktu pemesanan tiket.

## Struktur Data
1.  Dictionary daftar_tiket menyimpan kategori tiket beserta stoknya.
2. Dictionary harga_tiket menyimpan harga masing-masing kategori tiket.
3. daftar_pelanggan digunakan untuk mencatat pelanggan yang berhasil membeli tiket. Data pelanggan disimpan dalam bentuk tuple agar bersifat immutable (tidak bisa diubah setelah ditambahkan).

## Struktur Kontrol
1. Perulangan (while True) untuk menjalankan pemesanan secara berulang. Program akan terus berjalan hingga pengguna memilih untuk berhenti.
2. Perulangan (for) untuk menampilkan daftar tiket. Digunakan untuk mencetak jumlah tiket yang tersedia.
3. Percabangan (if-else) untuk mengecek ketersediaan tiket. Jika tiket tersedia, program akan menghitung total harga dan mengurangi stok. Jika tiket tidak tersedia atau kategori salah, program akan menampilkan pesan error.
4. Kontrol Perulangan (break) untuk keluar dari loop. Jika pengguna memilih 'n', maka perulangan dihentikan dengan break.
5. Perulangan (for) untuk menampilkan daftar pemesanan. Menampilkan hasil pesanan beserta waktu pemesanan menggunakan datetime.