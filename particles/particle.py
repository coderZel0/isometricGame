import pygame
import random
from .color import Color

class Particle:
    def __init__(self,color,speed=1,glow=False,emit_rate=3,direction:pygame.Vector2=None):
        self.particles =[]
        self.radius = 8
        self.colorObj = color
        self.color = color.color
        self.speed = speed
        self.counter = emit_rate
        self.particleDir = direction
        self.timer = 0
        self.canRender = True
        self.glowState = glow
        if self.glowState: self.glowColor = (self.colorObj*Color((0.1,0.1,0.1))).color

    def getRandomDir(self):
        dx,dy=random.randint(-1,1),random.randint(-1,1)
        if dx==0 or dy==0:
            return self.getRandomDir()
        return dx,dy    
    def setRender(self,val):
        self.canRender = val
    def setParticle(self,x,y):
        #dx,dy = random.choice([-1,0,1]),random.choice([-1,0,1])
        dx,dy = self.getRandomDir()
        particle = [[x,y],self.radius,self.particleDir if self.particleDir else pygame.Vector2(dx,dy).normalize()]
        self.particles.append(particle)

    def update(self,x,y):
        self.removeParticles()
        self.timer += self.counter
        if self.timer>10:
            self.setParticle(x,y)
            self.timer =0
        for particle in self.particles:
            particle[1] -= 0.1
            particle[0][0] += particle[2].x * self.speed
            particle[0][1] += particle[2].y * self.speed

    def glow(self,screen):
        for particle in self.particles:
            surf = pygame.Surface((48,48))
            surf.set_colorkey((0,0,0))
            pygame.draw.circle(surf,self.glowColor,(surf.get_width()//2,surf.get_height()//2),particle[1]*3)
            pygame.draw.circle(surf,(255,255,255),(surf.get_width()//2,surf.get_height()//2),particle[1])
            screen.blit(surf,particle[0],special_flags=pygame.BLEND_RGBA_ADD)
    
    def removeParticles(self):
        #self.particles = [particle for particle in self.particles if particle[1]>0]
        for particle in self.particles:
            if particle[1]<0:
                self.particles.remove(particle)
    def draw(self,screen,x,y):
        if self.canRender:
            self.update(x,y)
            if self.glowState:
                self.glow(screen)
            else:    
                for particle in self.particles:
                    pygame.draw.circle(screen,self.color,particle[0],particle[1])