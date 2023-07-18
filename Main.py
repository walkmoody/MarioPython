import pygame, sys
from pygame.locals import *
from Menus import *
#from GameMovement import *
from testClass import *
pygame.init()
#TODO add classes to game movement in order to clean up code
# The main function that controls the game
def main () :
  looping = True

  screen = 'splash'
  lives = 4 #Change if need more lives

  while looping :
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