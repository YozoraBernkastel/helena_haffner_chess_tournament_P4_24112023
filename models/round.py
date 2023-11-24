from models.player import Player
from models.game import Game

class Round:

    def __init__(self, round_number: int, player_list: list, tournament_name: str):
        self._round_number = round_number
        self._round_name = f"Round {round_number}"  # utile ?????
        self._player_list = player_list
        self._games_list = []
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

    @tournament.setter
    def tournament(self, new: str):
        self._tournament = new

    # Methods
    def create_games(self):
        if self.round_number != 1:
            print("not number one T_T")

        else:
            print("shuffle the cards ... hmm the players")
