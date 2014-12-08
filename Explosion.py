import copy
import pygame
from Effect import *
from AnimatedObject import *
from Animation import *

pygame.init()

class Explosion(AnimatedObject, Effect):
    def __init__(self, size = pygame.math.Vector2(40,40)):
        AnimatedObject.__init__(self, size = size)
        animation = Animation(img = EXPLOSION_IMAGE, frames = 3, size = size, frame_delay = [10,10,10])
        self.add_animation( animation )
        self.active_animation = self.animations[0]
        self.counter = 0
        self.max_counter = 50

    def update(self):
        AnimatedObject.update(self)
        Effect.update(self)
        return [copy.copy(self.rect)]
