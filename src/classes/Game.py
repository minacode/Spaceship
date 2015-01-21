import random
import pygame
from pygame.locals import *
from src.Constants import *
from src.classes.GameStateSpace import GameStateSpace
from src.classes.Player import Player

pygame.init()

class Game():
    def __init__(self):
        self.set_player( Player() )
        self.set_screen_size([int(WORLD_SIZE.x + 10), int(WORLD_SIZE.y + 5)])
        
        self.init_joysticks()
        self.set_fps( FPS )
        self.clock = pygame.time.Clock()
        self.set_font( FONT )
        self.set_game_state(GAMESTATE_SPACE)

    def set_game_state(self, game_state):
        if game_state == GAMESTATE_SPACE:
            self.game_state = GameStateSpace(self.player, self.screen, self.clock, self.fps)
    
    def stop(self):
        self.running = False
        
    def set_player(self, player):
        self.player = player
        
    def set_screen_size(self, screen_size):
        self.screen_size = screen_size
        if self.screen_size[0] > 0 and self.screen_size[0] > 0:
            self.screen = pygame.display.set_mode(self.screen_size)
        
    def init_joysticks(self):
        self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        for joystick in self.joysticks:
            joystick.init()
        
    def set_fps(self, fps):
        self.fps = fps
        
    def set_font(self, font):
        self.font = font

    def run(self):
        self.running = True
        while self.running:
            self.running, gamestate = self.game_state.run()
            self.set_game_state(gamestate)
        
