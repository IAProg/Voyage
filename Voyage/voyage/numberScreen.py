import pygame, sys
from pygame.locals import *
from random import randint, choice, randrange

import star, button

class NumberScreen:
	clock = pygame.time.Clock()

	buttonImage1 = pygame.image.load("Sprites/numberButton.png")
	buttonImage2 = pygame.image.load("Sprites/startButton.png")

	def __init__(self, surface):
		self.surface = surface
		self.clicks = 0

		self.remainingNumbers = 20
		self.selectedNumbers = []

		self.font = pygame.font.SysFont("system", 50)

		self.loop = True
		self.mouseIsPressed = False

		self.buttonPos = [200,600]
		self.numberButton = button.Button(NumberScreen.buttonImage1,self.buttonPos,self.surface)

		self.stars = pygame.sprite.Group()
		for i in range(50):
			self.stars.add(star.Star(self.surface))

		self.mainloop()

	def updateButton(self):
		self.numberButton.image = (NumberScreen.buttonImage2)
		self.numberButton.center()

	def generateNumber(self):
		self.selectedNumbers = []

		for size in range(1,5):

				maxVal = 25*size
				minVal = (maxVal-25)+1

				for i in range(5):
					inList = True

					while inList:
						value = randint(minVal,maxVal)
						if value not in self.selectedNumbers:
							self.selectedNumbers.append(value)
							inList = False

	def getNumbers(self):
		return self.selectedNumbers

	def eventHandle(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		mousePos = pygame.mouse.get_pos()
		mouseClick = pygame.mouse.get_pressed()

		if mouseClick[0] == 1:
			if not self.mouseIsPressed:
				if self.numberButton.isPressed(mousePos):
					self.generateNumber()
					self.updateButton()
					self.mouseIsPressed = True

					self.clicks += 1

					if self.clicks >= 2:
						self.loop = False
		else:
			self.mouseIsPressed = False

	def displayNumbers(self):

		text = self.font.render("Your Numbers Are", 0, (255, 219, 55))
		dest = (50, 50)
		self.surface.blit(text,dest)

		for x, number in enumerate(self.selectedNumbers, 1):

			col = 80*(x%4)+65
			row = 80*(x%5)+140

			text = self.font.render(str(number), 0, (255, 219, 55))
			dest = (col, row)
			self.surface.blit(text,dest)

	def displayInstructions(self):
		text = self.font.render("Click ""?""", 0, (255, 219, 55))
		dest = (150, 50)
		self.surface.blit(text,dest)


	def update(self):
		self.surface.fill([20,20,60])

		for star in self.stars:
			star.update()

		if self.selectedNumbers != []:
			self.displayNumbers()

		else:
			self.displayInstructions()

		self.numberButton.update()

		pygame.display.flip()

	def mainloop(self):
		while self.loop:
			NumberScreen.clock.tick(30)
			self.eventHandle()
			self.update()



