from models.player import Player


class Game:
    def __init__(self, player_one: Player, player_two: Player, round_name: str, tournament: str):
        # générer un id ?????????????????
        self._player_one = player_one
        self._player_two = player_two
        self._round_name = round_name
        self._tournament = tournament
        self._game_id = f"{round_name}-{player_one.chess_id}-{player_two}"
        self._game_result: str = "Le match n'est pas terminé"

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

    @round_name.setter
    def round_name(self, new: str):  # utile ????
        self._round_name = new

    @tournament.setter
    def tournament(self, new: str):  # utile ????
        self._tournament = new

    @game_result.setter
    def game_result(self, res: str):
        if res == "1":
            self._player_one.total_point = 1
            self._game_result = f"victoire du joueur {self._player_one}"
            return

        if res == "2":
            self._player_two.total_point = 1
            self._game_result = f"victoire du joueur {self._player_two}"
            return

        self._player_one.total_point = 0.5
        self._player_two.total_point = 0.5
        self._game_result = "match nul"



