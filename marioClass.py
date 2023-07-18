import pygame, sys
from pygame.locals import *
from Menus import *
from Functions import *
from Variables import *
pygame.init()

class marioClass:
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
    keys = pygame.key.get_pressed()

    def move(keys):
        if (keys[K_RIGHT] or keys[K_d]):
            marioClass.rightMove()
        if (keys[K_LEFT] or keys[K_a]):
            marioClass.leftMove()
        if (keys[K_SPACE] and marioClass.marioJumpVelocity < -marioClass.jumpStrength) :
            if marioClass.jumpActive == False: # CHANGE BACK TO TRUE IF NEEDED
                marioClass.marioJumpVelocity = marioClass.jumpStrength
        if marioClass.marioJumpVelocity >= -marioClass.jumpStrength:
            marioClass.jump()

    def jump():
        marioClass.characterY = marioClass.characterY - marioClass.marioJumpVelocity
        marioClass.marioJumpVelocity = marioClass.marioJumpVelocity - 1
        if (marioClass.keys[K_LEFT] or marioClass.keys[K_a]) :
            marioClass.printCharacter = marioJumpLeft
        else:
            marioClass.printCharacter = marioJump

    def rightMove():
        right = True # May be removed
        marioClass.characterX = marioClass.characterX + marioClass.marioSpeed
        marioClass.printCharacter = mario
        marioClass.CameraX += marioClass.cameraSpeed
        marioClass.count += 1
        if marioClass.CameraX > 8380 or marioClass.isPipe:
            marioClass.characterX =marioClass. characterX - marioClass.marioSpeed + marioClass.cameraSpeed
        if marioClass.CameraX > 8380:
            marioClass.CameraX = marioClass.CameraX - marioClass.cameraSpeed
        if (marioClass.count < 5):
            marioClass.printCharacter = marioRun1
        elif( marioClass.count < 10):
            marioClass.printCharacter = middleRun
        elif ( marioClass.count < 15):
            marioClass.printCharacter = marioRun3
        else: 
            marioClass.printCharacter = marioRun3
            marioClass.count = 0
        if(marioClass.keys[K_LSHIFT]):
            marioClass.characterX = marioClass.characterX + (marioClass.marioSpeed * 2)
            marioClass.CameraX += marioClass.cameraSpeed + 4

    def leftMove():
        marioClass.right = False
        marioClass.characterX = marioClass.characterX - marioClass.marioSpeed
        marioClass.printCharacter = pygame.transform.flip(mario, True, False)
        if (characterX < WINDOW_WIDTH/5):
            marioClass.CameraX -= marioClass.cameraSpeed 
        else:
            marioClass.characterX = marioClass.characterX + marioClass.marioSpeed - marioClass.cameraSpeed
        if  marioClass.isPipe == True and characterX < WINDOW_WIDTH/5:
            marioClass.characterX = marioClass.characterX + marioClass.marioSpeed - marioClass.cameraSpeed + marioClass.marioSpeed
        marioClass.countLeft += 1
        if (marioClass.countLeft < 5):
            marioClass.printCharacter = pygame.transform.flip(marioRun1, True, False)
        elif( marioClass.countLeft < 10):
            marioClass.printCharacter = pygame.transform.flip(middleRun, True, False)
        elif ( marioClass.countLeft < 15):
            marioClass.printCharacter = pygame.transform.flip(marioRun3, True, False)
        else: 
            marioClass.countLeft = 0
        if(marioClass.keys[K_LSHIFT]):
            marioClass.characterX = marioClass.characterX - (marioClass.marioSpeed * 2)
            marioClass.CameraX -= marioClass.cameraSpeed - 4

    
    '''''

    def __init__(self, keys):
        
    
        
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


    ###

    '''
