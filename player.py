import pygame
import time

music = pygame.mixer.music
#from pygame.mixer import music


from pygame import *
from mutagen.mp3 import MP3

song = "Music\\Destroy Boys - Secrets.mp3"



# mixer.music.load('example.mp3')
s = MP3(song)
songLength = s.info.length

# print("song length:", songLength)




# pygame.mixer.music.load(song)

# pygame.mixer.music.play()

# while pygame.mixer.music.get_busy() == True:
# 	continue

pygame.mixer.init(frequency=44100)

file = song

volume = 0.5# range [0.0, 1.0]
fadeout = 0 # fadeout lenght in miliseconds

def load(file):
	music.load(file)

def play():
	# play(loops=0, start=0.0, fade_ms=0) -> None
	music.play(fade_ms=fadeout)

def stop():
	music.stop()

def pause():
	music.pause()

def unpause():
	music.unpause()

def set_volume(vol):
	music.set_volume(vol)

def rewind():
	music.rewind()

def fastforward(sec):
	new_pos = music.get_pos() + sec # convert s into ms
	print("pos now:", music.get_pos(), "new pos:",new_pos)
	music.set_pos(new_pos)

###########idk got to get song length#################
def set_pos(position): # position= [0.0, 1.0] ???? set_pos = 0000 ... 10000=10sekund
	rewind()
	music.set_pos()

# def get_pos(): # miliseconds
# 	return music.get_pos()

def get_length():
	s = MP3(song)
	songLength = s.info.length
	return songLength


load(song)
play()

fastforward(songLength)

# print(music.get_pos(), "asdfkjačsldfjk")

while pygame.mixer.music.get_busy() == True:
	print(music.get_pos())
	continue

