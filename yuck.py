'''
Co-ordinate systems work differently in pygame as in real math. The origin is in the top-left corner 
and +x-axis is towards right & +y-axis is towards down. Quadrant 1 is bottom right, Quadrant 2 is bottom left,
Quadrant 3 is top left, and Quadrant 4 is top right.
'''
from textwrap import fill
import pygame
import math

pygame.init()
pygame.font.init()
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
bullet = pygame.image.load('pics/Bullet.png').convert_alpha() 
pygame.display.set_icon(rest)

bg =  pygame.image.load('pics/1200x800.png')

clock = pygame.time.Clock()

score = 0

class player(object):
    def __init__(self, x, y): 
        self.x = x                  #player co-ordinates
        self.y = y  
        self.width = 128            #image size
        self.height = 128
        self.vel = 5
        self.dir = None             #used to change directions as arrow keys/ wasd is pressed
        self.COUNT = 0              #variable used to iterate thru the list of player images 
        self.health = 100
        self.hit = 0
        self.die = False


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
            self.COUNT = 0  #resets iteration variable to prevent index out of range error
        

    def health(self):
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(100, 45, 100, 20))
        
        if self.hit == 0:
            color = (0,255,0)
            pygame.draw.rect(screen, color, pygame.Rect(100, 45, self.health, 20))

        elif self.hit >= 40 and self.hit < 80:
            color = (255, 255, 0)
            self.health = 75
            pygame.draw.rect(screen,color, pygame.Rect(100, 45, self.health, 20))
            
        elif self.hit >= 80 and self.hit < 120:
            self.health = 50
            color = (255,165,0)
            pygame.draw.rect(screen,color, pygame.Rect(100, 45, self.health, 20))

        elif self.hit >= 120 and self.hit < 160:
            self.health = 25
            color = (255,0,0)
            pygame.draw.rect(screen,color, pygame.Rect(100, 45, self.health, 20))

        elif self.hit >= 160:
            color = (0,0,0)
            self.health = 0
            pygame.draw.rect(screen,color, pygame.Rect(100, 45, self.health, 20))


        


class rival(object):
    global Enemy_Walk                                           #list of enemy images
    def __init__(self,startx,starty ,endx, endy,name): 
        self.name = name
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
        self.shoot_cooldown = 0

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
        self.die()
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
        
        

        if dir == 'u' and y > 0 :
            turn = math.degrees (math.atan(x/y))
            self.Angle = turn
            if (self.Angle <= endAngle1 and self.Angle >= endAngle2) and (rivalradius < radius):
                rival.shoot(self)
                self.theta = self.Angle
                self.shoot_cooldown -= 1
            else:
                self.move = True
                self.vely = -2.5

        elif dir == 'd' and y < 0:
            turn = math.degrees (math.atan(x/y))
            self.Angle =  turn

            if (self.Angle <= endAngle1 and self.Angle >= endAngle2) and (rivalradius < radius): 
                rival.shoot(self)
                self.theta = self.Angle + 180  
                self.shoot_cooldown -= 1                                    
            else:                                                      
                self.move = True
                self.vely = 2.5

    
        elif dir == 'l' and x > 0:
            turn = math.degrees (math.atan(y/x))
            self.Angle = turn 
            if (self.Angle <= endAngle1 and self.Angle >= endAngle2) and (rivalradius < radius):
                rival.shoot(self)
                self.theta = -self.Angle + 90
                self.shoot_cooldown -= 1
            else:
                self.move = True
                self.velx = -2.5


        elif dir == 'r' and x < 0:
            turn = math.degrees (math.atan(y/x))
            self.Angle =  -turn 

            if (self.Angle <= endAngle1 and self.Angle >= endAngle2) and (rivalradius < radius):
                rival.shoot(self)
                self.theta = self.Angle - 90
                self.shoot_cooldown -= 1
            else:
                self.move = True
                self.velx = 2.5

    def shoot(self):                                                        #fn called in checkPoint()
        
        self.velx = 0
        self.vely = 0
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 20
            bulletss(self.x,self.y,lad.x,lad.y,self.theta)

    def die(self):
        global score, enemy_dict

        if (self.x < lad.x + 64 < self.x + 128) and (self.y < lad.y + 64 < self.y + 128) and keys[pygame.K_SPACE]:
            enemy_dict [self.name] = None
            score += 100
        
        


