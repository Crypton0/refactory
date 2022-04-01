
def solution(num):

	hasil = []

	for i in range(1,num):
		if (i % 3 == 0) or (i % 5 == 0):
			hasil.append(str(i))

	total = ' + '.join(hasil)
	print(f'{total} = {eval(total)}')


solution(10)
solution(20)
