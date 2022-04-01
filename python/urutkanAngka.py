#mengurutkan angka

import os

def clear_screen():
	if os.name == 'posix':  # MacOS atau Linux
		os.system('clear')
	else:
		os.system('cls')

clear_screen()
###################################################

arr = [8, 9, 6, 5, 0, 0, 2, 1, 1, 3, 4, 5, 7, 7, 7, 7, 8]

def Pengurutan(angka):
	n = len(angka)
	
	for i in range(n - 1):
		for j in range(n - 1 - i):
			if angka[j] > angka[j + 1]:
				temp = angka[j]
				angka[j] = angka[j+1]
				angka[j+1] = temp
	return angka

print(Pengurutan(arr))
