import pygame
from util import calDist,getFrames


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,Path):
        super().__init__()
        self.index = 0
        self.canmove = False
        self.speed = 3.7
        #self.frames = getFrames(Path) 
        self.image = pygame.Surface((30,30))
        self.image.fill("green")
        self.colliding = False
        self.position = pygame.math.Vector2(x,y)
        self.direction = pygame.math.Vector2(0,0)
        self.lasPoint = pygame.math.Vector2(0)
        self.rect = self.image.get_rect(midbottom=(x,y))
        self.canMove = False
        self.max_health =100
        self.current_health =100

    def move(self):
        dy =0
        dx =0
        posx,posy = pygame.mouse.get_pos() 
        if pygame.mouse.get_pressed()[0]:
            x = posx
            y = posy 
            self.lasPoint = pygame.math.Vector2(posx,posy)
            #cp = pygame.math.Vector2(self.rect.x,self.rect.y)
            self.direction =  (self.lasPoint-self.position).normalize()
        if self.canMove:    
            self.position += self.direction*self.speed
            dx += (self.direction*self.speed).x
            dy += (self.direction*self.speed).y
        if (self.lasPoint-self.position).length() <=3:
            self.direction =pygame.math.Vector2(0)
            dx = 0
            dy = 0  

        self.lasPoint += -self.direction *  self.speed

        self.rect.centerx += dx
        self.rect.centery += dy    
        '''if self.rect.collidepoint(self.lasPoint):
            self.image.fill("blue")
            self.direction =pygame.math.Vector2(0)
            dx=0
            dy=0 
        else: self.image.fill("green")  '''       
       
        pygame.draw.line(pygame.display.get_surface(),"red",self.position,self.lasPoint)
        self.healthBar()
        self.update()
    def update(self):
        self.current_health = 50

    def healthBar(self):
        x,y = self.rect.midtop
        out_w,out_h = self.image.get_size()
        out_w =out_w*2
        out_h = out_h-5
        in_w = (out_w/self.max_health) * self.current_health
        print(in_w)
        pygame.draw.rect(pygame.display.get_surface(),"blue",(x-out_w//2,y-out_h,out_w,10),2)
        pygame.draw.rect(pygame.display.get_surface(),"green",(x-out_w//2,y-out_h+1,in_w,8))

    def handleCollision(self,type):
        if type.lower() =="tower":
            return True
    def setCanMove(self,val):
        self.canMove = val
