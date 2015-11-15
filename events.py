import pygame
from pygame.locals import *
def SPC_events():
	for event in pygame.event.get():
		   #quit event
     	   if event.type == QUIT:
        	    exit()
           #keyboard events
           if event.type == pygame.KEYDOWN:
               #move keys
               if event.key == pygame.K_a:
                   print('left')
               if event.key == pygame.K_d:
                   print('right')
               if event.key == pygame.K_w:
                   print('forward')
               if event.key == pygame.K_s:
                   print('backwards')
                   
               #ETC
               if event.key == pygame.K_SPACE:
                   print('space')
               if event.key == pygame.K_b:
                   print('build')
  	    
