from settings import *
import classes.button_class as button_class
import pygame
# Start screen
start_button = button_class.Button(button_font, "START", "white", "green", (SCREEN_W//2, SCREEN_H//2), (150,150), 3, start_button_group)
start_button.fit_to_text()
start_button.rect.center = (SCREEN_W//2, SCREEN_H//2)

# Class select
knight_button = button_class.Button(button_font, "KNIGHT", "white", "red4", (SCREEN_W//4, SCREEN_H//3), (150,150), 3, class_button_group)
knight_button.fit_to_text()

archer_button = button_class.Button(button_font, "ARCHER", "white", "green4", (2*SCREEN_W//4, SCREEN_H//3), (150,150), 3, class_button_group)
archer_button.fit_to_text()


mage_button = button_class.Button(button_font, "MAGE", "white", "blue4", (3*SCREEN_W//4, SCREEN_H//3), (150,150), 3, class_button_group)
mage_button.fit_to_text()

archer_button.rect.centerx = SCREEN_W//2
mage_button.rect.left = archer_button.rect.right + 50
knight_button.rect.right = archer_button.rect.left - 50

class_text = button_font.render("SELECT A CLASS:", True, "white")
class_text_rect = class_text.get_rect(midtop = (SCREEN_W//2, 50))

# Pause screen
resume_button = button_class.Button(button_font, "RESUME", "white", "green", (SCREEN_W//2, SCREEN_H//3), (150,150), 3, pause_button_group)
resume_button.fit_to_text()
resume_button.rect.center = (SCREEN_W//2, SCREEN_H//3)

quit_button = button_class.Button(button_font, "QUIT", "white", "red", (SCREEN_W//2, 2*SCREEN_H//3), (150,150), 3, pause_button_group)
quit_button.fit_to_text()
quit_button.rect.center = (SCREEN_W//2, 2*SCREEN_H//3)

background_1 = pygame.transform.scale(img.tile_2, (SCREEN_W, SCREEN_H))
background_2 = pygame.transform.scale(img.wall_img_1, (SCREEN_W, SCREEN_H))

def start_screen(surface):
  surface.fill("black")
  start_button_group.update()
  start_button_group.draw(surface)
  
def class_select_screen(surface):
  surface.fill("black")
  
  surface.blit(class_text, class_text_rect)
  class_button_group.update()
  class_button_group.draw(surface)
  
def pause_screen(surface):
  surface.fill("black")
  
  pause_button_group.update()
  pause_button_group.draw(surface)
  
  