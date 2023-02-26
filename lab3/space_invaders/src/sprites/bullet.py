import pygame
from pygame.sprite import Sprite

# BASE_DIR = '/Users/glebchanskiy/subjects/pivo/sem4/lab3/'


class Bullet(Sprite):

    def __init__(self, game):

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings


        self.counter = 0

        self.sprite = pygame.image.load(game.GAME_DIR + '/sprites/ship/shot/blaster_shot.png')

        # Создание снаряда в позиции (0,0) и назначение правильной позиции.
        self.rect = self.sprite.get_rect()

        self.rect.midtop = game.ship.rect.midtop
        # Позиция снаряда хранится в вещественном формате.
        self.y = float(self.rect.y)

    def update(self):

        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def blitme(self):
        # pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.sprite, self.rect)
