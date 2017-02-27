import pygame

class PacMan(pygame.sprite.Sprite):
    """The character PacMan based on the classic arcade game"""

    def __init__(self):
        #Call the parent class [Sprite] constructor
        super().__init__()

        #Load the starting picture of the character
        self.image = pygame.image.load("data\images\pacman_right_open.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 30))

        #Get the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

        self.amount_of_pellets_eaten = 0
        self.additional_lives = 2;

        #To help with animation
        self.mouth_status = "open"
        self.direction = "right"


