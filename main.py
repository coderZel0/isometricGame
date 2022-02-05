from re import S
import pygame,sys
from Tile import CollisionTile, Tile
from player import Player
from gameset import *
from util import fileData
from tower  import Tower

pygame.init()



screen = pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)

class Game:
    def __init__(self):
        pass
    def run(self):
        pass


block = pygame.image.load("assets/block.png").convert_alpha()
block = pygame.transform.scale(block,(TILE,TILE))
tile_width,tile_height = block.get_size()

tile_group = pygame.sprite.Group()
playerGroup = pygame.sprite.GroupSingle()
tower_group = pygame.sprite.Group()
collision_rects = pygame.sprite.Group()

world_offset_direction = pygame.Vector2(0)
world_offset = 0
world_offset_speed =0
can_world_shift= True
'''def drawMap(data,type):
    for rn,row in enumerate(data):
        for cn,col in enumerate(row):
            x = cn* TILE
            y = rn* TILE
            nx = (x+y-WIDTH//3)//2
            ny = (-0.5*x+0.5*y+HEIGHT-300)//2
            if col == '1':
                tile = Tile(screen,(nx,ny),TILE,block)
                tile_group.add(tile)'''
                
def renderMap(data,type):
    for i in range(len(data)-1):
        for j in range(len(data[i])-1,0,-1):
            x = j*TILE
            y = i*TILE
            nx = (x+y)/2-WIDTH/3-320
            ny = (-0.5*x + 0.5*y)/2+HEIGHT-570
            if data[i][j] == '1':
                if type == "TILE":
                    tile = Tile(screen,(nx,ny),TILE,block)
                    tile_group.add(tile)  
                elif type == "PLAYER":
                    player = Player(nx,ny,"assets/")
                    playerGroup.add(player)
            elif data[i][j] == 'T':  
                collision_rects.add(CollisionTile(nx,ny))      
                if type == "TOWER":
                    tower = Tower(nx,ny)  
                    tower_group.add(tower)  

def processMouseInput():
        posx,posy = pygame.mouse.get_pos()
        
        if pygame.mouse.get_pressed()[0]:
            x = posx
            y = posy
            return (x,y)    
def towerCollision():
    if pygame.sprite.spritecollide(playerGroup.sprite,collision_rects,False):
        playerGroup.sprite.handleCollision(type="Tower")
def processInputs():
    keys = pygame.key.get()
    if keys[pygame.K_y]:
        #setWorldShift()
        #playerGroup.sprite.setCanMove()
        pass

def setWorldShift():
    can_world_shift = not playerGroup.sprite.canMove        
# Function to update sprite groups
def updateSpriteGroups():
    for rect in collision_rects.sprites():
        rect.update(world_offset_direction,world_offset_speed)
    for tile in tile_group.sprites():
        tile.update(world_offset_direction,world_offset_speed)
    for t in tower_group.sprites():
        #t.render(screen)
        t.update(world_offset_direction,world_offset_speed)
        t.tower_shot(playerGroup.sprite.position,playerGroup.sprite.image.get_size()[0])
    playerGroup.sprite.update(world_offset_direction)    

#function to check if player position is greater than middle of map
world_middle = (len(fileData("maps/map2.csv")[0])//2)*TILE
def player_on_other_side():
    if playerGroup.sprite.position+world_offset>world_middle:
        return True
    return False    


renderMap(fileData("maps/map2.csv"),"TILE")
renderMap(fileData("player.csv"),"PLAYER")
renderMap(fileData("maps/tower.csv"),"TOWER")

while True:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()   
                sys.exit()

    world_offset_direction = -playerGroup.sprite.direction
    world_offset_speed = playerGroup.sprite.speed

    tile_group.draw(screen)
    playerGroup.draw(screen)
    tower_group.draw(screen)

    updateSpriteGroups()
    playerGroup.sprite.move()

    #collision_rects.draw(screen)
    #Collisions
    #towerCollision()

    pygame.time.Clock().tick(60)
    pygame.display.update()