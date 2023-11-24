class Player:
    def __init__(self, first_name, name, age, player_chess_id):
        self._first_name = first_name
        self._name = name
        self._age = age
        self._player_chess_id = player_chess_id

    def __repr__(self):
        return f"{self._first_name} {self._name} : {self._player_chess_id}"

    # getter
    @property
    def first_name(self):
        return self._first_name

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def chess_id(self):
        return self._player_chess_id

    # setter
    @first_name.setter
    def first_name(self, new):
        self._first_name = new

    @name.setter
    def name(self, new):
        self._name = new

    @age.setter
    def age(self, new):
        self._age = new

    @chess_id.setter
    def chess_id(self, new):
        self._player_chess_id = new


