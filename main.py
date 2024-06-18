from settings import *
import classes.player_class as player
import classes.level_class as level
import classes.weapon_class as weapon


screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

level_1 = level.Level(maps.level_1_map, img.level_1_img)
p1 = player.Player(level_1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white)
    player_sprite.sprite.level.update()
    player_sprite.sprite.level.draw(screen)
    player_sprite.draw(screen)
    player_sprite.update()
    
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()
