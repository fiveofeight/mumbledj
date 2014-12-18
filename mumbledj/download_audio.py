#---------------------#
#      MumbleDJ       #
# By Matthieu Grieger #
#---------------------#--------------------------------------------------#
# download_audio.py                                                      #
# Downloads audio (ogg format) from specified YouTube ID. If no ogg file #
# exists, it creates an empty file called .video_fail that tells the Lua #
# side of the program that the download failed. .video_fail will get     #
# deleted on the next successful download.                               #
#------------------------------------------------------------------------#

import pafy
import sys
from sys import argv
from os.path import isfile
from os import remove, system
from time import sleep

url = argv[1]
video = pafy.new(url)

try:
	video.m4astreams[0].download(filepath = 'song.m4a', quiet = True)
	if isfile('.video_fail'):
		remove('.video_fail')
except:
	with open('.video_fail', 'w+') as f:
		f.close()
		
while isfile('song.m4a.temp'):
	sleep(1)

if isfile('song.m4a'):
	system('ffmpeg -i song.m4a -acodec libvorbis -ar 48000 -ac 1 -loglevel quiet song-converted.ogg -y')
else:
	with open('.video_fail', 'w+') as f:
		f.close()

if not isfile('.video_fail'):
	while not isfile('song-converted.ogg'):
		sleep(1)

if isfile('song.m4a'):
	remove('song.m4a')

