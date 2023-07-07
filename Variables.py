import pygame
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