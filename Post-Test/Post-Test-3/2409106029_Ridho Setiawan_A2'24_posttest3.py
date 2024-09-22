print("""
+============================================================================+
|  ____                                                                      |
| |  _ \ _ __ ___   __ _ _ __ __ _ _ __ ___                                  |
| | |_) | '__/ _ \ / _` | '__/ _` | '_ ` _ \                                 |
| |  __/| | | (_) | (_| | | | (_| | | | | | |                                |
| |_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_|                                |
|  __  __          |___/        _         _                                  |
| |  \/  | ___ _ __   ___ _ __ | |_ _   _| | ____ _ _ __                     |
| | |\/| |/ _ \ '_ \ / _ \ '_ \| __| | | | |/ / _` | '_ \                    |
| | |  | |  __/ | | |  __/ | | | |_| |_| |   < (_| | | | |                   |
| |_|  |_|\___|_| |_|\___|_| |_|\__|\__,_|_|\_\__,_|_| |_|                   |
|   ____ _      _ _               ____             ____        _             |
|  / ___(_) ___(_) | __ _ _ __   |  _ \ ___ _ __  | __ ) _   _| | __ _ _ __  |
| | |   | |/ __| | |/ _` | '_ \  | |_) / _ \ '__| |  _ \| | | | |/ _` | '_ \ |
| | |___| | (__| | | (_| | | | | |  __/  __/ |    | |_) | |_| | | (_| | | | ||
|  \____|_|\___|_|_|\__,_|_| |_| |_|   \___|_|    |____/ \__,_|_|\__,_|_| |_||
|                                                                            |
+============================================================================+
""")

# proses input
inputNama = input("Masukkan Nama : ")
inputNIM = input("Masukkan NIM : ")
jumlahPinjaman = int(input("Masukkan total pinjaman : "))

print("""
Pilih lama cicilan : 
1 tahun dengan bunga 7%
2 tahun dengan bunga 13%
3 tahun dengan bunga 19%
""")

inputLamaCicilan = int(input("Lama Cicilan dalam tahun(1-3) : "))

# digunakan untuk memvalidasi apakah inputLamaCicilan
# memiliki nilai input yang Benar yaitu angka 1-3
validInput = True

if inputLamaCicilan == 1:
    bunga = 0.07
    jumlahBulan = 12
elif inputLamaCicilan == 2:
    bunga = 0.13
    jumlahBulan = 24
elif inputLamaCicilan == 3:
    bunga = 0.19
    jumlahBulan = 36
else:
    # mengubah validInput menjadi False karena nilai inputLamaCicilan Salah
    validInput = False
        
# output
if validInput == True:
    bungaPerBulan = (bunga/12)*jumlahPinjaman
    cicilanPerbulan = (jumlahPinjaman+bungaPerBulan)/jumlahBulan
    print(f"""
====+ Rincian Pinjaman +====
Nama Peminjam     : {inputNama}
NIM Peminjam      : {inputNIM}
Lama cicilan      : {inputLamaCicilan} tahun
Cicilan per bulan : Rp {cicilanPerbulan:,.2f}
=============================
    """.replace(",", "."))
else:
    print("\nMaaf, hanya bisa memilih lama cicilan 1-3 tahun")