# < Soal >
# Loop lah array berikut dengan terbalik

# < Ketentuan >
# dilarang menggunakan function reversed()
# sebagai ganti gunakan function range(), baca:
# https://www.w3schools.com/python/ref_func_range.asp

# < Tips >
# manfaatkan parameter step pada function range() untuk mendapatkan index mundur
# parameter range: range(<start>, <end>, <step>)


data = ['alpha', 'bravo', 'charlie', 'delta', 'echo']
panjang_data = len(data) - 1

for i in range(panjang_data, -1, -1):
    print(data[i])
