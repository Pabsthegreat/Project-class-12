'''
Co-ordinate systems work differently in pygame as in real math. The origin is in the top-left corner 
and +x-axis is towards right & +y-axis is towards down. Also up is taken as 0 deg and angles are measured counter-clockwise.
'''
from re import X
from tokenize import maybe
from xml.dom.expatbuilder import theDOMImplementation

import pygame
import math

pygame.init()

#creating the screen
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Hunter Assassin")

# loading all images of player
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

#loading images of enemy
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

rest1 = rest
bullets = pygame.image.load('pics/Bullet.png').convert_alpha() 
pygame.display.set_icon(rest)

bg =  pygame.image.load('pics/1200x800.png')

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y): 
        self.x = x                  #player co-ordinates
        self.y = y
        self.width = 128            #image size
        self.height = 128
        self.vel = 5
        self.dir = None             #used to change directions as arrow keys/ wasd is pressed
        self.COUNT = 0              #variable used to iterate thru the list of player images 


    def draw(self):                                                             #called in maindraw

        if self.dir == None:
            screen.blit(rest1, (self.x, self.y))

        elif self.COUNT <= 15:                                                  #no. of images in list = 16, => max index = 15

            if self.dir == "up":
                m = pygame.transform.rotate(Hunter_Walk[self.COUNT], 0)                 #turns player to reqd direction
                screen.blit(m,(self.x,self.y))                                          #displays character onto screen
            
            elif self.dir == "down":
                m = pygame.transform.rotate(Hunter_Walk[self.COUNT], 180)
                screen.blit(m,(self.x,self.y))
                
            elif self.dir == "right":
                m = pygame.transform.rotate(Hunter_Walk[self.COUNT], -90)
                screen.blit(m,(self.x,self.y))
                
            elif self.dir == "left":
                m = pygame.transform.rotate(Hunter_Walk[self.COUNT], 90)
                screen.blit(m,(self.x,self.y))

            self.COUNT += 1                                     #increment iterable to display next image
            
        else:
            self.COUNT = 0  
        color = (255,0,0)                                   #resets iteration variable to prevent index out of range error
        pygame.draw.rect(screen, color, pygame.Rect(self.x, self.y, 64, 64),  2)
        
