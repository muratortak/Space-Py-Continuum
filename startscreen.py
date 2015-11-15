import pygame
from pygame.locals import *
def SPC_startscreen(window):
	font=pygame.font.SysFont('arial',120)
	window.fill((0,0,0))
	window.blit(font.render("Space Py Continuum",True,(0,255,0)),(100,200))
	pygame.display.flip()
