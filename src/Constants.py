import pygame
from pygame.locals import *

pygame.init()

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)

# Pygame
FPS = 60
SCREEN_SIZE = [300,500]
FONT = pygame.font.SysFont('Times New Roman', 15)

# States
GAMESTATE_MAINMENU = 1
GAMESTATE_SPACE = 2

SPACESTATE_STONES = 1
SPACESTATE_ASTEROIDS = 2
SPAECSTATE_BATTLE = 3
SPACESTATE_BOSS = 4

PRIMARY_WEAPON_INDEX = 0
SECONDARY_WEAPON_INDEX = 1 

# World
WORLD_SIZE = pygame.math.Vector2(300, 500)
WORLD_POS = pygame.math.Vector2(5,0)
WORLD_BACKGROUND = WHITE

DUST_LAYER = 5
SPACESHIP_LAYER = 4
STONE_LAYER = 3
SHOT_LAYER = 2
EFFECT_LAYER = 1

# Player Spaceship
PLAYER_SPACESHIP_SPEED = 200
PLAYER_SPACESHIP_ENERGY_REGENERATION = 50 

LASER_SHOT_SPEED = 500

# Laser Cannon
LASER_CANNON_RELOAD_TIME = 0.2
LASER_CANNON_ENERGY_COST = 50

# Laser Pulse Cannon
LASER_PULSE_CANNON_RELOAD_TIME = 1
LASER_PULSE_CANNON_ENERGY_COST = 300

# Stones
CHANCE_NEW_STONE = 0.05
MAX_STONE_LEVEL = 3
STONE_SPEED = [ 50 *(i+1) for i in range( MAX_STONE_LEVEL )]

# Dust
BLUE_DUST_VALUE = 2
BLUE_DUST_ENERGY_VALUE = 15
BLUE_DUST_FOLLOW_RADIUS = 400
BLUE_DUST_MAX_TURN_ANGLE = 1
BLUE_DUST_SPEED = 200
GREEN_DUST_SPEED = 70
GREEN_DUST_VALUE = 5
GREEN_DUST_ENERGY_VALUE = 200
GREEN_DUST_FOLLOW_RADIUS = 70
CHANCE_GREEN_DUST = { 1 : 0.01 , 
                      2 : 0.1  , 
                      3 : 0.25  }
GREEN_DUST_ABS_V = 1
GREEN_DUST_MAX_ACCELERATION = 0.5

# Images
IMAGE_PATH = 'images/'

PLAYER_SPACESHIP_IMAGE = 'spaceship.png'
SHIELD_IMAGE = 'shield.png'
LASER_SHOT_IMAGE = 'lasershot.png'
BLUE_DUST_IMAGE = 'blue_dust.png'
GREEN_DUST_IMAGE = 'green_dust.png'
EXPLOSION_IMAGE = 'explosion.png'

# Sounds
SOUND_PATH = 'sounds/'

COLLECT_SOUND = 'pop.wav'
COLLECT_VOLUME = 0.3
LASER_CANNON_SOUND = 'EnergyCannon.wav'
LASER_CANNON_VOLUME = 0.3
LASER_PULSE_CANNON_SOUND = 'EnergyCannon.wav'
LASER_PULSE_CANNON_VOLUME = 0.3
EXPLOSION_SOUND = 'explosion.wav'
EXPLOSION_VOLUME = 0.1

BACKGROUNDMUSIC = 'Faunts - M4 (Part II).mp3'
BACKGROUNDMUSIC_VOLUME = 1.0

# Controls- Keyboard

KEY_QUIT_GAME = K_q

KEY_MOVE_LEFT = K_a
KEY_MOVE_RIGHT = K_d
KEY_PRIMARY_WEAPON = K_w
KEY_SECONDARY_WEAPON = K_s

# Controls - Joystick

JOYBUTTON_QUIT_GAME = 0

JOYBUTTON_MOVE_LEFT = 4
JOYBUTTON_MOVE_RIGHT = 6
JOYBUTTON_PRIMARY_WEAPON = 2
JOYBUTTON_SECONDARY_WEAPON = 3
