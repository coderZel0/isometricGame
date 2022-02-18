import pygame
from util import fileData
from gameset import *
from Tile import Tile,CollisionTile
from player import Player
from gameset import *
from util import fileData
from tower  import Tower

class Game:
    def __init__(self,surface):
        self.tile_group = pygame.sprite.Group()
        self.playerGroup = pygame.sprite.GroupSingle()
        self.tower_group = pygame.sprite.Group()
        self.collision_rects = pygame.sprite.Group()
        self.display_surface = surface
        self.world_offset_direction = pygame.Vector2(0)
        self.world_offset = 0
        self.world_offset_speed =0
        self.can_world_shift= True
        self.setMap()

    def renderMap(self,data,type):
        for i in range(len(data)-1):
            for j in range(len(data[i])-1,0,-1):
                x = j*TILE
                y = i*TILE
                nx = (x+y)/2-WIDTH/3-320
                ny = (-0.5*x + 0.5*y)/2+HEIGHT-570
                if data[i][j] == '1':
                    if type == "TILE":
                        block = pygame.image.load("assets/block.png").convert_alpha()
                        block = pygame.transform.scale(block,(TILE,TILE))
                        tile = Tile(self.display_surface,(nx,ny),TILE,block)
                        self.tile_group.add(tile)  
                    elif type == "PLAYER":
                        player = Player(nx+0.2*WIDTH,ny,"assets/")
                        self.playerGroup.add(player)
                elif data[i][j] == 'T':  
                    self.collision_rects.add(CollisionTile(nx,ny))      
                    if type == "TOWER":
                        tower = Tower(nx,ny)  
                        self.tower_group.add(tower)  

    def processMouseInput(self):
        posx,posy = pygame.mouse.get_pos()
        
        if pygame.mouse.get_pressed()[0]:
            x = posx
            y = posy
            return (x,y)    

    def towerCollision(self):
        if pygame.sprite.spritecollide(self.playerGroup.sprite,self.collision_rects,False):
            self.playerGroup.sprite.handleCollision(type="Tower")

    def processInputs(self):
        keys = pygame.key.get()
        if keys[pygame.K_y]:
            #setWorldShift()
            #playerGroup.sprite.setCanMove()
            pass

    def setWorldShift(self):
        self.can_world_shift = not self.playerGroup.sprite.canMove   

    # Function to update sprite groups
    def updateSpriteGroups(self):
        for rect in self.collision_rects.sprites():
            rect.update(self.world_offset_direction,self.world_offset_speed)
        for tile in self.tile_group.sprites():
            tile.update(self.world_offset_direction,self.world_offset_speed)
        for t in self.tower_group.sprites():
            t.render(self.display_surface)
            t.update(self.world_offset_direction,self.world_offset_speed)
            t.tower_shot(self.playerGroup.sprite)
        #self.playerGroup.sprite.update()    
    
    #rendering the map    
    def setMap(self):
        self.renderMap(fileData("maps/map2.csv"),"TILE")
        self.renderMap(fileData("player.csv"),"PLAYER")
        self.renderMap(fileData("maps/tower.csv"),"TOWER")

    #function to check if player position is greater than middle of map (//to check if player is on ememy side of the map)
    def player_on_other_side(self):
        world_middle = (len(fileData("maps/map2.csv")[0])//2)*TILE
        if self.playerGroup.sprite.position + self.world_offset>world_middle:
            return True
        return False    

    def run(self):
        self.world_offset_direction = - self.playerGroup.sprite.direction
        self.world_offset_speed = self.playerGroup.sprite.speed

        self.tile_group.draw(self.display_surface)
        self.playerGroup.draw(self.display_surface)
        self.tower_group.draw(self.display_surface)
        self.updateSpriteGroups()
        self.playerGroup.sprite.move()