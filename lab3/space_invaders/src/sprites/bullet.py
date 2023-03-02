import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.counter = 0

        self.sprite = pygame.image.load(
            game.GAME_DIR + '/sprites/ship/shot/blaster_shot.png')

        self.rect = self.sprite.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):

        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.sprite, self.rect)
