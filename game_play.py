import game_class
import settings, pygame
game_over_text = settings.button_font.render("GAME OVER: YOU LOST", True, "red")
game_over_rect = game_over_text.get_rect(center = (game_class.main_game.SCREEN_W//2-100, game_class.main_game.SCREEN_H//2))

victory_text = settings.button_font.render("YOU WIN!", True, "yellow")
victory_rect = victory_text.get_rect(center = (game_class.main_game.SCREEN_W//2, game_class.main_game.SCREEN_H//2))
dialogue_pause = False
def play_game(game):
    
    game.current_level.update()

    game.current_level.all_sprites.update()
    game.current_level.all_sprites.draw(game.screen)
    
    #Ensures dialogue is drawn on top
    for npc in game.current_level.npc_sprites.sprites():
        if npc.displaying_dialogue:
            npc.dialogue.display_dialogue()

def game_over(surface):
    surface.fill("black")
    surface.blit(game_over_text, game_over_rect)
    surface.blit(pygame.transform.scale(game_class.main_game.player.dead_image[1], (80,80)), game_over_rect.topright + pygame.math.Vector2(50,25))
    
def victory(surface):
    surface.fill("black")
    surface.blit(victory_text, victory_rect)
    game_class.main_game.player.image = pygame.transform.scale(game_class.main_game.player.image, (80,80))
    game_class.main_game.player.rect = game_class.main_game.player.image.get_rect(midleft = victory_rect.midright)
    game_class.main_game.player_group.draw(surface)
    
