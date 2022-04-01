#cek angka primer

import os

def clear_screen():
	if os.name == 'posix':  # MacOS atau Linux
		os.system('clear')
	else:
		os.system('cls')

clear_screen()
###################################################

num = int(input("Masukkan angka : "))

if num < 1 :
	print(num," Bukan angka primer")
else:
	for i in range(2, num):
		if num % i == 0:
			print(num, " Bukan angka primer")
			break
	else:
		print(num, " Adalah angka primer")
