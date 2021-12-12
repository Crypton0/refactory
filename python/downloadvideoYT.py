print("\n")
print(" ============================================= ")
print("|  Tool untuk mendownload video dari youtube  |")
print("|      dengan kualitas resolusi maksimal      |")
print(" ============================================= ")
print("\n")

from pytube import YouTube

#link = input("Masukkan URL Youtube : ")
#video = YouTube(link)
#stream = video.streams.get_highest_resolution()
#stream.download()

link = input ("Masukkan URL Youtube: ")
yt = YouTube (link)
video = yt.streams.filter(file_extension='mp4').order_by('resolution').desc()
try:
    video.first().download()
    print("Download berhasil : ", yt.title)
except Exception as e:
    print("Download gagal : ", e)
