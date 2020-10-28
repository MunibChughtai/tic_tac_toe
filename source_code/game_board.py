# from tic_tac_toe.source_code.player import Player

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
            # res2 = '  '.join([(board_position.get_player_symbol() if isinstance(board_position, Player) else board_position) for board_position in board_row])
            print('  '.join(
                [(board_position.get_player_symbol() if isinstance(board_position, Player) else board_position) for
                 board_position in board_row]))

    def display_board_message(self):
        print("here's the current board:")

    def _is_any_move_left(self):
        return self._moves_left

    # this cannot be tested,, only visual testing possible
    def assign_player_move_on_board(self, player):
        xposition, yposition = player.get_player_position()
        self._board[xposition - 1][yposition - 1] = player
        self._moves_left -= 1

    def _extract_x_and_y_coordinates(self, coordinates_to_check):
        xposition = int(coordinates_to_check[:coordinates_to_check.find(',')])
        yposition = int(coordinates_to_check[coordinates_to_check.find(',') + 1:])
        return (xposition - 1, yposition - 1)

    def is_board_position_vacant(self, coordinates_to_check):
        xposition, yposition = self._extract_x_and_y_coordinates(coordinates_to_check)
        return True if self._board[xposition][yposition] == '.' else False

    def are_board_coordnates_valid(self, coordinates_to_check):
        xposition, yposition = self._extract_x_and_y_coordinates(coordinates_to_check)
        return True if xposition in range(3) and yposition in range(3) else False

    # def is_a_valid_board_move(self, coordinates_to_check):
    #    return True if self.is_board_position_vacant(coordinates_to_check) and self.are_board_coordnates_valid(coordinates_to_check) else False

    def is_horizontal_match_found(self, coordinates_to_check, player_symbol):
        xposition, yposition = self._extract_x_and_y_coordinates(coordinates_to_check)
        return all([1 if (isinstance(self._board[xposition][yposition_index], Player) and (
                    self._board[xposition][yposition_index]._symbol == player_symbol)) else 0 for yposition_index in
                    range(len(self._board))])

    def is_vertical_match_found(self, coordinates_to_check, player_symbol):
        xposition, yposition = self._extract_x_and_y_coordinates(coordinates_to_check)
        return all([1 if (isinstance(self._board[xposition_index][yposition], Player) and (
                    self._board[xposition_index][yposition]._symbol == player_symbol)) else 0 for xposition_index in
                    range(len(self._board))])

    def is_diagonal1_match_found(self, player_symbol):
        return all([1 if (isinstance(self._board[xy_position][xy_position], Player) and self._board[xy_position][
            xy_position]._symbol == player_symbol) else 0 for xy_position in range(3)])

    def is_diagonal2_match_found(self, player_symbol):
        return all([1 if (isinstance(self._board[(3 - 1) - xy_position][0 + xy_position], Player) and
                          self._board[(3 - 1) - xy_position][0 + xy_position]._symbol == player_symbol) else 0 for
                    xy_position in range(3)])

    '''
    p1=Player('X',2,2)
    b = Game_Board()
    b.assign_player_move_on_board(p1)
    b.display_board()
    print(b.is_board_position_vacant('2,2'))
    '''
