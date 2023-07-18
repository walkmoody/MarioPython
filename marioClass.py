import pygame, sys
from pygame.locals import *
from Menus import *
from Functions import *
from Variables import *
pygame.init()

class marioClass:

    collisionDict = Collision()

    def move(keys):
        if(marioClass.right == True):
            marioClass.printCharacter = mario
        else:
            marioClass.printCharacter = pygame.transform.flip(mario, True, False)
        if (keys[K_RIGHT] or keys[K_d]):
            marioClass.rightMove()
        if (keys[K_LEFT] or keys[K_a]):
            marioClass.leftMove()
        if (keys[K_m]):
            marioClass.printCharacter = marioRun1
        if (keys[K_n]):
            marioClass.printCharacter = middleRun
        if (keys[K_o]):
            marioClass.printCharacter = marioRun3
        
    def jump(keys):
        if (keys[K_SPACE] and marioClass.marioJumpVelocity < -marioClass.jumpStrength) :
                marioClass.marioJumpVelocity = marioClass.jumpStrength
        if marioClass.marioJumpVelocity >= -marioClass.jumpStrength:
            marioClass.characterY = marioClass.characterY - marioClass.marioJumpVelocity
            marioClass.marioJumpVelocity = marioClass.marioJumpVelocity - 1
            if (marioClass.keys[K_LEFT] or marioClass.keys[K_a]) :
                marioClass.printCharacter = marioJumpLeft
            else:
                marioClass.printCharacter = marioJump
        elif (marioClass.characterY < 570 and marioClass.isGround == True):
            marioClass.characterY = marioClass.characterY - marioClass.marioJumpVelocity
        if marioClass.characterY > 570:
            marioClass.characterY = 570
    

    def rightMove():
        marioClass.right = True # May be removed
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
            marioClass.printCharacter = pygame.transform.flip(marioRun3, True, False)
            marioClass.countLeft = 0
        if(marioClass.keys[K_LSHIFT]):
            marioClass.characterX = marioClass.characterX - (marioClass.marioSpeed * 2)
            marioClass.CameraX -= marioClass.cameraSpeed - 4

    def checks(keys):
        if (marioClass.characterX  < -4 and marioClass.isPipe == False) : # stops mario from going to the left off screeb
            marioClass.characterX = marioClass.characterX + marioClass.marioSpeed
        if (marioClass.CameraX < 0 and marioClass.isPipe == False) :
            marioClass.CameraX = marioClass.CameraX + marioClass.cameraSpeed
        if (marioClass.characterX  > WINDOW_WIDTH/5 and marioClass.CameraX < 8375 and not marioClass.isPipe): # Stops mario from running off screen right
            marioClass.characterX = marioClass.characterX - marioClass.marioSpeed
            if(marioClass.keys[K_LSHIFT]):
                marioClass.characterX = marioClass.characterX - (marioClass.marioSpeed * 2)
        if(marioClass.characterX > WINDOW_WIDTH) :
            marioClass.characterX = marioClass.characterX - marioClass.marioSpeed
            if(marioClass.keys[K_LSHIFT]):
                characterX = characterX - (marioClass.marioSpeed * 2)
        if(marioClass.characterX < 2530 -marioClass.CameraX + 95 and marioClass.characterX > 2530 -marioClass.CameraX - 14):
            if marioClass.characterY > 250:
                if(keys[K_DOWN]):
                    marioClass.isPipe = True
                    marioClass.CameraX = -1000
                    marioClass.characterX = 60
                    marioClass.characterY = 0
        
    def pipe(keys):
        marioClass.CameraX = -1000
        blockHeight = 390
        if marioClass.characterX < 40: # collision for left wall
            marioClass.characterX = marioClass.characterX + marioClass.cameraSpeed - marioClass.marioSpeed
        if (marioClass.characterX > 135 and marioClass.characterX < 150 and marioClass.characterY > blockHeight) or (marioClass.characterX > 670 and marioClass.characterX < 710 and marioClass.characterY > blockHeight):
            if marioClass.characterX > 135 and characterX < 150 :
                marioClass.characterX = marioClass.characterX - marioClass.cameraSpeed
            if marioClass.characterX > 670 and marioClass.characterX < 710:
                marioClass.characterX = marioClass.characterX + marioClass.cameraSpeed
        elif(marioClass.characterX > 135 and marioClass.characterX < 700):
            marioClass.isGround = False
            if(marioClass.characterY == blockHeight):
                marioClass.marioJumpVelocity = -23
            if not (keys[K_SPACE] ) and marioClass.characterY > blockHeight:
                marioClass.characterY = blockHeight
            else:
                marioClass.isGround = True
        if marioClass.characterX > 850:
            marioClass.isPipe = False
            marioClass.CameraX = 7220
            marioClass.characterX = 120
            marioClass.characterY = 580
    
    def collision():
         #Collision loop checks for pipe collison
        for x,y, in marioClass.collisionDict.items():
            pipe1X = y[0] - marioClass.CameraX
            pipe1Y = 600
            pipe1H = y[1]
            if(marioClass.characterX < pipe1X + 15 and marioClass.characterX > pipe1X - 15 and marioClass.characterY < pipe1Y and marioClass.characterY > pipe1Y - pipe1H and (marioClass.keys[K_RIGHT] or marioClass.keys[K_d])):
                marioClass.characterX = marioClass.characterX - marioClass.marioSpeed
                marioClass.CameraX = marioClass.CameraX - marioClass.cameraSpeed
            elif(marioClass.characterX < pipe1X + 95 and marioClass.characterX > pipe1X - 14): 
                marioClass.isGround = False
                if(marioClass.characterY == pipe1Y - pipe1H):
                    marioClass.marioJumpVelocity = -23
                if (not (marioClass.keys[K_SPACE]) and marioClass.characterY > pipe1Y - pipe1H): #or ((keys[K_SPACE] ) or characterY < pipe1Y - pipe1H): #FIX ME 
                    marioClass.characterY = pipe1Y - pipe1H
            else:
                marioClass.isGround = True
            if(marioClass.characterX < pipe1X + 15 + 100  and marioClass.characterX > pipe1X - 15 + 100 and marioClass.characterY < pipe1Y and marioClass.characterY > pipe1Y - pipe1H and (marioClass.keys[K_LEFT] or marioClass.keys[K_a]) ): # pipewidth is 100
                marioClass.characterX = marioClass.characterX + marioClass.marioSpeed
                marioClass.CameraX = marioClass.CameraX + marioClass.cameraSpeed
    
    def death():
        for x,y in marioClass.deathDict.items():
            holeX = y[0] - marioClass.CameraX
            holeEnd = y[0] + 100  - marioClass.CameraX
            if(marioClass.characterX > holeX and marioClass.characterX < holeEnd and marioClass.characterY > 569):
                marioClass.looping = False
                HoleTouch(marioClass.characterX, marioClass.characterY, marioClass.CameraX, marioClass.CameraY)
                return 'death'

    
    '''''

    def __init__(self, keys):

       
       
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
    #character spawn location
    #Variables
    looping = True
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
    isGround = True
    right = True
    
    deathDict = Holes()
    goalX = 8900 # 8850
    isPipe = False
    marioSpeed = 1
    cameraSpeed = 8
    keys = pygame.key.get_pressed()

