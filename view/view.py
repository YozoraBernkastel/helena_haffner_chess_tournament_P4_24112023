from models.round import Round
from models.game import Game


class View:

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
                print("\nTournoi lancé, go go go !!!!")
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
        print(f"########   Round {actual_round.round_number}    ########")

    @staticmethod
    def asks_result(game: Game) -> str:
        """
        :param game: an object Game
         Asks the result of the Game in param
        """
        choice = ""
        check_answer = False
        while not check_answer:
            print("\nQuel a été le résultat ?\n")
            print(f"    1) Victoire de {game.player_one}")
            print(f"    2) Victoire de {game.player_two}")
            print("    3) Match nul\n")
            choice = input("")
            choice = choice.strip()

            if choice == "1" or choice == "2" or choice == "3":
                check_answer = True

            else:
                print("Choix invalide")

        return choice

    @staticmethod
    def round_number() -> int:
        number = ""
        check_answer = False
        while not check_answer:
            print("\n Nombre de Round total ?")
            number = input("")
            number = number.strip()

            if int(number) or number == "":
                check_answer = True

        if number == "":
            print("Le tournoi se déroulera sur 4 rounds")
            return 4

        print(f"Le tournoi se déroulera sur {number} rounds")
        return int(number)



    @staticmethod
    def display_players_score(player_list: list):
        """
        :param player_list: list containing one or more players
        :return: print the total point of each player.
        """
        sorted_list = sorted(player_list, key=lambda x: x.total_point, reverse=True)
        for player in sorted_list:
            print(f"{player} -> {player.total_point}")
