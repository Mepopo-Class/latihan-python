# < Soal >
# Buatlah program untuk mengurutkan angka dari kecil ke besar

# < Ketentuan >
# user diminta 3 kali input angka
# 3 angka tadi diprint dari kecil ke besar
# pakai logika kasaran tidak apa apa
# output yg diinginkan:
  # Peringkat satu: 12
  # Peringkat dua: 5  
  # Peringkat tiga: 4 


# < Tips >
# gunakan if-else bercabang:
# gunakan gerbang logika AND

user_inp1 = int(input("Masukkan angka pertama: "))
user_inp2 = int(input("Masukkan angka kedua: "))
user_inp3 = int(input("Masukkan angka ketiga: "))

if user_inp1 < user_inp2 and user_inp1 < user_inp3:
  if user_inp2 < user_inp3:
    print("Pertama: ", user_inp1)
    print("Kedua: ", user_inp2)
    print("Ketiga: ", user_inp3)
  else:
    print("Pertama: ", user_inp1)
    print("Kedua: ", user_inp3)
    print("Ketiga: ", user_inp2)
elif user_inp2 < user_inp1 and user_inp2 < user_inp3:
  if user_inp1 < user_inp3:
    print("Pertama: ", user_inp2)
    print("Kedua: ", user_inp1)
    print("Ketiga: ", user_inp3)
  else:
    print("Pertama: ", user_inp2)
    print("Kedua: ", user_inp3)
    print("Ketiga: ", user_inp1)
elif user_inp3 < user_inp2 and user_inp3 < user_inp1:
  if user_inp2 < user_inp1:
    print("Pertama: ", user_inp3)
    print("Kedua: ", user_inp2)
    print("Ketiga: ", user_inp1)
  else:
    print("Pertama: ", user_inp3)
    print("Kedua: ", user_inp1)
    print("Ketiga: ", user_inp2)