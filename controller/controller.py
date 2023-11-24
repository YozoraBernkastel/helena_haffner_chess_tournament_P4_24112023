from models.player import Player
from models.round import Round
from view.view import View


class Controller:

    @staticmethod
    def link():
        choice = View.display_menu()

        if choice == "q" or choice == "Q":
            return

        selene = Player("Sélène", "Tsuki", 22, "15av4")
        agathe = Player("Agathe", "Observer", 38, "8846uh8")
        frederica = Player("Frederica", "Majou", 7803, "11111aaaa1111")
        fall = Player("Fall", "Paradox", 7524, "22222qb55555")

        player_list = [selene, agathe, frederica, fall]
        around_the_world = Round(1, player_list, "End of the Golden Witch")
        around_the_world.create_games()
        print(around_the_world.games_list)

