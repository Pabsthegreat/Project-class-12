import pygame

pygame.init()

#creating the screen
screen = pygame.display.set_mode((800,800))

bg =  pygame.image.load('bg.png')
pygame.display.set_caption("Hunter Assassin")

icon = pygame.image.load("Hunter_Move/8a.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

#Getting images for player
h1 = pygame.image.load('Hunter_Move/1.png').convert_alpha() 
h2 = pygame.image.load('Hunter_Move/2.png').convert_alpha() 
h3 = pygame.image.load('Hunter_Move/3.png').convert_alpha()
h4 = pygame.image.load('Hunter_Move/4.png').convert_alpha()
h5 = pygame.image.load('Hunter_Move/5.png').convert_alpha()
h6 = pygame.image.load('Hunter_Move/6.png').convert_alpha()
h7 = pygame.image.load('Hunter_Move/7.png').convert_alpha()
h8 = pygame.image.load('Hunter_Move/8.png').convert_alpha()
rest = pygame.image.load("Hunter_Move/8a.png").convert_alpha()
h10 = pygame.image.load('Hunter_Move/9.png').convert_alpha()
h11 = pygame.image.load('Hunter_Move/10.png').convert_alpha()
h12 = pygame.image.load('Hunter_Move/11.png').convert_alpha()
h13 = pygame.image.load('Hunter_Move/12.png').convert_alpha()
h14 = pygame.image.load('Hunter_Move/13.png').convert_alpha()
h15 = pygame.image.load('Hunter_Move/14.png').convert_alpha()
h16 = pygame.image.load('Hunter_Move/15.png').convert_alpha()

Hunter_Walk = [h1,h2,h3,h4,h5,h6,h7,h8,rest,h10,h11,h12,h13,h14,h15,h16]
rest1 = pygame.image.load("Hunter_Move/8a.png").convert_alpha()

#Getting images for enemy
e1 = pygame.image.load('Enemy_Move/1.png').convert_alpha() 
e2 = pygame.image.load('Enemy_Move/2.png').convert_alpha() 
e3 = pygame.image.load('Enemy_Move/3.png').convert_alpha() 
e4 = pygame.image.load('Enemy_Move/4.png').convert_alpha() 
e5 = pygame.image.load('Enemy_Move/5.png').convert_alpha() 
e6 = pygame.image.load('Enemy_Move/5a.png').convert_alpha() 
e7 = pygame.image.load('Enemy_Move/5b.png').convert_alpha() 
e8 = pygame.image.load('Enemy_Move/5c.png').convert_alpha() 
REST = pygame.image.load('Enemy_Move/5d.png').convert_alpha() 
e10 = pygame.image.load('Enemy_Move/6.png').convert_alpha() 
e11 = pygame.image.load('Enemy_Move/7.png').convert_alpha() 
e12 = pygame.image.load('Enemy_Move/8.png').convert_alpha() 
e13 = pygame.image.load('Enemy_Move/9.png').convert_alpha() 
e14 = pygame.image.load('Enemy_Move/9a.png').convert_alpha() 
e15 = pygame.image.load('Enemy_Move/9b.png').convert_alpha() 
e16 = pygame.image.load('Enemy_Move/9c.png').convert_alpha() 

Enemy_Walk = [e1,e2,e3,e4,e5,e6,e7,e8,REST,e10,e11,e12,e13,e14,e15,e16]


class player(object):

    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.width = 128
        self.height = 128
        self.vel = 5
        self.dir = None
        self.COUNT = 0

    def move(self):
        global rest1

        if self.dir == None:
            screen.blit(rest1, (self.x, self.y))
            pygame.display.update()

        elif self.COUNT <= 15:

            if self.dir == "up":
                m = pygame.transform.rotate(Hunter_Walk[self.COUNT], 0)
                screen.blit(m,(self.x,self.y))
                pygame.display.update()

            if self.dir == "down":
                m = pygame.transform.rotate(Hunter_Walk[self.COUNT], 180)
                screen.blit(m,(self.x,self.y))
                pygame.display.update()

            if self.dir == "right":
                m = pygame.transform.rotate(Hunter_Walk[self.COUNT], -90)
                screen.blit(m,(self.x,self.y))
                pygame.display.update()

            if self.dir == "left":
                m = pygame.transform.rotate(Hunter_Walk[self.COUNT], 90)
                screen.blit(m,(self.x,self.y))
                pygame.display.update()

            self.COUNT += 1
            
        else:
            self.COUNT = 0

    def kill():
        pass

class rival(object):
    global Enemy_Walk
    def __init__(self, x, y, width, height ,endx, endy): 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 2.5
        self.startx = x
        self.starty = y
        self.endx = endx
        self.endy = endy
        self.count = 0  
        self.facing = ''
        self.dir = 'Front'
        self.DIR = ''
    
    def draw(self):
        global screen
        
        while self.dir == 'Front':

            if self.endx > self.endy:
                self.DIR = 'SIDEWAYS'

                if self.count <= 15:
                    if self.x <= self.endx - self.width and self.x >= self.startx:
                        right  = pygame.transform.rotate(Enemy_Walk[self.count], -90)
                        screen.blit(right, (self.x, self.y))
                        self.count += 1
                        self.x += self.vel
                        pygame.display.update()

                    else:
                        left = pygame.transform.rotate(Enemy_Walk[self.count], 90)
                        screen.blit(left, (self.x, self.y))
                        self.count += 1
                        self.dir == 'Back'
                        pygame.display.update()
                        break
                    

                else:
                    self.count = 0

                    

            else:
                self.DIR = 'UPDOWN'
                
                if self.count <= 15:
                    if self.y <= self.endy - self.width and self.y >= self.starty:
                        down  = pygame.transform.rotate(Enemy_Walk[self.count], 180)
                        screen.blit(down, (self.x, self.y))
                        self.count += 1
                        self.y += self.vel
                        pygame.display.update()

                    else:
                        up = Enemy_Walk[self.count]
                        screen.blit(up, (self.x, self.y))
                        self.count += 1
                        self.dir == 'Back'
                        pygame.display.update()
                        break
                else:
                    self.count = 0

                
            

        while self.dir == 'Back':

            if self.endx > self.endy:
                self.DIR = 'SIDEWAYS'

                if self.count <= 15:
                    if self.x >= self.startx:
                        left  = pygame.transform.rotate(Enemy_Walk[self.count], 90)
                        screen.blit(left, (self.x, self.y))
                        self.count += 1
                        self.x -= self.vel
                        pygame.display.update()
                    
                    else:
                        right = pygame.transform.rotate(Enemy_Walk[self.count], -90)
                        screen.blit(right, (self.x, self.y))
                        self.count += 1
                        self.dir == 'Front'
                        pygame.display.update()
                        break
                
                else:
                    self.count = 0

                
            else:
                self.DIR = 'UPDOWN'

                if self.count <= 15:
                    if self.y >= self.starty:
                        up  = Enemy_Walk[self.count]
                        screen.blit(up, (self.x, self.y))
                        self.count += 1
                        self.y -= self.vel
                        pygame.display.update()
                    
                    else:
                        down = pygame.transform.rotate(Enemy_Walk[self.count], 180)
                        screen.blit(down, (self.x, self.y))
                        self.count += 1
                        self.dir == 'Front'
                        pygame.display.update()
                        break
                
                else:
                    self.count = 0

    
'''
    def shoot(self):
        if self.facing == 'RIGHT':
            if self.x - lad.x <= 256:
                bullet(self.x,self.y)
        
        elif self.facing == 'LEFT':
            if lad.x - self.x <= 256:
                bullet(self.x,self.y)

        elif self.facing == 'DOWN':
            if self.y - lad.y <= 256:
                bullet(self.x,self.y)

        elif self.facing == 'UP':
            if lad.y - self.y <= 256:
                bullet(self.x,self.y)

 
class bullet(object):
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 5
        self.vel = 10
        
    def draw(self,screen):
        pygame.draw.rect(screen,(255, 215, 0), (self.x,self.y,self.width,self.height))
        pygame.display.update()
'''

#setting up players
lad = player(400,100)
chad = rival(128,128,128,128,800,128)
vlad = rival(256,256,128,128,256,800)


def maindraw():
    screen.blit(bg, (0,0))
    chad.draw()
    vlad.draw()
    lad.move()
    '''bullet.draw(screen)'''
    pygame.display.flip()

'''bullets = [] '''

#game loop
running = True
while running == True:
    clock.tick(64)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP:
            lad.dir = None
        
        if event.type == pygame.K_SPACE:
            lad.kill()

    '''for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel  
        else:
            bullets.pop(bullets.index(bullet))'''

    keys = pygame.key.get_pressed()
    
    #player movement
    if keys [pygame.K_LEFT] or keys [pygame.K_a]  :
        lad.x -= lad.vel
        lad.dir = "left"
        rest1 = pygame.transform.rotate(rest, 90)

    elif keys [pygame.K_RIGHT] or keys [pygame.K_d]  :
        lad.x += lad.vel
        lad.dir = "right"
        rest1 = pygame.transform.rotate(rest, -90)

    elif keys [pygame.K_UP] or keys [pygame.K_w]:
        lad.y -= lad.vel
        lad.dir = "up"
        rest1 = pygame.transform.rotate(rest, 0)

    elif keys [pygame.K_DOWN] or keys [pygame.K_s]  :
        lad.y += lad.vel
        lad.dir = "down"
        rest1 = pygame.transform.rotate(rest, 180)     
     

    if lad.x <= 0 :
        lad.x = 0
    
    if lad.y <= 0:
        lad.y = 0

    if lad.x >= 672:
        lad.x = 672

    if lad.y >= 672:
        lad.y = 672

    screen.fill((152,251,152))
    maindraw()

pygame.quit()
