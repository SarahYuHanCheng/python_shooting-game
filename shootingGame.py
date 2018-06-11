import sys, pygame

from pygame.locals import *

class Player(pygame.sprite.Sprite):
	"""docstring for Player"""
	def __init__(self):
		super(Player, self).__init__()
		self.surf = pygame.Surface((75,25))
		self.surf.fill((255,255,255))
		self.rect = self.surf.get_rect()
# 我們畫在屏幕上的surface現在成了player的一個屬性

pygame.init()

screen = pygame.display.set_mode((800,600))# (800,600)is tuple
# screen is a surface

player = Player()

surf = pygame.Surface((50,50))
surf.fill((255,0,255))
rect = surf.get_rect()
screen.blit(surf,(400,300))
screen.blit(player.surf,(300,300))
pygame.display.flip()


running = True
while running:
	for event in pygame.event.get():
		if event.type == QUIT: 
			running = False

	keys = pygame.key.get_pressed()
	if keys[K_ESCAPE]: # K_ESCAPE is in pygame.locals
		running = False

