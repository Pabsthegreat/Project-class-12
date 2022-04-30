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

'''
COUNT = 0
def mom(direction,x,y):
    
    global COUNT

    if COUNT <= 15:
        if direction == 'None':
            screen.blit(rest, (x, y))
            
            COUNT += 0

        elif direction == "up":
            m = pygame.transform.rotate(Walk[COUNT], 0)
            screen.blit(m,(x,y))
            
            COUNT += 1

        elif direction == "down":
            m = pygame.transform.rotate(Walk[COUNT], 180)
            screen.blit(m,(x,y))
           
            COUNT += 1
        

        elif direction == "left":
            m = pygame.transform.rotate(Walk[COUNT], 90)
            screen.blit(m,(x,y))
            
            COUNT += 1

        elif direction == "right":
            m = pygame.transform.rotate(Walk[COUNT], -90)
            screen.blit(m,(x,y))
            
            COUNT += 1

        pygame.display.update()

    else:
        COUNT = 0
'''

#changes
'''
def draw(self):
        global screen
        self.moveit()
        
        if self.COUNT <=15:
            if self.x < self.pathx[2] - self.width and self.x > self.pathx[1] + self.width:
                right  = pygame.transform.rotate(Walk[self.COUNT], -90)
                screen.blit(right, (self.x, self.y))
                self.COUNT += 1

            elif self.x > self.pathx[2] - self.width:
                left = pygame.transform.rotate(Walk[self.COUNT], 90)
                screen.blit(left, (self.x, self.y))
                self.COUNT += 1
            
            elif self.x < self.pathx[1] + self.width:
                right = pygame.transform.rotate(Walk[self.COUNT], -90)
                screen.blit(right, (self.x, self.y))
                self.COUNT += 1

            if self.y < self.pathy[2] - self.height and self.y > self.pathy[1] + self.height:
                up = pygame.transform.rotate(Walk[self.COUNT], 0)
                screen.blit(up, (self.x, self.y))
                self.COUNT += 1

            elif self.y < self.pathy[2] and self.y > self.pathy[1]:
                down = pygame.transform.rotate(Walk[self.COUNT], 180)
                screen.blit(down, (self.x, self.y))
                self.COUNT += 1

            elif self.y < self.pathy[1] + self.height:
                up = pygame.transform.rotate(Walk[self.COUNT], -90)
                screen.blit(up, (self.x, self.y))
                self.COUNT += 1

        else:
            self.COUNT = 0

        pygame.display.update()

    def moveit(self):
        if self.x < self.pathx[2] - self.width and self.x > self.pathx[1] + self.width:
            self.x += self.vel

        elif self.x == self.pathx[2] - self.width:
            self.x -= self.vel

        elif self.x < self.pathx[1] + self.width:
            self.x += self.vel

 
        if self.y < self.pathy[2] - self.height and self.y > self.pathy[1] + self.height:
            self.y += self.vel

        elif self.y == self.pathy[2] - self.height:
            self.y -= self.vel

        elif self.y < self.pathy[1] + self.height:
            self.y += self.vel

        if self.x <= 0 :
            self.x = 0
    
        if self.y <= 0:
            self.y = 0

        if self.x >= 672:
            self.x = 672

        if self.y >= 672:
            self.y = 672   

'''
#pabs changes
'''
    def draw(self):
        global screen
        self.moveit()
        
        if self.COUNT <=15:
            if self.eventx[-1] == "start":                                      #what if end>start
                right  = pygame.transform.rotate(Walk[self.COUNT], -90)
                screen.blit(right, (self.x, self.y))
                self.COUNT += 1

            elif self.eventx[-1] == "end":
                left = pygame.transform.rotate(Walk[self.COUNT], 90)
                screen.blit(left, (self.x, self.y))
                self.COUNT += 1

            if self.eventy[-1] == "end":
                up = pygame.transform.rotate(Walk[self.COUNT], 0)
                screen.blit(up, (self.x, self.y))
                self.COUNT += 1

            elif self.eventy[-1] == "start":
                down = pygame.transform.rotate(Walk[self.COUNT], 180)
                screen.blit(down, (self.x, self.y))
                self.COUNT += 1

        else:
            self.COUNT = 0

        pygame.display.update()
        
    def moveit(self):

        if self.eventy == []:
            if self.startx == self.endx:
                self.eventx.append("0")
                
            else:
                self.eventx.append("start")

        elif self.eventx[-1] == "0":
            self.x += 0

        elif self.eventx[-1] == "start":
            self.x += self.vel

        elif self.x == self.pathx[1] - self.width:
            self.eventx.append("start")
            
        elif self.x == self.pathx[2] + self.width :
            self.x -= self.vel
            self.eventx.append("end")

        elif self.eventx[-1] == "end":
            self.x -= self.vel
#y
        if self.eventy == []:
            if self.starty == self.endy:
                self.eventy.append("0")
                
            else:
                self.eventy.append("start")

        elif self.eventy[-1] == "0":
            self.y += 0

        elif self.eventy[-1] == "start":
            self.y += self.vel

        elif self.y == self.pathy[1] + self.height:
            self.eventy.append("start")
            
        elif self.y == self.pathy[2] - self.height :
            self.y -= self.vel
            self.eventx.append("end")

        elif self.eventy[-1] == "end":
            self.y -= self.vel



        if self.x <= 0 :
            self.x = 0
    
        if self.y <= 0:
            self.y = 0

        if self.x >= 672:
            self.x = 672

        if self.y >= 672:
            self.y = 672   
'''
#change 3
'''
class rival(object):
    global Walk
    def __init__(self, x, y, width, height,startx,starty ,endx, endy): 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velx = []
        self.vely = []
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

        elif self.velx[-1] == 5:
            right  = pygame.transform.rotate(Walk[self.COUNT], -90)
            screen.blit(right, (self.x, self.y))
            self.COUNT += 1

        elif self.velx[-1] == -5:
            left = pygame.transform.rotate(Walk[self.COUNT], 90)
            screen.blit(left, (self.x, self.y))
            self.COUNT += 1

        elif self.vely[-1] == -5:
            up = pygame.transform.rotate(Walk[self.COUNT], 0)
            screen.blit(up, (self.x, self.y))
            self.COUNT += 1

        elif self.vely[-1] == 5:
            down = pygame.transform.rotate(Walk[self.COUNT], 180)
            screen.blit(down, (self.x, self.y))
            self.COUNT += 1


        pygame.display.update()

    def moveit(self):
        if self.endx == self.startx:
            self.velx.append(0)
        else:
             self.velx.append(5)

        if self.endy == self.starty:
            self.vely.append(0)
        else:
            self.vely.append(5)

        if self.x + self.width < self.pathx[2] - self.width- self.velx[-1]:
            self.x += self.velx[-1]

        elif self.x +self.width == self.pathx[2]- self.width - self.velx[-1]:
            self.velx.append(-5)
            self.x += self.velx[-1]
            

        elif self.y + self.height< self.pathy[2] - self.height - self.vely[-1]:
            self.y += self.vely[-1]

        elif self.y + self.height == self.pathy[2] - self.height  - self.vely[-1]:
            self.vely.append(-5)
            self.y += self.vely[-1]

        if self.x <= 0 :
            self.x = 0
    
        if self.y <= 0:
            self.y = 0

        if self.x >= 672:
            self.x = 672

        if self.y >= 672:
            self.y = 672   

'''