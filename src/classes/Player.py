import pygame
from src.Constants import *
from pygame.locals import *

pygame.init()

class Player():
    def __init__(self):
        self.hud = None
        
    def set_spaceship(self, spaceship):
        self.spaceship = spaceship
        if self.hud is not None:
        	self.hud = self.spaceship.init_hud(self.hud)
        
    def set_hud(self, hud):
        self.hud = hud
        
    def set_weapon(self, weapon):
        self.hud = self.spaceship.set_weapon(weapon, self.hud)
        
    def set_shield(self, shield):
        self.spaceship.set_shield(shield)
        
    def handle_event(self, event, world):
        if not self.spaceship is None:
            if event.type == KEYDOWN:
                if event.key == KEY_SHOOT:
                    world.add_shot( self.spaceship.shoot() )
                if event.key == KEY_MOVE_LEFT:
                    self.spaceship.accelerate_left(PLAYER_SPACESHIP_SPEED)
                if event.key == KEY_MOVE_RIGHT:
                    self.spaceship.accelerate_right(PLAYER_SPACESHIP_SPEED)
            if event.type == KEYUP:
                if event.key == KEY_MOVE_LEFT:
                    self.spaceship.accelerate_right(PLAYER_SPACESHIP_SPEED)
                if event.key == KEY_MOVE_RIGHT:
                    self.spaceship.accelerate_left(PLAYER_SPACESHIP_SPEED)
            if event.type == JOYBUTTONDOWN:
                if event.button == JOYBUTTON_SHOOT:
                    world.add_shot( self.spaceship.shoot() )
                if event.button == JOYBUTTON_MOVE_LEFT:
                    self.spaceship.accelerate_left(PLAYER_SPACESHIP_SPEED)
                if event.button == JOYBUTTON_MOVE_RIGHT:
                    self.spaceship.accelerate_right(PLAYER_SPACESHIP_SPEED)
            if event.type == JOYBUTTONUP:
                if event.button == JOYBUTTON_MOVE_LEFT:
                    self.spaceship.accelerate_right(PLAYER_SPACESHIP_SPEED)
                if event.button == JOYBUTTON_MOVE_RIGHT:
                    self.spaceship.accelerate_left(PLAYER_SPACESHIP_SPEED)
    
    def clear(self, screen, background):
        self.hud.clear(screen, background)
    
    def update(self, frame_time):
        if not self.hud is None:
            self.hud.update()
        
    def draw(self, screen):
        drawn_rects = []
        if not self.hud is None:
            drawn_rects += self.hud.draw(screen)
        return drawn_rects
