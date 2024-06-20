from settings import *
import classes.bullet_class as bullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, level, image, pos, damage, hp, speed, size):
        super().__init__(level.enemy_sprites, level.all_sprites)
        self.level = level
        self.default_image = pygame.transform.scale(image, (size, size))
        self.hurt_img = pygame.transform.scale(img.enemy_hurt_img,(size, size))
        self.image = pygame.transform.scale(image, (size, size))
        self.rect = self.image.get_rect(topleft = pos)
        self.can_see_player = False
        self.attack_cooldown = 500
        self.idle = False
        self.dx, self.dy = 0,0
        self.last_attack = -self.attack_cooldown
        self.last_hit = -150
        self.direction_modifier = random.choice((1, -1))
        self.start_pos = pos
        self.last_turned = 0
        
        
        # Changes based on subclass
        self.damage = damage
        self.hp = hp
        self.speed = speed
        
    def update(self):
        if pygame.time.get_ticks() - self.last_hit >= 150:
            self.image = self.default_image
        self.check_line_of_sight()
        #self.draw_line_of_sight()
        self.move()
        self.check_borders()
        if self.hp <= 0:
            self.kill()
        
    def idle_movement(self):
        if self.idle == False:
            # Either move left right up or down
            #self.dx, self.dy = random.choice(((0, self.direction_modifier*self.speed), (self.direction_modifier*self.speed, 0)))
            self.dx, self.dy = self.direction_modifier*self.speed, 0
            self.idle = True
        if pygame.time.get_ticks() - self.last_turned >= 2000:
            self.dx *= -1
            self.dy *= -1
            self.last_turned = pygame.time.get_ticks()
        
    def check_line_of_sight(self):
        self.can_see_player = True
        for obstacle in self.level.obstacle_sprites:
            if obstacle.rect.clipline((self.rect.center, player_sprite.sprite.rect.center)):
                self.can_see_player = False
        
    def draw_line_of_sight(self):
        if self.can_see_player:
            pygame.draw.line(pygame.display.get_surface(), "red", self.rect.center-self.level.all_sprites.offset, player_sprite.sprite.rect.center-self.level.all_sprites.offset)
        else:
            pygame.draw.line(pygame.display.get_surface(), "white", self.rect.center-self.level.all_sprites.offset, player_sprite.sprite.rect.center-self.level.all_sprites.offset)
    
    def movement_pattern(self):
        if self.can_see_player:
            distance = pygame.math.Vector2(self.rect.center)
            distance = player_sprite.sprite.rect.center - distance
            self.dx, self.dy = calculate_movement(distance.x, distance.y, self.speed)
        else:
            self.idle_movement()
    
    def move(self):
        self.movement_pattern()
        self.rect.x += self.dx
        self.collide("x")
        self.rect.y += self.dy
        self.collide("y")
        
    def collide(self, direction):
        
        # Returns a sprite if you collide with it
        # Returns None if you aren't colliding with anything
        collisions = pygame.sprite.spritecollide(self, self.level.all_sprites, False)
        turn = False
        # If you are colliding with something that isn't yourself
        for collision in collisions:
            if collision != self and collision not in player_sprite and collision not in self.level.bullet_sprites:
                
                if direction == "x":
                    if self.dx > 0:
                        self.rect.right = collision.rect.left

                    if self.dx < 0:
                        self.rect.left = collision.rect.right

                if direction == "y":
                    if self.dy < 0:
                        self.rect.top = collision.rect.bottom

                    if self.dy > 0:
                        self.rect.bottom = collision.rect.top
                        
                turn = True
        if turn:
            self.direction_modifier *= -1
            self.idle = False

    def check_borders(self):
        if self.rect.left < self.level.rect.left:
            self.rect.left = self.level.rect.left
            
        # If you go past the right side of the screen and there is
        # another screen to the right, you go to the screen to the right
        if self.rect.right > self.level.rect.right:
            self.rect.right = self.level.rect.right
        
        # If you go past the top side of the screen and there is
        # another screen above, you go to the screen above
        if self.rect.top < self.level.rect.top:
            self.rect.top = self.level.rect.top
            
        # If you go past the bottom side of the screen and there is
        # another screen below, you go to the screen below
        if self.rect.bottom > self.level.rect.bottom:
            self.rect.bottom = self.level.rect.bottom
            
    
    def damage_player(self):
        player_sprite.sprite.take_damage(self.damage)
    # Movement pattern will be based on subclasses
            
    def in_attack_range(self):
        x_d = player_sprite.sprite.rect.centerx - self.rect.centerx
        y_d = player_sprite.sprite.rect.centery - self.rect.centery
        t_d = (x_d**2 + y_d**2)**0.5
        if t_d <= self.range:
            return True
        else:
            return False
        
    def take_damage(self, damage):
        self.hp -= damage
        self.image = self.hurt_img
        self.last_hit = pygame.time.get_ticks()
    
    
