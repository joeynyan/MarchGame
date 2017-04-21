import pygame, sys, sprites, random
from pygame.locals import *

#Name of Game
nameOfGame = "Start"

# Colours
BLACK = (0,0,0);
WHITE = (255, 255, 255);
RED = (255, 0 ,0);
GREEN = (0, 255, 0);
BLUE = (0, 0, 255);

# Template for Scene Objects
class Scene(object):
	#Constructor
    def __init__(self): 
        pass

    # renders
    def render(self, screen):
        raise NotImplementedError

    # for updates (not currently used)
    def update(self):
        raise NotImplementedError

    # event handler
    def handle_events(self, events):
        raise NotImplementedError


# Scene Manager for transitioning to difference scenes
class SceneManager(object):
	def __init__(self, DISPLAYSURF):
		self.go_to(TitleScene(DISPLAYSURF))

	def go_to(self, scene):
		self.scene = scene
		self.scene.manager = self


# Title Screen
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

		self.score = 0

		# location coords
		self.buttonlocation = (DISPLAYSURF.get_width()/2-self.hwidth, DISPLAYSURF.get_height()/2-self.hheight)
		self.onButton = False

	def render(self, DISPLAYSURF):
		# displays the image at the location set by buttonlocation
		DISPLAYSURF.blit(self.image, self.buttonlocation)
		# title = self.font.render(nameOfGame, True, BLACK)
		# DISPLAYSURF.blit(title, self.buttonlocation)

	# Handles events that occur
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
					level = 1
					self.manager.go_to(GameScene(self.DISPLAYSURF, level, self.score))
				pass


# Game over screen (currently just a blue/black button)
class GameOver(object):
	def __init__(self, DISPLAYSURF):
		super(GameOver, self).__init__()

		self.DISPLAYSURF = DISPLAYSURF
		self.imagew = 300
		self.imageh = 100
		self.image = pygame.Surface([self.imagew, self.imageh])
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()
		self.hwidth = self.image.get_width()/2
		self.hheight = self.image.get_height()/2

		self.score = 0

		# location coords
		self.buttonlocation = (DISPLAYSURF.get_width()/2-self.hwidth, DISPLAYSURF.get_height()/2-self.hheight)
		self.onButton = False

	def render(self, DISPLAYSURF):
		DISPLAYSURF.blit(self.image, self.buttonlocation)

	# Handles events that occur
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
					level = 1
					self.manager.go_to(GameScene(self.DISPLAYSURF, level, self.score))
				pass

class GameScene(Scene):
	def __init__(self, DISPLAYSURF, level, score):
		super(GameScene, self).__init__()
		
		# screen and starting level (level determines how quickly enemy spawns (too quick))
		self.DISPLAYSURF = DISPLAYSURF
		self.level = level
		self.score = score
		self.clock = pygame.time.Clock()

		# clock = level*10 seconds
		pygame.time.set_timer(pygame.USEREVENT, 2*10*level*10)
		self.font = pygame.font.SysFont('Consolas', 30)
		self.counter = 2*level*10
		self.text = str(self.counter/2).rjust(3) + '  Level ' + str(self.level)

		# sets mouse location
		self.mousex = 0
		self.mousey = 0

		# creates the main character
		self.cat = sprites.Cat(DISPLAYSURF)

		# Groups of Sprites (Required for Draw to work)
		self.cat_list = pygame.sprite.Group()
		self.cat_list.add(self.cat)
		self.enemy_list = pygame.sprite.Group()
		self.bullet_list = pygame.sprite.Group()
		self.ebullet_list = pygame.sprite.Group()


	def render(self, DISPLAYSURF):
		# Drawing/updating code
		DISPLAYSURF.fill(WHITE)
		self.cat_list.draw(DISPLAYSURF) #draws cat
		self.enemy_list.draw(DISPLAYSURF) # draws enemy
		self.enemy_list.update() # makes enemies move
		self.bullet_list.draw(DISPLAYSURF) # draws the bullets
		self.bullet_list.update() # ensures the bullets move
		self.ebullet_list.draw(DISPLAYSURF)
		self.ebullet_list.update()
		DISPLAYSURF.blit(self.font.render(self.text, True, BLACK), (32, 48))
		DISPLAYSURF.blit(self.font.render(str(self.score).rjust(4), True, BLACK), (DISPLAYSURF.get_width() - 50, 48))

		# Enemy Creation Code. Everytime it updates it creates an enemy and ebullet
		enemy = sprites.Enemy()
		enemybullet = sprites.EnemyBullet()
		if random.randint(1,10) <= self.level:
			enemy.spawn(DISPLAYSURF)
			self.enemy_list.add(enemy)
			enemybullet.spawn(enemy.getmidx(), enemy.getmidy())
			self.ebullet_list.add(enemybullet)

		#enemy reshooting code
		for enemy in self.enemy_list:
			if enemy.shoot(DISPLAYSURF) == True:
				enemybullet.spawn(enemy.getmidx(), enemy.getmidy())
				self.ebullet_list.add(enemybullet)

		# Bullet creation code. Everytime it updates it'll create a bullet
		bullet = sprites.Bullet()
		bullet.spawn(self.mousex, self.mousey)
		self.bullet_list.add(bullet)

		enemy.remove(self.enemy_list, self.cat_list, DISPLAYSURF)
		enemybullet.remove(self.ebullet_list, self.cat_list, DISPLAYSURF)
		self.score = bullet.remove(self.bullet_list, self.enemy_list, self.score)
		pass
	
	def handle_events(self, events):
		# check if cat is still alive
		if not self.cat_list:
			print 'Gameover'
			self.manager.go_to(GameOver(self.DISPLAYSURF))

		if self.counter <= 0:
			print 'Level up'
			self.level += 1
			self.manager.go_to(GameScene(self.DISPLAYSURF, self.level, self.score))
		for event in events:
			if event.type == MOUSEMOTION:
				self.mousex, self.mousey = event.pos
				self.cat.update(self.mousex, self.mousey)
			elif event.type == MOUSEBUTTONUP:
				pass
			elif event.type == MOUSEBUTTONDOWN:
				pass
			elif event.type == pygame.USEREVENT:
				self.counter -= 1;
				self.text = str(self.counter/2).rjust(3) + '  Level ' + str(self.level)

