import pygame, sys
from pygame.locals import *
from random import randint, randrange

class ScoreBoard:
	#Loading background image
	background = pygame.image.load("Sprites/scoreBackground.png")
	#init scoreboard
	def __init__(self,surface):
		self.surface = surface
		self.pos = (0,619)

	#update and display scoreboard
	def update(self,remainingAsteroids):
		self.surface.blit(ScoreBoard.background,self.pos) 

		for i in range(remainingAsteroids):
			rect = pygame.Rect(self.pos[0]+43+(i*13),self.pos[1]+11,15,62)

			r = 255+((i*10)*-1)
			g = 0+(10*i)

			pygame.draw.rect(self.surface,(r,g,r),rect)