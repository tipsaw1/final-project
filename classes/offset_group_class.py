import pygame
# This is a new subclass of the pygame.Group class
# This allows us to create an offset for it to be placed,
# letting us move the screen and everything on it

class OffsetGroup(pygame.sprite.Group):
    def __init__(self, game, *sprites):
        super().__init__(*sprites)
        # Stores an x and y value (by default is (0,0))
        self.offset = pygame.math.Vector2()
        self.game = game

    # Replaces normal group draw function
    def draw(self, surface):
        for sprite in self.sprites():
            #X offset is set to the player's x position - half the screen
            #Y offset is set to the player's y position - half the screen
            self.offset.x = self.game.player.rect.x-self.game.SCREEN_W//2
            self.offset.y = self.game.player.rect.y-self.game.SCREEN_H//2

            # Keep screen within borders
            # If the left side of the screen is at 0, it cannot decrease
            if self.offset.x <= 0:
                self.offset.x = 0
            # If the left side of the screen is at the right side of the map
            # minus the width of the screen, it cannot increase
            # (if the right side of the screen is at the right side of the map)
            if self.offset.x >= self.game.player.level.rect.right-self.game.SCREEN_W:
                self.offset.x = self.game.player.level.rect.right-self.game.SCREEN_W
            # If the top of the screen is at the top of the map, the y offset
            # cannot decrease
            if self.offset.y <= 0:
                self.offset.y = 0

            # If the top of the screen is at the bottom of the map minus the
            # height of the screen, the y offset cannot increase
            # (if the bottom of the screen is at the bottom of the map)
            if self.offset.y >= self.game.player.level.rect.bottom-self.game.SCREEN_H:
                self.offset.y = self.game.player.level.rect.bottom-self.game.SCREEN_H



            '''
            Offset is set to the players position - half the screen, meaning that
            As the player moves left, the offset decreases .

            ex: player position of 0 = offset value of -half the screen

            The sprites position is then subtracted by the offset, meaning the farther
            left the player goes, the farther right the sprite is drawn and vice versa

            The player is also affected by this, meaning that it cancels out their
            position and places them in the center of the screen

            ex: player position of 0 - offset value of -half the screen
             = player position of half the screen (2 negatives cancel out)

             The Rects remain in the same position relative to each other,
             allowing you to use collisions and other pygame Rect features
            '''
            if sprite != self.game.player:
                surface.blit(sprite.image, sprite.rect.topleft-self.offset)

        # Ensures player sprite is always on top
        if self.game.player in self.sprites():
            surface.blit(self.game.player.image, self.game.player.rect.topleft - self.offset)