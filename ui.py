from settings import *

def draw_ui(surface):
    draw_health(surface, (player_sprite.sprite.rect.centerx-25, player_sprite.sprite.rect.top-15)-level_sprite.sprite.all_sprites.offset)
    
    
def draw_health(surface, pos):
    surface.blit(img.health_bar_back, pos)
    surface.blit(img.health_bar_front, pos)
    if player_sprite.sprite.hp > 0:
        img.health_bar_front = pygame.transform.scale(img.health_bar_front, (player_sprite.sprite.health_percent*50,10))