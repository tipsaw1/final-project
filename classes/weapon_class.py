import settings, pygame, math
import classes.bullet_class as bullet

class Melee_weapon:
    # constructor
    def __init__(self, damage, range, cooldown, game):
        self.game = game
        self.damage = damage
        self.range = range
        self.attack_cooldown = cooldown
        self.last_attacked = -cooldown
        self.pos = self.game.player.rect.center
        self.type = "Melee"
        self.hit = []
        self.sound = settings.sound.sword_slash
        self.played = False
        
        
    def attack(self, pos):
        mouse_distance = pygame.math.Vector2(pos)
        mouse_distance -= self.game.player.rect.center
        mouse_angle = int(math.atan2(mouse_distance.y, mouse_distance.x)*180/math.pi)
        if not self.played:
            self.sound.play()
            self.played = True
            
        
        if mouse_angle < 0: mouse_angle += 360
        
        if pygame.time.get_ticks() - self.last_attacked <= 200:
            self.game.player.slashing = True
            self.pos = pos
            for sprite in self.game.current_level.enemy_sprites.sprites() + self.game.current_level.bullet_sprites.sprites():
                distance = pygame.math.Vector2(sprite.rect.center+pygame.math.Vector2(sprite.rect.width//2))
                distance -= self.game.player.rect.center
                total_distance_sq = distance.x**2 + distance.y**2
                target_angle = int(math.atan2(distance.y, distance.x)*180/math.pi)
                if target_angle <0: target_angle += 360
                if total_distance_sq <= self.range**2 and target_angle in range(mouse_angle-90, mouse_angle+90):
                    if total_distance_sq <= self.range**2:
                        print("in range")
                    if target_angle in range(mouse_angle-90, mouse_angle+90):
                        print("in angle")
                    if sprite in self.game.current_level.enemy_sprites and sprite not in self.hit:
                        sprite.take_damage(self.damage)
                        self.hit.append(sprite)
                    if sprite in self.game.current_level.bullet_sprites:
                        sprite.kill()
                        
        if pygame.time.get_ticks() - self.last_attacked >= self.attack_cooldown:
            self.last_attacked = pygame.time.get_ticks()
            self.hit = []
            self.played = False
        #mouse_angle*=math.pi/180
        #pygame.draw.line(pygame.display.get_surface(), "white",(settings.main_game.player.rect.center-settings.main_game.current_level.all_sprites.offset),(settings.main_game.player.rect.centerx+(90*math.cos(mouse_angle-90))-settings.main_game.current_level.all_sprites.offset.x, settings.main_game.player.rect.centery+(90*math.sin(mouse_angle-90))-settings.main_game.current_level.all_sprites.offset.y))
        #pygame.draw.line(pygame.display.get_surface(), "white",(settings.main_game.player.rect.center-settings.main_game.current_level.all_sprites.offset),(settings.main_game.player.rect.centerx+(90*math.cos(mouse_angle+90))-settings.main_game.current_level.all_sprites.offset.x, settings.main_game.player.rect.centery+(90*math.sin(mouse_angle+90))-settings.main_game.current_level.all_sprites.offset.y))
        #pygame.draw.line(pygame.display.get_surface(), "white", (settings.main_game.player.rect.center-settings.main_game.current_level.all_sprites.offset), (settings.main_game.player.rect.centerx, settings.main_game.player.rect.centery+self.range)-settings.main_game.current_level.all_sprites.offset)    
        #pygame.draw.line(pygame.display.get_surface(), "white",(settings.main_game.player.rect.center-settings.main_game.current_level.all_sprites.offset),(settings.main_game.player.rect.centerx+(self.range*math.cos(mouse_angle))-settings.main_game.current_level.all_sprites.offset.x, settings.main_game.player.rect.centery+(self.range*math.sin(mouse_angle))-settings.main_game.current_level.all_sprites.offset.y))
                    
    
                

class Ranged_weapon:
    # constructor
    def __init__(self, damage, cooldown, game):
        self.game = game
        self.damage = damage
        self.attack_cooldown = cooldown
        self.last_attacked = -cooldown
        self.type = "Ranged"
        self.sound = settings.sound.arrow_sound
        
    def attack(self, pos):
        if pygame.time.get_ticks() - self.last_attacked >= self.attack_cooldown:
            bullet.Bullet(self.game.current_level.enemy_sprites, self.game.player.rect.center, pos, self.damage, 25, settings.img.arrow_img, (self.game.TILESIZE//2, self.game.TILESIZE//4), self.game)
            self.last_attacked = pygame.time.get_ticks()
            self.sound.play()
            
        
        
class Magic_weapon:
    def __init__(self, damage, range, cooldown, game):
        self.game = game
        self.range = range
        self.damage = damage
        self.attack_cooldown = cooldown
        self.last_attacked = -cooldown
        self.type = "Magic"
        self.accuracy_modifier = 105
        
    def attack(self, pos):
        if pygame.time.get_ticks() - self.last_attacked >= self.attack_cooldown:
            bullet.Flame(self.game.current_level.enemy_sprites, self.game.player.rect.center, pos, self.damage, 25, settings.img.fireball_img, (self.game.TILESIZE//4,self.game.TILESIZE//4), self.range, self.game)
            self.last_attacked = pygame.time.get_ticks()
    
        

        