from settings import *

class Player(pygame.sprite.Sprite):
    # Equipped items are by default none
    equipped_weapon = None
    equipped_armor = None
    # Size is half a tile
    size = TILESIZE//2
    # Image is scaled to size
    image = pygame.transform.scale(img.player_img, (size, size))
    # Rect is positioned in the center of the screen
    rect = image.get_rect(center = (SCREEN_W//2, SCREEN_H//2))
    # Speed is 10
    speed = 5
    # Hp and max hp start at 50
    hp = 50
    max_hp = 50
    
    def __init__(self, level):
        super().__init__(player_sprite, level.all_sprites)
        # screen is stored
        self.level = level
        # dx and dy are 0
        self.dx, self.dy = 0, 0
        
    def update(self):
        self.check_keys()
        self.move()
        
    def check_keys(self):
        # Store keys and change dx/dy
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.dy -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.dy += 1
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.dx -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.dx += 1
        
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
        collision = pygame.sprite.spritecollideany(self, self.level.all_sprites)

        # If you are colliding with something that isn't yourself
        if collision and collision != self:
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