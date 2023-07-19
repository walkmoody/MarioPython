import pygame, sys, time
from pygame.locals import *
from files.Variables import *
pygame.init()

def Pause():
  looping = True
  font = pygame.font.Font('freesansbold.ttf', 40)

  menuItem1 = font.render('PAUSED PRESS W TO CONTINUE', True, WHITE)
  menuItem1Rect = menuItem1.get_rect()
  menuItem1Rect.topleft = (WINDOW_WIDTH/6, 350)

  while looping:
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
    keys = pygame.key.get_pressed()
    
    if(keys[K_w]):
       return
    WINDOW.blit(menuItem1, menuItem1Rect)

    pygame.display.update()
    
    fpsClock.tick(FPS)
  return 'game'

def Collision():
  Dict = {
    "pipe1" : [1230, 125],
    "pipe2" : [1680, 172],
    "pipe3" : [2030, 225],
    "pipe4" : [2530, 225],
    "pipe5" : [7320, 125],
    "pipe6" : [8040, 128]
  }

  return Dict

def Holes():
  Dict = {
      'hole1' : [3100],
      'hole2' : [3870],
      'hole3' : [6870]
  }

  return Dict

def HoleTouch(characterX, characterY, CameraX, CameraY):
  trueState = True
  deathTest = characterY 
  mult = 1
  while trueState:
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
    mult = (mult * mult)
    deathTest =  deathTest + 6 + mult
    characterX = characterX + 1
    if deathTest > 820:
      trueState = False
    WINDOW.blit(bg,(0 -CameraX,0 -CameraY))  
    WINDOW.blit(marioJump, (characterX, deathTest))
    pygame.display.flip()
    pygame.display.update()
    fpsClock.tick(FPS)
  return 'death'


def flagpole(characterY, characterX, CameraX, CameraY):
  print('win')
  trueState = True
  poleY = characterY
  marioFinish = characterX
  marioPrint = mario
  count = -1
  countX = 0
  poleRight = False
  while trueState:
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
    if poleY < 510 and poleRight == False:
      poleY += 5
    elif count == -1:
      poleY = 520
      count = count + 1
      poleRight = True
    else:
      if marioFinish < 1000:
        if count < 100:
          if marioFinish < 560:
            marioFinish = 560
          marioPrint = pygame.transform.flip(mario, True, False)
          count += 3
        else:
          marioFinish += 7
          if poleY < 570:
            poleY = poleY + 3
            marioPrint = marioJump
            #print(marioFinish)
            print(poleY)
          else:
            countX += 1
            poleY = 570
            if (countX < 5):
              marioPrint = marioRun1
            elif ( countX < 10):
                marioPrint = middleRun
            elif ( countX < 15):
              marioPrint = marioRun3
            else: 
              countX = 0
      else:
        trueState = False
    WINDOW.blit(bg,(0 -CameraX,0 -CameraY))  
    WINDOW.blit(marioPrint, (marioFinish, poleY))
    pygame.display.flip()
    pygame.display.update()
    fpsClock.tick(FPS)
  return 'menu'


  
