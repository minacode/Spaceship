import pygame
from src.classes.Shot import Shot
from src.Constants import *

class LaserShot(Shot):
    def __init__(self, img = 'lasershot.png', pos = pygame.math.Vector2(0,0), direction = pygame.math.Vector2(0,-1), v = None):
        if v is None:
            v = direction * LASER_SHOT_SPEED
        Shot.__init__(self, img, pos, direction, v)
