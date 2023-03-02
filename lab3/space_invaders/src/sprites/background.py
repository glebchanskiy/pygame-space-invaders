import pygame


class Background:
    def load_bg(self, game_path):

        bgs = ['Clouds 1', 'Clouds 2', 'Clouds 3', 'Clouds 4',
               'Clouds 5', 'Clouds 6', 'Clouds 7', 'Clouds 8']

        sprites = []
        sprites_rects = []

        for bg in bgs:
            sprite1 = pygame.image.load(
                f'{game_path}/sprites/backgrounds/{bg}/1.png')
            sprite2 = pygame.image.load(
                f'{game_path}/sprites/backgrounds/{bg}/2.png')
            sprite3 = pygame.image.load(
                f'{game_path}/sprites/backgrounds/{bg}/3.png')
            sprite4 = pygame.image.load(
                f'{game_path}/sprites/backgrounds/{bg}/4.png')

            width, height = sprite1.get_size()
            width *= 2.6
            height *= 2.6

            sprite1 = pygame.transform.scale(sprite1, (width, height))
            sprite2 = pygame.transform.scale(sprite2, (width, height))
            sprite3 = pygame.transform.scale(sprite3, (width, height))
            sprite4 = pygame.transform.scale(sprite4, (width, height))

            sprites.append(
                (sprite1, sprite2, sprite3, sprite4)
            )

            sprites_rects.append(
                (sprite1.get_rect(),
                 sprite2.get_rect(),
                 sprite3.get_rect(),
                 sprite4.get_rect())
            )

        return (
            sprites,
            sprites_rects
        )

    def __init__(self, game, ship) -> None:
        self.settings = game.settings
        self.screen = game.screen
        self.ship = ship
        self.screen_rect = game.screen.get_rect()

        self.sprites, self.sprites_rects = self.load_bg(game.GAME_DIR)

        self.sprite = self.sprites[0]
        self.sprite_rect = self.sprites_rects[0]

        self.width, self.height = self.sprite[0].get_size()
        self.width *= 2.6
        self.height *= 2.6

        for part in self.sprite_rect:
            part.midbottom = self.screen_rect.midbottom

        self.www = self.width / self.settings.screen_width
        self.hhh = self.height / self.settings.screen_height

    def update(self):
        count = 3
        for rect in self.sprite_rect:

            x_speed, y_speed = self.ship.rect.midbottom

            sprite_x_speed, sprite_y_speed = rect.midbottom
            if count == 0:
                sprite_x_speed = self.www * (x_speed / 13) + 450
                sprite_y_speed = self.hhh * (y_speed / 20) + 790
            elif count == 1:
                sprite_x_speed = self.www * (x_speed / 16) + 450
                sprite_y_speed = self.hhh * (y_speed / 30) + 790
            elif count == 2:
                sprite_x_speed = self.www * (x_speed / 20) + 450
                sprite_y_speed = self.hhh * (y_speed / 40) + 790
            elif count == 3:
                sprite_x_speed = self.www * (x_speed / 100) + 450
                sprite_y_speed = self.hhh * (y_speed / 100) + 790

            rect.midbottom = sprite_x_speed, sprite_y_speed
            count -= 1

    def blitme(self):
        self.screen.blit(self.sprite[0], self.sprite_rect[0])
        self.screen.blit(self.sprite[1], self.sprite_rect[1])
        self.screen.blit(self.sprite[2], self.sprite_rect[2])
        self.screen.blit(self.sprite[3], self.sprite_rect[3])

    def change_bg(self, index):
        self.sprite = self.sprites[index]
        self.sprite_rect = self.sprites_rects[index]
