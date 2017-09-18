# this will include all of the game text
import pygame

class Game_text(object):
	def __init__(self,font,color):
		self.font = font
		self.color = color

	def opening_sequence(self):
			init_text = font.render("""Welcome brave adventurer. 
			Are you ready for the greatest quest of your life?""", True, (0, 0, 0))  
			background_image.blit(init_text, [500,400])


