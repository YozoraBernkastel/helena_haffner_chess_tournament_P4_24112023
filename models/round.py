import random
from models.game import Game


class Round:
    # todo remplacer tournament_name par l'objet Tournament
    def __init__(self, round_number: int, player_list: list, lonely_players_list: list, tournament_name: str):
        # générer un id ?????????????????
        self._round_number = round_number
        self._round_name = f"Round {round_number}"  # utile ?????
        self._player_list: list = player_list
        self._games_list = []
        self._lonely_players_list = lonely_players_list
        self._tournament = tournament_name  # utile ??????

    # getter
    @property
    def round_number(self) -> int:
        return self._round_number

    @property
    def round_name(self) -> str:  # utile ?????
        return self._round_name

    @property
    def player_list(self) -> list:
        return self._player_list

    @property
    def games_list(self) -> list:
        return self._games_list

    @property
    def lonely_list(self) -> list:
        return self._lonely_players_list

    @property
    def tournament(self) -> str:  # utile ?????
        return self._tournament

    # setter
    @round_number.setter
    def round_number(self, new: int):
        self._round_number = new

    @round_name.setter
    def round_name(self, new: str):
        self._round_name = new

    @player_list.setter
    def player_list(self, new: list):
        self._player_list = new

    @games_list.setter
    def games_list(self, new: list):
        self._games_list = new

    @lonely_list.setter
    def lonely_list(self, new: list):
        self._lonely_players_list = new

    @tournament.setter
    def tournament(self, new: str):
        self._tournament = new

    # Methods
    def not_first_round(self):
        player_list = self.sort_player_list()
        print(player_list)
        for player in player_list:
            player_index: int = self.player_list.index(player)
            # Ne pas oublier que les listes en param de la classe sont en réaloté des pointeurs
            # donc attention à ne pas pop de joueurs.
            # Cela facilite la mise à jour de la lonely list du tournoi !!

    def first_round(self):
        random.shuffle(self._player_list)
        length_list = len(self._player_list)

        if len(self._player_list) % 2 != 0:
            self.lonely_list.append(self._player_list[-1].chess_id)
            print(f"lonely player : {self.lonely_list}")

        for i in range(0, length_list, 2):

            if len(self._player_list) % 2 == 0 or i != length_list - 1:
                game = Game(self._player_list[i], self._player_list[i + 1], self._round_name, self._tournament)

            # todo inutile de faire une opponent list -> boucle directement sur les round du tournoi si besoin de l'info
                self._player_list[i].add_opponent_to_list(self._tournament, self._player_list[i + 1])
                self._player_list[i + 1].add_opponent_to_list(self._tournament, self._player_list[i])
                self._games_list.append(game)

    def create_games(self):
        if self.round_number != 1:
            self.not_first_round()
        else:
            self.first_round()

    def sort_player_list(self):
        return sorted(self._player_list, key=lambda x: x.total_point, reverse=True)
