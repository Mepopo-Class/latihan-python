# < Soal >
# Buat program login

# < Ketentuan >
# user diminta input username dan password
# jika keduanya benar maka print: "Berhasil login"
# jika password saja yg salah: "Password salah"
# jika username salah: "Username salah"

# < Tips >
# gunakan if-else bercabang, misal:
# if blabla:
#   print(blabla)
#   if blabla:
#     print(blabla)
#   else:
#     print(blabla)
# else:
#   dst..

username = "admin"
password = "rimoromi"

# inpUser = input("Masukkan Username ")
# inpPass = input("Masukkan Password ")

# if inpUser == username and inpPass == password:
#     print("Berhasil Login")
# elif inpUser != username and inpPass != password:
#     print("Username dan Password Salah")
# elif inpUser != username:
#     print("Username Salah")
# elif inpPass != password:
#     print("Password Salah")


# Ini Versi Bercabang Yang Dikasih Rahman Hanya Saya Ubah Sedikit
while True:
    inpUser = input("Masukkan Username ")

    if inpUser == username:
        print("Hemlo", username, "\n")
        inpPass = input("Masukkan Password ")
        if inpPass != password:
            print("Password Salah, Coba Lagi\n")
        else:
            print("Berhasil Login")
            break
    else:
        print("Username Salah, Coba Lagi\n")
