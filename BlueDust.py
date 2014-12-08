import pygame
from Dust import *
from Constants import *
from pygame.locals import *

pygame.init()

class BlueDust(Dust):
    def __init__(self, img = BLUE_DUST_IMAGE, pos = pygame.math.Vector2(0,0), v = pygame.math.Vector2(0, 1 * BLUE_DUST_SPEED)):
        Dust.__init__(self, img = img, pos = pos, v = v, value = BLUE_DUST_VALUE, follow_radius = BLUE_DUST_FOLLOW_RADIUS, speed = BLUE_DUST_SPEED)
