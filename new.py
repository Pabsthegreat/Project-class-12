from re import X

import pygame
import math



pygame.init()

#creating the screen
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Hunter Assassin")

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

bullets = pygame.image.load('pics/Bullet.png').convert_alpha() 

rest = pygame.image.load("Hunter_Move/8a.png")
rest1 = rest
icon = pygame.image.load("Hunter_Move/8a.png")
pygame.display.set_icon(icon)

bg =  pygame.image.load('pics/bg.png')

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width,height): 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.dir = None
        self.COUNT = 0


    def move(self):
        if self.dir == None:
            screen.blit(rest1, (self.x, self.y))
            pygame.display.update()

        elif self.COUNT <= 15:

            if self.dir == "up":
                m = pygame.transform.rotate(Hunter_Walk[self.COUNT], 0)
                screen.blit(m,(self.x,self.y))
            

            elif self.dir == "down":
                m = pygame.transform.rotate(Hunter_Walk[self.COUNT], 180)
                screen.blit(m,(self.x,self.y))
                

            elif self.dir == "right":
                m = pygame.transform.rotate(Hunter_Walk[self.COUNT], -90)
                screen.blit(m,(self.x,self.y))
                

            elif self.dir == "left":
                m = pygame.transform.rotate(Hunter_Walk[self.COUNT], 90)
                screen.blit(m,(self.x,self.y))

            pygame.display.update()

            self.COUNT += 1
            
        else:
            self.COUNT = 0

class rival(object):
    global Enemy_Walk
    def __init__(self, x, y, width, height,startx,starty ,endx, endy): 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velx = 2.5
        self.vely = 2.5
        self.endx = endx
        self.endy = endy
        self.dir = ''
        self.startx = startx
        self.starty = starty
        self.pathx = [self.x, startx,self.endx]
        self.pathy = [self.y, starty,self.endy]
        self.COUNT = 0  
        self.angle = 0
        self.Angle = 0
        self.theta = 0
        self.a = math.degrees (math.pi)

    def draw(self):
        global screen,dir
        self.moveit()
        
        if self.COUNT >= 15:
            self.COUNT = 0

        elif self.velx < 0:
            left = pygame.transform.rotate(Enemy_Walk[self.COUNT], 90)
            screen.blit(left, (self.x, self.y))
            self.COUNT += 1
            self.dir = 'l'
            self.angle = 0
            

        elif self.velx > 0:

            right  = pygame.transform.rotate(Enemy_Walk[self.COUNT], -90)
            screen.blit(right, (self.x, self.y))
            self.COUNT += 1
            self.dir = 'r'
            self.angle = self.a 

        elif self.vely < 0:
            up = pygame.transform.rotate(Enemy_Walk[self.COUNT], 0)
            screen.blit(up, (self.x, self.y))
            self.COUNT += 1
            self.dir = 'u'
            self.angle = -self.a/2

        elif self.vely > 0:
            down = pygame.transform.rotate(Enemy_Walk[self.COUNT], 180)
            screen.blit(down, (self.x, self.y))
            self.COUNT += 1
            self.dir = 'd'
            self.angle = self.a/2
        
        else:
            shoot = pygame.transform.rotate(Enemy_Walk[8], self.theta)
            screen.blit(shoot, (self.x, self.y))
        

    def moveit(self):
        global lad 

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

        rival.checkPoint(self, 200 , lad.x, lad.y, self.x, self.y , self.angle, self.dir)

    def shoot(self):
        self.velx = 0
        self.vely = 0
        if self.dir== 'r':
            
            self.theta = self.angle - self.Angle        
            bulletss(self.x,self.y+bull.vel)
            bulletss.draw(bull)

        elif self.dir == 'l':
            
            self.theta = self.angle - self.Angle
            bulletss(self.x,self.y+bull.vel)
            bulletss.draw(bull)
        
        elif self.dir == 'd':
            self.theta = self.angle - self.Angle          
            bulletss(self.x + bull.vel,self.y)
            bulletss.draw(bull1)
        
        elif self.dir == 'u':
            
            self.theta = self.angle - self.Angle
            bulletss(self.x + bull.vel,self.y)
            bulletss.draw(bull1)
        
                 

    def checkPoint(self,radius, rx,ry , selfx ,selfy , startAngle, dir): 
        
        endAngle1 = math.degrees ( self.a /3 + startAngle)
        endAngle2 = int(math.degrees ( - self.a / 3 + startAngle))

        x =  selfx - rx 
        y =  selfy - ry 
        
        polarradius = math.sqrt(x * x + y * y)

        if dir == 'u':
            
            if x == 0:
                self.Angle = 270
            elif x > 0:
                self.Angle =  270 - math.degrees (math.atan(x/y))
            else:
                self.Angle =  270 - math.degrees(math.atan(x/y))

            if (self.Angle >= startAngle and self.Angle <= endAngle1 and polarradius <= radius and polarradius >=0 ):
                    print("Point (", x, ",", y, ") exist in the circle sector") 
                    self.theta = self.Angle
                    rival.shoot(self)
                    print("up")
            else:
                pass

        elif dir == 'd':
            if x == 0:
                self.Angle = 270
            elif x > 0:
                self.Angle = 270 - math.degrees (math.atan(x/y))
            else:
                self.Angle = 270 - math.degrees (math.atan(x/y))

            if ( self.Angle >= startAngle and self.Angle <= endAngle1 and polarradius <= radius and polarradius >=0 ):
                    print("Point (", x, ",", y, ") exist in the circle sector") 
                    self.theta = self.Angle
                    print("down")
                    rival.shoot(self)
            else:
                pass
        
        elif dir == 'l':
            if y == 0:
                self.Angle = 270
            
            elif x == 0:
                endAngle1 +=1
            elif y > 0:
                self.Angle = 270 + math.degrees (math.atan(y/x))
            elif y < 0:
                self.Angle = 270 + math.degrees (math.atan(y/x))

            if ( self.Angle >= startAngle and self.Angle <= endAngle1 and polarradius <= radius and polarradius >=0 ):
                    print("Point (", x, ",", y, ") exist in the circle sector") 
                    self.theta = self.Angle
                    rival.shoot(self)
            else:
                pass

        

        elif dir == 'r':
            if y == 0:
                self.Angle = 270
            elif x == 0:
                endAngle1 +=1

            elif y > 0:
                self.Angle =  270 + math.degrees (math.atan(y/x))
            elif y < 0:
                self.Angle = 270 + math.degrees (math.atan(y/x))

            if ( self.Angle >= startAngle and self.Angle <= endAngle1 and polarradius <= radius and polarradius >=0 ):
                    print("Point (", x, ",", y, ") exist in the circle sector") 
                    self.theta = self.Angle
                    rival.shoot(self)
            else:
                pass
        

    
 
