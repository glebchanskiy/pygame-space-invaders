import pygame
from lab3.space_invaders.src.sprites.enemies.enemy import Enemy
from lab3.space_invaders.src.sprites.weapon.rocket import Rocket


class Rocketer(Enemy):
    def __init__(self, game, color):
        super().__init__(game, Rocket(game, self))

        self.cost = self.settings.rocketer_cost
        self.image = pygame.image.load(game.GAME_DIR + f'/sprites/aliens/{color}/4.png')
        
        width, height = self.image.get_size()
        width *= 0.9
        height *= 0.9
        self.image = pygame.transform.scale(self.image, (width, width))
        self.rect = self.image.get_rect()

    def ability(self):
        self.game.rocket_sound.play()
        self.weapon = Rocket(self.game, self)
        self.weapon.rect.center = self.rect.center