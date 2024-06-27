from settings import *
import classes.enemy_class as enemy
import classes.obstacle_class as obstacle
import classes.tile_class as tile
import classes.npc_class as npc

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
        
        #Player start position
        self.player_spawn = (SCREEN_W//2,SCREEN_H//2)
        
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
        # Store items
        self.item_sprites = OffsetGroup()
        # Stores the bullets in the room        
        self.bullet_sprites = OffsetGroup()
        # Store npcs
        self.npc_sprites = OffsetGroup()
        
        # Stores the adjacent levels
        self.adjacents = {
            "up": None,
            "down": None,
            "left": None,
            "right": None
        }
        self.load_map()
    
    def update(self):
        surface = pygame.display.get_surface()
        self.tile_sprites.draw(surface)
        self.item_sprites.update()
        self.item_sprites.draw(surface)
    
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
        
        # Creates enemies
        if letter == "?":
            npc.Npc(self, pos, TILESIZE, img.player_idle_animation, img.player_walk_animation, npc.Dialogue(["123", "abc", "do-re-mi"]))
        
        if letter == "!":
            enemy.Melee_enemy(self, pos, 15, 30, 7, TILESIZE)
        
        if letter == ">":
            enemy.Ranged_enemy(self, pos, 10, 20, 7, TILESIZE)
            
        if letter == "B":
            enemy.Boss_enemy(self, pos, 25, 500, 5, TILESIZE*2.5)
        
        if letter == "P":
            self.player_spawn = pos
            
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