import pygame
from src.classes.ImageManager import IMAGE_MANAGER
from src.Constants import *
from pygame.locals import *

pygame.init()


class VisibleObject(pygame.sprite.DirtySprite):
    def __init__(self, img, pos = pygame.math.Vector2(0,0)):
        pygame.sprite.DirtySprite.__init__(self)
        global IMAGE_MANAGER
        self.image = IMAGE_MANAGER.load_image(img)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect(topleft = pos)
