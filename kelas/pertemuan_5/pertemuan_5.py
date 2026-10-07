# formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]

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

sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
print(sirkuit)
# sirkuit.append("Daniel")
# print(sirkuit)
# sirkuit.append("Nando")
# print(sirkuit)
# sirkuit.extend("Larry", "Rendy")
# print(sirkuit)
sirkuit.insert(2, "Alfi")
print(sirkuit)