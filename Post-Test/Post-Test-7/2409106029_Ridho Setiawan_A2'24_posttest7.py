import os
from tabulate import tabulate
import time
from tqdm import tqdm
import random

# Warna
BOLD = '\033[1m'
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' 
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m' 


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

# clear terminal
def clear():
    os.system("cls || clear")

# fake loading
def loading(loadingLength, delay):
    for i in tqdm(range(loadingLength)):
        time.sleep(delay)

# fake loading (2)
random = random.randint(1, 2)
def wait(index):
    clear()
    print("Loading", end='')
    for i in range(3):
        print(".", end='', flush=True)
        time.sleep(0.2)

    if index < random:
        wait(index+1)

# validasi input bertipe string
def validasi_input_huruf(charInput):
    for char in charInput:
        if not (char.isalpha()):
            return False
    return True

# validasi input bertipe number
def validasi_input_angka(numInput):
    return numInput.isdigit()

# menahan dan melanjutkan program
def lanjut():
    print("Tekan enter untuk lanjut...")
    input()
    clear()

# mengubah nama ukuran teh
def nama_ukuran_teh(ukuran):
    if ukuran in ("S", "M", "J"):
        if ukuran == "S":
            ukuran = "Small"
        elif ukuran == "M":
            ukuran = "Medium"
        elif ukuran == "J":
            ukuran = "Jumbo"
    return ukuran

# tambah data customer
def tambahCustomer():
    clear()
    print("====+ TAMBAH DATA +====\n")
    
    index_data_customers = (len(data_customers))
    
    while True:
        try:
            nama = input("Nama customer: ").strip()
            if not nama:
                raise ValueError("Nama customer tidak boleh kosong!")
            if not validasi_input_huruf(nama):
                raise ValueError("Nama customer hanya bisa berisi huruf!")
            
            ukuranTeh = input("Ukuran Teh (S/M/J): ").upper().strip()
            if not ukuranTeh:
                raise ValueError("Ukuran teh tidak boleh kosong!")
            if not validasi_input_huruf(ukuranTeh):
                raise ValueError("Ukuran teh hanya bisa berisi huruf!")
            if ukuranTeh not in ("S", "M", "J"):
                raise ValueError("Hanya bisa (S/M/J)")
            
            ukuranTeh = nama_ukuran_teh(ukuranTeh)

            for teh in jenisEsteh.values():
                if ukuranTeh == teh["ukuran"]:
                    hargaJual = teh["harga"]
                    labaBersih = hargaJual - teh["modal"]

            index_data_customers += 1

            data_customers[index_data_customers] = {"nama": nama, "ukuran_teh": ukuranTeh, "harga_jual": hargaJual, "laba_bersih": labaBersih}

            delay = 0.1
            if index_data_customers > 15:
                delay = 0.07
            elif index_data_customers > 30:
                delay = 0.05
            elif index_data_customers > 45:
                delay = 0.03
            elif index_data_customers > 60:
                delay = 0.01

            loading(index_data_customers, delay)
            
            print(GREEN+BOLD+"\nBerhasil menambah data customer!"+RESET)
            lanjut()
            break

        except ValueError as error:
            print(f"{RED}{BOLD}Input tidak valid: {error} Silakan coba lagi.\n{RESET}")
    
# tabel rincian pesanan
def rincianPesanan():
    totalS = 0
    totalM = 0
    totalJ = 0

    for data in data_customers.values():
        if data["ukuran_teh"] == 'Small':
            totalS += 1
        elif data["ukuran_teh"] == 'Medium':
            totalM += 1
        elif data["ukuran_teh"] == 'Jumbo':
            totalJ += 1
    
    totalPemesanan = 0
    totalPemesanan += len(data_customers)

    table = [["Small", "200ml", totalS],["Medium", "400ml", totalM],["Jumbo", "600ml", totalJ],["Total", "", totalPemesanan]]
    headers = ["Ukuran", "Isi bersih", "total pesanan"]
    
    print(BOLD+"\nTabel Rincian Pesanan"+RESET+BLUE)
    print(tabulate(table, headers, tablefmt="grid")+RESET)
    
# tampilkan data customer
def tampilkanCustomer():
    clear()
    print("==== DATA CUSTOMER ====")
    
    if not data_customers:
        print(RED+BOLD+"\nBelum ada Customer"+RESET)
        time.sleep(1)
    else:
        totalKeuntungan = 0
        
        table = []
    
        for i, data in enumerate(data_customers.values(), start=1):
            row = [i] + list(data.values())
            table.append(row)
            headers = ["No"] + list(data.keys())
                
            totalKeuntungan += data["laba_bersih"]

        # Menampilkan tabel data customer
        print(BOLD+"\nTabel Data Customer"+RESET+BLUE)
        print(tabulate(table, headers, tablefmt="grid")+RESET)

        # Menampilkan rincian pesanan
        rincianPesanan()

        # Menampilkan total keuntungan
        print(f"{BOLD}\nTotal Keuntungan : Rp{totalKeuntungan}\n{RESET}")
        lanjut()

    
