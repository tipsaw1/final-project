from settings import *

def draw_ui(game):
    draw_health(game, (player_sprite.sprite.rect.centerx-25, player_sprite.sprite.rect.top-15)-game.current_level.all_sprites.offset)
    
    
def draw_health(game, pos):
    game.screen.blit(img.health_bar_back, pos)
    game.screen.blit(img.health_bar_front, pos)
    img.health_bar_front = pygame.transform.scale(img.health_bar_front, (max(player_sprite.sprite.health_percent*50, 0),10))