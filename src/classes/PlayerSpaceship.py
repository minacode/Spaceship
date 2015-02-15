import pygame
from src.Constants import *
from src.classes.Spaceship import Spaceship
from src.classes.SoundManager import SOUND_MANAGER
from src.Constants import *

pygame.init()


class PlayerSpaceship(Spaceship):
    def __init__(self, img, pos = pygame.math.Vector2(0,0), direction = pygame.math.Vector2(0,-1), v = pygame.math.Vector2(0,0), weapons = [None, None]):
        Spaceship.__init__(self, img = img, pos = pos, direction = direction, v = v)
        global SOUND_MANAGER
        SOUND_MANAGER.load_sound( COLLECT_SOUND, COLLECT_VOLUME )

    def collect_dust(self, dust):
        global SOUND_MANAGER
        SOUND_MANAGER.play_sound( COLLECT_SOUND )
        self.energy.increase( dust.energy_value )
