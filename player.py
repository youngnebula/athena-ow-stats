import requests
import json
from utilities import difference_data, get_rank
import os.path
from typing import Set

hero_list = (
    "ana",
    "ashe",
    "baptiste",
    "bastion",
    "brigitte",
    "dva",
    "doomfist",
    "genji",
    "hanzo",
    "junkrat",
    "lucio",
    "mccree",
    "mei",
    "mercy",
    "moira",
    "orisa",
    "pharah",
    "reaper",
    "reinhardt",
    "roadhog",
    "sigma",
    "soldier76",
    "sombra",
    "symmetra",
    "torbjorn",
    "tracer",
    "widowmaker",
    "winston",
    "wreckingball",
    "zarya",
    "zenyatta",
)


class Player:
    def __init__(self, platform: str, region: str, battletag: str) -> None:
        """Player object.

        Args:
            platform (str): Platform (psn, xbl, pc, and nintendo-switch).
            region (str): Region of account (us, eu, asia).
            battletag (str): Specific account battletag/name.
        """
        self.platform = platform
        self.region = region
        self.battletag = battletag
        self.data = {}

    ##############
    # BASIC INFO #
    ##############

    def get_name(self) -> str:
        """Gets name of 'Player' object.

        Returns:
            str: Overwatch username of 'Player'.
        """
        return self.data["name"]

    def get_total_level(self) -> int:
        """Gets the total level of account. Uses 'prestige' and 'level' to determine.

        Returns:
            int: Total level of Player
        """
        return str(self.data["prestige"]) + str(self.data["level"])

    def get_games_won(self) -> int:
        """Gets number of games won by Player.

        Returns:
            int: number of games won by Player.
        """
        return self.data["gamesWon"]

    ######################
    # COMPETETITIVE INFO #
    ######################

    def get_loss(self) -> int:
        """Gets number of losses by Player.

        Returns:
            int: number of games lost by Player.
        """
        return int(self.data["competitiveStats"]["games"]["played"]) - int(
            self.data["competitiveStats"]["games"]["won"]
        )

    def get_win(self):
        return self.data["competitiveStats"]["games"]["won"]

    def get_avg_rating(self) -> int:
        """Gets average rating of Player.

        Returns:
            int: average rating of Player.
        """
        return self.data["rating"]

    def display_all_ratings(self) -> None:
        """Displays(prints) all ratings and rating names (gold, diamond, etc.)."""
        for r in self.data["ratings"]:
            print(r["role"].capitalize(), "-", r["level"], "-", get_rank(r["level"]))

    ##################
    # DATA FUNCTIONS #
    ##################

    def save_data(self) -> None:
        """Saves received API json in a dictionary."""
        with open("player_data.json", "w") as f:
            json.dump(self.data, f, sort_keys=True, indent=4)

    def retrieve_data(self) -> None:
        """GET Request to OW-API for Player instance."""
        self.data = json.loads(
            requests.get(
                f"https://ow-api.com/v1/stats/{self.platform}/{self.region}/{self.battletag}/complete"
            ).text
        )

    def find_heroes_played(self) -> Set[str]:
        """Finds and collects all heroes who have been played by this Player instance
           since the last time they played.

        Returns:
            List[str]: List of heroes who have been played by this Player instance.
        """
        heroes_played = []

        if os.path.exists("player_data.json"):
            with open("player_data.json", "r") as f:
                older_data = json.load(f)
            for heroes in self.data["competitiveStats"]["careerStats"]:
                if heroes in hero_list and difference_data(
                    self.data["competitiveStats"]["careerStats"][heroes],
                    older_data["competitiveStats"]["careerStats"][heroes],
                ):
                    heroes_played.append(heroes)
        else:
            heroes_played.append("No new data found.")
        return heroes_played


# Debugging only
######################################################################################
if __name__ == "__main__":
    player1 = Player("pc", "us", "pulsar-11413")
    player1.retrieve_data()
    player1.save_data()
    print(player1.find_heroes_played())