class Melee_enemy(Enemy):
    def __init__(self, level, image, pos, damage, hp, speed, size):
        super().__init__(level, image, pos, damage, hp, speed, size)
        self.range = 100
        
    def draw_slash(self, surface):
        if pygame.time.get_ticks() - self.last_attack >= 200:
            distance = pygame.math.Vector2(self.rect.center)
            distance = player_sprite.sprite.rect.center - distance
            angle = math.atan2(distance.y, distance.x)
            angle *= -180/math.pi
            image = pygame.transform.scale(img.slash_img, (self.rect.width*3, self.rect.width*3))
            image = pygame.transform.rotate(image, angle)
            dx, dy = calculate_movement(distance.x, distance.y, self.rect.width/2)
            image_rect = image.get_rect(center = (self.rect.centerx + dx, self.rect.centery + dy))
            pos = pygame.math.Vector2(image_rect.x, image_rect.y)
            pos -= self.level.all_sprites.offset
            image_rect.topleft = pos
            if self.in_attack_range():
                surface.blit(image, image_rect)
                self.damage_player()
        if pygame.time.get_ticks() - self.last_attack >= self.attack_cooldown:
            self.last_attack = pygame.time.get_ticks()
            
    def movement_pattern(self):
        distance = pygame.math.Vector2(self.rect.center)
        distance = player_sprite.sprite.rect.center - distance
        total_distance_sq = distance.x**2 + distance.y**2
        angle = math.atan2(distance.y, distance.x)
        if self.can_see_player:
            self.idle = False
            if total_distance_sq > (self.range-20)**2:
                self.dx, self.dy = calculate_movement(distance.x, distance.y, self.speed)
            else:
                self.dx, self.dy = 0,0
        else:   
            self.idle_movement()
            
            
    def update(self):
        super().update()
        self.draw_slash(pygame.display.get_surface())

