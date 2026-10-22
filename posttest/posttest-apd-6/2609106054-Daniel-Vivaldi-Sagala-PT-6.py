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

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("🏍️  SISTEM PENDATAAN KENDARAAN  🚗.")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    opsi = input("Pilih Menu : ")

    # Kesempatan Login 3x
    if opsi == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("=== LOGIN ===")
        percobaan = 0
        login_berhasil = False

        while percobaan < 3 and not login_berhasil:
            username = input("Masukkan username: ").strip()
            password = input("Masukkan password: ").strip()

            role = ""
            if (
                username in akun
                and akun[username]["password"] == password
            ):
                login_berhasil = True
                role = akun[username]["role"]
            else:
                percobaan += 1
                sisa = 3 - percobaan
                if sisa > 0:
                    print(f"Username atau password salah! Sisa percobaan: {sisa}")
                else:
                    print("Username atau password salah 3 kali. Silahkan mulai ulang")
                    input("\nTekan Enter untuk melanjutkan...")
            
        if login_berhasil:
            print("Login berhasil!")
            print("Selamat datang,", username)
            print("Role:", role)

            masuk_menu = True

            while masuk_menu:
                os.system("cls" if os.name == "nt" else "clear")

                print("\n===================================")
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

                # Create
                if menu == "1":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("======= TAMBAH KENDARAAN =======")

                    plat = input("Nomor plat: ").strip().upper()

                    plat_ada = False

                    for data in data_kendaraan.values():
                        if data["plat"] == plat:
                            plat_ada = True
                            break

                    if plat == "":
                        print("Error: Nomor plat wajib diisi.")
                    elif plat_ada:
                        print("Error: Nomor plat sudah terdaftar.")
                    else:
                        pemilik = input("Nama pemilik: ").strip()
                        jenis = input(
                            "Jenis kendaraan (Mobil/Motor): "
                        ).strip().capitalize()
                        merek = input("Merek kendaraan: ").strip()
                        tahun = input("Tahun kendaraan: ").strip()

                        tahun_valid = (
                            tahun.isdigit()
                            and len(tahun) == 4
                            and 1899 <= int(tahun) <= 2676
                        )

                        if pemilik == "" or merek == "":
                            print("Error: Data tidak boleh kosong.")
                        elif jenis not in ["Mobil", "Motor"]:
                            print("Error: Jenis harus Mobil atau Motor.")
                        elif not tahun_valid:
                            print("Error: Tahun kendaraan tidak valid.")
                        else:
                            data_kendaraan[id_berikutnya] = {
                                "plat": plat,
                                "pemilik": pemilik,
                                "jenis": jenis,
                                "merek": merek,
                                "tahun": int(tahun),
                                "username": username
                            }

                            print("Data kendaraan berhasil ditambahkan!")
                            print("ID kendaraan:", id_berikutnya)
                            id_berikutnya += 1

                # Read
                elif menu == "2":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("========== DATA KENDARAAN ==========")

                    if len(data_kendaraan) == 0:
                        print("Belum ada data kendaraan.")
                    else:
                        for id_kendaraan, data in data_kendaraan.items():
                            print("-----------------------------------")
                            print("ID           :", id_kendaraan)
                            print("Nomor Plat   :", data["plat"])
                            print("Nama Pemilik :", data["pemilik"])
                            print("Jenis        :", data["jenis"])
                            print("Merek        :", data["merek"])
                            print("Tahun        :", data["tahun"])
                            print("Input Oleh   :", data["username"])

                # Update
                elif menu == "3":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("========= UBAH KENDARAAN =========")

                    id_input = input("Masukkan ID kendaraan: ").strip()

                    if not id_input.isdigit():
                        print("Error: ID harus berupa angka.")
                    else:
                        id_kendaraan = int(id_input)

                        if id_kendaraan not in data_kendaraan:
                            print(
                                "Error: Data tidak ditemukan "
                                "atau Anda tidak memiliki akses."
                            )
                        else:
                            data = data_kendaraan[id_kendaraan]

                            if role != "Admin" and data["username"] != username:
                                print(
                                    "Error: Data tidak ditemukan "
                                    "atau Anda tidak memiliki akses."
                                )
                            else:
                                print("Data lama:", data)

                                plat_baru = input(
                                    "Nomor plat baru: "
                                ).strip().upper()

                                plat_baru_ada = False

                                for id_lain, kendaraan in data_kendaraan.items():
                                    if (
                                        kendaraan["plat"] == plat_baru
                                        and id_lain != id_kendaraan
                                    ):
                                        plat_baru_ada = True
                                        break

                                if plat_baru == "":
                                    print("Error: Nomor plat wajib diisi.")
                                elif plat_baru_ada:
                                    print("Error: Nomor plat sudah digunakan.")
                                else:
                                    pemilik_baru = input(
                                        "Nama pemilik baru: "
                                    ).strip()

                                    jenis_baru = input(
                                        "Jenis baru (Mobil/Motor): "
                                    ).strip().capitalize()

                                    merek_baru = input(
                                        "Merek baru: "
                                    ).strip()

                                    tahun_baru = input(
                                        "Tahun baru: "
                                    ).strip()

                                    tahun_valid = (
                                        tahun_baru.isdigit()
                                        and len(tahun_baru) == 4
                                        and 1899 <= int(tahun_baru) <= 2676
                                    )

                                    if pemilik_baru == "" or merek_baru == "":
                                        print("Error: Data tidak boleh kosong.")
                                    elif jenis_baru not in ("Mobil", "Motor"):
                                        print("Error: Jenis kendaraan tidak valid.")
                                    elif not tahun_valid:
                                        print("Error: Tahun kendaraan tidak valid.")
                                    else:
                                        data["plat"] = plat_baru
                                        data["pemilik"] = pemilik_baru
                                        data["jenis"] = jenis_baru
                                        data["merek"] = merek_baru
                                        data["tahun"] = int(tahun_baru)

                                        print("Data berhasil diperbarui!")

                # Delete
                elif menu == "4":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("========= HAPUS KENDARAAN =========")

                    id_input = input("Masukkan ID kendaraan: ").strip()

                    if not id_input.isdigit():
                        print("Error: ID harus berupa angka.")
                    else:
                        indeks = -1
                        id_kendaraan = int(id_input)
                        if id_kendaraan not in data_kendaraan:
                            print(
                                "Error: Data tidak ditemukan "
                                "atau Anda tidak memiliki akses."
                            )
                        else:
                            kendaraan = data_kendaraan[id_kendaraan]

                            if role != "Admin" and kendaraan["username"] != username:
                                print(
                                    "Error: Data tidak ditemukan "
                                    "atau Anda tidak memiliki akses."
                                )
                            else:
                                print("Data yang akan dihapus:")
                                print("ID           :", id_kendaraan)
                                print("Nomor Plat   :", kendaraan["plat"])
                                print("Nama Pemilik :", kendaraan["pemilik"])
                                print("Jenis        :", kendaraan["jenis"])
                                print("Merek        :", kendaraan["merek"])
                                print("Tahun        :", kendaraan["tahun"])

                                konfirmasi = input(
                                    "Yakin hapus data? (y/n): "
                                ).strip().lower()

                                if konfirmasi == "y":
                                    data_kendaraan.pop(id_kendaraan)
                                    print("Data berhasil dihapus!")
                                elif konfirmasi == "n":
                                    print("Penghapusan dibatalkan.")
                                else:
                                    print("Error: Pilihan harus y atau n.")

                # Lihat Data Pengguna
                elif menu == "5" and role == "Admin":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("========== DATA PENGGUNA ==========")

                    if len(akun) == 0:
                        print("Belum ada data pengguna.")
                    else:
                        i = 1
                        for username, data in akun.items():
                            print("-------------------------------")
                            print("Nomor   :", i)
                            print("Username:", username)
                            print("Role    :", data["role"])
                            i += 1

                # Edit Data Pengguna
                elif menu == "6" and role == "Admin":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("========== EDIT DATA PENGGUNA ==========")
                    i = 1
                    for username_akun, data in akun.items():
                        print("-------------------------------")
                        print("Nomor   :", i)
                        print("Username:", username_akun)
                        print("Role    :", data["role"])
                        i += 1

                    nomor = input(
                        "Pilih nomor akun yang ingin diedit: "
                    ).strip()

                    if not nomor.isdigit():
                        print("Error: Nomor harus berupa angka.")
                    elif int(nomor) < 1 or int(nomor) > len(akun):
                        print("Error: Akun tidak ditemukan.")
                    else:
                        indeks = int(nomor) - 1
                        username_lama = list(akun.keys())[indeks]

                        if username_lama == username:
                            print("Error: Anda tidak dapat mengedit akun sendiri.")
                        else:
                            print(
                                "Data lama:",
                                username_lama,
                                "-",
                                akun[username_lama]["role"]
                            )

                            username_baru = input(
                                "Username baru: "
                            ).strip()

                            password_baru = input(
                                "Password baru: "
                            ).strip()

                            role_baru = input(
                                "Role baru (User/Admin): "
                            ).strip().capitalize()

                            username_ada = False

                            for i in akun:
                                if i != username_lama and i == username_baru:
                                    username_ada = True

                            if username_baru == "" or password_baru == "":
                                print("Error: Username dan password wajib diisi.")
                            elif username_ada:
                                print("Error: Username sudah digunakan.")
                            elif role_baru not in ["User", "Admin"]:
                                print("Error: Role harus User atau Admin.")
                            else:
                                akun[username_baru] = akun.pop(username_lama)
                                akun[username_baru]["password"] = password_baru
                                akun[username_baru]["role"] = role_baru

                                for kendaraan in data_kendaraan.values():
                                    if kendaraan["username"] == username_lama:
                                        kendaraan["username"] = username_baru

                                print("Data pengguna berhasil diperbarui!")

                # Hapus Akun Pengguna
                elif menu == "7" and role == "Admin":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("========== HAPUS AKUN PENGGUNA ==========")

                    i = 1
                    for username_akun, data in akun.items():
                        print("-------------------------------")
                        print("Nomor   :", i)
                        print("Username:", username_akun)
                        print("Role    :", data["role"])
                        i += 1

                    nomor = input("Pilih nomor akun yang ingin dihapus: ").strip()

                    if not nomor.isdigit():
                        print("Error: Nomor harus berupa angka.")
                    elif int(nomor) < 1 or int(nomor) > len(akun):
                        print("Error: Akun tidak ditemukan.")
                    else:
                        indeks = int(nomor) - 1
                        username_target = list(akun.keys())[indeks]

                        if username_target == username:
                            print("Error: Tidak dapat menghapus akun sendiri.")
                        elif akun[username_target]["role"] == "Admin":
                            print("Error: Akun Admin tidak boleh dihapus.")
                        else:
                            print("Akun yang akan dihapus:", username_target)
                            konfirmasi = input("Yakin hapus akun? (y/n): ").strip().lower()

                            if konfirmasi == "y":
                                akun.pop(username_target)
                                print("Akun pengguna berhasil dihapus!")
                            elif konfirmasi == "n":
                                print("Penghapusan dibatalkan.")
                            else:
                                print("Error: Pilihan harus y atau n.")

                # Logout
                elif menu == "0":
                    masuk_menu = False
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Anda berhasil logout.")

                else:
                    print("Error: Menu tidak tersedia.")

                if masuk_menu:
                    input("\nTekan Enter untuk melanjutkan...")

        else:
            print("Error: Username atau password salah.")
        
    # Register
    elif opsi == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("========== REGISTER ==========")

        username_baru = input("Buat username: ").strip()
        password_baru = input("Buat password: ").strip()

        username_ada = False

        for user in akun:
            if user == username_baru:
                username_ada = True

        if username_baru == "" or password_baru == "":
            print("Error: Username dan password wajib diisi.")
        elif username_ada:
            print("Error: Username sudah digunakan.")
        else:
            akun[username_baru] = {
            "password": password_baru,
            "role": "User"
            }
            print("Registrasi berhasil!")
            print("Silakan login menggunakan akun baru.")
            input("\nTekan Enter untuk melanjutkan...")

    # keluar program
    elif opsi == "3":
        print("Terima kasih telah menggunakan Program ini!")
        break
    else:
        print("Error: Pilihan menu tidak tersedia.")
        input("\nTekan Enter untuk melanjutkan...")
