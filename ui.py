import game_class
import settings, pygame

def draw_ui(game):
    draw_health(game, (game_class.main_game.player.rect.centerx-25, game_class.main_game.player.rect.top-15)-game.current_level.all_sprites.offset)
    
    
def draw_health(game, pos):
    game.screen.blit(settings.img.health_bar_back, pos)
    game.screen.blit(settings.img.health_bar_front, pos)
    settings.img.health_bar_front = pygame.transform.scale(settings.img.health_bar_front, (max(game_class.main_game.player.health_percent*50, 0),10))
    
