# INTERGER, angka bulat
a = 2
b = 5

# FLOAT, desimal
a = 0.50
b = 1.50

# Operasi
a = 10
b = 3
print(a + b)
print(a - b)
print(a / b)
print(a // b)
print(a * b)
print(a % b)

# STRING
namaDepan = "Ridho"
namaBelakang = "Setiawan"
print(namaDepan)
print(namaBelakang)
print(namaDepan, namaBelakang)
print(f"Nama depan {namaDepan}, nama belakang {namaBelakang}")

print ("""Selamat pagi
saya Ridho Setiawan""")

print("Halo"" Saya"" Ridho")
print("Halo"+" Ridho")

nama = "Ridho Setiawan"
print(nama[3])
print(nama[0:8])
print(nama[:-5])

# BOOLEAN
T = True
F = False

# AND
print(T * T) # 1
print(T * F) # 0
print(F * F) # 0

# LIST
makanan = ["bakso", "mie ayam", "sate", "nasi goreng", "ayam goreng", "pizza"]
# makanan[index dimulai: jumlah nilai yang diambil: ambil nilai dari kelipatan angka]
print(makanan[3])
print(makanan[0:3:2])
print(makanan[:2])
print(makanan[1:])

# TUPLE
tuple = ("ridho", 18, True, 1.0)
print(tuple[1])  
print(tuple[2])

# DICTIONARY
biodata = {
    "nama" : "Ridho",
    "kelas" : "A24",
    "prodi" : "Informatika"
}
print(biodata["nama"],biodata["kelas"],biodata["prodi"])

# TIPE DATA
a = 12
b = 0.01
c = "str"
d = True
print(type (a))
print(type (b))
print(type (c))
print(type (d))

# INPUT
nim = input("masukkan nim anda : ")
print("nim anda adalah",nim)
