## program jalan terus tapi bagus buat background

a = 0
while a < 10:
	b = 0
	while b < 10:
		print(b, end=' ')
		b -= 1
	print('\n', end='')
	a += 1

## kode ke-2 untuk 1 digit angka

a = 1
while a < 10+1:
	b = 1
	while b < a+1:
		print(b, end=' ')
		b += 1
		if b == 7:
			print(b, end=' ')
			b -= a
	print('\n', end='')
	a += 1

