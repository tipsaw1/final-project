from settings import *
import classes.bullet_class as bullet
print('imported enemy class')

class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, level, image, pos, damage, hp, speed):
        super().__init__(level.enemy_sprites, level.all_sprites)
        self.name = name
        self.level = level
        self.default_image = pygame.transform.scale(image, (TILESIZE, TILESIZE))
        self.hurt_img = pygame.transform.scale(img.player_hurt_img,(TILESIZE, TILESIZE))
        self.image = pygame.transform.scale(image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft = pos)
        self.can_see_player = False
        self.dx, self.dy = 0,0
        self.attack_cooldown = 500
        self.last_attack = -self.attack_cooldown
        self.last_hit = -150
        
        
        
        # Changes based on subclass
        self.damage = damage
        self.hp = hp
        self.speed = speed
        
        
        
    def update(self):
        if pygame.time.get_ticks() - self.last_hit >= 150:
            self.image = self.default_image
        self.check_line_of_sight()
        self.draw_line_of_sight()
        self.move()
        if self.hp <= 0:
            self.kill()
        
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
            self.dx, self.dy = 0,0
    
    def move(self):
        self.movement_pattern()
        self.rect.x += self.dx
        self.collide("x")
        self.rect.y += self.dy
        self.collide("y")
        
    def collide(self, direction):
        
        # Returns a sprite if you collide with it
        # Returns None if you aren't colliding with anything
        collisions = pygame.sprite.spritecollide(self, self.level.obstacle_sprites, False)
        # If you are colliding with something that isn't yourself
        for collision in collisions:
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

        
    def damage_player(self):
        player_sprite.sprite.take_damage(self.damage)
    # Movement pattern will be based on subclasses
    
    
            
    def in_range(self):
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
    def __init__(self, name, level, image, pos, damage, hp, speed):
        super().__init__(name, level, image, pos, damage, hp, speed)
        self.range = 100
        
    def draw_slash(self, surface):
        if pygame.time.get_ticks() - self.last_attack >= 200:
            distance = pygame.math.Vector2(self.rect.center)
            distance = player_sprite.sprite.rect.center - distance
            angle = math.atan2(distance.y, distance.x)
            angle *= -180/math.pi
            image = pygame.transform.rotate(img.slash_img, angle)
            dx, dy = calculate_movement(distance.x, distance.y, self.rect.width/2)
            image_rect = image.get_rect(center = (self.rect.centerx + dx, self.rect.centery + dy))
            pos = pygame.math.Vector2(image_rect.x, image_rect.y)
            pos -= self.level.all_sprites.offset
            image_rect.topleft = pos
            if self.in_range():
                surface.blit(image, image_rect)
                self.damage_player()
                #print(player_sprite.sprite.hp)
        if pygame.time.get_ticks() - self.last_attack >= self.attack_cooldown:
            self.last_attack = pygame.time.get_ticks()
            
    def movement_pattern(self):
        if self.can_see_player:
            distance = pygame.math.Vector2(self.rect.center)
            distance = player_sprite.sprite.rect.center - distance
            total_distance_sq = distance.x**2 + distance.y**2
            if total_distance_sq > (self.range-20)**2:
                self.dx, self.dy = calculate_movement(distance.x, distance.y, self.speed)
            else:
                self.dx, self.dy = 0, 0
        else:
            self.dx, self.dy = 0,0
            
    def update(self):
        super().update()
        self.draw_slash(pygame.display.get_surface())

class Ranged_enemy(Enemy):
    def __init__(self, name, level, image, pos, damage, hp, speed):
        super().__init__(name, level, image, pos, damage, hp, speed)
        self.evade_distance = SCREEN_H//2
        
    def shoot(self):
        if self.can_see_player:
            if pygame.time.get_ticks() - self.last_attack >= self.attack_cooldown:
                bullet.Bullet(player_sprite, self.rect.center, player_sprite.sprite.rect.center, self.damage, 10, img.arrow_img)
                self.last_attack = pygame.time.get_ticks()
            
    def update(self):
        super().update()
        self.shoot()
        
    def movement_pattern(self):
        if self.can_see_player:
            distance = pygame.math.Vector2(self.rect.center)
            distance = player_sprite.sprite.rect.center - distance
            total_distance_sq = distance.x**2 + distance.y**2
            if total_distance_sq < self.evade_distance**2:
                self.dx, self.dy = calculate_movement(distance.x, distance.y, -self.speed)
            else:
                self.dx, self.dy = 0, 0
# Dungeon Enemies
class Goblin(Enemy):
    def __init__(self, level, image, pos):
        super().__init__("Goblin", level, image, pos, 10, 8, 8)


class Troll(Enemy):
    def __init__(self, level, image, pos):
        super().__init__(self, "Troll", level, image, pos, 50, 20, 5)
        
# Kings enemies
class Kings_knight(Enemy):
    def __init__(self, level, image, pos):
        super().__init__(self, "Knight", level, image, pos, 80, 25, 7)
        self.hp = 80
        self.damage = 25
class Kings_archer(Enemy):
    def __init__(self, level, image, pos):
        super().__init__(self, "Archer", level, image, pos, 50, 35, 7)
        self.hp = 50
        self.damage = 35
