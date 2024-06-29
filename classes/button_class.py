import settings, pygame

class Button():
  def __init__(self, font, text, text_color, collide_color, pos, size, width, group):
    group.add(self)
    self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
    self.collide_color = collide_color
    self.text_color = text_color
    self.rect_color = text_color
    self.font = font
    self.text = text
    self.text_render = font.render(text, True, text_color)
    self.text_rect = self.text_render.get_rect(center = self.rect.center)
    self.width = width
    
  def draw(self, surface):
    pygame.draw.rect(surface, self.rect_color, self.rect, self.width)
    surface.blit(self.text_render, self.text_rect)
  
  def update(self):
    mousePos = pygame.mouse.get_pos()
    if self.collide(mousePos):
      self.change_text(self.text, self.collide_color)
      
    else:
      self.change_text(self.text, self.text_color)
      
  def collide(self, mousePos):
    if self.rect.collidepoint(mousePos):
      return True
    return False
  
  def change_text(self, text, color):
    self.text_render = self.font.render(text, True, color)
    self.text_rect = self.text_render.get_rect(center = self.rect.center)
    self.rect_color = color
    
  def fit_to_text(self):
    tmp = self.rect.center
    self.rect.top = self.text_rect.top -10
    self.rect.left = self.text_rect.left -10
    self.rect.width = self.text_rect.width + 20
    self.rect.height = self.text_rect.height + 20
    self.rect.center = tmp