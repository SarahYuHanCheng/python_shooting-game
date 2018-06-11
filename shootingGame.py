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

	def update(self, pressed_k):
		
		if pressed_k[K_UP]:
			self.rect.move_ip(0,-5)
			print("K_UP")
		if pressed_k[K_DOWN]:
			self.rect.move_ip(0,5)
			print("K_DOWN")
		if pressed_keys[K_LEFT]:
			self.rect.move_ip(-5, 0)
		if pressed_keys[K_RIGHT]:
			self.rect.move_ip(5, 0)
		if self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > 800:
			self.rect.right = 800
		if self.rect.top <= 0:
			self.rect.top = 0
		elif self.rect.bottom >= 600:
			self.rect.bottom = 600

pygame.init()

screen = pygame.display.set_mode((800,600))# (800,600)is tuple
# screen is a surface

player = Player()

running = True
while running:
	for event in pygame.event.get():
		if event.type == QUIT: 
			running = False
		pressed_keys = pygame.key.get_pressed()
		if pressed_keys[K_ESCAPE]: # K_ESCAPE is in pygame.locals
			running = False
		player.update(pressed_keys)
		screen.blit(player.surf,player.rect)# (400,300)no move
		pygame.display.flip()
