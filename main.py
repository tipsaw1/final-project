from settings import *
from setup import *
import menu_screens
import game_play
import ui
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
current_screen = 1
paused = False



pygame.event.set_grab(True)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_screens.start_button.collide(event.pos) and current_screen == 1:
                current_screen = 2
            elif menu_screens.archer_button.collide(event.pos) and current_screen == 2:
                archer_select()
                current_screen = 3
            elif menu_screens.knight_button.collide(event.pos) and current_screen == 2:
                knight_select()
                current_screen = 3
            elif menu_screens.mage_button.collide(event.pos) and current_screen == 2:
                mage_select()
                current_screen = 3
                
            elif menu_screens.resume_button.collide(event.pos) and paused == True:
                paused = False
                
            elif menu_screens.quit_button.collide(event.pos) and paused == True:
                running = False
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                
                paused = True
                

    if paused == True:
        menu_screens.pause_screen(screen)
    elif current_screen == 1:
        menu_screens.start_screen(screen)
    elif current_screen == 2:
        menu_screens.class_select_screen(screen)
    elif current_screen == 3:
        game_play.play_game(screen)
        ui.draw_ui(screen)
        
        if player_sprite.sprite.hp <= 0:
            current_screen = 5
        if player_sprite.sprite.victory:
            current_screen = 6
    
    elif current_screen == 5:
        game_play.game_over(screen)       
        
    elif current_screen == 6:
        game_play.victory(screen) 
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()
