import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # noqa: F405

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    updatable.add(player)
    drawable.add(player)

    while True:
        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()

        delta = clock.tick(60)
        dt = delta / 1000

        for sprite in updatable:
            sprite.update(dt)


if __name__ == "__main__":
    main()
