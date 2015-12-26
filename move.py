from  globals import *
playerx = 0
playery = 0 
frame = 0 

def opening():
    return 0



def movingx():
    global gx # left == -1 right == +1
    global gy # up == 1 down == -1
    global spacek # on == 1
    global g # on == 1
    #controllers 
    global playerx
    global playery
    global frame
    
    if gx == -1:
        if playerx!=0:
            playerx-1
            return playerx
    if gx == 1:
        if playerx !=1300:
            playerx+1
            return playerx
    return 0
    
def movingy():
    global gx # left == -1 right == +1
    global gy # up == 1 down == -1
    global spacek # on == 1
    global g # on == 1
    #controllers 
    global playerx
    global playery
    global frame
    
    if gy == 1 and frame != 0:
        frame = 24
    if frame > 12:
        playery = playery-1
        return playery
        frame = frame -1
    if frame <= 12 and frame !=0 :
        playery = playery+1
        frame = frame -1
        return playery
    return 0
