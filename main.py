import pygame, sys, scenes, sprites
from pygame.locals import *

#game window
GameWidth = 500
GameHeight = 600
Caption = 'Cat Game'

# colors
BLACK = (0,0,0);
WHITE = (255, 255, 255);
RED = (255, 0 ,0);
GREEN = (0, 255, 0);
BLUE = (0, 0, 255);

def main():
	global DISPLAYSURF 

	pygame.init()
	FPS = 30
	fpsClock = pygame.time.Clock()

	DISPLAYSURF = pygame.display.set_mode((GameWidth, GameHeight))
	pygame.display.set_caption(Caption)

	title = scenes.TitleScene()


	while True:
		DISPLAYSURF.fill(WHITE)
		title.render(DISPLAYSURF)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()
		fpsClock.tick(FPS)


main()