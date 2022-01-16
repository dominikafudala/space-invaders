import pygame
from laser import Laser


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, max_width, change):
        super(Player, self).__init__()
        self.image = pygame.image.load('img/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.change = change
        self.max_width = max_width
        self.shoot_laser_recharge = 800
        self.shoot_laser_time = -self.shoot_laser_recharge
        self.lasers = pygame.sprite.Group()
        self.hearts = 3
        self.heart_img = pygame.image.load('img/player.png').convert_alpha()
        self.font = pygame.font.SysFont(None, 50)
        self.score = 0

    def update(self):
        self.check_pressed_key()
        self.lasers.update()

    def check_pressed_key(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.update_pos(-self.change)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.update_pos(self.change)
        elif keys[pygame.K_SPACE] and self.check_laser_availability():
            self.attack()

    def update_pos(self, change):
        self.rect.x += change
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= self.max_width:
            self.rect.right = self.max_width

    def attack(self):
        self.lasers.add(Laser(self.rect.center, self.max_width, -10))

    def check_laser_availability(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.shoot_laser_time >= self.shoot_laser_recharge:
            self.shoot_laser_time = pygame.time.get_ticks()
            return True
        else:
            return False

    def decrease_hearts(self):
        if self.hearts:
            self.hearts -= 1

    def display_hearts_score(self, window, height):
        hearts_area = self.font.render(str(self.hearts), True, 'white')
        window.blit(hearts_area, (10, height - 35))
        for heart in range(self.hearts):
            x = hearts_area.get_size()[0] + 20 + heart * (self.heart_img.get_size()[0] + 10)
            window.blit(self.heart_img, (x, height - 50))

        score_area = self.font.render(f'score: {self.score}', True, 'white')
        window.blit(score_area, (height - 20 - score_area.get_size()[0], height - 35))

    def update_score(self, val):
        self.score += val

