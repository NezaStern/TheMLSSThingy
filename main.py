### first install the dependencies wiht " pip install -r dependencies.txt
### spotdl --download-ffmpeg


#The MLSSS thingy

#lol idk pac the main handler and running file
# probbly bo tle runon pygame right?
# import pygame

import song

# import player

# player.play()

import metadata

import GUI_handler


import threading

# song_path = "Music\\MARINA - Primadonna.mp3"

# marina = metadata.Metadata(song_path)
# marina.get_lyrics()

#print(song.Song("Cry it out", "rain on fridays").get_lyrics())

# denial_lyric = song.Song("Denial is a river", "doechii").get_lyrics()
# print(denial_lyric)

a = song.Song("Denial is a river", "Doechii")
# a.download_song()
# print(a.get_path())
# print(a.get_lyrics())

# song1 = "Music\Doechii - DENIAL IS A RIVER.mp3"
# metadata.metadata(song1).add_lyrics_tag(denial_lyric)
# print(metadata.metadata(song1))



# song2 = "Music\Kendrick Lamar - Not Like Us.mp3"
# print(metadata.metadata(song2))


# s1 = song.Song("Dont delete the kisses", "Wolf Alice")
# s1.download_song()

# alice = "Music\\Wolf Alice - Don’t Delete The Kisses.mp3"
# aaaa = metadata.Metadata(alice)
# print(aaaa.get_lyrics)


# # pygame setup
# pygame.init()
# pygame.display.set_caption("The MLSS Thingy")

# screen_width = 1000
# screen_height = 600

# FPS = 60

# screen = pygame.display.set_mode((screen_width, screen_height))
# clock = pygame.time.Clock()

# # GUI
# # colors
# color_pastel_orange = "#F29F58"
# color_maroon = "#AB4459"
# color_dark_purple = "#441752"
# color_dark_blackish = "#1B1833"

# screen.fill(color_maroon)



# from button import Button

# tab1 = Button("tab1", pos=(100,100), size=(100,50), font_size=200)



# running = True
# while running:
# 	for event in pygame.event.get():  		# exit if escape key pressed (first needs to chekc if KEYDOWN is the event)
# 		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
# 			running = False

# 	# print(pygame.mouse.get_pos())

# 	pygame.display.update()
# 	clock.tick(FPS)

# 	tab1.update(screen)
# 	print(tab1.checkInput(pygame.mouse.get_pos()))

# pygame.quit()


GUI_thread = threading.Thread(target=GUI_handler.gui)

GUI_thread.start()

GUI_thread.join() # program dosent finish until this thread finishes