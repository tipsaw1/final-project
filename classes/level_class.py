from settings import *
import classes.enemy_class as enemy
import classes.obstacle_class as obstacle
import classes.tile_class as tile

# Different rooms/screens
class Level(pygame.sprite.Sprite):    
    def __init__(self, map_grid,):
        super().__init__()
        # Background image
        self.tile_images = (img.tile_1, img.tile_2, img.tile_3)
        # Stores the map grid that will be used to draw the screen
        self.map = map_grid
        # Sets up rect and image and etc
        height = len(self.map)*TILESIZE
        width = len(self.map[0])*TILESIZE
        self.rect = pygame.Rect(0,0, width, height)
        
        # Puts current level into the level sprite group
        # Level sprite is a GroupSingle()
        level_sprite.add(self)
        
        # Stores all sprites in this room (including the player)
        self.all_sprites = OffsetGroup()
        # Stores all the enemies in this room
        self.enemy_sprites = OffsetGroup()
        # Stores all the walls/items with collisions
        self.obstacle_sprites = OffsetGroup()
        # Stores the floor tiles in the room
        self.tile_sprites = OffsetGroup()
        
        # Stores the bullets in the room        
        self.bullet_sprites = OffsetGroup()
        # Stores the adjacent levels
        self.adjacents = {
            "up": None,
            "down": None,
            "left": None,
            "right": None
        }
        self.load_map()
    
        
    #Loads the map
    def load_map(self):
        
        # Adds the enemies and obstacles into their group
        # y position = the y offset
        y_pos = 0
        for y in self.map:
            # x position = the level's x offset
            x_pos = 0
            for x in y:
                tile.Tile(self, random.choice(self.tile_images), (x_pos, y_pos))
                self.map_key(x, (x_pos, y_pos))
                x_pos += TILESIZE
            y_pos += TILESIZE
            
    def reset_map(self):
        for enemy in self.enemy_sprites:
            enemy.rect.topleft = enemy.start_pos
        if player_sprite.sprite not in self.all_sprites:
            self.all_sprites.add(player_sprite.sprite)
            
            
                
    def map_key(self, letter, pos):
        # Creates wall obstacle
        if letter == "X":
            obstacle.Obstacle(self, img.wall_img_1, pos)
        
        # Creates default enemy (will probably change when we add subclasses)
        if letter == "!":
            enemy.Melee_enemy(self, img.enemy_img_1, pos, 5, 25, 7, TILESIZE//2)
        
        if letter == ">":
            enemy.Ranged_enemy(self, img.enemy_img_2, pos, 5, 20, 7, TILESIZE//2)
            
        if letter == "B":
            enemy.Boss_enemy(self, img.boss_enemy_img, pos, 20, 250, 5, TILESIZE*2.5)
            
    # Set adjacent rooms
    def set_adjacents(self, up = None, down = None, left = None, right = None):
        if not up:
            up = self.adjacents["up"]
        if not down:
            down = self.adjacents["down"]
        if not left:
            left = self.adjacents["left"]
        if not right:
            right = self.adjacents["right"]
        self.adjacents["up"] = up
        self.adjacents["down"] = down
        self.adjacents["left"] = left
        self.adjacents["right"] = right