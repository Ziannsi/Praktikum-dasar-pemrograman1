# Daftar nama mahasiswa
nama_mahasiswa = ["Ayu", "Bima", "Citra", "Doni"]

# Meminta input dari pengguna
cari = input("Nama yang dicari: ")

# Memeriksa keberadaan nama menggunakan operator 'in'
if cari in nama_mahasiswa:
    print("Nama ditemukan")
else:
    print("Nama tidak ditemukan")