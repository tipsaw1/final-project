from settings import *
import classes.player_class as player_class
import classes.level_class as level_class
import classes.weapon_class as weapon_class
"""
# Initialize levels
level_1 = level_class.Level(maps.level_1_map)
level_2 = level_class.Level(maps.level_2_map)
level_3 = level_class.Level(maps.level_3_map)
level_4 = level_class.Level(maps.level_4_map)
level_5 = level_class.Level(maps.level_5_map)
level_6 = level_class.Level(maps.level_6_map)
level_7 = level_class.Level(maps.level_7_map)
level_8 = level_class.Level(maps.level_8_map)
# Set adjacent rooms for levels
level_1.set_adjacents(down = level_2)
level_2.set_adjacents(up = level_1, down = level_3)
level_3.set_adjacents(up = level_2, down = level_4) #can add down after other levels
level_4.set_adjacents(up = level_3, down = level_5)
level_5.set_adjacents(up = level_4, down = level_6)
level_6.set_adjacents(up = level_5, down = level_7)
level_7.set_adjacents(up= level_6, down = level_8)
# initialize player
player = player_class.Player(level_1)
"""

