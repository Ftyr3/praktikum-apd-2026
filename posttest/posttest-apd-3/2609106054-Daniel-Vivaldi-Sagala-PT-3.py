nama = "Daniel"
nim = "54"


username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username == nama :
    if password == nim :
        print("Login berhasil")
        total_point = int(input("Masukkan total point rank: "))
        if total_point < 0 :
            print("Total point tidak boleh kurang dari 0")
        elif total_point < 100:
            print("Username:", username)
            print("Rank saat ini: Rokie")
            point_berikutnya = 100 - total_point
            print("Point untuk naik ke Warrior:", point_berikutnya)
        elif total_point <= 299:
            print("Username:", username)
            print("Rank saat ini: Warrior")
            point_berikutnya = 300 - total_point
            print("Point untuk naik ke Master:", point_berikutnya)
        elif total_point <= 999:
            print("Username:", username)
            print("Rank saat ini: Master")
            point_berikutnya = 1000 - total_point
            print("Point untuk naik ke Grand Master:", point_berikutnya)
        elif total_point <= 4999:
            print("Username:", username)
            print("Rank saat ini: Grand Master")
            point_berikutnya = 5000 - total_point
            print("Point untuk naik ke Legend:", point_berikutnya)
        else:
            print("Username:", username)
            print("Rank saat ini: Legend")
            print("Selamat Anda telah mencapai rank tertinggi!!11!!!!111!")
    else:
        print("Password salah")
else:
    print("Username salah")