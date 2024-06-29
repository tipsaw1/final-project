import game_class, pygame, menu_screens, game_play, ui
pygame.init()

clock = pygame.time.Clock()

while not game_class.main_game.quit:
      
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            game_class.main_game.quit = True

        menu_screens.check_events(game_class.main_game, event)

    # Gameplay
    if game_class.main_game.paused:
      menu_screens.pause_screen(game_class.main_game)
      
    elif game_class.main_game.current_screen == "start":
      menu_screens.start_screen(game_class.main_game)
      
    elif game_class.main_game.current_screen == "class":
      menu_screens.class_select_screen(game_class.main_game)
      
    elif game_class.main_game.current_screen == "gameplay":
      game_play.play_game(game_class.main_game)
      ui.draw_ui(game_class.main_game)
      
    elif game_class.main_game.current_screen == "gameover":
      game_play.game_over(game_class.main_game.screen)
      
    elif game_class.main_game.current_screen == "gamewon":
      game_play.victory(game_class.main_game.screen)
    
    pygame.display.flip()
    clock.tick(game_class.main_game.FPS)
    
pygame.quit()


  
