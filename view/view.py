class View:

    @staticmethod
    def display_menu() -> str:
        choice =""
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
                print("\nCette commande option n'existe malheureusement pas, veuillez sélectionner une commande valide parmi la liste\n")

        return choice
