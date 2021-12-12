print("\n")
print(" =========================================================== ")
print("|     Tool ini berfungsi hanya sebagai kalkulator saham     |")
print("|  Silahkan anda belajar lagi sebelum menggunakan tool ini  |")
print(" =========================================================== ")
print("\n")

equity			 = int(input("Equity          : "))
net_profit		 = int(input("Net Profit      : "))
total_liability	 = int(input("Total Liability : "))
listed_share	 = int(input("Listed Share    : "))
harga_saham		 = int(input("Harga Saham     : "))

# Equity = Assets - Liability (sudah di dapat dalam laporan perusahaan)
ROE	  = (net_profit / equity)*100
DER	  = (total_liability / equity)
BV	  = (equity / listed_share)
PBV	  = (harga_saham / BV)
EPS	  = (net_profit / listed_share)
PER	  = (harga_saham / EPS)

print("\n")
print(" ========= ")
print("|  Jawab  |")
print(" ========= ")
print("\n")

print("ROE = ", ROE,"% keuntungan")
print("DER = ", DER,"x utang yang menunggak")
print("BV  = ", BV ,"  --> harga rata-rata saham")
print("PBV = ", PBV,"x lipat lebih mahal dari harga aslinya")
print("EPS = ", EPS,"  --> penghasilan per saham")
print("PER = ", PER,"x lipat rupiah kita membayar ke perusahaan")

