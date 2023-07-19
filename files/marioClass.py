import pygame
from pygame.locals import *
from files.Menus import *
from files.Functions import *
from files.Variables import *
pygame.init()

class marioClass:
        
    collisionDict = Collision()
    deathDict = Holes()

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
        if (keys[K_q]):
            return 'quit'
        #FIXME PAUSE SCREEN
        if (keys[K_p]):
            marioClass.looping = False 
            Pause()
            marioClass.looping = True
        
    def jump(keys):
        if (keys[K_SPACE] and marioClass.marioJumpVelocity < -marioClass.jumpStrength) :
                marioClass.marioJumpVelocity = marioClass.jumpStrength
        if marioClass.marioJumpVelocity >= -marioClass.jumpStrength:
            marioClass.characterY = marioClass.characterY - marioClass.marioJumpVelocity
            marioClass.marioJumpVelocity = marioClass.marioJumpVelocity - 1
            if (marioClass.right == False):
                marioClass.printCharacter = marioJumpLeft
            else:
                marioClass.printCharacter = marioJump
        elif (marioClass.characterY < 570 and marioClass.isGround == True):
            marioClass.characterY = marioClass.characterY - marioClass.marioJumpVelocity
        if marioClass.characterY > 570:
            marioClass.characterY = 570
    

    def rightMove():
        marioClass.right = True
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

    def leftMove():
        marioClass.right = False
        marioClass.characterX = marioClass.characterX - marioClass.marioSpeed
        marioClass.printCharacter = pygame.transform.flip(mario, True, False)
        if (characterX < WINDOW_WIDTH/5):
            marioClass.CameraX -= marioClass.cameraSpeed 
        else:
            marioClass.characterX = marioClass.characterX + marioClass.marioSpeed - marioClass.cameraSpeed #Glitch right here
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

    def checks(keys):
        if (marioClass.characterX  < -4 and marioClass.isPipe == False) : # stops mario from going to the left off screeb
            marioClass.characterX = marioClass.characterX + marioClass.marioSpeed
        if (marioClass.CameraX < 0 and marioClass.isPipe == False) :
            marioClass.CameraX = marioClass.CameraX + marioClass.cameraSpeed
        if (marioClass.characterX  > WINDOW_WIDTH/5 and marioClass.CameraX < 8374 and not marioClass.isPipe): # Stops mario from running off screen right
            marioClass.characterX = marioClass.characterX - marioClass.marioSpeed
            marioClass.CameraX == 8374
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
        if marioClass.characterX > marioClass.goalX - marioClass.CameraX:
            marioClass.looping = False
            flagpole(marioClass.characterY, marioClass.characterX, marioClass.CameraX, marioClass.CameraY)
            return 'menu'
        
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
        #TODO needs to be fixed
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
            
    def init():
        marioClass.looping = True
        marioClass.characterX = 20
        marioClass.characterY = 570
        #Jump Strength
        marioClass.marioJumpVelocity = -23
        marioClass.jumpStrength = 22
        #Camera
        marioClass.CameraX, marioClass.CameraY= 0, 0
        #allows for mario Run animation
        marioClass.printCharacter = mario
        marioClass.count, marioClass.countLeft = 0, 0
        marioClass.isGround = True
        marioClass.right = True
        marioClass.goalX = 8900 # 8850
        marioClass.isPipe = False
        marioClass.marioSpeed = 1
        marioClass.cameraSpeed = 8

    #Variables
    looping = True
    characterX = 20
    characterY = 570
    #Jump Strength
    marioJumpVelocity = -23
    jumpStrength = 22
    #Camera
    CameraX, CameraY= 0, 0
    printCharacter = mario
    count, countLeft = 0, 0
    #goombaDeath = False
    isGround = True
    right = True
    goalX = 8900 # 8850
    isPipe = False
    marioSpeed = 1
    cameraSpeed = 8
    keys = pygame.key.get_pressed()

