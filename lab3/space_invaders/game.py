import sys
import os
from random import randint
from time import sleep

import pygame
import pygame_menu
from pygame_menu import sound
from pygame.locals import *


from lab3.space_invaders.src.menu_utils import mytheme
from lab3.space_invaders.src.config.settings import Settings
from lab3.space_invaders.src.config.gamestats import GameStats

from lab3.space_invaders.src.sprites.background import Background
from lab3.space_invaders.src.sprites.ship import Ship
from lab3.space_invaders.src.sprites.bullet import Bullet
from lab3.space_invaders.src.sprites.alien import Alien


class AlienInvasion:

    def __init__(self):
        self.GAME_DIR = os.path.realpath(os.path.dirname(__file__))

        pygame.init()
        pygame.display.set_caption("Alien Invasion")

        self._load_sounds()
        self.settings = Settings()
        self.stats = GameStats(self)

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self._sprites_initializing()
        self._create_fleet()

        self.isTheWARUDO = 1
        self.game_active = True
    
        self.start_menu = None

    def run_game(self):
        self.stats.reset_stats()
        self.start_menu = self._create_start_menu()
        self.start_menu.mainloop(self.screen)

    def end_game(self):
        self._create_end_menu().mainloop(self.screen)

    def loop(self):
        self.start_music.play()
        while True:
            self._check_events()

            if self.game_active:
                self._update_bg()
                self._update_ship()
                self._update_bullets()
                self._update_aliens()
                self._update_message()

            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_w:
            if self.isTheWARUDO == -1:
                pygame.display.set_caption("THEE WARUUDOOO")
                self.settings.alien_speed = 0
                self.settings.bullet_speed = 0
            elif self.isTheWARUDO == 1:
                pygame.display.set_caption("Alien Invasion")
                self.settings.alien_speed = 4
                self.settings.bullet_speed = 10
            self.isTheWARUDO = -self.isTheWARUDO
        elif event.key == pygame.K_1:
            self.background.change_bg(0)
        elif event.key == pygame.K_2:
            self.background.change_bg(1)
        elif event.key == pygame.K_3:
            self.background.change_bg(2)
        elif event.key == pygame.K_4:
            self.background.change_bg(3)
        elif event.key == pygame.K_5:
            self.background.change_bg(4)
        elif event.key == pygame.K_6:
            self.background.change_bg(5)
        elif event.key == pygame.K_7:
            self.background.change_bg(6)
        elif event.key == pygame.K_8:
            self.background.change_bg(7)
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_bg(self):
        self.background.blitme()
        self.background.update()

    def _update_ship(self):
        self.ship.update()
        self.ship.blitme()

    def _update_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self.bullets.update()

        for bullet in self.bullets.sprites():
            bullet.blitme()

        self._check_bullet_alien_collisions()

    def _update_aliens(self):
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()
        self._check_fleet_edges()

        self.aliens.update()
        self.aliens.draw(self.screen)

    def _update_message(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render(
            f'Score: {self.stats.score}', True, (255, 255, 255))
        wave_text = font.render(
            f'Wave {self.stats.wave}', True, (255, 255, 255))

        self.screen.blit(score_text, (10, 10))
        self.screen.blit(wave_text, (10, 40))

    def _update_screen(self):
        pygame.display.update()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        for groups in collisions.values():
            self.explousion_sound.play()
            for alien in groups:
                self.stats.score += alien.cost

        if not self.aliens:
            self._new_wave()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            self.blaster_sound.play()
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def _new_wave(self):
        self.stats.wave += 1
        self.settings.alien_speed += self.settings.difficulty_coof
        self.settings.fleet_drop_speed += self.settings.difficulty_coof
        self.background.change_bg(randint(0, 7))

        self.bullets.empty()
        self._create_fleet()

    def _create_fleet(self):
        """Создание флота вторжения."""
        # Создание пришельца.
        for row_number in range(3):
            for alien_number in range(5):
                self._create_alien(alien_number, row_number, 'green')

    def _create_alien(self, alien_number, row_number, color):
        if row_number == 0:
            alien = Alien(self, 'dreadnought', color)
        elif row_number == 1:
            alien = Alien(self, 'attack', color)
        elif row_number == 2:
            alien = Alien(self, 'heavy', color)

        alien_width, alien_height = alien.rect.size
        alien.x = 20 + 1.3 * alien_width * alien_number
        alien.y = 1.3 * alien_height * row_number

        self.aliens.add(alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()

            sleep(1)
        else:
            self.aliens.empty()
            self.bullets.empty()
            # self.game_active = False
            self.end_game()

    def _load_sounds(self):
        pygame.mixer.music.load(f'{self.GAME_DIR}/music/main_theme.mp3')
        pygame.mixer.music.play(10000)

        self.start_music = pygame.mixer.Sound(
            f'{self.GAME_DIR}/music/start.mp3')
        self.explousion_sound = pygame.mixer.Sound(
            f'{self.GAME_DIR}/music/exp.mp3')
        self.blaster_sound = pygame.mixer.Sound(
            f'{self.GAME_DIR}/music/blaster.mp3')

    def _sprites_initializing(self):
        self.ship = Ship(self)
        self.background = Background(self, self.ship)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

    def _create_start_menu(self):
        start_menu = pygame_menu.Menu(
            'Space Invaders',
            self.settings.screen_width,
            self.settings.screen_height,
            theme=mytheme)

        start_menu.add.button('Play', self.loop)
        start_menu.add.selector(
            'Difficulty :', [('Tests', 10), ('Hard', 2), ('Easy', 1)],
            onchange=self._set_difficulty)
        start_menu.add.button('Records table', self._set_records_table_screen)
        start_menu.add.button('Help', self._set_help_screen)
        start_menu.add.button('Quit', pygame_menu.events.EXIT)
        start_menu.set_sound(self._make_menu_sounds_engin(), recursive=True)
        return start_menu

    def _set_records_table_screen(self):
        self.start_menu = self._create_records_table_menu()
        self.start_menu.mainloop(self.screen)

    def _create_records_table_menu(self):
        records_menu = pygame_menu.Menu(
            'Records table',
            self.settings.screen_width,
            self.settings.screen_height,
            theme=mytheme)

        records_menu.add.button('Back', self.run_game)
        for record in self.stats.best_scores['best_scores']:
            records_menu.add.label(
                f"{record['datetime']} : {record['name']} : {record['score']}",
                align=pygame_menu.locals.ALIGN_LEFT,
                margin=(self.settings.screen_width // 4, 10)
            )
        return records_menu

    def _set_help_screen(self):
        self.start_menu = self._create_help_menu()
        self.start_menu.mainloop(self.screen)

    def _create_help_menu(self):
        help_menu = pygame_menu.Menu(
            'Help',
            self.settings.screen_width,
            self.settings.screen_height,
            theme=mytheme)

        help_menu.add.button('Back', self.run_game)

        help_menu.add.label(
            "Commodo aliqua elit aute sint officia excepteur enim \nnon cupidatat pariatur aliquip consequat. \nUllamco laborum eiusmod labore occaecat\nadipisicing nostrud tempor laborum tempor\nfugiat consectetur sunt. Ut irure incididunt \nconsectetur non culpa cillum nostrud enim irure\nvelit nisi aliqua.",
            align=pygame_menu.locals.ALIGN_LEFT,
            margin=(50, 10)
        )
        return help_menu

    def _create_end_menu(self):
        end_menu = pygame_menu.Menu(
            'Space Invaders',
            self.settings.screen_width,
            self.settings.screen_height,
            theme=mytheme)
        if self.stats.best_score < self.stats.score:
            end_menu.add.label(f'New record!!!')
            end_menu.add.label(f'Your score: {self.stats.score}')
            end_menu.add.text_input(
                'Name:', default='player', onchange=self.stats.playerName)
            end_menu.add.button('Save result', self.stats.set_record)
        else:
            end_menu.add.label(f'Your score: {self.stats.score}')

        end_menu.add.button('Play again', self.run_game)
        end_menu.add.button('Records table', self.loop)
        end_menu.add.button('Quit', pygame_menu.events.EXIT)
        return end_menu

    def _make_menu_sounds_engin(self):
        sounds_engine = sound.Sound()
        sounds_engine.set_sound(
            sound.SOUND_TYPE_WIDGET_SELECTION,
            f'{self.GAME_DIR}/music/menu_select.mp3')
        return sounds_engine

    def _set_difficulty(self, value, difficulty):
        print(value, difficulty)
        self.settings.alien_speed = difficulty * 10
        self.settings.difficulty_coof = difficulty * 2
