from settings import *
import classes.player_class as player
import classes.level_class as level
import classes.weapon_class as weapon

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))


# Initialize levels
level_1 = level.Level(maps.level_1_map, img.level_1_img)
level_2 = level.Level(maps.level_2_map, img.level_1_img)
level_3 = level.Level(maps.level_3_map, img.level_1_img)
level_4 = level.Level(maps.level_4_map, img.level_1_img)
level_5 = level.Level(maps.level_5_map, img.level_1_img)
level_6 = level.Level(maps.level_6_map, img.level_1_img)
# Set adjacent rooms for levels
level_1.set_adjacents(down = level_2)
level_2.set_adjacents(up = level_1, down = level_3)
level_3.set_adjacents(up = level_2, down = level_4) #can add down after other levels
level_4.set_adjacents(up = level_3, down = level_5)
level_5.set_adjacents(up = level_4)
# initialize player
p1 = player.Player(level_1)

test_weapon = weapon.Ranged_weapon(10, 500)
p1.equipped_weapon = test_weapon
#

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    level_sprite.update()
    level_sprite.draw(screen)
    level_sprite.sprite.all_sprites.update()
    level_sprite.sprite.all_sprites.draw(screen)
    #if player_sprite.sprite.hp <= 0:
        #running = False
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()
