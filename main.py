import sys
import pygame
from asteroid_field import AsteroidField
from asteroids import Asteroid
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # noqa: F405
    clock = pygame.time.Clock()
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Asteroid.containers = (updatable_group, drawable_group, asteroid_group)

    Player.containers = (updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    AsteroidField.containers = (updatable_group,)
    asteroid_field = AsteroidField()
    updatable_group.add(asteroid_field)

    Shot.containers = (updatable_group, drawable_group, shot_group)

    while True:
        screen.fill("black")

        for sprite in updatable_group:
            sprite.update(dt)

        for asteroid in asteroid_group:
            if asteroid.collision_check(player):
                print("Game over!")
                sys.exit()

            for shot in shot_group:
                if shot.collision_check(asteroid):
                    shot.kill()
                    asteroid.split()

        for sprite in drawable_group:
            sprite.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()

        delta = clock.tick(60)
        dt = delta / 1000


if __name__ == "__main__":
    main()
