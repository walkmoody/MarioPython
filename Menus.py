import pygame, sys, random, time, math
from pygame.locals import *
pygame.init()

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
# EXTCOLOUR = (200, 100, 0) Orange
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
fontObj = pygame.font.SysFont('freesansbold.ttf', 32)

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

  menuItem1 = font.render('INSTRUCTIONS - I', True, WHITE)
  menuItem2 = font.render('PLAY GAME - SPACE', True, WHITE)
  menuItem3 = font.render('QUIT - Q', True, WHITE)
 
  menuItem1Rect = menuItem1.get_rect()
  menuItem2Rect = menuItem2.get_rect()
  menuItem3Rect = menuItem3.get_rect()
 
  menuItem1Rect.topleft = (WINDOW_WIDTH/3, 350)
  menuItem2Rect.topleft = (WINDOW_WIDTH/3, 400)
  menuItem3Rect.topleft = (WINDOW_WIDTH/3, 450)
 
 
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
    WINDOW.blit(mario,(0,570))
    WINDOW.blit(SuperMarioBros, (WINDOW_WIDTH/4,47))
    
    pygame.display.update()
    fpsClock.tick(FPS)
  return action

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