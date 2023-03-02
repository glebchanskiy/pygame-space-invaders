import yaml
from yaml import CLoader as Loader, CDumper as Dumper
import os


class Settings():
    def __init__(self):
        with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), 'settings.yaml'), "r") as config:
            data = yaml.load(config, Loader=Loader)
            self.ship_speed = data['ship_speed']
            self.ship_limit = data['ship_limit']
            self.bullet_speed = data['bullet_speed']
            self.bullets_allowed = data['bullets_allowed']
            self.alien_speed = data['alien_speed']
            self.alien_bullet_speed = data['alien_bullet_speed']
            self.fleet_drop_speed = data['fleet_drop_speed']
            self.attacker_cost = data['attacker_cost']
            self.air_defensor_cost = data['air_defensor_cost']
            self.defensor_cost = data['defensor_cost']
            self.rocketer_cost = data['rocketer_cost']
            self.dreadnought_cost = data['dreadnought_cost']
            self.waves = data['waves']
            self.help_text = data['help_text']
            self.timestop_time = data['timestop_time']
            self.timestop_reload_time = data['timestop_reload_time']
            self.rockets_reload_time = data['rockets_reload_time']
            self.rockets_alowed = data['rockets_alowed']
            self.timestop_bullets_allowed = data['timestop_bullets_allowed']
            print(self.waves)

        self.current_alien_speed = self.alien_speed
        self.current_fleet_drop_speed = self.fleet_drop_speed

        self.screen_width = 1200
        self.screen_height = 800
        self.screen_size = self.screen_width, self.screen_height
        self.bg_color = (230, 230, 230)

        self.fleet_direction = -1
        self.difficulty_coof = 1

    def reset(self):
        self.current_alien_speed = self.alien_speed
        self.current_fleet_drop_speed = self.fleet_drop_speed
