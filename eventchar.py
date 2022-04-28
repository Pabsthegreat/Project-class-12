import pygame 
up = False
down = False
left = False
right = False
STAND = False
vel = 5
width = 64
x = 400
y = 400
runL = pygame.image.load('Running-02.png')
runR = pygame.image.load('Running-03.png')
stand = pygame.image.load('Resting-01.png')

def movement():
    global runL,runR,stand,runR1,runL1,stand1,left,right,STAND,up,down
    keys = pygame.key.get_pressed()

    if keys [pygame.K_LEFT] and x > vel :
            x -= vel
            left = True
            up = False
            down = False
            right = False
            STAND = False
            runR1 = pygame. transform. rotate(runR, 90)
            runL1 = pygame. transform. rotate(runL, 90)
            stand1 = pygame. transform. rotate(stand, 90)

    elif keys [pygame.K_RIGHT] and x < 800 - width - vel :
            x += vel
            right = True
            up = False
            down = False
            left = False
            STAND = False
            runR1 = pygame. transform. rotate(runR, -90)
            runL1 = pygame. transform. rotate(runL, -90)
            stand1 = pygame. transform. rotate(stand, -90)

    elif keys [pygame.K_UP] and y > vel:
            y -= vel
            up = True
            up = False
            down = False
            left = False
            right = False
            STAND = False
            runR1 = pygame. transform. rotate(runR, 0)
            runL1 = pygame. transform. rotate(runL, 0)
            stand1 = pygame. transform. rotate(stand, 0)

    elif keys [pygame.K_DOWN]  and y < 800 - width - vel :
            y += vel
            down = True
            up = False
            down = False
            left = False
            right = False
            STAND = False
            runR1 = pygame.transform.rotate(runR, 180)
            runL1 = pygame.transform.rotate(runL, 180)
            stand1 = pygame. transform. rotate(stand, 180)
        
    if keys [pygame.KEYUP]:
        STAND = True
        up = False
        up = False
        down = False
        left = False
        right = False
        runR1 = pygame.transform.rotate(runR, 180)
        runL1 = pygame.transform.rotate(runL, 180)
        stand1 = pygame. transform. rotate(stand, 180)

    return runR1,runL1,stand1,up,down,left,right,STAND


def charmove(runR1,runL1,stand1,up,down,left,right,STAND):

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

screen = pygame.display.set_mode((800,800))
