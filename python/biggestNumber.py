
def maxRedigit(num):
	if len(str(num)) == 3:

		angka = []
		for i in str(num):
			angka.append(i)

		n = len(angka)
		for i in range(n - 1):
			for j in range(n - i - 1):
				if angka[j] < angka[j + 1]:
					temp = angka[j]
					angka[j] = angka[j+1]
					angka[j+1] = temp

		bilangan = ''
		for i in angka:
			bilangan = bilangan + i
		return bilangan
	else:
		return 'null'



print(maxRedigit(123))
print(maxRedigit(231))
print(maxRedigit(321))
print(maxRedigit(684))
print(maxRedigit(879))
print('\n')
print(maxRedigit(-1)) 
print(maxRedigit(0))
print(maxRedigit(99))
print(maxRedigit(1000))
