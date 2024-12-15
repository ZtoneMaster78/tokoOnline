import os

# Fungsi untuk membersihkan layar terminal
# Function to clear the terminal screen
def layar_bersih():
    os.system("cls" if os.name == "nt" else "clear")

# Fungsi untuk mencetak garis horizontal sebagai pemisah
# Function to print a horizontal line as a separator
def garis(tebal=True):
    print("=" * 57 if tebal else "-" * 57)

# Fungsi untuk memformat angka menjadi mata uang Rupiah dengan batas lebar tertentu
# Function to format a number into Rupiah currency with a specific width limit
def format_rupiah(angka, batas=20):
    return f"{f'Rp{angka:,.0f}'.replace(',', '.'): <{batas}}"

# Fungsi untuk menghitung total belanja berdasarkan harga dan kuantitas setiap barang
# Function to calculate the total shopping cost based on the price and quantity of each item
def hitung_total_belanja(daftar_barang):
    return sum(barang['harga'] * barang['kuantitas'] for barang in daftar_barang)

# Fungsi untuk menghitung diskon jika total belanja melebihi Rp200.000
# Function to calculate a discount if the total shopping cost exceeds Rp200,000
def hitung_diskon(total):
    return total * 0.1 if total > 200000 else 0

# Fungsi untuk menampilkan daftar barang, subtotal, total belanja, dan diskon
# Function to display the list of items, subtotal, total shopping cost, and discount
def tampil_daftar(daftar_barang):
    layar_bersih()
    garis()
    print(f"{'Toko Online':^57}")
    garis()

    # Header tabel daftar barang
    # Header for the item list table
    print(f"{'No':<3} {'Pakaian':<10} {'Harga':<10} {'Kuantitas':^10} {'Subtotal':^20}")
    garis(tebal=False)

    # Menampilkan setiap barang dengan detail harga, kuantitas, dan subtotal
    # Display each item with details of price, quantity, and subtotal
    for index, barang in enumerate(daftar_barang, start=1):
        print(f"{index:<3} {barang['nama']:<10} {format_rupiah(barang['harga'], batas=10)} {barang['kuantitas']:^10} {format_rupiah(barang['harga'] * barang['kuantitas'])}")

    garis()

    # Menghitung total belanja, diskon, dan total akhir
    # Calculate the total shopping cost, discount, and final total
    total_belanja = hitung_total_belanja(daftar_barang)
    diskon = hitung_diskon(total_belanja)
    total_akhir = total_belanja - diskon

    # Menampilkan informasi total belanja dan diskon jika berlaku
    # Display total shopping cost and discount information if applicable
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
# Function to display the list of actions the user can perform
def tampil_aksi(daftar_aksi):
    for aksi in daftar_aksi:
        print(f"({aksi['kunci']}) {aksi['keterangan']}")
    print()

# Fungsi untuk memilih barang berdasarkan nomor urut dalam daftar
# Function to select an item based on its number in the list
def pilih_barang(daftar_barang, daftar_aksi, aksi_terpilih):
    salah_input = False

    while True:
        tampil_daftar(daftar_barang)
        print(daftar_aksi[aksi_terpilih]['keterangan'])
        print()
        print("Masukkan \"X\" untuk kembali ke menu utama")
        # Enter "X" to return to the main menu
        if salah_input: print("Masukan invalid. Harap masukkan nomor yang benar")
        # Invalid input. Please enter the correct number
        user_input = input(f"Masukkan nomor barang yang ingin Anda pilih (1-{len(daftar_barang)}): ").strip().capitalize()

        if user_input == "X": return -1  # Kembali ke menu utama
        # Return to the main menu
        
        # Validasi input apakah angka dan dalam rentang yang valid
        # Validate if the input is a number and within the valid range
        if not user_input.isnumeric() or int(user_input) < 1 or int(user_input) > len(daftar_barang):
            salah_input = True
            layar_bersih()
        else:
            return int(user_input) - 1  # Mengembalikan indeks barang terpilih
            # Return the index of the selected item

