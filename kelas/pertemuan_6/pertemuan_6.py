# Set
# Membuat Set
kartu = {"merah", "merah", "biru", "hijau"}
print(kartu)

# set menggunakan list​
matkul = ["apd", "orsikom", "apd", "kalkulus"]
sks = set(matkul)
print(sks)

#set menggunakan tuple​
buah = set(("apel", "jeruk", "mangga", "apel"))
print(buah)

# Mengakses elemen pada Set
angka_ganjil = {1, 3, 5, 7, 9}
for angka in angka_ganjil:
    print (angka)

# Menambahkan elemen pada Set
kelas = {"a", "b", "c"}
kelas.add("d")
print(kelas)

# Menghapus elemen pada Set
buah = {"apel", "mangga", "jeruk"}
buah.remove("mangga")
print(buah)

# Operasi Himpunan pada Set | union(), update(), intersection(), difference()
aslab1 = {"fina", "shasha", "risma", "attar"}
aslab2 = {"larry", "attar", "haekal", "risma"}
# gabung = aslab1.union(aslab2)
# print(gabung)
# aslab1.update(aslab2)
# print(aslab1)
# irisan = aslab1.intersection(aslab2)
# print(irisan)
beda = aslab2.difference(aslab1)
print(beda)

# Dictionary
# Contoh Dictionary
Matkul = {
    "Matkul_ganjil" : "kalkulus",
    "Matkul_genap" : "statistik"
}
print(Matkul["Matkul_ganjil"])
print(Matkul)

# Membuat Dictionary
Biodata = {
    "Nama" : "Siti Julpa",
    "NIM" : 25091060,
    "KRS" : ["Struktur Data", "Basis Data"],
    "Mahasiswa_Aktif" : True,
    "Instagram" : "julpatarr"
}

# dictionary menggunakan dict()
List_game = dict(Genshin_Impact="Open World", Mole="Moba", Stardew_Valley="Farming Simulation")

# Mengakses Item Pada Dictionary
# Format : nama_dictionary[key]
Biodata = {
    "Nama" : "Siti Julpa",
    "NIM" : 25091060,
    "KRS" : ["Struktur Data", "Basis Data"],
    "Mahasiswa_Aktif" : True,
    "Instagram" : "julpatarr"
}

print(f"Nama saya adalah {Biodata['Nama']}")
print(f"Saya mengambil mata kuliah {Biodata['KRS'][0]} dan {Biodata['KRS'][1]}")

# Menggunakan metode .get()
# Format : nama_dictionary.get(key)
Biodata = {
    "Nama" : "Siti Julpa",
    "NIM" : 25091060,
    "KRS" : ["Struktur Data", "Basis Data"],
    "Mahasiswa_Aktif" : True,
    "Instagram" : "julpatarr"
}

print(f"Nama saya adalah {Biodata.get('Nama')}")
print(Biodata.get("Nama"))
print(Biodata.get("Alamat"))
print(Biodata.get("Alamat", "Key untuk alamat tidak ada"))

# Perulangan Dalam Dictionary
# Perulangan untuk menampilkan key
game = {
    "pou" : "chill",
    "genshin impact" : "action",
    "valorant" : "fps",
    "minecraft" : "sandbox",
    "mobile legend" : "moba"
}

for i in game:
    print(i)

for i in game.keys():
    print(i)

# Perulangan untuk menampilkan value
game = {
    "pou" : "chill",
    "genshin impact" : "action",
    "valorant" : "fps",
    "minecraft" : "sandbox",
    "mobile legend" : "moba"
}

for i in game.values():
    print(i)

# Perulangan untuk menampilkan key dan value
game = {
    "pou" : "chill",
    "genshin impact" : "action",
    "valorant" : "fps",
    "minecraft" : "sandbox",
    "mobile legend" : "moba"
}

for i, j in game.items():
    print(f"{i} adalah jenis game {j}")

