from player import Player



def main():
    # Init and data retrieval.
    player1 = Player("pc", "us", "pulsar-11413")
    player1.retrieve_data()

    # Basic Outputs
    print('Name: ', player1.get_name())
    print('Level: ', player1.get_total_level())
    print('Losses: ', player1.get_loss())
    print('Wins: ', player1.get_win())    
    player1.display_all_ratings()



main()