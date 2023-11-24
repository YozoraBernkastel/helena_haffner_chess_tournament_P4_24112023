from models.player import Player


class Game:
    def __init__(self, player_one: Player, player_two: Player):  # ajouter round ???? Pas nécessaire je suppose, à voir lorsqu'il faudra afficher le tout
        self._player_one = player_one
        self._player_two = player_two

    # getter
    @property
    def player_one(self):
        return self._player_one

    @property
    def player_two(self):
        return self._player_two

    # setter
    @player_one.setter
    def player_one(self, new: Player):
        self._player_one = new

    @player_two.setter
    def player_two(self, new: Player):
        self._player_two = new


    # Methods
