import pygame
from lab3.space_invaders.src.sprites.enemies.enemy import Enemy
from lab3.space_invaders.src.sprites.weapon.energy_shield import EnergyShield

class Defensor(Enemy):
    def __init__(self, game, color):
        super().__init__(game, EnergyShield(game, self))

        self.cost = self.settings.defensor_cost
        self.image = pygame.image.load(game.GAME_DIR + f'/sprites/aliens/{color}/1.png')

        # self.weapon = 
        
        width, height = self.image.get_size()
        width *= 0.7
        height *= 0.7
        self.image = pygame.transform.scale(self.image, (width, width))
        self.rect = self.image.get_rect()

    def ability(self):
        self.weapon = EnergyShield(self.game, self)
        self.weapon.rect.center = self.rect.center

