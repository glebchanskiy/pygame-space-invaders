import yaml
from yaml import CLoader as Loader, CDumper as Dumper
import os
class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        # Параметры экрана
        with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), 'settings.yaml'), "r") as config:
            data = yaml.load(config, Loader=Loader)
            self.ship_speed = data['ship_speed']
            self.ship_limit = data['ship_limit']
            self.bullet_speed = data['bullet_speed']
            self.bullets_allowed = data['bullets_allowed']
            self.alien_speed = data['alien_speed']
            self.fleet_drop_speed = data['fleet_drop_speed']


        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.fleet_direction = -1
        self.difficulty_coof = 1
        

