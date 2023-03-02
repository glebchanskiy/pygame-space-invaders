import pygame
from lab3.space_invaders.src.sprites.enemies.enemy import Enemy
from lab3.space_invaders.src.sprites.weapon.laser import Laser


class Dreadnought(Enemy):
    def __init__(self, game, color):
        super().__init__(game, Laser(game, self))

        self.cost = self.settings.dreadnought_cost
        self.image = pygame.image.load(game.GAME_DIR + f'/sprites/aliens/{color}/3.png')
        
        width, height = self.image.get_size()
        width *= 0.8
        height *= 0.8
        self.image = pygame.transform.scale(self.image, (width, width))
        self.rect = self.image.get_rect()

    def ability(self):
        self.game.laser_sound.play()
        self.weapon = Laser(self.game, self)
        self.weapon.rect.center = self.rect.center
