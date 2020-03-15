import requests
import json
from jsondiff import diff

class Player:

    def __init__(self, platform, region, battletag):
        self.platform = platform
        self.region = region
        self.battletag = battletag
        # grabs profile
        self.data = {} 


    #########
    # BASIC #
    #########

    def get_name(self):
        return self.data['name']

    def get_total_level(self):
        return str(self.data['prestige']) + str(self.data['level'])
        
    def get_games_won(self):
        return self.data['gamesWon']

    #################
    # COMPETETITIVE #
    #################
    
    def get_loss(self):
        return int(self.data['competitiveStats']['games']['played']) - int(self.data['competitiveStats']['games']['won'])
        
    def get_win(self):
        return self.data['competitiveStats']['games']['won']
        
    def get_rating(self):
        return self.data['rating']

    def get_rank(self):
        rating = self.data['rating']
        if rating < 1500:
            rank = "Bronze"
        elif rating in range(1500, 2000):
            rank = "Silver"
        elif rating in range(2000, 2500):
            rank = "Gold"
        elif rating in range(2500, 3000):
            rank = "Platinum"
        elif rating in range(3000, 3500):
            rank = "Diamond"
        elif rating in range(3500, 4000):
            rank = "Master"
        elif rating >= 4000:
            rank = "Grandmaster"
        return rank

    def display_all_ratings(self):
        for r in self.data['ratings']:
            print(r['role'], '-', r['level'])


    ##################
    # DATA FUNCTIONS #
    ##################

    def save_data(self):
        with open('player_data.json', 'w') as f:
            json.dump(self.data, f, sort_keys=True, indent=4)

    def retrieve_data(self):
        self.data = json.loads(requests.get(f"https://ow-api.com/v1/stats/{self.platform}/{self.region}/{self.battletag}/complete").text) 

    def compare_data(self):
        with open('player_data.json', 'r') as f:
            older_data = json.load(f)
        print(diff(self.data, older_data)) 