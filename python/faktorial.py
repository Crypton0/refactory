
##################  Faktorial Biasa & Cetak Angka  ##################

## looping for i++ invers (pembalikan nilai array)
num = 5
hasil = []
for i in range(1,num+1):
	hasil.append(str(i))

total = ' * '.join(hasil[::-1])
print(f'hasil dari {num}! = ', total, '=', eval(total))

## looping while i--

num = 6
hasil = []
while num >= 1:
	hasil.append(str(num))
	num = num - 1

total = ' * '.join(hasil)
print(f'hasil dari {hasil[0]}! = ',total,'=',eval(total))


##################  Faktorial Biasa  ##################

def faktorial(nilai):
	if nilai <= 0:
		return 1

## looping for i++
	result = 1
	for i in range(1, nilai+1):
		result = result * i
	return result

## looping while i--
	result = 1
	while nilai >= 1:
		result = result * nilai 
		nilai = nilai - 1
	return result

print(faktorial(2))
print(faktorial(3))
print(faktorial(4))
print(faktorial(5))
print(faktorial(6))


##################  Faktorial Rekursif  ##################

def faktorialRekursif(nilai):
	if nilai <= 0:
		return 1
	else:
		return nilai * faktorialRekursif(nilai - 1)

print(faktorialRekursif(2))
print(faktorialRekursif(3))
print(faktorialRekursif(4))
print(faktorialRekursif(5))
print(faktorialRekursif(6))


##################  Faktorial Tail Rekursif  ##################

def faktorialTailRekursif(nilai, total=1):
	if nilai <= 0:
		return total
	else:
		return faktorialTailRekursif(nilai - 1, total * nilai)

print(faktorialTailRekursif(2))
print(faktorialTailRekursif(3))
print(faktorialTailRekursif(4))
print(faktorialTailRekursif(5))
print(faktorialTailRekursif(6))


