import pygame, sys
sys.dont_write_bytecode = True
from pygame.locals import *

import config

pygame.init()

class Base:
	def __init__(self, title, width, height, framerate, fullscreen):
		if not fullscreen:
			self.window = pygame.display.set_mode((width, height))
		else:
			self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
			config.SCREEN_WIDTH, config.SCREEN_HEIGHT = self.window.get_size()
			
		pygame.display.set_caption(title)

		self.clock = pygame.time.Clock()
		self.framerate = framerate

	def logic(self, keys, newkeys, buttons, newbuttons, mousepos, delta):
		raise NotImplementedError()

	def paint(self, surface):
		raise NotImplementedError()

	def main(self):
		keys = set()
		buttons = set()
		mousepos = (1, 1)

		while True:
			self.clock.tick(self.framerate)
			delta = float(self.clock.get_time()) / float(self.framerate)

			newkeys = set()
			newbuttons = set()

			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
					pygame.quit()
					sys.exit()
					return

				if event.type == MOUSEBUTTONDOWN:
					buttons.add(event.button)
					newbuttons.add(event.button)
					mousepos = event.pos
				if event.type == MOUSEBUTTONUP:
					buttons.discard(event.button)
					mousepos = event.pos

				if event.type == MOUSEMOTION:
					mousepos = event.pos

				if event.type == KEYDOWN:
					keys.add(event.key)
					newkeys.add(event.key)
				if event.type == KEYUP:
					keys.discard(event.key)

			self.logic(keys, newkeys, buttons, newbuttons, mousepos, delta)
			self.paint(self.window)

			pygame.display.update()