from src.classes.Shot import Shot
from src.Constants import *

class SpaceshipWreckage(Shot):
	def __init__(self, img = SPACESHIP_WRECKAGE_IMAGE, pos = pygame.math.Vector2(0,0), direction = pygame.math.Vector2(0,-1), v = None):
		if v is None:
			v = direction * SPACESHIP_WRECKAGE_SPEED
		Shot.__init__(self, img, pos = pos, direction = direction, v = v)
