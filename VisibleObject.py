import pygame
from Constants import *
from pygame.locals import *

pygame.init()


class VisibleObject(pygame.sprite.DirtySprite):
    def __init__(self, img, pos = pygame.math.Vector2(0,0)):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.image.load('images/' + img).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect(topleft = pos)
