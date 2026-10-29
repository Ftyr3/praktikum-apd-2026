import os

# (username, password, level_akses)
akun = {
    "admin": {
        "password": "admin123",
        "role": "Admin"
    },
    "Daniel": {
        "password": "054",
        "role": "User"
    }
}

# [id, nomor plat, nama pemilik, jenis, merek, tahun, username]
data_kendaraan = {
    1: {
        "plat": "KT 1234 AB",
        "pemilik": "Robin",
        "jenis": "Mobil",
        "merek": "Toyota Avanza",
        "tahun": 2022,
        "username": "Daniel"
    },
    2: {
        "plat": "KT 5678 CD",
        "pemilik": "Afid",
        "jenis": "Motor",
        "merek": "Honda Vario",
        "tahun": 2023,
        "username": "Daniel"
    }
}

id_berikutnya = 3

def login():
    print("=== LOGIN ===")
    percobaan = 0

    while percobaan < 3:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        role = ""
        if username in akun and akun[username]["password"] == password:
            role = akun[username]["role"]
            return username, akun[username]["role"]
        else:
            percobaan += 1
            sisa = 3 - percobaan
            if sisa > 0:
                print(f"Username atau password salah! Sisa percobaan: {sisa}")
            else:
                print("Username atau password salah 3 kali. Silahkan mulai ulang")
                input("\nTekan Enter untuk melanjutkan...")
    return None, None

def hitung_kendaraan():
    return len(data_kendaraan)

def cari_kendaraan(id_kendaraan):
    return data_kendaraan.get(id_kendaraan)

def validasi_tahun(tahun):
    try:
        tahun = int(tahun)
        return 1899 < tahun <= 2676
    except (ValueError, TypeError):
        return False

def hitung_kendaraan_rekursif(daftar_id, indeks=0):

    if indeks >= len(daftar_id):
        return 0

    return 1 + hitung_kendaraan_rekursif(
        daftar_id, indeks + 1
    )

# Read
def tampilkan_kendaraan():
    print("========== DATA KENDARAAN ==========")

    if hitung_kendaraan() == 0:
        print("Belum ada data kendaraan.")
        return

    for id_kendaraan, data in data_kendaraan.items():
        print("------------------------------------")
        print("ID           :", id_kendaraan)
        print("Nomor Plat   :", data["plat"])
        print("Nama Pemilik :", data["pemilik"])
        print("Jenis        :", data["jenis"])
        print("Merek        :", data["merek"])
        print("Tahun        :", data["tahun"])
        print("Input Oleh   :", data["username"])

    print("------------------------------------")
    daftar_id = list(data_kendaraan.keys())
    jumlah_rekursif = hitung_kendaraan_rekursif(daftar_id)
    print("Jumlah :", jumlah_rekursif)

# Create
def tambah_kendaraan(username):
    try:
        print("======= TAMBAH KENDARAAN =======")

        plat = input("Nomor plat: ").strip().upper()

        if plat == "":
            raise ValueError("Nomor plat wajib diisi.")

        for data in data_kendaraan.values():
            if data["plat"] == plat:
                raise ValueError("Nomor plat sudah terdaftar.")

        pemilik = input("Nama pemilik: ").strip()
        jenis = input("Jenis kendaraan (Mobil/Motor): ").strip().capitalize()
        merek = input("Merek kendaraan: ").strip()
        tahun_input = input("Tahun kendaraan: ").strip()

        if pemilik == "" or merek == "":
            raise ValueError("Data tidak boleh kosong.")
        elif jenis not in ("Mobil", "Motor"):
            raise ValueError("Jenis harus Mobil atau Motor.")
        elif not validasi_tahun(tahun_input):
            raise ValueError("Tahun kendaraan tidak valid.")
        else:
            id_baru = len(data_kendaraan) + 1
            data_kendaraan[id_baru] = {
                "plat": plat,
                "pemilik": pemilik,
                "jenis": jenis,
                "merek": merek,
                "tahun": int(tahun_input),
                "username": username
            }

            print("Data kendaraan berhasil ditambahkan!")
            print("ID kendaraan:", id_baru)

    except ValueError as error:
        print("Error:", error)

# Update
def ubah_kendaraan(username, role):
    try:
        tampilkan_kendaraan()

        if not data_kendaraan:
            return
        
        print("\n========= UBAH KENDARAAN =========")
        id_input = input("Masukkan ID kendaraan: ").strip()

        if not id_input.isdigit():
            raise ValueError("ID harus berupa angka.")

        id_kendaraan = int(id_input)
        data = cari_kendaraan(id_kendaraan)

        if data is None:
            raise ValueError("Data tidak ditemukan.")

        if role != "Admin" and data["username"] != username:
            raise ValueError("Anda tidak memiliki akses.")

        print("Data lama:", data)

        plat = input("Nomor plat baru: ").strip().upper()

        if not plat:
            raise ValueError("Nomor plat wajib diisi.")

        for id_lain, kendaraan in data_kendaraan.items():
            if kendaraan["plat"] == plat and id_lain != id_kendaraan:
                raise ValueError("Nomor plat sudah digunakan.")

        pemilik = input("Nama pemilik baru: ").strip()
        jenis = input("Jenis baru (Mobil/Motor): ").strip().capitalize()
        merek = input("Merek baru: ").strip()
        tahun_input = input("Tahun baru: ").strip()

        if pemilik_baru == "" or merek_baru == "":
            raise ValueError("Data tidak boleh kosong.")

        if jenis not in ("Mobil", "Motor"):
            raise ValueError("Jenis kendaraan tidak valid.")

        if not validasi_tahun(tahun_input):
            raise ValueError("Tahun kendaraan tidak valid.")

        data.update({
            "plat": plat,
            "pemilik": pemilik,
            "jenis": jenis,
            "merek": merek,
            "tahun": int(tahun_input)
        })

        print("Data kendaraan berhasil diperbarui.")

    except ValueError as error:
        print("Error:", error)

