from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time
# this script demonstrates how to create a class structure for gaming mode
sense = SenseHat()
sense.clear()

t = 0
while True:
	sense.set_pixel(t, 7, (192, 74, 35))
	time.sleep(.4)
	sense.clear()
	t += 1
	if t > 7:
		t = 0
#class stack():
#	def __init__(self):
#		pygame.init()
#		pygame.display.set_mode((640, 480))
#		self.gaming = True
#
#	def startGame(self):
#		pygame.time.set_timer(USEREVENT +1, 800)
#		while self.gaming:
#			for event in pygame.event.get():
#				t = 0
#				while True:
#					sense.set_pixel(t, 7, (0, 0, 255))
#					sense.clear()
#					t += 1
#					time.sleep(1)
#					if t > 7:
#						t = 0
#
#if __name__ == '__main__':
#	try:
#		game = stack()
#		game.startGame()
#	except KeyboardInterrupt:
#		print 'an I has cheezburger?'
#		sense.clear()
