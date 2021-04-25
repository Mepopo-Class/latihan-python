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

soal =  [
  {
    "kuwesen": "Apakah rita kawaii?",
    "enswer" : "ya"
  },
  {
    "kuwesen": "Apakah mei-senpai kawaii?",
    "enswer" : "ya"
  },
  {
    "kuwesen": "Apakah renie kawaii?",
    "enswer" : "ya"
  },
  {
    "kuwesen": "Apakah rita suka dengan kapten??",
    "enswer" : "tentu saja"
  },
  {
    "kuwesen": "Apakah kapten suka dengan rita??",
    "enswer" : "tentu saja"
  },
]

for s in soal:
  print(f"Soal:{s['kuwesen']}")
  jawaban = input("masukkan jawaban anda: ")
  if s['enswer'] == jawaban:
    print("Selamat jawaban benar")
    point += 1
  else:
    print("jawaban anda salah")

print("Nilai anda adalah:",point)