# update data customer
def updateCustomer():
    clear()
    print("==== UPDATE ====")
    if not data_customers:
        print(RED+BOLD+"\nBelum ada Customer"+RESET)
        time.sleep(1)
    else:
        print()
        for i, data in enumerate(data_customers.values()):
            print(f"{BLUE}{BOLD}{i+1}. {data['nama']}{RESET}")

        while True:
            try:
                pilihCustomer = (input("\nPilih customer yang akan di-update datanya (1/2/3...): ")).strip()
                
                if not pilihCustomer:
                    raise ValueError("Tidak boleh kosong!")
                if not validasi_input_angka(pilihCustomer):
                    raise ValueError("Hanya bisa angka!")
                
                pilihCustomer = int(pilihCustomer)

                if pilihCustomer not in range(1, len(data_customers) + 1):
                    raise ValueError("Data customer tidak ditemukan")
                
                # Mengambil data berdasarkan indeks
                dataTerpilih = list(data_customers.values())[pilihCustomer - 1]
                break 
            
            except ValueError as error:
               print(f"{RED}{BOLD}Input tidak valid: {error} Silakan coba lagi.{RESET}")

        print(f'''{BLUE}{BOLD}
    | Nama: {dataTerpilih["nama"]}
    | Ukuran Teh: {dataTerpilih["ukuran_teh"]}
    | Harga Jual: Rp{dataTerpilih["harga_jual"]}
    | Keuntungan: Rp{dataTerpilih["laba_bersih"]}
        {RESET}''')

        while True:
            try:
                updateNama = input("\nUbah nama (tekan enter jika tidak ingin mengubah): ").strip()
                if not validasi_input_huruf(updateNama):
                    raise ValueError("Nama customer hanya bisa berisi huruf!")
                
                updateUkTeh = input("Ubah ukuran teh (S/M/J) (tekan enter jika tidak ingin mengubah): ").upper().strip()
                if not validasi_input_huruf(updateUkTeh):
                    raise ValueError("Ukuran teh hanya bisa berisi huruf!")
                if updateUkTeh and updateUkTeh not in ("S", "M", "J"):
                    raise ValueError("Hanya bisa (S/M/J)")

                updateUkTeh = nama_ukuran_teh(updateUkTeh)

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

                loading(10, 0.1)
                print()
                print(GREEN+BOLD+"\nBerhasil update data customer!"+RESET)
                lanjut()     
                break

            except ValueError as error:
                print(f"{RED}{BOLD}Input tidak valid: {error} Silakan coba lagi.\n{RESET}")
    
# hapu data customer
def hapusCustomer():
    clear()
    print("==== DELETE ====")
    if not data_customers:
        print(RED+BOLD+"\nBelum ada Customer"+RESET)
        time.sleep(1)
    else:
        print()
        for i, data in enumerate(data_customers.values()):
            print(f"{RED}{BOLD}{i+1}. {data['nama']}{RESET}")

        while True:
            try:
                inputHapus = (input("\nData customer yang ingin dihapus (1/2/3...) : ")).strip()
                if not inputHapus:
                    raise ValueError("Tidak boleh kosong!")
                if not validasi_input_angka(inputHapus):
                    raise ValueError("Hanya bisa angka!")

                inputHapus = int(inputHapus)

                hapus_by_index = list(data_customers)[inputHapus-1]
                del data_customers[hapus_by_index]
                
                loading(10, 0.1)
                print()
                print(GREEN+BOLD+"Customer berhasil dihapus"+RESET)
                lanjut()
                break
            
            except ValueError as error:
                print(f"{RED}{BOLD}Input tidak valid: {error} Silakan coba lagi.\n{RESET}")
    
# menu untuk admin
def menuAdmin():
    wait(0)
    print(RED+BOLD+"\nLogin sebagai admin 👑"+RESET)
    time.sleep(1.5)
    clear()
    while True:
        print(BOLD+BLUE+'''
 KELOLA COSTUMER         

 > 1. Tambah Customer
 > 2. Tampilkan Customer
 > 3. Ubah Customer
 > 4. Hapus Customer
 > 0. Logout

'''+RESET)
        pilih = input("Pilih (0-4): ")

        if pilih == "1":
            clear()
            tambahCustomer()
        elif pilih == "2":
            clear()
            tampilkanCustomer()
        elif pilih == "3":
            clear()
            updateCustomer()
        elif pilih == "4":
            clear()
            hapusCustomer()
        elif pilih == "0":
            clear()
            print("Logout")
            time.sleep(1)
            menuUtama()
        else:
            clear()
            print(RED+BOLD+"input tidak valid!\n"+RESET)
    
