import pygame, sys, random, time, math
from pygame.locals import *
pygame.init()

fontsList = pygame.font.get_fonts()
   
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 720

#global variables for screens
characterX = 0
characterY = 0
bg = pygame.image.load('images\SMB_NES_World_1-1_Map.png')
bg = pygame.transform.scale(bg, (10100, 720))
opening = pygame.image.load("images\Loadupscreen.png")
opening = pygame.transform.scale(opening, (1500, 750))
SuperMarioBros = pygame.image.load("images\SUPERMARIOBROS.jpg")
SuperMarioBros = pygame.transform.scale(SuperMarioBros, (512, 240))
MainMenuTrue = pygame.image.load("images\MainMenuTrue.png")
MainMenuTrue = pygame.transform.scale(MainMenuTrue, (1000, 1000))
DeathScreen = pygame.image.load("images/MARIODEATHSCREEN.png")
DeathScreen = pygame.transform.scale(DeathScreen, (1000, 900))
Pipes = pygame.image.load("images/PIPES.png")
Pipes = pygame.transform.scale(Pipes, (1170, 900))

#Color declarations and set ups
BACKGROUND = (205, 215, 220) # make a random color that changes
OPENINGBACKGROUND = (255, 255, 255)
TEXTCOLOUR = (200, 100, 0)
BLACKGROUND = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 30, 70)
BLUE = (10, 20, 200)
GREEN = (50, 230, 40)
CHARACTER = (255, 30, 70) # Change color rn it is red
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
TEXTCOLOUR = (0, 0, 0)

#Mario Sprite list
mario = pygame.image.load('images\mario.png').convert_alpha()
mario = pygame.transform.scale(mario, (55, 55))
marioRun1   = pygame.image.load('images\MarioRun1.png').convert_alpha()
marioRun1 = pygame.transform.scale(marioRun1, (60, 60))
middleRun = pygame.image.load('images\MarioRun2.png').convert_alpha()
middleRun = pygame.transform.scale(middleRun, (55, 55))
marioRun3 = pygame.image.load('images\MarioRun3.png').convert_alpha()
marioRun3 = pygame.transform.scale(marioRun3, (60, 60))
marioJump = pygame.image.load('images\Jump.png').convert_alpha()
marioJump = pygame.transform.scale(marioJump, (55, 55))
marioJumpLeft = pygame.transform.flip(marioJump, True, False)
marioDeath = pygame.image.load('images\marioDeath.png').convert_alpha()
marioDeath = pygame.transform.scale(marioDeath, (55, 55))


#WINDOW.fill(BACKGROUND)
pygame.display.set_caption('Mario')

fontObj = pygame.font.Font(None, 32)
fontObj = pygame.font.SysFont('courier', 32)

def splash_screen():
   WINDOW.fill(OPENINGBACKGROUND)
   WINDOW.blit(opening,(-250,0))
   pygame.display.update()
   time.sleep(2)
 
   return 'menu'

def menu_screen ():
  looping = True
  action = 'game'
  font = pygame.font.Font('freesansbold.ttf', 32)

  menuItem1 = font.render('Instructions - i', True, TEXTCOLOUR)
  menuItem2 = font.render('Play Game - p or SPACE', True, TEXTCOLOUR)
  menuItem3 = font.render('Quit - q', True, TEXTCOLOUR)
 
  menuItem1Rect = menuItem1.get_rect()
  menuItem2Rect = menuItem2.get_rect()
  menuItem3Rect = menuItem3.get_rect()
 
  menuItem1Rect.topleft = (WINDOW_WIDTH/4, 350)
  menuItem2Rect.topleft = (WINDOW_WIDTH/4, 400)
  menuItem3Rect.topleft = (WINDOW_WIDTH/4, 450)
 
 
  while looping :
    # Get inputs
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
 
    pressed = pygame.key.get_pressed()
    if pressed[K_i] :
        action = 'instructions'
        looping = False
    elif pressed[K_SPACE] or pressed[K_p] :
        action = 'game'
        looping = False
    elif pressed[K_q] :
        action = 'bye'
        looping = False
 
    # render the screen
    WINDOW.fill(BACKGROUND)
    WINDOW.blit(bg, (0,0))
    WINDOW.blit(menuItem1, menuItem1Rect)
    WINDOW.blit(menuItem2, menuItem2Rect)
    WINDOW.blit(menuItem3, menuItem3Rect)
    WINDOW.blit(SuperMarioBros, (WINDOW_WIDTH/4,47))
    
    pygame.display.update()
    fpsClock.tick(FPS)
  return action

