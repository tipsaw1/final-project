from settings import *

class Weapon(pygame.sprite.Sprite):
    # constructor
    def __init__(self, damage, image, initial_positon):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center = initial_positon)
        self.speed = 5
        self.damage = damage
        
        

        