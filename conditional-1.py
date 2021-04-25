# < Soal >
# buatlah logika if-else yang dapat mendeteksi angka ganjil atau genap

# < Ketentuan >
# print "genap" jika bilangannya genap dan print "ganjil" jika bilangannya ganjil
# value yang diseleksi dari user input

# < Tips >
# pastikan anda sudah mengcasting variabel user_inp kedalam int()

user_inp = int(input("Masukkan angka: "))
if user_inp % 2 == 0:
  print("Angka yang anda masukkan adalah Genap")
else:
  print("Angka yang anda masukkan adalah Ganjil")