import pygame
from pygame.locals import *
import random
import threading
from src.classes.World import World
from src.classes.PlayerSpaceship import PlayerSpaceship
from src.classes.HUD import HUD
from src.classes.StateBar import StateBar
from src.classes.LaserCannon import LaserCannon
from src.classes.LaserPulseCannon import LaserPulseCannon
from src.classes.Shield import Shield
from src.classes.SoundManager import SOUND_MANAGER
from src.Constants import *

pygame.init()

class GameStateSpace():
    def __init__(self, player, screen, clock, fps):
        self.running = False
        self.game_running = False
        self.space_state = SPACESTATE_ASTEROIDS
        self.updated_rects = []

        self.set_screen(screen)
        self.set_clock(clock)
        self.set_fps(fps)

        self.set_world( World( player ) )
        self.set_player(player)
        
        spaceship = PlayerSpaceship(PLAYER_SPACESHIP_IMAGE, pygame.math.Vector2(WORLD_SIZE.x * 0.5, WORLD_SIZE.y * 0.8) )
        spaceship.set_weapon( PRIMARY_WEAPON_INDEX, LaserCannon( pos = pygame.math.Vector2( spaceship.rect.width / 2, 0 )))
        spaceship.set_weapon( SECONDARY_WEAPON_INDEX, LaserPulseCannon( pos = pygame.math.Vector2( spaceship.rect.width / 2, 0 )))
        spaceship.set_shield( Shield() )
        self.player.set_spaceship(spaceship)
        self.world.set_spaceship(spaceship)
        
        self.player.set_hud( HUD() )

    def set_screen(self, screen):
        self.screen = screen

    def set_clock(self, clock):
        self.clock = clock

    def set_fps(self, fps):
        self.fps = fps

    def set_player(self, player):
        self.player = player

    def set_world(self, world):
        self.world = world

    def start(self):
        self.running = True
        self.run()

    def quit_game(self):
        self.running = False
        self.game_running = False

    def generate_new_objects(self):
        if self.space_state == SPACESTATE_ASTEROIDS:
            self.generate_stones()
        if self.space_state == SPACESTATE_BOSS:
            self.generate_boss()

    def generate_stones(self):
        if random.randint(1, int(1 / CHANCE_NEW_STONE)) == 1:
            self.world.generate_stone()

    def generate_boss(self):
        self.world.generate_boss()

    def run_graphics(self):
        self.screen.blit(self.world.image, self.world.rect.topleft)
        while self.running and not self.collided:
            self.clear()
            drawn_rects = self.draw()
            pygame.display.update(self.updated_rects + drawn_rects)
            
    def run_logic(self):
        while self.running and not self.collided:
            self.clock.tick(self.fps)
            self.generate_new_objects()
            time = self.clock.get_time() / 1000
            self.updated_rects = self.update( time )
            self.collided = self.world.collide_objects()

    def run(self):
        global SOUND_MANAGER
        SOUND_MANAGER.play_music( BACKGROUNDMUSIC, BACKGROUNDMUSIC_VOLUME )
        self.running = True
        self.collided = False

        graphics_thread = threading.Thread(target = self.run_graphics)
        logic_thread    = threading.Thread(target = self.run_logic)
        graphics_thread.start()
        logic_thread.start()

        return self.game_running, GAMESTATE_MAINMENU
        
    def clear(self):
        if not self.world is None:
            self.world.clear()
        #if not self.player is None:
        #    self.player.clear(self.screen)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == KEY_QUIT_GAME:
                    self.quit_game()
                elif not self.player is None:
                    self.player.handle_event(event, self.world)
            elif event.type == JOYBUTTONDOWN:
                if event.button == JOYBUTTON_QUIT_GAME:
                    self.quit_game()
                elif not self.player is None:
                    self.player.handle_event(event, self.world)
            elif not self.player is None:
                self.player.handle_event(event, self.world)

    def update(self, frame_time):
        self.handle_input()
        old_rects = []
        if not self.player is None:
            self.player.update(frame_time)
        if not self.world is None:
            old_rects += self.world.update(frame_time)
        return old_rects
            
    def draw(self):
        drawn_rects = []
        if not self.world is None:
            drawn_rects += self.world.draw(self.screen)
        if not self.player is None:
            drawn_rects += self.player.draw(self.screen)
        return drawn_rects
