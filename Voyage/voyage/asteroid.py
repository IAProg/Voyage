import pygame, sys
from pygame.locals import *
from random import randint, randrange

import button

class Asteroid(pygame.sprite.Sprite, button.Button):
	#loading textures into list
	size1 = pygame.image.load("Sprites/AsteroidSmall.png")
	size2 = pygame.image.load("Sprites/AsteroidMed.png")
	size3 = pygame.image.load("Sprites/AsteroidLarge.png")
	size4 = pygame.image.load("Sprites/AsteroidVLarge.png")
	skins = [size1,size2,size3,size4]

	#speed that the asteroids move down the screen
	speed = 1.5

	rgbDefualt =  (255, 219, 55)
	rgbFound = (0,200,100)

	def __init__(self,surface,xPos):
		pygame.sprite.Sprite.__init__(self)
		self.clicked = False
		self.valueSent = False

		self.rgb = (0,0,0)

		self.surface = surface
		self.pos = [xPos*100+10,-50]
		self.size = randint(1,4)

		valRange = 25*self.size
		self.value = randrange(valRange-25+1,valRange)
		self.rect = Asteroid.size4.get_rect()

		self.font = pygame.font.SysFont("system", 72)

	def isPressed(self,mousePos, requiredNumbers):
		if self.rect.collidepoint(mousePos) and not self.clicked:
			self.clicked = True

			if self.value in requiredNumbers:
				self.rgb = Asteroid.rgbFound
			else:
				self.rgb = Asteroid.rgbDefualt

			return self.value
		else:
			return False

	def update(self):
		self.pos[1] += Asteroid.speed

		self.rect.x = self.pos[0]
		self.rect.y = self.pos[1]

		if self.pos[1] > 600:
			self.kill()


		if not self.clicked:
			self.surface.blit(Asteroid.skins[self.size-1],(self.pos))
		else:
			self.surface.blit(self.font.render(str(self.value), 0,self.rgb), self.rect)

