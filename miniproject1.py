# Tabel menggunakan prettytable
from prettytable import PrettyTable
table = PrettyTable()

# Untuk clear screen
import os
os.system("cls")

# Membuat entitas dari toko frozen food yakni produknya
class produk_daging:
    def __init__(self, id_produk, nama_produk, harga, stok, rating):
        self.id_produk = id_produk
        self.nama_produk = nama_produk
        self.harga = harga
        self.stok = stok
        self.rating = rating

# Membuat entitas untuk CRUD produk frozen food
class Manajemen_produk:
    def __init__(self):
        self.produk_daging = []

# Fungsi Create
    def tambah_produk(self, id_produk, nama_produk, harga, stok, rating):
        existing_product = self.cari_produk(id_produk)
        if existing_product:
            input("\nID produk sudah ada. Produk tidak dapat ditambahkan.")
            os.system("cls")
            return
        else:
            new_produk_daging = produk_daging(id_produk, nama_produk, harga, stok, rating)
            self.produk_daging.append(new_produk_daging)
            input("\nProduk baru berhasil ditambahkan.")
            os.system("cls")

    def cari_produk(self, id_produk):
        for produk_daging in self.produk_daging:
            if produk_daging.id_produk == id_produk:
                return produk_daging
        return None

# Fungsi Read
    def lihat_produk(self):
        table = PrettyTable()
        table.field_names = ["ID Produk", "Nama", "Harga", "Stok", "Rating"]
        for produk_daging in self.produk_daging:
            table.add_row([produk_daging.id_produk, produk_daging.nama_produk, produk_daging.harga, produk_daging.stok, produk_daging.rating])
        print(table)

# Def Update
    def update_produk(self, id_produk, nama_produk=None, harga=None, stok=None, rating=None):
        produk_daging = self.cari_produk(id_produk)
        if produk_daging:
            if nama_produk:
                produk_daging.nama_produk = nama_produk
            if harga:
                produk_daging.harga = harga
            if stok:
                produk_daging.stok = stok
            if rating is not None:
                produk_daging.rating = rating
            return True
        return False

# Fungsi Delete
    def delete_produk(self, id_produk):
        produk_daging = self.cari_produk(id_produk)
        if produk_daging:
            self.produk_daging.remove(produk_daging)
            return True
        return False


# Tampilan Menu Awal
def menu():
    print('''
==================================================
‖              FROZEN FOOD DAGING SI             ‖
==================================================\n''')
    print("1. Tambah Produk")
    print("2. Lihat Produk")
    print("3. Update Produk")
    print("4. Delete Produk")
    print("5. Keluar")
    choice = input("Masukkan Pilihan anda (1-5): ")
    return choice

Manajemen_produk = Manajemen_produk()

# Looping Menu Tampilan Awal
while True:
    choice = menu()

# Input Create Dalam Program
    if choice == "1":
        os.system("cls")
        print('''
==================================================
‖                  TAMBAH PRODUK                 ‖
==================================================\n''')
        id_produk = int(input("Masukkan ID produk: "))
        nama_produk = input("Masukkan nama produk: ")
        harga = float(input("Masukkan harga produk: "))
        stok = int(input("Masukkan stok produk: "))
        rating = str(input("Masukkan rating produk: "))
        Manajemen_produk.tambah_produk(id_produk, nama_produk, harga, stok, rating)

# Input Read Dalam Program
    elif choice == "2":
        os.system("cls")
        print('''
==================================================
‖                   Lihat PRODUK                 ‖
==================================================\n''')
        Manajemen_produk.lihat_produk()
        input("Tekan ENTER untuk melanjutkan.")
        os.system("cls")

# Input Update Dalam Program
    elif choice == "3":
        os.system("cls")
        print('''
==================================================
‖                   CARI PRODUK                  ‖
==================================================\n''')
        id_produk = int(input("Masukkan id produk yang ingin diperbarui: "))
        nama_produk = input("Masukkan nama produk baru (tekan ENTER langsung untuk skip): ")
        harga = input("Masukkan harga baru (langsung ENTER untuk skip): ")
        stok = input("Masukkan ketersediaan stok baru (langsung ENTER untuk skip): ")
        rating = input("Masukkan rating baru produk (langsung ENTER untuk skip)")
        if nama_produk == "":
            nama_produk = None
        if harga == "":
            harga = None
        else:
            harga = float(harga)
        if stok == "":
            stok = None
        else:
            stok = int(stok)
        if rating == "":
            rating = None
        else:
            rating = str(rating)
        if Manajemen_produk.update_produk(id_produk, nama_produk, harga, stok, rating):
            input("\nProduk berhasil diperbarui.")
            os.system("cls")
        else:
            input("\nProduk tidak dapat diperbarui karena tidak terdapatnya id!")
            os.system("cls")

# Input Delete Dalam Program
    elif choice == "4":
        os.system("cls")
        print('''
    ==================================================
    ‖                   HAPUS PRODUK                  ‖
    ==================================================\n''')
        id_produk = int(input("Enter produk_daging ID to delete: "))
        if Manajemen_produk.delete_produk(id_produk):
            input("\nProduk berhasil dihapus.")
            os.system("cls")
        else:
            print("Produk tidak dapat dihapus karena tidak terdapatnya id!")
            os.system("cls")
    elif choice == "5":
        input("Keluar dari program, terimakasih!")
        os.system("cls")
        quit()
    else:
        input("Tolong masukkan angka dari 1-5!")
        os.system("cls")
