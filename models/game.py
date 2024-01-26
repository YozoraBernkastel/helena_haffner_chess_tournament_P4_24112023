from models.player import Player


class Game:
    def __init__(self, player_one: Player, player_two: Player, round_object):
        self._player_one = player_one
        self._player_two = player_two
        self._round = round_object
        self._tournament = round_object.tournament
        self._game_id = f"{round}-{player_one.chess_id}-{player_two}"
        self._game_result: str = "La partie n'est pas terminée"

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
    def game_id(self):
        return self._game_id

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

    @belong_round.setter
    def belong_round(self, new: str):  # utile ????
        self._round = new

    @tournament.setter
    def tournament(self, new: str):  # utile ????
        self._tournament = new

    @game_result.setter
    def game_result(self, res: str):
        if res == "1":
            self._player_one.total_points = 1
            self._player_one.tournament_points = 1
            self._game_result = f"victoire de {self._player_one}"
            return

        if res == "2":
            self._player_two.total_points = 1
            self._player_two.tournament_points = 1
            self._game_result = f"victoire de {self._player_two}"
            return

        self._player_one.total_points = 0.5
        self._player_one.tournament_points = 0.5
        self._player_two.total_points = 0.5
        self._player_two.tournament_points = 0.5
        self._game_result = "match nul"

    # method
    def convert_data(self) -> dict:
        game_info = dict()
        game_info["player one"] = f"{self.player_one.firstname} {self.player_one.family_name} : {self.player_one.chess_id}"
        game_info["player_two"] = f"{self.player_two.firstname} {self.player_two.family_name}: {self.player_two.chess_id}"
        game_info["result"] = self._game_result
        return game_info
