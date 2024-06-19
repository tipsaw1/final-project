from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, target_group, start_pos, target_pos, damage, speed, image):
        super().__init__(level_sprite.sprite.all_sprites, level_sprite.sprite.bullet_sprites)
        self.image = image
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
                elif collision in self.target_group:
                    collision.take_damage(self.damage)
                    self.kill()