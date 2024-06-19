from settings import *
import classes.bullet_class as bullet

class Player(pygame.sprite.Sprite):
    # Equipped items are by default none
    equipped_weapon = None
    equipped_armor = None
    # Size is half a tile
    size = 3*TILESIZE//4
    # Image is scaled to size
    default_image = pygame.transform.scale(img.player_img, (size, size))
    hurt_image = pygame.transform.scale(img.player_hurt_img, (size,size))
    # Speed is 10
    speed = 10
    # Hp and max hp start at 50
    hp = 50
    max_hp = 50
    
    hurt_cooldown = 300
    last_hurt = -hurt_cooldown
    
    def __init__(self, level):
        super().__init__(player_sprite)
        self.image = self.default_image
        # Rect is positioned in the center of the screen
        self.rect = self.image.get_rect(center = (SCREEN_W//2, SCREEN_H//2))
        # screen is stored
        self.level = level
        self.level.all_sprites.add(self)
        # dx and dy are 0
        self.dx, self.dy = 0, 0
        
        
    def update(self):
        if pygame.time.get_ticks() - self.last_hurt >= 150:
            self.image = self.default_image
        self.check_keys()
        self.move()
        self.check_borders()
        
    def check_keys(self):
        # Store keys and change dx/dy
        keys = pygame.key.get_pressed()
        mouseX, mouseY = pygame.mouse.get_pos()
        offset_mouseX = mouseX+level_sprite.sprite.all_sprites.offset.x
        offset_mouseY = mouseY+level_sprite.sprite.all_sprites.offset.y
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.dy -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.dy += 1
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.dx -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.dx += 1
        if keys[pygame.K_SPACE]:
            if self.equipped_weapon:
                self.equipped_weapon.attack((offset_mouseX, offset_mouseY))
        
    def move(self):
        # Moves the player
        if self.dx != 0 or self.dy != 0:
            self.dx, self.dy = calculate_movement(self.dx, self.dy, self.speed)
            
        self.rect.x += self.dx
        self.check_collisions("x")
        self.rect.y += self.dy
        self.check_collisions("y")
        
        # Reset dx and dy
        self.dx = 0
        self.dy = 0
    
    def check_collisions(self, direction):
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
                        
            #if collision in self.level.enemy_sprites:
                #collision.damage_player()
                #print(self.hp)
                    
    def check_borders(self):
        # If you go past the left side of the screen and there is
        # another screen to the left, you go to the screen to the left
        if self.rect.centerx < self.level.rect.left and self.level.adjacents["left"]:
            self.level = self.level.adjacents["left"]
            level_sprite.add(self.level)
            self.level.reset_map()
            self.rect.right = self.level.rect.right
            
        # If you go past the right side of the screen and there is
        # another screen to the right, you go to the screen to the right
        if self.rect.centerx > self.level.rect.right and self.level.adjacents["right"]:
            self.level = self.level.adjacents["right"]
            level_sprite.add(self.level)
            self.level.reset_map()
            self.rect.left = self.level.rect.left
        
        # If you go past the top side of the screen and there is
        # another screen above, you go to the screen above
        if self.rect.centery < self.level.rect.top and self.level.adjacents["up"]:
            self.level = self.level.adjacents["up"]
            level_sprite.add(self.level)
            self.level.reset_map()
            self.rect.bottom = self.level.rect.bottom
            
        # If you go past the bottom side of the screen and there is
        # another screen below, you go to the screen below
        if self.rect.centery > self.level.rect.bottom and self.level.adjacents["down"]:
            self.level = self.level.adjacents["down"]
            level_sprite.add(self.level)
            self.level.reset_map()
            self.rect.top = self.level.rect.top
            
    
    def take_damage(self, damage):
        # Will probably change to reflect armor/defense
        if pygame.time.get_ticks() - self.last_hurt >= self.hurt_cooldown:
            self.hp -= damage
            self.image = self.hurt_image
            self.last_hurt = pygame.time.get_ticks()
            
    