import pygame, sys
from pygame.locals import *

BLACK = (0,	0, 0)
BLUE = (0, 0, 255)

class TitleScene(object):
	def __init__(self):
		super(TitleScene, self).__init__()
		self.image = pygame.Surface([300, 100])
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()
		self.hwidth = self.image.get_width()/2
		self.hheight = self.image.get_height()/2

	def render(self, DISPLAYSURF):
		DISPLAYSURF.blit(self.image, (DISPLAYSURF.get_width()/2-self.hwidth, DISPLAYSURF.get_height()/2-self.hheight))	