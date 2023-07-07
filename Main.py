import pygame, sys, random, time, math
from pygame.locals import *
import Functions
from Functions import *
import Menus
from Menus import *
import GameMovement
from GameMovement import *
pygame.init()

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