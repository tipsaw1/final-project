from settings import *
from setup import *
import start_screen
import game_play

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

#

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    game_play.play_game(screen)
    #start_screen.start()
    #if player_sprite.sprite.hp <= 0:
        #running = False
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()
