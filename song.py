import spotDL
import converter

import music

import metadata

class Song:

	def __init__(self, title, artist=None):
		self.title = title
		self.artist = artist
		#self.path = self.get_path()

		self.song_dict = music.find_song_dict(self.title, self.title)
		
	# returns the song lyrics
	def get_lyrics(self):
		return metadata.Metadata(music.get_path(self.title, self.artist)).lyrics()

	# downlaods the song mp3
	def download_song(self):

		# check if songs exists -> dont download
		#if self.title in music.songs and self.artist in music.songs: ############# NE DELA #################

		# for i in x:
		# 	if fi["artist"] == s2[0] and i["title"] == s2[1]:

		# checks if song dosent exist yes and downloads it if it dosent
		if music.song_exists(self.title, self.artist):
			print(f"Skipping download: {self.artist} - {self.title} File already exists")
		else:
			#calls the getmusic fucn and downlaod via spotdl lib to /Music dir
			spotDL.Spotdl(title=self.title, artist=self.artist).download()
			music.update_song_dict()
			# after download convert to ogg (mp3 not gut for pygame mixer music)
			converter.ogg(music.get_path(self.title, self.artist))

	## func moved to music.py
	# def get_path(self):
	# 	#find path to mp3 (by title and artist) 
	# 	return music.find_song_dict(title=self.title, artist=self.artist)["path"]
