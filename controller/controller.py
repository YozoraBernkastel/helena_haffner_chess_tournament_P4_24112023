from models.player import Player
from models.round import Round
from models.game import Game
from view.view import View


class Controller:

    @staticmethod
    def link():
        # todo demander en début de tournoi à enregistrer les joueurs !! Nécessaire
        choice = View.display_menu()

        if choice == "q" or choice == "Q":
            return

        selene = Player("Sélène", "Tsuki", 22, "15av4")
        agathe = Player("Agathe", "Observer", 38, "8846uh8")
        frederica = Player("Frederica", "Majou", 7803, "11aa11")
        fall = Player("Fall", "Paradox", 7524, "22qb55")
        ffffff = Player("Hipolyte", "Chimera", 4578, "bbbbb8888")

        player_list = [selene, agathe, frederica, fall, ffffff]

        # tout ce qui est en dessous sera dans la classe tournament à l'avenir !!!!!!
        # Il faudra nettoyer un peu !!
        "Set up the round"
        lonely = []
        around_the_world = Round(1, player_list, lonely, "End of the Golden Witch")
        around_the_world.create_games()
        games_list = around_the_world.games_list
        print(games_list)

        View.display_players_score(player_list)

        # Now the results
        for game in games_list:
            res = View.asks_result(game)
            game.game_result = res
            print(game.game_result)
            # todo ici il faudra exporter le résultat dans un json

        View.display_players_score(player_list)
        # todo créer un export "classement" que l'on met à jour après chaque round.
        print(frederica.opponent_list)
        print(f"lonely list -> {lonely}")
        around_the_world.not_first_round()




