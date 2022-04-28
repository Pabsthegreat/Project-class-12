import pygame

pygame.init()

#creating the screen
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Hunter Assassin")

icon = pygame.image.load("Resting-01.png")
pygame.display.set_icon(icon)

runL = pygame.image.load('sprite.gif')
runR = pygame.image.load('sprite.gif')
stand = pygame.image.load('Resting-01.png')
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
        self.STAND = False

    def charmove(self):
        global stand1, runR1, runL1, screen 

        if self.STAND == True:
            screen.blit(stand1, (self.x,self.y))
        
        elif self.up == True:
            screen.blit(runR1, (self.x,self.y))
            pygame.display.update()
            screen.blit(runL1, (self.x,self.y))

        elif self.down == True:
            
            screen.blit(runR1, (self.x,self.y))
            pygame.display.update()
            screen.blit(runL1, (self.x,self.y))

        elif self.right == True:
            screen.blit(runR1, (self.x,self.y))
            pygame.display.update()
            screen.blit(runL1, (self.x,self.y))

        elif self.left == True:
            screen.blit(runR1, (self.x,self.y))
            pygame.display.update()
            screen.blit(runL1, (self.x,self.y))

        pygame.display.update()
    
def draw():
    screen.blit(bg, (0,0))
    lad.charmove()
    pygame.display.update()


#game loop
lad = player(400,100,128,128)
running = True
while running == True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys [pygame.K_LEFT] or keys [pygame.K_a] :
        lad.x -= lad.vel
        lad.left = True
        runR1 = pygame. transform. rotate(runR, 90)
        runL1 = pygame. transform. rotate(runL, 90)
        stand1 = pygame. transform. rotate(stand, 90)

    elif keys [pygame.K_RIGHT] or keys [pygame.K_d]  :
        lad.x += lad.vel
        lad.right = True
        runR1 = pygame. transform. rotate(runR, -90)
        runL1 = pygame. transform. rotate(runL, -90)
        stand1 = pygame. transform. rotate(stand, -90)

    elif keys [pygame.K_UP] or keys [pygame.K_w] :
        lad.y -= lad.vel
        lad.up = True
        runR1 = pygame. transform. rotate(runR, 0)
        runL1 = pygame. transform. rotate(runL, 0)
        stand1 = pygame. transform. rotate(stand, 0)

    elif keys [pygame.K_DOWN] or keys [pygame.K_s] :
        lad.y += lad.vel
        lad.down = True
        runR1 = pygame.transform.rotate(runR, 180)
        runL1 = pygame.transform.rotate(runL, 180)
        stand1 = pygame. transform. rotate(stand, 180)
    
    if keys [pygame.KEYUP]:
        lad.STAND = True
      
    

#have to do it this was , as "and", "or" together in the previous method was not working when awsd was added
    if lad.x <= 0 :
        lad.x = 0
    
    if lad.y <= 0:
        lad.y = 0

    if lad.x >= 672:
        lad.x = 672

    if lad.y >= 672:
        lad.y = 672   

    draw()

pygame.quit()