#from tic_tac_toe.source_code.player import Player
#from tic_tac_toe.source_code.game_board import Game_Board



from ..source_code.game_board import Game_Board
from ..source_code.player import Player

import pytest

def test_player_symbol():
    p1=Player('X',2,2)
    assert p1.get_player_symbol()=='X'

def test_player_position():
    p1 = Player('X', 2, 2)
    assert p1.get_player_position() == (2,2)

@pytest.mark.parametrize('input, expected',
                         [
                           ('2,3', False),
                           ('2,2', True)
                          ]
                         )
def test_board_for_vacant_positions(input, expected):
    b = Game_Board()
    p1 = Player('X', 2, 3)
    b.assign_player_move_on_board(p1)
    assert b.is_board_position_vacant(input) == expected

@pytest.mark.parametrize('input, expected',
                         [
                           ('1,3', True),
                           ('2,1', True),
                           ('3,2', True),
                           ('4,2', False),
                           ('2,4', False)
                          ]
                         )
def test_board_for_valid_coordinates(input, expected):
    b = Game_Board()
    assert b.are_board_coordnates_valid(input) == expected

# need to retest this when all logic implementation is complete
def test_any_move_left():
    b = Game_Board()
    b._moves_left=1
    p1 = Player('X', 2, 3)
    b.assign_player_move_on_board(p1)
    b.display_board()
    assert b._is_any_move_left()==0

def test1_horizontal_match_found():
    b = Game_Board()
    p1 = Player('X', 2, 1)
    b.assign_player_move_on_board(p1)
    p2 = Player('X', 2, 2)
    b.assign_player_move_on_board(p2)
    p3 = Player('X', 2, 3)
    b.assign_player_move_on_board(p3)
    assert b.is_horizontal_match_found('2, 3', 'X') == True

def test2_horizontal_match_found():
    b = Game_Board()
    p1 = Player('X', 2, 1)
    b.assign_player_move_on_board(p1)
    p2 = Player('X', 1, 2)
    b.assign_player_move_on_board(p2)
    p3 = Player('X', 2, 3)
    b.assign_player_move_on_board(p3)
    assert b.is_horizontal_match_found('2, 3', 'X') == False

def test3_horizontal_match_found():
    b = Game_Board()
    p1 = Player('X', 3, 1)
    b.assign_player_move_on_board(p1)
    p2 = Player('X', 3, 2)
    b.assign_player_move_on_board(p2)
    p3 = Player('X', 3, 3)
    b.assign_player_move_on_board(p3)
    assert b.is_horizontal_match_found('3, 3', 'X') == True

def test4_horizontal_match_found():
    b = Game_Board()
    p1 = Player('X', 3, 1)
    b.assign_player_move_on_board(p1)
    p2 = Player('Y', 3, 2)
    b.assign_player_move_on_board(p2)
    p3 = Player('X', 3, 3)
    b.assign_player_move_on_board(p3)
    assert b.is_horizontal_match_found('3, 3', 'X') == False

def test5_horizontal_match_found():
    b = Game_Board()
    p1 = Player('X', 3, 1)
    b.assign_player_move_on_board(p1)
    p2 = Player('X', 3, 2)
    b.assign_player_move_on_board(p2)
    assert b.is_horizontal_match_found('3, 1', 'X') == False


def test1_vertical_match_found():
    b = Game_Board()
    p1 = Player('X', 1, 1)
    b.assign_player_move_on_board(p1)
    p2 = Player('X', 2, 1)
    b.assign_player_move_on_board(p2)
    p3 = Player('X', 3, 1)
    b.assign_player_move_on_board(p3)
    assert b.is_vertical_match_found('2, 1', 'X') == True

def test2_vertical_match_found():
    b = Game_Board()
    p1 = Player('X', 1, 2)
    b.assign_player_move_on_board(p1)
    p2 = Player('X', 2, 1)
    b.assign_player_move_on_board(p2)
    p3 = Player('X', 3, 2)
    b.assign_player_move_on_board(p3)
    assert b.is_vertical_match_found('3, 2', 'X') == False

def test3_vertical_match_found():
    b = Game_Board()
    p1 = Player('X', 1, 3)
    b.assign_player_move_on_board(p1)
    p2 = Player('X', 2, 3)
    b.assign_player_move_on_board(p2)
    p3 = Player('X', 3, 3)
    b.assign_player_move_on_board(p3)
    assert b.is_vertical_match_found('3, 3', 'X') == True

def test4_vertical_match_found():
    b = Game_Board()
    p1 = Player('X', 1, 3)
    b.assign_player_move_on_board(p1)
    p2 = Player('Y', 2, 3)
    b.assign_player_move_on_board(p2)
    p3 = Player('X', 3, 3)
    b.assign_player_move_on_board(p3)
    assert b.is_vertical_match_found('3, 3', 'X') == False

def test5_vertical_match_found():
    b = Game_Board()
    p1 = Player('X', 1, 3)
    b.assign_player_move_on_board(p1)
    p2 = Player('X', 2, 3)
    b.assign_player_move_on_board(p2)
    assert b.is_vertical_match_found('1, 3', 'X') == False

def test1_diagonal1_match_found():
    b = Game_Board()
    p1 = Player('X', 1, 1)
    b.assign_player_move_on_board(p1)
    p2 = Player('X', 2, 2)
    b.assign_player_move_on_board(p2)
    p3 = Player('X', 3, 3)
    b.assign_player_move_on_board(p3)
    assert b.is_diagonal1_match_found('X') == True

def test2_diagonal1_match_found():
    b = Game_Board()
    p1 = Player('X', 1, 1)
    b.assign_player_move_on_board(p1)
    p2 = Player('X', 2, 2)
    b.assign_player_move_on_board(p2)
    p3 = Player('Y', 3, 3)
    b.assign_player_move_on_board(p3)
    assert b.is_diagonal1_match_found('X') == False

def test1_diagonal2_match_found():
    b = Game_Board()
    p1 = Player('X', 3, 1)
    b.assign_player_move_on_board(p1)
    p2 = Player('X', 2, 2)
    b.assign_player_move_on_board(p2)
    p3 = Player('X', 1, 3)
    b.assign_player_move_on_board(p3)
    assert b.is_diagonal2_match_found('X') == True

def test2_diagonal2_match_found():
    b = Game_Board()
    p1 = Player('Y', 3, 1)
    b.assign_player_move_on_board(p1)
    p2 = Player('X', 2, 2)
    b.assign_player_move_on_board(p2)
    p3 = Player('X', 1, 3)
    b.assign_player_move_on_board(p3)
    assert b.is_diagonal2_match_found('X') == False