# Fungsi untuk mengatur jumlah barang yang dibeli atau dibatalkan
# Function to manage the quantity of items purchased or canceled
def berapa_barang(daftar_barang, daftar_aksi, aksi_terpilih, barang_terpilih):
    salah_input = False

    while True:
        tampil_daftar(daftar_barang)
        print(daftar_aksi[aksi_terpilih]['keterangan'], "-", daftar_barang[barang_terpilih]['nama'])
        print()
        print("Masukkan \"X\" untuk kembali ke menu utama")
        # Enter "X" to return to the main menu
        if salah_input: print("Masukan invalid. Harap masukkan angka bulat non-negatif")
        # Invalid input. Please enter a non-negative integer
        user_input = input(f"Berapa banyak {daftar_barang[barang_terpilih]['nama'].lower()} yang ingin Anda {daftar_aksi[aksi_terpilih]['aksi']}: ").strip().capitalize()

        if user_input == "X": break
        # Kembali ke menu utama
        # Return to the main menu
        
        # Validasi input apakah angka
        # Validate if the input is a number
        if not user_input.isnumeric():
            salah_input = True
            layar_bersih()
        else:
            # Update kuantitas barang
            # Update the quantity of the item
            daftar_barang[barang_terpilih]['kuantitas'] = max(0, daftar_barang[barang_terpilih]['kuantitas'] + (int(user_input) if aksi_terpilih == 0 else -int(user_input)))
            break

# Fungsi utama program
# Main program function
def main():
    # Daftar barang yang dijual
    # List of items for sale
    daftar_barang = [
        {"nama": "Kaos", "harga": 50000, "kuantitas": 0},
        {"nama": "Jaket", "harga": 150000, "kuantitas": 0},
        {"nama": "Topi", "harga": 30000, "kuantitas": 0}
    ]

    # Daftar aksi yang dapat dilakukan pengguna
    # List of actions the user can perform
    daftar_aksi = [
        {"kunci": "P", "aksi": "beli", "keterangan": "Pembelian"},
        {"kunci": "C", "aksi": "batal", "keterangan": "Pembatalan"},
        {"kunci": "X", "aksi": "keluar", "keterangan": "Selesai"}
    ]

    layar_bersih()
    salah_input = False

    # Loop utama program
    # Main program loop
    while True:
        tampil_daftar(daftar_barang)
        tampil_aksi(daftar_aksi)

        if salah_input: print("Masukan invalid. Harap masukkan P, C, atau X.")
        # Invalid input. Please enter P, C, or X.
        aksi_terpilih = input("Apa yang Anda ingin lakukan sekarang? (P/C/X): ").strip().capitalize()

        if any(aksi['kunci'] == aksi_terpilih for aksi in daftar_aksi):
            salah_input = False
            if aksi_terpilih == "X": break 
            # Keluar program
            # Exit program
            barang_terpilih = pilih_barang(daftar_barang, daftar_aksi, 0 if aksi_terpilih == "P" else 1)
            if barang_terpilih != -1:
                berapa_barang(daftar_barang, daftar_aksi, 0 if aksi_terpilih == "P" else 1, barang_terpilih)
        else:
            salah_input = True
        layar_bersih()

    # Pesan akhir program
    # End program message
    layar_bersih()
    tampil_daftar(daftar_barang)

    if hitung_total_belanja(daftar_barang) == 0:
        print(f"{'Terima Kasih Atas Kunjungan Anda':^57}")
        # Thank you for your visit
    else:
        print(f"{'Terima Kasih Atas Pembelian Anda':^57}")
        # Thank you for your purchase
    
    print(f"{'Sampai Jumpa Lagi ^_^':^57}")
    # See you again ^_^
    garis()

# Menjalankan program utama
# Run the main program
if __name__ == "__main__":
    main()
