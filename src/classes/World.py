import copy
import random
import math
import threading
import pygame
from pygame.locals import *
from src.Constants import *
from src.classes.Stone import Stone
from src.classes.EnemySpaceship import EnemySpaceship
from src.classes.Explosion import Explosion
from src.classes.SpaceshipWreckage import SpaceshipWreckage
from src.classes.BlueDust import BlueDust
from src.classes.GreenDust import GreenDust
from src.classes.TexturedObject import TexturedObject
from src.classes.SoundManager import SOUND_MANAGER

pygame.init()

class World(TexturedObject):
    def __init__(self, player, spaceship = None):
        self.pos = WORLD_POS
        self.size = WORLD_SIZE
        TexturedObject.__init__(self, pos = self.pos, size = self.size, background = WORLD_BACKGROUND)
        self.background = copy.copy(self.image)
        self.all_sprites_lock = threading.Lock()
        self.player = player
        self.spaceship = spaceship
        self.stones = pygame.sprite.LayeredDirty()
        self.enemy_spaceships = pygame.sprite.LayeredDirty()
        self.spaceship_wreckages = pygame.sprite.LayeredDirty()
        self.shots = pygame.sprite.LayeredDirty()
        self.effects = pygame.sprite.LayeredDirty()
        self.dust = pygame.sprite.LayeredDirty()
        self.all_objects = pygame.sprite.LayeredDirty()
        global SOUND_MANAGER
        SOUND_MANAGER.load_sound(EXPLOSION_SOUND, EXPLOSION_VOLUME)

    def set_spaceship(self, spaceship):
        if not self.spaceship is None:
            self.spaceship.kill()
        self.spaceship = spaceship
        self.all_sprites_lock.acquire()
        self.all_objects.add(spaceship, layer = SPACESHIP_LAYER)
        self.all_sprites_lock.release()
        
    def generate_stone(self):
        pos = pygame.math.Vector2( random.randint( 0, self.rect.width -50), 0)
        stone = Stone( pos = pos , level = random.randint(1, MAX_STONE_LEVEL) )
        if not pygame.sprite.spritecollideany(stone, self.stones):
            self.add_stone( stone )
            
    def generate_explosion(self, pos):
        global SOUND_MANAGER
        SOUND_MANAGER.play_sound( EXPLOSION_SOUND )
        explosion = Explosion()
        explosion.rect.center = pos
        self.add_explosion(explosion)    
    
    def generate_dust(self, pos, level):
        if random.randint(1, int(1 / CHANCE_GREEN_DUST[level])) == 1:
            dust = GreenDust()
        else:
            dust = BlueDust()
        dust.set_pos(pygame.math.Vector2(pos))
        self.add_dust(dust)
        
    def generate_enemy_spaceship(self):
        pos = pygame.math.Vector2( random.randint( 0, self.rect.width -50), 0)
        enemy_spaceship = EnemySpaceship( pos = pos )
        if not pygame.sprite.spritecollideany(enemy_spaceship, self.enemy_spaceships):
            self.add_enemy_spaceship( enemy_spaceship )
        
    def generate_spaceship_wreckage(self, center):
        self.add_spaceship_wreckage([ SpaceshipWreckage( img = SPACESHIP_WRECKAGE_IMAGE, pos = center, direction = pygame.math.Vector2(0, 0.5)) ])
        self.add_spaceship_wreckage([ SpaceshipWreckage( img = SPACESHIP_WRECKAGE_IMAGE, pos = center, direction = pygame.math.Vector2(0, 1.5)) ])        
        self.add_spaceship_wreckage([ SpaceshipWreckage( img = SPACESHIP_WRECKAGE_IMAGE, pos = center, direction = pygame.math.Vector2(-1, 1.5)) ])
        self.add_spaceship_wreckage([ SpaceshipWreckage( img = SPACESHIP_WRECKAGE_IMAGE, pos = center, direction = pygame.math.Vector2(1, 1.5)) ])
        
    def add_stone(self, stone):
        self.stones.add(stone, layer = STONE_LAYER)
        self.all_sprites_lock.acquire()
        self.all_objects.add(stone, layer = STONE_LAYER)
        self.all_sprites_lock.release()
    
    def add_shot(self, shots):
        for shot in shots:
            self.shots.add(shot, layer = SHOT_LAYER)
            self.all_sprites_lock.acquire()
            self.all_objects.add(shot, layer = SHOT_LAYER)
            self.all_sprites_lock.release()
        
    def add_explosion(self, explosion):
        self.effects.add(explosion, layer = EFFECT_LAYER)
        self.all_sprites_lock.acquire()
        self.all_objects.add(explosion, layer = EFFECT_LAYER)
        self.all_sprites_lock.release()
    
    def add_spaceship_wreckage(self, wreckage):
        self.spaceship_wreckages.add( wreckage )
        self.all_sprites_lock.acquire()
        self.all_objects.add(wreckage, layer = SPACESHIP_LAYER)
        self.all_sprites_lock.release()
        
    def add_dust(self, dust):
        self.dust.add(dust, layer = DUST_LAYER)
        self.all_sprites_lock.acquire()
        self.all_objects.add(dust, layer = DUST_LAYER)
        self.all_sprites_lock.release()
        
    def add_enemy_spaceship(self, enemy_spaceship):
        self.enemy_spaceships.add(enemy_spaceship)
        self.all_sprites_lock.acquire()
        self.all_objects.add(enemy_spaceship, layer = SPACESHIP_LAYER)
        self.all_sprites_lock.release()
    
    def clear(self):
        self.all_sprites_lock.acquire()
        self.all_objects.clear(self.image, self.background)
        self.all_sprites_lock.release()
        
    def update(self, frame_time):
        old_rects = []
        for sprite in self.dust:
            sprite.follow_pos(self.spaceship.rect.center)
        self.all_sprites_lock.acquire()
        for sprite in self.all_objects.sprites():
            old_rects += sprite.update(frame_time)
        self.all_sprites_lock.release()
        if self.spaceship.rect.left < 0:
            self.spaceship.rect.left = 0
        if self.spaceship.rect.right > self.rect.width:
            self.spaceship.rect.right = self.rect.width
        
        for effect in self.effects.sprites():
            if effect.counter >= effect.max_counter:
                effect.kill()
        
        self.all_sprites_lock.acquire()
        for sprite in self.all_objects.sprites():
            if not self.rect.colliderect(sprite.rect):
                sprite.kill()
        self.all_sprites_lock.release()
        return old_rects
    
	# does not collide objects, if spaceship collides with stones..
    def collide_objects(self):
        for group in [self.stones, self.enemy_spaceships, self.spaceship_wreckages]:
            if pygame.sprite.spritecollide(self.spaceship, group, True):
                return self.spaceship.handle_collision()
        else:
            for group in (self.shots, self.spaceship_wreckages):
                exploding_stones = pygame.sprite.groupcollide(self.stones, group, True, True)
                for stone in exploding_stones.keys():
                    self.generate_explosion(stone.rect.center)
                    self.generate_dust(stone.rect.center, stone.level)
            
            for group in (self.shots, self.spaceship_wreckages):
                exploding_enemy_spaceships = pygame.sprite.groupcollide(self.enemy_spaceships, group, True, True)
                for enemy_spaceship in exploding_enemy_spaceships.keys():
                    self.generate_explosion(enemy_spaceship.rect.center)
                    self.generate_spaceship_wreckage(enemy_spaceship.rect.center)
                
            exploding_wreckages = pygame.sprite.groupcollide(self.spaceship_wreckages, self.shots, True, True)
            for exploding_wreckage in exploding_wreckages.keys():
                self.generate_explosion(exploding_wreckage.rect.center)
                
            collected_dust = pygame.sprite.spritecollide(self.spaceship, self.dust, True)
            for dust in collected_dust:
                self.player.collect_dust(dust)
                self.spaceship.collect_dust(dust)
            return False

    def draw(self, screen):
        self.all_sprites_lock.acquire()
        drawn_rects = self.all_objects.draw(self.image)
        self.all_sprites_lock.release()
        for i in range(len(drawn_rects)):
            pos = [ drawn_rects[i].left + self.rect.left , drawn_rects[i].top + self.rect.top ]
            screen.blit(self.image, pos, drawn_rects[i])
            drawn_rects[i].topleft = pos
        return drawn_rects


# pygame.sprite.groundcollide(group1, group2, dokill1, dokill2, collided = None)
# collided = collide_mask -> True / False
#pygame.sprite.collide_mask(sprite1, sprite2) -> point / None
