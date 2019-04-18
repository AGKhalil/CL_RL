import pygame

class Player:

	def __init__(self, screen, x, y):

		self.screen = screen

		self.x = x
		self.y = y
		self.width = 24
		self.height = 24

		self.left = False
		self.right = False

		self.walkRight = pygame.image.load('BD_sprites/DudeRight.png')
		self.walkLeft = pygame.image.load('BD_sprites/DudeLeft.png')
		self.door = pygame.image.load('BD_sprites/Door.png')
		self.block = pygame.image.load('BD_sprites/Block.png')
		self.brick = pygame.image.load('BD_sprites/Brick.png')

	def draw(self):
		if self.right:
			self.screen.blit(self.walkRight, (self.x[0], self.y[0]))
		else:
			self.screen.blit(self.walkLeft, (self.x[0], self.y[0]))

	def set_direction(self, direction):
		if direction == 'LEFT':
			self.left = True
			self.right = False
		else:
			self.left = False
			self.right = True

	def get_direction(self):
		if self.left == True and self.right == False:
			return 'LEFT'
		else:
			return 'RIGHT'