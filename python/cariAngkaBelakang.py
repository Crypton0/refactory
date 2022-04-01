#cariAngkaBelakang

import os

def clear_screen():
	if os.name == 'posix':  # MacOS atau Linux
		os.system('clear')
	else:
		os.system('cls')

clear_screen()
###################################################

arr = [256, 265, 397, 438, 273, 365, 385, 295, 237, 786]
arri = []

for i in range(0, len(arr)):
	operasi = str(arr[i])[-1]

	if operasi == '5' or operasi == '7':
		arri.append(arr[i])

print(arri)
