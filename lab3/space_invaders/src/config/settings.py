class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Параметры корабля 
        self.ship_speed = 20
        self.ship_limit = 3
        self.bullet_speed = 10
        self.bullets_allowed = 5
        self.alien_speed = 5 # 5
        self.fleet_drop_speed = 10 # 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = -1
        self.difficulty_coof = 1
        

