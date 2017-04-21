import pygame, sys, sprites
from pygame.locals import *

#Name of Game
nameOfGame = "Start"

# Colours
BLACK = (0,0,0);
WHITE = (255, 255, 255);
RED = (255, 0 ,0);
GREEN = (0, 255, 0);
BLUE = (0, 0, 255);


class Scene(object):
    def __init__(self):
        pass

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError

class SceneManager(object):
	def __init__(self, DISPLAYSURF):
		self.go_to(TitleScene(DISPLAYSURF))

	def go_to(self, scene):
		self.scene = scene
		self.scene.manager = self

class TitleScene(object):
	def __init__(self, DISPLAYSURF):
		super(TitleScene, self).__init__()
		# width and height of the button/image
		self.DISPLAYSURF = DISPLAYSURF
		self.imagew = 300
		self.imageh = 100
		self.image = pygame.Surface([self.imagew, self.imageh])
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()
		self.hwidth = self.image.get_width()/2
		self.hheight = self.image.get_height()/2
		# self.font = pygame.font.SysFont('Arial', 56) #font
		# location coords
		self.buttonlocation = (DISPLAYSURF.get_width()/2-self.hwidth, DISPLAYSURF.get_height()/2-self.hheight)
		self.onButton = False

	def render(self, DISPLAYSURF):
		# displays the image at the location set by buttonlocation
		DISPLAYSURF.blit(self.image, self.buttonlocation)
		# title = self.font.render(nameOfGame, True, BLACK)
		# DISPLAYSURF.blit(title, self.buttonlocation)

	def handle_events(self, events):
		for event in events:
			if event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if((mousex > self.buttonlocation[0] and mousex < self.buttonlocation[0] + self.imagew)
					and (mousey > self.buttonlocation[1] and mousey < self.buttonlocation[1] + self.imageh)):
					self.image.fill(BLACK)
					self.onButton = True
				else:
					self.onButton = False
					self.image.fill(BLUE)

			elif event.type == MOUSEBUTTONUP:
				pass
			elif event.type == MOUSEBUTTONDOWN:
				if self.onButton == True:
					self.manager.go_to(GameScene())
				pass

class GameScene(Scene):
	def __init__(self):
		super(GameScene, self).__init__()
		# sets mouse location
		self.mousex = 0
		self.mousey = 0

		# creates the main character
		self.cat = sprites.Cat()

		# Groups of Sprites (Required for Draw to work)
		self.cat_list = pygame.sprite.Group()
		self.cat_list.add(self.cat)
		self.enemy_list = pygame.sprite.Group()
		self.bullet_list = pygame.sprite.Group()


	def render(self, DISPLAYSURF):
		DISPLAYSURF.fill(WHITE)
		self.cat_list.draw(DISPLAYSURF) #draws cat
		self.enemy_list.draw(DISPLAYSURF) # draws enemy
		self.enemy_list.update() # makes enemies move
		self.bullet_list.draw(DISPLAYSURF) # draws the bullets
		self.bullet_list.update() # ensures the bullets move
		pass
	
	def handle_events(self, events):
		for event in events:
			if event.type == MOUSEMOTION:
				self.mousex, self.mousey = event.pos
				self.cat.update(self.mousex, self.mousey)
			elif event.type == MOUSEBUTTONUP:
				pass
			elif event.type == MOUSEBUTTONDOWN:
				pass
