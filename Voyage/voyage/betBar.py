import pygame, sys
from pygame.locals import *
from random import randint, randrange

import button

class BetBar:
	upImage = pygame.image.load("Sprites/betUp.png")
	downImage = pygame.image.load("Sprites/betDown.png")
	frameImage = pygame.image.load("Sprites/betFrame.png")

	icon5 = pygame.image.load("Sprites/5p.png")
	icon20 = pygame.image.load("Sprites/20p.png")
	icon50 = pygame.image.load("Sprites/50p.png")
	icon100 = pygame.image.load("Sprites/100p.png")

	icons = [icon5,icon20,icon50,icon100]
	bets = [5,20,50,100]

	def __init__(self,position,surface):
		offset = 110

		self.betTrack = 1000
		self.currentBet = BetBar.bets[0]
		self.currentIcon = BetBar.icons[0]

		self.surface = surface
		self.frameRect = BetBar.frameImage.get_rect()
		self.frameRect.center = position

		self.iconRect = self.currentIcon.get_rect()
		self.iconRect.center = position

		self.upBet = button.Button(BetBar.upImage,(position[0]+offset,position[1]),self.surface)
		self.downBet = button.Button(BetBar.downImage,(position[0]-offset,position[1]),self.surface)

		self.buttonContainer = [self.upBet,self.downBet]

	def getBet(self):
		return self.currentBet

	def changeBet(self,choice):

		if choice:
			self.betTrack += 1

		else:
			self.betTrack -= 1

		self.currentIcon = BetBar.icons[self.betTrack % len(BetBar.icons)]			
		self.currentBet = BetBar.bets[self.betTrack % len(BetBar.bets)]	
		

	def update(self):
		self.surface.blit(BetBar.frameImage,self.frameRect)
		self.surface.blit(self.currentIcon,self.iconRect)
		self.upBet.update()
		self.downBet.update()

	def eventHandle(self,mousePos):
		if self.upBet.rect.collidepoint(mousePos):
			self.changeBet(1)

		if self.downBet.rect.collidepoint(mousePos):
			self.changeBet(0)

		print(self.currentBet)


