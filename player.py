import requests
import json
from jsondiff import diff
from utilities import *

hero_list = [
            'ana', 'ashe', 'baptiste', 'bastion', 
            'brigitte', 'dva', 'doomfist', 'genji', 
            'hanzo', 'junkrat', 'lucio', 'mccree', 
            'mei', 'mercy', 'moira', 'orisa', 
            'pharah', 'reaper', 'reinhardt', 'roadhog', 
            'sigma', 'soldier76', 'sombra', 'symmetra', 
            'torbjorn', 'tracer', 'widowmaker', 'winston', 
            'wreckingball', 'zarya', 'zenyatta', 
            ]




class Player:

    def __init__(self, platform, region, battletag):
        self.platform = platform
        self.region = region
        self.battletag = battletag
        self.data = {} 
        self.diff_data = {}

    ##############
    # BASIC INFO #
    ##############

    def get_name(self):
        return self.data['name']

    def get_total_level(self):
        return str(self.data['prestige']) + str(self.data['level'])
        
    def get_games_won(self):
        return self.data['gamesWon']

    ######################
    # COMPETETITIVE INFO #
    ######################
    
    def get_loss(self):
        return int(self.data['competitiveStats']['games']['played']) - int(self.data['competitiveStats']['games']['won'])
        
    def get_win(self):
        return self.data['competitiveStats']['games']['won']
        
    def get_rating(self):
        # Useless
        return self.data['rating']

    def display_all_ratings(self):
        for r in self.data['ratings']:
            print(r['role'].capitalize(), '-', r['level'], '-', get_rank(r['level']))


    ##################
    # DATA FUNCTIONS #
    ##################

    def save_data(self):
        with open('player_data.json', 'w') as f:
            json.dump(self.data, f, sort_keys=True, indent=4)

    def retrieve_data(self):
        self.data = json.loads(requests.get(f"https://ow-api.com/v1/stats/{self.platform}/{self.region}/{self.battletag}/complete").text) 

    def difference_data(self):
        with open('player_data.json', 'r') as f:
            older_data = json.load(f)
        diff_data1 = diff(self.data, older_data)
        diff_data2 = diff(older_data, self.data)
        return find_diffs(diff_data1, diff_data2)

    def find_heroes_played(self):
        heroes_played = []
        with open('player_data.json', 'r') as f:
            older_data = json.load(f)
        for heroes in self.data['competitiveStats']['careerStats']:
            if heroes in hero_list and difference_data(self.data['competitiveStats']['careerStats'][heroes], older_data['competitiveStats']['careerStats'][heroes]):
               heroes_played.append(heroes) 
        return heroes_played

# Debugging only
######################################################################################
if __name__ == '__main__':
    player1 = Player("pc", "us", "pulsar-11413")
    player1.retrieve_data()
    player1.find_heroes_played()