from settings import *
import classes.button_class as button_class
start_button = button_class.Button(button_font, "Start", "white", "white", (SCREEN_W//2, SCREEN_H//2), (150,150), 3)
start_button.fit_to_text()
start_button.rect.center = (SCREEN_W//2, SCREEN_H//2)
menu = True
def start():
  surface = pygame.display.get_surface()
  surface.fill("black")
  
  button_group.draw(surface)
  for button in button_group.buttons:
    if button.collide(pygame.mouse.get_pos()):
      button.color = "green"
      button.change_text(button.text, "green")
    else:
      button.color = "white"
      button.change_text(button.text, "white")
  
  