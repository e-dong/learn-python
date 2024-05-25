"""Prompt
In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board.
Write a function that takes a dictionary argument and returns True or False depending on if the board is valid.

A valid board will have exactly one black king and exactly one white king. Each player can only have at most 16 pieces, at most 8 pawns, and
all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'. The piece names begin with either a 'w' or 'b'
to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.
This function should detect when a bug has resulted in an improper chess board.
"""

from typing import Dict

def is_chess_board_valid(board_state: Dict) -> bool:
    num_w_pieces = 0
    num_w_pawns = 0
    num_w_kings = 0

    num_b_pieces = 0
    num_b_pawns = 0
    num_b_kings = 0

    VALID_COLS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    VALID_ROWS = range(1, 9) # 1 - 8

    result = True
    for space, piece in board_state.items():
        space = space.lower()
        piece = piece.lower()


        if int(space[0]) not in VALID_ROWS:
            result = False
            break
        if space[1] not in VALID_COLS:
            result = False
            break

        piece_team = piece[0]
        piece_name = piece[1:len(piece)]

        if piece_team == 'w':
            num_w_pieces += 1

            if piece_name == 'king':
                num_w_kings += 1
                if num_w_kings > 1:
                    result = False
                    break
            elif piece_name == 'pawn':
                num_w_pawns += 1
                if num_w_pawns > 8:
                    result = False
                    break
        elif piece_team == 'b':
            num_b_pieces += 1

            if piece_name == 'king':
                num_b_kings += 1
                if num_b_kings > 1:
                    result = False
                    break
            elif piece_name == 'pawn':
                num_b_pawns += 1
                if num_b_pawns > 8:
                    result = False
                    break

    print(f"num white pieces: {num_w_pieces}")
    print(f"num white pawns:  {num_w_pawns}")
    print(f"num white kings:  {num_w_kings}")

    print(f"num black pieces: {num_b_pieces}")
    print(f"num black pawns:  {num_b_pawns}")
    print(f"num black kings:  {num_b_kings}")
    return result

board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '1b': 'bpawn' }

result = is_chess_board_valid(board)
print(result)
