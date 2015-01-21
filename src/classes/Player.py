import pygame
from src.Constants import *
from pygame.locals import *

pygame.init()

class Player():
    def __init__(self):
        pass
        
    def set_spaceship(self, spaceship):
        self.spaceship = spaceship
        
    def set_hud(self, hud):
        self.hud = hud
        
    def set_weapon(self, weapon):
        self.hud = self.spaceship.set_weapon(weapon, self.hud)
        
    def set_shield(self, shield):
        self.hud = self.spaceship.set_shield(shield, self.hud)
        
    def handle_event(self, event, world):
        if not self.spaceship is None:
            if event.type == KEYDOWN:
                if event.key == KEY_SHOOT:
                    self.spaceship.shoot(world)
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
                    self.spaceship.shoot(world)
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
    
    def update(self):
        if not self.hud is None:
            self.hud.update()
        
    def draw(self, screen):
        drawn_rects = []
        if not self.hud is None:
            drawn_rects += self.hud.draw(screen)
        return drawn_rects
