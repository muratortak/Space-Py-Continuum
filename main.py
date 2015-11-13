
#Setup
import pygame
from pygame.locals import *
from startscreen import *
pygame.init()
window=pygame.display.set_mode([1300,640],0,24)
pygame.display.set_caption("Space Py Continuum")
clock=pygame.time.Clock()

#Display welcome screen
StartScreen(window)
