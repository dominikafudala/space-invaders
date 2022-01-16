import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, max_height, dir_laser):
        super(Laser, self).__init__()
        self.image = pygame.image.load('img/laser.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.max_height = max_height
        self.dir_laser = dir_laser

    def update(self):
        self.rect.y += self.dir_laser
        if self.rect.y <= 0 or self.rect.y >= self.max_height - 50:
            self.kill()
