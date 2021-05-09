# < Soal >
# buat function yang dapat memanipulasi variabel global

# < Ketentuan >
# buatlah function untuk memanipulasi variabel "x" berikut
# terserah mau tambah, kurang, kali, dll (yang penting data berubah)
# panggil function sebanyak 2 kali (atau lebih)
# untuk melihat apakah benar variabel global sudah dimanipulasi

# semisal kalo kita buat function "tambahkan"
# dengan fungsionalitasnya menambahkan nilai var dengan +5, maka:
# < Output >
# 15
# 20


x = 10

print("x adalah", x, "\nMari Kita Tambah")


def tambah():
    global x
    x += 5
    print("x =", x)


def kurang():
    global x
    x -= 5
    print("x =", x)


tambah()
tambah()

print("Kita Kurangi lagi biar kembali seperti semula :D")

kurang()
kurang()
