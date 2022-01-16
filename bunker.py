import pygame
from bunker_chunk import BunkerChunk


class Bunker:
    def __init__(self):
        self.grid = [
            ' xxxxxxxxx ',
            'xxxxxxxxxxx',
            'xxxxxxxxxxx',
            'xxxx   xxxx',
            'xxxx   xxxx'
        ]

        self.chunk_size = 5
        self.bunker = pygame.sprite.Group()

    def create_bunker(self, x_offset, y_offset):
        # enumerate grid to get position
        for ind_r, r in enumerate(self.grid):
            for ind_c, c in enumerate(r):
                if c == 'x':
                    chunk = BunkerChunk(self.chunk_size, x_offset + ind_c * self.chunk_size,
                                        y_offset + ind_r * self.chunk_size)
                    self.bunker.add(chunk)
