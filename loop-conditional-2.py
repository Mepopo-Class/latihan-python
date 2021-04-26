# < Soal >
# Buatlah program celengan(atau apapun anda ingin menyebutnya)

# < Ketentuan >
# ada permintaan user input misal "apakah anda ingin memasukkan koin?"
# jika user memasukan "iya" maka tambahkan +1 koin
# jika user memasukkan koin terlalu banyak (10 misal) maka cegah user menambahkan koin
# jika user memasukan "buka" maka print jumlah koin yg dikeluarkan dan kosongkanlah koin
# program hanya akan berhenti jika user memasukkan "end"

# < Tips >
# gunakan metode increment (var = var + 1) atau (var += 1)

koin = 0

while koin <= 10:
  user_inp = input("Apa yang ingin anda lakukan: ")
  if user_inp == "tambah koin":
    if koin < 10:
      koin += 1
    elif koin == 10:
      print("Koin sudah mencapai batas.")
  elif user_inp == "buka":
    print("Jumlah koin:", koin)
    print("Koin akan direset menjadi 0")
    koin = 0
  elif user_inp == "end":
    break