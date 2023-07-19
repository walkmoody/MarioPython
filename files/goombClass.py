import pygame
from pygame.locals import *
from files.Menus import *
from files.Functions import *
from files.Variables import *
from files.marioClass import *
pygame.init()


class GoombaClass:

    def goomba():
        marioClass.goombXCalc =  marioClass.goombXCalc + 1 #goomba Count in order to calc x value (allows movement)
        if marioClass.goombaDeath == False and   marioClass.goombXCalc < 900:
            death = Goomba(marioClass.CameraX, marioClass.CameraY, marioClass.goombXCalc, marioClass.characterX, marioClass.characterY)
            if (death == 'jump'):
                marioClass.goombaDeath = True
                marioClass.marioJumpVelocity =  marioClass.jumpStrength
                return 'goombDead'
            if (death == 'true'):
                return 'death'
            
def Goomba(CameraX, CameraY, goombXCalc, characterX, characterY):
    goomba1 = pygame.image.load('images\Goomba1.png').convert_alpha()
    goomba1 = pygame.transform.scale(goomba1, (50, 50))
    Goomba2 = pygame.image.load('images\Goomba2.png').convert_alpha()
    Goomba2 = pygame.transform.scale(Goomba2, (50, 50))
    Goomba3 = pygame.image.load('images\Goomb3.png').convert_alpha()
    Goomba3 = pygame.transform.scale(Goomba3, (50, 50))
    GoombaPrint = goomba1
    if(goombXCalc % 15 < 5):
        GoombaPrint = Goomba2
    elif (goombXCalc % 15 < 10):
        GoombaPrint = goomba1
    elif (goombXCalc % 15 < 16):
        GoombaPrint = Goomba3
    goombaY = 575
    goombaX = -CameraX + 950 - goombXCalc
    WINDOW.blit(GoombaPrint, (goombaX, goombaY))
    if(characterX < goombaX + 15 and characterX > goombaX - 15 and characterY < goombaY - 5 and characterY > goombaY -30):
        return 'jump'
    if(characterX < goombaX + 10 and characterX > goombaX - 10 and characterY == goombaY - 5):
        trueState = True
        deathTest = characterY 
        death2 = 0
        while trueState:
            for event in pygame.event.get() :
                if event.type == QUIT :
                    pygame.quit()
                    sys.exit()
            deathTest =  deathTest - 3
            if deathTest < characterY - 50:
                deathTest = deathTest + 1
            if deathTest < characterY - 100:
                death2 = deathTest
            if death2 != 0:
                deathTest =  deathTest + 7
                if deathTest > 650:
                    trueState = False
            WINDOW.blit(bg,(0 -CameraX,0 -CameraY))  
            WINDOW.blit(goomba1, (characterX + 10 , characterY + 5)) 
            WINDOW.blit(marioDeath, (characterX, deathTest))
            pygame.display.flip()
            pygame.display.update()
        fpsClock.tick(FPS)
        return 'true'
    else:
        return 'false'    
            
    