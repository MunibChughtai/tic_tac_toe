from source_code.player import Player


class Game_Board:
    def __init__(self):
        self._board = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]
        self._moves_left = len(self._board) * len(self._board)

    # this cannot be tested,, only visual testing possible
    def display_board(self):
        for board_row in self._board:
            print('  '.join(
                [
                 (board_coordinates.get_player_symbol() if isinstance(board_coordinates, Player) else board_coordinates)
                 for board_coordinates in board_row
                 ]
                            ))

    def display_board_message(self):
        print("here's the current board:")

    def _is_any_move_left(self):
        return self._moves_left

    # this cannot be tested,, only visual testing possible
    def assign_player_move_on_board(self, player):
        x_coordinate, y_coordinate = player.get_player_coordinate()
        self._board[x_coordinate - 1][y_coordinate - 1] = player
        self._moves_left -= 1

    def _extract_x_and_y_coordinates(self, coordinates_to_check):
        x_coordinate = int(coordinates_to_check[:coordinates_to_check.find(',')])
        y_coordinate = int(coordinates_to_check[coordinates_to_check.find(',') + 1:])
        return (x_coordinate - 1, y_coordinate - 1)

    def _extract_x_or_y_coordinate(self, coordinates_to_check, coordinate_to_extract):
        x_coordinate, y_coordinate = self._extract_x_and_y_coordinates(coordinates_to_check)
        if coordinate_to_extract=='x':
            return x_coordinate
        elif coordinate_to_extract=='y':
            return y_coordinate

    def are_board_coordinates_vacant(self, coordinates_to_check):
        x_coordinate, y_coordinate = self._extract_x_and_y_coordinates(coordinates_to_check)
        if self._board[x_coordinate][y_coordinate] == '.':
            return True
        else:
            return False

    def are_board_coordnates_valid(self, coordinates_to_check):
        x_coordinate, y_coordinate = self._extract_x_and_y_coordinates(coordinates_to_check)
        if x_coordinate in range(3) and y_coordinate in range(3):
            return True
        else:
            return False

    def is_horizontal_match_found(self, coordinates_to_check, player_symbol):
        x_coordinate = self._extract_x_or_y_coordinate(coordinates_to_check, 'x')

        for y_coordinate_index in range(len(self._board)):
            if isinstance(self._board[x_coordinate][y_coordinate_index], Player) and \
                    self._board[x_coordinate][y_coordinate_index]._symbol == player_symbol:
                continue
            else:
                return False
        return True

    def is_vertical_match_found(self, coordinates_to_check, player_symbol):
        y_coordinate = self._extract_x_or_y_coordinate(coordinates_to_check, 'y')

        for x_coordinate_index in range(len(self._board)):
            if isinstance(self._board[x_coordinate_index][y_coordinate], Player) and \
                    self._board[x_coordinate_index][y_coordinate]._symbol == player_symbol:
                continue
            else:
                return False
        return True

    def is_diagonal1_match_found(self, player_symbol):

        for xy_coordinate in range(len(self._board)):
            if (isinstance(self._board[xy_coordinate][xy_coordinate], Player) and \
                    self._board[xy_coordinate][xy_coordinate]._symbol == player_symbol):
                continue
            else:
                return False
        return True

    def is_diagonal2_match_found(self, player_symbol):

        for xy_coordinate in range(len(self._board)):
            if (isinstance(self._board[(3 - 1) - xy_coordinate][0 + xy_coordinate], Player) and \
                    self._board[(3 - 1) - xy_coordinate][0 + xy_coordinate]._symbol == player_symbol):
                continue
            else:
                return False
        return True