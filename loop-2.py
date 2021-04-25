# < Soal >
# Buat versi rip-off for loop menggunakan while loop

# < Ketentuan >
# nothing..

# < Tips >
# gunakan function len() untuk mengecek panjang data, baca:
# https://www.w3schools.com/python/ref_func_len.asp
# gunakan teknik increment misal (i = i + 1) pada loop


data = ['alpha', 'bravo', 'charlie', 'delta', 'echo']

inc = 0

while inc <= len(data) - 1:
    print(data[inc])
    inc += 1
