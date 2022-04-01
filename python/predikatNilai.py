a = int(input('masukkan nilai : '))

nilai = [100,95,85,80,75,60,50,0]
abjad = ['A+','A','B+','B','C','D','E']
panjang = len(nilai)

if a < 0 or a > 100:
	print('Error')
else:
	for i in range(panjang):
		if a <= nilai[i] and a > nilai[i+1]:
			print(abjad[i])


## cara ke-2

a = int(input('masukkan nilai : '))
nilai = {'A+':95,'A':85,'B+':80,'B':75,'C':60,'D':50,'E':0}

if a < 0 or a > 100:
	print('Error')
else:
	for i in nilai:
		if a >= nilai[i]:
			print([i][0])	# [0] sebagai indexing, jika tanpa [0]
			break			# maka nilai [i] akan tercetak [' ']

