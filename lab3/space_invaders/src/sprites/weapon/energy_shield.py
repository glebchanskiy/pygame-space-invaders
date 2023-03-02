import pygame
from lab3.space_invaders.src.sprites.weapon.weapon import Weapon


class EnergyShield(Weapon):
    def __init__(self, game, enemy):
        super().__init__(game, enemy)

        self.counter = 0
        self.last = 100
        self.reload = 200

        self.part1 = pygame.image.load(
            self.game.GAME_DIR + '/sprites/energy_shield/1.png')
        self.part2 = pygame.image.load(
            self.game.GAME_DIR + '/sprites/energy_shield/2.png')
        self.part3 = pygame.image.load(
            self.game.GAME_DIR + '/sprites/energy_shield/3.png')

        sprite_width, sprite_height = self.part1.get_size()

        self.part1 = pygame.transform.scale(
            self.part1, (sprite_width * 1, sprite_height * 1))
        self.part2 = pygame.transform.scale(
            self.part2, (sprite_width * 1, sprite_height * 1))
        self.part3 = pygame.transform.scale(
            self.part3, (sprite_width * 1, sprite_height * 1))

        self.image = self.part1
        self.rect = self.image.get_rect()

    def update(self):
        if self.counter == 0:
            self.image = self.part1
        if self.counter == 5:
            self.image = self.part2
        if self.counter == 10:
            self.image = self.part3
        if self.counter == self.last-10:
            self.image = self.part2
        if self.counter == self.last-5:
            self.image = self.part1

        self.counter += 1
        x, y = self.enemy.rect.center
        self.rect.center = x, y+50

    def blitme(self):
        self.screen.blit(self.image, self.rect)
