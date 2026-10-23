total_belanja = int(input("Masukkan total belanja (Rp): "))
if total_belanja >= 500000:
    diskon_persen = 20
elif total_belanja >= 200000:
    diskon_persen = 10
else:
    diskon_persen = 0
nominal_diskon = total_belanja * (diskon_persen / 100)
total_bayar = total_belanja - nominal_diskon
print(f"Diskon: {diskon_persen}% (Rp{int(nominal_diskon):,})")
print(f"Total Bayar: Rp{int(total_bayar):,}")