# List nilai awal
nilai = [85, 70, 92, 60, 78]

# Menampilkan jumlah data, total, dan rata-rata
print("Jumlah data:", len(nilai))
print("Total:", sum(nilai))
print("Rata-rata:", sum(nilai) / len(nilai))

# Menampilkan urutan naik (ascending) menggunakan sorted()
print("Urut naik:", sorted(nilai))

# Menampilkan urutan turun (descending) menggunakan sorted dengan reverse=True
print("Urut turun:", sorted(nilai, reverse=True))

# Menampilkan list asli untuk membuktikan sorted() tidak mengubah list awal
print("List asli:", nilai)