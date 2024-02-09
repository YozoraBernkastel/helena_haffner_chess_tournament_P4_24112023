from models.tournament import Tournament
from models.player import Player
import control.controller_helper as helper
from view.view import View
from export.export_tournament_data import export_tournament_data
import os
from os import path
from settings.settings import EXPORT_FOLDER
import datetime


class Controller:

    def __init__(self):
        self._tournaments_folder = f"{EXPORT_FOLDER}tournaments/"
        self._global_players_folder = f"{EXPORT_FOLDER}global_players_list/"

    def display_menu(self):
        choice = View.display_menu()

        if choice == "1":
            self.tournament_creation()
        if choice == "2":
            self.display_report()
        if helper.is_user_quits(choice):
            return

    @staticmethod
    def tournament_creation():
        # todo comment gérer la liste des lonely lors d'une reprise ? La recalculer à partir des lonely de chaque tour
        #  et simuler les opérations ou bien inclure la liste telle qu'elle dans le json puis la suppriemr à la toute fin ?

        tournament_name: str = View.tournament_name()
        tournament_location: str = View.tournament_location()
        description: str = View.tournament_description()
        number_of_round: int = View.round_number()
        number_of_players: int = View.number_of_players()
        tournament = Tournament(tournament_name, tournament_location, number_of_players, number_of_round)

        # tournament's description is set here because the object should be initialized
        # even if it's more natural for the user to written it after the name and the location.
        tournament.description = description

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
                firstname, name, birthdate, total_points = this_player["firstname"], this_player["name"], this_player[
                    "birthdate"], this_player["total points"]
            else:
                firstname, name, birthdate = View.players_registration(tournament)
                total_points = 0

            player = Player(firstname, name, birthdate, chess_id, total_points)
            tournament.add_player(player)

        View.display_players_score(tournament.players_list, True)

        while len(tournament.rounds_list) != number_of_round:
            around = tournament.create_round()

            # todo appeler ces trois méthodes dans une seule !!!!!!!!!!!!!!!
            View.show_round_number(around)
            View.show_round_lonely_player(around)
            View.show_all_games_of_round(around.games_list)

            for game in around.games_list:
                res: str = View.asks_result(game)
                game.set_result(res)
                export_tournament_data(tournament)

            View.display_players_score(tournament.players_list, False)
            around.set_ending_time()

            # todo mettre en view ou supprimer ?
            if tournament.odd_players_number():
                print(f"lonely list -> {tournament.lonely_players}\n\n")

            around.set_ending_time()

        print(f"supposed ending -> {datetime.datetime.now().replace(microsecond=0)}")
        tournament.set_ending_time()
        export_tournament_data(tournament, True)

        # todo !!!!!!!!! afficher le classement avec le nombre de points remporté dans le tournoi
        #  afin d'avoir le classement du tournoi et non le classement global !!!

    def display_report(self) -> None:
        choice = View.display_report_general_menu()

        if choice == "1":
            self.global_ranking_display()
        if choice == "2":
            self.global_ranking_display(True)
        if choice == "3":
            self.tournaments_list()
        if choice == "4":
            self.tournament_info()
        if helper.is_user_quits(choice):
            return

    def global_ranking_display(self, alphabetical = False) -> None:
        players_list = Player.reconstruct_player(self._global_players_folder)

        if alphabetical:
            players_list = sorted(players_list, key=lambda x: x.family_name, reverse=False)
        else:
            players_list = sorted(players_list, key=lambda x: x.total_points, reverse=True)

        View.display_players_info(players_list)

    def tournaments_list(self) -> list:

        if path.exists(self._tournaments_folder) and len(os.listdir(self._tournaments_folder)) > 0:
            tournaments_list = helper.items_in_folder(self._tournaments_folder)
            View.display_tournaments_list(tournaments_list)
            return tournaments_list

        View.no_tournament_found()
        return []

    def which_tournament(self):
        tournaments_list = self.tournaments_list()

        if len(tournaments_list) == 0:
            return False

        this_tournament: str = ""
        existing_tournament = False

        while not existing_tournament and not helper.is_user_quits(this_tournament):
            this_tournament = View.choose_tournament_to_display()
            existing_tournament = any(this_tournament == tournament for tournament in tournaments_list)

        return this_tournament

    def tournament_path_creation(self, this_tournament):
        tournament_path = f"{self._tournaments_folder}{this_tournament}"
        if not path.exists(tournament_path):
            View.tournament_folder_not_found()
            return False

        return tournament_path

    @staticmethod
    def more_info(tournament) -> None:
        check_more = True
        while check_more:
            check_more = View.this_tournament_menu(tournament)
            if helper.is_user_quits(check_more):
                check_more = False

            elif check_more == "1":
                View.display_players_info(tournament.players_list)

            elif check_more == "2":
                View.display_rounds_info(tournament.rounds_list, tournament.odd_players_number())

    def tournament_info(self) -> None:
        this_tournament = self.which_tournament()
        if not this_tournament or helper.is_user_quits(this_tournament):
            return

        tournament_path = self.tournament_path_creation(this_tournament)
        if not tournament_path:
            return

        tournament = Tournament.reconstruction(tournament_path, this_tournament)
        View.display_tournament_info(tournament)
        self.more_info(tournament)


# todo il faudra transformer les json data en objet tournament (etc) pour pouvoir
#  utiliser les mêmes fonctions à l'affichage et à la reprise ?? Ou était-ce pour l'affichage à la fin du tournoi ?
