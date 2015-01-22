import pygame
from src.classes.VisibleObject import VisibleObject
from src.classes.State import State
from src.Constants import *

pygame.init()

class Shield(VisibleObject):
    def __init__(self, img = SHIELD_IMAGE, pos = pygame.math.Vector2(0,0), energy = State(500), max_energy = 1000, regeneration = 0.2):
        VisibleObject.__init__(self, img, pos)
        self.energy = energy
        self.max_energy = max_energy
        self.regeneration = regeneration

    def set_position(self, pos):
        self.rect.topleft = pos - pygame.math.Vector2(10,10)
    
    def load_energy(self):
        load = self.max_energy - self.energy.get_value()
        if load > self.regeneration:
            load = self.regeneration
        self.energy.set_value( self.energy.get_value() +load )

    def handle_collision(self):
        if self.energy.get_value() >= 200:
            self.energy.set_value( self.energy.get_value() -200 )
            return False
        else:
            return True

    def update(self, pos):
        self.set_position(pos)
        if self.energy.get_value() < self.max_energy:
            self.load_energy()
