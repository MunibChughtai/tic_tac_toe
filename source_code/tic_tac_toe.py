from game_board import Game_Board
from player import Player  # only added for time being, may be removed later
import re

class Tic_Tac_Toe:

    def __init__(self):
        self._game_board = Game_Board()
        self._player_turn_controller=-1

    def _get_player_turn(self):
        self._player_turn_controller += 1
        if self._player_turn_controller%2==0:
            return ('Player 1', 'X')
        else:
            return ('Player 2', 'O')

    def _is_input_pattern_matched(self, coordinates):
        pattern_matched = re.match('^[0-9]+\s*,\s*[0-9]+$|q', coordinates)
        if pattern_matched:
            return True
        else:
            return False

    def _get_user_input(self):
        player_number, player_symbol = self._get_player_turn()
        while True:
            coordinates=input(f'{player_number} enter a coord x,y to place your {player_symbol} or enter ''q'' to give up: ').strip()
            if not self._is_input_pattern_matched(coordinates):
                print('Oh no, Invalid input format. Try again...')
                continue
            if (coordinates.lower()).strip()== 'q':
                print(f'{player_number} gave up, try again and you may win next time')
                return ('q', player_number, player_symbol)
            if not self._game_board.are_board_coordnates_valid(coordinates):
                print(f'Oh no, input coordinates are outside the board! Try again...')
                continue
            if not self._game_board.are_board_coordinates_vacant(coordinates):
                print(f'Oh no, a piece is already at this place! Try again...')
                continue
            break
        return (coordinates, player_number, player_symbol)

    def is_game_drawn(self):
        if not self._game_board._is_any_move_left():
            print(f'Good Try, Game drawn this time, you may win next time')
            return True
        return False

    def is_game_won(self, coordinates_to_check, player_symbol):
        game_won=False
        if self._game_board.is_horizontal_match_found(coordinates_to_check, player_symbol):
            game_won = True
        if self._game_board.is_vertical_match_found(coordinates_to_check, player_symbol):
            game_won = True
        if self._game_board.is_diagonal1_match_found(player_symbol):
            game_won = True
        if self._game_board.is_diagonal2_match_found(player_symbol):
            game_won = True
        if game_won:
            print("well done you've won the game!")
            return True
        return False

    def start_game(self):
        while True:
            self._game_board.display_board_message()
            self._game_board.display_board()
            coordinates, player_number, player_symbol = self._get_user_input()
            if (coordinates.lower()).strip()=='q':
                break
            print('Move accepted, ', end =' ')
            x_coordinate, y_coordinate = self._game_board._extract_x_and_y_coordinates(coordinates)
            self._game_board.assign_player_move_on_board(Player(player_symbol,x_coordinate+1, y_coordinate+1))
            if self.is_game_drawn() or self.is_game_won(coordinates, player_symbol):
                self._game_board.display_board()
                break