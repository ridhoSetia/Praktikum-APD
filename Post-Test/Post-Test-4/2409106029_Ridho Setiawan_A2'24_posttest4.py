username = "ridho"
password = "29"
salahInput = 0

while salahInput < 3:
    print("====+ Login +====")
    inputUsername = input("Username : ").lower()
    inputPassword = input("Password : ")

    if inputUsername == username and inputPassword == password:
        print(f"Berhasil login, selamat datang {username}")
        while True:
            # proses input
            inputNama = input("Masukkan nama peminjam : ")
            inputNIM = input("Masukkan NIM peminjam : ")
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
                # mengubah validInput menjadi False karena nilai inputLamaCicilan SalahInput
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

            while True:
                inputLanjut = input("Lanjut? (y/t): ").lower()
                if inputLanjut in ('y', 't'):
                    break
            if inputLanjut == 'y':
                pass
            else:
                break
    else:
        print("Username atau password salah")
        salahInput += 1
        if salahInput >= 3:
            print("Maaf, anda terlalu banyak melakukan percobaan login!")
            break