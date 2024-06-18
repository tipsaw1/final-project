from settings import *
import classes.player_class as player
import classes.level_class as level

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))


# Initialize levels
level_1 = level.Level(maps.level_1_map, img.level_1_img)
level_2 = level.Level(maps.level_2_map, img.level_2_img)

# Set adjacent rooms for levels
level_1.set_adjacent("down", level_2)
level_2.set_adjacent("up", level_1)

# initialize player
p1 = player.Player(level_1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("green")
    level_sprite.update()
    level_sprite.draw(screen)
    player_sprite.sprite.level.all_sprites.update()
    player_sprite.sprite.level.all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()
