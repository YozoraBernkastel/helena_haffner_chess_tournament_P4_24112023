from models.round import Round


class Tournament:
    def __init__(self, tournament_name: str, players_list: list):
        # générer un id ?????????????????
        # todo mettre en place le fait
        self._name = tournament_name
        self._players_list: list = players_list
        self._actual_round = 0
        self._rounds_list = []
        self._lonely_players: list = []

    def __repr__(self):
        return f"Tournoi {self._name}"

    @property
    def name(self):
        return self._name

    @property
    def players_list(self):
        return self._players_list

    @property
    def actual_round(self):
        return self._actual_round

    @property
    def rounds_list(self):
        return self._rounds_list

    @property
    def lonely_players(self):
        return self._lonely_players

    @name.setter
    def name(self, new):
        self._name = new

    @players_list.setter
    def players_list(self, new):
        self._players_list = new

    @actual_round.setter
    def actual_round(self, new):
        self._actual_round = new

    @rounds_list.setter
    def rounds_list(self, new: Round):
        self._rounds_list.append(new)

    @lonely_players.setter
    def lonely_players(self, new: Round):
        self._lonely_players.append(new)


