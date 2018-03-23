import vlc
import time
import eyed3

#mp3_file_path = 'C:\\chimes.mp3'
#mp3_file_path = 'D:\\Kamiku\\Music\\Blind-Test\\Dan In Real Life (Coup de foudre à Rhode Island) - 2007 - Sondre Lerche & Regina Spektor - Hell No.mp3'
mp3_file_path = "C:\\08 - Eric Burdon - House Of The Rising Sun.mp3"

fichier = "file:///" + mp3_file_path.replace("\\\\", "/").replace("\\", "/")
print(fichier)

audiofile = eyed3.load(mp3_file_path)
p = vlc.MediaPlayer(fichier)
p.play()

print("length = ", p.get_length())
print("volume =", p.audio_get_volume())

rangemin = 0
rangemax = 100
rangestep = 3

for i in range(rangemin, rangemax, rangestep):
    vol = int(i / rangemax * 100)
    p.audio_set_volume(vol)
    print("i =", i, "vol =", vol)
    time.sleep(0.05)

for i in range(rangemax, (rangemax * 2)):
    print("i =", i, "vol =", vol)
    time.sleep(0.05)

audiofile.tag.artist = u"Eric Burdon"
audiofile.tag.album = u"Casino"
audiofile.tag.title = u"House Of The Rising Sun"
audiofile.tag.save()

#pygame
"""
from pygame import mixer # Load the required library


mixer.init()
mixer.music.load(mp3_file_path)
mixer.music.play()
"""