import pygame, sys
from pygame.locals import *

class Bullet(pygame.sprite.Sprite):
	bulletImage = pygame.image.load("Sprites/bullet.png")
	speed = 40
	def __init__(self,surface,startPos,targetHeight):
		pygame.sprite.Sprite.__init__(self)

		self.surface = surface
		self.target = targetHeight
		self.rect = Bullet.bulletImage.get_rect()
		self.rect.center = startPos

	def update(self):
		self.rect.y -= Bullet.speed
		if self.rect.y <= self.target:
			self.kill()

		self.surface.blit(Bullet.bulletImage,(self.rect.center))

		#debug option draw hitbox
		#pygame.draw.rect(self.surface,(0,255,0),self.rect,1)