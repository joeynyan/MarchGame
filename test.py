import sprites, pygame, sys, random
from pygame.locals import *

pygame.init()
FPS = 30 #frames per sec
fpsClock = pygame.time.Clock()

# game window
GameWidth = 500
GameHeight = 600
DISPLAYSURF = pygame.display.set_mode((GameWidth, GameHeight), 0, 32)
pygame.display.set_caption('Cat Game')

# colors
BLACK = (0,0,0);
WHITE = (255, 255, 255);
RED = (255, 0 ,0);
GREEN = (0, 255, 0);
BLUE = (0, 0, 255);

# sets mouse location
mousex = 0
mousey = 0

# creates the main character
catImg = sprites.Cat() 

# Groups of Sprites (Required for Draw to work)
cat_list = pygame.sprite.Group()
cat_list.add(catImg)
enemy_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

while True:
	DISPLAYSURF.fill(WHITE)
	cat_list.draw(DISPLAYSURF) #draws cat
	enemy_list.draw(DISPLAYSURF) # draws enemy
	enemy_list.update() # makes enemies move
	bullet_list.draw(DISPLAYSURF) # draws the bullets
	bullet_list.update() # ensures the bullets move
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEMOTION:
			mousex, mousey = event.pos
			catImg.update(mousex, mousey)
		elif event.type == MOUSEBUTTONUP:
			pass
		elif event.type == MOUSEBUTTONDOWN:
			pass

	# Enemy Creation Code. Everytime it updates it creates an enemy
	enemy = sprites.Enemy()
	enemy.spawn()
	enemy_list.add(enemy)

	# Bullet creation code. Everytime it updates it'll create a bullet
	bullet = sprites.Bullet()
	bullet.spawn(mousex, mousey)
	bullet_list.add(bullet)

	# Removes Bullet sprite when it goes off the screen
	for bullet in bullet_list:
		hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)
		for enemy in hit_list:
			bullet_list.remove(bullet)
			enemy_list.remove(enemy)

		if bullet.rect.y <= -10:
			bullet_list.remove(bullet)

	for enemy in enemy_list:
		hit_list = pygame.sprite.spritecollide(enemy, cat_list, True)
		for cat in hit_list:
			enemy_list.remove(enemy)
			cat_list.remove(cat)
			print('cat dead')

		if enemy.rect.y >= GameHeight+20:
			enemy_list.remove(enemy)

	pygame.display.update()
	fpsClock.tick(FPS)