from view.view import View
from models.player import Player
from models.round import Round

def main():

    Selene = Player("Sélène", "Aoyama", 22, "15av4")
    Agathe = Player("Agathe", "Ombreux", 38, "8846uh8")
    Frederica = Player("Frederica", "Pantin", 7803, "11111aaaa1111")
    Fall = Player("Fall", "Parado", 7524, "22222qb55555")
    View.display_menu()


if __name__ == '__main__':
    main()
