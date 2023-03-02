import pygame
from lab3.space_invaders.src.sprites.weapon.weapon import Weapon
from lab3.space_invaders.src.sprites.ship_rocket import Rocket
from math import sqrt

# BASE_DIR = '/Users/glebchanskiy/subjects/pivo/sem4/lab3/'


class AirLaser(Weapon):
    def __init__(self, game, enemy):
        super().__init__( game, enemy)
      
        self.counter = 0
        self.last = 2
        self.reload = 30
        
        self.target = None

    
        # self.rect.x = enemy.rect.x
        # self.y = self.rect.y
        # self.x = self.rect.x
        
        

       

    def update(self):
        # self.rect = self.rect = pygame.draw.line(self.game.screen, (255, 255, 255), self.enemy.rect.center, self.enemy.rect.center, width=1) 
        self.target = self.enemy.rect.center
        self.rect = pygame.draw.line(self.game.screen, (255, 255, 255), self.enemy.rect.center, self.target, width=1)
        if self.game.bullets:
            # self.rect = pygame.draw.line(self.game.screen, (255, 255, 255), self.enemy.rect.center, self.enemy.rect.center, width=1)
            dist = 1000000

            for rocket in self.game.bullets:    
                if type(rocket) is Rocket and rocket.rect.y < 500 and sqrt(pow(abs(rocket.rect.x - self.rect.x), 2) +  pow(abs(rocket.rect.y - self.rect.y), 2)) < dist:   
                    self.target = rocket.rect.center
  
            
        self.counter += 1
        self.rect = pygame.draw.line(self.game.screen, (255, 255, 255), self.enemy.rect.center, self.target, width=1)



    def blitme(self):
        if self.target:
            pygame.draw.line(self.game.screen, (255, 255, 255), self.enemy.rect.center, self.target, width=1)
        # self.screen.blit(self.image, self.rect)
