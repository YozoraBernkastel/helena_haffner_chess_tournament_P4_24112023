import random

from models.round import Round
from models.game import Game
# from rich.console import console
from settings import settings


class View:
    @staticmethod
    def tournament_name():
        print("\nComment souhaitez-vous nommer le tournoi ?")
        name_choice = input("")
        # parcourir les exports pour voir si le nom est déjà utilisé ? et si oui, redemander ?
        return name_choice

    @staticmethod
    def tournament_location():
        print("\nOù se déroule le tournoi ?")
        location_choice = input("")
        return location_choice

    @staticmethod
    def display_menu() -> str:
        """
        Offers to the user the possibility to create a tournament, to display the statistics or to quit.
        """
        choice = ""
        check_answer = False

        while not check_answer:
            print("\nBienvenue ! Que souhaitez-vous faire ?\n")
            print("    1) Créer un tournoi")
            print("    2) Voir les statistiques")
            print("    Q) Quitter\n")
            choice = input("")
            choice = choice.strip()

            if choice == "1":
                print("\nNouveau tournoi lancé !!!")
                check_answer = True

            elif choice == "2":
                print("\nVoici les résultats ...")
                check_answer = True
            elif choice == "Q" or choice == "q":
                break
            else:
                print(
                    "\nCette option n'existe malheureusement pas, veuillez sélectionner une commande valide parmi la liste\n")

        return choice

    @staticmethod
    def show_round_number(actual_round: Round):
        print(f"     ########   {actual_round}    ########\n")

    @staticmethod
    def show_all_games_of_round(games_list: list):
        print(f"Liste des parties du round :")
        for game in games_list:
            print(game)
        print("\n")

    @staticmethod
    def show_round_lonely_player(actual_round: Round):
        if actual_round.tournament.odd_players_number():
            print(f"{actual_round.lonely_player} ne jouera pas durant ce Round.\n")

    @staticmethod
    def asks_result(game: Game) -> str:
        """
        :param game: an object Game
         Asks the result of the Game in param
        """

        choice = ""
        check_answer = False
        while not check_answer:
            print(f"Quel a été le résultat de la partie opposant {game.player_one} à {game.player_two}?\n")
            print(f"    1) Victoire de {game.player_one}")
            print(f"    2) Victoire de {game.player_two}")
            print("    3) Match nul\n")
            if settings.AUTOCOMPLETE:
                return str(random.randint(1, 3))

            choice = input("")
            choice = choice.strip()

            if choice == "1" or choice == "2" or choice == "3":
                check_answer = True

            else:
                print("Choix invalide")

        return choice

    @staticmethod
    def round_number() -> int:
        """View asking for the number total of round for the new tournament.
        By Default, there is 4 rounds"""
        number = ""
        check_answer = False
        while not check_answer:
            print("\n Nombre total de Rounds ?")
            number = input("")
            number = number.strip()

            if number == "" or int(number):
                check_answer = True

        if number == "":
            number = 4

        print(f"Le tournoi se déroulera sur {number} rounds\n")
        return int(number)

    @staticmethod
    def display_players_score(player_list: list, first_display=False):
        """
        :param first_display:
        :param player_list: list containing one or more players
        :return: print the total point of each player.
        """
        if first_display:
            print("Liste des joueurs prenant part au tournoi :\n")
        else:
            print("Classement actuel :\n")

        sorted_list = sorted(player_list, key=lambda x: x.total_point, reverse=True)
        for player in sorted_list:
            print(f"    {player} -> {player.total_point}")
        print("\n")
