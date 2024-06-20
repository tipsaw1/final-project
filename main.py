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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_screen.start_button.collide(event.pos):
                start_screen.menu = False    

    if start_screen.menu:
        start_screen.start()
    else:
        game_play.play_game(screen)
    
    #if player_sprite.sprite.hp <= 0:
        #running = False
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()
