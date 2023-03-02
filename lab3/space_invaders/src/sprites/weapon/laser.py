import pygame
from lab3.space_invaders.src.sprites.weapon.weapon import Weapon


# BASE_DIR = '/Users/glebchanskiy/subjects/pivo/sem4/lab3/'


class Laser(Weapon):
    def __init__(self, game, enemy):
        super().__init__( game, enemy)

        self.counter = 0
        self.last = 30
        self.reload = 700

        self.image = pygame.image.load(self.game.GAME_DIR + '/sprites/laser/laser.png')
        

        sprite_width, sprite_height = self.image.get_size()

        self.image = pygame.transform.scale(self.image, (sprite_width * 0.8, sprite_height * 0.8))
        self.rect = self.image.get_rect()

        # self.rect.x = enemy.rect.x
        self.y = self.rect.y
        self.x = self.rect.x
        
        
        

       

    def update(self):
        self.rect.midtop = self.enemy.rect.midbottom
        self.counter += 1


    def blitme(self):
        self.screen.blit(self.image, self.rect)
