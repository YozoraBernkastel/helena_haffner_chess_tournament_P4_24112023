from models.round import Round
import uuid


class Tournament:
    # nombre de round à définir !!! donc osef game_repeat_number
    def __init__(self, tournament_name: str, location: str, players_list: list, game_repeat_number: int):
        self._name = tournament_name
        self._location = location
        self._players_list: list = players_list
        self._rounds_list = []
        self._lonely_players: list = []
        self._game_repeat = game_repeat_number
        self._id = uuid.uuid1()
        # todo quel genre de description ? Une parlant de détails spécificiques décidés avant le tournoi ou plutôt
        #  des commentaires à faire suite au déroulé du tournoi (donc à ajouter en fin de tournoi) ?
        self._description = ""

    def __repr__(self):
        return f"Tournoi {self.name} de {self.location}"

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

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
    def id(self):
        return self._id

    # setter
    @name.setter
    def name(self, new):
        self._name = new

    @players_list.setter
    def players_list(self, new):
        self._players_list = new

    @rounds_list.setter
    def rounds_list(self, new: Round):
        self._rounds_list.append(new)

    @lonely_players.setter
    def lonely_players(self, new: Round):
        self._lonely_players.append(new)

    # methods
    def create_round(self):
        around_the_world = Round(self, len(self.rounds_list) + 1)
        around_the_world.create_games()
        games_list = around_the_world.games_list

        self.rounds_list.append(around_the_world)

        return games_list

