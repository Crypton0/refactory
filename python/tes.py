## Palondrim

print("\n")
angka = [7,6,1,1,6,5,5,7,5]

angka.sort()  # increment
angka[1] = angka[8]
angka[8] = angka[0]
angka[3] = angka[6]
angka[6] = angka[2]
print(angka)

print("\n")
print("========================================================")
print("\n")

input = int(input("Masukkan jumlah kolom/baris : "));  # masih gagal
for i in range (0, input+1):
    for pola in range (i):
        if pola == 0:
            print("*", end="")
        elif pola % 2:  # jika tanda % diganti == maka hasilnya akan seperti contoh,
            print("#", end="")
        elif pola % 3:  # tetapi hanya bisa print 3 simbol pertama
            print("%", end="")
        elif pola % 4:
            print("*", end="")


    print()
