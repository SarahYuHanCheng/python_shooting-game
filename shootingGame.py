import sys, pygame

from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800,600))# (800,600)is tuple

running = True
while running:
	for event in pygame.event.get():
		if event.type == QUIT: # KEYDOWN is in pygame.locals
			running = False

	keys = pygame.key.get_pressed()
	if keys[K_ESCAPE]:
		running = False
