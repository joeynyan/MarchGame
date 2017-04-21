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
	pygame.init()
	FPS = 30
	fpsClock = pygame.time.Clock()

	DISPLAYSURF = pygame.display.set_mode((GameWidth, GameHeight))
	pygame.display.set_caption(Caption)

	manager = scenes.SceneManager(DISPLAYSURF)

	while True:
		DISPLAYSURF.fill(WHITE)
		manager.scene.render(DISPLAYSURF)
		if pygame.event.get(QUIT):
				pygame.quit()
				sys.exit()
		manager.scene.handle_events(pygame.event.get())

		pygame.display.update()
		fpsClock.tick(FPS)

# Starts Game
main()
