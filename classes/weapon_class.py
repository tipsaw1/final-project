from settings import *
import classes.bullet_class as bullet

class Melee_weapon:
    # constructor
    def __init__(self, damage, range, cooldown):
        self.damage = damage
        self.range = range
        self.attack_cooldown = cooldown
        self.last_attacked = -cooldown
        self.pos = player_sprite.sprite.rect.center
        self.type = "Melee"
        
        
    def attack(self, pos):
        if pygame.time.get_ticks() - self.last_attacked >= self.attack_cooldown:
            for sprite in level_sprite.sprite.all_sprites:
                x_d = sprite.rect.x - player_sprite.sprite.rect.x
                y_d = sprite.rect.y - player_sprite.sprite.rect.y
                t_d = (x_d**2 + y_d**2)**0.5
                if t_d <= self.range and sprite.rect.clipline(player_sprite.sprite.rect.center, pos):
                    if sprite in level_sprite.sprite.enemy_sprites:
                        player_sprite.sprite.slashing = True
                        sprite.take_damage(self.damage)
                        self.last_attacked = pygame.time.get_ticks()
                        self.pos = pos
                    
                    
    
                

class Ranged_weapon:
    # constructor
    def __init__(self, damage, cooldown):
        self.damage = damage
        self.attack_cooldown = cooldown
        self.last_attacked = -cooldown
        self.type = "Ranged"
        
    def attack(self, pos):
        if pygame.time.get_ticks() - self.last_attacked >= self.attack_cooldown:
            bullet.Bullet(level_sprite.sprite.enemy_sprites, player_sprite.sprite.rect.center, pos, self.damage, 25, img.arrow_img)
            self.last_attacked = pygame.time.get_ticks()
        
        

        