class rival(object):
    global Enemy_Walk                                           #list of enemy images
    def __init__(self,startx,starty ,endx, endy): 
        self.x = startx                                              #rival co-ordinates
        self.y = starty
        self.width = 64                                             #image size
        self.height = 64
        self.velx = 2.5
        self.vely = 2.5
        self.startx = startx                                         #initial and final x & y co-ordinates since
        self.starty = starty                                         #character moves in a fixed path (straight line)
        self.endx = endx
        self.endy = endy
        self.dir = ''                                                #acts as flag variable used in checkPoint()
        self.pathx = [self.x, self.startx, self.endx]                 #path taken by rival
        self.pathy = [self.y, self.starty, self.endy]
        self.COUNT = 0                                                #iterabe to go thru list of images
        self.Angle = 0                                                #Angle by which rival is supposed to turn 
        self.theta = 0                                        #The angle by which rival must turn if player is in range wrt his initial posn
        self.move = True


    def draw(self):                                                   #fn called in maindraw()
        global screen
        self.moveit()                                                 #moves the player
        
        if self.COUNT > 15:                                           #no. of images in list = 16, => max index = 15
            self.COUNT = 0

        elif self.velx < 0:
            left = pygame.transform.rotate(Enemy_Walk[self.COUNT], 90)              #rival faces left
            screen.blit(left, (self.x, self.y))                                     #display change on screen
            self.COUNT += 1                                                  #increment iterable variables which goes thru images
            self.dir = 'l'                                                          #facing left

        
        elif self.velx > 0:
            right  = pygame.transform.rotate(Enemy_Walk[self.COUNT], -90)         #rightfacing
            screen.blit(right, (self.x, self.y))
            self.COUNT += 1
            self.dir = 'r'


        elif self.vely < 0:                                                     #moving up
            up = pygame.transform.rotate(Enemy_Walk[self.COUNT], 0) 
            screen.blit(up, (self.x, self.y))
            self.COUNT += 1
            self.dir = 'u'


        elif self.vely > 0:                                                      #moving down
            down = pygame.transform.rotate(Enemy_Walk[self.COUNT], 180)
            screen.blit(down, (self.x, self.y))
            self.COUNT += 1
            self.dir = 'd'

        
        else:                                                                   #rival stops moving in order to shoot
            shoot = pygame.transform.rotate(Enemy_Walk[8], self.theta)
          #turns by theta angle
            screen.blit(shoot, (self.x, self.y))                                #displayed on screen


    def moveit(self):                                                           #fn called in draw()
        global lad 
        if self.move:
            if self.starty == self.endy:                                  #if y co-ordinates are same => rival moves along x-axis
                self.vely = 0                                                   #no movement along y-axis

                if self.velx > 0:                                               #if rival is moving forward (towards right)
                    if self.x + self.velx < self.pathx[2] - self.height:        #check if character has reached the end
                        self.x += self.velx                                     #if no, move right with velx speed
                    else:                                                       #if yes, make velx negative so it enters next condn.
                        self.velx = self.velx * -1
                        
                else :                                                          #rival is moving backwards
                    if self.x- self.velx >  self.pathx[1]:                      #check if character has reached the beginning
                        self.x += self.velx                                     #if no, move left with velx speed(move right with -velx speed)
                    else:                                                       #if yes, make velx positive so it enters prev condn.
                        self.velx = self.velx * -1
                    
            elif self.startx == self.endx:
                self.velx = 0

                if self.vely > 0:
                    if self.y + self.vely < self.pathy[2] - self.height:
                        self.y += self.vely
                    else:
                        self.vely = self.vely * -1
                        

                else:
                    if self.y - self.vely >  self.pathy[1]:
                        self.y += self.vely
                    else:
                        self.vely = self.vely * -1          

        rival.checkPoint(self, lad.x, lad.y, self.x, self.y , self.dir)     #checks if player is in rival's field


    def checkPoint(self,playerx, playery , selfx ,selfy , dir):                  #fn called in moveit()

       
        radius = 200
        endAngle1 =  + 60
        endAngle2 =  - 60

        x =  selfx - playerx  #dist btw player and rival
        y =  selfy - playery 
        
        rivalradius = math.sqrt(x * x + y * y)
        
        
        if rivalradius > radius:
            self.move = True

        else:
            if dir == 'u' and y > 0 :
                turn = math.degrees (math.atan(x/y))
                self.Angle = turn
                if (self.Angle <= endAngle1 and self.Angle >= endAngle2):
                    rival.shoot(self)
                    self.theta = self.Angle
                else:
                    self.move = True
                    self.vely = -2.5

            elif dir == 'd' and y < 0:
                turn = math.degrees (math.atan(x/y))
                self.Angle =  turn

                if (self.Angle <= endAngle1 and self.Angle >= endAngle2): #print(self.Angle, ,endAngle1, endAngle2, dir)
                    rival.shoot(self)
                    self.theta = self.Angle + 180                                      #print("Point (", lad.x, ",", lad.y, ") exist in the circle sector") 
                else:                                                      
                    self.move = True
                    self.vely = 2.5

        
            elif dir == 'l' and x > 0:
                turn = math.degrees (math.atan(y/x))
                self.Angle = turn 
                if (self.Angle <= endAngle1 and self.Angle >= endAngle2):
                    rival.shoot(self)
                    self.theta = -self.Angle + 90
                else:
                    self.move = True
                    self.velx = -2.5


            elif dir == 'r' and x < 0:
                turn = math.degrees (math.atan(y/x))
                self.Angle =  -turn 
  
                if (self.Angle <= endAngle1 and self.Angle >= endAngle2):
                    rival.shoot(self)
                    self.theta = self.Angle - 90
                else:
                    self.move = True
                    self.velx = 2.5


    def shoot(self):                                                        #fn called in checkPoint()
        self.velx = 0
        self.vely = 0

        if self.dir== 'r':
            bx = self.x
            by = self.y                                  #bx,by are the coordinates of the gun, we use bx,by to get the bullet to start from the gun
            bull = bulletss(bx,by)
            bulletss.draw(bull,self.theta,self.dir)

        elif self.dir == 'l':
            bx = self.x
            by = self.y 
            bull = bulletss(bx,by)
            bulletss.draw(bull,self.theta,self.dir)
        
        elif self.dir == 'd':
            bx = self.x 
            by = self.y      
            bull = bulletss(bx,by)
            bulletss.draw(bull,self.theta,self.dir)
        
        elif self.dir == 'u':
            bx = self.x 
            by = self.y 
            bull = bulletss(bx,by)
            bulletss.draw(bull,self.theta,self.dir)

