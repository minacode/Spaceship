import pygame
from src.classes.VisibleObject import VisibleObject
from src.Constants import *

pygame.init()

class Animation(VisibleObject):
    def __init__(self, img, frames = 0, size = pygame.math.Vector2(1,1), frame_delay = []):
        VisibleObject.__init__(self, img)
        self.size = size
        self.return_image = pygame.Surface(self.size)
        self.return_image.set_colorkey(WHITE)
        self.frames = frames
        self.active_frame_number = 0
        if frame_delay == []:
            self.frame_delay = [1] * self.frames
        else:
            self.frame_delay = frame_delay
        self.delay_counter = 0
        
    def update(self):
        self.delay_counter += 1
        if self.delay_counter >= self.frame_delay[self.active_frame_number]:
            self.delay_counter = 0
            self.active_frame_number += 1
            if self.active_frame_number >= self.frames:
                self.active_frame_number = 0
            return self.get_frame()
        else:
            return None
        
    def get_frame(self):
        self.return_image.fill(WHITE)
        self.return_image.blit(self.image, (0,0), pygame.Rect((self.size.x * self.active_frame_number ,0), self.size))
        return self.return_image
