# < Soal >
# Cari rata rata dari data dalam array berikut!

# < Ketentuan >
# buatlah function untuk menjumlahkan semua data pada array berikut
# setelah dijumlahkan semua maka bagi hasil tersebut dengan banyak data, cari: "rumus rata-rata"
# print hasilnya terletak diluar function
# jadi function hanya digunakan untuk menjumlahkan data lalu mengirim(return) hasilnya

# < Tips >
# buatlah variabel kosong sebagai wadah untuk hasil penjumlahan seluruh datanya
# gunakan looping untuk menjumlahkan
# pastikan untuk me-return-kan hasil tsb

# < Output >
# Rata-rata: 16.285714285714285


angkaku = [12, 24, 14, 13, 12, 20, 19]


def avrg(angkaku):
    jumlah = 0
    angka = angkaku
    # jumlah = sum(angkaku) (Bisa pakai cara Ini, tapi takut ipan marah)
    for i in angka:
        jumlah += i
    return jumlah


jumlah_total = avrg(angkaku)
print("Jumlah Keseluruhan data adalah", jumlah_total)
hasil = jumlah_total / len(angkaku)
print("Rata rata nya adalah", hasil)
