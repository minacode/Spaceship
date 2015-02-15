import pygame
from src.classes.Spaceship import Spaceship
from src.Constants import *

class EnemySpaceship(Spaceship):
    def __init__(
        self, 
        img = ENEMY_SPACESHIP_IMAGE, 
        pos = pygame.math.Vector2(0,0), 
        direction = pygame.math.Vector2(0,1), 
        v = pygame.math.Vector2(0,1) * ENEMY_SPACESHIP_SPEED 
    ):
        Spaceship.__init__(self, img = img, pos = pos, direction = direction, v = v)
        
    def update(self, frame_time):
        old_rect = Spaceship.update(self, frame_time)
        return old_rect
