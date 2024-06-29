import settings
import pygame, random
import classes.offset_group_class
import classes.enemy_class as enemy
import classes.obstacle_class as obstacle
import classes.tile_class as tile
#import classes.npc_class as npc

# Different rooms/screens
class Level(pygame.sprite.Sprite):    
    def __init__(self, map_grid, game):
        super().__init__()
        
        # game
        self.game = game
        # Background image
        self.tile_images = (settings.img.tile_1, settings.img.tile_2, settings.img.tile_3)
        # Stores the map grid that will be used to draw the screen
        self.map = map_grid
        # Sets up rect and image and etc
        height = len(self.map)*self.game.TILESIZE
        width = len(self.map[0])*self.game.TILESIZE
        self.rect = pygame.Rect(0,0, width, height)
        
        #Player start position
        self.player_spawn = (self.game.SCREEN_W//2,self.game.SCREEN_H//2)
        
        # Stores all sprites in this room (including the player)
        self.all_sprites = classes.offset_group_class.OffsetGroup(self.game)
        # Stores all the enemies in this room
        self.enemy_sprites = classes.offset_group_class.OffsetGroup(self.game)
        # Stores all the walls/items with collisions
        self.obstacle_sprites = classes.offset_group_class.OffsetGroup(self.game)
        # Stores the floor tiles in the room
        self.tile_sprites = classes.offset_group_class.OffsetGroup(self.game)
        # Store items
        self.item_sprites = classes.offset_group_class.OffsetGroup(self.game)
        # Stores the bullets in the room        
        self.bullet_sprites = classes.offset_group_class.OffsetGroup(self.game)
        # Store npcs
        self.npc_sprites = classes.offset_group_class.OffsetGroup(self.game)
        
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
                x_pos += self.game.TILESIZE
            y_pos += self.game.TILESIZE
            
    def reset_map(self):
        for enemy in self.enemy_sprites:
            enemy.rect.topleft = enemy.start_pos
        if self.game.player not in self.all_sprites:
            self.all_sprites.add(self.game.player)
            
            
                
    def map_key(self, letter, pos):
        # Creates wall obstacle
        if letter == "X":
            obstacle.Obstacle(self, settings.img.wall_img_1, pos)
        
        # Creates enemies
        #if letter == "?":
            #npc.Npc(self, pos, self.game.TILESIZE, settings.img.player_idle_animation, settings.img.player_walk_animation, npc.Dialogue(["123", "abc", "do-re-mi"]))
        
        if letter == "!":
            enemy.Melee_enemy(self, pos, 15, 30, 7, self.game.TILESIZE, settings.img.melee_skeleton_animations)
        
        if letter == ">":
            enemy.Ranged_enemy(self, pos, 10, 20, 7, self.game.TILESIZE, settings.img.archer_skeleton_animations)
            
        if letter == "B":
            enemy.Boss_enemy(self, pos, 25, 500, 5, self.game.TILESIZE*2.5, settings.img.archer_skeleton_animations)
        
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