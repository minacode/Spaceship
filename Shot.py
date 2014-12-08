import pygame
from VisibleObject import *
from MovableObject import *
from CollidableObject import *

pygame.init()

class Shot(VisibleObject, MovableObject, CollidableObject):
    def __init__(self, img, pos = pygame.math.Vector2(0,0), direction = pygame.math.Vector2(0,-1), v = None):
        VisibleObject.__init__(self, img, pos)
        if v is None:
            v = direction
        MovableObject.__init__(self, v)
        CollidableObject.__init__(self)
        self.set_direction(direction)
        self.set_position(pos)

    def set_position(self, pos):
        self.rect.midbottom = pos

    def set_direction(self, direction):
        self.direction = direction
        angle = pygame.math.Vector2(0,-1).angle_to( self.direction )
        self.image = pygame.transform.rotate(self.image, angle)

    def update(self):
        old_rect = MovableObject.update(self)
        return old_rect
