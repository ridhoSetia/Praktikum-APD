adminName = "admin"
adminPassword = "1234#"

dataUser = [["ridho", "029"]]

data_customers = []
uang_modal = [2000, 3500, 6000]
daftar_harga = [3000, 5000, 8000]

while True:
    print(
"""
== Pengelolaan Laba Bersih Es Teh Mamat ==
--------------------
1. REGISTER
2. LOGIN
3. KELUAR
--------------------
====================
""")
    inputMenuPertama = input("Pilih (1-3) : ")
    if inputMenuPertama == "1":
        print("\n ===+ Registrasi +===")
        registUsername = input("Input username : ")
        registPassword = input("Input password : ")
        dataUser.append([registUsername, registPassword])
        print("Berhasil register")

    elif inputMenuPertama == "2":
        while True:
            inputUsername = input("Username anda : ")
            inputPassword = input("Password anda : ")

            for cek in range(len(dataUser)):
                usernameInData, passwordInData = dataUser[cek]
                if inputUsername == adminName and inputPassword == adminPassword:
                    print("\nLogin sebagai admin")
                    while True:
                        print("""
=== DATA COSTUMER ===
---------------------
1. TAMBAH DATA
2. TAMPILKAN DATA
3. UBAH DATA
4. HAPUS DATA
5. KEMBALI
=====================""")
                        pilih = input("\nPILIH: ")
                        
                        if pilih == "1":
                            print("== TAMBAH DATA ==")
                            nama = input("Nama customer: ")
                            while True:
                                ukuranTeh = input("Ukuran Teh (M/L/J): ").upper()
                                if ukuranTeh in ("M", "L", "J"):
                                    break
                                else:
                                    print("input salah! hanya bisa (M/L/J)")
                                    pass

                            if ukuranTeh == 'M':
                                hargaJual = daftar_harga[0]
                                laba_bersih = daftar_harga[0] - uang_modal[0]
                            elif ukuranTeh == 'L':
                                hargaJual = daftar_harga[1]
                                laba_bersih = daftar_harga[1] - uang_modal[1]
                            elif ukuranTeh == 'J':
                                hargaJual = daftar_harga[2]
                                laba_bersih = daftar_harga[2] - uang_modal[2]

                            data_customers.append([nama, ukuranTeh, hargaJual, laba_bersih])

                            print(f"Menambah data customer {data_customers}")

                        elif pilih == "2":
                            print("== DATABASE ==")

                            totalM = 0
                            totalL = 0
                            totalJ = 0
                            totalKeuntungan = 0
                            
                            for data in range(len(data_customers)):
                                print(f"\nCustomer ke-{data+1}")

                                nama, ukuranTeh, hargaJual, laba_bersih = data_customers[data]

                                print(f"Nama: {nama}")
                                print(f"Ukuran Teh: {ukuranTeh}")
                                print(f"Harga Jual: Rp{hargaJual}")
                                print(f"Keuntungan: Rp{laba_bersih}")

                                totalKeuntungan += laba_bersih
                                
                                if ukuranTeh == 'M':
                                    totalM += 1
                                elif ukuranTeh == 'L':
                                    totalL += 1
                                elif ukuranTeh == 'J':
                                    totalJ += 1

                            print(f"""
Rincian pesanan Es Teh
1. M (Mini) : Isinya 200ml
    Total pesanan Es Teh Mini : {totalM} 
2. L (Large) : Isinya 400ml
    Total pesanan Es Teh Large : {totalL} 
3. J (Jumbo) : Isinya 600ml
    Total pesanan Es Teh Jumbo : {totalJ} 
                            """)

                            totalPemesanan = 0
                            totalPemesanan += len(data_customers)
                            print(f"Total pesanan es teh Mamat : {totalPemesanan}")

                            print(f"Total Keuntungan : Rp{totalKeuntungan}")

                        elif pilih == "3":
                                print("== UPDATE ==")
                                
                                # Tampilkan daftar customer
                                for data in range(len(data_customers)):
                                    nama, ukuranTeh, hargaJual, laba_bersih = data_customers[data]
                                    print(f"{data+1}. {nama}")

                                pilihCustomer = int(input("Pilih customer yang akan di-update datanya (1/2/3...): ")) - 1
                                
                                nama, ukuranTeh, hargaJual, laba_bersih = data_customers[pilihCustomer]

                                print(f"""
Nama: {nama}
Ukuran Teh: {ukuranTeh}
Harga Jual: Rp{hargaJual}
Keuntungan: Rp{laba_bersih} """)

                                updateNama = input("\nUbah nama (tekan enter jika tidak ingin mengubah): ")
                                updateUkTeh = input("Ubah ukuran teh (M/L/J) (tekan enter jika tidak ingin mengubah): ").upper()

                                # Update data jika ada input baru
                                if updateNama:
                                    data_customers[pilihCustomer][0] = updateNama
                                if updateUkTeh:
                                    data_customers[pilihCustomer][1] = updateUkTeh

                                # Hitung ulang harga jual dan laba bersih berdasarkan ukuran teh baru
                                ukuranTeh = data_customers[pilihCustomer][1]  # Ambil ukuran teh terbaru
                                if ukuranTeh == 'M':
                                    data_customers[pilihCustomer][2] = daftar_harga[0]
                                    data_customers[pilihCustomer][3] = daftar_harga[0] - uang_modal[0]
                                elif ukuranTeh == 'L':
                                    data_customers[pilihCustomer][2] = daftar_harga[1]
                                    data_customers[pilihCustomer][3] = daftar_harga[1] - uang_modal[1]
                                elif ukuranTeh == 'J':
                                    data_customers[pilihCustomer][2] = daftar_harga[2]
                                    data_customers[pilihCustomer][3] = daftar_harga[2] - uang_modal[2]

                                print(f"Data customer setelah update: {data_customers[pilihCustomer]}")          

                        elif pilih == "4":
                            print("== DELETE ==")
                                
                            for data in range(len(data_customers)):
                                nama, ukuranTeh, hargaJual, laba_bersih = data_customers[data]
                                print(f"{data+1}. {nama}")

                            inputHapus = int(input("\nData customer yang ingin dihapus (1/2/3...) : ")) - 1
                            del data_customers[inputHapus]
                            
                        elif pilih == 5:
                            break
                        
                        else:
                            pass

                elif inputUsername == usernameInData and inputPassword == passwordInData:
                    print("\nLogin sebagai user")
                    while True:
                        print("""
==+ PENJUALAN ES TEH MAMAT +==
------------------------------
1. ES TEH TERLARIS
2. JUMLAH PESANAN
3. KEMBALI
==============================""")
                        pilih = input("\nPILIH: ")

                        if pilih == "1":
                            totalM = 0
                            totalL = 0
                            totalJ = 0

                            for data in range(len(data_customers)):
                                nama, ukuranTeh, hargaJual, laba_bersih = data_customers[data]

                                if ukuranTeh == 'M':
                                    totalM += 1
                                elif ukuranTeh == 'L':
                                    totalL += 1
                                elif ukuranTeh == 'J':
                                    totalJ += 1

                            print(f"""
Rincian pesanan Es Teh
1. M (Mini)  : Isinya 200ml
    Total pesanan Es Teh Mini  : {totalM} 
2. L (Large) : Isinya 400ml
    Total pesanan Es Teh Large : {totalL} 
3. J (Jumbo) : Isinya 600ml
    Total pesanan Es Teh Jumbo : {totalJ} 
                            """)

                        elif pilih == "2":
                            totalPemesanan = 0
                            totalPemesanan += len(data_customers)
                            print(f"\nTotal pesanan es teh Mamat : {totalPemesanan}")

                        elif pilih == "3":
                            break

                elif (inputUsername == usernameInData and inputPassword == passwordInData) or (inputUsername == adminName and inputPassword == adminPassword):
                    print("username atau password salah!")
            break
    elif inputMenuPertama == "3":
        print("Program Berhenti")
        break