class Player:
    def __init__(self, first_name: str, family_name: str, age: int, player_chess_id: str):
        # générer un id ?????????????????
        self._first_name = first_name
        self._family_name = family_name
        self._age = age
        self._player_chess_id = player_chess_id
        self._opponent_list: dict = {}
        self._total_point: int = 0

    def __repr__(self):
        return f"{self._first_name} {self._family_name}"  #: {self._player_chess_id}"

    # getter
    @property
    def first_name(self) -> str:
        return self._first_name

    @property
    def family_name(self) -> str:
        return self._family_name

    @property
    def age(self) -> int:
        return self._age

    @property
    def chess_id(self) -> str:
        return self._player_chess_id

    @property
    def opponent_list(self) -> dict:
        return self.opponent_list

    @property
    def total_point(self):
        return self._total_point

    # setter
    @first_name.setter
    def first_name(self, new):
        self._first_name = new

    @family_name.setter
    def family_name(self, new: str):
        self._family_name = new

    @age.setter
    def age(self, new: int):
        self._age = new

    @chess_id.setter
    def chess_id(self, new: str):
        self._player_chess_id = new

    @opponent_list.setter
    def opponent_list(self, new: list):
        self._opponent_list = new

    @total_point.setter
    def total_point(self, new: int):
        self._total_point += new

    # Methods
    def add_opponent_to_list(self, tournament_name: str, opponent):
        self._opponent_list[tournament_name] = opponent

