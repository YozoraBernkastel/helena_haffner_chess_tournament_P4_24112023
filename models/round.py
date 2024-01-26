import random
import datetime
import operator as op
from models.game import Game


class Round:
    def __init__(self, tournament, round_number: int):
        self._round_name = round_number
        self._games_list = []
        self._tournament = tournament
        self._starting_time = str(datetime.datetime.now().replace(microsecond=0))
        self._ending_time = "Le round est en cours"
        self._lonely_player = None

    def __repr__(self):
        return f"Round {self.round_name}"

    # getter
    @property
    def round_name(self) -> int:
        return self._round_name

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
    def starting_time(self):
        return self._starting_time

    @property
    def ending_time(self):
        return self._ending_time

    @property
    def lonely_player(self):
        return self._lonely_player

    # setter
    @round_name.setter
    def round_name(self, new: int):
        self._round_name = new

    @games_list.setter
    def games_list(self, new: list):
        self._games_list = new

    @tournament.setter
    def tournament(self, new: str):
        self._tournament = new

    @ending_time.setter
    def ending_time(self, date):
        self._ending_time = str(date)

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
        self.choose_lonely_player()
        return [p for p in self.tournament.players_list if p is not self._lonely_player]

    def round_matchmaking(self, round_players: list):
        count = 0
        full_players_list = []

        for player in round_players:
            full_players_list.append(player)

        while len(round_players) > 1:
            count += 1
            for player in round_players:
                if count > 2:
                    self.games_list.clear()
                    round_players.clear()

                    for p in full_players_list:
                        round_players.append(p)

                    random.shuffle(round_players)
                    count = 0

                possible_opponents = [opponent for opponent in round_players if opponent is not player]
                possible_opponents = self.tournament.no_repeat_game(player, possible_opponents) if len(self.players_list) > 4 \
                    else possible_opponents
                if len(possible_opponents) == 0:
                    continue

                game = Game(player, possible_opponents[0], self)
                self._games_list.append(game)
                round_players.remove(player)
                round_players.remove(possible_opponents[0])

    def create_games(self):
        if len(self.games_list) > 0:
            self.games_list.clear()
        round_players_list = self.compute_lonely() if self.tournament.odd_players_number() else self.tournament.players_list
        round_players_list = self.sort_custom_player_list(round_players_list)
        self.round_matchmaking(round_players_list)

        self.tournament.lonely_players.append(self.lonely_player)

    @staticmethod
    def sort_custom_player_list(players_list):
        return sorted(players_list, key=lambda x: x.total_point, reverse=True)

    def sort_player_list(self):
        return self.sort_custom_player_list(self.tournament.players_list)

    def convert_data(self) -> dict:
        round_info = dict()
        round_info["name"] = self.round_name
        round_info["starting time"] = self.starting_time
        round_info["ending time"] = self.ending_time
        if self.tournament.odd_players_number():
            round_info["player without game"] = (f"{self.lonely_player.firstname} {self.lonely_player.family_name}"
                                                 f": {self.lonely_player.chess_id}")
        round_info["games"] = [game.convert_data() for game in self.games_list]
        return round_info
