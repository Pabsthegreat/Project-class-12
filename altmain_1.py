import pygame

pygame.init()

#creating the screen
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Hunter Assassin")

Walk = [pygame.image.load('Hunter_Move/1.png'),pygame.image.load('Hunter_Move/2.png'),pygame.image.load('Hunter_Move/3.png'),
pygame.image.load('Hunter_Move/4.png'),pygame.image.load('Hunter_Move/5.png'),pygame.image.load('Hunter_Move/6.png'),
pygame.image.load('Hunter_Move/7.png'),pygame.image.load('Hunter_Move/8.png'), pygame.image.load("Hunter_Move/8a.png"),pygame.image.load('Hunter_Move/9.png'),pygame.image.load('Hunter_Move/10.png'),pygame.image.load('Hunter_Move/11.png'),
pygame.image.load('Hunter_Move/12.png'),pygame.image.load('Hunter_Move/13.png'),pygame.image.load('Hunter_Move/14.png'),
pygame.image.load('Hunter_Move/15.png')]

rest = pygame.image.load("Hunter_Move/8a.png")

icon = pygame.image.load("Hunter_Move/8a.png")
pygame.display.set_icon(icon)

bg =  pygame.image.load('bg.png')

#enemy
enemy = pygame.image.load("enemy.png")

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width,height): 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.stand = False
        self.COUNT = 0


    def move(self):

        if self.stand == True:
            screen.blit(rest, (self.x, self.y))
            pygame.display.update()

        elif self.COUNT <= 15:

            if self.up == True:
                m = pygame.transform.rotate(Walk[self.COUNT], 0)
                screen.blit(m,(self.x,self.y))
                pygame.display.update()

            elif self.down == True:
                m = pygame.transform.rotate(Walk[self.COUNT], 180)
                screen.blit(m,(self.x,self.y))
                pygame.display.update()

            elif self.right == True:
                m = pygame.transform.rotate(Walk[self.COUNT], -90)
                screen.blit(m,(self.x,self.y))
                pygame.display.update()

            elif self.left == True:
                m = pygame.transform.rotate(Walk[self.COUNT], 90)
                screen.blit(m,(self.x,self.y))
                pygame.display.update()

            self.COUNT += 1
            

        else:
            self.COUNT = 0


def draw():
    screen.blit(bg, (0,0))
    lad.move()
    pygame.display.update()


#game loop
lad = player(400,100,128,128)
running = True
while running == True:
    clock.tick(48)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys [pygame.K_LEFT] or keys [pygame.K_a] :
        lad.x -= lad.vel
        lad.left = True
        rest = pygame. transform. rotate(rest, 90)


    elif keys [pygame.K_RIGHT] or keys [pygame.K_d]  :
        lad.x += lad.vel
        lad.right = True
        rest = pygame. transform. rotate(rest, -90)
        
    elif keys [pygame.K_UP] or keys [pygame.K_w] :
        lad.y -= lad.vel
        lad.up = True
        rest = pygame. transform. rotate(rest, 0)
        
    elif keys [pygame.K_DOWN] or keys [pygame.K_s] :
        lad.y += lad.vel
        lad.down = True
        rest = pygame. transform. rotate(rest, 180)
        
    
    while keys [pygame.KEYUP]:
        lad.stand = True
      
    

#have to do it this was , as "and", "or" together in the previous method was not working when awsd was added
    if lad.x <= 0 :
        lad.x = 0
    
    if lad.y <= 0:
        lad.y = 0

    if lad.x >= 672:
        lad.x = 672

    if lad.y >= 672:
        lad.y = 672   

    screen.fill((0,0,0))
    draw()

pygame.quit()


