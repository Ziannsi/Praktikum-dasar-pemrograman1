# List nilai mahasiswa
nilai = [85, 70, 92, 60, 78]

# Menggunakan enumerate untuk mendapatkan indeks dan nilai
for indeks, angka in enumerate(nilai):
    print(f"Mahasiswa ke-{indeks + 1}: nilai {angka}")