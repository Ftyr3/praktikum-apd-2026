# formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]

# Menampilkan(Read)
# print(formula1)
# Output
# ['Suzuka', 10, True, 20.3, ['Lewis Hamilton', 2]]

# print(formula1[3])
# Output
# 20.30
# print(formula1[4][0])
# Output
# "Lewis Hamilton"

# for index,elemen in enumerate(formula1, start=1):
#     print(index, elemen)

# sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
# print(sirkuit)

# Menambah (Create)
# sirkuit.append("Daniel")
# print(sirkuit)
# sirkuit.append("Nando")
# print(sirkuit)
# sirkuit.extend(["Larry", "Rendy"])
# print(sirkuit)
# sirkuit.insert(2, "Alfi")
# print(sirkuit)

# Mengubah(Update)
# sirkuit[2] = "Afif"
# print(sirkuit)
# sirkuit[0:5:2] = ["Rizky", "Naufal", "Rahman"]
# print(sirkuit)

# Menghapus(Delete)
# del sirkuit[4]
# print(sirkuit)
# sirkuit.remove("Afif")
# print(sirkuit)

# ambil_sirkuit = sirkuit.pop(6)
# print(ambil_sirkuit)


# print(sirkuit[0:4:2])

# Operator penjumlahan
# team1 = ["Mercedes", "Ferrari", "MacLaren"]
# team2 = ["Red Bull", "Alpine", "Aston Martin"]

# gabung_team = team1 + team2
# print(gabung_team)

# Operator pengulangan
# juara_WDC = ["MacLaren", "Red Bull"]
# juara = juara_WDC * 3
# print(juara)

# Nested List
# line_up = [
#     ["Ferrari", "Leclerc", 16],
#     ["Mercedes", "Hamilton", 44],
#     ["Red Bull", "Verstappen", 1],
#     ["McLaren", "Norris", 4]
# ]
# print(line_up[2][1])

# for i in line_up:
#     for j in i:
#         print(j)

# Tuple
chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
print(chara)
print(chara[2])
print(chara[-1])
print(chara[4][0])

# Menambah elemen pada tuple
listchara = list(chara)
# listchara.append("Yui ")
# chara = tuple(listchara)
# print(chara)

# listchara.extend(["Kohaku", "Hikaru"])
# chara = tuple(listchara)
# print(chara)

# listchara.insert(2, "Senku")
# chara = tuple(listchara)
# print(chara)

# del listchara[3]
# chara = tuple(listchara)
# print(chara)

chara = ("Yukari", "Yukino", "Odette", "Senku")
(Persona, Oregairu, Genshin, DrStone) = chara

print(Persona)
print(Oregairu)