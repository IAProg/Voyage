import pygame, sys
from pygame.locals import *
from random import randint, randrange

import startScreen, numberScreen, Voyage, endScreen

def game():
	pygame.init()
	pygame.font.init()

	pygame.display.set_caption('Voyage!')
	surface = pygame.display.set_mode((400,700))

	screen1 = startScreen.StartScreen(surface)
	screen2 = numberScreen.NumberScreen(surface)

	requiredNumbers = screen2.getNumbers()
	placedBet = screen1.getBet()

	screen3 = Voyage.Game(surface, requiredNumbers)

	numbersFound = screen3.getNumbers()

	screen4 = endScreen.EndScreen(surface, numbersFound, requiredNumbers, placedBet)

	if screen4.replay:
		game()
	else:
		quit()

if __name__ == "__main__":
	game()
