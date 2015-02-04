import pygame
from src.classes.VisibleObject import VisibleObject
from src.classes.MovableObject import MovableObject
from src.classes.CollidableObject import CollidableObject
from src.classes.State import State
from src.classes.StateBar import StateBar
from src.Constants import *

pygame.init()

class Spaceship(VisibleObject, MovableObject, CollidableObject):
    def __init__(
            self, img, 
            pos = pygame.math.Vector2(0,0), 
            direction = pygame.math.Vector2(0,-1), 
            v = pygame.math.Vector2(0,0), 
            energy = State(500), 
            max_energy = 1000, 
            regeneration = PLAYER_SPACESHIP_ENERGY_REGENERATION, 
            weapons = [None, None], 
            shield = None, 
            hp = None, 
            max_hp = None ):
        VisibleObject.__init__(self, img, pos)
        MovableObject.__init__(self, v)
        CollidableObject.__init__(self)
        self.direction = direction
        self.energy = energy
        self.max_energy = max_energy
        self.regeneration = regeneration
        self.weapons = weapons
        self.shield = shield

    def set_weapon(self, index, weapon):
        self.weapons[index] = weapon
        
    def set_shield(self, shield):
        self.shield = shield
    
    def load_energy(self, frame_time):
        load = self.max_energy - self.energy.get_value()
        frame_regeneration = self.regeneration * frame_time
        if load > frame_regeneration:
            load = frame_regeneration
        self.energy.increase(load)
        
    def handle_collision(self):
        if not self.shield is None:
            self.energy.decrease( self.shield.handle_collision() )
            if self.energy > 0: # >= ?
                return False
        return True
        
    def shoot_weapon(self, i):
        if not self.weapons[i] is None:
            self.energy, shots = self.weapons[i].shoot( self.energy, list(self.rect.topleft) )
            return shots
        else:
            return []
    
    def clear(self, screen, background):
        VisibleObject.clear(self, screen, background)
        if not self.shield is None:
            self.shield.clear(screen, background)
    
    def update(self, frame_time):
        if self.energy.get_value() < self.max_energy:
            self.load_energy(frame_time)
        old_rect = MovableObject.update(self, frame_time)
        for weapon in self.weapons:
            if not weapon is None:
                weapon.update(frame_time)
        if not self.shield is None:
            self.shield.update(self.rect.topleft)
        return old_rect
