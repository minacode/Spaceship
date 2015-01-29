import pygame
from src.Constants import *
from src.classes.TexturedObject import TexturedObject
from src.classes.State import State

pygame.init()

class StateBar(TexturedObject):
    def __init__(self, 
                 state = State(0), 
                 max_state_value = 1, 
                 size = pygame.math.Vector2(1,1), 
                 pos = pygame.math.Vector2(0,0), 
                 img = None, 
                 direction = pygame.math.Vector2(1,0), 
                 color = BLACK, 
                 background = GREEN ):
        TexturedObject.__init__(self, size = size, pos = pos, img = img, background = background)
        self.max_state_value = max_state_value
        self.state = state
        self.last_state_value = self.state.get_value()
        self.direction = direction
        self.color = color
        self.background = background
        if not self.state is None and not self.max_state_value is None:
            self.render()
        else:
            self.image.fill(self.color)
            
    def render(self):
        self.image.fill(self.background)
        if self.direction.x != 0 and self.direction.y == 0:
            width = int( self.rect.width * (self.state.get_value() / self.max_state_value) )
            bar = pygame.Surface((width, self.rect.height))
            bar.fill(self.color)
            if self.direction.x > 0:
                self.image.blit(bar, (0,0))
            else:
                self.image.blit(bar, ( self.rect.width - width ,0))
        elif self.direction.x == 0 and self.direction.y != 0:
            height = int( self.rect.height * (self.state.get_value() / self.max_state_value) )
            bar = pygame.Surface((self.rect.width, height))
            bar.fill(self.color)
            if self.direction.y > 0:
                self.image.blit(bar, (0,0))
            else:
                self.image.blit(bar, (0, self.rect.height - height ))
                
    def update(self):
        self.dirty = 1
        if not (self.state is None or self.max_state_value is None):
            if self.state.get_value() != self.last_state_value:
                self.last_state_value = self.state.get_value()
                self.render()
