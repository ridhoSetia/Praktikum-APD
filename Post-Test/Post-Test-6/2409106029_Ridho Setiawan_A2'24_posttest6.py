import os
from tabulate import tabulate

dataAkun = {
    1: {1:{"username": "admin","password": "1234#"}},
    0: {
        1:{"username": "ridho", "password": "029"},
    }
}

jenisEsteh = {
    "S": {"ukuran": "Small", "modal": 2000, "harga": 3000},
    "M": {"ukuran": "Medium", "modal": 3500, "harga": 5000},
    "J": {"ukuran": "Jumbo", "modal": 6000, "harga": 8000}
}

data_customers = {}

index_data_customers = (len(data_customers))

while True:
    print(
"""                                              
\033[34m
███████ ███████     ████████ ███████ ██   ██     ███    ███  █████  ███    ███  █████  ████████ 
██      ██             ██    ██      ██   ██     ████  ████ ██   ██ ████  ████ ██   ██    ██    
█████   ███████        ██    █████   ███████     ██ ████ ██ ███████ ██ ████ ██ ███████    ██    
██           ██        ██    ██      ██   ██     ██  ██  ██ ██   ██ ██  ██  ██ ██   ██    ██    
███████ ███████        ██    ███████ ██   ██     ██      ██ ██   ██ ██      ██ ██   ██    ██    
                                                                                                
 _                         _
|                           |
|   1. Register             |
|   2. Login                |
|   3. Keluar               |
|_                         _|
\033[37m""")
    inputMenuUtama = input("Pilih (1-3) : ")
    if inputMenuUtama == "1":
        os.system("cls || clear")
        print("""
\033[34m
██████  ███████  ██████  ██ ███████ ████████ ██████   █████  ███████ ██ 
██   ██ ██      ██       ██ ██         ██    ██   ██ ██   ██ ██      ██ 
██████  █████   ██   ███ ██ ███████    ██    ██████  ███████ ███████ ██ 
██   ██ ██      ██    ██ ██      ██    ██    ██   ██ ██   ██      ██ ██ 
██   ██ ███████  ██████  ██ ███████    ██    ██   ██ ██   ██ ███████ ██ 
                                                                                                      
\033[37m""")
        registUsername = input("Input username : ")
        registPassword = input("Input password : ")
        index_data_akun = (len(dataAkun[0])+1)

        dataAkun[0][index_data_akun] = {"username": registUsername, "password": registPassword}
        os.system("cls || clear")
        
        print("\nBerhasil register")

    elif inputMenuUtama == "2":
        os.system("cls || clear")
        while True:
            print("""
\033[34m
██       ██████   ██████  ██ ███    ██ 
██      ██    ██ ██       ██ ████   ██ 
██      ██    ██ ██   ███ ██ ██ ██  ██ 
██      ██    ██ ██    ██ ██ ██  ██ ██ 
███████  ██████   ██████  ██ ██   ████ 
                                                 
\033[37m""")
            inputUsername = input("Username anda : ")
            inputPassword = input("Password anda : ")
            
            login_sukses = False

            for cekRole, isiAkun in dataAkun.items():
                for cekAkun in isiAkun.values():
                    if inputUsername == cekAkun["username"] and inputPassword == cekAkun["password"]:
                        login_sukses = True
                        if cekRole == 1:
                            os.system("cls || clear")

                            print("\nLogin sebagai admin")
                            while True:
                                print("""
\033[34m
 _                            _
|        DATA COSTUMER         |
| ---------------------------- |
|    1. Tambah Customer        |
|    2. Tampilkan Customer     |
|    3. Ubah Customer          |
|    4. Hapus Customer         |
|    5. Logout                 |
|_                            _|
\033[37m""")
                                pilih = input("PILIH: ")
                                
                                if pilih == "1":
                                    os.system("cls || clear")
                                    print("====+ TAMBAH DATA +====\n")
                                    nama = input("Nama customer: ")
                                    while True:
                                        ukuranTeh = input("Ukuran Teh (S/M/J): ").upper()
                                        if ukuranTeh in ("S", "M", "J"):
                                            if ukuranTeh == "S":
                                                ukuranTeh = "Small"
                                            elif ukuranTeh == "M":
                                                ukuranTeh = "Medium"
                                            elif ukuranTeh == "J":
                                                ukuranTeh = "Jumbo"      
                                            break
                                        else:
                                            print("input salah! hanya bisa (S/M/J)")

                                    for teh in jenisEsteh.values():
                                        if ukuranTeh == teh["ukuran"]:
                                            hargaJual = teh["harga"]
                                            labaBersih = hargaJual - teh["modal"]

                                    index_data_customers += 1

                                    data_customers[index_data_customers] = {"nama": nama, "ukuran_teh": ukuranTeh, "harga_jual": hargaJual, "laba_bersih": labaBersih}

                                    os.system("cls || clear")

                                    print("| Berhasil menambah data customer! |")

                                elif pilih == "2":
                                    os.system("cls || clear")
                                    print("====+ DATABASE +====")

                                    totalS = 0
                                    totalM = 0
                                    totalJ = 0
                                    totalKeuntungan = 0
                                    
                                    table = []

                                    for i, data in enumerate(data_customers.values(), start=1):
                                        row = [i] + list(data.values())
                                        table.append(row)
                                        headers = ["No"] + list(data.keys())
                                            
                                        totalKeuntungan += data["laba_bersih"]
                                        
                                        if data["ukuran_teh"] == 'Small':
                                            totalS += 1
                                        elif data["ukuran_teh"] == 'Medium':
                                            totalM += 1
                                        elif data["ukuran_teh"] == 'Jumbo':
                                            totalJ += 1

                                    print("\nTabel Data Customer\033[34m")
                                    print(tabulate(table, headers, tablefmt="mixed_grid"), "\033[37m")

                                    totalPemesanan = 0
                                    totalPemesanan += len(data_customers)

                                    table = [["Small", "200ml", totalS],["Medium", "400ml", totalM],["Jumbo", "600ml", totalJ],["","",totalPemesanan]]
                                    headers = ["Ukuran", "Isi bersih", "total pesanan"]

                                    print("\nTabel Rincian Pesanan\033[34m")
                                    print(tabulate(table, headers, tablefmt="mixed_grid"),"\033[37m")

                                    print(f"\nTotal Keuntungan : Rp{totalKeuntungan}")

                                elif pilih == "3":
                                    os.system("cls || clear")
                                    print("====+ UPDATE +====\n")
                                        
                                    for i, data in enumerate(data_customers.values()):
                                        print(f"{i+1}. {data['nama']}")

                                    while True:
                                        try:
                                            pilihCustomer = int(input("\nPilih customer yang akan di-update datanya (1/2/3...): "))

                                            # Memeriksa apakah pilihan berada dalam range indeks yang valid
                                            if pilihCustomer in range(1, len(data_customers) + 1):
                                                # Mengambil data berdasarkan indeks
                                                dataTerpilih = list(data_customers.values())[pilihCustomer - 1]
                                                break 
                                            else:
                                                print("Data customer tidak ada")
                                        except ValueError:
                                            print("Wajib angka saja.")

                                    print(f"""
\033[34m
| Nama: {dataTerpilih["nama"]}
| Ukuran Teh: {dataTerpilih["ukuran_teh"]}
| Harga Jual: Rp{dataTerpilih["harga_jual"]}
| Keuntungan: Rp{dataTerpilih["laba_bersih"]}
\033[37m""")

                                    updateNama = input("\nUbah nama (tekan enter jika tidak ingin mengubah): ")
                                    while True:
                                        updateUkTeh = input("Ubah ukuran teh (S/M/J) (tekan enter jika tidak ingin mengubah): ").upper()
                                        if updateUkTeh in ("S", "M", "J"):
                                            if updateUkTeh == "S":
                                                updateUkTeh = "Small"
                                            elif updateUkTeh == "M":
                                                updateUkTeh = "Medium"
                                            elif updateUkTeh == "J":
                                                updateUkTeh = "Jumbo"      
                                            break
                                        elif updateUkTeh == "":
                                            break
                                        else:
                                            print("input salah! hanya bisa (S/M/J)")

                                    # Update data jika ada input baru
                                    update_by_index = list(data_customers.values())[pilihCustomer-1]
                                    print(update_by_index)
                                    if updateNama:
                                        update_by_index["nama"] = updateNama
                                    if updateUkTeh:
                                        update_by_index["ukuran_teh"] = updateUkTeh

                                    # Hitung ulang harga jual dan laba bersih berdasarkan ukuran teh baru
                                    ukuranTeh = update_by_index["ukuran_teh"]  # Ambil ukuran teh terbaru
                                    for teh in jenisEsteh.values():
                                        if ukuranTeh == teh["ukuran"]:
                                            update_by_index["harga_jual"] = teh["harga"]
                                            update_by_index["laba_bersih"] = teh["harga"] - teh["modal"]

                                    os.system("cls || clear")

                                    print(f"| Berhasil update data customer! |")  

                                elif pilih == "4":
                                    os.system("cls || clear")
                                    print("====+ DELETE +====")
                                        
                                    for i, data in enumerate(data_customers.values()):
                                        print(f"{i+1}. {data['nama']}")

                                    inputHapus = int(input("\nData customer yang ingin dihapus (1/2/3...) : "))
                                    hapus_by_index = list(data_customers)[inputHapus-1]
                                    del data_customers[hapus_by_index]
                                    
                                    os.system("cls || clear")

                                    print("Customer berhasil dihapus")
                                    
                                elif pilih == "5":
                                    os.system("cls || clear")
                                    print("Logout")
                                    break
                                
                                else:
                                    os.system("cls || clear")
                                    print("input salah! hanya bisa (1-5)")

                        elif cekRole == 0:
                            os.system("cls || clear")
                            print("\nLogin sebagai user")
                            while True:
                                print("""
\033[34m
 _                          _
|   PENJUALAN ES TEH MAMAT   |
| -------------------------- |
|    1. Variasi Es Teh       |
|    2. Jumlah Pesanan       |
|    3. Logout               |
|_                          _|
\033[37m""")
                                pilih = input("PILIH: ")

                                if pilih == "1":
                                    os.system("cls || clear")
                                    totalS = 0
                                    totalM = 0
                                    totalJ = 0
                                    totalKeuntungan = 0
                                    
                                    table = []

                                    for i, data in enumerate(data_customers.values(), start=1):
                                        row = [i] + list(data.values())
                                        table.append(row)
                                        headers = ["No"] + list(data.keys())
                                            
                                        totalKeuntungan += data["laba_bersih"]
                                        
                                        if data["ukuran_teh"] == 'Small':
                                            totalS += 1
                                        elif data["ukuran_teh"] == 'Medium':
                                            totalM += 1
                                        elif data["ukuran_teh"] == 'Jumbo':
                                            totalJ += 1

                                    print("\033[34m")
                                    print(tabulate(table, headers, tablefmt="mixed_grid"), "\033[37m")

                                elif pilih == "2":
                                    os.system("cls || clear")
                                    totalPemesanan = 0
                                    totalPemesanan += len(data_customers)

                                    print(f"\nTotal pesanan Es Teh Mamat : {totalPemesanan}")

                                elif pilih == "3":
                                    break

                                else:
                                    print("input salah! hanya bisa 1-3")

                if not login_sukses:
                    os.system("cls || clear")
                    print("Username atau password salah, silakan coba lagi!")

            if login_sukses:
                break

    elif inputMenuUtama == "3":
        os.system("cls || clear")
        print("Program Berhenti")
        break

    else:
        print("input salah! hanya bisa 1-3")