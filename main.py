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

        if event.type == pygame.KEYUP:
            STAND = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                x -= vel
                left = True
                runR1 = pygame. transform. rotate(runR, 90)
                runL1 = pygame. transform. rotate(runL, 90)
                stand1 = pygame. transform. rotate(stand, 90)

            if event.key == pygame.K_RIGHT :
                x += vel
                right = True
                runR1 = pygame. transform. rotate(runR, -90)
                runL1 = pygame. transform. rotate(runL, -90)
                stand1 = pygame. transform. rotate(stand, -90)

            if event.key == pygame.K_UP :
                y -= vel
                up = True
                runR1 = pygame. transform. rotate(runR, 0)
                runL1 = pygame. transform. rotate(runL, 0)
                stand1 = pygame. transform. rotate(stand, 0)


            if event.key == pygame.K_DOWN  :
                y += vel
                down = True
                runR1 = pygame.transform.rotate(runR, 180)
                runL1 = pygame.transform.rotate(runL, 180)
                stand1 = pygame. transform. rotate(stand, 180)
        
      
    if x <= 0 :
        x = 0
    
    if y <= 0:
        y = 0

    if x >= 736:
        x = 736

    if y >= 736:
        y = 736

    charmove()
    screen.fill((0,128,0))

pygame.quit()
