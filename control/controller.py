from models.tournament import Tournament
from models.player import Player
import control.controller_helper as helper
from view.view import View
from export.export_tournament_data import export_tournament_data
import os
from os import path
import json
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
        tournament.set_ending_time()
        export_tournament_data(tournament, True)

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
        if choice == "q" or choice == "Q":
            return

    @staticmethod
    def global_ranking_display(sort_by):
        # todo afficher la liste des joueurs par odre alphabétique et le classement général
        print("en construction")

    @staticmethod
    def tournaments_list() -> list:
        tournaments_folder = f"{EXPORT_FOLDER}tournaments/"

        if path.exists(tournaments_folder) and len(os.listdir(tournaments_folder)) > 0:
            tournaments_list = helper.items_in_folder(tournaments_folder)
            View.display_tournaments_list(tournaments_list)
            return tournaments_list

        View.no_tournament_found()
        return []

    @staticmethod
    def tournament_data_import(file_path, tournament_name):
        with open(f"{file_path}/{tournament_name}.json", 'r') as f:
            tournament_data = json.load(f)
        tournament = Tournament(tournament_data["name"], tournament_data["location"],
                                tournament_data["number of players"],
                                tournament_data["Total Number of Rounds"], False)
        tournament.id = tournament_data["id"]

        with open(f"{file_path}/players_list.json", "r") as f:
            players_data = json.load(f)

        players_list = [
            Player(player["firstname"], player["name"], player["birthdate"], player["id"], player["total points"]) for
            player in players_data]
        tournament.add_player(players_list, False)

        tournament.reconstruct_rounds(tournament_data["list of rounds"])


        # todo ajouter les rounds au tournoi avec tournament.rounds_list

        return tournament

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

        tournament: Tournament = self.tournament_data_import(tournament_path, this_tournament)
        View.display_tournament_info(tournament)

# todo il faudra transformer les json data en objet tournament (etc) pour pouvoir
#  utiliser les mêmes fonctions à l'affichage et à la reprise ?? Ou était-ce pour l'affichage à la fin du tournoi ?
