def login():
    print("=== LOGIN ===")
    percobaan = 0

    while percobaan < 3:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        role = ""
        if username in akun and akun[username]["password"] == password:
            role = akun[username]["role"]
            return username, akun[username]["role"]
        else:
            percobaan += 1
            sisa = 3 - percobaan
            if sisa > 0:
                print(f"Username atau password salah! Sisa percobaan: {sisa}")
            else:
                print("Username atau password salah 3 kali. Silahkan mulai ulang")
                input("\nTekan Enter untuk melanjutkan...")
    return None, None

# Register
def register():
    try:
        print("========== REGISTER ==========")

        username = input("Buat username: ").strip()
        password = input("Buat password: ").strip()

        if not username or not password:
            raise ValueError("Username dan password wajib diisi.")

        if username in akun:
            raise ValueError("Username sudah digunakan.")

        akun[username] = {
            "password": password,
            "role": "User"
        }

        print("Registrasi berhasil. Silakan login.")

    except ValueError as error:
        print("Error:", error)