# Menambahkan Item Dalam Dictionary
# Menambah item secara langsung
game = {
    "pou" : "chill",
    "genshin impact" : "action",
    "valorant" : "fps",
    "minecraft" : "sandbox",
    "mobile legend" : "moba"
}

game["resident evil"] = "horror"
print(game)

# Menambah item menggunakan metode .update()
game = {
    "pou" : "chill",
    "genshin impact" : "action",
    "valorant" : "fps",
    "minecraft" : "sandbox",
    "mobile legend" : "moba"
}

game.update({"resident evil" : "horror"})
print(game)

# Menambah key dan value menggunakan metode setdefault()
game = {
    "pou" : "chill",
    "genshin impact" : "action",
    "valorant" : "fps",
    "minecraft" : "sandbox",
    "mobile legend" : "moba"
}

tambah = game.setdefault("resident evil", "horror")
print(game)
print("Tipe game", game.setdefault("grow a garden", "gardening"))

# Mengubah Item Dalam Dictionary
# Menambah item secara langsung
game = {
    "pou" : "chill",
    "genshin impact" : "action",
    "valorant" : "fps",
    "minecraft" : "sandbox",
    "mobile legend" : "moba"
}

print(game)
game["genshin impact"] = "adventure"
print(game)

# Mengubah item menggunakan metode .update()
game = {
    "pou" : "chill",
    "genshin impact" : "action",
    "valorant" : "fps",
    "minecraft" : "sandbox",
    "mobile legend" : "moba"
}


print(game)
game.update({"genshin impact" : "adventure"})
print(game)

# Menghapus Item Dalam Dictionary
# Menghapus menggunakan metode del
aset = {
    "jenis" : "rumah",
    "harga" : 120000000,
    "alamat" : "Jl. Raya No. 1",
    "berpenghuni" : True,
    "luas" : "120m x 80m"
}

print(aset)
del aset["luas"]
print(aset)
print(aset.get("luas"))

# Menghapus menggunakan metode pop()
aset = {
    "jenis" : "rumah",
    "harga" : 120000000,
    "alamat" : "Jl. Raya No. 1",
    "berpenghuni" : True,
    "luas" : "120m x 80m"
}

print(aset)
cache = aset.pop("luas")
print(aset)
print(aset.get("luas"))
print(cache)

# Menghapus menggunakan metode clear()
aset = {
    "jenis" : "rumah",
    "harga" : 120000000,
    "alamat" : "Jl. Raya No. 1",
    "berpenghuni" : True,
    "luas" : "120m x 80m"
}

print(aset)
aset.clear()
print(aset)

# Fungsi yang Dapat Digunakan
# Mengetahui panjang dictionary
aset = {
    "jenis" : "rumah",
    "harga" : 120000000,
    "alamat" : "Jl. Raya No. 1",
    "berpenghuni" : True,
    "luas" : "120m x 80m"
}

print("Panjang dictionary :", len(aset))
print(len(aset))

# Membuat salinan dictionary
menu = {
    "ayam geprek" : 15000,
    "ayam goreng" : 13000,
    "ayam bakar" : 17000,
    "nasi goreng" : 12000,
    "mie goreng" : 10000
}

menu_baru = menu.copy()
menu_baru["nasi goreng"] = 15000

print(menu)
print(menu_baru)

# Membuat dictionary menggunakan key
key = "ayam geprek", "ayam goreng", "ayam bakar",
value = 12000

menu = dict.fromkeys(key, value)
print(menu)

# Dictionary of List dan Nested Dictionary
menu = {
"ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
"nasi" : ["nasi goreng", "nasi uduk"],
"mie" : ["mie goreng rendang", "mie goreng aceh"],
"kuah" : ["soto", "rawon", "sop iga"]
}

for i, j in menu.items():
    print(f"Kategori {i} memiliki menu :")
    for kategori in j:
        print(kategori)
    print("")