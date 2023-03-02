import pygame
from pygame.sprite import Sprite
from math import sqrt


class Rocket(Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings

        self.counter = 0

        self.sprite = pygame.image.load(
            game.GAME_DIR + '/sprites/ship/shot/rocket.png')
        sprite_width, sprite_height = self.sprite.get_size()

        self.sprite = pygame.transform.scale(
            self.sprite, (sprite_width * 0.03, sprite_height * 0.03))

        self.rect = self.sprite.get_rect()
        self.rect.midtop = game.ship.rect.midtop

    def update(self):
        dist = 100000
        target = None
        for alien in self.game.aliens:
            if sqrt(pow(abs(alien.rect.x - self.rect.x), 2) + pow(abs(alien.rect.y - self.rect.y), 2)) < dist:
                target = alien

        if target.rect.x > self.rect.x:
            self.rect.x += sqrt(abs(self.game.ship.rect.x - self.rect.x))
        else:
            self.rect.x -= sqrt(abs(self.game.ship.rect.x - self.rect.x))

        self.rect.y -= self.settings.bullet_speed

    def blitme(self):
        self.screen.blit(self.sprite, self.rect)
