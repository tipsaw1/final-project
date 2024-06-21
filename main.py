from settings import *
from setup import *
import start_screen
import game_play
import ui

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
current_screen = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_screen.start_button.collide(event.pos) and current_screen == 1:
                current_screen = 2
            elif start_screen.archer_button.collide(event.pos) and current_screen == 2:
                archer_select()
                current_screen = 3
            elif start_screen.knight_button.collide(event.pos) and current_screen == 2:
                knight_select()
                current_screen = 3
            elif start_screen.mage_button.collide(event.pos) and current_screen == 2:
                mage_select()
                current_screen = 3

    if current_screen == 1:
        start_screen.start()
    elif current_screen == 2:
        start_screen.class_select()
    elif current_screen == 3:
        game_play.play_game(screen)
        ui.draw_ui(screen)
        if player_sprite.sprite.hp <= 0:
            current_screen = 4
    if current_screen == 4:
        game_play.game_over(screen)        
    
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()
