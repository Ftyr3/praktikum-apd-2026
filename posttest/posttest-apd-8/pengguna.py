from data import akun, data_kendaraan
from prettytable import PrettyTable


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
