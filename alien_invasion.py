import pygame
import sys
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets an behavior"""
    def __init__(self):
        pygame.init()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_length))
        self.bgcolor =(self.settings.bgcolor)
        pygame.display.set_caption("AlienInvasion")
        self.ship=Ship(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bgcolor)
            self.ship.blitme()
            pygame.display.flip()

if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()


