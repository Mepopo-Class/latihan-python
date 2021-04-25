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

user_inp = input("Masukkan Username: ")

if user_inp == username:
  print(f"Selamat Datang {username}")
  password_inp = input("Masukkan password: ")
  if password_inp == password:
    print("Berhasil Lomgin")
  else:
    print("Password Salah")
else:
  print("Password Salah")