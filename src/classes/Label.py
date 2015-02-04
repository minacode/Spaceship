import pygame
from src.classes.State import State
from src.Constants import *

class Label(pygame.sprite.DirtySprite):
    def __init__(self, state, pos):
        pygame.sprite.DirtySprite.__init__(self)
        self.position = pos
        self.state = state
        self.old_state = State( self.state.get_value() )
        self.create_image()

    def create_image(self):
        self.image = FONT.render( str( self.state.get_value() ), 1, RED, WHITE )
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position

    def update(self):
        if self.state.get_value() != self.old_state.get_value():
            self.old_state.set_value( self.state.get_value() )
            self.create_image()
            self.dirty = 1
