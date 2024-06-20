from settings import *

class Tile(pygame.sprite.Sprite):
    # Creates an obstacle
    def __init__(self, level, image, pos):
        super().__init__(level.tile_sprites)
        self.level = level
        self.image = pygame.transform.scale(image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft = pos)
        