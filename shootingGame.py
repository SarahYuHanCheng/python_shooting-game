import sys, pygame

from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800,600))# (800,600)is tuple
# screen is a surface
surf = pygame.Surface((50,50))
surf.fill((255,0,255))
rect = surf.get_rect()
screen.blit(surf,(400,300))
pygame.display.flip()

running = True
while running:
	for event in pygame.event.get():
		if event.type == QUIT: 
			running = False

	keys = pygame.key.get_pressed()
	if keys[K_ESCAPE]: # K_ESCAPE is in pygame.locals
		running = False

