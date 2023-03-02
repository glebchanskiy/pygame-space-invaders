import pygame
from pygame.sprite import Sprite
from random import randint

from lab3.space_invaders.src.sprites.weapon.weapon import Weapon

# BASE_DIR = '/Users/glebchanskiy/subjects/pivo/sem4/lab3/'


class Enemy(Sprite):
    def __init__(self, game, weapon: Weapon):
        super().__init__()
        self.game = game
        self.weapon = weapon
        

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.group = game.aliens

        self.image = None
        self.rect = pygame.Rect(0, 0, 80, 80)
    
        self.speed = self.settings.current_alien_speed
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.is_ability = False

    def ability(self):
        pass
        

    def update(self):
        
        if self.settings.current_alien_speed != 0:
            if not self.is_ability and randint(1, self.weapon.reload) == 10:
                self.is_ability = True
                # self.weapon.rect.center = self.rect.center
                self.ability()
                self.game.weapons.add(self.weapon)
                
        
        if self.is_ability:
           
            if self.settings.current_alien_speed != 0:
                self.weapon.update()
            
            self.weapon.blitme()
            if self.weapon.counter >= self.weapon.last:          
                self.game.weapons.remove(self.weapon)   
                self.weapon.counter = 0
                self.is_ability = False

        self.x += self.settings.current_alien_speed * self.settings.fleet_direction

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.sprite, self.rect)
            
            


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        else:
            return False
