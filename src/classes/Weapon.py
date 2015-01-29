import pygame
from src.classes.State import State

pygame.init()

class Weapon():
    def __init__(self, pos = pygame.math.Vector2(0,0), direction = pygame.math.Vector2(0,-1), counter = 0, reload_time = None, energy_cost = 0):
        self.counter = State(counter)
        self.reload_time = reload_time
        self.position = pos
        self.direction = direction
        self.energy_cost = energy_cost
        
    def set_direction(self, direction):
        self.direction = direction
        
    def set_position(self, pos):
        self.position = pos
    
    def update(self, frame_time):
        if not self.reload_time is None:
            if self.counter.get_value() < self.reload_time:
                self.counter.increase(frame_time)
            
    def shoot(self, energy, pos):
        if energy.get_value() >= self.energy_cost:
            energy.decrease( self.energy_cost )
            pos += self.position
            if not self.reload_time is None:
                if self.counter.get_value() >= self.reload_time:
                    self.counter.set_value(0)
            return energy, self.create_shot(pos)
        return energy, []
            
    def create_shot(self, pos):
        return []
