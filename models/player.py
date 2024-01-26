from export.export_player_data import export_player_list


class Player:
    def __init__(self, first_name: str, family_name: str, birthdate, player_chess_id: str, total_points):
        self._firstname = first_name
        self._family_name = family_name
        self._birthdate = birthdate
        self._player_chess_id = player_chess_id
        self._total_points = total_points
        self._tournament_points = 0
        self.player_save()

    def __repr__(self):
        return f"{self._firstname} {self._family_name} ({self._player_chess_id})"

    # getter
    @property
    def firstname(self) -> str:
        return self._firstname

    @property
    def family_name(self) -> str:
        return self._family_name

    @property
    def birthdate(self):
        # todo il faut un format précis
        return self._birthdate

    @property
    def chess_id(self) -> str:
        return self._player_chess_id

    @property
    def total_points(self):
        return self._total_points

    @property
    def tournament_points(self):
        return self._tournament_points

    # setter
    @firstname.setter
    def firstname(self, new):
        self._firstname = new

    @family_name.setter
    def family_name(self, new: str):
        self._family_name = new

    @birthdate.setter
    def birthdate(self, new: int):
        self._birthdate = new

    @chess_id.setter
    def chess_id(self, new: str):
        self._player_chess_id = new

    @total_points.setter
    def total_points(self, new: int):
        self._total_points += new

    @tournament_points.setter
    def tournament_points(self, new: int):
        self._tournament_points += new

    # Methods
    def player_save(self):
        export_player_list(self)

    def format_data(self) -> dict:
        player_info = dict()
        player_info["id"] = self.chess_id
        player_info["name"] = self.family_name
        player_info["firstname"] = self.firstname
        player_info["birthdate"] = self.birthdate
        player_info["total points"] = self.total_points
        return player_info
