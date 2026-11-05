import os
from auth import login, register

from kendaraan import (
    tambah_kendaraan,
    tampilkan_kendaraan,
    ubah_kendaraan,
    hapus_kendaraan
)

from pengguna import (
    tampilkan_pengguna,
    edit_pengguna,
    hapus_pengguna
)



# Menu 
def menu_pengguna(username, role):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("===================================")
        print(" MENU PENDATAAN KENDARAAN")
        print("===================================")
        print("Login sebagai:", username, "-", role)
        print("1. Tambah Kendaraan")
        print("2. Lihat Kendaraan")
        print("3. Ubah Kendaraan")
        print("4. Hapus Kendaraan")

        if role == "Admin":
            print("5. Lihat Data Pengguna")
            print("6. Edit Data Pengguna")
            print("7. Hapus Akun Pengguna")

        print("0. Logout")

        menu = input("Pilih menu: ").strip()

        if menu == "1":
            os.system("cls" if os.name == "nt" else "clear")
            tambah_kendaraan(username)

        elif menu == "2":
            os.system("cls" if os.name == "nt" else "clear")
            tampilkan_kendaraan()

        elif menu == "3":
            os.system("cls" if os.name == "nt" else "clear")
            ubah_kendaraan(username, role)

        elif menu == "4":
            os.system("cls" if os.name == "nt" else "clear")
            hapus_kendaraan(username, role)

        elif menu == "5" and role == "Admin":
            os.system("cls" if os.name == "nt" else "clear")
            tampilkan_pengguna()

        elif menu == "6" and role == "Admin":
            os.system("cls" if os.name == "nt" else "clear")
            edit_pengguna(username)

        elif menu == "7" and role == "Admin":
            os.system("cls" if os.name == "nt" else "clear")
            hapus_pengguna(username)

        elif menu == "0":
            os.system("cls" if os.name == "nt" else "clear")
            print("Logout berhasil.")
            break

        else:
            print("Error: Menu tidak tersedia.")
        input("\nTekan Enter untuk melanjutkan...")

# Prugram
def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("🏍️  SISTEM PENDATAAN KENDARAAN  🚗.")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")

        opsi = input("Pilih menu: ").strip()

        if opsi == "1":
            os.system("cls" if os.name == "nt" else "clear")
            username, role = login()

            if username is not None:
                os.system("cls" if os.name == "nt" else "clear")
                menu_pengguna(username, role)

        elif opsi == "2":
            os.system("cls" if os.name == "nt" else "clear")
            register()

        elif opsi == "3":
            os.system("cls" if os.name == "nt" else "clear")
            print("Terima kasih telah menggunakan program.")
            break

        else:
            print("Error: Pilihan menu tidak tersedia.")

if __name__ == "__main__":
    main()