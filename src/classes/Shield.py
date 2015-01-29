import pygame
from src.classes.VisibleObject import VisibleObject
from src.Constants import *

pygame.init()

class Shield(VisibleObject):
    def __init__(self, img = SHIELD_IMAGE, pos = pygame.math.Vector2(0,0), collision_energy = 200):
        VisibleObject.__init__(self, img, pos)
        self.collision_energy = collision_energy

    def set_position(self, pos):
        self.rect.topleft = pos - pygame.math.Vector2(10,10)

    def handle_collision(self):
        return self.collision_energy

    def update(self, pos):
        self.set_position(pos)