# menu untuk user
def menuUser():
    wait(0)
    print(RED+BOLD+"\nLogin sebagai user 👤"+RESET)
    time.sleep(1.5)
    clear()
    while True:
        print(BLUE+BOLD+'''
 PENJUALAN ES TEH MAMAT   

 > 1. Variasi Es Teh
 > 0. Logout

'''+RESET)
        pilih = input("Pilih (0-1): ")

        if pilih == "1":
            clear()
            rincianPesanan()
            print()
            lanjut()
        elif pilih == "0":
            clear()
            print("Logout")
            time.sleep(1)
            menuUtama()
        else:
            print(RED+BOLD+"input tidak valid!\n"+RESET)
        
# registrasi akun user
def registrasi():
    clear()
    print(BLUE+
'''
██████  ███████  ██████  ██ ███████ ████████ ██████   █████  ███████ ██ 
██   ██ ██      ██       ██ ██         ██    ██   ██ ██   ██ ██      ██ 
██████  █████   ██   ███ ██ ███████    ██    ██████  ███████ ███████ ██ 
██   ██ ██      ██    ██ ██      ██    ██    ██   ██ ██   ██      ██ ██ 
██   ██ ███████  ██████  ██ ███████    ██    ██   ██ ██   ██ ███████ ██ 
                                                                                                      
'''+RESET)
    while True:
        try:
            registUsername = input("Input username : ").strip()
            if not registUsername:
                raise ValueError("Username tidak boleh kosong")
            
            registPassword = input("Input password : ").strip()
            if not registPassword:
                raise ValueError("Password tidak boleh kosong")
            
            index_data_akun = (len(dataAkun[0])+1)

            dataAkun[0][index_data_akun] = {"username": registUsername, "password": registPassword}
            
            loading(10, 0.1)
            print(GREEN+BOLD+"\nBerhasil melakukan registrasi"+RESET)
            lanjut()
            break

        except ValueError as error:
            print(f"{RED}{BOLD}Input tidak valid: {error} Silakan coba lagi.\n{RESET}")
    
# login
def login():
    clear()
    print(BLUE+BOLD+'''
██       ██████   ██████  ██ ███    ██ 
██      ██    ██ ██       ██ ████   ██ 
██      ██    ██ ██   ███ ██ ██ ██  ██ 
██      ██    ██ ██    ██ ██ ██  ██ ██ 
███████  ██████   ██████  ██ ██   ████ 
                                                 
'''+RESET)
    while True:
        try:
            inputUsername = input("Username anda : ").strip()
            if not inputUsername:
                raise ValueError("Username tidak boleh kosong")
            
            inputPassword = input("Password anda : ").strip()
            if not inputPassword:
                raise ValueError("Password tidak boleh kosong")
        
            login_sukses = False

            # Memeriksa setiap akun
            for cekRole, isiAkun in dataAkun.items():
                for cekAkun in isiAkun.values():
                    if inputUsername == cekAkun["username"] and inputPassword == cekAkun["password"]:
                        login_sukses = True
                        if cekRole == 1:
                            menuAdmin()
                        elif cekRole == 0:
                            menuUser()
                        break  # Keluar dari loop ketika akun ditemukan dan login berhasil
                if login_sukses:
                    break  # Keluar dari loop level atas jika login berhasil
            
            if not login_sukses:
                raise ValueError("Username atau password salah, silakan coba lagi!")

            break  # Keluar dari loop utama jika login sukses

        except ValueError as error:
            print(f"{RED}{BOLD}Input tidak valid: {error} Silakan coba lagi.\n{RESET}")


# menu utama es teh mamat
def menuUtama():
    clear()
    print(BOLD+BLUE+
'''                                              
███████ ███████     ████████ ███████ ██   ██     ███    ███  █████  ███    ███  █████  ████████ 
██      ██             ██    ██      ██   ██     ████  ████ ██   ██ ████  ████ ██   ██    ██    
█████   ███████        ██    █████   ███████     ██ ████ ██ ███████ ██ ████ ██ ███████    ██    
██           ██        ██    ██      ██   ██     ██  ██  ██ ██   ██ ██  ██  ██ ██   ██    ██    
███████ ███████        ██    ███████ ██   ██     ██      ██ ██   ██ ██      ██ ██   ██    ██    
                                                                                                

> 1. Register
> 2. Login
> 0. Keluar

'''+RESET)
    while True:
        inputMenuUtama = input("Pilih (0-2) : ")

        if inputMenuUtama == "1":
            registrasi()
            menuUtama()
        elif inputMenuUtama == "2":
            login()
        elif inputMenuUtama == "0":
            print("Program Berhenti")
            exit(0)
        else:
            print(RED+BOLD+"input tidak valid!\n"+RESET)

menuUtama()