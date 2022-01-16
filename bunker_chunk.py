import pygame


class BunkerChunk(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super(BunkerChunk, self).__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=(x, y))