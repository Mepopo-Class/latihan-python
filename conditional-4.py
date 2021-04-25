# < Soal >
# Buatlah program untuk mengurutkan angka dari kecil ke besar

# < Ketentuan >
# user diminta 3 kali input angka
# 3 angka tadi diprint dari besar ke kecil
# pakai logika kasaran tidak apa apa
# output yg diinginkan:
# Peringkat satu: 12
# Peringkat dua: 5
# Peringkat tiga: 4


# < Tips >
# gunakan if-else bercabang:
# gunakan gerbang logika AND

satu = int(input("Masukkan Angka "))
dua = int(input("Masukkan Angka Lagi "))
tiga = int(input("Masukkan Angka Terakhir "))

if (satu > dua) and (satu > tiga):
    if (dua > tiga):
        print("\nPeringkat 1 :", satu)
        print("Peringkat 2 :", dua)
        print("Peringkat 3 :", tiga)
    else:
        print("\nPeringkat 1 :", satu)
        print("Peringkat 2 :", tiga)
        print("Peringkat 3 :", dua)
elif (dua > satu) and (dua > tiga):
    if (satu > tiga):
        print("\nPeringkat 1 :", dua)
        print("Peringkat 2 :", satu)
        print("Peringkat 3 :", tiga)
    else:
        print("\nPeringkat 1 :", dua)
        print("Peringkat 2 :", tiga)
        print("Peringkat 3 :", satu)
else:
    if (dua > satu):
        print("\nPeringkat 1 :", tiga)
        print("Peringkat 2 :", dua)
        print("Peringkat 3 :", satu)
    else:
        print("\nPeringkat 1 :", tiga)
        print("Peringkat 2 :", satu)
        print("Peringkat 3 :", dua)
