import os

# spotDL

class Spotdl:

	#### handle errorrsss:
	"""Processing query: Doechii - Denial is a river                                  
	FFmpegError: Failed to convert Doechii - DENIAL IS A RIVER, you can find error 
	here: C:\\Users\\nezas\\.spotdl\\errors\\ffmpeg_error_2025-03-24-11-47-23.txt"""


	#### succesfull download:
	"""Processing query: Doechii - Denial is a river                                  
Downloaded "Doechii - DENIAL IS A RIVER":                                      
https://music.youtube.com/watch?v=VlNktqr9cYk  """


	def __init__(self, title=None, artist=None, song_http=None, playlist_http=None):
		self.title = title
		self.artist = artist
		self.song_http = song_http
		self.playlist_http = playlist_http

	def download(self):
		os.chdir("Music")
		print("Prepering for downlaod.........")
		if self.title and self.artist:
			os.system(f'spotdl "{self.artist} - {self.title}"')
			print(f"finished downloading {self.title} - {self.artist}")


		elif self.title or self.song_http:
			os.system(f'spotdl "{self.title}"')
		# elif self.song_http:
		# 	os.system(f'spotdl "{self.song_http}"')

		elif self.playlist_http:
			os.system(f'spotdl "{self.playlist_http}"')

		else:
			return "Invalid data format/lacing data -> unable to download media"

		os.chdir("..") # move back to main folder (out of Music)
