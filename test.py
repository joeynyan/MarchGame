import pygame, sys, random
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

# main character class
class Cat(pygame.sprite.Sprite):
	def __init__(self):
		super(Cat, self).__init__()

		self.image = pygame.image.load('cat.png')
		self.rect = self.image.get_rect()
		self.width = self.image.get_width()/2
		self.height = self.image.get_height()/2

	def update(self):
		self.rect.y = mousey - self.height
		self.rect.x = mousex - self.width

class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		super(Enemy, self).__init__()

		self.image = pygame.Surface([10,10])
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y += 3

	def loc(self):
		self.rect.x = random.randint(0, GameWidth)
		self.rect.y = -20

# bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
 		
 		# defines size of bullet and colour
        self.image = pygame.Surface([4, 4]) 
        self.image.fill(RED) 
        self.rect = self.image.get_rect() # bullet is a rectangle
 
    def update(self):
        self.rect.y -= 10

    def shoot(self):
    	self.rect.x = mousex
    	self.rect.y = mousey

catImg = Cat() # creates your main character

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
			catImg.update()
		elif event.type == MOUSEBUTTONUP:
			pass
		elif event.type == MOUSEBUTTONDOWN:
			pass

	enemy = Enemy()
	enemy.loc()
	enemy_list.add(enemy)

	# Bullet creation code. Everytime it updates it'll create a bullet
	bullet = Bullet()
	bullet.shoot()
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
		if enemy.rect.y >= GameHeight+20:
			enemy_list.remove(enemy)

	pygame.display.update()
	fpsClock.tick(FPS)