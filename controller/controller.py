from models.tournament import Tournament
from models.player import Player
from models.round import Round
from models.game import Game
from view.view import View
import datetime


class Controller:

    @staticmethod
    def link():
        # todo demander en début de tournoi à enregistrer les joueurs !! Nécessaire
        choice = View.display_menu()

        if choice == "q" or choice == "Q":
            return

        number_of_round = View.round_number()

        selene = Player("Sélène", "Tsuki", 22, "15av4")
        agathe = Player("Agathe", "Observer", 38, "8846uh8")
        frederica = Player("Frederica", "Majou", 7803, "11aa11")
        fall = Player("Fall", "Paradox", 7524, "22qb55")
        ffffff = Player("Hipolyte", "Chimera", 4578, "bbbbb8888")

        player_list = [selene, agathe, frederica, fall, ffffff]

        View.display_players_score(player_list)

        tournament = Tournament("Chessy","Strasbourg", player_list,  number_of_round)

        while len(tournament.rounds_list) != number_of_round:
            games_list = tournament.create_round()

            # Now the results
            for game in games_list:
                res = View.asks_result(game)
                game.game_result = res
                # todo ici il faudra exporter le résultat dans un json

            View.display_players_score(player_list)
            # todo vérifier que les dates de starting time et ending time sont correctes -> pour le moment le print donne le type
            games_list[-1].belong_round.ending = datetime.datetime.now
            print(games_list[-1].belong_round.ending)
            # todo créer un export "classement" que l'on met à jour après chaque round.
            print(f"lonely list -> {tournament.lonely_players}\n\n")




