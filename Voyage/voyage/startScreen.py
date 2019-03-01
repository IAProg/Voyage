import pygame, sys
from pygame.locals import *

import star, betBar, button

class StartScreen:
	clock = pygame.time.Clock()

	titleText = pygame.image.load("Sprites/titleText.png")
	helpText = pygame.image.load("Sprites/helpText.png")
	startButton = pygame.image.load("Sprites/startButton.png")

	def __init__(self, surface):
		self.loop = True
		self.surface = surface 

		self.mouseIsPressed = False

		self.titlePos = [0,25]
		self.helpPos = [50,375]
		self.startButtonPos = [200,280]

		self.startButton = button.Button(StartScreen.startButton,self.startButtonPos,self.surface)

		self.stars = pygame.sprite.Group()
		for i in range(50):
			self.stars.add(star.Star(self.surface))

		self.betBar = betBar.BetBar((200,620),self.surface)

		self.mainloop()

	def eventHandle(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		mousePos = pygame.mouse.get_pos()
		mouseClick = pygame.mouse.get_pressed()

		if mouseClick[0] == 1:
			if not self.mouseIsPressed:
				self.betBar.eventHandle(mousePos)
				self.mouseIsPressed = True
		else:
			self.mouseIsPressed = False


		if mouseClick[0] == 1:
			if self.startButton.isPressed(mousePos):
				self.exit()

	def exit(self):
		self.loop = False

	def getBet(self):
		return self.betBar.getBet()

	def update(self):
		self.surface.fill([20,20,60])

		for star in self.stars:
			star.update()

		self.surface.blit(StartScreen.titleText,self.titlePos)
		self.surface.blit(StartScreen.helpText,self.helpPos)

		self.startButton.update()

		self.betBar.update()

		pygame.display.flip()

	def mainloop(self):
		while self.loop:
			StartScreen.clock.tick(30)
			self.eventHandle()
			self.update()



