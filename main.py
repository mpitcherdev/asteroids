	
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	# groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	# containers
	Asteroid.containers = (asteroids, updatable, drawable)
	Player.containers = (updatable, drawable)
	AsteroidField.containers = (updatable,)
	Shot.containers = (shots, updatable, drawable)
	asteroid_field = AsteroidField()

	player_obj = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		updatable.update(dt)

		for asteroid in asteroids:
			if asteroid.collision(player_obj):  # If collision is detected
				print("Game over!")
				sys.exit()  # Exit the program\
		
			# Check collisions between asteroids and bullets
			for shot in shots:  # Loop over all shots in the shots group
				if asteroid.collision(shot):  # If an asteroid collides with a shot
					asteroid.split()  # Remove asteroid
					shot.kill()      # Remove shot
		
		screen.fill("black")
		for obj in drawable:
			obj.draw(screen)
		pygame.display.flip()
		
		# 60 fps limit
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
