import requests
import json


class Player:
    def __init__(self, platform, region, battletag):
        self.platform = platform
        self.region = region
        self.battletag = battletag

    def get_stats(self):
        """
        This function will convert the json from requests into a dictionary.
        """
        response = requests.get(f"https://ow-api.com/v1/stats/{self.platform}/{self.region}/{self.battletag}/profile")
        data = json.loads(response.text)
        return data

    def get_name(self):
        return self.get_stats()['name']

    def get_total_level(self):
        return str(self.get_stats()['prestige']) + str(self.get_stats()['level'])

    def get_rating(self):
        return self.get_stats()['rating']


    def get_loss(self):
        return int(self.get_stats()['competitiveStats']['games']['played']) - int(self.get_stats()['competitiveStats']['games']['won'])


    def get_win(self):
        return self.get_stats()['competitiveStats']['games']['won']

    def get_rank(self):
        rating = self.get_stats['rating']
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

if __name__ == "__main__":
    player = Player("pc", "us", "nebula-11571")
    print('Name: ', player.get_name())
    print('Level: ', player.get_total_level())
    print('Rating: ', player.get_rating())
    print('Losses: ', player.get_loss())
    print('Wins: ', player.get_win())    








