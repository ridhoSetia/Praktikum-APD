inputNama = input("Masukkan nama kamu : ")
inputNIM = input("Masukkan NIM kamu : ")
hargaBeras = int(input("Masukkan harga beras : "))

diskonBerasMawar = int(hargaBeras - (0.11 * hargaBeras))
diskonBerasSani = int(hargaBeras - (0.14 * hargaBeras))
diskonBerasMaknyus = int(hargaBeras - (0.17 * hargaBeras))

print(f"{inputNama} dengan NIM {inputNIM} ingin membeli beras seharga Rp{hargaBeras}") 
print(f"Jika dia membeli beras Mawar ia harus membayar Rp{diskonBerasMawar} Setelah mendapat diskon 11%.")
print(f"Jika dia membeli beras Sani ia harus membayar Rp{diskonBerasSani} Setelah mendapat diskon 14%.")
print(f"Jika dia membeli beras Maknyus ia harus membayar Rp{diskonBerasMaknyus} Setelah mendapat diskon 17%.")