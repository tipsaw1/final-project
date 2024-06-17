from settings import *

def create_obstacle(level, image, pos = (-1000, -1000)):
    Obstacle(level, image, pos)
class Obstacle(pygame.sprite.Sprite):
    # Creates an obstacle
    # If position is not defined, it defaults to (-1000,-1000)
    def __init__(self, level, image, pos) -> None:
        super().__init__(level.obstacle_sprites)
        self.image = pygame.transform.scale(image, (TILESIZE, TILESIZE))
        self.level = level
        self.x_offset = self.level.x
        self.y_offset = self.level.y
        self.rect = self.image.get_rect(topleft = pos)
        self.relative_x = self.rect.x - self.level.x
        self.relative_y = self.rect.y - self.level.y
        
    def update(self):
        self.rect.topleft = (self.relative_x + self.level.x, self.relative_y + self.level.y)