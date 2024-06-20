from settings import *
def play_game(surface):
    level_sprite.sprite.tile_sprites.draw(surface)
    level_sprite.sprite.all_sprites.update()
    level_sprite.sprite.all_sprites.draw(surface)
    
def draw_health(surface):
  pass