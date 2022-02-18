import pygame,sys
from gameset import  WIDTH,HEIGHT
from game import Game


pygame.init()



screen = pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)

                
game = Game(screen)

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
   
    

    #game run method
    game.run()

    #collision_rects.draw(screen)
    #Collisions
    #towerCollision()

    pygame.time.Clock().tick(60)
    pygame.display.update()