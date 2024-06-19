from settings import *

print('imported enemy class')

class Enemy(pygame.sprite.Sprite):
    def __init__(self, level, image, pos):
        super().__init__(level.enemy_sprites, level.all_sprites)
        self.level = level
        self.image = pygame.transform.scale(image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft = pos)
        
        # Changes based on subclass
        self.damage = 10
        self.hp = 10

    def damage_player(self):
        player_sprite.sprite.take_damage(self.damage)
        
    # Movement pattern will be based on subclasses
    
    
    
