# Soal 3 - Reaktor Nuklir Chernobyl

suhu = float(input("Masukkan suhu reaktor (Celcius): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

print("\nSuhu yang diinputkan    :", suhu, "derajat Celcius")
print("Tekanan yang diinputkan :", tekanan, "Bar")

# Nested if untuk status bahaya
if suhu > 1000:
    if tekanan > 50:
        pesan = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        pesan = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu > 500: 
    if tekanan > 30:
        pesan = "Tekanan Tidak Stabil"
    else:
        pesan = "Operasi Reaktor Normal"
else:
    pesan = "Reaktor Belum Cukup Panas"

print("Status bahaya reaktor   :", pesan)

# Ternary operator untuk pompa air
pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"
print("Status pompa air        :", pompa)
