 # #import mutagen.id3.ID3 # mp3 tags
# import mutagen
# from mutagen.id3 import ID3, USLT, ID3NoHeaderError

# # # def encodeTextFrame(text):
# # # 	return mutagen.id3.TextFrame(encoding=3, text=[text])

# song2 = "Music\\Kendrick Lamar - Not Like Us.mp3" ### type : <class 'mutagen.mp3.MP3'>
# 											#### type tags : <class 'mutagen.id3.ID3'>

"""
<Header for 'Unsynchronised lyrics/text transcription', ID: "USLT">
     Text encoding        $xx
     Language             $xx xx xx
     Content descriptor   <text string according to encoding> $00 (00)
     Lyrics/text          <full text string according to encoding>
"""



# song2 = "Music\\TamaraDRA_SLO_MMC.PR1.20250204.2.2105_14910612.mp3"

# lyrics
# 'USLT::XXX': USLT(encoding=<Encoding.UTF16: 1>, lang='XXX', desc='', text="insert lyrics"

# s1 = "Music\\MARINA - Primadonna.mp3"
# ss = ID3(s1)
# # print(ss.pprint())
# # print(ss)
# print(ss["USLT::XXX"])


# s = mutagen.File(song2)
# try:
# 	a = ID3(song2)
# except ID3NoHeaderError:
# 	a = ID3()

# org = a["USLT::XXX"]
# print(a.pprint())
# print(a["USLT::XXX"])
#a["USLT::XXX"] = USLT(encoding=3, lang='XXX', desc='', text="LRYSADYYYSSS\n[intor]\nLyricsss\naslkdjfčlasjčdf\n[end]")
# a["USLT::XXX"] = USLT(encoding=3, lang='XXX', desc='', text=None)
# print(a["USLT::XXX"])

# a = ID3(song2)
# # print(type(a))
# # print(a.tags.pprint())
# print("------------------------------------------------------------------------------------------")
# a["TXXX:LYRICS"] = "tesstttt lyricsss" #mutagen.id3.TextFrame(encoding=3, text=["testtttttt 12346567890"])
# print(a.tags.pprint())



#################################################
import lyricsgenius # genius api lib
import mutagen
# from mutagen.id3 import ID3, USLT, ID3NoHeaderError

class Metadata:
	def __init__(self, audio_path):
		self.audio_path = audio_path
		print(self.audio_path)
		# try:
		# 	self.song = ID3(self.audio_path)
		# except ID3NoHeaderError: # if files metadata isnt ID3
		# 	self.song = ID3()
		self.song = mutagen.File(audio_path)

		GENIUS_ACCESS_TOKEN = "xlLSXmgcSQdbv7JQ9bPob7wUtx7RmenXPQd7YDdHqeLsOzHrh0GVbzb-5MJvsajU"
		self.genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)

	def api_lyrics(self):
		# returns the song lyrics from genius api
		song = self.genius.search_song(self.song_title, self.artist)
		return song.lyrics

	def lyrics(self):
		# try:
		# 	return self.song["USLT::XXX"]
		# except KeyError: # if lyric tag dosent exist manualy make the tag and search for lyric
		# 	self.song["USLT::XXX"] = USLT(encoding=3, lang='XXX', desc='', text=api_lyrics())
		# 	self.song.save()
		# 	return self.song["USLT::XXX"]
		# print(self.song["lyrics-xxx"][0])
		return self.song["lyrics-xxx"][0]

	def __str__(self):
		return self.song.pprint()
		
##########################################
