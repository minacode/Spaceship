import pygame
from src.Constants import *

class ImageManager():
	def __init__(self):
		self.images = {}

	def search_image(self, path):
		try:
			return self.images[path]
		except:
			return None

	def load_image(self, path):
		image = self.search_image(path)
		if image == None:
			image = pygame.image.load(PATH_IMAGES + path).convert()
			self.images.update( { path : image } )
		return image

IMAGE_MANAGER = ImageManager()
