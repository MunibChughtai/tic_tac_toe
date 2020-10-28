class Player:
    def __init__(self, symbol, x_position=-1, y_position=-1):
        self._symbol=symbol
        self._x_position=x_position
        self._y_position=y_position

    def get_player_symbol(self):
        return self._symbol

    def get_player_position(self):
        return (self._x_position, self._y_position)