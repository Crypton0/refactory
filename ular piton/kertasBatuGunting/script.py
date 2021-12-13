# Pindahkan ke 3 function dibawah ke utils.py
## Sudah saya pindah ya bro ##
# import module utils  = modul buatan sedniri
# import module random = modul bawaan python untuk mengacak

import os
import utils
import random

def clear_screen():
	if os.name == 'posix':  ## MacOS atau Linux
		os.system('clear')
	else:
		os.system('cls')

clear_screen()

print(' -------------------------------------------------- ')
print('|      Memulai permainan Batu Kertas Gunting!      |')
print('|  Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)  |')
print(' -------------------------------------------------- \n')

player_name = input('Masukkan nama Anda: ')
while True:

	try:
		player_hand = int(input('Masukkan nomor (0-2): '))
		print('\n')
	except ValueError:
		print('\nSilahkan masukkan nomor...\n\n')
		continue

	if utils.validate(player_hand):

		# Tetapkan nomor acak antara 0 dan 2 ke computer_hand menggunakan randint
		computer_hand = random.randint(0,2)
		
		utils.print_hand(player_hand, player_name)
		utils.print_hand(computer_hand, 'Komputer')

		result = utils.cek(player_hand, computer_hand)
		print('-----------------------------------')
		print('Hasil : ' + result)
		break
	else:
		print('Mohon masukkan nomor dengan benar... \n\n')
		continue
