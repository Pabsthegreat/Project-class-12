import pygame

pygame.init()

#creating the screen
screen = pygame.display.set_mode((800,800))


pygame.display.set_caption("Hunter Assassin")

icon = pygame.image.load("Resting-01.png")
pygame.display.set_icon(icon)

Walk = [pygame.image.load('Hunter_Move/1.png'),pygame.image.load('Hunter_Move/2.png'),pygame.image.load('Hunter_Move/3.png'),
pygame.image.load('Hunter_Move/4.png'),pygame.image.load('Hunter_Move/5.png'),pygame.image.load('Hunter_Move/6.png'),
pygame.image.load('Hunter_Move/7.png'),pygame.image.load('Hunter_Move/8.png'), pygame.image.load("Hunter_Move/8a.png"),pygame.image.load('Hunter_Move/9.png'),pygame.image.load('Hunter_Move/10.png'),pygame.image.load('Hunter_Move/11.png'),
pygame.image.load('Hunter_Move/12.png'),pygame.image.load('Hunter_Move/13.png'),pygame.image.load('Hunter_Move/14.png'),
pygame.image.load('Hunter_Move/15.png')]

rest = pygame.image.load("Hunter_Move/8a.png")
rest1 = rest

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
COUNT = 0

def move():
    global COUNT,rest1

    if STAND == True:
        screen.blit(rest1, (x, y))
        pygame.display.update()

    elif COUNT <= 15:

        if up == True:
            m = pygame.transform.rotate(Walk[COUNT], 0)
            screen.blit(m,(x,y))
            pygame.display.update()

        if down == True:
            m = pygame.transform.rotate(Walk[COUNT], 180)
            screen.blit(m,(x,y))
            pygame.display.update()

        if right == True:
            m = pygame.transform.rotate(Walk[COUNT], -90)
            screen.blit(m,(x,y))
            pygame.display.update()

        if left == True:
            m = pygame.transform.rotate(Walk[COUNT], 90)
            screen.blit(m,(x,y))
            pygame.display.update()

        COUNT += 1
        
    else:
        COUNT = 0



#game loop
running = True
while running == True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP:
            STAND = True

    keys = pygame.key.get_pressed()

    if keys [pygame.K_LEFT] or keys [pygame.K_a] and x > vel :
        x -= vel
        left = True
        up = False
        down = False
        right = False
        STAND = False
        rest1 = pygame.transform.rotate(rest, 90)

    elif keys [pygame.K_RIGHT] or keys [pygame.K_d] and x < 800 - width - vel :
        x += vel
        right = True
        up = False
        down = False
        left = False
        STAND = False
        rest1 = pygame.transform.rotate(rest, -90)

    elif keys [pygame.K_UP] or keys [pygame.K_w] and y > vel:
        y -= vel
        up = True
        right = False
        down = False
        left = False
        STAND = False
        rest1 = pygame.transform.rotate(rest, 0)

    elif keys [pygame.K_DOWN] or keys [pygame.K_s] and y < 800 - width - vel :
        y += vel
        down = True
        STAND = False
        up = False
        right = False
        left = False
        rest1 = pygame.transform.rotate(rest, 180)     
      
    move()

    if x <= 0 :
        x = 0
    
    if y <= 0:
        y = 0

    if x >= 672:
        x = 672

    if y >= 672:
        y = 672

    screen.fill((152,251,152))
    

pygame.quit()
