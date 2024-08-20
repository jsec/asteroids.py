import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # noqa: F405

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    screen.fill("black")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()

        delta = clock.tick(60)
        dt = delta / 1000

        player.draw(screen)


if __name__ == "__main__":
    main()
