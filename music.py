import os
import converter

# [ {artist:xxx, title:xxx, path:xxx}, {artist:yyy, title:yyy, path:yyy}, ...]

# files = os.listdir(".\\Music")
# print(files)

songs = []
		
def update_song_dict():
	global songs

	# print("################")
	# dir_path = os.path.dirname(os.path.realpath(__file__))
	# print("DIRPATH:", dir_path)

	# cwd = os.getcwd()
	# print("PWD:", cwd)
	# print("################")

	#os.chdir("Music")
	files = os.listdir("Music")

	for f in files:
		try:																	# -4 to remove ".mp3		
			if {"artist" : f.split(" - ")[0], "title" : f.split(" - ")[1][:-4], "path" : f"Music\\{f}"} not in songs:
				songs.append({"artist" : f.split(" - ")[0], "title" : f.split(" - ")[1][:-4], "path" : f"Music\\{f}"})
		except IndexError: # if file isnt named "artist - title"
			if {"artist" : None, "title" : f, "path" : f"Music\\{f}"} not in songs:
				songs.append({"artist" : None, "title" : f, "path" : f"Music\\{f}"})



# def song_dict():
# 	return songs

# print(song_dict())
# x = [{'artist': 'Destroy Boys', 'title': 'Secrets.mp3', 'path': 'Music\\Destroy Boys - Secrets.mp3'}, 
# {'artist': 'Kendrick Lamar', 'title': 'Not Like Us.mp3', 'path': 'Music\\Kendrick Lamar - Not Like Us.mp3'}, 
# {'artist': 'MARINA', 'title': 'Primadonna.mp3', 'path': 'Music\\MARINA - Primadonna.mp3'}, 
# {'artist': None, 'title': 'TamaraDRA_SLO_MMC.PR1.20250204.2.2105_14910612.mp3', 'path': 'Music\\TamaraDRA_SLO_MMC.PR1.20250204.2.2105_14910612.mp3'}, 
# {'artist': 'Wolf Alice', 'title': 'Don’t Delete The Kisses.mp3', 'path': 'Music\\Wolf Alice - Don’t Delete The Kisses.mp3'}]

# s1 = ("Destroy Boys", "Secrets.mp3")
# s2 = ("Destroy Boys", "Primadonna.mp3")


# check if a file already exists in the dict
def song_exists(title, artist):
	for i in songs:
		try:
			if i["artist"].lower() == artist.lower() and i["title"].lower() == title.lower():
				return True
		except AttributeError:
			if i["title"].lower() == title.lower():
				return True
	return False

def find_song_dict(title, artist): # returns the dict of a song
	update_song_dict()
	print("after updated song dict", songs)
	for i in songs:
		if i["title"].lower() == title.lower() and i["artist"].lower() == artist.lower():
			return i
	else:
		return f"[find_song_dict] Song not found in songs list: title={title}, artist={artist}"

def get_path(title, artist):

	#print("in get_path, fnd song dict:[path]:", find_song_dict(title, artist))#["path"])
	return find_song_dict(title, artist)["path"]

def convert_ogg():
	#check if any song isnt ogg file yet and convert it
	for i in songs:
		#print(i["path"][-3:])
		if i["path"][-3:] == "mp3":
			converter.ogg(i["path"])



update_song_dict()
convert_ogg()
print(songs)