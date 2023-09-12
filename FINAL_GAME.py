'''
Co-ordinate systems work differently in pygame as in real math. The origin is in the top-left corner 
and +x-axis is towards right & +y-axis is towards down. Quadrant 1 is bottom right, Quadrant 2 is bottom left,
Quadrant 3 is top left, and Quadrant 4 is top right.
'''
if __name__ == '__main__':
    def game_loop():
        import pygame
        import math
        pygame.init()
        pygame.font.init()
        #creating the screen
        screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Hunter Assassin")

        
        pygame.mixer.init()
        pygame.mixer.music.load("theme.wav")     
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)  

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
        rest1 = rest

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

        bullet = pygame.image.load('pics/Bullet.png').convert_alpha() 

        bg =  pygame.image.load('pics/bg-2.jpg')

        clock = pygame.time.Clock()

        score = 0

        #---------------------------------------------------------------------------

        class player(object):

            def __init__(self, x, y): 
                self.x = x                  #player co-ordinates
                self.y = y  
                self.width = 128            #image size
                self.height = 128
                self.vel = 5                #player velocity
                self.dir = None             #used to change directions as arrow keys/ wasd is pressed
                self.COUNT = 0              #variable used to iterate thru the list of player images 
                self.health = 100           #initial health
                self.die = False            #flag variable to check if player is alive or dead


            def draw(self):                                             #called in maindraw

                if self.dir == None:                                    #if player is not moving
                    screen.blit(rest1, (self.x, self.y))                                

                elif self.COUNT <= 15:                                  #no. of images in list = 16, => max index = 15
                    if self.dir == "up":
                        m = pygame.transform.rotate(Hunter_Walk[self.COUNT], 0)             #turns player to reqd direction
                        screen.blit(m,(self.x,self.y))                                      #displays character onto screen
                    
                    elif self.dir == "down":
                        m = pygame.transform.rotate(Hunter_Walk[self.COUNT], 180)
                        screen.blit(m,(self.x,self.y))
                        
                    elif self.dir == "right":
                        m = pygame.transform.rotate(Hunter_Walk[self.COUNT], -90)
                        screen.blit(m,(self.x,self.y))
                        
                    elif self.dir == "left":
                        m = pygame.transform.rotate(Hunter_Walk[self.COUNT], 90)
                        screen.blit(m,(self.x,self.y))
                    
                    self.COUNT += 1                 #increment iterable to display next image

                else:
                    self.COUNT = 0                  #resets iteration variable to prevent index out of range error
                
            #health bar which shows how much health is left, with each bullet hit, it reduces health
            def health(self):                       #called in maindraw

                pygame.draw.rect(screen, (0,0,0), pygame.Rect(100, 45, 100, 20))
                
                if self.health == 100:
                    color = (0,255,0)
                    pygame.draw.rect(screen, color, pygame.Rect(100, 45, self.health, 20))

                elif self.health == 75:
                    color = (255, 255, 0)
                    pygame.draw.rect(screen,color, pygame.Rect(100, 45, self.health, 20))
                    
                elif self.health == 50:
                    color = (255,165,0)
                    pygame.draw.rect(screen,color, pygame.Rect(100, 45, self.health, 20))

                elif self.health == 25:
                    color = (255,0,0)
                    pygame.draw.rect(screen,color, pygame.Rect(100, 45, self.health, 20))

                elif self.health == 0:
                    color = (0,0,0)
                    pygame.draw.rect(screen,color, pygame.Rect(100, 45, self.health, 20))               

        #---------------------------------------------------------------------------

        class rival(object):
            #initialising rival object
            nonlocal Enemy_Walk                                           #list of enemy images
            def __init__(self, startx, starty, endx, endy, name): 
                #all variables/ attributes of the rival
                self.name = name
                self.x = startx                                              #rival co-ordinates
                self.y = starty                                              #starting coordinates
                self.width = 64                                              #image width
                self.height = 64                                             #image height
                self.startx = startx                                         #initial and final x & y co-ordinates since
                self.starty = starty                                         #character moves in a fixed path (straight line)
                self.endx = endx                                             #end coordinates
                self.endy = endy

                if self.startx > self.endx and self.starty == self.endy:
                    self.velx = -2.5
                elif self.startx < self.endx and self.starty == self.endy:
                    self.velx = 2.5
                elif self.starty > self.endy and self.startx == self.endx:
                    self.vely = -2.5
                elif self.starty < self.endy and self.startx == self.endx:
                    self.vely = 2.5
                
                self.dir = ''                                                #acts as flag variable used in checkPoint()
                self.COUNT = 0                                               #iterabe to go thru list of images
                self.Angle = 0                                               #Angle by which rival is supposed to turn 
                self.theta = 0                                               #The angle by which rival must turn if player is in range wrt his initial posn
                self.move = True                                             #variable that controls movement of rival
                self.shoot_cooldown = 0                                      #time counter of shpootingwwd

            def draw(self):                                                   #fn called in maindraw()
                nonlocal screen            
                self.moveit()                                                 #moves the player

                if self.COUNT > 15:                                           #no. of images in list = 16, => max index = 15
                    self.COUNT = 0

                elif self.velx < 0:
                    left = pygame.transform.rotate(Enemy_Walk[self.COUNT], 90)              #rival faces left
                    screen.blit(left, (self.x, self.y))                                     #display change on screen
                    self.COUNT += 1                                                  #increment iterable variables which goes thru images
                
                elif self.velx > 0:
                    right  = pygame.transform.rotate(Enemy_Walk[self.COUNT], -90)         #rightfacing
                    screen.blit(right, (self.x, self.y))
                    self.COUNT += 1
                    

                elif self.vely < 0:                                                     #moving up
                    up = pygame.transform.rotate(Enemy_Walk[self.COUNT], 0) 
                    screen.blit(up, (self.x, self.y))
                    self.COUNT += 1
                    
                elif self.vely > 0:                                                      #moving down
                    down = pygame.transform.rotate(Enemy_Walk[self.COUNT], 180)
                    screen.blit(down, (self.x, self.y))
                    self.COUNT += 1
                                    
                else:                                                                   #rival stops moving in order to shoot
                    shoot = pygame.transform.rotate(Enemy_Walk[8], self.theta)          #turns by theta angle
                    screen.blit(shoot, (self.x, self.y))                                #displayed on screen


            def moveit(self):                                                           #fn called in draw()
                nonlocal lad 
                self.die()
                if self.move:

                    if self.starty == self.endy:   
                    #if y co-ordinates are same => rival moves along x-axis
                        self.vely = 0                                                   #no movement along y-axis

                        if self.startx < self.endx:

                            if self.velx > 0:                                   #if rival is moving forward (towards right)
                                if self.x <= self.endx - self.height:           #check if character has reached the end
                                    self.x += self.velx                         #if no, move right with velx speed
                                else:                                           #if yes, make velx negative so it enters next condn.
                                    self.velx = self.velx * -1
                                    self.dir = 'l'                              #change direction to go in reverse

                            elif self.velx < 0:                                 #rival is moving backwards
                                if self.x + self.velx >= self.startx:           #check if character has reached the beginning
                                    self.x += self.velx                         #if no, move left with velx speed(move right with -velx speed)
                                else:                                           #if yes, make velx positive so it enters prev condn.
                                    self.velx = self.velx * -1
                                    self.dir = 'r'                              #change direction to go in reverse

                        elif self.startx > self.endx: 
                            if self.velx < 0:                                   #rival is moving backwards
                                if self.x >= self.endx:                         #check if character has reached the beginning
                                    self.x += self.velx                         #if no, move left with velx speed(move right with -velx speed)
                                else:                                           #if yes, make velx positive so it enters prev condn.
                                    self.velx = self.velx * -1
                                    self.dir = 'r'                              #change direction to go in reverse

                            elif self.velx > 0:                                 #if rival is moving forward (towards right)
                                if self.x <= self.startx - self.height:         #check if character has reached the end
                                    self.x += self.velx                         #if no, move right with velx speed
                                else:                                           #if yes, make velx negative so it enters next condn.
                                    self.velx = self.velx * -1
                                    self.dir = 'l'                              #change direction to go in reverse

                    elif self.startx == self.endx:
                        self.velx = 0                                           #no movement along y-axis

                        if self.starty < self.endy:

                            if self.vely > 0:                                   #if rival is moving forward (towards right)
                                if self.y <= self.endy - self.height:           #check if character has reached the end
                                    self.y += self.vely                         #if no, move right with vely speed
                                else:                                           #if yes, make vely negative so it enters next condn.
                                    self.vely = self.vely * -1
                                    self.dir = 'u'                              #change direction to go in reverse

                            elif self.vely < 0:                                 #rival is moving backwards
                                if self.y + self.vely >= self.starty:           #check if character has reached the beginning
                                    self.y += self.vely                         #if no, move left with vely speed(move right with -vely speed)
                                else:                                           #if yes, make vely positive so it enters prev condn.
                                    self.vely = self.vely * -1
                                    self.dir = 'd'                              #change direction to go in reverse

                        elif self.starty > self.endy: 
                            if self.vely < 0:                                   #rival is moving backwards
                                if self.y >= self.endy:                         #check if character has reached the beginning
                                    self.y += self.vely                         #if no, move left with vely speed(move right with -vely speed)
                                else:                                           #if yes, make vely positive so it enters prev condn.
                                    self.vely = self.vely * -1
                                    self.dir = 'd'                              #change direction to go in reverse

                            elif self.vely > 0:                                 #if rival is moving forward (towards right)
                                if self.y <= self.starty - self.height:         #check if character has reached the end
                                    self.y += self.vely                         #if no, move right with vely speed
                                else:                                           #if yes, make vely negative so it enters next condn.
                                    self.vely = self.vely * -1
                                    self.dir = 'u'                              #change direction to go in reverse

                rival.checkPoint(self, lad.x, lad.y, self.x, self.y , self.dir)     #checks if player is in rival's field
            
            #fn called in moveit()
            def checkPoint(self,playerx, playery , selfx ,selfy , dir):      
            
                #getting a 120 degree arc with a radius of 200 px , this is the activation zone of the rival
                radius = 200
                endAngle1 =  60              
                endAngle2 =  -60

                #dist btw player and rival x coordinates
                x =  selfx - playerx    
                #dist btw player and rival y coordinates     
                y =  selfy - playery   
                
                #shortest distance between the rival and player
                rivalradius = math.sqrt(x * x + y * y)   
                
                #turn =  the angle the rival has to turn in order to face and shoot the player correctly
                #self.Angle is the class variable equal to turn.
                if dir == 'u' and y > 0 :
                    turn = math.degrees (math.atan(x/y)) 
                    self.Angle = turn 

                #checking if the player lies within the activation zone.    
                    if (self.Angle <= endAngle1 and self.Angle >= endAngle2) and (rivalradius < radius):
                        #activating shoot
                        rival.shoot(self)       
                        #angle adjusting to the first and 4th quadrants, + 0 in this case as the rival is facing ahead already.
                        self.theta = self.Angle 
                        #reducing the cooldown time by one so that the bullets have enough time to shoot.
                        self.shoot_cooldown -= 1 
                    else:
                        #if the player is not in the activation zone the rival returns to normal path.
                        self.move = True  
                        self.vely = -2.5 

                elif dir == 'd' and y < 0:
                    turn = math.degrees (math.atan(x/y))
                    self.Angle =  turn
                    

                    if (self.Angle <= endAngle1 and self.Angle >= endAngle2) and (rivalradius < radius): 
                        rival.shoot(self)
                        #turning the rival into the second and third quadrants.
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
                        #turining the rival to first and second quadrants.
                        self.theta = 90 - self.Angle 
                        self.shoot_cooldown -= 1
                    else:
                        self.move = True
                        self.velx = -2.5

                elif dir == 'r' and x < 0:
                    turn = math.degrees (math.atan(y/x))
                    self.Angle =  -turn
                    
                    if (self.Angle <= endAngle1 and self.Angle >= endAngle2) and (rivalradius < radius):
                        rival.shoot(self)
                        #bringing the rival into third and 4th quadrants.
                        self.theta = self.Angle - 90 
                        self.shoot_cooldown -= 1
                    else:
                        self.move = True
                        self.velx = 2.5

            #fn called in checkPoint()
            def shoot(self):    
                # the rival stops moving to take aim and shoot
                self.velx = 0
                self.vely = 0
                # case that bullet has just been shot, the cool down is set back to 20 so there is ample gap between shots.
                if self.shoot_cooldown == 0:    
                    self.shoot_cooldown = 20
                    #assigning variables to the bullet class
                    bulletss(self.x, self.y, lad.x, lad.y, self.theta)

            #fn called in moveit()
            def die(self):  
                nonlocal score, enemy_dict, killcount
                #if the player is within the coordinates of the rival, rival is terminated and is removed from the screen and game.
                if (self.x < lad.x + 64 < self.x + 128) and (self.y < lad.y + 64 < self.y + 128) and keys [pygame.K_SPACE]:
                    #setting the value of enemy key to none so it cannot be called/ drawn in the game again.
                    enemy_dict [self.name] = None 
                    #100 points increment per kill, killcount increment by 1 per kill.
                    score += 100   
                    killcount += 1

        #---------------------------------------------------------------------------

        class bulletss(object):
            #list of bullets queued to shoot
            bullet_list = []     
            #bullet velocity                       
            vel = 30   

            def __init__(self, ex, ey, px, py, bullet_theta):
                #(ex, ey) gives us the coordinate of the mid point of the rival , the bullet is spawned and shot from this point.
                #defining angle by which the bullet must turn in order to face the player.
                self.thetaa = bullet_theta
                #checking if the bullet list has less than 5 bullets, proceeding to move bullet.
                if len(self.bullet_list) < 5:  
                    
                    #angle between the shooting point and the player,we find it so that 
                    #we can configure the bullet into the right quadrant using propertins of sin and cos of angles.
                    theta = math.atan2((py - ey),(px - ex)) 
                    sin = math.sin(theta)
                    cos = math.cos(theta)
                    
                    #the bullet with required configuration is appended into bullet list and queued for shooting.
                    self.bullet_list.append([ex + 64 ,ey + 64, cos, sin, self.thetaa]) 
                    
                else:
                    #if there are 5 bullets in the list the last bullet is removed from the list to make space for a new bullet on screen.
                    self.bullet_list.pop()   

            def movebull(self,i): 
                #i is the list containig the information about the configuration of that bullet.
                #we are considering the velocity of bullet as a vector in the x-y plane hence the resultant velocity 
                #is the result of the components of the velocity along the x and y axes.
                #getting the x component of the bullet velocity so that the bullet moves towards the player with the required configuration. 
                #(x component of bullet velocity = velocity*cos(thetaa))
                i[0] += self.vel * i[2]  
                #getting the y component of the bullet velocity so that the bullet moves towards the player with the required configuration. 
                #(y component of bullet velocity = velocity*sin(thetaa))
                i[1] += self.vel * i[3]
                #deleting bullets 
                bulletss.delete(self,i) 
            

            def delete(self,i):
                #if bullet hits the edges, it is deleted
                if i[0] > 1200 or i[1] > 800 or i[1] < 0 or i[0] < 0: 
                    self.bullet_list.remove(i)
                #if the bullet hits the player it is deleted
                elif (i[0] > lad.x) and (i[0] < lad.x + 128)  and (i[1] > lad.y) and (i[1] < lad.y + 128):
                    #reducing the player health accordingly with impact of each bullet.
                    lad.health -= 25 
                    self.bullet_list.remove(i)            

        #---------------------------------------------------------------------------

        #setting a font to be used to display text on screen
        font = pygame.font.SysFont('Comic Sans MS', 25)
        health_text = font.render('Health: ', False, (0, 0, 0), (122,122,122))

        #assigning values and co-ordinates to player and rivals
        lad = player(1072,0)
        #horizontal moving rivals
        rival_1= rival(300,600,900,600,'rival_1')
        rival_2 = rival(1072,300,550,300,'rival_2')
        rival_3 = rival(600,150,0, 150,'rival_3')
        rival_4 = rival(250,0,850,0,'rival_4')
        rival_5 = rival(800, 460, 200, 460, 'rival_5')
        #vertical moving rivals
        rival_6 = rival(50,128,50,672,'rival_6')
        rival_7 = rival(1000,672,1000,200,'rival_7')
        rival_8 = rival(750, 400, 750, 672,'rival_8')
        rival_9= rival(300,672,300,300,'rival_9')
        rival_10 = rival(500,600,500,0,'rival_10')
        not_running_dict = {'rival_4':rival_4,'rival_8':rival_8, 'rival_5':rival_5, 'rival_10':rival_10,
        'rival_2': rival_2,'rival_9':rival_9,'rival_6':rival_6}                             #rivals not yet displayed on screen
        enemy_dict = {'rival_1':rival_1,'rival_3':rival_3,'rival_7': rival_7}               #rivals present on screen
        
        def maindraw():                                 #draws all characters on screen
            screen.blit(bg, (0,0))                      #draws the screen bg
            for enemy in enemy_dict:
                if enemy_dict[enemy] != None:
                    enemy_dict[enemy].draw()

            lad.draw()
            player.health(lad)
            score_text = font.render('Score: {}'.format(score), False, (0, 0, 0),(122,122,122))
            screen.blit(score_text, (0,0))
            screen.blit(health_text, (0,40))
            timelabel = font.render("Time - {} s".format(seconds), False, (0,0,0), (122,122,122))
            screen.blit(timelabel, (1050,0))
            
            if len(bulletss.bullet_list) != 0:
                i = bulletss.bullet_list[bull_iterable]
                dishoom = pygame.transform.rotate(bullet,i[4])                 #turns bullet in direction for shooting
                screen.blit(dishoom, (i[0], i[1]))                             #displays bullet on screen
                bulletss.movebull(bulletss,i)                                  #fn to move bullet
            
            pygame.display.update()                     #updates screen to show all characters 

        milliseconds = 0                            
        seconds = 0                                 #time in seconds
        new_guy_timer = 0                           #time in 
        bull_iterable = 0                                       #iterable to iterate through bullet_list
        killcount = 0                               #no. of enemies killed
        running = True

        #---------------------------------------------------------------------------

        while running:                                                         #game loop
            clock.tick(32) 
                                                    #32 ms delay for better accuracy
                
            for event in pygame.event.get():                                
                if event.type == pygame.QUIT:                                  #if game is closed
                    running = False                                            #stop the game

                if event.type == pygame.KEYUP:                                 #if no key is pressed
                    lad.dir = None                                             #moving in no direction
                
            if lad.health == 0:                                                #if the player has no health
                running = False                                                #stop the game

            if killcount == len(enemy_dict):                                   #if the player has killed all rivals
                running = False                                                #stop the game
        
            if bull_iterable < len(bulletss.bullet_list) - 1:                              #so that index does not go out of range
                bull_iterable += 1                                                         #increment iterable
            else:
                bull_iterable = 0                                                          #reset to 0 if it is out of range

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
                seconds += 1                                                #increment time
                new_guy_timer += 1                                          #variable for adding new player on screen
                milliseconds -= 150

            if new_guy_timer == 5 and len(not_running_dict) != 0:                              
                #if more than 5s have elapsed and if there are enemies have not yet been displayed on screen
                    x = not_running_dict.popitem()                          #remove them from not_running_dict
                    enemy_dict [x[0]] = x[1]                                #and add to enemy_dict
                    new_guy_timer = 0                                       #reset timer to 0

            #so that character does not go out of bounds 
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
        return score, seconds
game_loop()