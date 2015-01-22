import pygame
from src.Constants import *

class SoundManager():
	def __init__(self):
		self.sounds = {}
		self.music = {}
		
	def load_sound(self, sound_name, volume):
		sound = pygame.mixer.Sound( SOUND_PATH + sound_name )
		sound.set_volume( volume )
		self.sounds.update( { sound_name : sound } )
		
	def play_sound(self, sound_name):
		self.sounds[sound_name].play()
		
	def play_music(self, music_id, volume):
		music_path = SOUND_PATH + music_id
		pygame.mixer.music.load( music_path )
		pygame.mixer.music.set_volume( volume )
		pygame.mixer.music.play( loops = -1)
		
		
SOUND_MANAGER = SoundManager()
