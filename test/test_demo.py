import pytest
from source_code.demo import is_winning_board
def test_is_horizontal_winning_board():
    board = [
        ["X", "X", "X"],
        ["", "O", ""],
        ["", "", "O"],
    ]
    assert is_winning_board(board)

def test_is_vertical_winning_board():
    board = [
        ["X", "O", "X"],
        ["X", "O", ""],
        ["X", "", "O"],
    ]
    assert is_winning_board(board)

def test_is_right_diagonal_winning_board():
    board = [
        ["O", "X", "X"],
        ["", "O", ""],
        ["", "", "O"],
    ]
    assert is_winning_board(board)

def test_is_left_diagonal_winning_board():
    board = [
        ["X", "X", "O"],
        ["", "O", ""],
        ["O", "", "O"],
    ]
    assert is_winning_board(board)

def test_is_not_winning_board():
    board = [
        ["X", "O", "X"],
        ["", "O", ""],
        ["", "", "O"],
    ]
    assert is_winning_board(board) == False

def test_empty_board():
    board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ]
    assert is_winning_board(board)==False