def Pause():
  looping = True

  while looping:
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
    keys = pygame.key.get_pressed()
    print("test")
    if(keys[K_w]):
       return
    WINDOW.blit(BACKGROUND)
    
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
    "pipe1" : [1230, 145],
    "pipe2" : [1680, 192],
    "pipe3" : [2030, 245],
    "pipe4" : [2530, 245],
    "pipe5" : [7320, 145],
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
  

def game_screen(lives): 
  #allows game to run
  looping = True
  #character spawn location
  characterX = 0
  characterY = 570
  #Jump Strength
  marioJumpVelocity = -23
  jumpStrength = 22
  #Camera
  CameraX, CameraY= 0, 0
  #allows for mario Run animation
  printCharacter = mario
  count, countLeft = 0, 0
  #Goomba
  goombXCalc = 0
  goombaDeath = False
  #add lives to screen
  isGround = True
  right = True
  collisionDict = Collision()
  deathDict = Holes()
  goalX = 8900 # 8850
  isPipe = False
  while looping :
    # Checks for orientation of player
    if(right == True):
      printCharacter = mario
    else:
      printCharacter = pygame.transform.flip(mario, True, False)
    #allows the player to exit
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed() # gets key value
    #hot key to leave the game
    if (keys[K_q]):
      return 'quit'
    #FIXME PAUSE SCREEN
    if (keys[K_p]):
      looping = False
      Pause()
      looping = True
      print('pause')
    #mario speed and camera speed need to be different
    marioSpeed = 1
    cameraSpeed = 8
    #MOVEMENT
    if (keys[K_RIGHT] or keys[K_d]):
        right = True
        characterX = characterX + marioSpeed
        printCharacter = mario
        CameraX += cameraSpeed
        count += 1
        if CameraX > 8380 or isPipe:
          characterX = characterX - marioSpeed + cameraSpeed
        if CameraX > 8380:
          CameraX = CameraX - cameraSpeed
        if (count < 5):
          printCharacter = marioRun1
        elif( count < 10):
          printCharacter = middleRun
        elif ( count < 15):
          printCharacter = marioRun3
        else: 
          printCharacter = marioRun3
          count = 0
        if(keys[K_LSHIFT]):
            characterX = characterX + (marioSpeed * 2)
            CameraX += cameraSpeed + 4

    if (keys[K_LEFT] or keys[K_a]) :
        right = False
        characterX = characterX - marioSpeed
        printCharacter = pygame.transform.flip(mario, True, False)
        if (characterX < WINDOW_WIDTH/5):
          CameraX -= cameraSpeed 
        else:
          characterX = characterX + marioSpeed - cameraSpeed
        if isPipe == True:
          characterX = characterX - cameraSpeed + marioSpeed + marioSpeed
        countLeft += 1
        if (countLeft < 5):
          printCharacter = pygame.transform.flip(marioRun1, True, False)
        elif( countLeft < 10):
            printCharacter = pygame.transform.flip(middleRun, True, False)
        elif ( countLeft < 15):
          printCharacter = pygame.transform.flip(marioRun3, True, False)
        else: 
          countLeft = 0
        if(keys[K_LSHIFT]):
            characterX = characterX - (marioSpeed * 2)
            CameraX -= cameraSpeed - 4

    if (characterX  < -4 and isPipe == False) : # stops mario from going to the left off screeb
        characterX = characterX + marioSpeed
    if (CameraX < 0 and isPipe == False) :
      CameraX = CameraX + cameraSpeed
    if (characterX  > WINDOW_WIDTH/5 and CameraX < 8375 and not isPipe): # Stops mario from running off screen right
        characterX = characterX - marioSpeed
        if(keys[K_LSHIFT]):
          characterX = characterX - (marioSpeed * 2)
    if(characterX > WINDOW_WIDTH) :
          characterX = characterX - marioSpeed
          if(keys[K_LSHIFT]):
            characterX = characterX - (marioSpeed * 2)    
    if (keys[K_SPACE] and marioJumpVelocity < -jumpStrength) :
        marioJumpVelocity = jumpStrength
    if marioJumpVelocity >= -jumpStrength :
        characterY = characterY - marioJumpVelocity
        marioJumpVelocity = marioJumpVelocity - 1
        if (keys[K_LEFT] or keys[K_a]) :
          printCharacter = marioJumpLeft
        else:
          printCharacter = marioJump
    elif (characterY < 570 and isGround == True):
      characterY = characterY - marioJumpVelocity
    if characterY > 570:
         characterY = 570

    #Animation Test (or hidden Feature: emote)
    if (keys[K_m]):
        printCharacter = marioRun1
    if (keys[K_n]):
        printCharacter = middleRun
    if (keys[K_o]):
      printCharacter = marioRun3
    
    #Prints the backgounrd and character sprte


    #Collision loop checks for pipe collison
    for x,y, in collisionDict.items():
      pipe1X = y[0] - CameraX
      pipe1Y = 600
      pipe1H = y[1]
      if(characterX < pipe1X + 15 and characterX > pipe1X - 15 and characterY < pipe1Y and characterY > pipe1Y - pipe1H and (keys[K_RIGHT] or keys[K_d])):
        characterX = characterX - marioSpeed
        CameraX = CameraX - cameraSpeed
      elif(characterX < pipe1X + 95 and characterX > pipe1X - 14):
        isGround = False
        if(characterY == pipe1Y - pipe1H):
          marioJumpVelocity = -23
        if not (keys[K_SPACE] ) and characterY > pipe1Y - pipe1H:
          characterY = pipe1Y - pipe1H
      else:
        isGround = True
      if(characterX < pipe1X + 15 + 100  and characterX > pipe1X - 15 + 100 and characterY < pipe1Y and characterY > pipe1Y - pipe1H and (keys[K_LEFT] or keys[K_a]) ):
        characterX = characterX + marioSpeed
        CameraX = CameraX + cameraSpeed

    if(characterX < 2530 -CameraX + 95 and characterX > 2530 -CameraX - 14):
      if characterY > 250:
        if(keys[K_DOWN]):
          isPipe = True
          CameraX = -1000
          characterX = 60
          characterY = 0
    if isPipe == True:
      CameraX = -1000
      if characterX < 40:
        characterX = characterX + cameraSpeed
    #Calculations for holes
    for x,y in deathDict.items():
      holeX = y[0] - CameraX
      holeEnd = y[0] + 100  - CameraX
      if(characterX > holeX and characterX < holeEnd and characterY > 569):
        looping = False
        HoleTouch(characterX, characterY, CameraX, CameraY)
        return 'death'
    
 

    #Win condition
    if characterX > goalX - CameraX:
      looping = False
      flagpole(characterY, characterX, CameraX, CameraY)
      return 'menu'
    
    WINDOW.fill(BACKGROUND)
    WINDOW.blit(bg,(0 -CameraX,0 -CameraY))
    if isPipe:
      WINDOW.blit(Pipes,(0 ,-152))
    WINDOW.blit(printCharacter, (characterX, characterY))
    #NEEDS TO BE AFTER BLIT
    #all goomba calculations including death and jump 
    goombXCalc = goombXCalc + 1 #goomba Count in order to calc x value (allows movement)

    if goombaDeath == False and  goombXCalc < 900:
      death = Goomba(CameraX, CameraY, goombXCalc, characterX, characterY)
      if (death == 'jump'):
        goombaDeath = True
        marioJumpVelocity = jumpStrength
      if (death == 'true'):
        return 'death'
    #need to be last 2 lines
    #updates the screen
    pygame.display.flip()
    pygame.display.update()
    
    fpsClock.tick(FPS)

  return 'menu'

