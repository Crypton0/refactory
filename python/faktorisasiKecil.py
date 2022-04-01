#faktorisasi kecil terdekat dari 2 angka

import os

def clear_screen():
	if os.name == 'posix':  # MacOS atau Linux
		os.system('clear')
	else:
		os.system('cls')

clear_screen()
###################################################

def hcf(num1, num2):
	if num1 < num2:
		smaller = num1
	else:
		smaller = num2

	for i in range(1, smaller + 1):
		if (num1 % i == 0) and (num2 % i == 0):
			factor = i
	return factor

angka1 = int(input('Angka 1 : '))
angka2 = int(input('Angka 2 : '))
print(f'\nFaktorisasi dari ({angka1} dan {angka2}) = {hcf(angka1, angka2)}')
