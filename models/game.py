from models.player import Player


class Game:
    def __init__(self, player_one: Player, player_two: Player, round_object):
        self._player_one = player_one
        self._player_two = player_two
        self._round = round_object
        self._tournament = round_object.tournament
        self._game_result = False

    def __repr__(self):
        return f"{self._player_one} vs {self._player_two}"

    # getter
    @property
    def player_one(self):
        return self._player_one

    @property
    def player_two(self):
        return self._player_two

    @property
    def belong_round(self):
        return self._round

    @property
    def tournament(self):
        return self._tournament

    @property
    def game_result(self):
        return self._game_result

    # setter
    @player_one.setter
    def player_one(self, new: Player):
        self._player_one = new

    @player_two.setter
    def player_two(self, new: Player):
        self._player_two = new

    @tournament.setter
    def tournament(self, new: str):
        self._tournament = new

    @game_result.setter
    def game_result(self, result):
        self._game_result = result

    def victory_points(self, player: Player):
        player.total_points = 1.0
        player.tournament_points = 1.0
        self.game_result = f"victoire de {player}"

    def stalemate_points(self):
        self._player_one.total_points = 0.5
        self._player_one.tournament_points = 0.5
        self._player_two.total_points = 0.5
        self._player_two.tournament_points = 0.5
        self.game_result = "match nul"

    def set_result(self, res: str):
        if res == "1":
            self.victory_points(self.player_one)
            return

        if res == "2":
            self.victory_points(self.player_two)
            return

        self.stalemate_points()

    # method
    def convert_data(self) -> dict:
        game_info = dict()
        game_info["player one"] = self.player_one.format_data(False)
        game_info["player two"] = self.player_two.format_data(False)
        game_info["result"] = self.game_result

        return game_info
