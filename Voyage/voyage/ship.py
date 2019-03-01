import pygame, sys
from pygame.locals import *
from random import randint, randrange

class Ship(pygame.sprite.Sprite):
	shipImage = pygame.image.load("Sprites/ship.png")
	def __init__(self,surface):
		pygame.sprite.Sprite.__init__(self)

		self.surface = surface
		self.rect = Ship.shipImage.get_rect()
		self.rect.y = 580

	def getPos(self):
		return (self.rect.centerx-4,self.rect.y)

	def move(self,position):
		self.rect.centerx = position[0]

	def update(self):
		self.surface.blit(Ship.shipImage,self.rect)
		#debug option draw hitbox
		#pygame.draw.rect(self.surface,(0,255,0),self.rect,1)