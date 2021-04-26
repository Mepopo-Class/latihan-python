# < Soal >
# buatlah program quiz low budget menggunakan if-else

# < Ketentuan >
# jika user memasukkan jawaban benar maka tambahkan 1 point(jika salah gausah)
# total soal ada 5 (terserah soal apa)
# jika soal sudah habis maka print point-nya

# < Tips >
# untuk menambahkan point deklarasikan ulang variabel dengan nilainya ditambahkan 1
# contoh penulisan:
# point = point + 1


poin = 0
print("1 + 1 = ...")
jawab1 = int(input("Masukkan jawaban: "))
if jawab1 == 2:
  poin = poin + 1

print("2 + 2 = ...")
jawab2 = int(input("Masukkan jawaban: "))
if jawab2 == 4:
  poin = poin + 1

print("3 + 3 = ...")
jawab3 = int(input("Masukkan jawaban: "))
if jawab3 == 6:
  poin = poin + 1

print("4 + 4 = ...")
jawab4 = int(input("Masukkan jawaban: "))
if jawab4 == 8:
  poin = poin + 1

print("5 + 5 = ...")
jawab5 = int(input("Masukkan jawaban: "))
if jawab5 == 10:
  poin = poin + 1

print("Poin: ", poin)