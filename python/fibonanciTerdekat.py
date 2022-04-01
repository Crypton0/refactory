def fibonanci(num):
	if num == 0:
		return 0

	bilangan1 = 0
	bilangan2 = 1
	bilangan3 = bilangan1 + bilangan2

	while bilangan3 <= num:
		bilangan1 = bilangan2
		bilangan2 = bilangan3
		bilangan3 = bilangan1 + bilangan2

	if abs(bilangan3 - num) <= abs(bilangan2 - num):
		return bilangan2
	else:
		return bilangan3

print(fibonanci(11))
print(fibonanci(20))
print(fibonanci(26))
print(fibonanci(28))
print(fibonanci(35))


