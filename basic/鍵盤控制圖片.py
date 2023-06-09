# -*- coding: utf-8 -*-
# Using Keyboard to move an image
import pygame
# 取得目前程式碼執行的路徑
import os.path
main_dir = os.path.split(os.path.abspath(__file__))[0]
file = os.path.join(main_dir, 'pics', "intro_ball.gif")

pygame.init()

#
# Step 1: Create the screen window
#

# Screen width, height
S_W = 500
S_H = 500

winScreen = pygame.display.set_mode((S_W, S_H))
pygame.display.set_caption("Keyboard Controlled Image Demo")

#
# Step 2: Set the Ball's velocity, position, size
#

R = 20
x = int((S_W - R) / 2)
y = int((S_H - R) / 2)
vel = 5

run = True

ball = pygame.image.load(file)
ballrect = ball.get_rect()

while run:
    pygame.time.delay(10)

#
# Step 3: Detect which key is pressed.
#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel

#
# Step 4: Draw the image.
#
    winScreen.fill((0, 0, 0))  # Fills the screen with black
    winScreen.blit(ball, (x,y))
    pygame.display.update() 
    
pygame.quit()