from models.tournament import Tournament
from models.player import Player
import control.controller_helper as helper
from view.view import View
from export.export_tournament_data import export_tournament_data
import os
from os import path
import datetime


from settings.settings import EXPORT_FOLDER


class Controller:

    def display_menu(self):

        choice = View.display_menu()

        if choice == "1":
            self.tournament_creation()

        if choice == "2":
            self.display_report()

        if choice == "q" or choice == "Q":
            return

    @staticmethod
    def tournament_creation():
        # todo comment gérer la liste des lonely lors d'une reprise ? La recalculer à partir des lonely de chaque tour
        #  et simuler les opérations ou bien inclure la liste telle qu'elle dans le json puis la suppriemr à la toute fin ?

        tournament_name: str = View.tournament_name()
        tournament_location: str = View.tournament_location()
        # todo demander à écrire une description pour le tournoi !!!

        # todo enregistrer après le résultat de chaque partie

        number_of_round: int = View.round_number()
        number_of_players: int = View.number_of_players()
        tournament = Tournament(tournament_name, tournament_location, number_of_players, number_of_round)

        created_players = 0
        while number_of_players > created_players:
            created_players += 1

            chess_id = ""
            already_registered = False

            while chess_id == "" or already_registered:
                if chess_id != "":
                    View.already_added(chess_id)
                chess_id: str = View.asks_chess_id()
                already_registered: bool = helper.already_in_tournament(chess_id, tournament)

            id_exist, this_player = helper.is_already_known_id(chess_id)

            if id_exist:
                View.known_player_prompt(chess_id)
                firstname, name, birthdate, total_points = this_player["firstname"], this_player["name"], this_player["birthdate"], this_player["total points"]
            else:
                firstname, name, birthdate = View.players_registration(tournament)
                total_points = 0

            player = Player(firstname, name, birthdate, chess_id, total_points)
            tournament.add_player(player)

        View.display_players_score(tournament.players_list, True)

        while len(tournament.rounds_list) != number_of_round:
            games_list = tournament.create_round()

            # Now the results
            for game in games_list:
                if game is games_list[0]:
                    View.show_round_number(game.belong_round)
                    View.show_round_lonely_player(game.belong_round)
                    View.show_all_games_of_round(games_list)

                res: str = View.asks_result(game)
                game.game_result = res
                export_tournament_data(tournament)

            View.display_players_score(tournament.players_list, False)
            games_list[-1].belong_round.ending = datetime.datetime.now().replace(microsecond=0)

            if len(tournament.rounds_list) == tournament.number_of_rounds:
                tournament.set_ending_time()
                export_tournament_data(tournament, True)

            # todo mettre en view ou supprimer ?
            if tournament.odd_players_number():
                print(f"lonely list -> {tournament.lonely_players}\n\n")

            # todo !!!!!!!!! afficher le classement avec le nombre de points remporté dans le tournoi
            #  afin d'avoir le classement du tournoi et non le classement global !!!

    def display_report(self):
        choice = View.display_report_general_menu()

        if choice == "1":
            self.global_ranking_display("points")
        if choice == "2":
            self.global_ranking_display("alphabetical")
        if choice == "3":
            self.tournaments_list()
        if choice == "4":
            self.tournament_info()

    @staticmethod
    def global_ranking_display(sort_by):
        print("en construction")

    @staticmethod
    def tournaments_list():
        tournaments_folder = f"{EXPORT_FOLDER}tournaments/"

        if path.exists(tournaments_folder) and len(os.listdir(tournaments_folder)) > 0:
            tournaments_list = helper.items_in_folder(tournaments_folder)
            View.display_tournaments_list(tournaments_list)
            return tournaments_list

        View.no_tournament_found()
        return []

    def tournament_info(self):
        tournaments_folder = f"{EXPORT_FOLDER}tournaments/"
        tournaments_list = self.tournaments_list()

        if len(tournaments_list) == 0:
            return

        this_tournament: str = ""

        existing_tournament = False
        while not existing_tournament:
            this_tournament = View.choose_tournament_to_display()
            existing_tournament = any(this_tournament == tournament for tournament in tournaments_list)

        tournament_path = f"{tournaments_folder}{this_tournament}"

        if not path.exists(tournament_path):
            View.tournament_folder_not_found()
            return

        View.display_tournament_info(tournament_path)






# todo il faudra transformer les json data en objet tournament (etc) pour pouvoir
#  utiliser les mêmes fonctions à l'affichage et à la reprise ?? Ou était-ce pour l'affichage à la fin du tournoi ?


