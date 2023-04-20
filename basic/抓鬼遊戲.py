# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import random

# Pygame Initialization
pygame.init()

#
# Step 1: Create the screen window
#

# Screen width, height
S_W = 500
S_H = 500

screen = pygame.display.set_mode((S_W, S_H))
pygame.display.set_caption("Ghost Catcher Game")

#
# Step 2: Set the Ball's velocity, position, size
#
ghostImg = pygame.image.load("./pics/ghost-a.png")
ghostImgRect = ghostImg.get_rect()

ghostX = int((S_W - ghostImgRect.width) / 2)
ghostY = int((S_H - ghostImgRect.height) / 2)

ghostImgRect = ghostImgRect.move(ghostX, ghostY)

ghostHitImg = pygame.image.load("pics/ghost-c.png")

font = pygame.font.SysFont(None, 40)


clickCnt = 0

run = True

# timer
clock = pygame.time.Clock()
time_interval = 1000 # 1000 milliseconds == 1 second
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, time_interval) 

# 遊戲時間
gameDuration = 3
text = str(gameDuration).rjust(3)

while run:
    pygame.time.delay(1)

#
# Step 3: Detect which key is pressed.
#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        elif event.type == timer_event:
            gameDuration -= 1
            text = str(gameDuration).rjust(3) if gameDuration > 0 else 'Game Over'

        # Making the image move
        elif event.type == MOUSEBUTTONDOWN:
            if gameDuration > 0:
                if ghostImgRect.collidepoint(event.pos):
                    clickCnt = clickCnt + 1
                    screen.fill((0, 0, 0))  # Fills the screen with black
                    screen.blit(ghostHitImg, ghostImgRect)
                    pygame.display.update() 
                    pygame.time.delay(500)
                    ghostX = random.randint(0,S_W)
                    ghostY = random.randint(0,S_H)
                    ghostImgRect.left = ghostX
                    ghostImgRect.bottom = ghostY
                
#
# Step 4: Draw the ghost.
#
    screen.fill((0, 0, 0))  # Fills the screen with black
    screen.blit(ghostImg, ghostImgRect)

    img = font.render('Clicks:' + str(clickCnt), True, (0,0,255))
    screen.blit(img, (S_W/2, 0))
    screen.blit(font.render(text, True, (0, 255, 0)), (S_W/2, S_H/2))
    pygame.display.flip()
    clock.tick(60)
    pygame.display.update() 
    
pygame.quit()