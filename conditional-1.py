# < Soal >
# buatlah logika if-else yang dapat mendeteksi angka ganjil atau genap

# < Ketentuan >
# print "genap" jika bilangannya genap dan print "ganjil" jika bilangannya ganjil
# value yang diseleksi dari user input

# < Tips >
# pastikan anda sudah mengcasting variabel user_inp kedalam int()

inpAngka = int(input("Masukkan Angka Ganjil/Genap "))

if inpAngka % 2 == 0 :
    print("\nAngka Yang Anda Masukkan Adalah", inpAngka, "Termasuk Angka Genap")
elif inpAngka % 2 == 1 :
    print("\nAngka Yang Anda Masukkan Adalah", inpAngka, "Termasuk Angka Ganjil")