from settings import *
game_over_text = button_font.render("GAME OVER: YOU LOST", True, "red")
game_over_rect = game_over_text.get_rect(center = (SCREEN_W//2-100, SCREEN_H//2))

victory_text = button_font.render("YOU WIN!", True, "yellow")
victory_rect = victory_text.get_rect(center = (SCREEN_W//2, SCREEN_H//2))
def play_game(surface):
    level_sprite.update()
    level_sprite.sprite.all_sprites.update()
    level_sprite.sprite.all_sprites.draw(surface)

def game_over(surface):
    surface.fill("black")
    surface.blit(game_over_text, game_over_rect)
    surface.blit(pygame.transform.scale(player_sprite.sprite.dead_image[1], (80,80)), game_over_rect.topright + pygame.math.Vector2(50,25))
    
def victory(surface):
    surface.blit(victory_text, victory_rect)