#from settings import *
import pygame

print('imported enemy class')

class Enemy(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__(level.enemy_sprites)
        
        
        
        
    def update(self):
        pass
        
