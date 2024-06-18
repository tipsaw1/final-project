from settings import *
import classes.enemy_class as enemy
import classes.obstacle_class as obstacle

# Different rooms/screens
class Level(pygame.sprite.Sprite):
    def __init__(self, map_grid, image):
        super().__init__()
        # Background image
        # Width and height is the width/height of the map
        # Subtract 20 for smoothness while moving
        height = len(map_grid)*TILESIZE
        width = len(map_grid[0])*TILESIZE
        self.image = pygame.transform.scale(image, (width,height))
        print(width, height)
        self.rect = self.image.get_rect(topleft = (0,0))
        # Stores all sprites in this room (including the player)
        self.all_sprites = OffsetGroup()
        # Stores all the enemies in this room
        self.enemy_sprites = OffsetGroup()
        # Stores all the walls/items with collisions
        self.obstacle_sprites = OffsetGroup()
        # Stores the map grid that will be used to draw the screen
        self.map = map_grid
        
        #Loads the map
        self.load_map()
        
    def load_map(self):
        # Adds the enemies and obstacles into their group
        # y position = the y offset
        y_pos = 0
        for y in self.map:
            # x position = the level's x offset
            x_pos = 0
            for x in y:
                self.map_key(x, (x_pos, y_pos))
                x_pos += TILESIZE
            y_pos += TILESIZE
                
    def map_key(self, letter, pos):
        if letter == "X":
            obstacle.Obstacle(self, img.tree_img_1, pos)
            
        