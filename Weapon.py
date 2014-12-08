import pygame
from State import *

pygame.init()

class Weapon():
    def __init__(self, pos = pygame.math.Vector2(0,0), direction = pygame.math.Vector2(0,-1), counter = 0, reload_time = None):
        self.counter = State(counter)
        self.reload_time = reload_time
        self.position = pos
        self.direction = direction
        
    def set_counter(self, counter):
        self.counter.set_value(counter)
        
    def get_counter(self):
        return self.counter.get_value()
    
    def increment_counter(self):
        self.counter.set_value( self.counter.get_value() +1 )
        
    def set_direction(self, direction):
        self.direction = direction
        
    def set_position(self, pos):
        self.position = pos
    
    def update(self):
        if not self.reload_time is None:
            if self.get_counter() < self.reload_time:
                self.increment_counter()
            
    def shoot(self, pos, world):
        pos += self.position
        if not self.reload_time is None:
            if self.get_counter() >= self.reload_time:
                self.set_counter(0)
                self.create_shot(pos, world)
        else:
            self.create_shot(pos, world)
            
    def create_shot(self, pos, world):
        pass # template method
