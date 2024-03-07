import pygame
import random
pygame.init() 
pygame.display.set_caption("Space Invaders") #Window Title
screen = pygame.display.set_mode((800,800)) #creates game screen
Clock = pygame.time.Clock() #Sets the clock
LoseCon = False # Varible to run game loop
timer = 0
class Alien:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = True
        self.direction = 1
    def draw(self):
        pygame.draw.rect(screen, (250, 250, 250), (self.xpos, self.ypos, 40, 40))
    def move(self, time):
        if time % 800==0:
            self.ypos += 100 #moves down
            self.direction *=-1 #flips
            return 0 #resets timer
        if time % 100==0: 
            self.xpos+=50*self.direction # move right
        return time
class Bullet:
    def __init__(self,xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = False
        
    def move(self, xpos, ypos):
        if self.isAlive == True: #only shoot live bullets
            self.ypos-=5 #move upward when shot
        if self.ypos <0:
            self.isAlive = False
            self.xpos = xpos
            self.ypos = ypos
    def draw(self):
        pygame.draw.rect(screen, (250, 250,250), (self.xpos, self.ypos, 3, 20))
        
class Wall:
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.numHits = 0
    def draw(self):
        if self.numHits ==0:
            pygame.draw.rect(screen, (250,250,20), (self.xpos, self.ypos, 30, 30))
        if self.numHits==1:
            pygame.draw.rect(screen, (250,250,20), (self.xpos, self.ypos, 30, 30))
        if self.numHits==2:
            pygame.draw.rect(screen, (250,250,20), (self.xpos, self.ypos, 30, 30))
        
armada = [] #create list
walls = []
for k in range(4):
    for i in range(2):
        for j in range(3):
            walls.append(Wall(j*30+200*k+50, i*30+600))
for i in range (4):
    for j in range(8):
        armada.append(Alien(j*60+50, i*50+50))
         


#Player Variables
xpos = 400
ypos = 750
moveLeft = False
moveRight = False
shoot = False 
#instantiate bullet obj
bullet = Bullet(xpos+28, ypos) #create bullet obj and pass player pos
while not LoseCon: #Game loop
    Clock.tick(60)
    timer +=1 
    #Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True #quit game is x is pressed in the top corner
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveLeft = True
            if event.key == pygame.K_RIGHT:
                moveRight = True
            if event.key == pygame.K_SPACE:
                shoot= True
        elif event.type == pygame.KEYUP:
            if event. key == pygame.K_LEFT:
                moveLeft = False
            if event.key == pygame.K_RIGHT:
                moveRight = False
            if event.key == pygame.K_SPACE:
                shoot= False
        
    #Physics Section---------------------------------------------
    for i in range(len(armada)):
        timer = armada[i].move(timer)
    def collide(self, BulletX, BulletY):
        if self.isAlive: #only hit live aliens
            if BulletX > self.xpos: #check to see if bullet is right of the left side of the alien
                if BulletX < self.xpos + 40: #check to see if the bullet is lef of the right side
                    if BulletY < self.ypos + 40: #check if the bullet is above the Alien's bottom
                        if BulletY > self.ypos: #check if the bullet is below the top of the alien
                            print("hit!") #for testing
                            self.isAlive = False #set the alien to dead
                            return False
        return True #otherwise keep bullet alive
    #Bullet Check
    if shoot == True: #Check keyboard input
        bullet.isAlive = True
    if bullet.isAlive == True:
        bullet.move(xpos+28, ypos) #shoot from player position
        if bullet.isAlive == True:
        #check for collision between bullet and enemy
            for i in range (len(armada)): #Check bullet with the entire armada's position
                bullet.isAlive= armada[i].collide(bullet.xpos, bullet.ypos) #if we hit, set bullet to false
                if bullet.isAlive == False:
                    break
        #check for collision between player and wall
            for i in range (len(walls)): #Check bullet with the entire armada's position
                bullet.isAlive= walls[i].collide(bullet.xpos, bullet.ypos) #if we hit, set bullet to false
                if numHits < 3:
                    numHits +=1 
                    break
    else: #make bullet follow player when not moving up
        bullet.xpos = xpos +28
        bullet.ypos = ypos 
    # Check variables from the input
    if moveLeft == True:
        vx =- 3
    elif moveRight == True:
        vx = 3 
    else:
        vx = 0
    xpos += vx
    #Render Sect------------------------------------------------
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(200, 200, 100), (xpos, 750, 60, 20)) #Draw Player
    
    #draws all aliens in list
    for i in range (len(armada)):
        armada[i].draw()
    for i in range (len(walls)):
        walls[i].draw()
    pygame.display.flip()
    
#end game loop--------------------------------------------------

pygame.quit()