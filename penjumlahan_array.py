nilai = [3, 5, 2, -4, 8, 11]

data = len(nilai)  # hasil 6

for i in range(data):  # hasil dari 0-5
	#print(i)
	for j in range(i):
		jumlah = nilai[i] + nilai[j]
		
		if jumlah == 7:
			print(nilai[i], nilai[j])

