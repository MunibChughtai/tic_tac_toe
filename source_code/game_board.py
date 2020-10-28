from player import Player


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
                 (board_position.get_player_symbol() if isinstance(board_position, Player) else board_position)
                 for board_position in board_row
                 ]
                            ))

    def display_board_message(self):
        print("here's the current board:")

    def _is_any_move_left(self):
        return self._moves_left

    # this cannot be tested,, only visual testing possible
    def assign_player_move_on_board(self, player):
        x_position, y_position = player.get_player_position()
        self._board[x_position - 1][y_position - 1] = player
        self._moves_left -= 1

    def _extract_x_and_y_coordinates(self, coordinates_to_check):
        x_position = int(coordinates_to_check[:coordinates_to_check.find(',')])
        y_position = int(coordinates_to_check[coordinates_to_check.find(',') + 1:])
        return (x_position - 1, y_position - 1)

    def _extract_x_or_y_coordinate(self, coordinates_to_check, coordinate_to_extract):
        x_position, y_position = self._extract_x_and_y_coordinates(coordinates_to_check)
        if coordinate_to_extract=='x':
            return x_position
        elif coordinate_to_extract=='y':
            return y_position

    def is_board_position_vacant(self, coordinates_to_check):
        x_position, y_position = self._extract_x_and_y_coordinates(coordinates_to_check)
        return True if self._board[x_position][y_position] == '.' else False

    def are_board_coordnates_valid(self, coordinates_to_check):
        x_position, y_position = self._extract_x_and_y_coordinates(coordinates_to_check)
        return True if x_position in range(3) and y_position in range(3) else False

    def is_horizontal_match_found(self, coordinates_to_check, player_symbol):
        x_position = self._extract_x_or_y_coordinate(coordinates_to_check, 'x')

        for y_position_index in range(len(self._board)):
            if isinstance(self._board[x_position][y_position_index], Player) and \
                    self._board[x_position][y_position_index]._symbol == player_symbol:
                continue
            else:
                return False
        return True

    def is_vertical_match_found(self, coordinates_to_check, player_symbol):
        y_position = self._extract_x_or_y_coordinate(coordinates_to_check, 'y')

        for x_position_index in range(len(self._board)):
            if isinstance(self._board[x_position_index][y_position], Player) and \
                    self._board[x_position_index][y_position]._symbol == player_symbol:
                continue
            else:
                return False
        return True

    def is_diagonal1_match_found(self, player_symbol):

        for xy_position in range(len(self._board)):
            if (isinstance(self._board[xy_position][xy_position], Player) and \
                    self._board[xy_position][xy_position]._symbol == player_symbol):
                continue
            else:
                return False
        return True

    def is_diagonal2_match_found(self, player_symbol):

        for xy_position in range(len(self._board)):
            if (isinstance(self._board[(3 - 1) - xy_position][0 + xy_position], Player) and \
                    self._board[(3 - 1) - xy_position][0 + xy_position]._symbol == player_symbol):
                continue
            else:
                return False
        return True