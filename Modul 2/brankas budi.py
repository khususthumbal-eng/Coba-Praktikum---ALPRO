# Soal 1 - Brankas Kuno Budi

kode = int(input("Masukkan kode rahasia (3 digit): "))

if kode < 100 or kode > 999:
    print("Kode harus tepat 3 digit angka!")
else:
    # Pisahkan digit secara matematis
    digit1 = kode // 100
    digit2 = (kode // 10) % 10
    digit3 = kode % 10

    print("\n=== Hasil Pemisahan Digit ===")
    print("Digit pertama :", digit1)
    print("Digit kedua   :", digit2)
    print("Digit ketiga  :", digit3)

    # Nilai pelacak awal
    pelacak = digit1 * digit3
    print("\nNilai pelacak awal              :", pelacak)

    # Perubahan tahap pertama
    if digit2 % 2 != 0:
        pelacak = pelacak + 25
    else:
        pelacak = pelacak - digit2
    print("Nilai pelacak setelah tahap 1   :", pelacak)

    # Perubahan tahap kedua
    if pelacak % 3 == 0:
        pelacak = pelacak // 3
    else:
        pelacak = pelacak * 2
    print("Nilai pelacak setelah tahap 2   :", pelacak)

    # Status password
    if pelacak > 50:
        print("\nStatus Password : Password terdeteksi sebagai Kategori A")
    elif pelacak > 20:
        print("\nStatus Password : Password terdeteksi sebagai Kategori B")
    else:
        print("\nStatus Password : Password Ditolak")

    # Siklus berdasarkan nilai akhir
    if pelacak % 2 == 0:
        print("Siklus Genap")
    else:
        print("Siklus Ganjil")
