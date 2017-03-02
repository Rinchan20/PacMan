import os, sys
import pygame
from pygame.locals import *

from pacman import PacMan
from ghost import Ghost

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
        blinky = Ghost("blinky", "up", pacman, 50, 0)
        clyde = Ghost("clyde", "down", pacman, 100, 0)
        inky = Ghost("inky", "up", pacman, 150, 0)
        pinky = Ghost("pinky", "down", pacman, 200, 0)

        all_sprites_list.add(pacman)
        all_sprites_list.add(blinky)
        all_sprites_list.add(clyde)
        all_sprites_list.add(inky)
        all_sprites_list.add(pinky)
        
        while playing:
            for game_event in pygame.event.get():
                if game_event.type == pygame.QUIT:
                    playing = False

            #Game logic
            blinky.ghost_general_presentation()
            clyde.ghost_general_presentation()
            inky.ghost_general_presentation()
            pinky.ghost_general_presentation()
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