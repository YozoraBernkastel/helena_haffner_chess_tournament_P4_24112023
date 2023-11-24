from models.player import Player


class Game:
    def __init__(self, player_one: Player, player_two: Player, round_name: str, tournament: str):
        # générer un id ?????????????????
        self._player_one = player_one
        self._player_two = player_two
        self._round_name = round_name
        self._tournament = tournament

    def __repr__(self):
        return (f"{self._player_one} vs {self._player_two} lors du "
                f"{self._round_name} du tournoi {self._tournament}")

    # getter
    @property
    def player_one(self):
        return self._player_one

    @property
    def player_two(self):
        return self._player_two

    @property
    def round_name(self):
        return self._round_name

    @property
    def tournament(self):
        return self._tournament

    # setter
    @player_one.setter
    def player_one(self, new: Player):
        self._player_one = new

    @player_two.setter
    def player_two(self, new: Player):
        self._player_two = new

    @round_name.setter
    def round_name(self, new: str):  # utile ????
        self._round_name = new

    @tournament.setter
    def tournament(self, new: str):  # utile ????
        self._tournament = new

    # Methods
    def victory_player(self, player="draw"):
        if player == "draw":
            self._player_one.total_point(0.5)
            self._player_two.total_point(0.5)
        if player == self._player_one:
            self._player_one.total_point(1)
        if player == self.player_two:
            self._player_two.total_point(1)
