# < Soal >
# seleksi data dalam array (ganjil atau genap)

# < Ketentuan >
# print "genap" jika bilangannya genap dan print "ganjil" jika bilangannya ganjil
# output yg diharapkan:
  # Genap
  # Ganjil
  # Genap 
  # Ganjil
  # Ganjil
  

data = [2, 23, 4, 9, 3]

for i in data:
  if i % 2 == 0:
    print("genap")
  elif i % 2 == 1:
    print("ganjil")