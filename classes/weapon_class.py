from settings import *
import pygame

class Weapon(pygame.sprite.Sprite):
    # constructor
    def __init__(self, damage, image_path, initial_positon):
        super().__init__()
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect()
        self.rect.center = initial_positon
        self.speed = 5
        self.damage = damage
        
    def update(self):
        self.rect.x += self.speed
        
        

        