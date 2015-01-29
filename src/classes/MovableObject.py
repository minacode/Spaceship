import copy
import pygame

pygame.init()

class MovableObject():
    def __init__(self, v = pygame.math.Vector2(0,0)):
        self.v = v
        self.vec_pos = pygame.math.Vector2(self.rect.left, self.rect.top)
        
    def accelerate_left(self, a):
        self.v.x -= a
        
    def accelerate_right(self, a):
        self.v.x += a
        
    def set_pos(self, pos):
        self.vec_pos = pos
        self.rect.topleft = ( int(self.vec_pos.x), int(self.vec_pos.y) )
        
    def update(self, frame_time):
        old_rect = copy.copy(self.rect)
        self.vec_pos = self.vec_pos + (self.v * frame_time)
        self.rect.top = int(self.vec_pos.y)
        self.rect.left = int(self.vec_pos.x)
        #self.rect.topleft += self.v
        self.dirty = 1
        return [old_rect]

#if self.v[0] != 0:
#    if self.rect.left + self.v[0] >= world_rect.left and self.rect.right + self.v[0] <= world_rect.right:
#        self.rect.move_ip(self.v[0], 0)
#        self.dirty = 1
#    elif self.v[0] < 0:
#        self.rect.move_ip(world_rect.left - self.rect.left, 0)
#        self.dirty = 1
#    else:
#        self.rect.move_ip(world_rect.right - self.rect.right, 0)
#        self.dirty = 1
