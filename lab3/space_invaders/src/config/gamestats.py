
import os
import json
import datetime

class GameStats():
    def __init__(self, ai_game):
        self.best_scores = []
        self.best_score = 0

        with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), 'gamestats.json'), "r") as gamestats:
            self.best_scores = json.load(gamestats)
            self.best_scores['best_scores'].sort(key=self.myFunc, reverse=True)
          
          
        for sc in self.best_scores['best_scores']:
            print(sc)
            if sc['score'] > self.best_score:
                self.best_score = sc['score']

        self.settings = ai_game.settings
        self.player_name = "player"
        
        self.score = 0
        self.wave = 1
        self.reset_stats()

    def myFunc(self, element):
        return element['score']

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.wave = 0

    def set_record(self):
        
        self.best_scores['best_scores'].insert(0,{ 
            "name": self.player_name, 
            "score": self.score, 
            "datetime": datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")})
        
        self.best_score = self.score
        print(self.best_scores)
        self.save()

    def playerName(self, name):
        self.player_name = name

    def save(self):
        with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), 'gamestats.json'), "w") as gamestats:
            json.dump(self.best_scores, gamestats, indent=4, default=str)

