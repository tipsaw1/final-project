import pygame
import random
import math
import assets.images as img
import assets.maps as maps
pygame.init()

SCREEN_H = 720 
SCREEN_W = 1280
white = ('white')
black = ('black')
clock = pygame.time.Clock()
FPS = 60
TILESIZE = 64
HP = 10

player_sprite = pygame.sprite.GroupSingle()
enemy_sprite = pygame.sprite.GroupSingle()


# This function calculates the x and y values needed to move a specific distance at an angle
# This prevents you from moving faster when moving diagonally (1 up and 1 to the right = √2 diagonally)
# Also useful for bullets
def calculate_movement(dx, dy, speed):
    # Calculate the angle that you're moveing at
    angle = math.atan2(dy, dx)
    # Move x and y
    dx = speed*math.cos(angle)
    dy = speed*math.sin(angle)
    return dx, dy


 

