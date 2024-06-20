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
'''
value = 0
screen = pygame.display.set_mode((500,500))
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(player_idle_animation[int(value)], (0,0))
    value += 0.25
    if value >= len(player_idle_animation):
        value = 0
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
'''

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

# Slash
slash_img = pygame.image.load("assets/images/slash.png")
wave_attack_img = pygame.image.load("assets/images/fire_ring.png")

# Arrow
arrow_img = pygame.Surface((20,20))
arrow_img.fill('yellow')

# Items
health_item = pygame.Surface((50,50))
health_item.fill("green")

#Hp
health_bar_back = pygame.Surface((50,10))
health_bar_back.fill("red4")

health_bar_front = pygame.Surface((50,10))
health_bar_front.fill("green")
        