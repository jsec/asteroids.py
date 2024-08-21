import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        first_child_vector = self.velocity.rotate(angle)
        second_child_vector = self.velocity.rotate(-angle)
        child_radius = self.radius - ASTEROID_MIN_RADIUS

        first_child = Asteroid(int(self.position.x), int(self.position.y), child_radius)
        second_child = Asteroid(
            int(self.position.x), int(self.position.y), child_radius
        )

        first_child.velocity = first_child_vector * 1.2
        second_child.velocity = second_child_vector * 1.2
