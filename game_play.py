from settings import *
game_over_text = button_font.render("GAME OVER: YOU LOST", True, "red")
game_over_rect = game_over_text.get_rect(center = (SCREEN_W//2-100, SCREEN_H//2))

victory_text = button_font.render("YOU WIN!", True, "yellow")
victory_rect = victory_text.get_rect(center = (SCREEN_W//2, SCREEN_H//2))
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
    surface.blit(pygame.transform.scale(player_sprite.sprite.dead_image[1], (80,80)), game_over_rect.topright + pygame.math.Vector2(50,25))
    
def victory(surface):
    surface.fill("black")
    surface.blit(victory_text, victory_rect)
    player_sprite.sprite.image = pygame.transform.scale(player_sprite.sprite.image, (80,80))
    player_sprite.sprite.rect = player_sprite.sprite.image.get_rect(midleft = victory_rect.midright)
    player_sprite.draw(surface)
    
