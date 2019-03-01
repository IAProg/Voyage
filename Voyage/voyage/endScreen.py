import pygame, sys
from pygame.locals import *

import button, star

class EndScreen:

	clock = pygame.time.Clock()

	quitButtonImage = pygame.image.load("Sprites/quitButton.png")
	replayButtonImage = pygame.image.load("Sprites/replayButton.png")

	def __init__(self,surface,numbersFound,numbersRequired, placedBet):
		self.score = len(set(numbersFound).intersection(numbersRequired))
		self.font = pygame.font.SysFont("system", 72)

		self.surface = surface
		self.loop = True
		self.replay = True

		replayButtonPos = [200,500]
		self.replayButton = button.Button(EndScreen.replayButtonImage, replayButtonPos, surface)

		quitButtonPos = [200,600]
		self.quitButton = button.Button(EndScreen.quitButtonImage, quitButtonPos, surface)

		self.stars = pygame.sprite.Group()
		for i in range(50):
			self.stars.add(star.Star(self.surface))

		self.mainloop()

	def update(self):
		self.surface.fill([20,20,60])

		for star in self.stars:
			star.update()

		self.replayButton.update()
		self.quitButton.update()

		self.surface.blit(self.font.render((str(self.score)+"/20"), 0, (255, 219, 55)), [150,100])
		self.surface.blit(self.font.render(("N/A"), 0, (255, 219, 55)), [150,150])

		pygame.display.flip()

	def eventHandle(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			mousePos = pygame.mouse.get_pos()
			mouseClick = pygame.mouse.get_pressed()

			if mouseClick[0] == 1:
				if self.replayButton.isPressed(mousePos):
					self.loop = False
					self.replay = True 

				if self.quitButton.isPressed(mousePos):
					self.loop = False
					self.replay = False

	def mainloop(self):
		while self.loop:
			EndScreen.clock.tick(30)
			self.eventHandle()
			self.update()