def game_over_screen ():
  #shows game over and takes you to the menu
  action = 'menu'
  font = pygame.font.Font('freesansbold.ttf', 32)
  fontTitle = pygame.font.Font('freesansbold.ttf', 64)
 
  title = fontTitle.render('GAME OVER!', True, RED)
  
  titleRect = title.get_rect()

  titleRect.center = (WINDOW_WIDTH // 2, 100)
 
 
  WINDOW.fill(BLACKGROUND)
  WINDOW.blit(title, titleRect)
  pygame.display.update()
  time.sleep(2)
 
  return action

def instructions_screen () : #FIXME need to change the instruction screen
  looping = True
  action = 'game'
  font = pygame.font.Font('freesansbold.ttf', 32)
  fontTitle = pygame.font.Font('freesansbold.ttf', 64)
 
  title = fontTitle.render('Mario!', True, TEXTCOLOUR)
  menuItem1 = font.render('Instructions', True, TEXTCOLOUR)
  menuItem2 = font.render('press q to quit mid game, space to jump, w and d or arrows to move', True, TEXTCOLOUR)
  menuItem3 = font.render('Back - b, Play game - g or SPACE', True, TEXTCOLOUR)
 
  titleRect = title.get_rect()
  menuItem1Rect = menuItem1.get_rect()
  menuItem2Rect = menuItem2.get_rect()
  menuItem3Rect = menuItem3.get_rect()
 
  titleRect.center = (WINDOW_WIDTH // 2, 100)
  menuItem1Rect.topleft = (200, 200)
  menuItem2Rect.topleft = (200, 300)
  menuItem3Rect.topleft = (200, 400)
 
 
  while looping :
    # Get inputs
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
 
    pressed = pygame.key.get_pressed()
    if pressed[K_b] :
      action = 'menu'
      looping = False
    elif pressed[K_SPACE] or pressed[K_p] :
      action = 'game'
      looping = False
 
    # render the screen
    WINDOW.fill(BACKGROUND)
    WINDOW.blit(title, titleRect)
    WINDOW.blit(menuItem1, menuItem1Rect)
    WINDOW.blit(menuItem2, menuItem2Rect)
    WINDOW.blit(menuItem3, menuItem3Rect)
    pygame.display.update()
    fpsClock.tick(FPS)
 
  return action

def goodbye_screen(): #shows up when player quits the game, this leaves a message and exits
  font = pygame.font.Font('freesansbold.ttf', 32)
  text = font.render('MARIO!', True, TEXTCOLOUR)
  goodbyeText = font.render('Play again soon...', True, TEXTCOLOUR)
 
  textRect = text.get_rect()
  goodbyeTextRect = goodbyeText.get_rect()
 
  textRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 50)
  goodbyeTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 50)
 
  WINDOW.fill(BACKGROUND)
  WINDOW.blit(text, textRect)
  WINDOW.blit(goodbyeText, goodbyeTextRect)
  pygame.display.update()
  time.sleep(2)
 
  pygame.quit()
  sys.exit()
 

# The main function that controls the game
def main () :
  looping = True

  screen = 'splash'
  winner = '' #not sure if I want to implemnet 
  lives = 4 #Change if need more lives

  while looping :
    # Get inputs
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
    if screen == 'splash' :
      screen = splash_screen()
    elif screen == 'menu' :
      screen = menu_screen()
      lives = 4
    elif screen == 'game' or screen == 'death':
      while(screen == 'game' or screen == 'death'):
        if screen == 'game':
          screen = game_screen(lives)
        lives -= 1
        if screen == 'death':
           screen = death(lives)
    elif screen == 'game_over' :
      screen = game_over_screen()
    elif screen == 'instructions' :
      screen = instructions_screen() 
    else :
      screen = goodbye_screen()

 
main()