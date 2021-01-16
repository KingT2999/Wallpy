import sys
import os

if sys.argv[1] != "K":
	for proc in os.popen("tasklist").readlines():
		if proc.find("mpv.exe") != -1:
			os.system('taskkill /IM "mpv.exe" /F')

	os.system("wp id >id.txt")
	with open("id.txt", "r") as file:
		os.system(f"wp run mpv --wid={file.read()} {sys.argv[1]} --loop=inf --player-operation-mode=pseudo-gui --force-window=yes --no-audio")
else:
	os.system('taskkill /IM "mpv.exe" /F')