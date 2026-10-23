# List bertingkat (nested list) nilai kelas
nilai_kelas = [[80, 90], [75, 85], [88, 92]]

# 1. Menampilkan nilai pertama mahasiswa pertama
# Mahasiswa pertama ada di indeks 0, nilai pertamanya ada di indeks 0
print("Nilai pertama mahasiswa pertama:", nilai_kelas[0][0])

# 2. Menampilkan nilai kedua mahasiswa ketiga
# Mahasiswa ketiga ada di indeks 2, nilai keduanya ada di indeks 1
print("Nilai kedua mahasiswa ketiga:", nilai_kelas[2][1])

# 3. Menghitung dan menampilkan rata-rata setiap mahasiswa
print("\nRata-rata masing-masing mahasiswa:")
for i, data in enumerate(nilai_kelas):
    rata_rata = sum(data) / len(data)
    print(f"Mahasiswa {i + 1}: {rata_rata}")