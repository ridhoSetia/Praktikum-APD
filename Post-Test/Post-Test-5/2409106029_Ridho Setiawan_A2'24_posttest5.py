dataAkun = [["admin", "1234#", 1],["ridho", "029", 0]]

data_customers = []

jenisEsteh = [["S", 2000, 3000],["M", 3500, 5000],["J", 6000, 8000]]

while True:
    print(
"""                                              
\033[34m
    ______       ______     __         __  ___                      __ 
   / ____/____  /_  __/__  / /_       /  |/  /___ _____ ___  ____ _/ /_
  / __/ / ___/   / / / _ \/ __ \     / /|_/ / __ `/ __ `__ \/ __ `/ __/
 / /___(__  )   / / /  __/ / / /    / /  / / /_/ / / / / / / /_/ / /_  
/_____/____/   /_/  \___/_/ /_/    /_/  /_/\__,_/_/ /_/ /_/\__,_/\__/  
                                              
--------------------------------
- 1. REGISTER                  -
- 2. LOGIN                     -
- 3. KELUAR                    -
--------------------------------
\033[37m""")
    inputMenuUtama = input("Pilih (1-3) : ")
    if inputMenuUtama == "1":
        print("""
\033[34m
    ____             _      __                  _ 
   / __ \___  ____ _(_)____/ /__________ ______(_)
  / /_/ / _ \/ __ `/ / ___/ __/ ___/ __ `/ ___/ / 
 / _, _/  __/ /_/ / (__  ) /_/ /  / /_/ (__  ) /  
/_/ |_|\___/\__, /_/____/\__/_/   \__,_/____/_/   
           /____/                               
\033[37m""")
        registUsername = input("Input username : ")
        registPassword = input("Input password : ")
        registRole = 0

        dataAkun.append([registUsername, registPassword, registRole])
        print("Berhasil register")

    elif inputMenuUtama == "2":
        while True:
            print("""
\033[34m
    __                _     
   / /   ____  ____ _(_)___ 
  / /   / __ \/ __ `/ / __ /
 / /___/ /_/ / /_/ / / / / /
/_____/\____/\__, /_/_/ /_/ 
            /____/          
\033[37m""")
            inputUsername = input("Username anda : ")
            inputPassword = input("Password anda : ")

            for cekAkun in range(len(dataAkun)):
                usernameInData, passwordInData, role = dataAkun[cekAkun]
                
                if inputUsername == usernameInData and inputPassword == passwordInData:
                    if role == 1:
                        print("\nLogin sebagai admin")
                        while True:
                            print("""
\033[34m
=== DATA COSTUMER ===
---------------------
1. TAMBAH CUSTOMER
2. TAMPILKAN CUSTOMER
3. UBAH CUSTOMER
4. HAPUS CUSTOMER
5. LOGOUT
=====================
\033[37m""")
                            pilih = input("PILIH: ")
                            
                            if pilih == "1":
                                print("== TAMBAH DATA ==")
                                nama = input("Nama customer: ")
                                while True:
                                    ukuranTeh = input("Ukuran Teh (S/M/J): ").upper()
                                    if ukuranTeh in ("S", "M", "J"):
                                        break
                                    else:
                                        print("input salah! hanya bisa (S/M/J)")
                                        pass

                                for teh in range(len(jenisEsteh)):
                                    ukuran, modal, harga = jenisEsteh[teh]
                                    if ukuranTeh == ukuran:
                                        hargaJual = harga
                                        laba_bersih = harga - modal

                                data_customers.append([nama, ukuranTeh, hargaJual, laba_bersih])

                                print(f"Menambah data customer {data_customers}")

                            elif pilih == "2":
                                print("== DATABASE ==")

                                totalS = 0
                                totalM = 0
                                totalJ = 0
                                totalKeuntungan = 0
                                
                                for data in range(len(data_customers)):
                                    nama, ukuranTeh, hargaJual, laba_bersih = data_customers[data]

                                    print(f"""\033[34m
_____________________________
| Customer ke-{data+1} 
| Nama: {nama}
| Ukuran Teh: {ukuranTeh}
| Harga Jual: Rp{hargaJual}
| Keuntungan: Rp{laba_bersih}
-----------------------------
\033[37m""")
                                    
                                    totalKeuntungan += laba_bersih
                                    
                                    if ukuranTeh == 'S':
                                        totalS += 1
                                    elif ukuranTeh == 'M':
                                        totalM += 1
                                    elif ukuranTeh == 'J':
                                        totalJ += 1

                                print(f"""\033[34m
Rincian pesanan Es Teh
    1. M (Small) : Isinya 200ml
    Total pesanan Es Teh Small : {totalS}
    2. L (Medium) : Isinya 400ml
    Total pesanan Es Teh Medium : {totalM}
    3. J (Jumbo) : Isinya 600ml
    Total pesanan Es Teh Jumbo : {totalJ}
\033[37m""")

                                totalPemesanan = 0
                                totalPemesanan += len(data_customers)

                                print(f"\nTotal pesanan es teh Mamat : {totalPemesanan}")

                                print(f"\nTotal Keuntungan : Rp{totalKeuntungan}")

                            elif pilih == "3":
                                    print("== UPDATE ==")
                                    
                                    for data in range(len(data_customers)):
                                        nama, ukuranTeh, hargaJual, laba_bersih = data_customers[data]
                                        print("")
                                        print(f"{data+1}. {nama}")

                                    pilihCustomer = int(input("Pilih customer yang akan di-update datanya (1/2/3...): ")) - 1
                                    
                                    nama, ukuranTeh, hargaJual, laba_bersih = data_customers[pilihCustomer]

                                    print(f"""
\033[34m
Nama: {nama}
Ukuran Teh: {ukuranTeh}
Harga Jual: Rp{hargaJual}
Keuntungan: Rp{laba_bersih}
\033[37m""")

                                    updateNama = input("\nUbah nama (tekan enter jika tidak ingin mengubah): ")
                                    updateUkTeh = input("Ubah ukuran teh (S/M/J) (tekan enter jika tidak ingin mengubah): ").upper()

                                    # Update data jika ada input baru
                                    if updateNama:
                                        data_customers[pilihCustomer][0] = updateNama
                                    if updateUkTeh:
                                        data_customers[pilihCustomer][1] = updateUkTeh

                                    # Hitung ulang harga jual dan laba bersih berdasarkan ukuran teh baru
                                    ukuranTeh = data_customers[pilihCustomer][1]  # Ambil ukuran teh terbaru
                                    for teh in range(len(jenisEsteh)):
                                        ukuran, modal, harga = jenisEsteh[teh]
                                        if ukuranTeh == ukuran:
                                            data_customers[pilihCustomer][2] = harga
                                            data_customers[pilihCustomer][3] = harga - modal

                                    print(f"Data customer setelah update: {data_customers[pilihCustomer]}")          

                            elif pilih == "4":
                                print("== DELETE ==")
                                    
                                for data in range(len(data_customers)):
                                    nama, ukuranTeh, hargaJual, laba_bersih = data_customers[data]
                                    print(f"{data+1}. {nama}")

                                inputHapus = int(input("\nData customer yang ingin dihapus (1/2/3...) : ")) - 1
                                del data_customers[inputHapus]

                                print("Customer berhasil dihapus")
                                
                            elif pilih == "5":
                                print("Logout")
                                break
                            
                            else:
                                print("input salah! hanya bisa (1-5)")
                                pass

                    elif role == 0:
                        print("\nLogin sebagai user")
                        while True:
                            print("""
\033[34m
==+ PENJUALAN ES TEH MAMAT +==
------------------------------
    1. VARIASI ES TEH
    2. JUMLAH PESANAN
    3. LOGOUT
==============================
\033[37m""")
                            pilih = input("PILIH: ")

                            if pilih == "1":
                                totalS = 0
                                totalM = 0
                                totalJ = 0

                                for data in range(len(data_customers)):
                                    nama, ukuranTeh, hargaJual, laba_bersih = data_customers[data]

                                    if ukuranTeh == 'S':
                                        totalS += 1
                                    elif ukuranTeh == 'M':
                                        totalM += 1
                                    elif ukuranTeh == 'J':
                                        totalJ += 1

                                print(f"""
\033[34m
Rincian pesanan Es Teh
                                      
    1. M (Small)  : Rp3000 (200ml)
    Total pesanan Es Teh Small  : {totalS} 
    2. L (Medium) : Rp5000 (400ml)
    Total pesanan Es Teh Medium : {totalM} 
    3. J (Jumbo) : Rp8000 (600ml)
    
    Total pesanan Es Teh Jumbo  : {totalJ} 
\033[37m""")

                            elif pilih == "2":
                                totalPemesanan = 0
                                totalPemesanan += len(data_customers)
                                print(f"\nTotal pesanan Es Teh Mamat : {totalPemesanan}")

                            elif pilih == "3":
                                break

                            else:
                                print("input salah! hanya bisa 1-3")

            if inputUsername != usernameInData and inputPassword != passwordInData:
                print("username atau password salah!")

            break
    elif inputMenuUtama == "3":
        print("Program Berhenti")
        break

    else:
        print("input salah! hanya bisa 1-3")
        pass
