import random
import datetime

def sistem_pemesanan_tiket():
    print("=== Sistem Pemesanan Tiket Konser ===")
    daftar_tiket = {"VIP": 5, "Reguler": 10, "Ekonomi": 15}  # Struktur Data: Dictionary
    harga_tiket = {"VIP": 500000, "Reguler": 250000, "Ekonomi": 100000}
    daftar_pelanggan = []  # Struktur Data: List
    
    while True:
        print("\nDaftar Tiket yang Tersedia:")
        for kategori, stok in daftar_tiket.items():
            print(f"{kategori}: {stok} tiket tersedia")
        
        nama = input("Masukkan nama pelanggan: ")
        kategori_tiket = input("Pilih kategori tiket (VIP/Reguler/Ekonomi): ").capitalize()
        jumlah = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
        
        if kategori_tiket in daftar_tiket and daftar_tiket[kategori_tiket] >= jumlah:
            total_harga = jumlah * harga_tiket[kategori_tiket]
            daftar_tiket[kategori_tiket] -= jumlah
            daftar_pelanggan.append((nama, kategori_tiket, jumlah, total_harga))
            print(f"\nTiket berhasil dipesan! Total harga: Rp{total_harga}")
        else:
            print("Maaf, tiket tidak mencukupi atau kategori tidak valid!")
        
        ulang = input("Ingin memesan lagi? (y/n): ").lower()
        if ulang == 'n':
            break
    
    print("\n=== Daftar Pemesanan ===")
    for pelanggan in daftar_pelanggan:
        nama, kategori, jumlah, total = pelanggan
        waktu_pemesanan = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Nama: {nama}, Kategori: {kategori}, Jumlah: {jumlah}, Total: Rp{total}, Waktu: {waktu_pemesanan}")
    
    print("\nTerima kasih telah menggunakan sistem pemesanan tiket!")

def main():
    sistem_pemesanan_tiket()
    
if __name__ == "__main__":
    main()
