# < Soal >
# Loop lah string berikut menjadi terbalik

# < Ketentuan >
# reverse string berikut
# buat variabel terpisah untuk wadah jawaban
# ambil per huruf dan incrementkan pada variabel wadah
# cara ambil per huruf.. nama_variabel[index]
# output yg diharapkan:
# sucsibiH

# < Tips >
# Gunakan kembali teknik yg pernah digunakan pada soal loop array terbalik (loop-3)
# gunakan concate string += dan assign nilainya ke variabel wadah


kata = "Hibiscus"
panjang = len(kata) - 1
jawaban = ""

for i in range(panjang, -1, -1):
    jawaban += kata[i]

print(jawaban)
