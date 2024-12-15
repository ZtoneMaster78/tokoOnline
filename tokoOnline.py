import os

# Fungsi untuk membersihkan layar terminal
def layar_bersih():
    os.system("cls" if os.name == "nt" else "clear")

# Fungsi untuk mencetak garis horizontal sebagai pemisah
def garis(tebal=True):
    print("=" * 57 if tebal else "-" * 57)

# Fungsi untuk memformat angka menjadi mata uang Rupiah dengan batas lebar tertentu
def format_rupiah(angka, batas=20):
    return f"{f'Rp{angka:,.0f}'.replace(',', '.'): <{batas}}"

# Fungsi untuk menghitung total belanja berdasarkan harga dan kuantitas setiap barang
def hitung_total_belanja(daftar_barang):
    return sum(barang['harga'] * barang['kuantitas'] for barang in daftar_barang)

# Fungsi untuk menghitung diskon jika total belanja melebihi Rp200.000
def hitung_diskon(total):
    return total * 0.1 if total > 200000 else 0

# Fungsi untuk menampilkan daftar barang, subtotal, total belanja, dan diskon
def tampil_daftar(daftar_barang):
    layar_bersih()
    garis()
    print(f"{'Toko Online':^57}")
    garis()

    # Header tabel daftar barang
    print(f"{'No':<3} {'Pakaian':<10} {'Harga':<10} {'Kuantitas':^10} {'Subtotal':^20}")
    garis(tebal=False)

    # Menampilkan setiap barang dengan detail harga, kuantitas, dan subtotal
    for index, barang in enumerate(daftar_barang, start=1):
        print(f"{index:<3} {barang['nama']:<10} {format_rupiah(barang['harga'], batas=10)} {barang['kuantitas']:^10} {format_rupiah(barang['harga'] * barang['kuantitas'])}")

    garis()

    # Menghitung total belanja, diskon, dan total akhir
    total_belanja = hitung_total_belanja(daftar_barang)
    diskon = hitung_diskon(total_belanja)
    total_akhir = total_belanja - diskon

    # Menampilkan informasi total belanja dan diskon jika berlaku
    if diskon > 0:
        print(f"{'Total Belanja':<36} {format_rupiah(total_belanja)}")
        print(f"{'Diskon 10%':<36} {format_rupiah(diskon)}")
        garis()
        print(f"{'Total Akhir':<36} {format_rupiah(total_akhir)}")
    else:
        print(f"{'Total Akhir':<36} {format_rupiah(total_akhir)}")
        garis()
        print(f"{'Diskon 10% untuk pembelian lebih dari Rp200.000':^57}")
    garis()

# Fungsi untuk menampilkan daftar aksi yang dapat dilakukan pengguna
def tampil_aksi(daftar_aksi):
    for aksi in daftar_aksi:
        print(f"({aksi['kunci']}) {aksi['keterangan']}")
    print()

# Fungsi untuk memilih barang berdasarkan nomor urut dalam daftar
def pilih_barang(daftar_barang, daftar_aksi, aksi_terpilih):
    salah_input = False

    while True:
        tampil_daftar(daftar_barang)
        print(daftar_aksi[aksi_terpilih]['keterangan'])
        print()
        print("Masukkan \"X\" untuk kembali ke menu utama")
        if salah_input: print("Masukan invalid. Harap masukkan nomor yang benar")
        user_input = input(f"Masukkan nomor barang yang ingin Anda pilih (1-{len(daftar_barang)}): ").strip().capitalize()

        if user_input == "X": return -1  # Kembali ke menu utama
        
        # Validasi input apakah angka dan dalam rentang yang valid
        if not user_input.isnumeric() or int(user_input) < 1 or int(user_input) > len(daftar_barang):
            salah_input = True
            layar_bersih()
        else:
            return int(user_input) - 1  # Mengembalikan indeks barang terpilih

# Fungsi untuk mengatur jumlah barang yang dibeli atau dibatalkan
def berapa_barang(daftar_barang, daftar_aksi, aksi_terpilih, barang_terpilih):
    salah_input = False

    while True:
        tampil_daftar(daftar_barang)
        print(daftar_aksi[aksi_terpilih]['keterangan'], "-", daftar_barang[barang_terpilih]['nama'])
        print()
        print("Masukkan \"X\" untuk kembali ke menu utama")
        if salah_input: print("Masukan invalid. Harap masukkan angka bulat non-negatif")
        user_input = input(f"Berapa banyak {daftar_barang[barang_terpilih]['nama'].lower()} yang ingin Anda {daftar_aksi[aksi_terpilih]['aksi']}: ").strip().capitalize()

        if user_input == "X": break  # Kembali ke menu utama
        
        # Validasi input apakah angka
        if not user_input.isnumeric():
            salah_input = True
            layar_bersih()
        else:
            # Update kuantitas barang
            daftar_barang[barang_terpilih]['kuantitas'] = max(0, daftar_barang[barang_terpilih]['kuantitas'] + (int(user_input) if aksi_terpilih == 0 else -int(user_input)))
            break

# Fungsi utama program
def main():
    # Daftar barang yang dijual
    daftar_barang = [
        {"nama": "Kaos", "harga": 50000, "kuantitas": 0},
        {"nama": "Jaket", "harga": 150000, "kuantitas": 0},
        {"nama": "Topi", "harga": 30000, "kuantitas": 0}
    ]

    # Daftar aksi yang dapat dilakukan pengguna
    daftar_aksi = [
        {"kunci": "P", "aksi": "beli", "keterangan": "Pembelian"},
        {"kunci": "C", "aksi": "batal", "keterangan": "Pembatalan"},
        {"kunci": "X", "aksi": "keluar", "keterangan": "Selesai"}
    ]

    layar_bersih()
    salah_input = False

    # Loop utama program
    while True:
        tampil_daftar(daftar_barang)
        tampil_aksi(daftar_aksi)

        if salah_input: print("Masukan invalid. Harap masukkan P, C, atau X.")
        aksi_terpilih = input("Apa yang Anda ingin lakukan sekarang? (P/C/X): ").strip().capitalize()

        if any(aksi['kunci'] == aksi_terpilih for aksi in daftar_aksi):
            salah_input = False
            if aksi_terpilih == "X": break  # Keluar program
            barang_terpilih = pilih_barang(daftar_barang, daftar_aksi, 0 if aksi_terpilih == "P" else 1)
            if barang_terpilih != -1:
                berapa_barang(daftar_barang, daftar_aksi, 0 if aksi_terpilih == "P" else 1, barang_terpilih)
        else:
            salah_input = True
        layar_bersih()

    # Pesan akhir program
    layar_bersih()
    tampil_daftar(daftar_barang)

    if hitung_total_belanja(daftar_barang) == 0:
        print(f"{'Terima Kasih Atas Kunjungan Anda':^57}")
    else:
        print(f"{'Terima Kasih Atas Pembelian Anda':^57}")
    
    print(f"{'Sampai Jumpa Lagi ^_^':^57}")
    garis()

# Menjalankan program utama
if __name__ == "__main__":
    main()