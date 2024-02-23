import random
from models.tournament import Tournament
from models.round import Round
from models.game import Game
from settings import settings


class View:
    @staticmethod
    def tournament_name() -> str:
        print("\nComment souhaitez-vous nommer le tournoi ?")
        name_choice = input("")

        return name_choice

    @staticmethod
    def tournament_location() -> str:
        print("\nOù se déroule le tournoi ?")
        location_choice = input("")
        return location_choice

    @staticmethod
    def quit_option_display() -> None:
        print("   Q) pour quitter")

    @staticmethod
    def unknown_option():
        print(
            "\nCette option n'existe malheureusement pas,"
            " veuillez sélectionner une commande valide parmi la liste\n")

    @staticmethod
    def display_menu() -> str:
        """
        Offers to the user the possibility to create a tournament, to display the statistics or to quit.
        """
        choice = ""
        check_answer = False

        while not check_answer:
            print("\nBienvenue ! Que souhaitez-vous faire ?\n")
            print("   1) Créer un tournoi")
            print("   2) Voir les statistiques")
            print("   3) Continuer un tournoi en cours")
            View.quit_option_display()
            choice = input("")
            choice = choice.strip()

            if choice == "1":
                print("\nNouveau tournoi lancé !!!")
                check_answer = True

            elif choice == "2" or choice == "3":
                check_answer = True

            elif choice == "Q" or choice == "q":
                break
            else:
                View.unknown_option()

        return choice

    @staticmethod
    def tournament_description() -> str:
        print("Description du tournoi (touche entrée pour passer) :")
        return input("")

    @staticmethod
    def number_of_players() -> int:
        players_number = ""
        while players_number == "" or not players_number.isdigit() or int(players_number) < 2:
            print("Combien de joueurs participeront au tournoi ?")
            players_number = input("")
        return int(players_number)

    @staticmethod
    def asks_chess_id(registration_number) -> str:
        print(f"\nVeuillez entrer les informations du joueur n° {registration_number}")
        print("Identifiant national d’échecs :")
        return input("")

    @staticmethod
    def players_registration(tournament: Tournament) -> tuple:
        print("Nom de famille :")
        name = input("")
        print("Prénom : ")
        firstname = input("")
        print("Date de naissance (au format jj/mm/aaaa) :")
        birthdate = input("")

        return firstname, name, birthdate

    @staticmethod
    def show_round_number(actual_round: Round) -> None:
        print(f"     ########   {actual_round}    ########\n")

    @staticmethod
    def show_all_games_of_round(games_list: list) -> None:
        print("Liste des parties du round :")
        for game in games_list:
            print(game)
        print("\n")

    @staticmethod
    def show_round_lonely_player(actual_round: Round) -> None:
        if actual_round.tournament.odd_players_number():
            print(f"{actual_round.lonely_player} ne jouera pas durant ce Round.\n")

    @staticmethod
    def display_round_info(around: Round) -> None:
        View.show_round_number(around)
        View.show_round_lonely_player(around)
        View.show_all_games_of_round(around.games_list)

    @staticmethod
    def asks_result(game: Game) -> str:
        choice = ""
        check_answer = False
        while not check_answer:
            print(f"Quel a été le résultat de la partie opposant {game.player_one} à {game.player_two}?\n")
            print(f"    1) Victoire de {game.player_one}")
            print(f"    2) Victoire de {game.player_two}")
            print("    3) Match nul\n")

            if settings.AUTOCOMPLETE:
                rand = str(random.randint(1, 3))
                print(rand)
                return rand

            choice = input("")
            choice = choice.strip()

            if choice == "1" or choice == "2" or choice == "3":
                check_answer = True
            else:
                print("Choix invalide")

        return choice

    @staticmethod
    def round_number() -> int:
        """
        View asking for the number total of round for the new tournament.
        By Default, there is 4 rounds
        """
        number = ""
        check_answer = False
        while not check_answer:
            print("\nNombre total de Rounds ?")
            number = input("")
            number = number.strip()

            if number == "" or int(number):
                check_answer = True

        if number == "":
            number = 4

        print(f"Le tournoi se déroulera sur {number} rounds\n")
        return int(number)

    @staticmethod
    def display_players_score(player_list: list, first_display=False, last_display=False) -> None:
        """
        :param last_display: change introduction print for the last display of the tournament
        :param first_display: change introduction print for the first display of the tournament
        :param player_list: list containing one or more players
        :return: print the total point of each player.
        """
        if first_display:
            print("Liste des joueurs prenant part au tournoi :\n")
            sorted_list = sorted(player_list, key=lambda x: x.total_points, reverse=True)
            for player in sorted_list:
                print(f"    {player} -> {player.total_points} points")
        else:
            print("Classement actuel :\n") if not last_display else print("Classement final : \n")

            sorted_list = sorted(player_list, key=lambda x: x.tournament_points, reverse=True)
            for player in sorted_list:
                print(f"    {player} -> {player.tournament_points} points")

        print("\n")

    @staticmethod
    def display_lonely_players_list(lonely_players_list) -> None:
        print("liste des joueurs n'ayant pas joués durant les derniers rounds: ")
        print(lonely_players_list)
        print("NOTE: Affichage n'existant que pour présenter le fonctionnement "
              "d'un tournoi avec des joueurs impairs\n\n")

    @staticmethod
    def display_players_id_error(chess_id: str, loop_count: int, already_registered: bool, wrong_format: bool):
        if loop_count == 0:
            return
        if chess_id == "":
            print("Vous n'avez entrez aucun identifiant.\n")
            return
        if already_registered:
            print(f"Le joueur id {chess_id} a déjà été ajouté à la "
                  f"liste des joueurs prenant part au tournoi.\n")
            return
        if wrong_format:
            print(f"L'id {chess_id} ne respecte pas la norme concernant "
                  f"les identifiants nationaux d'échecs "
                  f"(deux lettres suivies de cinq chiffres).\n")

    @staticmethod
    def known_player_prompt(chess_id) -> None:
        print(f"Les informations du joueur id {chess_id} sont déjà connues !\n")

    @staticmethod
    def no_tournament_found() -> None:
        print("La base de données est vide")

    @staticmethod
    def display_tournaments_list(tournaments_list: list) -> None:
        if len(tournaments_list) == 0:
            View.no_tournament_found()
            return

        print("Liste des tournois enregistrés :\n")
        [print(f"   - {tournament}") for tournament in tournaments_list]

    @staticmethod
    def choose_tournament_to_display() -> str:
        print("\nChoisissez un tournoi parmi ceux dans la liste")
        return input("")

    @staticmethod
    def display_report_general_menu() -> str:
        choice = ""
        check_answer = False
        while not check_answer:
            print("Quelles informations souhaitez-vous consulter ?\n")
            print("   1) Afficher le classement général")
            print("   2) Afficher la liste de tous les joueurs par ordre alphabétique")
            print("   3) Afficher la liste de tous les tournois")
            print("   4) Consulter les informations d'un tournoi")
            View.quit_option_display()
            choice = input("")

            valid_choices = ["1", "2", "3", "4", "q", "Q"]
            if any(choice == valid for valid in valid_choices):
                check_answer = True
            else:
                print("\nChoix invalide\n")

        return choice

    @staticmethod
    def tournament_folder_not_found() -> None:
        print("Le dossier du tournoi n'a pas été trouvé.")
        print("Peut-être a-t-il été supprimé, déplacé ou renommé entre le moment où "
              "la liste des tournoi a été faite et celui où vous avez fait votre choix")

    @staticmethod
    def display_tournament_info(tournament: Tournament) -> None:
        print(f"Nom du Tournoi : {tournament.name}")
        print(f"Localisation : {tournament.location}")
        print(f"Description : {tournament.description}")
        print(f"Date de début : {tournament.starting_time}")
        print(f"Date de fin : {tournament.ending_time}")
        print(f"Nombre de joueurs : {tournament.number_of_players}")
        print(f"Nombre de tours : {tournament.number_of_rounds}\n")

    @staticmethod
    def this_tournament_menu() -> str:
        print("Souhaitez-vous faire autre chose ?\n")
        check_answer = False
        choice = ""
        while not check_answer:
            print("   1) Consulter la liste des joueurs")
            print("   2) Consulter la liste des tours")
            View.quit_option_display()
            choice = input("")

            if choice == "1" or choice == "2" or choice == "Q" or choice == "q":
                check_answer = True
            else:
                View.unknown_option()
        return choice

    @staticmethod
    def display_players_info(players_list: list) -> None:
        for p in players_list:
            print(f"Nom : {p.family_name}")
            print(f"Prénom : {p.firstname}")
            print(f"ID : {p.chess_id}")
            print(f"Date de naissance : {p.birthdate}")
            print(f"Points : {p.total_points}\n")

    @staticmethod
    def display_rounds_info(rounds_list: list, odd_players: int) -> None:
        if len(rounds_list) == 0:
            print("Le premier tour n'a pas encore commencé.\n")
            return

        for r in rounds_list:
            print(f"Tour n° {r.round_name}")
            print(f"  Début du tour : {r.starting_time}")
            print(f"  Fin du tour : {r.ending_time}")
            if odd_players:
                print(f"  Joueur sans partie : {r.lonely_player}")

            for i, game in enumerate(r.games_list):
                print(f"\n  Partie n°{i + 1} :")
                print(f"    {game.player_one} contre {game.player_two}")
                print("    La partie n'est pas terminée") if not game.game_result \
                    else print(f"    {game.game_result}")
            print("")

    @staticmethod
    def all_tournaments_are_finished() -> None:
        print("Il n'y a aucun tournoi en cours !")
