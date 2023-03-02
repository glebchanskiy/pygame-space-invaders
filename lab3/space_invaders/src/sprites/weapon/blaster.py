import pygame
from lab3.space_invaders.src.sprites.weapon.weapon import Weapon


# BASE_DIR = '/Users/glebchanskiy/subjects/pivo/sem4/lab3/'


class Blaster(Weapon):
    def __init__(self, game, enemy):
        super().__init__(game, enemy)

        self.screen_rect = game.screen.get_rect()
        self.counter = 0
        self.last = 100
        self.reload = 300

        self.image = pygame.image.load(
            self.game.GAME_DIR + '/sprites/blaster/blaster_shot.png')

        sprite_width, sprite_height = self.image.get_size()

        self.image = pygame.transform.scale(
            self.image, (sprite_width * 1, sprite_height * 1))
        self.rect = self.image.get_rect()

    def update(self):
        # if self.rect.top > self.game.settings.screen_height:
        #     self.rect.center = self.enemy.rect.center

        self.rect.y += self.settings.alien_bullet_speed

        self.counter += 1
   
        if not self.screen_rect.contains(self.rect):
            self.kill()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
