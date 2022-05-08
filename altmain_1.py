import pygame

pygame.init()

#creating the screen
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Hunter Assassin")

w1 = pygame.image.load('Hunter_Move/1.png').convert_alpha() 
w2 = pygame.image.load('Hunter_Move/2.png').convert_alpha() 
w3 = pygame.image.load('Hunter_Move/3.png').convert_alpha()
w4 = pygame.image.load('Hunter_Move/4.png').convert_alpha()
w5 = pygame.image.load('Hunter_Move/5.png').convert_alpha()
w6 = pygame.image.load('Hunter_Move/6.png').convert_alpha()
w7 = pygame.image.load('Hunter_Move/7.png').convert_alpha()
w8 = pygame.image.load('Hunter_Move/8.png').convert_alpha()
rest = pygame.image.load("Hunter_Move/8a.png").convert_alpha()
w10 = pygame.image.load('Hunter_Move/9.png').convert_alpha()
w11 = pygame.image.load('Hunter_Move/10.png').convert_alpha()
w12 = pygame.image.load('Hunter_Move/11.png').convert_alpha()
w13 = pygame.image.load('Hunter_Move/12.png').convert_alpha()
w14 = pygame.image.load('Hunter_Move/13.png').convert_alpha()
w15 = pygame.image.load('Hunter_Move/14.png').convert_alpha()
w16 = pygame.image.load('Hunter_Move/15.png').convert_alpha()

Walk = [w1,w2,w3,w4,w5,w6,w7,w8,rest,w10,w11,w12,w13,w14,w15,w16]

rest = pygame.image.load("Hunter_Move/8a.png")
rest1 = rest
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
            screen.blit(rest1, (self.x, self.y))
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

class rival(object):
    global Walk
    def __init__(self, x, y, width, height,startx,starty ,endx, endy): 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velx = 2.5
        self.vely = 2.5
        self.endx = endx
        self.endy = endy
        self.startx = startx
        self.starty = starty
        self.pathx = [self.x, startx,self.endx]
        self.pathy = [self.y, starty,self.endy]
        self.COUNT = 0  
    
    def draw(self):
        global screen
        self.moveit()
        
        if self.COUNT >= 15:
            self.COUNT = 0

        elif self.velx < 0:
            left = pygame.transform.rotate(Walk[self.COUNT], 90)
            screen.blit(left, (self.x, self.y))
            self.COUNT += 1

        elif self.velx > 0:
            right  = pygame.transform.rotate(Walk[self.COUNT], -90)
            screen.blit(right, (self.x, self.y))
            self.COUNT += 1

        elif self.vely < 0:
            up = pygame.transform.rotate(Walk[self.COUNT], 0)
            screen.blit(up, (self.x, self.y))
            self.COUNT += 1

        elif self.vely > 0:
            down = pygame.transform.rotate(Walk[self.COUNT], 180)
            screen.blit(down, (self.x, self.y))
            self.COUNT += 1


        pygame.display.update()

    def moveit(self):

        if self.startx == self.endx or self.starty == self.endy:

            if self.starty == self.endy:

                self.vely == 0

                if self.velx > 0:
                    if self.x + self.velx < self.pathx[2] - self.height:
                        self.x += self.velx
                    else:
                        self.velx = self.velx * -1
                        self.COUNT = 0
                else :
                    if self.x- self.velx >  self.pathx[1]:
                        self.x += self.velx

                    else:
                        self.velx = self.velx * -1
                        self.COUNT = 0

            elif self.startx == self.endx:

                self.velx = 0

                if self.vely > 0:
                    if self.y + self.vely < self.pathy[2] - self.height:
                        self.y += self.vely
                    else:
                        self.vely = self.vely * -1
                        self.COUNT = 0

                else:
                    if self.y - self.vely >  self.pathy[1]:
                        self.y += self.vely

                    else:
                        self.vely = self.vely * -1
                        self.COUNT =0

def maindraw():
    screen.blit(bg, (0,0))
    chad.draw()
    vlad.draw()
    lad.move()
  
    pygame.display.flip()


#game loop
lad = player(400,100,128,128)
chad = rival(100,100,128,128,128,128,800,128)
vlad = rival(100,200,128,128,256,256,256,800)
running = True
while running == True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP:

            lad.stand = True
            lad.left = True
            lad.up = False
            lad.down = False
            lad.right = False

    keys = pygame.key.get_pressed()
    
    if keys [pygame.K_LEFT] or keys [pygame.K_a] :
        lad.x -= lad.vel
        lad.left = True
        lad.up = False
        lad.down = False
        lad.right = False
        lad.stand = False
        rest1 = pygame. transform. rotate(rest, 90)


    elif keys [pygame.K_RIGHT] or keys [pygame.K_d]  :
        lad.x += lad.vel
        lad.right = True
        lad.left = True
        lad.up = False
        lad.down = False
        lad.stand = False
        rest1 = pygame. transform. rotate(rest, -90)
        
    elif keys [pygame.K_UP] or keys [pygame.K_w] :
        lad.y -= lad.vel
        lad.up = True
        lad.left = True
        lad.down = False
        lad.right = False
        lad.stand = False
        rest1 = pygame. transform. rotate(rest, 0)
        
    elif keys [pygame.K_DOWN] or keys [pygame.K_s] :
        lad.y += lad.vel
        lad.down = True
        lad.left = True
        lad.up = False
        lad.right = False
        lad.stand = False
        rest1 = pygame. transform. rotate(rest, 180)
        
    
    
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
    maindraw()
    
pygame.quit()

COUNT = 0
