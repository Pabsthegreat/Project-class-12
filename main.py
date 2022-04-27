import pygame

pygame.init()

#creating the screen
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Hunter Assassin")

runL = pygame.image.load('Running-02.png')
runR = pygame.image.load('Running-03.png')
stand = pygame.image.load('Resting-01.png')

clock = pygame.time.Clock()
x = 400
y = 400
width = 64
height = 64
vel = 5
up = False
down = False
left = False
right = False
STAND = False


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
    


#game loop
running = True
while running == True:
    clock.tick(30)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
   

    keys = pygame.key.get_pressed()

    if keys [pygame.K_LEFT] and x > vel :
        x -= vel
        left = True
        runR1 = pygame. transform. rotate(runR, 90)
        runL1 = pygame. transform. rotate(runL, 90)
        stand1 = pygame. transform. rotate(stand, 90)

    if keys [pygame.K_RIGHT] and x < 800 - width - vel :
        x += vel
        right = True
        runR1 = pygame. transform. rotate(runR, -90)
        runL1 = pygame. transform. rotate(runL, -90)
        stand1 = pygame. transform. rotate(stand, -90)

    if keys [pygame.K_UP] and y > vel:
        y -= vel
        up = True
        runR1 = pygame. transform. rotate(runR, 0)
        runL1 = pygame. transform. rotate(runL, 0)
        stand1 = pygame. transform. rotate(stand, 0)


    if keys [pygame.K_DOWN] and y < 800 - width - vel :
        y += vel
        down = True
        runR1 = pygame.transform.rotate(runR, 180)
        runL1 = pygame.transform.rotate(runL, 180)
        stand1 = pygame. transform. rotate(stand, 180)
    
    if keys [pygame.KEYUP]:
        STAND = True
      
    charmove()

    screen.fill((0,128,0))

pygame.quit()
