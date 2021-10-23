# Judul Program
print("==========================================")
print("            PROGRAM BIODATA               ")
print("==========================================")

# variabel inputan
nama = str(input("Masukkan Nama Anda:"))
nim = int(input("Masukkan NIM Anda:"))
prodi = str(input("Masukkan Program Studi Anda:"))
tb = float(input("Masukkan Tinggi Badan Anda (meter):"))
bb = int(input("Masukkan Berat Badan Anda:"))
print("")

# List
print("==========================================")
print("           BIODATA MAHASISWA              ")
print("==========================================")
biodata_mahasiswa = [nama, nim, prodi, tb, bb]
print("Nama             : ", biodata_mahasiswa[0])
print("NIM              : ", biodata_mahasiswa[1])
print("Program Studi    : ", biodata_mahasiswa[2])
print("Tinggi Badan     : ", biodata_mahasiswa[3], "m")
print("Berat Badan      : ", biodata_mahasiswa[4])
