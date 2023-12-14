import random
from models.game import Game
import datetime
import operator as op


class Round:
    def __init__(self, tournament, round_number: int):
        self._round_number = round_number
        self._games_list = []
        self._tournament = tournament
        self._starting_time = datetime.datetime.now
        self._ending_time = None
        self._lonely_player = None

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

    @property
    def starting(self):
        return self._starting_time

    @property
    def ending(self):
        return self._ending_time

    @property
    def lonely_player(self):
        return self._lonely_player

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

    @ending.setter
    def ending(self, date):
        self._ending_time = datetime.date

    @lonely_player.setter
    def lonely_player(self, new):
        self._lonely_player = new

    # Methods
    @staticmethod
    def not_lonely_yet_list(self) -> list:
        return [i for i in self.tournament.players_list if op.countOf(self.tournament.lonely_players, i) == 0]

    def choose_lonely_player(self):
        not_lonely_list = self.not_lonely_yet_list(self)
        round_lonely_player = random.choice(not_lonely_list)
        self.tournament.lonely_players.append(round_lonely_player)
        self.lonely_player = round_lonely_player

    def set_round(self):
        players_list = self.tournament.players_list
        length_list = len(players_list)

        if length_list % 2 != 0:
            if len(self.tournament.lonely_players) >= len(self.tournament.players_list):
                # if there is more round than players number, reset the list when all of them skipped a round
                self.tournament.lonely_players.clear()

            self.choose_lonely_player()

        for i in range(0, length_list, 2):
            if length_list % 2 == 0 or i != length_list - 1:
                game = Game(players_list[i], players_list[i + 1], self)

                self._games_list.append(game)

    def create_games(self):
        if self.round_number != 1:
            self.tournament.players_list = self.sort_player_list()
        else:
            random.shuffle(self.tournament.players_list)

        self.set_round()

    def sort_player_list(self):
        return sorted(self.tournament.players_list, key=lambda x: x.total_point, reverse=True)
