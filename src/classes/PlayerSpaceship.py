import pygame
from src.Constants import *
from src.classes.Spaceship import Spaceship

pygame.init()


class PlayerSpaceship(Spaceship):
    def __init__(self, img, pos = pygame.math.Vector2(0,0), direction = pygame.math.Vector2(0,-1), v = pygame.math.Vector2(0,0), weapon = None, hp = None):
        Spaceship.__init__(self, img = img, pos = pos, direction = direction, v = v)
        self.hp = hp
        self.collected_dust = 0
        self.collect_sound = pygame.mixer.Sound('sounds/pop.wav')
        self.collect_sound.set_volume(0.3)

    def set_weapon(self, weapon, hud):
        self.weapon = weapon
        hud.add( StateBar(state = weapon.counter,
                          max_state_value = weapon.reload_time,
                          size = pygame.math.Vector2(300,6),
                          pos = pygame.math.Vector2(5,500),
                          direction = pygame.math.Vector2(1,0)
               ) )
        return hud

    def set_shield(self, shield, hud):
        self.shield = shield
        hud.add( StateBar(state = shield.energy,
                          max_state_value = shield.max_energy,
                          size = pygame.math.Vector2(5,500),
                          pos = pygame.math.Vector2(0, 0),
                          direction = pygame.math.Vector2(0,-1),
                          color = BLUE
                ) )
        return hud

    def collect_dust(self, dust):
        self.collect_sound.play()
        self.collected_dust += dust.value
