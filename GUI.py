import pygame
from pygame.font import Font

pygame.font.init()

class Button:
	def __init__(self, text, pos, color="Black", hovering_color="Grey", size=(0,0), font_size=20):
		self.text = text
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.color = color
		self.hovering_color = hovering_color

		self.font = Font(size=font_size)
		self.text_rect = self.font.render(self.text, True, self.color)

		if size != (0,0):
			self.width = size[0]
			self.heigth = size[1]
			
			self.rect = pygame.Rect( (self.x_pos, self.y_pos), (self.width, self.heigth) )
		else:
			self.rect = pygame.Rect( (self.x_pos, self.y_pos), Font.size(Font(size=font_size), text) )

	def update(self, screen, pos=(-1,-1)):
		self.checkHover(pos)
		screen.blit(self.text_rect, self.rect)

	def checkInput(self, mouse_pos): # return true if mouse is over button rect
		# print(self.rect.left, self.rect.right)
		# print(self.rect.top, self.rect.bottom)

		if mouse_pos[0] in range(self.rect.left, self.rect.right) and mouse_pos[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def checkHover(self, mouse_pos):
		if self.checkInput(mouse_pos):
			self.text_rect = self.font.render(self.text, True, self.hovering_color)
		else:
			self.text_rect = self.font.render(self.text, True, self.color)

class Text:
	def __init__(self, text, pos, color, font_size=20):
		self.text = text
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.color = color
		self.font_size = font_size

		self.font = Font(size=font_size)
		self.text_rect = self.font.render(self.text, True, self.color)

		self.rect = pygame.Rect( (self.x_pos, self.y_pos), Font.size(Font(size=font_size), text) )

	def draw(self, screen):
		screen.blit(self.text_rect, self.rect)