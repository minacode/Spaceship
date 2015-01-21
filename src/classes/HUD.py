import pygame
from pygame.locals import *

class HUD():
    def __init__(self):
        self.elements = pygame.sprite.LayeredDirty()
    
    def add(self, element):
        self.elements.add(element)
    
    def clear(self, screen, background):
        self.elements.clear(screen, background)
    
    def update(self):
        self.elements.update()
        
    def draw(self, screen):
        return self.elements.draw(screen)
