import pygame

class Ghost(pygame.sprite.Sprite):
    """The ghost that chases Pacman"""
    
    def __init__(self, name, direction, target, position_x, position_y):
        #Call the parent class [Sprite] constructor
        super().__init__()
        self.name = name
        self.direction = direction

        #Load the starting picture of the character
        self.image = pygame.image.load("data\images\\base_ghost.png").convert_alpha() 
        self.image = pygame.transform.scale(self.image, (50, 30))

        #Get the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

        #Set the ghost's (x,y) position/location
        self.rect.x = position_x
        self.rect.y = position_y

        #Set the ghost's state; it switches between edibile, inedible, and eaten
        self.state = "inedible"

        #Set the ghost's target e.g. Pacman
        self.target = target

    def change_ghost_state(self, state):
        """Changes the ghost's state which is used to determine presentation"""
        self.state = state

    def change_direction(self, direction):
        """Changes the status of the ghost's direction"""
        self.direction = direction

    def ghost_general_presentation(self):
        """Handles the presentation (the picture model/image) of the ghosts"""
        if(self.state == "edible"):
            #Show as the scared blue ghost
            self.image = pygame.image.load("data\images\\edible_ghost.png").convert_alpha() 

        elif(self.state == "eaten"):
            #Show as the invisible eaten ghost
            if(self.direction == "up"):
                self.image = pygame.image.load("data\images\\eaten_ghost_up.png").convert_alpha()

            elif(self.direction == "down"):
                self.image = pygame.image.load("data\images\\eaten_ghost_down.png").convert_alpha()

            elif(self.direction == "left"):
                self.image = pygame.image.load("data\images\\eaten_ghost_left.png").convert_alpha()

            elif(self.direction == "right"):
                self.image = pygame.image.load("data\images\\eaten_ghost_right.png").convert_alpha()
                
        elif(self.state == "inedible"):
            #Show the normal state of the ghost (e.g. as blinky, blyde, inky, or pinky)
            picture_location = ""
            if(self.direction == "up"):
                picture_location = "data\images\\" + self.name + "_up.png"               
                self.image = pygame.image.load(picture_location).convert_alpha()

            elif(self.direction == "down"):
                picture_location = "data\images\\" + self.name + "_down.png" 
                self.image = pygame.image.load(picture_location).convert_alpha()

            elif(self.direction == "left"):
                picture_location = "data\images\\" + self.name + "_left.png" 
                self.image = pygame.image.load(picture_location).convert_alpha()

            elif(self.direction == "right"):
                picture_location = "data\images\\" + self.name + "_right.png"
                self.image = pygame.image.load(picture_location).convert_alpha()
        
        #Scale the resulting image as normal
        self.image = pygame.transform.scale(self.image, (50, 30))


