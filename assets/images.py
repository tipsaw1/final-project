import pygame

# Player 1 image (temporarily a blue square)
player_img = pygame.Surface((50,50))
player_img.fill('blue')

player_hurt_img = pygame.Surface((50,50))
player_hurt_img.fill('white')

# Level 1 background (temporarily a tan square)
level_1_img = pygame.Surface((50,50))
level_1_img.fill("navajowhite2")

# Level 2 background (temporarily a gray square)
level_2_img = pygame.Surface((50,50))
level_2_img.fill("gray20")

# Level 3 backround :] made by yesung yay
level_3_img = pygame.Surface((50,50))
level_3_img.fill("navajowhite2")

# wall image (temporarily a green square)
wall_img_1 = pygame.Surface((50,50))
wall_img_1.fill("forestgreen")

# Enemy image (temporarily a red square)
enemy_img_1 = pygame.Surface((50, 50))
enemy_img_1.fill('red')

enemy_img_2 = pygame.Surface((50, 50))
enemy_img_2.fill('orange')

# Slash
slash_img = pygame.image.load("assets/slash.png")

# Arrow
arrow_img = pygame.Surface((20,20))
arrow_img.fill('yellow')
