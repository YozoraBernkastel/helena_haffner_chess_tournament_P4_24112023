import random

from models.player import Player
from models.game import Game


class Round:

    def __init__(self, round_number: int, player_list: list, tournament_name: str):
        # générer un id ?????????????????
        self._round_number = round_number
        self._round_name = f"Round {round_number}"  # utile ?????
        self._player_list: list = player_list
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
    def create_games(self):  # penser à gérer les cas où le nombre de joueurs est impaire!!!!!!!!
        if self.round_number != 1:
            
            print("not number one T_T")

        else:
            random.shuffle(self._player_list)
            for player in self._player_list:  # comment gérer le cas où deux personnes portent le même nom ? Il faut utiliser le chess id mais où ?
                player_index: int = self.player_list.index(player)
                if player_index != self._player_list[-1] and player_index % 2 == 0:
                    game = Game(player, self._player_list[player_index + 1], self._round_name, self._tournament)
                    player.add_opponent_to_list(self._tournament, self._player_list[player_index + 1])
                    self._games_list.append(game)
                else:
                    player.add_opponent_to_list(self._tournament, self._player_list[player_index - 1])

