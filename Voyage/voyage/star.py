import pygame, sys
from pygame.locals import *
from random import randint, randrange

class Star(pygame.sprite.Sprite):
	#loading star textures into list
	star1 = pygame.image.load("Sprites/Star1.png")
	star2 = pygame.image.load("Sprites/Star2.png")
	star3 = pygame.image.load("Sprites/Star3.png")
	star4 = pygame.image.load("Sprites/Star4.png")
	skins = [star1,star2,star3,star4]

	#Star init function giving random start data
	def __init__(self,surface):
		pygame.sprite.Sprite.__init__(self)
		self.surface = surface
		self.size = randint(1,4)
		self.pos = [randint(-5,405),randint(-10,700)]
	
	#reset function to reuse star object
	def new(self):
		self.pos[0] = randint(0,400)
		self.pos[1] = -10
		self.size = randint(1,4)

	#update function, moves and displays star
	def update(self):
		self.pos[1] += 0.1 * self.size
		if self.pos[1]>700:
			self.new()

		self.surface.blit(Star.skins[self.size-1],(self.pos))
