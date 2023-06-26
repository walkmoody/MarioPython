import pygame, sys, random, time, math
from pygame.locals import *
pygame.init()

fontsList = pygame.font.get_fonts()
 
# Colours
#def BackgroundGenerator()
    

BACKGROUND = (205, 215, 220) # make a random color that changes
TEXTCOLOUR = (200, 100, 0)
BLACKGROUND = (0,0,0)
GAMEBACKGROUND = ('SMB_NES_World_1-1_Map.png')
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 720

bg = pygame.image.load("SMB_NES_World_1-1_Map.png")
bg = pygame.transform.scale(bg, (10100, 720))


RED = (255, 30, 70)
BLUE = (10, 20, 200)
GREEN = (50, 230, 40)
CHARACTER = (255, 30, 70) # Change color rn it is red
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
TEXTCOLOUR = (0, 0, 0)


#WINDOW.fill(BACKGROUND)
pygame.display.set_caption('Mario')

fontObj = pygame.font.Font(None, 32)
fontObj = pygame.font.SysFont('courier', 32)
textSufaceObj = fontObj.render('Grant Sucks', True, TEXTCOLOUR, None)

def splash_screen():
   font = pygame.font.Font('freesansbold.ttf', 32)
   text = font.render('ITS FUCKING MAMAMAMARIO!', True, TEXTCOLOUR)
 
   textRect = text.get_rect()
 
   textRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
 
   WINDOW.fill(BACKGROUND)
   WINDOW.blit(text, textRect)
   pygame.display.update()
   time.sleep(1)
 
   return 'menu'

def menu_screen ():
  looping = True
  action = 'game'
  font = pygame.font.Font('freesansbold.ttf', 32)
  fontTitle = pygame.font.Font('freesansbold.ttf', 64)
 
  title = fontTitle.render('FUCK MARIO!', True, TEXTCOLOUR)
  menuItem1 = font.render('Instructions - i', True, TEXTCOLOUR)
  menuItem2 = font.render('Play Game - p or SPACE', True, TEXTCOLOUR)
  menuItem3 = font.render('Quit - q', True, TEXTCOLOUR)
 
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
    WINDOW.blit(title, titleRect)
    WINDOW.blit(menuItem1, menuItem1Rect)
    WINDOW.blit(menuItem2, menuItem2Rect)
    WINDOW.blit(menuItem3, menuItem3Rect)
    pygame.display.update()
    fpsClock.tick(FPS)
  return action



def Block(characterX, characterY, CameraX):
  blockX =  -CameraX + 50
  blockY = 400
  blockHeight = 50
  blockWidth = 50
  block = pygame.image.load('Block.png').convert_alpha()
  block = pygame.transform.scale(block, (50, 50))
  if (characterY < blockHeight + blockY and characterX < blockWidth + blockX):
    characterY = characterY - 20
  WINDOW.blit(block, (blockX, blockY))
# ComeBACK

  

def game_screen (): 
  looping = True
  mario = pygame.image.load('mario.png').convert_alpha()
  mario = pygame.transform.scale(mario, (55, 55))
  characterX = 0
  characterY = 570
  marioLeft = pygame.transform.flip(mario, True, False)
  marioJump = pygame.image.load('Jump.png').convert_alpha()
  marioJump = pygame.transform.scale(marioJump, (55, 55))
  marioJumpLeft = pygame.transform.flip(marioJump, True, False)
  marioRunning = mario # this line initialises the variable
  marioRun1   = pygame.image.load('MarioRun1.png').convert_alpha()
  marioRun1 = pygame.transform.scale(marioRun1, (60, 60))
  middleRun = pygame.image.load('MarioRun2.png').convert_alpha()
  middleRun = pygame.transform.scale(middleRun, (55, 55))
  marioRun3 = pygame.image.load('MarioRun3.png').convert_alpha()
  marioRun3 = pygame.transform.scale(marioRun3, (60, 60))
  marioJumpVelocity = -21
  jumpStrength = 20
  x,y = 0, 0
  CameraX = x
  CameraY= y
  bif = bg
  #Block
  block = pygame.image.load('Block.png').convert_alpha()
  block = pygame.transform.scale(block, (70, 70))
  count = 0
  printCharacter = marioRunning


  
  while looping :
    # Get inputs

        printCharacter = marioRunning
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed() # gets key value
        marioSpeed = 1
        cameraSpeed = 8
        if (keys[K_RIGHT] or keys[K_d]):
            
            characterX = characterX + marioSpeed
            marioRunning = mario
            CameraX += cameraSpeed
            count += 1
            if (count < 5):
              printCharacter = marioRun1
            else:
              if ( count < 10):
                printCharacter = middleRun
              else:
                if ( count < 15):
                  printCharacter = marioRun3
                else: 
                  count = 0
            
            if(keys[K_LSHIFT]):
               characterX = characterX + (marioSpeed * 2)
               CameraX += cameraSpeed + 4
        if (keys[K_LEFT] or keys[K_a]) :
            characterX = characterX - marioSpeed
            marioRunning = marioLeft
            CameraX -= cameraSpeed 
            if(keys[K_LSHIFT]):
               characterX = characterX - (marioSpeed * 2)
               CameraX -= cameraSpeed - 4
        if (characterX  < -4) :
            characterX = characterX + marioSpeed
        if (CameraX < 0) :
          CameraX = CameraX + cameraSpeed

        if (characterX  > WINDOW_WIDTH/5) :
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


      

        if (keys[K_m]):
           printCharacter = marioRun1

        if (keys[K_n]):
           printCharacter = middleRun
        
        if (keys[K_o]):
          printCharacter = marioRun3


       
        WINDOW.fill(BACKGROUND)
        WINDOW.blit(bg,(0,0))
    
  
        
        WINDOW.blit(bif,(0 -CameraX,0 -CameraY))
        #WINDOW.blit(mario,(x -CameraX,y -CameraY))
        WINDOW.blit(printCharacter, (characterX, characterY) )
        #WINDOW.blit(textSufaceObj, (100, 100))
        #WINDOW.blit(block, (blockX, blockY))
        Block(characterX, characterY, CameraX)

        pygame.display.flip()
        pygame.display.update()
    
        fpsClock.tick(FPS)

  return 'menu'

def game_over_screen ():
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


def instructions_screen () : 
  looping = True
  action = 'game'
  font = pygame.font.Font('freesansbold.ttf', 32)
  fontTitle = pygame.font.Font('freesansbold.ttf', 64)
 
  title = fontTitle.render('Mario!', True, TEXTCOLOUR)
  menuItem1 = font.render('Instructions', True, TEXTCOLOUR)
  menuItem2 = font.render('Content coming soon', True, TEXTCOLOUR)
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

def goodbye_screen():
  font = pygame.font.Font('freesansbold.ttf', 32)
  text = font.render('MARIO!', True, TEXTCOLOUR)
  goodbyeText = font.render('See you again...', True, TEXTCOLOUR)
 
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
 
  return 'menu'

# The main function that controls the game
def main () :
  looping = True

  screen = 'splash'
  winner = ''
  
  while looping :
    # Get inputs
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
           
    # Processing

    if screen == 'splash' :
      screen = splash_screen()
    elif screen == 'menu' :
      screen = menu_screen()
    elif screen == 'game' :
      screen = game_screen()
    elif screen == 'game_over' :
      screen = game_over_screen()
    elif screen == 'instructions' :
      screen = instructions_screen() 
    else :
      screen = goodbye_screen()

    
 
main()