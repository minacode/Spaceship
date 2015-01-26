import pygame
from src.classes.Weapon import Weapon
from src.classes.LaserShot import LaserShot
from src.classes.SoundManager import SOUND_MANAGER
from src.Constants import *

class LaserCannon(Weapon):
    def __init__(self, pos = pygame.math.Vector2(0,0), direction = pygame.math.Vector2(0,-1), counter = 60, reload_time = 5):
        Weapon.__init__(self, pos = pos, direction = direction, counter = counter, reload_time = reload_time)
        global SOUND_MANAGER
        SOUND_MANAGER.load_sound( LASER_CANNON_SOUND, LASER_CANNON_VOLUME )
        
    def create_shot(self, pos):
        global SOUND_MANAGER
        SOUND_MANAGER.play_sound( LASER_CANNON_SOUND )
        offset = pygame.math.Vector2(10,0)
        return [
			LaserShot(pos = pos, direction = self.direction),
			LaserShot(pos = pos - offset, direction = self.direction),
			LaserShot(pos = pos + offset, direction = self.direction)
		]
