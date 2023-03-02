from pygame.sprite import Sprite


class Weapon(Sprite):
    def __init__(self, game, enemy):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.game = game
        self.enemy = enemy

        self.counter = 0
        self.last = 30
        