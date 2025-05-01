import ffmpeg
import os

# path = "Music\\Destroy Boys - Secrets.mp3"

# out = "convertedd.ogg"

# ffmpeg.input(path).output(out).run()


def delete(path):
	if os.path.exists(path):
  		os.remove(path)
	else:
  		print(f"Could not delete {path} cuz file does not exist") 

def ogg(path):
	print("IN OGG pathhh:", path)
	output = path[:-3] + "ogg"
	print(output)
	ffmpeg.input(path).output(output).run()
	delete(path)

