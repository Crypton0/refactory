nilai = [3, 5, 2, -4, 8, 11]

count = len(nilai)		## hasil 6
hasil = []

for i in range(count):	## hasil 0-5
	for j in range(i, count):	## hasil 0-5 1-5 2-5 3-5 4-5 5
		if nilai[i]+nilai[j] == 7:
			hasil.append([nilai[i], nilai[j]])
			## print(nilai[i], nilai[j]) -> ketika tidak di append
print(hasil)


