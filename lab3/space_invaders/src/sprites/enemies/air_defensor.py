import pygame
from lab3.space_invaders.src.sprites.enemies.enemy import Enemy
from lab3.space_invaders.src.sprites.weapon.air_laser import AirLaser

class AirDefensor(Enemy):
    def __init__(self, game, color):
        super().__init__(game, AirLaser(game, self))

        self.cost = self.settings.air_defensor_cost
        self.image = pygame.image.load(game.GAME_DIR + f'/sprites/aliens/{color}/5.png')
        
        width, height = self.image.get_size()
        width *= 0.6
        height *= 0.6
        self.image = pygame.transform.scale(self.image, (width, width))
        self.rect = self.image.get_rect()

    def ability(self):
        # self.game.rocket_sound.play()
        self.weapon = AirLaser(self.game, self)
        # self.weapon.rect.center = self.rect.center