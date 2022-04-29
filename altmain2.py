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

#fuck this shit im sleeping , see you tomorrow ,im starting enemy tomorrow

    def draw(self):
        global screen
        self.moveit()
        if self.COUNT >= 15:
            self.COUNT = 0

        if self.right == True:
            right  = pygame.transform.rotate(Walk[self.COUNT], -90)
            screen.blit(right, (self.x, self.y))
            self.COUNT += 1

        if self.left == True:
            left = pygame.transform.rotate(Walk[self.COUNT], 90)
            screen.blit(left, (self.x, self.y))
            self.COUNT += 1

        if self.up == True:
            up = pygame.transform.rotate(Walk[self.COUNT], 0)
            screen.blit(up, (self.x, self.y))
            self.COUNT += 1

        if self.down == True:
            down = pygame.transform.rotate(Walk[self.COUNT], 180)
            screen.blit(down, (self.x, self.y))
            self.COUNT += 1


        pygame.display.update()

    def moveit(self):
        if self.x + self.width == self.pathx[1] - self.width and self.right == True :
            self.left = True
            self.right = False

        elif self.x + self.width == 0 + self.width and self.left == True :
            self.right = True
            self.left = False
            

        else:
            if self.x + self.width < self.pathx[1] - self.width:
                self.right = True
                self.left = False
                self.up = False
                self.down  = False
                self.x += self.vel

            else:
                self.right = False
                self.left = True
                self.up = False
                self.down  = False
                self.x -= self.vel

        if self.y + self.height == self.pathy[1] - self.height :
            self.up = False
            self.down = False

        else:
            if self.y + self.height < self.pathy[1] - self.height:
                self.right = False
                self.left = False
                self.up = False
                self.down  = True
                self.y += self.vel

            else:
                self.right = False
                self.left = False
                self.up = True
                self.down  = False
                self.y -= self.vel

        if self.x <= 0 :
            self.x = 0
    
        if self.y <= 0:
            self.y = 0

        if self.x >= 672:
            self.x = 672

        if self.y >= 672:
            self.y = 672 

#alt mom
'''
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



class rival(object):
    global Walk
    def __init__(self, x, y, width, height): 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 0
        self.right = False
        self.left = False
        self.up = False
        self.down  = False
        self.COUNT = 0  
    
    def draw(self):
        global screen
        self.moveit()
        if self.COUNT >= 15:
            self.COUNT = 0

        if self.right == True:
            right  = pygame.transform.rotate(Walk[self.COUNT], -90)
            screen.blit(right, (self.x, self.y))
            self.COUNT += 1

        if self.left == True:
            left = pygame.transform.rotate(Walk[self.COUNT], 90)
            screen.blit(left, (self.x, self.y))
            self.COUNT += 1

        if self.up == True:
            up = pygame.transform.rotate(Walk[self.COUNT], 0)
            screen.blit(up, (self.x, self.y))
            self.COUNT += 1

        if self.down == True:
            down = pygame.transform.rotate(Walk[self.COUNT], 180)
            screen.blit(down, (self.x, self.y))
            self.COUNT += 1


        pygame.display.update()

    def moveit(self):

        move  = self.choice()

        if move == self.right:   
                self.right = True
                self.left = False
                self.up = False
                self.down  = False
                self.x += self.vel

        elif move == self.left: 
                self.right = False
                self.left = True
                self.up = False
                self.down  = False
                self.x -= self.vel

        elif move == self.down:
                self.right = False
                self.left = False
                self.up = False
                self.down  = True
                self.y += self.vel


        elif move == self.up:
                self.right = False
                self.left = False
                self.up = True
                self.down  = False
                self.y -= self.vel

        if self.x <= 0 :
            self.x = 0
    
        if self.y <= 0:
            self.y = 0

        if self.x >= 672:
            self.x = 672

        if self.y >= 672:
            self.y = 672 

    def choice(self):
        pygame.time.set_timer(self.send(),400)
        return self.send()

    def send(self):
        move = random.choice([self.left, self.right, self.up , self.down])
        return move
