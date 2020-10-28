from game_board import Game_Board

from player import Player  # only added for time being, may be removed later

class Tic_Tac_Toe:
    player_1_symbol = 'X'
    player_2_symbol = 'O'
    give_up_message = 'You have given up, You should NEVER give up'
    piece_already_at_coordinate_message= 'Oh no, a piece is already at this place! Try again...'
    invalid_board_coordinates_message = 'Oh no, invalid board coordinates are entered! Try again...'
    move_accepted_message = 'Move accepted, '
    def __init__(self):
        _game_board = Game_Board()

    def start_game(self):
        #b = Game_Board()

        while True:
            give_up=return_value_player1=self.get_input_from_player(player_number=1, symbol=Tic_Tac_Toe.player_1_symbol)
            if give_up=='q':
                break
            else:
                give_up=return_value_player2=self.get_input_from_player(player_number=2, symbol=Tic_Tac_Toe.player_2_symbol)

        #p1=Player('X',2,2)
        #b.assign_player_move_on_board(p1)
        #b.display_board()

    def get_input_from_player(self, player_number, player_symbol):
        #user_input_valid=False

        while True: #not user_input_valid:
            input_coord=input(f'Player {player_number} enter a coord x,y to place your {player_symbol} or enter ''q'' to give up :').strip()
            if input_coord=='q':
                print(Tic_Tac_Toe.give_up_message)
                return 'q'

            if self.is_valid_user_input(input_coord):
                self.process_player_input(input_coord, player_symbol)
                print(Tic_Tac_Toe.move_accepted_message)
                self._game_board.display_board()
                break

    def process_player_input(self, input_coord, player_symbol):
        xposition, yposition = self._game_board._extract_x_and_y_coordinates(input_coord)
        self._game_board.assign_player_move_on_board(Player(player_symbol, xposition, yposition))


    def is_valid_user_input(self, input_coord):
        if not self._game_board.is_board_position_vacant(input_coord):
            print(Tic_Tac_Toe.piece_already_at_coordinate_message)
            return False

        if not self._game_board.are_board_coordnates_valid(input_coord):
            print(Tic_Tac_Toe.invalid_board_coordinates_message)
            return False
        return True

    #is_a_valid_board_move()


        #==============================
        #ask_player_to_make_move(X)
        #verify_move_for_correctness
        #  give Up
        #  draw
        #  win
        # display game board
        # ==============================

g=Tic_Tac_Toe()
g.start_game()