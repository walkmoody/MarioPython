import pygame, sys
from pygame.locals import *
from Menus import *
from Functions import *
from Variables import *
from marioClass import *
pygame.init()

def testScreen():
    looping = True
    player = marioClass
    while looping:
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        marioClass.move(keys)
        WINDOW.fill(BACKGROUND)


        pygame.display.flip()
        pygame.display.update()
    
        fpsClock.tick(FPS)

    return 'menu'
