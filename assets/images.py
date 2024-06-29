import pygame
pygame.init()
def load_animation(*images):
    animation_list = []
    for image in images:
        animation_list.append(pygame.image.load(image))
    return animation_list
# Player 1 image (temporarily a blue square)
player_idle_animation = load_animation("assets/Sprite_1/idle/default_sprite_idle_1.png","assets/Sprite_1/idle/default_sprite_idle_2.png","assets/Sprite_1/idle/default_sprite_idle_3.png","assets/Sprite_1/idle/default_sprite_idle_4.png")
player_walk_animation = load_animation("assets/Sprite_1/walk/default_sprite_walk_1.png","assets/Sprite_1/walk/default_sprite_walk_2.png","assets/Sprite_1/walk/default_sprite_walk_3.png","assets/Sprite_1/walk/default_sprite_walk_4.png")
player_hurt_animation = load_animation("assets/Sprite_1/injured/default_sprite_injured_1.png","assets/Sprite_1/injured/default_sprite_injured_1.png")
player_attack_animation = load_animation("assets/Sprite_1/attack/default_sprite_attack_1.png","assets/Sprite_1/attack/default_sprite_attack_2.png","assets/Sprite_1/attack/default_sprite_attack_3.png","assets/Sprite_1/attack/default_sprite_attack_4.png")

mage_idle_animation_left = load_animation("assets/mage_sprites/left/idle/mage_idle_1.png","assets/mage_sprites/left/idle/mage_idle_2.png","assets/mage_sprites/left/idle/mage_idle_3.png","assets/mage_sprites/left/idle/mage_idle_4.png")
mage_walk_animation_left = load_animation("assets/mage_sprites/left/walk/mage_walk_1.png","assets/mage_sprites/left/walk/mage_walk_2.png","assets/mage_sprites/left/walk/mage_walk_3.png","assets/mage_sprites/left/walk/mage_walk_4.png")
mage_hurt_animation_left = load_animation("assets/mage_sprites/left/other/mage_injured.png","assets/mage_sprites/left/other/mage_ghost.png","assets/mage_sprites/left/other/mage_injured.png","assets/mage_sprites/left/other/mage_ghost.png")
mage_attack_animation_left = load_animation("assets/mage_sprites/left/attack/mage_attack_1.png","assets/mage_sprites/left/attack/mage_attack_2.png","assets/mage_sprites/left/attack/mage_attack_3.png","assets/mage_sprites/left/attack/mage_attack_4.png")
mage_death_left = pygame.image.load("assets/mage_sprites/left/other/mage_dead.png")

mage_idle_animation_right = load_animation("assets/mage_sprites/right/idle/mage_idle_1.png","assets/mage_sprites/right/idle/mage_idle_2.png","assets/mage_sprites/right/idle/mage_idle_3.png","assets/mage_sprites/right/idle/mage_idle_4.png")
mage_walk_animation_right = load_animation("assets/mage_sprites/right/walk/mage_walk_1.png","assets/mage_sprites/right/walk/mage_walk_2.png","assets/mage_sprites/right/walk/mage_walk_3.png","assets/mage_sprites/right/walk/mage_walk_4.png")
mage_hurt_animation_right = load_animation("assets/mage_sprites/right/other/mage_injured.png","assets/mage_sprites/right/other/mage_ghost.png","assets/mage_sprites/right/other/mage_injured.png","assets/mage_sprites/right/other/mage_ghost.png")
mage_attack_animation_right = load_animation("assets/mage_sprites/right/attack/mage_attack_1.png","assets/mage_sprites/right/attack/mage_attack_2.png","assets/mage_sprites/right/attack/mage_attack_3.png","assets/mage_sprites/right/attack/mage_attack_4.png")
mage_death_right = pygame.image.load("assets/mage_sprites/right/other/mage_dead.png")

archer_idle_animation_left = load_animation("assets/archer_sprites/left/idle/archer_idle_1.png","assets/archer_sprites/left/idle/archer_idle_2.png","assets/archer_sprites/left/idle/archer_idle_3.png","assets/archer_sprites/left/idle/archer_idle_4.png")
archer_walk_animation_left = load_animation("assets/archer_sprites/left/walk/archer_walk_1.png","assets/archer_sprites/left/walk/archer_walk_2.png","assets/archer_sprites/left/walk/archer_walk_3.png","assets/archer_sprites/left/walk/archer_walk_4.png")
archer_hurt_animation_left = load_animation("assets/archer_sprites/left/other/archer_injured.png","assets/archer_sprites/left/other/archer_ghost.png","assets/archer_sprites/left/other/archer_injured.png","assets/archer_sprites/left/other/archer_ghost.png")
archer_attack_animation_left = load_animation("assets/archer_sprites/left/attack/archer_attack_1.png","assets/archer_sprites/left/attack/archer_attack_2.png","assets/archer_sprites/left/attack/archer_attack_3.png","assets/archer_sprites/left/attack/archer_attack_4.png")
archer_death_left = pygame.image.load("assets/archer_sprites/left/other/archer_dead.png")

