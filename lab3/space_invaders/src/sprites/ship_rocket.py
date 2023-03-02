import pygame
from pygame.sprite import Sprite
from math import sqrt

# BASE_DIR = '/Users/glebchanskiy/subjects/pivo/sem4/lab3/'


class Rocket(Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings

        self.counter = 0

        self.sprite = pygame.image.load(game.GAME_DIR + '/sprites/ship/shot/rocket.png')
        sprite_width, sprite_height = self.sprite.get_size()

        self.sprite = pygame.transform.scale(
            self.sprite, (sprite_width * 0.03, sprite_height * 0.03))

        # Создание снаряда в позиции (0,0) и назначение правильной позиции.
        self.rect = self.sprite.get_rect()

        self.rect.midtop = game.ship.rect.midtop
        # Позиция снаряда хранится в вещественном формате.
        # self.y = float(self.rect.y)

    def update(self):
        dist = 100000
        target = None
        for alien in self.game.aliens:
            if sqrt(pow(abs(alien.rect.x - self.rect.x), 2) +  pow(abs(alien.rect.y - self.rect.y), 2)) < dist:
                target = alien

        if target.rect.x > self.rect.x:
            self.rect.x += sqrt(abs(self.game.ship.rect.x - self.rect.x))
        else:
            self.rect.x -= sqrt(abs(self.game.ship.rect.x - self.rect.x))

        self.rect.y -= self.settings.bullet_speed

    def blitme(self):
        # pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.sprite, self.rect)
