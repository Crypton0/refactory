batas = 8

for i in range(0,batas):
	for j in range(0,batas):
		if (i+j) % 2 <= 0:
			print(' ', end='')
		else:
			print('#', end='')
	print('\n', end='')

print('\n ilustrasi penempatan angka\n')

batas = 8

for i in range(0,batas):
	for j in range(0,batas):
		if (i+j) % 2 <= 0:
			print('#', end=' ')
		else:
			print(i+j, end=' ')
	print('\n', end='')
