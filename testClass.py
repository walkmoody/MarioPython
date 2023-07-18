import pygame, sys
from pygame.locals import *
from Menus import *
from Functions import *
from Variables import *
from marioClass import *
pygame.init()

def testScreen():
    player = marioClass
    while marioClass.looping:
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        player.move(keys)
        player.jump(keys)
        player.checks(keys)
        if player.isPipe:
            player.pipe(keys)
        else:
            player.collision()
            player.death()
        WINDOW.fill(BACKGROUND)
        WINDOW.blit(bg,(0 -player.CameraX,0 -player.CameraY))
        if player.isPipe:
            WINDOW.blit(Pipes,(0 ,-152))
        WINDOW.blit(marioClass.printCharacter, (player.characterX, player.characterY))
        pygame.display.flip()
        pygame.display.update()
    
        fpsClock.tick(FPS)

    return 'menu'
