import pygame
from src.classes.VisibleObject import VisibleObject
from src.classes.MovableObject import MovableObject
from src.classes.CollidableObject import CollidableObject
from src.Constants import *

pygame.init()

class Dust(VisibleObject, MovableObject, CollidableObject):
    def __init__(self, img, pos = pygame.math.Vector2(0,0), v = pygame.math.Vector2(0, 1), value = 0, energy_value = 0, follow_radius = 0, speed = 0):
        VisibleObject.__init__(self, img = img, pos = pos)
        MovableObject.__init__(self, v = v)
        CollidableObject.__init__(self)
        self.direction = v.normalize()
        self.v = self.direction * speed
        self.value = value
        self.energy_value = energy_value
        self.follow_radius = follow_radius
        self.speed = speed
    
    def set_direction(self, direction):
        self.direction = direction
        self.v = self.direction * self.speed
        
    def follow_pos(self, pos):
        target_direction = pygame.math.Vector2(pos) - pygame.math.Vector2(self.rect.center)
        if target_direction.length() <= self.follow_radius:
            self.direction = target_direction.normalize()
        else:
            self.direction = pygame.math.Vector2(0,1)
        self.v = self.direction * self.speed
        
    def update(self, frame_time):
        old_rect = MovableObject.update(self, frame_time)
        return old_rect
