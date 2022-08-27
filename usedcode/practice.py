import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock() #fps


#Title and Icon
pygame.display.set_caption("Hunter Assasin")
icon = pygame.image.load("Resting-01.png")
pygame.display.set_icon(icon)

'''
#bg
bg = pygame.image.load("bg.png")
screen.blit(bg ,(0,0))
pygame.display.update()
'''

x = 0
y = 0
up = False
down = False
left = False
right = False
STAND = False

#player Image 
playerimg = pygame.image.load("Resting-01.png")
runL = pygame.image.load('Running-02.png')
runR = pygame.image.load('Running-03.png')
stand = pygame.image.load('Resting-01.png')
x = 0
y = 0

#player fn


#player controls.
def charmove():
    global stand1, runR1, runL1

    if STAND == True:
        screen.blit(stand1, (x,y))
    
    elif up == True:
        screen.blit(runL1, (x,y))
        pygame.display.update()
        screen.blit(runR1, (x,y))

    elif down == True:
        screen.blit(runL1, (x,y))
        pygame.display.update()
        screen.blit(runR1, (x,y))

    elif right == True:
        screen.blit(runL1, (x,y))
        pygame.display.update()
        screen.blit(runR1, (x,y))

    elif left == True:
        screen.blit(runL1, (x,y))
        pygame.display.update()
        screen.blit(runR1, (x,y))


    pygame.display.update()

'''
#controls
up = (pygame.K_UP)
down = (pygame.K_DOWN)
left = (pygame.K_LEFT) 
right = (pygame.K_RIGHT)
'''

loop = True
while loop:

    screen.fill((100, 100, 100))
    clock.tick(30)
    #pygame.time.delay(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False 

        cx ,cy = 0 , 0
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                left = True
                runR1 = pygame. transform. rotate(runR, 90)
                runL1 = pygame. transform. rotate(runL, 90)
                stand1 = pygame. transform. rotate(stand, 90)
                x -= 5

            if event.key == pygame.K_RIGHT:
                right = True
                runR1 = pygame. transform. rotate(runR, -90)
                runL1 = pygame. transform. rotate(runL, -90)
                stand1 = pygame. transform. rotate(stand, -90)
                x += 5

            if event.key == pygame.K_UP:
                up = True
                runR1 = pygame. transform. rotate(runR, 0)
                runL1 = pygame. transform. rotate(runL, 0)
                stand1 = pygame. transform. rotate(stand, 0)
                y -= 5

            if event.key == pygame.K_DOWN:
                down = True
                runR1 = pygame.transform.rotate(runR, 180)
                runL1 = pygame.transform.rotate(runL, 180)
                stand1 = pygame. transform. rotate(stand, 180)
                y += 5

        if event.type == pygame.KEYUP:
                x += 0
                y += 0
                STAND = True
    charmove()
    #to prevent it from going out of bounds, subtract the width of the player i,e in pixels.
    if x <= 0 :
        x = 0
    
    if y <= 0:
        y = 0

    if x >= 736:
        x = 736

    if y >= 736:
        y = 736


    pygame.display.update()
    

pygame.quit()
 
#Just Checking

