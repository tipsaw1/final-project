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
    speed = 10
    # Hp and max hp start at 50
    hp = 50
    max_hp = 50
    
    def __init__(self, level):
        super().__init__(player_sprite)
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
        if keys[pygame.K_SPACE]:
            print(self.level.obstacle_sprites.sprites()[0].rect.center, self.rect.center)
            
    def move(self):
        # Move the screen in the opposite direction of the player
        if self.dx != 0 or self.dy != 0:
            self.dx, self.dy = calculate_movement(self.dx, self.dy, self.speed)
        self.level.x -= self.dx
        self.check_collisions("x")
        self.level.y -= self.dy
        self.check_collisions("y")
        
        # Reset dx and dy
        self.dx = 0
        self.dy = 0
        
    def check_collisions(self, direction):
        # Returns any sprite that the player collides with within the level's list of obstacles
        collide = pygame.sprite.spritecollideany(self, self.level.obstacle_sprites)
        # If you collided with anything:
        if collide:
            # Collisions for moving left and right
            if direction == "x":
                distance = 0
                # If moving right and colliding
                if self.dx > 0:
                    distance = collide.rect.left - self.rect.right
                    
                # If moving left and collliding
                if self.dx < 0:
                    distance = self.rect.left - collide.rect.right 
                    
                self.level.x += distance
            # Collisions for moving up and down
            if direction == "y":
                distance = 0
                # If moving up and colliding
                if self.dy < 0:
                    distance = self.rect.top - collide.rect.bottom 
                # If moving down and
                if self.dy > 0:
                    distance = collide.rect.top - self.rect.bottom
                self.level.y += distance