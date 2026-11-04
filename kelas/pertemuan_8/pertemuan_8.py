# Konversi Tipe Data
# bin() – Mengubah integer ke bilangan biner (string)
# bool() – Mengubah ke boolean
# dict() – Membuat dictionary
# float() – Mengubah ke float
# frozenset() – Membuat himpunan (set) yang tidak bisa diubah
# int() – Mengubah ke integer
# list() – Mengubah ke list
# set() – Membuat set
# str() – Mengubah ke string
# tuple() – Mengubah ke tuple
# type() – Mengecek atau membuat tipe objek
angka = int("40") # 40​
string = str(66) # "66"​
data_1 = list("ABC") # ['A', 'B', 'C']​
data_2 = dict(A=11, B=13) # {'A': 11, 'B': 13}​
print(type(data_2)) #  <class 'dict'>


# Operasi Matematika
# abs() – Nilai absolut
# divmod() – Mengembalikan tuple (hasil_bagi, sisa_bagi)
# max() – Nilai maksimum
# min() – Nilai minimum
# pow() – Pangkat (dengan opsi modulus)
# round() – Pembulatan angka
# sum() – Penjumlahan iterable
divmod(9,3) # (3, 0)​
abs(-10) # 10​
pow(3,2) # 9​
max([40, 77, 76]) # 77​
min([40, 77, 76]) # 40​
round(19.6741) # 20 ​
sum([81, 89, 73]) # 243


# Iterasi & Collection
# enumerate() – Memberi indeks pada iterable
# filter() – Memfilter iterable dengan fungsi
# iter() – Membuat iterator dari objek iterable
# len() – Panjang objek
# map() – Menerapkan fungsi ke iterable
# next() - Mengambil item berikutnya dari iterator
# range() – Membuat range angka
# reversed() – Membalik urutan iterable
# slice() – Membuat objek slice
# sorted() – Mengurutkan iterable
for index, value in enumerate(['A','B']):
    print(index, value) # 0 A , 1 B​

len([2, 4, 6, 8 ,10]) # 5​
list(map(str, [5, 15, 25])) # ['5', '15', '25']​
sorted([5, 3, 1]) # [1, 3, 5]​
list(zip([2, 3],['a','b'])) # [(2,'a'), (3,'b')]


# Fungsi Lingkungan (Environment)
# globals() - Mendapatkan variabel global
# locals() - Mendapatkan variabel lokal
x = "Enam puluh tiga"
def fungsi():
    x = 63
    y = 70
    z = 50
    print(globals()['x']) # mendapatkan isi dari variabel x (global)​
    print(locals()['x']) # mendapatkan isi dari variabel x (lokal)​
    print(locals()) # {'x': 63, 'y': 70, 'z': 50}​
fungsi()


# String Methods
# lower() – Mengubah string menjadi huruf kecil
# upper() – Mengubah string menjadi huruf besar
# strip() – Menghapus spasi/karakter tertentu di awal/akhir string
# replace() – Mengganti substring dengan substring lain
# split() – Memisahkan string menjadi list dengan delimiter
# join() – Menggabungkan list menjadi string dengan delimiter
# find() – Menemukan posisi pertama substring (-1 jika tidak ada)
# startswith() – Mengecek apakah string diawali substring tertentu
# endswith() – Mengecek apakah string diakhiri substring tertentu
"PYTHON".lower() # "python"

"saya akan kembali ke desa".upper() # "SAYA AKAN KEMBALI KE DESA"

" loh".strip() # "loh"

"Aku suka praktikum".replace("suka", "cinta") # Aku cinta praktikum

"A, B, C".split(",") # ['A', 'B', 'C']

",".join(['A', 'B', 'C']) # A,B,C

"Karhutla".find("a") # 1

"Karhutla".startswith("Ka") # True

"Pahlawan Pemberantas Karhutla.pdf".endswith(".pdf") # True

# Cara Menggunakan Library
import math # Mengimpor semua fungsi yang ada di dalam library math

from math import sqrt # Hanya mengimpor fungsi sqrt() dari library math

import math as m # Mendefinisikan math dengan nama m

# Built-in Library
# 1. math
# Contoh fungsi yang ada di dalam math: pow(), factorial(), sqrt(), dll.
import math
print(math.sqrt(100))
print(math.factorial(5))
# 2. datetime
# Mendapatkan waktu sekarang, menambah hari, dan memformat waktu
from datetime import datetime
print(datetime.now())
# 3. calendar
# Mengolah, memformat, dan menampilkan informasi terkait penanggalan (kalender)
import calendar as kalender
print(kalender.calendar(2026))
# 4. random
# Contoh fungsi yang ada di dalam random: randint(), choice(), shuffle()
import random

# Menghasilkan satu bilangan bulat acak dari 1 sampai 5 (inklusif)​
print(random.randint(1, 5))

# Memilih 1 elemen acak dari list atau string​
buah = ["pisang", "rambutan", "manggis"]
huruf = "abcd"
print(random.choice(buah))
 # memilih 1 item acak pada list​
print(random.choice(huruf)) # memilih 1 karakter acak pada string​

# Menyusun 4 angka PIN acak menggunakan perulangan​
kumpulan_angka = "0123456789"
pin_acak = ""
for i in range(4):
    pin_acak += random.choice(kumpulan_angka)
print(pin_acak)

# Mengacak urutan elemen di dalam list secara langsung​
kartu = ["As Wajik", "3 Hati", "7 Sekop"]
random.shuffle(kartu)
print(kartu)

# Third-party Library
#  Cara Menginstal dan Mengelola Library Eksternal dengan PIP
# Perintah pip dijalankan langsung melalui Terminal atau Command Prompt (CMD).
# Cara umum menginstal library eksternal​
# pip install prettytable

# Alternatif jika perintah 'pip' tidak dikenali (khususnya di Windows)​
# python -m pip install prettytable

# Melihat daftar library eksternal yang sudah terinstal​
# pip list

# Menghapus library eksternal jika sudah tidak digunakan​
# pip uninstall nama-library