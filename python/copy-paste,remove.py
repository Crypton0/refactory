import os
import random
import shutil

a = 6
b = 0
for i in range(a):
	b += i

#print(b)
c = random.randint(1, b)
#print(c)
file = 'C:/Users/Lenopo/Desktop/wew.txt'
if c == 8:
	if os.path.exists(file):
		os.remove(file)
	else:
		pass
else:
	shutil.copy('C:/Users/Lenopo/Desktop/2.txt','C:/Users/Lenopo/Desktop/wew.txt')
	print(c)
