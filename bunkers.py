import pygame
from bunker import Bunker


class Bunkers:
    def __init__(self):
        self.bunkers = pygame.sprite.Group()

    def create_bunkers(self, x_offset, y_offset, window_width):
        x_offset_new = x_offset
        while x_offset_new <= window_width:
            bunker = Bunker()
            if x_offset_new + self.get_bunker_width(bunker) >= window_width:
                break
            bunker.create_bunker(x_offset_new, y_offset)
            self.bunkers.add(bunker.bunker)
            x_offset_new = x_offset_new + x_offset + self.get_bunker_width(bunker)

    def draw_bunkers(self, window):
        self.bunkers.draw(window)


    def get_bunker_width(self, bunker):
        max_width = 0

        for ind_r, r in enumerate(bunker.grid):
            for ind_c, c in enumerate(r):
                if ind_c > max_width:
                    max_width = ind_c

        return (max_width + 1) * bunker.chunk_size
