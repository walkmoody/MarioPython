import pygame, sys
from pygame.locals import *
from Functions import *
from Variables import *
from marioClass import *
pygame.init()

def game_screen(lives): 
  #character spawn location
  characterX = 0
  characterY = 570
  #Jump Strength
  marioJumpVelocity = -23
  jumpStrength = 22
  jumpActive = False # makes it so player cant jump multiple times
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
  marioSpeed = 1
  cameraSpeed = 8
  #allows game to run
  looping = True
  #marioClass(keys)
  while looping :
    # Checks for orientation of player
    if(right == True):
      marioClass.printCharacter = mario
    else:
      marioClass.printCharacter = pygame.transform.flip(mario, True, False)
    #allows the player to exit
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed() # gets key value
    marioClass(keys)
    #hot key to leave the game
    if (keys[K_q]):
      return 'quit'
    #FIXME PAUSE SCREEN
    if (keys[K_p]):
      looping = False 
      Pause()
      looping = True
    #mario speed and camera speed need to be different
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
        if isPipe == True and characterX < WINDOW_WIDTH/5:
          characterX = characterX + marioSpeed - cameraSpeed + marioSpeed
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
        if jumpActive == True:
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
    if marioJumpVelocity >= -jumpStrength : # attmempt to fix multiple mario JUMPS
      jumpActive = False
    else: 
      jumpActive = True
    
    #Animation Test (or hidden Feature: emote)
    if (keys[K_m]):
        printCharacter = marioRun1
    if (keys[K_n]):
        printCharacter = middleRun
    if (keys[K_o]):
      printCharacter = marioRun3
    
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
        if (not (keys[K_SPACE]) and characterY > pipe1Y - pipe1H): #or ((keys[K_SPACE] ) or characterY < pipe1Y - pipe1H): #FIX ME 
          characterY = pipe1Y - pipe1H
      else:
        isGround = True
      if(characterX < pipe1X + 15 + 100  and characterX > pipe1X - 15 + 100 and characterY < pipe1Y and characterY > pipe1Y - pipe1H and (keys[K_LEFT] or keys[K_a]) ): # pipewidth is 100
        characterX = characterX + marioSpeed
        CameraX = CameraX + cameraSpeed
    #allows the player to go into 4th pipe
    if(characterX < 2530 -CameraX + 95 and characterX > 2530 -CameraX - 14):
      if characterY > 250:
        if(keys[K_DOWN]):
          isPipe = True
          CameraX = -1000
          characterX = 60
          characterY = 0
    #if player is in the fourth pipe it no longer moves camera
    if isPipe == True:
      CameraX = -1000
      blockHeight = 390
      if characterX < 40: # collision for left wall
        characterX = characterX + cameraSpeed - marioSpeed
      if (characterX > 135 and characterX < 150 and characterY > blockHeight) or (characterX > 670 and characterX < 710 and characterY > blockHeight):
        if characterX > 135 and characterX < 150 :
          characterX = characterX - cameraSpeed
        if characterX > 670 and characterX < 710:
          characterX = characterX + cameraSpeed
      elif(characterX > 135 and characterX < 700):
        isGround = False
        if(characterY == blockHeight):
          marioJumpVelocity = -23
        if not (keys[K_SPACE] ) and characterY > blockHeight:
          characterY = blockHeight
        else:
          isGround = True
      if characterX > 850:
        isPipe = False
        CameraX = 7220
        characterX = 120
        characterY = 580
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
    #Prints the background and character sprites
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