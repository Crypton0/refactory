arr = ['*','#','$','%','@','$','*','#','$','%','@','$'];
arrLen = len(arr)

for i in range(0, arrLen-1):
	for j in range(0, i):
		print(arr[i] + arr[j], end='')
	print('')


