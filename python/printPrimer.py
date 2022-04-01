#print angka primer

import os

def clear_screen():
	if os.name == 'posix':  # MacOS atau Linux
		os.system('clear')
	else:
		os.system('cls')

clear_screen()
###################################################

lower = 100
upper = 200

for num in range(lower, upper + 1):
	if num > 1:
		for i in range(2, num):
			if num % i == 0:
				break
		else:
			print(num)
