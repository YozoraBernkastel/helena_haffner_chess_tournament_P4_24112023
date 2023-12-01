from models.player import Player
from models.round import Round
from models.game import Game
from view.view import View


class Controller:

    @staticmethod
    def link():
        choice = View.display_menu()

        if choice == "q" or choice == "Q":
            return

        selene = Player("Sélène", "Tsuki", 22, "15av4")
        agathe = Player("Agathe", "Observer", 38, "8846uh8")
        frederica = Player("Frederica", "Majou", 7803, "11aa11")
        fall = Player("Fall", "Paradox", 7524, "22qb55")

        player_list = [selene, agathe, frederica, fall]

        "Set up the round"
        around_the_world = Round(1, player_list, "End of the Golden Witch")
        around_the_world.create_games()
        games_list = around_the_world.games_list
        print(games_list)

        View.display_players_score(player_list)

        # Now the results
        for game in games_list:
            res = View.asks_result(game)
            game.game_result = res
            print(game.game_result)

        View.display_players_score(player_list)




