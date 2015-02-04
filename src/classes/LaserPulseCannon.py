import pygame
from src.classes.Weapon import Weapon
from src.classes.LaserShot import LaserShot
from src.classes.SoundManager import SOUND_MANAGER
from src.Constants import *

class LaserPulseCannon(Weapon):
    def __init__(self, 
                 pos = pygame.math.Vector2(0,0), 
                 direction = pygame.math.Vector2(0,-1), 
                 counter = LASER_PULSE_CANNON_RELOAD_TIME, 
                 reload_time = LASER_PULSE_CANNON_RELOAD_TIME, 
                 energy_cost = LASER_PULSE_CANNON_ENERGY_COST ):
        Weapon.__init__(self, pos = pos, direction = direction, counter = counter, reload_time = reload_time, energy_cost = energy_cost)
        self.sound = LASER_PULSE_CANNON_SOUND
        global SOUND_MANAGER
        SOUND_MANAGER.load_sound( self.sound, LASER_PULSE_CANNON_VOLUME )
        
    def create_shot(self, pos):
        global SOUND_MANAGER
        SOUND_MANAGER.play_sound( self.sound )
        return [ LaserShot( pos = pos, direction = self.direction.rotate( i*5 )) for i in range(-9,10) ]
