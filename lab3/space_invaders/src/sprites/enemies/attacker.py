import pygame
from lab3.space_invaders.src.sprites.enemies.enemy import Enemy
from lab3.space_invaders.src.sprites.weapon.blaster import Blaster

class Attacker(Enemy):
    def __init__(self, game, color):
        super().__init__(game, Blaster(game, self))

        self.cost = self.settings.attacker_cost
        self.image = pygame.image.load(game.GAME_DIR + f'/sprites/aliens/{color}/2.png')
        
        width, height = self.image.get_size()
        width *= 0.7
        height *= 0.7
        self.image = pygame.transform.scale(self.image, (width, width))
        self.rect = self.image.get_rect()

    def ability(self):
        self.game.blaster_sound.play()
        self.weapon = Blaster(self.game, self)
        self.weapon.rect.center = self.rect.center