#from settings import *
import pygame
import random

print('imported enemy class')

class Enemy(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__(level.enemy_sprites)
        self.image = pygame.Surface((30, 30))  # Replace with actual enemy image
        self.image.fill((255, 0, 0))  # Red color (for illustration)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 600)  # Initial x position (adjust as needed)
        self.rect.y = random.randint(-100, -50)  # Initial y position (off-screen)
        self.speed = random.randint(1, 3)  # Enemy speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 600:  # Respawn enemy if it goes off-screen
            self.rect.y = random.randint(-100, -50)
            self.rect.x = random.randint(0, 600)
