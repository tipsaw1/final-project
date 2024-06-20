from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, target_group, start_pos, target_pos, damage, speed, image, size):
        super().__init__(level_sprite.sprite.all_sprites, level_sprite.sprite.bullet_sprites)
        self.image = pygame.transform.scale(image, (size, size))
        self.rect = image.get_rect(center = start_pos)
        self.target_group = target_group
        self.damage = damage
        x_distance = target_pos[0] - start_pos[0]
        y_distance = target_pos[1] - start_pos[1]
        self.dx, self.dy = calculate_movement(x_distance, y_distance, speed)
        
    def update(self):
        self.move()
        self.check_collisions()
    
    def move(self):
        self.rect.move_ip(self.dx, self.dy)
        
    def check_collisions(self):
        collisions = pygame.sprite.spritecollide(self, level_sprite.sprite.all_sprites, False)
        
        for collision in collisions:
            if collision != self:
                if collision in level_sprite.sprite.obstacle_sprites:
                    self.kill()
                    break
                elif collision in self.target_group:
                    collision.take_damage(self.damage)
                    self.kill()
                    break
                
class Flame(Bullet):
    def __init__(self, target_group, start_pos, target_pos, damage, speed, image, size, range):
        super().__init__(target_group, start_pos, target_pos, damage, speed, image, size)
        self.range = range
        distance = pygame.math.Vector2(target_pos)
        distance -= self.rect.center
        angle = math.atan2(distance.y, distance.x)
        angle *= 180/math.pi
        angle = random.randrange(int(angle-50), int(angle+50))
        angle *= math.pi/180
        self.dx = speed*math.cos(angle)
        self.dy = speed*math.sin(angle)
        
    def update(self):
        super().update()
        distance = pygame.math.Vector2(self.rect.center)
        distance -= player_sprite.sprite.rect.center
        total_distance_sq = distance.x**2 + distance.y**2
        if abs(total_distance_sq) >= self.range**2:
            self.kill()
            
    def check_collisions(self):
        
        collisions = pygame.sprite.spritecollide(self, level_sprite.sprite.all_sprites, False)
        
        for collision in collisions:
            if collision != self:
                if collision in level_sprite.sprite.obstacle_sprites:
                    self.kill()
                    break
                elif collision in self.target_group:
                    collision.take_damage(self.damage)
                    break