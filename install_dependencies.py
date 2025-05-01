import os

# spotdl --download-ffmpeg
# pip install -r dependencies.txt


os.system("python.exe -m pip install --upgrade pip") #update python
os.system("pip install -r dependencies.txt") # install libs from file
os.system("echo y|spotdl --download-ffmpeg") # download ffmpeg for spotdl (echo y to auto confirm overwriting existing version)

print("Installing dependencies finnisheddd")
