import pygame, sys
from pygame.locals import *
from files.Menus import *
from files.Functions import *
from files.Variables import *
from files.marioClass import *
from files.goombClass import *
pygame.init()

def game_screen(lives):
    player = marioClass
    GoombaClass.init()
    player.init()
    goombKill = ''
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
        if goombKill != 'goombdead':
            goombKill = GoombaClass.goomba()
            if (goombKill == 'death'):
                    marioClass.looping = False
                    return 'death'
        pygame.display.flip()
        pygame.display.update()
    
        fpsClock.tick(FPS)

    return 'menu'
