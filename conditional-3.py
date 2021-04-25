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


point = 0

print("Jawab Dengan Baik Dan Benar")

soal1 = str(input("\nSiapakah Penemu Teori Relativitas ? "))
if soal1 == "Albert Einstein":
    point = point + 1
    print("\nBenar !")
else:
    print("\nSalah !")

soal2 = str(input("\nSiapakah Penemu Dinamit ? "))
if soal2 == "Alfred Nobel":
    point = point + 1
    print("\nBenar !")
else:
    print("\nSalah !")

soal3 = str(input("\nSiapakah Penemu Batu Baterai ? "))
if soal3 == "Alessandro Volta":
    point = point + 1
    print("\nBenar !")
else:
    print("\nSalah !")

soal4 = str(input("\nSiapakah Penemu Teori Gravitasi ? "))
if soal4 == "Isaac Newton":
    point = point + 1
    print("\nBenar !")
else:
    print("\nSalah !")

soal5 = str(input("\nSiapakah Penemu Lensa Kacamata ? "))
if soal5 == "Benyamin Franklin":
    point = point + 1
    print("\nBenar !")
else:
    print("\nSalah !")

print("\nPoint Anda Adalah", point * 20)
