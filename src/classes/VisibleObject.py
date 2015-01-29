import pygame
from src.classes.ImageManager import IMAGE_MANAGER
from src.Constants import *
from pygame.locals import *

pygame.init()


class VisibleObject(pygame.sprite.DirtySprite):
    def __init__(self, img = None, pos = pygame.math.Vector2(0,0)):
        pygame.sprite.DirtySprite.__init__(self)
        global IMAGE_MANAGER
        if not img is None:
            self.image = IMAGE_MANAGER.load_image(img)
            self.image.set_colorkey(WHITE)
        else:
            self.image = pygame.Surface( pygame.math.Vector2(1,1) )
        self.rect = self.image.get_rect(topleft = pos)
