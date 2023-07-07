import pygame, sys, time
from pygame.locals import *
from Variables import *
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
    
def death(lives):
  if lives < 0:
    return 'game_over'
  font = pygame.font.Font('freesansbold.ttf', 40)

  text = font.render(f'{lives}', True, WHITE)

  textRect = text.get_rect()
  textRect.center = ((WINDOW_WIDTH / 2) + 50, (WINDOW_HEIGHT // 2) + 70)
  blackRectangle = pygame.Rect((WINDOW_WIDTH / 2) + 50, (WINDOW_HEIGHT // 2) + 40 , 50, 70)

 
  WINDOW.fill(BLACKGROUND)
  WINDOW.blit(DeathScreen, (0,0))
  pygame.draw.rect(WINDOW, BLACKGROUND, blackRectangle)
  WINDOW.blit(text, textRect)
  
  pygame.display.update()
  time.sleep(2) 

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
  
