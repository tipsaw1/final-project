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
        self.hit = []
        self.sound = sound.sword_slash
        self.played = False
        
        
    def attack(self, pos):
        mouse_distance = pygame.math.Vector2(pos)
        mouse_distance -= player_sprite.sprite.rect.center
        mouse_angle = int(math.atan2(mouse_distance.y, mouse_distance.x)*180/math.pi)
        if not self.played:
            self.sound.play()
            self.played = True
            
        
        if mouse_angle < 0: mouse_angle += 360
        
        if pygame.time.get_ticks() - self.last_attacked <= 200:
            player_sprite.sprite.slashing = True
            self.pos = pos
            for sprite in level_sprite.sprite.enemy_sprites.sprites() + level_sprite.sprite.bullet_sprites.sprites():
                distance = pygame.math.Vector2(sprite.rect.center+pygame.math.Vector2(sprite.rect.width//2))
                distance -= player_sprite.sprite.rect.center
                total_distance_sq = distance.x**2 + distance.y**2
                target_angle = int(math.atan2(distance.y, distance.x)*180/math.pi)
                if target_angle <0: target_angle += 360
                if total_distance_sq <= self.range**2 and target_angle in range(mouse_angle-90, mouse_angle+90):
                    if total_distance_sq <= self.range**2:
                        print("in range")
                    if target_angle in range(mouse_angle-90, mouse_angle+90):
                        print("in angle")
                    if sprite in level_sprite.sprite.enemy_sprites and sprite not in self.hit:
                        sprite.take_damage(self.damage)
                        self.hit.append(sprite)
                    if sprite in level_sprite.sprite.bullet_sprites:
                        sprite.kill()
                        
        if pygame.time.get_ticks() - self.last_attacked >= self.attack_cooldown:
            self.last_attacked = pygame.time.get_ticks()
            self.hit = []
            self.played = False
        #mouse_angle*=math.pi/180
        #pygame.draw.line(pygame.display.get_surface(), "white",(player_sprite.sprite.rect.center-level_sprite.sprite.all_sprites.offset),(player_sprite.sprite.rect.centerx+(90*math.cos(mouse_angle-90))-level_sprite.sprite.all_sprites.offset.x, player_sprite.sprite.rect.centery+(90*math.sin(mouse_angle-90))-level_sprite.sprite.all_sprites.offset.y))
        #pygame.draw.line(pygame.display.get_surface(), "white",(player_sprite.sprite.rect.center-level_sprite.sprite.all_sprites.offset),(player_sprite.sprite.rect.centerx+(90*math.cos(mouse_angle+90))-level_sprite.sprite.all_sprites.offset.x, player_sprite.sprite.rect.centery+(90*math.sin(mouse_angle+90))-level_sprite.sprite.all_sprites.offset.y))
        #pygame.draw.line(pygame.display.get_surface(), "white", (player_sprite.sprite.rect.center-level_sprite.sprite.all_sprites.offset), (player_sprite.sprite.rect.centerx, player_sprite.sprite.rect.centery+self.range)-level_sprite.sprite.all_sprites.offset)    
        #pygame.draw.line(pygame.display.get_surface(), "white",(player_sprite.sprite.rect.center-level_sprite.sprite.all_sprites.offset),(player_sprite.sprite.rect.centerx+(self.range*math.cos(mouse_angle))-level_sprite.sprite.all_sprites.offset.x, player_sprite.sprite.rect.centery+(self.range*math.sin(mouse_angle))-level_sprite.sprite.all_sprites.offset.y))
                    
    
                

class Ranged_weapon:
    # constructor
    def __init__(self, damage, cooldown):
        self.damage = damage
        self.attack_cooldown = cooldown
        self.last_attacked = -cooldown
        self.type = "Ranged"
        self.sound = sound.arrow_sound
        
    def attack(self, pos):
        if pygame.time.get_ticks() - self.last_attacked >= self.attack_cooldown:
            bullet.Bullet(level_sprite.sprite.enemy_sprites, player_sprite.sprite.rect.center, pos, self.damage, 25, img.arrow_img, (TILESIZE//2, TILESIZE//4))
            self.last_attacked = pygame.time.get_ticks()
            self.sound.play()
            
        
        
class Magic_weapon:
    def __init__(self, damage, range, cooldown):
        self.range = range
        self.damage = damage
        self.attack_cooldown = cooldown
        self.last_attacked = -cooldown
        self.type = "Magic"
        self.accuracy_modifier = 105
        self.sound = None
        
    def attack(self, pos):
        if pygame.time.get_ticks() - self.last_attacked >= self.attack_cooldown:
            bullet.Flame(level_sprite.sprite.enemy_sprites, player_sprite.sprite.rect.center, pos, self.damage, 25, img.fireball_img, (TILESIZE//4,TILESIZE//4), self.range)
            self.last_attacked = pygame.time.get_ticks()
    
        

        