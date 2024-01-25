from models.round import Round
from models.player import Player
from export.export_tournament_data import export_tournament_data
import uuid
import datetime


class Tournament:
    def __init__(self, tournament_name: str, location: str, number_of_players: int,  number_of_rounds: int):
        self._name = tournament_name
        self._location = location
        self._number_of_players = number_of_players
        self._players_list: list = []
        self._rounds_list = []
        self._lonely_players: list = []
        self._number_of_rounds = number_of_rounds
        self._id = uuid.uuid1()
        # todo quel genre de description ? Une parlant de détails spécificiques décidés avant le tournoi ou plutôt
        #  des commentaires à faire suite au déroulé du tournoi (donc à ajouter en fin de tournoi) ?
        self._description = ""
        self._starting_time = str(datetime.datetime.now())
        self._ending_time = "Le tournoi est en cours"
        self.save()

    def __repr__(self):
        return f"Tournoi {self.name} de {self.location}"

    @property
    def name(self):
        return self._name

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

    @players_list.setter
    def players_list(self, new) -> None:
        """
         If the attribute is a Player object, add it to the players_list.
         If the attribute is a list of Player object, add each of them to the players_list.
        """
        if type(new) == Player:
            self._players_list.append(new)
            export_tournament_data(self)
            return

        if type(new) == list:
            for p in new:
                self.players_list = p

    @rounds_list.setter
    def rounds_list(self, new: Round):
        self._rounds_list.append(new)

    @lonely_players.setter
    def lonely_players(self, new: Round):
        self._lonely_players.append(new)

    def set_ending_time(self):
        self._ending_time = str(datetime.datetime.now())

    @description.setter
    def description(self, new):
        self._description = new

    # methods
    def odd_players_number(self) -> bool:
        return self.number_of_players % 2 != 0

    def create_round(self):
        around_the_world = Round(self, len(self.rounds_list) + 1)
        around_the_world.create_games()
        games_list = around_the_world.games_list

        self.rounds_list.append(around_the_world)

        return games_list

    @staticmethod
    def was_already_played(actual_player, opponent, game) -> bool:
        return((game.player_one is actual_player and game.player_two is opponent) or
               (game.player_one is opponent and game.player_two is actual_player))

    def no_repeat_game(self, actual_player, round_possible_opponents: list) -> list:
        possible_opponents = []
        for opponent in round_possible_opponents:
            already_played = False
            if len(self.rounds_list) < len(self.players_list) - 2:
                for r in self.rounds_list:
                    for game in r.games_list:
                        if self.was_already_played(actual_player, opponent, game):
                            already_played = True
                            break
                if not already_played:
                    possible_opponents.append(opponent)
            else:
                for r in self.rounds_list[-2:]:
                    for game in r.games_list:
                        if ((game.player_one is actual_player and game.player_two is opponent) or
                                (game.player_one is opponent and game.player_two is actual_player)):
                            already_played = True
                            break
                if not already_played:
                    possible_opponents.append(opponent)
        return possible_opponents

    def save(self):
        export_tournament_data(self)

    def convert_data(self) -> dict:
        tournament_info = dict()
        tournament_info["id"] = str(self.id)
        tournament_info["name"] = self.name
        tournament_info["location"] = self.location
        tournament_info["number_of_players"] = self.number_of_players
        tournament_info["Total Number of Rounds"] = self.number_of_rounds
        tournament_info["description"] = self.description
        tournament_info["starting time"] = self.starting_time
        tournament_info["ending time"] = self.ending_time
        tournament_info["list of rounds"] = [around.convert_data() for around in self.rounds_list]
        return tournament_info





