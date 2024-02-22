from models.round import Round
from models.player import Player
from export.export_tournament_data import export_tournament_data
import uuid
import datetime
import json
from os import path, stat


class Tournament:
    def __init__(self, tournament_name: str, location: str, number_of_players: int,  number_of_rounds: int,
                 creation=True):
        self._name: str = tournament_name
        self._location: str = location
        self._number_of_players: int = number_of_players
        self._players_list: list = []
        self._rounds_list: list = []
        self._lonely_players: list = []
        self._number_of_rounds: int = number_of_rounds
        self._actual_round: int = len(self._rounds_list)+1
        self._id: uuid = uuid.uuid1()
        self._description: str = ""
        self._starting_time: datetime = str(datetime.datetime.now().replace(microsecond=0))
        self._ending_time: datetime = "Le tournoi est en cours"
        self._export_name: str = f"{self.name}_{self.starting_time}"
        if creation:
            self.save()

    def __repr__(self):
        return f"Tournoi {self.name} de {self.location}"

    @property
    def name(self):
        return self._name

    @property
    def export_name(self):
        return self._export_name

    @property
    def location(self):
        return self._location

    @property
    def number_of_players(self):
        return self._number_of_players

    @property
    def players_list(self):
        return self._players_list

    @property
    def rounds_list(self):
        return self._rounds_list

    @property
    def lonely_players(self):
        return self._lonely_players

    @property
    def number_of_rounds(self):
        return self._number_of_rounds

    @property
    def actual_round_number(self):
        return self._actual_round

    @property
    def id(self):
        return self._id

    @property
    def starting_time(self):
        return self._starting_time

    @property
    def ending_time(self):
        return self._ending_time

    @property
    def description(self):
        return self._description

    # setter
    @name.setter
    def name(self, new):
        self._name = new

    @export_name.setter
    def export_name(self, new):
        self._export_name = new

    @id.setter
    def id(self, new):
        self._id = new

    @lonely_players.setter
    def lonely_players(self, new: Round):
        self._lonely_players.append(new)

    @starting_time.setter
    def starting_time(self, new):
        self._starting_time = new

    # not using the property setter as the function doesn't necessary need an argument to set ending_time
    def set_ending_time(self, new="") -> None:
        if new == "":
            self._ending_time = str(datetime.datetime.now().replace(microsecond=0))
            return
        self._ending_time = new

    @description.setter
    def description(self, new):
        self._description = new

    def increment_actual_round_number(self) -> None:
        self._actual_round = len(self.rounds_list) + 1

    # methods
    def reset_lonely_players_list(self) -> None:
        """
         # When all the players skipped a round, lonely players list should only remember
         the lonely player of the last round.
        :return: None
        """
        if len(self.lonely_players) >= len(self.players_list):
            self._lonely_players = [self.lonely_players[-1]]

    def odd_players_number(self) -> bool:
        return self.number_of_players % 2 != 0

    def create_round(self) -> Round:
        self.increment_actual_round_number()
        around_the_world = Round(self, self.actual_round_number)
        around_the_world.create_games()
        self.rounds_list.append(around_the_world)

        return around_the_world

    def add_round(self, new) -> None:
        if isinstance(new, Round):
            self._rounds_list.append(new)
            return

        if isinstance(new, list):
            [self.add_round(new) for r in new]

    def add_player(self, new, export=True) -> None:
        """
         If the attribute is a Player object, add it to the players_list.
         If the attribute is a list of Player object, add each of them to the players_list.
        """
        if isinstance(new, Player):
            self._players_list.append(new)
            if export:
                export_tournament_data(self)
            return

        if isinstance(new, list):
            [self.add_player(p, export) for p in new]

    @staticmethod
    def was_already_played(actual_player, opponent, game) -> bool:
        return ((game.player_one is actual_player and game.player_two is opponent)
                or (game.player_one is opponent and game.player_two is actual_player))

    def check_earlier_rounds(self, rounds_list, actual_player, opponent) -> bool:
        for r in rounds_list:
            for game in r.games_list:
                if self.was_already_played(actual_player, opponent, game):
                    return True
        return False

    def no_repeat_game(self, actual_player, round_possible_opponents: list) -> list:
        possible_opponents = []
        for opponent in round_possible_opponents:
            if len(self.rounds_list) < len(self.players_list) - 2:
                already_played = self.check_earlier_rounds(self.rounds_list, actual_player, opponent)
                if not already_played:
                    possible_opponents.append(opponent)
            else:
                already_played = self.check_earlier_rounds(self.rounds_list[-2:], actual_player, opponent)
                if not already_played:
                    possible_opponents.append(opponent)

        return possible_opponents

    def save(self) -> None:
        export_tournament_data(self)

    def convert_data(self) -> dict:
        tournament_info = dict()
        tournament_info["id"] = str(self.id)
        tournament_info["name"] = self.name
        tournament_info["location"] = self.location
        tournament_info["number of players"] = self.number_of_players
        tournament_info["total number of rounds"] = self.number_of_rounds
        tournament_info["description"] = self.description
        tournament_info["starting time"] = self.starting_time
        tournament_info["ending time"] = self.ending_time
        tournament_info["list of rounds"] = [around.convert_data() for around in self.rounds_list]

        return tournament_info

    @classmethod
    def reconstruction(cls, file_path: str, tournament_name):
        if path.exists(file_path) and stat(file_path).st_size != 0:
            with open(f"{file_path}/{tournament_name}.json", 'r') as f:
                tournament_data = json.load(f)
            tournament = Tournament(tournament_data["name"], tournament_data["location"],
                                    tournament_data["number of players"],
                                    tournament_data["total number of rounds"], False)
            tournament.id = tournament_data["id"]
            tournament.description = tournament_data["description"]
            tournament.starting_time = tournament_data["starting time"]
            tournament.set_ending_time(tournament_data["ending time"])
            tournament.export_name = f"{tournament_data['name']}_{tournament_data['starting time']}"

            players_list = Player.reconstruct_player(file_path)
            tournament.add_player(players_list, False)
            tournament.reconstruct_rounds(tournament_data["list of rounds"])
            if tournament.odd_players_number() and len(tournament.rounds_list) > 0:
                tournament.lonely_players = tournament.rounds_list[-1].lonely_player

            return tournament

    def reconstruct_rounds(self, rounds_data: list) -> None:
        for r in rounds_data:
            around = Round(self, int(r["name"]))
            around.starting_time = r["starting time"]
            around.ending_time = r["ending time"]
            if self.odd_players_number():
                for player in around.tournament.players_list:
                    if player.chess_id == r["player without game"]["id"]:
                        around.lonely_player = player

            around.reconstruct_games(r["games"])
            self.add_round(around)
