import pygame
from pygame.locals import *
def SPC_startscreen(window):
    window.fill((0,0,0))
    splashscreen = pygame.image.load("startscreen.png")
    window.blit(splashscreen,(0,0))
    pygame.display.flip()
    pygame.time.delay(1000)
