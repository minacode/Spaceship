import pygame

pygame.init()

class CollidableObject():
    def __init__(self):
        self.set_mask(self.image)
        
    def set_mask(self, img):
        self.mask = pygame.mask.from_surface(img)
