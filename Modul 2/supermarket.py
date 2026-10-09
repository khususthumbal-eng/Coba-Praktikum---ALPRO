# Soal 2 - Supermarket KOPERASI NDESO

total = int(input("Masukkan total belanja (Rp): "))

print("\nTotal belanja awal sebelum diskon : Rp", total)

# Diskon diseleksi berurutan dari promo terbesar ke terkecil
if total % 100000 == 0:
    bayar = 0
    print("Promo: Belanjaan digratiskan!")
elif total % 50000 == 0:
    bayar = total - (total * 50 // 100)
    print("Promo: Diskon 50%")
elif total % 10000 == 0:
    bayar = total - (total * 20 // 100)
    print("Promo: Diskon 20%")
elif total >= 200000:
    bayar = total - (total * 10 // 100)
    print("Promo: Diskon 10%")
else:
    bayar = total
    print("Promo: Tidak ada diskon, bayar harga normal")

print("Total harga akhir yang dibayar    : Rp", bayar)

# Ternary operator untuk poin keanggotaan
status_poin = "Poin Bertambah" if bayar > 0 else "Tidak Ada Poin"
print("Status poin keanggotaan           :", status_poin)
