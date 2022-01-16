import pygame
import sys
from player import Player
from bunkers import Bunkers
from aliens import Aliens


class Game:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.player = pygame.sprite.GroupSingle(
            Player(
                (window_width / 2.0, window_height - 50.0),
                window_width,
                window_width / 50.0
            )
        )

        self.bunkers = Bunkers()
        self.bunkers.create_bunkers(window_width / 8.0, 450, window_width)

        self.aliens = Aliens()
        self.aliens.create_aliens()

        self.font = pygame.font.SysFont(None, 150)

        self.lost = False

    def alien_attack(self):
        self.aliens.attack(self.window_height)

    def collision(self, window):
        # check collision player laser
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                if pygame.sprite.spritecollide(laser, self.bunkers.bunkers, True):
                    laser.kill()

                alien_hit = pygame.sprite.spritecollide(laser, self.aliens.aliens, True)
                if alien_hit:
                    laser.kill()
                    for alien in alien_hit:
                        self.player.sprite.update_score(alien.score)

        # check collision aliens laser
        if self.aliens.lasers:
            for laser in self.aliens.lasers:
                if pygame.sprite.spritecollide(laser, self.bunkers.bunkers, True):
                    laser.kill()

                if pygame.sprite.spritecollide(laser, self.player, False):
                    laser.kill()
                    self.player.sprite.decrease_hearts()

        # collision aliens
        if self.aliens.aliens:
            for alien in self.aliens.aliens:
                pygame.sprite.spritecollide(alien, self.bunkers.bunkers, True)

                if pygame.sprite.spritecollide(alien, self.player, False):
                    self.lost = True

    def run(self, window):
        if self.player.sprite.hearts >= 1 and not self.lost and self.aliens.aliens:
            self.player.update()
            self.aliens.update()
            self.aliens.check_position_x(self.window_width)
            self.collision(window)
            self.redraw(window)
        else:
            if not self.aliens.aliens:
                self.display_end(window, 'You won')
            else:
                self.display_end(window, 'You lost')

    def redraw(self, window):
        if self.player.sprite.hearts >= 1 and not self.lost and self.aliens.aliens:
            self.player.sprite.lasers.draw(window)
            self.player.sprite.display_hearts_score(window, self.window_height)
            self.bunkers.draw_bunkers(window)
            self.player.draw(window)
            self.aliens.draw_aliens(window)
            self.aliens.lasers.draw(window)
        else:
            if not self.aliens.aliens:
                self.display_end(window, 'You won')
            else:
                self.display_end(window, 'You lost')

    def display_end(self, window, text):
        window.fill((0, 0, 0))
        img = self.font.render(text, True, 'white')
        window.blit(img, (self.window_width / 2. - img.get_size()[0]/2., self.window_height / 2. - img.get_size()[1]/2.))

        font_score = pygame.font.SysFont(None, 70)
        score = font_score.render(f'score: {self.player.sprite.score}', True, 'white')
        window.blit(score,
                    (self.window_width / 2. - score.get_size()[0] / 2., self.window_height / 2. - score.get_size()[1] / 2. + img.get_size()[1] ))

