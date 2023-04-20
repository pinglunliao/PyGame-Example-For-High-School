# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
# 取得目前程式碼執行的路徑
import os.path
main_dir = os.path.split(os.path.abspath(__file__))[0]
file = os.path.join(main_dir, 'pics', "intro_ball.gif")

# Pygame Initialization
pygame.init()

#
# Step 1: Create the screen window
#

# Screen width, height
S_W = 500
S_H = 500

winScreen = pygame.display.set_mode((S_W, S_H))
pygame.display.set_caption("Mouse Keyboard Demo")

#
# Step 2: Set the Ball's velocity, position, size
#

ballImg = pygame.image.load(file)
ballImgRect = ballImg.get_rect()
vel = 5

run = True
moving = False

while run:
    pygame.time.delay(10)

#
# Step 3: Detect which key is pressed.
#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        # Making the image move
        elif event.type == MOUSEBUTTONDOWN:
            if ballImgRect.collidepoint(event.pos):
                moving = True
        
        # Set moving as False if you want
        # to move the image only with the
        # mouse click
        # Set moving as True if you want
        # to move the image without the
        # mouse click
        elif event.type == MOUSEBUTTONUP:
            moving = False
 
        # Make your image move continuously
        elif event.type == MOUSEMOTION and moving:
            ballImgRect.move_ip(event.rel)
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        ballImgRect[0] -= vel

    if keys[pygame.K_RIGHT]:
        ballImgRect[0] += vel

    if keys[pygame.K_UP]:
        ballImgRect[1] -= vel

    if keys[pygame.K_DOWN]:
        ballImgRect[1] += vel

#
# Step 4: Draw the ball.
#
    winScreen.fill((0, 0, 0))  # Fills the screen with black
    winScreen.blit(ballImg, ballImgRect)
    pygame.display.update() 
    
pygame.quit()