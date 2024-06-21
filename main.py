from settings import *
from setup import *
import start_screen
import game_play
import ui

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

#

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_screen.start_button.collide(event.pos) and start_screen.menu == 1:
                start_screen.menu = 2
            elif start_screen.archer_button.collide(event.pos) and start_screen.menu == 2:
                archer_select()
                start_screen.menu = 3
            elif start_screen.knight_button.collide(event.pos) and start_screen.menu == 2:
                knight_select()
                start_screen.menu = 3
            elif start_screen.mage_button.collide(event.pos) and start_screen.menu == 2:
                mage_select()
                start_screen.menu = 3

    if start_screen.menu == 1:
        start_screen.start()
    elif start_screen.menu == 2:
        start_screen.class_select()
    elif start_screen.menu == 3:
        game_play.play_game(screen)
        ui.draw_ui(screen)
    
    #if player_sprite.sprite.hp <= 0:
        #running = False
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()
