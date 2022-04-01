#cek palindrome

import os

def clear_screen():
	if os.name == 'posix':  # MacOS atau Linux
		os.system('clear')
	else:
		os.system('cls')

clear_screen()
###################################################

array = ['radar','Malam','kasur ini rusak','Ibu Ratna antar ubi','Malas', 'Makan nasi goreng','Balonku ada lima'];

kata = input("Masukkan kata : ")
print("\n")

def palindrome(string):
	for i in range(0, int(len(string) / 2)):
		if string[i] == string[len(string) - i - 1]:
			print(kata," = Palindrome\n")
		else:
			print(kata," = Bukan palindrome\n")

palindrome(kata)
