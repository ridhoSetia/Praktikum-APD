# # percabangan
# cuaca = "mendung"

# if(cuaca == "cerah"):
#     print("kamu pergi keluar rumah")
# else:
#     print("hari ini mendung")

# umur = int(input("masukkan umur : "))

# # nested if
# if umur > 0:
#     if umur <= 10:
#         print("umur terkategori anak-anak")
#     elif umur <= 18:
#         print("umur terkategori anak-anak")
#     elif umur <= 36:
#         print("umur terkategori anak-anak")
#     else:
#         print("umur terkategori anak-anak")
# else:
#     print("umur harus bilangan positif")

# # Ternary Operator
# angka = int(input("input angka : "))
# hasil = "genap" if angka%2 == 0 else "ganjil"
# print(f"{angka} adalah bilangan {hasil}")

# # Match case
# print("""
# === KALKULATOR ===
# 1. +
# 2. -
# 3. *
# 4. /
# """)
# fitur = int(input("pilih operasi : "))
# match fitur:
#     case 1:
#         a = int(input("masukkan angka pertama: "))
#         b = int(input("masukkan angka pertama: "))
#         c = a + b 
#         print(f"Hasil penjumlahan {a} + {b} = {c}")
#     case 2:
#         a = int(input("masukkan angka pertama: "))
#         b = int(input("masukkan angka pertama: "))
#         c = a - b 
#         print(f"Hasil penjumlahan {a} - {b} = {c}")
#     case 3:
#         a = int(input("masukkan angka pertama: "))
#         b = int(input("masukkan angka pertama: "))
#         c = a * b 
#         print(f"Hasil penjumlahan {a} * {b} = {c}")
#     case 4:
#         a = int(input("masukkan angka pertama: "))
#         b = int(input("masukkan angka pertama: "))
#         c = a / b 
#         print(f"Hasil penjumlahan {a} / {b} = {c}")
#     case _:
#         print("pilih antara 1 - 4")



# inputBeliBuku = int(input("Jumlah buku yang dibeli : "))
# inputTotalPembelian = int(input("Total pembelian : "))

# if(inputBeliBuku == 5 and inputTotalPembelian > 100000):
#     harga = inputTotalPembelian - (0.20*inputTotalPembelian)
# else:
#     harga = inputTotalPembelian

# print(harga)

# inputJenisKelamin = input("input jenis kelamin (L/P) : ")
# hasil = "laki-laki" if inputJenisKelamin == "L" else "perempuan" if inputJenisKelamin == "P" else "jenis kelamin tidak diketahui"
# print(hasil)

inputNilai = int(input("input nilai : "))
if inputNilai > 100:
    print("tidak memenuhi kondisi")
elif inputNilai >= 80:
    if inputNilai >= 90 and inputNilai <= 100:
        print("nilai A+")
    elif inputNilai >= 80 and inputNilai <= 89:
        print("nilai A-")
elif inputNilai >= 70:
    if inputNilai >= 75 and inputNilai <= 79:
        print("nilai B+")
    elif inputNilai >= 70 and inputNilai <= 74:
        print("nilai B-")
else:
    print("nilai dibawah 70 = C!!!")