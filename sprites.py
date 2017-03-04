import pygame, random
from pygame.locals import *

GameWidth = 500

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
		self.width = self.image.get_width()/2
		self.height = self.image.get_height()/2

	def update(self, mousex, mousey):
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

	def spawn(self):
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

    def spawn(self, mousex, mousey):
    	self.rect.x = mousex
    	self.rect.y = mousey