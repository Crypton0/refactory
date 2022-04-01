#reverse number

import os

def clear_screen():
	if os.name == 'posix':  # MacOS atau Linux
		os.system('clear')
	else:
		os.system('cls')

clear_screen()
###################################################

def revNum(num):
	rev = 0
	
	while num > 0:
		reminder = num % 10
		rev = (rev * 10) + reminder
		num = num // 10
	return rev

angka = int(input("Masukkan angka : "))

print(f"\nPembalikannya adalah {revNum(angka)}")
