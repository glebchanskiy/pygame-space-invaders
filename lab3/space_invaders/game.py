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
from lab3.space_invaders.src.sprites.explosion import Explosion

from lab3.space_invaders.src.sprites.enemies.attacker import Attacker
from lab3.space_invaders.src.sprites.enemies.defensor import Defensor
from lab3.space_invaders.src.sprites.enemies.air_defensor import AirDefensor
from lab3.space_invaders.src.sprites.enemies.dreadnought import Dreadnought
from lab3.space_invaders.src.sprites.enemies.rocketer import Rocketer

from lab3.space_invaders.src.sprites.ship import Ship
from lab3.space_invaders.src.sprites.bullet import Bullet
from lab3.space_invaders.src.sprites.ship_rocket import Rocket


class AlienInvasion:

    def __init__(self):
        self.GAME_DIR = os.path.realpath(os.path.dirname(__file__))

        pygame.init()
        pygame.display.set_caption("Alien Invasion")

        self.settings = Settings()
        self.stats = GameStats(self)

        self._load_sounds()

        self.screen = pygame.display.set_mode(self.settings.screen_size)

        self._sprites_initializing()
        self._create_fleet(1)

        self._prepare_rockets()
        self._prepare_timestop()

        self.game_active = True
        self.menu = None

    def run_game(self):
        self.stats.reset_stats()
        self.settings.reset()
        self.menu = self._create_start_menu()
        self.menu.mainloop(self.screen)

    def end_game(self):
        self.menu = self._create_end_menu()
        self.menu.mainloop(self.screen)

    def loop(self):
        self.start_music.play()
        while True:
            print('Sprites active: ', len(self.weapons) +
                  len(self.bullets) + len(self.aliens))
            self._check_events()

            if self.game_active:
                self._update_bg()
                self._update_ship()
                self._update_bullets()
                self._update_aliens()
                self._update_message()
                self._update_explosions()
                self._update_the_warudo()
                self._update_rockets()

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

        self._check_background_change(event)
        self._check_ship_control(event)

        if event.key == pygame.K_w:
            if not self.isTheWARUDO and self.the_warudo_reload_still == 0:
                self.THE_WARUDO()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_background_change(self, event):
        if event.key == pygame.K_1:
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

    def _check_ship_control(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_r:
            self._fire_rocket()

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
        self._check_aliens_bottom()
        self._check_fleet_edges()

        self.aliens.update()
        self.aliens.draw(self.screen)

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _update_message(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render(
            f'score: {self.stats.score}', True, (255, 255, 255))
        wave_text = font.render(
            f'wave {self.stats.wave}', True, (255, 255, 255))

        hp = font.render(
            'hp: '+'¤' * self.stats.ships_left, True, (255, 255, 255))
        thewarudo = font.render(
            'timestop: ' + (str(self.the_warudo_reload_still) if self.the_warudo_reload_still != 0 else 'ready'), True, (255, 255, 255))
        rockets = font.render(
            'rockets: ' + (str(self.rockets_reload_still) if self.rockets_reload_still != 0 else str(self.rockets_now)), True, (255, 255, 255))

        self.screen.blit(score_text, (10, 10))
        self.screen.blit(wave_text, (10, 40))
        self.screen.blit(hp, (10, 70))
        self.screen.blit(thewarudo, (10, 100))
        self.screen.blit(rockets, (10, 130))

    def _update_explosions(self):
        for exp in self.explosions:
            if exp.counter == exp.last:
                self.explosions.remove(exp)
            exp.update()

        for exp in self.explosions:
            exp.blitme()

    def _update_the_warudo(self):
        if self.the_warudo_reload_still > 0:
            self.the_warudo_reload_still -= 1
        if self.isTheWARUDO:
            if self.time_befor_time_stop == self.the_warudo_time:
                self.UN_THE_WARUDO()
            self.time_befor_time_stop += 1

    def _update_rockets(self):
        if self.rockets_reload_still > 0:
            self.rockets_reload_still -= 1
            self.rockets_can_fire = False
        else:
            self.rockets_can_fire = True

    def _update_screen(self):
        pygame.display.update()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        shiled_collisions = pygame.sprite.groupcollide(
            self.bullets, self.weapons, True, False)

        if pygame.sprite.spritecollideany(self.ship, self.weapons):
            self._ship_hit()

        for groups in collisions.values():
            for alien in groups:
                self.explousion_sound.play()
                self.stats.score += alien.cost
                self.weapons.remove(alien.weapon)
                exp = Explosion(self, alien.rect.center)
                self.explosions.add(exp)

        if not self.aliens:
            self._new_wave()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            self.blaster_sound.play()
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def _fire_rocket(self):
        if self.rockets_now != 0 and self.rockets_can_fire:
            self.rockets_now -= 1
            self.rocket_sound.play()
            rocket = Rocket(self)
            self.bullets.add(rocket)
        if self.rockets_now == 0:
            self.rockets_reload_still = self.rockets_reload_time
            self.rockets_now = self.rockets_alowed

    def _new_wave(self):
        self.stats.wave += 1
        self.settings.current_alien_speed += self.settings.difficulty_coof
        self.settings.fleet_drop_speed += self.settings.difficulty_coof
        self.background.change_bg(randint(0, 7))

        self.bullets.empty()
        self.explosions.empty()
        self._create_fleet(self.stats.wave)

    def _create_fleet(self, wave_number):
        if wave_number > 20:
            self._fleet_auto_gen()
            # self._fleet_debug_gen()
        else:
            self._flee_load_from_settings(wave_number)

    def _fleet_debug_gen(self):
        for i in range(1):
            self._create_alien_row(
                i,
                3,
                'rocketer',
                'blue'
            )

    def _fleet_auto_gen(self):
        alien_types = ['attack', 'heavy', 'dreadnought', 'rocketer']
        alien_color = ['blue', 'green', 'orange', 'red']
        aliens_per_row = randint(3, 5)
        for i in range(randint(3, 4)):
            self._create_alien_row(
                i,
                aliens_per_row,
                alien_types[randint(0, len(alien_types)-1)],
                alien_color[randint(0, len(alien_color)-1)]
            )

    def _flee_load_from_settings(self, wave_number):
        count = 0
        for row in self.settings.waves[f'wave_{wave_number}']['rows']:
            self._create_alien_row(
                count,
                self.settings.waves[f'wave_{wave_number}']['alien_in_row'],
                row['type'],
                row['color']
            )
            count += 1

    def _create_alien_row(self, row_number, amount_of_aliens, type, color):
        for i in range(amount_of_aliens):
            if type == 'attack':
                alien = Attacker(self, color)
            elif type == 'heavy':
                alien = Defensor(self, color)
            elif type == 'rocketer':
                alien = Rocketer(self, color)
            elif type == 'pvo':
                alien = AirDefensor(self, color)
            else:
                alien = Dreadnought(self, color)

            alien.y = 20 + 90 * row_number
            alien.x = 20 + 80 * i

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
            alien.y += self.settings.current_fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        if self.stats.ships_left > 1:
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self.weapons.empty()
            self._create_fleet(self.stats.wave)
            self.ship.center_ship()

            sleep(1)
        else:
            self.aliens.empty()
            self.bullets.empty()
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
        self.rocket_sound = pygame.mixer.Sound(
            f'{self.GAME_DIR}/music/rocket.mp3')
        self.laser_sound = pygame.mixer.Sound(
            f'{self.GAME_DIR}/music/laser.mp3')
        self.time_resume = pygame.mixer.Sound(
            f'{self.GAME_DIR}/music/time.mp3')

    def _sprites_initializing(self):
        self.ship = Ship(self)
        self.background = Background(self, self.ship)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.weapons = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()

    def _prepare_rockets(self):
        self.rockets_reload_still = 0
        self.rockets_reload_time = self.settings.rockets_reload_time
        self.rockets_alowed = self.settings.rockets_alowed
        self.rockets_now = 3

    def _prepare_timestop(self):
        self.isTheWARUDO = False
        self.the_warudo_reload_still = 0
        self.the_warudo_reload_time = self.settings.timestop_reload_time
        self.the_warudo_time = self.settings.timestop_time
        self.time_befor_time_stop = 0
        self.alien_bullet_speed_befor = 0
        self.speed_befor = 0
        self.bullet_speed_befor = 0
        self.bullet_amount_befor = 0

    def _create_start_menu(self):
        start_menu = pygame_menu.Menu(
            'Space Invaders',
            self.settings.screen_width,
            self.settings.screen_height,
            theme=mytheme)

        start_menu.add.button('Play', self.loop)
        start_menu.add.selector(
            'Difficulty :', [('Easy', 1), ('Hard', 2)],
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
                margin=(self.settings.screen_width // 7, 10)
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
            self.settings.help_text,
            align=pygame_menu.locals.ALIGN_LEFT,
            margin=(200, 10)
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
        end_menu.add.button('Records table', self._set_records_table_screen)
        end_menu.add.button('Quit', pygame_menu.events.EXIT)
        return end_menu

    def _make_menu_sounds_engin(self):
        sounds_engine = sound.Sound()
        sounds_engine.set_sound(
            sound.SOUND_TYPE_WIDGET_SELECTION,
            f'{self.GAME_DIR}/music/menu_select.mp3')
        return sounds_engine

    def _set_difficulty(self, value, difficulty):
        self.settings.current_alien_speed = difficulty * 5
        self.settings.difficulty_coof = difficulty * 2

    def THE_WARUDO(self):
        pygame.mixer.music.pause()
        self.time_resume.play()

        pygame.display.set_caption("THEE WARUUDOOO")
        self.bullet_amount_befor = self.settings.bullets_allowed
        self.settings.bullets_allowed = self.settings.timestop_bullets_allowed
        self.alien_bullet_speed_befor = self.settings.alien_bullet_speed
        self.settings.alien_bullet_speed = 0
        self.speed_befor = self.settings.current_alien_speed
        self.settings.current_alien_speed = 0
        self.bullet_speed_befor = self.settings.bullet_speed
        self.settings.bullet_speed = 0
        self.isTheWARUDO = True

    def UN_THE_WARUDO(self):
        pygame.mixer.music.unpause()
        pygame.display.set_caption("Alien Invasion")
        self.settings.alien_bullet_speed = self.alien_bullet_speed_befor
        self.settings.current_alien_speed = self.speed_befor
        self.settings.bullet_speed = self.bullet_speed_befor
        self.settings.bullets_allowed = self.bullet_amount_befor
        self.isTheWARUDO = False
        self.time_befor_time_stop = 0
        self.the_warudo_reload_still = self.the_warudo_reload_time
