from globals import *
import pygame
from pygame.locals import * 
class SPC_item:
    # The object ID
    ID = 0
    # the total size of the surface 
    frameLength = 0
    # the total size of the surface 
    frameHeight = 0
    # the image data
    imageSurface = 0
    # the surface size 
    frameSurface = 0
    # the point where the image starts to display the file 
    startDisplayFrame = 0 
    current_x = 0 
    current_y = 0
    
    #The image length and height are the total frame sizes not image sizes 
    def __init__(self,imagePath,frameLength,frameHeight):
        #setting up the ID of the item
        global itemCounter
        itemCounter = itemCounter+1
        self.ID = itemCounter
        global masterArray
        masterArray.append((0,0,0,0))
        self.frameLength = frameLength
        self.frameHeight = frameHeight
        
        self.imageSurface = pygame.image.load(imagePath)
    def getID(self):
        return self.ID
    def showFrame(self,screen,frame,posx,posy):
        self.current_y = posy
        self.current_x = posx 
        global masterArray
        masterArray[self.getID()] = (self.current_x,
                                     self.current_x+self.frameLength,
                                     self.current_y,
                                     self.current_y+self.frameHeight)

        pygame.Surface.blit(screen,self.imageSurface,(posx,posy),
                            (frame*self.frameLength,0,self.frameLength,
                             self.frameHeight))
    def getPos(self):
        return (self.current_x,self.current_y)
    def getFrameSize(self):
        return (self.frameLength,self.frameHeight)
    #checks if the item is colliding and returns the ID of the first item that it is coliding with 
    #TODO - turn this into a quad tree 
    def checkCol(self):
        elementCount = len(masterArray)
       
        while elementCount != 1:
            if masterArray[elementCount-1][1] >=self.current_x and masterArray[elementCount-1][0]<=self.current_x+self.frameLength and masterArray[elementCount-1][3] >= self.current_y and masterArray[elementCount-1][2] <= self.current_y+self.frameHeight:
                if elementCount-1 != self.ID:
                    return elementCount-1
            elementCount=elementCount-1
            if(elementCount == 0):
                return 0
            
