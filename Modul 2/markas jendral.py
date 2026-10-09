# Soal 4 - Markas CIA Jendral Wito

pin = int(input("Masukkan 3 digit kode PIN: "))
jam = int(input("Masukkan jam kedatangan (0-23): "))

if pin < 100 or pin > 999 or jam < 0 or jam > 23:
    print("Input tidak valid! PIN harus 3 digit dan jam antara 0-23.")
else:
    # Pisahkan digit secara matematis
    digit1 = pin // 100
    digit2 = (pin // 10) % 10
    digit3 = pin % 10

    print("\nDigit pertama :", digit1)
    print("Digit kedua   :", digit2)
    print("Digit ketiga  :", digit3)

    # Status akses pintu garasi
    if pin % 5 == 0:
        if jam < 12:
            print("\nStatus akses : Garasi Pagi Terbuka")
        else:
            print("\nStatus akses : Garasi Malam Terbuka")
            print("Lampu Dinyalakan")
    elif pin % 2 == 0:
        if digit1 + digit3 == digit2:
            print("\nStatus akses : Garasi VIP Terbuka Khusus Bos")
        else:
            print("\nStatus akses : Kode Genap Ditolak, Alarm Berbunyi!")
    else:
        print("\nStatus akses : Akses Ditolak")

    # Ternary operator untuk CCTV
    cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"
    print("Status CCTV  :", cctv)
