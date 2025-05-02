import pygame
import sys
from GUI import Button, Text

# class Tab:
# 	def __init__(self, title, background_color):
# 		self.title = title
# 		self.background_color = background_color


# class Player(Tab):
# 	def __init__(self, title, background_color):
# 		super().__init__(title, background_color)

screen_width = 1000
screen_height = 600

FPS = 60

# colors
color_pastel_orange = "#F29F58"
color_maroon = "#AB4459"
color_dark_purple = "#441752"
color_dark_blackish = "#1B1833"

def get_font(size):
	FONT = pygame.font.Font(size=size)
	return FONT

space_between_tabs = 150
tabs_font_size = 30

# tabs = ["Player", "Files", "Sheet"]
PLAYER_BUTTON = Button("Player", pos=(space_between_tabs,0), color="Pink", hovering_color="Black", font_size=tabs_font_size)
DOWNLOAD_BUTTON = Button("Download", pos=(PLAYER_BUTTON.rect.right + space_between_tabs, 0), color=color_pastel_orange, hovering_color="Purple", font_size=tabs_font_size)
FILES_BUTTON = Button("Files", pos=(DOWNLOAD_BUTTON.rect.right + space_between_tabs, 0), color="Black", hovering_color="White", font_size=tabs_font_size)
SHEET_BUTTON = Button("Sheet", pos=(FILES_BUTTON.rect.right + space_between_tabs, 0), color="Orange", hovering_color="Black", font_size=tabs_font_size)

def gui():

	pygame.init()
	pygame.display.set_caption("The MLSS Thingy")		

	screen = pygame.display.set_mode((screen_width, screen_height))
	clock = pygame.time.Clock()

	screen.fill(color_maroon)

	while True:

		screen.fill(color_maroon)

		MOUSE_POS = pygame.mouse.get_pos()
		# print(pygame.mouse.get_pos())

		# tabs background color strip
		pygame.draw.rect(screen, color_dark_purple, rect=(0,0, screen_width, 20))

		# draw buttons
		for button in [PLAYER_BUTTON, DOWNLOAD_BUTTON, FILES_BUTTON, SHEET_BUTTON]:
			button.update(screen, MOUSE_POS)

		for event in pygame.event.get():  		# exit if escape key pressed (first needs to chekc if KEYDOWN is the event)
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				pygame.quit()
				sys.exit()

			# check for tab buttons input
			if event.type == pygame.MOUSEBUTTONDOWN:
				if PLAYER_BUTTON.checkInput(MOUSE_POS):
					print("clicked palyer button")
					player_tab()
				elif DOWNLOAD_BUTTON.checkInput(MOUSE_POS):
					print("download button clicked")
					download_tab()
				elif FILES_BUTTON.checkInput(MOUSE_POS):
					print("files button clicled")
					files_tab()
				elif SHEET_BUTTON.checkInput(MOUSE_POS):
					print("Sheet button clicked")
					sheet_tab()

		pygame.display.update()
		clock.tick(FPS)

def player_tab():
	pygame.display.set_caption("The MLSS Thingy : Player")	

	screen = pygame.display.set_mode((screen_width, screen_height))
	clock = pygame.time.Clock()

	###

	info_text = Text("Player tab", (screen_width/2, screen_height/2), "Purple", font_size=50)


	# player buttons
	player_color = color_dark_purple
	player_hover_color = "White"
	player_font = 50
	player_hight = 540
	PLAY = Button(">", (screen_width/2-20, player_hight), color=player_color, hovering_color=player_hover_color, font_size=player_font)
	NEXT = Button(">|", (screen_width/2+60, player_hight), color=player_color, hovering_color=player_hover_color, font_size=player_font)
	PREV = Button("|<", (screen_width/2-120, player_hight), color=player_color, hovering_color=player_hover_color, font_size=player_font)

	PLAY_BUTTONS = [PLAY, NEXT, PREV]

	current_song_title = "test title ..........aaa"
	current_song_artist = "test artist name"
	playing_time = 11.11

	title = Text(current_song_title, (20, 480), "Pink", 35)
	artist = Text(current_song_artist, (25, 505), color_dark_purple, 22)
	playing_time_text = Text(str(playing_time), (screen_width-85, screen_height-90), "White", 28)

	text_to_display = [title, artist, playing_time_text]
	###

	while True:

		screen.fill(color_maroon)

		MOUSE_POS = pygame.mouse.get_pos()

		# tabs background color strip
		pygame.draw.rect(screen, color_dark_purple, rect=(0,0, screen_width, 20))

		###

		info_text.draw(screen)

		timeline = pygame.draw.rect(screen, "Gray", rect=(40, 530, screen_width-80, 5))

		for button in PLAY_BUTTONS:
			button.update(screen, MOUSE_POS)

		for t in text_to_display:
			t.draw(screen)

		###

		# draw buttons
		for button in [PLAYER_BUTTON, DOWNLOAD_BUTTON, FILES_BUTTON, SHEET_BUTTON]:
			button.update(screen, MOUSE_POS)

		for event in pygame.event.get():  		# exit if escape key pressed (first needs to chekc if KEYDOWN is the event)
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				pygame.quit()
				sys.exit()

			# check for tab buttons input
			if event.type == pygame.MOUSEBUTTONDOWN:
				if PLAYER_BUTTON.checkInput(MOUSE_POS):
					print("clicked palyer button, but we're here lol")
				elif DOWNLOAD_BUTTON.checkInput(MOUSE_POS):
					print("download button clicked")
					download_tab()
				elif FILES_BUTTON.checkInput(MOUSE_POS):
					print("files button clicled")
					files_tab()
				elif SHEET_BUTTON.checkInput(MOUSE_POS):
					print("Sheet button clicked")
					sheet_tab()

		pygame.display.update()
		clock.tick(FPS)

