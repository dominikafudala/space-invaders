import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, color, score):
        super(Alien, self).__init__()
        self.image = pygame.image.load('img/alien_' + color + '.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.score = score

    def update(self, offset):
        self.rect.x += offset
