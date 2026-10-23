usia = int(input("Masukan Usia tahun (tahun): "))
if usia < 0 :
    print("Usia tidak valid!")
elif usia <= 5:
    print("Kategori: Balita")
elif usia <= 15:
    print("Kategori: Anak")
elif usia <= 17:
    print("Kategori: Remaja")
elif usia <= 59:
    print("Kategori Dewasa")
else:
    print("Kategori: Lansia")