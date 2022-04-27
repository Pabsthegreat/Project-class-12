import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,800))

#Title and Icon
pygame.display.set_caption("Hunter Assasin")
icon = pygame.image.load("001-hunter.png")
pygame.display.set_icon(icon)

#bg
bg = pygame.image.load("bg.png")
screen.blit(bg ,(0,0))
pygame.display.update()

x = 0
y = 0

#player Image 
playerimg = pygame.image.load("001-caveman.png")
x = 0
y = 0
def player(x,y):
    screen.blit(playerimg, (x, y))



#controls
up = (pygame.K_UP, ord('w'))
down = (pygame.K_DOWN, ord('s'))
left = (pygame.K_LEFT , ord('a'))
right = (pygame.K_RIGHT, ord('d'))

loop = True
while loop:

    pygame.time.delay(100)

    screen.fill((100, 100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False 

        cx ,cy = 0 , 0
        if event.type == pygame.KEYDOWN:
            if event.key in left:
                cx -= 0.3

            if event.key in right:
                cx += 0.3

            if event.key in up:
                cy -= 0.3

            if event.key in down:
                cy += 0.3

            if event.type == pygame.KEYUP:
                cx , cy = 0 , 0

    x += cx
    y += cy 
    #to prevent it from going out of bounds, subtract the width of the player i,e in pixels.
    if x <= 0 :
        x = 0
    
    if y <= 0:
        y = 0

    if x >= 736:
        x = 736

    if y >= 736:
        y = 736


    player(x,y)
    pygame.display.update()
    

pygame.quit()
 

