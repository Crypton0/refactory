print('\n\n segitiga full angka \n')

batas = 8
for i in range(1, batas+1):
	for j in range(1, i+1):
		print(j, end='')
	print('\n')

#######
awal = 1
kelipatan = 6
print(f'\n\n mencetak kelipatan {kelipatan}\n')

while awal < 100+1:
	if awal % kelipatan == 0:
		print(awal, end=' ')
	awal += 1

######
batas = 100
potong = 12
print(f'\n\n mencetak angka dan memotong kelipatan {potong}\n')

for i in range(1, batas+1):
	if i % potong == 0:
		print(i, '\n')
	else:
		print(i, end=' ')

######
print('\n\n segitiga siku-siku tengah kosong\n')

for i in range(0, 10+1):
	for j in range(1, i+1):
		if j == i:
			print(j, end=' ')
		elif i == 10 and j < 11:
			print(j, end=' ')
		elif i < 11 and j == 1:
			print(j, end=' ')
		else:
			print(' ', end=' ')
	print('\n')

######
print('\n\n kotak tengah kosong\n')

for i in range(1, 10+1):
	for j in range(1, 10+1):
		if (i <= 10 and j == 1) or (i == 1 and j <= 10):
			print('*', end=' ')
		elif (i == 10 and j <= 10) or (i <= 10 and j == 10):
			print('*', end=' ')
		elif (i == 5 and j == 5) or (i == 6 and j == 6): # tengah
			print('*', end=' ')
		elif (i == 5 and j == 6) or (i == 6 and j == 5): # tengah
			print('*', end=' ')
		else:
			print(' ', end=' ')
	print(' ')

######
print('\n\n kotak tengah bentuk jendela\n')

size = 20
sizer = size + 1

for i in range(1, sizer):
	for j in range(1, sizer):
		if (i == 1) and (j >= 1) or (j == 1) and (i >= 1):
			print('*', end=' ')
		elif (i == size) and (j >= 1) or (j == size) and (i >= 1):
			print('*', end=' ')
		elif (i == size/2) and (j >= 1) or (j == size/2) and (i >= 1):
			print('*', end=' ')
		else:
			print(' ', end=' ')
	print(' ')

######
print('\n\n segitiga siku-siku tengah kosong\n')

for i in range(1,3+1):
	print('Perulangan luar [i] = ', i)

	for j in range(5):
		print('   Perulangan dalam [i, j] = ', str(i) + ', ' + str(j))

######
print('\n\n mencetak data aktif\n')

listKota = ['Jakarta', 'Surabaya', 'Makassar']
for kota in listKota:
	print(kota)

	listTempat = ['Taman', 'Lapangan', 'Mall']
	while listTempat:		# mengeksekusi listTempat
		print('-->', listTempat.pop(0))		# 0 adalah indexdari array

######
print('\n\n persegi potong diagonal (2 segitiga siku-siku) while\n')

max_baris = 8	# bisa dijadikan 1 variable
max_kolom = 8	# tapi ini sebagai pembeda antara baris dan kolom

baris = 0
while baris < max_baris:
	kolom = 0
	while kolom < max_kolom:
		if kolom <= baris:
			print('o', end=' ')
		else:
			print('x', end=' ')
		kolom += 1
	else:
		print('')
	baris += 1

######
print('\n\n spersegi potong diagonal (2 segitiga siku-siku) for\n')

max_baris = 8	# bisa dijadikan 1 variable
max_kolom = 8	# tapi ini sebagai pembeda antara baris dan kolom

for i in range(0,max_baris):
	for j in range(0,max_kolom):
		if j <= i:
			print('k', end=' ')
		else:
			print('s', end=' ')
	print('\n', end='')

######
print('\n\n mengubah huruf\n')

import re

listKota = ['Solo', 'Surabaya', 'Bekasi', 'Jakarta']
listHurufVokal = ['a', 'i', 'u', 'e', 'o']
for kota in listKota:
	print('[' + kota + ']')

	for vokal in listHurufVokal:
		print('-->', re.sub('[aiueo]', vokal, kota))	# huruf yang akan diubah ke data array

######
print('\n\n \n')



######
print('\n\n \n')



######
print('\n\n \n')



######
print('\n\n \n')





