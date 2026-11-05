from data import data_kendaraan
from prettytable import PrettyTable
from datetime import datetime



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

        if pemilik == "" or merek == "":
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
