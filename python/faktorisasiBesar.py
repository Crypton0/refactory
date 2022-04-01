#faktorisasi besar terdekat dari 2 angka

import os

def clear_screen():
	if os.name == 'posix':  # MacOS atau Linux
		os.system('clear')
	else:
		os.system('cls')

clear_screen()
###################################################

def lcm(num1, num2):
	if num1 < num2:
		greater = num2
	else:
		greater = num1

	while True:
		if (greater % num1 == 0) and (greater % num2 == 0):
			break
		greater += 1
	return greater

angka1 = int(input('Angka 1 : '))
angka2 = int(input('Angka 2 : '))

print(f'\nFaktorisasi dari ({angka1} dan {angka2}) = {lcm(angka1, angka2)}')
