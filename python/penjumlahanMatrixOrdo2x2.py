print('\n')
print('Penjumlahan matrix ordo 2x2')
print('\n')

mat1 = [[5,0],
		[2,6]]

mat2 = [[3,5],
		[4,9]]

hasil = []
for i in range(0, len(mat1)):
	for j in range(0, len(mat1[0])):
		print(mat1[i][j] + mat2[i][j], end=' ')
	print('')


###################
print('\n')
print('Penjumlahan matrix ordo 2x2, 3x3, 4x4, dll')
print('\n')

mat1 = [[5,0], [2,6], [5,9]]
mat2 = [[3,5], [4,9], [-2,-5]]

bungkus = zip(mat1, mat2)
hasil = []
for item in bungkus:
	x = zip(*item)
	jumlah = map(lambda y: sum(y), x)
	hasil.append(list(jumlah))

print(hasil)


###################
print('\n')
print('Penjumlahan matrix ordo 2x2, 3x3, 4x4, dll. Modues Numpy')
print('\n')

import numpy as np

mat1 = np.array([[5,0], [2,6], [5,9]])
mat2 = np.array([[3,5], [4,9], [-2,-5]])

s = np.add(mat1, mat2)
print(s)


