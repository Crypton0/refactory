#print angka primer

import os

def clear_screen():
	if os.name == 'posix':  # MacOS atau Linux
		os.system('clear')
	else:
		os.system('cls')

clear_screen()
###################################################

n = 8
a = 1

grouping	 = []
patternGroup = []

for i in range(n):
	a += i
	b = a
	
	for j in range(i+1, n+1):
		grouping.append(str(b))
		b = b * 2 + j

	n1		 = ' '.join(grouping)		# menggabung pola & mengubah ke string
	n2		 = ' '.join(grouping[::-1])	# menggabung pola & mengubah ke string reverse
	star	 = '* ' * (i + 1)
	pattern	 = n1 + ' ' + star + n2
	
	if star  == '* ': maxWidth = len(pattern)
	space	 = int((maxWidth - len(pattern)) / 2)
	pattern	 = n1 + ' ' * space + ' ' + star + ' ' * space + n2

	grouping = []
	print(pattern)					## pattern atas
	patternGroup.append(pattern)	## duplikat pattern

for k in patternGroup[::-1]: print(k)	## pattern bawah
