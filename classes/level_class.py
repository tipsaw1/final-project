from settings import *
import classes.enemy_class as enemy
import classes.obstacle_class as obstacle
# Different rooms/screens
print(SCREEN_W)

class Level:
    
    def __init__(self, map_grid, image):
        # Background image
        self.image = pygame.transform.scale(image, (SCREEN_W,SCREEN_H))
        # Stores all the enemies in this room
        self.enemy_sprites = pygame.sprite.Group()
        # Stores all the walls/items with collisions
        self.obstacle_sprites = pygame.sprite.Group()
        # Stores the map grid that will be used to draw the screen
        self.map = map_grid
        # x and y offset
        self.x = 0
        self.y = 0
        
        #Loads the map
        self.load_map()
    
    # Draws the enemies and obstacles
    def draw(self, surface):
        surface.blit(self.image, (self.x,self.y))
        self.enemy_sprites.draw(surface)
        self.obstacle_sprites.draw(surface)
        
    def update(self):
        # Updates the obstacles and enemies
        self.enemy_sprites.update()
        self.obstacle_sprites.update()
        
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
            
        