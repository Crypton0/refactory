#print angka primer

import os

def clear_screen():
	if os.name == 'posix':  # MacOS atau Linux
		os.system('clear')
	else:
		os.system('cls')

clear_screen()
###################################################

bil = int(input("Masukkan angka faktorial : "))

total = 0

for i in range(1, bil+1):

	total += i
	
	if i == bil:
		print(f'{i} = {total}')
		break
	print(f'{i} + ', end='')

###################################################

print('\n')

num = []
for x in range(1, bil+1):
	num.append(str(x))

print(" + ".join(num)+" = %s " % eval(" + ".join(num)))
