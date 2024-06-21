from settings import *
import classes.bullet_class as bullet

class Player(pygame.sprite.Sprite):
    # Equipped items are by default none
    equipped_weapon = None
    equipped_armor = None
    
    # Size is half a tile
    size = 3.2*TILESIZE//4
    
    # Animation frame is 0
    animation_frame = 0
    
    # Facing right
    facing = 1
    
    # Speed is 10
    speed = 10
    
    # Hp and max hp start at 200
    hp = 250
    max_hp = 250
    
    # hurt cooldown
    hurt_cooldown = 300
    last_hurt = -hurt_cooldown
    
    victory = False
    
    def __init__(self, level):
        super().__init__(player_sprite)
        # Animation [left, right]
        self.idle_animation = [img.archer_idle_animation_left, img.archer_idle_animation_right]
        self.walk_animation = [img.archer_walk_animation_left, img.archer_walk_animation_right]
        self.attack_animation = [img.archer_attack_animation_left, img.archer_attack_animation_right]
        self.hurt_animation = [img.archer_hurt_animation_left, img.archer_hurt_animation_right]
        self.dead_image = [img.archer_death_left, img.archer_death_right]
        
        self.current_animation = self.idle_animation
        
        # screen is stored
        self.level = level
        self.level.all_sprites.add(self)
        level_sprite.add(self.level)
        
        # Set image to the first frame of the current animation
        self.image = self.current_animation[self.facing][0]
        
        # Rect is positioned in the center of the screen
        self.rect = self.image.get_rect(center = self.level.rect.center)
        
        # dx and dy are 0
        self.dx, self.dy = 0, 0
        self.slashing = False
        self.player_class = "knight"
        self.health_percent = self.hp/self.max_hp
        self.frame_speed = 0.09
        
        
        
        
        
    def update(self):
        self.update_animation_frame(self.frame_speed)
        self.check_keys()
        self.move()
        self.check_borders()
        if self.equipped_weapon.type == "Melee":
            self.draw_slash(self.equipped_weapon.pos)
            
        self.health_percent = self.hp/self.max_hp
        
    def draw_slash(self, mousePos):
        surface = pygame.display.get_surface()
        if self.slashing:
            if pygame.time.get_ticks() - self.equipped_weapon.last_attacked <= 200:
                distance = pygame.math.Vector2(self.rect.center)
                distance = mousePos - distance
                
                angle = math.atan2(distance.y, distance.x)*-180/math.pi
                image = pygame.transform.scale(img.slash_img, (self.equipped_weapon.range+self.rect.width, self.equipped_weapon.range+self.rect.width))
                image = pygame.transform.rotate(image, angle)
                dx, dy = calculate_movement(distance.x, distance.y, self.rect.width/2)
                image_rect = image.get_rect(center = (self.rect.centerx + dx, self.rect.centery + dy))
                
                pos = pygame.math.Vector2(image_rect.x, image_rect.y)
                pos -= level_sprite.sprite.all_sprites.offset
                image_rect.topleft = pos
                surface.blit(image, image_rect)
            else:
                self.slashing = False

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
            #self.facing = 0
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.dx += 1
            #self.facing = 1
        if keys[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]:
            if self.equipped_weapon and self.current_animation != self.hurt_animation:
                self.equipped_weapon.attack([offset_mouseX, offset_mouseY])
                self.change_animation(self.attack_animation)
                
        
        if offset_mouseX < player_sprite.sprite.rect.centerx:
            self.facing = 0
        if offset_mouseX > player_sprite.sprite.rect.centerx:
            self.facing = 1
            
    def move(self):
        # Moves the player
        if self.dx != 0 or self.dy != 0:
            self.dx, self.dy = calculate_movement(self.dx, self.dy, self.speed)
            if self.current_animation != self.hurt_animation: # add "and self.current_animation != self.attack_animation" to attack when moving
                self.change_animation(self.walk_animation)
        else:
            if self.current_animation != self.hurt_animation and self.current_animation != self.attack_animation:
                self.change_animation(self.idle_animation)
                
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
            self.change_animation(self.hurt_animation, True)
            self.last_hurt = pygame.time.get_ticks()
            
    def change_animation(self, animation, reset_frames = False):
        self.current_animation = animation
        self.rect = self.image.get_rect(topleft = self.rect.topleft)
        if reset_frames:
            self.animation_frame = 0
            
    def update_animation_frame(self, amount):
        #if self.current_animation == self.attack_animation and self.player_class == "mage" and (pygame.key.get_pressed()[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]):
            #if self.animation_frame > 3:
                #self.animation_frame = 3
        self.image = self.current_animation[self.facing][int(self.animation_frame)]
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

        # Mage fireball hold
        self.animation_frame += amount
            
        # Reset frame
        if self.animation_frame >= len(self.current_animation[self.facing]):
            if self.current_animation == self.hurt_animation or self.current_animation == self.attack_animation:
                    self.change_animation(self.idle_animation)
            self.animation_frame = 0
            
        
        # Faster animations
        if self.current_animation != self.idle_animation:
            self.frame_speed = 0.15
        else:
            self.frame_speed = 0.1
            
            
