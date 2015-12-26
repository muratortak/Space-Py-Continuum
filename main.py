
import pygame
from pygame.locals import *
from startscreen import *
from events import *
from itemClass import *
from move import *
from globals import *

def main():

    global gx
    global gy
    #Setup
    FLOOR = 500
    pygame.init()
    window=pygame.display.set_mode([1300,640],0,24)
    pygame.display.set_caption("Space Py Continuum")
    clock=pygame.time.Clock()

    globals = vars()

    #Display welcome screen
    SPC_startscreen(window)
    #Create SPC_item 

    #player32x32.png frames 
    #0 stand 
    #1 walk right
    #2 walk left 
    #3 shoot
    #4 got hit 
    #5 jump 
    player = SPC_item("player32x32.png",32,32)
    playerFrame = 5
    playerEvents = 0
    #frame timers
    frames = 48
    walkframes = 24
    #main loop
    playerx = 0
    playery = 0
    jumpstarted = 0
    #keys 

    while True:
        
        clock.tick(24)
        
        player.showFrame(window,playerFrame,playerx,playery)
        #start and fall 
        if (player.getPos())[1]<FLOOR:
            playery=playery+5
        if (player.getPos())[1]== FLOOR and playerEvents == 0:
            playerFrame = 0
        #moving logic 
        if globals.gx == 1:
            if walkframes >=12:
                playerFrame = 1
                walkframes = walkframes -1
            if walkframes <=12:
                playerFrame = 0
                walkframes = walkframes -1
            if walkframes <= 0:
                walkframes = 24
            playerx = playerx+4
        if globals.gx == -1:
            if walkframes >=12:
                playerFrame = 2
                walkframes = walkframes-1
            if walkframes <=12:
                playerFrame = 0
                walkframes = walkframes-1
            if walkframes <=0:
                walkframes = 24
            playerx = playerx-4

        if globals.gy == 1 and jumpstarted != 1:
            jumpstarted = 1
        if jumpstarted == 1:
            playerFrame = 5
            if frames >24:
                playery = playery -10
                frames = frames -1
                print frames
            if frames <= 24:
                if frames <= 0:
                    jumpstarted = 0
                    frames = 48
            
                frames = frames -1
                print frames
               
        #main event handler
        SPC_events(globals)
        pygame.display.flip()
        window.fill((10,10,10))
main()
