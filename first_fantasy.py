import pygame

from pygame.sprite import Group, groupcollide
from Game_text import Game_text

pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 25)

screen_size = (1000,800)
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("FIRST FANTASY")
background_image = pygame.image.load("first_fantasy_images/ffbackgroundsmall.png")

# find music later
# pygame.mixer.init()
# pygame.mixer.music.load()
# pygame.mixer.music.play()

game_on = True

while game_on: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False
		else:
			Game_text.opening_sequence

			init_text = font.render("""Welcome brave adventurer. Are you ready for the greatest quest of your life?""", True, (0, 0, 0))  
			background_image.blit(init_text, [190,390])


	
	pygame_screen.blit(background_image, [0,0])

	pygame.display.flip() 

