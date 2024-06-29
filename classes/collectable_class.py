import settings, pygame

class Collectable(pygame.sprite.Sprite):
    def __init__(self, pos, size, image, game):
        super().__init__(game.current_level.item_sprites)
        self.game = game
        self.image = pygame.transform.scale(image, size)
        self.rect = self.image.get_rect(topleft = pos)
        
    def update(self):
        collision = pygame.sprite.spritecollideany(self, self.game.player_group)
        if collision:
            self.collect()
    
    def collect(self):
        self.kill()
    
class Health_item(Collectable):
    def __init__(self, pos, size, image, game):
        super().__init__(pos, size, image, game)
    
    def collect(self):
        self.game.player.hp += 15
        self.game.player.hp = min(self.game.player.max_hp, self.game.player.hp)
        print(self.game.player.hp)
        self.kill()