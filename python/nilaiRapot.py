import os

def screen():
	if os.name == 'posix':
		os.system('clear')
	else:
		os.system('cls')
screen()

#######################################################################################

def rapot(name):
	
	siswa = {
	"1" : {"nama":"Wildan","kelas":"12A","jurusan":"komputer","nilai":{"math":90, "indo":95, "ingg":72, "ppkn":78, "penj":86, "fisk":88, "kimi":84, "komp":98}},
	"2" : {"nama":"Dimas","kelas":"12B","jurusan":"mesin","nilai":{"math":60, "indo":65, "ingg":42, "ppkn":78, "penj":96, "fisk":68, "kimi":54, "komp":88}},
	"3" : {"nama":"Andi","kelas":"12C","jurusan":"arsitektur","nilai":{"math":70, "indo":85, "ingg":92, "ppkn":78, "penj":76, "fisk":88, "kimi":84, "komp":88}},
	"4" : {"nama":"Ali","kelas":"12D","jurusan":"kriya logam","nilai":{"math":80, "indo":95, "ingg":62, "ppkn":88, "penj":96, "fisk":78, "kimi":74, "komp":68}}
	}

	for no, item in siswa.items():		## mencetak array semua daftar produk
		#print(no, item["nama"] +"	>> nilai "+ str(item['nilai'].values())
	
		panjNilai = len(item['nilai'].values())
		rataRata = sum(item['nilai'].values()) / panjNilai

		if name == item['nama'].lower():
			##### membuat hasil print
			print('---------------------------------')
			print('\n')
			print('Nama            : ', item['nama'])
			print('Kelas           : ', item['kelas'])
			print('Jurusan         : ', item['jurusan'])
			print('Nilai rata-rata : ', int(rataRata))
	print('\n')
	return name

nama	= input('masukkan nama    : ')

rapot(nama)
