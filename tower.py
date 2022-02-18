from asyncio.windows_events import NULL
from pickle import NONE
import pygame
from gameset import TILE
from util import calDist
from particles import particle,color



class Tower(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("assets/tower.png").convert_alpha()
        self.image = pygame.transform.flip(self.image,True,False)
        self.width,self.height = self.image.get_size()
        self.image = pygame.transform.scale(self.image,(100,2*100))
        self.rect = self.image.get_rect(bottomleft=(x,y+50))
        self.shot_speed = 3
        self.origin_x = x
        self.origin_y = y
        self.range = 70
        self.towerPosition = pygame.Vector2(x,y+50)
        self.position = pygame.Vector2(x+50,y-15)
        self.current_target = None
        self.targetList = []
        self.setPowerSprite(x,y)

    def setPowerSprite(self,x,y):
        self.particle = particle.Particle(color.Color((1,0,0)),speed=0.3,glow=True,emit_rate=10)
        self.particlePos = pygame.Vector2(x+TILE//4,y-TILE-TILE//2)
        self.particleDir = pygame.Vector2(0)

    def update(self,offsetDir,speed):
        self.processTargetList()
        #process target list
        if(self.current_target):
            x,y = self.current_target.rect.center
            self.particleDir = (pygame.Vector2(x,y)-self.particlePos).normalize()
             #Reset particles effect
            if self.current_target.rect.collidepoint(self.particlePos):
                self.particle.setRender(False)
                self.setPowerSprite(self.origin_x,self.origin_y)
                self.current_target = 0

        self.particlePos += self.particleDir*self.shot_speed
        
        self.origin_x += (offsetDir*speed).x
        self.origin_y += (offsetDir*speed).y        
        self.towerPosition += offsetDir*speed
        self.particlePos += offsetDir*speed
        self.rect.bottomleft = self.towerPosition
        self.position += offsetDir*speed
    
    def processTargetList(self):
        if len(self.targetList)<=0: return
        self.current_target = self.targetList[0]
        self.targetList.remove(self.current_target)
        self.targetList.sort(key=lambda obj:((obj.position-self.position).length()))  

    def tower_shot(self,player):
        if self.inRange(player.position,player.image.get_size()[0]):
            self.targetList.append(player)
        else:
            pass
    def inRange(self,playerPos,playerWidth):
        #if calDist(playerPos,self.position) <:
        if (playerPos-self.position).length() <= self.range + playerWidth//2:
            return True
    def render(self,surface):
        #Draw particles here
        if self.current_target:
            self.particle.draw(surface,self.particlePos.x,self.particlePos.y)

        pygame.draw.circle(surface,"red",self.position,self.range)     

