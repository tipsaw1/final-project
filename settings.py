import pygame
import random
import math
import assets.images as img
import assets.maps as maps
pygame.init()

# Constants
SCREEN_H = 720 
SCREEN_W = 1280
white = ('white')
black = ('black')
clock = pygame.time.Clock()
FPS = 60
TILESIZE = 64
button_font = pygame.font.SysFont("impact", 100)

# Player sprite accesible from any file
player_sprite = pygame.sprite.GroupSingle()
# Level sprite
level_sprite = pygame.sprite.GroupSingle()

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




# This is a new subclass of the pygame.Group class
# This allows us to create an offset for it to be placed,
# letting us move the screen and everything on it
class OffsetGroup(pygame.sprite.Group):
    def __init__(self, *sprites):
        super().__init__(*sprites)
        # Stores an x and y value (by default is (0,0))
        self.offset = pygame.math.Vector2()
    
    # Replaces normal group draw function
    def draw(self, surface):
        for sprite in self.sprites():
            #X offset is set to the player's x position - half the screen
            #Y offset is set to the player's y position - half the screen
            self.offset.x = player_sprite.sprite.rect.x-SCREEN_W//2
            self.offset.y =player_sprite.sprite.rect.y-SCREEN_H//2
            
            # Keep screen within borders
            # If the left side of the screen is at 0, it cannot decrease
            if self.offset.x <= 0:
                self.offset.x = 0
            # If the left side of the screen is at the right side of the map
            # minus the width of the screen, it cannot increase
            # (if the right side of the screen is at the right side of the map)
            if self.offset.x >= player_sprite.sprite.level.rect.right-SCREEN_W:
                self.offset.x = player_sprite.sprite.level.rect.right-SCREEN_W
            # If the top of the screen is at the top of the map, the y offset
            # cannot decrease
            if self.offset.y <= 0:
                self.offset.y = 0
            
            # If the top of the screen is at the bottom of the map minus the
            # height of the screen, the y offset cannot increase
            # (if the bottom of the screen is at the bottom of the map)
            if self.offset.y >= player_sprite.sprite.level.rect.bottom-SCREEN_H:
                self.offset.y = player_sprite.sprite.level.rect.bottom-SCREEN_H
            
            
            
            '''
            Offset is set to the players position - half the screen, meaning that
            As the player moves left, the offset decreases .
            
            ex: player position of 0 = offset value of -half the screen
            
            The sprites position is then subtracted by the offset, meaning the farther
            left the player goes, the farther right the sprite is drawn and vice versa
            
            The player is also affected by this, meaning that it cancels out their
            position and places them in the center of the screen
            
            ex: player position of 0 - offset value of -half the screen
             = player position of half the screen (2 negatives cancel out)
             
             The Rects remain in the same position relative to each other,
             allowing you to use collisions and other pygame Rect features
            '''
            if sprite != player_sprite.sprite:
                surface.blit(sprite.image, sprite.rect.topleft-self.offset)
        
        # Ensures player sprite is always on top
        if player_sprite.sprite in self.sprites():
            surface.blit(player_sprite.sprite.image, player_sprite.sprite.rect.topleft - self.offset)

# Button group class
class ButtonGroup():
    def __init__(self, *buttons):
        self.buttons = list(buttons)
        
    def draw(self, surface):
        for button in self.buttons:
            button.draw(surface)
            
    def update(self):
        for button in self.buttons:
            button.update()
            
    def add(self, button):
        self.buttons.append(button)
        
start_button_group = ButtonGroup()
class_button_group = ButtonGroup()