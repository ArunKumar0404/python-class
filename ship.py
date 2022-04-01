import pygame
import sys

class Ship:
    """A class to manage ship"""
    def __init__(self,ai_game):
        """initiate the ship and set it bottom position of the screen"""
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        #load the ship
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its location"""
        self.screen.blit(self.image,self.rect)






