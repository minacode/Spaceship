import pygame
from src.classes.Weapon import Weapon
from src.classes.LaserShot import LaserShot

class LaserCannon(Weapon):
    def __init__(self, pos = pygame.math.Vector2(0,0), direction = pygame.math.Vector2(0,-1), counter = 60, reload_time = 5):
        Weapon.__init__(self, pos = pos, direction = direction, counter = counter, reload_time = reload_time)
        self.sound = pygame.mixer.Sound('sounds/EnergyCannon.wav')
        self.sound.set_volume(0.3)
        
    def create_shot(self, pos, world):
        self.sound.play()
        offset = pygame.math.Vector2(10,0)
        world.add_shot( LaserShot(pos = pos, direction = self.direction) )
        world.add_shot( LaserShot(pos = pos - offset, direction = self.direction) )
        world.add_shot( LaserShot(pos = pos + offset, direction = self.direction) )
