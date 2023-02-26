class GameStats():
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.best_score = 100
        self.score = 0
        self.wave = 1
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.wave = 0