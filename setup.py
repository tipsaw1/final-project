from settings import *
import classes.player_class as player
import classes.level_class as level
import classes.weapon_class as weapon

# Initialize levels
level_1 = level.Level(maps.level_1_map)
level_2 = level.Level(maps.level_2_map)
level_3 = level.Level(maps.level_3_map)
level_4 = level.Level(maps.level_4_map)
level_5 = level.Level(maps.level_5_map)
level_6 = level.Level(maps.level_6_map)
# Set adjacent rooms for levels
level_1.set_adjacents(down = level_2)
level_2.set_adjacents(up = level_1, down = level_3)
level_3.set_adjacents(up = level_2, down = level_4) #can add down after other levels
level_4.set_adjacents(up = level_3, down = level_5)
level_5.set_adjacents(up = level_4, down = level_6)
level_6.set_adjacents(up = level_5)
# initialize player
p1 = player.Player(level_1)

def mage_select():
    p1.equipped_weapon = weapon.Magic_weapon(1, TILESIZE*5, 2)
    p1.idle_animation = [img.mage_idle_animation_left, img.mage_idle_animation_right]
    p1.walk_animation = [img.mage_walk_animation_left,img.mage_walk_animation_right]
    p1.attack_animation = [img.mage_attack_animation_left,img.mage_attack_animation_right]
    p1.hurt_animation = [img.mage_hurt_animation_left,img.mage_hurt_animation_right]
    p1.player_class = "mage"
def archer_select():
    p1.equipped_weapon = weapon.Ranged_weapon(10, 300)
    p1.idle_animation = [img.archer_idle_animation_left,img.archer_idle_animation_right]
    p1.walk_animation = [img.archer_walk_animation_left,img.archer_walk_animation_right]
    p1.attack_animation = [img.archer_attack_animation_left,img.archer_attack_animation_right]
    p1.hurt_animation = [img.archer_hurt_animation_left,img.archer_hurt_animation_right]
    p1.player_class = "archer"
def knight_select():
    p1.equipped_weapon = weapon.Melee_weapon(10, TILESIZE*2, 500)
    p1.idle_animation = [img.knight_idle_animation_left, img.knight_idle_animation_right]
    p1.walk_animation = [img.knight_walk_animation_left, img.knight_walk_animation_right]
    p1.attack_animation = [img.knight_attack_animation_left,img.knight_attack_animation_right]
    p1.hurt_animation = [img.knight_hurt_animation_left,img.knight_hurt_animation_right]
    p1.player_class = "knight"