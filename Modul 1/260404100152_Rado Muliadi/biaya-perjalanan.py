jarak = 100
bahan_bakar_awal = 1.5
konsumsi_bahan_bakar = 1 / 40
harga_bahan_bakar = 10000
total_jarak = jarak * 2
kebutuhan_bahan_bakar = total_jarak * konsumsi_bahan_bakar
bahan_bakar_dibeli = kebutuhan_bahan_bakar - bahan_bakar_awal
biaya_bahan_bakar = bahan_bakar_dibeli * harga_bahan_bakar

print("Total jarak perjalanan pulang-pergi adalah:", total_jarak, "km")
print("Total kebutuhan bahan bakar untuk seluruh perjalanan adalah:", (kebutuhan_bahan_bakar), "liter")
print("Jumlah bahan bakar yang harus dibeli adalah:", bahan_bakar_dibeli, "liter")
print("Total biaya bahan bakar yang harus dikeluarkan adalah:", int(biaya_bahan_bakar), "rupiah")






