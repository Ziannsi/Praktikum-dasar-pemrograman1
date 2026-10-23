# Daftar angka dari 1 sampai 10
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Membuat list bilangan genap menggunakan list comprehension dengan kondisi
genap = [x for x in angka if x % 2 == 0]

# Membuat list kuadrat angka menggunakan list comprehension
kuadrat = [x ** 2 for x in angka]

# Menampilkan hasil
print("Genap:", genap)
print("Kuadrat:", kuadrat)