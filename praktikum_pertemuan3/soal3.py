usia = int(input("Masukkan usia (tahun): "))
if usia >= 0:
    if usia <= 5:
        print("Kategori: Balita")
    elif usia <= 12:
        print("Kategori: Anak")
    elif usia <= 17:
        print("Kategori: Remaja")
    elif usia <= 59:
        print("Kategori: Dewasa")
    else:
        print("Kategori: Lansia")
else:
    print("Usia tidak valid! Usia tidak boleh negatif.")