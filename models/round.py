import random
from models.game import Game


class Round:
    def __init__(self, tournament, round_number: int):
        # générer un id ?????????????????
        self._round_number = round_number
        self._games_list = []
        self._tournament = tournament

    def __repr__(self):
        return f"Round {self.round_number}"

    # getter
    @property
    def round_number(self) -> int:
        return self._round_number

    @property
    def games_list(self) -> list:
        return self._games_list

    @property
    def players_list(self):
        return self.tournament.players_list

    @property
    def tournament(self):
        return self._tournament

    # setter
    @round_number.setter
    def round_number(self, new: int):
        self._round_number = new

    @games_list.setter
    def games_list(self, new: list):
        self._games_list = new

    @tournament.setter
    def tournament(self, new: str):
        self._tournament = new

    # Methods
    def set_round(self):
        length_list = len(self.tournament.players_list)
        players_list = self.tournament.players_list

        if len(players_list) % 2 != 0:
            self.tournament.lonely_players.append(players_list[-1].chess_id)
            print(f"lonely player : {self._tournament.lonely_players}")

        for i in range(0, length_list, 2):
            if len(players_list) % 2 == 0 or i != length_list - 1:
                game = Game(players_list[i], players_list[i + 1], self)

                self._games_list.append(game)

    def create_games(self):
        if self.round_number != 0:
            self.tournament.players_list = self.sort_player_list()
        else:
            random.shuffle(self.tournament.players_list)

        self.set_round()

    def sort_player_list(self):
        return sorted(self.tournament.players_list, key=lambda x: x.total_point, reverse=True)
