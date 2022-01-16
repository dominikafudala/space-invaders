import pygame
import sys
from game import Game

if __name__ == '__main__':
    pygame.init()

    window_width, window_height = 600, 600
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Space Invaders')

    clock = pygame.time.Clock()

    game = Game(window_width, window_height)

    ALIENATTACK = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENATTACK, 700)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == ALIENATTACK:
                game.alien_attack()

        window.fill((0, 0, 0))

        game.run(window)

        pygame.display.flip()
        clock.tick(30)