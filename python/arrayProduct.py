
def productArray(arr): 

	n = len(arr)

	if(n == 1):
		print([0])
		return

	# membuat variable array dengan panjang sama seperti array utama dan bernilai 0
	left  = [0]*n 
	right = [0]*n 
	prod  = [0]*n 		# sebagi penampung nilai Left[] dan right[]

	# Nilai Left (angka awal) dan Right (angka terakhir) akan selalu bernilai 1
	left[0]		 = 1 
	right[n-1]	 = 1
#	print(' '*20,left)
#	print(' '*20,right) 

	for i in range(1, n): 
		left[i] = arr[i - 1] * left[i - 1] 
#		print(' '*20,left[i]) 
 
	for j in range(n-2, -1, -1): 		# looping descending, sama seperti j--
		right[j] = arr[j + 1] * right[j + 1] 
#		print('='*20,right[j]) 

	for k in range(n): 
#		print('L'*20,left[k]) 
#		print('R'*20,right[k]) 
		prod[k] = left[k] * right[k] 
#		print(' '*20,prod[k]) 
 
	print(prod)


## Eksekusi 

productArray([12])				# => [0]
productArray([12,20])			# => [20,12]
productArray([3,27,4,2])		# => [216,24,162,324]
productArray([13,10,5,2,9])		# => [900,1170,2340,5850,1300]
productArray([16,17,4,3,5,2])	# => [2040,1920,8160,10880,6528,16320]

