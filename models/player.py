from export.export_player_data import export_player_list


class Player:
    def __init__(self, first_name: str, family_name: str, birthdate, player_chess_id: str):
        self._firstname = first_name
        self._family_name = family_name
        self._birthdate = birthdate
        self._player_chess_id = player_chess_id
        self._total_point: int = 0
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
    def total_point(self):
        return self._total_point

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

    @total_point.setter
    def total_point(self, new: int):
        self._total_point += new

    # Methods
    def player_save(self):
        export_player_list(self)

    def format_data(self) -> dict:
        player_info = dict()
        player_info["id"] = self.chess_id
        player_info["name"] = self.family_name
        player_info["firstname"] = self.firstname
        player_info["birthdate"] = self.birthdate
        player_info["total Points"] = self.total_point
        return player_info
