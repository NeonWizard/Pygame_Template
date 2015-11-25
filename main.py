from base import *
import sys
sys.dont_write_bytecode = True

class Game(Base):
	def __init__(self, title, width, height, framerate, fullscreen):
		Base.__init__(self, title, width, height, framerate, fullscreen)

	def logic(self, keys, newkeys, buttons, newbuttons, mousepos, delta):
		pass

	def paint(self, surface):
		surface.fill((50, 50, 100))


if __name__ == "__main__":
	g = Game(config.SCREEN_TITLE, config.SCREEN_WIDTH, config.SCREEN_HEIGHT, config.FRAMERATE, config.SCREEN_FULLSCREEN)
	g.main()