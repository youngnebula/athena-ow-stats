from player import Player


def main():

    player = Player("pc", "us", "pulsar-11413")
    print('Name: ', player.get_name())
    print('Level: ', player.get_total_level())
    print('Rating: ', player.get_rating(), '-', player.get_rank())
    print('Losses: ', player.get_loss())
    print('Wins: ', player.get_win())    
    player.display_all_ratings()



main()