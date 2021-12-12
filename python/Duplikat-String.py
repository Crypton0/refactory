## Untuk menduplikat

simpan = open("Duplikat.txt", "w")  # w = write, baris ini untuk membuat file bernama Duplikat.txt

print("\n")
print(" ================================================================= ")
print("|    Tool ini hanya untuk menduplikat string agar lebih banyak    |")
print("|  dan akan menyimpan file bernama Duplikat.txt di layar Desktop  |")
print(" ================================================================= ")
print("\n")

url = input("Masukkan string : ")
max = int(input("Berapa banyak : "))

count = 0
while (count < max):
    print(url)
    count = count + 1
    simpan.write(str(url) + '\n')

simpan.close()
