berat = int(input("Masukkan berat paket (kg): "))
if berat <= 0:
    print("Berat paket tidak valid!")
elif berat <= 1:
    ongkir = 10000
    print(f"Ongkos kirim: Rp{ongkir:,}")
elif berat <= 5:
    ongkir = 20000
    print(f"Ongkos kirim: Rp{ongkir:,}")
else:
    ongkir = 35000
    print(f"Ongkos kirim: Rp{ongkir:,}")