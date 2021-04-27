# < Soal >
# Ambil judul postingan pada path berikut

# < Ketentuan >
# gunakanlah built-in function dan method python
# pada soal ini kita pakai method .split(), baca:
# https://www.w3schools.com/python/ref_string_split.asps

# < Output >
# Judul postingan: cara-bernafas

# < Tips >
# pay $999 to unlock tips..

# Method ku
path = "postingan/trending/cara-bernafas"

posting, trend, judul = path.split('/')

print("judul postingan :", judul)

# Method Seng Dikandani Ipan
jumdul = path.split('/')
print("\nJudul Postingan :", jumdul[2])
