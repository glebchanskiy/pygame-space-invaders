import pygame
from pygame.sprite import Sprite


class Explosion(Sprite):

    def __init__(self, game, cords):

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.counter = 0
        self.last = 20

        self.ex1 = pygame.image.load(
            game.GAME_DIR + '/sprites/explosion/1.png')
        self.ex2 = pygame.image.load(
            game.GAME_DIR + '/sprites/explosion/2.png')
        self.ex3 = pygame.image.load(
            game.GAME_DIR + '/sprites/explosion/3.png')
        self.ex4 = pygame.image.load(
            game.GAME_DIR + '/sprites/explosion/4.png')
        self.ex5 = pygame.image.load(
            game.GAME_DIR + '/sprites/explosion/5.png')
        self.ex6 = pygame.image.load(
            game.GAME_DIR + '/sprites/explosion/6.png')
        self.ex7 = pygame.image.load(
            game.GAME_DIR + '/sprites/explosion/7.png')
        self.ex8 = pygame.image.load(
            game.GAME_DIR + '/sprites/explosion/8.png')
        self.ex9 = pygame.image.load(
            game.GAME_DIR + '/sprites/explosion/9.png')
        self.ex10 = pygame.image.load(
            game.GAME_DIR + '/sprites/explosion/10.png')

        sprite_width, sprite_height = self.ex1.get_size()

        self.ex1 = pygame.transform.scale(
            self.ex1, (sprite_width * 0.2, sprite_height * 0.2))
        self.ex2 = pygame.transform.scale(
            self.ex2, (sprite_width * 0.2, sprite_height * 0.2))
        self.ex3 = pygame.transform.scale(
            self.ex3, (sprite_width * 0.2, sprite_height * 0.2))
        self.ex4 = pygame.transform.scale(
            self.ex4, (sprite_width * 0.2, sprite_height * 0.2))
        self.ex5 = pygame.transform.scale(
            self.ex5, (sprite_width * 0.2, sprite_height * 0.2))
        self.ex6 = pygame.transform.scale(
            self.ex6, (sprite_width * 0.2, sprite_height * 0.2))
        self.ex7 = pygame.transform.scale(
            self.ex7, (sprite_width * 0.2, sprite_height * 0.2))
        self.ex8 = pygame.transform.scale(
            self.ex8, (sprite_width * 0.2, sprite_height * 0.2))
        self.ex9 = pygame.transform.scale(
            self.ex9, (sprite_width * 0.2, sprite_height * 0.2))
        self.ex10 = pygame.transform.scale(
            self.ex10, (sprite_width * 0.2, sprite_height * 0.2))

        self.image = self.ex1
        self.rect = self.ex1.get_rect()
        self.rect.center = cords

    def update(self):
        if self.counter == 0:
            self.image = self.ex1
        if self.counter == 2:
            self.image = self.ex2
        if self.counter == 4:
            self.image = self.ex3
        if self.counter == 6:
            self.image = self.ex4
        if self.counter == 8:
            self.image = self.ex5
        if self.counter == 10:
            self.image = self.ex6
        if self.counter == 12:
            self.image = self.ex7
        if self.counter == 14:
            self.image = self.ex8
        if self.counter == 16:
            self.image = self.ex9
        if self.counter == 18:
            self.image = self.ex10
        if self.counter == 20:
            self.image = self.ex1

        self.counter += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
