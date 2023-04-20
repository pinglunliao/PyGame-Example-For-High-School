# -*- coding: utf-8 -*-
# Using Keyboard to move an image
import pygame

pygame.init()

#
# Step 1: Create the screen window
#

# Screen width, height
S_W = 500
S_H = 500

winScreen = pygame.display.set_mode((S_W, S_H))
pygame.display.set_caption("Control Two Balls Demo")

#
# Step 2: Set the Ball's velocity, position, size
#

# 
vel = 5

# The ball's radius
R = 20
# The ball's position
ballX = int((S_W - R) / 2)
ballY = int((S_H - R) / 2)

# The image for ball(?)
# ballImgX = ballX
# ballImgY = ballY

run = True

ballImg = pygame.image.load("intro_ball.gif")
ballImgrect = ballImg.get_rect()

while run:
    pygame.time.delay(10)

    #
    # Step 3: Detect which key is pressed.
    #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Move the ball with left, right, up, down arrow key
    if keys[pygame.K_LEFT]:
        ballX -= vel

    if keys[pygame.K_RIGHT]:
        ballX += vel

    if keys[pygame.K_UP]:
        ballY -= vel

    if keys[pygame.K_DOWN]:
        ballY += vel

    # Move the image with a, w, d, x
    # if keys[pygame.K_a]:
    #   ballImgX -= vel

    # if keys[pygame.K_d]:
    #   ballImgX += vel

    # if keys[pygame.K_w]:
    #   ballImgY -= vel

    # if keys[pygame.K_x]:
    #   ballImgY += vel
     
#
# Step 4: Draw the ball.
#
    winScreen.fill((0, 0, 0))  # Fills the screen with black
    pygame.draw.circle(winScreen, (255, 255, 0), (ballX, ballY), R)
    winScreen.blit(ballImg, (ballImgX, ballImgY))
    pygame.display.update()

pygame.quit()