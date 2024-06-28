from settings import *
import classes.button_class as button_class
import classes.weapon_class as weapon_class
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

def start_screen(game):
  game.screen.fill("black")
  start_button_group.update()
  start_button_group.draw(game.screen)
  
def class_select_screen(game):
  game.screen.fill("black")
  game.screen.blit(class_text, class_text_rect)
  class_button_group.update()
  class_button_group.draw(game.screen)
  
def pause_screen(game):
  game.screen.fill("black")
  
  pause_button_group.update()
  pause_button_group.draw(game.screen)
  
def mage_select(game):
  game.player.equipped_weapon = weapon_class.Magic_weapon(1.55, TILESIZE*5, 2, game)
  game.player.idle_animation = [img.mage_idle_animation_left, img.mage_idle_animation_right]
  game.player.walk_animation = [img.mage_walk_animation_left,img.mage_walk_animation_right]
  game.player.attack_animation = [img.mage_attack_animation_left,img.mage_attack_animation_right]
  game.player.hurt_animation = [img.mage_hurt_animation_left,img.mage_hurt_animation_right]
  game.player.dead_image = [img.mage_death_left, img.mage_death_right]
  game.player.player_class = "mage"
    
def archer_select(game):
  game.player.equipped_weapon = weapon_class.Ranged_weapon(25, 300, game)
  game.player.idle_animation = [img.archer_idle_animation_left,img.archer_idle_animation_right]
  game.player.walk_animation = [img.archer_walk_animation_left,img.archer_walk_animation_right]
  game.player.attack_animation = [img.archer_attack_animation_left,img.archer_attack_animation_right]
  game.player.hurt_animation = [img.archer_hurt_animation_left,img.archer_hurt_animation_right]
  game.player.dead_image = [img.archer_death_left, img.archer_death_right]
  game.player.player_class = "archer"
  
def knight_select(game):
  game.player.equipped_weapon = weapon_class.Melee_weapon(35, 5*TILESIZE//2, 500, game)
  game.player.idle_animation = [img.knight_idle_animation_left, img.knight_idle_animation_right]
  game.player.walk_animation = [img.knight_walk_animation_left, img.knight_walk_animation_right]
  game.player.attack_animation = [img.knight_attack_animation_left,img.knight_attack_animation_right]
  game.player.hurt_animation = [img.knight_hurt_animation_left,img.knight_hurt_animation_right]
  game.player.dead_image = [img.knight_death_left, img.knight_death_right]
  game.player.player_class = "knight"
    