# Delete
def hapus_kendaraan(username, role):
    try:
        tampilkan_kendaraan()

        if not data_kendaraan:
            return

        print("\n========= HAPUS KENDARAAN =========")
        id_input = input("Masukkan ID kendaraan: ").strip()

        if not id_input.isdigit():
            raise ValueError("ID harus berupa angka.")

        id_kendaraan = int(id_input)
        data = cari_kendaraan(id_kendaraan)

        if data is None:
            raise ValueError("Data tidak ditemukan.")

        if role != "Admin" and data["username"] != username:
            raise ValueError("Anda tidak memiliki akses.")

        print("Data yang akan dihapus:")
        print("ID           :", id_kendaraan)
        print("Nomor Plat   :", data["plat"])
        print("Nama Pemilik :", data["pemilik"])
        print("Jenis        :", data["jenis"])
        print("Merek        :", data["merek"])
        print("Tahun        :", data["tahun"])
        konfirmasi = input("Yakin hapus? (y/n): ").strip().lower()

        if konfirmasi == "y":
            del data_kendaraan[id_kendaraan]
            print("Data berhasil dihapus.")
        elif konfirmasi == "n":
            print("Penghapusan dibatalkan.")
        else:
            raise ValueError("Pilihan harus y atau n.")

    except ValueError as error:
        print("Error:", error)

# Lihat Data Pengguna
def tampilkan_pengguna():
    print("========== DATA PENGGUNA ==========")

    if not akun:
        print("Belum ada data pengguna.")
        return

    for nomor, (username, data) in enumerate(akun.items(), start=1):
        print("------------------------------------")
        print("Nomor   :", nomor)
        print("Username:", username)
        print("Role    :", data["role"])

# Edit Data Pengguna
def edit_pengguna(username_login):
    try:
        tampilkan_pengguna()

        print("\n========== EDIT DATA PENGGUNA ==========")
        nomor = input("Pilih nomor akun yang ingin diedit: ").strip()

        if not nomor.isdigit():
            raise ValueError("Nomor harus berupa angka.")

        daftar_username = list(akun.keys())
        indeks = int(nomor) - 1

        if indeks < 0 or indeks >= len(daftar_username):
            raise ValueError("Akun tidak ditemukan.")

        username_lama = daftar_username[indeks]

        if username_lama == username_login:
            raise ValueError("Anda tidak dapat mengedit akun sendiri.")

        username_baru = input("Username baru: ").strip()
        password_baru = input("Password baru: ").strip()
        role_baru = input("Role baru (User/Admin): ").strip().capitalize()

        username_ada = False

        for i in akun:
            if i != username_lama and i == username_baru:
                username_ada = True

        if username_baru == "" or password_baru == "":
            raise ValueError("Username dan password wajib diisi.")
        elif username_ada:
            raise ValueError("Username sudah digunakan.")
        elif role_baru not in ("User", "Admin"):
            raise ValueError("Role harus User atau Admin.")

        akun[username_baru] = akun.pop(username_lama)
        akun[username_baru]["password"] = password_baru
        akun[username_baru]["role"] = role_baru

        for kendaraan in data_kendaraan.values():
            if kendaraan["username"] == username_lama:
                kendaraan["username"] = username_baru

        print("Data pengguna berhasil diperbarui.")

    except ValueError as error:
        print("Error:", error)

# Hapus Akun Pengguna
def hapus_pengguna(username_login):
    try:
        tampilkan_pengguna()

        print("\n========== HAPUS AKUN PENGGUNA ==========")
        nomor = input("Pilih nomor akun yang ingin dihapus: ").strip()

        if not nomor.isdigit():
            raise ValueError("Nomor harus berupa angka.")

        daftar_username = list(akun.keys())
        indeks = int(nomor) - 1

        if indeks < 0 or indeks >= len(daftar_username):
            raise ValueError("Akun tidak ditemukan.")

        target = daftar_username[indeks]

        if target == username_login:
            raise ValueError("Tidak dapat menghapus akun sendiri.")

        if akun[target]["role"] == "Admin":
            raise ValueError("Akun Admin tidak boleh dihapus.")

        konfirmasi = input(
            f"Yakin hapus akun {target}? (y/n): "
        ).strip().lower()

        if konfirmasi == "y":
            # Kendaraan milik akun tetap tersimpan.
            # Hak aksesnya mengikuti aturan login yang berlaku.
            del akun[target]
            print("Akun pengguna berhasil dihapus.")
        elif konfirmasi == "n":
            print("Penghapusan dibatalkan.")
        else:
            raise ValueError("Pilihan harus y atau n.")

    except ValueError as error:
        print("Error:", error)

# Register
def register():
    try:
        print("========== REGISTER ==========")

        username = input("Buat username: ").strip()
        password = input("Buat password: ").strip()

        if not username or not password:
            raise ValueError("Username dan password wajib diisi.")

        if username in akun:
            raise ValueError("Username sudah digunakan.")

        akun[username] = {
            "password": password,
            "role": "User"
        }

        print("Registrasi berhasil. Silakan login.")

    except ValueError as error:
        print("Error:", error)

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

main()