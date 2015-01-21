import pygame
from src.Constants import *

pygame.init()

class AnimatedObject(pygame.sprite.DirtySprite):
    def __init__(self, img = None, pos = pygame.math.Vector2(0,0), size = pygame.math.Vector2(1,1), animations = []):
        self.animations = animations
        if self.animations == []:
            self.active_animation = None
        else:
            self.active_animation = self.animations[0]
        self.image = pygame.Surface(size)
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(topleft = pos)
        pygame.sprite.DirtySprite.__init__(self)
        
    def update(self):
        self.dirty = 1
        if not self.active_animation is None:
            update_return = self.active_animation.update()
            if not update_return is None:
                self.image = update_return
        
    def add_animation(self, animation):
        self.animations.append(animation)