def download_tab():
	pygame.display.set_caption("The MLSS Thingy : Download")	

	screen = pygame.display.set_mode((screen_width, screen_height))
	clock = pygame.time.Clock()

	info_text = Text("download tab", (screen_width/2, screen_height/2), "Purple", font_size=50)

	while True:

		screen.fill(color_maroon)

		MOUSE_POS = pygame.mouse.get_pos()

		# tabs background color strip
		pygame.draw.rect(screen, color_dark_purple, rect=(0,0, screen_width, 20))

		info_text.draw(screen)

		# draw buttons
		for button in [PLAYER_BUTTON, DOWNLOAD_BUTTON, FILES_BUTTON, SHEET_BUTTON]:
			button.update(screen, MOUSE_POS)

		for event in pygame.event.get():  		# exit if escape key pressed (first needs to chekc if KEYDOWN is the event)
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				pygame.quit()
				sys.exit()

			# check for tab buttons input
			if event.type == pygame.MOUSEBUTTONDOWN:
				if PLAYER_BUTTON.checkInput(MOUSE_POS):
					print("clicked palyer button")
					player_tab()
				elif DOWNLOAD_BUTTON.checkInput(MOUSE_POS):
					print("download button clicked, but we're here lol")
				elif FILES_BUTTON.checkInput(MOUSE_POS):
					print("files button clicled")
					files_tab()
				elif SHEET_BUTTON.checkInput(MOUSE_POS):
					print("Sheet button clicked")
					sheet_tab()

		pygame.display.update()
		clock.tick(FPS)

def files_tab():
	pygame.display.set_caption("The MLSS Thingy : Files")	

	screen = pygame.display.set_mode((screen_width, screen_height))
	clock = pygame.time.Clock()

	info_text = Text("files tab", (screen_width/2, screen_height/2), "Purple", font_size=50)

	while True:

		screen.fill(color_maroon)

		MOUSE_POS = pygame.mouse.get_pos()
		# print(pygame.mouse.get_pos())

		# tabs background color strip
		pygame.draw.rect(screen, color_dark_purple, rect=(0,0, screen_width, 20))

		info_text.draw(screen)

		# draw buttons
		for button in [PLAYER_BUTTON, DOWNLOAD_BUTTON, FILES_BUTTON, SHEET_BUTTON]:
			button.update(screen, MOUSE_POS)

		for event in pygame.event.get():  		# exit if escape key pressed (first needs to chekc if KEYDOWN is the event)
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				pygame.quit()
				sys.exit()

			# check for tab buttons input
			if event.type == pygame.MOUSEBUTTONDOWN:
				if PLAYER_BUTTON.checkInput(MOUSE_POS):
					print("clicked palyer button")
					player_tab()
				elif DOWNLOAD_BUTTON.checkInput(MOUSE_POS):
					print("download button clicked")
					download_tab()
				elif FILES_BUTTON.checkInput(MOUSE_POS):
					print("files button clicled, but we're here lol")
				elif SHEET_BUTTON.checkInput(MOUSE_POS):
					print("Sheet button clicked")
					sheet_tab()

		pygame.display.update()
		clock.tick(FPS)

def sheet_tab():
	pygame.display.set_caption("The MLSS Thingy : Sheet")	

	screen = pygame.display.set_mode((screen_width, screen_height))
	clock = pygame.time.Clock()

	info_text = Text("sheet tab", (screen_width/2, screen_height/2), "Purple", font_size=50)

	while True:

		screen.fill(color_maroon)

		MOUSE_POS = pygame.mouse.get_pos()
		# print(pygame.mouse.get_pos())

		# tabs background color strip
		pygame.draw.rect(screen, color_dark_purple, rect=(0,0, screen_width, 20))

		info_text.draw(screen)

		# draw buttons
		for button in [PLAYER_BUTTON, DOWNLOAD_BUTTON, FILES_BUTTON, SHEET_BUTTON]:
			button.update(screen, MOUSE_POS)

		for event in pygame.event.get():  		# exit if escape key pressed (first needs to chekc if KEYDOWN is the event)
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				pygame.quit()
				sys.exit()

			# check for tab buttons input
			if event.type == pygame.MOUSEBUTTONDOWN:
				if PLAYER_BUTTON.checkInput(MOUSE_POS):
					print("clicked palyer button")
					player_tab()
				elif DOWNLOAD_BUTTON.checkInput(MOUSE_POS):
					print("download button clicked")
					download_tab()
				elif FILES_BUTTON.checkInput(MOUSE_POS):
					print("files button clicled")
					files_tab()
				elif SHEET_BUTTON.checkInput(MOUSE_POS):
					print("Sheet button clicked, but we're here lol")

		pygame.display.update()
		clock.tick(FPS)

