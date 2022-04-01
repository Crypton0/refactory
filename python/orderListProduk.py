def main():
	produk = {
		"1" : {"nama": "Nasi Putih", "harga": 4000, "id": "001"},
		"2" : {"nama": "Ayam Goreng", "harga": 7000, "id": "002"},
		"3" : {"nama": "Nasi Goreng", "harga": 15000, "id": "003"},
		"4" : {"nama": "Mie Goreng", "harga": 15000, "id": "004"},
		"5" : {"nama": "Bakso Goreng", "harga": 5000, "id": "005"},
		"6" : {"nama": "Sosis Goreng", "harga": 5000, "id": "006"}
	}
	
	pesanan = {}
	
	while True:
		print("\n")
		
		for no, item in produk.items():		## mencetak array semua daftar produk
			print(no, item["nama"] +"	>> harga "+ str(item["harga"]))
		
		try:
			pilihan = input ("\nSilahkan pilih nomor pesanan : ")
			data_item = produk[pilihan]
		
		except KeyError:
			print("\nMaaf pilihan tidak tersedia...\n")
			continue		## melanjutkan pesanan agar terus berjalan
		
		jumlah = int(input("Mau pesan berapa? : "))
		
		if pesanan.get(data_item["id"]) is None:		## memproses pesanan
			pesanan[data_item["id"]] = {
				"nama": data_item["nama"],
				"harga": data_item["harga"],
				"jumlah": jumlah
			}
		else:
			pesanan[data_item["id"]]["jumlah"]+= jumlah
		
		if input("Mau pesan yang lainnya? (Y/N) : ").strip().lower() == "y":
			continue
		else:
			break		## mengakhiri pesanan
	
	print("\n")
	total_bayar = 0
	
	for id_item, item in pesanan.items():		## mencetak hasil pesanan berdasarkan id
		print("Nama          : "+item["nama"])
		print("Harga         : "+str(item["harga"]))
		print("Jumlah        : "+str(item["jumlah"]))
		print("Total         : "+str(item["harga"]*item["jumlah"]))
		print("-------------------------------------")
		
		total_bayar += item["harga"]*item["jumlah"]		## menjumlahkan semua pesanan dari semua id
	
	print("Total bayar   : "+str(total_bayar)+"\n")

main()


