


def is_winning_board(board):
    return is_horizontal_winner(board) or is_vertical_winner(board)


def is_horizontal_winner(board):
    # iterate each row
    # for each row, the length of set should be 1
    # if found return true
    # if we reach the end return false
    for row in board:
        unique_characters =  len(set(row))
        if unique_characters == 1 and set(row) != {""}:
            return True
    return False

def is_vertical_winner(board):
    for column in range(3):
        unique_character_set={row[column] for row in board}
        if len(unique_character_set) ==1 and unique_character_set!= {""}:
            return True
    return False

