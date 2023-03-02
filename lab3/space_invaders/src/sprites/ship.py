import pygame


class Ship:
    def __init__(self, game) -> None:
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.sprite_base = pygame.image.load(
            game.GAME_DIR + '/sprites/ship/starship.png')
        self.sprite_turn_right = [
            pygame.image.load(game.GAME_DIR + '/sprites/ship/turn_r_1.png'),
            pygame.image.load(game.GAME_DIR + '/sprites/ship/turn_r_2.png'),
            pygame.image.load(game.GAME_DIR + '/sprites/ship/turn_r_3.png'),
            pygame.image.load(game.GAME_DIR + '/sprites/ship/turn_r_4.png'),
        ]
        self.sprite_turn_left = [
            pygame.image.load(game.GAME_DIR + '/sprites/ship/turn_l_1.png'),
            pygame.image.load(game.GAME_DIR + '/sprites/ship/turn_l_2.png'),
            pygame.image.load(game.GAME_DIR + '/sprites/ship/turn_l_3.png'),
            pygame.image.load(game.GAME_DIR + '/sprites/ship/turn_l_4.png'),
        ]

        sprite_width, sprite_height = self.sprite_base.get_size()
        self.sprite = pygame.transform.scale(
            self.sprite_base, (sprite_width * 0.8, sprite_height * 0.8))

        self.rect = self.sprite.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_up = False
        self.moving_down = False

        self.moving_right = False
        self.moving_left = False

        self.moving_time = 0

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > (self.screen_rect.top + 600):
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom - 50:
            self.y += self.settings.ship_speed

        self.rect.y = self.y
        self.rect.x = self.x

        if self.moving_right:
            if self.moving_time == 1:
                self.sprite = self.sprite_turn_right[0]
            if self.moving_time == 3:
                self.sprite = self.sprite_turn_right[1]
            if self.moving_time == 6:
                self.sprite = self.sprite_turn_right[2]
            if self.moving_time < 6:
                self.moving_time += 1
        elif self.moving_left:
            if self.moving_time == -1:
                self.sprite = self.sprite_turn_left[0]
            if self.moving_time == -3:
                self.sprite = self.sprite_turn_left[1]
            if self.moving_time == -6:
                self.sprite = self.sprite_turn_left[2]
            if self.moving_time > -6:
                self.moving_time -= 1
        else:
            if self.moving_time > 0:
                self.moving_time -= 1
            elif self.moving_time < 0:
                self.moving_time += 1
            else:
                self.sprite = self.sprite_base

    def blitme(self):
        self.screen.blit(self.sprite, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