archer_idle_animation_right = load_animation("assets/archer_sprites/right/idle/archer_idle_1.png","assets/archer_sprites/right/idle/archer_idle_2.png","assets/archer_sprites/right/idle/archer_idle_3.png","assets/archer_sprites/right/idle/archer_idle_4.png")
archer_walk_animation_right = load_animation("assets/archer_sprites/right/walk/archer_walk_1.png","assets/archer_sprites/right/walk/archer_walk_2.png","assets/archer_sprites/right/walk/archer_walk_3.png","assets/archer_sprites/right/walk/archer_walk_4.png")
archer_hurt_animation_right = load_animation("assets/archer_sprites/right/other/archer_injured.png","assets/archer_sprites/right/other/archer_ghost.png","assets/archer_sprites/right/other/archer_injured.png","assets/archer_sprites/right/other/archer_ghost.png")
archer_attack_animation_right = load_animation("assets/archer_sprites/right/attack/archer_attack_1.png","assets/archer_sprites/right/attack/archer_attack_2.png","assets/archer_sprites/right/attack/archer_attack_3.png","assets/archer_sprites/right/attack/archer_attack_4.png")
archer_death_right = pygame.image.load("assets/archer_sprites/right/other/archer_dead.png")

knight_idle_animation_left = load_animation("assets/knight_sprites/left/idle/knight_idle_1.png","assets/knight_sprites/left/idle/knight_idle_2.png","assets/knight_sprites/left/idle/knight_idle_3.png","assets/knight_sprites/left/idle/knight_idle_4.png")
knight_walk_animation_left = load_animation("assets/knight_sprites/left/walk/knight_walk_1.png","assets/knight_sprites/left/walk/knight_walk_2.png","assets/knight_sprites/left/walk/knight_walk_3.png","assets/knight_sprites/left/walk/knight_walk_4.png")
knight_hurt_animation_left = load_animation("assets/knight_sprites/left/other/knight_injured.png","assets/knight_sprites/left/other/knight_ghost.png","assets/knight_sprites/left/other/knight_injured.png","assets/knight_sprites/left/other/knight_ghost.png")
knight_attack_animation_left = load_animation("assets/knight_sprites/left/attack/knight_attack_1.png","assets/knight_sprites/left/attack/knight_attack_2.png","assets/knight_sprites/left/attack/knight_attack_3.png","assets/knight_sprites/left/attack/knight_attack_4.png")
knight_death_left = pygame.image.load("assets/knight_sprites/left/other/knight_dead.png")

knight_idle_animation_right = load_animation("assets/knight_sprites/right/idle/knight_idle_1.png","assets/knight_sprites/right/idle/knight_idle_2.png","assets/knight_sprites/right/idle/knight_idle_3.png","assets/knight_sprites/right/idle/knight_idle_4.png")
knight_walk_animation_right = load_animation("assets/knight_sprites/right/walk/knight_walk_1.png","assets/knight_sprites/right/walk/knight_walk_2.png","assets/knight_sprites/right/walk/knight_walk_3.png","assets/knight_sprites/right/walk/knight_walk_4.png")
knight_hurt_animation_right = load_animation("assets/knight_sprites/right/other/knight_injured.png","assets/knight_sprites/right/other/knight_ghost.png","assets/knight_sprites/right/other/knight_injured.png","assets/knight_sprites/right/other/knight_ghost.png")
knight_attack_animation_right = load_animation("assets/knight_sprites/right/attack/knight_attack_1.png","assets/knight_sprites/right/attack/knight_attack_2.png","assets/knight_sprites/right/attack/knight_attack_3.png","assets/knight_sprites/right/attack/knight_attack_4.png")
knight_death_right = pygame.image.load("assets/knight_sprites/right/other/knight_dead.png")

