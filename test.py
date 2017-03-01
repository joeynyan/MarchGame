import pygame, sys
from pygame.locals import *

pygame.init()
FPS = 30 #frames per sec
fpsClock = pygame.time.Clock()

# game window
DISPLAYSURF = pygame.display.set_mode((430, 350), 0, 32)
pygame.display.set_caption('Hello World!')

# colors
BLACK = (0,0,0);
WHITE = (255, 255, 255);
RED = (255, 0 ,0);
GREEN = (0, 255, 0);
BLUE = (0, 0, 255);

catImg = pygame.image.load('cat.png')
mousex = 0
mousey = 0
width = catImg.get_width()/2
height = catImg.get_height()/2
catx = mousex - width
caty = mousey - height
direction = 'right'
# DISPLAYSURF.fill(WHITE)
# pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
# pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
# pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
# pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
# pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
# pygame.draw.rect(DISPLAYSURF, red, (200, 140, 100, 50))

# pixObj = pygame.PixelArray(DISPLAYSURF)
# pixObj[480][380] = BLACK
# pixObj[482][382] = BLACK
# pixObj[484][384] = BLACK
# pixObj[486][386] = BLACK
# pixObj[488][388] = BLACK
# del pixObj

while True:
	DISPLAYSURF.fill(BLUE)

	# if direction == 'right':
	# 	catx+=5
	# 	if catx == 280:
	# 		direction = 'down'
	# elif direction == 'down':
	# 	caty+=5
	# 	if caty == 220:
	# 		direction = 'left'
	# elif direction == 'left':
	# 	catx-=5
	# 	if catx == 20:
	# 		direction = 'up'
	# elif direction == 'up':
	# 	caty-=5
	# 	if caty == 10:
	# 		direction = 'right'
	
	DISPLAYSURF.blit(catImg, (catx, caty));	#copies cat image to next location	
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEMOTION:
			mousex, mousey = event.pos
			catx = mousex - width
			caty = mousey - height
		elif event.type == MOUSEBUTTONUP:
			mousex, mousey = event.pos
		elif event.type == MOUSEBUTTONDOWN:
			mousex, mousey = event.pos
			mouseClicked = True;
	pygame.display.update()
	fpsClock.tick(FPS)