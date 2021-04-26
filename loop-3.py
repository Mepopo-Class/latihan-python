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
length = len(data)
for i in range(length-1,-1,-1):
  print(data[i])