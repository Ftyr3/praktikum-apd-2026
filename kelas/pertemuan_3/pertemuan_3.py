




























# if kondisi :

cuaca = "cerah"

if cuaca == "hujan":
    print("bawa payung/jas hujan")

print("otw ke kampus")

budget = 20000
cuaca = "hujan"

if budget > 30000 and cuaca == "cerah":
    print("beli yoshinoya")
else:
    print("masak indomie aja")

kendaraan = input("Masukkan jenis kendaraan anda: ").lower().strip()

if kendaraan == "mobil":
    tarif_parkir = 10_000
elif kendaraan == "motor":
    tarif_parkir = 5_000
elif kendaraan == "sepeda":
    tarif_parkir = 6_700
else:
    tarif_parkir = 15_000

print("Tarif parkir yang harus dibayar:", tarif_parkir)

# Bentuk Awal Percabangan IF/ELSE
umur = 20
if umur >= 18:
    status = "Dewasa"
else:
    status = "Belum Dewasa"

# Bentuk Ternary Operator
umur = 20
status = "Dewasa" if umur >= 18 else "Belum Dewasa"

bilangan = -5

status = "bilangan negatif" if bilangan < 0 else "bilangan positif"

print("bilangan adalah:", status)

username = input("masukkan username: ").lower().strip()
password = input("masukkan password: ").lower().strip()

if username == "daniel":
    if password == "054":
        print("login berhasil")
    else:
        print("password salah")
else:
    print("username salah")

angka = 10 / 6
print(f"angka {angka:.02f}")