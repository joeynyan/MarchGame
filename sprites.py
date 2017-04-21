import pygame, random
from pygame.locals import *

# GameWidth = 500
# GameHeight = 600

BLACK = (0,0,0);
WHITE = (255, 255, 255);
RED = (255, 0 ,0);
GREEN = (0, 255, 0);
BLUE = (0, 0, 255);

# main character class
class Cat(pygame.sprite.Sprite):
	def __init__(self, DISPLAYSURF):
		super(Cat, self).__init__()

		# self.image = pygame.image.load('cat.png')
		self.image = pygame.Surface([30, 30])
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		 
		self.width = self.image.get_width()/2
		self.height = self.image.get_height()/2

		self.rect.x = DISPLAYSURF.get_width()/2 - self.width
		self.rect.y = DISPLAYSURF.get_height()/2 - self.height

	def update(self, mousex, mousey):
		self.rect.y = mousey - self.height
		self.rect.x = mousex - self.width

# Enemy Class
class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		super(Enemy, self).__init__()

		self.image = pygame.Surface([30, 30])
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()
		self.midx = 0
		self.midy = 0
		self.speed = random.uniform(1, 2)
		self.BulletLoc = 0

	def getmidx(self):
		return self.midx
	def getmidy(self):
		return self.midy

	def update(self):
		self.rect.y += 3*self.speed
		self.midy = self.rect.y + self.rect.height/2
		self.BulletLoc += 10

	def shoot(self, DISPLAYSURF):
		if self.BulletLoc >= DISPLAYSURF.get_height()+20:
			self.BulletLoc = 0
			return True


	def spawn(self, DISPLAYSURF):
		self.rect.x = random.randint(0, DISPLAYSURF.get_width())
		self.rect.y = -20
		self.midx = self.rect.x + self.rect.width/2
		self.midy = self.rect.y + self.rect.height/2
		self.BulletLoc = self.midy

	def remove(self, enemy_list, cat_list, DISPLAYSURF):
		# Removes enemies when they go off screen also detects cat collision
		for enemy in enemy_list:
			hit_list = pygame.sprite.spritecollide(enemy, cat_list, True)
			for cat in hit_list:
				enemy_list.remove(enemy)
				cat_list.remove(cat)
				print('cat dead')

			if enemy.rect.y >= DISPLAYSURF.get_height()+20:
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

    def remove(self, bullet_list, enemy_list, score):
    	# Removes Bullet sprite when it goes off the screen and kills enemies
		for bullet in bullet_list:
			hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)
			for enemy in hit_list:
				bullet_list.remove(bullet)
				enemy_list.remove(enemy)
				score += 1

			if bullet.rect.y <= -10:
				bullet_list.remove(bullet)
		return score

class EnemyBullet(pygame.sprite.Sprite):
	def __init__(self):
		super(EnemyBullet, self).__init__()
		
		# defines size of bullet and colour
		self.image = pygame.Surface([4, 4]) 
		self.image.fill(BLACK) 
		self.rect = self.image.get_rect() # bullet is a rectangle
 
 	def update(self):
		self.rect.y += 10

	def spawn(self, x, y):
		self.rect.x = x
		self.rect.y = y

	def remove(self, ebullet_list, cat_list, DISPLAYSURF):
		# Removes Bullet sprite when it goes off the screen and kills enemies
		for bullet in ebullet_list:
			hit_list = pygame.sprite.spritecollide(bullet, cat_list, True)
			for cat in hit_list:
				ebullet_list.remove(bullet)
				cat_list.remove(cat)

			if bullet.rect.y >= DISPLAYSURF.get_height()+20:
				ebullet_list.remove(bullet)

