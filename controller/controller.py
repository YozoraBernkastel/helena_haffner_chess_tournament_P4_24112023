from models.tournament import Tournament
from models.player import Player
from view.view import View
import datetime
from extractor.player_list_extract import extract_global_player_list


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
        fipolyte = Player("Hipolyte", "Chimera", 4578, "bbbbb8888")
        sophie = Player("Sophie", "Spring", 22, "15abg4")
        octave = Player("Octave", "Leblanc", 38, "88ok4uh8")
        diane = Player("Diane", "Tsuki", 7803, "11a12411")
        mikako = Player("Mikako", "Tantei", 7524, "22bhhij55")

        players_list = [selene, agathe, frederica, fall, fipolyte, sophie, octave, diane, mikako]

        View.display_players_score(players_list, True)

        tournament = Tournament("Chessy", "Strasbourg", players_list,  number_of_round)
        extract_global_player_list(players_list)

        while len(tournament.rounds_list) != number_of_round:
            games_list = tournament.create_round()

            # Now the results
            for game in games_list:
                if game is games_list[0]:
                    View.show_round_number(game.belong_round)
                    View.show_round_lonely_player(game.belong_round)
                    View.show_all_games_of_round(games_list)

                res = View.asks_result(game)
                game.game_result = res
                # todo ici il faudra exporter le résultat dans un json

            View.display_players_score(tournament.players_list, False)
            games_list[-1].belong_round.ending = datetime.datetime.now()
            print(f"Ending Time :::: {games_list[-1].belong_round.ending}")
            # todo créer un export "classement" que l'on met à jour après chaque round.

            # todo supprimer quand plus nécessaire ou conserver pour la démonstration ??????
            #  Peut-être améliorer l'affichage dans ce cas
            print(f"lonely list -> {tournament.lonely_players}\n\n")
        print(tournament.rounds_list)