class bulletss(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 20
        self.vel = 30
        self.endbx = 1200 - self.width
        self.endby = 800 - self.height

            
    def draw(self,theta,dir):                                           #fn called in rival.shoot()
        dir = dir
        self.theta = theta   
        self.movebull(dir,lad.x,lad.y)                                         #moves bullet to attack player
        dishoom = pygame.transform.rotate(bullets, self.theta + 90)             
        screen.blit(dishoom, (self.x, self.y))                             #displays bullet on screen

 
    def movebull(self,dir,plx,ply): 
        dir = dir                          
            
        #fn called in draw()
        #if self.x == self.endbx or self.y == self.endby:
                #self.vely = 0
                #self.velx = 0
                #kill sprite

        
        if dir == 'r':
            pass

        if dir == 'l':
            pass

        if dir == 'u':
            pass


        if dir == 'd':
            pass
#put calc end value instead of plx,ply

        rad = math.atan2(plx-self.y,ply-self.y)
        dist = math.hypot(plx-self.x, ply-self.y)/2
        dx = math.cos(rad)*2
        dy = math.sin(rad)*2
        dist = int(dist)

        while dist:
            dist -= 1
            self.x += dx
            self.y += dy
            print(self.x,self.y,dist)   

    
    #update and draw  

def maindraw():                                 #draws all characters on screen
    screen.blit(bg, (0,0))
    chad.draw()
    vlad.draw()
    lad.draw()
    pygame.display.update()                     #updates screen to show all characters 

#assigning values and co-ordinates to player and rivals
lad = player(512,128)
chad = rival(128,128,800,128)
vlad = rival(128,128,128,800)

running = True
while running == True:                                                 #game loop
    clock.tick(30)                                                     #30 ms delay for better accuracy

    for event in pygame.event.get():                                
        if event.type == pygame.QUIT:                                  #if game is closed
            running = False

        if event.type == pygame.KEYUP:                                 #if no key is pressed
            lad.dir = None


    keys = pygame.key.get_pressed()                                    #list of all keys on keyboard
    
    if keys [pygame.K_LEFT] or keys [pygame.K_a] :                     #when the left arrow key or 'a' is pressed,
        lad.x -= lad.vel                                               #player co-ordinate changes with assigned velocity,
        lad.dir = "left"                                               #direction is assigned as left.
        rest1 = pygame. transform. rotate(rest, 90)                    #in case key is released, character remains facing left


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
        
    
#character does not go out of bounds 
    if lad.x <= 0 :                                                     
        lad.x = 0
    
    if lad.y <= 0:
        lad.y = 0

    if lad.x >= 672:
        lad.x = 672

    if lad.y >= 672:
        lad.y = 672   

    screen.fill((0,0,0))
    maindraw()                                                         #all draw functions are called here
    
pygame.quit()                                                          #closes pygame

COUNT = 0

#if len(b) < 5:  # This will make sure we cannot exceed 5 bullets on the screen at once
   ## b.append((round(vlad.x+vlad.width//2), round(vlad.y + vlad.height//2), 6, (0,0,0), facing)) 
#pygame.quit()

#for bull in b:
            #if bull.x < 500 and bull.x > 0:
                #bull.x += bull.vel
            #else:
                #b.pop(b.index(bull))