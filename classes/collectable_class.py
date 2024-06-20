from settings import *

class Collectable(pygame.sprite.Sprite):
    def __init__(self, pos, size, image):
        super().__init__(level_sprite.sprite.item_sprites)
        self.image = pygame.transform.scale(image, size)
        self.rect = self.image.get_rect(topleft = pos)
        
    def update(self):
        collision = pygame.sprite.spritecollideany(self, player_sprite)
        if collision:
            self.collect()
    
    def collect(self):
        pass
    
class Health_item(Collectable):
    def __init__(self, pos, size, image):
        super().__init__(pos, size, image)
    
    def collect(self):
        player_sprite.sprite.hp += 5
        player_sprite.sprite.hp = min(player_sprite.sprite.max_hp, player_sprite.sprite.hp)
        print(player_sprite.sprite.hp)
        self.kill()