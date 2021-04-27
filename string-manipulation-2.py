# < Soal >
# Manipulasilah string berikut

# < Ketentuan >
# rubah string berikut dari:
# Hibiscus
# menjadi:
# H-i-b-i-s-c-u-s

# < Tips >
# gunakan teknik increment
# ambil per huruf lalu incrementkan dengan garisnya (-)


kata = "Hibiscus"
panjang = len(kata)
cetak = ""

for i in range(panjang):
    cetak += kata[i]
    if i < len(kata) - 1:
        cetak += "-"

print(cetak)
