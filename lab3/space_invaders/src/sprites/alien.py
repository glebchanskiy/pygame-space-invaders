import pygame
from pygame.sprite import Sprite
from random import randint

# BASE_DIR = '/Users/glebchanskiy/subjects/pivo/sem4/lab3/'


class Alien(Sprite):

    def __init__(self, game, ship_type, ship_color):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.group = game.aliens
        self.type = ship_type

        if self.type == 'attack':
            self.image = pygame.image.load(game.GAME_DIR + f'/sprites/aliens/{ship_color}/2.png')
            self.cost = 2
        elif self.type == 'heavy':
            self.image = pygame.image.load(game.GAME_DIR + f'/sprites/aliens/{ship_color}/1.png')
            self.cost = 1
        elif self.type == 'dreadnought':
            self.image = pygame.image.load(game.GAME_DIR + f'/sprites/aliens/{ship_color}/3.png')
            self.cost = 3

        width, height = self.image.get_size()
        width *= 0.8
        height *= 0.8

        self.image = pygame.transform.scale(self.image, (width, width))
        self.rect = self.image.get_rect()

        self.speed = self.settings.alien_speed
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def ability(self):
        # if self.type == 'attack':
        pass


    def update(self):
        if randint(1, 20) == 15:
            self.ability()
        self.x += self.settings.alien_speed * self.settings.fleet_direction

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        # pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.sprite, self.rect)


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        else:
            return False
