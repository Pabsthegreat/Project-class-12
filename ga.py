import pygame

pygame.init()

screen = pygame.display.set_mode((800,800))
lrun = pygame.image.load("leftrun.png")
rrun = pygame.image.load("rightrun.png")
rest = pygame.image.load("rest.png")
bg = pygame.image.load("bg.png")


#Title and Icon
pygame.display.set_caption("Assassin")
icon = pygame.image.load("rest.png")
pygame.display.set_icon(icon)

"""#bg
bg = pygame.image.load("bg.png")
screen.blit(bg ,(0,0))
pygame.display.update()
"""

#player Image 
playerimg = pygame.image.load("rest.png")

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


    screen.fill((100, 100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False 

        cx ,cy = 0 , 0
        if event.type == pygame.KEYDOWN:
            if event.key in left:
                cx -= 0.3

            if event.key in right:
                rotate = pygame.transform.rotate(playerimg, 90)
                screen.blit(rotate, (x,y))
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
 
