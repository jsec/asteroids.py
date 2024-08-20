from __future__ import annotations
import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def collision_check(self, sprite: CircleShape):
        distance = self.position.distance_to(sprite.position)
        return distance < self.radius + sprite.radius
