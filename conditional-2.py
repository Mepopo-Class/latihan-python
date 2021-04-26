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

user_inp = input("Masukkan username: ")
if user_inp == username:
  pass_inp = input("Masukkan password: ")
  if pass_inp == password:
    print("Berhasil login")
  else:
    print("Password salah")
else:
  print("Username salah")