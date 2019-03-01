import pygame, sys
from pygame.locals import *
from random import randint, randrange

import star, asteroid, bullet, ship, scoreBoard

class Game:
	clock = pygame.time.Clock()
	def __init__(self, surface, numbersRequired):
		self.surface = surface 

		self.mouseIsPressed = False

		self.numbersRequired = numbersRequired	
		self.remainingAsteroids = 25
		self.numbersFound = []

		self.scoreBoard= scoreBoard.ScoreBoard(self.surface)
		self.ship = ship.Ship(self.surface)

		self.stars = pygame.sprite.Group()
		for i in range(50):
			self.stars.add(star.Star(self.surface))

		self.asteroids = pygame.sprite.Group()
		pygame.time.set_timer(USEREVENT, 2000)

		self.bullets = pygame.sprite.Group()

		self.mainloop()

	def spawnAsteroid(self):
		for column in range(4):
			self.asteroids.add(asteroid.Asteroid(self.surface,column))

	def fire(self,mousePos):
		self.bullets.add(bullet.Bullet(self.surface,self.ship.getPos(),mousePos))
		self.remainingAsteroids -= 1

	def getNumbers(self):
		return self.numbersFound

	def eventHandle(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if event.type == USEREVENT:
				self.spawnAsteroid()


		mousePos = pygame.mouse.get_pos()
		mouseClick = pygame.mouse.get_pressed()

		self.ship.move(mousePos)

		if mouseClick[0] == 1:
			if not self.mouseIsPressed:
				self.fire(mousePos[1])
				self.mouseIsPressed = True

				for asteroid in self.asteroids:
					value = asteroid.isPressed(mousePos, self.numbersRequired)

					if value is not False:
						self.numbersFound.append(value)
		else:
			self.mouseIsPressed = False



	def update(self):

		self.surface.fill([20,20,60])

		for star in self.stars:
			star.update()

		for bullet in self.bullets:
			bullet.update()

		for asteroid in self.asteroids:
			asteroid.update()

		self.scoreBoard.update(self.remainingAsteroids)

		self.ship.update()
		pygame.display.flip()

	def mainloop(self):
		while self.remainingAsteroids > 0:
			Game.clock.tick(30)
			self.eventHandle()
			self.update()
