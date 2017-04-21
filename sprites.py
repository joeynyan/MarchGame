import pygame, random
from pygame.locals import *

GameWidth = 500
GameHeight = 600

BLACK = (0,0,0);
WHITE = (255, 255, 255);
RED = (255, 0 ,0);
GREEN = (0, 255, 0);
BLUE = (0, 0, 255);

# main character class
class Cat(pygame.sprite.Sprite):
	def __init__(self):
		super(Cat, self).__init__()

		self.image = pygame.image.load('cat.png')
		self.rect = self.image.get_rect()
		self.rect.x = GameWidth/2
		self.rect.y = GameHeight/2 
		self.width = self.image.get_width()/2
		self.height = self.image.get_height()/2

	def update(self, mousex, mousey):
		self.rect.y = mousey - self.height
		self.rect.x = mousex - self.width

# Enemy Class
class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		super(Enemy, self).__init__()

		self.image = pygame.Surface([10,10])
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y += 3

	def spawn(self):
		self.rect.x = random.randint(0, GameWidth)
		self.rect.y = -20

	def remove(self, enemy_list, cat_list):
		# Removes enemies when they go off screen also detects cat collision
		for enemy in enemy_list:
			hit_list = pygame.sprite.spritecollide(enemy, cat_list, True)
			for cat in hit_list:
				enemy_list.remove(enemy)
				cat_list.remove(cat)
				print('cat dead')

			if enemy.rect.y >= GameHeight+20:
				enemy_list.remove(enemy)

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

    def spawn(self, mousex, mousey):
    	self.rect.x = mousex
    	self.rect.y = mousey

    def remove(self, bullet_list, enemy_list):
    	# Removes Bullet sprite when it goes off the screen and kills enemies
		for bullet in bullet_list:
			hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)
			for enemy in hit_list:
				bullet_list.remove(bullet)
				enemy_list.remove(enemy)

			if bullet.rect.y <= -10:
				bullet_list.remove(bullet)