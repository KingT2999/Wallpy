import eel
import os

@eel.expose
def video_files():
	os.chdir("web/video/")

	files = os.listdir()

	os.chdir("../../")

	return files

@eel.expose
def set_as_wallpaper(file_name):
	for proc in os.popen("tasklist").readlines():
		if proc.find("mpv.exe") != -1:
			os.system('taskkill /IM "mpv.exe" /F')

	os.system("wp id >id.txt")
	with open("id.txt", "r") as file:
		os.system(f"wp run mpv --wid={file.read()} web/video/{file_name} --loop=inf --player-operation-mode=pseudo-gui --force-window=yes --no-audio")

@eel.expose
def remove_wallpaper():
	os.system('taskkill /IM "mpv.exe" /F')


eel.init("web")

eel.start("index.html")