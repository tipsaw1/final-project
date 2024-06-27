from settings import *

class Npc(pygame.sprite.Sprite):
  def __init__(self, level, pos, size, idle_animation, talking_animation, dialogue):
    super().__init__(level.npc_sprites, level.all_sprites)
    self.level = level
    
    # Dialogue
    self.dialogue = dialogue
    self.displaying_dialogue = False
    # Animation
    self.animation_frame = 0
    self.animation_speed = 0.1
    self.idle_animation = idle_animation
    self.talking_animation = talking_animation
    self.current_animation = self.idle_animation
    
    self.size = size
    self.image = pygame.transform.scale(self.current_animation[int(self.animation_frame)], (size, size))
    self.rect = self.image.get_rect(topleft = pos)
    
    
  def update(self):
    self.update_animation(self.animation_speed)
    
  def interact(self):
    if not self.displaying_dialogue:
      self.displaying_dialogue = True
    else:
      self.dialogue.update_dialogue()
      self.displaying_dialogue = False
  
  def update_animation(self, amount):
    self.image = self.current_animation[int(self.animation_frame)]
    self.image = pygame.transform.scale(self.image, (self.size, self.size)) 
    self.rect = self.image.get_rect(topleft = self.rect.topleft)
    
    self.animation_frame += amount
    if self.animation_frame >= len(self.current_animation):
      self.animation_frame = 0
      
  def change_animation(self, animation, reset_frames = False):
    self.current_animation = animation
    if self.animation_frame > len(self.current_animation):
      self.animation_frame = len(self.current_animation)
      
    if reset_frames:
      self.animation_frame = 0
      
class Dialogue:
  def __init__(self, dialogue_list):
    self.dialogue_list = dialogue_list
    self.current_dialogue = 0
    self.font = pygame.font.Font(None, 64)
    self.render = self.font.render(self.dialogue_list[self.current_dialogue], True, "white")
    self.rect = pygame.Rect(SCREEN_W//8, 0, 6*SCREEN_W//8, SCREEN_H//4)
    self.rect.bottom = SCREEN_H - 50
      
  def display_dialogue(self):
    surface = pygame.display.get_surface()
    
    pygame.draw.rect(surface, "black", self.rect)
    pygame.draw.rect(surface, "white", self.rect, 5)
    surface.blit(self.render, self.rect.topleft + pygame.math.Vector2(20,20))
    
  def update_dialogue(self):
    if self.current_dialogue < len(self.dialogue_list)-1:
      self.current_dialogue += 1
      
    self.render = self.font.render(self.dialogue_list[self.current_dialogue], True, "white")
      
  