from models.tournament import Tournament
from models.player import Player
import control.controller_helper as helper
from view.view import View
from export.export_tournament_data import (export_tournament_data,
                                           add_tournament_to_unfinished_list,
                                           remove_tournament_from_unfinished_list)
import os
from os import path
from settings.settings import EXPORT_FOLDER


class Controller:

    def __init__(self):
        self._tournaments_folder = f"{EXPORT_FOLDER}tournaments/"
        self._global_players_folder = f"{EXPORT_FOLDER}global_players_list/"

    def display_menu(self):
        choice = View.display_menu()

        if choice == "1":
            self.tournament_creation()
            return
        if choice == "2":
            self.display_report()
            return
        if choice == "3":
            self.restart_tournament()
            return
        if helper.is_user_quits(choice):
            return

    @staticmethod
    def initiate_tournament():
        tournament_name: str = View.tournament_name()
        tournament_location: str = View.tournament_location()
        description: str = View.tournament_description()
        number_of_round: int = View.round_number()
        number_of_players: int = View.number_of_players()
        tournament = Tournament(tournament_name, tournament_location,
                                number_of_players, number_of_round)
        add_tournament_to_unfinished_list(tournament)

        # tournament's description is set here because the object should be initialized
        # even if it's more natural for the user to written it after the name and the location.
        tournament.description = description

        return tournament

    @staticmethod
    def create_player(tournament, chess_id):
        id_exist, this_player = helper.is_already_known_id(chess_id)

        if id_exist:
            View.known_player_prompt(chess_id)
            firstname, name, birthdate, total_points = this_player["firstname"], this_player["name"], this_player[
                "birthdate"], this_player["total points"]
        else:
            firstname, name, birthdate = View.players_registration(tournament)
            total_points = 0

        return Player(firstname, name, birthdate, chess_id, total_points)

    def players_registration(self, tournament):
        created_players = len(tournament.players_list)
        while tournament.number_of_players > created_players:
            created_players += 1
            chess_id = ""
            already_registered = False

            while chess_id == "" or already_registered:
                if chess_id != "":
                    View.already_added(chess_id)
                chess_id: str = View.asks_chess_id()
                already_registered: bool = helper.already_in_tournament(chess_id, tournament)

            player = self.create_player(tournament, chess_id)
            tournament.add_player(player)

        View.display_players_score(tournament.players_list, True)

    @staticmethod
    def games_generation(around, tournament):
        for game in around.games_list:
            if not game.game_result:
                res: str = View.asks_result(game)
                game.set_result(res)
                export_tournament_data(tournament)

    def rounds_generation(self, tournament):
        while len(tournament.rounds_list) != tournament.number_of_rounds:
            around = tournament.create_round()
            View.display_round_info(around)
            self.games_generation(around, tournament)

            is_last_round: bool = int(around.round_name) == tournament.number_of_rounds
            View.display_players_score(tournament.players_list, False, is_last_round)
            around.set_ending_time()

            if tournament.odd_players_number():
                View.display_lonely_players_list(tournament.lonely_players)

    @staticmethod
    def close_tournament(tournament):
        tournament.set_ending_time()
        export_tournament_data(tournament, True)
        remove_tournament_from_unfinished_list(tournament)

    def tournament_creation(self, tournament=None, reconstruct=False):
        if not reconstruct:
            tournament = self.initiate_tournament()

        self.players_registration(tournament)

        if reconstruct:
            if len(tournament.rounds_list) > 0:
                self.games_generation(tournament.rounds_list[-1], tournament)

        self.rounds_generation(tournament)
        self.close_tournament(tournament)

    def display_report(self) -> None:
        choice = View.display_report_general_menu()

        if choice == "1":
            self.global_ranking_display()
        if choice == "2":
            self.global_ranking_display(True)
        if choice == "3":
            View.display_tournaments_list(self.tournaments_list())
        if choice == "4":
            self.tournament_info()
        if helper.is_user_quits(choice):
            return

    def global_ranking_display(self, alphabetical=False) -> None:
        players_list = Player.reconstruct_player(self._global_players_folder, alphabetical)
        View.display_players_info(players_list)

    def tournaments_list(self) -> list:
        tournaments_list = list()
        if path.exists(self._tournaments_folder) and len(os.listdir(self._tournaments_folder)) > 0:
            tournaments_list = helper.items_in_folder(self._tournaments_folder)

        return tournaments_list

    @staticmethod
    def which_tournament(tournaments_list):

        if len(tournaments_list) == 0:
            View.no_tournament_found()
            return False

        View.display_tournaments_list(tournaments_list)
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
            check_more = View.this_tournament_menu()
            if helper.is_user_quits(check_more):
                check_more = False

            elif check_more == "1":
                View.display_players_info(tournament.players_list)

            elif check_more == "2":
                View.display_rounds_info(tournament.rounds_list, tournament.odd_players_number())

    def reconstruct_selected_tournament(self):
        this_tournament = self.which_tournament(self.tournaments_list())
        if not this_tournament or helper.is_user_quits(this_tournament):
            return False

        tournament_path = self.tournament_path_creation(this_tournament)
        if not tournament_path:
            return False

        return Tournament.reconstruction(tournament_path, this_tournament)

    def tournament_info(self) -> None:
        tournament = self.reconstruct_selected_tournament()
        if isinstance(tournament, Tournament):
            View.display_tournament_info(tournament)
            self.more_info(tournament)

    def restart_tournament(self) -> None:
        unfinished_tournaments_list = helper.unfinished_tournaments()
        if not unfinished_tournaments_list:
            View.all_tournaments_are_finished()
            return

        tournament = self.reconstruct_selected_tournament()
        self.tournament_creation(tournament, True)
