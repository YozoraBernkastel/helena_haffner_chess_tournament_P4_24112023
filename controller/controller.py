from models.tournament import Tournament
from models.player import Player
from view.view import View
import datetime
from export.export_tournament_data import export_tournament_data
from controller.controller_helper import is_already_known_id, already_in_tournament


class Controller:

    @staticmethod
    def link():
        # todo comment gérer la liste des lonely lors d'une reprise ? La recalculer à partir des lonely de chaque tour
        #  et simuler les opérations ou bien inclure la liste telle qu'elle dans le json puis la suppriemr à la toute fin ?

        choice = View.display_menu()

        if choice == "1":
            tournament_name = View.tournament_name()
            tournament_location = View.tournament_location()

            if choice == "q" or choice == "Q":
                return

            number_of_round = View.round_number()
            number_of_players = View.number_of_players()
            tournament = Tournament(tournament_name, tournament_location, number_of_players, number_of_round)
            # export_tournament_data(tournament)

            created_players = 0
            while number_of_players > created_players:
                created_players += 1

                chess_id = ""
                already_registered = False

                while chess_id == "" or already_registered:
                    if chess_id != "":
                        View.already_added(chess_id)
                    chess_id = View.asks_chess_id()
                    already_registered = already_in_tournament(chess_id, tournament.name)

                id_exist, this_player = is_already_known_id(chess_id)

                if id_exist:
                    View.known_player_prompt(chess_id)
                    firstname, name, birthdate = this_player["firstname"], this_player["name"], this_player["birthdate"]
                else:
                    firstname, name, birthdate = View.players_registration(tournament)

                player = Player(firstname, name, birthdate, chess_id)
                tournament.players_list = player

            View.display_players_score(tournament.players_list, True)

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

                if (len(tournament.rounds_list) + 1) == tournament.number_of_rounds:
                    tournament.set_ending_time()
                export_tournament_data(tournament)
                # todo créer un export "classement" que l'on met à jour après chaque round.

                if tournament.odd_players_number():
                    print(f"lonely list -> {tournament.lonely_players}\n\n")

            print(tournament.rounds_list)

