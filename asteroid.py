import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # Draw a circle on the given surface
        # Parameters: surface, color, position, radius, width
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            velocity1 = self.velocity.rotate(random_angle)
            velocity2 = self.velocity.rotate(-random_angle) 
            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            split_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid1.velocity = velocity1 * 1.2
            split_asteroid2.velocity = velocity2 * 1.2
            
            for group in self.groups():
                group.add(split_asteroid1)
                group.add(split_asteroid2)