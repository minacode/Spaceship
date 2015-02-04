import pygame
from pygame.locals import *
from src.classes.Label import Label
from src.classes.State import State
from src.classes.StateBar import StateBar
from src.Constants import *

pygame.init()

class Player():
    def __init__(self):
        self.spaceship = None
        self.hud = None
        self.collected_dust = State(0)
        
    def set_spaceship(self, spaceship):
        self.spaceship = spaceship
        
    def set_hud(self, hud):
        self.hud = hud
        self.hud.add( Label( self.collected_dust, pygame.math.Vector2(6,0) ))
        if not self.spaceship is None:
            self.hud.add( 
                StateBar(
                    state = self.spaceship.energy,
                    max_state_value = self.spaceship.max_energy,
                    size = pygame.math.Vector2(5,500),
                    pos = pygame.math.Vector2(0, 0),
                    direction = pygame.math.Vector2(0,-1),
                    color = BLUE
                )
            )
            if not self.spaceship.weapons[0] is None:
                if not self.spaceship.weapons[0].reload_time is None:
                    self.hud.add(
                        StateBar(
                            state = self.spaceship.weapons[0].counter,
                            max_state_value = self.spaceship.weapons[0].reload_time,
                            size = pygame.math.Vector2(300,6),
                            pos = pygame.math.Vector2(5,500),
                            direction = pygame.math.Vector2(1,0)
                        )
                    )
        
    def collect_dust(self, dust):
        self.collected_dust.increase( dust.value )
        
    def handle_event(self, event, world):
        if not self.spaceship is None:
            if event.type == KEYDOWN:
                if event.key == KEY_PRIMARY_WEAPON:
                    world.add_shot( self.spaceship.shoot_weapon( PRIMARY_WEAPON_INDEX ) )
                elif event.key == KEY_SECONDARY_WEAPON:
                    world.add_shot( self.spaceship.shoot_weapon( SECONDARY_WEAPON_INDEX ) )
                elif event.key == KEY_MOVE_LEFT:
                    self.spaceship.accelerate_left(PLAYER_SPACESHIP_SPEED)
                elif event.key == KEY_MOVE_RIGHT:
                    self.spaceship.accelerate_right(PLAYER_SPACESHIP_SPEED)
            if event.type == KEYUP:
                if event.key == KEY_MOVE_LEFT:
                    self.spaceship.accelerate_right(PLAYER_SPACESHIP_SPEED)
                elif event.key == KEY_MOVE_RIGHT:
                    self.spaceship.accelerate_left(PLAYER_SPACESHIP_SPEED)
            if event.type == JOYBUTTONDOWN:
                if event.button == JOYBUTTON_PRIMARY_WEAPON:
                    world.add_shot( self.spaceship.shoot_weapon( PRIMARY_WEAPON_INDEX ) )
                elif event.button == JOYBUTTON_SECONDARY_WEAPON:
                    world.add_shot( self.spaceship.shoot_weapon( SECONDARY_WEAPON_INDEX ) )
                elif event.button == JOYBUTTON_MOVE_LEFT:
                    self.spaceship.accelerate_left(PLAYER_SPACESHIP_SPEED)
                elif event.button == JOYBUTTON_MOVE_RIGHT:
                    self.spaceship.accelerate_right(PLAYER_SPACESHIP_SPEED)
            if event.type == JOYBUTTONUP:
                if event.button == JOYBUTTON_MOVE_LEFT:
                    self.spaceship.accelerate_right(PLAYER_SPACESHIP_SPEED)
                elif event.button == JOYBUTTON_MOVE_RIGHT:
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
