import pygame
from VisibleObject import *
from MovableObject import *
from CollidableObject import *
from StateBar import *

pygame.init()

class Spaceship(VisibleObject, MovableObject, CollidableObject):
    def __init__(self, img, pos = pygame.math.Vector2(0,0), direction = pygame.math.Vector2(0,-1), v = pygame.math.Vector2(0,0), weapon = None, shield = None, hp = None, max_hp = None):
        VisibleObject.__init__(self, img, pos)
        MovableObject.__init__(self, v)
        CollidableObject.__init__(self)
        self.direction = direction
        self.weapon = weapon
        self.shield = shield

    def set_weapon(self, weapon):
        self.weapon = weapon
        
    def set_shield(self, shield, hud):
        self.shield = shield
        
    def handle_collision(self):
        if not self.shield is None:
            return self.shield.handle_collision()
        else:
            return True
        
    def shoot(self, world):
        if not self.weapon is None:
            self.weapon.shoot( list(self.rect.topleft), world )
    
    def clear(self, screen, background):
        VisibleObject.clear(self, screen, background)
        if not self.shield is None:
            self.shield.clear(screen, background)
    
    def update(self):
        old_rect = MovableObject.update(self)
        if not self.weapon is None:
            self.weapon.update()
        if not self.shield is None:
            self.shield.update(self.rect.topleft)
        return old_rect