skeleton_melee_idle_animation = load_animation("assets/skeleton_melee/idle/skeleton_idle_1.png","assets/skeleton_melee/idle/skeleton_idle_2.png","assets/skeleton_melee/idle/skeleton_idle_3.png","assets/skeleton_melee/idle/skeleton_idle_4.png","assets/skeleton_melee/idle/skeleton_idle_5.png","assets/skeleton_melee/idle/skeleton_idle_6.png","assets/skeleton_melee/idle/skeleton_idle_7.png","assets/skeleton_melee/idle/skeleton_idle_8.png","assets/skeleton_melee/idle/skeleton_idle_9.png","assets/skeleton_melee/idle/skeleton_idle_10.png")
skeleton_melee_walk_animation = load_animation("assets/skeleton_melee/walk/skeleton_walk_1.png","assets/skeleton_melee/walk/skeleton_walk_2.png","assets/skeleton_melee/walk/skeleton_walk_3.png","assets/skeleton_melee/walk/skeleton_walk_4.png","assets/skeleton_melee/walk/skeleton_walk_5.png",)
skeleton_melee_attack_animation = load_animation("assets/skeleton_melee/attack/skeleton_attack_1.png","assets/skeleton_melee/attack/skeleton_attack_2.png","assets/skeleton_melee/attack/skeleton_attack_3.png","assets/skeleton_melee/attack/skeleton_attack_4.png","assets/skeleton_melee/attack/skeleton_attack_5.png","assets/skeleton_melee/attack/skeleton_attack_6.png","assets/skeleton_melee/attack/skeleton_attack_7.png","assets/skeleton_melee/attack/skeleton_attack_8.png","assets/skeleton_melee/attack/skeleton_attack_9.png","assets/skeleton_melee/attack/skeleton_attack_10.png")
skeleton_melee_hurt_animation = load_animation("assets/skeleton_melee/hurt/skeleton_hurt_1.png","assets/skeleton_melee/hurt/skeleton_hurt_2.png","assets/skeleton_melee/hurt/skeleton_hurt_3.png","assets/skeleton_melee/hurt/skeleton_hurt_4.png","assets/skeleton_melee/hurt/skeleton_hurt_5.png",)
melee_skeleton_animations = [skeleton_melee_idle_animation, skeleton_melee_walk_animation, skeleton_melee_attack_animation, skeleton_melee_hurt_animation]

skeleton_archer_idle_animation = load_animation("assets/skeleton_archer/idle/skeleton_archer_idle_1.png","assets/skeleton_archer/idle/skeleton_archer_idle_2.png","assets/skeleton_archer/idle/skeleton_archer_idle_3.png","assets/skeleton_archer/idle/skeleton_archer_idle_4.png","assets/skeleton_archer/idle/skeleton_archer_idle_5.png","assets/skeleton_archer/idle/skeleton_archer_idle_6.png","assets/skeleton_archer/idle/skeleton_archer_idle_7.png","assets/skeleton_archer/idle/skeleton_archer_idle_8.png","assets/skeleton_archer/idle/skeleton_archer_idle_9.png","assets/skeleton_archer/idle/skeleton_archer_idle_10.png")
skeleton_archer_walk_animation = load_animation("assets/skeleton_archer/walk/skeleton_archer_walk_1.png","assets/skeleton_archer/walk/skeleton_archer_walk_2.png","assets/skeleton_archer/walk/skeleton_archer_walk_3.png","assets/skeleton_archer/walk/skeleton_archer_walk_4.png","assets/skeleton_archer/walk/skeleton_archer_walk_5.png",)
skeleton_archer_attack_animation = load_animation("assets/skeleton_archer/attack/skeleton_archer_attack_1.png","assets/skeleton_archer/attack/skeleton_archer_attack_2.png","assets/skeleton_archer/attack/skeleton_archer_attack_3.png","assets/skeleton_archer/attack/skeleton_archer_attack_4.png","assets/skeleton_archer/attack/skeleton_archer_attack_5.png","assets/skeleton_archer/attack/skeleton_archer_attack_6.png","assets/skeleton_archer/attack/skeleton_archer_attack_7.png","assets/skeleton_archer/attack/skeleton_archer_attack_8.png")
skeleton_archer_hurt_animation = load_animation("assets/skeleton_archer/hurt/skeleton_archer_hurt_1.png","assets/skeleton_archer/hurt/skeleton_archer_hurt_2.png","assets/skeleton_archer/hurt/skeleton_archer_hurt_3.png")
archer_skeleton_animations = [skeleton_archer_idle_animation, skeleton_archer_walk_animation, skeleton_archer_attack_animation, skeleton_archer_hurt_animation]

tile_1 = pygame.image.load("assets/images/tile_1.jpg")
tile_2 = pygame.image.load("assets/images/tile_2.jpg")
tile_3 = pygame.image.load("assets/images/tile_3.jpg")

# wall image (temporarily a green square)
wall_img_1 = pygame.image.load("assets/images/wall_tile.png")

# Enemy image (temporarily a red square)
enemy_img_1 = pygame.Surface((50, 50))
enemy_img_1.fill('red')

enemy_img_2 = pygame.Surface((50, 50))
enemy_img_2.fill('orange')

boss_enemy_img = pygame.Surface((120, 120))
boss_enemy_img.fill("green")

enemy_hurt_img = pygame.Surface((50,50))
enemy_hurt_img.fill("white")

# Npcs

# Slash
slash_img = pygame.image.load("assets/images/slash.png")
wave_attack_img = pygame.image.load("assets/images/fire_ring.png")

# Arrow
arrow_img = pygame.image.load("assets/archer_sprites/right/other/arrow.png")

# Fireball
fireball_img = pygame.image.load("assets/mage_sprites/fireball.png")

# Items
health_item = pygame.Surface((50,50))
health_item.fill("green")

#Hp
health_bar_back = pygame.Surface((50,10))
health_bar_back.fill("red4")

health_bar_front = pygame.Surface((50,10))
health_bar_front.fill("green")
        