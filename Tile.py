import pygame
from gameset import TILE

class Tile(pygame.sprite.Sprite):
    def __init__(self,surface,pos,size,image):
        super().__init__()
        self.size = size
        self.surface = surface
        self.imageOrigin = image
        self.image = image
        self.position = pygame.Vector2(pos)
        self.rect = self.image.get_rect(topleft=pos)
    def update(self,offsetDir,speed):
        self.position += offsetDir*speed
        self.rect = self.position
    
class CollisionTile(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((TILE-TILE/2,TILE-TILE/2))
        self.image.fill("red")
        self.position = pygame.Vector2(x,y)
        self.rect = self.image.get_rect(midtop=(x+TILE//2,y)) 
    def update(self,offsetDir,speed):
        self.position +=offsetDir*speed
        self.rect = self.position       