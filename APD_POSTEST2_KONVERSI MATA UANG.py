# Judul Program
print("======================================")
print("   PROGRAM KONVERSI NILAI MATA UANG   ")
print("======================================")
print("")

# Menu untuk pilih konversi
def mata_uang() :
    print("--------MENU--------")
    print("[1] Konversi IDR-USD")
    print("[2] Konversi IDR-SGD")
    print("[3] Konversi IDR-EUR")
    print("[4] Konversi IDR-JPY")
    print("[5] Keluar")

# Program 
while True:
    mata_uang()
    pilih = input("Masukkan pilihan:")
    pilih = int(pilih)

    if pilih==1 :
        nominal = int(input("Masukkan nominal:Rp"))
        kurs = 14194
        hasil = nominal / kurs
        print(f"{nominal} IDR senilai dengan {hasil} USD")
        print("")
    
    elif pilih==2 :
        nominal = int(input("Masukkan nominal:Rp"))
        kurs = 10534
        hasil = nominal / kurs
        print(f"{nominal} IDR senilai dengan {hasil} SGD")
        print("")

    elif pilih==3 :
        nominal = int(input("Masukkan nominal:Rp"))
        kurs = 16467
        hasil = nominal / kurs
        print(f"{nominal} IDR senilai dengan {hasil} EUR")
        print("")

    elif pilih==4 :
        nominal = int(input("Masukkan nominal:Rp"))
        kurs = 124
        hasil = nominal / kurs
        print(f"{nominal} IDR senilai dengan {hasil} JPY")
        print("")

    else :
        print("Konversi Mata Uang Selesai")
        break


