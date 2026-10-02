Perulangan For
batas = 5
for i in range(batas):
	print("Perulangan ke-", i)

Penggunaan For pada List:
game = ["Genshin", 7.0, True]
for i in game:
	print(i)

Struktur Range pada For:
for i in range(1,10,2):
	print(i)

Penggunaan Nested For :
for i in range(1, 3):# Mengontrol baris dalam tabel perkalian
	for j in range(1, 4):# Mengontrol kolom dalam tabel perkalian
		print(f'{i} x {j} = {i * j}')
	print('') #biar ada jarak tiap iterasi

Perulangan While
jawab = "ya"
hitung = 0
while(jawab == "ya"):
	hitung += 1
	print("halo")
	jawab = input("Ulang lagi tidak? ")
print(f"Total Perulangan : {hitung}")

Break
for i in range(10):
	if i == 5:
		break
	print(i)

for i in range(20):
	if i >12:
		break
	print("perulangan ke", i)
	
angka_benar = 7

while True:
	print("game tebak angka")
	
	angka_input = int(input("masukkan angka (1-10: )"))
	angka_input = input("masukkan angka (1-10: ")
	
	if not angka_input.isdigit():
		continue
	
	angka_input = int(angka_input)
	
	
	if angka_benar == angka_input:
		print("angka benar")
		break
	else:
		print("angka salah")


Continue
for i in range(10):
 if i % 2 == 0:
	continue
 print(i)

uang_saku = int(input("masukkan uang saku: "))

while uang_saku >= 0:
	pengeluaran = int(input("masukkan nominal pengeluaran: "))
	saldo_pengeluaran = uang_saku - pengeluaran
	uang_saku = saldo_pengeluaran
	
	print(saldo_pengeluaran)
print(uang_saku)	
