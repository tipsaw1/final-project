import pygame
import math
import assets.images as img
import assets.maps as maps
import assets.Sounds as sound

button_font = pygame.font.SysFont("impact", 100)

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


        
