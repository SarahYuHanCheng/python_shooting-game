import sys, pygame, random
from pygame.locals import *

class Enemy(pygame.sprite.Sprite):
	"""docstring for Enemy"""
	def __init__(self):
		super(Enemy, self).__init__()
		picture = pygame.image.load('missile.jpeg').convert()
		self.surf = pygame.transform.scale(picture, (80, 80))
		self.surf.set_colorkey((255,255,255), RLEACCEL)
		self.rect = self.surf.get_rect(
			center=(random.randint(820,900), random.randint(0,600))) 
		self.speed = random.randint(5,20)

	def update(self):
			self.rect.move_ip(-self.speed,0)
			if self.rect.right<0:
				self.kill() # kill() is built-in sprite class
				
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
ADDENEMY = pygame.USEREVENT+1 # 自定義事件需要比USEREVENT大
pygame.time.set_timer(ADDENEMY, 500)

player = Player()
background = pygame.Surface(screen.get_size())
background.fill((0,0,0))
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


running = True
while running:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
		elif event.type == QUIT: 
			running = False
		elif (event.type == ADDENEMY):
			new_enemy = Enemy()
			enemies.add(new_enemy)
			all_sprites.add(new_enemy)

		screen.blit(background,(0,0))
		pressed_keys = pygame.key.get_pressed()
		player.update(pressed_keys)
		enemies.update()
		for entity in all_sprites:
			screen.blit(entity.surf, entity.rect)
		if pygame.sprite.spritecollideany(player, enemies):
			player.kill()
		pygame.display.flip()
