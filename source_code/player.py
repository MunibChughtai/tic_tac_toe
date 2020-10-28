class Player:
    def __init__(self, symbol, x_coordinate=-1, y_coordinate=-1):
        self._symbol=symbol
        self._x_coordinate=x_coordinate
        self._y_coordinate=y_coordinate

    def get_player_symbol(self):
        return self._symbol

    def get_player_coordinate(self):
        return (self._x_coordinate, self._y_coordinate)