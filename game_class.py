import pygame
import assets.maps as maps
import classes.level_class as level_class
import classes.player_class as player_class
class game:
  # screen constants
  SCREEN_H = 720 
  SCREEN_W = 1280
  TILESIZE = 64
  paused = False
  quit = False
  FPS = 60
  
  # Current screen variable
  # will equal "start", "class", "gameplay", "gameover", or "gamewon"
  current_screen = "start"
  
  # Screen
  screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
  
  
  
  
  
  def __init__(self):
    # Initialize levels
    self.level_1 = level_class.Level(maps.level_1_map, self)
    self.level_2 = level_class.Level(maps.level_2_map, self)
    self.level_3 = level_class.Level(maps.level_3_map, self)
    self.level_4 = level_class.Level(maps.level_4_map, self)
    self.level_5 = level_class.Level(maps.level_5_map, self)
    self.level_6 = level_class.Level(maps.level_6_map, self)
    self.level_7 = level_class.Level(maps.level_7_map, self)
    self.level_8 = level_class.Level(maps.level_8_map, self)
    
    # Set adjacent rooms for levels
    self.level_1.set_adjacents(down = self.level_2)
    self.level_2.set_adjacents(up = self.level_1, down = self.level_3)
    self.level_3.set_adjacents(up = self.level_2, down = self.level_4) #can add down after other levels
    self.level_4.set_adjacents(up = self.level_3, down = self.level_5)
    self.level_5.set_adjacents(up = self.level_4, down = self.level_6)
    self.level_6.set_adjacents(up = self.level_5, down = self.level_7)
    self.level_7.set_adjacents(up= self.level_6, down = self.level_8)
  
    # Set current level
    self.current_level = self.level_1
    
    # Player instance
    self.player_group = pygame.sprite.GroupSingle()
    self.player = player_class.Player(self)
'''
  def gameplay(self):
    if self.paused:
      menu_screens.pause_screen(self)
      
    elif self.current_screen == "start":
      menu_screens.start_screen(self)
      
    elif self.current_screen == "class":
      menu_screens.class_select_screen(self)
      
    elif self.current_screen == "gameplay":
      game_play.play_game(self)
      ui.draw_ui(self)
      
    elif self.current_screen == "gameover":
      game_play.game_over(self.screen)
      
    elif self.current_screen == "gamewon":
      game_play.victory(self.screen)
    
  def check_events(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      
      # Buttons for the menu screens
      match self.current_screen:
        # Start screen
        case "start":
          if menu_screens.start_button.collide(event.pos):
            self.current_screen = "class"
          
        
        # Class select screen
        case "class":
          if menu_screens.archer_button.collide(event.pos):
            menu_screens.archer_select(self)
            self.current_screen = "gameplay"
            
            
          elif menu_screens.knight_button.collide(event.pos):
            menu_screens.knight_select(self)
            self.current_screen = "gameplay"
            
          elif menu_screens.mage_button.collide(event.pos):
            menu_screens.mage_select(self)
            self.current_screen = "gameplay"
          
      # Pause screen buttons
      if self.paused:
        if menu_screens.resume_button.collide(event.pos):
          self.paused = False
          
        if menu_screens.quit_button.collide(event.pos):
          self.quit = True
      
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        self.paused = True
'''
main_game = game()

  