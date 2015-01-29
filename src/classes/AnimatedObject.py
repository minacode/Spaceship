import pygame
from src.classes.VisibleObject import VisibleObject
from src.Constants import *

pygame.init()

class AnimatedObject(VisibleObject):
    def __init__(self, img = None, pos = pygame.math.Vector2(0,0), size = pygame.math.Vector2(1,1), animations = []):
        VisibleObject.__init__(self, img, pos)
        self.animations = animations
        if self.animations == []:
            self.active_animation = None
        else:
            self.active_animation = self.animations[0]
        self.rect = self.image.get_rect(topleft = pos)
        
    def update(self):
        self.dirty = 1
        if not self.active_animation is None:
            update_return = self.active_animation.update()
            if not update_return is None:
                self.image = update_return
        
    def add_animation(self, animation):
        self.animations.append(animation)
