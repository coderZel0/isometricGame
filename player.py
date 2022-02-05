import pygame
from util import calDist,getFrames


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,Path):
        super().__init__()
        self.index = 0
        self.canmove = False
        self.speed = 1.7
        self.frames = getFrames(Path) 
        self.image = pygame.Surface((30,30))
        self.image.fill("green")
        self.colliding = False
        self.position = pygame.math.Vector2(x,y)
        self.direction = pygame.math.Vector2(0,0)
        self.lasPoint = pygame.math.Vector2(0)
        self.rect = self.image.get_rect(midbottom=(x,y))
        self.canMove = False

    def move(self):
        posx,posy = pygame.mouse.get_pos() 
        if pygame.mouse.get_pressed()[0]:
            x = posx
            y = posy 
            self.lasPoint = pygame.math.Vector2(posx,posy)
            #cp = pygame.math.Vector2(self.rect.x,self.rect.y)
            self.direction =  (self.lasPoint-self.position).normalize()
        if self.canMove:    
            self.position += self.direction*self.speed
        self.rect.center = self.position
        if (self.lasPoint-self.position).length() <=1:
            self.direction =pygame.math.Vector2(0)
    def update(self,offsetDir):
        self.lasPoint += offsetDir*self.speed
    def handleCollision(self,type):
        if type.lower() =="tower":
            self.direction = pygame.Vector2(0,0)
    def setCanMove(self):
        self.canMove = True
