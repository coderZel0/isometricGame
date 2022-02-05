import pygame
from gameset import TILE
from util import calDist;


class Tower(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("assets/tower.png").convert_alpha()
        self.image = pygame.transform.flip(self.image,True,False)
        self.width,self.height = self.image.get_size()
        self.image = pygame.transform.scale(self.image,(100,2*100))
        self.rect = self.image.get_rect(bottomleft=(x,y+50))
        self.shot_speed = 0.5
        self.range = 70
        self.towerPosition = pygame.Vector2(x,y+50)
        self.position = pygame.Vector2(x+50,y-15)
        self.setPowerSprite(x,y)
    def update(self,offsetDir,speed):
        self.towerPosition += offsetDir*speed
        self.rect.bottomleft = self.towerPosition
        self.position += offsetDir*speed
        self.orbPos += offsetDir*speed
        self.orbRect.bottomleft = self.orbPos
    def setPowerSprite(self,x,y):
        self.powerSprite = pygame.Surface((50,50))
        self.powerSprite.set_colorkey((0,0,0))
        self.powerSprite.fill("green")
        self.orbRect =self.powerSprite.get_rect(bottomleft=(x+TILE//4,y-TILE-TILE//2))
        self.orbPos = pygame.Vector2(x+TILE//4,y-TILE-TILE//2)
    def tower_shot(self,pos,playerwidth):
        if self.inRange(pos,playerwidth):
            self.powerSprite.fill("red")
        else:
            self.powerSprite.fill("green")    
    def inRange(self,playerPos,playerWidth):
        #if calDist(playerPos,self.position) <:
        if (playerPos-self.position).length() <= self.range + playerWidth//2:
            return True
    def render(self,surface):
        pygame.draw.circle(self.powerSprite,"cyan",(25,25),25)
        pygame.draw.circle(surface,"red",self.position,self.range)
        surface.blit(self.powerSprite,self.orbRect)     

