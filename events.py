import pygame
from globals import *
from pygame.locals import *
def SPC_events(globals):

    for event in pygame.event.get():
        #quit event
        if event.type == QUIT:
            exit()
            #keyboard events
        if event.type == pygame.KEYDOWN:
            #move keys
            if event.key == pygame.K_a:
               globals.gx = globals.gx-1
               
            if event.key == pygame.K_d:
                globals.gx = globals.gx+1
             
            if event.key == pygame.K_w:
                globals.gy = globals.gy+1
             
            if event.key == pygame.K_s:
                globals.gy = globals.gy-1
               
               #ETC
            if event.key == pygame.K_SPACE:
                globals.spacek = globals.spacek+1
              
            if event.key == pygame.K_b:
                globals.buildk = globals.buildk+1
               
            if event.key == pygame.K_g:
                globals.g = globals.g+1
               
        if event.type == pygame.KEYUP:
               #move keys
            if event.key == pygame.K_a:
                globals.gx = globals.gx+1
              
            if event.key == pygame.K_d:
                globals.gx = globals.gx-1
              
            if event.key == pygame.K_w:
                globals.gy = globals.gy-1
               
            if event.key == pygame.K_s:
                globals.gy = globals.gy+1
               
               #ETC
            if event.key == pygame.K_SPACE:
                globals.space = globals.space-1
               
            if event.key == pygame.K_b:
                globals.buildk = globals.buildk-1
               
            if event.key == pygame.K_g:
                globals.g = globals.g-1
                  
        
                
