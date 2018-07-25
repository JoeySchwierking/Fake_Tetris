from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time
# this script demonstrates how to create a class structure for gaming mode
sense = SenseHat()
sense.clear()

class stack():
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((640, 480))
		self.gaming = True
		self.stop = False
		self.t = 0
#		sense.set_pixel(self.t, 7, (192, 74, 35))
#		time.sleep(.4)
#		sense.clear()
#		self.t += 1
#		if self.t > 7:
#			self.t = 0

	def startGame(self):
		pygame.time.set_timer(USEREVENT +1, 800)
		while self.gaming:
			for event in pygame.event.get():
				sense.set_pixel(self.t, 7, (192, 74, 35))
				time.sleep(.4)
				sense.clear()
				if self.stop == False:
					self.t += 1
					if self.t > 7:
						self.t = 0
				if event.type == KEYDOWN:
					self.stop = True


if __name__ == '__main__':
	try:
		game = stack()
		game.startGame()
	except KeyboardInterrupt:
		print 'an I has cheezburger?'
		sense.clear()
