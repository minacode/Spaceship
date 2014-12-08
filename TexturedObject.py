import pygame
from Constants import *

pygame.init()

class TexturedObject(pygame.sprite.DirtySprite):
    def __init__(self, size = pygame.math.Vector2(1,1), pos = pygame.math.Vector2(0,0), img = None, background = WHITE):
        pygame.sprite.DirtySprite.__init__(self)
        # create image
        self.image = pygame.Surface(size)
        self.texture = img
        self.background = background
        self.set_texture(self.texture)
        self.rect = self.image.get_rect(topleft = pos)
        
    def set_texture(self, texture):
        if texture == None:
            self.image.fill(self.background)
        else:
            texture = pygame.image.load(PATH_IMAGES + texture).convert()
            texture_w = texture.get_width()
            texture_h = texture.get_height()
            img_w = self.image.get_width()
            img_h = self.image.get_height()
            w = 0
            while w <= img_w:
                h = 0
                while h <= img_h:
                    self.image.blit(texture, (w,h))
                    h += texture_h
                w += texture_w
