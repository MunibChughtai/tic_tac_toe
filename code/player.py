class Player:
    def __init__(self, symbol, xposition=-1, yposition=-1):
        self._symbol=symbol
        self._xposition=xposition
        self._yposition=yposition
        #error handling needed

    def get_player_symbol(self):
        return self._symbol

    def get_player_position(self):
        return (self._xposition, self._yposition)