class bulletss(object):
    bullet_list = []
    vel = 30
    def __init__(self,ex,ey,px,py,theta1):
        self.thetaa = theta1
        if len(self.bullet_list) < 5:
            theta = math.atan2((py - ey),(px - ex))
            sin = math.sin(theta)
            cos = math.cos(theta)
            
            if sin >= 0 and cos >= 0:
                Q = 1

            elif sin >= 0 and cos <= 0:
                Q = 2
            
            elif sin <= 0 and cos <= 0:
                Q = 3
            
            elif sin <= 0 and cos >= 0:
                Q = 4

            self.bullet_list.append([ex + 64 ,ey + 64, cos, sin, self.thetaa])

        else:
            self.bullet_list.pop()
    

    def movebull(self,i): 
        i[0] += self.vel * i[2]
        i[1] += self.vel * i[3]

        bulletss.delete(self,i)
        

    def delete(self,i):
        
        if i[0] > 1200 or i[1] > 800 or i[1] < 0 or i[0] < 0:
            self.bullet_list.remove(i)

        elif (i[0] > lad.x) and (i[0] < lad.x + 128)  and (i[1] > lad.y) and (i[1] < lad.y + 128):
            lad.health -= 20
            self.bullet_list.remove(i)            

    
    

font = pygame.font.SysFont('Georgia', 25)

health_text = font.render('Health: ', False, (0, 0, 0),(122,122,122))

def maindraw():                                 #draws all characters on screen
    screen.blit(bg, (0,0))
    for enemy in enemy_dict:
        if enemy_dict[enemy] != None:
            enemy_dict[enemy].draw()
    lad.draw()
    player.health(lad)
    score_text = font.render('Score: {}'.format(score), False, (0, 0, 0),(122,122,122))
    screen.blit(score_text, (0,0))
    screen.blit(health_text, (0,40))
    timelabel = font.render("Time - {} s".format(seconds), False, (0,0,0), (122,122,122))
    screen.blit(timelabel,(1050,0))
    

    if len(bulletss.bullet_list) != 0:
        i = bulletss.bullet_list[j]
        dishoom = pygame.transform.rotate(bullet,i[4])  
        screen.blit(dishoom, (i[0], i[1]))                             #displays bullet on screen
        bulletss.movebull(bulletss,i)
    pygame.display.update()                     #updates screen to show all characters 
    
#assigning values and co-ordinates to player and rivals
lad = player(512,128)
chad = rival(308,300,1072,300,'chad')
vlad = rival(128,128,128,800,'vlad')
mad = rival(700,600,1072,600,'mad')
thug = rival(900,400,900,800,'thug')
not_running_dict = {'mad': mad,'thug':thug}
enemy_dict = {'chad':chad,'vlad':vlad}

milliseconds = 0
seconds = 0
new_guy_timer = 0
minutes = 0


j = 0
running = True
while running:                                                 #game loop
    clock.tick(60)                                                     #30 ms delay for better accuracy

    for event in pygame.event.get():                                
        if event.type == pygame.QUIT:                                  #if game is closed
            running = False

        if event.type == pygame.KEYUP:                                 #if no key is pressed
            lad.dir = None
        
    if lad.health == 0:
        running = False
        

    if j < len(bulletss.bullet_list) - 1:
        j += 1
    else:
        j = 0

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
    
    
    milliseconds += clock.tick_busy_loop(150)
    if milliseconds > 150:
        seconds += 1
        new_guy_timer += 1
        milliseconds -= 150

    if new_guy_timer == 10:

        if len(not_running_dict) != 0:
            x = not_running_dict.popitem()
            enemy_dict [x[0]] = x[1]
        
        new_guy_timer = 0
    
#character does not go out of bounds 
    if lad.x <= 0 :                                                     
        lad.x = 0
    
    if lad.y <= 0:
        lad.y = 0

    if lad.x >= 1072:
        lad.x = 1072

    if lad.y >= 672:
        lad.y = 672   

    screen.fill((0,0,0))
    maindraw()                                                         #all draw functions are called here
    
pygame.quit()                                                          #closes pygame

