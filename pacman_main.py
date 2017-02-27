import os, sys
import pygame
from pygame.locals import *

from pacman import PacMan

class PacManMain():

    def __init__(self, title, width=700, height=500):
        #Initialize the game engine
        pygame.init()

        #Setup game window
        self.width = width
        self.height = height
        self.game_title = title

        #Create the screen
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.game_title)


    def main_game_loop(self):
        #Game logic setup
        playing = True
        game_clock = pygame.time.Clock()
        all_sprites_list = pygame.sprite.Group()

        #Create all sprites and put them into the sprites list
        pacman = PacMan()

        all_sprites_list.add(pacman)

        
        while playing:
            for game_event in pygame.event.get():
                if game_event.type == pygame.QUIT:
                    playing = False

            #Game logic
            all_sprites_list.update()

            #Draw all the sprites at once
            all_sprites_list.draw(self.screen)

            #Refresh the screen
            pygame.display.flip()

            #Set the number of frames per second e.g. 60
            game_clock.tick(60)

        pygame.quit()


#Start the game
if __name__ == "__main__":
    main_window = PacManMain("PacMan")
    main_window.main_game_loop()