import pygame
import sys

from const import *
from game import *

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self):

        self.game.show_bg(self.screen)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

main = Main()
main.mainloop()