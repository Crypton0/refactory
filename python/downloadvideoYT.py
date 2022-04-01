print("\n")
print(" ============================================= ")
print("|  Tool untuk mendownload video dari youtube  |")
print("|      dengan kualitas resolusi maksimal      |")
print(" ============================================= ")
print("\n")

from pytube import YouTube

link = input("Masukkan URL Youtube : ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()

