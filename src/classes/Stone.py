import pygame
from src.classes.VisibleObject import VisibleObject
from src.classes.MovableObject import MovableObject
from src.classes.CollidableObject import CollidableObject

pygame.init()

class Stone(VisibleObject, MovableObject, CollidableObject):
    def __init__(self, img = 'stone.png', pos = pygame.math.Vector2(0,0), level = 1):
        VisibleObject.__init__(self, img = img, pos = pos)
        v = pygame.math.Vector2(0, level)
        self.level = level
        MovableObject.__init__(self, v = v)
        CollidableObject.__init__(self)

    def update(self):
        old_rect = MovableObject.update(self)
        return old_rect
