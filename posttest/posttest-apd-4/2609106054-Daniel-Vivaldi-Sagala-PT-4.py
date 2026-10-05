nama = "Daniel"
nim = "54"
percobaan_login = 0
login_berhasil = False

while percobaan_login < 3:
    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()

    if username == "" and password == "":
        print("username dan password tidak boleh kosong!")
        percobaan_login += 1
        print("sisa percobaan:", 3 - percobaan_login)
        continue
    elif username == "":
        print("username tidak boleh kosong!")
        percobaan_login += 1
        print("sisa percobaan:", 3 - percobaan_login)
        continue
    elif password == "":
        print("password tidak boleh kosong!")
        percobaan_login += 1
        print("sisa percobaan:", 3 - percobaan_login)
        continue

    if username.lower() != nama.lower and password != nim:
        print("username dan password salah!")
    elif username.lower() != nama.lower:
        print("username salah!")
    elif password != nim:
        print("password salah")
    else:
        print("login berhasil")
        login_berhasil = True
        break

    percobaan_login += 1
    print("sisa percobaan:", 3 - percobaan_login)

if not login_berhasil:
    print("login gagal")
else:
    while True:
        print("MENU DISTRIBUSI PAKET")
        print("1. Paket Reguler, 1 porsi makanan")
        print("2. Paket Anak, 1 porsi makanan")
        print("3. Paket Keluarga, 4 porsi makanan")
        print("4. Keluar")
        opsi = input("Pilih (1-4) : ").strip()
        
        if opsi == "":
            print("opsi tidak boleh kosong!")
            continue

        if not opsi.isdigit():
            print("opsi tidak valid")
            continue

        opsi = int(opsi)

        if opsi < 1 or opsi > 4:
            print("opsi tidak valid")
            continue

        if opsi == 1:
            jenis_paket = "Paket Reguler"
            porsi_per_paket = 1
        elif opsi == 2:
            jenis_paket = "Paket Anak"
            porsi_per_paket = 1
        elif opsi == 3:
            jenis_paket = "Paket Keluarga"
            porsi_per_paket = 4
        elif opsi == 4:
            print("Terima kasih telah menggunakan program.")
            break
            
        while True:
            jumlah_paket = input("Masukkan jumlah paket yang akan dibagikan: ").strip()
            
            if jumlah_paket == "":
                print("jumlah paket tidak boleh kosong!")
                continue
            
            if not jumlah_paket.isdigit():
                print("jumlah paket harus angka!")
                continue

            jumlah_paket = int(jumlah_paket)

            if jumlah_paket <= 0:
                print("jumlah paket harus lebih dari 0!")
                continue

            break

        total_porsi = 0

        for i in range(jumlah_paket):
            total_porsi = total_porsi + porsi_per_paket

        jumlah_penerima = total_porsi

        if total_porsi >= 20:
            bonus = "5 paket buah"

        elif total_porsi >= 10:
            bonus = "3 botol susu"

        elif total_porsi >= 5:
            bonus = "1 paket vitamin"

        else:
            bonus = "Tidak mendapat bonus"

        print("hasil distribusi")

        print(f"Jenis paket: {jenis_paket}")
        print(f"Jumlah paket: {jumlah_paket}")
        print(f"Total porsi: {total_porsi} porsi")
        print(f"Penerima manfaat: {jumlah_penerima} orang")
        print(f"Bonus: {bonus}")
        print("")
        print("Nikmati MBG Bergizi Gratis Los Pollos Hermanos!!11!!")