class Ranged_enemy(Enemy):
    def __init__(self, level, image, pos, damage, hp, speed,size):
        super().__init__(level, image, pos, damage, hp, speed,size)
        self.evade_distance = SCREEN_H//2
        
    def shoot(self):
        if self.can_see_player:
            if pygame.time.get_ticks() - self.last_attack >= self.attack_cooldown:
                bullet.Bullet(player_sprite, self.rect.center, player_sprite.sprite.rect.center, self.damage, 10, img.arrow_img, TILESIZE//4)
                self.last_attack = pygame.time.get_ticks()
            
    def update(self):
        super().update()
        self.shoot()
        
    def movement_pattern(self):
        distance = pygame.math.Vector2(self.rect.center)
        distance = player_sprite.sprite.rect.center - distance
        total_distance_sq = distance.x**2 + distance.y**2
        angle = math.atan2(distance.y, distance.x)
        if self.can_see_player:
            self.idle = False
            if total_distance_sq < self.evade_distance**2:
                self.dx, self.dy = calculate_movement(distance.x, distance.y, -self.speed)
            elif total_distance_sq > (self.evade_distance+50)**2:
                self.dx, self.dy = calculate_movement(distance.x, distance.y, self.speed)
            else:
                self.dx = self.direction_modifier*(total_distance_sq**0.5)*(math.cos(angle+math.pi/360)-math.cos(angle))
                self.dy = self.direction_modifier*(total_distance_sq**0.5)*(math.sin(angle+math.pi/360)-math.sin(angle))
        
        else:
            self.idle_movement()
        
class Boss_enemy(Enemy):
    def __init__(self, level, image, pos, damage, hp, speed,size):
        super().__init__(level, image, pos, damage, hp, speed,size)
        # Attacks
        self.default_attack_cooldown = self.attack_cooldown
        self.far_attack_range = 300
        
        # Wave attacks
        self.wave_attacking = False
        self.wave_attack_update_rate = 50
        self.last_wave_attack_update = 0
        self.wave_img = pygame.transform.scale(img.wave_attack_img, (self.rect.width, self.rect.width))
        self.wave_rect = self.wave_img.get_rect()
        
        # Dash
        self.dash_timer = 1500
        self.last_dashed = 0
        self.dashing = False
        
        
    def update(self):
        super().update()
        #self.rect.center = self.level.rect.center
        self.attack_cycle()
        
        
    def idle_movement(self):
        self.dx = 0
        self.dy = 0
        
    def attack_cycle(self):
        if pygame.time.get_ticks() - self.last_attack >= self.attack_cooldown:
            distance = pygame.math.Vector2(player_sprite.sprite.rect.center)
            distance -= self.rect.center
            total_distance_sq = distance.x**2 + distance.y**2
            if total_distance_sq > self.far_attack_range**2:
                self.far_attack()
            else:
                self.mid_attack()
            self.last_attack = pygame.time.get_ticks()
                
        
        if self.wave_attacking:
            if pygame.time.get_ticks() - self.last_wave_attack_update >= self.wave_attack_update_rate:
                self.update_wave_attack()
            self.draw_wave_attack()
            
                
    def far_attack(self):
        self.attack_cooldown = 100
        bullet.Bullet(player_sprite, self.rect.center, player_sprite.sprite.rect.center, self.damage, 20, img.arrow_img, TILESIZE//4)
        
    def close_attack(self):
        self.attack_cooldown = self.default_attack_cooldown
        if self.in_attack_range():
            self.damage_player()
            
    def mid_attack(self):
        self.attack_cooldown = 100
        self.wave_attacking = True
        
    def update_wave_attack(self):
        self.wave_img = pygame.transform.scale_by(self.wave_img, 1.1)
        self.wave_rect = self.wave_img.get_rect()
        self.wave_rect.center = self.rect.center
        self.last_wave_attack_update = pygame.time.get_ticks()
        if self.wave_rect.width >= SCREEN_H:
            self.end_wave_attack()
            
    def end_wave_attack(self):
            self.wave_attacking = False
            self.wave_img = pygame.transform.scale(img.wave_attack_img, (self.rect.width, self.rect.height))
            self.wave_rect = self.wave_img.get_rect()
            
    def draw_wave_attack(self):
        self.wave_rect.center = self.rect.center
        surface = pygame.display.get_surface()
        surface.blit(self.wave_img, self.wave_rect.topleft-level_sprite.sprite.all_sprites.offset)
        distance = pygame.math.Vector2(player_sprite.sprite.rect.center)
        distance -= self.rect.center
        total_distance_sq = distance.x**2 + distance.y**2
        radius = self.wave_rect.width//2
        radius *= 4/5
        pygame.draw.circle(pygame.display.get_surface(), "white",self.wave_rect.center - level_sprite.sprite.all_sprites.offset, radius, 2)
        
        #pygame.draw.circle(pygame.display.get_surface(), "white",self.wave_rect.center - level_sprite.sprite.all_sprites.offset, radius)
        if total_distance_sq < radius**2:
                self.damage_player()
    
    def movement_pattern(self):
        distance = pygame.math.Vector2(self.rect.center)
        distance = player_sprite.sprite.rect.center - distance
        if not self.dashing:
            self.dx, self.dy = calculate_movement(distance.x, distance.y, self.speed)
        self.dash()
        
            
    def dash(self):
        distance = pygame.math.Vector2(self.rect.center)
        distance = player_sprite.sprite.rect.center - distance
        elapsed_time = pygame.time.get_ticks() - self.last_dashed
        if elapsed_time >= self.dash_timer:
            if not self.dashing:
                self.dx, self.dy = 0,0
            self.end_wave_attack()
            
        if elapsed_time >= self.dash_timer+500:
            if not self.dashing:
                self.dx, self.dy = calculate_movement(distance.x, distance.y, 5*self.speed)
                self.dashing = True
        
        if elapsed_time >= self.dash_timer+700:
            self.dx, self.dy = 0,0
            self.dashing = False
            
        if elapsed_time >= self.dash_timer+1000:
            self.last_dashed = pygame.time.get_ticks()
            
        
    
    
        
        
# Dungeon Enemies
class Goblin(Melee_enemy):
    def __init__(self, level, image, pos):
        super().__init__(level, image, pos, 10, 8, 8)


class Troll(Melee_enemy):
    def __init__(self, level, image, pos):
        super().__init__(self, level, image, pos, 50, 20, 5)
        
# Kings enemies
class Kings_knight(Melee_enemy):
    def __init__(self, level, image, pos):
        super().__init__(self, level, image, pos, 80, 25, 7)
        self.hp = 80
        self.damage = 25
class Kings_archer(Ranged_enemy):
    def __init__(self, level, image, pos):
        super().__init__(self, level, image, pos, 50, 35, 7)
        self.hp = 50
        self.damage = 35
