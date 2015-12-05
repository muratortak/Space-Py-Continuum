#Setup
import pygame
from pygame.locals import *
from startscreen import *
from events import *
pygame.init()
window=pygame.display.set_mode([1300,640],0,24)
pygame.display.set_caption("Space Py Continuum")
clock=pygame.time.Clock()

#Display welcome screen
SPC_startscreen(window)
#main loop
while True:
    clock.tick(60)
    #main event handler
    SPC_events()


    window.fill((10,10,10))
    pygame.display.flip()