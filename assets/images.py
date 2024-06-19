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
# Level 1 background (temporarily a tan square)
level_1_img = pygame.Surface((50,50))
level_1_img.fill("navajowhite2")


player_hurt_img = pygame.Surface((50,50))
player_hurt_img.fill("white")
# Level 2 background (temporarily a gray square)
#level_2_img = pygame.image.load("assets/images/dungeonBG.png")


# Level 3 backround :] made by yesung yay
#level_3_img = pygame.image.load("assets/images/dungeonBG.png")


# wall image (temporarily a green square)
wall_img_1 = pygame.Surface((50,50))
wall_img_1.fill("forestgreen")

# Enemy image (temporarily a red square)
enemy_img_1 = pygame.Surface((50, 50))
enemy_img_1.fill('red')

enemy_img_2 = pygame.Surface((50, 50))
enemy_img_2.fill('orange')

boss_enemy_img = pygame.Surface((120, 120))
boss_enemy_img.fill("green")
# Slash
slash_img = pygame.image.load("assets/images/slash.png")
wave_attack_img = pygame.image.load("assets/images/fire_ring.png")

# Arrow
arrow_img = pygame.Surface((20,20))
arrow_img.fill('yellow')



        
        