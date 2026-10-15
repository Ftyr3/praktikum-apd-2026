import os

# (username, password, level_akses)
akun = [
    ["admin", "admin123", "Admin"],
    ["Daniel", "054", "User"]
]

# [id, nomor plat, nama pemilik, jenis, merek, tahun, username]
data_kendaraan = [
    [1, "KT 1234 AB", "Robin", "Mobil", "Toyota Avanza", 2022, "Daniel"],
    [2, "KT 5678 CD", "Afid", "Motor", "Honda Vario", 2023, "Daniel"]
]

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
            for user in akun:
                if user[0] == username and user[1] == password:
                    login_berhasil = True
                    role = user[2]

            if login_berhasil == False:
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

                menu = input("Pilih menu: ")

                # Create
                if menu == "1":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("======= TAMBAH KENDARAAN =======")

                    plat = input("Nomor plat: ").strip().upper()

                    plat_ada = False

                    for data in data_kendaraan:
                        if data[1] == plat:
                            plat_ada = True

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
                            data_kendaraan.append([
                                id_berikutnya,
                                plat,
                                pemilik,
                                jenis,
                                merek,
                                int(tahun),
                                username
                            ])

                            id_berikutnya += 1
                            print("Data kendaraan berhasil ditambahkan!")

                # Read
                elif menu == "2":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("========== DATA KENDARAAN ==========")

                    if len(data_kendaraan) == 0:
                        print("Belum ada data kendaraan.")
                    else:
                        for data in data_kendaraan:
                            print("-----------------------------------")
                            print("ID             :", data[0])
                            print("Nomor Plat   :", data[1])
                            print("Nama Pemilik   :", data[2])
                            print("Jenis          :", data[3])
                            print("Merek          :", data[4])
                            print("Tahun          :", data[5])
                            print("Input Oleh     :", data[6])

                # Update
                elif menu == "3":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("========= UBAH KENDARAAN =========")

                    id_input = input("Masukkan ID kendaraan: ").strip()

                    if not id_input.isdigit():
                        print("Error: ID harus berupa angka.")
                    else:
                        indeks = -1

                        for i in range(len(data_kendaraan)):
                            if data_kendaraan[i][0] == int(id_input):
                                if (
                                    role == "Admin"
                                    or data_kendaraan[i][6] == username
                                ):
                                    indeks = i

                        if indeks == -1:
                            print(
                                "Error: Data tidak ditemukan "
                                "atau Anda tidak memiliki akses."
                            )
                        else:
                            print("Data lama:", data_kendaraan[indeks])
                            plat_baru = input(
                                "Nomor plat baru: "
                            ).strip().upper()

                            plat_baru_ada = False

                            for data in data_kendaraan:
                                if (
                                    data[1] == plat_baru
                                    and data[0] != data_kendaraan[indeks][0]
                                ):
                                    plat_baru_ada = True

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

                                if (
                                    pemilik_baru == ""
                                    or merek_baru == ""
                                ):
                                    print("Error: Data tidak boleh kosong.")
                                elif jenis_baru not in ["Mobil", "Motor"]:
                                    print("Error: Jenis kendaraan tidak valid.")
                                elif not tahun_valid:
                                    print("Error: Tahun kendaraan tidak valid.")
                                else:
                                    data_kendaraan[indeks][1] = plat_baru
                                    data_kendaraan[indeks][2] = pemilik_baru
                                    data_kendaraan[indeks][3] = jenis_baru
                                    data_kendaraan[indeks][4] = merek_baru
                                    data_kendaraan[indeks][5] = int(tahun_baru)

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

                        for i in range(len(data_kendaraan)):
                            if data_kendaraan[i][0] == int(id_input):
                                if (
                                    role == "Admin"
                                    or data_kendaraan[i][6] == username
                                ):
                                    indeks = i

                        if indeks == -1:
                            print(
                                "Error: Data tidak ditemukan "
                                "atau Anda tidak memiliki akses."
                            )
                        else:
                            print("Data yang akan dihapus:")
                            print(data_kendaraan[indeks])

                            konfirmasi = input(
                                "Yakin hapus data? (y/n): "
                            ).strip().lower()

                            if konfirmasi == "y":
                                data_kendaraan.pop(indeks)
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
                        for i in range(len(akun)):
                            print("-------------------------------")
                            print("Nomor   :", i + 1)
                            print("Username:", akun[i][0])
                            print("Role    :", akun[i][2])

                # Edit Data Pengguna
                elif menu == "6" and role == "Admin":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("========== EDIT DATA PENGGUNA ==========")

                    for i in range(len(akun)):
                        print("-----------------------------------")
                        print("Nomor   :", i + 1)
                        print("Username:", akun[i][0])
                        print("Role    :", akun[i][2])

                    nomor = input(
                        "Pilih nomor akun yang ingin diedit: "
                    ).strip()

                    if not nomor.isdigit():
                        print("Error: Nomor harus berupa angka.")
                    elif int(nomor) < 1 or int(nomor) > len(akun):
                        print("Error: Akun tidak ditemukan.")
                    else:
                        indeks = int(nomor) - 1

                        if akun[indeks][0] == username:
                            print("Error: Anda tidak dapat mengedit akun sendiri.")
                        else:
                            print("Data lama:", akun[indeks][0], "-", akun[indeks][2])

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

                            for i in range(len(akun)):
                                if i != indeks and akun[i][0] == username_baru:
                                    username_ada = True

                            if username_baru == "" or password_baru == "":
                                print("Error: Username dan password wajib diisi.")
                            elif username_ada:
                                print("Error: Username sudah digunakan.")
                            elif role_baru not in ["User", "Admin"]:
                                print("Error: Role harus User atau Admin.")
                            else:
                                akun[indeks][0] = username_baru
                                akun[indeks][1] = password_baru
                                akun[indeks][2] = role_baru

                                print("Data pengguna berhasil diperbarui!")

                # Hapus Akun Pengguna
                elif menu == "7" and role == "Admin":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("========== HAPUS AKUN PENGGUNA ==========")

                    for i in range(len(akun)):
                        print("-----------------------------------")
                        print("Nomor   :", i + 1)
                        print("Username:", akun[i][0])
                        print("Role    :", akun[i][2])

                    nomor = input("Pilih nomor akun yang ingin dihapus: ").strip()

                    if not nomor.isdigit():
                        print("Error: Nomor harus berupa angka.")
                    elif int(nomor) < 1 or int(nomor) > len(akun):
                        print("Error: Akun tidak ditemukan.")
                    else:
                        indeks = int(nomor) - 1

                        if akun[indeks][0] == username:
                            print("Error: Tidak dapat menghapus akun sendiri.")
                        elif akun[indeks][2] == "Admin":
                            print("Error: Akun Admin tidak boleh dihapus.")
                        else:
                            print("Akun yang akan dihapus:", akun[indeks][0])
                            konfirmasi = input("Yakin hapus akun? (y/n): ").strip().lower()

                            if konfirmasi == "y":
                                akun.pop(indeks)
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
            if user[0] == username_baru:
                username_ada = True

        if username_baru == "" or password_baru == "":
            print("Error: Username dan password wajib diisi.")
        elif username_ada:
            print("Error: Username sudah digunakan.")
        else:
            akun.append([
                username_baru,
                password_baru,
                "User"
            ])
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
