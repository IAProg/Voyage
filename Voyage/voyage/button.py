import pygame, sys
from pygame.locals import *
from random import randint, randrange

class Button:
	def __init__(self,image,position,surface):
		self.image = image
		self.surface = surface
		self.position = position

		self.center()

	def center(self):
		self.rect = self.image.get_rect()
		self.rect.center = (self.position[0],self.position[1])

	def update(self):
		self.surface.blit(self.image,self.rect)

	def isPressed(self,mousePos):
		if self.rect.collidepoint(mousePos):
			return True
		else:
			return False
