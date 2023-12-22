import random
import datetime
import operator as op

from models.game import Game


class Round:
    def __init__(self, tournament, round_number: int):
        self._round_number = round_number
        self._games_list = []
        self._tournament = tournament
        self._starting_time = datetime.datetime.now()
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
        self._ending_time = date

    @lonely_player.setter
    def lonely_player(self, new):
        self._lonely_player = new

    # Methods
    @staticmethod
    def not_lonely_yet_list(self) -> list:
        return [i for i in self.tournament.players_list if op.countOf(self.tournament.lonely_players, i) == 0]

    # remove the lonely player of the round to the players_list
    def choose_lonely_player(self):
        not_lonely_list = self.not_lonely_yet_list(self)
        round_lonely_player = random.choice(not_lonely_list)
        self.lonely_player = round_lonely_player

    def compute_lonely(self):
        # if there is more rounds than players number,
        if len(self.tournament.lonely_players) >= len(self.tournament.players_list):
            # reset the lonely players list when all of them skipped a round
            self.tournament.lonely_players.clear()
            print("coucou")
        self.choose_lonely_player()
        return [p for p in self.tournament.players_list if p is not self._lonely_player]

    def first_round(self, round_players: list):
        for i in range(0, len(round_players), 2):
            if len(round_players) % 2 == 0 or i != len(round_players) - 1:
                game = Game(round_players[i], round_players[i + 1], self)
                self._games_list.append(game)

    def not_first_round(self, round_players: list) -> bool:
        for player in round_players:
            possible_opponents = self.tournament.no_repeat_game(player, round_players)
            if len(possible_opponents) == 0:
                return False
            game = Game(player, possible_opponents[0], self)
            self._games_list.append(game)
            round_players.remove(player)
            round_players.remove(possible_opponents[0])
        return True

    def create_games(self):
        # relaunch all the round if there is a problem during the construction of it
        approved_round = False
        # todo ne règle pas le problème si le problème arrive alors qu'il ne reste qu'un joueur pouvant être observateur !!
        while not approved_round:
            if len(self.games_list) > 0:
                self.games_list.clear()
            round_players_list = self.compute_lonely() if self.tournament.odd_players_number() else self.tournament.players_list
            if self.round_number != 1:
                self.tournament.players_list = self.sort_player_list()
                approved_round = self.not_first_round(round_players_list)
            else:
                random.shuffle(self.tournament.players_list)
                self.first_round(round_players_list)
                approved_round = True

        self.tournament.lonely_players.append(self.lonely_player)

    def sort_player_list(self):
        return sorted(self.tournament.players_list, key=lambda x: x.total_point, reverse=True)
