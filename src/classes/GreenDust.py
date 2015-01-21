import random
import pygame
from src.classes.Dust import Dust
from src.Constants import *
from pygame.locals import *

pygame.init()

class GreenDust(Dust):
    def __init__(self, img = GREEN_DUST_IMAGE, pos = pygame.math.Vector2(0,0), v = pygame.math.Vector2(0, 1 * GREEN_DUST_SPEED)):
        Dust.__init__(self, img = img, pos = pos, v = v, value = GREEN_DUST_VALUE, follow_radius = GREEN_DUST_FOLLOW_RADIUS, speed = GREEN_DUST_SPEED)
