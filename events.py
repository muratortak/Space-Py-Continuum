import pygame
from globals import *
from pygame.locals import *
def SPC_events():
        global gy
        global gx
        global gz
	for event in pygame.event.get():
		   #quit event
     	   if event.type == QUIT:
        	    exit()
           #keyboard events
           if event.type == pygame.KEYDOWN:
               #move keys
               if event.key == pygame.K_a:
                   gx = gx-1
                   print gx
               if event.key == pygame.K_d:
                   gx = gx+1
                   print gx
               if event.key == pygame.K_w:
                   gy = gy+1
                   print gy
               if event.key == pygame.K_s:
                   gy = gy-1
                   print gy
               #ETC
               if event.key == pygame.K_SPACE:
                   print('space')
               if event.key == pygame.K_b:
                   print('build')
               if event.key == pygame.K_g:
                   print('key g')
  	    
