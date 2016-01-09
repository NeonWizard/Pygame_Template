import sys
sys.dont_write_bytecode = True

from base import *

class Game(Base):
	def __init__(self):
		Base.__init__(self, config.SCREEN_TITLE, config.SCREEN_WIDTH, config.SCREEN_HEIGHT, config.FRAMERATE, config.SCREEN_FULLSCREEN)
		self.loadFolders(images=True)

	def logic(self, keys, newkeys, buttons, newbuttons, mousepos, lastmousepos, delta):
		pass

	def paint(self, surface):
		surface.fill((50, 50, 100))


if __name__ == "__main__":
	g = Game()
	g.main()