# Tabel menggunakan prettytable
from prettytable import PrettyTable

# Untuk menyalakan kode clear screen
import os

class produk_daging:
    def __init__(self, id_produk, nama_produk, harga, stok, rating):
        self.id_produk = id_produk
        self.nama_produk = nama_produk
        self.harga = harga
        self.stok = stok
        self.rating = rating

# Node dalam linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# linked listnya
class LinkedList:
    def __init__(self):
        self.head = None

# Menambah node di awal
    def tambah_di_awal(self, data):
        new_node = Node(data) 
        new_node.next = self.head
        self.head = new_node

# Menambahkan node di akhir
    def tambah_di_akhir(self, data):
        new_node = Node(data) 
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

# Menambahkan node di antara dua node
    def tambah_di_antara(self, prev_node, data):
        if prev_node is None:
            print("Node sebelumnya tidak ada.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

# Mencari node dengan ID produk tertentu
    def cari_node(self, id_produk):
        current_node = self.head
        while current_node:
            if current_node.data.id_produk == id_produk:
                return current_node
            current_node = current_node.next
        return None

# Menghapus node dengan ID produk tertentu
    def hapus_node(self, id_produk):
        current_element = self.head
        if current_element is not None:
            if current_element.data.id_produk == id_produk:
                self.head = current_element.next
                current_element = None
                return
        while current_element is not None:
            if current_element.data.id_produk == id_produk:
                break
            prev = current_element
            current_element = current_element.next
        if current_element is None:
            return
        prev.next = current_element.next
        current_element = None

def lihat_produk(linked_list):
    if linked_list.head is None:
        print("Produk Masih kosong.")
        return
    table = PrettyTable(["ID Produk", "Nama", "Harga", "Stok", "Rating"])
    current_node = linked_list.head
    while current_node:
        table.add_row([current_node.data.id_produk, current_node.data.nama_produk, current_node.data.harga, current_node.data.stok, current_node.data.rating])
        current_node = current_node.next
    print(table)

def update_produk(linked_list, id_produk, nama_produk=None, harga=None, stok=None, rating=None):
    node = linked_list.cari_node(id_produk)
    if node:
        if nama_produk:
            node.data.nama_produk = nama_produk
        if harga:
            node.data.harga = harga
        if stok:
            node.data.stok = stok
        if rating is not None:
            node.data.rating = rating
        return True
    return False

def delete_produk(linked_list, id_produk):
    linked_list.hapus_node(id_produk)

# Membuat Manajemen Produk dalam bentuk linkedlist untuk produk frozen food
class manajemen_produk:
    def __init__(self):
        self.linked_list = LinkedList()

    def tambah_produk(self, id_produk, nama_produk, harga, stok, rating):
        new_produk = produk_daging(id_produk, nama_produk, harga, stok, rating)
        self.linked_list.tambah_di_akhir(new_produk)
        input("\nProduk baru berhasil ditambahkan.")
        os.system("cls")

manajemen_produk = manajemen_produk()

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


while True:
    choice = menu()

    if choice == "1":
        os.system("cls")
        print('''
==================================================
‖                  TAMBAH PRODUK                 ‖
==================================================\n''')
        
        print("Pilih lokasi penambahan produk:")
        print("1. Bagian awal")
        print("2. Bagian akhir")
        print("3. Di antara produk")
        choice_tambah = input("Masukkan Pilihan anda (1-3): ")

        id_produk = int(input("Masukkan ID produk: "))
        nama_produk = input("Masukkan nama produk: ")
        harga = float(input("Masukkan harga produk: "))
        stok = int(input("Masukkan stok produk: "))
        rating = str(input("Masukkan rating produk: "))

        if choice_tambah == "1":
            manajemen_produk.linked_list.tambah_di_awal(produk_daging(id_produk, nama_produk, harga, stok, rating))
            input("\nProduk baru berhasil ditambahkan.")
            os.system("cls")
        elif choice_tambah == "2":
            manajemen_produk.linked_list.tambah_di_akhir(produk_daging(id_produk, nama_produk, harga, stok, rating))
            input("\nProduk baru berhasil ditambahkan.")
            os.system("cls")
        elif choice_tambah == "3":
            id_sebelumnya = int(input("Masukkan ID produk sebelumnya: "))
            prev_node = manajemen_produk.linked_list.cari_node(id_sebelumnya)
            if prev_node:
                manajemen_produk.linked_list.tambah_di_antara(prev_node, produk_daging(id_produk, nama_produk, harga, stok, rating))
                input("\nProduk baru berhasil ditambahkan.")
                os.system("cls")
            else:
                print("Produk dengan ID tersebut tidak ditemukan.")
                input("\nTekan ENTER untuk melanjutkan.")
                os.system("cls")


    elif choice == "2":
        os.system("cls")
        print('''
==================================================
‖                   LIHAT PRODUK                 ‖
==================================================\n''')
        lihat_produk(manajemen_produk.linked_list)
        input("\nTekan ENTER untuk melanjutkan.")
        os.system("cls")


    elif choice == "3":
        os.system("cls")
        print('''
==================================================
‖                  UPDATE PRODUK                 ‖
==================================================\n''')
        id_produk = int(input("Masukkan id produk yang ingin diperbarui: "))
        nama_produk = input("Masukkan nama produk baru (tekan ENTER langsung untuk skip): ")
        harga = input("Masukkan harga baru (langsung ENTER untuk skip): ")
        stok = input("Masukkan ketersediaan stok baru (langsung ENTER untuk skip): ")
        rating = input("Masukkan rating baru produk (langsung ENTER untuk skip): ")
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
        if update_produk(manajemen_produk.linked_list, id_produk, nama_produk, harga, stok, rating):
            input("\nProduk berhasil diperbarui.")
            os.system("cls")
        else:
            input("\nProduk tidak dapat diperbarui karena tidak terdapatnya id!")
            os.system("cls")


    elif choice == "4":
        os.system("cls")
        print('''
==================================================
‖                   HAPUS PRODUK                  ‖
==================================================\n''')
        if not manajemen_produk.linked_list.head:
            input("Tidak ada produk yang dapat dihapus.")
            os.system("cls")
        else:
            lihat_produk(manajemen_produk.linked_list)
            print("\nPilih lokasi menghapus produk:")
            print("1. Bagian Awal")
            print("2. Bagian Akhir")
            print("3. Menghapus ID tertentu")
            choice_hapus = input("Masukkan Pilihan anda (1-3): ")

            if choice_hapus == "1":
                delete_produk(manajemen_produk.linked_list, manajemen_produk.linked_list.head.data.id_produk)
                input("\nProduk berhasil dihapus.")
                os.system("cls")
            elif choice_hapus == "2":
                current_node = manajemen_produk.linked_list.head
                prev_node = None
                while current_node.next:
                    prev_node = current_node
                    current_node = current_node.next
                delete_produk(manajemen_produk.linked_list, current_node.data.id_produk)
                input("\nProduk berhasil dihapus.")
                os.system("cls")
            elif choice_hapus == "3":
                id_hapus = int(input("Masukkan ID produk yang ingin dihapus: "))
                if manajemen_produk.linked_list.cari_node(id_hapus) is None:
                    input("ID produk tidak ditemukan. Tekan ENTER untuk kembali ke menu utama.")
                    os.system("cls")
                else:
                    delete_produk(manajemen_produk.linked_list, id_hapus)
                    input("\nProduk berhasil dihapus.")
                    os.system("cls")
            else:
                input("Pilihan tidak valid. Tekan ENTER untuk kembali.")
                os.system("cls")


    elif choice == "5":
        input("Keluar dari program, terimakasih!")
        os.system("cls")
        quit()

    else:
        input("Tolong masukkan angka dari 1-5!")
        os.system("cls")
