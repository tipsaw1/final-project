from settings import *
from setup import *
import game_class
import menu_screens
import game_play
import ui
main_game = game_class.game()

pygame.event.set_grab(True)
running = True
while not main_game.quit:
      
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            main_game.quit = True

        main_game.check_events(event)
    
    main_game.gameplay()
    
    pygame.display.flip()
    clock.tick(main_game.FPS)
    
pygame.quit()
