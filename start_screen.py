from settings import *
import classes.button_class as button_class
start_button = button_class.Button(button_font, "Start", "white", "green", (SCREEN_W//2, SCREEN_H//2), (150,150), 3, start_button_group)
start_button.fit_to_text()
start_button.rect.center = (SCREEN_W//2, SCREEN_H//2)

melee_button = button_class.Button(button_font, "Melee", "white", "red4", (SCREEN_W//4, SCREEN_H//3), (150,150), 3, class_button_group)
melee_button.fit_to_text()

ranger_button = button_class.Button(button_font, "Ranger", "white", "green4", (2*SCREEN_W//4, SCREEN_H//3), (150,150), 3, class_button_group)
ranger_button.fit_to_text()


mage_button = button_class.Button(button_font, "Mage", "white", "blue4", (3*SCREEN_W//4, SCREEN_H//3), (150,150), 3, class_button_group)
mage_button.fit_to_text()


ranger_button.rect.centerx = SCREEN_W//2
mage_button.rect.left = ranger_button.rect.right + 50
melee_button.rect.right = ranger_button.rect.left - 50
test = button_font.render("SELECT A CLASS:", True, "white")
test_rect = test.get_rect(midtop = (SCREEN_W//2, 50))
menu = 1


def start():
  surface = pygame.display.get_surface()
  surface.fill("black")
  
  start_button_group.update()
  start_button_group.draw(surface)
  
def class_select():
  surface = pygame.display.get_surface()
  surface.fill("black")
  
  surface.blit(test, test_rect)
  class_button_group.update()
  class_button_group.draw(surface)
  
#def class_select():
  
  