# input nama lengkap
inputNama = input("Masukkan nama kamu : ")
# input NIM
inputNIM = input("Masukkan NIM kamu : ")
# input harga beras (400000) dan mengubah nilai harga beras menjadi integer
hargaBeras = int(input("Masukkan harga beras : "))

# melakukan perhitungan pada masing-masing jenis beras, lalu mengubah nilainya menjadi integer

# 0.11 = diskon beras mawar yaitu 11%
hargaBerasMawar = int(hargaBeras - (0.11 * hargaBeras))
# 0.14 = diskon beras mawar yaitu 14%
hargaBerasSani = int(hargaBeras - (0.14 * hargaBeras))
# 0.17 = diskon beras mawar yaitu 17%
diskonBerasMaknyus = int(hargaBeras - (0.17 * hargaBeras))

# menampilkan output
print(f"{inputNama} dengan NIM {inputNIM} ingin membeli beras seharga Rp{hargaBeras}") 
print(f"Jika dia membeli beras Mawar ia harus membayar Rp{hargaBerasMawar} Setelah mendapat diskon 11%.")
print(f"Jika dia membeli beras Sani ia harus membayar Rp{hargaBerasSani} Setelah mendapat diskon 14%.")
print(f"Jika dia membeli beras Maknyus ia harus membayar Rp{diskonBerasMaknyus} Setelah mendapat diskon 17%.")