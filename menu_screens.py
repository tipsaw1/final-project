import game_class
import settings, pygame
import classes.button_class as button_class
import classes.weapon_class as weapon_class

start_button_group = settings.ButtonGroup()
class_button_group = settings.ButtonGroup()
pause_button_group = settings.ButtonGroup()
# Start screen
start_button = button_class.Button(settings.button_font, "START", "white", "green", (game_class.main_game.SCREEN_W//2, game_class.main_game.SCREEN_H//2), (150,150), 3, start_button_group)
start_button.fit_to_text()
start_button.rect.center = (game_class.main_game.SCREEN_W//2, game_class.main_game.SCREEN_H//2)

# Class select
knight_button = button_class.Button(settings.button_font, "KNIGHT", "white", "red4", (game_class.main_game.SCREEN_W//4, game_class.main_game.SCREEN_H//3), (150,150), 3, class_button_group)
knight_button.fit_to_text()

archer_button = button_class.Button(settings.button_font, "ARCHER", "white", "green4", (2*game_class.main_game.SCREEN_W//4, game_class.main_game.SCREEN_H//3), (150,150), 3, class_button_group)
archer_button.fit_to_text()


mage_button = button_class.Button(settings.button_font, "MAGE", "white", "blue4", (3*game_class.main_game.SCREEN_W//4, game_class.main_game.SCREEN_H//3), (150,150), 3, class_button_group)
mage_button.fit_to_text()

archer_button.rect.centerx = game_class.main_game.SCREEN_W//2
mage_button.rect.left = archer_button.rect.right + 50
knight_button.rect.right = archer_button.rect.left - 50

class_text = settings.button_font.render("SELECT A CLASS:", True, "white")
class_text_rect = class_text.get_rect(midtop = (game_class.main_game.SCREEN_W//2, 50))

# Pause screen
resume_button = button_class.Button(settings.button_font, "RESUME", "white", "green", (game_class.main_game.SCREEN_W//2, game_class.main_game.SCREEN_H//3), (150,150), 3, pause_button_group)
resume_button.fit_to_text()
resume_button.rect.center = (game_class.main_game.SCREEN_W//2, game_class.main_game.SCREEN_H//3)

quit_button = button_class.Button(settings.button_font, "QUIT", "white", "red", (game_class.main_game.SCREEN_W//2, 2*game_class.main_game.SCREEN_H//3), (150,150), 3, pause_button_group)
quit_button.fit_to_text()
quit_button.rect.center = (game_class.main_game.SCREEN_W//2, 2*game_class.main_game.SCREEN_H//3)

background_1 = pygame.transform.scale(settings.img.tile_2, (game_class.main_game.SCREEN_W, game_class.main_game.SCREEN_H))
background_2 = pygame.transform.scale(settings.img.wall_img_1, (game_class.main_game.SCREEN_W, game_class.main_game.SCREEN_H))

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
  game.player.equipped_weapon = weapon_class.Magic_weapon(1.55, game_class.main_game.TILESIZE*5, 2, game)
  game.player.idle_animation = [settings.img.mage_idle_animation_left, settings.img.mage_idle_animation_right]
  game.player.walk_animation = [settings.img.mage_walk_animation_left,settings.img.mage_walk_animation_right]
  game.player.attack_animation = [settings.img.mage_attack_animation_left,settings.img.mage_attack_animation_right]
  game.player.hurt_animation = [settings.img.mage_hurt_animation_left,settings.img.mage_hurt_animation_right]
  game.player.dead_image = [settings.img.mage_death_left, settings.img.mage_death_right]
  game.player.player_class = "mage"
    
def archer_select(game):
  game.player.equipped_weapon = weapon_class.Ranged_weapon(25, 300, game)
  game.player.idle_animation = [settings.img.archer_idle_animation_left,settings.img.archer_idle_animation_right]
  game.player.walk_animation = [settings.img.archer_walk_animation_left,settings.img.archer_walk_animation_right]
  game.player.attack_animation = [settings.img.archer_attack_animation_left,settings.img.archer_attack_animation_right]
  game.player.hurt_animation = [settings.img.archer_hurt_animation_left,settings.img.archer_hurt_animation_right]
  game.player.dead_image = [settings.img.archer_death_left, settings.img.archer_death_right]
  game.player.player_class = "archer"
  
def knight_select(game):
  game.player.equipped_weapon = weapon_class.Melee_weapon(35, 5*game_class.main_game.TILESIZE//2, 500, game)
  game.player.idle_animation = [settings.img.knight_idle_animation_left, settings.img.knight_idle_animation_right]
  game.player.walk_animation = [settings.img.knight_walk_animation_left, settings.img.knight_walk_animation_right]
  game.player.attack_animation = [settings.img.knight_attack_animation_left,settings.img.knight_attack_animation_right]
  game.player.hurt_animation = [settings.img.knight_hurt_animation_left,settings.img.knight_hurt_animation_right]
  game.player.dead_image = [settings.img.knight_death_left, settings.img.knight_death_right]
  game.player.player_class = "knight"
    

def check_events(game, event):
  if event.type == pygame.MOUSEBUTTONDOWN:
    
    # Buttons for the menu screens
    match game.current_screen:
      # Start screen
      case "start":
        if start_button.collide(event.pos):
          game.current_screen = "class"
        
      
      # Class select screen
      case "class":
        if archer_button.collide(event.pos):
          archer_select(game)
          game.current_screen = "gameplay"
          
          
        elif knight_button.collide(event.pos):
          knight_select(game)
          game.current_screen = "gameplay"
          
        elif mage_button.collide(event.pos):
          mage_select(game)
          game.current_screen = "gameplay"
        
    # Pause screen buttons
    if game.paused:
      if resume_button.collide(event.pos):
        game.paused = False
        
      if quit_button.collide(event.pos):
        game.quit = True
    
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_ESCAPE:
      game.paused = True
      