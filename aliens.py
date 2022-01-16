import pygame
from alien import Alien
from random import choice
from laser import Laser


class Aliens:
    def __init__(self):
        self.aliens = pygame.sprite.Group()
        self.offset = 2
        self.lasers = pygame.sprite.Group()

    def create_aliens(self, num_rows=5, num_columns=8, x_offset=50, y_offset=40, start_x=20, start_y=20):
        for ind_r, r in enumerate(range(num_rows)):
            for ind_c, c in enumerate(range(num_columns)):
                x = ind_c * x_offset + start_x
                y = ind_r * y_offset + start_y
                if ind_r == 0:
                    alien = Alien(x, y, 'red', 30)
                elif ind_r == 1 or ind_r == 2:
                    alien = Alien(x, y, 'blue', 20)
                else:
                    alien = Alien(x, y, 'white', 10)
                self.aliens.add(alien)

    def draw_aliens(self, window):
        self.aliens.draw(window)

    def change_position_y(self):
        if self.aliens.sprites():
            for alien in self.aliens.sprites():
                alien.rect.y += 2

    def check_position_x(self, screen_width):
        for alien in self.aliens.sprites():
            if alien.rect.right >= screen_width - 20:
                self.offset = -2
                self.change_position_y()
            elif alien.rect.left <= 20:
                self.offset = 2
                self.change_position_y()

    def attack(self, screen_height):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            self.lasers.add(Laser(random_alien.rect.center, screen_height, 10))

    def update(self):
        self.lasers.update()
        self.aliens.update(self.offset)
