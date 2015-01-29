import pygame

pygame.init()

class CollidableObject():
    def __init__(self):
        # self.set_mask(self.image)
        self.radius = ( self.image.get_height() + self.image.get_width() ) / 4
        
    def set_mask(self, img):
        self.mask = pygame.mask.from_surface(img)