class bulletss(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 20
        self.vel = 30
        
            
    def draw(self):
        self.x, self.y
        screen.blit(bullets,(self.x, self.y))
    
    #update and draw  

def maindraw():
    screen.blit(bg, (0,0))
    chad.draw()
    vlad.draw()
    lad.move()
    pygame.display.update()

#game loop
lad = player(512,128,128,128)
chad = rival(100,100,128,128,128,128,800,128)
vlad = rival(100,200,128,128,256,256,256,800)
bull = bulletss(vlad.x,vlad.y)
bull1 = bulletss(chad.x,chad.y)
b = [bull,bull1]

running = True
while running == True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP:

            lad.dir = None

        #for bull in b:
            #if bull.x < 500 and bull.x > 0:
                #bull.x += bull.vel
            #else:
                #b.pop(b.index(bull))

    keys = pygame.key.get_pressed()
    
    if keys [pygame.K_LEFT] or keys [pygame.K_a] :
        lad.x -= lad.vel
        lad.dir = "left"
        rest1 = pygame. transform. rotate(rest, 90)


    elif keys [pygame.K_RIGHT] or keys [pygame.K_d]  :
        lad.x += lad.vel
        lad.dir = "right"
        rest1 = pygame. transform. rotate(rest, -90)
        
    elif keys [pygame.K_UP] or keys [pygame.K_w] :
        lad.y -= lad.vel
        lad.dir = "up"
        rest1 = pygame. transform. rotate(rest, 0)
        
    elif keys [pygame.K_DOWN] or keys [pygame.K_s] :
        lad.y += lad.vel
        lad.dir = "down"
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

#if vlad.dir == left:
    #facing = -1
#else:
    #facing = 1

#if len(b) < 5:  # This will make sure we cannot exceed 5 bullets on the screen at once
   ## b.append((round(vlad.x+vlad.width//2), round(vlad.y + vlad.height//2), 6, (0,0,0), facing)) 
#pygame.quit()